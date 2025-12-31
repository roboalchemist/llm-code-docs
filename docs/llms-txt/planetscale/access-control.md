# Source: https://planetscale.com/docs/security/access-control.md

# Access control

## Organization access control

When you set up your PlanetScale account, you're asked to create an **Organization**.

An organization is essentially a container for your databases, settings, and members. You can create multiple organizations in the same account for different applications or use cases.

Within each organization, you can add members and assign them different roles. This document covers the different roles, the ways you can assign roles, permissions associated with those roles.

## Roles and permissions

We currently support three different roles in your organization:

* `Organization Administrator`
* `Organization Member`
* `Database Administrator`

### Organization Administrator

An `Organization Administrator` can perform all actions in an organization, as well as all actions on *every* database within that organization.

### Organization Member

An `Organization Member` can only perform limited actions within an organization and on all databases in that organization. By default, all users added to an organization have this role.

### Database Administrator

A `Database Administrator` can perform all actions on the database for which they were assigned the `Databases Administrator` role.

This role is assigned at the **database level** and gives elevated permissions for the particular database that an organization member is the `Database Administrator` of. If you want to [grant a member *full* access to manage one or several databases](#assign-roles-at-a-database-level) but not full `Organization Administrator` access, then this is the role you want. Please note, a user that is granted this role must be a member of the organization of which the database exists in, so they will have the permissions associated with `Organization Member` as well.

## Organization-level permissions

Each role has a set of permissions assigned to it, which determines what actions that role is allowed to take within an organization or database.

The following table describes permissions assigned at the organization level for `Organization Administrators` and `Organization Members`. Because `Database Administrators` don't have any organization-level permissions, they are not included in this table.

| Action                                 | Description                                                                    | Member                             | Administrator                      |
| -------------------------------------- | ------------------------------------------------------------------------------ | ---------------------------------- | ---------------------------------- |
| View branches                          | View a database branch                                                         | <Icon icon="check" color="blue" /> | <Icon icon="check" color="blue" /> |
| Create branches                        | Create a database branch                                                       | <Icon icon="check" color="blue" /> | <Icon icon="check" color="blue" /> |
| Delete non-production branches         | Delete a non-production database branch                                        | <Icon icon="check" color="blue" /> | <Icon icon="check" color="blue" /> |
| View databases                         | View one or all databases                                                      | <Icon icon="check" color="blue" /> | <Icon icon="check" color="blue" /> |
| Create databases                       | Create a new database                                                          | <Icon icon="check" color="blue" /> | <Icon icon="check" color="blue" /> |
| Create deploy requests                 | Create a deploy request for a branch                                           | <Icon icon="check" color="blue" /> | <Icon icon="check" color="blue" /> |
| Manage service tokens                  | Create, view, or delete service tokens                                         | <Icon icon="check" color="blue" /> | <Icon icon="check" color="blue" /> |
| Manage service token grants            | Create, view, update, or delete service token grants                           | <Icon icon="check" color="blue" /> | <Icon icon="check" color="blue" /> |
| View organization members              | View one or all organization members                                           | <Icon icon="check" color="blue" /> | <Icon icon="check" color="blue" /> |
| View database members                  | View one or all database members                                               | <Icon icon="check" color="blue" /> | <Icon icon="check" color="blue" /> |
| View organization                      | View an organization                                                           | <Icon icon="check" color="blue" /> | <Icon icon="check" color="blue" /> |
| View query statistics                  | View query statistics for an organization's databases                          | <Icon icon="check" color="blue" /> | <Icon icon="check" color="blue" /> |
| Connect to development branches        | Create passwords or use pscale shell for development branches                  | <Icon icon="check" color="blue" /> | <Icon icon="check" color="blue" /> |
| Connect to production branches         | Create passwords or use pscale shell for production branches                   |                                    | <Icon icon="check" color="blue" /> |
| Delete production branches             | Delete a production database branch                                            |                                    | <Icon icon="check" color="blue" /> |
| Promote branches                       | Promote a branch to production                                                 |                                    | <Icon icon="check" color="blue" /> |
| Modify VSchema (Vitess only)           | Edit the VSchema of a keyspace                                                 |                                    | <Icon icon="check" color="blue" /> |
| Manage databases                       | Delete, update settings, or import a database                                  |                                    | <Icon icon="check" color="blue" /> |
| Manage beta features                   | Opt-in or opt-out of a beta feature                                            |                                    | <Icon icon="check" color="blue" /> |
| Create production service token grants | Create a service token grant to connect or delete a production database branch |                                    | <Icon icon="check" color="blue" /> |
| Update an integration                  | Update a third-party integration                                               |                                    | <Icon icon="check" color="blue" /> |
| Manage invitations                     | View, create, or cancel organization invitations                               |                                    | <Icon icon="check" color="blue" /> |
| Manage invoices                        | View or download organization invoices                                         |                                    | <Icon icon="check" color="blue" /> |
| Manage billing                         | View or update billing plans and payment methods                               |                                    | <Icon icon="check" color="blue" /> |
| View audit logs                        | View all audit logs                                                            |                                    | <Icon icon="check" color="blue" /> |
| Manage organization members            | Update member roles or delete organization members                             |                                    | <Icon icon="check" color="blue" /> |
| Manage database members                | Update member roles, add, or remove database members                           |                                    | <Icon icon="check" color="blue" /> |
| Manage organization                    | Update organization settings, SSO, or delete organization                      |                                    | <Icon icon="check" color="blue" /> |

## Database-level permissions

The following table describes the permissions assigned at the **database level** for `Organization Administrators`, `Organization Members`, and `Database Administrators`.

For `Organization Administrators` and `Organization Members`, these permissions apply to every database in the organization. Because the `Database Administrator` role is assigned at the database level, the permissions are for the specific database(s) for which they have the `Database Administrator` role.

| Action                          | Description                                                   | Member                             | Administrator                      |
| ------------------------------- | ------------------------------------------------------------- | ---------------------------------- | ---------------------------------- |
| Create and view branches        | Create or view a database branch                              | <Icon icon="check" color="blue" /> | <Icon icon="check" color="blue" /> |
| Delete non-production branches  | Delete a non-production branch of a specific database         | <Icon icon="check" color="blue" /> | <Icon icon="check" color="blue" /> |
| View database                   | View a database in an organization                            | <Icon icon="check" color="blue" /> | <Icon icon="check" color="blue" /> |
| Create deploy requests          | Create a deploy request for a branch on a specific database   | <Icon icon="check" color="blue" /> | <Icon icon="check" color="blue" /> |
| View database members           | View one or all database members                              | <Icon icon="check" color="blue" /> | <Icon icon="check" color="blue" /> |
| View query statistics           | View query statistics for an organization's databases         | <Icon icon="check" color="blue" /> | <Icon icon="check" color="blue" /> |
| Restore non-production backups  | Restore the backup of a development branch                    | <Icon icon="check" color="blue" /> | <Icon icon="check" color="blue" /> |
| Connect to development branches | Create passwords or use pscale shell for development branches | <Icon icon="check" color="blue" /> | <Icon icon="check" color="blue" /> |
| Connect to production branches  | Create passwords or use pscale shell for production branches  |                                    | <Icon icon="check" color="blue" /> |
| Manage billing                  | Update the billing plan of a specific database                |                                    | <Icon icon="check" color="blue" /> |
| Delete production branches      | Delete a production database branch of a specific database    |                                    | <Icon icon="check" color="blue" /> |
| Promote branches                | Promote a branch of a specific database to production         |                                    | <Icon icon="check" color="blue" /> |
| Manage database                 | Delete, update settings, or import a database                 |                                    | <Icon icon="check" color="blue" /> |
| Manage beta features            | Opt-in or opt-out of a beta feature for a database            |                                    | <Icon icon="check" color="blue" /> |
| Manage database members         | Update database member roles, add, or remove database members |                                    | <Icon icon="check" color="blue" /> |
| Restore production backups      | Restore the backup of a production branch                     |                                    | <Icon icon="check" color="blue" /> |

An organization may have several databases, and an `Organization Member` may have different access to each database depending on whether or not they also have the `Database Administrator` role.

## Assign organization roles to members

You can follow the steps below to assign roles to your members. You must be an Organization Administrator to modify member roles.

* In the [PlanetScale dashboard](https://app.planetscale.com), click on the Settings tab in the top navigation.
* Click on "Members" in the sidebar on the left.
* From here, you can click on the dropdown on the right under the "Role" column to select the role you want to apply to each member.

You can also invite new members to your organization and assign roles once they accept their invitation. New members will be added with the [`Organization Member`](#organization-member) role by default.

<Note>
  Member role management is issued at the organization level. Each organization in your account may have different
  members with different access levels.
</Note>

## Assign roles at a database level

There are two ways to assign database-level roles to Organization members:

1. Individually using the `Database Administrator` role.
2. Creating a Team, adding member(s), and adding database(s) to that team.

### Individually assign the `Database Administrator` role

To assign a member the role of `Database Administrator`, follow the steps outlined below. You must be an Organization Administrator or an existing Database Administrator to manage the `Database Administrator` role.

<Note>
  Members that create a database are automatically assigned the role of `Database Administrator` for that database.
</Note>

<Steps>
  <Step>
    In the [PlanetScale dashboard](https://app.planetscale.com), click on the name of the database you want to add a Database Administrator to.
  </Step>

  <Step>
    Click on the "**Settings**" tab in the top navigation.
  </Step>

  <Step>
    Click on "**Administrators**" in the sidebar on the left.
  </Step>

  <Step>
    To add an administrator, click on the "**Add administrator**" button and select the member you wish to add as a Database Administrator.
  </Step>

  <Step>
    From here, you can also remove a Database Administrator by clicking the "**Remove**" button next to their name.
  </Step>
</Steps>

### Add Database Administrator role via Teams

If you wish to give several members the Database Administrator role, you may want to [create a Team](/docs/security/teams#create-and-manage-teams). This will allow you to manage the access to that database all in one place.

For instructions, see our [Teams documentation](/docs/security/teams).

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt