# Source: https://docs.acceldata.io/api/organize-users-into-teams-groups.md

# Organize Users into Teams/Groups

Create and manage groups that organize users by teams, departments, or functions. Groups are how you scale access management - instead of managing 50 individual users, you manage 5 groups.

---

## Real-World Scenario

**Situation**: Your company is creating a new "Customer Analytics" team with 8 people. They need:

- Access to customer data domain
- Ability to create dashboards
- View-only access to production pipelines
- Shared team resources

**Solution**: Create "Customer Analytics" group → Assign roles to group → Add 8 users → Everyone gets consistent access instantly.

---

## Quick Start Workflow

### Step 1: Create the Group

```bash
POST /admin/api/groups
```



**Request:**

```json
{
  "name": "Customer Analytics",
  "attributes": {
    "department": ["Analytics"],
    "manager": ["analytics-lead@company.com"],
    "description": ["Customer-facing analytics and reporting team"]
  }
}
```



**Response:** Save `group-015`

---

### Step 2: Assign Roles to Group

```bash
PUT /admin/api/assign-client-roles
```



**Request:**

```json
{
  "groupId": "group-015",
  "roles": [
    "dashboard-creator",
    "pipeline-viewer",
    "customer-data-viewer"
  ]
}
```



---

### Step 3: Add Users to Group

```bash
PUT /admin/api/users/user-201/assign-groups
```



**Request:**

```json
{
  "groupIds": ["group-015"]
}
```



Repeat for all 8 team members.

---

### Step 4: Verify Group Setup

```bash
GET /admin/api/groups/group-015
```



Check: All users listed, roles assigned, attributes set.

---

## Common Group Patterns

- **By Team**: Data Engineering, Analytics, ML Team 
- **By Function**: Pipeline Admins, Dashboard Viewers, API Developers 
- **By Access Level**: Power Users, Standard Users, Read Only 
- **By Project**: Q1-Launch-Team, Migration-Project-2024 
- **By Environment**: Prod-Access, Dev-Access, Staging-Access

---

## APIs Used

1. `POST /admin/api/groups` - Create group
2. `GET /admin/api/groups` - List groups
3. `GET /admin/api/groups/:groupId` - Get details
4. `PUT /admin/api/groups/:groupId` - Update group
5. `DELETE /admin/api/groups/:groupId` - Delete group
6. `PUT /admin/api/assign-client-roles` - Assign roles to group