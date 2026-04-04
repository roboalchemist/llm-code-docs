# Source: https://docs.acceldata.io/api/manage-role-lifecycle.md

# Manage Role Lifecycle

Systematically create, update, archive, and delete roles as your organization evolves.

---

## Role Lifecycle Stages

### 1. Creation

Use [Create Custom Roles](https://docs.acceldata.io/acceldata-data-observability-cloud/api/create-custom-roles)

### 2. Active Use

- Assign to users/groups
- Monitor usage
- Gather feedback

### 3. Update

Use [Update Roles & Permissions](https://docs.acceldata.io/acceldata-data-observability-cloud/api/update-roles---permissions)

### 4. Deprecation

```bash
# Rename to indicate deprecated
PUT /authz/api/v1/roles/role-old
{
  "name": "DEPRECATED-old-role-name",
  "description": "Deprecated - Use new-role-name instead"
}

# Remove new assignments
# (existing users keep it until migrated)
```



### 5. Migration

```bash
# For each user with old role:
PUT /admin/api/remove-assigned-client-roles
{
  "userId": "user-XXX",
  "roles": ["DEPRECATED-old-role-name"]
}

PUT /admin/api/assign-client-roles
{
  "userId": "user-XXX",
  "roles": ["new-role-name"]
}
```



### 6. Deletion

```bash
# Only after all users migrated
DELETE /authz/api/v1/roles/role-old
```



---

## Role Health Check (Monthly)

```bash
# 1. List all roles
GET /authz/api/v1/roles

# 2. Check usage of each role
GET /authz/api/v1/roles/role-XXX
# Look at assignedTo count

# 3. Identify:
# - Unused roles (0 assignments)
# - Deprecated roles (should be removed)
# - Overlapping roles (consolidate)
```



---

## APIs Used

1. `GET /authz/api/v1/roles` - List roles
2. `POST /authz/api/v1/roles` - Create new
3. `PUT /authz/api/v1/roles/:roleId` - Update existing
4. `DELETE /authz/api/v1/roles/:roleId` - Delete old
5. `PUT /admin/api/assign-client-roles` - Migrate users
6. `PUT /admin/api/remove-assigned-client-roles` - Remove old assignments