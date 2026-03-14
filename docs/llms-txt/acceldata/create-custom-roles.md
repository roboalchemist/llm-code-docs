# Source: https://docs.acceldata.io/api/create-custom-roles.md

# Create Custom Roles

Design and create custom roles tailored to your organization's specific needs.

---

## Role Design Process

### Step 1: Identify Need

**Questions to ask:**

- What job function needs access?
- What should they be able to do?
- What should they NOT be able to do?
- Is this temporary or permanent?

---

### Step 2: Get Permission Template

```bash
GET /authz/api/v1/roles/template
```



Review available permissions.

---

### Step 3: Create Role

```bash
POST /authz/api/v1/roles
```



**Example: Dashboard Editor**

```json
{
  "name": "dashboard-editor",
  "description": "Can create and edit dashboards but not publish to production",
  "permissions": [
    "dashboard.create",
    "dashboard.edit",
    "dashboard.view",
    "catalog.view"
  ]
}
```



**Example: Pipeline Monitor**

```json
{
  "name": "pipeline-monitor",
  "description": "View pipelines and runs, can trigger manual runs",
  "permissions": [
    "pipeline.view",
    "pipeline.execute",
    "pipeline.run.view"
  ]
}
```



---

### Step 4: Test Role

```bash
# Assign to test user
PUT /admin/api/assign-client-roles
{
  "userId": "test-user",
  "roles": ["dashboard-editor"]
}

# Verify permissions
GET /authz/api/v1/users/permissions?userId=test-user
```



---

### Step 5: Deploy to Production

```bash
# Assign to appropriate groups
PUT /admin/api/assign-client-roles
{
  "groupId": "group-dashboard-team",
  "roles": ["dashboard-editor"]
}
```



---

## Common Custom Roles

**Auditor Role:**

```json
{
  "name": "auditor",
  "permissions": ["*.view", "audit.read", "log.read"]
}
```



**Data Steward:**

```json
{
  "name": "data-steward",
  "permissions": ["catalog.certify", "catalog.tag", "metadata.edit"]
}
```



**Pipeline Operator:**

```json
{
  "name": "pipeline-operator",
  "permissions": ["pipeline.view", "pipeline.execute", "pipeline.monitor"]
}
```



---

## APIs Used

1. `GET /authz/api/v1/roles/template` - Get permissions
2. `POST /authz/api/v1/roles` - Create role
3. `GET /authz/api/v1/roles/:roleId` - View role details
4. `PUT /admin/api/assign-client-roles` - Assign role