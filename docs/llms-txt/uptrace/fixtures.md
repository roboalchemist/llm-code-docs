# Source: https://uptrace.dev/raw/features/fixtures.md

# Using fixtures to sync data into Uptrace

> Define YAML or JSON fixtures that sync users, organizations, projects, and tokens so every Uptrace environment can be bootstrapped consistently.

## Overview

Data fixtures provide a powerful way to programmatically create and manage users, organizations, and projects in Uptrace using YAML or JSON configuration files. This feature is particularly valuable for:

- **Environment bootstrapping**: Quickly set up development, staging, or testing environments
- **Automation workflows**: Integrate user and project creation into CI/CD pipelines
- **Bulk operations**: Avoid repetitive manual creation of similar resources
- **Configuration as code**: Version control your Uptrace setup alongside your application code

Fixtures leverage a unique `key` field that enables Uptrace to intelligently create, update, and delete resources while maintaining relationships and avoiding duplicates.

## Key Concepts

### The Key System

The `key` field serves as a stable, user-defined identifier that allows Uptrace to:

- **Track resources** across multiple fixture operations
- **Update existing resources** instead of creating duplicates
- **Establish relationships** between different resource types
- **Enable idempotent operations** - running the same fixture multiple times produces the same result

**Important**: Keys are case-sensitive and must be unique within each resource type.

### Supported Resource Types

- **Users**: Individual user accounts with authentication credentials
- **User Tokens**: API tokens for programmatic access
- **Organizations**: Top-level containers for projects and users
- **Organization Users**: User membership and roles within organizations
- **Projects**: Individual monitoring projects within organizations
- **Project Tokens**: API tokens scoped to specific projects
- **Project Users**: User permissions within specific projects

## Configuration Methods

### YAML Configuration (Self-hosted Only)

For self-hosted Uptrace instances, you can define fixtures directly in your configuration file:

```yaml
seed_data:
  users:
    - key: admin_user
      name: System Administrator
      email: admin@company.com
      password: change_me_immediately # TODO: Update in production!
    - key: developer_user
      name: John Developer
      email: john@company.com
      password: dev_password

  orgs:
    - key: main_org
      name: Acme Corporation
    - key: dev_org
      name: Development Team

  org_users:
    - key: admin_membership
      org: main_org      # References org.key above
      user: admin_user   # References user.key above
      role: owner
    - key: dev_membership
      org: dev_org
      user: developer_user
      role: member

  projects:
    - key: web_app_project
      name: Web Application
      org: main_org      # References org.key above
    - key: api_project
      name: REST API
      org: main_org
```

### JSON API (Cloud & Self-hosted)

Both cloud and self-hosted instances support the JSON API for dynamic fixture management.

## Authentication

### Obtaining an Auth Token

1. Navigate to your Uptrace user profile page
2. Look for the "Auth tokens" section
3. Click "Create token" or similar button
4. Copy the generated auth token immediately
5. Store the token securely - treat it like a password

**Security Note**: The auth token inherits all permissions from your user account. Use dedicated service accounts with minimal required permissions for production automation.

### Using Authentication Headers

Include your user token in API requests using the Bearer token format:

```text
Authorization: Bearer <your_user_token>
```

## Syncing Fixtures via API

### Basic Sync Request

```bash
curl https://api.uptrace.dev/api/v1/fixtures \
  --request PUT \
  --header "Authorization: Bearer <user_token>" \
  --header "Content-Type: application/json" \
  --data @fixtures.json
```

### Response Handling

The API returns:

- **200 OK**: Fixtures applied successfully
- **400 Bad Request**: Invalid JSON structure or missing required fields
- **401 Unauthorized**: Invalid or missing authentication token
- **403 Forbidden**: Insufficient permissions for requested operations

## Complete Data Structure Reference

### Full JSON Schema

```json
{
  "users": [
    {
      "key": "user1",               // Required: Unique identifier
      "name": "Display Name",       // Required: User's display name
      "email": "user@example.com",  // Required: Must be valid email format
      "password": "secure_password" // Required: Plain text (hashed by Uptrace)
    }
  ],
  "userTokens": [
    {
      "key": "token1",           // Required: Unique identifier
      "userKey": "user1",        // Required: References user.key
      "token": "api_token",      // Required: The actual token value
      "name": "CI/CD Token"      // Optional: Human-readable token name
    }
  ],
  "orgs": [
    {
      "key": "org1",            // Required: Unique identifier
      "name": "Organization",   // Required: Organization display name
      "description": "Org desc" // Optional: Organization description
    }
  ],
  "orgUsers": [
    {
      "key": "org_user1",    // Required: Unique identifier
      "orgKey": "org1",      // Required: References org.key
      "userKey": "user1",    // Required: References user.key
      "role": "owner"        // Required: owner, admin, viewer, member, collaborator, billing-manager
    }
  ],
  "projects": [
    {
      "key": "project1",                   // Required: Unique identifier
      "name": "Project Name",              // Required: Project display name
      "orgKey": "org1",                    // Required: References org.key
      "description": "Project description" // Optional
    }
  ],
  "projectTokens": [
    {
      "key": "proj_token1",      // Required: Unique identifier
      "projectKey": "project1",  // Required: References project.key
      "token": "project_secret", // Required: The actual token value
      "name": "Production Token" // Optional: Human-readable token name
    }
  ],
  "projectUsers": [
    {
      "key": "proj_user1",       // Required: Unique identifier
      "projectKey": "project1",  // Required: References project.key
      "orgUserKey": "org_user1", // Required: References orgUsers.key
      "permLevel": "admin"       // Required: admin, maintain, view, none
    }
  ]
}
```

### Role and Permission Levels

**Organization Roles:**

- `owner`: Has full administrative access to the entire organization.
- `admin`: Can view and admin any project in the org. Can create new projects.
- `viewer`: Can view any project in the org. Can create new projects.
- `member`: Can access projects in the org. Can create new projects.
- `collaborator`: Can access individual projects. Can't create new projects.
- `billing_manager`: Can manage billing details. Can create new projects.

**Project Permission Levels:**

- `admin`: Can view project data, configure alerting rules and project settings.
- `maintain`: Can view project data and configure alerting rules.
- `view`: Can view project.
- `none`: No permissions. Forbids access.

## Working with Existing Resources

### The Binding API

When you need to reference resources created through the Uptrace UI in your fixtures, use the binding API to assign keys to existing resources.

```bash
curl https://api.uptrace.dev/api/v1/fixtures/bindings \
  --request PUT \
  --header "Authorization: Bearer <user_token>" \
  --header "Content-Type: application/json" \
  --data '{
    "orgs": [
      {"id": 123, "key": "legacy_org"}
    ],
    "projects": [
      {"id": 456, "key": "existing_project"}
    ]
  }'
```

### Finding Resource IDs

To find the numeric IDs of existing resources:

1. **Via UI**: Check the URL when viewing a resource (e.g., `/orgs/123`)
2. **Via API**: Use the respective GET endpoints:```bash
# List organizations
curl https://api.uptrace.dev/internal/v1/orgs \
  --header "Authorization: Bearer <user_token>"

# List projects
curl https://api.uptrace.dev/internal/v1/projects \
  --header "Authorization: Bearer <user_token>"
```

### Supported Binding Models

```json
{
  "orgs": [{"id": 1, "key": "key1"}],
  "orgUsers": [{"id": 1, "key": "key1"}],
  "projects": [{"id": 1, "key": "key1"}],
  "projectTokens": [{"id": 1, "key": "key1"}]
}
```

## Practical Examples

### Development Team Setup

```json
{
  "users": [
    {
      "key": "tech_lead",
      "name": "Alice Johnson",
      "email": "alice@company.com",
      "password": "temp_password_123"
    },
    {
      "key": "backend_dev",
      "name": "Bob Smith",
      "email": "bob@company.com",
      "password": "temp_password_456"
    }
  ],
  "orgs": [
    {
      "key": "engineering",
      "name": "Engineering Team",
      "description": "All engineering projects and monitoring"
    }
  ],
  "orgUsers": [
    {
      "key": "alice_eng",
      "orgKey": "engineering",
      "userKey": "tech_lead",
      "role": "admin"
    },
    {
      "key": "bob_eng",
      "orgKey": "engineering",
      "userKey": "backend_dev",
      "role": "member"
    }
  ],
  "projects": [
    {
      "key": "user_service",
      "name": "User Service",
      "orgKey": "engineering",
      "description": "User authentication and profile management"
    },
    {
      "key": "payment_service",
      "name": "Payment Service",
      "orgKey": "engineering",
      "description": "Payment processing and billing"
    }
  ],
  "projectTokens": [
    {
      "key": "user_service_prod",
      "projectKey": "user_service",
      "token": "us_prod_abc123xyz789",
      "name": "Production Environment"
    }
  ]
}
```

### Multi-Environment Setup

```json
{
  "orgs": [
    {
      "key": "company_prod",
      "name": "Production Environment"
    },
    {
      "key": "company_staging",
      "name": "Staging Environment"
    }
  ],
  "projects": [
    {
      "key": "app_prod",
      "name": "Main Application",
      "orgKey": "company_prod"
    },
    {
      "key": "app_staging",
      "name": "Main Application",
      "orgKey": "company_staging"
    }
  ]
}
```

## Best Practices

### Security Guidelines

- **Never commit passwords**: Use placeholder values in version control
- **Rotate tokens regularly**: Especially for production environments
- **Use environment variables**: For sensitive values in automation scripts
- **Principle of least privilege**: Create service accounts with minimal required permissions

### Key Naming Conventions

- **Use descriptive names**: `web_app_prod_token` vs `token1`
- **Include environment**: `user_staging`, `project_prod`
- **Be consistent**: Choose a naming pattern and stick to it
- **Avoid special characters**: Stick to alphanumeric and underscores

## Troubleshooting

### Common Issues

**"Key already exists" errors:**

- This is usually not an error - Uptrace updates existing resources with matching keys
- Ensure key uniqueness within each resource type

**Reference errors (e.g., "org not found"):**

- Verify that referenced keys exist in the same fixture or were previously created
- Check for typos in key references
- Ensure proper dependency order in your fixtures

**Permission denied:**

- Verify your user token is correct and has sufficient permissions
- Check that you're referencing the correct API endpoint for your instance

**Invalid JSON structure:**

- Validate your JSON using a JSON validator
- Ensure all required fields are present
- Check for trailing commas or syntax errors

### Validation Tips

```bash
# Validate JSON before sending
cat fixtures.json | jq empty && echo "Valid JSON" || echo "Invalid JSON"

# Test with a minimal fixture first
curl https://api.uptrace.dev/api/v1/fixtures \
  --request PUT \
  --header "Authorization: Bearer <user_token>" \
  --header "Content-Type: application/json" \
  --data '{"orgs": [{"key": "test_org", "name": "Test"}]}'
```

## Limitations and Considerations

- **UI-created resources**: Cannot be referenced in fixtures without first using the binding API
- **Rate limiting**: API calls are subject to standard rate limits
- **Passwords**: Stored in plain text in fixtures, hashed by Uptrace upon creation

## FAQ

**Q: Can I update existing resources using fixtures?**<br />


A: Yes, if a resource with the same key already exists, Uptrace will update it with the new values from your fixture.

**Q: What happens if I reference a key that doesn't exist?**<br />


A: The API will return an error indicating that the referenced resource was not found. Ensure all referenced keys exist in the same fixture.

**Q: Can I use fixtures to delete resources?**<br />


A: Yes, if a resource with the assigned key is removed from the fixture, it is automatically deleted.

**Q: How do I migrate from manual setup to fixtures?**<br />


A: Use the binding API to assign keys to your existing resources, then create fixtures that reference those keys for future modifications.

**Q: Are there any limits on the number of resources in a single fixture?**<br />


A: While there's no hard limit, very large fixtures may timeout. Consider splitting large datasets into smaller batches if you encounter issues.
