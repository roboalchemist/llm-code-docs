# Source: https://tyk.io/docs/developer-support/release-notes/tib.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tyk Identity Broker Release Notes

> Release notes documenting updates, enhancements, and changes for Tyk Identity Broker versions within the 1.6.x series.

****Open Source** ([Mozilla Public License](https://github.com/TykTechnologies/tyk/blob/master/LICENSE.md))**

**This page contains all release notes for Tyk Identity Broker displayed in a reverse chronological order**

## Support Lifetime

Our minor releases are supported until our next minor comes out.

***

## 1.7 Release Notes

### 1.7.0 Release Notes

#### Release Date 28 March 2025

#### Release Highlights

This release introduces enhancements to TIB, improving group-based permission mapping, adding support for proxy settings from environment variables, and allowing dynamic state values in the OAuth2 flow.

For a comprehensive list of changes, please refer to the detailed [changelog](#Changelog-v1.7.0) below.

#### Breaking Changes

This release has no breaking changes.

#### Dependencies

##### 3rd Party Dependencies & Tools

| Third Party Dependency                                    | Tested Versions | Compatible Versions       | Comments                    |
| :-------------------------------------------------------- | :-------------- | :------------------------ | :-------------------------- |
| [GoLang](https://go.dev/dl/)                              | 1.21            | 1.21                      | All our binaries            |
| [MongoDB](https://www.mongodb.com/try/download/community) | 5.x, 6.x, 7.0   | 4.4.x, 5.x, 6.x and 7.0.x | Used by Tyk Identity Broker |
| [Redis](https://redis.io/download/)                       | 6.x - 7.0       | 6.x - 7.0                 | Used by Tyk Identity Broker |

Given the time difference between your upgrade and the release of this version, we recommend customers verify the ongoing support of third-party dependencies they install, as their status may have changed since the release.

#### Deprecations

There are no deprecations in this release.

#### Upgrade instructions

For users currently on v1.6.0, we strongly recommend promptly upgrading to the latest release. If you are working with an older version (lower major), it is advisable to bypass version 1.6.0 and proceed directly to this latest patch release.

<br />

Go to the [Upgrading Tyk](#upgrading-tyk) section for detailed upgrade Instructions.

#### Downloads

* [Docker image to pull](https://hub.docker.com/r/tykio/tyk-identity-broker/tags?name=1.7.0)

  ```
  docker pull tykio/tyk-identity-broker:v1.7.0
  ```

* source code tarball for oss projects - [TIB v1.7.0](https://github.com/TykTechnologies/tyk-identity-broker/releases/tag/v1.7.0)

#### Changelog

<a id="Changelog-v1.7.0" data-scroll-offset />

##### Added

<AccordionGroup>
  <Accordion title="Load Proxy Settings from Environment Variables">
    TIB now respects `HTTP_PROXY`, `HTTPS_PROXY`, and `NO_PROXY` environment variables when making outbound connections. This change ensures compatibility with air-gapped Kubernetes environments where external services can only be accessed via an HTTP proxy.
  </Accordion>

  <Accordion title="Dynamic State Query Support in OAuth2 Flow">
    The OAuth2 "state" field can now be dynamically set via the URL or form-encoded body. This improvement allows integration with external APIs that require custom state values, ensuring compliance with various regulatory and enterprise authentication requirements.
  </Accordion>

  <Accordion title="Improved Multi-Group Permission Mapping for Identity Providers">
    Previously, TIB assigned a user to the last matched group when multiple groups were mapped, regardless of the identity provider (SAML, LDAP, OAuth, OIDC, etc.). The new functionality introduces support for multi-group mapping, allowing permissions to be merged. This update is backward compatible and ensures that multi-group rights (combined permissions) are only applied if the user does not have a `groupId` assigned via the Dashboard.
  </Accordion>
</AccordionGroup>

##### Security Fixes

<Expandable title="Fixed the following CVE">
  * [GHSA-v778-237x](https://github.com/advisories/GHSA-v778-237x-gjrc)
</Expandable>

***

## 1.6 Release Notes

### 1.6.1 Release Notes

#### Release Date 5 Nov 2024

#### Release Highlights

###### Enhanced Security with JWE Support for OIDC SSO

This release introduces JSON Web Encryption (JWE) support for OpenID Connect (OIDC) Single Sign-On (SSO) in the Tyk Identity Broker (TIB). With this enhancement, organizations can achieve greater security for token handling during authentication flows. JWE token validation and processing are now seamlessly integrated, offering configurable private key support for decryption.

#### Breaking Changes

This release has no breaking changes.

{/*##### Changed error log messages
  Important for users who monitor Tyk components using the application logs (i.e. Tyk Gateway log, Tyk Dashboard log, etc.).
  We try to avoid making changes to our log messages, especially at error and critical levels. However, sometimes it's necessary. Please find the list of changes made to the application log in this release:*/}

{/*##### Planned Breaking Changes*/}

#### Dependencies

##### 3rd Party Dependencies & Tools

| Third Party Dependency                                    | Tested Versions | Compatible Versions       | Comments                    |
| :-------------------------------------------------------- | :-------------- | :------------------------ | :-------------------------- |
| [GoLang](https://go.dev/dl/)                              | 1.21            | 1.21                      | All our binaries            |
| [MongoDB](https://www.mongodb.com/try/download/community) | 5.x, 6.x, 7.0   | 4.4.x, 5.x, 6.x and 7.0.x | Used by Tyk Identity Broker |
| [Redis](https://redis.io/download/)                       | 6.x - 7.0       | 6.x - 7.0                 | Used by Tyk Identity Broker |

Given the time difference between your upgrade and the release of this version, we recommend customers verify the ongoing support of third-party dependencies they install, as their status may have changed since the release.

#### Deprecations

There are no deprecations in this release.

{/*###### Future deprecations*/}

#### Upgrade instructions

For users currently on v1.6.0, we strongly recommend promptly upgrading to the latest release. If you are working with an older version (lower major), it is advisable to bypass version 1.6.0 and proceed directly to this latest patch release.

<br />

Go to the [Upgrading Tyk](#upgrading-tyk) section for detailed upgrade Instructions.

#### Downloads

* [Docker image to pull](https://hub.docker.com/r/tykio/tyk-identity-broker/tags?name=1.6.1)

  ```
  docker pull tykio/tyk-identity-broker:v1.6.1
  ```

* source code tarball for oss projects - [TIB v1.6.1](https://github.com/TykTechnologies/tyk-identity-broker/releases/tag/v1.6.1)

#### Changelog

##### Added

<Expandable title="Support for JSON Web Encryption (JWE) in OIDC SSO with TIB">
  This release adds support for JSON Web Encryption (JWE) in OIDC Single Sign-On (SSO) with TIB, providing enhanced security for token handling in authentication flows. This feature enables processing and validation of JWE tokens, with configuration options for setting the private key required for decryption.

  For more details, refer to the [OIDC SSO with JWE](/api-management/external-service-integration#social-profile-fields) documentation.
</Expandable>

***

{/*The footer of the release notes page. It contains a further information section with details of how to upgrade Tyk,
  links to API documentation and FAQs. You can copy it from the previous release.*/}

## Further Information

### Upgrading Tyk

Please refer to the [upgrading Tyk](/developer-support/upgrading) page for further guidance on the upgrade strategy.

### FAQ

Please visit our [Developer Support](/developer-support/community) page for further information relating to reporting bugs, upgrading Tyk, technical support and how to contribute.

Built with [Mintlify](https://mintlify.com).
