# Source: https://docs.startree.ai/corecapabilities/security/custom-policies.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Policy Configuration

> Define and implement custom RBAC policies in StarTree Cloud by configuring granular permissions using StarTree Resource Names (SRNs), supporting over 150 distinct actions for precise access control across environments, clusters, and tables.

A policy configuration is a collection of one or more statement objects, each containing:

* A description of the policy statement.
* One or more [actions](/corecapabilities/security/actions) that the policy statement applies to.
* The resources that the policy statement is applied to, identified using the [SRN format](#identifying-resources-using-srns).
* The effect of the policy statement (`allow` or `deny`).

Here’s an example of a policy that allows querying a table called “myTable”:

```json  theme={null}
{
  "version": "v1",
  "statements": [
    {
      "description": "A sample policy - allow query on a table called 'myTable', deny everything else",
      "resources": [
        "srn2:cluster#*:table#myTable"
      ],
      "effect": "allow",
      "actions": [
        "query"
      ]
    }
  ]
}
```

<Info>
  * Within a policy, **deny statements take precedence** regardless of their location in the policy.
  * If actions aren’t explicitly specified, then all actions are implicitly included in the statement (the equivalent of writing `“actions”: “*”`).
  * If the effect isn’t explicitly specified, then `deny` is implicitly applied (the equivalent of writing `“effect”: “deny”`).
</Info>

## Identifying resources using SRNs

A StarTree Resource Name (SRN) is a unique identifier for any resource within your StarTree environment. It follows a standardized format that makes it easy to understand and use.

### SRNv2 format

The basic format of an SRNv2 is: `srn2:<resource-type>#<resource-id>`.
For example: srn2:table#myTable identifies the table called “myTable”.
Some resources may have a more complex format to represent hierarchical relationships.

### Constructing an SRNv2 string

Each SRNv2 string starts with the prefix `srn2:`, followed by the resource type and then the resource identifier. A simple SRNv2 would follow this format: `srn2:resource-type#resource-id`

Since resources in StarTree are hierarchical, the SRNv2 string can include any number of levels of hierarchy. An SRNv2 with two levels of hierarchy would look like this: `srn2:resource-type#resource-id:sub-resource-type#sub-resource-id`

Commonly used resource types include: environment, cluster, workspace, and table.

Hierarchy levels can be omitted. For example, you can write a policy that applies to all tables called “myTable” across the entire environment by omitting the cluster resource type. Alternatively, you can explicitly include all clusters by adding `cluster#*` in the SRN.

## Examples of Policy Configurations for Common Functional Roles

With over 150 distinct [actions](/corecapabilities/security/actions), Apache Pinot and StarTree allow for very granular custom policy creation. This section provides guidance on mapping common functional roles and application usage to the specific permissions required in Apache Pinot.

This information serves as a guide for RBAC administrators to create and maintain policies and roles efficiently.

### System Administrator

A System Administrator can perform all actions on any resource in the environment.

<Info>
  The `system-admin` policy is predefined in StarTree, so you won't need to define it yourself. We're just showing it here as an example.
</Info>

```json  theme={null}
{
  "version": "v1",
  "statements": [
    {
      "description": "Can do everything in an environment",
      "resources": "*",
      "effect": "allow",
      "actions": "*"
    }
  ]
}
```

### Cluster Administrator

A cluster administrator can perform all actions in a Pinot cluster

```json  theme={null}
{
  "version": "v1",
  "statements": [
    {
      "description": "Allow all actions on the 'Pinot' cluster, and all tables in the cluster",
      "resources": [
        "srn2:cluster#pinot",
        "srn2:cluster#pinot:table#*"
      ],
      "effect": "allow",
      "actions": "*"
    }
  ]
}
```

The same policy can also be written like this:

```json  theme={null}
{
  "version": "v1",
  "statements": [
    {
      "description": "Allow all actions on the 'Pinot' cluster, including all resources in the cluster.",
      "resources": "srn2:cluster#pinot:*#*",
      "effect": "allow",
      "actions": "*"
    }
  ]
}
```

### Table Admin

A table admin can perform any action on a table.

```json  theme={null}
{
    "version": "v1",
    "statements": [
    {
        "resources": "srn2:cluster#*:table#*",
        "effect": "allow",
        "actions": "*"
      },
      {
        "resources": "srn2:cluster#*",
        "effect": "allow",
        "actions": [
          "Get*",
          "*Task",
          "RecommendConfig"
        ]
      }
    ]
  }
```

### Table Reader

A table reader policy allows any read-only operation on a given table using the Query Console UI. Unlike the [QueryTable](../security/custom-policies#query-table) policy, this policy includes additional permissions that allow the UI to retrieve additional helpful information about the table.

```json  theme={null}
{
  "version": "v1",
  "statements": [
    {
      "description": "Allow any read-only operation on a Pinot table",
      "resources": "srn2:cluster#pinot:table#myTable",
      "effect": "allow",
      "actions": [
  "GetState",
  "ValidateTableConfigs",
  "GetTableConfig",
  "GetSchema",
  "ValidateSchema",
  "Query"
      ]
    },
 {
      "resources": "srn2:cluster#pinot",
      "effect": "allow",
      "actions": [
  "GetTable"
      ]
 }
  ]
}
```

### **Query Table**

This policy allows querying a given table.

```
{
  "version": "v1",
  "statements": [
    {
      "description": "Allow querying a Pinot table",
      "resources": "srn2:cluster#pinot:table#myTable",
      "effect": "allow",
      "actions": "Query"
    }
  ]
}RBAC Admin
```

### RBAC Admin

This policy allows viewing and making changes to the RBAC policies, roles, assignments, and API tokens.

```json  theme={null}
{
  "version": "v1",
  "statements": [
    {
      "description": "Allow all actions on policies, role, and service tokens",
      "resources": [
        "srn2:policy#*",
        "srn2:role#*",
  "srn2:service-token#*"
      ]
      "effect": "allow",
      "actions": [
  "delete*",
  "create*",
  "update*",
  "detach*",
  "attach*"
   ]
    }
  ]
}
```

### Row-Level Access Control Policies

<Warning>
  Row-Level Access Control is currently in beta. Contact your customer success manager for a private preview.
</Warning>

Row-Level Access Control policies allow you to restrict access to specific rows within a table using conditional filters. These policies include a `conditions` section with `rowFilters`:

#### Single Condition

```json  theme={null}
{
  "version": "v1",
  "statements": [
    {
      "description": "Allow access to specific user data only",
      "resources": ["srn2:cluster#pinot:table#pageviews"],
      "effect": "allow",
      "actions": ["query"],
      "conditions": {
        "rowFilters": ["user_id = 18314973"]
      }
    }
  ]
}
```

#### Multi-Condition

```json  theme={null}
{
  "version": "v1",
  "statements": [
    {
      "description": "Allow high-value sessions for specific user",
      "resources": ["srn2:cluster#pinot:table#pageviews"],
      "effect": "allow",
      "actions": ["query"],
      "conditions": {
        "rowFilters": ["user_id = 18314973 AND session_value > 1000"]
      }
    }
  ]
}
```

Learn more about [Row-Level Access Control](/corecapabilities/security/row-level-access-control) for detailed implementation guidance.

### Using Wildcards

Wildcards provide flexibility to leverage naming conventions used in your organization.

In this example, the policy will:

* Allow all actions on tables with the prefix "Test"
* Allow queries on tables with the prefix "Prod"
* Deny deletes for all tables

```json  theme={null}
{
  "version": "v1",
  "statements": [
    {
      "description": "Query tables with the prefix 'Prod'",
      "resources": "srn2:cluster#*:table#Prod*",
      "effect": "allow",
      "actions": "Query"
    },
    {
      "description": "All actions on tables with the prefix 'Test'",
      "resources": "srn2:cluster#*:table#Test*",
      "effect": "allow",
      "actions": "*"
    },
    {
      "description": "Deny dropping tables and pausing consumption on all tables",
      "resources": "srn2:cluster#*:table#*",
      "effect": "deny",
      "actions": [
        "Delete*",
        "PauseConsumption"
      ]
    }
  ]
}
```

Built with [Mintlify](https://mintlify.com).
