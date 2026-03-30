# Source: https://docs.infrahub.app/release-notes/infrahub/release-0_15_3.md

| Release Number   | 0.15.3                                                                                |
| ---------------- | ------------------------------------------------------------------------------------- |
| Release Date     | August 13th, 2024                                                                     |
| Release Codename | Beta #4, Patch #3                                                                     |
| Tag              | [infrahub-v0.15.3](https://github.com/opsmill/infrahub/releases/tag/infrahub-v0.15.3) |

# Release 0.15.3

We are thrilled to announce the latest release of Infrahub (0.15.3).

## Main changes[​](#main-changes "Direct link to Main changes")

### Unified storage[​](#unified-storage "Direct link to Unified storage")

### Schema[​](#schema "Direct link to Schema")

### Frontend[​](#frontend "Direct link to Frontend")

### Helm chart[​](#helm-chart "Direct link to Helm chart")

### Infrahub sync[​](#infrahub-sync "Direct link to Infrahub sync")

### Other[​](#other "Direct link to Other")

#### Added[​](#added "Direct link to Added")

* Add usage of Towncrier to generate Changelog as part of the release process. For detailed information, see the [Documentation](/development/changelog.md). ([#4023](https://github.com/opsmill/infrahub/issues/4023))
* Serve Swagger & Redoc files locally so that the REST-API docs work offline or when isolated from the internet. ([#4063](https://github.com/opsmill/infrahub/issues/4063))

#### Fixed[​](#fixed "Direct link to Fixed")

* Fix attribute uniqueness check that was incorrectly running against schema nodes, ([#3986](https://github.com/opsmill/infrahub/issues/3986))
* Provide better information when available during schema conflicts in the pipeline. ([#3987](https://github.com/opsmill/infrahub/issues/3987))
* Fix schema sync issue between worker nodes. ([#3994](https://github.com/opsmill/infrahub/issues/3994))
* Updates the Profile type select when creating a Profile, to display more relevant information about the related nodes. ([#4001](https://github.com/opsmill/infrahub/issues/4001))
* Fix logic that prevented existing inherited attribute / relationships from being updated. ([#4004](https://github.com/opsmill/infrahub/issues/4004))
* Fix attribute uniqueness validator to not run in isolated mode. ([#4025](https://github.com/opsmill/infrahub/issues/4025))
* Update getting-started/branches referencing the wrong org from previous step. Update getting-started/resource-manager referencing the wrong button. Regenerate the screenshots for the tutorial. ([#4035](https://github.com/opsmill/infrahub/issues/4035))
* Fix object creation for schema node using enum attribute in uniqueness constraint groups. ([#4054](https://github.com/opsmill/infrahub/issues/4054))

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
