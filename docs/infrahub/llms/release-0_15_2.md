# Source: https://docs.infrahub.app/release-notes/infrahub/release-0_15_2.md

| Release Number   | 0.15.2                                                                                |
| ---------------- | ------------------------------------------------------------------------------------- |
| Release Date     | July 31st, 2024                                                                       |
| Release Codename | Beta #4, Patch #2                                                                     |
| Tag              | [infrahub-v0.15.2](https://github.com/opsmill/infrahub/releases/tag/infrahub-v0.15.2) |

# Release 0.15.2

We are thrilled to announce the latest release of Infrahub (0.15.2).

## Main changes[​](#main-changes "Direct link to Main changes")

### Unified storage[​](#unified-storage "Direct link to Unified storage")

### Schema[​](#schema "Direct link to Schema")

* Allow using HFID for relationships when creating new nodes @gmazoyer (#3966)

### Frontend[​](#frontend "Direct link to Frontend")

### Helm chart[​](#helm-chart "Direct link to Helm chart")

### Infrahub sync[​](#infrahub-sync "Direct link to Infrahub sync")

### Other[​](#other "Direct link to Other")

#### 🐛 Bug fixes[​](#-bug-fixes "Direct link to 🐛 Bug fixes")

* Fix OpenAPI documentation of schema load endpoint @dgarros (#3911)
* Fix return code when trying to use a restricted namespace @dgarros (#3912)
* Validate HFID and uniqueness constraints format when loading a schema @gmazoyer (#3972)
* Run artifact refresh after Generators in proposed changes pipeline @ajtmccarty (#3897)
* Fix button covering GraphQL query view @bilalabbad (#3964)
* Fix dot on tree being hidden when there is a very long text, also improve CSS for the tree @bilalabbad (#3958)
* Fix branch details page open correctly when the branch name contains a `/` @bilalabbad (#3917)

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
