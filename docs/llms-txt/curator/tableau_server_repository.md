# Source: https://docs.curator.interworks.com/creating_integrations/tableau_connection/tableau_server_repository.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Tableau Server Repository

> Connect directly to Tableau Server repository database for high-volume deployments

Sometimes (but very rarely) you may need to connect directly to Tableau Server's repository.  Generally this is
recommended when your user-count is very high (5000+ users), your Tableau Server connection is dealing with severe
latency that cannot be overcome (making the REST API responses very slow), or you need to enable the password reset
feature.  In these instances you will need to make sure your Tableau Server repository is enabled on Tableau Server first.

## Configuring Tableau Server's Readonly Account

By default, access to the Tableau Server repository is disabled.  To enable it, as well as set the password, you need to
issue a TSM command like the following against your Tableau Server:

```bash  theme={null}
tsm data-access repository-access enable –repository-username readonly –repository-password "YOUR PASSWORD HERE"
```

Refer to Tableau’s [documentation](https://help.tableau.com/current/server/en-us/perf_collect_server_repo.htm) if you
would like a little more information about this.  Also, if your IT security has locked ports down on your Tableau
Server, make sure they open up port 8060 to Curator.

## Connecting Curator to the Repository

Once you have enabled access to the repository and set its password, you can configure the connection on Curator:

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Integrations** > **Connections** section from the left-hand menu.
3. Click on the Tableau Server connection you want to edit.
4. Expand the "Tableau Server Repository Connection" near the bottom of the page.
5. Enable the toggle for *Connect to Tableau Server's Repository Database* in the "Primary Tableau Connection" section.
6. Enabling the toggle will display a new section: "Tableau Server Repository Connection".
7. Check for any errors shown in this section.  They must be addressed before the connection can be established.
8. Expand the "Tableau Server Repository Connection" section and fill out the connection fields.  For information on how
   to find the default connection information on your Tableau Server, see:

   * **Repository Host** Tableau Server host url

   * **Repository Port** This value is *8060* by default.

   * **Repository User** *readonly* (recommended user)

   * **Repository Password** Password you set up in Step #1 on Tableau Server
9. Once properly filled out, click the "Save" button.
