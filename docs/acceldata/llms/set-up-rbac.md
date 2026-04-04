# Source: https://docs.acceldata.io/api/set-up-rbac.md

# Set Up RBAC (Role-Based Access Control)

Implement a complete role-based access control framework from scratch - defining roles, assigning permissions, and establishing access patterns.

---

## RBAC Implementation Roadmap

### Phase 1: Plan Your Roles

**Document needed roles:**

- Admin roles (platform-admin, team-lead)
- Creator roles (pipeline-creator, dashboard-creator)
- Editor roles (data-editor, catalog-editor)
- Viewer roles (pipeline-viewer, data-viewer)

---

### Phase 2: Get Available Permissions

```bash
GET /authz/api/v1/roles/template
```



**Returns:** All available permissions in ADOC

---

### Phase 3: Create Roles

```bash
# Platform Admin (full access)
POST /authz/api/v1/roles
{
  "name": "platform-admin",
  "description": "Full platform administration",
  "permissions": ["*"]
}

# Pipeline Creator (create & manage pipelines)
POST /authz/api/v1/roles
{
  "name": "pipeline-creator",
  "description": "Create and manage pipelines",
  "permissions": [
    "pipeline.create",
    "pipeline.edit",
    "pipeline.view",
    "pipeline.execute"
  ]
}

# Data Viewer (read-only)
POST /authz/api/v1/roles
{
  "name": "data-viewer",
  "description": "View-only access to data",
  "permissions": [
    "pipeline.view",
    "catalog.view",
    "dashboard.view"
  ]
}
```



---

### Phase 4: Assign Roles to Groups

```bash
# Data Engineering gets creator access
PUT /admin/api/assign-client-roles
{
  "groupId": "group-data-eng",
  "roles": ["pipeline-creator", "catalog-editor"]
}

# Analytics gets viewer access
PUT /admin/api/assign-client-roles
{
  "groupId": "group-analytics",
  "roles": ["data-viewer", "dashboard-creator"]
}
```



---

### Phase 5: Test & Verify

```bash
# Test each role
GET /authz/api/v1/users/test-user/roles
GET /authz/api/v1/users/permissions?userId=test-user

# Verify users can access what they need
# Verify users cannot access what they shouldn't
```



---

## APIs Used

1. `GET /authz/api/v1/roles/template` - Available permissions
2. `POST /authz/api/v1/roles` - Create roles
3. `GET /authz/api/v1/roles` - List all roles
4. `PUT /admin/api/assign-client-roles` - Assign to groups/users
5. `GET /authz/api/v1/users/:userId/roles` - Verify assignments