# Source: https://docs.infrahub.app/ansible/references/plugins/artifact_fetch_module.md

# Modules modules

Fetch the content of an artifact from Infrahub through Infrahub SDK

## Parameters[​](#parameters "Direct link to Parameters")

| Parameter        | Type   | Required | Default | Description                                                               |
| ---------------- | ------ | -------- | ------- | ------------------------------------------------------------------------- |
| `api_endpoint`   | `str`  | No       |         | Endpoint of the Infrahub API, optional env=INFRAHUB\_ADDRESS              |
| `token`          | `str`  | No       |         | The API token created through Infrahub, optional env=INFRAHUB\_API\_TOKEN |
| `timeout`        | `int`  | No       | 10      | Timeout for Infrahub requests in seconds                                  |
| `artifact_name`  | `str`  | No       |         | Name of the artifact                                                      |
| `artifact_id`    | `str`  | No       |         | UUID of the artifact                                                      |
| `target_id`      | `str`  | No       |         | Id of the target for this artifact                                        |
| `branch`         | `str`  | No       | main    | Branch in which the request is made                                       |
| `validate_certs` | `bool` | No       | True    | Whether or not to validate SSL of the Infrahub instance                   |

## Examples[​](#examples "Direct link to Examples")

```
---
- name: Infrahub action plugin artifact_fetch
  gather_facts: false
  hosts: platform_eos
  vars:
    ansible_become: true

  tasks:
    - name: Query Startup Config for Edge Devices
      opsmill.infrahub.artifact_fetch:
        artifact_name: "Startup Config for Edge devices"
        target_id: "{{ id }}"
      register: startup_artifact

    - name: Save configs to localhost
      ansible.builtin.copy:
        content: "{{ startup_artifact.text }}"
        dest: "/tmp/{{ inventory_hostname }}-startup.conf"
        mode: '644'
      delegate_to: localhost
```

## Return values[​](#return-values "Direct link to Return values")

| Key    | Type   | Description                             |
| ------ | ------ | --------------------------------------- |
| `json` | `dict` | Content of the artifact in JSON format. |
| `text` | `str`  | Content of the artifact in TEXT format. |
