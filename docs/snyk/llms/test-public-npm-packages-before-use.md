# Source: https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/test-public-npm-packages-before-use.md

# Test public npm packages before use

You can use `snyk test` to **scrutinize a public package before installing it**, to see if it has known vulnerabilities or not. Use the package name to test the latest version of the package.

`snyk test ionic@1.6.5`

You can also provide a specific version or range using `snyk test module[@semver-range]`.

See also [Getting started with the CLI](https://docs.snyk.io/developer-tools/snyk-cli/getting-started-with-the-snyk-cli).
