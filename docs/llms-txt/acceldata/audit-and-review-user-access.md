# Source: https://docs.acceldata.io/api/audit-and-review-user-access.md

# Audit and Review User Access

Generate comprehensive access reports, identify security risks, ensure compliance, and prepare for audits.

---

## Quarterly Access Review Workflow

### Step 1: Get Complete User List

```bash
GET /admin/api/users/list
```



Export to spreadsheet for review.

---

### Step 2: Check Each User's Access

```bash
# For each user:
GET /authz/api/v1/users/user-XXX/roles
GET /authz/api/v1/users/permissions?userId=user-XXX
```



---

### Step 3: Identify Issues

**Red Flags:**

- Users with no groups (direct role assignments)
- Users with admin access who shouldn't have it
- Inactive users (last login &gt;90 days)
- Contractors with permanent employee access
- Users in too many groups (&gt;5)

---

### Step 4: Generate Report

**Report Template:**

| User | Email | Groups | Roles | Last Login | Issues | 
| ---- | ---- | ---- | ---- | ---- | ---- | 
| user-123 | sarah@... | Data Eng | viewer | 2024-12-05 | OK | 
| user-124 | old@... | 8 groups | admin | 2024-06-01 | Inactive, Too many groups | 


---

### Step 5: Take Action

```bash
# Disable inactive users
PUT /admin/api/users/user-124 {"enabled": false}

# Remove excess groups
PUT /admin/api/users/user-124/remove-groups {...}
```



---

## APIs Used

1. `GET /admin/api/users/list` - All users with details
2. `GET /authz/api/v1/users/:userId/roles` - User roles
3. `GET /authz/api/v1/users/permissions` - Effective permissions
4. `GET /admin/api/users/count` - Total user count