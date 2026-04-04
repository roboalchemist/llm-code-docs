# Source: https://planetscale.com/docs/postgres/settings.md

# Settings

> The Settings page allows you to configure general settings and options for your PlanetScale Postgres database.

To access the settings:

<Steps>
  <Step>
    From the PlanetScale organization dashboard, select your database
  </Step>

  <Step>
    Navigate to **Settings** on the left sidebar menu
  </Step>
</Steps>

## General Settings

### Database Name

The database name field displays your current database name. **This name cannot be changed** because it's used to connect to the database. Changing the name would break existing connections and applications.

### Default Branch

The default branch dropdown allows you to select which branch serves as the default for your database. This branch will be used as the source when creating new development branches.

To change the default branch:

<Steps>
  <Step>
    Click the **Default branch** dropdown
  </Step>

  <Step>
    Select the desired branch from the list
  </Step>

  <Step>
    Click **Save database settings** at the bottom of the page
  </Step>
</Steps>

### Restrict Branch Regions

The "Restrict branch regions" option allows you to limit where new branches can be created geographically. When enabled, this setting restricts branch creation to the same region as the default branch only.

To enable region restrictions:

<Steps>
  <Step>
    Check the **Restrict branch regions** checkbox
  </Step>

  <Step>
    Click **Save database settings** to apply the change
  </Step>
</Steps>

This setting is useful for:

* Compliance requirements that mandate data residency
* Cost optimization by keeping resources in a specific region
* Reducing latency by keeping all branches in the same geographic area

### Save Settings

After making any changes to the general settings, click the **Save database settings** button to apply your changes.

## Delete Database

The settings page also provides the option to permanently delete your database. This action is irreversible and will:

* Delete the entire database and all of its branches
* Remove all data and backups permanently
* Disconnect any applications currently connected to the database
* Include usage charges in your final invoice through the deletion date

<Warning>
  Database deletion cannot be undone. Make sure you have proper backups and that no critical applications depend on this database before proceeding.
</Warning>

To delete a database:

<Steps>
  <Step>
    Scroll to the bottom of the Settings page
  </Step>

  <Step>
    Click the red **Delete database** button
  </Step>

  <Step>
    Enter the database name
  </Step>

  <Step>
    Click **Delete database** to confirm
  </Step>
</Steps>

Only Organization Administrators and Database Administrators have permission to delete databases. See the [Access Control documentation](/docs/security/access-control) for more information about user permissions.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt