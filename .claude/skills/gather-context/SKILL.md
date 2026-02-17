---
name: gather-context
description: Search GitHub issues and PRs for discussion related to the current task. Use when starting work on a topic to find relevant project history.
argument-hint: "[search terms | github-url] [--limit N]"
context: fork
---

You are a research agent. Search this project's GitHub issues and PR discussions for context relevant to the current task. Fetch generously — read everything that might be relevant — but return only a curated summary.

## Parse arguments

Parse $ARGUMENTS for:
- An optional `--limit N` flag (default: 5) controlling how many search results to fetch
- A GitHub issue/PR URL (e.g. `https://github.com/myyoda/principles-paper/issues/36`)
- Or plain search terms

Examples:
- `STAMPED --limit 3` → terms="STAMPED", limit=3
- `STAMPED` → terms="STAMPED", limit=5
- `https://github.com/myyoda/principles-paper/issues/36` → seed from that issue
- `--limit 10` → no explicit terms (infer them), limit=10

## Determine search terms

**If a GitHub URL was provided:**
1. Fetch the issue/PR with comments: `gh issue view <number> --comments` or `gh pr view <number> --comments`
2. Extract linked issues/PRs from the body and comments (look for `#N` references, URLs)
3. Fetch each linked issue/PR
4. Derive search terms from titles, labels, and key discussion topics
5. Continue to the search process below using those terms

**If search terms were provided**, use those directly.

**If neither**, infer search terms from:
1. The current git branch name (split on `/` and `-`)
2. Recent commit messages on this branch (`git log main..HEAD --oneline`)

## Search process

1. Search open AND closed issues (discussion often lives in closed issues):
   ```
   gh search issues "<terms>" --repo myyoda/principles-paper --limit <limit>
   ```

2. Search PRs:
   ```
   gh search prs "<terms>" --repo myyoda/principles-paper --limit <limit>
   ```

3. For each result that looks relevant, fetch the full discussion:
   ```
   gh issue view <number> --comments
   gh pr view <number> --comments
   ```

4. For PRs with review comments, also fetch inline review comments:
   ```
   .claude/scripts/gh-pr-comments myyoda/principles-paper <number>
   ```

5. If you discover additional linked issues/PRs in the discussion that seem relevant, follow those too.

## Output

Return a curated summary — not a transcript. The user's main conversation should not be bloated.

Structure:
- **Issues/PRs found**: table with number, title, status, and one-line relevance note. Under each entry, include a bulleted list of relevant comments (author + key point) and any linked URLs/references.
- **Key discussion themes**: the 3-5 most important points across all discussions
- **Open questions**: unresolved disagreements or decisions still pending
- **Recommendations**: if any issues/PRs are especially relevant to the current branch/task, call them out

Be opinionated about what matters. Skip noise, housekeeping comments, and resolved tangents.

## Save to file

After composing the summary, write it to `local-notes/` (which is gitignored).

**Filename**: derive from the seed input:
- GitHub URL → `context-issue-36.md` or `context-pr-39.md`
- Search terms → slugify the terms, e.g. `context-stamped-actionable.md`
- No explicit seed → `context-branch-<branchname>.md`

Write the full markdown summary to that file using the Write tool. Then return the summary as usual so the main conversation also sees it.
