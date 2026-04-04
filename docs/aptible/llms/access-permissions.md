# Source: https://www.aptible.com/docs/core-concepts/security-compliance/access-permissions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Roles & Permissions

# Organization

Aptible organizations represent an administrative domain consisting of users and resources.

# Users

Users represent individuals or robots with access to your organization. A user's assigned roles determine their permissions and what they can access Aptible. Manage users in the Aptible dashboard by navigating to Settings > Members.

<Frame>
    <img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/org-members.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=e679ff67eb7e8f65bac2acf12ce008af" alt="Managing Members" data-og-width="1550" width="1550" data-og-height="1155" height="1155" data-path="images/org-members.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/org-members.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=8b6a4abca712d1170671ccab412f3cb0 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/org-members.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=ecc685ce7a3f4eec9c8504ffc3200350 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/org-members.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=88f1e8262ec311025f835d63785c0c30 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/org-members.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=02b36f90d894bc40a66ad6ab596d7b4e 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/org-members.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=2165b33fb06645e8a0329dc2fa0f2ebd 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/org-members.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=ca6dadcb83a5ead51e2061752c1fba9b 2500w" />
</Frame>

# Roles

Use roles to define users' access in your Aptible organization. Manage roles in the Aptible Dashboard by navigating to Settings > Roles.

<Frame>
    <img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/role-mgmt.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=533cc6b3d234e52387499d437fa1db25" alt="Role Management" data-og-width="1541" width="1541" data-og-height="1157" height="1157" data-path="images/role-mgmt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/role-mgmt.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=9dfb32475ec5d920d27b1021660a4f2e 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/role-mgmt.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=8455dabf272e907396717b13640eac11 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/role-mgmt.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=71af101b5857d67bd87a8d70724e6088 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/role-mgmt.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=bf590ab78ad0dfcc6ebc8526f3a92c58 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/role-mgmt.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=49ea7fc2f3e509c55b444cd5bfa02c19 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/role-mgmt.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=17b3fc72acbf1d58d09053ed21de9f14 2500w" />
</Frame>

## Types of Roles

### Account Owners

The Account Owners Role is one of the built-in roles in your organization that grants the following:

* admin access to all resources
* access to [billing information](/core-concepts/billing-payments) such as invoices, projections, plans, and contracts
* the ability to invite users
* the ability to manage all Roles
* the ability to remove all users from the organization

### Aptible Deploy Owners

The Deploy Owners Role is one of the built-in roles in your organization that grants the following:

* admin access to all resources
* the ability to invite users
* the ability to manage the Aptible Deploy Owners Role and Custom Roles
* the ability to remove users within Aptible Deploy Owners Role and/or Custom Roles from the organization

### Custom Roles

Use custom roles to configure which Aptible environments a user can access and what permissions they have within those environments. Aptible provides many permission types so you can fine-tune user access.

Since roles define what environments users can access, we highly recommend using multiple environments and roles to ensure you are granting access based on [the least-privilege principle](https://csrc.nist.gov/glossary/term/least_privilege).

#### Custom Role Admin

The Custom Role Admin role is an optional role that grants:

* access to resources as defined by the permission types of their custom role
* the ability to add new users to the custom roles of which they are role admins

<Frame>
    <img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/role-members.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=c7c00a06cf5e10616418c1bcec8c40bc" alt="Edit role admins" data-og-width="1544" width="1544" data-og-height="1157" height="1157" data-path="images/role-members.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/role-members.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=6371f39a841bf2cb11a3ba02da2b45df 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/role-members.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=6b485fe66aade6b6cde38f414f21f21a 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/role-members.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=b61c2592a011e04e11536fb10039618f 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/role-members.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=9543fe086bf9d4e990cfef9c6bef7d06 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/role-members.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=837cdfe652cf15929f740ffde6ea21a4 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/role-members.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=10f731525019ca2bb8b2d8822484ecdc 2500w" />
</Frame>

#### Custom Role Members

Custom Role Members have access to resources as defined by the permission types of their custom role.

#### Custom Role Permissions

Manage custom role permission types in the Aptible Dashboard by navigating to Settings > Roles. Select the respective role, navigate to Environments, and grant the desired permissions for the separate environments.

<Frame>
    <img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/role-env-perms-edit.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=3ae374878ea35c43586035ce2853065f" alt="Edit permissions" data-og-width="1542" width="1542" data-og-height="1156" height="1156" data-path="images/role-env-perms-edit.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/role-env-perms-edit.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=b2b6049b9f9987ba1a29c4a44e973540 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/role-env-perms-edit.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=588cd5cf0e9ab99bb85848dcc9e0d8c4 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/role-env-perms-edit.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=a1f23be4c5ace9d018ca42688ffe8fb6 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/role-env-perms-edit.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=daac06ecc60e1006705092d88b33c883 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/role-env-perms-edit.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=00507e50f6a0b653c5b7cd662a76d723 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/role-env-perms-edit.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=b30cada0a8a96e3cb09fc01a381ac419 2500w" />
</Frame>

#### Read Permissions

Assign one of the following permissions to give users read permission in a specific environment:

* **Basic Visibility**: can read general information about all resources
* **Full Visibility (formerly Read)**: can read general information about all resources and app configurations

#### Write Permissions

To give users write permission to a given environment, you can assign the following permissions:

* **Environment Admin** (formerly Write): can perform all actions listed below within the environment
* **Deployment**: can create and deploy resources
* **Destruction**: can destroy resources
* **Ops**: can create and manage log and metric drains and restart and scale apps and databases
* **Sensitive Access**:  can view and manage sensitive values such as app configurations, database credentials, and endpoint certificates
* **Tunnel**: can tunnel into databases but cannot view database credentials

<Tip> Provide read-only database access by granting the Tunnel permission without the Sensitive Access permission. Use this to manage read-only database access within the database itself.</Tip>

#### Full Permission Type Matrix

This matrix describes the required permission (header) for actions available for a given resource(left column).

|                                | Environment Admin | Full Visibility | Deployment | Destruction | Ops | Sensitive Access | Tunnel |
| :----------------------------: | :---------------: | :-------------: | :--------: | :---------: | :-: | :--------------: | ------ |
|           Environment          |        ---        |       ---       |     ---    |     ---     | --- |        ---       | ---    |
|           Deprovision          |         ✔         |                 |            |      ✔      |     |                  |        |
|             Rename             |         ✔         |                 |            |             |     |                  |        |
| Manage Backup Retention Policy |         ✔         |                 |            |             |     |                  |        |
|              Apps              | Environment Admin | Full Visibility | Deployment | Destruction | Ops | Sensitive Access | Tunnel |
|             Create             |         ✔         |                 |      ✔     |             |     |         ✔        |        |
|           Deprovision          |         ✔         |                 |            |      ✔      |     |                  |        |
|       Read Configuration       |         ✔         |        ✔        |            |             |     |         ✔        |        |
|            Configure           |         ✔         |                 |      ✔     |             |     |         ✔        |        |
|             Rename             |         ✔         |                 |      ✔     |             |     |                  |        |
|             Deploy             |         ✔         |                 |      ✔     |             |     |                  |        |
|             Rebuild            |         ✔         |                 |      ✔     |             |     |                  |        |
|              Scale             |         ✔         |                 |      ✔     |             |  ✔  |                  |        |
|             Restart            |         ✔         |                 |      ✔     |             |  ✔  |                  |        |
|        Create Endpoints        |         ✔         |                 |      ✔     |             |     |                  |        |
|      Deprovision Endpoints     |         ✔         |                 |            |      ✔      |     |                  |        |
|           Stream Logs          |         ✔         |                 |      ✔     |             |  ✔  |                  |        |
|           SSH/Execute          |         ✔         |                 |            |             |     |         ✔        |        |
|           Scan Image           |         ✔         |                 |      ✔     |             |  ✔  |                  |        |
|            Databases           | Environment Admin | Full Visibility | Deployment | Destruction | Ops | Sensitive Access | Tunnel |
|             Create             |         ✔         |                 |      ✔     |             |     |                  |        |
|           Deprovision          |         ✔         |                 |            |      ✔      |     |                  |        |
|        Read Credentials        |         ✔         |                 |            |             |     |         ✔        |        |
|         Create Backups         |         ✔         |                 |      ✔     |             |  ✔  |                  |        |
|         Restore Backups        |         ✔         |                 |      ✔     |             |     |                  |        |
|         Delete Backups         |         ✔         |                 |            |      ✔      |     |                  |        |
|             Rename             |         ✔         |                 |      ✔     |             |     |                  |        |
|    Restart / Reload / Modify   |         ✔         |                 |      ✔     |             |  ✔  |                  |        |
|         Create Replicas        |         ✔         |                 |      ✔     |             |     |                  |        |
|         Unlink Replicas        |         ✔         |                 |            |      ✔      |     |                  |        |
|        Create Endpoints        |         ✔         |                 |      ✔     |             |     |                  |        |
|      Deprovision Endpoints     |         ✔         |                 |            |      ✔      |     |                  |        |
|         Create Tunnels         |         ✔         |                 |            |             |     |                  | ✔      |
|           Stream Logs          |         ✔         |                 |      ✔     |             |  ✔  |                  |        |
|      Log and Metric Drains     | Environment Admin | Full Visibility | Deployment | Destruction | Ops | Sensitive Access | Tunnel |
|             Create             |         ✔         |                 |      ✔     |             |  ✔  |                  |        |
|           Deprovision          |         ✔         |                 |      ✔     |      ✔      |  ✔  |                  |        |
|        SSL Certificates        | Environment Admin | Full Visibility | Deployment | Destruction | Ops | Sensitive Access | Tunnel |
|             Create             |         ✔         |                 |            |             |     |         ✔        |        |
