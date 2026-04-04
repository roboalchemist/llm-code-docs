# Source: https://kreya.app/docs/cli/global-options.md

# Global options - Kreya CLI

Global options can be applied to every `kreyac` command. The Kreya [configuration](/docs/configuration.md) also applies to `kreyac`.

## Options[​](#options "Direct link to Options")

### verbose[​](#verbose "Direct link to verbose")

`-v`, `--verbose`<br /><!-- -->Can also be set via the environment variable `KREYA_VERBOSE`<br /><!-- -->Default: `false`

Show verbose output

### project[​](#project "Direct link to project")

`-p`, `--project`<br /><!-- -->Can also be set via the environment variable `KREYA_PROJECT`<br /><!-- -->Default: `.`

The Kreya project to work on

### disable-telemetry[​](#disable-telemetry "Direct link to disable-telemetry")

`--disable-telemetry`<br /><!-- -->Can also be set via the environment variable `KREYA_DISABLETELEMETRY`<br /><!-- -->Default: `false`

Disable telemetry

## Flags files / response files[​](#flags-files--response-files "Direct link to Flags files / response files")

Response files allow you to specify command-line arguments in a file instead of passing them directly in the terminal. This can be useful for commands with many options or for reusing configurations.

To use a response file with `kreyac`, create a file containing the desired options and prefix the file path with `@` when running the command. For example:

```
kreyac @options.txt
```

Contents of `options.txt`:

```
operation invoke
grpc/**
!grpc/not-tested
rest/**
!rest/not-tested
```
