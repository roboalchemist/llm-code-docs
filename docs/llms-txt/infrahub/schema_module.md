# Source: https://docs.infrahub.app/ansible/references/plugins/schema_module.md

# Modules modules

Load, check, or export schemas in Infrahub through the Infrahub SDK. Use C(action=load) to load schemas into Infrahub. Use C(action=check) to validate schemas without applying them. Use C(action=export) to export existing schemas from Infrahub.

## Parameters[​](#parameters "Direct link to Parameters")

| Parameter              | Type   | Required | Default | Description                                                                                                                                                                                 |
| ---------------------- | ------ | -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api_endpoint`         | `str`  | No       |         | Endpoint of the Infrahub API, optional env=INFRAHUB\_ADDRESS                                                                                                                                |
| `token`                | `str`  | No       |         | The API token created through Infrahub, optional env=INFRAHUB\_API\_TOKEN                                                                                                                   |
| `timeout`              | `int`  | No       | 10      | Timeout for Infrahub requests in seconds                                                                                                                                                    |
| `validate_certs`       | `bool` | No       | True    | Whether or not to validate SSL of the Infrahub instance                                                                                                                                     |
| `action`               | `str`  | Yes      |         | The schema action to perform. C(load) loads schemas into Infrahub. C(check) validates schemas without applying them. C(export) exports existing schemas from Infrahub.                      |
| `branch`               | `str`  | No       | main    | Branch in which the request is made                                                                                                                                                         |
| `schemas`              | `list` | No       |         | List of inline schema definitions (nodes and generics). For C(load) and C(check), at least one of C(schemas) or C(schema\_files) must be provided.                                          |
| `schema_files`         | `list` | No       |         | List of YAML file paths containing schema definitions. Files are read on the Ansible controller. For C(load) and C(check), at least one of C(schemas) or C(schema\_files) must be provided. |
| `namespaces`           | `list` | No       |         | List of namespace names to filter the export. Only used with C(action=export).                                                                                                              |
| `wait_until_converged` | `bool` | No       | False   | Wait for schema to be synchronized across all workers. Only used with C(action=load).                                                                                                       |

## Examples[​](#examples "Direct link to Examples")

```
---
- name: Check schema from inline definition
  opsmill.infrahub.schema:
    action: check
    schemas:
      - name: Site
        namespace: Location
        attributes:
          - name: name
            kind: Text
            unique: true

- name: Load schema from file
  opsmill.infrahub.schema:
    action: load
    schema_files:
      - "schemas/my_schema.yml"

- name: Load schema with convergence wait
  opsmill.infrahub.schema:
    action: load
    schema_files:
      - "schemas/my_schema.yml"
    wait_until_converged: true

- name: Export all schemas
  opsmill.infrahub.schema:
    action: export
  register: result

- name: Export schemas for specific namespaces
  opsmill.infrahub.schema:
    action: export
    namespaces:
      - Infra
      - Location
  register: result
```

## Return values[​](#return-values "Direct link to Return values")

| Key              | Type   | Description                                                           |
| ---------------- | ------ | --------------------------------------------------------------------- |
| `changed`        | `bool` | Whether the schema was updated (load) or always false (check/export). |
| `schema_updated` | `bool` | Whether the schema hash changed after loading.                        |
| `hash`           | `str`  | New schema hash after loading.                                        |
| `previous_hash`  | `str`  | Previous schema hash before loading.                                  |
| `warnings`       | `list` | Schema warnings returned during load.                                 |
| `valid`          | `bool` | Whether the schema passed validation.                                 |
| `errors`         | `dict` | Validation errors when schema check fails.                            |
| `schemas`        | `dict` | Exported schemas organized by namespace.                              |
| `msg`            | `str`  | Message indicating the result of the operation.                       |
