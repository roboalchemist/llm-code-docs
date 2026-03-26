# Source: https://docs.infrahub.app/vscode/guides/execute-graphql-queries.md

# How to Execute GraphQL Queries

If you want to test GraphQL queries against your Infrahub instance without leaving VSCode, this guide shows you how to write, organize, and execute queries using the extension.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* Infrahub VSCode extension installed and configured
* At least one Infrahub server configured
* A workspace with `.infrahub.yml` file

## Step 1: Create query files[​](#step-1-create-query-files "Direct link to Step 1: Create query files")

Create a directory for your GraphQL queries:

```
mkdir queries
```

Create a GraphQL query file `queries/get_devices.gql`:

```
query GetDevices($status: String = "active") {
  NetworkDevice(status__value: $status) {
    edges {
      node {
        id
        hostname {
          value
        }
        model {
          value
        }
        status {
          value
        }
      }
    }
  }
}
```

## Step 2: Register queries in .infrahub.yml[​](#step-2-register-queries-in-infrahubyml "Direct link to Step 2: Register queries in .infrahub.yml")

Create or update your `.infrahub.yml` file to reference your queries:

```
---
queries:
  - name: get_active_devices
    file: queries/get_devices.gql
    
  - name: get_interfaces
    file: queries/get_interfaces.gql
    
  - name: topology_report
    file: queries/topology.gql
```

## Step 3: Execute a query[​](#step-3-execute-a-query "Direct link to Step 3: Execute a query")

1. Open the Infrahub YAML tree view in the Activity Bar
2. Expand your `.infrahub.yml` file
3. Navigate to the queries section
4. Right-click on "get\_active\_devices"
5. Select **Execute GraphQL Query**
6. Choose your server when prompted
7. Select the branch (usually "main")
8. View results in the new panel that opens

## Step 4: Work with query variables[​](#step-4-work-with-query-variables "Direct link to Step 4: Work with query variables")

For queries with variables, create `queries/get_devices_by_location.gql`:

```
query GetDevicesByLocation(
  $location: String!,
  $limit: Int = 10,
  $offset: Int = 0
) {
  NetworkDevice(
    location__name__value: $location,
    limit: $limit,
    offset: $offset
  ) {
    edges {
      node {
        hostname {
          value
        }
        location {
          node {
            name {
              value
            }
          }
        }
      }
    }
  }
}
```

When executing this query:

1. You'll be prompted for required variables (`$location`)
2. Optional variables (`$limit`, `$offset`) can be left empty to use defaults
3. Enter values in the input prompts that appear

## Step 5: Query different branches[​](#step-5-query-different-branches "Direct link to Step 5: Query different branches")

To execute queries against specific branches:

1. Right-click on your query in the tree view
2. Select **Execute GraphQL Query**
3. Choose your server
4. You'll see a list of available branches
5. Select the branch you want to query
6. The query executes against that branch's data

## Step 6: Complex query examples[​](#step-6-complex-query-examples "Direct link to Step 6: Complex query examples")

### Query with nested relationships[​](#query-with-nested-relationships "Direct link to Query with nested relationships")

```
query GetDeviceDetails($device_id: String!) {
  NetworkDevice(id: $device_id) {
    edges {
      node {
        hostname {
          value
        }
        interfaces {
          edges {
            node {
              name {
                value
              }
              ip_addresses {
                edges {
                  node {
                    address {
                      value
                    }
                    prefix {
                      node {
                        prefix {
                          value
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

### Mutation example[​](#mutation-example "Direct link to Mutation example")

```
mutation CreateDevice(
  $hostname: String!,
  $model: String!,
  $location_id: String!
) {
  NetworkDeviceCreate(
    data: {
      hostname: { value: $hostname }
      model: { value: $model }
      location: { id: $location_id }
    }
  ) {
    ok
    object {
      id
      hostname {
        value
      }
    }
  }
}
```

## Step 7: Organize queries by category[​](#step-7-organize-queries-by-category "Direct link to Step 7: Organize queries by category")

Structure your `.infrahub.yml` for better organization:

```
---
queries:
  # Inventory Queries
  - name: inventory_all_devices
    file: queries/inventory/all_devices.gql
    
  - name: inventory_by_location
    file: queries/inventory/by_location.gql
    
  # Network Topology
  - name: topology_layer2
    file: queries/topology/layer2.gql
    
  - name: topology_layer3
    file: queries/topology/layer3.gql
    
  # Reporting
  - name: report_capacity
    file: queries/reports/capacity.gql
    
  - name: report_compliance
    file: queries/reports/compliance.gql
```

## Validation[​](#validation "Direct link to Validation")

To verify your queries are working:

1. **Syntax Check**: The extension validates GraphQL syntax
2. **Test Execution**: Run each query with sample variables
3. **Branch Testing**: Execute against different branches
4. **Result Verification**: Check the output panel for expected data

## Advanced usage[​](#advanced-usage "Direct link to Advanced usage")

### Using fragments[​](#using-fragments "Direct link to Using fragments")

Create reusable fragments in `queries/fragments.gql`:

```
fragment DeviceBasicInfo on NetworkDevice {
  id
  hostname {
    value
  }
  model {
    value
  }
  status {
    value
  }
}

query GetDevicesWithFragment {
  NetworkDevice {
    edges {
      node {
        ...DeviceBasicInfo
        location {
          node {
            name {
              value
            }
          }
        }
      }
    }
  }
}
```

### Batch operations[​](#batch-operations "Direct link to Batch operations")

For multiple related queries, create a batch file:

```
query BatchDeviceQuery(
  $location: String!,
  $status: String = "active"
) {
  devices: NetworkDevice(
    location__name__value: $location,
    status__value: $status
  ) {
    count
    edges {
      node {
        hostname {
          value
        }
      }
    }
  }
  
  interfaces: NetworkInterface(
    device__location__name__value: $location
  ) {
    count
  }
  
  locations: LocationSite(
    name__value: $location
  ) {
    edges {
      node {
        name {
          value
        }
      }
    }
  }
}
```

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### Query execution fails[​](#query-execution-fails "Direct link to Query execution fails")

* Verify the GraphQL syntax is correct
* Check that all required variables are provided
* Ensure the schema types exist in your Infrahub instance
* Verify you have permission to access the queried data

### Variables not prompting[​](#variables-not-prompting "Direct link to Variables not prompting")

* Check variable definitions in your query
* Required variables use `!` (for example, `$location: String!`)
* Optional variables have defaults (for example, `$limit: Int = 10`)

### No results returned[​](#no-results-returned "Direct link to No results returned")

* Verify data exists on the selected branch
* Check filters in your query
* Ensure proper permissions for the data

## Related resources[​](#related-resources "Direct link to Related resources")

* [How to Manage Branches](/vscode/guides/manage-branches.md)
* [Understanding Schema Validation](/vscode/topics/schema-validation.md)
* [Extension Commands Reference](/vscode/reference/commands-settings.md)
