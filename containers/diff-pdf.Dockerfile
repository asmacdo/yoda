FROM debian:trixie-slim

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      diff-pdf-wx \
      xvfb \
      xauth \
      poppler-utils \
      imagemagick \
      curl \
      ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# diff-pdf needs a display; wrap it so callers don't have to remember xvfb-run
COPY diff-pdf-wrapper.sh /usr/local/bin/diff-pdf
RUN chmod +x /usr/local/bin/diff-pdf

WORKDIR /work
