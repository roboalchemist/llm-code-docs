# Source: https://docs.infrahub.app/release-notes/infrahub/release-0_15_1.md

| Release Number   | 0.15.1                                                                                |
| ---------------- | ------------------------------------------------------------------------------------- |
| Release Date     | July 23rd, 2024                                                                       |
| Release Codename | Beta #4, Patch #1                                                                     |
| Tag              | [infrahub-v0.15.1](https://github.com/opsmill/infrahub/releases/tag/infrahub-v0.15.1) |

# Release 0.15.1

We are thrilled to announce the latest release of Infrahub (0.15.1).

## Main changes[​](#main-changes "Direct link to Main changes")

### Unified storage[​](#unified-storage "Direct link to Unified storage")

### Schema[​](#schema "Direct link to Schema")

### Frontend[​](#frontend "Direct link to Frontend")

#### Multi Profiles[​](#multi-profiles "Direct link to Multi Profiles")

We can now select multiple Profiles when creating and editing an object.

The `profile_priority` value from the Profile schema is used to understand which value is used for the fields (the lower the number is, the higher the priority is).

#### Generic relationship select fixes[​](#generic-relationship-select-fixes "Direct link to Generic relationship select fixes")

The select for a generic relationship has been fixed to properly reset the value when changing the kind or the parent.

The parent is also not showing "Unknown" after choosing an object.

The parent select is also now hidden if it's not available.

It's displayed and available only of the kind selected can point to an object which we can filter depending on its parent.

### Helm chart[​](#helm-chart "Direct link to Helm chart")

### Infrahub sync[​](#infrahub-sync "Direct link to Infrahub sync")

### Other[​](#other "Direct link to Other")

#### 🐛 Bug fixes[​](#-bug-fixes "Direct link to 🐛 Bug fixes")

* Fix disabling fields when it is protected and owned by another user by @bilalabbad in [#3838](https://github.com/opsmill/infrahub/pull/3838)
* Generic selector fixes to correctly reset values when changing kind or object by @pa-lem in [#3837](https://github.com/opsmill/infrahub/pull/3837)

#### 🧰 Maintenance[​](#-maintenance "Direct link to 🧰 Maintenance")

* Hides parent field if not available in generic relationship select by @pa-lem in [#3861](https://github.com/opsmill/infrahub/pull/3861)
* Add missing overview docs pages by @petercrocker in [#3856](https://github.com/opsmill/infrahub/pull/3856)
* Add option to fetch peers nodes in query\_peers by @dgarros in [#3870](https://github.com/opsmill/infrahub/pull/3870)

### Demo environment[​](#demo-environment "Direct link to Demo environment")

## Migration guide[​](#migration-guide "Direct link to Migration guide")

To migrate your instance of Infrahub to the latest version, please run the following commands and restart all instances of Infrahub.

```
infrahub db migrate
infrahub db update-core-schema
```

> If you are running in Docker these commands need to run from the container where Infrahub is installed

### Migration of the demo instance[​](#migration-of-the-demo-instance "Direct link to Migration of the demo instance")

If you are using the demo environment, you can migrate to the latest version with the following commands

```
invoke demo.stop
invoke demo.build
invoke demo.migrate
invoke demo.start
```

If you don't want to keep your data, you can start a clean instance with the following command

```
invoke demo.destroy demo.build demo.start demo.load-infra-schema demo.load-infra-data
```

> All data will be lost, please make sure to backup everything you need before running this command.

The repository [infrahub-demo-edge](https://github.com/opsmill/infrahub-demo-edge) has also been updated, it's recommended to pull the latest changes into your fork.
