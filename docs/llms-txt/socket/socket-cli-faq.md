# Source: https://docs.socket.dev/docs/socket-cli-faq.md

# Socket CLI FAQ

# Does this run locally on my computer?

The CLI itself runs locally, but certain commands need to communicate with our public API, for example by uploading your dependency manifest files to Socket for analysis or asking about the repositories you've defined.

* Socket is designed to work without the need to analyze, upload, or share your source code.
* The only data we collect from your repository are manifest and associated lock files. For example, for npm we'd collect `package.json` / `package-lock.json`, for python `requirements.txt` /`requirements.lock.txt`, or Ruby `Gemfile`/`Gemfile.lock`. This is what we call the dependency snapshot. We do this for every ecosystems we support.
* We use the dependency snapshot to determine the list of packages used by your repository, perform our open source risk analysis, and produce a report.

# Can I look at reports locally on the computer?

Yes! If you have a Scan ID you can use `socket scan view` or `socket scan report` to view details on them. You can export them raw with the `--json` flag or get nice shareable output with the `--markdown` flag.

# Why does my scan not show up in the alerts dashboard?

Most likely you need to set the `--pending-head` flag. Without that option new scans will not show up.

It should still show up in the "Full Scans" page, regardless.

# Why is there a Scan URL without results?

When using `socket report create` the files are uploaded and a Scan ID is created and returned to you right away.

The actual report is generated lazily when you go to view it.

When you specify the `--report` flag, the CLI does this fetch for you and will trigger the generation, then reads the results to report the outcome to you.