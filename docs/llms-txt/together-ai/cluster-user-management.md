# Source: https://docs.together.ai/docs/cluster-user-management.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Cluster User Management

Manage user access to your GPU clusters by adding team members who can SSH into Slurm clusters or access Kubernetes resources.

[Learn more about GPU Clusters →](/docs/gpu-clusters-overview)

## Understanding Organizations and Projects

Before managing cluster access, it's important to understand how Together AI organizes resources:

### Organizational Hierarchy

**Organizations** → **Projects** → **Clusters & Volumes**

1. **Organization**: Your company or team's top-level account
   * Managed at [api.together.ai/settings/organization](https://api.together.ai/settings/organization)
   * Supports both [SSO](/docs/sso) and [OAuth-based organization invites](/docs/organizations#organization-membership) for multi-user access
   * Being added to an organization does NOT automatically grant access to specific projects or clusters

2. **GPU Cluster Projects**: The collaboration boundary for teams and workloads
   * Managed at [api.together.ai/settings/gpu-projects](https://api.together.ai/settings/gpu-projects)
   * Contains GPU clusters and storage volumes
   * Each cluster and volume is tied to exactly one project
   * Access control is managed at the project level

3. **GPU Clusters**: Individual Kubernetes or Slurm clusters
   * Viewed at [api.together.ai/clusters](https://api.together.ai/clusters)
   * Inherit permissions from their parent project
   * Users see all clusters from all projects they have access to

### How Access Control Works

<Note>
  **Key Concept:** Think of projects as the collaboration boundary. Your GPU clusters and volumes are mapped to a project, and users are granted access at the project level.
</Note>

**Adding users to a project grants them access to ALL resources within that project:**

* All GPU clusters in the project
* All storage volumes in the project
* SSH access to cluster nodes
* In-cluster permissions based on their role (Member or Admin)

**Example Scenario:**

```
Organization: Acme Corp
├── Project: ML-Training
│   ├── Cluster: h100-cluster-1
│   ├── Cluster: h100-cluster-2
│   └── Volume: training-data
└── Project: Research
    ├── Cluster: b200-cluster
    └── Volume: research-data
```

If you add a user as a Member to the "ML-Training" project, they get access to both H100 clusters and the training-data volume, but NOT the Research project resources.

### Access Control is Project-Based

* **Organization membership** ≠ **Project access**: Users must be explicitly added to individual projects
* **Project creators** automatically become project admins
* **All clusters in a project** share the same access control list
* To grant cluster access, invite users to the cluster's parent project

## User Roles and Permissions

GPU Cluster projects support two user roles with different permission levels:

### Admin

Admins have full control over both control plane and data plane operations.

**Control Plane Permissions (Full Write Access):**

* Create clusters
* Delete clusters
* Create storage volumes
* Delete storage volumes
* Modify cluster configurations
* Scale up or down nodes

**Data Plane Permissions (Full Access):**

* SSH into cluster nodes
* Run workloads and jobs
* Access Kubernetes Dashboard
* Execute kubectl commands

**User Management:**

* Add members to the project
* Remove members from the project
* Assign user roles

### Member

Members have read-only access to control plane resources but full access to data plane operations.

**Control Plane Permissions (Read-Only):**

* ✓ View clusters
* ✓ View storage volumes
* ✓ View cluster configurations
* ✗ Cannot create clusters
* ✗ Cannot delete clusters
* ✗ Cannot create storage volumes
* ✗ Cannot delete storage volumes
* ✗ Cannot scale the cluster - up or down

**Data Plane Permissions (Full Access):**

* SSH into cluster nodes
* Run workloads and view job status
* Access Kubernetes Dashboard
* Execute kubectl commands
* View pod log and status

<Note>
  **RBAC Enforcement:** Member permissions for in-cluster operations may vary based on cluster configuration. Contact support to understand the specific RBAC policies applied to your cluster.
</Note>

**User Management:**

* ✗ Cannot add or remove users

<Note>
  **Key Difference:** Members have read-only access to control plane resources (cannot create/destroy clusters or volumes) and can SSH into nodes. In-cluster permissions (deploying pods, running jobs) depend on RBAC configuration.
</Note>

## Adding Users to Projects

<Note>
  **Important:** When you add a user to a project, they gain access to **all clusters and volumes** within that project. You cannot grant access to individual clusters - access is always project-wide.
</Note>

<Note>
  **Prerequisites:** Users must have:

  * A Together AI account ([sign up here](https://api.together.ai/signin))

  Without these, users cannot be added to your project.
</Note>

### Step-by-Step Instructions

1. **Access Settings**
   * Log in to your Together AI account at [api.together.ai](https://api.together.ai)
   * Click your avatar in the top-right corner
   * Select **Settings** from the dropdown menu

2. **Navigate to GPU Cluster Projects**
   * In the left sidebar, click **GPU Cluster Projects**
   * You'll see a list of all projects you have admin access to

3. **Select Your Project**
   * Click **View Project** on the project containing the clusters you want to share
   * This shows all users currently in the project and their roles

4. **Add a New User**
   * Click the **Add User** button
   * A popup dialog will appear

5. **Enter User Email**
   * Enter the email address of the user you want to add
   * Click **Add User** to confirm

<Note>
  **Default Role:** New users are added as Members by default. To grant admin access, you can change their role to Admin after adding them via the members table.
</Note>

6. **Verify Addition**
   * If successful, the user will appear in the members grid
   * They now have access to all clusters in this project
   * If the user doesn't have a Together AI account, you'll see an error message

<Tip>
  **Managing Multiple Clusters:** If you need different access control for different clusters, create separate projects for each access boundary. For example:

  * "Production" project for production clusters
  * "Development" project for dev/test clusters

  Note: Please contact this support if you need this capability, since this feature is currently in closed beta.
</Tip>

## Removing Users from Projects

Removing a user from a project revokes their access to all clusters and volumes in that project.

### Steps to Remove a User

1. Navigate to **Settings** > **GPU Cluster Projects**
2. Click **View Project** on the relevant project
3. Find the user in the members grid
4. Click the **three dots** (⋯) on the right side of their row
5. Select **Remove User** from the dropdown menu
6. Confirm the removal when prompted

<Warning>
  **Access Revocation:** The user will lose access to:

  * All clusters in the project
  * All storage volumes in the project
  * SSH access (revoked within minutes as identity changes sync)
  * Any running jobs or pods will continue but the user cannot manage them
</Warning>

## Frequently Asked Questions

### Why can't my team members see our cluster?

Users must be explicitly added to the GPU Cluster Project that contains the cluster. Being part of your organization is not enough - they need project-level access.

### Can I grant access to just one cluster in a project?

No. Access control is at the project level. All clusters in a project share the same access control list. To have different access controls, create separate projects.

### What's the difference between Organization and Project access?

* **Organization**: Your company's top-level account. Used for billing and SSO. Does not grant cluster access.
* **Project**: The collaboration boundary. Users added to a project can access all clusters and volumes in that project.

### How do I see all my clusters across different projects?

Visit [api.together.ai/clusters](https://api.together.ai/clusters) - this view aggregates all clusters from all projects you have access to.


Built with [Mintlify](https://mintlify.com).