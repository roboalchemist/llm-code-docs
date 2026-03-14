# Source: https://docs.acceldata.io/api/user-authentication.md

# User Authentication

Authentication answers the fundamental question: **"Who are you?"**

It's the process of verifying identity and managing user accounts in your ADOC platform. Think of it as the front door to your data observability system - it controls who can walk through that door.

---

## Why Authentication Matters

### Security Foundation

Authentication is your first line of defense. Without proper user management:

- You don't know who accessed what
- You can't revoke access when someone leaves
- You have no audit trail for compliance
- Security breaches go undetected

### Operational Efficiency

Good authentication practices mean:

- New hires get access on day one
- Team reorganizations happen smoothly
- API keys enable automation
- Access reviews take minutes, not days

### Compliance Requirements

Most regulations require you to:

- Track who has access to sensitive data
- Remove access when people leave
- Regularly review and audit access
- Document access decisions

---

## Authentication in ADOC: The Building Blocks

### 1. Users

Individual people who access ADOC.

**Key Concepts:**

- Each user has a unique identity (email address)
- Users authenticate with username/password or SSO
- User accounts can be enabled or disabled
- Users are assigned to groups for access management

**Example:** Sarah Chen (sarah.chen@company.com) - Data Engineer

---

### 2. Groups

Collections of users organized by team, department, or function.

**Key Concepts:**

- Groups organize users at scale
- Permissions are assigned to groups, not individual users
- Users can belong to multiple groups
- Groups align with your organizational structure

**Example:** "Data Engineering" group contains all data engineers

---

### 3. API Keys

Credentials for programmatic access (scripts, CI/CD, integrations).

**Key Concepts:**

- API keys enable automation without using personal credentials
- Each key has an access key and secret key pair
- Keys can be revoked independently
- Keys should have expiration dates

**Example:** CI/CD pipeline uses API key to deploy pipelines automatically

---

## The Authentication Flow

```none
1. INVITATION
   Admin sends invitation email
   ↓
2. ACCOUNT CREATION
   User clicks link, sets password
   ↓
3. GROUP ASSIGNMENT
   Admin adds user to appropriate groups
   ↓
4. ACCESS GRANTED
   User can now log in and access ADOC
   ↓
5. ONGOING MANAGEMENT
   Update access as roles change
   ↓
6. OFFBOARDING
   Disable account and revoke API keys when user leaves
```



---

## Real-World Example: Sarah's Journey

### Day 1: Onboarding

**Monday Morning - 9:00 AM**

Sarah Chen joins your data engineering team.

**Admin actions** (5 minutes):

1. Send invitation to **sarah.chen@company.com**
2. Assign to "Data Engineering" group
3. Verify she can log in
4. Set attributes (team, manager, start date)

**Result:** Sarah logs in at 9:15 AM, sees her team's pipelines, starts working.

---

### Week 1-12: Active Use

**Daily Operations**

Sarah uses ADOC every day:

- Views pipeline execution status
- Investigates failed runs
- Creates new data pipelines
- Collaborates with team

**Admin actions:** Minimal (groups manage permissions automatically)

---

### Month 6: Promotion

**Sarah Becomes Team Lead**

**Admin actions** (2 minutes):

1. Add Sarah to "Team Leads" group
2. Sarah now has approval permissions
3. Update attributes (level: Senior Engineer)

**Result:** Sarah's access automatically elevated based on group membership.

---

### Month 18: Departure

**Sarah Accepts Job at Another Company**

**Admin actions** (10 minutes):

1. Disable Sarah's account immediately
2. Revoke all API keys
3. Remove from all groups
4. Document in audit log
5. Transfer resource ownership

**Result:** Sarah's access removed within 1 hour of notification. Complete audit trail maintained for compliance.

---

## Common Authentication Tasks

| Task | When You Do It | 
| ---- | ---- | 
| [Onboard a New Team Member](https://docs.acceldata.io/acceldata-data-observability-cloud/api/onboard-a-new-team-member) | New hire starts | 
| [Organize Users into Teams/Groups](https://docs.acceldata.io/acceldata-data-observability-cloud/api/organize-users-into-teams-groups) | New team forms | 
| [Manage Access Changes](https://docs.acceldata.io/acceldata-data-observability-cloud/api/manage-access-changes) | Promotions, transfers | 
| [Offboard a User](https://docs.acceldata.io/acceldata-data-observability-cloud/api/offboard-a-user) | Employee leaves | 
| [Audit and Review User Access](https://docs.acceldata.io/acceldata-data-observability-cloud/api/audit-and-review-user-access) | Quarterly reviews | 
| [Bulk User Management](https://docs.acceldata.io/acceldata-data-observability-cloud/api/bulk-user-management) | Mass onboarding | 


---

## Authentication Best Practices

### Do's

**User Management:**

- Onboard users 1-2 days before start date
- Use consistent naming conventions (**first.last@company.com)**
- Set attributes for HR tracking (manager, department, start date)
- Test access before announcing it's ready

**Group Management:**

- Organize by job function, not by person
- Keep groups aligned with org structure
- Use descriptive names (Data Engineering, not Group1)
- Limit to 20-30 groups for most organizations

**API Keys:**

- Use service accounts for automation (not personal keys)
- Set expiration dates on all keys
- Rotate keys every 90 days
- Store in secret management systems

**Offboarding:**

- Disable accounts immediately (don't delete)
- Revoke API keys separately
- Document offboarding in attributes
- Preserve accounts for audit trail

---

### Don'ts

**Common Mistakes:**

- Don't assign permissions to individual users (use groups!)
- Don't share API keys across systems
- Don't delete user accounts (disable instead)
- Don't skip setting user attributes
- Don't forget to revoke API keys during offboarding
- Don't create groups for individuals
- Don't let API keys live forever without expiration

---

## Authentication Metrics to Track

### Health Metrics

- **Active Users**: Currently enabled accounts
- **Inactive Users**: No login in &gt;90 days (offboard candidates)
- **Users Without Groups**: Over-permissioned users (security risk)
- **API Keys**: Total keys, expired keys, unused keys

### Operational Metrics

- **Average Onboarding Time**: Target &lt;10 minutes
- **Access Request Turnaround**: Target &lt;1 day
- **Offboarding Completion**: Target &lt;1 hour from notification

### Compliance Metrics

- **Access Review Frequency**: Quarterly recommended
- **Orphaned Accounts**: Users whose manager left
- **Stale API Keys**: Keys &gt;90 days old
- **Audit Coverage**: % of users reviewed

---

## Authentication vs Authorization

**Important:** Authentication and Authorization work together but serve different purposes:

| Authentication (Who) | Authorization (What) | 
| ---- | ---- | 
| Who are you? | What can you do? | 
| Verifies identity | Grants permissions | 
| Users, Groups, API Keys | Roles, Domains, Resources | 
| "Sarah is a data engineer" | "Data engineers can create pipelines" | 


---

## Common Questions

### Q: Should I create a group for each user?

**A:** No! Groups are for shared access. If only one person needs specific access, assign a role directly (but this should be rare).

### Q: What happens to a user's data when I disable their account?

**A:** Nothing! Pipelines they created continue running. Only their ability to log in is removed. This is why we disable instead of delete.

### Q: How do I know if someone needs access?

**A:** Follow these guidelines:

- Manager approval required
- Access based on job function
- Least privilege by default
- Time-bound for contractors

### Q: Can a user belong to multiple groups?

**A:** Yes! This is normal. For example, Sarah might be in "Data Engineering" (her team) and "Pipeline Owners" (her function).

### Q: How often should I audit access?

**A:** Quarterly for most organizations. More frequently for highly regulated industries or high-turnover teams.