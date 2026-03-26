# Source: https://docs.infrahub.app/release-notes/infrahub/release-0_16_2.md

| Release Number   | 0.16.2                                                                                |
| ---------------- | ------------------------------------------------------------------------------------- |
| Release Date     | October 1st, 2024                                                                     |
| Release Codename | Beta #5, Patch #2                                                                     |
| Tag              | [infrahub-v0.16.2](https://github.com/opsmill/infrahub/releases/tag/infrahub-v0.16.2) |

# Release 0.16.2

We are thrilled to announce the latest release of Infrahub, version *0.16.2*!

This release focuses largely on bug fixes and is driven by our Beta Test users, and as always we greatly appreciate their feedback and time!

## Main changes[​](#main-changes "Direct link to Main changes")

The complete list of changes can always be found in the `CHANGELOG.md` file in the Infrahub Git repository.

### Fixed[​](#fixed "Direct link to Fixed")

* Loading a schema with an invalid order\_by field raise a proper error. ([#4323](https://github.com/opsmill/infrahub/issues/4323))

* Updates internal logic to improve performance when generating a diff.

  BREAKING CHANGE: Diff data, including conflict selections, will be deleted. We recommend merging any outstanding proposed changes before upgrading to this version. ([#4438](https://github.com/opsmill/infrahub/issues/4438))

* Fix performance issue for GraphQL queries that only count nodes. ([#4454](https://github.com/opsmill/infrahub/issues/4454))

* Fix ability to construct HFID for upsert mutations where a number attribute is used. ([#4460](https://github.com/opsmill/infrahub/issues/4460))

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
