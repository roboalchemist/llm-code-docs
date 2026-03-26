# Source: https://docs.api7.ai/enterprise/3.2.16.7/reference/permission-policy-examples.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/reference/permission-policy-examples.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/reference/permission-policy-examples.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/reference/permission-policy-examples.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/reference/permission-policy-examples.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/reference/permission-policy-examples.md

# Source: https://docs.api7.ai/enterprise/reference/permission-policy-examples.md

# Source: https://docs.api7.ai/enterprise/3.8.x/reference/permission-policy-examples.md

# Source: https://docs.api7.ai/enterprise/3.7.x/reference/permission-policy-examples.md

# Source: https://docs.api7.ai/enterprise/3.6.x/reference/permission-policy-examples.md

# Source: https://docs.api7.ai/enterprise/3.5.x/reference/permission-policy-examples.md

# Source: https://docs.api7.ai/enterprise/3.4.x/reference/permission-policy-examples.md

# Source: https://docs.api7.ai/enterprise/3.3.x/reference/permission-policy-examples.md

# Permission Policy Examples

### Full Access to All Resources[â](#full-access-to-all-resources "Direct link to Full Access to All Resources")

This policy grants unrestricted access to all resources and actions within API7 Enterprise. The `<.*>` wildcard in both `resources` and `actions` signifies "all". This is the most permissive policy and is typically reserved for super administrators.

```
{
 "statement": [
    {
      "resources": [
        "<.*>"
      ],
      "actions": [
        "<.*>"
      ],
      "effect": "allow" 
    }
  ]
}
```

### View-only to All Resources[â](#view-only-to-all-resources "Direct link to View-only to All Resources")

This policy allows a user to view all resources but not make any changes. The `actions` are restricted to those containing "Get", which typically corresponds to read-only operations. This is useful for roles that need visibility across the system without modification privileges.

```
{
 "statement": [
    {
      "resources": [
        "<.*>"
      ],
      "actions": [
        "<.*>Get<.*>"
      ],
      "effect": "allow"      
    }
  ]
}
```

### View-only to Specific Gateway Groups[â](#view-only-to-specific-gateway-groups "Direct link to View-only to Specific Gateway Groups")

This policy grants read-only access to a specific list of Gateway Groups and the services published within them. It uses the unique gateway group ID to identify each resource. This is ideal for users who need to monitor specific environments, like production or testing, without the ability to alter configurations.

```
{
  "statement": [
    {
      "resources": [
        "arn:api7:gateway:gatewaygroup/{gateway group id 1}",
        "arn:api7:gateway:gatewaygroup/{gateway group id 2}"
      ],
      "actions": [
        "<.*>Get<.*>"
      ],
      "effect": "allow"
    },
    {
      "resources": [
         "arn:api7:gateway:gatewaygroup/{gateway group id 1}/publishedservice/<.*>",
         "arn:api7:gateway:gatewaygroup/{gateway group id 2}/publishedservice/<.*>"
      ],
      "actions": [
        "<.*>Get<.*>"
      ],
      "effect": "allow"
    }
  ]
}
```

### Full Access to Specific Gateway Groups[â](#full-access-to-specific-gateway-groups "Direct link to Full Access to Specific Gateway Groups")

This policy provides complete control over specified Gateway Groups and their associated services. Multiple statements in a policy are combined with an "OR" relationship, meaning if any statement allows an action, it is permitted. This is suitable for environment-specific administrators, such as a production operations team.

```
{
  "statement": [
    {
      "resources": [
        "arn:api7:gateway:gatewaygroup/{gateway group id 1}",
        "arn:api7:gateway:gatewaygroup/{gateway group id 2}" 
      ],
      "actions": [
        "<.*>"
      ],
      "effect": "allow"
    },
    {
      "resources": [
        "arn:api7:gateway:gatewaygroup/{gateway group id 1}/publishedservice/<.*>",
        "arn:api7:gateway:gatewaygroup/{gateway group id 2}/publishedservice/<.*>"
      ],
      "actions": [
        "<.*>"
      ],
      "effect": "allow"
    }
  ]
} 
```

### Full Access to Specific Gateway Groups except Consumer Credentials[â](#full-access-to-specific-gateway-groups-except-consumer-credentials "Direct link to Full Access to Specific Gateway Groups except Consumer Credentials")

This policy grants broad permissions to specific Gateway Groups but explicitly denies the ability to manage consumer credentials. It demonstrates the "deny overrides allow" principle, where a `deny` effect takes precedence over any `allow` statements for the same resource and action. This is a crucial security measure to protect sensitive consumer data.

```
{
  "statement": [
    {
      "resources": [
        "arn:api7:gateway:gatewaygroup/{gateway group id 1}",
        "arn:api7:gateway:gatewaygroup/{gateway group id 2}"
      ],
      "actions": [
        "<.*>"
      ],
      "effect": "allow"
    },
    {
      "resources": [
        "arn:api7:gateway:gatewaygroup/{gateway group id 1}/publishedservice/<.*>",
        "arn:api7:gateway:gatewaygroup/{gateway group id 2}/publishedservice/<.*>"
      ],
      "actions": [
        "<.*>"
      ],
      "effect": "allow"
    },
    {
      "resources": [
        "arn:api7:gateway:gatewaygroup/<.*>/consumer/<.*>"
      ],
      "actions": [
        "gateway:GetConsumerCredential",
        "gateway:UpdateConsumerCredential",
        "gateway:DeleteConsumerCredential"
      ],
      "effect": "deny"
    }
  ]
} 
```

### Service Manager[â](#service-manager "Direct link to Service Manager")

This policy is designed for a "Service Manager" role who can manage specific services across all Gateway Groups. This includes modifying service templates, publishing services, and syncing them between groups. It grants broad permissions to specific service templates and their corresponding published services, while also providing necessary read access to Gateway Groups and global plugin rules to avoid conflicts.

note

Please learn the [difference between `ServiceTemplateID` and `ServiceID`](https://docs.api7.ai/enterprise/3.3.x/key-concepts/services.md#serviceid-vs-servicetemplateid)

```
{
  "statement": [
    {
      "resources": [
        "arn:api7:gateway:servicetemplate/{service template id}" 
      ],
      "actions": [
        "<.*>"
      ],
      "effect": "allow"
    },
    {
      "resources": [
        "arn:api7:gateway:gatewaygroup/<.*>/publishedservice/{service template id}"
      ],
      "actions": [
        "<.*>"
      ],
      "effect": "allow"
    },
     {
      "resources": [
        "arn:api7:gateway:gatewaygroup/<.*>"
      ],
      "actions": [
        "gateway:GetGatewayGroup",
        "gateway:GetGlobalPluginRule",
        "gateway:GetPluginMetadata"
      ],
      "effect": "allow" 
    }
  ]
}
```

Alternatively, you can use labels for more dynamic and scalable management of multiple services. This policy grants the same service management permissions but uses a `MatchLabel` condition to apply them to all services with the label `team: enterprise`.

```
{
  "statement": [
    {
      "resources": [
        "arn:api7:gateway:servicetemplate/<.*>" 
      ],
      "actions": [
        "<.*>"
      ],
      "conditions": {
        "service_label": {
          "type": "MatchLabel",
          "options": {
            "key": "team",
            "operator": "exact_match",
            "value": "enterprise"
          }
        }
      },
      "effect": "allow"
    },
    {
      "resources": [
        "arn:api7:gateway:gatewaygroup/<.*>/publishedservice/<.*>" 
      ],
      "actions": [
        "<.*>"
      ],
      "conditions": {
        "service_label": {
          "type": "MatchLabel",
          "options": {
            "key": "team",
            "operator": "exact_match",
            "value": "enterprise"
          }
        }
      },
      "effect": "allow"
    },
    {
      "resources": [
        "arn:api7:gateway:gatewaygroup/<.*>"
      ],
      "actions": [
        "gateway:GetGatewayGroup"
      ],
      "effect": "allow" 
    }
  ]
}
```

### Manage Custom Plugins[â](#manage-custom-plugins "Direct link to Manage Custom Plugins")

This policy grants permissions to manage custom plugins within the gateway settings. It allows any action that includes "CustomPlugin", providing full control over the lifecycle of custom plugins.

```
{
  "statement": [
    {
      "resources": [
        "arn:api7:gateway:gatewaysetting/*"
      ],
      "actions": [
        "gateway:<.*>CustomPlugin<.*>"
      ],
      "effect": "allow"
    }
  ]
}
```

### Role Manager[â](#role-manager "Direct link to Role Manager")

This policy is for a "Role Manager" who is responsible for user and role administration. It grants full permissions to manage users, roles, and permission policies, allowing them to invite/delete users, reset passwords, design custom roles, and assign roles to users.

```
{
  "statement": [
    {
      "resources": [
        "arn:api7:iam:user/<.*>"
      ],
      "actions": [
        "<.*>"
      ],
      "effect": "allow"
    },
    {
      "resources": [
        "arn:api7:iam:role/<.*>"
      ],
      "actions": [
        "<.*>"
      ],
      "effect": "allow"
    },
    {
      "resources": [
        "arn:api7:iam:permissionpolicy/<.*>"
      ],
      "actions": [
        "<.*>"
      ],
      "effect": "allow"
    }
  ]
}
```

### Create and Manage Production Gateway Groups[â](#create-and-manage-production-gateway-groups "Direct link to Create and Manage Production Gateway Groups")

This policy allows a user to create new Gateway Groups and fully manage existing Gateway Groups that are labeled as "production". The `conditions` block filters the scope of the permissions, ensuring that the user can only affect resources with the specified label. This is a powerful way to enforce environment-specific access control.

```
{
  "statement": [
    {
      "resources": [
        "arn:api7:gateway:gatewaygroup/<.*>"
      ],
      "actions": [
        "<.*>"
      ],
      "conditions": {
        "gateway_group_label": {
          "type": "MatchLabel",
          "options": {
            "key": "type",
            "operator": "exact_match",
            "value": "production"
          }
        }
      },
      "effect": "allow"
    },
    {
      "resources": [
        "arn:api7:gateway:gatewaygroup/*"
      ],
      "actions": [
        "gateway:CreateGatewayGroup"
      ],
      "effect": "allow"
    }
  ]
}
```

### Full Resource Access with License Update Restriction[â](#full-resource-access-with-license-update-restriction "Direct link to Full Resource Access with License Update Restriction")

This policy provides a user with broad access to all resources while explicitly denying the ability to update the license. This is another example of the "deny overrides allow" rule and is a common security practice to prevent unauthorized changes to critical system settings like licensing. The `deny` statement ensures that even with full `allow` permissions on everything, the specific `UpdateLicense` action is prohibited.

```
{
  "statement": [
    {
      "resources": [
        "<.*>"
      ],
      "actions": [
        "<.*>"
      ],
      "effect": "allow"
    },
     {
      "resources": [
        "arn:api7:iam:organization/*"
      ],
      "actions": [
        "iam:UpdateLicense"
      ],
      "effect": "deny"
    }   
  ]
}
```

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* [Best Practices: Design Custom Role System](https://docs.api7.ai/best-practices/design-custom-role-system)
* [Roles and Permission Policies](https://docs.api7.ai/key-concepts/roles-and-permission-policies)
