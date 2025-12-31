# Source: https://planetscale.com/docs/vitess/security/password-roles.md

# Password roles

> PlanetScale allows you to [create and manage passwords](/docs/vitess/connecting/connection-strings) for each branch of your database.

## Overview

PlanetScale passwords can be created with one of four roles:

* **Read-only** — Can query rows
* **Write-only** — Can modify rows
* **Read/Write** — Can query and modify rows
* **Admin** — All read/write permissions and can modify schema\*

\* *This does not apply to production branches with [safe migrations](/docs/vitess/schema-changes/safe-migrations) enabled, as we [do not allow direct DDL](/docs/vitess/schema-changes/how-online-schema-change-tools-work) on those branches, even if your password has the `Admin` role.*

## Create a password with custom role

<Steps>
  <Step>
    Go to your database settings page.
  </Step>

  <Step>
    Click "**Passwords**" > "**New password**".
  </Step>

  <Step>
    Give it a name, select the role from the dropdown, select the branch, and click "**Generate password**".

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/password-roles/roles.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=2baaa80270578f1e6206191646adf4bf" alt="PlanetScale password roles priority" data-og-width="970" width="970" data-og-height="756" height="756" data-path="docs/images/assets/docs/concepts/password-roles/roles.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/password-roles/roles.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=40430875893a8fc58fd82c9f13255e07 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/password-roles/roles.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=8e8750f0d041aa0e593fa68ab2b5d9f0 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/password-roles/roles.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=1f040900eb136963309a2106393373f9 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/password-roles/roles.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=77a64d0174a81f19e335cb3742a77649 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/password-roles/roles.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=68bb427aaddb8e3a1909832c657dc015 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/password-roles/roles.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=dde9a198d4570e2c5fa89f73288decf1 2500w" />
    </Frame>
  </Step>
</Steps>

Once a password is created, **its role cannot be changed**.

The access level available to these roles is shown in the table below.

| Role name  | Can create/edit schema             | Can insert/update/delete rows      | Can query rows                     |
| :--------- | :--------------------------------- | :--------------------------------- | :--------------------------------- |
| Read-only  | <Icon icon="xmark" color="red" />  | <Icon icon="xmark" color="red" />  | <Icon icon="check" color="blue" /> |
| Write-only | <Icon icon="xmark" color="red" />  | <Icon icon="check" color="blue" /> | <Icon icon="xmark" color="red" />  |
| Read/write | <Icon icon="xmark" color="red" />  | <Icon icon="check" color="blue" /> | <Icon icon="check" color="blue" /> |
| Admin      | <Icon icon="check" color="blue" /> | <Icon icon="check" color="blue" /> | <Icon icon="check" color="blue" /> |

<Note>
  The default role for all passwords created by the **Connect** button is `Administrator`. Passwords with custom roles
  must be created from your database settings page.
</Note>

## Troubleshooting

The following errors indicate that you do not have the permissions needed to perform an action. You must create a new password with a more privileged role to proceed.

**SELECT DENIED**

`Select command denied to user ‘planetscale-writer-only for table ‘customers’ (ACL check error) (CallerID: planetscale-writer-only)`

**INSERT DENIED**

`Insert command denied to user ‘planetscale-reader’ for table ‘customers’ (ACL check error) (CallerID: planetscale-reader)`

**DELETE DENIED**

`Delete command denied to user ‘planetscale-reader’ for table ‘customers’ (ACL check error) (CallerID: planetscale-reader)`

**DDL DENIED**

`DDL command denied to user ‘planetscale-writer' for table my-new-table’ (ACL check error) (CallerID: planetscale-writer)`

<Note>
  If your pscale CLI version is less than 0.94.0, please upgrade your installation by following [this
  document](/docs/cli/planetscale-environment-setup)
</Note>

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt