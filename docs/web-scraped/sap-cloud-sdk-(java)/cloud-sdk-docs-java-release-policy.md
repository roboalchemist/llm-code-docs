# Source: https://sap.github.io/cloud-sdk/docs/java/release-policy

Title: Minor and Major Release Policy for the SAP Cloud SDK for Java | SAP Cloud SDK

URL Source: https://sap.github.io/cloud-sdk/docs/java/release-policy

Markdown Content:
Planned Major Releases[​](https://sap.github.io/cloud-sdk/docs/java/release-policy#planned-major-releases "Direct link to Planned Major Releases")
--------------------------------------------------------------------------------------------------------------------------------------------------

| Version | Status | Release Date | End of Life | Upgrade guide |
| --- | --- | --- | --- | --- |
| 1.x | Deprecated | 2017, Sept | 2018, May | N/A |
| 2.x | Deprecated | 2018, May | 2020, February | N/A |
| 3.x | Deprecated | 2019, August | 2023, March | [Link](https://developers.sap.com/tutorials/s4sdk-migration-v3.html) |
| 4.x | Deprecated | 2022, October | 2024, May 31 | [Link](https://sap.github.io/cloud-sdk/docs/java/v4/guides/4.0-upgrade) |
| 5.x | Released GA | 2023, December |  | [Link](https://sap.github.io/cloud-sdk/docs/java/guides/5.0-upgrade-steps) |

Minor and Major Release Policy[​](https://sap.github.io/cloud-sdk/docs/java/release-policy#minor-and-major-release-policy "Direct link to Minor and Major Release Policy")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We follow [Semantic Versioning](https://semver.org/) for our releases.

### Minor Release Schedule[​](https://sap.github.io/cloud-sdk/docs/java/release-policy#minor-release-schedule "Direct link to Minor Release Schedule")

Our regular **minor version** release happens every **two weeks**. It includes new functionality, fixes, and maintenance updates that we communicate in the [release notes](https://sap.github.io/cloud-sdk/docs/java/release-notes).

We sometimes change our release frequency to:

*   Provide a patch version to the latest minor release when a critical bug fix is necessary.
*   Accommodate a longer development cycle. We can extend an interval between **minor version** releases.

Upgrading between minor releases

Usually, an upgrade between minor releases does not involve any effort. All the changes are incremental and backward compatible. We do not remove any deprecated code before the next major release.

### Major Release Schedule[​](https://sap.github.io/cloud-sdk/docs/java/release-policy#major-release-schedule "Direct link to Major Release Schedule")

We intend to release a new **major version** every **12 months** to introduce significant feature upgrades, refactor existing features, and clean up deprecated code.

*   **Major version** release intervals are indicative and may change.
*   After release of a new major version, the preceding version will be moved into maintenance mode before being marked as deprecated. In maintenance mode, the version will still receive vulnerability fixes and major bug fixes. The duration for which we grant support highly depends customer demand.
*   We will announce planned date and scope of the next **major version** release in this [document](https://sap.github.io/cloud-sdk/docs/java/release-policy#planned-major-release-schedule) and [release notes](https://sap.github.io/cloud-sdk/docs/java/release-notes) at least 3 months before the planned release date.

Upgrading between major versions

Major releases include incompatible API changes. An upgrade will usually involve a certain effort to make your code benefit from new APIs. We intend to minimize this effort between adjacent major versions.

*   We provide a step-by-step upgrade guide for each major version.
*   Following the upgrade steps should take less than a day of development effort regardless of the project size.

### Documentation[​](https://sap.github.io/cloud-sdk/docs/java/release-policy#documentation "Direct link to Documentation")

The documentation is always up to date with the **latest major release**. We provide documentation for the two most recent major versions at the same time. Use the versioning toggle in the top right corner to switch between versions of the documentation.

### Maintenance and Support[​](https://sap.github.io/cloud-sdk/docs/java/release-policy#maintenance-and-support "Direct link to Maintenance and Support")

*   We provide new features and fixes **only** for the **latest major release** of the SAP Cloud SDK for Java.
*   We continue to [support](https://sap.github.io/cloud-sdk/docs/overview/get-support) customers using any version of the SAP Cloud SDK for Java. In case the identified solution resides in upgrading to the newer version of the SAP Cloud SDK - it will be the default recommended solution.

Upgrade regularly

We recommend upgrading to the latest major version immediately or at least not later than within 3 months after its release. This guarantees:

*   easy upgrade path
*   compatibility to the latest features of SAP Business Technology Platform
*   protection of your development process from disruptions in the future. Upgrading gets more complex if you have to migrate between more than one major version.

Support and Feedback[​](https://sap.github.io/cloud-sdk/docs/java/release-policy#support-and-feedback "Direct link to Support and Feedback")
--------------------------------------------------------------------------------------------------------------------------------------------

Let us know if you have any questions about our release policy. We usually respond within one day. Check our [support channels](https://sap.github.io/cloud-sdk/docs/overview/get-support) and choose the one working best for you.
