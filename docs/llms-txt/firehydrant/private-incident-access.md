# Source: https://docs.firehydrant.com/docs/private-incident-access.md

# Private Incident Access

> 📘 Note:
>
> Modifying private/public incident access controls requires <Glossary>Owner</Glossary>. See [Role-Based Access Controls](https://docs.firehydrant.com/docs/role-based-access-controls) for more information.

Access control for private incidents was inspired by [security standards for incident handling](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final), developed by the National Institute of Standards and Technology. Private incident access control focuses on the following:

* Securely containing incident information
* Enabling collaboration to resolve and learn from incidents

## Access Controls

<Image alt="Users table example with access controls " align="center" width="650px" src="https://files.readme.io/498b283-users-table.png">
  Users table example with access controls
</Image>

* **Owners**
  * Owners always have access to all public and private incidents.
  * Owners can change other users' public/private permissions and access roles.
* **"Private" Access Control**
  * Users who have the "Private" access control who are not **Owners** will have the permission to declare, view, and manage both private and public incidents.
  * These users can also invite others, including Public users, to a private incident ad-hoc.
* **"Public" Access Control**
  * Any user assigned "Public" access controls cannot create, manage, or view private incidents.
  * This is the default permission for all users in your organization until changed by an **Owner**.
  * However, **Public access users can be added to individual private incidents on an ad-hoc basis**. When this happens, they will gain permissions for that particular incident according to their [access role](https://docs.firehydrant.com/docs/role-based-access-controls).

To configure permissions, go to a specific user's settings in **Settings> Users > ser]**\*\* and toggle their private incident access accordingly.

<Image alt="User role and private incident access permissions in Settings" align="center" width="650px" src="https://files.readme.io/49d5a7b-image.png">
  User role and private incident access permissions in Settings
</Image>

## Ad-hoc Users

**Owners** and users with **Private** incident access can add individual users to Private Incidents, even if those users do not have **Private** permissions.

This allows **Public** users to join private incidents if and when needed on an ad-hoc basis, and this access is only scoped to that specific incident and not all private incidents.

To learn more, see [adding ad hoc users](/docs/private-incidents#ad-hoc-users).

## Next Steps

* See how to [conduct Private Incidents](https://docs.firehydrant.com/docs/private-incidents)
* Learn more about [Role-Based Access Controls](https://docs.firehydrant.com/docs/role-based-access-controls) on FireHydrant