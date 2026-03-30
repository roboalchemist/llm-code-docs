# Source: https://docs.snowflake.com/en/release-notes/clients-drivers/php-pdo-2026.md

# PHP PDO Driver for Snowflake release notes for 2026

This article contains the release notes for the PHP PDO Driver for Snowflake, including the following when applicable:

* Behavior changes
* New features
* Customer-facing bug fixes

Snowflake uses semantic versioning for PHP PDO Driver for Snowflake updates.

See [PHP PDO Driver for Snowflake](../../developer-guide/php-pdo/php-pdo-driver.md) for documentation.

## Version 3.6.0 (Mar 05, 2026)

### New features and updates

* Implemented richer `client_environment` telemetry information to include on which environment the driver runs (such as Lambda, EC2, GCP, Azure VM, and so on) and whether the managed identity is enabled.
* Added support for workload identity federation authentication, including the following new connection parameters:

  * `workload_identity_provider` - Platform of the workload identity provider. Possible values include: AWS, AZURE, GCP, and OIDC.
  * `workload_identity_azure_resource` - If the AZURE `workload_identity_provider` is used, this parameter sets the resource that the driver should use to idenitify itself.
  * `workload_identity_impersonation_path` - An array of strings that provides an identity chain to use when connecting to Snowflake. Array elements are either a full service account address or a service account’s unique ID.

    Impersonation works by following each array entry to obtain a token that allows authorization of the next service account. Each account in the identity chain needs permissions to impersonate the next account only. The final account in the list obtains your Snowflake connection token and uses it to connect to Snowflake.

    This parameter is supported for AWS and Google Cloud workloads and only applies when `authenticator=WORKLOAD_IDENTITY`.
* Updated OpenSSL to 3.0.19.
* Added support for multistatement queries.

### Bug fixes

* None.

## Version 3.5.0 (Feb 03, 2026)

### New features and updates

* Added support for Red Hat Enterprise Linux (RHEL) 9.
* Deprecated CentOS 7 builds. Rocky 8/RHEL8 is now the minimum system version.
* Added a warning for HTTP usage in OAuth authentication flows.
* Set `LOCAL_APPLICATION` as a default for the `client_id` and `client_secret` for the OAuth Authorization code flow.
* Updated Curl to 8.16.0.
* Removed the workload identity federation (WIF) auto-detection mechanism.
* Added auto-detection of the application path and included it in the `CLIENT_ENVIRONMENT` variable.
* Updated OpenSSL to 3.0.18

### Bug fixes

* Fixed the expired file lock on Linux for the Secure Storage.
* Removed the username requirement for the WIF authentication.
