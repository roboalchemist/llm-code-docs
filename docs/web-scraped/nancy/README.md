# Source: https://github.com/sonatype-nexus-community/nancy

# Nancy - Go Dependency Vulnerability Scanner

`nancy` is a tool to check for vulnerabilities in your Golang dependencies, powered by [Sonatype OSS Index](https://ossindex.sonatype.org/), and as well, works with Nexus IQ Server, allowing you a smooth experience as a Golang developer, using the best tools in the market!

## Installation

### From Source

```sh
go install github.com/sonatype-nexus-community/nancy@latest
```

### Binary Releases

Download pre-built binaries from the [releases page](https://github.com/sonatype-nexus-community/nancy/releases).

### Homebrew (macOS)

```sh
brew tap sonatype-nexus-community/nancy
brew install nancy
```

### AUR (Arch Linux)

```sh
yay -S nancy-bin
```

or

```sh
pacman -S nancy
```

## Usage

Nancy currently works for projects that use `dep` or `go mod` for dependencies.

### Basic Command Help

```
nancy is a tool to check for vulnerabilities in your Golang dependencies,
powered by the 'Sonatype OSS Index', and as well, works with Nexus IQ Server, allowing you
a smooth experience as a Golang developer, using the best tools in the market!

Usage:
  nancy [flags]
  nancy [command]

Examples:
  Typical usage will pipe the output of 'go list -json -deps' to 'nancy':
  go list -json -deps ./... | nancy sleuth [flags]
  go list -json -deps ./... | nancy iq [flags]

  If using dep typical usage is as follows :
  nancy sleuth -p Gopkg.lock [flags]
  nancy iq -p Gopkg.lock [flags]

Available Commands:
  config      Setup credentials to use when connecting to services
  help        Help about any command
  iq          Check for vulnerabilities in your Golang dependencies using 'Sonatype's Nexus IQ IQServer'
  sleuth      Check for vulnerabilities in your Golang dependencies using Sonatype's OSS Index
  update      Check if there are any updates available

Flags:
  -v, --count                   Set log level, multiple v's is more verbose
  -c, --clean-cache             Deletes local cache directory
  -d, --db-cache-path string    Specify an alternate path for caching responses from OSS Index, example: /tmp
  -h, --help                    help for nancy
      --loud                    indicate output should include non-vulnerable packages
  -p, --path string             Specify a path to a dep Gopkg.lock file for scanning
  -q, --quiet                   indicate output should contain only packages with vulnerabilities (default true)
      --skip-update-check       Skip the check for updates.
  -t, --token string            Specify OSS Index API token for request
  -u, --username string         Specify OSS Index username for request
  -V, --version                 Get the version
```

### Sleuth Command

The `sleuth` command checks for vulnerabilities using Sonatype's OSS Index.

```
'nancy sleuth' is a command to check for vulnerabilities in your Golang dependencies, powered by the 'Sonatype OSS Index'.

Usage:
  nancy sleuth [flags]

Examples:
  go list -json -deps ./... | nancy sleuth --username your_user --token your_token
  nancy sleuth -p Gopkg.lock --username your_user --token your_token

Flags:
  -a, --additional-exclude-vulnerability-files strings   Path to additional files containing newline separated CVEs or OSS Index IDs to be excluded
  -e, --exclude-vulnerability CveListFlag                Comma separated list of CVEs or OSS Index IDs to exclude (default [])
  -x, --exclude-vulnerability-file string                Path to a file containing newline separated CVEs or OSS Index IDs to be excluded (default "./.nancy-ignore")
  -h, --help                                             help for sleuth
  -n, --no-color                                         indicate output should not be colorized
  -o, --output string                                    Styling for output format. json, json-pretty, text, csv (default "text")

Global Flags:
  -v, --count                   Set log level, multiple v's is more verbose
  -d, --db-cache-path string    Specify an alternate path for caching responses from OSS Index, example: /tmp
      --loud                    indicate output should include non-vulnerable packages
  -p, --path string             Specify a path to a dep Gopkg.lock file for scanning
```

### IQ Command

The `iq` command checks for vulnerabilities using Sonatype's Nexus IQ Server.

```
'nancy iq' is a command to check for vulnerabilities in your Golang dependencies, powered by Sonatype's Nexus IQ Server.

Usage:
  nancy iq [flags]

Examples:
  go list -json -deps ./... | nancy iq --user your_user --token your_token
  nancy iq -p Gopkg.lock --user your_user --token your_token

Flags:
  -a, --additional-exclude-vulnerability-files strings   Path to additional files containing newline separated CVEs or OSS Index IDs to be excluded
  -e, --exclude-vulnerability CveListFlag                Comma separated list of CVEs or OSS Index IDs to exclude (default [])
  -x, --exclude-vulnerability-file string                Path to a file containing newline separated CVEs or OSS Index IDs to be excluded (default "./.nancy-ignore")
  -h, --help                                             help for iq
  -n, --no-color                                         indicate output should not be colorized
  -o, --output string                                    Styling for output format. json, json-pretty, text, csv (default "text")
  --server-url string                                    Specify the server url for iq server (default "http://localhost:8070")
  --user string                                          Specify the user for iq server
  --token string                                         Specify the token/password for iq server
  -p, --path string                                      Specify a path to a dep Gopkg.lock file for scanning

Global Flags:
  -v, --count                   Set log level, multiple v's is more verbose
```

### Config Command

The `config` command helps you setup credentials for connecting to services.

## Usage Examples

### Scanning go.mod with OSS Index

```sh
go list -json -deps ./... | nancy sleuth
```

With authentication:

```sh
go list -json -deps ./... | nancy sleuth --username your_user --token your_token
```

### Scanning Gopkg.lock with OSS Index

```sh
nancy sleuth -p Gopkg.lock
```

With authentication:

```sh
nancy sleuth -p Gopkg.lock --username your_user --token your_token
```

### Scanning with Nexus IQ Server

```sh
go list -json -deps ./... | nancy iq --server-url http://your-iq-server:8070 --user your_user --token your_token
```

## Output Formats

Nancy supports multiple output formats:

- **text** (default): Human-readable output
- **json**: Machine-readable JSON format
- **json-pretty**: Pretty-printed JSON
- **csv**: Comma-separated values for spreadsheet import

Example with JSON output:

```sh
go list -json -deps ./... | nancy sleuth -o json
```

## Vulnerability Exclusion

### Using .nancy-ignore File

Create a `.nancy-ignore` file in your project root with CVE or OSS Index IDs to exclude:

```
CVE-2021-12345
sonatype-2021-1234
```

Nancy automatically looks for `.nancy-ignore` in the current directory.

### Command Line Exclusion

Exclude specific vulnerabilities via CLI:

```sh
nancy sleuth -e CVE-2021-12345,sonatype-2021-1234
```

### Additional Exclusion Files

Specify additional exclusion files:

```sh
nancy sleuth -a /path/to/exclude1.txt -a /path/to/exclude2.txt
```

## Environment Variables

- `NANCY_OSSI_USERNAME` - OSS Index username
- `NANCY_OSSI_TOKEN` - OSS Index API token
- `NANCY_IQ_SERVER` - Nexus IQ Server URL
- `NANCY_IQ_USER` - Nexus IQ Server username
- `NANCY_IQ_TOKEN` - Nexus IQ Server token

## CI/CD Integration

### GitHub Actions

```yaml
- name: Nancy Vulnerability Check
  uses: sonatype-nexus-community/nancy-github-action@main
  with:
    args: -o json
```

### Jenkins

```groovy
stage('Vulnerability Check') {
  steps {
    sh 'go list -json -deps ./... | nancy sleuth'
  }
}
```

### GitLab CI

```yaml
security_scan:
  image: golang:latest
  script:
    - go install github.com/sonatype-nexus-community/nancy@latest
    - go list -json -deps ./... | nancy sleuth
```

## Caching

Nancy caches responses from OSS Index to improve performance on subsequent runs. The cache is stored locally by default. You can:

- Clean the cache: `nancy --clean-cache`
- Specify alternate cache path: `nancy --db-cache-path /tmp`

## Verbose Logging

Enable verbose output for debugging:

```sh
nancy sleuth -vvv
```

Multiple `-v` flags increase verbosity level.

## Troubleshooting

### Authentication Issues

If you encounter authentication errors with OSS Index:

1. Verify your username and token credentials
2. Use environment variables: `NANCY_OSSI_USERNAME` and `NANCY_OSSI_TOKEN`
3. Try without credentials (limited requests per day without auth)

### Performance

For large projects:

1. Use caching (enabled by default)
2. Consider running in CI/CD with dedicated infrastructure
3. Batch multiple scans if possible

### API Rate Limiting

OSS Index applies rate limits. Authenticated requests have higher limits:

```sh
nancy sleuth --username user --token token
```

## Security Policy

For reporting security vulnerabilities, please email [security@sonatype.com](mailto:security@sonatype.com).

First check [Important advisories of known security vulnerabilities in Sonatype products](https://support.sonatype.com/hc/en-us/sections/203012668-Security-Advisories).

## License

Nancy is licensed under the Apache License 2.0.

## See Also

- [Sonatype OSS Index](https://ossindex.sonatype.org/) - Online vulnerability database
- [Nexus IQ Server](https://www.sonatype.com/products/quality-and-supply-chain-management) - Enterprise dependency management
- [Project Repository](https://github.com/sonatype-nexus-community/nancy)
