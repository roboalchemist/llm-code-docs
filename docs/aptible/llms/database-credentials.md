# Source: https://www.aptible.com/docs/core-concepts/managed-databases/connecting-databases/database-credentials.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Database Credentials

# Overview

When you provision a [Database](/core-concepts/managed-databases/overview) on Aptible, you'll be provided with a set of Database Credentials.

<Warning>
  The password in Database Credentials should be protected for security.
</Warning>

Database Credentials are presented as connection URLs. Many libraries can use those directly, but you can always break down the URL into components.  The structure is:

<img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/dbcredspath.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=d06fa246b9c6116dfffaeb19e691e8b2" alt="" data-og-width="1134" width="1134" data-og-height="394" height="394" data-path="images/dbcredspath.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/dbcredspath.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=c7509b740b6f48e2fdf50529ecfa9088 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/dbcredspath.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=400497ce613ec794972d84981ba8fa91 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/dbcredspath.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=f285f16856b7680bf7bd48411c91d6b6 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/dbcredspath.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=750b9c6e3d35c55bb37c932952987ea4 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/dbcredspath.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=814f2d57a9e8b1bc18c6ac66912baab5 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/dbcredspath.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=99cf80d6833df864fe3e1fd0d594f456 2500w" />

<Accordion title="Accessing Database Credentials">
  Database Credentials can be accessed from the Aptible Dashboard by selecting the respective Database > selecting "Reveal" under "Credentials"

    <img src="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_Database_Credentials.png?fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=7799b2561a44e7b3df7aa7cc9f415141" alt="" data-og-width="2800" width="2800" data-og-height="2142" height="2142" data-path="images/App_UI_Database_Credentials.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_Database_Credentials.png?w=280&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=86b7e798c0c78eb2549ba2830f8a0ea7 280w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_Database_Credentials.png?w=560&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=086eb3e51353ad47b04a44c65076aaa7 560w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_Database_Credentials.png?w=840&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=d660672d188df537ee200143a81514e6 840w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_Database_Credentials.png?w=1100&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=2fc0a6cad414ac5ee5c64e6b8d3b0ce8 1100w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_Database_Credentials.png?w=1650&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=44dc9898f2945bb6497b76f07fddb2d3 1650w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_Database_Credentials.png?w=2500&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=70de68fe2c29539525e17dc21d6d973e 2500w" />
</Accordion>

# Connecting to a Database using Database Credentials

There are three ways to connect to a Database using Database Credentials:

* **Direct Access:** This set of credentials is usable with [Network Integrations](/core-concepts/integrations/network-integrations). This is also how [Apps](/core-concepts/apps/overview), other [Databases](/core-concepts/managed-databases/overview), and [Ephemeral SSH Sessions](/core-concepts/apps/connecting-to-apps/ssh-sessions) within the [Stack](/core-concepts/architecture/stacks) can contact the Database. Direct Access can be achieved by running the `aptible db:url` command and accessing the Database Credentials from the Aptible Dashboard.
* **Database Endpoint:** [Database Endpoints](/core-concepts/managed-databases/connecting-databases/database-endpoints) allow users to expose Aptible Databases on the public internet. When another Database Endpoint is created, a separate set of Database Credentials is provided. Database Endpoints are useful if, for example, a third party needs to be granted access to the Aptible Database. This set of Database Credentials can be found in the Dashboard.
* **Database Tunnels:** The `aptible db:tunnel` CLI command allows users to create a [Database Tunnel](/core-concepts/managed-databases/connecting-databases/database-tunnels), which provides a convenient, ad-hoc method for users to connect to Aptible Databases from a local workstation. Database Credentials are exposed in the terminal when you successfully tunnel and are only valid while the `db:tunnel` is up. Database Tunnels persist until the connection is closed or for a maximum of 24 hours.

<Tip>
  The Database Credentials provides credentials for the `aptible` user, but you can also create your own users for database types that support multiple users, such as PostgreSQL and MySQL. Refer to the database's own documentation for detailed instructions. If setting up a restricted user, review our [Setting Up Restricted User documentation](https://www.aptible.com/docs/core-concepts/managed-databases/connecting-databases/database-credentials#setting-up-a-restricted-user) for extra considerations.
</Tip>

Note that certain [Supported Databases](/core-concepts/managed-databases/supported-databases/overview) provide multiple credentials. Refer to the respective Database documentation for more information.

# Connecting to Multiple Databases within your App

You can create multiple environment variables to store multiple database URLs, utilizing different variable names for each database. These can then be used in a database.yml file. The Aptible platform is agnostic as to how you store your DB configuration, as long as your are reading the added environment variables correctly.

If you have additional questions regarding configuring a Database.yml file, please contact [Aptible Support](https://app.aptible.com/support)

# Rotating Database Credentials

The only way to rotate Database Credentials without any downtime is to create separate Database users and update Apps to use the newly created user's credentials. Additionally, these separate users limit the impact of security vulnerabilities because applications are not granted more permissions than they need.

While using the built-in `aptible` user may be convenient for Databases that support it (MySQL, PostgreSQL, MongoDB, Elasticsearch 7). Aptible recommends creating a separate user that is granted only the minimum permissions required by the application.

The `aptible` user credentials can only be rotated by contacting [Aptible Support](https://contact.aptible.com). Please note that rotating the `aptible` user's credentials will involve an interruption to the app's availability.

# Setting Up a Restricted User

Aptible role management for the Environment is limited to what the Aptible user can do through the CLI or Dashboard; Database user management is separate.

You can create other database users on the Database with CREATE USER . However, this can lead to exposing the Database so that it can be accessed by this individual without giving them access to the aptible database user’s credentials. Traditionally, you use aptible db:tunnel to access the Database locally, but this command prints the tunnel URL with the aptible user credentials. This can lead to two main scenarios:

### If you don’t mind giving this individual access to the aptible credentials

Then you can give them Manage access to the Database’s Environment so they can tunnel into the database, and use the read-only user and password to log in via the tunnel. This is relatively easy to implement and can help prevent accidental writes but doesn’t ensure that this individual doesn’t login as aptible. The user would also have to remember not to copy/paste the aptible user credentials printed every time they tunnel.

### If this individual cannot have access to the aptible credentials

Then this user cannot have Manage access to the Database, which removes db:tunnel as an option.

* If the user only needs CLI access, you can create an App with a tool like psql installed on a different Environment on the same Stack. The user can aptible SSH into the App and use psql to access the Database using the read-only credentials. The Aptible user would require Manage access to this second Environment, but would not need any access to the Database’s Environment for this to work.
* If the user needs access from their private system, then you’ll have to create a Database Endpoint to expose the Database over the internet. We strongly recommend using [IP Filtering](https://www.aptible.com/docs/core-concepts/apps/connecting-to-apps/app-endpoints/ip-filtering#ip-filtering) to restrict access to the IP addresses or address ranges that they’ll be accessing the Database from so that the Database isn’t exposed to the entire internet for anyone to attempt to connect to.
