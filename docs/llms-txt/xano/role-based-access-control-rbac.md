# Source: https://docs.xano.com/team-collaboration/role-based-access-control-rbac.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Role Based Access Control (RBAC)

<Tip>
  Role-Based Access Control (Permissions) is included with our **Pro** and **Enterprise / Custom** plans.
</Tip>

Xano Enterprise allows granular permissions control for each team member and workspace within an Instance.

## Permissions Center

The Permissions Center, when enabled, allows the Instance owner full control over role-based permissions across each workspace within the Instance.

To access the Permissions Center, open the menu panel on the Instance then choose Permissions (RBAC).

<Frame caption="Open the menu panel of your instance.">
  <img src="https://mintcdn.com/xano-997cb9ee/_FyaEhYRFYQZinJ0/images/e02e354c-image.jpeg?fit=max&auto=format&n=_FyaEhYRFYQZinJ0&q=85&s=c780aca00b1861401ea8162548b0b1ea" width="760" height="187" data-path="images/e02e354c-image.jpeg" />
</Frame>

<Frame caption="Open Permissions (RBAC).">
  <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/6ebf66ec-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=7c76b51c758cc165c75825c9e08691e2" width="401" height="603" data-path="images/6ebf66ec-image.jpeg" />
</Frame>

### Roles

Roles can be managed and created from the Roles view of the Permission Center.

<Frame caption="Manage Role in the Permissions Center.">
  <img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/12009b4e-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=c67b63fce04debe8acc9d2e37cf4e9a5" width="1594" height="680" data-path="images/12009b4e-image.jpeg" />
</Frame>

#### Default Roles

Xano includes two default roles, which permissions are standard and cannot be modified. These roles are admin and developer.

#### Permissions

Permission types can be set on the various workspace objects in Xano. The permission types are as follows:

* **(C) Create** - permission to create the specified object.

* **(R) Read**- permission to read the specific object.

* **(U) Update** - permission to update or modify the specified object.

* **(D) Delete** - permission to delete the specified object.

* **Full** - permission to Create, Read, Update, and Delete (CRUD).

* **Enabled/Disabled** - some objects only require enabling or disabling the permission.

* **Inherit\*** - inherit is a special permission type. This permission will inherit the same permission from the parent role type. Meaning, inherit is chosen for Jane Doe on Workspace A for Run & Debug, then Jane's permission on Run & Debug will inherit the permission of her assigned role.

#### Objects

Please read each description carefully to understand the permissions for each object. The objects with role-based access control include:

* Instance Billing - access to manage Instance billing.

* Instance Workspace - access to manage Instance workspaces.

* Workspace Export - allows usage of the workspace export feature.

* Workspace Run & Debug - allows usage of the workspace Run & Debug feature.

* Workspace Addons - allows access to workspace Addons.

* Workspace API Groups - allows access to workspace API groups.

* Workspace Connect - allows access to workspace Connect Center.

* Workspace Content - allows access to workspace content (database records).

* Workspace Live Data Source - allows access to workspace content (database records) **on the live data source**.

<Info>
  When disabled, users can still access non-live data source content (if Workspace Content permission is enabled).\*\* Use this permission to protect access to production data.\*\*
</Info>

* Workspace Database - allows access to workspace database.

* Workspace Env - allows access to workspace Environment Variables.

* Workspace Files - allows access to workspace Files and File Management.

* Workspace Functions - allows access to workspace Custom Functions in the Library.

* Workspace Marketplace - allows access to workspace Marketplace.

* Workspace Request History - allows access to workspace API Request History.

* Workspace Task - allows access to workspace Background Tasks.

* Additional objects coming soon.

#### Create a Custom Role

To create a new role select **+ Add new custom role**.

<Frame caption="Create a new Custom Role.">
  <img src="https://mintcdn.com/xano-997cb9ee/ClU5W_-qt6GI3QWZ/images/44b8c2b1-image.jpeg?fit=max&auto=format&n=ClU5W_-qt6GI3QWZ&q=85&s=f016269ea2f0afaff924e00b68b6c7cc" width="800" height="440" data-path="images/44b8c2b1-image.jpeg" />
</Frame>

#### Edit Role Permissions

To edit the permissions on a custom role, double-click the permission level to modify and select the new permission from the dropdown.

<Frame caption="Modify Permissions of a Role.">
  <img src="https://mintcdn.com/xano-997cb9ee/pz6e9Ndbn8i3u8Zz/images/66fb44d6-image.jpeg?fit=max&auto=format&n=pz6e9Ndbn8i3u8Zz&q=85&s=d859260a79b8888855901c55c498cc73" width="800" height="420" data-path="images/66fb44d6-image.jpeg" />
</Frame>

### Workspaces View

The initial view in the Permissions Center provides a view of all the Workspaces, team members, and permissions in the Instance.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/31eda0dd-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=2005a95680bb40507029f63d41b062b1" width="1610" height="852" data-path="images/31eda0dd-image.jpeg" />
</Frame>

You can easily filter by team member and workspace to see which permissions are enabled for a particular person and workspace.

<Frame caption="In this example, we are looking at Michael's permissions across all workspaces.">
  <img src="https://mintcdn.com/xano-997cb9ee/WBQXG-4Ngk82eYAW/images/fff25e10-image.jpeg?fit=max&auto=format&n=WBQXG-4Ngk82eYAW&q=85&s=a8d08902fd05fe1eb8b5835640139856" width="1580" height="861" data-path="images/fff25e10-image.jpeg" />
</Frame>

#### **Copy/Paste Permissions**

Copy/Paste Permission\*\* \*\*enables you to quickly assign a team member the same permissions as another one. This is useful when you have team members that need the exact same access across each Workspace.

To do this, choose the Copy/Paste button, then the team member you want to copy permissions from, and the team member you wish to paste permissions to.

<Frame caption="COPY/PASTE Permissions of one team member to another.">
  <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/58221c73-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=bd1a73b9195813a3ec77f5807518be27" width="1608" height="730" data-path="images/58221c73-image.jpeg" />
</Frame>

#### Edit Permissions on a Workspace

You can edit specific permissions on a Workspace for a team member by [clicking on the permission](/team-collaboration/role-based-access-control-rbac#edit-role-permissions) you want to modify.

#### Bulk-Assigning Roles and Permissions

Click the three dots above your roles list to open a menu, offering quick access to managing roles and permissions.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f8c6f212-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=351f7f4b054a73ad8083d6163c4269a5" width="331" height="250" data-path="images/f8c6f212-image.jpeg" />
</Frame>

**Managing Team Roles**

Choose the role you would like to apply and then select the users you would like to apply the role to.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/39e88d76-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=1eed9172a24e24f5ad56f924fffd726d" width="821" height="696" data-path="images/39e88d76-image.jpeg" />
</Frame>

**Bulk Editing Permissions**

Select the users who you would like to modify permissions for. After that, select the workspaces you would like to modify the permissions for with each user. Finally, you can modify the permissions as desired. Any row left **Unmodified** will not be changes,

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/tjSJ_pOzk8E0WRhF/images/c5bc08e4-image.jpeg?fit=max&auto=format&n=tjSJ_pOzk8E0WRhF&q=85&s=f978ea0236726f7d3ce437e5ecabcc74" width="1212" height="765" data-path="images/c5bc08e4-image.jpeg" />
</Frame>


Built with [Mintlify](https://mintlify.com).