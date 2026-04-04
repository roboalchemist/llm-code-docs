# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_0_6.md

| Release Number   | 1.0.6                                                                               |
| ---------------- | ----------------------------------------------------------------------------------- |
| Release Date     | November 18th, 2024                                                                 |
| Release Codename | Stockholm, Patch #6                                                                 |
| Tag              | [infrahub-v1.0.6](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.0.6) |

# Release 1.0.6

This release is a bug-fix release to resolve issues found in Infrahub v1.0.5 and prior.

## Main changes[​](#main-changes "Direct link to Main changes")

The complete list of changes can always be found in the `CHANGELOG.md` file in the Infrahub Git repository.

### Fixed[​](#fixed "Direct link to Fixed")

* Forbid changing the "optional" property of an inherited attribute to not break GraphQL schema generation ([#4936](https://github.com/opsmill/infrahub/issues/4936))
* Permission edit\_default\_branch is now enforced properly when loading a schema ([#4958](https://github.com/opsmill/infrahub/issues/4958))
* Session is now correctly cleared when logging out from the web UI ([#4962](https://github.com/opsmill/infrahub/issues/4962))
* Anonymous user will get a 401 response when trying to load a schema

## Migration guide[​](#migration-guide "Direct link to Migration guide")

The process to migrate your instance of Infrahub to the latest version may vary depending on your deployment of Infrahub. However, at a high-level, it will involve getting the latest version of the Infrahub code, and then performing any needed Database Migrations and Schema updates.

Please ensure you have a **backup of your Infrahub environment** prior to attempting any migration or upgrade activities.

### Migration of an Infrahub instance[​](#migration-of-an-infrahub-instance "Direct link to Migration of an Infrahub instance")

**First**, update the Infrahub version running in your environment.

Below are some example ways to get the latest version of Infrahub in your environment.

* For deployments via Docker Compose, update your container version by updating the `VERSION` environment variable and relaunch:
  <!-- -->
  * `export VERSION="1.0.6"; docker compose pull && docker compose up -d`
* For deployments via Kubernetes, utilize the latest version of the Helm chart supplied with this release

**Second**, once you have gotten the desired version of Infrahub in your environment, please run the following commands.

> Note: If you are running Infrahub in Docker/K8s, these commands need to run from a container where Infrahub is installed.

```
infrahub db migrate
infrahub db update-core-schema
```

**Finally**, restart all instances of Infrahub.

### Migration of a dev or demo instance[​](#migration-of-a-dev-or-demo-instance "Direct link to Migration of a dev or demo instance")

If you are using the `dev` or `demo` environments, we have provided `invoke` commands to aid in the migration to the latest version. The below examples provide the `demo` version of the commands, however similar commands can be used for `dev` as well.

```
invoke demo.stop
invoke demo.build
invoke demo.migrate
invoke demo.start
```

If you don't want to keep your data, you can start a clean instance with the following command.

> **Warning: All data will be lost, please make sure to backup everything you need before running this command.**

```
invoke demo.destroy demo.build demo.start demo.load-infra-schema demo.load-infra-data
```

The repository [infrahub-demo-edge](https://github.com/opsmill/infrahub-demo-edge) has also been updated, it's recommended to pull the latest changes into your fork.
