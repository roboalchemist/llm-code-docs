# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/VersionHelper.md

# [VersionHelper](https://bryntum.com/docs/gantt/api/Core/helper/VersionHelper)

Helper for version handling

```
VersionHelper.setVersion('grid', '1.5');
if (VersionHelper.grid.isNewerThan('1.0')) {
  ...
}
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTestEnv](https://bryntum.com/docs/gantt/api/Core/helper/VersionHelper#property-isTestEnv-static)
Returns truthy value if environment is in testing mode

## Functions

Functions are methods available for calling on the class

[setVersion](https://bryntum.com/docs/gantt/api/Core/helper/VersionHelper#function-setVersion-static)
Set version for specified product

[getVersion](https://bryntum.com/docs/gantt/api/Core/helper/VersionHelper#function-getVersion-static)
Get (previously set) version for specified product

[semanticCompareVersion](https://bryntum.com/docs/gantt/api/Core/helper/VersionHelper#function-semanticCompareVersion-static)
Checks the version1 against the passed version2 using the comparison operator. Supports `rc`, `beta`, `alpha` release states. Eg. `1.2.3-alpha-1`. State which is not listed above means some version below `alpha`.

[checkVersion](https://bryntum.com/docs/gantt/api/Core/helper/VersionHelper#function-checkVersion-static)
Checks the passed product against the passed version using the passed test.

[deprecate](https://bryntum.com/docs/gantt/api/Core/helper/VersionHelper#function-deprecate-static)
Based on a comparison of current product version and the passed version this method either outputs a console.warn or throws an error.
