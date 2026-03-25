# Source: https://docs.startree.ai/corecapabilities/security/row-level-access-control.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Row-Level Access Control

> Restrict access to specific rows within tables using conditional policies, enabling secure data sharing while maintaining data isolation for different users and groups.

<Warning>
  Row-Level Access Control is currently in beta. Contact your customer success manager for a private preview.
</Warning>

Row-Level Access Control allows you to restrict access to a subset of rows within a table for specific entities (users, groups, or tokens). This provides more granular control than traditional table-level permissions.

<Info>
  Row-Level Access Control builds upon StarTree's Role-Based Access Control (RBAC) system. Ensure you have [RBAC enabled](/corecapabilities/security/manage-access) before implementing row-level policies.
</Info>

## How Row-Level Access Control Works

Unlike table-level RBAC which provides all-or-nothing access to a table, Row-Level Access Control allows you to define conditions that determine which rows a user can access within a table.

When a user with row-level policies queries a table, StarTree automatically:

1. **Identifies** the user's assigned roles and associated row-level policies
2. **Extracts** the row filter conditions from the policies
3. **Applies** these conditions as additional WHERE clauses to the query
4. **Returns** only the rows that match both the original query and the row filter conditions

## Policy Configuration

Row-level policies use the same structure as standard RBAC policies but include a `conditions` section with `rowFilters`:

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

## Row Filter Syntax

### Single Condition Filters

Row filters are valid SQL expressions that can be used in WHERE clauses:

```json  theme={null}
{
  "conditions": {
    "rowFilters": ["user_id = 12345"]
  }
}
```

```json  theme={null}
{
  "conditions": {
    "rowFilters": ["region = 'US'"]
  }
}
```

### Multi-Condition Filters

Combine multiple conditions using SQL operators:

```json  theme={null}
{
  "conditions": {
    "rowFilters": ["user_id = 18314973 AND session_value > 1000"]
  }
}
```

```json  theme={null}
{
  "conditions": {
    "rowFilters": ["user_id IN (18314973, 18314974, 18314975) AND total_time_spent >= 10000"]
  }
}
```

```json  theme={null}
{
  "conditions": {
    "rowFilters": ["data_region = 'EU' AND compliance_flag = 'GDPR'"]
  }
}
```

## Implementation Steps

Row-Level Access Control follows the same implementation process as any other RBAC policy:

1. **Create a policy** with row filter conditions in the Security Manager
2. **Create a role** and attach the policy to it
3. **Assign the role** to users or groups

The process is identical to standard RBAC - the only difference is adding the `conditions` section with `rowFilters` to your policy configuration.

You can use the StarTree Security Manager UI to apply these policies.

## Use Cases

### Vendor Data Isolation

Allow vendors to see only their own orders in a shared table:

```json  theme={null}
{
  "version": "v1",
  "statements": [
    {
      "description": "Vendor can only see their own orders",
      "resources": ["srn2:cluster#pinot:table#orders"],
      "effect": "allow",
      "actions": ["query"],
      "conditions": {
        "rowFilters": ["vendor_id = 'VENDOR_123'"]
      }
    }
  ]
}
```

### Sales Territory Management

Restrict sales reps to view only their assigned accounts:

```json  theme={null}
{
  "version": "v1",
  "statements": [
    {
      "description": "Sales rep can only access assigned territories",
      "resources": ["srn2:cluster#pinot:table#customer_accounts"],
      "effect": "allow",
      "actions": ["query"],
      "conditions": {
        "rowFilters": ["sales_rep_id = 'REP_456' AND territory = 'West'"]
      }
    }
  ]
}
```

### Regional Data Compliance

Enforce data residency by region within a global table:

```json  theme={null}
{
  "version": "v1",
  "statements": [
    {
      "description": "EU users can only access EU data",
      "resources": ["srn2:cluster#pinot:table#user_analytics"],
      "effect": "allow",
      "actions": ["query"],
      "conditions": {
        "rowFilters": ["data_region = 'EU' AND compliance_flag = 'GDPR'"]
      }
    }
  ]
}
```

## Limitations

* Row-level policies may take up to one hour to propagate and become effective after creation or modification.
* Row filter conditions currently require static values to be specified in the policy configuration. Dynamic row filtering capabilities are planned for future releases.

## Next Steps

* Learn about [Custom Policy Configuration](/corecapabilities/security/custom-policies)
* Explore [RBAC API usage](/corecapabilities/security/using-rbac-api)
* Review [Security Actions](/corecapabilities/security/actions) available for policies

Built with [Mintlify](https://mintlify.com).
