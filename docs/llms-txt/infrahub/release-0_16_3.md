# Source: https://docs.infrahub.app/release-notes/infrahub/release-0_16_3.md

| Release Number   | 0.16.3                                                                                |
| ---------------- | ------------------------------------------------------------------------------------- |
| Release Date     | October 10th, 2024                                                                    |
| Release Codename | Beta #5, Patch #3                                                                     |
| Tag              | [infrahub-v0.16.3](https://github.com/opsmill/infrahub/releases/tag/infrahub-v0.16.3) |

# Release 0.16.3

We are thrilled to announce the latest release of Infrahub, version *0.16.3*!

This release focuses largely on bug fixes and is driven by our Beta Test users, and as always we greatly appreciate their feedback and time!

## Main changes[​](#main-changes "Direct link to Main changes")

The complete list of changes can always be found in the `CHANGELOG.md` file in the Infrahub Git repository.

### Removed[​](#removed "Direct link to Removed")

* Removed `infrahub.toml` configuration file from Docker builds.

### Fixed[​](#fixed "Direct link to Fixed")

* Save a diff in smaller pieces instead of all at once to prevent out-of-memory error. ([#4511](https://github.com/opsmill/infrahub/issues/4511))
* Fixes exception handling section in the Python SDK batch guide.

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
