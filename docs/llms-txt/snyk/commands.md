# Source: https://docs.snyk.io/developer-tools/snyk-cli/commands.md

# CLI help

Snyk CLI scans and monitors your projects for security vulnerabilities and license issues.

For more information, visit the [Snyk website](https://snyk.io)

For details, see the [CLI documentation](https://docs.snyk.io/snyk-cli)

## How to get started

1. Authenticate by running `snyk auth`.
2. Test your local project with `snyk test`.
3. Get alerted for new vulnerabilities with `snyk monitor`.

## Available commands

To learn more about each Snyk CLI command, use the `--help` option, for example, `snyk auth --help`.

**Note:** The help on the docs site is the same as the `--help` in the CLI.

### [`snyk auth`](https://docs.snyk.io/developer-tools/snyk-cli/commands/auth)

Authenticate Snyk CLI with a Snyk account.

### [`snyk test`](https://docs.snyk.io/developer-tools/snyk-cli/commands/test)

Test a project for open-source vulnerabilities and license issues.

**Note**: Use `snyk test --unmanaged` to scan all files for known open-source dependencies (C/C++ only).

### [`snyk monitor`](https://docs.snyk.io/developer-tools/snyk-cli/commands/monitor)

Snapshot and continuously monitor a project for open-source vulnerabilities and license issues.

### [`snyk container`](https://docs.snyk.io/developer-tools/snyk-cli/commands/container)

These commands test and continuously monitor container images for vulnerabilities and generate an SBOM for a container image.

### [`snyk iac`](https://docs.snyk.io/developer-tools/snyk-cli/commands/iac)

These commands find and report security issues in Infrastructure as Code files; detect, track, and alert on unmanaged resources; and create a .driftignore file.

### [`snyk code`](https://docs.snyk.io/developer-tools/snyk-cli/commands/code)

The `snyk code test` command finds security issues using Static Code Analysis.

### [`snyk sbom`](https://docs.snyk.io/developer-tools/snyk-cli/commands/sbom)

Generate or test an SBOM document in ecosystems supported by Snyk.

### [`snyk aibom`](https://docs.snyk.io/developer-tools/snyk-cli/commands/aibom)

Generates an AIBOM for a local software project that is written in Python, to understand what AI models, datasets, tools, and so on are used in that project.

### [`snyk redteam`](https://docs.snyk.io/developer-tools/snyk-cli/commands/redteam)

Runs a red teaming scan against AI targets and reports vulnerabilities.

### [`snyk log4shell`](https://docs.snyk.io/developer-tools/snyk-cli/commands/log4shell)

Find Log4Shell vulnerability.

### [`snyk config`](https://docs.snyk.io/developer-tools/snyk-cli/commands/config)

Manage Snyk CLI configuration.

### [`snyk policy`](https://docs.snyk.io/developer-tools/snyk-cli/commands/policy)

Display the `.snyk` policy for a package.

### [`snyk ignore`](https://docs.snyk.io/developer-tools/snyk-cli/commands/ignore)

Modify the `.snyk` policy to ignore stated issues.

## Debug

Use `-d` option to output the debug logs.

## Configure the Snyk CLI

You can use environment variables to configure the Snyk CLI and also set variables to configure the Snyk CLI to connect with the Snyk API. See [Configure the Snyk CLI](https://docs.snyk.io/snyk-cli/configure-the-snyk-cli)
