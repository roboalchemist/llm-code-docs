# Source: https://headscale.net/stable/ref/configuration/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiIC8+PC9zdmc+)](https://github.com/juanfont/headscale/blob/main/docs/ref/configuration.md "Edit this page") [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE3IDE4Yy41NiAwIDEgLjQ0IDEgMXMtLjQ0IDEtMSAxLTEtLjQ0LTEtMSAuNDQtMSAxLTFtMC0zYy0yLjczIDAtNS4wNiAxLjY2LTYgNCAuOTQgMi4zNCAzLjI3IDQgNiA0czUuMDYtMS42NiA2LTRjLS45NC0yLjM0LTMuMjctNC02LTRtMCA2LjVhMi41IDIuNSAwIDAgMS0yLjUtMi41IDIuNSAyLjUgMCAwIDEgMi41LTIuNSAyLjUgMi41IDAgMCAxIDIuNSAyLjUgMi41IDIuNSAwIDAgMS0yLjUgMi41TTkuMjcgMjBINlY0aDd2NWg1djQuMDdjLjcuMDggMS4zNi4yNSAyIC40OVY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNC41YTguMiA4LjIgMCAwIDEtMS4yMy0yIiAvPjwvc3ZnPg==)](https://github.com/juanfont/headscale/raw/main/docs/ref/configuration.md "View source of this page")

# Configuration[¶](#configuration "Permanent link")

- Headscale loads its configuration from a YAML file
- It searches for `config.yaml` in the following paths:
  - `/etc/headscale`
  - `$HOME/.headscale`
  - the current working directory
- To load the configuration from a different path, use:
  - the command line flag `-c`, `--config`
  - the environment variable `HEADSCALE_CONFIG`
- Validate the configuration file with: `headscale configtest`

Get the [example configuration from the GitHub repository](https://github.com/juanfont/headscale/blob/main/config-example.yaml)

Always select the [same GitHub tag](https://github.com/juanfont/headscale/tags) as the released version you use to ensure you have the correct example configuration. The `main` branch might contain unreleased changes.

View on GitHubDownload with `wget`Download with `curl`

- Development version: <https://github.com/juanfont/headscale/blob/main/config-example.yaml>
- Version 0.27.1: <https://github.com/juanfont/headscale/blob/v0.27.1/config-example.yaml>

    # Development version
    wget -O config.yaml https://raw.githubusercontent.com/juanfont/headscale/main/config-example.yaml

    # Version 0.27.1
    wget -O config.yaml https://raw.githubusercontent.com/juanfont/headscale/v0.27.1/config-example.yaml

    # Development version
    curl -o config.yaml https://raw.githubusercontent.com/juanfont/headscale/main/config-example.yaml

    # Version 0.27.1
    curl -o config.yaml https://raw.githubusercontent.com/juanfont/headscale/v0.27.1/config-example.yaml