# Source: https://docs.acceldata.io/api/implement-least-privilege.md

# Implement Least Privilege

Systematically reduce permissions to the minimum needed, improving security posture.

---

## Least Privilege Implementation

### Step 1: Document Current State

```bash
# Get all users and their permissions
GET /admin/api/users/list
# For each user:
GET /authz/api/v1/users/permissions?userId=XXX
```



---

### Step 2: Interview Teams

**Questions:**

- What do you actually do day-to-day?
- What access do you use regularly?
- What could you lose without impact?
- What access have you never used?

---

### Step 3: Create Minimal Roles

```bash
# Instead of "admin" role, create specific roles:
POST /authz/api/v1/roles
{
  "name": "pipeline-operator",
  "permissions": ["pipeline.view", "pipeline.execute"]  // Not edit, not delete
}
```



---

### Step 4: Migrate Users

```bash
# Remove broad roles
PUT /admin/api/remove-assigned-client-roles
{
  "userId": "user-123",
  "roles": ["admin"]
}

# Add specific roles
PUT /admin/api/assign-client-roles
{
  "userId": "user-123",
  "roles": ["pipeline-operator", "dashboard-viewer"]
}
```



---

### Step 5: Monitor & Adjust

After 1 week, check if users need any access restored.

---

## APIs Used

1. `GET /authz/api/v1/users/permissions` - Current permissions
2. `POST /authz/api/v1/roles` - Create minimal roles
3. `PUT /admin/api/remove-assigned-client-roles` - Remove excess
4. `PUT /admin/api/assign-client-roles` - Add minimal access
5. `GET /authz/api/v1/users/:userId/roles` - Verify changes