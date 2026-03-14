# Source: https://docs.acceldata.io/documentation/authorization.md

# Authorization

As organizations scale their data operations, it becomes critical to manage who can do what — and more importantly, on which data.

In earlier versions of ADOC (prior to v4.2), access was managed purely using **RBAC** (Role-Based Access Control). This meant you could define what actions a user could perform, such as creating reports or editing policies, but not which resources or data assets they could access. Everyone with a role had visibility into the same set of assets — a model that quickly became too broad and inflexible.

## Resource-Based Access Management

With RBAM, ADOC introduced a more secure, granular, and business-aligned approach to access control. RBAM allows admins to restrict resource visibility and operations by business domain — like Finance, Sales, or Operations — giving teams access only to the data and tools they need.

**Think of RBAC as answering the question:**

“Can this person create or edit something?”

**Whereas RBAM answers:**

“Which specific data or dashboards can they see or work on?”

**Why This Matters to You:**

- Prevents accidental data access or edits across departments.
- Aligns with compliance, security, and internal data governance policies.
- Supports complex team structures without manual oversight.

**RBAC** and **RBAM** now work together in ADOC to deliver secure, domain-scoped access — ensuring users can do only what they’re permitted to, only where they’re authorized to do it.

## 1. What Users Can Do

**Tenant Roles** such as **Owner**, **Admin**, **Editor**, and **Viewer** govern access to platform-wide features.

Role permissions are defined across categories:

- Administration (users, SSO, API keys)
- Compute (budget, monitors)
- Reliability (rule creation, KPIs, asset configuration)
- Pipeline management
- Alerts, General settings, etc.

Each permission has levels: **Create**, **Modify**, and **View**. Roles can be assigned to users or user groups. If a user has multiple roles, permissions are combined for full access.

**Example:** A user group assigned the **Editor** role can create pipelines, modify reports, and view dashboards as long as RBAM allows access to the correct domain.

## 2. What Resources Users Can Access

Resources are grouped into Domains (e.g., Finance, Marketing, HR). Within each domain, Resource Groups define collections of assets: data sources, dashboards, policy sets. 

Domain roles (e.g., resource_viewer, policy_editor, domain_manager) control access within a domain. These roles are assigned to user groups, not individuals.

Even if RBAC allows an action, the user can only see or act on resources inside domains they belong to.

**Example:** A user with “policy_editor” role in the Finance domain can create or modify policies—but only for assets in the Finance domain, not elsewhere.

## 3. How RBAC + RBAM Work Together

Combined Access Rules:

- The user’s **Tenant Role** (RBAC) governs what actions they can perform (e.g. "can create pipelines").
- The user’s **Domain Role** (RBAM) controls which domain's resources they can operate on.

Only if both checks pass, access is allowed.

**Scenario:** Sasha has the **RBAC Editor** and is part of the Finance domain group. She can create pipelines—but only for finance assets, not marketing assets.

## 4. Managing Access in ADOC

**Users & Groups**

- View and manage all users: email/ID, status, roles, groups, last login.
- Invite users in bulk with assigned roles and groups.
- Deactivate or edit user profiles, resend invites, or reset passwords.
- Use user groups to scale role/domain assignments.

**Tenant Roles (RBAC)**

- Accessible under **Settings** → **User Management and Access** → **Tenant Roles**
- Create or edit roles; assign permissions across categories (e.g. create pipelines, view alerts).
- Assign roles to user groups or individuals.
- Audit who created/modified each role and when.

**Domains & Domain Roles (RBAM)**

- Accessible under **Settings** → **Domain Management** → **Domains**
- Define business domains and attach resource groups (data, dashboards).
- Create domain roles and assign them to user groups.
- Domains restrict resource visibility—editors can modify only within assigned domains.
- Audit domain mappings and membership details.

### Example: Policy Import with Access Restrictions

ADOC allows importing policy packages (e.g. from ZIP files). Imported policies may be created even without domain assignment. Users will still not see or manage policies unless assigned the relevant domain role.

**Example:** Imported Finance policies remain hidden to users not in the Finance domain—even if RBAC identifies them as "admins."

## Common Use Cases

| **User** **Type** | **Intended Role** | **Domain** | **Access Rights** | 
| ---- | ---- | ---- | ---- | 
| Data Analyst | Viewer | Sales_Viewer | View dashboards/reports in Sales domain only | 
| Data Engineer | Editor | Finance_Editors | Can build and modify pipelines/policies in Finance domain | 
| SRE | Reliability Editor | Platform Operations | Manage metric pipelines in Platform domain | 
| Policy Admin | Policy Editor | Marketing_Editors | Edit policy sets for marketing data sets | 


---

## Best Practices

1. Use clear and consistent naming: e.g. FIN_PolicyEditors, Sales_Viewer.
2. Maintain RBAC and RBAM groups separately to reduce complexity.
3. Use the **Access Visualizer** tool to see effective permissions per user.
4. Review user and group membership regularly to minimize overprovisioning.
5. Prefer system-defined domain roles, create custom roles only when absolutely necessary.
6. When importing policies, ensure correct domains exist first.
7. Start with broad domains and refine resource groups as needed.

---

## FAQs

**If someone has RBAC rights but no domain role, can they access resources?**

No, access is denied unless the user also has the appropriate domain role in that specific domain.

**Can a user belong to multiple domains?**

Yes, a user can be part of more than one domain group as independently mapped.

**Are imported policies instantly accessible?**

No, they exist in the system, but only become visible/editable once appropriate domain roles are in place.