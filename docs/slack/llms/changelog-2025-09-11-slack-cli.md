Source: https://docs.slack.dev/changelog/2025/09/11/slack-cli

# Release: Slack CLI v3.7.0

September 11, 2025

Version `3.7.0` of the developer tools for the Slack platform has arrived!

* The macOS & Linux installation scripts now install to the `$HOME/.local/bin` path if installing to the `/usr/local/bin` path causes an error. Additional `$PATH` setup may be required and is output as needed. The `$HOME/.local/bin` path adheres to the emerging [XDG specification](https://specifications.freedesktop.org/basedir-spec/latest/).
* We now parse the app manifest fields of `features.search` when gathering an app manifest.

**Tags:**

* [Release](/changelog/tags/release)
* [Slack CLI](/changelog/tags/slack-cli)
