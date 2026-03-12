# Source: https://docs.acceldata.io/api/manage-access-changes.md

# Manage Access Changes

Handle day-to-day access changes: promotions, team transfers, temporary access grants, and permission adjustments.

---

## Common Scenarios

### Scenario 1: Promotion to Team Lead

User needs elevated permissions.

```bash
# Add to team lead group
PUT /admin/api/users/user-123/assign-groups
{
  "groupIds": ["group-team-leads"]
}
```



---

### Scenario 2: Team Transfer

User moving from Analytics to Data Engineering.

```bash
# Remove from old group
PUT /admin/api/users/user-123/remove-groups
{
  "groupIds": ["group-analytics"]
}

# Add to new group
PUT /admin/api/users/user-123/assign-groups
{
  "groupIds": ["group-data-engineering"]
}
```



---

### Scenario 3: Temporary Project Access

Grant elevated access for 2 weeks.

```bash
# Add to project group
PUT /admin/api/users/user-123/assign-groups
{
  "groupIds": ["group-migration-project"]
}

# Set calendar reminder to remove after project
```



---

### Scenario 4: Update User Info

Name change, new manager, department transfer.

```bash
PUT /admin/api/users/user-123
{
  "firstName": "Sarah",
  "lastName": "Chen-Martinez",
  "attributes": {
    "manager": ["new-manager@company.com"],
    "department": ["Engineering - Platform"]
  }
}
```



---

## APIs Used

1. `PUT /admin/api/users/:userId` - Update user details
2. `PUT /admin/api/users/:userId/assign-groups` - Add to groups
3. `PUT /admin/api/users/:userId/remove-groups` - Remove from groups
4. `GET /authz/api/v1/users/:userId/roles` - Verify changes