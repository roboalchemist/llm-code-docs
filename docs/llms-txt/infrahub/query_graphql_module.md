# Source: https://docs.infrahub.app/ansible/references/plugins/query_graphql_module.md

# Modules modules

Queries Infrahub via its GraphQL API through Infrahub SDK

## Parameters[​](#parameters "Direct link to Parameters")

| Parameter         | Type   | Required | Default | Description                                                                                                                                                                                                                                                                                                               |
| ----------------- | ------ | -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api_endpoint`    | `str`  | No       |         | Endpoint of the Infrahub API, optional env=INFRAHUB\_ADDRESS                                                                                                                                                                                                                                                              |
| `token`           | `str`  | No       |         | The API token created through Infrahub, optional env=INFRAHUB\_API\_TOKEN                                                                                                                                                                                                                                                 |
| `timeout`         | `int`  | No       | 10      | Timeout for Infrahub requests in seconds                                                                                                                                                                                                                                                                                  |
| `query`           | `str`  | Yes      |         | GraphQL query parameters or filters to send to Infrahub to obtain desired data                                                                                                                                                                                                                                            |
| `graph_variables` | `dict` | No       |         | Dictionary of keys/values to pass into the GraphQL query                                                                                                                                                                                                                                                                  |
| `branch`          | `str`  | No       | main    | Branch in which the request is made                                                                                                                                                                                                                                                                                       |
| `validate_certs`  | `bool` | No       | True    | Whether or not to validate SSL of the Infrahub instance                                                                                                                                                                                                                                                                   |
| `update_hostvars` | `bool` | No       | False   | Whether or not to populate data in the in the root (example hostvars\[inventory\_hostname]) or within the 'data' key (example `hostvars[inventory_hostname]['data']`). Beware, that the root keys provided by the query will overwrite any root keys already present, leverage the GraphQL alias feature to avoid issues. |

## Examples[​](#examples "Direct link to Examples")

```
---
- name: Infrahub action plugin query_graphql
  gather_facts: false
  hosts: localhost

  tasks:
    - name: SET FACTS TO SEND TO GRAPHQL ENDPOINT
      ansible.builtin.set_fact:
        variables:
          device_name: "atl1-edge1"
          enabled: true

        query_dict:
          InfraDevice:
            '@filters': {name__value: '$device_name'}
            edges:
              node:
                name:
                  value: null
                interfaces:
                  '@filters': {enabled__value: '$enabled'}
                  edges:
                    node:
                      name:
                        value: null

    - name: Action Plugin
      opsmill.infrahub.query_graphql:
        query: "{{ query_dict }}"
        graph_variables: "{{ variables }}"
```

## Return values[​](#return-values "Direct link to Return values")

| Key    | Type   | Description                                    |
| ------ | ------ | ---------------------------------------------- |
| `data` | `dict` | Data result from the Infrahub GraphQL endpoint |
