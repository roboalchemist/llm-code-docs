# Source: https://docs.acceldata.io/api/bulk-user-management.md

# Bulk User Management

Manage multiple users simultaneously - mass invitations, bulk updates, team reorganizations.

---

## Scenario 1: Onboard 20 Contractors

```bash
POST /admin/api/users/invite-users
{
  "emails": [
    "contractor1@company.com",
    "contractor2@company.com",
    ...20 emails...
  ],
  "groups": ["Contractors", "Read-Only-Access"],
  "sendEmail": true
}
```



---

## Scenario 2: Team Reorganization

Split Analytics team into Customer Analytics and Product Analytics.

```bash
# Create new groups
POST /admin/api/groups {"name": "Customer Analytics"}
POST /admin/api/groups {"name": "Product Analytics"}

# Move users
# For each user in old team:
PUT /admin/api/users/user-XXX/remove-groups {"groupIds": ["Analytics"]}
PUT /admin/api/users/user-XXX/assign-groups {"groupIds": ["Customer Analytics"]}
```



---

## Scenario 3: Bulk Attribute Update

Update department for entire team.

```bash
# For each user:
PUT /admin/api/users/user-XXX
{
  "attributes": {
    "department": ["Engineering - Data Platform"]
  }
}
```



**Tip:** Script this with a loop for 50+ users.

---

## APIs Used

1. `POST /admin/api/users/invite-users` - Batch invitations
2. `GET /admin/api/users/list` - Get users to update
3. `PUT /admin/api/users/:userId/assign-groups` - Bulk group changes
4. `PUT /admin/api/users/:userId/remove-groups` - Bulk removals
5. `PUT /admin/api/users/:userId` - Bulk attribute updates