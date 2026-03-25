# Source: https://docs.acceldata.io/api/user-authorization.md

# User Authorization

Authorization answers the critical question: **"What can you do?"**

Once we know who you are (Authentication), authorization determines what you're allowed to access and what actions you can perform. It's the difference between opening the front door and deciding which rooms you can enter.

---

## Why Authorization Matters

### Security by Design

Without proper authorization:

- Everyone can delete production pipelines
- Junior engineers can modify critical data
- Contractors have same access as employees
- No separation of duties

### Compliance & Governance

Authorization enables you to:

- Enforce least privilege principle
- Separate duties (who creates vs. who approves)
- Control access to sensitive data
- Audit who can do what

### Operational Safety

Proper authorization prevents:

- Accidental deletions by inexperienced users
- Unauthorized changes to production
- Data breaches through over-permissioned accounts
- Compliance violations

---

## Authorization in ADOC: The Building Blocks

### 1. Roles

Named collections of permissions that define what actions users can perform.

**Key Concepts:**

- Roles contain permissions (pipeline.create, catalog.view, etc.)
- Users get roles through group membership
- Roles are reusable across multiple users
- Custom roles can be created for specific needs

**Example:** "pipeline-creator" role contains permissions to create, edit, and view pipelines

---

### 2. Permissions

Individual capabilities to perform specific actions.

**Key Concepts:**

- Format: `resource.action` (e.g., pipeline.create, catalog.edit)
- Permissions are granted through roles
- Fine-grained control over every action
- Can be combined for custom access patterns

**Example:**

- `pipeline.create` - Can create new pipelines
- `pipeline.view` - Can view pipelines
- `pipeline.delete` - Can delete pipelines

---

### 3. Domains

Logical boundaries for data governance and access control.

**Key Concepts:**

- Organize data assets by business function
- Domain-level access control
- Clear data ownership
- Supports data mesh architecture

**Example:** "Customer Data" domain contains all customer-related datasets and pipelines

---

### 4. Resource Groups

Collections of ADOC resources for bulk management.

**Key Concepts:**

- Group pipelines, connections, datasets
- Environment separation (Dev, Staging, Prod)
- Team-based organization
- Simplify bulk access grants

**Example:** "Production Resources" group contains all prod pipelines and connections

---

## How Authorization Works

```none
USER IDENTITY (Authentication)
     ↓
BELONGS TO → GROUPS
     ↓
GROUPS HAVE → ROLES
     ↓
ROLES CONTAIN → PERMISSIONS
     ↓
PERMISSIONS GRANT → ACCESS TO RESOURCES
     ↓
RESOURCES ORGANIZED IN → DOMAINS & RESOURCE GROUPS
```



---

## Real-World Example: Three Users, Different Access

### Sarah - Senior Data Engineer

**Groups:**

- Data Engineering
- Pipeline Owners
- Production Access

**Roles (from groups):**

- pipeline-creator
- catalog-editor
- dashboard-publisher

**What Sarah Can Do:**

- Create pipelines
- Edit data catalogs
- Publish dashboards
- Access production environment
- Execute pipeline runs
- Cannot delete users
- Cannot modify permissions

---

### Mike - Data Analyst

**Groups:**

- Analytics Team
- Dashboard Users

**Roles (from groups):**

- pipeline-viewer
- catalog-viewer
- dashboard-creator

**What Mike Can Do:**

- View all pipelines
- Browse data catalogs
- Create dashboards
- Run reports
- Cannot create pipelines
- Cannot modify data
- Cannot access production

---

### Alex - Platform Administrator

**Groups:**

- Platform Admins

**Roles (from groups):**

- platform-admin (all permissions)

**What Alex Can Do:**

- Everything Sarah can do
- Everything Mike can do
- Plus: Manage users
- Plus: Assign roles
- Plus: Configure system
- Plus: Delete resources

---

## The Authorization Hierarchy

### Permission Inheritance

```none
DOMAINS (Highest Level)
  ↓ "Finance Domain"
  ├── Contains datasets
  ├── Contains pipelines
  └── Domain-level access control
      ↓
RESOURCE GROUPS (Mid Level)
  ↓ "Production Pipelines"
  ├── Pipelines 1-50
  └── Group-level access
      ↓
INDIVIDUAL RESOURCES (Lowest Level)
  ↓ "Customer ETL Pipeline"
  └── Resource-specific permissions
```



**Access Rule:** User needs permission at ANY level to access a resource.

---

## Common Authorization Patterns

### Pattern 1: Role-Based (Most Common)

```none
Data Engineering Group
  ↓ assigned
pipeline-creator Role
  ↓ contains
[pipeline.create, pipeline.edit, pipeline.view]
  ↓ grants access to
All Pipelines
```



**Use when:** Standard team-based access

---

### Pattern 2: Domain-Based (Data Governance)

```none
Finance Domain
  ↓ contains
Financial Datasets & Pipelines
  ↓ accessible by
Finance Team + Auditors
  ↓ not accessible by
Marketing Team
```



**Use when:** Need strict data boundaries

---

### Pattern 3: Environment-Based (DevOps)

```none
Production Resource Group
  ↓ contains
Prod Pipelines + Connections
  ↓ accessible by
Senior Engineers Only
  ↓ not accessible by
Junior Engineers
```



**Use when:** Separate dev/staging/prod access

---

### Pattern 4: Least Privilege (Security)

```none
New User
  ↓ starts with
View-Only Access
  ↓ graduates to
Standard Access
  ↓ eventually
Elevated Access (if needed)
```



**Use when:** Security is critical

---

## Authorization Tasks

| Task | When You Do It | Time Required | 
| ---- | ---- | ---- | 
| [Set Up RBAC (Role-Based Access Control)](https://docs.acceldata.io/acceldata-data-observability-cloud/api/set-up-rbac) | Initial implementation | 2 hours | 
| [Create Custom Roles](https://docs.acceldata.io/acceldata-data-observability-cloud/api/create-custom-roles) | Need specific access pattern | 30 minutes | 
| [Update Roles & Permissions](https://docs.acceldata.io/acceldata-data-observability-cloud/api/update-roles---permissions) | Requirements change | 15 minutes | 
| [Audit Permissions](https://docs.acceldata.io/acceldata-data-observability-cloud/api/audit-permissions) | Regular security review | 45 minutes | 
| [Implement Least Privilege](https://docs.acceldata.io/acceldata-data-observability-cloud/api/implement-least-privilege) | Security hardening | 1 hour/team | 
| [Manage Role Lifecycle](https://docs.acceldata.io/acceldata-data-observability-cloud/api/manage-role-lifecycle) | Ongoing maintenance | Ongoing | 


---

## Authorization Best Practices

### Do's

**Role Design:**

- Create roles by job function, not by person
- Use descriptive names (pipeline-creator, not role1)
- Start with minimal permissions, add as needed
- Document what each role is for
- Regular review and cleanup

**Permission Management:**

- Follow least privilege principle
- Grant access through roles, not direct permissions
- Use groups to assign roles (not individual users)
- Test new roles in non-prod first
- Avoid wildcard permissions (*) unless necessary

**Domain Organization:**

- Align domains with business structure
- Assign clear domain owners
- Document domain boundaries
- Plan for cross-domain use cases
- Start with 3-7 domains, evolve

**Resource Groups:**

- Use consistent naming conventions
- Separate by environment (Dev/Staging/Prod)
- Align with organizational structure
- Limit resources per group (max 100)
- Regular cleanup of unused groups

---

### Don'ts

**Common Mistakes:**

- Don't assign admin role to everyone "just in case"
- Don't create a role for each individual user
- Don't grant permissions directly to users (use roles!)
- Don't use generic role names (role1, role2)
- Don't forget to test roles before deploying
- Don't skip documentation
- Don't leave deprecated roles active

---

## Permission Naming Convention

### Format: `resource.action`

**Resources:**

- `pipeline` - Data pipelines
- `catalog` - Data catalogs
- `dashboard` - Dashboards and reports
- `user` - User management
- `role` - Role management
- `domain` - Domain management

**Actions:**

- `create` - Create new resources
- `view` - Read/view resources
- `edit` - Modify existing resources
- `delete` - Remove resources
- `execute` - Run/execute resources
- `manage` - Full administrative control
- `*` - All actions (use sparingly!)

**Examples:**

- `pipeline.create` - Create new pipelines
- `catalog.view` - Browse data catalogs
- `dashboard.edit` - Modify dashboards
- `user.manage` - Full user management
- `pipeline.*` - All pipeline permissions

---

## Authorization Maturity Model

### Level 1: Basic (Everyone is Admin)

- All users have admin access
- No separation of duties
- High security risk
- No compliance readiness

**Action:** Start with [Set Up RBAC (Role-Based Access Control)](https://docs.acceldata.io/acceldata-data-observability-cloud/api/set-up-rbac)

---

### Level 2: Role-Based (Most Organizations)

- Roles defined by job function
- Users assigned to groups
- Groups have appropriate roles
- Basic audit capability

**Action:** [Create Custom Roles](https://docs.acceldata.io/acceldata-data-observability-cloud/api/create-custom-roles) for your needs

---

### Level 3: Least Privilege (Security Focused)

- Minimal permissions by default
- Justification required for elevated access
- Regular permission audits
- Temporary access patterns

**Action:** [Implement Least Privilege](https://docs.acceldata.io/acceldata-data-observability-cloud/api/implement-least-privilege)

---

### Level 4: Advanced Governance (Enterprise)

- Domain-based access control
- Resource group organization
- Automated compliance reporting
- Self-service within boundaries

**Action:** Implement Domains & Resource Groups

---

## Security Principles

### Principle 1: Least Privilege

**Definition:** Users get minimum access needed to do their job.

**Example:**

- Bad: All engineers have admin access
- Good: Engineers have edit access to their projects

---

### Principle 2: Separation of Duties

**Definition:** No single person can complete high-risk actions alone.

**Example:**

- Bad: Same person creates and approves pipeline deployments
- Good: Junior creates, senior approves

---

### Principle 3: Defense in Depth

**Definition:** Multiple layers of access control.

**Example:**

- Layer 1: User authentication
- Layer 2: Group membership
- Layer 3: Role permissions
- Layer 4: Domain boundaries
- Layer 5: Resource-level controls

---

### Principle 4: Regular Review

**Definition:** Access permissions should be reviewed periodically.

**Example:**

- Quarterly: Review all user permissions
- Monthly: Check for over-privileged accounts
- Weekly: Monitor permission changes

---

## Authorization vs Authentication

**Remember:** These work together but are different:

| Authentication | Authorization | 
| ---- | ---- | 
| Who are you? | What can you do? | 
| Login credentials | Permissions and roles | 
| Users, Groups, API Keys | Roles, Domains, Resources | 
| Verifies identity | Grants access | 
| "Sarah Chen, Data Engineer" | "Can create pipelines" | 


**Both Required:** You can't have authorization without authentication!

---

Common Questions

### Q: What's the difference between a role and a group?

**A:**

- **Group** = Collection of users (WHO)
- **Role** = Collection of permissions (WHAT)
- Groups are assigned roles
- Users inherit permissions from their group's roles

### Q: Can a user have multiple roles?

**A:** Yes! Users typically have multiple roles from different groups.

### Q: Should I create custom roles or use default ones?

**A:** Start with defaults. Create custom roles when you need specific combinations of permissions that don't fit existing roles.

### Q: How do I know if someone has too much access?

**A:** Red flags:

- Junior user with admin role
- Contractor with permanent employee access
- User with delete permissions they don't use
- User in more than 5 groups

### Q: Can I remove permissions without breaking things?

**A:** Yes! Use this process:

1. Audit what user actually uses
2. Create new minimal role
3. Assign new role
4. Monitor for 1 week
5. Remove old role if no issues

---