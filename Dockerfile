FROM your-base-image:latest

# Install ShellCheck
RUN apt-get update && apt-get install -y shellcheck

# Set the SHELLCHECK_PATH environment variable
ENV SHELLCHECK_PATH=/usr/local/bin/shellcheck
