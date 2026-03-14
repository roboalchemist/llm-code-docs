# Source: https://docs.acceldata.io/api/update-roles---permissions.md

# Update Roles & Permissions

Modify existing roles as requirements evolve - add permissions, remove access, refine role definitions.

## Common Update Scenarios

### Scenario 1: Add Permission to Role

Team needs additional capability.

```bash
PUT /authz/api/v1/roles/role-pipeline-creator
{
  "name": "pipeline-creator",
  "description": "Create and manage pipelines",
  "permissions": [
    "pipeline.create",
    "pipeline.edit",
    "pipeline.view",
    "pipeline.execute",
    "pipeline.delete"  // NEW: Added delete permission
  ]
}
```



---

### Scenario 2: Remove Permission from Role

Security tightening - remove risky permission.

```bash
PUT /authz/api/v1/roles/role-data-viewer
{
  "name": "data-viewer",
  "permissions": [
    "pipeline.view",
    "catalog.view"
    // REMOVED: "data.export" - too risky
  ]
}
```



---

### Scenario 3: Rename/Update Description

```bash
PUT /authz/api/v1/roles/role-015
{
  "name": "senior-data-engineer",
  "description": "Senior engineers - can approve deployments",
  "permissions": [...existing...]
}
```



---

## APIs Used

1. `GET /authz/api/v1/roles/:roleId` - Get current role
2. `PUT /authz/api/v1/roles/:roleId` - Update role
3. `GET /authz/api/v1/users/:userId/roles` - Verify changes