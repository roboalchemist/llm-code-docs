# Source: https://docs.acceldata.io/api/onboard-a-new-team-member.md

# Onboard a New Team Member

Get a new team member fully set up in ADOC with appropriate access - from sending the invitation email to verifying their permissions work correctly.

---

## Real-World Scenario

**Situation**: Sarah Chen joins your data engineering team on Monday. She needs:

- Access to ADOC for pipeline monitoring
- Ability to view production pipelines (but not edit yet)
- Access to development environment for testing
- Membership in "Data Engineering" team group

**Deadline**: Ready before her 9 AM start time

**Outcome**: Sarah logs in Monday morning, sees her team's pipelines, and can start learning the system.

---

## Prerequisites

- New hire's work email address
- Their team/department name 
- Their manager's name
- Access level needed (viewer, editor, admin)
- Admin credentials for ADOC

---

## Step-by-Step Workflow

### Step 1: Send Invitation Email

Invite the new team member to create their ADOC account.

#### API Call

```bash
POST /admin/api/users/invite-users
```



#### Request

```json
{
  "emails": [
    "sarah.chen@company.com"
  ],
  "groups": ["Data Engineering"],
  "sendEmail": true,
  "customMessage": "Welcome to the Data Engineering team! This invitation gives you access to ADOC, our data observability platform. You'll be able to monitor pipelines, view data catalogs, and collaborate with the team. See you Monday!"
}
```



#### Response

```json
{
  "invitations": [
    {
      "email": "sarah.chen@company.com",
      "status": "SENT",
      "invitationLink": "https://adoc.company.com/accept-invite?token=abc123xyz",
      "expiresAt": "2024-12-12T10:00:00Z"
    }
  ]
}
```



**Checkpoint**: Sarah receives email with invitation link

**Pro Tip**: Send invitations 1-2 days before start date so users can set up accounts on their own schedule.

---

### Step 2: Wait for Account Creation

The new user clicks the invitation link and creates their account by setting a password.

**What happens**:

1. User clicks link in email
2. User sets their password
3. User completes profile (optional)
4. Account is activated

**You'll know it's done**: User will be listed in the system with status "active"

---

### Step 3: Verify User Was Created

Check that the user's account exists and is active.

#### API Call

```bash
GET /admin/api/users/list
```



#### Look for in Response

```json
{
  "users": [
    {
      "id": "user-301",
      "email": "sarah.chen@company.com",
      "firstName": "Sarah",
      "lastName": "Chen",
      "enabled": true,
      "emailVerified": true,
      "groups": ["Data Engineering"]
    }
  ]
}
```



**Checkpoint**: User appears in list with `enabled: true`

**Save this**: `user-301` - you'll need this ID for the next steps!

---

### Step 4: Assign Additional Groups (If Needed)

If Sarah needs access to multiple teams or projects, add her to additional groups.

#### API Call

```bash
PUT /admin/api/users/user-301/assign-groups
```



**Path Parameters:**

| Parameter | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| userId | string | Yes | The user ID from Step 3 (e.g., `user-301`) | 


#### Request

```json
{
  "groupIds": [
    "group-pipeline-viewers",
    "group-dev-environment"
  ]
}
```



#### Response

```json
{
  "success": true,
  "user": {
    "id": "user-301",
    "groups": [
      "Data Engineering",
      "Pipeline Viewers",
      "Dev Environment Access"
    ]
  }
}
```



**Common Additional Groups**:

- Pipeline Viewers - See all pipelines
- Dev Environment - Access development resources
- Dashboard Users - Access to dashboards
- Read Only - View-only across platform

---

### Step 5: Verify Roles Were Assigned

Check that group memberships automatically granted the correct roles.

#### API Call

```bash
GET /authz/api/v1/users/user-301/roles
```



**Path Parameters:**

| Parameter | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| userId | string | Yes | The user ID (e.g., `user-301`) | 


#### Response

```json
{
  "roles": [
    {
      "id": "role-pipeline-viewer",
      "name": "pipeline-viewer",
      "description": "View pipelines and runs",
      "source": "group:Data Engineering"
    },
    {
      "id": "role-catalog-viewer",
      "name": "catalog-viewer",
      "description": "Browse data catalogs",
      "source": "group:Data Engineering"
    }
  ]
}
```



**What to check**:

- User has at least one role
- Roles match their job function
- No excessive permissions (like admin access)

---

### Step 6: Set User Attributes (Metadata)

Add organizational metadata for HR tracking and access reviews.

#### API Call

```bash
PUT /admin/api/users/user-301
```



**Path Parameters:**

| Parameter | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| userId | string | Yes | The user ID (e.g., `user-301`) | 


#### Request

```json
{
  "firstName": "Sarah",
  "lastName": "Chen",
  "email": "sarah.chen@company.com",
  "attributes": {
    "department": ["Engineering"],
    "team": ["Data Engineering"],
    "level": ["Engineer II"],
    "manager": ["john.smith@company.com"],
    "startDate": ["2024-12-09"],
    "location": ["San Francisco"],
    "employeeType": ["Full-Time"]
  }
}
```



**Why this matters**:

- Access reviews: Find all users in a department
- Offboarding: Know who their manager is
- Auditing: Track when access was granted
- Compliance: Employment type affects data access

---

### Step 7: Test Access

Have the user (or you, as admin) test that they can actually access what they need.

#### Test Checklist

```bash
# As the new user, try to:

# 1. View pipelines
GET /torch-pipeline/api/pipelines/summary

# 2. View a specific pipeline
GET /torch-pipeline/api/pipelines/15

# 3. View data catalog (if applicable)
GET /catalog-server/api/datasets

# 4. Cannot create/edit (if they're view-only)
PUT /torch-pipeline/api/pipelines
# Should fail with 403 Forbidden
```



**Success criteria**:

- Can access what they need
- Cannot access what they shouldn't
- No error messages about missing permissions

---

## Complete Onboarding Script

For quick copy-paste onboarding:

```bash
# Step 1: Send invitation
POST /admin/api/users/invite-users
{
  "emails": ["sarah.chen@company.com"],
  "groups": ["Data Engineering"],
  "sendEmail": true
}

# Step 2: Wait for user to accept (check email)

# Step 3: Verify user exists
GET /admin/api/users/list
# Find user ID (e.g., user-301)

# Step 4: Assign additional groups
PUT /admin/api/users/user-301/assign-groups
{
  "groupIds": ["group-pipeline-viewers", "group-dev-access"]
}

# Step 5: Verify roles
GET /authz/api/v1/users/user-301/roles

# Step 6: Set attributes
PUT /admin/api/users/user-301
{
  "attributes": {
    "team": ["Data Engineering"],
    "manager": ["manager@company.com"],
    "startDate": ["2024-12-09"]
  }
}

# Step 7: Test access
GET /authz/api/v1/users/permissions?userId=user-301
```



---

## Common Issues & Solutions

### Issue: Invitation email not received

**Causes**:

- Email in spam folder
- Typo in email address
- Email server delay

**Solutions**:

1. Check spam folder
2. Resend invitation with correct email
3. Manually send invitation link via Slack

---

### Issue: User can't access pipelines

**Causes**:

- Missing group assignment
- Group doesn't have the right role
- Domain/resource restrictions

**Solutions**:

1. Check groups: `GET /admin/api/users/:userId`
2. Check roles: `GET /authz/api/v1/users/:userId/roles`
3. Check permissions: `GET /authz/api/v1/users/permissions?userId=:userId`

---

### Issue: User has too much access

**Causes**:

- Assigned to wrong group
- Group has excessive permissions

**Solutions**:

1. Remove from incorrect groups
2. Review group role assignments
3. Consider creating more granular groups

---

## Bulk Onboarding

**Scenario**: Onboarding 10+ people at once

See [Bulk User Management](https://docs.acceldata.io/acceldata-data-observability-cloud/api/bulk-user-management)  for:

- CSV import workflows
- Batch invitation scripts
- Template-based onboarding
- Automation options

---

## APIs Used

1. `POST /admin/api/users/invite-users` - Send invitation
2. `GET /admin/api/users/list` - Verify user created
3. `PUT /admin/api/users/:userId/assign-groups` - Add to groups
4. `GET /authz/api/v1/users/:userId/roles` - Check roles
5. `PUT /admin/api/users/:userId` - Set attributes