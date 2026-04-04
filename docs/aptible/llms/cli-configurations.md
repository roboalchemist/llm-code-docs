# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-configurations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# CLI Configurations

> The Aptible CLI provides configuration options such as MFA support, customizing output format, and overriding configuration location.

## MFA support

To use hardware-based MFA (e.g., Yubikey) on Windows and Linux, manually install the libfido2 command line tools. You can find the latest installation release and installation instructions [here](https://developers.yubico.com/libfido2/).

For OSX users, installation via Homebrew will automatically include the libfido2 dependency.

## Output Format

The Aptible CLI supports two output formats: plain text and JSON. You can select your preferred output format by setting the `APTIBLE_OUTPUT_FORMAT` environment variable to `text` or `json`.

If the `APTIBLE_OUTPUT_FORMAT` variable is left unset (i.e., the default), the CLI will provide output as plain text.

> 📘 The Aptible CLI sends logging output to `stderr`, and everything else to `stdout` (this is the standard behavior for well-behaved UNIX programs).

> If you're calling the Aptible CLI from another program, make sure you don't merge the two streams (if you did, you'd have to filter out the logging output).

> Note that if you're simply using a shell such as Bash, the pipe operator (i.e. `|`) only pipes `stdout` through, which is exactly what you want here.

## Configuration location

The Aptible CLI normally stores its configuration (your Aptible authentication token and automatically generated SSH keys) in a hidden subfolder of your home directory: `~/.aptible`. To override this default location, you can specify a custom path by using the environment variable `APTIBLE_CONFIG_PATH`. Since the files in this path grant access to your Aptible account, protect them as if they were your password itself!
