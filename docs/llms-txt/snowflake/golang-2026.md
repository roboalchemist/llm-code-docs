# Source: https://docs.snowflake.com/en/release-notes/clients-drivers/golang-2026.md

# Go Snowflake Driver release notes for 2026

This article contains the release notes for the Go Snowflake Driver, including the following when applicable:

* Behavior changes
* New features
* Customer-facing bug fixes

Snowflake uses semantic versioning for Go Snowflake Driver updates.

See [Go Snowflake Driver](../../developer-guide/golang/go-driver.md) for documentation.

## Version 2.0.0 (Mar 03, 2026)

### BCR (Behavior Change Release) changes

* Removed `RaisePutGetError` from `SnowflakeFileTransferOptions` to ensure errors are raised for PUT/GET operations.
* Removed `GetFileToStream` from `SnowflakeFileTransferOptions`. Use `WithFileGetStream` to automatically enable file streaming for GET operations.
* Removed `WithOriginalTimestamp`. Use `WithArrowBatchesTimestampOption(UseOriginalTimestamp)` instead.
* Removed the `ClientIP` field from the `Config` struct. This field was never used and is not needed for any functionality.
* Removed the `InsecureMode` field from `Config` struct. Use `DisableOCSPChecks` instead.
* Removed the `DisableTelemetry` field from the `Config` struct. Use the `CLIENT_TELEMETRY_ENABLED` session parameter instead.
* Removed the stream chunk downloader. Use the default downloader instead.
* Removed `SnowflakeTransport`. Use `Config.Transporter`, or simply register your own TLS configuration with `RegisterTLSConfig` if you just need a custom root certificates set.
* Renamed `WithFileStream` to `WithFilePutStream` for consistency.
* Renamed the `KeepSessionAlive` field in the `Config` struct to `ServerSessionKeepAlive` for consistency with other drivers.
* The `Array` function now returns an error for unsupported types.
* `WithMultiStatement` no longer returns an error.
* Combined `WithMapValuesNullable` and `WithArrayValuesNullable` into the single `WithEmbeddedValuesNullable` option.
* Hid the streaming chunk downloader. It will be removed completely in a future release.
* The maximum number of chunk download goroutines is now configured with the `CLIENT_PREFETCH_THREADS` session parameter.
* Fixed a typo in the `GOSNOWFLAKE_SKIP_REGISTRATION` environment variable.
* Unexported `MfaToken` and `IdToken`.
* Arrow batches changes:

  * Arrow batches have been extracted to a separate package, which should significantly reduce the compilation size for those who don’t need arrow batches (~34MB -> ~18MB).
  * Removed `GetArrowBatches` from `SnowflakeRows` and `SnowflakeResult`. Use `arrowbatches.GetArrowBatches(rows.(SnowflakeRows))` instead.
  * Migrated the following functions:

    * `sf.WithArrowBatchesTimestampOption` to `arrowbatches.WithTimestampOption`
    * `sf.WithArrowBatchesUtf8Validation` to `arrowbatches.WithUtf8Validation`
    * `sf.ArrowSnowflakeTimestampToTime` to `arrowbatches.ArrowSnowflakeTimestampToTime`
* Logging changes:

  * Removed the Logrus logger and migrated to slog.
  * Simplified the `SFLogger` interface.
  * Added the `SFSlogLogger` interface for setting a custom slog handler.

### New features and updates

* Added support for Go 1.26, and dropped support for Go 1.23.
* Added support for FIPS-only mode.

### Bug fixes

* Added a panic recovery block for stage file upload and download operations.
* Fixed a WIF metadata request from an Azure container that manifested as an HTTP 400 error.
* Fixed a SAML authentication port validation bypass in `isPrefixEqual` where the second URL’s port was never checked.
* Fixed a race condition in the OCSP cache clearer.
* The `context.Context` query is now propagated to cloud storage operations for PUT and GET queries, allowing for better cancellation handling.
* Fixed minicore crashes (SIGFPE) on fully statically linked Linux binaries by detecting static linking via ELF PT_INTERP inspection and skipping `dlopen` gracefully.

## Version 1.19.0 (Feb 03, 2026)

### New features and updates

* Exposed `tokenFilePath` in the `Config` struct, in addition to the existing DSN option.
* `tokenFilePath` is now read for every new connection, not only once at driver startup.
* Added support for identity impersonation when using workload identity federation.
* Added the ability to disable minicore from loading at compile time using the `-tags minicore_disabled` parameter.

### Bug fixes

* Fixed an issue with getting files from an unencrypted stage.
* Fixed the minicore file name gathering in client environment.
* Fixed path escaping for GCS URLs that manifested in 403 responses from GCS when a file or directory contained spaces.
* Fixed leaking file descriptors when uploading files to stages (especially in GCS).
