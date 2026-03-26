# Source: https://docs.socket.dev/docs/quality.md

# Quality

| Severity | Alert Type                                                             | Description                                                                                                                                                                    |
| :------- | :--------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Medium   | [Wildcard dependency](https://socket.dev/alerts/floatingDependency)    | Package has a dependency with a floating version range. This can cause issues if the dependency publishes a new major version.                                                 |
| Medium   | [Unpopular package](https://socket.dev/alerts/unpopularPackage)        | This package is not very popular.                                                                                                                                              |
| Low      | [Bad dependency semver](https://socket.dev/alerts/badSemverDependency) | Package has dependencies with an invalid semantic version. This could be a sign of beta, low quality, or unmaintained dependencies.                                            |
| Low      | [Minified code](https://socket.dev/alerts/minifiedFile)                | This package contains minified code. This may be harmless in some cases where minified code is included in packaged libraries, however packages on npm should not minify code. |