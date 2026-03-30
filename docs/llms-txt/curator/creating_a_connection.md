# Source: https://docs.curator.interworks.com/creating_integrations/tableau_connection/creating_a_connection.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating a Tableau Connection

> Learn how to connect Curator to your Tableau Server or Tableau Cloud site using REST API for seamless dashboard integration.

Curator leverages Tableau’s REST API to communicate with your Tableau Server or Tableau Cloud Site to retrieve data
related to your dashboards and users, so it can display the right information to the right people. To connect Curator to
your Tableau Server/Tableau Cloud Site:

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Integration** > **Connections** section from the left-hand menu.
3. Click on the **New Connection** button at the top of the page.
4. Fill out the form, and select *Tableau* from the platform dropdown to reveal the connection details form below.
5. Expand the *Tableau Connection* section, select whether *Tableau Server* or *Tableau Cloud*, and enter in your
   Tableau Server URL or select your Tableau Cloud host, respectively.  Once the server check has been confirmed, you can
   begin filling out the authentication details using **either** a username + password or a Personal Access Token (PAT)
   using the steps below:

*Note: Only 1 connection to a specific Tableau Server URL or Tableau Cloud host can be made at a time.*

## Tableau Connections

### Tableau Server / Tableau Cloud: Personal Access Token (PAT)

**This connection-type is more stable and preferred over username and password due to changes in Tableau's APIs.**

1. Enable the toggle for *Use Personal Access Token for REST API Connection* in the "Tableau Connection" section
2. Ensure you have
   [created up Personal Access token on Tableau Server](https://help.tableau.com/current/pro/desktop/en-us/useracct.htm#create-and-revoke-personal-access-tokens),
   with at least a site administrator role and that you have the name and token.
3. Fill out the fields below, and once the confirmation check has been successful, save your settings:
   * **Personal Access Token Name** PAT Token Name
   * **Personal Access Token** PAT Token
   * **Tableau Server Site** Tableau Server Site\*
   * **Tableau Server Site (Custom)** Manually entered Tableau Server site\*

### Username & Password connection (not recommended - Tableau Server only)

**This connection type is not recommended and should only be used when absolutely required.**

Fill out the fields below, and once the confirmation check has been successful, save your settings:

* **Service Username** Tableau Server Admin Username
* **Service Password** Tableau Server Admin Password
* **Tableau Server Site** Tableau Server Site\*
* **Tableau Server Site (Custom)** Manually entered Tableau Server site\*

## Tableau Server Site (Custom)

Before saving your Tableau Connection settings for the the first time, when switching Tableau Servers, or when
connecting to Tableau Cloud you may need to use the "Tableau Server Site (Custom)" field.

1. Select "Custom" in the *Tableau Server Site* dropdown to enable the *Tableau Server Site (Custom)* field.

2. Manually enter the name of the site you wish to connect to

   **Tableau Server Site (Custom)** The value is derived from the url on Tableau Server.  For example: using
   `https://tableau.interworks.com/#/site/CuratorDemo`, you would enter **CuratorDemo**.

3. Save your settings.

*Note:* If you try to connect to a Custom Site with a Server Administrator account and get an error, make sure the user
account is specifically added to the Tableau Site you are trying to connect to. Even though it is a Server Administrator
and has frontend access to everything, it needs to be added to the site to get REST API access.

## Supported Tableau Server Versions

Curator supports Tableau Server version 2019.1 and on. This includes the latest version of Tableau Server as well.
Due to the fact that each new version of Tableau Server includes the older versions of the APIs we can support the
latest version.

In some cases people confuse support of a Tableau Server version with inclusion of new Tableau features. We strive to
integrate many of these new features when possible. Many times this is dependent on the API support. If there is a
feature you are interested in, or would like us to integrate, please reach out to our support team.
