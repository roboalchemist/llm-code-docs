# Source: https://docs.acceldata.io/api/audit-permissions.md

# Audit Permissions

Review who has what permissions, identify over-privileged users, ensure least privilege, prepare for compliance audits.

---

## Permission Audit Workflow

### Step 1: List All Roles

```bash
GET /authz/api/v1/roles
```



Review each role's permissions.

---

### Step 2: Check User Permissions

```bash
# For each user or sample of users:
GET /authz/api/v1/users/user-XXX/roles
GET /authz/api/v1/users/permissions?userId=user-XXX
```



---

### Step 3: Identify Over-Privileged Users

**Red flags:**

- Users with admin roles who shouldn't have them
- Users with write access who only need read
- Contractor with same access as employees
- Users with permissions from multiple conflicting roles

---

### Step 4: Generate Permission Matrix

| User | Roles | Can Create | Can Delete | Can Admin | Review Status | 
| ---- | ---- | ---- | ---- | ---- | ---- | 
| user-123 | viewer | ❌ | ❌ | ❌ | Appropriate | 
| user-124 | admin | ✓ | ✓ | ✓ | Over-privileged | 


---

### Step 5: Remediate Issues

```bash
# Remove excessive roles
PUT /admin/api/remove-assigned-client-roles
{
  "userId": "user-124",
  "roles": ["admin"]
}
```



---

## APIs Used

1. `GET /authz/api/v1/roles` - All roles
2. `GET /authz/api/v1/users/:userId/roles` - User roles
3. `GET /authz/api/v1/users/permissions` - Effective permissions