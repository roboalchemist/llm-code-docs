# Source: https://planetscale.com/docs/vitess/delete-a-database.md

# Deleting a database

> How to remove a database from PlanetScale.

To access the settings for deleting a database:

<Steps>
  <Step>
    From the PlanetScale organization dashboard, select your database
  </Step>

  <Step>
    Navigate to **Settings** on the left sidebar menu
  </Step>
</Steps>

## Delete Database

The settings page provides the option to permanently delete your database. This action is irreversible and will:

* Delete the entire database and all of its branches
* Remove all data and backups permanently
* Disconnect any applications currently connected to the database
* Include usage charges in your invoice through the deletion date

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

Only organization administrators and database administrators have permission to delete databases. See the [Access Control documentation](/docs/security/access-control) for more information about user permissions.

## IP Restrictions

If you would like to 'soft delete' your database first, you can instead enable IP restrictions on the passwords for that database.

To enable IP restrictions:

<Steps>
  <Step>
    From the **Settings** page, select **Passwords** from the list
  </Step>

  <Step>
    Click the three dots button next to the password you wish to restrict
  </Step>

  <Step>
    Click the **Manage IP restrictions** button
  </Step>

  <Step>
    Add in an IP range that is NOT used by any clients and click the **Add** button
  </Step>
</Steps>

This will restrict the IP range to what is specified and can be used to test if connection are going to the database via the password in question.
This is a useful test for determining if the password in question is still in use, before deleting either the database or the password.
You should also confirm in [Insights](/docs/vitess/monitoring/query-insights) that no queries are executing on the database.

This helps avoid remaking passwords that are still in use or deleting a database that is still in use.

Once you've confirmed that no traffic is using any of your database passwords, you can follow the steps above to delete the database if desired and safe.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt