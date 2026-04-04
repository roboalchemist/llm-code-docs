# Source: https://docs.getdbt.com/docs/dbt-versions/core.md

# About dbt Core versions

Learn about versioning for the dbt Core engine (Python-based CLI). If you run the dbt Core engine locally (for example, using `pip`), then this page is for you. dbt Core releases follow [semantic versioning](https://semver.org/).

If you're using dbt platform (including the dbt CLI, you don't need to manage dbt versions yourself. [Release tracks](https://docs.getdbt.com/docs/dbt-versions/cloud-release-tracks.md) automatically keep you up to date and provide early access to new features before they’re available in dbt Core.

note

If you want to use the dbt Fusion engine, locally or in dbt platform, then read [Get Started](https://docs.getdbt.com/docs/local/install-dbt.md?version=2).

If you manage your own dbt Core versions locally, read on. dbt Core releases follow [semantic versioning](https://semver.org/).

* **[Active](https://docs.getdbt.com/docs/dbt-versions/core.md#current-version-support)**: In the first few months after a minor version's initial release, we patch it with bugfix releases. These include fixes for regressions, new bugs, and older bugs / quality-of-life improvements. We implement these changes when we have high confidence that they're narrowly scoped and won't cause unintended side effects.
* **[Critical](https://docs.getdbt.com/docs/dbt-versions/core.md#current-version-support)**: When a newer minor version ships, the previous one transitions to "Critical Support" for the remainder of its one-year window. Patches during this period are limited to critical security and installation fixes. After the one-year window ends, the version reaches end of life.
* **[End of Life](https://docs.getdbt.com/docs/dbt-versions/core.md#end-of-life-versions)**: Minor versions that have reached EOL no longer receive new patch releases.
* **Deprecated**: dbt Core versions that are no longer maintained by dbt Labs, nor supported in the dbt platform.

### Latest releases[​](#latest-releases "Direct link to Latest releases")

| dbt Core                                                                                                 | Initial release | Support level and end date          |
| -------------------------------------------------------------------------------------------------------- | --------------- | ----------------------------------- |
| [**v1.11**](https://docs.getdbt.com/docs/dbt-versions/core-upgrade/upgrading-to-v1.11.md)                | Dec 19, 2025    | **Active Support — Dec 18, 2026**   |
| [**v1.10**](https://docs.getdbt.com/docs/dbt-versions/core-upgrade/upgrading-to-v1.10.md)                | Jun 16, 2025    | **Critical Support — Jun 15, 2026** |
| [**v1.9**](https://docs.getdbt.com/docs/dbt-versions/core-upgrade/upgrading-to-v1.9.md)                  | Dec 9, 2024     | Deprecated ⛔️                      |
| [**v1.8**](https://docs.getdbt.com/docs/dbt-versions/core-upgrade/upgrading-to-v1.8.md)                  | May 9, 2024     | Deprecated ⛔️                      |
| [**v1.7**](https://docs.getdbt.com/docs/dbt-versions/core-upgrade/upgrading-to-v1.7.md)                  | Nov 2, 2023     | End of Life ⚠️                      |
| [**v1.6**](<https://docs.getdbt.com/docs/dbt-versions/core-upgrade/Older versions/upgrading-to-v1.6.md>) | Jul 31, 2023    | End of Life ⚠️                      |
| [**v1.5**](<https://docs.getdbt.com/docs/dbt-versions/core-upgrade/Older versions/upgrading-to-v1.5.md>) | Apr 27, 2023    | End of Life ⚠️                      |
| [**v1.4**](<https://docs.getdbt.com/docs/dbt-versions/core-upgrade/Older versions/upgrading-to-v1.4.md>) | Jan 25, 2023    | End of Life ⚠️                      |
| [**v1.3**](<https://docs.getdbt.com/docs/dbt-versions/core-upgrade/Older versions/upgrading-to-v1.3.md>) | Oct 12, 2022    | End of Life ⚠️                      |
| [**v1.2**](<https://docs.getdbt.com/docs/dbt-versions/core-upgrade/Older versions/upgrading-to-v1.2.md>) | Jul 26, 2022    | Deprecated ⛔️                      |
| [**v1.1**](<https://docs.getdbt.com/docs/dbt-versions/core-upgrade/Older versions/upgrading-to-v1.1.md>) | Apr 28, 2022    | Deprecated ⛔️                      |
| [**v1.0**](<https://docs.getdbt.com/docs/dbt-versions/core-upgrade/Older versions/upgrading-to-v1.0.md>) | Dec 3, 2021     | Deprecated ⛔️                      |
| **v0.X** ⛔️                                                                                             | (Various dates) | Deprecated ⛔️                      |

Search table...

|                  |   |   |   |   |
| ---------------- | - | - | - | - |
| Loading table... |   |   |   |   |

All functionality in dbt Core since the v1.7 release is available in [dbt release tracks](https://docs.getdbt.com/docs/dbt-versions/cloud-release-tracks.md), which provide automated upgrades at a cadence appropriate for your team.

1 Release tracks are required for the Developer and Starter plans on dbt. Accounts using older dbt versions will be migrated to the **Latest** release track.

For customers of dbt: dbt Labs strongly recommends migrating environments on older and unsupported versions to [release tracks](https://docs.getdbt.com/docs/dbt-versions/cloud-release-tracks.md) or a supported version. In 2025, dbt Labs will remove the oldest dbt Core versions from availability in dbt platform, starting with v1.0 -- v1.2.

### Further reading[​](#further-reading "Direct link to Further reading")

* [Choosing a dbt Core version in dbt](https://docs.getdbt.com/docs/dbt-versions/upgrade-dbt-version-in-cloud.md): Learn how you can use dbt Core versions in dbt.
* [How to install dbt Core](https://docs.getdbt.com/docs/local/install-dbt.md): Learn about installing dbt Core.
* [`require-dbt-version`](https://docs.getdbt.com/reference/project-configs/require-dbt-version.md) and [`dbt_version`](https://docs.getdbt.com/reference/dbt-jinja-functions/dbt_version.md): Restrict your project to only work with a range of dbt Core versions, or use the currently running version.

## End-of-life versions[​](#end-of-life-versions "Direct link to End-of-life versions")

Once a dbt Core version reaches end-of-life (EOL), it no longer receives patches, including for known bugs. We recommend upgrading to a newer version in [dbt](https://docs.getdbt.com/docs/dbt-versions/upgrade-dbt-version-in-cloud.md) or [dbt Core](https://docs.getdbt.com/docs/local/install-dbt.md#upgrading-dbt-core). All versions prior to v1.0 have been deprecated.

## Current version support[​](#current-version-support "Direct link to Current version support")

dbt supports each minor version (for example, v1.8) for *one year* from its initial release. During that window, we release patches with bug fixes and security updates. When we refer to a minor version, we mean its latest available patch (v1.8.x).

After a newer minor version ships, the previous one transitions to **critical support** (security and installation fixes only) for the remainder of its one-year window. After the one-year window ends, the version reaches **end of life** and no longer receives patches.

While a minor version is officially supported:

* You can use it in dbt. For more on dbt versioning, see [Choosing a dbt version](https://docs.getdbt.com/docs/dbt-versions/upgrade-dbt-version-in-cloud.md).
* You can select it from the version dropdown on this website, to see documentation that is accurate for use with that minor version.

For upcoming releases, refer to the [`dbt-core` milestones](https://github.com/dbt-labs/dbt-core/milestones).

## Upgrading[​](#upgrading "Direct link to Upgrading")

Upgrade to new patch versions as soon as they're available. Upgrade to new minor versions when you're ready because you can only get some features and fixes on the latest minor version.

dbt makes all versions available as prereleases before the final release. For minor versions, we aim to release one or more betas 4+ weeks before the final release so you can try new features and share feedback. Release candidates are available about two weeks before the final release for testing in production-like environments. Refer to the [`dbt-core` milestones](https://github.com/dbt-labs/dbt-core/milestones) for details.

## How dbt Core uses semantic versioning[​](#how-dbt-core-uses-semantic-versioning "Direct link to How dbt Core uses semantic versioning")

dbt Core follows [semantic versioning](https://semver.org/):

* **Major versions** (for example, v1 to v2) may include breaking changes. Deprecated functionality will stop working.
* **Minor versions** (for example, v1.8 to v1.9) add features and are backwards compatible. They will not break project code that relies on documented functionality.
* **Patch versions** (for example, v1.8.0 to v1.8.1) include fixes only: bug fixes, security fixes, or installation fixes.

We are committed to avoiding breaking changes in minor versions for end users of dbt. There are two types of breaking changes that may be included in minor versions:

* Changes to the Python interface for adapter plugins. These changes are relevant only to adapter maintainers, and they will be clearly communicated in documentation and release notes. For more information, refer to [Build, test, document, and promote adapters guide](https://docs.getdbt.com/guides/adapter-creation.md).

* Changes to metadata interfaces, including [artifacts](https://docs.getdbt.com/docs/deploy/artifacts.md) and [logging](https://docs.getdbt.com/reference/events-logging.md), signalled by a version bump. Those version upgrades may require you to update external code that depends on these interfaces, or to coordinate upgrades between dbt orchestrations that share metadata, such as [state-powered selection](https://docs.getdbt.com/reference/node-selection/syntax.md#about-node-selection).

### Adapter plugin versions[​](#adapter-plugin-versions "Direct link to Adapter plugin versions")

dbt releases `dbt-core` and adapter plugins (such as `dbt-snowflake`) independently. Their minor and patch version numbers may not match, but they coordinate through the `dbt-adapters` interface so you won't get a broken experience. For example, `dbt-core==1.8.0` can work with `dbt-snowflake==1.9.0`.

If you're building or maintaining an adapter, refer to the [adapter creation guide](https://docs.getdbt.com/guides/adapter-creation.md) for details on the `dbt-adapters` interface.

Run `dbt --version` to check your installed versions:

```text
$ dbt --version
Core:
  - installed: 1.8.0
  - latest:    1.8.0 - Up to date!

Plugins:
  - snowflake: 1.9.0 - Up to date!
```

You can also find the registered adapter version in [logs](https://docs.getdbt.com/reference/global-configs/logs.md). For example, in `logs/dbt.log`:

```text
[0m13:13:48.572182 [info ] [MainThread]: Registered adapter: snowflake=1.9.0
```

Refer to [Supported data platforms](https://docs.getdbt.com/docs/supported-data-platforms.md) for the full list of adapters.

## Was this page helpful?

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
