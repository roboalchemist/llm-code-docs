# Source: https://rspack.dev/misc/planning/future.md

# Future behavior

## Breaking changes

During the 0.y.z phase, Rspack may include breaking changes only when upgrading the minor (y) version, and ensures backward compatibility when upgrading the patch (z) version.

After reaching version 1.0.0, we will adhere to [semver](https://semver.org/) for version management.

## Deprecation

| Stage | Version | Description |
| --- | --- | --- |
| **Deprecated***default value ~unchanged~* | Current version | It's open for migration. The default behavior remains **unchanged**. |
| **Deprecated***default value ~applied~* | Next minor | The default behavior is **changed** to the latest one. Turning off this new behavior is still an option, but you should migrate to the new behavior as soon as possible. |
| **Removed** | Minor/Major after next minor | The migration should be completed. The old behavior and its corresponding option is **removed**. At the time, please refer to the migration guide or release note for the new behavior. |

