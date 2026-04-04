# Source: https://docs.acceldata.io/api/offboard-a-user.md

# Offboard a User

Securely remove a departing employee's access while maintaining audit trail and preventing disruption to team workflows.

---

## Critical: Security Checklist

### Immediate Actions (Do First)

1. **Disable User Account**

```bash
PUT /admin/api/users/user-123
{
  "enabled": false
}
```



2. **Revoke All API Keys**

```bash
# List user's keys
GET /admin/api/users/user-123/api-keys

# Delete each key
DELETE /admin/api/users/api-keys/AK-abc123
DELETE /admin/api/users/api-keys/AK-def456
```



3. **Remove from All Groups**

```bash
PUT /admin/api/users/user-123/remove-groups
{
  "groupIds": [
    "group-data-eng",
    "group-pipeline-owners",
    "group-prod-access"
  ]
}
```



**Timeline**: Complete within 1 hour of departure notification

---

## Complete Offboarding Workflow

### Step 1: Document Current Access

```bash
# Get full user details
GET /admin/api/users/user-123

# Get roles
GET /authz/api/v1/users/user-123/roles

# Get API keys
GET /admin/api/users/user-123/api-keys
```



**Save this** for audit trail and handover documentation.

---

### Step 2: Disable Account (Don't Delete)

```bash
PUT /admin/api/users/user-123
{
  "enabled": false,
  "attributes": {
    "status": ["OFFBOARDED"],
    "offboardDate": ["2024-12-05"],
    "reason": ["Voluntary - New Job"],
    "handedOffTo": ["replacement@company.com"]
  }
}
```



**Why not delete?**

- Preserves audit history
- Maintains data lineage
- Compliance requirements
- Can reactivate if they return

---

### Step 3: Revoke API Keys

```bash
# Get all keys
GET /admin/api/users/user-123/api-keys

# Revoke each
DELETE /admin/api/users/api-keys/AK-key1
DELETE /admin/api/users/api-keys/AK-key2
```



---

### Step 4: Remove Group Memberships

```bash
PUT /admin/api/users/user-123/remove-groups
{
  "groupIds": ["all", "groups", "user", "was", "in"]
}
```



---

### Step 5: Verify Access Removed

```bash
# Should return empty/minimal permissions
GET /authz/api/v1/users/permissions?userId=user-123

# Should show enabled: false
GET /admin/api/users/user-123
```



---

### Step 6: Update Ownership

Transfer ownership of resources created by departing user:

```bash
# Update pipeline metadata
PUT /torch-pipeline/api/pipelines
{
  "meta": {
    "owner": "replacement@company.com"
  }
}
```



---

## Emergency Offboarding

**If user leaves unexpectedly or security incident:**

```bash
# 1. Immediate disable (2 minutes)
PUT /admin/api/users/user-123 {"enabled": false}

# 2. Mass revoke (5 minutes)
DELETE /admin/api/users/api-keys/AK-* (all keys)

# 3. Group removal (3 minutes)
PUT /admin/api/users/user-123/remove-groups {"groupIds": [...all]}

# Total time: 10 minutes
```



---

## APIs Used

1. `PUT /admin/api/users/:userId` - Disable account
2. `GET /admin/api/users/:userId/api-keys` - List keys
3. `DELETE /admin/api/users/api-keys/:accessKey` - Revoke keys
4. `PUT /admin/api/users/:userId/remove-groups` - Remove access
5. `GET /authz/api/v1/users/permissions` - Verify removal