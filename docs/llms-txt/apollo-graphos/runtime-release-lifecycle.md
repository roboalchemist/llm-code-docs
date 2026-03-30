# Source: https://www.apollographql.com/docs/graphos/resources/runtime-release-lifecycle.md

# GraphOS Runtime Release Lifecycle

This guide explains the lifecycle of GraphOS Router and Apollo Federation releases to help you understand support timelines and feature availability.

The current LTS policy version is v2026.1

## Release Lifecycle Stages

Each software release can go through various stages that indicate its state of development or support. These stages apply to both GraphOS Router and Apollo Federation versions. To learn more about the lifecycle of new features released across the GraphOS platform, see [Apollo Feature Launch Stages](https://www.apollographql.com/docs/graphos/reference/feature-launch-stages).

### Preview

Use preview releases to validate new versions and their upcoming changes before they become Active. Preview releases might include breaking changes, so testing them helps you prepare for migrations and identify any compatibility issues early. Provide feedback on the new release to help shape the final Active version. After the Developer Preview phase completes, the release moves to Active status.

### Active

From the time a release line is released for General Availability (GA) in the Active phase, it is actively developed. Active release lines regularly receive new features, bug fixes, and security patches. Patch updates are made to the latest minor version and are not applied to previous major or minor versions unless those versions are marked for LTS. Only one release line is Active at a time.

After a release line reaches Active status, Apollo avoids breaking changes to its functionality, APIs, or documented public interfaces. In rare circumstances, breaking changes might be required, for example to address a security vulnerability.

A non-GA feature (Experimental or Preview) might still include breaking changes within its associated functionality, as defined in [Apollo Feature Launch Stages](https://www.apollographql.com/docs/graphos/reference/feature-launch-stages).

### Long-Term Support (LTS)

After a period of development, an Active release transitions to Long-Term Support (LTS) status. Although an LTS version is no longer under active feature development, it continues to receive critical and high-priority bug fixes and security patches, as well as [support](https://www.apollographql.com/enterprise/support) through paid support plans. Apollo provides bug fixes and security patches on the latest minor release in each LTS line.

### End-of-Support (EOS)

After the LTS phase concludes, a release line transitions to End-of-Support status (EOS). After a release is EOS, Apollo stops providing patches, security updates, or support for the release. Do not use EOS releases in production.

## GraphOS Router

GraphOS Router uses [semantic versioning](https://semver.org/). Apollo releases a new major version yearly, though major versions may be released more frequently on an as-needed basis. Each line of a major release goes through the stages of the release lifecycle, starting from Preview and ending with End-of-Support.

A typical major version cycle consists of:

* 3 months for Preview
* 12 months for Active
* 9 months of LTS halfway through Active development
* 9 months of LTS at the conclusion of the Active phase

During the Active phase, Apollo releases feature/minor versions, planned on a monthly cadence, and patch updates as needed onto the latest minor release.

### Long-Term Support

Every six months, Apollo marks the current minor version of GraphOS Router as Long-Term Support (LTS). Because Apollo releases new major versions yearly, we designate LTS versions halfway through and at the end of a major's Active phase. For example, we try to release a new minor version monthly; following that schedule, it's likely the vX.6 and vX.12 versions are marked as the LTS versions. Keep in mind, though, that deviations from the schedule may occur.

Each LTS version is supported for nine months, with an overlap of three months where both versions are supported. This ensures there is at least one LTS version for a given major version line for 15 months.

This LTS policy starts in 2026 with the release of GraphOS Router v3. For the interim, GraphOS Router v2 continues to be supported with LTS versions that provide overlap with the new LTS policy (see dates in the following table).

### Premier Support extension of LTS

For Premier Support customers, Apollo provides extended support for an LTS release for a period of three months after the EOS date. This provides Premier Support customers with a 12-month LTS support period.

In this extension period, Apollo provides bug fixes and security patches for the LTS releases for customers with Premier Support plans. For all other customers, we mark the release line as End of Service (EOS). After the extension period, Apollo marks the release line as EOS for all customers, including Premier Support customers.

[Contact Apollo to discuss extending LTS support](https://www.apollographql.com/contact-sales?referrer=docs-contact-sales).

### Release Timeline

The following diagram shows the timelines with the lifecycle stages and how those result in Preview, Active, and LTS timeframes:

#### Standard Support

#### Premier Support

This timeline and exact dates and/or version numbers are subject to change for future LTS releases.

### Why Mid-Cycle LTS?

This policy balances long periods of support on a given major version with supporting those who prefer to stay closer to the latest features.

If you want long periods of consistent versions and only move as required to stay in support, each major version is released in Preview and then tested with production workloads for 6 months of Active development. During this period, you have time to plan for all backwards-incompatible changes in advance of upgrading to the new major version. Apollo then designates a mid-cycle LTS (vX.6), and you have a 3-month transition period to complete the migration to the new major version. You can continue to use the mid-cycle LTS (vX.6) for the support period. Then, the next LTS bump does not require a major version upgrade, only a minor bump (vX.12), which is supported for 9 months after its release (or 12 months if you are a Premier Support customer). This means you only have to plan a major version upgrade every 12-15 months.

If you prefer to stay closer to the latest developments and new features, you can stay on Active versions, which receive continuous upgrades and patches. If your organization has a code freeze, use the minor version within the major version you're actively using that receives Long-Term Support. This allows your team to apply any critical fixes as semver patches in your code freeze period. After your code freeze ends, you can upgrade to the latest Active minor version or look ahead to upcoming Preview releases.

### GraphOS Router release schedule

Dates and version numbers are subject to change for future releases. For support information on a specific release, see the [Router release notes](https://github.com/apollographql/router/releases).

| Version             | Release Type | Current Version | Federation Version | Preview Date | Active Date   | LTS Date      | EOS Date       | Premier Support EOS Date |
| ------------------- | ------------ | --------------- | ------------------ | ------------ | ------------- | ------------- | -------------- | ------------------------ |
| GraphOS Router 1.61 | LTS          | v1.61.12        | Federation v2.9    | -            | -             | February 2025 | March 2026     | No extension available   |
| GraphOS Router 2.x  | Active       | v2.10.0         | Federation v2.x    | July 2024    | February 2025 | -             | Q2 2026        | -                        |
| GraphOS Router 2.10 | LTS          | v2.10.0         | Federation v2.12   | -            | -             | December 2025 | September 2026 | No extension available   |
| GraphOS Router 2.16 | LTS          | -               | -                  | -            | -             | Q2 2026       | Q1 2027        | Q2 2027                  |
| GraphOS Router 3.x  | Active       | -               | -                  | Q1 2026      | Q2 2026       | -             | Q2 2027        | -                        |
| GraphOS Router 3.6  | LTS          | -               | -                  | -            | -             | Q4 2026       | Q3 2027        | Q4 2027                  |
| GraphOS Router 3.12 | LTS          | -               | -                  | -            | -             | Q2 2027       | Q1 2028        | Q2 2028                  |
| GraphOS Router 4.x  | Active       | -               | -                  | Q1 2027      | Q2 2027       | -             | Q2 2028        | -                        |

### Compatible operating systems and versions

GraphOS Router is compatible with the following operating systems and software versions (with noted clarifications). Apollo provides official router binaries on the [Releases](https://github.com/apollographql/router/releases) page. Router binaries might work on other operating systems and versions, but Apollo only targets the following set:

| Operating System      | Version          | Binaries Supported                                    | Notes                                            |
| --------------------- | ---------------- | ----------------------------------------------------- | ------------------------------------------------ |
| RHEL                  | 9.9              | `x86_64-unknown-linux-gnu``aarch64-unknown-linux-gnu` | When linked with `glibc`>=2.29                   |
| Ubuntu                | 20.04            | `x86_64-unknown-linux-gnu``aarch64-unknown-linux-gnu` | When linked with `glibc`>=2.29                   |
| Windows               | 10               | `x86_64-pc-windows-msvc`                              | Until Windows 10 end-of-life on October 14, 2025 |
| macOS (x86)           | 13.5.1 (Ventura) | `x86_64-apple-darwin`                                 | With Xcode 15.0.x                                |
| macOS (Apple Silicon) | 13.5.1 (Ventura) | `aarch64-apple-darwin`                                | With Xcode 15.0.x                                |

### Containers and custom builds of the router

Apollo provides officially supported pre-compiled router binaries on the [Releases page](https://github.com/apollographql/router/releases).

Apollo supports custom builds of the router (those not provided pre-compiled by Apollo) on a reasonable-effort basis. For support requests on custom builds, Apollo Technical Support might suggest you remove custom Rust code, build using [Rust v1.76.0](https://github.com/rust-lang/rust/releases/tag/1.76.0), and use a compatible operating system from the preceding list.

Apollo [provides official Docker containers](https://www.apollographql.com/docs/graphos/routing/self-hosted/containerization#about-router-container-images) with pre-compiled binary releases of the router. Although the pre-compiled router binary included in the container images is fully supported, the non-router components of the container distribution are covered under the Long-Term Support terms of the base operating system (currently the [Debian LTS program](https://wiki.debian.org/LTS)).

Other containers or base images might be supported on a reasonable-effort basis.

## Apollo Federation

Apollo Federation uses [semantic versioning](https://semver.org/). The minor version released in conjunction with a GraphOS Router release is supported for the same period as GraphOS Router.

Apollo provides security patches and critical bug fixes for the latest minor version of Apollo Federation or provides patches to the previous supported version used by an LTS GraphOS Router version if necessary.
