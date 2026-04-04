# Curator Documentation

Source: https://docs.curator.interworks.com/llms-full.txt

---

# Cache Warming
Source: https://docs.curator.interworks.com/best_practices/performance/cache_warming

Improve initial page load times by pre-warming caches for better user experience

Sometimes the initial page load or log in flow for your users can be very slow. This is because we must perform API
calls to check if the user has permission to see each navigation item related to analytic content. Single API calls are
fast but when your menu is large and many calls must be made it can really anchor the load time.

This feature allows you to choose a select group of Curator users to warm the cache for. This improves the initial page
load and skips the long wait caused by permission checks. The affect is even greater if your menu is very large.

## Setting Up the Group

First, we need to make sure you have a Frontend Group that contains the users needing their cache warmed. This Frontend
Group needs to have less than 200 users because this process is intensive. Increasing the number of users could clog the
queue and hurt performance. We're still playing with the sweet spot for number of users so this may change in the future.

1. Navigate to your Curator backend > Settings > Users > Frontend Groups. If you already have a group with less than
   200 members that contains the users you’d like to receive the speed bump, you’re good to go and can skip to “Setting
   Up the Feature”! Otherwise, hit the “New Frontend Group” button:
2. Give your group a name:
3. Either manually select users in the “Group Members” section or choose a group from one of your analytic platforms in
   the sections below:
4. Hit “Save!”

## Enabling Cache Warming for your Group

1. Navigate to your Curator backend > Settings > Curator > Portal Settings > Features tab:
2. Enable the “Cache Warming” feature at the top of the Functionality section:
3. Choose the Frontend Group we created earlier.
4. Hit “Save!”


# Menu Tuning
Source: https://docs.curator.interworks.com/best_practices/performance/menu_tuning

Optimize menu system performance with tips and configuration recommendations

## Menu Overview

While Curator’s menu system is about as streamlined as possible, there are some tips and tricks you can use to tune its
performance if fancy yourself as a Vin Diesel type. Most of the delays Curator clients see when rendering their
navigation relates to the permission checking that ensures each user only sees the links they have access to view. One
of the big selling points with Curator is that it inherits permissions from the connected platforms by default, so this
is a necessary step. The good news is that Curator does cache all of those permission checks, so it’s really only an
issue when users first log in to Curator for the day. However, that’s also the first impression users get to your
Curator portal, so it’s understandable that this should be as fast as possible. With a little thought, this is where
performance gains can be realized.

## The Obvious Stuff

The first thing to check is always that Curator and any platforms it is connected to are running at full speed. If your
Tableau Server is underpowered or is being bombarded by users, that will slow down the permission checks Curator needs
to make. Same goes if the network connection between Curator and the other platforms is handled by letter-carrying
snails instead of bullet train-esque transfers. Lastly, the most common cause of general performance issues with Curator
itself is file system speed. If the storage mounted to your Curator server runs through the laziest of digital
stonemasons hand chiseling each bit on the drive platters, it’s going to slow down things like Curator’s caching system
and generally make life unbearable. Many times, the file system itself is fast but malware detection running on the
server prevents it from running at full speed.

## Short-Circuiting

Let’s say your main navigation is organized by high level categories. If most of your users only have access to one or
two of those categories, then it doesn’t make sense to check permissions on each link under the others. By using
Curator’s restrict access functionality, you can set which groups have access to each category and this will essentially
short circuit the permission checking for any top-level categories where the user is restricted.

For instance, if you have a category for human resources and you set its restrict access to only allow users in the HR
group, any user who isn’t in the HR group will skip checking the links under the human resources category. Any
permission checks that get skipped means the navigation will render that much faster.

## Utilizing Landing Pages

If you’ve got hundreds or thousands of links in your navigation and can’t use the short-circuiting approach above, then
you could try creating landing pages for sections of the navigation to reduce the number of links it needs to check
permissions against.

Using the same human resources example, you could create a human resources page that has links to the various human
resources content using the built-in tiles or lists. When you add this page to the navigation, Curator only has to check
whether the user is allowed to see that page, which should be quick. Only when a user clicks to open that human
resources page will Curator check permissions for each of those links on the page. If you repeat this for several
sections of the navigation, it really cuts down on the number of permission checks the menu system needs to make before
showing the home page.
Combining Tableau Workbooks

The way Curator checks permissions for Tableau is by getting the list of workbooks a user has access to on a per site
basis and then checking which dashboards are in each of those workbooks. This means that if you have a million
dashboards and they are all in their own workbook, Curator is going to have to make a million API (application
programming interface – or a fancy way to say that Curator is talking to Tableau) calls to Tableau just to determine
whether a link should be shown in the navigation. On the other hand, if you combined those into a single workbook with a
million dashboards, Curator would only have to make one API request to Tableau to check. While your network connection
and Tableau Server might be supercharged, there will always be overhead delays when increasing the number of API calls
over the web. By minimizing the number of API calls, you’ll see better performance.

## Combining Tableau Sites

Tableau sites are wonderful for making sure your various audiences are segregated from each other, since each site is
independent from the others. However, this also means that if you have content published from multiple sites, Curator
has to make separate API calls to check permissions for each one. Like combining your dashboards into fewer workbooks,
combining your workbooks into fewer sites will also see those gains.
Connecting to Tableau Server’s Repository

As mentioned earlier, making API calls between Curator and Tableau incurs some overhead which slows down the process. An
alternative to that is allowing Curator to connect directly to Tableau Server’s underlying database (AKA repository).
This avoids a lot of that overhead. Additionally, Curator is able to create custom queries to pull exactly the
information it needs in a single request. This includes checking all workbooks at the same time as well as only
requiring Curator to authenticate once instead of once per Tableau site. Needless to say, whenever Curator can use the
repository connection instead of the API, it’s able to shave precious seconds off of its quarter mile time.

Unfortunately, connecting to the repository is only possible for Tableau Server; so if you’re using Tableau Cloud, this
won’t be an option for you.

## Warming the Cache (Advanced)

As you’ve probably seen in a lot of motor sports, racers often spin their tires to warm them up before a race. This
increases traction and allows them to go faster around the track. Since Curator uses cache for permission checks, one
way you can make it go faster around the track is to warm its cache at the beginning of each day. In a nutshell, this is
scheduling something each morning to call Curator’s API to generate the navigation for each user before they try to log
in for the first time. When a user does log in for the first time, all of the permission checks will have already been
cached, so Curator can build the navigation fast and furious.

Curator’s API end point can be found at /api/v1/Content/generateNavMenus. You’ll need to pass it a valid API key, the ID
of the menu to generate, and the username to generate it for. Documentation on how to call this API endpoint can be
found by navigating to Backend >Settings >Curator >API Keys, click on one of the keys, and change the drop-downs at the
bottom to “Content” and “generateNavMenus,” respectively.

If you don’t have a good way to schedule API calls, you can take advantage of Curator’s automation scripts. This feature
is disabled by default, so to enable it navigate to Backend >Settings >Curator >Portal Settings >Features tab >
Functionality Section >Integration Automation switch and save. Once enabled, refresh the page and you should see a new
section under Backend >Integrations >Automation to create scripts or commands. This is an advanced topic, so we’ll leave
the rest up to you to implement, but if you want to create a script to call the API you’ll use Manage Scripts. If you
want to issue commands on Curator’s server to call the API, you’ll use Manage Commands. Both can be configured for
whatever schedule makes sense in your environment.


# Password Settings
Source: https://docs.curator.interworks.com/best_practices/security/password_settings

Configure password complexity requirements and security policies for enhanced site security

It’s always a good idea to keep your site as secure as possible. Beyond settings like https, multi-factor authentication
and firewalls, you can now set better password policies. Password complexity options allow you to set stricter rules for
passwords to prevent users from creating weak passwords. Password expiration allows you to require users to change their
passwords on a frequent basis. Let’s take a deeper look into these two settings.

## Password Complexity Options

Password complexity allows you to set rules to require stronger passwords. To enable and configure password complexity
options, go to Backend > Settings > Curator > Portal Settings. Under the general tab, you will find a section called
Security. Expand that, and you can now find the Password Complexity Options toggle. Please note that in order to view
and configure this setting, you must have Password Change or Password Reset settings (or both) enabled, which require
you to use Tableau or Curator as your authentication:

Once you toggle on Password Complexity Options, you will see three different options you can set to require stronger passwords:

It’s a good idea to set a long length requirement, the longer the better, but don’t go too overboard or your users may
want to write their passwords down on a Post-it note attached to their display. The first time you enable this setting,
it will default to 10.

Once enabled, you will now see these requirements on pages that allow you to set a password:

## Password Expiration

Password expiration can be found on the same Portal Settings page and tab, right next to the Password Complexity
Options. Like the prior option we looked at, you must have Password Change or Password Reset enabled to be able to view
password expiration. Click the toggle to enable it, and you will now see you can set the number of days until user
passwords will expire:

If enabled, the login page will check to see if the user’s password is expired and, if so, redirect them to a page to
set a new password. Once this is done, they will be able to log in with the new password.

Setting a prudent expiration date, such as 90 days, and turning on password complexity options are easy, effective ways
to make your Curator portal even more secure.


# Overview
Source: https://docs.curator.interworks.com/creating_integrations/overview

Overview of creating and managing integrations with external platforms in Curator

## Overview

Integrations connect Curator to your business intelligence platforms, allowing
you to embed dashboards, synchronize users, and centralize analytics access.

### What are Integrations?

Integrations (also called "Connections") allow Curator to communicate with external BI platforms. Once configured,
these connections enable you to:

* **Embed visualizations**: Add dashboards and reports from your BI platforms directly to Curator
  by selecting dropdown options
* **Synchronize users**: Keep user access and permissions in sync between Curator and your BI platforms
* **Monitor health**: Automatically detect connection issues and receive email alerts when problems occur
* **Automate tasks**: Schedule data refreshes, run scripts, and execute platform-specific commands

### How Connections Work

Each connection stores the server details and authentication credentials needed to communicate with the external
platform. Curator securely encrypts sensitive information and continuously monitors connection health to ensure
reliable access to your analytics. Follow the platform-specific setup guides to create and configure the
connection to your BI tool.

### Supported Platforms

Curator supports integrations with the following platforms:

* [Tableau Cloud](/creating_integrations/tableau_connection/tableau_cloud_setup)
* [Tableau Server](/creating_integrations/tableau_connection/creating_a_connection)
* [Power BI](/creating_integrations/power_bi_connection/azure_app_setup)
* [ThoughtSpot](/creating_integrations/thoughtspot_connection/integrating_thoughtspot_with_curator)
* [Sigma Computing](/creating_integrations/sigma_connection/creating_a_sigma_connection)


# Azure Admin Registered App Setup
Source: https://docs.curator.interworks.com/creating_integrations/power_bi_connection/azure_admin_app_setup

Step-by-step guide to set up Azure application registration for Power BI's Admin API integration with Curator.

## Steps

<PowerBIConnectionSteps />

## Creating a registered app for the admin API within the Azure Portal

This will be a very similar process to creating the non-admin registered app in the previous step, but this registered app will
be used for authentication to the read-only Power BI **Admin API** for Curator to be able to check permissions, etc. on behalf of
Power BI users.

1. Log in to the [Azure Portal](https://portal.azure.com);
2. Search for “App Registrations” to start the process.  You may also find them inside the *Microsoft Entra ID* > *Manage* > *App Registrations*.
3. Click the button to register a new application.
4. Add a distinct and descriptive name. It's suggested to clarify that this is for the Admin API (e.g. "Curator Power BI Admin API App").
   * You should skip the "Redirect URI" step for this registered app as it will not be used.
     <Note>Make sure to create this app registration under the same Azure tenant as the non-admin registered app created previously.</Note>
5. Once the app is registered, make note of the following details from the “Overview” page as you will need them when
   setting up the configuration on Curator:
   * Application (client) ID - This will be used as the **Admin Client ID** in Curator.
   * Directory (tenant) ID - This should be the same as the tenant ID used for the registered app.

## API Permissions

<Warning>Do **not** add any API permissions to this registered app.  It does not need permissions assigned in order to access
the read-only admin APIs, and in fact adding them will actually prevent it from being able to access those APIs.</Warning>

## Create a Client Secret

1. While still viewing the admin registered app, click on *Manage* > *Certificates & secrets* in the left navigation.
2. Click the button to add a new client secret.  This will be used as the **Admin Client Secret** in Curator.
3. Fill in the description and adjust the expiration date as desired, and click the save button.
4. Copy the client secret **value** and document it in a secure place.
   <Info>You will not be able to retrieve the value again once you leave this screen.</Info>
   <Warning>Do not confuse this with the *Secret ID*.  Curator must have the secret *value* to authenticate.</Warning>


# Azure Registered App Setup
Source: https://docs.curator.interworks.com/creating_integrations/power_bi_connection/azure_app_setup

Step-by-step guide to set up Azure application registration for non-admin Power BI integration with Curator.

## Steps

<PowerBIConnectionSteps />

## Creating a Registered App within the Azure Portal

This registered app will be used for authentication to the Power BI non-admin APIs on behalf of users accessing Power BI content within Curator.

1. Log in to the [Azure Portal](https://portal.azure.com);

2. Search for “App Registrations” to start the process.  You may also find them inside the *Microsoft Entra ID* > *Manage* > *App Registrations*.

3. Click the button to register a new application.

4. Give the app a distinct and descriptive name and provide a redirect URI during this process under the "Web" platform.  The redirect URI should follow
   this format:

   `https://curatorexample.com/powerbi`

   <Warning>
     If the redirect URI is not configured correctly, users will see an error like:

     `AADSTS50011: The redirect URI specified in the request does not match the redirect URIs configured for the application.`

     **To fix this:**

     1. Go to [Azure Portal](https://portal.azure.com)
     2. Find your app registration
     3. Click **Manage** > **Authentication (Preview)** in the left navigation
     4. Add a **Web** redirect URI using your Curator portal's domain with the `/powerbi` suffix (e.g., `https://curatorexample.com/powerbi`)
   </Warning>

5. Once the app is registered, make note of the following details from the “Overview” page as you will need them when
   setting up the configuration on Curator:
   * Application (client) ID
   * Directory (tenant) ID
   * Application ID URI

## API Permissions

Your InterWorks Curator Azure Registered App will need several delegated API permissions.  While still viewing the
registered app, click on *Manage* > *API permissions* in the left navigation.  Add the following permissions as delegated
permissions:

* Microsoft Graph
  * User.Read
* Power BI Service
  * Dashboard.Read.All
  * Dataset.Read.All
  * Report.Read.All
  * Workspace.Read.All

If you intend to use **persistent filters** or other functionality that tracks user state, you'll also need to add:

* Power BI Service
  * UserState.ReadWrite.All

<Note>
  Depending on your level of access, you may need to ask Azure administrators to grant admin consent for these permissions.
</Note>

## Create a Client Secret

1. While still viewing the registered app, click on *Manage* > *Certificates & secrets* in the left navigation.
2. Click the button to add a new client secret.
3. Fill in the description and adjust the expiration date as desired, and click the save button.
4. Copy the client secret **value** and document it in a secure place.
   <Info>You will not be able to retrieve the value again once you leave this screen.</Info>
   <Warning>Do not confuse this with the *Secret ID*.  Curator must have the secret *value* to authenticate.</Warning>


# Curator Connection
Source: https://docs.curator.interworks.com/creating_integrations/power_bi_connection/curator_connection

Final setup steps to create and configure the Power BI connection within Curator backend.

## Steps

<PowerBIConnectionSteps />

## Creating Curator Connection to Power BI

Note: You will need details from your non-admin registered app and your admin registered app.  See steps 1-3 above if you have not configured those yet.

If your Curator license allows you to connect to Power BI, you can connect to it by following this process:

1. <BackendNavPath />
2. Click the button at the top to create a new connection.
3. From here, fill out the details under the *Power BI Connection* section, then click save.  The first 3 fields need to be
   filled in, but the 2 admin fields are highly recommended because they will lead to a better overall experience.

   * **Client ID**: "Application (client) ID" from the non-admin registered app (see [Azure App Setup](/creating_integrations/power_bi_connection/azure_app_setup)).
   * **Tenant ID**: "Directory (tenant) ID" from the non-admin registered app (see [Azure App Setup](/creating_integrations/power_bi_connection/azure_app_setup)).
   * **Client Secret**: "Client secret" value (again, not the client secret ID) from the non-admin registered app (see [Azure App Setup](/creating_integrations/power_bi_connection/azure_app_setup)).
   * **Admin Client ID**: "Application (client) ID" from the *admin* registered app (see [Azure Admin App Setup](/creating_integrations/power_bi_connection/azure_admin_app_setup)).
   * **Admin Client Secret**: "Client secret" value (again, not the client secret ID) from the *admin* registered app (see [Azure Admin App Setup](/creating_integrations/power_bi_connection/azure_admin_app_setup)).
4. Refresh the page after saving and you should see a Power BI section show up in the left navigation.

### Validate a successful connection

* The admin registered app connection was successful if the dropdowns in the backend under **Power BI** > **Reports** >
  **Create** a new report populate.
* The non-admin registered app connection was successful if reports load in the frontend.  Be sure to log out of the frontend and log back in fresh.

If you run into any issues, you can refer to the [Troubleshooting Power BI Access](./troubleshooting_power_bi_access) documentation for help.


# Power BI Workspace Access
Source: https://docs.curator.interworks.com/creating_integrations/power_bi_connection/power_bi_workspace_access

Configure workspace permissions for Power BI integration with Curator.

## Steps

<PowerBIConnectionSteps />

## A Note on Terminology

The terms "registered app", "service principal", and "client" are technically not the same thing, however, for the
purposes of this documentation you can think of them as the same thing.  Similarly, "Power BI" and "Fabric" can also be
considered the same things for the purposes of this documentation. If you already understand the differences, you
probably also understand how to adjust the steps outlined in this documentation to meet your own needs.

## Allow service principals to use Fabric APIs

The registered apps created in the previous steps need to be able to access Power BI APIs in order to query which
workspaces, Dashboard, reports, etc. exist in your environment when publishing content to Curator.

To enable the Power BI APIs:

1. Log in to the [Power BI portal](https://app.powerbi.com) with an account that has access to the admin portal.
2. Navigate to the [admin portal](https://app.powerbi.com/admin-portal) by clicking on the gear icon at the top right.
3. Select "Tenant Settings" on the left if not already selected.
4. Scroll to the "Developer settings" section and expand the "Allow service principals to use Fabric APIs" group.
5. Click the switch to enable.  If desired, restrict access to only specific security groups (make sure the registered
   apps that Curator will be using are included in a security group specified here).
   <Note>Enabling this setting may take \~15 minutes to take effect.</Note>

## Allow service principals to access read-only admin APIs

The admin registered app needs read-only access to the Power BI Admin APIs in order to query permissions, etc. on behalf of
Power BI users.

To enable the read-only admin APIs:

1. Log in to the [Power BI portal](https://app.powerbi.com) with an account that has access to the admin portal.
2. Navigate to the [admin portal](https://app.powerbi.com/admin-portal) by clicking on the gear icon at the top right.
3. Select "Tenant Settings" on the left if not already selected.
4. Scroll to the "Admin API settings" section and expand the "Service principals can access read-only admin APIs" group.
5. Click the switch to enable.  If desired, restrict access to only specific security groups (make sure the admin registered app that Curator will be using is included in a security group specified here).
   <Note>Enabling this setting may take \~15 minutes to take effect.</Note>

## Add Registered Apps to Power BI Workspace(s)

In order for the non-admin and admin registered apps to have access to your Power BI content, they must have
permissions to the Power BI workspace(s) you intend to use with Curator.

To add access to a workspace:

1. Log in to the [Power BI portal](https://app.powerbi.com).
2. In the left navigation, click on “Workspaces”.
3. Hover your mouse over one of the workspaces and click on the 3 dots that appear on the right.  Choose “Workspace access”.
4. Search for the non-admin registered app name and give it the "Admin" permission.  This ensures Curator will
   have access to add any content from Power BI that your Curator admins would like to add.
5. Repeat step 4 for the admin registered app name, also giving it "Admin" permission.
6. (optional) Repeat steps 2-5 for any remaining workspaces that need access.

<Note>
  There are other paths to get to the screens mentioned above, but there have been times when those paths
  don't work correctly. The steps above are the most reliable way to get to the correct screens.
</Note>


# Troubleshooting Power BI Access
Source: https://docs.curator.interworks.com/creating_integrations/power_bi_connection/troubleshooting_power_bi_access

Common issues and solutions for Power BI connection problems in both frontend and backend access scenarios.

Power BI connections have separate frontend and backend functionality, even though everything is configured from the
backend connection. When troubleshooting issues, it's important to test each area separately since one might work
perfectly while the other fails completely.

***

## Backend Troubleshooting

The backend integration with Power BI is straightforward - there's one reliable way to test it and only a few common
failure points.

### Test if Backend is Working

Follow these steps to verify your backend connection:

1. <BackendNavPath />

2. Click the **Clear Cache** button (top right) to ensure fresh data.

3. Click the **New Report** button to navigate to the "Create Report" page.

4. Use the dropdown menus to select a workspace and report

   * **Success:** If you can select both workspace and report, your backend is working! Skip to the
     [Frontend section](#frontend-troubleshooting)
   * **Problem:** If either dropdown is empty when it shouldn't be, continue to the troubleshooting steps below

<img alt="Power BI Backend Success" />

### Debug Backend Issues

When the backend isn't working, you need to see what Power BI is actually telling Curator.

#### Enable Debug Mode

1. <BackendNavPath /> Find your Power BI connection and click the one you'd like to troubleshoot.

2. **Enable debugging**
   Toggle on **Debug Mode for Power BI** and click save

   <Warning>
     Debug mode increases logging and can fill up your server. Set a reasonable **Debug Mode Expiration**
     (default: 24 hours).
   </Warning>

3. **Repeat the steps to recreate the issue**
   Follow the steps in [Test if Backend is Working](#test-if-backend-is-working) again to recreate the issue while
   debug logging is enabled.

4. **Check the logs:**
   1. <BackendNavPath />

   2. **Find Power BI calls**
      Filter for `Power BI API Call` using the search box (top right)

   3. **Review responses**
      Click on entries to see Power BI's detailed responses

For more information about Curator's logging systems, see the [Logging Overview](/site_administration/logging/logging_overview).

#### Common Solutions

**If you see error messages:**
The solution depends on the specific error. Contact Curator support if the fix isn't obvious.

Some errors may be prefixed with `POWER BI ERROR` or `ERROR during powerbi flow`, but others may have different text.

**If responses are blank:**
This means Curator can connect to Power BI, but the admin registered app (or non-admin registered app if not using admin)
lacks workspace access. Try these fixes:

##### 1. Grant workspace access

Follow the [Add Registered App to Power BI Workspace(s)](/creating_integrations/power_bi_connection/power_bi_workspace_access)
instructions

##### 2. Enable Fabric APIs

Follow the [Allow service principals to use Fabric APIs](/creating_integrations/power_bi_connection/power_bi_workspace_access)
instructions
*(Note: This change can take time to take effect in Power BI)*

##### 3. Check security groups

If Fabric APIs are restricted to specific security groups, ensure your registered apps are a member of one of those
groups.

***

## Frontend Troubleshooting

Once your backend connection works and you've published Power BI content to Curator's navigation, users should be able
to access it seamlessly.

### Expected User Flow

When everything is configured correctly (following [setup steps 1-4](/creating_integrations/power_bi_connection/azure_app_setup)),
users should experience:

1. **Log in to Curator**
   Using the method configured in your [Authentication Settings](/setup/authentication/overview).

2. **Authenticate with Power BI**
   *(This may happen automatically with SSO)*

3. **Access content**
   Curator displays all accessible content based on platform permissions:

   * Tableau content: controlled by Tableau
   * ThoughtSpot content: controlled by ThoughtSpot
   * Power BI content: controlled by Power BI

   <Note>
     Curator can add additional restrictions but cannot expand access beyond what the source platform allows.
   </Note>

### Debug Frontend Issues

If users see other Curator content but Power BI content is missing from navigation, follow these steps:

#### Verify Power BI Authentication

1. **Enable frontend debug mode**
   Follow the steps to [enable frontend debug mode](/site_administration/performance/troubleshooting_load_times).

   <Tip>Remember to disable this after troubleshooting.</Tip>

2. **Add debug parameter**
   In your browser, add `?debug=1` to the URL
   * Example: `https://curator.yourcompany.com/` becomes `https://curator.yourcompany.com/?debug=1`
     <Note>If URL already has a `?` character in it, use `&debug=1` instead</Note>

3. **Check session data**
   * Look for the debug bar at the bottom of the screen
   * Click **Session** tab
   * Look for a **`powerbi`** > **`user`** entry to ensure it has an "accessToken" value.

4. **Interpret results**
   * **Missing entry:** Authentication failed → Log out and log back into Curator
   * **Valid entry:** Authentication succeeded but Power BI reports no accessible content → Continue to next section

#### Check Power BI API Responses

1. <BackendNavPath /> From this list, find the Power BI connection you're troubleshooting and click to open it.  Enable the
   **Debug Mode for Power BI** toggle under the "Debug" section and save the connection.

   <Warning>
     This increases logging significantly. Set a reasonable **Debug Mode Expiration** (default: 24 hours).
   </Warning>

2. **Clear cache:**
   Click **Clear Cache** button (top right) to force fresh API calls.

3. **Refresh frontend:**
   Go back to Curator's frontend and refresh the page.

4. **Check API logs:**
   If Power BI content still doesn't appear:
   * <BackendNavPath />
   * Look for Power BI API calls
   * Click entries to view detailed responses

5. **Get support:**
   API responses can be complex. Send the details to Curator support for analysis. Meanwhile, verify the user has
   proper access to the Power BI workspace and content in question.

#### Redirect URI Mismatch (AADSTS50011)

If you see an error containing `AADSTS50011: The redirect URI specified in the request does not match the redirect URIs
configured for the application`, the Azure app registration is missing the correct redirect URI.

**To fix this:**

1. Go to the [Azure Portal](https://portal.azure.com) and find your app registration
2. Click **Manage** > **Authentication (Preview)** in the left navigation
3. Under the **Web** platform, add a redirect URI using your Curator portal's domain with the `/powerbi` suffix
   * Example: `https://curatorexample.com/powerbi`
4. Save the changes
5. Log out and log back in to Curator to verify the fix


# Alternative URL Routing
Source: https://docs.curator.interworks.com/creating_integrations/tableau_connection/alternative_url_routing

Configure URL routing for Tableau Server connections when using reverse proxies or alternative network configurations.

Curator connects to Tableau Server to verify a user's access and permissions.

Sometimes, Tableau Server is configured to live behind a "Reverse Proxy".
There are many reasons why this configuration may be preferable.

Often, though, Reverse Proxy setups with Tableau are misconfigured.
This can lead to trusted ticket whitelisting issues.

Since the Tableau Server whitelisting for issuing a trusted ticket is based on an IP address, when proxies are
misconfigured, Tableau Server sees the proxy/load balancer, instead of Curator and rejects the ticket request.

Tableau Server requires
[tsm configuration options, gateway whitelisting and several headers](https://help.tableau.com/current/server/en-us/proxy.htm#configure-the-reverse-proxy-server)
for these API calls to work correctly.

## Working Around Reverse Proxy Setups

Usually, instead of fixing Tableau Server Reverse Proxy setups, routing Curator around them is quicker and easier.

Of course, end users should continue to be routed over the reverse proxy/load balancer.

**To configure alternative routing:**

* Go to **Integrations** > **Connections** and click on your Tableau Server connection.
* Place the *internal route* to Tableau Server in *Tableau Server URL*.
* Place the user-facing route to Tableau Server in *Alternate Tableau Server URL*.

<img alt="Reverse Proxy Alt URL" />


# Creating a Tableau Connection
Source: https://docs.curator.interworks.com/creating_integrations/tableau_connection/creating_a_connection

Learn how to connect Curator to your Tableau Server or Tableau Cloud site using REST API for seamless dashboard integration.

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


# Embed Authentication
Source: https://docs.curator.interworks.com/creating_integrations/tableau_connection/embed_authentication

Configure secure authentication methods for embedding Tableau dashboards in Curator with single sign-on options.

Embedded Authentication is how we securely connect users on the frontend to their Tableau Dashboards. Depending
on your selected method it automatically establishes a single sign-on experience or requires additional configuration
outside of Curator to avoid a second login screen to authenticate to Tableau.

Different authentication methods are available, including:

* [Connected Apps (Recommended)](#connected-apps-recommended)
* [Tableau Default Authentication](#tableau-default-authentication)
* [Trusted Tickets (Deprecated - End of Life in October 2025)](#trusted-tickets-deprecated---end-of-life-in-october-2025)

This article will guide you through setting up Embed Authentication using these methods.

## Connected Apps (Recommended)

Connected Apps establish a trusted relationship between Curator and Tableau, enabling secure authentication for
embedded Tableau content and REST API access. Unlike Trusted Tickets and Tableau Default Authentication, Connected
Apps do not depend on third-party cookies, which are increasingly being blocked by modern web browsers.

### Troubleshooting

The following scenarios have been encountered during the process of updating an existing connection to use Connected
Apps. We have added the steps to resolve here.

> * Trying to save my connection, I get an error message that contains:
>   `Missing Site <your site> from the list of secondary site.`

Curator detected that you are embedding Dashboards from multiple sites but not all the sites have been added to your
connection so far. Use the **Secondary Sites** section to add an item for each individual site. Curator requires
a separate Connected App for each individual site!

> * The details of the Connected App show blank.

If you are updating a Trusted Ticket connection, cached data may cause display issues. Clear the backend cache and
reload the Connection page.  If this issue persists, please reach out to Curator support.

> * Trying to save my connection, I get an error saying
>   `A syntax error was detected in <some fields.yaml> .. No such file or directory`

Clear the cache from the backend and apply the changes again. Hit save and the connection should be updated.

> * My Dashboards load indefinitely when trying to access them in the frontend.

The browser may be storing outdated settings or old Tableau session data. If you can log in and access the Dashboard
using an Incognito Window, then your users will need to hard-refresh their browsers, or clear
site site cookies.
If not, this issue generally resolves itself after 24 hours, so it's helpful to consider upgrading to connected apps
just prior to the weekend.

> * When accessing the Dashboard in the frontend, I get a 401.

Follow the steps in the *My Dashboards load indefinitely* section to resolve.

> * After updating my dev environment, my prod environment stopped working

If both Curator environments (test/dev and production) connect to the same Tableau Server, switching between Trusted
Tickets and Connected Apps can cause cookie conflicts when migrating one instance after the other. To prevent issues:

* Test each environment in a separate browser or incognito window.
* Ensure users testing Connected Apps clear their cookies before switching to the production environment again.

If further issues persist, reach out to your friendly Curator support team.

### Requirements

* Connected Apps are supported on
  * **Tableau Cloud**
  * **Tableau Server version 2022.4 and higher**.
* The Service Account User must be a
  * **Site Admin** on Tableau Cloud and
  * **Server Admin** on Tableau Server (Site Admin cannot manage Connected Apps on Tableau Server!)
* Both **Tableau Server and Curator must use SSL** to establish a trusted relationship.

*Note:* You can set up Connected Apps with either Service Username and Password or Personal Access Token.

### Setup

To set up Embed Authentication using Connected Apps you need to have an existing Connection to either Tableau Cloud or
Tableau Server. If not, follow our
[Tableau Connection setup guide](/creating_integrations/tableau_connection/creating_a_connection).

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Navigate to Integrations > Connections and select your Tableau connection that you want to set up Connected Apps for.
3. Scroll down to the ***Embed Authentication*** section and expand it.
4. Select **Connected Apps**.
5. Save the Connection.

After saving, Curator will create the Connected App and display following details:

* Primary Site Connected App
* Client ID & Secret - the secret is obfuscated, but a placeholder represents successful retrieval
* Creation Timestamps

If multiple Connected Apps are detected, you can select in the Primary Site Connected App dropdown which one to
use. All other fields are automatically populated and show information for troubleshooting purposes only.
If you are embedding Dashboards from multiple sites add each additional site you'd like to
connect Curator to under *Secondary Sites* ensuring each has its own Connected App.

### Allowed Domains - additional configuration option on Tableau Server/Cloud

Connected Apps can be configured to allow embedding from a specified domain only. You can find more details on
Tableau's Connected Apps in their
[Knowledge Base](https://help.tableau.com/current/online/en-us/connected_apps_direct.htm).

## Tableau Default Authentication

Using Tableau Default Authentication for your Embed Authentication mechanism means that your users will either be
prompted with a Tableau login screen when accessing a Dashboard, or you need to configure your own SSO mechanism
(e.g. SAML, OAuth, Active Directory etc.) to enable seamless authentication.

For organizations that require an integrated authentication experience, we **strongly recommend** using
**Connected Apps** instead of relying on Tableau Default Authentication.

## Trusted Tickets (Deprecated - End of Life in October 2025)

**IMPORTANT:** Trusted Tickets are deprecated and will be removed from Curator in October 2025. From that point,
Curator will no longer support issuing Trusted Tickets or using the associated JavaScript API.

For more information about Trusted Ticket authentication, please refer to our documentation article
[Creating Integrations: Tableau Connection - Trusted Authentication](/creating_integrations/tableau_connection/trusted_authentication).


# Tableau Cloud Setup
Source: https://docs.curator.interworks.com/creating_integrations/tableau_connection/tableau_cloud_setup

Configure Tableau Cloud with Curator using connected apps for secure authentication and seamless dashboard integration.

## Creating a new Connection

Follow the steps in the [Tableau Connection Setup](/creating_integrations/tableau_connection/creating_a_connection)
section to get connected to your Tableau Server.

## Connected Apps

As of the `01-04-23` Curator release, Tableau's connected apps are now supported as a method of authentication.
This means SSO is no longer required to support a seamless authentication experience for Tableau Cloud users.  All
Tableau Cloud connections in Curator utilize connected apps.  Curator will create a connected app on your Tableau Cloud
site if one doesn't already exist.  You may switch which connected app Curator uses if you need.

For more information and a troubleshooting guide, refer to our article about
[Creating Integrations: Tableau Connection - Connected Apps](/creating_integrations/tableau_connection/embed_authentication)

## Custom Domains

In the August 2025 release of Tableau Cloud, Tableau introduced the ability to use custom domains (also known as vanity
URLs). This feature primarily circumvents the need for users to modify their browser's cookie settings to allow
third-party cookies, creating a truly seamless authentication experience when accessing Tableau dashboards via Curator.
*This feature is only available in Curator versions `2025-10-02` and later.*

### Setting up a Custom Domain on Tableau Cloud

To set up a custom domain on Tableau Cloud, follow the [instructions provided by Tableau](https://help.tableau.com/current/online/en-us/custom_domain.htm).

### Adding your Custom Domain to Curator

Once your custom domain is set up and verified on Tableau Cloud, add your custom domain to Curator  to add it to Curator
to ensure seamless integration.  Begin by navigating to your Tableau Cloud connection in Curator.  Then, follow these
steps:

1. <BackendNavPath /> Click on the Tableau connection you'd like to modify.

2. In the **Tableau Connection** section, enter your custom domain URL in the **Custom Domain** field.

3. Confirm that Curator can reach the domain, and that there are no warnings:
   <img alt="Custom Domain Success" />

4. Click **Save** to apply your changes.

Now when users access embedded Tableau Cloud dashboards they will be loaded through your Custom Domain in Curator.


# Tableau Connection Troubleshooting
Source: https://docs.curator.interworks.com/creating_integrations/tableau_connection/tableau_connection_troubleshooting

Debug and resolve common Tableau connection issues including networking problems, authentication errors and API connectivity.

When setting up Curator's connection to Tableau, or dealing with unexpected networking or feature related issues, it's
beneficial to understand how to get details on the issues you're facing to help narrow down root-causes.  Whether you're
managing a Curator site need to understand how to enable Debug Mode to view the data returned from Tableau, or you're
a developer or system administrator working with Tableau Server and need to understand how to use Postman to make API
calls to ensure your Curator and Tableau Server can communicate with one another, you'll find all you need below.

## Tableau API Debugging

Sometimes there are issues that are hard to diagnose without seeing exactly which API calls Curator is making to Tableau
and what responses Curator is getting back from Tableau.  To log all of those API calls, Curator provides a
**Debug Mode for Tableau Server**.

### Side Effects

A word of warning though, when this debug mode is enabled, the amount of logging that takes place is drastically
increased and may fill up your server if left on for long periods.  Be sure to turn it back off once you've logged
enough to diagnose the issue.

For more information about Curator's logging systems, see the [Logging Overview](/site_administration/logging/logging_overview).

### How to Enable Debug Mode

To turn on Curator's **Debug Mode for Tableau Server**:

1. Navigate to Backend > Settings > Tableau > Tableau Server Settings > Advanced tab.
2. Toggle on the switch labeled Debug Mode for Tableau Server.
3. Save the settings by using the button in the upper right.

### Using Debug Mode to Troubleshoot

Once Curator's Debug Mode for Tableau Server is enabled, you'll want to recreate the scenario that led to the
troublesome behavior and then view the debug logs by navigating to Backend > Settings > Logs > Event log.

If you don't see the applicable API calls in the logs, you may need to clear Curator's cache by using the Clear Cache
button in the upper right portion of the Backend, and then repeat the steps to recreate the troublesome scenario.

## Using Postman to Test Connection

Sometimes, it's difficult to establish a connection to Tableau and the reason why isn't clear.  One method to help rule
out bugs in Curator is to use the Postman application to directly make the API call.  This document will guide you
through using Postman to authenticate to Tableau's REST API like Curator does behind the scenes.

### Install Postman

The first step is to download and install Postman.  You can get it from:
[https://www.postman.com/downloads/](https://www.postman.com/downloads/)

### Make API Call

Follow these steps to configure a new API call against Tableau's REST API.

1. Open Postman and start a new tab.

2. Enter your Tableau Server/Cloud URL into the URL bar.  Append `/api/3.4/auth/signin`.  Update the API version if
   needed based on [this page](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_versions.htm#tableau-server-versions-and-rest-api-versions1).

3. Change the request type from `GET` to `POST`.

4. Click on the **Body** tab.

5. Select **raw**.

6. In the text box, copy and paste the following XML:

   Username/Password:

   ```xml theme={null}
   <?xml version="1.0" encoding="utf-8"?><tsRequest><credentials name="" password=""><site contentUrl=""/></credentials></tsRequest>
   ```

   Personal Access Token (PAT):

   ```xml theme={null}
   <?xml version="1.0" encoding="utf-8"?><tsRequest><credentials personalAccessTokenName="" personalAccessTokenSecret=""><site contentUrl=""/></credentials></tsRequest>
   ```

7. Fill in the username/password or PAT name/secret, and site content URL details within the above XML.

8. Click the **Send** button.

You should get back XML with a credentials session token and the site and user IDs.

<img alt="Postman Screenshot" />

If needed, use the credentials session token from this response to make subsequent API calls to Tableau.  Open the
headers tab for the request and add an entry where the key is `X-Tableau-Auth` and the value is your credentials session
token.  If this token expires, you'll need to make a new request to the signin end point to get a new token.


# Tableau Server Repository
Source: https://docs.curator.interworks.com/creating_integrations/tableau_connection/tableau_server_repository

Connect directly to Tableau Server repository database for high-volume deployments

Sometimes (but very rarely) you may need to connect directly to Tableau Server's repository.  Generally this is
recommended when your user-count is very high (5000+ users), your Tableau Server connection is dealing with severe
latency that cannot be overcome (making the REST API responses very slow), or you need to enable the password reset
feature.  In these instances you will need to make sure your Tableau Server repository is enabled on Tableau Server first.

## Configuring Tableau Server's Readonly Account

By default, access to the Tableau Server repository is disabled.  To enable it, as well as set the password, you need to
issue a TSM command like the following against your Tableau Server:

```bash theme={null}
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


# Trusted Authentication (Unavailable)
Source: https://docs.curator.interworks.com/creating_integrations/tableau_connection/trusted_authentication

Legacy trusted authentication method for Tableau Server (deprecated)

<Danger>
  This authentication method is deprecated and no longer supported in Curator. Please migrate to Connected Apps or another
  SSO method as soon as possible.
</Danger>

Curator no longer supports Embed Authentication using Trusted Tickets.
**Versions released in October 2025 or later, Trusted Tickets will no longer be supported**.
To ensure uninterrupted Dashboard access, you must migrate to Connected Apps or another SSO method before upgrading to
those versions.

For guidance on transitioning, refer to our [guide on how to setup Connected Apps](/creating_integrations/tableau_connection/embed_authentication).

***

By default, if the Tableau Server workbook views which are embedded in dashboards require a login, the user will be
prompted for their username and password the first time they view any Dashboard.  With trusted ticket authentication
enabled on the system and on the associated Tableau Server, the system will authenticate on behalf of the user.

One drawback to using trusted tickets is that there is a little more overhead to authenticate on behalf of the user
before showing the Dashboard.  Since trusted tickets are one-time use, this authentication takes place before each and
every Dashboard is shown.

This functionality requires that the Tableau Server REST API is enabled which you can
[establish by creating a Tableau Connection](/creating_integrations/tableau_connection/creating_a_connection).

## Enabling Trusted Tickets (Unavailable)

<Warning>
  This feature is no longer supported in Curator as of October 1, 2025, and is for reference purposes only.
</Warning>

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to **Integrations** > **Connections** from the left-hand menu.
3. Click on your Tableau Server from the list view.
4. Expand the *Embed Authentication* Section.
5. Select **Trusted Ticket Authentication** in the drop-down selection box for *Which authentication type will embedded
   dashboards use*.
6. If you have not set up Curator as a trusted host on your Tableau Server, follow the instructions in the dialog box
   that appears below the enabled button.
7. Save the Connection.

**Note:** The dialog box lists out a couple of different trusted hosts to add to Tableau Server. Those include the
server address (Outbound IP), local address, server name and hostname.  These are Curator's best guess at which hosts
requests originating from Curator will be seen by Tableau Server.  Depending on your network configuration, these may
not be correct by the time the request reaches Tableau Server.  Adjust as needed.

**Note:** If you use a reverse proxy or load balancer on the network between Curator and Tableau Server, ***DO NOT***
configure the reverse proxy or load balancer as a *trusted host*.  Reverse proxies or load balancers can be configured
instead as a *trusted gateway* if needed.  However, it's likely that you'll need to configure the reverse proxy or load
balancer to pass through specific headers so Tableau Server can tell that the request comes from Curator.  Instructions
for these headers can be found in [Tableau's documentation](https://help.tableau.com/current/server/en-us/proxy.htm#configure-the-reverse-proxy-server)


# Integrating ThoughtSpot with Curator
Source: https://docs.curator.interworks.com/creating_integrations/thoughtspot_connection/integrating_thoughtspot_with_curator

Connect and integrate your ThoughtSpot instance with Curator for unified analytics access

You can follow this guide to connect to your ThoughtSpot instance to Curator.

## Preparing ThoughtSpot

1. Verify your ThoughtSpot admin has enabled either [SAML SSO](https://developers.thoughtspot.com/docs/saml-sso) or
   [trusted authentication](https://developers.thoughtspot.com/docs/trusted-auth).  If you are using trusted
   authentication, have the *secret\_key* ready to add to the Curator configuration.
2. Verify your ThoughtSpot admin has configured your Curator domain to be
   [whitelisted for CORS and CSP](https://developers.thoughtspot.com/docs/security-settings).
3. Have the credentials for a user with administrator access on the intended Org ready to add to the Curator configuration.

Note: The user with administrator access to the intended Org must also exist on the "Primary" Org. This is due to a
limitation in the ThoughtSpot REST API where we can only query user details when we know the Org ID the user exists
on. The "Primary" Org ID is always the same so we can confidently pull the user details when they exist there, but
other Orgs have randomly generated ID's that aren't available in the ThoughtSpot UI anywhere. While the user must
exist on the "Primary" Org for Curator to be able to pull its details, it doesn't need to be an admin there, only
on the intended Org.

## Connect to Curator

1. Go to the backend of your Curator instance.  Navigate to Integrations > Connections using the left-hand menu.
2. Click the new New Connection button on the top of the page.
3. Enter a name for the connection (something like "ThoughtSpot" is sufficient) and edit the slug if you'd like (but
   you don't need to).
4. Choose "ThoughtSpot in the Platform dropdown.  If the option is disabled then you already have a ThoughtSpot
   Connection  created.
5. Fill out the form that appears below the Platform dropdown:
   * **ThoughtSpot URL**: The full URL to for your ThoughtSpot instance.
     e.g. [https://example.thoughtspot.cloud](https://example.thoughtspot.cloud)
   * **REST Connection Username**: The username for a ThoughtSpot administrator.
   * **REST Connection Password**: The password for a ThoughtSpot administrator.
   * **Use Trusted Authentication?**: If you ***don't*** have SAML enabled for your ThoughtSpot environment you need
     to use trusted authentication.  Flip this switch on to enable it.
   * **Trusted Authentication Secret Key**: Enter the secret key your ThoughtSpot admin received when enabling trusted authentication.
6. Hit "Save" at the top of the page.


# Replace Dashboard URLs
Source: https://docs.curator.interworks.com/creating_integrations/updating_connections/replace_dashboard_urls

Bulk find and replace dashboard URLs when updating Tableau Server connections

You can find/replace URLs in bulk.  If you are modifying your overall Tableau Server Connection settings you may need to
[update the URL in Tableau integration or update the credentials associated](/creating_integrations/tableau_connection/creating_a_connection).

## To replace Dashboard URLs

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Tableau** > **Dashboards** in the dropdown.
4. Select the dashboards you'd like to replace the URL for using the checkboxes on the left
5. Click the "Replace Dashboard URLs" button with the hyperlink logo.
6. Enter the text you'd like the Portal to FIND in the field "Look for this text in the Dashboard URLs"
7. Enter the text you'd like the Portal to REPLACE in the field "Replace with"
8. Click the "Replace" button


# Temporarily Disabling Connections
Source: https://docs.curator.interworks.com/creating_integrations/updating_connections/temporarily_disabling_connections

Temporarily disable integration connections without removing configuration settings

If you need to temporarily turn off a connection, you can toggle off the **Enabled** switch when editing the connection
(Backend > Integrations > Connections > click a connection).

To re-enable the connection, just toggle the **Enabled** switch back on and save.

***Important* Note:** If your Curator licensing limits how many connections you can have in a single portal,
disabled/inactive connections are still counted toward those limits.  If you need to remove a connection from that count,
you'll need to fully delete the connection instead of disabling it.


# Authentication
Source: https://docs.curator.interworks.com/curator_api/api_docs/authentication

API authentication methods and user verification processes for external applications integrating with Curator.

## Introduction

Occasionally, various external applications need to rely on Curator to authenticate users for them.
Curator provides a simple interface to determine which user is currently authenticated to Curator,
and provide information to your external application about that user.

This is particularly helpful for applications that need to keep user authentication in sync with Curator,
such as custom applications embedded within Curator.

Retrieving information about the currently authenticated user requires two API calls to Curator:

1. First, your application must forward the user to Curator's /fetchUser endpoint,
   with a `redirect_url` parameter. Curator returns the user to the redirect\_url with a `payload`
   GET parameter containing a JSON wad containing an identifier token.
2. Next, use the `token` value from this JSON wad to call Curator's `/user/getUser` endpoint to retrieve the user's information.

## Important Setup

In order for the redirect to work, you must whitelist your domain in the Curator Portal Settings.
Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
Under the **General** tab, expand the **Security** section.

## /fetchUser

`HTTP REDIRECT [your_domain]/fetchUser?redirect_url=[group_name_here]`

## /user/getUser

Returns the currently logged in user's information.
`POST [your_domain]/api/v1/User/getUser?apikey=[your_api_key_here]&token=[token_here]`

**Returns:**
array

## Example Authentication Script

```PHP theme={null}
<?php
/**
 * This is a basic example of how to authenticate a user with Curator.
 *
 * From a flow perspective, this is what happens:
 *     1. The user is redirected to the Curator authentication system. (/fetchUser)
 *     2. The authenticated user is redirected back to this page with a JSON wad in the "payload" GET variable.
 *     3. The JSON wad contains a "token".
 *     4. The token is used against the Curator REST API to get the user's details.
 *
 * NOTE: VERY IMPORTANT:
 *     In order for the redirect to work, you must whitelist your domain in the Curator Portal Settings.
 *     Go to Settings->Curator->Portal Settings to add your domain. (Look under "security")
 *
 **/

/**
 * API Key: You can get this from the Curator backend.
 * Go to Settings->Curator->API Keys to retrieve and/or create a key.
 */
$api_key = 'YOUR_API_KEY';

/**
 * Curator Domain. This is the domain of your Curator instance.
 * For example: https://curator.example.com
 */
$curator_domain = 'YOUR_CURATOR_DOMAIN';

/**
 * This part is just a very basic session example.
 * You will likely want to customize it.
 */
session_start();

/**
 * If the user is returning from the Curator system, process their token.
 **/
if (!empty($_GET['payload'])) {
    processSessionPayload($_GET['payload'], $api_key, $curator_domain);

/**
 * Otherwise, if we need to start a NEW session, redirect to Curator.
 **/
} elseif (!isset($_SESSION['username'])) {
    // Where to return the user after the redirect.
    $returnURL = 'https://' . $_SERVER['HTTP_HOST'];

    // Redirect the unauthenticated user to the authentication system.
    header('Location: ' . $curator_domain . '/fetchUser?redirect_url=' . $returnURL);
    exit;
}

/**
 * If the user is authenticated, show them their information.
 **/
echo 'Hello, ' . $_SESSION['display_name'] . '!</br><pre>';
print_r($_SESSION);
echo '</pre>';

/**
 * Exchange the redirect session payload for user information.
 *
 * @param string $payload The JSON wad from the redirect.
 * @param string $api_key The API key for the Curator instance.
 * @param string $curator_domain The domain of the Curator instance.
 *
 * @return void
 */
function processSessionPayload($payload, $api_key, $curator_domain)
{
    $payload = json_decode($payload);
    if (isset($payload->token)) {
        // This is a 1-time use token returned from the /fetchUser endpoint.
        $token = $payload->token;

        // This is the REST API endpoint to exchange the token for user information.
        $url = $curator_domain . '/api/v1/user/getUser?apikey=' . $api_key . '&token=' . $token;

        $ch = curl_init($url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        $response = curl_exec($ch);
        curl_close($ch);

        $response = json_decode($response);
        $user = $response->user;

        /**
         * Uncomment the code below to see the user information available.
         *
         * echo "<pre>";
         * print_r($user);
         * echo "</pre>";
        */

        // Store the user information in the session.
        $_SESSION['username']     = $user->name;
        $_SESSION['email']        = $user->email;
        $_SESSION['display_name'] = $user->full_name;

        // The "SAML Attributes" are stored in the "custom_attributes" field.
        if (!empty($user->custom_attributes)) {
            $_SESSION['custom_attributes'] = $user->custom_attributes;
        }
    }
}
```


# Content
Source: https://docs.curator.interworks.com/curator_api/api_docs/content

Content API endpoints for creating and managing files and content within Curator

## /content/createFile

Creates a file model

Example Usage:

[Python Script](https://curator.interworks.com/file/api-example-createfile)

**Parameters:**
**file**

The file

**Returns:**

array

**Example Response:**

```JSON theme={null}
    {
        "result": "Success",
        "msg": 0
    }
```

## /content/createNavMenu

Creates a nav menu model

**Returns:**

array

**Example Response:**

```JSON theme={null}
    {
        "result": "Success",
        "msg": 0
    }
```

## /content/deleteFile

deletes a file model by ID

**Returns:**

array

**Example Response:**

```JSON theme={null}
    {
        "result": "Success",
        "msg": 0
    }
```

## /content/listFiles

Lists file content types.

**Returns:**

array

**Example Response:**

```JSON theme={null}
    [
        {
            "id": 1,
            "title": "HexTileAlt",
            "description": "",
            "slug": "hex-tile-alt",
            "restrict_group_access": 0,
            "created_at": "2017-09-12 16:11:10",
            "updated_at": "2017-09-12 16:11:10"
        },
        {
            "id": 2,
            "title": "Logo 196",
            "description": "",
            "slug": "logo-196",
            "restrict_group_access": 0,
            "created_at": "2017-12-15 17:15:07",
            "updated_at": "2017-12-15 17:15:07"
        }
    ]
```

## /content/listDashboards

Lists Tableau dashboard content types with associated keywords.

**Returns:**

array

**Example Response:**

```JSON theme={null}
    [
        {
            "id": 1,
            "title": "Sales Dashboard",
            "description": "Dashboard showing sales metrics",
            "slug": "sales-dashboard",
            "url": "https://tableau.example.com/#/views/Sales/Dashboard",
            "server": "https://tableau.example.com",
            "site": "Default",
            "restrict_group_access": 0,
            "created_at": "2023-01-15 10:30:00",
            "updated_at": "2024-01-10 14:22:00",
            "keywords": [
                {
                    "id": 2,
                    "title": "Scorecard",
                    "created_at": "2023-08-15T10:24:49.000000Z",
                    "created_by": "admin (backend)",
                    "updated_at": "2023-08-21T07:53:26.000000Z",
                    "updated_by": "admin (backend)",
                    "favoritable": 1,
                    "pivot": {
                        "dashboard_id": 1,
                        "keyword_id": 2
                    }
                },
                {
                    "id": 4,
                    "title": "Pink Cards",
                    "created_at": "2023-08-23T07:28:05.000000Z",
                    "created_by": "admin (backend)",
                    "updated_at": "2023-08-23T07:28:05.000000Z",
                    "updated_by": "admin (backend)",
                    "favoritable": 1,
                    "pivot": {
                        "dashboard_id": 1,
                        "keyword_id": 4
                    }
                }
            ]
        },
        {
            "id": 2,
            "title": "Marketing Dashboard",
            "description": "",
            "slug": "marketing-dashboard",
            "url": "https://tableau.example.com/#/views/Marketing/Overview",
            "server": "https://tableau.example.com",
            "site": "Default",
            "restrict_group_access": 0,
            "created_at": "2023-02-20 09:15:00",
            "updated_at": "2023-12-05 11:45:00"
        }
    ]
```

## /content/listNavMenus

Lists nav menu links.

**Returns:**

array

**Example Response:**

```JSON theme={null}
    [
        {
            "id": 1,
            "parent_id": null,
            "title": "Main Menu",
            "description": "The main menu items",
            "url": null,
            "enabled": 1,
            "parameters": null,
            "query_string": null,
            "is_external": 0,
            "link_target": "_self",
            "created_at": {
                "date": "2017-10-08 14:51:28.000000",
                "timezone_type": 3,
                "timezone": "UTC"
            },
            "updated_at": {
                "date": "2018-03-08 19:41:42.000000",
                "timezone_type": 3,
                "timezone": "UTC"
            },
            "link_type": "custom_url",
            "notice_id": null,
            "restrict_group_access": 0
        },
        {
            "id": 2,
            "parent_id": 1,
            "title": "Home",
            "description": "Website Home Page",
            "url": "home",
            "enabled": 1,
            "parameters": null,
            "query_string": null,
            "is_external": 0,
            "link_target": "_self",
            "created_at": {
                "date": "2017-10-08 14:51:28.000000",
                "timezone_type": 3,
                "timezone": "UTC"
            },
            "updated_at": {
                "date": "2018-01-16 15:24:38.000000",
                "timezone_type": 3,
                "timezone": "UTC"
            },
            "link_type": "custom_url",
            "notice_id": null,
            "restrict_group_access": 0
        }
    ]
```


# Curator API
Source: https://docs.curator.interworks.com/curator_api/api_docs/curator_api

Complete API reference for Curator including portal information, user management and system endpoints.

## /portal/info

Returns all information about Curator.

**Parameters:**

**boolean**
ini Shows PHP ini settings
**boolean**
extensions Shows loaded PHP extensions

**Returns:**

array

**Example Response:**

```JSON theme={null}
    {
        "version": "2020.09.17-01",
        "kernel_build": 446,
        "key": "[YOUR KEY HERE]",
        "php_version": "7.2.11",
        "os": "Linux ip-XX-XX-XX-XXXus-west.compute.internal 4.14.77-86.82.amzn2.x86_64 #1 SMP Tue Dec 1 20:40:13 UTC 2018 x86_64",
        "user": "apache",
        "server_addr": "ip-XXX-XX-XX-XXX.us-west-2.compute.internal",
        "server_ips": [
            "XX.XXX.XXX.X,
            "XXX.XX.XX.XXX",
            "curatordemo.interworks.com",
            "ip-XX-XX-XX-XXX.us-west.compute.internal"
        ],
        "database": "mysql",
        "display_errors": "Off",
        "max_execution_time": "60",
        "cache": "memcached",
        "gd": true,
        "fileinfo": true,
        "zip": true,
        "zlib": true,
        "curl": true,
        "openssl": true,
        "memcached": true,
        "php_ini_path": "\/etc\/php.ini",
        "tableau_version": "2018.1",
        "php_location": "\/usr\/bin\/php",
        "is_windows": false,
        "post_max_size": "250M",
        "upload_max_filesize": "250M",
        "memory_limit": "1024M",
        "webroot": "\/var\/www\/html",
        "cron_timestamp": "2019-01-08T21:01:02+00:00",
        "writeable": true,
        "upload_max_filesize_bytes": 262144000,
        "post_max_size_bytes": 262144000,
        "memory_limit_bytes": 1073741824,
        "install_files": false,
        "cron_check": true
    }
```

## /portal/version

Returns version information about the Curator portal.

**Returns:**

array

**Example Response:**

```JSON theme={null}
    {
        "version": "2017.08.10-01"
    }
```

## /portal/key

Returns key for the Curator portal.

**Returns:**

array

**Example Response:**

```JSON theme={null}
    {
        "key": "1234-5678-9101-1112-1314"
    }
```

## /portal/setKey

Sets the Curator's portal key.

**Returns:**

array

**Example Response:**

```JSON theme={null}
    {
        "result": "Success",
        "msg": 0
    }
```

## /portal/upgrade

Upgrades Curator to the latest version.

**Returns:**

array

**Example Response:**

```JSON theme={null}
    {
        "result": "Success",
        "msg": 0
    }
```

## /portal/cron

Runs the Curator Schedules.

**Returns:**

array

**Example Response:**

```JSON theme={null}
    {
        "result": "Success",
        "msg": 0
    }
```

## /portal/migrations

Runs database migrations.

**Returns:**

array

**Example Response:**

```JSON theme={null}
    {
        "result": "Success",
        "msg": 0
    }
```

## /portal/clearCache

Clears Curator cache.

**Returns:**

array

**Example Response:**

```JSON theme={null}
    {
        "result": "Success",
        "msg": 0
    }
```

## /portal/phpinfo

Returns the PHP Information Page

**Returns:**

array

## /portal/setPortalName

Sets the Curator portal name.

**Returns:**

array

**Example Response:**

```JSON theme={null}
    {
        "result": "Success",
        "msg": 0
    }
```

## /portal/octoberUpgrade

Upgrades the underlying OctoberCMS.

**Returns:**

array

**Example Response:**

```JSON theme={null}
    {
        "result": "Success",
        "msg": 0
    }
```

## /portal/export

Exports Curator portal data.

**Parameters:**

**string**
models (optional) Comma separated list of models to export. Default: everything.  Options include:

* `api_keys`
* `attributes`
* `commands`
* `connections`
* `dashboards`
* `favorites`
* `files`
* `filter_categories`
* `filters`
* `fonts`
* `frontend_groups`
* `frontend_group_overrides`
* `groups`
* `items`
* `interworks_authentication_settings`
* `interworks_integration_settings`
* `interworks_portal_settings`
* `interworks_tableauviz_settings`
* `interworks_usermgmt_samlsettings`
* `keywords`
* `loading_screens`
* `navigation`
* `notices`
* `pages`
* `parameters`
* `powerbi_dashboards`
* `powerbi_reports`
* `scheduledreport`
* `scripts`
* `slideshows`
* `themes`
* `tos`
* `tutorials`
* `user_comments  `

**boolean**
thumbnails (optional) Whether to include thumbnails in the export. Default: false.

**boolean**
tiles (optional) Whether the output data should use the tile information instead of export. Default: false.

**Returns:**

array

## /portal/cacheInfo

Returns all cache information about Curator

**Parameters:**
**boolean**
ini Shows PHP ini settings
**boolean**
extensions Shows loaded PHP extensions

**Returns:**

array

**Example Response:**

```JSON theme={null}
    {
        "result": "Success",
        "msg": {
            "cms_cache_path": "5.7 KB",
            "cms_combiner_path": "964.04 KB",
            "twig_cache": "529.57 KB",
            "framework_cache": "1.05 MB",
            "thumbnails": "28.95 MB"
        }
    }
```

## /portal/setAnalyticsSettings

Sets the analytics tracking settings.

**Returns:**

array

## /portal/setParameter

Sets a system parameter.

**Parameters:**
**Returns:**

array

## /portal/cleanSettings

Cleans up settings data, if there are duplicates.

**Returns:**

array

## /portal/fixStoragePerms

Attempts to fix storage file permissions, recursively.

**Returns:**

array

## /portal/checkSettings

Check settings items.

**Returns:**

array

## /portal/downloadLog

Exports Curator's system log data.

**Returns:**

array

## /portal/cleanUploadDir

Cleans out old uploaded files.

**Returns:**

array

## /portal/features

Returns information on features in use.

**Returns:**

array

## /portal/stats

Returns stats on Curator.

**Returns:**

array

## /portal/styles

Returns head insert and custom stylesheet from Portal Settings.

**Returns:**

array


# Integration
Source: https://docs.curator.interworks.com/curator_api/api_docs/integration

Integration API endpoints for managing commands and custom integrations

## /integration/commands

Returns a list of all commands

**Returns:**

array

**Example Response:**

```JSON theme={null}
    {
        "result": "Success",
        "msg": [
            {
                "id": 1,
                "name": "Test Command",
                "description": "This command refreshes extracts",
                "type": "tabcmd",
                "arguments": "",
                "schedule": "",
                "created": {
                    "date": "2017-08-17 21:08:02.000000",
                    "timezone_type": 3,
                    "timezone": "UTC"
                },
                "updated": {
                    "date": "2017-08-17 21:08:02.000000",
                    "timezone_type": 3,
                    "timezone": "UTC"
                }
            }
        ]
    }
```

## /integration/runCommand

Runs the specified command and returns its output.

**Parameters:**

**id**
Identifier of the command to run.

**Returns:**

array

**Example Response:**

```JSON theme={null}
    {
        "result": "Success",
        "msg": "Status not provided by command"
    }
```

## /integration/runScript

Runs the specified script and returns its output.

**Parameters:**

**id**
Identifier of the script to run.

**Returns:**

array

**Example Response:**

```JSON theme={null}
    {
        "result": "Success",
        "msg": "Status not provided by script"
    }
```

## /integration/scripts

Returns a list of all scripts

**Returns:**

array

**Example Response:**

```JSON theme={null}
    {
        "result": "Success",
        "msg": [
            {
                "id": 1,
                "name": "Test Script",
                "description": "This Script Does a Thing",
                "language": "python",
                "arguments": "",
                "schedule": "",
                "created": {
                    "date": "2017-08-17 21:11:44.000000",
                    "timezone_type": 3,
                    "timezone": "UTC"
                },
                "updated": {
                    "date": "2017-08-17 21:11:44.000000",
                    "timezone_type": 3,
                    "timezone": "UTC"
                }
            }
        ]
    }
```

## /integration/apiRelay

Kicks off an API relay request

**Returns:**

array


# Tableau API
Source: https://docs.curator.interworks.com/curator_api/api_docs/tableau_api

Tableau API endpoints for dashboard creation and management through Curator

## /Tableau/createDashboard

Creates a Dashboard record

**Common Parameters:**

* **title** *required*
  The title of your Dashboard
* **url** *required*
  This is the url of the Dashboard on the Tableau Server environment.
* **slug**
  This is the url of the Dashboard on the Curator environment.

***Note:** Other optional parameters, such as keywords, featured, etc. are supported but not listed here.*

**Returns:**

array

**Example Response:**

```JSON theme={null}
    {
        "result": "success",
        "msg": "Created Dashboard record",
        "Dashboard": {...},
    }
```

## /Tableau/syncTags

Kicks off tag schedule which synchronizes tags from Tableau Server

**Returns:**

string

**Example Response:**

```JSON theme={null}
    {
        "result": "Success",
        "msg": "Tag sync is complete"
    }
```

## /Tableau/syncGroups

Kicks off a schedule which synchronizes groups from Tableau Server.

**Returns:**

array

**Example Response:**

```JSON theme={null}
    {
        "result": "Success",
        "msg": "Group sync is complete"
    }
```

## /Tableau/listUsers

Lists users and groups.

**Returns:**

array

**Example Response:**

```JSON theme={null}
    [
        {
            "tableau_user_id": "21342134-236a-49f9-88e9-224272ab312c",
            "name": "CuratorDemo",
            "full_name": "Curator Demo",
            "site_role": "SiteAdministrator",
            "skip_sync": null,
            "groups": []
        },
        {
            "tableau_user_id": "12341234-89a3-4fde-acd9-a3b806995d69",
            "name": "admin",
            "full_name": "Administrator",
            "site_role": "ServerAdministrator",
            "skip_sync": null,
            "groups": []
        }
    ]
```

## /Tableau/setAuthentication

Sets the authentication type.

**Returns:**

array

## Tableau/setRest

Sets the REST credentials for Tableau Server Settings.

**Returns:**

array

## /Tableau/syncTableauDashboardIds

Kicks off tag schedule which synchronizes tags from Tableau Server

**Returns:**

string

**Example Response:**

```JSON theme={null}
    {
        "result": "Success",
        "msg": 0
    }
```

## /Tableau/resetViews

Kicks off a schedule task which clears out the Dashboard views

**Returns:**

string

**Example Response:**

```JSON theme={null}
    {
        "result": "Success",
        "msg": 0
    }
```

## /Tableau/refreshGroups

Kicks off tag schedule which clears the old groups and adds in new groups

**Returns:**

string

**Example Response:**

```JSON theme={null}
    {
        "result": "Success",
        "msg": 0
    }
```

## /Tableau/refreshThumbnails

Kicks off task which refreshes all thumbnails.

**Returns:**

string

**Example Response:**

```JSON theme={null}
    {
        "result": "Success",
        "msg": "Dashboard thumbnails are refreshed."
    }
```


# User API
Source: https://docs.curator.interworks.com/curator_api/api_docs/user_api

User management API endpoints for creating and managing backend users

## /user/createBackendUser

Creates a backend user

**Returns:**

array

## /user/createFrontendGroup

Creates a Frontend Group.

*Note: To add members to your Frontend Group, use the addUserToGroup API endpoint.*

**Example Request:**

`POST [your_domain]/api/v1/User/createFrontendGroup?apikey=[your_api_key_here]&name=[group_name_here]`

```JSON theme={null}
    {
        "platforms": {
            "tableau":[
                {
                    "server":"tableau us", // Name of your Tableau Server Connection
                    "site":"__DEFAULT__",
                    "group":"Alligator Admins" // Display Name of your Tableau Server Group
                }
            ],
            "thoughtspot":[
                "Europe Sales" // Display Name of your ThoughSpot Group
            ]
        },
        "custom_attributes": {
            "color": "blue"
        }
    }
```

**Returns:**

array

**Example Response:**

```JSON theme={null}
    {
        "result": "Success",
        "msg": "Successfully added platform groups to frontend group 30 and added syncing to the queue",
        "metadata": [
            {
                "tableau_server": "tableau us|||https://tableau.your-domain.com",
                "tableau_site": "__DEFAULT__",
                "tableau_group": "Alligator Admins|||[tableau_group_id_here]"
            },
            {
                "thoughtspot_group": "Europe Sales|||[thoughtspot_group_id_here]"
            }
        ],
        "tableauGroupsNotFound": "",
        "thoughtspotGroupsNotFound": ""
    }
```

## /user/fetchUser

Returns the currently logged in user's information.

**Returns:**

array

## /user/getManageablePermissions

Gets a listing of available manageable permissions

**Returns:**

array

**Example Response:**

```JSON theme={null}
    {
        "status": "Success",
        "permissions": [
            "InterWorks.datamanager.data_structure",
            "InterWorks.datamanager.data",
            "InterWorks.tableauviz.access_tableau_settings",
            "InterWorks.tableauviz.access_dashboards",
            "InterWorks.integration.manage_scripts",
            "InterWorks.integration.run_scripts",
            "InterWorks.integration.manage_commands",
            "InterWorks.integration.run_commands",
            "InterWorks.integration.manage_api_relay",
            "InterWorks.usermgmt.manage_backend_users",
            "InterWorks.usermgmt.manage_frontend_users",
            "InterWorks.content.access_content",
            "InterWorks.portal.access_portal_settings",
            "InterWorks.portal.manage_upgrade",
            "InterWorks.portal.api_keys"
        ]
    }
```

## /user/addUserToGroup

Adds a user to a group (syncs with Tableau if possible)

**Returns:**

array

## /user/listGroups

Lists groups.

**Returns:**

array

## /user/listUsers

Lists users and groups.

**Returns:**

array

## /user/removeUserFromGroup

Removes a user from a group (syncs with Tableau if possible)

**Returns:**

array


# Commands
Source: https://docs.curator.interworks.com/curator_api/custom_integration/commands

Create and manage custom commands for scheduled or ad-hoc execution

You can set up custom commands to run by the site. This requires the "Integration" setting to be enabled. To
create a command to be run on a schedule or ad hoc:

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on the "Integration" link at the top.
4. Click on "Manage Commands" in the left navigation.
5. Click on the "New Command" button at the top of the main page content.
6. Enter the name, description, and command type, arguments, schedule, etc. as needed and click "Create".


# Scripts
Source: https://docs.curator.interworks.com/curator_api/custom_integration/scripts

Set up and manage custom scripts for scheduled or ad-hoc execution

You can set up custom scripts to run by the site. This requires the "Integration" setting to be enabled. To
create a custom script to be run on a schedule or ad hoc:

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on the "Integration" link at the top.
4. Click on "Manage Scripts" in the left navigation.
5. Click on the "New Script" button at the top of the main page content.
6. Enter the name, description, and schedule of execution of the script, and select the appropriate script language.
7. Enter the script details as appropriate
   * For EDT, the full path to the EDT console runner must be specified and the EDT plan must be uploaded.
   * For powershell and python, the script code must be typed or copy and pasted in.
   * If additional arguments need to be passed to the command which runs the script (i.e. powershell.exe,
     etc.), enter those in the arguments field.
8. Click on the "Create" button.


# Subscription Routing
Source: https://docs.curator.interworks.com/curator_api/custom_integration/subscription_routing

Configure subscription email routing to direct users through Curator instead of Tableau Server

Curator integrates nicely with Tableau's native subscription system.
When users receive a subscription email, however, you may not wish the users to be routed to Tableau Server.

If you would rather users be routed to the appropriate Dashboard on Curator, [update Tableau Server's "subscription url"](https://kb.tableau.com/articles/issue/subscription-link-in-email-broken).

Point this url to your Curator website with /subscription/ appended.
For example, `https://examplecurator.interworks.com/subscription`.

***Note:** At the time of this writing, updating this value in Tableau Server requires a Tableau Server reboot.*


# Curator API Overview
Source: https://docs.curator.interworks.com/curator_api/getting_started/curator_api_overview

Complete guide to the Curator API including metadata access, content management and integration command capabilities.

The Integration System gives you many options for interfacing programmatically with the backend. This API
gives you access to the metadata behind your portal content as well as the ability to update content and run
integration commands.
Before you do, though, you'll need an API Key and the endpoint!

## 1. Obtaining an API Key

To access the API, you will need an API key. You can create an API Key in the /backend area of your portal.
API Keys are managed in Settings -> API Keys

## 2. Accessing the API

Once you have an API Key, you can access the API through the "api" folder on your portal's URL.
For example: `https://yourportal.example.com/api/v1/portal/upgrade?apikey=my_api_key_here`

## 3. API Response

All of the Integration System's APIs return JSON. You can convert this easily to an array in most languages.
(json\_decode, for example, in PHP)

## Auto Generate API Links

You can also use Curator's backend to generate links to the various Curator API endpoints

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **API Keys** section from the left-hand menu.
3. Change the dropdowns in the REST API to the respective endpoint you would like to try.
4. Use the preview link generated below the dropdowns to start using the endpoint.  *Note: Some variables may
   be missing from these preview links.*


# Curator Integration Overview
Source: https://docs.curator.interworks.com/curator_api/getting_started/curator_integration_overview

Overview of Curator API integration capabilities including API calls, scripts and custom automation features.

You can relay API calls from Curator, make Curator run scripts and do other interesting things.


# Connecting to Data Manager
Source: https://docs.curator.interworks.com/embedding_using_analytics/data_manager/connecting_to_data_manager

Set up connections and integrate Data Manager with your analytics workflow for data collection and processing.

When using Data Manager you will likely need to connect to the underlying database that stores the data input from your
users.  You can find the connection information on the "Data Group" edit page, but first you'll need to create a
readonly user (if one does not exist in the info.txt/info.json file found in the root directory of the Curator install).

Note: This will allow your readonly user to connect from anywhere.  If you'd like to specify the IP address they can
connect from replace the '%' with your IP address in the examples below to limit where they can query from.

## Creating a Readonly MySQL User

### 1. Log into MySQL

#### Linux

Run the command below on your server to login to mysql:

```bash theme={null}
mysql -u root -p
```

#### Windows

Navigate into MariaDB/MySQL root directory and then login to MySQL:

```bash theme={null}
cd C:\InterWorks\Curator\libs\MariaDB\bin
mysql -u root -p
```

### 2. Create a new MySQL user

Run the command below to create a new user that can run a connection from *anywhere* (replacing 'USER' and 'PASSWORD'
with a username and password you'd like to use):

```SQL theme={null}
CREATE USER 'USER'@'%' IDENTIFIED BY 'PASSWORD';
```

### 3. Grant read-only permission to the MySQL user

Run the command below to create a new user that can read data from *anywhere* (again replacing 'USER' and 'PASSWORD'
with a username and password you'd like to use):

```SQL theme={null}
GRANT SELECT, SHOW VIEW ON curator.* TO 'USER'@'%' IDENTIFIED BY 'PASSWORD';
FLUSH PRIVILEGES;
```

**Important!** Be sure you keep these credentials secure, but also available for reference as they will be required to
connect to your data.

### Connecting to the Datamanager Database

1. Find the connection information for the table you would like to view in the top section of the edit "Data Group" page

   * Database Name: **Curator**
   * Host Name: **127.0.0.1**
   * Table Name: **a\_reports\_data\_group**

2. Use the connection details from the "Creating a Readonly MySQL User" and the database, hostname, and table name from
   the previous step to connect to your MySQL data source.

### Troubleshooting Connections

1. Ensure your firewall rules allow inbound traffic over port 3306 to allow remote connections to your database.
   If you are having trouble connecting, please contact your hosting team for further help.
2. By default, remote connections are not allowed on some operating systems (e.g. Ubuntu 20).  You can run the commands
   below to set up remote connections:

   Determine the location of your MySQL config file by running the command below:

   ```bash theme={null}
   mysql --help | grep "Default options" -A 1
   ```

   Open the file that is returned from these commands (i.e. `/etc/my.cnf`):
   Add the following line to the bottom of the file, where `xxx.ip.xxx` is replaced with your IP address, or you can use
   `0.0.0.0` to allow remote connections from anywhere:

   ```conf theme={null}
   bind-address= xxx.ip.xxx
   ```

   Now save your file and restart mysql to allow remote connections:

   ```bash theme={null}
   sudo systemctl restart mysql
   ```


# Creating a Form
Source: https://docs.curator.interworks.com/embedding_using_analytics/data_manager/creating_a_form

Build custom data collection forms using Data Manager to gather structured information from users.

First before you continue - take a look at our [Data Manager Basics](/embedding_using_analytics/data_manager/data_manager_basics)
to get familiar with terms and how Data Manager works generally.  Once you've perused that page, check out all the
flexible ways you can add forms and gather important feedback in your Curator site.

## Building your Form

To create a form, simply map all the Attributes you would like your Group to include.  If you're not sure which field
types you'd like your form to contain refer to the "Available Fields" section below.  Once you've created your
attributes, simply collect them into your Data Manager Group to begin placing your form throughout your site.  For
details on how to make your form accessible, refer to the "Accessing the Data Manager Form" section below.

## Available Fields

There are many ways to build a form using Curator's Data manager. Below, you'll find an outline of each field and what
it's used for.

### User-populated fields

There are many flexible options when building a form, and your users may want flexible free-text input or pre-selected
date or dropdown options:

* **Short Text**: A standard user-input text field, typically used for things like first name, last name, and email.

* **Long Text**: A free-form text entry allowing for lengthy input, primarily used when your users will be entering
  one or more sentences into the form.

* **Number**: Short Text input that limits entry to numbers (whole or decimal).

* **URL**: Short Text input that limits the format to a URL.

* **Dropdown**: Create a pre-set list of options for users to select from.

* **Date**: A calendar-date picker allowing users to select a given day.

* **Password**: Short Text input that hides the input for secure browsing (however, the password will not be encrypted
  in the database once stored).

* **Markdown**: A markdown field - renders a markdown text-editor on the backend when inputting new data.  This is
  primarily used when creating documentation.

### Fields populated from other sources

Some other sources within Curator may contain the data you want to populate your form with.  For these
more complex scenarios, you can leverage the following fields:

* **Lookup**: A dropdown that allows you to retrieve the selected options from another data manager group's input.

* **Read-only Field**: Short Text input that users cannot interact with - for use when populating an input using custom
  code.

### Fields populated from other sources: *Tableau mark-commenting only*

When selecting a data-point on a Tableau Dashboard, you can leverage that Dashboard's underlying data to pre-populate the
form that renders in the pop-up modal.  To learn ore about this, refer to the
[Mark Commenting](/embedding_using_analytics/data_manager/mark_commenting)
details.  To utilize the data that resides in your Dashboard to pre-fill dropdown options use these two fields:

* **Tableau Field**: A dropdown field that retrieves the data from the Tableau mark-selection for a given field name and
  populates the possible options when the form is rendered.

* **Tableau Parameter**: A dropdown field that retrieves the data from the Tableau mark-selection for a given parameter
  and populates the possible options when the form is rendered.

## Accessing the Data Manager Form

Once your Data Manager Group has been created, you will need to share the form so users can access it and start adding
their own data in to Curator's data manager storage.  There are four possible ways to access the form you've created
through your Group.

### Default Data Manager Form

Once a Data Manager Group has been created, Curator provides you with a templated page that contains your Data Manager
form - along with an option view of the data depending on the settings you've enabled for your group.

### Adding a Data Manager form to a page

Using Curator's page builder system, you can add a form - with a few different options for layout types - to a page.
Refer to the [Forms](/site_content_design/pages/forms) documentation on how to
add a form to a Page.

### Mark Commenting Pop-up Form

When interacting with a Dashboard, you can show your users a form after they click on a given Tableau data-point.
To learn ore about this, refer to the
[Mark Commenting](/embedding_using_analytics/data_manager/mark_commenting)
document.

### Dashboard Feedback

Curious what your users think about your dashboards?  You can add a single form to incorporate their feedback, gathering
the Dashboard URL automatically and tying it to their form-submission.  For details on Dashboard Feedback
[check out this outline](/embedding_using_analytics/data_manager/dashboard_feedback).


# Dashboard Feedback
Source: https://docs.curator.interworks.com/embedding_using_analytics/data_manager/dashboard_feedback

Enable user feedback collection on dashboards through Data Manager integration for improved user experience and insights.

In order to gather valuable insights from your audience about their experience using your Dashboards, Curator can
provide a simple and easy feedback mechanism for your users to submit their feedback, questions, and requests.  After
following the [Creating a Form](/embedding_using_analytics/data_manager/creating_a_form)
outline to build out your desired form, follow the guide below to integrate the Dashboard feedback in to your Dashboard
pages.

## Modifying your for to support the Dashboard URL

In order to gather the context of which Dashboard a user is providing feedback for, you'll need to add a new hidden
field that will store the Dashboard URL (the Curator URL).

### Adding a new Data Attribute

To add this attribute to your form:

1. Go to Data Manager > Data Attributes to set up the fields you want:
   <img alt="Create Data Attribute" />
2. In the Create Attribute page, set the name, description (optional), and the field type.
3. Make sure the field type is set to **Short Text**.
   <img alt="Select Short Text from Dropdown" />

Next, navigate to your Data Manager Group, and associate the Attribute you just created with your Group.

### Identifying the form to use in Portal Settings

There's one last step to set up your Dashboard Feedback.

1. Navigate to Settings > Tableau > Tableau Server Settings.
2. Find the Dashboard Feedback on the General tab.
3. For the **Feedback Form** select your Data Group.
4. For the **Dashboard URL** select the Short Text Data Attribute you created to store the the Dashboard URL.

<img alt="Settings" />


# Data Manager Basics
Source: https://docs.curator.interworks.com/embedding_using_analytics/data_manager/data_manager_basics

Introduction to Data Manager functionality for creating forms, capturing dashboard interactions and managing user-submitted data.

Data Manager allows you to create forms for users to fill out, and to store that data for retrieval later.  These forms
can even retrieve data-points that users click on in a Tableau Dashboard to be stored alongside the form they submit.
The data from these forms are then stored in Curator's database, where you can later retrieve that data for use in other
dashboards, or even for the same Dashboard itself, providing immediate feedback!

## Data Manager Terminology

When starting with the data manger, it's important to understand core concepts, and thankfully we've made it pretty
simple for you.  Here's a quick mapping to understand the Data Manager components when building a form:

* Data Attribute = Individual Field/Input
* Data Group = Entire Form

or another way to view these is from how the data will be stored in the database:

* Data Attribute = Column
* Data Group = Table

## Enabling Data Manager

If you do not see "Data Manager" as a top-level menu option on the left-hand nav on the backend of Curator, you can
enable it by following these steps:

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
3. Click on the **Features** tab
4. In the "Functionality" section ensure the toggle for "Data Manager" is enabled and click the "Save" button.

That's it!  Curious what's under the "Manage Data" section on the left-hand nav?  That's where you can create or edit
existing rows in your Data Groups once they've already been added.

### Creating a Data Attribute

To create a data attribute, you can

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Data Manager** > **Data Attributes** section from the left-hand menu.
3. Click on the **New Attribute** button
4. Fill out the form keeping in mind how you'd like your end user to interact with this field, then click "Save".

#### Creating a Data Group

Once you have created all the data attributes you need for your user form, you can group them all together into a
Data Group for use with Data Manager features like
[Mark Commenting](/embedding_using_analytics/data_manager/mark_commenting).
To create a data group:

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Data Manager** > **Data Groups** section from the left-hand menu.
3. Click on the **New Group** button
4. Check all of the boxes next to the Data Attributes you wish to add to your Data Group then click "Create" or "Save".

## Migrating Data to another Database

If you would like to use a different database to store this data, we recommend using your preferred ETL process to
extract the data out of Curator's MySQL database.  Curator does not support any other databases beyond MySQL.

## Styling Data Manager Forms in Curator

If you would like to customize the background, text, or highlight colors for your data manager forms, you can do update
the colors in **Settings** > **Curator** > **Themes** section from the left-hand menu under the "Pages" tab.


# Exporting Data
Source: https://docs.curator.interworks.com/embedding_using_analytics/data_manager/exporting_data

Export data collected by Data Manager using various export options including CSV downloads for backend users.

You can export the data collected by the Data Manager by using the Data Manager Export options.

## Download as CSV - Backend Users Only

In the backend, you need an administrator account with Data Manager privileges.

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to **Data Manager > Data Groups** section from the left-hand menu.
3. Click on the Data Group you want to export the data from.
4. Click **Download as CSV** to trigger the manual export.

## Download as CSV - Frontend Users

In the backend, you need an administrator account with Data Manager privileges.

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to **Data Manager > Data Groups** section from the left-hand menu.
3. Click on the Data Group you want to export the data from.
4. Toggle on **Allow CSV Export on frontend** to enable the export feature on the front end.
5. Make sure the toggle **Hide List** is off.
6. Save.

Once the feature is enabled, as a frontend user:

1. Login to the front end (e.g. `http://curatorexample.com/`).
2. Navigate to the Data Group (aka form) that you want to export the data from
   (e.g. `https://www.curatorexample.com/data/your-data-group`).
3. Open the section Your Data Group List.
4. Click the **CSV** button to trigger the manual export.


# Field Calculations
Source: https://docs.curator.interworks.com/embedding_using_analytics/data_manager/field_calculations

Create calculated fields and formulas within Data Manager to transform and analyze collected data.

Performs some formula calculations on fields like addition, subtraction, multiplication, division, and concatenate with
a separator. For more on this check out our
[blog post](https://interworks.com/blog/morr/2018/11/14/portals-for-tableau-new-feature-spotlight-data-manager-calculated-fields/).

## Add a Field Calculation to a Data Manager Group

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Data Manager** > **Data Groups** in the left navigation.
4. Select the group you want to edit or click on the "New Group" button.
5. Click on the Field Calculation to add a new item.


# Importing Data
Source: https://docs.curator.interworks.com/embedding_using_analytics/data_manager/importing_data

Import external data into Data Manager from various sources for analysis and integration with existing datasets.

If you already have data collected somewhere else for your form and want to bring everything together in your Curator
table, use the Data Manager Batch Import option.

## Using Batch Import

In the backend, you need an administrator account with Data Manager privileges.

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to **Settings > Data Manager > Manage Data** section from the left-hand menu.
3. Click on the Batch Import above the overview table.
4. Click on Schedule Import.
5. Select the Data Group for which the data should be imported.
6. Select the CSV file that holds your data.
7. Decide whether or not to trim white-spaces around the string values.
8. Click Import.

If you want to enable your frontend users to upload data:

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to **Settings > Data Manager > Data Groups** section from the left-hand menu.
3. Select the Data Group for which frontend users should be able to import data.
4. Enable **Batch Import** by using the toggle.
5. On the front end, a new section **Batch Import** appears. Click on it to expand the section.
6. Select the CSV file that holds the data.

### Format your CSV

* Add the headers of your table as the first row of your CSV file. Make sure it:
  1. Only has the Data Groups attributes' name in it.
  2. Uses the very same spelling.
  3. Has no spaces around the single attribute names.
* Have one row in the CSV for each row of data. Make sure it:
  1. Has as many attributes as defined in the Data Group.
  2. Has two consecutive commas, if you want to add a blank value.
  3. Do not add any quotes around the values.


# Mark Commenting
Source: https://docs.curator.interworks.com/embedding_using_analytics/data_manager/mark_commenting

Enable mark-based commenting functionality for data points and visualization elements to enhance collaborative analysis.

Curator can allow you to capture input from a user after they select a specific data point on your Dashboard.  Once you
associate a Data Group with a specific field/column from your Dashboard, any time a user clicks on a data-point that
contains that field, a pop-up will display asking the user to input information about that data-point.  This feature
allows you to capture comments on specific data points, projections or estimates, and even the ability to capture
feedback about the data itself.

This functionality requires that Data Manager management is enabled and at least one Data Group has been created.  See
the [Data Manager Basics](/embedding_using_analytics/data_manager/data_manager_basics)
section for more information on how to get things set up if you haven't already.

## Enable Mark-Commenting on a Dashboard

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Tableau** > **Dashboard** section from the left-hand menu.
3. From the list view, find the Dashboard you wish to add Mark Commenting to.
4. On the edit Dashboard page, click the "Mark Commenting" tab.
5. Select the Data Group you have created from the "Data Manager Group" dropdown you would like to display when the user
   clicks on your Dashboard.
6. In the "Mark Details" section, choose as many fields as you'd like from your Dashboard to trigger the
   "Mark Commenting" pop-up.  The logic here is that it must contain *all* fields you have chosen.
7. Click the "Save" button.

**Note:** Make sure the **dimension** name matches the spelling from your Dashboard. Measures or *Measure Names* cannot
be used as a connecting field.

Do you want a step-by-step guide with screenshots? Take a look [here](https://interworks.com/blog/jlyons/2018/10/01/portals-for-tableau-101-inline-commenting-on-dashboards/).

Once you've set up Mark Commenting on your Dashboard, you may want to connect to this data.  See the
[Connecting to Data Manager](/embedding_using_analytics/data_manager/connecting_to_data_manager)
section for more info on how to get started there.


# Sending Data to Webhooks
Source: https://docs.curator.interworks.com/embedding_using_analytics/data_manager/sending_data_to_webhooks

Configure Data Manager to automatically send collected data to external systems via webhook integrations.

When using mark commenting, you have the option to send the metadata to a webhook. This features allows you to send
mark commenting data to any webhook endpoint, instead of Data Manager.

To enable this feature,

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Portal Settings** > **Features** section from the left-hand menu.
3. Enable "Integration Automation" in the Functionality Section.
4. Save and refresh the page.
5. Navigate to **Integrations** > **Automation** > **API Relay** section from the left-hand menu.
6. Create a new API Relay. Use the webhook endpoint as the URL field.
7. "Outgoing Request Content" and "Incoming Request Validation" can be edited as needed for more complex webhook usage.
8. Once an API Relay is created, it needs to be selected for the necessary Data Group. For more information on Data
   Manager, take a look [here](/embedding_using_analytics/data_manager/data_manager_basics).
9. Visit **Data Manager** > **Data Groups** and select the necessary Data Group. Enable "Send to Webhook" and select
   the appropriate API Relay from the dropdown.
10. Visit **Tableau** > **Dashboards** and select the Dashboard you wish to enable. In the
    "Mark Commenting" tab, now select the Data Manager Group you wish to use (from step 9).
11. Data from the Data Manager Group form will now be sent to the webhook provided.


# Updating Data Groups
Source: https://docs.curator.interworks.com/embedding_using_analytics/data_manager/updating_data_groups

Modify existing Data Groups to add new fields and information requirements while preserving previously collected data.

If you have been using your Data Group and frontend users have input information diligently, you might find out that you
need extra pieces of information on top of what you are gathering to drive your analysis.

No problem, we have you covered by allowing you to simply add or remove the fields as required. Just follow these steps:

## Adding new Data Manager Attribute

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to **Settings > Data Manager > Data Group** section from the left-hand menu.
3. Click on the Data Group you want to alter.
4. Check more attributes (aka form fields) as required.
5. Click Save
6. Click on **Regenerate Summary Table** to reflect the changes in the respective database table.

Existing data entries will have an empty value in the newly added column.

## Remove an existing Data Manager Attribute

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to **Settings > Data Manager > Data Group** section from the left-hand menu.
3. Click on the Data Group you want to alter.
4. Uncheck attributes (aka form fields) as required.
5. Check **Permanently delete attribute data from items when unlinking from group?** underneath the Attributes selection
   section.
6. Check **Confirm permanently deleting attribute data from items** if you are sure you want to delete the attribute
   from your table.
7. Click Save
8. Click on **Regenerate Summary Table** to reflect the changes in the respective database table.

Existing data in the removed attributes will be lost after this process!


# User Commenting
Source: https://docs.curator.interworks.com/embedding_using_analytics/data_manager/user_commenting

Enable user commenting functionality on dashboards and pages through Data Manager integration for enhanced collaboration.

User Commenting provides the option to allow comments on individual dashboards, pages, and mixed content pages. The
Data Manager must be enabled to use the "User Commenting" feature. To enable for dashboards:

## Enable Curator-stored User Commenting

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Tableau** > **Dashboards** in the left navigation.
4. Select the Dashboard you want to enable "User Commenting" on.
5. Click on the "Misc" tab.
6. Click to switch on the "Allow User Commenting" setting under the "Education" section and click the "Save" button.


# Web Data Connector (WDC)
Source: https://docs.curator.interworks.com/embedding_using_analytics/data_manager/web_data_connector_wdc

Integrate external data sources using Web Data Connector technology for dynamic data access in analytics platforms.

**As of Tableau Server version 2023.1, Tableau has deprecated Web Data Connector and will no longer be available**
**through Curator. Read more**
**[here](https://kb.Tableau.com/articles/Issue/web-data-connectors-deprecated-in-2023-1-release)**

The Web Data Connector allows you to connect easily to your Data Manager tables and a few usage statistics. The Data
Manager needs to be enabled only if you want to connect to your Data Manager tables.

1. Open Tableau Desktop and add a new datasource of the type **Web Data Connector** to your workbook.
2. Enter the url to your Web Data Connector, e.g. [https://www.curatorexample.com\*\*/backend/interworks/datamanager/wdc\*\*](https://www.curatorexample.com/backend/interworks/datamanager/wdc).
3. Log in with your backend administrator credentials.
4. Select the table you want to analyze in Tableau and start your analysis.

Available usage statistics are:

* Views per Dashboard
* Curator Content Views
* Curator Data Manager Groups
* Curator Favorites
* Curator Files
* Curator Keywords
* Curator Pages
* Curator Power BI Dashboards
* Curator Power BI Reports
* Curator Tableau Dashboards
* Curator Usage Log

For further usage tracking consider adding Matomo or Google Analytics as your web analytics tool to your Curator
instance as described in [this blog post](https://interworks.com/blog/morr/2018/07/26/portals-for-tableau-new-feature-spotlight-on-premises-analytics-tracking/).

## Refreshing WDC Extracts

Connecting to a [Tableau Web Data Connector](https://help.tableau.com/current/pro/desktop/en-us/examples_web_data_connector.htm)
creates an extract of the data's state at a specific point in time. Yet, you might want to do a continuous and automated
analysis of your Curator's usage.
Publish the data source on Tableau Server where you can run scheduled refreshes of the extract. For security reasons,
you need to add your Curator's WDC to Tableau Server's safe list by running the following command on tsm:

```bash theme={null}
tsm data-access web-data-connectors add --name "Curator WDC" --url https://[your-curator-url-here]:443/wdc --secondary https://fonts.googleapis.com/.*,https://use.typekit.net/.*,https://[your-curator-url-here]/.*,https://connectors.tableau.com/.*
```

The above command allows Tableau Server to connect to the WDC and the asset domains used by the WDC. Tableau explains
[further details in their documentation](https://help.tableau.com/current/server/en-us/datasource_wdc.htm). To make the
above change effective **Tableau Server needs a restart**.


# Caching Filter and Parameter Options
Source: https://docs.curator.interworks.com/embedding_using_analytics/filters_parameters/caching_filter_and_parameter_options

Optimize performance by configuring caching strategies for filter and parameter options to reduce load times.

Curator has the ability to populate the filter and parameter options from the Dashboard's data by using the
"Get Filter Options from data". This option is normally only enabled when you have a large number of options to
retrieve for the filter. The time to retrieve all these options can take a while if you have several hundred or several
thousands of options. While we can't speed up the initial time, we can make subsequent requests faster. To do this
enable "Cache filter/parameter options from data" after enabling "Get Filter options from data".

## To enable Cache Filter/Parameter Options

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on "Tableau" in the left-hand menu.
4. Click on the "Filters" or "Parameters" link on the left.
5. Click to switch on the "Cache filter options from data" under the Display Options section of a filter or parameter.
6. Select the desired cache time from the dropdown below the switch.
7. Click the "Save" button.


# Filter Apply Button
Source: https://docs.curator.interworks.com/embedding_using_analytics/filters_parameters/filter_apply_button

Configure apply buttons for filters to control when filter changes are applied to dashboard visualizations.

Each Filter and Parameter gets applied as soon as their values are changed. When you have many filters and parameters,
this can become time-consuming. To alleviate this issue we have created the "Apply" button. This button will not apply
any of your changes until you click on it.

## Enable the Filter Apply Button

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on the **Settings** > **Tableau** > **Tableau Server Settings** in the left-hand menu.
4. Click the "General" tab at the top.
5. Expand the "Filters and Parameters" section.
6. Click to switch on the "Filters and Parameters Apply Button".
7. Click the "Save" button.

*Note*: Date Range Filters have their own apply button. As a result, they are applied
to the report immediately after this button is pressed. They do not respond to Curator's
Apply button.


# Filter Categories
Source: https://docs.curator.interworks.com/embedding_using_analytics/filters_parameters/filter_categories

Organize filters into logical categories for improved user experience and streamlined dashboard interaction.

Filter Categories can group filters/parameters together under a specific category. When the Dashboard filter pop out is
rendered on the right side, it will group all of the filters/parameters together under the filter category name. If
there are no filters displayed using the filter category, then it will not be rendered either.

## Enable Filter Categories

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Settings** > **Curator** > **Portal Settings** in the left-hand menu.
4. Click on "Features" at the top of content page.
5. Expand the "Functionality" section and toggle on the "Filter Categories" button.
6. Click "Save" on the top right of the page.

## Create a filter category

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Tableau** > **Filter Categories** in the left-hand menu.
4. Click the "New Filter Category" button.
5. Type in a display name in the "Name" field.
6. Click the "Save" button.


# Filters
Source: https://docs.curator.interworks.com/embedding_using_analytics/filters_parameters/filters

Configure and implement filters to enable users to interactively control dashboard content and focus on specific data subsets.

Filters in Curator provide a powerful way to refine and control the data displayed in Dashboards, giving you expansive
capabilities beyond what is natively available with the tools you're embedding.  You can share filters across
multiple dashboards, placing your users back into their browsing context without having to constantly re-set filters,
even integrating filters across different BI platforms to unify this experience regardless of the tool you're embedding.

With this guide to Filters, we will explain how to configure and manage your filters, providing you with details on
which settings are best for all the scenarios you may encounter.

***

## To Create a filter

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Tableau** > **Filters** in the left-hand menu.
4. Click the "New Filter" button.
5. Find the details of how to set up filters in the following [overview](#overview-of-filter-settings)

## Overview of Filter Settings

### Filter Fields

<img alt="Overview of the top section - Filter fields" />

* **Display Name**: The name visible to users when interacting with the filter.
* **Filter Type**: The type of filter (e.g. Single-select, Multi-select, Date) to control this field.
* **Filter Category** (optional): Allows you to group filters into sections in the filter pane. See the
  [Filter Categories Section](/embedding_using_analytics/filters_parameters/filter_categories)
  for more information.
* **Field Name Mapping**: Links the filter to a specific field in the analytics platform.
* Once your Field Name Mapping is verified, you will see a teal notice appear confirming the filter has been found
  on your BI platform. If your Field Name Mapping could not be verified, a yellow notice appears. Use the **Check
  All Tableau Site** button if you are certain that the field name exists on a different Site.

### Dashboards

* Assign filters en-masse to specific Dashboards. The filter will show as a Curator filter inside the Curator toolbar
  when you load a given Dashboard. You can also add filters to a specific Dashboard via the "Filters" tab on the edit
  Dashboard page.

### Secondary Data Source

In most cases, this toggle should remain **off**. It is only required in specific scenarios where filtering needs to
be applied to a field that is not part of the primary data source on your Tableau sheet but comes from a secondary
data source. You can identify secondary data source fields in Tableau by the orange check mark in editing mode.

If you need to filter on a field marked with this orange check mark:

1. Enable the **Specify a Secondary Data Source** toggle.
2. Enter the name of the secondary data source (as displayed in the workbook) into the input field that appears.
   The filter will then be sent to Tableau in the format of `datasource_name.filter_field_name`.
   This ensures that the filter is correctly applied across your data sources.

## Display Options

1. **Sticky Filter**
   * Saves filter selections per user for consistent filtering across Dashboards. This
     is using browser cookies which will be applied to any Dashboard that uses the specified
     field name from the specified field name mapping. I.e. it is not only applied to the
     Dashboards selected in the [Dashboards](#dashboards) section above.

2. **Add "All" Option**
   * Adds an "All" selection option for Single Select filters. If there is no "All" option for the single select
     filter, the first value of the field will be shown even if not yet selected. Once you started filtering you
     can only reset the filter by using the toolbar button "Reset".

3. **Get Filter Options from Data**
   * Pulls options directly from the data source to populate the filter options for a given dropdown. This will
     slow down the Dashboard's load time if the Dashboard contains a lot of data. This process can be
     sped up by enabling "Specify Filter Sheet" from a Dashboard's backend settings. See the
     [Specify Filter Sheet Section](/embedding_using_analytics/filters_parameters/specify_filter_sheet)
     for more information.  If this field is disabled, you must add items via the Options list (manually)
     otherwise the filter will contain no options for users to select and they will only see "No results found".

4. **Cache Filter Options**
   * This saves the dropdown options via Curator's cache on a user basis and will retrieve options in a more
     performant manner.  However, the list of options may be stale given the time you set the cache to. The cache
     begins the first time a user loads the options, and is not related to the underlying Dashboard's data-refresh
     schedule, so ensure you only enable this setting for dropdowns that rarely see new data.
   * **Cache Expiration Options**: 4 Hours, 1 Day, 1 Week

5. **Filter-Blacklist**
   * If you have a Filter Blacklist set up, it can be reused by toggling on **Use Filter-Blacklist Group**.
     Once enabled, you can select from you existing Blacklist Groups to be applied on this filter.
   * Note, if you either don't have a Filter Blacklist Group set up or only want specific sheets to be
     blacklisted, i.e. the filter to not be applied on this sheet, add the sheet names as individual items
     to the **Sheet Blacklist** list.
   * More information in Filter Blacklists can be found under [Hidden Sticky Filters
     and Parameters](/embedding_using_analytics/filters_parameters/hidden_sticky_filters_and_parameters)

## Filter Types

### Single Select

* Allows the frontend user to select only a single value for this filter.

### Multi-Select

* Allows the frontend user to select multiple values for this filter.

### Date

* Allows the frontend user to pick a date from the standard date picker widget. The date format
  is displayed based on the users locale settings. To successfully filter for dates make sure that the
  Tableau Dashboard is published with the correct specific locale settings or with automatic locale detection.

### Date Range

* Allows the frontend user to pick a start and an end date from the standard date picker widget. The date
  format is displayed based on the users locale settings. To successfully filter for dates make sure that the
  Tableau Dashboard is published with the correct specific locale settings or with automatic locale detection.

### Relative Date Filters

* Works similarly to Tableau's Relative Date Filters where you get a slider to dynamically update to show a
  time period relative to when you open the view, such as the current week, the year to date, or the past 10 days.
  Relative date filters make it easy to create views that always show the most recent data ([cf. Tableau Relative
  Date Filters](https://help.tableau.com/current/pro/desktop/en-us/qs_relative_dates.htm)).
* When you use a Relative Date Filter you will get more options to configure your filter:
* **Direction**: Filter by Past or Future.
* **Scale**: Choose Days, Months, Quarters, or Years.
* **Range**: Specify the maximum relative date range.

### Boolean

* Allows the frontend user to select between True and False.

## More on Filters

### URL Filters

* You can apply filters and parameters by appending `key=value` pairs to URLs to pre-filter Dashboards. E.g.
  my-Curator.com/Dashboard/superstore?region=North will pre-filter my Superstore Dashboard to only show the North region.
* Automatically applied when using Curator or Tableau filter UI.
* **Important**: Disabling "Ignore filter and parameter changes from Dashboard" prevents
  [Report Builder](/embedding_using_analytics/report_builder/overview_and_enabling_report_builder)
  from capturing filters.

### Evaluation of Filters

In this order, filters are evaluated:

* **URL filters** - Values that are appended to the Curator URL in your browser (e.g. `?Region=South`)
* **Preloaded sticky filters** - Filters identified via the Tableau Server Settings.
* **Cookie-based sticky filters** - Browser-session stored filters, also managed via Tableau Server Settings.
* **Published filter settings** - The default state of the Dashboard.

In case of any conflicting values, the first evaluation is considered the correct one.  For example, if one of your
users has been browsing around and setting their **Region** filter to *North* and that drops a *Cookie-based sticky
filter* in their browser, when they return to the page, the filter will be evaluated as `Region=North` by default.
However, if they are emailed a link from a colleague sharing an insight and the URL is sent over with `?Region=South`
when they click on the link, the Dashboard will be filtered to Region=South since *URL filters* are evaluated first
taking precedence over the *Cookie-based sticky filters*

***

## Troubleshooting Filters

### Filter Options are not visible

* Verify that either "Get Filter Options from Data" or the manual Options list is configured.

### I want to apply a filter across Dashboards but I do not want to show the Curator Filter UI

* Use [Hidden Sticky Filters](/embedding_using_analytics/filters_parameters/hidden_sticky_filters_and_parameters)
  instead

### My view is empty after I switched tabs on my dashboards

* If your view loads briefly and then suddenly turns blank, then a filter is probably being applied that should
  not be applied. That can happen if you either track filter and parameter changes in the url (a) or you have a
  sticky filter enabled (b) which should not be applied to this view.
  * a) Turn on **Ignore Filter and Parameter Changes from Dashboard** on the Dashboard level which
    will stop adding the changes to the url. When you switch tabs, the filter and parameter actions need to be
    defined in the Workbook itself. However please note, that turning this on will break Report Builder's functionality.
  * b) Apply Filter Blacklists to prevent filters being applied on specific sheets. However, this
    does not currently work with Hidden Sticky Filters and Parameters.

### Date Filters show differently for my global users

* That is not necessarily an issue because Curator can handle locale date formats.
* Locale-specific formats (e.g., DD/MM/YYYY, MM/DD/YYYY) depend on:
  * Browser language settings.
  * Tableau User Language and Region settings.
* As long as your Workbook is flexible with date formats, Curator will handle dates for your different users and
  present them the format they are used to based on their settings.

### Date Filters do not filter properly

* This is mostly due to a locale mismatch: Ensure browser and Tableau settings align. You have three options:

1. When you have multiple regions that are working with your Dashboard, make sure that the Workbook's locale is
   set to automatic when published to Tableau. It will then adjust to your users location which Curator will also
   look pick up and then send the date in the expected format.
2. If you require a specific format you can also force the browser to use the specific locale date format instead
   which again Curator will pick up.
3. You can also use dates in YYYY-MM-DD format and it will ignore any browser or Workbook settings and just handle
   dates correctly in that format.


# Hidden Sticky Filters and Parameters
Source: https://docs.curator.interworks.com/embedding_using_analytics/filters_parameters/hidden_sticky_filters_and_parameters

Configure invisible persistent filters and parameters that remain active across user sessions and dashboard navigation.

Hidden sticky filters and parameters are used to remember the filter/parameter values a user selects across the system,
without showing up in the filters list on a Dashboard.

You can blacklist sheets for the Hidden Filter to not apply to. The name should match the sheets' name in Tableau.

## To create a hidden sticky filter/parameter

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Settings** > **Tableau** > **Tableau Server Settings** in the left-hand menu.
4. Click the "General" tab at the top.
5. Expand the "Sticky Filters" section and toggle on "Use Hidden Sticky Filters".
6. Click to add a new item under hidden sticky filters or hidden sticky parameters section.
7. Enter the name of the filter/parameter.
8. Click the "Save" button.

## Filter Blacklists

If you have individual sheets that a filter should not be applied to Curator's Filter Blacklists can help here.
Curator provides two types of filter blacklists to control where filters are applied within Tableau Dashboards:
filter-specific blacklists and global sheet-specific blacklists.

### Filter-Specific Blacklists

A filter-specific blacklist allows you to prevent a specific Curator filter from being applied to selected sheets.
This requires the Curator filter to be present in the front-end.

To configure a filter-specific blacklist:

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Tableau** > **Filter** > select the filter that should not be applied to all sheets.
4. In the **Display Options** section, add one item to the **Sheet Blacklist** per sheet you want to exclude from the
   filter.

If multiple filters need to be excluded from the same set of sheets, you can create a reusable **Filter Blacklist
Group**:

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backen`).
2. Log in if prompted.
3. Click on **Tableau** > **Filter Blacklists**.
4. Create a new blacklist group.
5. Name your blacklist group.
6. Add one item per sheet you do not want the filter to be applied to to the Sheet Blacklist.
7. Navigate to your Filter to apply the Filter Blacklist Group. Click on **Tableau** > **Filter** > select the filter
   that should not be applied to all sheets.
8. In the **Display Options** section, toggle on **Use Filter Blacklist Group**.
9. Select the Filter Blacklist group that you created in steps 3-6.

### Global Filter Sheet Blacklists

If you need to exclude sheets from a hidden sticky filter, a global filter blacklist must be used. This applies
to filters that are not explicitly present in the Curator UI but are set as sticky and therefore influence the
Dashboard on load with the last value set applied. Or because Hidden Sticky Filters or Parameters are enabled.

To configure a global filter blacklist:

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backen`).
2. Log in if prompted.
3. Click on **Settings** > **Tableau** > **Tableau Server Settings**.
4. Open the Filters and Parameters section.
5. Add the respective sheets to the Global Filter Sheet Blacklist.

If you using Filter Blacklist is slowing down your Dashboard load performance, there is a workaround within
Tableau. Following the below steps is more performant on especially large Dashboards.

1. In Tableau Desktop (or Tableau Server Edit Mode), go to the sheet that the filter should not be applied on.
2. Duplicate the data source the filter field(s) comes from.
3. Replace the existing fields on your sheet with the fields from the duplicated data source.
4. **Rename the filter field**, regardless of whether used on your sheet or not. ***Note:*** If you are not using the
   filter field on your sheet, you may as well delete it from your duplicated data source. By renaming/deleting it, you
   ensure that the filter request will have no effect on this specific sheet.
5. Repeat for all other fields the sheet should not be filtered by.
6. Repeat for all sheets that should not listen to the filter(s).
7. Republish your Dashboard.


# Parameters
Source: https://docs.curator.interworks.com/embedding_using_analytics/filters_parameters/parameters

Set up parameters to control dashboard behavior and calculations, enabling dynamic user interactions with analytics content.

Parameters are used for various purposes within a Dashboard. The system provides a user-friendly way to enter and
change the parameter values for dashboards. Parameters can even be shared with more than one Dashboard.

## To create a parameter

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Tableau** > **Parameters** in the left-hand menu.
4. Click the "New Parameter" button.
5. Enter the name of the parameter you want to be shown to your users in the "Display Name" field.
6. Enter the name of the parameter from the Dashboard in the "Parameter Name" field. This field text should be edited
   to match the field name in the data exactly. If there are any trailing white-spaces those will be removed on saving so
   you will need to remove them from the data name.
7. Select the parameter type.
8. Select the filter category if desired. See the [Filter Categories Section](/embedding_using_analytics/filters_parameters/filter_categories)
   for more
   information.
9. Select existing dashboards to add the parameter to them.
10. If you want to, enter a default value for the parameter to load the Dashboard with initially.
11. If you want the parameter value to be remembered from one Dashboard to the next, turn on the sticky parameter feature.
12. If you want to get the parameter options from the Dashboard's allowable values list, turn on that feature.
13. If you want to get the parameter options from the Dashboard's data, turn on the "get parameter options from data"
    feature. Note that this will be slow if the Dashboard contains a lot of data.
14. Add parameter options if not getting the options directly from the Dashboard.
15. Click the "Save" button.

## Or add a parameter to a Dashboard from the Dashboard

1. While editing the Dashboard, click on the "Misc" tab.
2. Expand the "Filters & Parameters" section.
3. Select the parameter(s) that are applicable to the Dashboard.
4. Click the "Save" button.

## To apply a Parameter

1. Navigate to the frontend of the system (e.g. `http://curatorexample.com`).
2. Log in if prompted.
3. Navigate to the desired Dashboard by using the navigation menu.
4. Open the filter menu on the right side of the screen.
5. Select or enter the value of the parameter.

### Multi Select Parameter Controls

Currently, Tableau does not offer multi-select-parameter controls. Instead, you can select one parameter value at a
time or type the long names by hand. In Curator, you can set up a parameter to allow multi-selection of your parameter
values without typing everything in.

1. Navigate to Tableau Desktop (or Tableau Server Edit Mode), and go to the sheet that the parameter should be applied to.
2. Create the parameter you need, and make sure
   * the Data type is a ***String***
   * the Current value is set to ***(ALL)***
   * the Allowable values is set to ***All***
3. Create a calculated field
   * `[param name]='(ALL)' OR CONTAINS([param name], [values field])`
   * Drag the calculated field onto the filter shelf and allow only ***True***
4. Publish Dashboard.
5. Do the steps described above to create a parameter in Curator backend, make sure
   * the Parameter type is ***Multi-Select***
   * toggle on ***Get parameter options from a field in the data***
   * enter the name of \[values field] (see 3.a) in ***Field Name*** input field
6. Click the "Save" button

### Step-by-step Guide

You can also follow the
[step-by-step guide](https://interworks.com/blog/tladd/2018/07/16/5-steps-to-enabling-a-multi-select-parameter-control-in-tableau/)
with screenshots that Tanner put together.


# Preloading Filters and Parameters
Source: https://docs.curator.interworks.com/embedding_using_analytics/filters_parameters/preloading_filters_and_parameters

Improve user experience by preloading filter and parameter values to reduce wait times during dashboard interactions.

## Setup

When you filter your Tableau Dashboards in Curator, this is typically done through the Tableau JavaScript API after the
Dashboard has loaded. This post-load filtering process will cause the Dashboard to refresh. If the filter or parameter
values are already known before the Dashboard is loaded, though sticky filters/parameters or because you want to
explicitly define them, you can take advantage of Preload Filters and Parameters. This feature injects the filter and
parameter values directly into the Dashboard’s initial load request (within the HTML), rather than applying them via
JavaScript afterward. The result is a faster, cleaner user experience with no visible reload.

When using Tableau's Connected Apps for the Embed authentication ([more details on Connected Apps](/creating_integrations/tableau_connection/embed_authentication))
you can no longer preload filters and parameters by appending them to the Tableau Server Dashboard URL on the
edit page of a Dashboard. Instead you can specify them by following these steps:

1. Navigate to your Curator backend > Tableau > Dashboards.
2. Select the Dashboards you want to define filters or parameters for that should be applied on load.
3. Switch to the Filters tab and open the **Preloading Filters & Parameters** section.
4. Add an item and enter the filter's/parameter's name into the name field as shown in the datasource/in the workbook.
5. Enter the value that you want the filter/parameter to preload with into the value field. You can leave it blank if
   you want the Dashboard to listen for possible preload options given through the Curator URL or sticky filters/parameters.
6. Specify whether this is a filter or a parameter in the type field.
7. Save the Dashboard.

> **Note:** When trying to filter on secondary datasources you'll likely see unexpected behavior.
> This is due to Tableau's embedding limitations. The JavaScript API still works on secondary
> datasources, but preloading may not function as expected.

When using Tableau's Trusted Ticket authentication (Attention: Deprecated!) you can append the name-value pairs to the
Tableau Server Dashboard URL directly.

## Preload Behavior

In the value field, you can enter the specific value you want the filter or parameter to preload with when the Dashboard
is initially rendered. This value will be directly injected into the HTML and used during the first load of the
visualization. No JavaScript will be executed to apply the filter/parameter, i.e. no reload will happen.
If you leave the value field blank, Curator will look for a matching value from other sources to optimize your initial
load experience, such as sticky filters/parameters saved from previous analysis steps or values passed through the
Curator URL (e.g., ?Region=West).
This makes the preload feature flexible: you can hardcode a default if needed, or allow Curator to dynamically detect
and apply a value based on your user's context.

### Full Domain Loading for Curator Filters

*This feature is only available when using [Connected Apps](/creating_integrations/tableau_connection/embed_authentication)
to authenticate to your Tableau Server.*

Curator gives you the flexibility to control whether Curator filters load with the full domain of
available values or only the subset of preloaded values. This setting can be configured individually for
each Dashboard.

To configure this behavior:

1. Navigate to your Curator backend > Tableau > Dashboards.
2. Select the Dashboard you want to configure.
3. Switch to the Filters tab and open the **Preloading Filters & Parameters** section.
4. Use the toggle **Preload Filters with Full Domain Values** to enable full domain loading or disable it to show
   only filtered values.

When enabled, users will see all possible filter values, maintaining full filtering capability while still benefiting
from the performance improvements of preloaded filters.

**Note**: To use the full domain values feature, ensure your field is placed on at least one filter shelf in your
Dashboard. The filter doesn't need to be visible or have a value applied, just Tableau needs to recognize it as a filter.

## Migration notice

If you used the Tableau Server Dashboard URL parameters you do not need to move everything manually once you are switching
to Connected Apps. They should be migrated for you once you upgrade to version when they became available. To have the
type automatically declared you will need to have Tableau's Metadata API enabled.
In case you want to rerun the migration and make sure filters and parameters are declared correctly do:

1. Run the migration command in the browser's address bar by just appending **/up** to you Curator domain.
2. In the console on your server, navigate to the root directory and run:

   ```php {/*cspell:disable-next-line*/} theme={null}
   php artisan tableauviz:updatepreloadsettings
   ```

   This will try to connect to the primary's Tableau Metadata
   API and check whether the specified names are parameters, otherwise they will be declared as filters.

To maintain previous functionality, we decided to migrate existing preload filters to not load the full domain of values.
However you can easily adjust the setting per Dashboard according to your needs.


# Specify Filter Sheet
Source: https://docs.curator.interworks.com/embedding_using_analytics/filters_parameters/specify_filter_sheet

Configure which specific worksheet or sheet should be used as the source for filter controls and options.

Curator provides the ability to get your filter options from the data. The standard dynamic filtering looks at the first
worksheet loaded. However, you may have multiple data sources compromising your Dashboard or a slow-loading worksheet
you want to avoid. Use the steps below to specify a worksheet to improve load time and narrow the scope of the data
that Curator has to retrieve to populate your filter values.

## To enable Specify Filter Sheet

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Tableau** > **Dashboards** in the left-hand menu.
4. Click on the Dashboard you want to edit.
5. Click the Misc tab.
6. Toggle on the Specify Filter Sheet option in the Filters & Parameters section.

This will display two additional fields "Filter Worksheet" and "Use Summary Data". The "Filter Worksheet" field will
allow you to specify the name of the worksheet to pull from. The switch for "Use Summary Data" uses a quicker API call
that pulls from the Summary Data rather than all of the Underlying Data. To determine if what you're looking for is in
the Summary Data you will need to View Data within your workbook on Tableau Desktop.


# Adding a Power BI Report
Source: https://docs.curator.interworks.com/embedding_using_analytics/power_bi_reports/adding_a_power_bi_report

Add and configure Power BI reports in Curator for seamless access via embedding.

Curator enables you to embed Power BI reports as a seamless part of your portal, providing your users with a unified
analytics experience, streamlining access to critical insights.

## Prerequisites

Before adding Power BI reports to Curator, ensure you have
[established your Power BI connection](/creating_integrations/power_bi_connection/curator_connection) and have reports
published to a Power BI workspace.

## Creating a Power BI Report in Curator

To add a new Power BI report to your Curator portal follow the steps below:

### Navigate to Power BI Reports

1. <BackendNavPath />
2. Click the **New Report** button
   <Frame>
     <img alt="Add new Power BI report from list page" />
   </Frame>
3. Fill out the details in the **Create Power BI Report** form:

   <Frame>
     <img alt="Create new Power BI report" />
   </Frame>

   * **Workspace**: Select the Power BI workspace containing the report.
   * **Report**: Select the specific report to embed.
   * **Title**: This appears in navigation menus and page titles - can be different from the Power BI report name.

The display options will allow you to control the appearance of the toolbar, the persistence of filters, the appearance
of the filter pane as well as the Power BI report Page Navigation.

Optionally, explore the Discovery and Display tabs to further customize how the report appears and is found by users
or linked to other content across your site.

Be sure to save your report before navigating away from the page.

## Adding Reports to Navigation

After creating a report, [add it to your site's menu](/site_content_design/menus/menu_items) for easy access and
automated authorization.

## Adding Reports to Pages

Once a Power BI Report has been added to Curator it can also be added to pages for a more dynamic layout.  Embed Power
BI reports in custom pages [using the Page Builder](/site_content_design/pages/power_bi_report).

## Security Considerations

Curator utilizes the permissions set within your Power BI tenant including both workspace-level permissions as well as
direct-access permissions.

### Workspace-Level Access

When a user has access to a workspace, they automatically have access to all reports within that workspace.
Curator checks workspace access to determine report visibility.  Due to performance concerns we strongly recommend
utilizing workspace-level access whenever possible.

### Direct Report Access

If a user does not have access to a workspace, Curator will check for direct access permissions to individual reports. This
allows for more granular control over report access but can lead to performance issues due to limitations in the Power
BI APIs.


# Email Option
Source: https://docs.curator.interworks.com/embedding_using_analytics/report_builder/email_option

Configure email delivery settings for automated report distribution including recipients, formatting, and attachment options.

This feature allows the frontend user to email their newly created report to multiple individuals. The Report Builder
Email Option requires that the Report Builder feature is enabled and that Curator is configured to send out emails. You
can set up the Mail configuration settings on the left navigation in the Mail section of the Settings.

## Enable Report Builder Email Option

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. In the left hand navigation click on **Settings** > **Curator** > **Portal Settings**.
4. Click on the "Features" tab at the top of the main page content.
5. Scroll down to, and expand, the "Toolbar Buttons (Curator Actions)" section.
6. Click to toggle on the "Report Builder: Email Option" button and click the "Save" button.

## Configure the default bcc, subject, and body

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. In the left hand navigation click on **Settings** > **Curator** > **Portal Settings**.
4. Click on the "Report Builder" tab at the top of the main page content.
5. Scroll down to, and expand the "Report Builder: E-Mail Settings" section.
6. Fill out the "Email BCC Addresses", "Email subject", or "Email body" fields as desired, and click the "Save" button.

## Send an email with the built report

1. Navigate to the frontend of the system (e.g. `http://curatorexample.com`).
2. Log in if prompted.
3. Navigate to the desired Dashboard by using the navigation menu.
4. Generate the images you want to use for your report.
5. Click on the presentation icon at the top right portion of the screen. Normally this is displayed on the right side
   of the title bar in the Dashboard.
6. Click on the email icon to "Email presentation as PDF".
7. Fill out the Email Address(es) field with the desired recipients. You can enter multiple email addresses by using
   commas to separate them.
8. If you have the correct permissions you can edit the subject and body.
9. Click the send button when finished.


# Fallback Image
Source: https://docs.curator.interworks.com/embedding_using_analytics/report_builder/fallback_image

Configure fallback images for reports when live dashboard content cannot be rendered or is unavailable.

There may be occasional issues when generating reports using Curator's Scheduled Reports.  This can be for a variety of
reasons, such as bad Tableau Server configuration, networking interruptions, permission changes, or dashboards getting
moved/deleted.  To handle these scenarios, the majority of them are fixed by simply having your user log back in to
Curator, and re-create the slide.  See the steps below on how to update the existing "Fallback Image" if you'd like to
customize this for your users.

## Updating the Fallback Image

Before you proceed below, you need to upload your file using the [File](/site_content_design/files/files)
system in Curator.

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
3. Click on the "Report Builder" tab at the top of the main page content.
4. Expand the "Report Builder E-Mail Settings" and update the Fallback Image.
5. Click the save button.


# Overview and Enabling Report Builder
Source: https://docs.curator.interworks.com/embedding_using_analytics/report_builder/overview_and_enabling_report_builder

Introduction to Report Builder functionality and step-by-step instructions for enabling report generation capabilities.

The system can allow users to export one or more Dashboard snapshots as a Microsoft PowerPoint or PDF presentation.

## Optimal Tableau Connection

This functionality requires either Trusted Ticket authentication is enabled, or that you use Connected Apps. However
**Connected Apps are the most stable option**.  If you are experiencing any issues with image-retrieval and you are
using Trusted Tickets with your Tableau connection, make sure to change to Connected Apps.

## Enable Report Builder

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Settings** > **Curator** > **Portal Settings** in the left navigation.
4. Click on the "Features" tab at the top of the main page content.
5. Scroll down to, and expand the "Toolbar Buttons (Curator Actions)" section.
6. Click to toggle on the "Report Builder" function and click the "Save" button.

## Download one or more dashboards as a PowerPoint or PDF presentation

1. Navigate to the frontend of the system (e.g. `http://curatorexample.com`).
2. Log in if prompted.
3. Navigate to the desired Dashboard by using the navigation menu.
4. Modify the filters, etc. as desired on the Dashboard.
5. Click on the presentation icon at the top right portion of the screen. Normally this is displayed on the right side
   of the title bar in the Dashboard.
6. Click on the camera icon to take a snapshot of the current Dashboard as a presentation slide.
7. Repeat steps 3-6 as desired to create the slides that should be included in the presentation. Note: You can navigate
   to other eligible dashboards to add as slides to the same PowerPoint presentation.
8. If you need to rearrange the ordering of the slides, you can drag and drop them as needed.
9. If you need to delete all of the slides, click on the trash can icon to remove them and repeat steps 3-6 as desired
   to add the correct slides.  If you need to delete a single slide, drag and drop the slide on to the trash can icon.
10. Click on the PowerPoint button to create a PowerPoint presentation of the specified slides. Click on the PDF button
    to create a PDF presentation of the specified slides.

## Adding all Tabs from a Single Workbook

When capturing slides for your Report Builder Report, you may want to capture the entirety of a workbook that has been
embedded into Curator.  This setting can be enabled by administrators and will present an optional button in the
Report Builder modal in addition to the standard "Capture Dashboard" button.  To enable this additional button:

1. Click on **Settings** > **Curator** > **Portal Settings** in the left navigation.
2. Click on the "Report Builder" tab.
3. Click to toggle ON the "Enable Workbook Capture" button and click the "Save" button.

NOTE: When using this feature with Connected Apps, Tableau requires that the Dashboard be published with the
[Show Sheets as Tabs](https://help.tableau.com/current/pro/desktop/en-us/publish_workbooks_howto.htm#show-sheets-as-tabs)
checkbox is selected.


# PowerPoint
Source: https://docs.curator.interworks.com/embedding_using_analytics/report_builder/powerpoint

Generate PowerPoint presentations from dashboard content using Report Builder for professional report delivery.

The [Report Builder](/embedding_using_analytics/report_builder/overview_and_enabling_report_builder)
functionality in Curator allows users to create Microsoft PowerPoint presentations of Tableau dashboards. We'll guide
you through setting up a template for these presentations, which can be automatically applied to your exported images.

## Setting Up PowerPoint Template

1. Create or open an existing Microsoft PowerPoint presentation.
2. Access Slide Master by clicking on the "View" ribbon and then the "Slide Master" button.
3. Identify Blank Layout: Look for the Blank layout in the Slide Master. This layout is used by the [Report Builder](/embedding_using_analytics/report_builder/overview_and_enabling_report_builder).
   * If Blank Layout is Missing:
     * Right-click in the left pane and select "Insert Layout".
     * Right-click on the newly created layout and select "Rename Layout".
     * In the pop-up, change the name to "Blank" and click "Rename".
4. Save Template: Save the presentation in an easy-to-find location on your computer.

**Note**: Powerpoint Presentations cannot contain more than one Slide Master.  In addition, some images formats are
unsupported as they become blended with Dashboard images on export.  If you need to convert these images, typically
clicking the "Convert to shape" button on the "Graphics Format" tab will suffice.

## Applying Template in Portal Settings

1. Access Portal Settings: Navigate to Settings > Portal Settings > Layout in your portal's backend.
2. Upload Template: In the "Powerpoint Template" field, upload the saved PowerPoint presentation.
3. Save Changes: Click the "Save" button to apply the template.

## Group Override settings

Utilize group override functionality to apply different templates for various Tableau user groups, adding excitement
and customization to presentations.


# Scheduled Reports
Source: https://docs.curator.interworks.com/embedding_using_analytics/report_builder/scheduled_reports

Configure automated report generation and distribution on recurring schedules for consistent business intelligence delivery.

The Scheduled Reports feature allows you to set a report to be sent out via email on a recurring schedule. This feature
requires that the
[Report Builder](/embedding_using_analytics/report_builder/overview_and_enabling_report_builder)
and
[Report Builder: Email Option](/embedding_using_analytics/report_builder/email_option)
both be turned on.

As of the 2024.09-02 release, [Scheduled Reports](/embedding_using_analytics/report_builder/email_option)
now have an unsubscribe option.  Recipients who receive the email can remove themselves from the distribution list -
unless they are the only recipient, in which case the report needs to be deleted to cease distribution via the schedule.

## Setup

### To enable the Scheduled Reports Option

1. Navigate to the backend of the system (e.g. `https://www.curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Settings** > **Curator** > **Portal Settings** in the left navigation.
4. Click on the "Features" tab at the top of the main page content.
5. Click to switch on the "Scheduled Reports Option" setting under the "Toolbar Buttons (Curator Actions)" section and
   click the "Save" button.

### To configure the default bcc, subject, and body

1. Navigate to the backend of the system (e.g. `https://www.curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Settings** > **Curator** > **Portal Settings** in the left navigation.
4. Click on the "[Report Builder](/embedding_using_analytics/report_builder/overview_and_enabling_report_builder)"
   tab at the top of the main page content.
5. Scroll down and expand the
   "[Report Builder Email Settings](/embedding_using_analytics/report_builder/email_option)"
   section.
6. Fill out the "Email BCC Addresses", "Email subject", or "Email body" files as desired, under the
   "[Report Builder Email Settings](/embedding_using_analytics/report_builder/email_option)"
   section and click the "Save" button.

### To send a scheduled report with the built report

1. Navigate to the backend of the system (e.g. `https://www.curatorexample.com/backend`).
2. Log in if prompted.
3. Navigate to the desired Dashboard by using the navigation menu.
4. Generate the images you want to use for your report.
5. Click on the presentation icon at the top right portion of the screen. Normally this is displayed on the right side
   of the title bar in the Dashboard.
6. Click on the Schedule button to "Schedule recurring report email".
7. Click on the "New Scheduled Report" button
8. Fill out the Email Address(es) field with the desired recipients. You can enter multiple email addresses by using
   commas to separate them.
9. If you have the correct permissions you can edit the subject and body.
10. Select the Recurring Schedule time frame you want your report sent out on.
11. Click the send button when finished.

## Existing Scheduled Reports

### Backend overview

1. Once Scheduled Reports are setup, navigate to the backend of the system (e.g. `https://www.curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Tableau** > **Scheduled Reports** in the left navigation.

In this view, you can see all existing Scheduled Reports and status information like ***last sent*** and
***is active?***. By using the checkboxes on the left side, you can select which Scheduled Reports you want to send out
immediately.
You can also create a new Scheduled Report by clicking on ***New Scheduled Report***.
By clicking on a specific Scheduled Report you enter Edit Mode. You can edit details of your Scheduled Report, change
the schedule, change the status and trigger sending out the report. You can also delete the Scheduled Report.

### Clone Scheduled Reports (2023.10-03)

To duplicate a scheduled report, this can be done on the backend of Curator by system administrators.  To clone a
report, simply visit the edit-report page, and click the "Clone" button in the top-right corner of the page.  This will
display a "Clone Report" page where you can change the title and create your new report.

### Frontend overview (available in release 2023.02.22)

If you want to give users an overview of their existing Scheduled Reports, follow the steps below:

1. Navigate to the backend of the system (e.g. `https://www.curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Settings** > **Curator** > **Portal Settings** in the left navigation.
4. Navigate to the **Features** tab > open the **Toolbar Buttons (Curator Actions)** section.
5. Enable **Manage my Scheduled Reports - Page**

As a frontend user:

1. Navigate to the frontend of the system (e.g. [https://www.curatorexample.com](https://www.curatorexample.com)).
2. Open the user menu in the top right corner by clicking on your username.
3. Click on **My Scheduled Reports**.

In this view, you can see all your existing Scheduled Reports and information like ***schedule***, ***timezone*** and
***is active?***.
By clicking on the pencil icon of a specific Scheduled Report you enter Edit Mode. You can edit details of your
Scheduled Report, change the schedule, change the status and trigger sending out the report.
By clicking on the bin icon, you delete the specific Scheduled Report.


# Watermark Text
Source: https://docs.curator.interworks.com/embedding_using_analytics/report_builder/watermark_text

Add custom watermark text to generated reports for branding, security, or identification purposes.

With Watermark Text, you can add your own custom text to the bottom left of every image exported out by the Report
Builder feature.

## Enable the Watermark Text

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Settings** > **Curator** > **Portal Settings** in the left navigation.
4. Click on the "Report Builder" tab at the top of the main page content.
5. Fill out the text field under the "Watermark Text" section and click the "Save" button.


# Adding a Dashboard
Source: https://docs.curator.interworks.com/embedding_using_analytics/tableau_dashboards/adding_a_dashboard

Learn how to create and configure Tableau dashboards in Curator for seamless embedding and display.

Curator excels at showcasing embedded Tableau dashboards as a seamless part of your Curator site.

\***Note:** Due to limitations in Tableau's JS API we do not support embedding worksheets.  We recommend adding a
worksheet to a Dashboard instead.

## Create a Dashboard

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`) and log in if prompted.
2. Navigate to **Tableau** > **Dashboards**.
3. Click on the "New Dashboard" button.
4. Fill out the **Tableau Server**, **Site**, **Project**, **Workbook** and **Dashboard** drop-downs to select the
   Dashboard you'd like to embed.
5. Populate the remainder of the fields as desired and click on the "Create" button.

## Dashboard Sizes

Curator respects the Dashboard sizes applied in Tableau. We experience that a fixed size ensures consistency in design
throughout many screen sizes. You wonder what the best suitable size is? Consider the size of your users' screens. How
much space do you need for navigation, titles, toolbar buttons and margins you want to apply.
Do you have dashboards that should take up the full remaining screen? Go to Tableau and set its size to *automatic* and
the Dashboard will stretch to all ends in Curator.


# Chrome 142 and Edge 143 Tableau Embedding Issues
Source: https://docs.curator.interworks.com/embedding_using_analytics/tableau_dashboards/chrome_edge_embedding_issues

Troubleshoot embedded Tableau views that fail to load in Chrome 142 or Edge 143 due to Local Network Access restrictions

## Overview

If you're running **Google Chrome 142** (or later) or **Microsoft Edge 143** (or later), you may find that embedded
Tableau views in Curator fail to load. Instead of seeing your Dashboard, you might see a blank area where the Tableau
content should appear.

This happens because of a new security feature in Chromium browsers called **Local Network Access restrictions** (LNA).
This feature blocks public websites from connecting to devices or services on your local network. While Curator and
Tableau Server/Cloud use only public HTTPS endpoints, certain security tools on your computer can trigger this
restriction and break embedded Tableau views.

<Warning>
  This is a browser security feature that Curator and Tableau cannot override from the server side. Your IT team will
  need to configure browser policies to fix this issue permanently.
</Warning>

You can read more about this feature in [Chrome's developer blog](https://developer.chrome.com/blog/local-network-access)
and [Tableau's documentation](https://help.salesforce.com/s/articleView?id=005228129\&language=en_US\&type=1).

***

## Symptoms

<Frame>
  <img alt="Example error message" />
</Frame>

You'll know you're experiencing this issue if you see:

* You might see a **blank area, loading screen, or error message** where Tableau content should appear.
* **Error messages** in the browser saying a public page tried to connect to devices on the local network.
* **Content loads in other browsers** - The same Tableau views work fine in Firefox, Safari, or older versions of Chrome/Edge.
* **Works on other devices** - The views load normally on personal devices that aren't connected to your corporate network.

***

## Why this happens

### What is Local Network Access?

Chrome 142 ([release notes](https://developer.chrome.com/release-notes/142#local_network_access_restrictions)) and Edge 143
([release notes](https://learn.microsoft.com/en-us/microsoft-edge/web-platform/release-notes/143#local-network-access-from-non-secure-contexts))
introduced Local Network Access (LNA) restrictions to protect users from malicious websites trying to access devices
on their local network.

When a public website tries to connect to these addresses, the browser will block or prompt:

* **Loopback addresses:** `127.0.0.1`, `localhost`
* **Private IP ranges:** `10.x.x.x`, `172.16-31.x.x`, `192.168.x.x`
* **Carrier-grade NAT ranges:** `100.64.0.0` to `100.127.255.255` (commonly used by security products)

### Why does this affect Curator?

In most cases, Curator and Tableau use only public HTTPS endpoints, so LNA shouldn't be triggered. However, in
corporate environments with certain security tools installed, those tools may create connections to local addresses
while you're using Curator.

Common security tools that can trigger this issue:

* **[Zscaler Client Connector or ZPA](https://trust.zscaler.com/posts/26216)** - Uses IP range `100.64.0.0` and higher
  for internal routing
* **[Duo Desktop](https://help.duo.com/s/article/9470)** - Runs a local helper service
* **[Okta FastPass](https://support.okta.com/help/s/article/configure-chrome-to-suppress-the-local-network-access-prompt-for-okta-fastpass)**
  \- Uses local authentication components
* **[Box Tools](https://support.box.com/hc/en-us/articles/45163820905107)** - Connects to local services
* **Other DLP or endpoint security agents** - May expose local HTTP services

When one of these tools is running, your browser sees this as "public site (Curator) accessing local network" and
applies LNA restrictions. If this happens while loading a Tableau view in an iframe, you often won't see a prompt—the
embedded content will simply fail to load.

***

## Who is affected

You'll see this issue if:

1. You're using **Google Chrome 142** (or later) or **Microsoft Edge 143** (or later)
2. Your organization uses security tools like those listed above that rely on local addresses or carrier-grade NAT ranges
3. You're accessing Curator on a managed corporate device

If you're using Firefox, Safari, or older versions of Chrome/Edge, you typically won't see this issue.

***

## Quick troubleshooting for end users

If embedded Tableau views aren't loading in Curator, try these quick checks:

1. **Test in another browser** - Try Firefox or Safari to see if the views load normally. If they do, this confirms an
   LNA issue.

2. **Check your browser version**
   * In Chrome: Go to `chrome://settings/help`
   * In Edge: Go to `edge://settings/help`
   * If you see version 142+ (Chrome) or 143+ (Edge), LNA may be the cause

3. **Test on a different device** - Try accessing Curator from a personal device or home network. If it works there,
   the issue is related to your corporate security tools.

4. **Contact your IT team** - Share this article with them. They'll need to configure browser policies to fix the issue permanently.

***

## Diagnostic steps for IT teams

If users are reporting blank or failed Tableau embeds, follow these steps to confirm this is an LNA issue:

### Step 1: Confirm the environment

Check that:

* Users are on Chrome 142+ or Edge 143+
* Affected devices are managed corporate machines
* Users have security tools installed (Zscaler, Duo Desktop, Okta FastPass, Box Tools, or similar)

### Step 2: Inspect the browser console

On an affected computer:

1. Open Curator and navigate to a page with an embedded Tableau view that's failing to load.
2. Open **Developer Tools** in the browser:
   * Chrome: Press `F12` or `Ctrl+Shift+I` (Windows) / `Cmd+Option+I` (Mac)
   * Edge: Press `F12` or `Ctrl+Shift+I` (Windows) / `Cmd+Option+I` (Mac)
3. Click the **Network** tab in Developer Tools.
4. Reload the page and look for failed requests:
   * Look for error messages mentioning **Local Network Access**
   * Check for remote addresses in these ranges:
     * `127.0.0.1` or `localhost`
     * `10.x.x.x`, `172.16-31.x.x`, `192.168.x.x`
     * `100.64.0.0` to `100.127.255.255` (used by Zscaler and others)
5. For failed requests, check the **Initiator** or **Origin** column to see which site initiated the request.

### Step 3: Capture diagnostic information

Take screenshots or note:

* The full URL of any failing requests
* The remote IP address and port
* Which security tool is involved (based on the URL/IP)
* The browser version

This information will help you determine which domains to allowlist in browser policies.

***

## Solutions for managed environments

For corporate-managed Chrome and Edge browsers, your IT team needs to configure Local Network Access policies to
allowlist trusted domains.

### For Google Chrome

Your IT team should configure Chrome enterprise policies ([full policy list](https://chromeenterprise.google/policies))
using your management platform (Group Policy, Jamf, Intune, etc.).

**Key policies** ([atomic group documentation](https://chromeenterprise.google/policies/atomic-groups)):

* `LocalNetworkAccessAllowedForUrls` - List of domains allowed to make local network requests without prompting
* `LocalNetworkAccessBlockedForUrls` - List of domains blocked from local network access
* `LocalNetworkAccessRestrictionsTemporaryOptOut` - Temporary opt-out (reverts to pre-142 behavior)

#### Example configuration

In JSON format for Chrome policy:

```json theme={null}
{
  "LocalNetworkAccessAllowedForUrls": {
    "Value": [
      "https://your-curator-domain.com",
      "https://your-tableau-server.com"
    ]
  }
}
```

<Info>
  Replace the example domains with:

  * Your Curator portal URL(s)
  * Your Tableau Server or Tableau Cloud URL(s)
  * Any identity provider domains if you use SSO
</Info>

**To verify the policy is working:**

1. On a managed computer, open Chrome and navigate to `chrome://policy`
2. Search for "LocalNetworkAccess" in the policy list
3. Verify that your `LocalNetworkAccessAllowedForUrls` policy appears with the correct domains

**Temporary workaround:**

If you need time to configure policies properly, you can temporarily enable `LocalNetworkAccessRestrictionsTemporaryOptOut`
to restore the old behavior. Note that Chrome plans to remove this option in a future release, so this is only a
short-term solution.

### For Microsoft Edge

Edge has equivalent policies
([policy documentation](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-policies)) that work the same way.

**Key policies:**

* [`LocalNetworkAccessRestrictionsEnabled`](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-browser-policies/localnetworkaccessrestrictionsenabled)
  \- Enable or disable the restriction
* [`LocalNetworkAccessAllowedForUrls`](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-browser-policies/localnetworkaccessallowedforurls)
  \- Allowlist specific domains
* [`LocalNetworkAccessRestrictionsTemporaryOptOut`](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-browser-policies/localnetworkaccessrestrictionstemporaryoptout)
  \- Temporary opt-out

#### Example Edge configuration

In Group Policy:

1. Navigate to **Administrative Templates** > **Microsoft Edge** > **Network settings**
2. Open the **Allow sites to make requests to local network endpoints** setting
   (`LocalNetworkAccessAllowedForUrls`)
3. Enable the policy and add your domains:
   * `https://your-curator-domain.com`
   * `https://your-tableau-server.com`
4. Click **OK** and apply the policy

**Temporary workaround:**

If needed during transition, you can set **Local Network Access restrictions** (`LocalNetworkAccessRestrictionsEnabled`)
to **Disabled**. This should only be used temporarily while you configure the proper allowlist.

***

## Temporary workaround for individual users

If you need immediate access while your IT team configures the policies, you can temporarily disable Local Network
Access checks in your browser.

<Warning>
  This is a temporary workaround only. Your IT team should implement the browser policies above for a permanent solution.
  This setting may be reset when your browser updates or if your IT team enforces policies.
</Warning>

### Chrome flags workaround

1. Open Chrome and go to `chrome://flags/` in the address bar.
2. Search for "Local Network Access" in the search box at the top.
3. Find the **Local Network Access Checks** flag and click the dropdown next to it.
4. Select **Disabled** from the dropdown.
5. Click the **Relaunch** button that appears at the bottom of the page to restart Chrome.

### Edge flags workaround

1. Open Edge and go to `edge://flags/` in the address bar.
2. Search for "Local Network Access" in the search box at the top.
3. Find the **Local Network Access Checks** flag and click the dropdown next to it.
4. Select **Disabled** from the dropdown.
5. Click the **Restart** button that appears at the bottom of the page to restart Edge.

After restarting, try accessing the Tableau views in Curator again. They should load normally.

***

## Consider switching to Connected Apps

If your Curator system is currently using **Tableau Default** or **Trusted Tickets** for Tableau authentication,
switching to **Connected Apps** may resolve embedding issues related to Local Network Access restrictions.

These authentication methods often involve additional redirects and local network interactions that can trigger LNA
restrictions in Chrome 142+ and Edge 143+. Connected Apps use a more streamlined authentication flow that is less
likely to be affected by these browser security features.

***

## Additional vendor-specific guidance

If you've identified which security tool is causing the issue, these vendor guides may help your IT team configure
both the browser policies and the security tool itself:

* **Tableau:** [Embedded Tableau views fail to load after Chrome 142](https://help.salesforce.com/s/articleView?id=005228129\&language=en_US\&type=1)
* **Zscaler:** [Chrome 142 Local Network Access Advisory](https://trust.zscaler.com/posts/26216)
* **Duo Desktop:** [Chrome 142 and Edge 143 Changes](https://help.duo.com/s/article/9470)
* **Okta FastPass:**
  [Configure Chrome for Local Network Access](https://support.okta.com/help/s/article/configure-chrome-to-suppress-the-local-network-access-prompt-for-okta-fastpass)
* **Box Tools:** [Allow Local Network Access in Chrome and Edge](https://support.box.com/hc/en-us/articles/45163820905107)


# Custom Views
Source: https://docs.curator.interworks.com/embedding_using_analytics/tableau_dashboards/custom_views

Configure and enable custom views functionality to allow users to save and reload dashboard states with applied filters and parameters.

Curator can allow users to save a Custom View of a Dashboard, which will include any applied filters and parameters, and
then load it again at a later date.

## Enable Custom Views

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on the **Settings** > **Curator** > **Portal Settings** in the left-hand side navigation.
4. Click on the "Features" tab at the top of the main page content.
5. Click to switch on the "Custom Views" setting under the "Toolbar Buttons (Tableau Actions)" section and click the
   "Save" button.

## Enable create/load a Custom View

1. Navigate to the frontend of the system (e.g. `http://curatorexample.com`).
2. Log in if prompted.
3. Navigate to the desired Dashboard by using the navigation menu.
4. Modify the filters, etc. as desired on the Dashboard.
5. Click on the Custom Views icon at the top right portion of the screen. Normally this is displayed on the right side
   of the title bar in the Dashboard.
6. Enter a name for the new Custom View in the text box and click the "Create" button.
7. To load a different Custom View, select an existing view from the drop-down and click on the "Apply" button.

## Sharing Direct Links to Custom Views

Custom Views can be shared via direct URL links, allowing users to access specific Custom Views without manually
selecting them from the dropdown. This functionality works similar to Tableau's native Custom View sharing capabilities.

### How to share a Custom View via direct link

1. **Apply the desired Custom View** using the steps above (steps 1-7).
2. **Copy the current URL** from your browser's address bar. The URL will automatically include the Custom View parameter.
3. **Share the URL** with other users who have access to the Dashboard.

### URL Parameter Format

Custom Views are accessed through the `curator_custom_view` URL parameter (or the legacy `::custom_view` parameter for
backward compatibility). For example:

```txt theme={null}
http://curatorexample.com/dashboard-name?curator_custom_view=MyCustomViewName
```

When a Custom View is loaded, Curator automatically adds a Custom View ID parameter (`cvi`) to the URL:

```txt theme={null}
http://curatorexample.com/dashboard-name?curator_custom_view=MyCustomViewName&cvi=abc123def456
```

The `cvi` (Custom View ID) URL parameter contains Tableau's unique identifier (LUID) for the Custom View, which ensures the
correct view is loaded even if multiple Custom Views share the same name. This parameter gets automatically added to the
URL for troubleshooting purposes by Curator. If no Custom View ID is provided via URL load, the first Custom View by
match on name is selected and its ID is added as the cvi parameter.

If a URL contains both the Custom View name and ID parameters, the `cvi` parameter takes precedence to ensure
the exact Custom View is loaded. This means you can safely share URLs that include both parameters without
worrying about ambiguity.

#### Legacy URL Format

For backward compatibility, the legacy `::custom_view` parameter is still supported:

```txt theme={null}
http://curatorexample.com/dashboard-name?::custom_view=MyCustomViewName
```

However, new Custom View links will use the modern `curator_custom_view` parameter format.

### Sharing Private Custom Views

Private Custom Views are only visible in the dropdown for the user who created them. However, similar to
[sharing a Custom View in Tableau](https://help.tableau.com/current/pro/desktop/en-us/customview.htm#share-a-custom-view)
anyone with access to the Dashboard can see a Custom View using the direct link [outlined above](#how-to-share-a-custom-view-via-direct-link).


# Dashboard Settings
Source: https://docs.curator.interworks.com/embedding_using_analytics/tableau_dashboards/dashboard_settings

Complete guide to configuring Tableau dashboard settings in Curator including display, functionality and integration options.

When adding a Tableau Dashboard to the Curator backend, there are several tabs that offer a range of settings to
customize the integration, display, and functionality of your Dashboard. This guide will walk you through each tab
and its available options, ensuring you make the most of Curator’s features to enhance your Tableau experience.

To access these settings:

1. Navigate to the backend of the system and log in if prompted.
2. Navigate to Tableau > Dashboards.
3. Select the Dashboard for which you want to adjust the settings.

If you have not added a Dashboard yet, check out our [Adding a Dashboard Guide](/embedding_using_analytics/tableau_dashboards/adding_a_dashboard)

Below, you find detailed explanations of all the toggles, input fields, and settings within each tab:

## Tab: Dashboard

This tab contains the primary settings for adding a Tableau Dashboard to Curator. When you select a Dashboard
from the dropdown fields, the input fields below will automatically populate with the corresponding values.

* **Title**: The name of the Dashboard as it will appear in the Curator portal. It automatically picks up the
  title of your Dashboard from Tableau, but you can adjust it here if you prefer a different title. If you want
  to change titles in Curator, ensure you have the *Use Curator Dashboard Titles* toggle enabled in your Portal
  Settings (Backend > Settings > Curator > Portal Settings > Features tab > Usability section).

* **Tableau Server Dashboard URL**: The direct URL to the Dashboard on Tableau Server. No changes are needed here.
  This is useful for ensuring you are embedding the correct Dashboard - copying and pasting this into a new tab
  ensures you're certain of the Dashboard you're embedding.

* **Curator Dashboard URL "Slug"**: The ending of the URL used to access the Dashboard in Curator. You can adjust
  this as needed, but note that special characters are not supported. The full link to your Dashboard is displayed
  in the top right corner of the edit-Dashboard page.

* **Dashboard Tabs**: Determines whether or not other Dashboards published in the workbook should be shown
  and how. The display options are:

  1. **Off** - Do not show any other Dashboards from this workbook.
  2. **Styled (Web Friendly)** - Show tabs that can be styled in the Themes (Backend > Settings > Curator > Themes >
     select your Theme > *Title and Toolbar* tab). Check out our Design options [here](/site_content_design/theme/titles_and_toolbars).
  3. **Tableau Server Native** - Show tabs as they appear on Tableau Server. When using this option it is important to
     know that Tableau renders the Dashboard with the largest dimensions assigned in the workbook. This may lead to
     scroll bars within the iframe. Please refer to the [Knowledge Base article for more info](https://help.salesforce.com/s/articleView?id=001474123\&type=1).

  **Note:** This selection field is influenced by two factors:

  1. To make a selection, you need to publish your workbook with sheets as tabs.
  2. A global setting takes precedence over whether or not you can show tabs. This setting is found in Tableau
     Server Settings (Backend > Settings > Tableau > Tableau Server Settings > Workbooks section
     > **Global Dashboard Tabs** selection field).

## Tab: Discovery

This tab focuses on how the Dashboard will be discovered within the Curator portal.

* **Search & Content Discovery**: Add keywords to associate with your Dashboard. When users search for the specified
  keyword, the Dashboard will appear in the results. To add new keywords refer to [this guide](/site_content_design/content_discovery/keywords).

  If you turn on the **Hidden** switch, this Dashboard will not be discoverable through search, and it will not be
  displayed in any tiles or in the Explorer.

  The **Featured** flag adds the Dashboard to the list of featured Dashboards. This list can be used for content
  selection in Tiles, Explorer, Feed, and List elements on your pages.

* **Description**: Add context to your Dashboard. This information can be displayed in two places:

  1. **On hover over tiles**:
     * The global setting can be adjusted in Themes (Backend > Settings > Curator > Themes > select your Theme >
       Pages tab > Tiles Styles on the left-hand side > *Show Tile Description* selection field).
     * The individual setting is on the Page > Tiles Element > Tiles Settings > *Show Description*.
     * **Note:** The global setting will enable the individual setting.
  2. **In the toolbar**: Show the description when navigating to the frontend page of the Dashboard. To enable this, go to
     Backend > Settings > Curator > Portal Settings > Features tab > Toolbar Buttons
     (Curator Actions) > switch on *Dashboard Info Button*.

* **Related Content**: Associate menu items with your Dashboard. You can set how related content is displayed in
  Backend > Settings > Curator > Portal Settings > Features tab >
  Usability section > *Related Content Position* selection field.

* **New & Updated Flags**: Use the toggles to manually add a flag to the Dashboard that notifies your users.

## Tab: Display

In this tab, you can configure the visual aspects and layout of how the Dashboard will be displayed within Curator.

* **Thumbnail/Icon**: This displays the current thumbnail of your Dashboard, retrieved using Tableau's REST API
  during regular cron jobs. You can delete the current image by clicking the "x" next to the file name.
  In *Alternate Thumbnail URL*, you can specify a different URL to retrieve the thumbnail. If you want to
  refresh the thumbnail immediately, use the *Refresh Thumbnail* button. If you prefer to upload a static image,
  use the *Icon Image* file upload instead.

* **Loading Screen**: Select the loading screen to display while this Dashboard is loading. If you want to add new
  loading screens to the options, check out [this guide](/site_content_design/loading_screens/loading_screens).

* **Tutorial**: Select a tutorial to show when users navigate to the Dashboard.
  [This guide](/site_content_design/user_notifications_and_email/tutorials)
  walks you through the steps of how to create a tutorial.

* **Comments**: Enable [*User Commenting*](/embedding_using_analytics/data_manager/user_commenting)
  if you want to allow users to add comments to the Dashboard. To use this feature, you need to have Data Manager
  enabled. If you don't have Data Manager enabled yet, refer to [these steps](/embedding_using_analytics/data_manager/data_manager_basics).
  Comments are stored in the Curator database in the `interworks_datamanager_comment` table.

* **Mobile**: Point to a different Dashboard on Tableau Server for use in mobile view. *Note* that this feature is
  deprecated and will be removed in a future release.

## Tab: Filters

The Filters tab allows you to configure the filters and parameters available for users interacting with the Dashboard.

* **Filters**: Add any of the selectable Curator filters to the Dashboard. Filters that don't match any field in your
  applied data source will be greyed out.
  Check out [this guide](/embedding_using_analytics/filters_parameters/filters)
  to add new Filters.

* **Parameters**: Add any of the selectable Curator parameters to the Dashboard. Parameters that don't match any field
  in your applied data source will be greyed out.
  Check out [this guide](/embedding_using_analytics/filters_parameters/parameters)
  to add new Parameters.

* **Specify Filter Sheet**: Specify a sheet from your Dashboard to retrieve filter or parameter options if you want to
  customize Curator's default behavior. Check out
  [this documentation](/embedding_using_analytics/filters_parameters/specify_filter_sheet)
  for all the details.

* **Ignore Filter and Parameter Changes from Dashboard**: By default, Curator listens to filter and parameter changes
  made within the Dashboard and adds them to the Curator URL. This allows the Dashboard to be reloaded with the same
  filters and parameters applied without resetting them. If you prefer not to have this behavior for your Dashboard,
  turn on this switch.

## Tab: Advanced

This tab provides access to more advanced settings and customizations.

* **Data Export Options**: Configure export options for your users. If allowing CSV and/or Excel exports, you can
  either show a list of worksheets for data export or specify a worksheet for automatic download. Alternatively,
  you can specify a link for the export in the *Alternate CSV Link* field. You can also provide an *Alternate PDF
  Link* for downloading in PDF format. *Note*: You need to enable the export features in
  Backend > Settings > Curator > Portal Settings > Features Tab > Toolbar Buttons (Tableau Actions) section.

* **Report Builder**: If Report Builder is enabled, you can specify a sheet for export to presentations in the
  *Use PPTX Tab* field. You can also specify an *Alternate Report Builder Dashboard Link* to use this Dashboard
  for export instead. More details on the Report Builder feature are documented
  [here](/embedding_using_analytics/report_builder/overview_and_enabling_report_builder).

* **Menu Options**: Turn on the *Treat as a Workbook?* switch if you want all Dashboards in this workbook to be
  listed under this Dashboard's menu item. This option also enables tabs.

* **Embedded Options**: Adjust these settings to refine how your Dashboard is embedded in Curator. Your options are:
  1. **Link Target**: Override where links from within the Dashboard should load. For more information, click
     [here](https://help.salesforce.com/s/articleView?language=en_US\&id=url-actions-open-a-new-browser-tab-instead-of-the-same-tab\&type=1\&type2=1).
  2. **Show Toolbar**: Switch on if you want to show the Tableau Server toolbar below the Dashboard, in addition
     to or instead of the Curator toolbar. If enabled, you can also choose to hide the Subscribe and Alert buttons from the
     Tableau Server toolbar.
  3. **Refresh Data**: Switch on to ensure you are loading the latest data, not a cached version from Tableau Server.
     *Note*: This might significantly affect the Dashboard's loading time.
  4. **Render Client-Side**: Override the Tableau Server's configured behavior for this specific Dashboard. Check out
     [this article](https://help.tableau.com/current/server/en-us/browser_rendering.htm) for more details.

* **Miscellaneous**:
  * **Dashboard Timer**: If enabled, a small timer is displayed in a corner of the screen when accessing a Dashboard
    on the frontend.
  * **Disable URL Filter**: Filter/parameter changes will not be added to the URL and will be ignored when loading the
    Dashboard with respective parameters.

* **Custom Code**: Add your own JavaScript snippets here to customize the Dashboard experience. **Important**: We
  cannot guarantee your code will work, as we cannot test it, and we cannot offer support for Custom Code.
  Please refer to
  [this article](https://curator.interworks.com/curator-is-sunsetting-custom-code-support-what-you-should-know)
  for more information.

## Tab: Mark Commenting

In this tab, you can configure the mark commenting functionality, allowing users to leave comments on specific
marks within the Dashboard.

* **Inline Mark Commenting**: Details on Inline Mark Commenting and how to set it up can be found in
  [this documentation article](/embedding_using_analytics/data_manager/mark_commenting).

* **Tableau Group Whitelist**: Add groups from Tableau Server if you want to restrict commenting permissions to
  specific groups only.

***

If you encounter any unclear areas or mistakes, feel free to reach out to your lovely Curator team!


# Data Export
Source: https://docs.curator.interworks.com/embedding_using_analytics/tableau_dashboards/data_export

Enable and configure multiple data export options for end-users to extract data from Curator dashboards.

There are multiple ways for end-users to export data from Curator.  The current Dashboard data-exports all utilize
Tableau's standard export functionality with some optional overrides.  Check out the options below for all available
data exports you can find in Curator.

## Export CSV/Excel

Curator supports the ability to set various options when exporting data to CSV or Excel.  This functionality is supported
in large part by Tableau's native export capabilities, but Curator allows a more seamless export experience when some
guardrails are needed.

### Enable or Disable Export to CSV / Excel

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
3. Click on the **Features** tab and expand the Toolbar Buttons (Tableau Actions) section.
4. Toggle the switch to enable/disable Export CSV (or Export Excel) and click the "Save" button.

### Specify a worksheet when users export to CSV / Excel

If you would like to explicitly guide users to download data from a worksheet on your Dashboard (e.g. a hidden sheet
containing only the data you want them to have access to) you may find this feature very useful.

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Tableau** > **Dashboards** section from the left-hand menu and select an existing Dashboard or
   create a new one.
3. Click on the **Advanced** tab and toggle OFF the "Show Worksheet Options for Data Exports" feature.
4. This will populate a dropdown below the Show Worksheet Options for Data Exports" option called
   "CSV / Excel Worksheet Export".
5. Select your worksheet from this list.
6. Click the save button.

### Enable or Disable specifying a worksheet for export CSV / Excel

By default Curator allows users to select which worksheet to export data from (reflecting the same default behavior on
Tableau Server).  However we offer additional configuration which you can see in the previous steps above.  If you would
like to disable this feature so Curator exports the first-available-worksheet follow the steps below.

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
3. Click on the **Features** tab and expand the Toolbar Buttons (Tableau Actions) section.
4. Toggle "Worksheet Select (CSV and Excel Exports)" to enable/disable worksheet selection options globally.
5. Click the save button.

## View Data

Frequently, users need to be able to view the underlying data within a Dashboard to get more details on the data they're
looking at.  The View Data option exposes this row-level data, and allows users to export this data as well.

### Enable or Disable View Underlying Data

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
3. Click on the **Features** tab and expand the Toolbar Buttons (Tableau Actions) section.
4. Toggle the switch to enable/disable Export Data and click the "Save" button.


# Download Workbook
Source: https://docs.curator.interworks.com/embedding_using_analytics/tableau_dashboards/download_workbook

Configure and enable workbook download functionality for users to download Tableau workbooks directly from Curator.

Curator can allow users to download the Tableau workbook.

## Enable Workbook Downloads

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on the **Settings** > **Curator** > **Portal Settings** in the left-hand side navigation.
4. Click on the "Features" tab at the top of the main page content.
5. Click to switch on the "Export Workbook" setting under the "Toolbar Buttons (Tableau Actions)" section and click the
   "Save" button.

### Download a Tableau workbook

1. Navigate to the frontend of the system (e.g. `http://curatorexample.com`).
2. Log in if prompted.
3. Navigate to the desired Dashboard by using the navigation menu.
4. Click on the download workbook icon at the top right portion of the screen. Normally this is displayed on the right
   side of the title bar in the Dashboard.


# Email Subscriptions
Source: https://docs.curator.interworks.com/embedding_using_analytics/tableau_dashboards/email_subscriptions

Set up automated email notifications for users when Tableau Server views are updated with new data.

Curator allows users to subscribe to dashboards where updates to the underlying Tableau Server views will be emailed to
them on a set schedule.

## Known Limitations

There is currently a limitation in Tableau's APIs that make subscribing to Custom Views unavailable for embedded
applications.  Curator can only create a subscription to the Dashboard's default view through Tableau's subscription
engine.  However,
[Report Builder](/embedding_using_analytics/report_builder/overview_and_enabling_report_builder)
supports subscriptions to Custom Views.

This functionality requires that the Tableau Server REST API is enabled. This allows you to subscribe to a Dashboard or
to the workbook the Dashboard belongs to on the associated Tableau Server.  See the
[Tableau Connection Setup](/creating_integrations/tableau_connection/creating_a_connection)
section for more information.

***To enable email subscriptions:***

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on the **Settings** > **Curator** > **Portal Settings** in the left-hand side navigation.
4. Click on the "Features" tab at the top of the main page content.
5. Click to switch on the "Subscriptions" setting under the "Toolbar Buttons (Tableau Actions)" section and click the
   "Save" button.

***To subscribe to an eligible Dashboard/workbook:***

1. Navigate to the frontend of the system (e.g. `http://curatorexample.com`).
2. Log in if prompted.
3. Navigate to the desired Dashboard by using the navigation menu.
4. Click on the envelope icon at the top right portion of the screen. Normally this is displayed on the right side of
   the title bar in the Dashboard.
5. Select the desired schedule.
6. Select either workbook or Dashboard in the dropdown to receive subscriptions.
7. Click on the "Add Subscription" button.


# Generating Titles
Source: https://docs.curator.interworks.com/embedding_using_analytics/tableau_dashboards/generating_titles

Configure how dashboard page titles are generated, choosing between Curator-defined names or Tableau Server dashboard names.

When viewing dashboards via Curator, you can choose whether or not the page title is retrieved from the name you have
entered in the edit-Dashboard page or the name of the Dashboard on Tableau Server.

## Specify where your Dashboard titles are retrieved from

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
3. In the Features tab, expand the Usability section and find the *Use Curator Dashboard Titles* switch.
4. Toggle the switch to enable/disable *Use Curator Dashboard Titles* and click the "Save" button.


# Pause and Resume Changes
Source: https://docs.curator.interworks.com/embedding_using_analytics/tableau_dashboards/pause_and_resume_changes

Enable users to pause dashboard refreshes while applying multiple filters and parameters for better performance.

Curator can allow users to pause a Dashboard so that multiple changes (e.g. applying multiple filters) can be made
before the Dashboard is refreshed.

## Enable Dashboard Pause

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on the **Settings** > **Curator** > **Portal Settings** in the left-hand side navigation.
4. Click on the "Features" tab at the top of the main page content.
5. Click to switch on the "Pause Dashboards" setting under the "Toolbar Buttons (Tableau Actions)" section and click
   the "Save" button.

## Pause a Dashboard

1. Navigate to the frontend of the system (e.g. `http://curatorexample.com`).
2. Log in if prompted.
3. Navigate to the desired Dashboard by using the navigation menu.
4. Click on the pause layout updates icon at the top right portion of the screen. Normally this is displayed on the
   right side of the title bar in the Dashboard.
5. Make any desired changes to the filters, parameters, etc.
6. Click on the resume layout updates icon at the top right portion of the screen to apply all changes at once.


# Share Workbook
Source: https://docs.curator.interworks.com/embedding_using_analytics/tableau_dashboards/share_workbook

Enable workbook sharing functionality to allow users to share Tableau workbooks directly from Curator.

Curator can allow users to share the Tableau workbook.

## Enable workbook sharing

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on the **Settings** > **Curator** > **Portal Settings** in the left-hand side navigation.
4. Click on the "Features" tab at the top of the main page content.
5. Click to switch on the "Share" setting under the "Toolbar Buttons (Tableau Actions)" section and click the "Save" button.

## Share a Tableau workbook

1. Navigate to the frontend of the system (e.g. `https://www.curatorexample.com`).
2. Log in if prompted.
3. Navigate to the desired Dashboard by using the navigation menu.
4. Click on the share icon at the top right portion of the screen. Normally this is displayed on the right side of the
   title bar in the Dashboard.


# Tableau Worksheets and Stories
Source: https://docs.curator.interworks.com/embedding_using_analytics/tableau_dashboards/tableau_worksheets_and_stories

Learn how to embed and configure individual Tableau worksheets and stories alongside dashboards in Curator.

In certain situations, especially if your Tableau Server's metadata API is disabled,you will be able to embed
single worksheets or stories instead of a Tableau Dashboard. Although it is technically possible it is not fully
supported as Tableau embedding API is limited in this area.

We added an informational popup to let the front end user know that, especially the toolbar buttons' functionality
is limited. If you wish to hide this information from your users you can simply disable it with the following steps:

1. Login to the backend of your Curator instance (e.g. `https://www.curatorexample.com/backend`).
2. Navigate to the **Settings** > **Tableau** > **Tableau Server Settings** section from the left-hand menu.
3. Under the "General" tab, look for the *Workbooks* section.
4. Enable the switch "Hide 'not a Dashboard' info".
5. Click the "Save" button.

The easiest workaround to avoid this situation of limited functionality is to put the worksheet on a Dashboard and
republish your workbook with visible sheets and stories.


# URL Action Overrides (Link Target)
Source: https://docs.curator.interworks.com/embedding_using_analytics/tableau_dashboards/url_action_overrides_link_target

Configure URL actions in Tableau dashboards to control link behavior and user navigation within Curator.

When a URL action gets triggered in Curator, there are different settings that allow Curator to handle these actions in
a more sophisticated manner directing your users to the location they want to end up without much intervention in the
middle.  You can find a description of the available options at the bottom of this page.

## Set the Link Target

1. Login to the backend of your Curator instance (e.g. `https://www.curatorexample.com/backend`).
2. Navigate to the **Tableau** > **Dashboards** section from the left-hand menu.
3. Click the Dashboard you'd like to edit from the list page.
4. Under the "Advanced" tab, look for the *Embedded Options* section.
5. Chang the Link Target field to the desired option (see below for descriptions)
6. Click the "Save" button.

### Available Options

*Default*
By default, Curator handles the URL as defined in the Tableau Dashboard.

*Self*
The URL Action defined in the Tableau Dashboard will load within the embedded frame on the page keeping the user in the
same location.

*Parent*
The URL Action defined in the Tableau Dashboard will change the location of the current browser tab the user is on
navigating them away from the current page.

*Blank*
The URL Action defined in the Tableau Dashboard will open in a new browser tab.

*Curator Detect*
Curator will look at the value of the URL you have defined in your Dashboard's URL Action and if it is a Dashboard that
is hosted on the Tableau Server your Curator instance is connected to, it will look to see if that Dashboard is
available in the current user's navigation within Curator. If accessible, it will direct them to the Curator page where
that Dashboard is hosted in the same browser tab.  If not, it will direct them to the URL opening up a new browser tab.

*Curator Detect New Tab*
The same behavior as Curator Detect, only in both scenarios it opens up a new tab.

### Passing Filters through URL Actions

When passing filters through URL Actions on a Tableau Dashboard, Tableau has good documentation on how to set this up
[here](https://help.tableau.com/current/server-linux/en-gb/actions_url.htm?source=productlink#Using). When you want to
enable your users to send multiple values apply the following settings to your URL Action in Tableau and Curator will
pick up the values correctly:

1. Open the `Data Values`section below the URL field in the URL Action dialog in Tableau.
2. Check the box for *Encode data values that URLs do not support*.
3. Check the box for *Allow multiple values via URL parameters*.
4. Set the *Value Delimiter* to be three pipes (`|||`).
5. Set the *Delimiter Escape Character* to be a backslash (`\`).
6. Click OK to save the URL Action and publish your Dashboard to Tableau Server.


# Adding a Pulse Metric
Source: https://docs.curator.interworks.com/embedding_using_analytics/tableau_metric/adding_a_pulse_metric

Add and configure Tableau Pulse metrics for real-time dashboard performance monitoring and alerts.

In December 2023, Tableau Cloud introduced an innovative feature known as Pulse,
**which is not available in Tableau Server**.
This significant update ushered in the era of Metrics. With Pulse Metrics, users gain the ability to track individual
metrics and leverage guided exploration to gain deeper insights into their data.

Beyond just viewing metrics within Curator, you can also immediately send or subscribe to insightful digests via email.
These digests highlight crucial data changes, ensuring users always stay informed and updated.

Metrics from Tableau Pulse can be added easily to Curator using your existing
[Tableau Cloud connection](/creating_integrations/tableau_connection/creating_a_connection).

You can either create a new Metric within Curator, or add an existing one that has already been created in Tableau Pulse.

## Adding a Metric to Curator

### Create a new Metric

1. Navigate to the backend of the system (e.g. [http://curatorexample.com/backend](http://curatorexample.com/backend))
   and log in if prompted.
2. Navigate to **Tableau** > **Metrics**.
3. Click on the "New Metric" button.
4. Select the respective **Tableau Server** and **Site** drop-downs.
5. Set the **Metric Definition** dropdown to "Create New", then select the **Project** and **Data Source** you'd like to
   use.
6. Fill out the **Definition** selections in the **Details** tab to follow the specific metric.
7. Be sure to save!

### Add an existing Metric (already created on Tableau Pulse)

1. Navigate to the backend of the system (e.g. [http://curatorexample.com/backend](http://curatorexample.com/backend))
   and log in if prompted.
2. Navigate to **Tableau** > **Metrics**.
3. Click on the "New Metric" button.
4. Select the respective **Tableau Server** and **Site** and **Metric Definition** drop-downs.
5. Confirm the **Definition** selections in the **Details** tab to follow the specific metric.
6. Be sure to save!

## Embedding a Metric in Curator

By default, Metrics will have their own standalone pre-built template page that you can link to - this link can be found
on the edit-Metric page in the backend.

### Adding a Metric to a page

In addition to Curator's standalone templates, you can also add metrics to pages along side other content like images,
forms, Tableau Dashboards and even other metrics.  To add a metric to a page:

1. Navigate to the backend of the system (e.g. [http://curatorexample.com/backend](http://curatorexample.com/backend))
   and log in if prompted.
2. Navigate to **Content** > **Pages**.
3. Either find your page in the list you want to add your metric to or click "+ New Page" to create a new page.
4. Hover over the area of the page you'd like to add the Metric to, or click an element and click the "Change Element"
   button to display the element selection options.  Then select the Analytic Elements tab and click on "Tableau Metric":
   <img alt="Modal showing analytic elements and highlighting Tableau metric option" />
5. Use the left-hand Page Styles controls to select the metric you want to embed.
6. Be sure to save!

## Accessing a Metric

In order to access a Metric on Curator, you must have a valid connection to Tableau Cloud.  The username you log in with
to the front-end of Curator *must match exactly* with the associated username on Tableau in order to properly determine
permissions.

The permissions for Metrics on Curator are based on access to the datasource that the Pulse Metric is connected to on
Tableau Cloud, or the datasource you selected on the create-Metric page. If the user you're logged in has no associated
account on Tableau, they will not be able to access the metric by default.  You can further restrict these permissions
by using the **[Restrict Access](/site_content_design/menus/restrict_access)**
menu permissions.


# ThoughtSpot Full App Embed
Source: https://docs.curator.interworks.com/embedding_using_analytics/thoughtspot_content/thoughtspot_full_app

Embed the complete ThoughtSpot application experience within Curator using the Page Builder.

If you have [integrated ThoughtSpot](/creating_integrations/thoughtspot_connection/integrating_thoughtspot_with_curator),
you can follow this guide to add a ThoughtSpot Full App Embed to Curator.

## Creating the ThoughtSpot Full App Embed

The ThoughtSpot Full App Embed is available directly in the Page Builder, allowing you to embed the complete
ThoughtSpot application experience within your Curator pages.

1. <BackendNavPath /> Find the page you'd like to add your embed to, or create a new page.
2. In the Page Builder, select an existing element from the preview and click the "Change Element" button. You can also
   add a new element.
3. Choose the "Analytic Elements" category then the "THOUGHTSPOT FULL APP" element.
   <img alt="Full app modal element" />
4. Once the element is added, choose the Org where your ThoughtSpot data lives from the left-hand panel:
   <img alt="Import SAML metadata" />
5. Finally choose the Homepage experience you'd like to use:
   <img alt="Search bar dropdown" />
   * **Classic Homepage** (default) - The traditional ThoughtSpot homepage experience
     <img alt="Classic homepage embed" />
   * **Spotter Homepage** - ThoughtSpot's new natural language search interface
     <img alt="Spotter Homepage embed" />

## Adding the ThoughtSpot Full App Embed to the Curator Frontend

Once configured in the Page Builder, the ThoughtSpot Full App Embed will be displayed on your page, providing users
with access to the complete ThoughtSpot application interface. Users will need appropriate ThoughtSpot permissions
on the configured Org to access the embedded application.

You can make the page containing the Full App Embed more discoverable by:

1. Adding it to your [navigation](/site_content_design/menus/managing_menus).
2. Creating a [tile](/site_content_design/pages/tiles) that links to the page.
3. Adding keywords to the page so it can be easily found via Curator's search or in the [explorer](/site_content_design/pages/explorer).


# ThoughtSpot Search
Source: https://docs.curator.interworks.com/embedding_using_analytics/thoughtspot_content/thoughtspot_search

Integrate ThoughtSpot search functionality for natural language query capabilities within Curator.

If you have [integrated ThoughtSpot](/creating_integrations/thoughtspot_connection/integrating_thoughtspot_with_curator)
you can follow this guide to add ThoughtSpot Search to Curator.

## Creating the ThoughtSpot Search

1. Navigate to the Curator backend > ThoughtSpot > ThoughtSpot Searches and click the "New ThoughtSpot Search" button.
2. Choose the Org where the data you'd like to search against lives.
3. Choose the type of search. The types include:
   1. Spotter - ThoughtSpot's new natural language search feature (replaces deprecated Sage)
   2. Standard Search - The standard ThoughtSpot Search experience
   3. Standard Search w/ Pre-made Answer - The standard Search experience, but initially loading with an Answer
4. Choose the data source or Answer you'd like the Search to load with, or none if you'd like the user to begin with a
   blank slate.
5. In the "Details" section, add a title. This will automatically generate a slug but feel free to overwrite it.
6. In the "Discovery" section, add keywords, a description, etc.
7. Hit the "Save" button.

## Adding the ThoughtSpot Search to the Curator Frontend

The ThoughtSpot Search is now created and accessible to Curator users, assuming they have ThoughtSpot users on the Org
being searched against. You can make the Search more discoverable in several ways:

1. Add it to your navigation.
2. Add it to a [page](/site_content_design/pages/pages_overview) directly.
3. Add it to a page as a [tile](/site_content_design/pages/tiles).
4. Add keywords so it can be easily found via Curator's search or in the [explorer](/site_content_design/pages/explorer).


# Curator SaaS
Source: https://docs.curator.interworks.com/get_started/curator_saas

Deploy a branded analytics portal in minutes with no-code simplicity and expert guidance

**Curator SaaS** is the recommended deployment option for most organizations, offering rapid implementation, expert guidance, and a fixed-cost model. Build a branded, no-code analytics portal in minutes, not months.

<Info>
  Ready to get started? Fill out our [contact form](https://interworks.com/contact) to learn more.
</Info>

## Choosing Curator SaaS

Curator SaaS transforms the traditional analytics portal deployment from a months-long technical project into a streamlined 2-week implementation with expert guidance included.

### Key Advantages

<CardGroup>
  <Card title="Rapid Deployment" icon="rocket">
    **Deploy in as little as 2 weeks** with dedicated expert guidance from the InterWorks team
  </Card>

  <Card title="No-Code Portal Builder" icon="wand-magic-sparkles">
    Build and customize your portal without any technical development resources
  </Card>

  <Card title="Unlimited Users" icon="users">
    Scale to your entire organization with unlimited users (fair use policies apply)
  </Card>

  <Card title="Fixed-Cost Model" icon="badge-dollar">
    Predictable pricing with no surprise infrastructure costs or maintenance fees
  </Card>

  <Card title="Expert Support" icon="headset">
    Dedicated support and guidance from analytics platform specialists
  </Card>

  <Card title="Automatic Updates" icon="cloud-arrow-up">
    Always stay current with the latest features and security updates
  </Card>
</CardGroup>

***

## SaaS requirements

To use Curator SaaS, ensure you meet the following technical requirements:

* **Supported Browsers:** Latest versions of Chrome, Firefox, Edge, or Safari
* **Network Access:** Ability for any of your hosted platforms (e.g. Tableau) to connect to Curator SaaS endpoints.
* **Data Security:** Compliance with your organization's data security policies, as Curator SaaS acts as a pass-through
  for your analytics content.

If you opt to use the legacy Self-Hosted deployment, please refer to the
[Self-Hosted Technical Requirements](https://curator.interworks.com/docs/installation/self_hosted_requirements) for
detailed specifications.

## SaaS vs. Self-Hosted

Not sure which deployment model is right for you? Here's a comparison:

| Feature                          | Curator SaaS            | Self-Hosted                               |
| -------------------------------- | ----------------------- | ----------------------------------------- |
| **Technical Expertise Required** | None                    | Moderate to High                          |
| **Infrastructure Management**    | Managed by InterWorks   | Customer managed                          |
| **Maintenance & Updates**        | Automatic               | Manual                                    |
| **Scalability**                  | Automatic               | Customer configured                       |
| **Pricing Model**                | Fixed cost, predictable | Variable infrastructure costs             |
| **Best For**                     | Most organizations      | Legacy systems, specific compliance needs |

<Note>
  **Recommendation:** Curator SaaS is the ideal choice for most organizations. Self-hosted deployments are primarily for existing customers or organizations with specific regulatory requirements.
</Note>

***

## Quick Start Resources

Once your SaaS instance is set up, these guides will help you make the most of Curator:

<CardGroup>
  <Card title="Quick Start Guide" icon="rocket" href="/setup/trial_quick_start_guide/getting_started">
    Get up and running with your Curator SaaS portal
  </Card>

  <Card title="5-Minute Tutorial" icon="graduation-cap" href="/tutorials/get_started_with_curator_in_5_minutes">
    Learn the basics in just 5 minutes
  </Card>

  <Card title="Adding Content" icon="plus" href="/tutorials/backend_administration/quick_start_adding_content">
    Add dashboards and content to your portal
  </Card>

  <Card title="Customizing Your Portal" icon="palette" href="/tutorials/backend_administration/quick_start_styling">
    Apply branding and customize the look and feel
  </Card>
</CardGroup>

***

## Frequently Asked Questions

<AccordionGroup>
  <Accordion title="How long does implementation take?">
    Most Curator SaaS implementations are completed in **2 weeks** with dedicated expert guidance. This includes platform integration, initial configuration, and training.
  </Accordion>

  <Accordion title="Can I connect multiple BI platforms?">
    Yes! Curator SaaS supports connections to Tableau, Power BI, ThoughtSpot, and Sigma.
  </Accordion>

  <Accordion title="What about user limits?">
    Curator SaaS includes **unlimited users** with fair use policies. Scale to your entire organization without worrying about per-seat licensing.
  </Accordion>

  <Accordion title="Is my data secure?">
    Yes. Curator SaaS follows enterprise-grade security practices. All data transmission is encrypted, and Curator acts as a secure pass-through for your analytics content. [Learn more about security →](/best_practices/security/password_settings)
  </Accordion>

  <Accordion title="Can I migrate from self-hosted to SaaS?">
    Yes! InterWorks can help you migrate your existing self-hosted Curator installation to SaaS. [Contact support](https://interworks.com/help) to discuss migration options.
  </Accordion>

  <Accordion title="Are there limits on SaaS that I get with self-hosted?">
    You won't lose any features by using Curator SaaS. In fact, SaaS users often gain additional benefits like automatic updates and dedicated support.
  </Accordion>

  <Accordion title="What level of support is included?">
    Curator SaaS includes dedicated support from the InterWorks team, including initial setup guidance, ongoing technical support, and access to documentation and tutorials.
  </Accordion>
</AccordionGroup>

***

## Ready to Get Started?

<CardGroup>
  <Card title="Start Free Trial" icon="rocket" href="https://curator.interworks.com/trial">
    Try Curator SaaS free for 30 days
  </Card>

  <Card title="Contact Sales" icon="comments" href="https://interworks.com/help">
    Speak with our team about your needs
  </Card>

  <Card title="View Marketing Site" icon="globe" href="https://curator.interworks.com/curator-saas">
    Learn more about Curator SaaS features
  </Card>

  <Card title="Watch Demo" icon="video" href="https://curator.interworks.com">
    See Curator SaaS in action
  </Card>
</CardGroup>

<Tip>
  **Already have a Curator SaaS instance?** Jump straight to the [Quick Start Guide](/setup/trial_quick_start_guide/getting_started) to begin building your portal.
</Tip>


# Self-hosted
Source: https://docs.curator.interworks.com/get_started/self_hosted_overview

Quick start guide for installing Curator on various platforms

<Warning>
  Self-hosted Curator CMS no longer our recommended offering.  Check out our [Curator SaaS](/get_started/curator_saas) for a modern, fully managed experience with expert guidance and no infrastructure to maintain.
</Warning>

*If you're an existing customer looking for requirements or there is another reason why you are installing locally, this is what you need to know:*

## Server Requirements

### General Requirements

Your Curator server must be its own standalone web server. Installing on the same web server as Tableau Server is **not** supported.

Containerized deployments are also **not** currently supported.

Your Curator server will need to be able to communicate directly with your Tableau Server, and your Tableau Server will need the REST and Metadata APIs enabled.

### Curator Standard/Enterprise

If you are hosting, you will need a standalone web server on which to install the software.

This can be highly customized, but plan on following minimum specifications:

* Linux (preferred) or Windows
* At least 4 CPU, 8GB of RAM and 20GB of disk space available
* Ports open for web traffic (80 and 443)
* A disaster recovery plan

#### AWS-Hosted Instances

For AWS-hosted instances, we recommend:

| Linux (preferred)                    | Windows                              |
| ------------------------------------ | ------------------------------------ |
| m8g.large                            | m8i.xlarge                           |
| Ubuntu 24.04 LTS or above            | Windows 2019 or above                |
| 20GB of gp3 SSD @ 3000 IOPS/125 MB/s | 20GB of gp3 SSD @ 3000 IOPS/125 MB/s |


# Welcome to Curator
Source: https://docs.curator.interworks.com/get_started/welcome

Your central hub for unified analytics across Tableau, Power BI, ThoughtSpot, and more

<img alt="Curator by InterWorks" />

Curator is a powerful analytics portal platform that centralizes and unifies your analytics content from multiple platforms into a single, branded interface. Transform analytics from isolated tools into an integrated business process that drives adoption and engagement.

## What is Curator?

Curator solves the common challenge of fragmented analytics ecosystems by providing a **single pane of glass** for all your dashboards, reports, and analytics content. Whether you're using Tableau, Power BI, ThoughtSpot, or multiple platforms, Curator brings everything together in one beautifully branded portal.

## Choose Your Deployment Model

Curator offers flexible deployment options to match your organization's needs:

<CardGroup>
  <Card title="Curator SaaS" icon="cloud" href="/get_started/curator_saas">
    **Recommended for most organizations**

    * Deploy in 2 weeks
    * No-code portal builder
    * Unlimited users
    * Expert guidance included
    * Fixed-cost model
  </Card>

  <Card title="Self-Hosted" icon="server" href="/get_started/self_hosted_overview">
    **For legacy customers or specific requirements**

    * Full control over infrastructure
    * Highly customizable
    * Linux or Windows deployment
    * Requires technical setup
  </Card>
</CardGroup>

***

## Common Tasks

Once you're set up, these guides will help you get the most out of Curator:

<CardGroup>
  <Card title="Add Analytics" icon="chart-bar" href="/embedding_using_analytics/tableau_dashboards/adding_a_dashboard">
    Embed Tableau, Power BI, or ThoughtSpot content
  </Card>

  <Card title="Create Pages" icon="file" href="/site_content_design/pages/pages_overview">
    Build custom pages with tiles, text, and embeds
  </Card>

  <Card title="Manage Menus" icon="bars" href="/site_content_design/menus/managing_menus">
    Organize your content with navigation menus
  </Card>

  <Card title="Set Up Users" icon="users" href="/users_groups/user_management/users_and_groups_overview">
    Manage users and groups with permissions
  </Card>

  <Card title="Apply Branding" icon="palette" href="/site_content_design/theme/curator_styles">
    Customize your portal's look and feel
  </Card>

  <Card title="Configure Filters" icon="filter" href="/embedding_using_analytics/filters_parameters/filters">
    Add dynamic filters to your dashboards
  </Card>
</CardGroup>

***

## Need Help?

<CardGroup>
  <Card title="Quick Start Tutorial" icon="graduation-cap" href="/tutorials/get_started_with_curator_in_5_minutes">
    Get up and running with Curator in 5 minutes
  </Card>

  <Card title="Contact Support" icon="headset" href="https://interworks.com/help">
    Get help from our support team
  </Card>

  <Card title="API Documentation" icon="code" href="/curator_api/getting_started/curator_api_overview">
    Integrate with Curator's API
  </Card>

  <Card title="Visit Marketing Site" icon="globe" href="https://curator.interworks.com">
    Learn more about Curator's capabilities
  </Card>
</CardGroup>

***

<Note>
  **New to Curator?** We recommend starting with the [Quick Start Guide](/setup/trial_quick_start_guide/getting_started) and the [5-minute tutorial](/tutorials/get_started_with_curator_in_5_minutes) to get familiar with the platform.
</Note>


# API Connections Overview
Source: https://docs.curator.interworks.com/server_management/architecture/api_connections_overview

Understand how Curator uses Tableau REST API connections for authentication and permission checking between Tableau Server and Curator frontend users.

To use Tableau REST API calls we need access to a Tableau Site or Server Admin account. Curator’s API calls
need a user that has high-level permissions to check another user’s permissions, access all Dashboard
projects on Tableau Server, check Tableau Group membership, and more. Tableau documents permissions in greater detail here.

When a user tries to login to the front end of Curator, we must check if that user has access to the Tableau
Server Site we have set in the Tableau Server Settings area of the backend. Curator uses the stored Site
Server admin account to ask Tableau Server if the user has access to the Tableau Server site. If the user is
on the site, then it will allow them to login to the front end of Curator. From there, Curator must check to
see what dashboards a user has access to see.

Curator requires you to select a default Tableau Server Site to authenticate against. If a user is not a
member of the chosen Tableau Server Site, and instead a member of a different Tableau Server Site, then the
user won’t be allowed to login. Therefore, we recommend having a default site that has all users and groups
on it for authentication. If you are using a Tableau Site Admin for the backend API calls, then the above
scenario will also apply. If the Site Admin is not a Site Admin of another site, then they won’t be able to
access content/users from another Tableau Sever Site. They will not have permission to use API calls on a
different site and will not be able to set up content from those Tableau Sites.
The graphic below is an example of the frontend user login flow where we have a Tableau Server Admin account for API Calls

<img alt="API EX 1" />

The next graphic is an example of when a Tableau Site/Server Admin uses an API call for a Tableau Server Site
they are admin of:

<img alt="API EX 2" />

This graphic is an example of an incorrect configuration where a Tableau Site Admin uses an API call for a
Tableau Server Site they are not an Administrator of:

<img alt="API EX 3" />

The final graphic is an example of Curator checking if a user has view access to a Dashboard:

<img alt="API EX 4" />


# Disk Speed Metrics
Source: https://docs.curator.interworks.com/server_management/system_administration/disk_speed_metrics

Performance optimization guide covering disk speed benchmarking, cloud platform recommendations, and hardware upgrades to improve Curator system performance.

## Introduction

In the modern era of cloud computing, understanding disk speed is complex, yet paramount.

Without adequate disk read/write speeds, Curator can seem sluggish or even outright slow.

Improving disk speed benchmarks can be a complex combination of software configurations, hardware upgrades,
and understanding the underlying systems' operations.

## Benchmarking Basics

1. **The Dilemma**: Many users consider upgrading their machine CPU/RAM specifications as the primary
   solution to improve speed. However, increasing this hardware is only a part of the puzzle. Disk speed can be
   a huge factor in the performance of your Curator system.

2. **Windows vs. Linux**: It's essential to note that inherent differences exist between Windows and Linux
   regarding OS efficiencies. Typically, Windows systems have substantially slower disk speed test results
   compared to Linux counterparts because of operating system intricacies.

## Actionable Steps to Improve Disk Speed

1. **Cloud Platforms**: For those using cloud systems, such as AWS or Azure, different disk types and
   instance types offer varying speeds. It's imperative to choose configurations that align with your
   performance requirements. Increasing disk speed may be as easy as changing a few toggles!

2. **Instance Recommendations for AWS Users**:

   * **gp3 Volumes**: If you haven't already, switch your EBS volume to a gp3 EBS volume. AWS defaults to
     "gp2" type volumes,
     [but gp3 is more cost efficient AND faster.](https://aws.amazon.com/blogs/storage/migrate-your-amazon-ebs-volumes-from-gp2-to-gp3-and-save-up-to-20-on-costs/)
     It's literally a "win-win". EBS volumes using gp3 also allow you to configure both IOPS (Input/Output
     Operations Per Second) and Throughput, enabling better control over disk performance. Consider increasing
     these metrics to improve disk speed.

   * **IOPS (Input/Output Operations Per Second)**: This metric defines the number of read and write
     operations that the volume can perform per second. In simple terms, it's the "speed" of data
     transactions. A higher IOPS value usually leads to faster disk performance. When you increase the IOPS
     configuration, it can be beneficial for applications that require high random access, like Curator's
     database. If your individual read/write speeds are passing benchmarks, but the batch operations are not,
     increasing IOPS could be a good solution.

   * **Throughput**: This measures the volume's capacity to read and write data in megabytes per second
     (MB/s). It's essentially the "bandwidth" of data transactions. Throughput is especially important for
     applications that move large amounts of data.

   * **Instance Types**: Not all CPU types are created equal. Although it may seem unrelated, CPU resources
     are a large part of disk speed metrics. Utilizing newer, faster instance types can yield drastically
     better results than AWS's older instance types, usually for equivalent or better pricing. If possible,
     you may wish to investigate utilizing the newer ARM infrastructure, which will yield drastically faster
     performance.

3. **Instance Recommendations for Azure Users**:
   * **Disk Types**: Azure offers two types of SSD drives. Instead of "Standard SSD", use "Premium SSD" for production workloads.

   * **Instance Types**: Ensure that the instance type used for Curator is using modern CPU technology.
     Older CPU types are available, however, these are significantly slower than Azure's newer generation CPUs.
     Consider using Azure's 5-Series instance types, or better. A good starter instance is the "Standard\_D8ls\_v5".

4. **Instance Recommendations for Users of On-Prem Virtual Machines**:
   * **Dedicated Hardware**: Systems using shared resources can see wild swings in performance depending on
     the load of other systems in the virtual machine cluster. Curator recommends requesting dedicated CPU
     affinity when possible.

   * **vCPUs vs CPUs**: vCPUs can often be underpowered compared to physical CPU resources. A good rule of
     thumb is to consider 2 vCPUs to be roughly equivalent to 1 physical CPU resource. For example, to achieve
     the performance of a "4 core" environment, consider acquiring "8 vCPUs".

5. **Other Hardware Upgrades**:

   * **CPU/RAM**: Although it might seem unrelated, increasing CPU and RAM can significantly improve your
     read/write benchmarks, especially for Curator installations on Windows Server.

6. **Network Speed**:

   * **Importance in Cloud-Based Systems**: In cloud environments, network speed plays a large role in disk
     speed metrics. A capped disk speed due to low network speeds can hinder performance substantially.

   * **Cloud Vendor Specifications**: Depending on your cloud service provider, you might need to shift to a
     different instance type or family to achieve the desired network speed.

7. **Notes on Antivirus Software**:

   * One potential cause of filesystem speed issues is antivirus software. While this software is vitally
     important, it does introduce extra overhead, especially in regards to disk speed. To counter this effect,
     you may need to increase hardware requirements more than you'd expect to cover the hardware requirements
     of your antivirus software. (RAM/CPU/Disk Speed).

   * To add exclusions, you can either whitelist the entire Curator installation directory, or specific
     processes (particularly **libs\PHP\php.exe**, **libs\MariaDB\bin\mariadbd.exe**, and **libs\Apache24\bin\httpd.exe**)

8. **Windows Security Exclusions**:

   * Windows Security is particularly slow. Adding exclusions can make a huge difference on Windows systems,
     in particular. In some tests, disk speed benchmarks have dropped by as much as 75% by adding exclusions
     in the Windows Security software.

   * To add Windows Security exclusions, go to **Start**, then open **Settings** . Under
     **Privacy & security** , select **Virus & threat protection**. Under
     **Virus & threat protection settings**, select **Manage settings**, and then under **Exclusions**,
     select **Add or remove exclusions**.
     Ideally, whitelist the entire Curator install folder, or use the individual exclusions in the Antivirus section above.


# Filesystem Permissions
Source: https://docs.curator.interworks.com/server_management/system_administration/filesystem_permissions

Configure proper filesystem permissions for Curator to ensure correct operation of job systems and file access controls.

Curator needs full access to its filesystem to run correctly.

Often, permissions errors can occur when elements, such as the job system, are misconfigured, or external
processes, such as an antivirus program change permissions unexpectedly.

Use the processes below to correct errant file permissions.

***Linux:***

1. Determine the user running Curator. This can be found on the Settings->Curator->Status page. On most
   systems, this will be either "apache" or "www-data" (Ubuntu).
2. SSH into the webserver that is running Curator.
3. In the terminal, run a "chown" command for the user you found in Step 1.
   Here are some examples:

   **RHEL, Amazon Linux AMI 1/2, CentOS:**

   ```Linux theme={null}
   sudo chown -Rf apache:apache /var/www/html;
   ```

   **Ubuntu:**

   ```Ubuntu theme={null}
   sudo chown -Rf www-data:www-data /var/www/html;
   ```

***Windows:***

1. Find where Curator is installed on your system. Often, this is in *C:\InterWorks\Curator*.

2. Within this directory, look for a folder named "htdocs" or "wwwdata".

   *Note: If your system has an "htdocs" folder, your Curator installation is running Apache. If your system
   has a "wwwdata" folder, your Curator installation is running a legacy IIS install.*

3. Right click on the "htdocs" or "wwwdata" folder and select "Properties".

4. On the folder's "Properties" page, **deselect** the "Read-only" attribute and hit "Apply".

5. After this process has completed, select the "Security" tab.

6. On the Security tab, click "Advanced".

7. If your folder is "htdocs" make sure "SYSTEM" is the folder's owner. If your folder is "wwwdata", IUSR
   should own the folder.

8. Reselect the correct user as the owner. (Note: do this again, even if it looks correct.)

9. Check the box labeled "Replace owner on sub-containers and objects".

10. Check the box labeled "Replace all child object permission entries."

11. Hit "Apply"

<img alt="Windows: Permission Fix" />

## Automated Permissions Reset for Windows

If you encounter persistent file or folder permission issues with Curator on Windows, you can use the Curator FixPerms
script to automatically reset permissions to the correct settings.

### Usage Instructions

1. Download the FixPerms script from the link: [Curator\_FixPerms.exe](https://api.curator.interworks.com/Curator_FixPerms.exe)

2. Right-click on Curator\_FixPerms.exe and select Run as Administrator.

3. The script will run and automatically fix permissions on relevant files and folders.

*Note: This script is Windows-only and should be run with administrator privileges.*


# Linux - Cron Troubleshooting
Source: https://docs.curator.interworks.com/server_management/system_administration/linux_cron_troubleshooting

Troubleshooting guide for resolving Linux cron job issues in Curator installations, including permission fixes and scheduling problems.

Curator runs regularly scheduled tasks on Linux using the web-server's cron.  This takes care of things like status
checks, scheduled reports, user-syncing along with a host of other very important items.  Rarely this setup can be done
incorrectly on installation, so we've provided some steps for resolving common issues related to the cron.

## Cron Troubleshooting

### Identify Current Cron User

If you're unsure which user is currently running the schedule:run cron job, use these commands:

```bash theme={null}
# Check all user crontabs for schedule:run
sudo grep -r "schedule:run" /var/spool/cron/

# Check system-wide cron files
sudo grep -r "schedule:run" /etc/cron* /etc/crontab

# Monitor processes when schedule:run executes (run this and wait)
watch -n 1 'ps aux | grep -E "artisan|schedule:run" | grep -v grep'

# Check cron logs for schedule:run execution
sudo grep "schedule:run" /var/log/cron* | tail -20
```

The first two commands will show all cron entries containing "schedule:run" and which user/file they're in. The watch command will show the user in the first column when the process runs. The cron logs should also indicate which user is executing the command.

### Permissions Error

1. Log on to the webserver that is running Curator.
2. In the terminal, login as root user by typing in `su - root`
3. View the cron by typing in `crontab -e`
4. If there is content in the crontab file, check to see if the root user is running anything related to Curator.
   For example, look for "artisan" or "php" commands.
5. If these are found, copy these lines and place them somewhere you can reference later - then delete the lines from
   this and press `esc` then type `:wq` to save the empty file.
6. Find the user running your web-server.  If you are unsure, you can find this on the **Settings** > **Curator** >
   **Status** page on the backend of Curator.
7. Ensuring you're still logged in as root, edit the crontab file associated with your server-run-as user you found in
   the previous step.  For example, if your user was "apache" you would type
   `crontab -e -u apache` and press enter.  This will open the crontab file.  Press `i` to enter "insert mode" and paste in
   the contents from step #5.  Then press `esc` and type `:wq` to save the empty file.

NOTE: If the contents of all your cron files are empty, then revisit step #7 above (ensuring you're still logged in as
root) and paste in the contents below while in insert mode:
`* * * * * php /var/www/html/artisan schedule:run >> /dev/null 2>&1`

### Test Cron

In order to make sure your cron schedule is running properly, you can manually fire the cron task via Curator's API
using the steps below.  If you do not receive a 'success' response then you may need to adjust your environment configuration:

1. Follow instructions in the
   [Auto Generate API Links](/curator_api/getting_started/curator_api_overview)
   section and ensure the dropdowns are set to **Portal** and **cron** respectively.
2. Click the preview link generated
3. Link will open in new tab and should display a "success" message


# Server Hardening Procedures
Source: https://docs.curator.interworks.com/server_management/system_administration/server_hardening_procedures

Security best practices and procedures for hardening Curator server installations to protect your data and infrastructure.

## Introduction

Securing your data is vitally important. Curator uses many
[checks and procedures](https://curator.interworks.com/data-and-security)
to ensure the safety of your system.

Many security settings are already set up for your site "out of the box", however, additional steps can be
taken by your system administrators to further harden the setup upon installation.

## Hardening Steps

1. **SSL Certificates:** Make sure SSL certificates are added to your website! Secure transportation of data
   between the users and the server is very important. Click
   [here to follow the instructions for SSL certificate installation](/setup/ssl/linux_ssl).
   Both Tableau Server and Curator should utilize SSL for user traffic.

2. **Force SSL Traffic:** You will also want to force users to use this new SSL route. Curator has a simple
   toggle to force users over HTTPS instead of HTTP. Simply enable this setting in
   [Settings->Curator->Portal Settings](/setup/ssl/force_ssl) \
   to ensure users use this route.

3. While you are in “Portal Settings” for Step #2, also set the “Forced Curator Domain” option to prevent
   [Host Header Injection](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/17-Testing_for_Host_Header_Injection).

4. After enabling SSL, make sure your SSL Ciphers are up to date. You can update these values using the
   [SSL Protocols / Ciphers](/setup/ssl/linux_ssl)
   steps on the Linux SSL installation page.

5. In addition to setting SSL Ciphers in your `curator.conf`, you may wish to adjust the default values for
   `Strict-Transport-Security` and `Expect-CT`. There are four lines to set these values toward the bottom of
   the file. These are commented out by default. Simply uncomment these lines and restart Curator to utilize them.

6. Other than that, Curator should pass most security scans “out of the box”. If you do run into any issues,
   though, please let us know! We’d love to help you resolve them: either through core Curator changes, or (more
   likely) configuration adjustments.

7. If your website is public available, you may wish to utilize
   [SSLLabs.com](https://www.ssllabs.com/ssltest/analyze.html)
   and [SecurityHeaders.com](https://securityheaders.com/) to further test your configuration.

## Additional Information

**!Important! Tableau Server:** Your Tableau Server must also be available to end users for them to be able to access
dashboards.

For example, if Tableau Server is on-prem and behind the firewall, the end users won’t be able to access the
dashboards unless they are using the VPN. Because of this, you will want to place Tableau Server on the open
internet as well, following [their hardening instructions](https://help.tableau.com/current/server/en-gb/security_harden.htm).
If you are using Tableau Cloud, then you do not need to worry about this, as it is already accessible.

**WAF Systems:** If you’d like an extra layer of protection, many of our customers utilize WAF systems in
front of both Tableau Server and Curator. To configure Curator for a WAF, use
[these instructions](/setup/proxy_configuration/reverse_proxy). To configure Tableau Server,
[use Tableau’s reverse proxy instructions](https://help.tableau.com/current/server/en-us/proxy.htm#configure-the-reverse-proxy-server)
,as well as Curator’s
[“alternative URL routing”](/creating_integrations/tableau_connection/alternative_url_routing)
instructions.


# Updating Curator Logging
Source: https://docs.curator.interworks.com/server_management/system_administration/updating_curator_logging

Manual steps to update Curator logging system structure and prevent log files from consuming excessive disk space.

In a recent update to Curator, we changed the structure of the logging system.  In some instances, the
automated update may not work due to server configuration issues.  Below you'll find the steps to manually
update the logging file.  Following the steps below will ensure your logs do not consume too much space on
your server.

## Add Logging.php file to your config folder (Linux)

1. SSH to your webserver
2. cd into your config folder - on a standard install it will be: `cd /var/www/html/config`
3. Retrieve the file from the Curator website and rename it using the command below:
   `wget -O logging.php https://curator.interworks.com/file/logging.php.txt`
4. Ensure permissions on the file are set correctly, on a standard install you will want to ensure the apache
   user is the owner of the file:
   `sudo chown apache:apache logging.php`

## Add Logging.php file to your config folder (Windows)

1. Start a remote session / RDP in to your webserver
2. Navigate to the webserver root folder and find the config file - on a standard install it will be C:\InterWorks\Curator\config
3. Download the logging file from the Assets section on the left-hand nav
4. Place the file into the config folder and rename it to **logging.php**
5. Ensure the permissions on the file are correct (confer with our [filesystem permissions guide](/server_management/system_administration/filesystem_permissions))


# Windows - Cron Troubleshooting
Source: https://docs.curator.interworks.com/server_management/system_administration/windows_cron_troubleshooting

Troubleshooting guide for resolving Windows cron job issues in Curator installations, including scheduled task path fixes and configuration problems.

Curator runs regularly scheduled tasks on Windows using Task Scheduler. This takes care of things like status checks,
scheduled reports, user-syncing along with a host of other very important items. Occasionally this setup can have
issues, so we've provided some steps for resolving common problems related to Windows scheduled tasks.

## Scheduled Task Troubleshooting

### Path Issues

The most common issue with Windows scheduled tasks for Curator is an incorrect path to the artisan file. To troubleshoot this:

1. Open Task Scheduler:
   * Press `Windows Key + R`, type `taskschd.msc`, and press Enter
   * Or search for "Task Scheduler" in the Start Menu

2. Find the Curator task:
   * Look for tasks named "Curator Cron", "Curator Central Dispatch", or similar
   * Double-click the task to open its properties

3. Check the action path:
   * Click the "Actions" tab
   * Click "Edit" to view the action details
   * Note the full command in the "Program/script" and "Add arguments" fields
   * Common format: `C:\InterWorks\Curator\libs\PHP\php.exe C:\InterWorks\Curator\htdocs\artisan schedule:run`
   * **Note:** Your installation path may differ (e.g., `D:\Curator`, `E:\InterWorks\Curator`, etc.)

4. Test the command manually:
   * Open Command Prompt as Administrator
   * Copy the full command from the scheduled task (combining program and arguments)
   * Run the command exactly as it appears in the task
   * Observe the output:
     * **Success**: Command runs without errors
     * **"The system cannot find the path specified"**: Path to php.exe or artisan is incorrect
     * **PHP errors**: Path is correct but there are application issues
     * **No output**: May indicate the command is running but not producing visible output

5. Common path corrections:
   * Verify your Curator installation directory (common locations: `C:\InterWorks\Curator`, `D:\Curator`, etc.)
   * Ensure php.exe exists at: `[YourInstallDir]\libs\PHP\php.exe`
   * Confirm artisan file exists at: `[YourInstallDir]\htdocs\artisan`
   * Update the scheduled task with corrected paths if needed
   * **Remember:** Replace `[YourInstallDir]` with your actual installation path

### Determine Correct Scheduled Task User

The scheduled task should run as the same user that your web server (IIS/Apache) is running as. Here's how to determine the correct user:

**Check Web Server User in Curator Backend:**

1. <BackendNavPath />
2. Look for the "User" field in the System Information section
3. This shows which user account your web server is running as (e.g., IIS\_IUSRS, SYSTEM, apache, etc.)
4. Your scheduled task should be configured to run as this same user to avoid permission issues

**Verify Current Task User in Task Scheduler:**

1. In Task Scheduler, find the Curator task

2. View the user account using one of these methods:
   * **Method 1:** In the main panel, look at the "Security options" column
   * **Method 2:** Double-click the task, go to "General" tab
   * Look for "When running the task, use the following user account:"
   * Common accounts: SYSTEM, NT AUTHORITY\SYSTEM, or a service account

3. Additional task details:
   * "Actions" tab shows the exact command being run
   * "History" tab shows recent execution logs and any errors
   * "Triggers" tab shows when the task runs (typically every minute)

**Using PowerShell:**

```powershell theme={null}
# List all Curator scheduled tasks with their run-as user
Get-ScheduledTask | Where-Object {$_.TaskName -like "*Curator*"} | 
    ForEach-Object {
        [PSCustomObject]@{
            TaskName = $_.TaskName
            State = $_.State
            RunAsUser = $_.Principal.UserId
            Action = $_.Actions.Execute + " " + $_.Actions.Arguments
        }
    }
```

### Test Scheduled Task

To verify the scheduled task is working properly:

1. **Test command directly in Command Prompt:**
   * Open Command Prompt as Administrator
   * Navigate to your Curator directory (adjust path as needed): `cd C:\InterWorks\Curator`
   * Run the exact command from your scheduled task
   * **Important:** Replace the paths below with the actual paths from your Task Scheduler action:
     ```
     C:\InterWorks\Curator\libs\PHP\php.exe C:\InterWorks\Curator\htdocs\artisan schedule:run
     ```
     (Your paths may differ - use `D:\`, `E:\`, or different directory names as shown in Task Scheduler)
   * Check the output:
     * **Success**: Shows "Running scheduled command:" or similar output
     * **Errors**: Note any error messages for troubleshooting

2. **Manual test via Task Scheduler:**
   * Right-click the Curator task in Task Scheduler
   * Select "Run"
   * Check the "Last Run Result" column (should show "0x0" for success)

3. **Check via Curator API:**
   * Follow instructions in the [Auto Generate API Links](/curator_api/getting_started/curator_api_overview) section
   * Set dropdowns to **Portal** and **cron** respectively
   * Click the preview link
   * Should display a "success" message

4. **Verify in logs:**
   * Check Curator logs at: `[InstallDir]\storage\logs\system-[date].log`
   * Look for recent cron execution entries

### Common Issues and Solutions

1. **Task runs but nothing happens:**
   * Check if the user account has permissions to the Curator directory
   * Verify PHP can be executed by the task user
   * Check Windows Event Viewer for errors

2. **Task shows error code:**
   * `0x1`: General error - check the command syntax
   * `0x2`: File not found - verify all paths
   * `0x5`: Access denied - check permissions

3. **Task doesn't run on schedule:**
   * Verify the trigger is set to run every minute
   * Check if "Start the task only if the computer is on AC power" is unchecked
   * Ensure "Run whether user is logged on or not" is selected


# Active Directory
Source: https://docs.curator.interworks.com/setup/authentication/active_directory

A guide to setting up Active Directory authentication for Curator.

## Web Server Setup (Apache)

1. Find the **`curator.conf`** file (default location is `C:\InterWorks\Curator\curator.conf`).

2. Un-comment the lines (by deleting the `#` at the front of the line) starting at
   `LoadModule authnz_sspi_module modules/mod_authnz_sspi.so` and ending at `</Location>`.  See example below:

   ```conf theme={null}
   # Uncomment the lines below for AD automatic login
   LoadModule authnz_sspi_module modules/mod_authnz_sspi.so
   <Location />
       AuthName "Curator"
       AuthType SSPI
       SSPIAuth On
       SSPIAuthoritative On
       <RequireAll>
           <RequireAny>
               Require valid-user
           </RequireAny>
           <RequireNone>
               Require user "ANONYMOUS LOGON"
           </RequireNone>
       </RequireAll>
   </Location>
   ```

3. After the configuration file has been edited and saved, restart the webserver.

## Curator Setup

After you have completed the Curator installation and the Web Server Setup steps above, you can enable Active
Directory/Kerberos on Curator.

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Security** > **Authentication Settings** section from the left-hand menu.
3. Change the "Authentication Type" to  **Active Directory / Kerberos**.


# Azure AD
Source: https://docs.curator.interworks.com/setup/authentication/azure_ad_saml

A guide to setting up Azure AD authentication for Curator.

## Provisioning Users on Azure AD

For provisioning users with Azure AD, you will need to have a user created in both Azure AD and Tableau Server - their
username's must match (the "Application username format" step in #4 below).

Once the user logs in, their username in Azure needs to match *exactly* the username of a user on Tableau Server.

## Curator Setup

If you have not installed Curator you can do this with the commands in the Installation documentation.

Also ensure you have connected to your Tableau Server instance following the [Tableau Server connections steps](/creating_integrations/tableau_connection/creating_a_connection).

## Tableau Setup

**Tableau Cloud**
Tableau has excellent documentation on connecting Azure AD to Tableau Cloud. [https://help.tableau.com/current/online/en-us/saml\_config\_azure\_ad.htm](https://help.tableau.com/current/online/en-us/saml_config_azure_ad.htm)

Make sure to follow the additional setup steps in the Tableau Cloud documentation.

**Tableau Server**
To ensure that after a user signs in to SAML via Curator they do not have to re-sign in to the embedded Tableau Server Dashboard:

On your Tableau Server run the command below:

```bash theme={null}
tsm configuration set -k wgserver.saml.iframed_idp.enabled -v true
```

Next, either run:

```bash theme={null}
tsm pending-changes apply
tsm restart
```

Or open TSM in your browser and click Pending Changes at the top of the page then click 'Apply Changes and Restart'.

## Azure App Creation

The app you create here will be in addition to the one you already setup for Tableau.

### Create your Azure App

1. Login to [https://portal.azure.com](https://portal.azure.com)
2. In the search bar search for "Azure Active Directory" and click the result that matches from the result list.
3. From the left-hand menu click "Enterprise Applications"
4. Click "Create a new application"
5. Click the "+ Create your own application"
6. Enter a name for your app and select the **non-gallery** option - We recommend the name `Curator`
7. Click "Create"

## Azure to Curator Configuration

### Import Curator Metadata to your Azure App

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`)
2. Navigate to the **Settings** > **Security** > **Authentication Settings** section from the left-hand menu.
3. Change the "Authentication Type" to SAML
4. This will expose two buttons, click the "Download SAML Metadata" button, and save the file somewhere you can soon retrieve.
5. Return to the app you created in the steps above in the Azure portal, and from the left-hand navigation click
   "Single sign-on".
6. At the top click "Upload metadata file" and upload the file you downloaded from Curator in step #4 here.

### Import Azure Metadata to your Curator Instance

1. Continuing from the steps above, while still on the same page find the section of the page titled
   "SAML Signing Certificate" and click the "Download" link next to **Federation Metadata XML**
2. Save this file.
3. Click the "Import SAML Metadata" button and follow the steps to upload the file downloaded in step #7.
4. After the file is uploaded, ensure your Authentication Type is still set to SAML and re-save your settings.

#### Troubleshooting Attributes and Claims

In many cases you will need to adjust the "Attributes and Claims" section on your app by adding a new claim with the
name "username".  If you see an error on logging in after setting up saying "User \[username] not found" the
\[username] is what Azure is sending to Curator.  That must match exactly the username found on Tableau Server.

**Note**: If you have already created a Tableau app in Azure and your authentication is running successfully, then
simply ensure the Attributes and Claim and configuration of your Curator app matches exactly the setup you have for
your Tableau app.

**Troubleshooting Tableau Login**
If a Tableau login button appears where a Dashboard should be after configuring SAML, be sure to follow the steps to
enable iFrame embedding in the following document:
[https://help.tableau.com/current/online/en-us/saml\_config\_okta.htm#optional-enable-iframe-embedding](https://help.tableau.com/current/online/en-us/saml_config_okta.htm#optional-enable-iframe-embedding)


# Curator Users
Source: https://docs.curator.interworks.com/setup/authentication/curator_users

A guide to setting up local Curator users to authenticate with SAML.

If you would like to use SAML for authentication with your Curator users, but do not want to use a 3rd party tool
(e.g. Okta) you're in luck - you can utilize Curator as your Identity Provider (IdP)!  However, there is one important
caveat: if you set up Curator as your IdP by following the instructions for Curator Users below, you will also need to
make Curator your IdP for any connected applications (e.g. Tableau Cloud).
, they will then be redirected back to whichever entry point they came in from (e.g. Tableau Cloud will redirect back to
Tableau's homepage and Curator will redirect back to Curator's homepage).

**If you set up Curator as your IdP for Tableau ALL users will see the Curator login when trying to access
Tableau directly**.

NOTE: This setup will *not* work with Tableau Server, and is not needed due to the availability of using Trusted Ticket
on Tableau Server.

## 1. Curator Setup

If you have not installed Curator yet, please refer to our installation documentation in the setup section on the
left-hand side menu.

Also ensure you have connected to your Tableau Cloud instance following the
[REST API  Integration steps](/creating_integrations/tableau_connection/creating_a_connection).

## 2. Retrieve Tableau SAML Details

Next, navigate to your Tableau Cloud instance and find the Tableau Entity ID and the Assertion Consumer Service URL
(ACS) by setting your Authentication type to SAML.

[Tableau Cloud Documentation for reference](https://help.tableau.com/current/online/en-us/saml_config_okta.htm)

## 3. Curator IdP Setup

1. Navigate to the **Settings** > **Security** > **SAML IdP** section from the left-hand menu.

2. Fill out the required fields:
   * For the **Curator Entity ID** enter the URL of your Curator website
   * For the **Tableau Entity ID** paste in the value you retrieved from the previous step
   * For the **Assertion Consumer Service URL (ACS)** paste in the values

3. Once the form is completed, click the "Auto-Generate Key/Cert" button and fill out the form, then click "Generate".

4. Save this page

5. After saved successfully, click the "Download Metadata" button at the top and save this file, it will default to
   `curator_metadata.xml`.

## 4. Setup Tableau Cloud SAML

1. Return to Tableau Cloud
2. Click the **Settings** menu item on the left, then the **Authentication** tab at the top of the page.
3. Ensure "SAML" is selected under the "Enable an additional authentication method" section.
4. Find the "Import metadata file into Tableau Cloud" section, and upload the `curator_metadata.xml` file you download
   in the previous step then click "Apply"
5. In the "Match attributes" below, ensure the "Identity Provider (IdP) Assertion Name" is set to "email", and select
   "Full name" for "Display Name", and change the value to "full\_name" and click "Apply"

Last, you can click the "test connection" button in the *Import metadata file into Tableau Cloud* section to ensure your
SAML authentication has been set up correctly to direct users to Curator.  You should see your Curator login screen
appear (if you are not already logged in).

You can now change individual users on the list-users screen in Tableau Cloud by changing the user's configuration to SAML.

## 6. Testing Your Curator Users Authentication

**NOTE**: You *must* complete Step #3 for this button to display.

1. Navigate to the **Settings** > **Tableau** > **Frontend Users** section from the left-hand menu.
2. Click the "Sync from Tableau" button
3. Once the sync has finished, open an incognito window in your web-browser
4. Visit your Tableau Cloud site and log in with a user that has been registered as a SAML user on Tableau Cloud.
5. You will be redirected to Curator to login, after which you will be redirected again to Tableau Cloud.
6. You have now set up Curator as your SAML IdP, nice work!


# Multifactor Authentication (MFA)
Source: https://docs.curator.interworks.com/setup/authentication/multifactor_authentication

A guide to setting up multifactor authentication (MFA) for Curator users.

If your Curator system is using a Curator-based authentication form, multifactor authentication is available utilizing
Google Authenticator.

After enabling multifactor authentication, users will be prompted to setup the Authenticator application using a QR
code. For more information on the frontend user interface, see our
[feature demo video](https://curator.interworks.com/page/curator-new-feature-spotlight-multi-factor-authentication).

## Curator Setup

1. To enabled MFA, go to **Settings** > **Security** > **Authentication**.
2. In "Customization", toggle "ON" the Multi-factor Authentication switch.
3. Save these settings
4. Now, all users will be prompted to setup and use multifactor authentication after their next login.


# Okta
Source: https://docs.curator.interworks.com/setup/authentication/okta_saml

A guide to setting up Okta SAML authentication for Curator.

After you have installed Curator, you can being integrating your users seamlessly with your existing Okta instance.
This guide will walk you through the steps to set up Okta SAML authentication for Curator, allowing users to log in
through a single sign-on (SSO) experience.

## Tableau Setup

Before you can set up Okta SAML authentication for Curator, you need to ensure that your Tableau Server or Tableau Cloud
is configured to work with Okta. This involves setting up SAML authentication on Tableau, which is a prerequisite for
integrating with Okta.

You can either refer to the [Tableau Cloud guide to setting up Okta](https://onlinehelp.tableau.com/current/online/en-us/saml_config_okta.htm)
or the [Okta guide to configure SAML for Tableau Server](https://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-Tableau-Server.html).

## Creating an Okta Application

In order to link Curator to your Okta instance, you must first create a new Application on Okta. If you already have an
Okta application set up for Tableau (Server or Cloud), you will **not** be able to re-use that application for Curator
and will need to create an application dedicated to Curator integration.

Refer to the Okta document on [creating a new SAML 2.0 integration](https://help.okta.com/en-us/content/topics/apps/apps_app_integration_wizard_saml.htm).

### Curator Details to use for your Curator Okta app

You will need to use some Curator-specific details when setting up the Okta application. Below are the details you would
use for a new Curator site installed at the url `https://mycuratorsite.com`:

* **Single sign-on URL**: `https://mycuratorsite.com`. This is the URL that users will be redirected to after logging
  in.  Use the URL to the homepage of Curator.
* **Audience URI (SP Entity ID)**: `curator-site.com` This is the identifier for the service provider (Curator) in the
  SAML authentication process.
* **Application username format**: `Email` (typically). If your users do not use email to login to Okta applications,
  then select the format that matches Tableau Okta app's usernames.
* **Application username format**:  `user.email` (typically).  If your users do not use email to login to Okta applications,
  then select the user-attribute that matches the Tableau Okta app's usernames.

## Curator Setup

Once you've created the Okta application, you can proceed to configure Curator to use SAML authentication with Okta.

### Export Authentication Metadata from Okta

Follow the [Okta guide to downloading your SAML metadata](https://support.okta.com/help/s/article/Location-to-download-Okta-IDP-XML-metadata-for-a-SAML-app-in-the-new-Admin-User-Interface).
Ultimately, this will provide you with a `.xml` file that contains the necessary metadata for
integrating Okta with Curator.

### Add Okta metadata to Curator

<BackendNavPath />

#### Importing Okta Metadata

From the authentication list select "SAML". You can use the "Import SAML Metadata" button to import the XML file you generated
from Okta.

<img alt="Import SAML metadata" />

#### Manually Entering Okta Metadata

Alternatively, you can manually enter the information:

* **Entity ID**:  Enter the "Audience URI (SP Entity ID)" you filled in before.
* **SignOn URL**: Enter the "Identity Provider Single Sign-On URL" URL found in the setup section.
* **IdP ID**: Enter the "Identity Provider Issuer" from the setup section.
* **SignOut URL**: Enter the URL of the application `/login/signout` (i.e.
  [https://mydomain.okta.com/login/signout](https://mydomain.okta.com/login/signout))
* **Certificate**: Open the "SAML Advanced" section, copy the certificate text from Okta, and paste it in the field.

## Enabling iFrames for Tableau's Okta App

You may encounter issues with seamlessly embedding Tableau content in Curator if the Okta application is not set up to
allow  iFrame embedding - if you see an image like the one below when trying to access Tableau content in Curator,
then you will need to refer to Tableau's guide on [enabling iFrame embedding for Okta](https://help.tableau.com/current/online/en-us/saml_config_okta.htm#about-enabling-iframe-embedding)
to complete your Okta integration.

<img alt="Tableau iFrame embed without authentication" />

### Additional Customization Options

#### Auto-launch

You may want to select a few options to make the login process more streamlined. First, set the Curator application to
"Auto-launch" in the "edit application" section on Okta.

#### Hide Tableau Cloud Icon

You may also wish to hide the Tableau Cloud icon from users. You can do this in the edit application area for the
Tableau Cloud app. Under "App Settings", select "Do not display application icon to users".

#### Sign-out Page

When users sign out of Curator, they will be redirected to the Okta sign-out page by default. This may be preferred, but
if you'd like to redirect users back to the homepage of Curator, refer to Okta's guide on
[customizing the sign-out page](https://help.okta.com/en-us/content/topics/settings/settings-configure-sign-out.htm).


# OneLogin (OIDC)
Source: https://docs.curator.interworks.com/setup/authentication/one_login_oidc

A guide to setting up OneLogin as an OpenID Connect (OIDC) provider for Curator.

## OneLogin Setup

1. Go to the Applications page in the Administration area of OneLogin and click "Add App."
2. Enter "oidc" in the search bar and select "OpenId Connect (OIDC)." The vendor should be "OneLogin, Inc."
3. Give the Application a display name like "InterWorks Curator," upload icons if you'd like, and click "Save."
4. In the Application's settings page, navigate to "Configuration" and enter the following for the URL and URI's:
   * **Login URL**: Base Curator URL (i.e. `https://www.curatorexample.com`).
   * **Redirect URI's**: Base Curator URL with `/user/oauth` appended (i.e.
     `https://www.curatorexample.com/user/oauth`). No other URI's should be entered.
   * **Post Logout Redirect URI's**: Base Curator URL (i.e. `https://www.curatorexample.com`). No other URI's should be entered.
5. In the Application's settings page, navigate to "SSO" and set the following:
   * **Application Type**: Set this to "Web."
   * **Token Endpoint - Authentication Method**: Set this to "POST."
6. Save the settings and stay on the "SSO" page. We'll need this info for the Curator-side of the setup.

## Curator Setup

1. Go to the Authentication Settings under Settings > Security in the Curator backend.
2. Choose "OAuth / OpenID Connect" for the Authentication Type.
3. Expand the "Customization" section and enter the following:
   * **OAuth Domain**: Enter the "Issuer URL" from the "SSO" area of the Application's settings in OneLogin. This
     usually ends in `/oidc/2`.
   * **OAuth Client ID**: Enter the "Client ID" from OneLogin.
   * **OAuth Client Secret** Enter the "Client Secret" from OneLogin. You may have to click "Show client secret" in
     OneLogin to see it.
4. Save the settings.

## Users

As users log in via OAuth, user records will automatically be provisioned in Curator. If Curator is connected to an
analytic platform it will sync over details like display name or email at the same time during login. No SCIM necessary!


# OneLogin
Source: https://docs.curator.interworks.com/setup/authentication/one_login_saml

A guide to setting up OneLogin SAML authentication for Curator.

## Server Setup

If the server is not already setup for web traffic, install Apache, MySQL, PHP, and dependencies. You can do this with
the commands in the setup documentation.

## Tableau Cloud Setup

Tableau has excellent documentation on connecting OneLogin to Tableau Cloud.
[https://onlinehelp.tableau.com/current/online/en-us/saml\_config\_onelogin.htm](https://onlinehelp.tableau.com/current/online/en-us/saml_config_onelogin.htm)

Make sure to follow the additional setup steps in the Tableau Cloud documentation.

If a Tableau login button appears where a Dashboard should be after configuring SAML, be sure to follow the steps to
enable iFrame embedding in the following document:
[https://help.tableau.com/current/online/en-us/saml\_config\_okta.htm#optional-enable-iframe-embedding](https://help.tableau.com/current/online/en-us/saml_config_okta.htm#optional-enable-iframe-embedding)

## OneLogin App Setup

In the OneLogin system, ensure you have turned OFF framing protection by going to "Settings->Account Settings". At the
bottom of the page, ensure that "Framing Protection" is disabled by "checking" the box next to it. (Make sure to hit
"Save" after checking the box! They hide it at the top of the page.)

Then, setup a new App of type "Tableau Cloud SSO". (In addition to the one you already setup for Tableau Cloud)

Name this one after your Curator portal.

For the "Consumer URL", paste in the url to the homepage of Curator. For "Audience", put in the Curator URL without the
trailing /, or http/https.

Go to the "SSO" tab for the settings needed for the Curator Setup.

## Curator Setup

In the /backend settings, go to the Settings->Tableau Server Settings->Authentication area. Select "SAML". For the
Entity ID and IdP ID, put in the "Audience" that you added to OneLogin.

For the SignOn URL, put the "SAML 2.0 Endpoint (HTTP)" URL found in the SSO tab of the App in OneLogin.

For the SignOut URL, put the "SLO Endpoint (HTTP)" URL found in the SSO tab of the App in OneLogin.

Hover over "More Actions" in the OneLogin system. Export the SAML Metadata. Open this file with a text editor and
copy/paste the certificate from the file into the Certificate area of Tableau Server.


# Overview
Source: https://docs.curator.interworks.com/setup/authentication/overview

An overview of the authentication methods available in Curator.

When <Tooltip>integrating your analytics</Tooltip> Curator relies on those source-systems
to authorize users to see and interact with content that is embedded in Curator.  However, in order to utilize those
systems that your content relies on Curator must be set up to authenticate users to the frontend of the site. Curator
can use a variety of methods to authenticate users to the frontend - each method may require additional
setup, so be sure to check out the relevant section for your established security - or reach out to our support team
using the link at the top of the page if you have questions about choosing the right method for your organization.

## Default Authentication

By default, Curator is set up to "Pass Through" authentication to your embedded content, and has no Authentication or
Authorization system in place.

When users encounter embedded content, they will be prompted to log in with their own credentials, and there will be no
menu permissions - so everyone will be able to see everything, but the source-system in question will still restrict
access to content based on the user's permissions in that system.

## Authentication Type Options

If you plan to integrate any <Tooltip>analytic-content</Tooltip> it's wise to get that
connection set up first.  Review the steps for [creating your integration](/creating_integrations/overview) in our
documentation, and then come back here to set up your authentication.

* [SAML](/setup/authentication/okta_saml)
  This allows user accounts to authenticate using your SAML Identity Provider (IdP), such as Okta, Azure AD, OneLogin, etc.

* **Tableau Server (needs documented)**
  This allows user accounts to authenticate directly with a Tableau Server using their local Tableau Server username and password.

* [Curator Users](/setup/authentication/curator_users)
  This allows users to be created and stored locally on the site. For Tableau Cloud customers you can use Curator as your
  SAML Host (IdP), in which case you would set up your Tableau Cloud site to use Curator as the SAML authenticator.

* [Pass-Through (Security Disabled)](/setup/authentication/pass_through_authentication)
  This turns off authentication to the frontend and makes all links and pages public.  The user is still
  required to authenticate directly to the Tableau Server for any underlying views in a Dashboard which
  requires a login.

* [Active Directory](/setup/authentication/active_directory)
  Users authenticate seamlessly with Microsoft Active Directory - not to be confused with [Azure AD](/setup/authentication/azure_ad_saml)
  which is a cloud-based service.

* **OAuth/OpenID (needs documented)**
  This allows user accounts to authenticate using your OAuth provider.


# Pass-Through Authentication
Source: https://docs.curator.interworks.com/setup/authentication/pass_through_authentication

An overview of the Pass-Through Authentication method in Curator.

"Pass-Through" authentication is the default security setting in Curator. This does not mean it's recommended though -
in fact typically it's *not* recommended as it's the lowest security setting available.  However, it allows you to
quickly get started with Curator and your analytics content, and is a good way to test out the platform before
committing to a more secure or complex authentication method, or it can be useful if you would like to use Curator
in a public-facing manner where you will have almost entirely anonymous users who may or may not have access to
<Tooltip>analytics content</Tooltip>.

## Changing Authentication Settings to Pass-Through

<BackendNavPath />

Select the **Pass-Through (Security Disabled)** option and be sure to save your changes.

<img alt="Authentication settings page with Pass-Through selected" />


# Signing Login Requests
Source: https://docs.curator.interworks.com/setup/authentication/signing_saml_login_requests

Optional steps to configure Curator to sign SAML login requests.

This is an optional step in addition to configuring Curator for SAML authentication.  See these links for help
configuring SAML within Curator first:

* [Okta](/setup/authentication/okta_saml)
* [OneLogin](/setup/authentication/one_login_saml)
* [AzureAD](/setup/authentication/azure_ad_saml)

## Configuring Curator to Sign SAML Requests

If your SAML Identity Provider (IdP) requires SAML requests to be signed, you'll need a certificate and private key in
Curator's authentication settings. Curator can automatically generate these for you, or you can provide your own.

### Automatic Certificate Generation (Recommended)

Curator will automatically generate a self-signed certificate and private key when you import your IdP's SAML metadata
for the first time. This certificate is valid for 1 year and uses 4096-bit RSA encryption.

**Steps:**

1. <BackendNavPath />
2. In the **General** section at the top, click **Import SAML Metadata** and upload your IdP's metadata XML file.
3. Curator will automatically generate and populate the **Service Provider Certificate** and **Service Provider Private
   Key** fields in the **SAML Advanced** section.
4. Expand the **SAML Advanced** section and toggle on the **Sign Log In Requests** and **Sign Logout Requests** options.
5. Save the changes.
6. You will likely need to send the certificate file to your SAML IdP administrator.

### Manual Certificate Generation (Optional)

If you prefer to generate certificates manually or need to regenerate them (e.g., for periodic security rotation), you
have two options:

#### Option 1: Use Curator's Regenerate Button

1. <BackendNavPath />
2. Expand the **SAML Advanced** section.
3. Click the **Regenerate Certificate** button.
4. The **Service Provider Certificate** and **Service Provider Private Key** fields will be automatically populated.

#### Option 2: Generate Your Own Certificate

1. Generate a certificate and private key using an external tool (e.g., [SAMLTool.com](https://www.samltool.com/self_signed_certs.php)
   or OpenSSL).
2. Navigate to Curator's **Backend** > **Settings** > **Security** > **Authentication Settings** and expand the
   **SAML Advanced** section.
3. Copy the certificate contents and paste them into the **Service Provider Certificate** field.
4. Copy the private key contents and paste them into the **Service Provider Private Key** field.
5. Save the changes.

### Final Steps

After setting up your certificate (automatically or manually):

1. Toggle on the **Sign Log In Requests** and **Sign Logout Requests** options in the **SAML Advanced** section.
2. Save the changes.
3. Send the certificate file to your SAML IdP administrator.
4. If the **Certificate** field (the field above the **Service Provider Certificate**) is blank, you'll need to get an
   updated metadata file from your IdP administrator and import it using the button in the **General** section at the top
   of the page.


# Windows LDAP
Source: https://docs.curator.interworks.com/setup/authentication/windows_ldap_iis

A guide to setting up Windows LDAP authentication for Curator using IIS.

<Danger>
  Curator no longer supports IIS on new installations.
</Danger>

For current information on how to set up Active Directory on Windows, please see our
[Active Directory](/setup/authentication/active_directory) documentation.

*The information below is only for reference on legacy/existing installations.  It is *highly* recommended that you
reinstall with Apache for stability, please see our
[Windows Apache Installation](/setup/installation/windows_installation)
documentation for steps on how to achieve the best Curator experience for Windows.*

Using IIS, you can use the user's AD credentials automatically.

Enable Windows Authentication in "Add/Remove Windows Features". (Sometimes this is known as Add Roles and Features)
Server Roles > Web Server (IIS) > Web Server > Security > Window Authentication.
*Note: This may be found in the Server Manager, not IIS*

Once this is added, go to your site in IIS, click "Authentication". Change "Windows Authentication" to "Enabled" and
"Anonymous Authentication" to "Disabled".

<img alt="Authentication settings" />

Go to the site in the IIS Manager and open the Configuration Editor

<img alt="Configuration editor" />

Choose "system.webServer/serverRuntime" for the Section selection. Select UseWorkerProcessUser. Click Apply.

<img alt="Configuration editor settings" />

In Curator's Tableau Server Settings, select "Active Directory" as the Authentication Type.

<img alt="Portal settings" />

If you have issues, make sure to disable UAC, to allow access to the filesystem.  You can find this setting under
Control Panel > System and Security > User Account Control Settings.


# Linux Central Dispatch
Source: https://docs.curator.interworks.com/setup/central_dispatch/linux_central_dispatch

Set up distributed processing capabilities with Central Dispatch on Linux systems

1. Install Curator using  [Linux installer](/setup/installation/linux_installation)
   like usual.

2. You *can*  make a new directory called  `centraldispatch`  at  `/var/www`  and move the contents of the webroot
   (`/var/www/html`) there or you can leave it as is. The newly deployed instances will be located at
   `/var/www/instance-name`  while the main Central Dispatch site remains at `/var/www/html` or `/var/www/centraldispatch`.
   The rest of the guide will assume `/var/www/html`  so change all of the commands to the correct path if you chose
   `/var/www/centraldispatch`.

3. Set up SSL for this initial instance. This
   [blog by the great and powerful Orr](https://interworks.com/blog/morr/2019/10/24/portals-for-tableau-101-setting-up-ssltls-certificates-for-https/)
   will get you most of the way there.  NOTE: Ubuntu systems are slightly different.

4. There should already be a default conf file that has an **IncludeOptional** line that points to a directory where
   additional vhost conf files can go. Make sure you know where the newly added vhost conf files should go:
   * Ubuntu:
     * Default conf:  `etc/apache2/apache2.conf`
     * Includes vhost conf files:  `etc/apache2/sites-enabled/*.conf`
     * Ubuntu is a little different and actually stages the conf files here before being enabled:  `/etc/apache2/sites-available/*.conf`
   * Everything else:
     * Default conf:  `/etc/httpd/conf/httpd.conf`
     * Includes vhost conf files:  `/etc/httpd/conf.d/*.conf`

5. Create database user using the `worker_database_user.sql` example script at
   `/var/www/html/plugins/interworks/centraldispatch/workers` directory. Tweak the password if you'd like before executing.
   * Run the sql file:

     ```bash theme={null}
     mysql -u root -p curator < worker_database_user.sql
     ```

   * Enter root password

   * Test if the new user is there:  **mysql -u worker -p**

   * Enter worker password

6. Create directory  `/var/www/archives`

7. Set up worker script
   1. Copy php\_worker.example.php script to php\_worker.php in the `/var/www/html/plugins/interworks/centraldispatch/workers`
      directory:

      ```bash theme={null}
      sudo cp php_worker.example.php php_worker.php
      ```

   2. Copy `vhost.template.example.conf` to `vhost.template.conf` in the same directory.

      ```bash theme={null}
      sudo cp vhost.template.example.conf vhost.template.conf
      ```

   3. Make sure apache user owns everything:

      ```bash theme={null}
      sudo chown -R $APACHEUSER:$APACHEUSER /var/www
      ```

   4. Tweak paths as needed in  `php_worker.php`
      1. DB\_ENV\_DISPATCHER uses details from step 5 above.
      2. DB\_ENV\_INSTANCE uses the root database details to be able to provision users as needed. Can set up dispatcher
         user with these permissions if you don’t want to use the root account.
      3. Modify vhost section:
         1. Uncomment `directory` and modify as needed to where the vhost conf files should go from step 4.
         2. Uncomment `template` for `/var/www/html/plugins/interworks/centraldispatch/workers/vhost.template.conf`.
      4. Modify worker section:
         1. Uncomment `source_directory` for `/var/www/html`.
         2. Uncomment `archive_directory` for `/var/www/archives`.
      5. Modify \$DEFAULT\_BACKEND\_EMAIL as needed.
      6. Modify \$LINUX\_APACHE\_RESTART to the relevant apache restart command for your distro.
      7. Modify \$LINUX\_APACHE\_USER to the relevant apache user for your distro.

   5. Tweak vhost template as needed in workers directory
      1. Comment out the #apache 2.2 lines (lines 22-23) and uncomment out the #apache 2.4 lines unless using Apache 2.2.
      2. Update SSLCertificateChainFile, SSLCertificateFile, and SSLCertificateKeyFile as needed.

   6. Schedule root to run worker with the following command. Feel free to change the frequency (this one is every 15
      minutes). Also, make sure to change  `$APACHEUSER`  to the relevant apache user in the chown command (this makes
      sure the application owns all the files even though root is making everything).

      ```bash theme={null}
      (sudo crontab -l ; echo "*****/15 * * * * sudo php
      /var/www/html/plugins/interworks/centraldispatch/workers/php_worker.php >> /dev/null 2>&1 && sudo chown -R $APACHEUSER:$APACHEUSER /var/www****") | sudo crontab -
      ```

8. Restart apache

9. In the Central Dispatch Curator portal’s backend, register the workers with the dispatcher at **Backend** >
   **Settings** > **Central Dispatch** > **Central Dispatch Settings**. Probably with these settings:
   1. Host URL: localhost
   2. Worker name: localhost (or use something more descriptive)
   3. Install Path:  `/var/www`

10. Attempt to deploy a new managed instance at Backend > Central Dispatch > Managed Instances.

## Manual Back Out of Deployment

In case of a failure during a deployment, Central Dispatch is not yet able to automatically back out the deployment to
try again. You can determine the nature of the failure by visiting the Managed Instance record in the backend of the
Central Dispatch portal and scrolling to the bottom of the page. There will be an error field that will show any issues
the worker had during the deployment.

To back out a deployment, it's important to determine which step it failed at so you'll know which of the following
steps you'll need to take to back it out. They are in reverse order of the deployment, so you can skip steps if the
deployment didn't make it that far. When in doubt, just perform all of the steps.

1. Remove cron job with the name of this managed instance by using `sudo -u <apache user> crontab -e` to edit.
   *Note: This will use VI as the default editor in case you need to look up how to edit the file.*

2. If using Ubuntu, disable the vhost entry by running `sudo a2dissite <managed instance vhost record without .conf>`

3. Remove the vhost record specific to this managed instance in the vhosts directory (see step 4 above to determine
   location). The command will be similar to `sudo rm /etc/apache2/sites-available/<managed instance vhost record>`

4. Remove site-specific SSL/TLS certificate, key, and (optional) chain certificate, if the managed instance supplied
   them. These should be in the /etc/apache2/certs/ directory. The commands will be similar to these two commands below:

   ```bash theme={null}
   sudo rm /etc/apache2/certs/<name of manage instance crt file>
   ```

   ```bash theme={null}
   sudo rm /etc/apache2/certs/<name of managed instance key file>
   ```

5. Remove the portal code for the managed instance in the /var/www/ directory. The command will be similar to
   `sudo rm -Rf /var/www/<managed instance web root directory name>`

6. Drop the database specific to the managed instance by using `mysql -u root -p` and the root database credentials
   (see `/var/www/info.txt`). The SQL statement to drop the database would be: `DROP DATABASE '<database name>';`

7. Delete the database user specific to the managed instance by using `mysql -u root -p` and the root database
   credentials (see `/var/www/info.txt`). The SQL statement to drop the database would be:

   ```SQL theme={null}
   DROP USER IF EXISTS '<username>'@'localhost';
   ```


# Windows Central Dispatch
Source: https://docs.curator.interworks.com/setup/central_dispatch/windows_central_dispatch

Configure distributed processing with Central Dispatch on Windows systems

Each section below has steps you can follow, all steps must be followed to set up Central Dispatch accordingly.

## 1. Curator install and folder Creation

1. Install Curator using Apache installer like usual.
2. Ensure the following folders exist, and if not, use a Windows Explorer window to create them
   * `C:\InterWorks\Curator\vhosts`
   * `C:\InterWorks\Curator\archives`

## 2. `curator.conf` file adjustments

1. Move Central Dispatch portal to subfolder of htdocs
   1. Make directory `C:\InterWorks\Curator\htdocs\centraldispatch`
   2. Move all other files and folders in `htdocs` directory to `centraldispatch` directory using Windows Explorer
2. Save SSL/TLS certificates and key files to `C:\InterWorks\Curator\certs` directory (create if it doesn’t exist)
3. Update `curator.conf` Located in `C:\InterWorks\Curator`
   1. Point the default virtualhost’s document root and directory to `C:\InterWorks\Curator\htdocs\centraldispatch`
   2. Use wildcard subdomain for servername and/or serveralias (do not use \* in the path)
   3. Add include statement at the bottom to look for configuration files in `C:\InterWorks\Curator\vhosts` directory:
      1. IncludeOptional `C:\InterWorks\Curator\vhosts\`
   4. Configure it to listen on 443 and point at the certs and key in the certs directory by uncommenting the lines at
      the bottom section.
   5. Add these 2 lines to the 443 VirtualHost (usually under the DocumentRoot)
      1. ErrorLog `${APACHE_LOG_DIR}/centraldispatch_error.log`
      2. CustomLog `${APACHE_LOG_DIR}/centraldispatch_access.log` combined
4. Update the existing Curator cron scheduled task to fix the path to the (now) Central Dispatch portal (i.e.
   `C:\InterWorks\Curator\htdocs\centraldispatch\artisan`).
5. Restart apache using the shortcuts on the desktop. If you receive an error message about access, then right click on
   the `stop.bat` and `start.bat` scripts within `C:\InterWorks\Curator` and run as administrator.  Ensure the portal still
   works as expected.

## 3. Create the Worker Database User

1. Open the `worker_database_user.sql` example script in a text-editor, located in the
   `C:\InterWorks\Curator\htdocs\centraldispatch\plugins\interworks\centraldispatch\workers` directory.

2. Change the username and password as needed before executing.

3. Open a terminal and run the command below to create the new user

   ```bash theme={null}
   mysql -u root -p -e "source C:\InterWorks\Curator\htdocs\centraldispatch\plugins\interworks\centraldispatch\workers\worker_database_user.sql"
   ```

4. NOTE: You will be prompted to enter a password. Use the root user's password that was created when you installed
   Curator. Refer to the [Windows Installation here](/setup/installation/windows_installation).

## 4. Create script and vhost files

1. Navigate to the `C:\InterWorks\Curator\htdocs\centraldispatch\plugins\interworks\centraldispatch\workers` directory
2. Create a copy of `php_worker.example.php`, rename it to `php_worker.php`, and move it to `C:\InterWorks\Curator`.
3. Create a copy of `vhost.template.example.conf`, rename it to `vhost.template.conf`, and move it to
   `C:\InterWorks\Curator`.
4. You will have created the following files
   * `C:\InterWorks\Curator\php_worker.php`
   * `C:\InterWorks\Curator\vhost.template.conf`

## 5. Worker Script Setup

NOTE: Within PHP, use forward slashes, not backslashes for directory separators.  Outside of PHP, use backslashes.

1. Open `php_worker.php` in a text editor
2. Modify the user section:
   1. For the `DB_ENV_DISPATCHER` set the `user` and `pass` values to the user and password you set using the script in
      the **Create the Worker Database User** section above.
   2. `DB_ENV_INSTANCE` uses the `root` user's details for simplicity. This ensures you can provision with the highest
      access. Alternatively, if you do not want to use the `root` user for this create a separate user and use those details.
3. Modify vhost section:
   1. Uncomment `directory` for "C:/InterWorks/Curator/vhosts" (update path as needed).
   2. Uncomment `template` for `C:/InterWorks/Curator/vhost.template.conf` (update path as needed).
4. Modify worker section:
   1. Uncomment `source_directory` for "C:/InterWorks/Curator/htdocs/centraldispatch" (update path as needed).
   2. Uncomment `archive_directory` for "C:/InterWorks/Curator/archives" (update path as needed).
      1. Modify `$DEFAULT_BACKEND_EMAIL` as needed
      2. Modify `$WINDOWS_INSTALL_DIR` if not using C:/InterWorks/Curator (i.e. if installed to D:\InterWorks\Curator)

## 6. vhost Template Setup

1. Determine the Apache version you're using by running `C:\InterWorks\Curator\libs\Apache24\bin\httpd -v` in a Command
   Prompt window
2. Open `C:\InterWorks\Curator\vhost.template.conf` in a text editor
   1. If using Apache 2.2:
      1. Ensure lines 22-23 **do not** start with a '#', enabling those lines.
      2. Ensure line 25 starts with a '#', disabling that line.
   2. If using Apache 2.4:
      1. Ensure line 25 **does not** start with a '#', enabling that line.
      2. Ensure lines 22-23 start with a '#', disabling those lines.
3. Schedule worker by running the command in the `worker_scheduled_task.bat` example script. Tweak as needed. It
   defaults to 15 minutes.

## 7. Register and Test Dispatcher

1. In the Central Dispatch Curator portal’s backend, register the workers with the dispatcher at **Backend** >
   **Settings** > **Central Dispatch** > **Central Dispatch Settings**. Probably with these settings:
   1. Host URL: localhost
   2. Worker name: localhost (or use something more descriptive)
   3. Install Path: C:/InterWorks/Curator/htdocs/
2. Attempt to deploy a new managed instance at Backend > Central Dispatch > Managed Instances.

## Manual Back Out of Deployment

In case of a failure during a deployment, Central Dispatch is not yet able to automatically back out the deployment to
try again. You can determine the nature of the failure by visiting the Managed Instance record in the backend of the
Central Dispatch portal and scrolling to the bottom of the page. There will be an error field that will show any issues
the worker had during the deployment.

To back out a deployment, it's important to determine which step it failed at so you'll know which of the following steps
you'll need to take to back it out. They are in reverse order of the deployment, so you can skip steps if the deployment
didn't make it that far. When in doubt, just perform all of the steps.

1. Remove scheduled task with the name of this managed instance by opening the Windows Task Scheduler.

2. Remove the vhost record specific to this managed instance in the `C:\InterWorks\Curator\vhosts directory` (adjust drive
   letter as needed).

3. Remove site-specific SSL/TLS keys if the managed instance supplied them. These will be in the
   `C:\InterWorks\Curator\certs directory` (adjust drive letter as needed).

4. Remove the portal code for the managed instance in the `C:\InterWorks\Curator\htdocs directory` (adjust drive letter
   as needed).

5. Drop the database specific to the managed instance by using HeidiSQL and the root database credentials
   (see `C:\InterWorks\Curator\info.txt`). The SQL statement to drop the database would be:

   ```SQL theme={null}
   DROP DATABASE '<database name>';
   ```

6. Delete the database user specific to the managed instance by using HeidiSQL and the root database credentials
   (see `C:\InterWorks\Curator\info.txt`). The SQL statement to drop the database would be:

   ```SQL theme={null}
   DROP USER IF EXISTS '<username>'@'localhost';;
   ```


# Email Configuration
Source: https://docs.curator.interworks.com/setup/email/email_configuration

Configure SMTP and email settings for Curator features including Report Builder and notification systems.

There are a variety of places that use e-mail settings across Curator.  The largest piece is the
[Report Builder](/embedding_using_analytics/report_builder/overview_and_enabling_report_builder),
but you may want to also set up email to get notified when someone fills out a data-manager form.
Whatever the case, the e-mail setup will reside almost entirely with your e-mail provide or IT group that manages your
mail server.  Once you have confirmed with them that you'll be able to utilize their mail service, use the steps below
to fill out the details for your e-mail configuration on Curator.

## Enabling and Testing Mail Settings

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Mail** > **Mail Configuration** section from the left-hand menu (see "Mail
   Configuration Permissions" below if you do not see this menu item).
3. Fill out the form using the details provided from your mail administrator.
4. Save the form.
5. Ensure the details are accurate by clicking the "Test Saved Settings" and entering your email.
6. Once you click send, wait up to 5 minutes (and double-check your spam inbox) - if you have not received an e-mail
   double-check the settings with your mail administrator to ensure everything is set up properly

## Mail Configuration Permissions

Access to Mail configuration may not be granted by default depending on your installation.  In order to view the mail
configuration, ensure that your
[Backend User](/site_administration/backend_administrators/overview) has access.


# High Availability
Source: https://docs.curator.interworks.com/setup/high_availability/high_availability

Configure Curator for high availability infrastructure to ensure reliability and handle increased load

Curator can be configured to run in a high availability (HA) infrastructure to ensure better "up time" for your users
as well as handling more concurrent user load.  The standard components of the HA infrastructure are:

* **Load balancer** - Domain name is pointed here.  Routes user traffic to one of the application nodes.
  Example: AWS Elastic Load Balancer (ELB).
* **Application nodes** (2 or more) - Where Curator is installed.
  Example: AWS Elastic Compute Cloud (EC2).
* **Database** - The application nodes will use this to store data.  Having a single database keeps things synchronized.
  Example: AWS Relational Database Service (RDS).
* **Filesystem** - The application nodes will use this to store thumbnails, backups, etc.
  Example: AWS Elastic File System (EFS).
  <img alt="HA diagram" />
  *Note: the example above shows AWS services but Azure and other cloud providers are viable options.*

## Requirements

Below are the specific requirements for each component of the infrastructure and what needs to be completed prior to the
install.

* **Load Balancer**
  * This is where SSL will need to be handled.  The most common setup is to terminate SSL at the load balancer as
    opposed to having certificates on each application node.
  * **Prior to install:**  You don't need to have the load balancer ready prior to the install.  This can be configured afterwards.
* **Application nodes**
  * The same server requirements for the standard Curator installation exist for each application node.  Those
    requirements can be found here: [https://curator.interworks.com/requirements](https://curator.interworks.com/requirements).
  * **Prior to install:**  The application nodes need to be spun up and have root SSH or admin RDP access.  The SSH or
    RDP access should be tested before the installation.
* **Database**
  * The database should be *separate* from the application nodes.  Although it can be configured inside one of the
    application nodes it defeats the purpose of high availability because if that node goes down none of the others will
    be functional.
  * **Prior to install:**  The database needs to be spun up, an empty database needs to be created (it can be called
    `curator` for simplicity), and it needs to be accessible from each application node.  Test the accessibility from each
    application node with something like this:

    ```bash theme={null}
    sudo mysql -u $DBUSER--password=$DBPASSWORD -h $DBHOST -e "SHOW DATABASES"
    ```

    Replace variables with your credentials and database host.  You should be able to see the empty database you created
    in the output.
* **Filesystem**
  * Like the database, the filesystem needs to be separate from the application nodes to prevent unnecessary downtime.
    Cloud services (AWS, Azure, etc.) have great options for this that have built in redundancy.  If you aren't using a
    cloud service and are using Windows for the infrastructure you can use the database node for the shared filesystem
    with a network drive.
  * **Prior to install:**  The filesystem needs to be spun up and accessible by each application node.  This should be
    tested by creating a simple text file and ensuring it's visible from each application node.

## Other Infrastructures

There are numerous ways to do high availability that include different patterns with the database and filesystem setups.
What's described above is certainly not the only method but it is the simplest for Curator.  We're happy to help
troubleshoot if you take a different route or run into issues with the infrastructure detailed above.  While we're
fully responsible for errors rising from the application code, the success of the infrastructure will be dependent on
your team that manages it.

## Post Install

Once the install and configuration is complete at the server-level make sure to go to the **Curator backend** >
**Settings** > **Curator** > **Worker Nodes** and add each application node to the list.  This will ensure when a
software upgrade is initiated or the application cache is cleared each node will stay synchronized.

### Worker Nodes

Worker nodes are essential for maintaining high availability and load balancing. Each worker node runs an instance of
Curator and shares the load of incoming requests. This setup ensures that if one node fails, others can continue to
handle the traffic, minimizing downtime and improving reliability.

#### Adding Worker Nodes (Command Line)

To register a worker node to your Curator cluster, you can use the  `distributed:addnode`  console command. This command
registers a new node with the cluster, allowing Curator to properly sync changes with it.

* **Open the terminal**  and navigate to the directory where Curator is installed.

* **Run the command**  with the IP address of the new node:

  ```bash theme={null}
      php artisan distributed:addnode {Curator Node IP}
  ```

  Replace  `{Curator Node IP}`  with the actual IP address of the node you want to register.

* **Verify the node addition**: The command will output a confirmation message indicating that the node has been
  registered successfully, and you can find the newly added node in the **Curator backend** >**Settings** > **Curator** >
  **Worker Nodes**.

**Example:**

```bash theme={null}
php artisan distributed:addnode "http://192.168.1.2"
```

This command will register the node with IP address  `192.168.1.2`  to the Curator cluster.

#### Adding Worker Nodes (In the Backend)

You can also register worker nodes directly through the Curator backend interface.

1. **Navigate** to the Curator backend > Settings > Curator > Worker Nodes.
2. **Add a new node**  by entering the URL (e.g.,  `http://192.168.1.2`) in the **URL** field.
3. **Save the changes**  to register the new node with the cluster.


# IIS Installation (Unavailable)
Source: https://docs.curator.interworks.com/setup/installation/iis_installation

Information about IIS installation support status and migration recommendations for Curator.

**Curator no longer supports new installations on IIS.**

Instead, download the installer for [Windows](/setup/installation/windows_installation)

NOTE: *If you already have IIS installed, Curator's support team will continue to support your instance, but any new
installations will require our Apache installation.  It is highly recommended that you migrate to Apache for increased
stability.*


# Linux Installation
Source: https://docs.curator.interworks.com/setup/installation/linux_installation

Instructions for installing Curator on Linux.

The automated installer covers the vast majority of setups, but each server is different and may require
commands specific to your IT infrastructure.

## Installation Steps

If you are using one of the following Linux Operating Systems, follow our simple instruction steps to get started:

* Ubuntu
* CentOS
* RHEL

<Steps>
  <Step title="Run the Installation Script">
    SSH into your web server, ensure you're using a user that has full sudo access, and run the command below:

    ```bash theme={null}
    curl -s -o curator.sh https://api.curator.interworks.com/scripts/linux_install.sh && chmod +x ./curator.sh && ./curator.sh
    ```
  </Step>

  <Step title="Retrieve Your Credentials">
    Locate your license key (sent from InterWorks) and open `/var/www/curator_info.txt` to retrieve your default
    administrator credentials.
  </Step>

  <Step title="Open the Installer">
    Open `http://curatorexample.com/install.php` in a browser - replacing `curatorexample.com` with your site's URL. If
    you're on the server you installed, you may also use `localhost`.

    *This may be an IP address or computer name until your IT team sets up DNS.*
  </Step>

  <Step title="Credentials">
    The installer will generate credentials for use during installation and will store them in a file in the installation
    directory (Default: `/var/www/curator_info.txt` or `C:\InterWorks\Curator\curator_info.txt` in Windows). You will need
    these credentials to complete the installation and to log in to the Curator backend after installation.
  </Step>

  <Step title="License Key">
    Enter your license key when prompted. If you do not have a license key, please contact InterWorks to obtain one.

    <img alt="License key prompt page" />
  </Step>

  <Step title="Database Connection">
    You may be prompted to enter your database connection information if the installer is unable to automatically find the
    database for you.

    <img alt="Database credentials prompt page" />
  </Step>

  <Step title="Success">
    If the installation is successful, you will be redirected to your new Curator homepage

    <img alt="Database credentials prompt page" />

    Using the same auto-generated credentials created in the install script above, you can log into the Curator backend which
    can be accessed from `http://curatorexample.com/backend`. If you're on the server you installed, you may also use localhost.
    Keep in mind this may be an IP address or computer name until your IT team sets up DNS.
  </Step>
</Steps>

## Custom Setup

The install script can take optional parameters to specify values for the installation script. This can be helpful in
distributed setups, or scripted installations.

```bash theme={null}
curl -o curator.sh https://api.curator.interworks.com/scripts/linux_install.sh
chmod +x ./curator.sh
./curator.sh -f -h [database_host] -u [database_username] -p [database_password] -P [database_port] -d [database_name] -l [license_key] -s [persistent_storage_location] -v [curator_version]
```

Arguments:

* `-h` The database hostname *Needed when using an external database host*
* `-u` The database username  *`Default: curator`*
* `-p` The database password *Default: auto-generated password.  Use this when you need to use a connection to a
  database for a user that has already been created with a specific password.*
* `-P` The database port *`Default: 3306`*
* `-d` The database name *`Default: curator`*
* `-l` The License Key for your Curator installation. When performing a full installation, this is required.
* `-s` Path to a persistent storage location *Container-based or distributed installations typically require this.*
* `-v` Sets the version of Curator to install. *Default: most recent version.*

Options:

* `-f` Full Installation, this flag is required in most custom setups to avoid the in-browser installer.

## AWS EC2 Process

AWS provides a helpful outline on [how to connect to an AWS EC2 instance from Windows using Putty](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html).

## Network Whitelist Requirements

For installations in environments with restricted internet access or firewall configurations, the following URLs
should be whitelisted to ensure proper functionality:

### RHEL/CentOS Systems

* InterWorks API
  * `api.curator.interworks.com`
* EPEL Repository
  * `dl.fedoraproject.org`
  * `download.fedoraproject.org` (covers mirrors.fedoraproject.org)
* Remi Repository (PHP packages)
  * `*.remirepo.net` (covers rpms.remirepo.net, repo.remirepo.net, mirrors.remirepo.net)
* Base RHEL/CentOS Repositories
  * `*.centos.org` (covers vault.centos.org, mirror.centos.org)
  * `download.redhat.com`
  * `cdn.redhat.com`
* CDN Networks
  * `*.akamaiedge.net` (covers `*.akamaitechnologies.com` - same Akamai network)

### Ubuntu Systems

* InterWorks API
  * `api.curator.interworks.com`
* Ubuntu Repositories
  * `*.archive.ubuntu.com` (covers archive.ubuntu.com, us.archive.ubuntu.com, gb.archive.ubuntu.com, etc.)
  * `security.ubuntu.com`
  * `ports.ubuntu.com`
  * `changelogs.ubuntu.com`
* Launchpad PPAs (for ondrej/apache2 and ondrej/php)
  * `*.launchpad.net` (covers ppa.launchpad.net, launchpad.net)
  * `ppa.launchpadcontent.net`
  * `keyserver.ubuntu.com`


# Windows Installation
Source: https://docs.curator.interworks.com/setup/installation/windows_installation

Instructions for installing Curator on Windows.

## Installation Steps

<Steps>
  <Step title="Download the Installer">
    Log in to the server where you'd like to install Curator and [download the Curator installer for Windows](https://api.curator.interworks.com/CuratorSetup.exe).
  </Step>

  <Step title="Run the Installer">
    Locate your download and right-click the file, then select "Run as Administrator" to begin the installation process.

    <img alt="Run .exe as admin" />

    Click the "Install" button to run initial installation process:

    <img alt="Installer view" />

    Click "Options" to change the installation directory.
  </Step>

  <Step title="Credentials">
    The installer will generate credentials for use during installation and will store them in a file in the installation
    directory (Default: `/var/www/curator_info.txt` or `C:\InterWorks\Curator\curator_info.txt` in Windows). You will need
    these credentials to complete the installation and to log in to the Curator backend after installation.
  </Step>

  <Step title="License Key">
    Enter your license key when prompted. If you do not have a license key, please contact InterWorks to obtain one.

    <img alt="License key prompt page" />
  </Step>

  <Step title="Database Connection">
    You may be prompted to enter your database connection information if the installer is unable to automatically find the
    database for you.

    <img alt="Database credentials prompt page" />
  </Step>

  <Step title="Success">
    If the installation is successful, you will be redirected to your new Curator homepage

    <img alt="Database credentials prompt page" />

    Using the same auto-generated credentials created in the install script above, you can log into the Curator backend which
    can be accessed from `http://curatorexample.com/backend`. If you're on the server you installed, you may also use localhost.
    Keep in mind this may be an IP address or computer name until your IT team sets up DNS.
  </Step>
</Steps>

## Log Locations

These paths are dependant on your installation location, but these are the default paths:

* Apache: `C:\InterWorks\Curator\httpd_errors.log`
* PHP: `C:\InterWorks\Curator\php_errors.log`
* Installation Log: `C:\InterWorks\Curator\install.log`

## Other Information

These paths are dependant on your installation location, but these are the default paths:

* Webroot: `C:\InterWorks\Curator\htdocs`
* HTTPD Config: `C:\InterWorks\Curator\web.conf`
* PHP.ini: `C:\InterWorks\Curator\php.ini`
* Start Process: `C:\InterWorks\Curator\start.bat` (Also desktop shortcut)
* Stop Process: `C:\InterWorks\Curator\stop.bat` (Also desktop shortcut)
* Apache Location: `C:\InterWorks\Curator\libs\Apache24`
* Database Location: `C:\InterWorks\Curator\libs\MariaDB`
* PHP Location: `C:\InterWorks\Curator\libs\PHP`

## Changing the Install Path

This is *not recommended* but may be necessary in rare circumstances. The installer will default to
`C:\InterWorks\Curator` if no changes are made to the install path. If you must change the install path, click the
"Options" button in the installer window

<img alt="Highlight options button" />

then change the Install Location path:

<img alt="Change install path" />

Please note that the paths above may no longer be valid if you change the install path.


# Forward Proxy
Source: https://docs.curator.interworks.com/setup/proxy_configuration/forward_proxy

Configure forward proxy settings for internet access and external connectivity

Curator utilizes internet access to connect to Tableau Server as well as Curator's web servers for updates.
When configured without outbound internet access, Curator upgrades must be performed manually and Tableau Server must
be accessible within the LAN.

Often, IT teams prefer to route internet traffic first through a proxy.
When configured to work through a proxy, Curator doesn't send requests directly to the internet.
Instead, it sends requests to the forward proxy, which in turn forwards the request.

To configure a forward proxy with Curator, Apache configuration files can be used.

On Windows, the `curator.conf` file is a great place for this configuration.
On Linux, `/var/www/html/.htaccess`, or any of the httpd.conf files can also be utilized.

The **proxy\_override** environment variable points Curator to a specific proxy for web requests.
If needed, **no\_proxy\_override** can be used to specify a route that should not use the proxy for traffic.

```conf theme={null}
SetEnv proxy_override "http://proxy:80"
SetEnv no_proxy_override "www.example.com"
```


# Reverse Proxy
Source: https://docs.curator.interworks.com/setup/proxy_configuration/reverse_proxy

Configure reverse proxy and load balancing solutions for Curator

When installing Curator, you may wish to place Curator behind a reverse proxy or load balanced solution.

## Health Checks

Health checks should be run against the `/ping` route instead of simply the base `/` route.
The base / route will often return a 302 redirect, which many load balancers view as a "down" response.
The /ping route will always return a 200 response.

## Headers

When your users access Curator over the reverse proxy, specific "headers" are used to tell Curator how to process the
request.

**X-FORWARDED-FOR** : The IP address of the end user.

**X-FORWARDED-HOST** : The host name of the request.
*Note: A "Forced Domain" in Portal Settings->Security overrides this value.*

**X-FORWARDED-PROTO** :  Whether to use HTTPS or HTTP for routes.

## Unable to adjust headers

Often, reverse proxy solutions are missing some or all of these headers.

To help configure a reverse proxy with Curator, Apache configuration files can be used.

On Windows, the `curator.conf` file is a great place for this configuration.
On Linux, `/var/www/html/.htaccess`, or any of the httpd.conf files can also be utilized.

```conf theme={null}
SetEnv HOST "example.curator.interworks.com"
SetEnv HTTP_X_FORWARDED_HOST "example.curator.interworks.com"

SetEnv HTTPS "on"
SetEnv HTTP_X_FORWARDED_PROTO "https"
```

In addition to these settings, the security settings in **Settings** > **Curator** > **Portal Settings** > **General**
can be used.
In particular, **Forced Domain** and **Force SSL** should be utilized to specify the domain of Curator and to use SSL.


# Basic HTTP Authentication
Source: https://docs.curator.interworks.com/setup/ssl/basic_http_authentication

Set up basic HTTP authentication for additional browser-level security

Basic HTTP Authentication provides a secondary browser-level authentication system. Usually used to secure
non-production setups. To enable the Basic HTTP Authentication:

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Settings** > **Curator** > **Portal Settings** in the left navigation.
4. Click on the "General" tab at the top of the main page content.
5. Click to switch on the "Basic HTTP Authentication" setting under the "Security" section and click the "Save" button.


# Force SSL
Source: https://docs.curator.interworks.com/setup/ssl/force_ssl

Configure Curator to enforce SSL/HTTPS connections for enhanced security.

Force SSL (https) will force all HTTP request to be https instead. This will require you to set up SSL certificates
first before enabling the feature. Otherwise, the site will run into an issue. To enable Force SSL (https):

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Settings** > **Curator** > **Portal Settings** in the left navigation.
4. Click on the "General" tab at the top of the main page content.
5. Click to switch on the "Force SSL" setting under the "Security" section and click the "Save" button.


# Linux SSL
Source: https://docs.curator.interworks.com/setup/ssl/linux_ssl

Configure SSL certificates and HTTPS encryption for Curator on Linux systems

1. First, find your `curator.conf` file. For Ubuntu installations, this is located in `/etc/apache2/sites-enabled`. For
   all other Linux distributions, this file is located in `/etc/httpd/conf.d/curator.conf`. If you cannot find this file,
   you may have an old Curator installation. If so,
   [download `curator.conf` here](https://api.curator.interworks.com/file/curator_conf).

2. Upload your SSL certificate, key, and (optionally) chain files to the webserver. This can be done with a secure copy
   (SCP) client, such as FileZilla. Place these certificates in */etc/apache2/certs* for Ubuntu, or */etc/httpd/certs*, for
   all other Linux distributions.

3. Replace the references to SSLCertificateChainFile, SSLCertificateFile, and SSLCertificateKeyFile in the `curator.conf`
   to the location you uploaded them to in Step #2.

4. Save the contents of the file and restart apache with the commands below:

   ```bash theme={null}
   sudo apachectl restart
   ```

5. Navigate to the HTTPS version of the link to your portal in your browser (i.e. `https://curatorexample.com`). You
   should see a lock icon appear in the URL bar after the site loads to indicate that it is successfully encrypted. If you
   don’t see the lock or if you get an error, check your certificate for invalid information, such as incorrect site name
   or missing Subject Alternative Names.

## Debugging SSL

Having issues? It happens! SSL certificates can be uniquely challenging to implement. Here are a few debugging tips:

1. Make sure the certificate and key match. Often these get mismatched. Your server will not start if they do not match.
   If either of these commands errors, you may not have correctly formatted certificates. Make sure you acquired Apache/PEM
   certificates:

   ```bash theme={null}
   openssl rsa -modulus -noout -in yourKeyFile.key | openssl md5
   openssl x509 -modulus -noout -in myServer.crt | openssl md5
   ```

2. The certificate chain file is important, but can cause issues. If your Curator server won't start, try commenting out
   the SSLCertificateChainFile line in `curator.conf` temporarily to ensure that the issue is not the chain file.

3. Check Apache/HTTPD's error log. This can be found in /var/log/apache2/error\_log (Ubuntu) or /var/log/httpd/error\_log
   (All other distros). Also check `/var/www/curator_error.log`, if it exists. If the error message is not detailed enough,
   try increasing "LogLevel" to "debug" in `curator.conf`. (Note: be sure to set this value back to "warn" after you are done!)

## Notes on obtaining SSL certificates

1. Curator uses "Apache" type certificates. These may be referred to as "OpenSSL" or PEM certificates as well.
2. These certificates may in one big bundle, or separated into key, certificate, and chain files.
3. When installing key certificates, many providers require a key-passphrase.
   Once installed on the Curator server and at rest, you may wish to remove this passphrase.
   If the passphrase remains, it will be required anytime there is a restart of the web server.
   **STORE THE PASSPHRASE IN A SAFE PLACE. IF IT REMAINS ON THE KEY AND IS LOST YOU WILL HAVE TO GENERATE NEW CERTIFICATES.**
   To remove the passphrase, use this command.

   ```bash theme={null}
   openssl rsa -in [original.key] -out [new.key]
   ```

## SSL Protocols / Ciphers (Optional)

1. You may wish to update your SSL protocols and cipher suites. To do this, you'll need a little more info about your
   web server. Run the command below to get the Apache and OpenSSL versions:

   ```bash theme={null}
   httpd -V 2>/dev/null | grep version; apache2 -V 2>/dev/null | grep version; openssl version; php -v | grep cli
   ```

2. The expected output will look something like this:

   ```bash theme={null}
   Server version: Apache/2.4.48 ()
   OpenSSL 1.0.2k-fips  26 Jan 2017
   PHP 7.4.21 (cli) (built: Jul  7 2021 17:35:08) ( NTS )
   ```

3. Take the information retrieved in the previous step and use it to fill out the form on this
   [SSL Certificate Generator site](https://ssl-config.mozilla.org/#server=apache).

   * Select **Apache** for "Server Software"
   * Select **Intermediate** for "Mozilla Configuration".
   * Enter your Apache version
   * Enter your OpenSSL version

4. Replace the appropriate areas in the `curator.conf` file with the SSLProtocol and SSLCipherSuite that was generated
   on the SSL Certificate Generator site.

   For example:

   ```conf theme={null}
   SSLProtocol             all -SSLv3 -TLSv1 -TLSv1.1
   SSLCipherSuite          ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384
   ```

5. Have a server open to the internet? Qualys has a free tool to test the certificates, protocols/ciphers, and their
   security: [https://www.ssllabs.com/ssltest/analyze.html](https://www.ssllabs.com/ssltest/analyze.html)


# Windows SSL
Source: https://docs.curator.interworks.com/setup/ssl/windows_ssl

Configure SSL/HTTPS for Curator installations on Windows servers with IIS.

## Finding relevant files

1. Find the **`curator.conf`** file (default location is `C:\InterWorks\Curator\curator.conf`).
2. Find the relevant keys. These will either be in a bundle, or separated into key, certificate, and chain files.
3. Put your keys into the correct directory (default location is `C:\InterWorks\Curator\certs\`).

## Removing Passphrases (Required, if applicable)

If your certificate utilizes a passphrase, you'll need to remove it in order to use the certificate with Curator since
passphrases are not supported by Apache on Microsoft Windows servers.

1. Curator uses "Apache" type certificates. These may be referred to as "OpenSSL" or PEM certificates as well.
2. Windows is unique in that it cannot use certificates with embedded passphrases,
   so these have to be removed if they are present.
   These passphrases would normally be required before a restart of your web server on other operating systems,
   but are not able to be used here.
3. To remove the passphrases, you can use this command in the same directory as the certificates using Powershell.

   ```bash theme={null}
   & 'C:\InterWorks\Curator\libs\Apache24\bin\openssl.exe' rsa -in [original.key] -out [new.key]
   ```

## Replacing References

1. Locate the references in the file (listed below) and replace your new .crt, .pem, and .key files where they are
   referenced in the `curator.conf` file.

2. Un-comment the lines (by deleting the `#` at the front of the line) starting at `Listen 443` and ending at
   `</IfModule>`.  See example below:

   ```conf theme={null}
   #Uncomment the lines below for SSL
   Listen 443
   <IfModule mod_ssl.c>
       <VirtualHost _default_:443>
           SSLEngine on
           ServerName www.example.com
           DocumentRoot "C:\InterWorks\Curator\htdocs"
           RewriteEngine on

           SSLCertificateChainFile C:\InterWorks\Curator\certs\chain.crt
           SSLCertificateFile C:\InterWorks\Curator\certs\cert.pem
           SSLCertificateKeyFile C:\InterWorks\Curator\certs\cert.key

           SSLProtocol                 [protocol]
           SSLCipherSuite              [ciphersuite]
           SSLHonorCipherOrder         on
           SSLCompression              off

           <Directory "C:\InterWorks\Curator\htdocs">
               AllowOverride All
               Options Indexes FollowSymLinks
               Require all granted
           </Directory>
   </VirtualHost>
   </IfModule>
   ```

3. After the configuration file has been edited and saved, restart Curator.

## SSL Protocols / Ciphers (Optional)

1. You may wish to update your SSL protocols and cipher suites. To do this, you'll need a little more info about your
   environment. Run the command below to get your Apache and OpenSSL versions, assuming default install locations for both:

   ```bash theme={null}
   & 'C:\InterWorks\Curator\libs\Apache24\bin\httpd.exe' -v; & 'C:\InterWorks\Curator\libs\Apache24\bin\openssl.exe' version
   ```

2. The expected output will look something like this:

   ```bash theme={null}
   Server version: Apache/2.4.59 (Win 64)
   OpenSSL 3.3.1 4 Jun 2024 (Library: OpenSSL 3.3.1 4 Jun 2024)
   ```

3. Take the information retrieved in the previous step and use it to fill out the form on this
   [SSL Certificate Generator site](https://ssl-config.mozilla.org/#server=apache).

   * Select **Apache** for "Server Software"
   * Select **Intermediate** for "Mozilla Configuration".
   * Enter your Apache version
   * Enter your OpenSSL version

4. Replace the appropriate areas in the `curator.conf` file with the SSLProtocol and SSLCipherSuite that was generated
   on the SSL Certificate Generator site.

   For example:

   ```conf theme={null}
   SSLProtocol             all -SSLv3 -TLSv1 -TLSv1.1
   SSLCipherSuite          ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:
   ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:
   DHE-RSA-AES256-GCM-SHA384:DHE-RSA-CHACHA20-POLY1305
   ```

5. Have a server open to the internet? Qualys has a free tool to test the certificates, protocols/ciphers, and their
   security: [https://www.ssllabs.com/ssltest/analyze.html](https://www.ssllabs.com/ssltest/analyze.html)

## Troubleshooting

If Apache fails to start after configuring SSL, see the
[Windows Apache SSL Troubleshooting](/setup/ssl/windows_ssl_troubleshooting) guide for step-by-step diagnostics
and fixes for common issues.


# Windows SSL (IIS)
Source: https://docs.curator.interworks.com/setup/ssl/windows_ssl_iis_deprecated

Legacy SSL configuration for deprecated Windows IIS installations

<Danger>Curator no longer supports IIS on new installations.</Danger>

The information below is for use only for existing installs.  It is *highly* recommended that you reinstall with Apache for
stability, please see our
[Windows Apache Installation](/setup/installation/windows_installation)
documentation for steps on how to achieve the best Curator experience for Windows.

## Enabling SSL

1. In IIS Manager, on the left-hand pane, select the server (note: not the site).

2. On the server Home page double-click **Server Certificates** (in the center pane).

3. On the right-hand pane click the `Complete Certificate Request` link.

4. Follow the steps below in the Complete Certificate Request wizard, then click **OK**:

   **File name containing the certificate authority's response:** Your .cer file

   **Friendly name:** Give your cert a name!  Recommended format: `curator-cert-[expiration-date]`

   **Select a certificate store for the new certificate:** Select *Web Hosting*.

5. In IIS Manager, on the left-hand pane, select the site that is running Curator.

6. On the right-hand pane under *Edit Site*, click **Bindings...**.

7. In the Bindings window, click **Add**

8. Follow the steps below in the  Add Site Bindings window, then click **OK**:

   **Type** Select https.

   **IP address** Select the IP address of the site (or select All Unassigned).

   **Port** Type port 443

   **SSL certificate** 	Select the new SSL cert you created in step #4

9. On the right-hand pane click **Restart**


# Windows Apache SSL Troubleshooting
Source: https://docs.curator.interworks.com/setup/ssl/windows_ssl_troubleshooting

Diagnose and resolve common Apache SSL startup failures on Windows servers running Curator.

If Apache fails to start after configuring SSL on a Windows Curator installation, work through the steps below
to identify and resolve the issue.

<Note>
  The examples below use the default installation path `C:\InterWorks\Curator`. If Curator was installed on a
  different drive or directory, adjust the paths accordingly (e.g. `D:\InterWorks\Curator`).
</Note>

## Step 1: Test the Configuration From the Command Line

Open PowerShell as Administrator and run:

```bash theme={null}
& 'C:\InterWorks\Curator\libs\Apache24\bin\httpd.exe' -t
```

This validates the configuration and outputs a specific error message pointing to the exact file, line number, and
problem. If everything is valid, it outputs `Syntax OK`.

<Note>
  This is the fastest way to identify the issue. If the output points to a clear problem, skip to
  [Common SSL Issues and Fixes](#common-ssl-issues-and-fixes) for the resolution.
</Note>

## Step 2: Check the Apache Error Log

If Step 1 wasn't sufficient, check the Apache error log:

```
C:\InterWorks\Curator\libs\Apache24\logs\error.log
```

Open this in Notepad — the most recent entries at the bottom will show what went wrong during the last startup attempt.

## Step 3: Check the Windows Event Log

1. Attempt to start the **Curator HTTPD Server** service from the Windows Services Manager.
2. After it fails, press **Win + R**, type `eventvwr.msc`, and press **Enter**.
3. Navigate to **Windows Logs** > **Application**.
4. The most recent error entries at the top will be from the failed startup attempt — double-click them and read
   the **Description** field for the actual error message.

## Common SSL Issues and Fixes

<AccordionGroup>
  <Accordion title="Certificate key has a passphrase (most common on Windows)">
    **Error:** `SSLPassPhraseDialog builtin is not supported on Win32` or the service hangs waiting for passphrase input.

    **Fix:** Strip the passphrase from the key:

    ```bash theme={null}
    & 'C:\InterWorks\Curator\libs\Apache24\bin\openssl.exe' rsa -in C:\InterWorks\Curator\certs\your_key.key -out C:\InterWorks\Curator\certs\your_key_nopass.key
    ```

    Then update `SSLCertificateKeyFile` in `C:\InterWorks\Curator\curator.conf` to point to the new key.

    See also: [Removing Passphrases](/setup/ssl/windows_ssl#removing-passphrases-required-if-applicable) in the
    Windows SSL setup guide.
  </Accordion>

  <Accordion title="Certificate file path is wrong or file missing">
    **Error:** `SSLCertificateFile: file 'C:\...' does not exist or is empty`

    **Fix:** Verify the paths in `C:\InterWorks\Curator\curator.conf` for these directives all point to files that
    actually exist in `C:\InterWorks\Curator\certs\`:

    * `SSLCertificateFile`
    * `SSLCertificateKeyFile`
    * `SSLCertificateChainFile`
  </Accordion>

  <Accordion title="SSL section not fully uncommented in curator.conf">
    **Error:** Syntax errors referencing lines in the SSL block.

    **Fix:** Open `C:\InterWorks\Curator\curator.conf` and ensure the entire `<VirtualHost *:443>` block and the
    `Listen 443` line are fully uncommented (no stray `#` characters).

    See: [Replacing References](/setup/ssl/windows_ssl#replacing-references) in the Windows SSL setup guide.
  </Accordion>

  <Accordion title="Chain/intermediate certificate file missing">
    **Error:** `SSLCertificateChainFile: file does not exist`

    **Fix:** Ensure the CA intermediate/chain certificate is in the certs directory and referenced correctly. If you
    have a single combined cert, comment out the `SSLCertificateChainFile` directive.
  </Accordion>

  <Accordion title="Certificate and key don't match">
    **Error:** `certificate and private key do not match`

    **Fix:** Verify they match by comparing their modulus hashes:

    ```bash theme={null}
    & 'C:\InterWorks\Curator\libs\Apache24\bin\openssl.exe' x509 -noout -modulus -in C:\InterWorks\Curator\certs\your_cert.crt | & 'C:\InterWorks\Curator\libs\Apache24\bin\openssl.exe' md5
    & 'C:\InterWorks\Curator\libs\Apache24\bin\openssl.exe' rsa -noout -modulus -in C:\InterWorks\Curator\certs\your_key.key | & 'C:\InterWorks\Curator\libs\Apache24\bin\openssl.exe' md5
    ```

    Both commands should output the same hash. If they don't, the wrong key or certificate file is being used.
  </Accordion>

  <Accordion title="Port 443 already in use">
    **Error:** `could not bind to address 0.0.0.0:443`

    **Fix:** Check what's using port 443:

    ```bash theme={null}
    netstat -ano | findstr :443
    ```

    If IIS or another service is on port 443, stop it or change the Curator port.
  </Accordion>

  <Accordion title="Certificate in wrong format (DER instead of PEM)">
    **Error:** `error reading certificate` or `PEM routines:get_name:no start line`

    **Fix:** Apache requires PEM format (text starting with `-----BEGIN CERTIFICATE-----`). Convert from DER if needed:

    ```bash theme={null}
    & 'C:\InterWorks\Curator\libs\Apache24\bin\openssl.exe' x509 -inform DER -in your_cert.cer -out your_cert.pem
    ```
  </Accordion>
</AccordionGroup>

## After Fixing

1. Re-run the config test:

   ```bash theme={null}
   & 'C:\InterWorks\Curator\libs\Apache24\bin\httpd.exe' -t
   ```

2. If it says `Syntax OK`, start the **Curator HTTPD Server** service from Services Manager.


# Adding Your First Dashboard
Source: https://docs.curator.interworks.com/setup/trial_quick_start_guide/adding_your_first_dashboard

Step-by-step guide to create your first analytics connection and add dashboards to Curator.

Click on **Integrations → Connections**

Click on **New Connection button**

* **Name**
  * Name your connection
* **Slug**
  * This slug (url extension) will auto-generate but can be customized
* **Description**
* **Platform**
  * Options include: Tableau, Power BI, ThoughtSpot
  * After selecting an option, fill out the platform specific connection information and credentials

## Tableau

### Tableau Server

1. **Enter Site name** (e.g. `https://analytics.acme.com`)
2. **Enter Service Account credentials or Personal Access Token**. To enter Personal Access Token, follow the below steps:
   1. Log onto your Tableau Server
   2. Click account icon on top right of screen (by default, will by a circle with your initials in it)
   3. Select My Account Settings
   4. Scroll to Personal Access Token
   5. Enter a Name for your Token and click Create Token

Additional information on Personal Access Tokens can be found in [Tableau’s documentation](https://help.tableau.com/current/pro/desktop/en-us/useracct.htm#create-and-revoke-personal-access-tokens).

### Tableau Cloud

1. **Select the Tableau Cloud Host region** (found in the server url)
2. **Enter the Site name** (found in the server url after logging in)
3. **Enter your Personal Access Token**
4. **To enter Personal Access Token, follow the below steps:**
   1. Log onto your Tableau Server
   2. Click account icon on top right of screen (by default, will by a circle with your initials in it)
   3. Select My Account Settings
   4. Scroll to Personal Access Token
   5. Enter a Name for your Token and click Create Token

Additional information on Personal Access Tokens can be found in [Tableau’s documentation](https://help.tableau.com/current/pro/desktop/en-us/useracct.htm#create-and-revoke-personal-access-tokens).

#### Power BI

**Enter your Tenant ID in Azure**. To find your Tenant ID, follow this [documentation](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/how-to-find-tenant).

#### ThoughtSpot

1. Enter your ThoughtSpot URL
2. Enter your ThoughtSpot credentials

## Adding a Dashboard From Your Server

Once you have established a connection to your server you can begin adding individual Dashboard connections. For our
example we will follow along with a Tableau Dashboard but the instructions are similar for other BI platforms.

1. **Click Tableau** (or your BI Platform Option) → **Dashboards**
2. **Click the New Dashboard Button**

Select desired Server, Site, Project, Workbook, and Dashboard then click create to establish a connection.

<img alt="Dashboard dropdowns" />

Connect dashboards will be listed in the Tableau → Dashboard menu:

<img alt="Dashboard list" />

## Adding a Menu Link to the Navigation

After a connection to a Dashboard has been established, the simplest method is to add a menu link to the navigation pane
at the top of your environment.

<img alt="homepage hero image and menu" />

Click **Content → Navigation**

1. Select New Menu Link
2. Select your Dashboard Link Type
3. Select your Dashboard
4. Select Create

Once you create the link you will be brought to a page that displays the navigation hierarchy. You can control the
navigation pane’s order and drop down menus here:

<img alt="navigation reorder view" />

After you have decided on hierarchy, navigate to the front end and see your new navigation menu items that lead to your dashboards:

<img alt="homepage hero image and menu" />


# Creating Your First Page
Source: https://docs.curator.interworks.com/setup/trial_quick_start_guide/creating_your_first_page

Learn how to use the page builder to create and customize your first content page in Curator.

Click on **Content → Pages → New Page**

To get started, enter a page title and toggle whether you want to show or hide it.

## Page Builder

To get started with the page builder, click the + button on the empty page builder interface.

<img alt="empty page" />

### Add an Element

An interface will popup which gives you the option to Add an Element.

The default container in your preview represents a single element. These elements can be broken down into 3 different types:

1. **Web Elements** (Text, Banners, etc)
2. **Analytic Elements** (BI Dashboards, SSRS, etc)
3. **Additional Elements** (Unrestricted HTML, Embedded URLS, etc)

After adding an element, select the element and a menu window will appear on the left side with options to change,
delete, and customize your element.

## Example: Creating a Page

Some of our most common elements are listed below

### Add a Hero Element

1. After naming your page, the first step in our sample page will be to add a Hero Element.
2. On the left menu window, select Hero Settings and select one of the template starter images.
3. Add in a Heading (e.g. ACME Sample Page) and Body Texts and Change Text Color if needed
4. Under Row Styles, update the Row Width to Full Width if the Hero Image should go across the full width.
   <img alt="page elements modal hero image highlighted" />

### Add a Dashboard to a Page

Dashboards can be either set up as standalone items or embedded within a page for greater customization on the wider page.

To add a Dashboard to a page, go ahead and add an element, select Analytic Elements and add your desired Dashboard to
replace the element.

**Note:** If the Analytics Element is unavailable to be selected, please add the relevant connection.

<img alt="Analytics Element modal" />

### Add a Text Field

<img alt="page elements modal text highlighted" />

Make updates to your text like bolding, italicizing, strike-through and many more options in the text editor.

<img alt="wysiwyg text editor" />

### Add Buttons

<img alt="page elements modal buttons highlighted" />

#### Buttons

Add externally linking buttons with the buttons component. Under Content Selection, link to different options like:

* Tableau/Power BI Dashboards
* Pages
* Files
* Content Tagged by Keywords
* External URLs
* Manual Selections (Combination of above options)

## Additional Options

Add more elements to customize and complete your page and then select save in the top right. Congrats your first page
has been created!

**TIP:** Clone your pages if you want to have a consistent design and save time when adding dashboards to separate pages


# Getting Started
Source: https://docs.curator.interworks.com/setup/trial_quick_start_guide/getting_started

Comprehensive guide to building your first analytics portal in Curator with step-by-step instructions.

Welcome to our comprehensive guide on building an analytics portal in Curator —a powerful tool that will empower you to
make data-driven decisions and unlock valuable insights within your organization. In today's data-driven world, the
ability to harness and interpret information is crucial for staying ahead of the competition and optimizing business
processes. Whether you're a seasoned developer or a novice enthusiast, this step-by-step tutorial will walk you through
the process of creating an analytics portal, integrating data sources, adding dashboards, and designing an intuitive user
interface. Get ready to transform your data into actionable knowledge and unleash the full potential of analytics with
our easy-to-follow instructions and best practices. Let's embark on this exciting journey of building your very own
analytics portal!

## First Steps

You’ve just reached out to an InterWorks Account Executive and have had a free trial set up.

You should have received an email that looks like this:

<img alt="trial screen" />

## Front End vs Admin

The front-end login will direct you to your portal and show you what your end users will see.  The default URL should
appear as `companyname.portals.interworks.com` and is fully customizable.

The admin login will lead you to administrative settings and the URL should appear as
`companyname.portals.interworks.com/backend`. The administrative settings are where you will build your analytics portal,
control your authentication, and manage your users.

Click on the Admin login and continue to the Admin Settings below.

## Admin Settings

After entering your username and password, you should enter a screen that looks like this:

<img alt="Curator home Dashboard" />

### Admin Menu Options

To the left, you’ll see the menu options. They are categorized into 4 sections.

1. **Content:** Pages, files and navigation
2. **Tableau:** Dashboards, filters and parameters
3. **Integrations:** Tableau Server connections and user group syncs
4. **Settings:** Curator settings, upgrades, security and users

### Update your Account Information and Password

In a Curator trial? Go ahead and navigate to the next page on Setting Up Your Portal. If you change your trial
credentials then we will not be able to easily troubleshoot issues for you!

If you are working on setting up your own instance, then go ahead and update your account information and password from
the defaults.

To do this, click on your icon on the top right, and update your First Name, Last Name, and Password.

<img alt="backend user account page" />

Click the save button to apply your changes.


# Setting Up Your Portal
Source: https://docs.curator.interworks.com/setup/trial_quick_start_guide/setting_up_your_portal

Initial setup and configuration guide to customize your Curator portal theme and frontend access.

Click on **Settings → Curator → Themes → Main Theme**

Click on the Main Theme **Global Theme** to edit our global theme

A live view of your Curator site will appear on the screen. We recommend logging into the front end on a separate screen
before making any changes so that you can see the changes you make on your Curator site. Keep in mind that your admin
account is separate from the front end accounts. Your credentials may be different based on how you choose to
authenticate your users. If you are not able to log into the front end then click **Settings** → **Security** →
**Authentication Settings** to see how your front end user credentials are being pulled in.

**Live preview:**

<img alt="Live preview" />

**On the left-hand side:**

* **Rename your Curator Site** (e.g. ACME Analytics Portal)

* **Upload a logo**
  * File formats supported: .jpg, .png, .gif, .svg
  * Curator is flexible with image sizes but we recommend wider over taller logos
  * Logo padding by entering pixels or percentages (Ex: 15px or 20%)
    * Tip: use negative padding if you are trying to increase the size of your image

* **Upload a favicon**- the icon used in the browser tab

**Favicon example:**

<img alt="favicon example" />

**Logo and Favicon Settings:**

<img alt="Logo and Favicon Settings" />

**Click Save button on the top right or press enter.**

## Updating the Navigation Bar

Click on the **Menu** tab

On the left-hand side you’l see various options.

* **Main Menu**
  * This lets you inter-change different main menu objects you may have created
  * For now, leave this as default
* **Navigation Type**
  * This lets you alter the location of the menu whether Top Navigation, Mega Menu or Side Navigation
* **Navigation Background Color**
* **Navigation Text Color**
* **Navigation Highlight Color**

There’s other navigation options as well below, but for now, we’ll stick to these main ones.

## Other Settings

There’s a whole host of other settings including:

**Brand**- Site Name, Site Logo and Icons

**Home**- Default home page settings

**Global**- Search, Alerts, Mobile Settings

**Fonts**- Customizable font options

**Menu**- Menu design settings

**Titles & Toolbar**- Pages titles and toolbar settings

**Dashboards**- Dashboard tabs

**Pages**- Tile styles, tutorial styles, button options, page margins

**Footer**- Footer options


# Accessing the Backend
Source: https://docs.curator.interworks.com/site_administration/accessing_the_backend

Learn how to access the backend of Curator for configuration and management tasks.

To access the backend administration area of your Curator instance, you will need to log in with an account that has
administrative privileges.  Typically this is created in the [initial setup](setup/installation/linux_installation) of
your Curator instance, or by an [existing administrator](site_administration/backend_administrators/overview).

### Logging into the Backend

1. Open your web browser and navigate to the backend URL of your Curator instance. This is usually in the format:
   `https://www.yourcuratorexample.com/backend`.

   <Frame>
     <img alt="Backend login screen" />
   </Frame>

2. Enter your administrator username and password in the login form.


# Data Manager Notifications 
Source: https://docs.curator.interworks.com/site_administration/admin_email_notifications/data_manager_notifications

Set up email notifications for Data Manager form submissions to stay informed of user data input and feedback.

To stay up-to-date on the data being submitted to Curator you can subscribe multiple users to receive email
notifications immediately after a form has been submitted.  These emails will also contain the data from the
form that has been submitted, allowing you to instantly review anything that comes in: whether it's a Contact
Us form, a Feedback form, or tracking your users favorite pizza, you'll know right away!

**NOTE**: Email configuration on Curator is required to use this email notification system.  If you have not
configured email on your Curator instance, please get in touch with your email administrator and [use these instructions](/setup/email/email_configuration)
to set up email.

## Enabling Data Manager Email Notifications

1. Login to the backend of your Curator instance (e.g. `https://www.curatorexample.com/backend` ).
2. Navigate to the **Data Manager** > **Data Groups** section from the left-hand menu.
3. Click on the Group you would like to add an email to.
4. Toggle ON the switch labelled "Email submissions"
5. This will display a repeater that you can add individual emails to.  Populate them one-at-a time.
6. Click the "Save" button.


# System Notifications 
Source: https://docs.curator.interworks.com/site_administration/admin_email_notifications/system_notifications

Configure automated email notifications for system alerts, issues, and maintenance updates to improve Curator instance management.

To ensure you are able to easily manage your Curator instance without having to check-in all the time, you
can subscribe to emails that generate from Curator's notification system.  These emails will scan Curator's
running list of issues, suggestions and to-do items that will ensure you have more visibility into your
Curator instance making management easier and increasing stability.

**NOTE**: Email configuration on Curator is required to use this email notification system.  If you have not(/setup/email/email\_configuration)
configured email on your Curator instance, please get in touch with your email administrator and [use these instructions](/setup/email/email_configuration)
to set up email.

## Enabling Email Notifications

1. Login to the backend of your Curator instance (e.g. `https://www.curatorexample.com/backend` ).
2. Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
3. Click on the "Notifications" tab at the top of the page.
4. Toggle ON the switch labelled "Send Curator Digests"
5. This will display scheduling options.  Choose your weekly/daily/monthly scheduling options, and whiter or
   not you'd like immediate notifications for new alerts.
6. Click the "Save" button.

## Subscribing to and Un-Subscribing from Email Notifications

1. Login to the backend of your Curator instance (e.g. `https://www.curatorexample.com/backend` ).
2. Navigate to the **Settings** > **Curator** > **Backend Administrators** section from the left-hand menu.
3. Click on the User whose settings you would like to change.
4. Un-check the "Subscribe to admin digest" checkbox.
5. Click the "Save" button.

   <img alt="Subscribe Image" />


# Overview
Source: https://docs.curator.interworks.com/site_administration/backend_administrators/overview

Manage backend administrator accounts, permissions, and access levels separate from Tableau Server users.

Backend Administrators accounts are separate from Tableau Server users and only exist on Curator.
Permissions can be customized for a backend user to allow for a range of access.
New permissions become available as you enable "Features" and must be enabled for older users if applicable.

**To manage backend users:**

1. If a backend user is unable to view menu items, it is possible they do not have the appropriate backend
   permissions. These permissions can be edited using the following steps. If the "Backend Administrators" menu
   item is not visible, it is likely that user does not have the necessary permissions. A backend admin with
   access to "Backend Administrators" will need to update the permissions for the other user.
2. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
3. Log in if prompted.
4. Click on **Settings** > **Curator** > **Backend Administrators** in the left navigation.
5. Click on the "New Backend User" button to create a new user, or click on an existing user to modify user details or permissions.

## SAML Integration

Curator can integrate backend users with the same SAML authentication that is being used on the front-end.
In order for this to work, set up your environment following the steps below:

1. Ensure your [SAML authentication](/setup/authentication/okta_saml)
   has been set up properly.
2. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
3. Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
4. Click on the **General** tab and expand the Security section.
5. Toggle the switch to enable "Force Backend Users to Login Via Frontend Authentication Forms" then click save

After this you can create users normally, and when they visit the backend of Curator they will be redirected
to log in via SAML, then re-routed to the backend.
*Note:* You can create backend users as normal following the steps above (including a password)
however users will not be able to log in via these credentials due to *Force Backend Users to Login Via
Frontend Authentication Forms* being enabled.
Only backend usernames matching frontend usernames will be able to access Curator's administrative interface.
Compare the two by checking the Frontend User section and Backend User section.

### Using Frontend Users as Backend Users

Curator can use the same Portal Settings as SAML to allow Frontend Users to login to the backend as well.
This will restrict backend users who don't have a corresponding frontend user.
In order for this to work, set up your environment following the steps below:

1. Ensure your chosen Authentication Type is set up properly, and sign in with a frontend user of your choice.
2. Create a backend user with account info that matches the frontend user you just used.
3. Sign out of both the frontend and the backend.
4. Login to only the frontend with the corresponding account.
5. Go to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
6. It should sign you in automatically.  You should then enable *Force Backend Users to Login Via
   Frontend Authentication Forms*.
7. This should enable frontend users to sign into the backend automatically with the same account.
   *Note:* In order to access the backend, a given frontend user will have to have a backend account manually made
   by an existing backend user.


# Password Reset 
Source: https://docs.curator.interworks.com/site_administration/backend_administrators/password_reset

Reset backend administrator passwords through self-service or administrative override when access is lost.

Forget your backend administrator password?

A Curator backend administrator user's password can easily be reset by other users who have Backend User access.

## No one left to reset your password?

If there is no one else with administrative access to the system, the account can also be reset using the steps below.

1. Connect to the server running Curator. (Windows: RDP, or with Linux: SSH)

2. Open a command prompt \[Windows Only, Linux will start in a command prompt.]

3. Change to the webroot directory where Curator is installed.
   Here are some examples:

   * **Windows (Apache: Standard):**

     ```Apache theme={null}
     cd C:\InterWorks\Curator\htdocs;
     ```

   * **Windows (IIS: Legacy):**

     ```Windows theme={null}
     cd C:\InterWorks\Curator\wwwdata;
     ```

   * **Linux:**

     ```Linux theme={null}
     cd /var/www/html;
     ```

4. Run "artisan" to reset the administrative user:

   ```PHP theme={null}
   php artisan winter:passwd
   ```


# Updating License Key 
Source: https://docs.curator.interworks.com/site_administration/license_key/updating_license_key

Update or add your Curator license key for new installations, migrations, or license renewals.

Adding or updating your license key is only required for new installations, or migrations that have failed to
carry over your license key.  Typical license keys are allowed on up to 3 instances so long as only one
instance is used for Production.  If you'd like to deploy multiple Curator sites, please talk to your Account
Executive about our Enterprise offering.

## How to Update your License Key

In order to add or update your license key, follow the steps below:

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).

2. Navigate to the **Settings** > **Curator** > **System Upgrade** section from the left-hand menu.

3. Click on the pencil "Update Key" link

   <img alt="update key link" />

4. Enter your license key and click "Save".


# Backend Logs
Source: https://docs.curator.interworks.com/site_administration/logging/database_logs

Database-stored logs accessible through the Curator backend including Usage Log, Event Log, Access Log, and Alert Log.

Backend logs are stored in the Curator database and can be viewed through the Curator backend interface. These
logs are designed for day-to-day monitoring and auditing by administrators who may not have direct server access.

## Usage Log

The Usage Log serves as an audit trail for your Curator instance, tracking who made what changes and when.
This includes configuration changes, content modifications, user management actions, and administrative
operations. The Usage Log is essential for compliance, security auditing, and troubleshooting issues
caused by configuration changes.

### Viewing the Usage Log

1. <BackendNavPath />
2. Use the filters to search for specific users, date ranges, or action types.

### Usage Log Retention

The Usage Log retention period can be configured in Portal Settings:

1. <BackendNavPath />
2. Find the **Usage Log Retention** setting.
3. Select the desired retention period (1 Month, 3 Months, 6 Months, or 12 Months).
4. Click **Save**.

Older usage log entries will be automatically purged based on this setting.

## Event Log

The Event Log records system events including errors, warnings, informational messages, and debug output.
This is the primary log for troubleshooting issues with your Curator instance.

<Tip>
  The Event Log is stored in the database and mirrors the file-based System Log. In rare cases where
  event log entries appear to be missing, the [System Log](/site_administration/logging/file_based_logs#system-log)
  may contain additional information.
</Tip>

### Debug Modes

Curator provides several debug modes that can drastically increase the amount of logging in the Event Log.
These modes are useful for troubleshooting specific integrations or features:

* [Tableau Debug Mode](/creating_integrations/tableau_connection/tableau_connection_troubleshooting#how-to-enable-debug-mode) - Detailed logging for Tableau Server/Cloud communication
* [Power BI Debug Mode](/creating_integrations/power_bi_connection/troubleshooting_power_bi_access#enable-debug-mode) - Detailed logging for Power BI integration
* **Cron Debug Mode** - Detailed logging for scheduled tasks
* And others depending on your enabled features

Debug modes should typically only be turned on temporarily while troubleshooting, as they can
significantly increase the volume of log entries.

### Viewing the Event Log

1. <BackendNavPath />
2. Click on any entry to view its details, including the full message and any associated context data.

### Download Debug Package

The Event Log page includes a **Download Debug Package** button that bundles various logs and system
information into a single downloadable archive. This package is useful when reporting issues to
InterWorks Support, as it includes:

* Recent event log entries
* System log files
* System configuration information

To download the debug package, click the **Download Debug Package** button in the toolbar on the Event Log page.

### Event Log Retention

The Event Log retention period can be configured in Portal Settings:

1. <BackendNavPath />
2. Find the **Event Log Retention** setting.
3. Select the desired retention period:
   * **Never (Manual)** - Logs are not automatically purged; use the Event Log interface to manually clear entries
   * **1 Week** - Entries older than 7 days are automatically purged
   * **2 Weeks** - Entries older than 14 days are automatically purged
   * **1 Month** - Entries older than 30 days are automatically purged
   * **3 Months** - Entries older than 90 days are automatically purged
4. Click **Save**.

When automatic purging is enabled, old event log entries are removed daily at 2:00 AM (server timezone).

## Access Log

The Access Log tracks backend administrator logins and activity. This is useful for security auditing and
compliance purposes.

### Viewing the Access Log

1. <BackendNavPath />
2. Review administrator access history including login times and IP addresses.

## Alert Log

The Alert Log aggregates recurring system alerts into a single, manageable view. Rather than creating
duplicate event log entries for the same recurring issue, the Alert Log consolidates these alerts and
tracks how many times they have occurred.

### Viewing the Alert Log

Alert Log entries are displayed in two locations:

1. **Status Page** - <BackendNavPath /> Here you can see active alerts alongside other system health information.

2. **Alert Log List** - <BackendNavPath /> This provides a detailed view where you can:
   * View all active, resolved, and suppressed alerts
   * See occurrence counts and timestamps
   * Mark alerts as resolved or suppressed
   * Clear alerts in bulk

### Alert Statuses

* **Active** - The alert is current and requires attention
* **Resolved** - The underlying issue has been addressed
* **Suppressed** - The alert has been acknowledged but hidden from the active view


# Server Logs
Source: https://docs.curator.interworks.com/site_administration/logging/file_based_logs

File-based logs on the Curator server including the System Log, PHP error log, and Apache error log.

Server logs are stored as files on the Curator server and require direct server or file system access to view.
These logs are typically used for deeper troubleshooting, especially when database connectivity issues prevent
backend access or when investigating web server configuration problems.

## System Log

The System Log is Curator's primary application log, recording system events, errors, warnings, and debug
information. This log mirrors much of the same information found in the
[Event Log](/site_administration/logging/database_logs#event-log), but writes directly to disk rather than
the database.

<Note>
  The System Log can be particularly useful when the Event Log is unavailable (such as during database
  connectivity issues) or when troubleshooting errors that may not appear in the Event Log. In some cases,
  database transaction rollbacks can prevent Event Log entries from being saved, but the corresponding
  System Log entries will still be present.
</Note>

### Log File Location

The default System Log locations are:

| Operating System | Default Path                                 |
| ---------------- | -------------------------------------------- |
| Linux            | `/var/www/html/storage/logs/`                |
| Windows          | `C:\InterWorks\Curator\htdocs\storage\logs\` |

<Note>
  These paths may vary based on your installation. Central Dispatch installations, custom installation
  directories, or different Windows drive letters will affect the actual location. The log files are
  always located in the `storage/logs/` directory relative to your Curator installation root.
</Note>

### Log File Format

By default, Curator uses daily log rotation, creating files named `system-YYYY-MM-DD.log`. For example:

* `system-2025-01-15.log`
* `system-2025-01-14.log`

### Log Rotation Configuration

File-based log retention is configured separately from the database log retention settings. The number of
log files retained and other logging behavior is controlled by the `config/logging.php` configuration file.

If your log files are consuming excessive disk space or not rotating properly, refer to the
[Updating Curator Logging](/server_management/system_administration/updating_curator_logging) guide for
configuration instructions.

## PHP Error Log

The PHP error log captures PHP runtime errors, warnings, and notices that occur outside of Curator's
application logging. This can include syntax errors, memory issues, and extension-related problems that
may prevent Curator from starting properly.

### Log File Location

The PHP error log location depends on your server configuration:

| Operating System | Default Path                                                 |
| ---------------- | ------------------------------------------------------------ |
| Linux            | `/var/log/php-fpm/www-error.log` or `/var/log/php/error.log` |
| Windows          | `C:\InterWorks\Curator\php_error.log`                        |

<Note>
  The actual location may vary based on your PHP and web server configuration. Check your `php.ini` file
  for the `error_log` directive to find the exact path.
</Note>

### Common PHP Errors

| Error Type  | Description                                                                                      |
| ----------- | ------------------------------------------------------------------------------------------------ |
| Fatal Error | Critical errors that halt script execution (e.g., missing required files, syntax errors)         |
| Warning     | Non-fatal issues that may indicate problems (e.g., missing optional files, deprecated functions) |
| Notice      | Minor issues that don't affect functionality (e.g., undefined variables)                         |

### Viewing PHP Configuration

To find your PHP error log location and other settings:

```bash theme={null}
# Linux
php -i | grep error_log

# Or check the loaded php.ini file
php --ini
```

## Apache Error Log

The Apache error log records web server errors, including failed requests, configuration issues, and
module errors. This log is essential for diagnosing issues with SSL certificates, URL rewrites, and
server connectivity.

### Log File Location

| Operating System | Default Path                                               |
| ---------------- | ---------------------------------------------------------- |
| Linux            | `/var/log/httpd/error_log` or `/var/log/apache2/error.log` |
| Windows          | `C:\InterWorks\Curator\libs\apache\logs\error.log`         |

<Note>
  The location varies based on your Linux distribution. RHEL/CentOS typically use `/var/log/httpd/`,
  while Debian/Ubuntu use `/var/log/apache2/`.
</Note>

### Apache Access Log

In addition to the error log, Apache maintains an access log that records all HTTP requests to the server.
This can be useful for:

* Tracking request patterns
* Identifying slow requests
* Debugging authentication issues
* Monitoring for suspicious activity

| Operating System | Default Path                                                 |
| ---------------- | ------------------------------------------------------------ |
| Linux            | `/var/log/httpd/access_log` or `/var/log/apache2/access.log` |
| Windows          | `C:\InterWorks\Curator\libs\apache\logs\access.log`          |

### Common Apache Errors

| Error                     | Description                                  |
| ------------------------- | -------------------------------------------- |
| 403 Forbidden             | Permission denied to access a resource       |
| 404 Not Found             | Requested file or page does not exist        |
| 500 Internal Server Error | Server-side error, often a PHP fatal error   |
| 502 Bad Gateway           | PHP-FPM or backend service not responding    |
| 503 Service Unavailable   | Server temporarily unable to handle requests |

## Troubleshooting Workflow

When troubleshooting issues with Curator, check logs in this order:

1. **Event Log** - Start with the backend Event Log for application-level errors
2. **System Log** - Check for entries that may not have been saved to the Event Log
3. **PHP Error Log** - Look for PHP runtime errors that prevent Curator from functioning
4. **Apache Error Log** - Check for web server configuration or connectivity issues

<Tip>
  When reporting issues to InterWorks Support, providing relevant excerpts from all applicable logs
  can significantly speed up diagnosis and resolution.
</Tip>


# Logging Overview
Source: https://docs.curator.interworks.com/site_administration/logging/logging_overview

Understanding Curator logging systems including usage logs, event logs, access logs, and alert logs.

Curator provides several logging systems to help administrators monitor, troubleshoot, and audit their Curator
instance. Logs are available through both the Curator backend interface and directly on the server file system.

## Types of Logs

Curator maintains several different log types, each serving a specific purpose:

| Log Type                                                                          | Purpose                                     | Access             |
| --------------------------------------------------------------------------------- | ------------------------------------------- | ------------------ |
| [Usage Log](/site_administration/logging/database_logs#usage-log)                 | Audit trail of who made what changes        | Curator Backend    |
| [Event Log](/site_administration/logging/database_logs#event-log)                 | Records system events, errors, and warnings | Curator Backend    |
| [Access Log](/site_administration/logging/database_logs#access-log)               | Logs backend administrator access           | Curator Backend    |
| [Alert Log](/site_administration/logging/database_logs#alert-log)                 | Aggregates recurring system alerts          | Curator Backend    |
| [System Log](/site_administration/logging/file_based_logs#system-log)             | Detailed application logs for debugging     | Server File System |
| [PHP Error Log](/site_administration/logging/file_based_logs#php-error-log)       | PHP runtime errors and warnings             | Server File System |
| [Apache Error Log](/site_administration/logging/file_based_logs#apache-error-log) | Web server errors and access information    | Server File System |

## Backend Logs vs Server Logs

**[Backend Logs](/site_administration/logging/database_logs)** are stored in the Curator database and accessible
through the Curator backend interface. These logs are designed for day-to-day monitoring and auditing by
administrators who may not have direct server access.

**[Server Logs](/site_administration/logging/file_based_logs)** are stored as files on the server and require
direct server or file system access. These logs are typically used for deeper troubleshooting, especially when
database connectivity issues prevent backend access or when investigating web server configuration problems.

## API Access

Curator provides API endpoints for programmatic access to log data. All API endpoints require a valid API key.
For general information about using the Curator API, see the
[Curator API Overview](/curator_api/getting_started/curator_api_overview).

### List Event Log

Returns event log entries with pagination support.

```
GET /api/v1/portal/listEventLog?apikey=YOUR_API_KEY
```

**Parameters:**

* `limit` (optional) - Maximum number of results to return (default: 1000)
* `offset` (optional) - Number of results to skip for pagination (default: 0)

### List Usage Log

Returns usage log entries with filtering options.

```
GET /api/v1/portal/listUsageLog?apikey=YOUR_API_KEY
```

**Parameters:**

* `limit` (optional) - Maximum number of results to return (default: 1000)
* `offset` (optional) - Number of results to skip for pagination (default: 0)
* `username` (optional) - Filter results by username
* `is_frontend` (optional) - Filter by frontend (`true`), backend (`false`), or both (omit parameter)

### List Alert Log

Returns alert log entries with filtering options.

```
GET /api/v1/portal/listAlertLogs?apikey=YOUR_API_KEY
```

**Parameters:**

* `limit` (optional) - Maximum number of results to return (default: 1000)
* `offset` (optional) - Number of results to skip for pagination (default: 0)
* `status` (optional) - Filter by status: `active`, `resolved`, `suppressed`
* `level` (optional) - Filter by level: `error`, `warning`, `info`

### Download System Log

Downloads the current system log file.

```
GET /api/v1/portal/downloadLog?apikey=YOUR_API_KEY
```

This endpoint returns the `storage/logs/system.log` file as a downloadable attachment.

## Best Practices

1. **Set appropriate retention periods** - Balance the need for historical data against database storage
   requirements. For most installations, 1-3 months of event log retention is sufficient.

2. **Monitor the Alert Log** - Regularly review the Status page to catch recurring issues early.

3. **Archive logs before purging** - If compliance requirements mandate long-term log retention, use the API
   endpoints to export log data before automatic purging occurs.

4. **Review Access Logs periodically** - Regular review of administrator access helps identify unauthorized
   access attempts.

5. **Check multiple log sources** - When troubleshooting issues, check both backend logs and server logs for
   a complete picture. The System Log may contain entries not present in the Event Log.


# Cache Warming 
Source: https://docs.curator.interworks.com/site_administration/performance/cache_warming

Configure cache warming to improve initial page load times for designated user groups through automated cache preloading.

Later page load times are much quicker than the first load due to caching. The "Cache Warming" feature allows
a group of users to have their cache warmed every hour. This improves their first page load and avoids that
initial long wait for the page to render when logging in.

## Enabling the Cache Warming Feature

1. Navigate to your Curator backend > Settings > Curator > Portal Settings > Features tab.
2. Enable the “Cache Warming” feature at the top of the Functionality section.
3. In the "Priority Group for Cache Warming" field, choose a Frontend Group with less than 200 members. The
   options should already be limited to applicable groups. For more information about creating Frontend Groups,
   visit [the doc](/users_groups/user_management/users_and_groups_overview).
4. Hit "Save."

## Notes

* Every hour the members of the chosen group will have their cache warmed. This is ran every hour in case
  another process has cleared the cache such as logging out or making a configuration change.
* The group has to contain less than 200 members because the process to warm the cache is intensive. Warming
  for more than 200 members might bog down the queue that runs scheduled processes, preventing other important
  functions to run.


# Performance Diagnostics
Source: https://docs.curator.interworks.com/site_administration/performance/performance_diagnostics

Guide for collecting system performance data to help the Curator support team diagnose and resolve slow performance issues.

When experiencing slow performance with Curator, collecting detailed system information helps the support team identify
the root cause. Follow these steps to gather the necessary diagnostic files.

## Step 1: Collect Server Performance Data

Connect to your Curator server via SSH (Linux) or RDP (Windows), then run the performance script for your operating
system to generate a comprehensive report of your server's configuration, performance metrics, and usage statistics.

<Tabs>
  <Tab title="Linux Servers">
    ```bash theme={null}
    curl -o /tmp/curator_server_info.sh "https://api.curator.interworks.com/scripts/curator_server_info.sh";
    chmod +x /tmp/curator_server_info.sh && /tmp/curator_server_info.sh
    ```
  </Tab>

  <Tab title="Windows Servers">
    ```powershell theme={null}
    Invoke-WebRequest -Uri "https://api.curator.interworks.com/scripts/curator_server_info.ps1" -OutFile "$env:TEMP\curator_server_info.ps1";
    PowerShell -ExecutionPolicy Bypass -File "$env:TEMP\curator_server_info.ps1"
    ```
  </Tab>
</Tabs>

<Note>
  The generated file will contain system information including server configuration, performance metrics,
  and usage statistics needed for performance analysis.
</Note>

## Step 2: Access API Keys Settings

<BackendNavPath />

<Note>
  You'll use the **REST API Explorer** section on this page to generate diagnostic endpoint URLs.
</Note>

## Step 3: Collect Portal Info Endpoint

1. Under **REST API Explorer**, use the dropdowns to select:
   * **API Section:** Portal
   * **API Method:** Info
2. Click the **REST API Access URL** link to open the endpoint in a new tab.
3. You should see raw JSON data.
4. Right-click on the page and select **Save As** to save the output to a file.
5. Save the file as `info.json` (save as JSON format, **not PDF**).

## Step 4: Collect Portal PHPInfo Endpoint

1. Return to the API Keys page and change the **API Method** dropdown to **PHPInfo** (keep Portal selected).
2. Click the **REST API Access URL** link to open the PHPInfo page.
3. Right-click on the page and select **Save As** to save the output to a file.
4. Save the file as `phpinfo.html` (save as HTML format, **not PDF**).

## Send Files for Analysis

Email the following files to the Curator support team for analysis:

* Server performance data (markdown file from Step 1)
* `info.json` (from Step 3)
* `phpinfo.html` (from Step 4)
* Feel free to include screenshots of any relevant system information.

The support team will analyze these files and provide specific recommendations to improve your system's performance.


# Troubleshooting Load Times 
Source: https://docs.curator.interworks.com/site_administration/performance/troubleshooting_load_times

Diagnose and resolve slow loading issues using Curator debug mode for performance optimization.

When determining the root-cause of latency issues on Curator, using the debug mode for Curator is the fastest
way to rule out a number of issues that may be causing slow loading times.  This can come from the location
of your servers and/or networking issues, custom code, internal Curator issues or slow Dashboard load times.
Curator's debug mode provides the Curator team with enough information to know where to start looking when
addressing these issues.  Follow the steps below to view Curator's debug data, and download the debug file
and send it to the Curator support team if you have any concerns.

## Enabling Debug Mode

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
3. Click on the "General" tab at the top of the main page content.
4. In the "Debug" section, turn ON *Enable Frontend Debug* and click the "Save" button.

## Using the Debug Mode

1. Append `?debug=1` to the end of any url (unless there is already a `?` in the url, in which case append `&debug=1`)\*
2. Click the arrow on the bottom tray to expand the debug menu, then navigate between the tabs to view the debug output.
   \*NOTE: If you are debugging slow login times, be sure to logout first, and then add the debug parameter to
   your URL (e.g. `http://curatorexample.com/backend`?debug=1)

## Capturing Debugging Results

1. Once you have followed the **Using the debug mode** steps above, you can download the results of your
   debugging session using the export button on the debugging tray:

   <img alt="debug download" />

2. This will output a `.iw` file which you can send to Curator support for assistance with slow load times.


# Web Accessibility
Source: https://docs.curator.interworks.com/site_administration/standards_compliance/web_accessibility

Scan and evaluate Curator portal for WCAG web accessibility compliance using browser extensions and tools.

This document provides instructions on how to scan your Curator portal for compliance with the Web Content
Accessibility Guidelines (WCAG)

## Prerequisites

Install the [WAVE Accessibility Extension for Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/wave-accessibility-tool/).

Similar extensions may exist in other browsers, but those are outside of the scope of this document.

## What to Scan

There are 3 main sections you'll need to check about when scanning your Curator portal.

1. Login Page
2. Global Structure
3. Page Content

### Login Page

Depending on which authentication type your Curator portal uses, you will likely need to scan the login page
and any related pages shown during the authentication process.  If you utilize a third-party authentication
source, any accessibility issues found with it will need to be fixed within that third-party product.

### Global Structure

Once authenticated to Curator, there are elements shared across all pages, such navigation, search, theme,
logo, and footer.  Any issues found with these elements will be found on each page you test, so it's worth
tracking these separately.

### Page Content

Each page on your site is by nature unique in some aspect.  Whether a page has simple static text, images,
embedded content, or multiple elements of varying content types, each page will need to be checked
individually to verify that all of the content on the page meets accessibility standards.

It should be noted that any issues found with embedded content will need to be addressed in their source
system.  For instance, if you determine there are accessibility issues with a Tableau Dashboard, you'll need
to correct those issues within your Tableau workbook and then republish it.

## How to Scan

Loop through each section and page listed above in Mozilla Firefox.  For each one, right-click on the page
and select **WAVE this page**.

As of the time of this writing, a pane will show up in your browser that lists errors, alerts, contrast
errors, and other elements that were checked for WCAG compliance.  Address the errors and contrast errors
first by clicking on the **Details** tab.  After addressing those, then focus on the alerts.

You should be able to click on each issue to show the element in question and a description of the issue.  If
the element is covered by the WAVE pane, you may need to toggle the styles off.

Most of the issues you may encounter will likely be:

* **Missing alternative text for images:** Each image should have some sort of alternative text to describe
  the image for people with visual impairments.  For instance, an image may just be a logo, but it also might
  be a chart with important information being conveyed.
* **Missing title/label text for page elements:** Some elements on a page, such as buttons, form fields, etc.
  require title text (often displayed as tooltips) or an explicit label in order for people to understand their
  use.  For instance, have you ever tried to use an app where the buttons only show an icon you've never seen
  before?  This issue is exacerbated if you must consume the entire page through a screen reader.
* **Low contrast:** Certain visual impairments make it difficult to discern elements that are too similar
  with respect to contrast.  For instance, try reading light grey text on a white background.
* **Tab order:** The order that elements are highlighted when tabbing through the site makes a big difference
  of how usable or frustrating your site is.  Imagine that your mouse stopped working and you had to use your
  site with nothing more than your keyboard's tab key.  This is how many people must navigate the web.

## Implementation vs. Core Issues

Curator provides a content management platform.  Accessibility issues may exist in the core Curator
functionality or in your actual content or implementation.  Issues found related to your content or
implementation will need to be fixed in your portal.  The Curator development staff make a good faith effort
to routinely check that core features meet accessibility standards, but issues may still slip through.  If
you find an accessibility issue in a core feature, please report it to Curator support so we can address it
in a future version.


# Third Party Cookies 
Source: https://docs.curator.interworks.com/site_administration/user_notifications/third_party_cookies

Configure third-party cookie warnings and troubleshoot embedded visualization login issues in Safari browsers.

Embedding visualizations within Curator requires third party cookies to be enabled.  By default Chrome and
Firefox allow this but Safari does not.  When you encounter this issue,
**the embedded visualization (e.g.Tableau) login prompt might continue to appear inside of Curator even after
successfully logging in to Curator**.

## Warning Users About Third-Party Cookie Embedding Issues

Since your Curator users may not be aware this setting is preventing them from being able to use the embedded
view in Curator, you can enable an alert that tells them if this is preventing them from being able to
seamlessly log in to their embedded visualization.  To enable this warning follow the steps below:

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`) and log in if prompted.
2. Navigate to **Settings** > **Curator** > **Portal Settings**.
3. Click on the "Features" tab.
4. Scroll down to the "Usability" section and enable *3rd Party Cookies Enabled Check*.

## Information on How to Enable Third-Party Cookies

See the steps here to allow cookies on devices that use Safari:

* [Unblocking cookies on iOS](https://support.apple.com/en-us/HT201265)
* [Unblocking cookies on MacOS](https://support.apple.com/guide/safari/manage-cookies-and-website-data-sfri11471/mac)


# Favorites
Source: https://docs.curator.interworks.com/site_content_design/content_discovery/favorites

Enable user favoriting functionality to personalize homepages and prioritize frequently accessed content.

Curator has the ability to mark dashboards as favorites.  Favorited dashboards will show up first on the home page once
the user logs in.

This functionality requires any authentication method other than "Pass-Through".  See the [Authentication Methods](/setup/authentication/overview)
section for more information.

If you have a [Tableau Connection](/creating_integrations/tableau_connection/creating_a_connection)
the favorites will also synchronize across to Tableau Server/Cloud.

You can also display the number of favorites a Dashboard has. This number shows up in both the Dashboard action-buttons
area when viewing a Dashboard and on the homepage when showing Dashboard tiles.

## Enabling Favorites

1. <BackendNavPath />
2. Find the "Favorites" setting and toggle it on.
3. Be sure to save your changes.

## Favoriting a Dashboard

1. Navigate to the frontend of the system (e.g. `http://curatorexample.com`).
2. Log in if prompted.
3. Navigate to the desired Dashboard by using the navigation menu.
4. Click on the star icon at the top right portion of the screen. Normally this is displayed on the right side of the
   title bar in the Dashboard.

## Showing the Number of Favorites

1. <BackendNavPath />
2. Find the "Favorites" setting and toggle it on.
3. Be sure to save your changes.


# Featuring Content 
Source: https://docs.curator.interworks.com/site_content_design/content_discovery/featuring_content

Promote and highlight important content using featuring options to increase visibility and user engagement.

The landing page typically shows an assortment of many different dashboards from the site. These displays will show
favorited and featured dashboards first before others. While Favorited dashboards is a feature that is driven by the user
we provide the ability to bump certain dashboards to the top using the Feature switch (requires a tiled homepage). The
dashboards that are shown will only ever be dashboards the user has permission to see.

***To feature a Dashboard:***

1. While editing the Dashboard, click on the "Misc" tab.
2. Scroll to the "Discovery" section.
3. Toggle on the switch labeled "Featured".
4. Click the "Save" button.


# Hidden Content
Source: https://docs.curator.interworks.com/site_content_design/content_discovery/hidden_content

Control visibility by hiding dashboards and other content from tiles, explorer, and search results while maintaining direct access and navigation visibility.

## Hidden and Hidden from Search Toggles

You can now control where content appears throughout Curator using the **Hidden** and **Hidden from Search** toggles.
These toggles are available for most content types and allow fine-grained control over how users discover content.

### Availability

| Content Type          | Hidden |  Hidden from Search  |
| --------------------- | :----: | :------------------: |
| File                  |   Yes  |          Yes         |
| Page                  |   Yes  |          Yes         |
| Menu                  |   Yes  | No *(not available)* |
| Power BI Dashboard    |   Yes  |          Yes         |
| Power BI Report       |   Yes  |          Yes         |
| Tableau Dashboard     |   Yes  |          Yes         |
| Tableau Metrics       |   Yes  |          Yes         |
| Sigma Workbooks       |   Yes  |          Yes         |
| ThoughtSpot Liveboard |   Yes  |          Yes         |
| ThoughtSpot Search    |   Yes  |          Yes         |

***

### Behavior

#### Hidden

* Removes the item from **all content displays**, including tiles and Explorer tiles.
* Prevents the content from appearing in featured or related content sections.

#### Hidden from Search

* Excludes the item only from **Curator search results**.
* The content continues to appear in other locations, such as tiles, related content, and Explorer tiles.
* This setting is **not available for Menus**.

***

### Where to Find the Hidden Settings

| Content Type              | Navigation Path                     |
| ------------------------- | ----------------------------------- |
| **File**                  | Content → File → General            |
| **Page**                  | Content → Page → Page Details       |
| **Menu**                  | Content → Navigation → Menu         |
| **Power BI Dashboard**    | Power BI → Dashboards → Discovery   |
| **Power BI Report**       | Power BI → Reports → Discovery      |
| **Tableau Dashboard**     | Tableau → Dashboards → Discovery    |
| **Tableau Metrics**       | Tableau → Metrics → Discovery       |
| **Sigma Workbooks**       | Sigma → Workbooks → Discovery       |
| **ThoughtSpot Liveboard** | ThoughtSpot → Liveboard → Discovery |
| **ThoughtSpot Search**    | ThoughtSpot → Search → Discovery    |

***

### How to Update Visibility Settings

1. Edit the desired content item (for example, a Dashboard, Report, Page, or File).
2. Navigate to the section shown in the table above.
3. Locate the **Hidden** and **Hidden from Search** toggles.
4. Use the toggles:
   * **Hidden** — hides the item from all content listings including menus.
   * **Hidden from Search** — hides the item only from search results.
5. Click **Save** to apply your changes.

***

### Notes

* Hidden items are still accessible through direct URLs for users with the correct permissions.


# Keywords 
Source: https://docs.curator.interworks.com/site_content_design/content_discovery/keywords

Assign and manage keywords for content organization and improved search and filtering capabilities.

Keywords can be associated with dashboards, pages, individual files, and menu items. These keywords can be utilized in
the Search and Explorer feature when pulling in results, as well as when determining which content to display on a page.
A keyword page can be set up that will pull in all content tagged with the keyword.

***To create a new keyword***

1. Navigate to the **Content** section in the backend of your Curator instance.
2. Select **Keywords** from the Content dropdown.
3. Click the **New Keyword** button.
4. Assign a title to the new keyword (this will be the keyword that is created)
5. From here you can check the box next to an existing piece of content to associate it with that keyword. This new
   keyword will now be available in the keywords list when creating new pieces of content as well.

***To link a keyword to a Dashboard:***

1. While editing a Dashboard, click on the **Misc** tab.
2. Scroll to the **Discovery** section.
3. Select the **Search Keywords** field.
4. Type in the text for the first keyword.
5. Check the box next to the desired keyword.
6. Click the **Save** button at the top-right corner of the page.

The above process is used for linking keywords to pages and files as well. To link a keyword to a menu item, first
create the menu item, then link it to the desired keyword in the **Keywords** section.


# Search
Source: https://docs.curator.interworks.com/site_content_design/content_discovery/search

Enable and configure search functionality to help users discover and locate content across the Curator portal.

The frontend search functionality helps explore your Curator content or access specific content directly without
navigating through the menus.

## Enabling Search

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`) and log in if prompted.
2. Navigate to *Settings > Curator > Portal Settings > Features > Usability*
3. Switch the toggle *Search* on to enable search

*Note: The search toggle enables the search prompt shown in the menu. If enabled, you can also add a search bar to your
page by using [Page Builder](/site_content_design/pages/pages_overview)*

### Content that is searched

The search considers the following components to generate the search results:

1. Titles
2. Descriptions
3. Keywords
4. From version 2023.02.15 onwards: Text content on pages

*Note:* Search results reflect all permissions set on the BI Platforms or by using [Restrict Access](/site_content_design/menus/restrict_access).
In case you have added dashboards or built content that should not be visible in search results, enable the *Hidden*
toggle. To hide dashboards navigate to the *Misc* tab and then in the *Discovery* section you find the toggle.
To hide other types of content, the toggle is in the details pane.

## Changing Search Result Display

Search results show the following components:

* Thumbnail (default if none was created/ set)
* Title
* Description (if existing)
* Keywords (if existing and matching the search term; max. 2 - more are indicated by an ellipsis)
* If the result content is favorited or not

**From release 2023.02.15 onwards**: The description is only shown for Pages if there is a match in it. Otherwise, Pages
will always show a preview of their content (with or without a match).

We highlight the match from your search term in the title, description, and keywords in bold font.

## Styling Search

Brand your search with the following settings

* Add a custom search icon (Available since 2022.11.30)
* Navigate to *Settings > Curator > Themes > Styles > Logo and Icons* to add your own search icon
* Style the colors of your search results
* Navigate to *Settings > Curator > Themes > Search Options* (in versions until 2022.09.28: *Settings > Curator > Portal
  Settings > Styles > Search Options*) to set the background and text color
* Navigate to *Settings > Curator > Themes > Styles > Miscellaneous > Navigation Highlight Color* (in versions until
  2022.09.28: *Settings > Curator > Portal Settings > Styles > Miscellaneous > Navigation Highlight Color*) to set the
  text color on hover

## Algorithm Details

Our search applies a fuzzy search algorithm, so search results are intentionally loose so as to help users find the
content regardless of minor typos or alternate spellings.

<img alt="search result example!" />


# Thumbnail Preview Images
Source: https://docs.curator.interworks.com/site_content_design/content_discovery/thumbnail_preview_images

Set up thumbnail and preview images for content to enhance visual discovery and user engagement.

When viewing a list of dashboards, Curator has the ability to display a custom preview of the Tableau Server view as a
thumbnail image.

These thumbnails can either be set manually while creating or
[editing a Dashboard](/site_content_design/pages/pages_overview) or the system will attempt to automatically grab the
thumbnail from the Tableau Server if the Dashboard is created without one.

Once the Dashboard is created you can manually refresh the thumbnail by pressing the Refresh Thumbnail button.

***To refresh the dashboards thumbnail:***

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Tableau** > **Dashboards** section from the left-hand menu.
3. Click on the "New Dashboard" button or select an existing Dashboard.
4. In the Misc tab, expand the Look/Feel section and click the "Refresh Thumbnail" button.

You can manually upload a thumbnail on the Dashboard edit page.

***To manually upload a thumbnail:***

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Tableau** > **Dashboards** section from the left-hand menu.
3. Click on the "New Dashboard" button or select an existing Dashboard.
4. In the **Misc** tab, expand the Look/Feel section and use the Thumbnail Image form to upload your custom image.
   *Note: You will need to click the "X" in the bottom-right corner to remove an existing image.*

***To set a global default thumbnail:***

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
3. Click on the **Home** tab and expand the Tile Type section.
4. Use the "Custom Default Thumbnail" form to upload your custom image.
   *Note: You will need to click the "X" in the bottom-right corner to remove an existing image.*
5. If you wish to use this image for *all* dashboards, disable *Refresh Dashboard Thumbnails* under **Settings** >
   **Curator** > **Portal Settings** > **Features** tab.

Curator also has a feature to enable nightly refreshes of the site's Dashboard thumbnails. This helps to keep the thumbnail
up to date with any changes while also saving time from manually updating every Dashboard thumbnail.

***Enabling or Disabling Refresh Dashboard Thumbnails:***

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
3. Click on the **Features** tab at the top of the main page content.
4. Toggle the switch to enable/disable *Refresh Dashboard Thumbnails* setting under the Functionality section and click
   the "Save" button.


# Files
Source: https://docs.curator.interworks.com/site_content_design/files/files

Manage file uploads and downloads with group-based access controls and search functionality for document management.

The system supports adding downloadable files and linking to them using the regular navigation menu process. File access
can be restricted based on Groups from the Tableau Server. Search keywords are also provided to help narrow down your
options when searching.

***To manage files:***

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`) and log in if prompted.
2. Navigate to **Content** > **Files** section from the left-hand menu.
3. Add, modify, or delete files as desired.

## Hidden Settings

In Curator, there are two general use-cases for uploading files: **Images** and **Documents**.  By default, the
file-features are configured for Images since this is a much more common scenario.  See configuration items below that
describe treating files as images or documents:

**Hidden**: For images, for example a logo, it may cause confusion to surface the logo in search or inside of a
["recently viewed" Tiles](/site_content_design/pages/tiles) page-element.
In this scenario, hiding the file ensures the logo only shows up on the page you explicitly added it to.
However, you may want to show a PDF inside of the search results, or add it as a link to a tile selection.
*In this case, make sure to un-check the Hidden toggle on the edit-file page*.


# Loading Screens
Source: https://docs.curator.interworks.com/site_content_design/loading_screens/loading_screens

Configure custom loading screens and progress indicators to improve user experience during content loading.

Loading screens can be used to show text or animations while a Dashboard is loading.

***To create a loading screen:***

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Content** > **Loading Screens** in the dropdown.
4. Click the "New Loading Screen" button.
5. Enter the title of the loading screen in the title field.
6. Enter the content of the loading screen in the content field. This field allows for fully formatted content,
   including images, links, etc.
7. Click the "Create" button.

***To select a default loading screen for all dashboards:***

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Navigate to the **Settings** > **Curator** > **Themes** section from the left-hand menu.
4. Click on the "Loading Screens" tab at the top right.
5. Select the desired loading screen in the "Default Loading Screen" field.
6. Click the "Save" button.

***To display the Dashboard thumbnail while loading for all dashboards:***

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on "Settings" link in the left-hand menu.
4. Navigate to the **Settings** > **Curator** > **Themes** section from the left-hand menu.
5. Click on the "Loading Screens" tab at the top right.
6. Toggle on "Show Dashboard Thumbnail During Load". Note the "Custom Loading Screen" option and this option
   can not both be enabled at the same time.
7. Click the "Save" button.

***To set a loading screen for a specific Dashboard:***

1. While editing the Dashboard, click on the "Misc" tab.
2. Scroll to the Look/Feel section.
3. Select the desired loading screen.
4. Click the "Save" button.

***To view the loading screen:***

1. Navigate to the frontend of the system (e.g. `http://curatorexample.com`).
2. Log in if prompted.
3. Navigate to the desired Dashboard by using the navigation menu.
4. The configured loading screen will be shown while the Dashboard is loading.


# Managing Menus
Source: https://docs.curator.interworks.com/site_content_design/menus/managing_menus

Create, edit, and organize menu structures to provide intuitive navigation throughout your Curator portal.

You can only display *one* top-level menu item at a time. It is recommended that you nest your entire navigation under the
default 'Main Menu' parent-item or create a new "Dropdown Placeholder" if you wish to manage multiple menus - often this
approach is used to organize unreleased content via menus. Group Overrides allow you to select one different 'Main Menu'
parent item per group.\*

***To Select the Global Navigation:***

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Navigate to the *Curator* > *Settings* > *Portal Settings* section from the left-hand menu and click the "Styles" tab.
3. Expand the "Menu Options" section and select your menu using the *Main Menu* dropdown.

***To Select a Group Override  Navigation:***

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Navigate to the *Curator* > *Settings* > *Users* > *Frontend Group Overrides* section from the left-hand menu.
3. Click on the Group Override you would like to modify or click the "New Group Override" button at the top to create a
   new override.
4. Click the "Styles" tab,
5. Choose your overridden Main Menu *Main Menu* dropdown.


# Menu Items
Source: https://docs.curator.interworks.com/site_content_design/menus/menu_items

Configure individual menu items including links, labels, icons, and access permissions for effective site navigation.

***To Create a Navigation menu item:***

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Navigate to the *Content* > *Navigation* section from the left-hand menu.
3. Expand/collapse the navigation using the carets to find the menu you would like to edit - or click "New Menu Link" to
   create a new item.
4. From the Create New / Update Link page, you can create/modify your new menu item as you'd like.
5. Once your menu items have been created, visit the Reorder page by navigating to the *Content* > *Reorder Navigation*
   section from the left-hand menu.
6. Click and hold the dots ⠀ to drag/drop your menu items and reorder them as you'd like

***To Bulk Create Tableau Dashboards as Menu Items:***

1. Navigate to *Tableau > Dashboards* on the backend
2. Select the Dashboards you would like to create as menu items
3. Click Create Menu Items button

***To Bulk Create Power BI Dashboards as Menu Items:***

1. Navigate to *Power BI > Dashboards* on the backend
2. Select the Dashboards you would like to create as menu items
3. Click Create Menu Items button

***To Bulk Create Power BI Reports as Menu Items:***

1. Navigate to *Power BI > Reports* on the backend
2. Select the Reports you would like to create as menu items
3. Click Create Menu Items button

***Link Types:***

**Dashboard**
The Dashboard type is used to link to existing dashboards.  See the [Embedded Tableau Server Views](/embedding_using_analytics/tableau_dashboards/adding_a_dashboard)
section for more information.

**Data Manager**
The data manager type is used to link to a front-end enabled data manager page. See the [Data Manager](/embedding_using_analytics/data_manager/data_manager_basics)
section for more information.

**Dropdown Placeholder**
The dropdown placeholder type is used to create a grouping or level in the multilevel navigation. Doesn't contain a link
and only displays text.

**File**
The file type links to a file that has been uploaded to the site. See the [File](/site_content_design/files/files)
section for more information.

**Keyword**
The keyword type is used to create a link to a listing of content tagged with a specified keyword.

**Menu Page**
The menu page type allows you to enter the name of a menu item. The menu link will then take you to a page that displays
all of the dashboards directly under (one menu level) the specified menu item. Similar to a keyword page.

**Project**
The project type is used to mark the spot within the navigation where Dashboards will be synced to from the chosen Project.
These Dashboards will be created and configurable in the Dashboards area of the Backend. Note that the project link will
place all Dashboards as siblings to itself. More info on this can be found [here](https://interworks.com/blog/morr/2017/11/22/automatically-sync-your-dashboards-portals-tableau/).

**Projects**
The projects type will automatically find all the available Workbooks from the specified Site for the logged in user and
places links to view them within Curator in the navigation, organized beneath dropdown placeholders named after the Project
they came from. This will not add Dashboards to the Curator backend as opposed to the project type. Note: if the user has
access to many Workbooks (Site Admin or Server Admin) this will generate many links.

**Page**
The page type is used to link to a static page.  See the [Pages](/site_content_design/pages/pages_overview)
section for more information.

**Tag**
The tag type is used to automatically create links to any Tableau Server workbooks which have been tagged with a specific
name. See the [Tagged Workbooks](/site_content_design/menus/tagged_workbooks)
section for more information.

**Web Edit**
The web edit type is used to create a link to the Tableau Server web editor for a specified Dashboard.

**Workbook**
The workbook link type imports in all of the dashboards from a workbook as menu items. It will also automatically pull in
future dashboards added to the workbook.

**Workbooks**
The workbooks link type imports in all of the dashboards from all workbooks in a project as menu items. It will also automatically
pull in future dashboards added to the project.

**Custom URL**
This link type is used to create a link to a custom URL. Extra options are provided to customize this like opening the link
in a new tab or the same tab.

**External URL**
This link type is used to create a link to an external URL. This is a slimmed-down version of the Custom URL.

*NOTE: If you are adding a link that is external to your Curator instance, ensure that you prepend the proper protocol to
your URL. For example, to add InterWorks.com use `http://www.interworks.com`, or `https://www.interworks.com`.*


# Restrict Access
Source: https://docs.curator.interworks.com/site_content_design/menus/restrict_access

Control menu visibility and access permissions based on user groups and roles to secure content appropriately.

When you add a Dashboard or other content brought in from connected integrations like Tableau, Curator will inherit the
security settings from those integrations. However, you may want to override those source-systems or you may want to prevent
users from seeing content that exists solely within Curator - for example, restricting access to a specific
[page](/site_content_design/pages/pages_overview).  With **Restrict Access**
you can override inherited security settings when necessary, offering you maximum flexibility over the visibility of content.

## Enabling Restrict Access

1. On the backend of Curator, navigate to the **Content** > **Reorder Navigation** section from the left-hand menu.
2. Find the menu link you'd like to restrict access to and click the pencil/edit icon - or click the "New Menu Link"
   button to create a new menu item.
3. Toggle the Restrict Access to ON to display a list of [groups](/users_groups/user_management/users_and_groups_overview)
4. Select the groups you'd like to grant access to
5. Save the menu item

You can then confirm the restrict access is enabled on the Reorder Navigation page by hovering over the lock icon and
seeing the phrase "Restricted Access based on Group Membership"

**Tableau admins** automatically have access to all Tableau-connected content in Curator.  Restrict access overrides
these permissions, so admins will need to be in one of the selected groups to see the content within the menu.


# Site Switcher
Source: https://docs.curator.interworks.com/site_content_design/menus/site_switcher

Enable users to easily navigate between multiple Curator sites or environments through integrated site switching functionality.

Some Tableau Servers have different sites with different dashboards associated with those sites. The site switcher allows
a frontend user to filter the dashboards in the navigation by Tableau Site from a dropdown.

***To enable:***

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Settings** > **Curator** > **Portal Settings** in the left-hand menu.
4. Click on the "Features" tab at the top of the main page content.
5. Scroll to and expand the "Usability" section and then toggle on "Site Switcher".
6. Click "Save".


# Tagged Workbooks
Source: https://docs.curator.interworks.com/site_content_design/menus/tagged_workbooks

Organize and display workbooks in menus using tags to create dynamic, categorized content navigation.

The system can automatically create dashboards for any workbooks that have a matching tag on the associated Tableau Server.
It will poll the Tableau Server every 10 minutes to check for any newly tagged workbooks which match a tag navigational
item (see the [Navigation](/site_content_design/menus/managing_menus) section
for more information). A new Dashboard and corresponding navigation link will be created for each view in any workbooks
it finds.

Links to any new dashboards created through this process will be placed in the same location as the tag navigational item.
However, these links can be safely moved or deleted if desired.

This functionality requires that the REST API is enabled
(see the [Enabling the REST API](/creating_integrations/tableau_connection/creating_a_connection)
section for more information).


# Org Chart
Source: https://docs.curator.interworks.com/site_content_design/org_chart/org_chart

Create and display organizational charts with hierarchical employee structure and reporting relationships visualization.

The Org Chart provides a visual representation of the organizational structure within a company or organization. It
outlines the hierarchy of positions, roles, and reporting relationships.

## Creating an Org Chart

### Preparing the data

The Curator Org Chart is built using the
[Data Manager](/embedding_using_analytics/data_manager/data_manager_basics)
for its underlying data. You'll need to create an Attribute for each column in the employee data you'll be adding or
importing. It's important the names of the Attributes match the names of the columns from your data if you'll be
importing from another system. Once you have created the Attributes, you'll need to create a Data Manager Group and
select the Attributes you've just created. Finally, you can use the "Batch Import" button on the Data Manager > Manage
Data page in your Curator backend. There, you can upload a CSV with all of your employee data.

### Creating the Org Chart

Navigate to the Data Manager > Org Chart area of your Curator backend. There, you can click "New Org Chart" and fill
out the form. Below are descriptions of each field:

* **Title**: This is the title for your Org Chart. The primary place this will be displayed is in the browser tab
  displaying the Org Chart on the frontend.
* **Data Manager Group**: This is the Data Manager Group we created and imported the data to.
* **Employee Name Attribute**: This is the Attribute name that corresponds to the column in the data for the employee’s
  name. This will be displayed on the employee’s node in the chart.
* **Employee ID Attribute**: This is the Attribute name that corresponds to the column in the data for the employee’s
  ID. This column and the Supervisor ID column will be how the chart knows where to put each employee in the tree.
* **Supervisor Name Attribute**: This is the Attribute name that corresponds to the column in the data for the
  employee’s supervisor’s name.
* **Supervisor ID Attribute**: This is the Attribute name that corresponds to the column in the data for the
  supervisor’s ID. This column and the Employee ID column will be how the chart knows where to put each employee in the
  tree.
* **Role Name Attribute**: This is the Attribute name that corresponds to the column in the data for the employee’s
  role at the company.
* **Who is the top node for the Org Chart?**: Enter the name here for who is at the top of the Org Chart (typically a
  CEO). This needs to match the Employee Name Attribute value of your highest ranking employee.
* **Slug**: This is the bit at the end of the URL for the page where the Org Chart will be displayed. This will be
  automatically generated based on the Title field, but you can change it if you’d like.

### Customize the Org Chart Design

Below the primary configuration for the Org Chart are many fields that can be used to customize the look of the Org
Chart. Here are descriptions of each option in the Design tab:

* **What shape should the nodes be?**: You can choose a circle or a rectangle. The rectangle allows you to show more
  information in each node.
* **How should nodes be named?**: You can choose to show the employee’s name or, if you’d like to be a bit more
  confidential, the employee’s role at the company on the node in the chart.
* **Specify any additional attributes to show in each node**: This is where we can add more information to the
  rectangular nodes. *(This only appears if the node shape is set to rectangle.)*
* **Show employee headshot?**: This will tell the Org Chart you have URLs in your data and would like to show those
  images.
* **Employee Headshot Attribute**: This is the Attribute name that corresponds to the column in the data for the
  employee’s headshot URL. Users will be able to flip the switch in the top right of the chart to toggle headshots and
  the employee info. *(This only shows if the “Show employee headshot?” switch is on.)*
* **Show tooltip on hover with additional employee details?**: This will tell the Org Chart you’d like to show a
  tooltip when hovering over a node. It’s very useful if you’re wanting to display employee details without making the
  chart look too busy.
* **Attributes to show in tooltip**: Add any Attributes here you’d like to appear in the tooltip. *(This only appears*
  *if the tooltip option is flipped on.)*
* **Color employee nodes by attribute?**: This allows adding a visual way to differentiate each employee. The most
  common use cases are coloring by employee department and full-time vs. part-time. A legend will be shown in the
  top-left corner of the chart designating what each color means.
* **Specify any additional attributes for the search bar to parse (default is only employee name)**: This adds
  Attributes/columns that the search will parse. Sometimes you don’t know the employee’s name but know their department,
  so this improves parsing a large org chart.

### Frontend Org Chart Editing

While the Org Chart is more for reporting pre-determined organization data, we do have some light editing tools. Here
are descriptions of each option in the Editing tab:

* **Which Frontend Groups can edit?**: You don’t want just anyone to be able to edit or delete employees from your Org
  Chart, so you can choose specific Frontend Groups to give these privileges to. There will be an Edit button and a
  Delete button that become visible on each node. The Edit button will show a pop-up window with the employee’s relevant
  details, which can be changed and saved. The Delete button will give a confirmation message before sending the node
  into oblivion. *Note: The Edit and Delete buttons are omitted from the top node because changing those details could*
  *easily break the underlying data and leave the Org Chart blank.*
* **Fields to show in edit Form**: By default, only the name, role and supervisor Attributes are shown in the edit
  form. You can use this field to add additional Attributes to the form.
* **PDF Download**: Sometimes the browser’s print functionality doesn’t quite hit the mark with visualizations like
  this, so we’ve added a PDF download option for a much more visually appealing download of the chart.
* **PDF Download Watermark**: The data being revealed on the Org Chart could be sensitive, so it’s important to make it
  known this shouldn’t be shared. Whatever text is added to this field will be slapped over the chart in the PDF.
* **CSV Download**: This will generate a CSV containing data for the visible nodes, as opposed to the full data the Org
  Chart is running on. The button for this, as well as the PDF download, will be in the top-right corner of the Org Chart
  page.


# Blogs
Source: https://docs.curator.interworks.com/site_content_design/pages/blogs

Create and manage blog-style pages for news updates and educational content with feed-based display options.

When using Curator, you may need to notify your audience about updates related to news in your business or may need to
help break down important concepts, and allow those updates to be highlighted in a specific area of your site.  If you
find yourself needing to really this type of information on your Curator pages, then the Blog flag is extremely useful.

All Curator pages can be marked as a "blog" allowing you to filter a subset of pages in a feed-type of display in the
various elements available on the page builder, whether you want to display blog pages in a list, a feed, tiles or any
other format.  While the page is not flagged as a blog, it will only be accessible via the menu or directly from the URL,
allowing you to have pages that are in a draft state priori to a go-live date.

**To mark a page as a blog:**

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Content** > **Pages** section from the left-hand menu.
3. Find the page in the list view or click "New Page" to create a new page.
4. At the bottom of the page, enable the "Blog" toggle, and save the page


# Box Embedding 
Source: https://docs.curator.interworks.com/site_content_design/pages/box_embedding

Embed Box file sharing and collaboration content directly into Curator pages using embed widgets.

## Getting the Embed Widget

1. In your web browser, navigate to your box environment from which you wish to embed a folder within Curator.
2. In the row of your folder, hover over the right-hand-site, click on the ***More options*** ellipsis (**...**).
3. Hover over ***More actions***.
4. Click on ***Embed Widget***.
5. Click on ***Copy*** and all necessary code will be copied

## Adding Box to a Curator Page

Start by either creating a new page or editing an existing Curator page from Curator's backend.  Click on the plus (+)
icon in the Page Builder preview pane to add a new blank element to the page.  This blank element is a placeholder that
you'll use to embed the desired Box folder by following these steps:

1. Hover your mouse over the blank element and click on the pencil icon.
2. Click on the **Additional Elements** tab at the top of the pop-up.
3. Select the **BOX Cloud** option.
4. The pop-up will close and the Box settings will appear on the left.  Paste the widget you copied above into the
   **Box Embed Code** field.  You should see the Page Builder preview update to show the Box folder or login screen.
5. Adjust the height as you need it by using the ***Height*** field in the Box Settings.
6. Once you're happy with the layout, click on the **Save** button.


# Explorer 
Source: https://docs.curator.interworks.com/site_content_design/pages/explorer

Interactive tile layout element with search and filtering capabilities for dynamic content discovery and navigation.

Explorer is an interactive and dynamic tile layout element that can be added in the Page Builder. It provides users the
ability to search and filter displayed content. Filters utilize keywords to get the desired results. This layout is best
used when you have a lot of content on your site as the tiles are small.

## To add a Explorer page element

1. Navigate to the **Content** section in the backend of your Curator instance.
2. Select **Pages** from the Content dropdown.
3. Click the **New Page** button or edit an existing one.
4. Add a new row element and/or click the **Edit Content** button (pencil) icon of a row element.
5. In the element popup select Explorer under the Web Elements tab.

After this your Page will display the Explorer element. Since this uses the Keywords functionality please review the
subject [here](/site_content_design/content_discovery/keywords).


# Forms
Source: https://docs.curator.interworks.com/site_content_design/pages/forms

Build custom web forms for data collection, feedback, and user requests using Curator Data Manager capabilities.

Whether it's storing small data-sets from around your business, getting valuable feedback from your users, or creating a
simple contact-us / request access form Curator's data manager has the web form building capabilities you need.

## Creating a Form

You can create a form on the backend using Curator's Data Manager feature.  See here for more information on how to
create forms and fields in our [Data Manager Basics](/embedding_using_analytics/data_manager/data_manager_basics)
section.

## Adding a Form to a Page

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Content** > **Pages** section from the left-hand menu.
3. Find the page you want to add your form to from the Pages list or click "New Page" to create a new page.
4. Add a new element to your page, and when the modal pops-up, click the "Analytic Element" tab and select the "Curator
   Data Group" option.
   <img alt="Curator Data Group element" />
5. In the Page Styles section on the left-hand side, you can choose to either embed the Form Only for receiving inputs,
   or you can add the Table view to allow your end-users to see the data that has already been added.

## Forms and Tableau Dashboards on Pages

Some Tableau Dashboards can pull their results from Form submissions. In cases like this it can be useful to have the
Tableau Dashboard refresh it's data after a Form submission. Curator will automatically refresh all Tableau Dashboards
that are on a page with a Form if a Form submission occurs.


# Looker Embedding
Source: https://docs.curator.interworks.com/site_content_design/pages/looker_embedding

Embed Looker reports and dashboards directly into Curator pages for integrated analytics viewing.

## Getting the Report URL

In your web browser, navigate to the Looker report you wish to embed within Curator.  Once the report has loaded, copy
the link in the URL bar of your browser.

### Adding Looker to a Curator Page

Start by either creating a new page or editing an existing Curator page from Curator's backend.  Click on the plus (+)
icon in the Page Builder preview pane to add a new blank element to the page.  This blank element is a placeholder that
you'll use to embed the desired Looker report by following these steps:

1. Hover your mouse over the blank element and click on the pencil icon.
2. Click on the **Analytic Elements** tab at the top of the pop-up.
3. Select the **Looker** option.
4. The pop-up will close and the Looker settings will appear on the left.  Paste the link you copied above into the
   **Report URL** field.  You should see the Page Builder preview update to show the Looker report.
5. Once you're happy with the layout, click on the **Save** button.

<img alt="GIF illustrating the steps written above" />


# Manual Embed - (iFrames) 
Source: https://docs.curator.interworks.com/site_content_design/pages/manual_embed_iframes

Embed content from external websites and legacy systems using iFrames and custom embed code.

Sometimes you need to go beyond Curator's standard embedding capabilities and embed content from your unique or legacy
systems into Curator. That's where Curator's **Manual Embeds** feature comes to the rescue! We'll walk you through the
steps to seamlessly embed any other website, using iFrames, into your Curator pages!

**Important Considerations:**

* While you're adding Manual Embeds, keep in mind that the embed code should come from trusted sources. This will help
  you avoid any security risks or funky user experiences.
* Some systems might require some extra configuration or customization to display perfectly within an iFrame. Check out
  the documentation or support resources for the specific system you're embedding to ensure compatibility and the best
  possible display.
* Don't forget to pay attention to the dimensions and aspect ratio of the iFrame content. We want it to fit smoothly
  within your Curator page. Adjust those dimensions if needed, so you avoid any cropping or weird distortions.

## Adding a Manual Embed to a Page

1. Login to the backend of your Curator instance (e.g. `https://www.curatorexample.com/backend` ).
2. Navigate to the **Content** > **Pages** section from the left-hand menu.
3. Find the page you'd like to add your Manual Embed to, or click the "+ New Page" button.
4. On the page builder editor, click the section you'd like to add your embed to, or click the "+" icon on the page
   builder page to add a new section.
5. Click the "Additional Elements" tab from the "Add Element" popup and select the **Embed** content type.
6. Choose the dropdown option that best fits your need from the options below
   * iFrame: For use when pasting in a simple URL (e.g. `https://mycuratorexample.com/embed`)
   * Embed Code (HTML): For use when copying embed code from another website - this will be in HTML and can be
     identified by searching the copied code for `</iframe>` - if this string is found in your code it means you are using
     an iFrame to embed.
7. Once you've pasted the correct information in, click "Add"


# Pages Overview 
Source: https://docs.curator.interworks.com/site_content_design/pages/pages_overview

Introduction to creating and managing custom pages within Curator using the page builder for flexible content organization and presentation.

When adding content from your analytics environments, Curator will automatically create default template pages for you.
These can be accessed via the edit page of those individual pieces of content.

However, you may want to create something more tailored for your users to showcase certain content.  In this case, using
Curator's page builder allows a huge amount of flexibility for creating and styling your pages, while still allowing you
to link to content that is both secured to the user viewing the page as well as relevant based on their recent browsing activity.

## Building Pages in Curator

### To create a page in Curator

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Content** > **Pages** section from the left-hand menu.
3. Click "New Page" to create a new page.

### To add content to your page

1. Hover over the element on the page-preview on the right-hand side of the page builder and click the "edit" icon
2. Choose the content you'd like to add to your page

## To style content to your page

1. Click on an item on the page-preview on the right-hand side of the page builder.
2. This will expand a side-panel over the menu on the left-hand side of the page that will give you styling controls
   related to the active content.

## Page Security

Pages will first inherit any [Restrict Access](/site_content_design/menus/restrict_access)
permission that have been set on the individual menu item.  Continuing from there, the permissions will apply according
to the sections below.

Page security for embedded-content was added in the 2024.03-02 release, all prior releases have no security applied
when loading embedded content for pages.  The following section only applies to 2024.03-02 and later.  Proceed to the
**Security for Pages Without Embedded Content** section if you are on an earlier version.

### Security for Pages With Embedded Content

When embedding analytic-content into pages, for example a Dashboard, Curator will check permissions on that embedded
piece of content.  If the user does not have access to the embedded content it will deny them access, routing them to
the
[Access Denied page](/site_content_design/user_notifications_and_email/error_pages).

This applies to both menu items as well as loading the page directly.

#### Disabling Embedded Content Security

To disable the security check in versions released after 2024.03-02:

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Click on **Settings** > **Curator** > **Portal Settings** in the left-hand menu.
3. On the **General** tab, scroll down to the **Security** section and expand it.
4. Toggle the switch **Disable Page Element Security Checks** to ON and click the "Save" button.

### Security for Pages Without Embedded Content

Content that is *linked* on a page, for example Tiles, will run through permissions checks while loading the page.
check when rendering the tiles.  So if a page contains a *Tile* that links to a Dashboard that a user does not have
access to the user will simply not see the tile.  However, for pages that have content *embedded* in them, see the
**Security for Pages With Embedded Content** section above.


# SSRS Embedding
Source: https://docs.curator.interworks.com/site_content_design/pages/ssrs_embedding

Embed SQL Server Reporting Services (SSRS) reports directly into Curator pages for integrated reporting.

## Getting the Report URL

In your web browser, navigate to the SSRS report you wish to embed within Curator.  Once the report has loaded, copy the
link in the URL bar of your browser.

### Adding SSRS to a Curator Page

Start by either creating a new page or editing an existing Curator page from Curator's backend.  Click on the plus (+)
icon in the Page Builder preview pane to add a new blank element to the page.  This blank element is a placeholder that
you'll use to embed the desired SSRS report by following these steps:

1. Hover your mouse over the blank element and click on the pencil icon.
2. Click on the **Analytic Elements** tab at the top of the pop-up.
3. Select the **SQL Server Reporting Services (SSRS)** option.
4. The pop-up will close and the SSRS settings will appear on the left.  Paste the link you copied above into the
   **Report URL** field. You should see the Page Builder preview update to show the SSRS report.
5. Once you're happy with the layout, click on the **Save** button.


# Text Element
Source: https://docs.curator.interworks.com/site_content_design/pages/text_element

WYSIWYG text elements for adding formatted text, links, and images to your Curator pages.

## Adding a Text Element

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Content** > **Pages** section from the left-hand menu.
3. Find the page you want to add your form to from the Pages list or click "New Page" to create a new page.
4. Add a new element to your page, and when the modal pops-up select the "Text" option.
   <img alt="Curator Text element" />
5. You will then be prompted with the WYSIWYG editor, where you can add and format your text, add links, and images.
   <img alt="Curator Text element" />

## Page Variables

Page variables can be used to display important user or session based information on pages.

* `{{ full_name }}` : Displays the full name for the logged in user
* `{{ first_name }}` : Displays the first name for the logged in user
* `{{ last_name }}` : Displays the last name for the logged in user
* `{{ username }}` : Displays the Curator username for the logged in user
* `{{ original_username }}` : Displays the original username for the logged in user


# Tiles
Source: https://docs.curator.interworks.com/site_content_design/pages/tiles

Create visual tile layouts to organize and link content from multiple source systems with automatic permission handling.

Creating a central location to link all of the content users have access to is a breeze with Curator's tiles feature.
You can bring in content that pulls across different source-systems, from Curator's page system, as well as adding in
your own custom links to send users to other useful websites.

NOTE: All tiles, unless specifically overridden, will respect the permissions of what the user has access to.
If there are any group restrictions on menu items, those will be taken into account.
Second, it will check the source-system permission (e.g. Tableau, Power BI, etc.).
Then finally will look at the individual item's permission (e.g.
[Restrict Access](/site_content_design/menus/restrict_access) on a file).

## Tile Types

You can quickly add tiles into your page in a few clicks.  To give you more insight into what each of these tiles allow
you to display for your users, we've provided a brief description of each section below:

**Dashboards**
Dashboard Tiles allow you to link to analytic content that you have brought into Curator.  This links from any source-system,
be it Tableau, Power BI, or ThoughtSpot - anything that Curator supports natively!  This runs through a permissions check
to make sure the user has access, and can be sorted to your preference.  The default sorting after your preference will
be to place user-favorited dashboards first, then order them by visit, and finally by alphabetical order.

**Pages**
Page Tiles allow you to link to other pages you have created on Curator.  You may want to embed a "contact us" page,
create a feedback form, link to other detail pages, or maybe even use our explorer feature to allow users to browse
through all the content they can see.  Whatever you want to create within Curator, Page Tiles can specifically link to
that content.

**Menus**
Menu Tiles repeat the same-level menu items as the menu you've linked to.  So if you want to display all the top-level
menu items someone has access to, you can add in a link to your highest menu item, and it will display all the links
one level below the link you've selected.  It's an easy way to allow people a more visual exploration while still
maintaining the guardrails of your neatly maintained menu system.

**Keyword Pages**
Keyword Page Tiles pull in content of any sort so long as it has been associated with a specific keyword on Curator.
Linking this content together allows you to logically group things at a topic level that may not make sense to be grouped
in other ways.  It unifies areas that cut across your site in a categorically succinct manner.

**External URL**
External URLs can be created in the Navigation section, and allow you to link to other websites.

**Media**
Media brings in any content that has been uploaded to Curator's Files system.  This allows you to link to specific files
(e.g. PDFs) that are hosted on Curator. Files can have security applied directly to them without needing to be added to
the menu.

**External (RSS) Feeds**
Allows you to bring in external and RSS feeds as tiles, that serve as links to the host page.

**Custom Mix**
For when you want bring in anything and everything someone has access to.  This combines all the tile types listed here
and displays content based on the criteria you've chosen.

**Managed Instances (Enterprise Only)**
If your users have access to multiple Curator sites that you've deployed through Central Dispatch, this tile-type will
allow them to view all the different Curator sites they have access to.

## Tile Style

**Tile Style** can be selected on the Page Styles menu when tiles are selected in the Page Builder. The tile style
selection includes shapes in Square, Small Horizontal, Boxy, Circle, and Hex.

Tile styles in Page Builder is independent of the Global tile styles in Portal Settings. You are able to have different
tile styles for different Pages, but the same Dashboards have to have the same tile style.

## Tile Thumbnails

**Tableau Dashboards** can generate thumbnails automatically and they will be updated regularly if you want them to.
Yet, this might display data that you do not want to show on a thumbnail. To show a generic thumbnail for this Dashboard:

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Navigate to the Tableau > Dashboards section from the left-hand menu.
3. Click on the Dashboard you want to change the thumbnail for.
4. Open the Misc tab and expand the Look/ Feel section.
5. Delete the auto-generated thumbnail.
6. Use the Upload button to upload your custom thumbnail.
7. Click Save.

**Pages**' thumbnails default to the global default thumbnail unless you set one on the Page itself:

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Navigate to the Content > Pages section from the left-hand menu.
3. Click on the page you want to change the thumbnail for.
4. Scroll down, under the Preview window.
5. Use the Upload button for the Thumbnail Image to upload your custom thumbnail.
6. Click Save.

**Files & Keywords**' thumbnails default to the global default thumbnail unless you set one on the Page itself:

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Navigate to the Content > Files or Keywords section from the left-hand menu.
3. Click on the file or keyword you want to change the thumbnail for.
4. Use the Upload button for the Thumbnail Image to upload your custom thumbnail.
5. Click Save.

Most of the **Navigation** items can have an icon associated with them. If there is no additional explicit option to
upload a thumbnail for it, the default thumbnail will be the icon. To set the icon or thumbnail for a navigation item:

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Navigate to the Content > Reorder Navigation section from the left-hand menu.
3. Click on the pen icon (edit button) of the navigation item you want to change the icon or thumbnail for.
4. Use the Upload button for the Icon or if existent the Thumbnail Image to upload your custom icon/ thumbnail.
5. Click Save.

If you want to customize the **default thumbnail** to show for any content type that does not have a thumbnail set:

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Navigate to the Settings > Curator > Themes section from the left-hand menu.
3. Click on the Pages tab in the middle of the screen.
4. In the new left-hand-side menu, Pages Options, expand the Tile Styles section.
5. Use the Upload button for the Custom Default Thumbnail to upload your default thumbnail.
6. Click Save.

   ***2024.02-02 Default Thumbnail update***

   The default tile was updated in the 2024.02-03 release to a more modern design.  If you wish to re-upload the old file,
   you can right click the file link to save this image: [Old Default Thumbnail](/assets/images/site_content_design/pages/old_default_thumbnail_file.png).


# User Customized Metrics 
Source: https://docs.curator.interworks.com/site_content_design/pages/user_customized_metrics

Enable users to personalize their landing pages with custom dashboard selections displayed in a grid layout.

User Customized Metrics gives your users the ability to customize their landing page with their desired dashboards that
will be displayed in a grid layout. For the best experience it’s recommended to create smaller dashboards or Dashboard
cards, for example this could be Dashboard with your KPIs.

**To enable User Customized Metrics:**

1. Navigate to the **Content** section in the backend of your Curator instance.
2. Select **Pages** from the Content dropdown.
3. Click the **New Page** button or edit an existing one.
4. Add a new row element and/or click the **Edit Content** button (pencil) icon of a row element.
5. Select **User Customized Metrics** under the Web Elements tab.
6. You may wish to tweak some settings by expanding **Custom Metrics Settings** on the left:

* **Use Keywords** allows you to pre-filter the list of dashboards displayed by a specific keyword. This ensures
  your users can only pick from dashboards tagged with that keyword. To find out more about keywords [click here](/site_content_design/content_discovery/keywords).
* **Default Dashboards** allows you to pre-select the Dashboard which are displayed to your user by default.

**To select your Customized Metrics on the frontend:**

1. Navigate to the page which has the User Customized Metrics Element.
2. Login if prompted (you must be logged in).
3. Click on the **Edit button** on the top right.
4. Drag your desired Dashboard(s) from **Available Dashboards** to **Selected Tiles**.
5. Click on **Save**.


# YouTube Embedding
Source: https://docs.curator.interworks.com/site_content_design/pages/youtube_embedding

Embed YouTube videos directly into Curator pages for educational content and multimedia presentations.

## Getting the Video URL

In your web browser, navigate to the YouTube video you wish to embed within Curator.  Once the video has loaded, copy
the link in the URL bar of your browser.

### Adding a YouTube video to a Curator Page

Start by either creating a new page or editing an existing Curator page from Curator's backend.  Click on the plus (+)
icon in the Page Builder preview pane to add a new blank element to the page.  This blank element is a placeholder that
you'll use to embed the desired YouTube video by following these steps:

1. Hover your mouse over the blank element and click on the pencil icon.
2. Click on the **Additional Elements** tab at the top of the pop-up.
3. Select the **YouTube** option.
4. The pop-up will close and the YouTube settings will appear on the left.  Paste the link you copied above into the
   **Video URL** field.  You should see the Page Builder preview update to show the YouTube video.
5. Once you're happy with the layout, click on the **Save** button.

<img alt="GIF illustrating the steps written above" />


# Curator Styles
Source: https://docs.curator.interworks.com/site_content_design/theme/curator_styles

Customize the visual appearance of your Curator portal with built-in styling options and theme configurations.

Curator allows controls related to your site design across all content types, however having a central place to modify
styles that will impact every page your user visits allows you to create a standard and consistent brand.  The live
preview makes this even easier, allowing you to change the configuration of options in the Curator Styles section while
previewing those changes (across device sizes too).  It's best to look through all of the options, and toggle each
selection on or off.  Deleting any content that is input into a text box will revert it back to the default setting.
Feel free to play around and revisit your design as much as you'd like!

## Creating a new Theme

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to:
   * **Settings** > **Curator** > **Theme** section from the left-hand menu. Select the Theme you'd like to update.
   * *Pre 2022-11-30:* **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
3. Click through each tab, expand the sections on the left-hand navigation to see more advanced styling options.
   Changing the the selections will update the live preview on the screen and will show the pending changes.
4. Once you have configured your theme the way you would like, click "Save" to apply your changes to this Theme.

## Applying a Theme to your Site

This feature is only available for Curator instances running 2022-11-30 and above.

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
3. On the "General" tab, use the "Global Theme" dropdown to change the theme applied to your Curator site.  If you would
   like to apply your Theme to a specific group of users, see the
   [Group Override instructions](/site_content_design/theme/group_overrides).
4. Click "Save" to apply your changes.

## Defaults when Using Multiple Themes

Every new theme leverages out-of-the-box defaults for each field if they're left unchanged. These defaults will also be
leveraged if the field is blank, no color is selected, or the "Default" option is selected depending on if it's a text
input, color picker, or dropdown, respectively. You also have the option to have a theme default to the values chosen
in your Global Theme (which is chosen in **Settings** > **Curator** > **Portal Settings**). This is particularly useful
if you have [Group Overrides](/site_content_design/theme/group_overrides) that
need to use themes that look exactly like the Global Theme with just a few minor changes. To enable this you can switch
on **Use Global Theme for Defaults** in any theme that isn't the Global Theme.


# Group Overrides
Source: https://docs.curator.interworks.com/site_content_design/theme/group_overrides

Apply group-specific theme customizations and styling overrides to provide tailored experiences for different user groups.

When using Curator, you may want to surface different content to different users.  You can achieve this using Curator's
Group Overrides.  Whether you want to show a homepage to a certain subset of users or you want to change the colors and
logos for a specific client, you can use groups (synced from Tableau or your SAML provider) to modify the look and feel
of your Curator site. For additional info, view our
[Group Overrides blog post](https://interworks.com/blog/morr/2018/04/09/portals-tableau-new-feature-spotlight-overriding-settings-tableau-group/).

## To Create a new Group Override

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Users** > **Frontend Group Overrides** section from the left-hand menu.
3. Click the 'New Group Override' button at the top.
4. From the Frontend Group list, select the group you would like these settings to apply to.
5. Give the group override a title, if a user has access to multiple groups, this will be the title that is displayed
   that allows them to switch between group overrides\*.
6. Modify the settings you wish to override for this group using the tabbed form fields at the bottom of the page, and
   once you're done, click Save.

## Using the Theme-switcher

If you are logged in to the front-end of Curator and your user is a member of multiple groups, by default you will see
a dropdown in your menu that allows you to view either the "Default" setting\*, or individual Themes.  The experience
when selecting these themes will depend on whether or not "Use Global Theme for Defaults" has been enabled for the theme.

\***Group Override Inheritance - Use Global Theme for Defaults Enabled**
When "Use Global Theme for Defaults" is enabled, and your use is a member of multiple groups, they will see all settings
that have been saved inside of Themes across those groups.

For example, if there are two groups:

* Group 1 - Green menu, default/no bg color
* Group 2 - Default/no bg menu color, black background

"Default" would show you a Green menu and black background, whereas selecting Group 1, you will see a Green menu and the
remainder of settings will show the default settings, and the same goes for Group 2 where you will see a default menu
color but the background of the site will be black.

\***Group Override Inheritance - Use Global Theme for Defaults Disabled**
If you create a  group override with the Global Theme Default disabled, this group override will remain distinct and
separate from the inheritance flow, only allowing you to see this if:

1. You are a member of that group and *only* that group.
2. You are a member of multiple groups, and have chosen that group from the Theme-switcher dropdown on the front-end of Curator.

## Disabling Group Switching

By default, users who have access to multiple group overrides will be allowed to cycle through the group overrides they
belong to.  Group Overrides are inherited by creation-date, with the oldest group-override taking the highest priority.
If you do not want to give users access to changing this to view distinct Themes on a per-group basis you can disable
that dropdown using the steps below:

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
3. Click on the 'Features' tab and expand the 'Usability' section at the bottom of the page.
4. Toggle **Group Override Selector** to the off position.
5. Save your settings.


# Homepage
Source: https://docs.curator.interworks.com/site_content_design/theme/homepage

Configure and customize the homepage layout, content, and design elements to create an engaging user landing experience.

Curator allows you to create unique web pages using
[Curator's page builder](/site_content_design/pages/pages_overview) to customize
the layout and content of any page on your site.  This is particularly useful when creating your homepage to ensure
users start off with all the information they need.  By default, Curator comes installed with some sample pages, but if
you no longer have that page or want to start by creating a new page, follow the
[steps to create a page](/site_content_design/pages/pages_overview) first.  Once
your page has been created use the steps below to set that page as your homepage.

## Setting the Homepage

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to **Settings** > **Curator** > **Theme** section from the left-hand menu. Select the Theme to apply the
   new homepage to.
3. Click on the 'Home' tab at the top of the page.
4. Change the Homepage Type dropdown to **Page**.
5. Change the Homepage Page dropdown to the page you'd like to set as your homepage.
6. Click "Save" to apply your changes.


# Page Meta Titles (SEO)
Source: https://docs.curator.interworks.com/site_content_design/theme/page_meta_titles_seo

Configure page meta titles and SEO metadata to improve search engine visibility and social media sharing.

Meta titles play a crucial role in the realm of Search Engine Optimization (SEO) and website usability. When displayed
in search engine results or shared links via internal communication tools (e.g. Slack) meta titles serve as the first
impression of your content.

You can take advantage of Curator's meta title controls impacting the the meta titles for your entire site by creating
a site name, specifying a title on the home page.
*All other meta titles will be auto-generated based on the title of the content (e.g. Page Title, Dashboard Title).*

All Meta titles for individual pages will have this structure:

`Page Meta Title | Site Meta Title`

So for example, if we were to call our site "My Website", and create a page with a title of "My Page" that would result
in

`My Page | My Website`

## Changing the Site Meta Title

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to **Settings** > **Curator** > **Themes** section from the left-hand menu.
3. Click on the Theme you'd like to modify.
4. Click on the **Brand** tab and change the *Curator Site Name* field to show the Site Name you'd like to appear on
   every page.
5. Be sure to save your Theme settings.

## Changing the Homepage Page Meta Title

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to **Settings** > **Curator** > **Themes** section from the left-hand menu.
3. Click on the Theme you'd like to modify.
4. Click on the **Home** tab and change the *Curator Home Title (Meta tag)* field to show the Homepage Name you'd like
   to appear on the home page.  If you would like to have no homepage title, simply delete any text in this field.
5. Be sure to save your Theme settings.

## Changing the Page Meta Title for an individual Page

When creating a page, or analytic element (e.g. Tableau Dashboard), the Page Meta title will draw from the name of the
content given on the edit page.  The only exception to this is the homepage Meta Title which will override the page
being displayed on the homepage.  If you wish to change a Page's Meta title you must change teh Page's title itself.

## SEO Considerations

Remember that meta titles play a crucial role in SEO and determining how your website appears in search engine results.
Make sure to use relevant keywords, keep the titles concise (usually between 50-60 characters), and create compelling
titles that entice users to click through to your site. Also, check your website regularly to ensure the meta titles
are accurately representing the content and objectives of your pages.


# Titles and Toolbars
Source: https://docs.curator.interworks.com/site_content_design/theme/titles_and_toolbars

Customize page titles, toolbar elements, and navigation components to match your brand and improve user experience.

The title and toolbar location, for most options, are dependent upon one another for the styling of your site.  While
titles help your users understand where they are and what they are looking at,  Toolbars contain the action buttons that
allow your users to interact with, filter, export and even send scheduled emails of your embedded visualization.

**NOTE**: As of now, all actions are available for Tableau Dashboards. There is no feature parity for Power BI or ThoughtSpot.

## Title & Toolbar Location (examples below)

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`) and log in if prompted.
2. Navigate to **Settings** > **Curator** > **Themes** from the left-hand menu and select the Theme you'd like to update\*.
3. Chang the "Title and Toolbar Location" dropdown to modify the layout, using the live-preview to view your pending
   changes.
4. Click "Save" to apply your changes.

## Title Settings

Titles can be controlled globally, or by content type.  Follow the steps below to show or hide titles:

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`) and log in if prompted.

2. Navigate to **Settings** > **Curator** > **Themes** from the left-hand menu and select the Theme you'd like to update\*.

3. Click on the \**Titles & Toolbar* tab and expand the "Title Display" section.

4. Choose from one of the options below

   * Hide All Titles: Hides all titles - this will ensure that no titles display across your entire site, regardless of
     the page-type.
   * Hide Dashboard Titles: This allows control for titles on the page level, and automatically displays them (except for
     the homepage).  This setting is typically most useful if your dashboards already contain titles.
   * Hide Page Titles: This ensures all titles are displayed on Dashboard pages, but will not show up on Pages created with
     the page-builder.

5. Click "Save" to apply your changes.

Prior to the 2022-11-30, these setting can be found under:
**Settings** > **Curator** > **Portal Settings** > **Styles tab**.  Title and Toolbar location are found in the
"Menu options" section, global title settings are found in the the "Global Settings" section, Dashboard title settings
are under the "Dashboard Styles" section, and Page title settings are under the "Page Styles" section.

## Title & Toolbar location examples

### Top Navigation and Mega Menu

#### Top of page: Top Navigation and Mega Menu

Have your title at the top of a page and the toolbar situated right beneath it. With this option, you can further adjust
your toolbar in the *Toolbar Styles* and *Toolbar Colors* sections.

<img alt="Top Navigation and Top of page Title/Toolbar Location" />

* *Hide Action Titles* - If enabled the toolbar buttons will not show any titles on a desktop screen. Hovering over a
  button will show the title to clarify functionalities.

* *Action Button Size* - Choose between large, medium, and small-sized buttons to save space or prevent wrapping. The
  default size is large.

#### Inside of top nav: Top Navigation and Mega Menu

The title and toolbar move inside the navigation bar along the top of the screen. They are placed between the menu items
and the user menu. Make sure you have enough space to have everything readable.

<img alt="Top Navigation and Inside of top nav Title/Toolbar Location" />

#### Beneath top nav: Top Navigation and Mega Menu

Create a second navigation-like bar right beneath your actual navigation. The title and toolbar move next to each other
inside one row. You can set the background, *Subnav Background Color*, and text color, *Subnav Text Color*, in the
*Toolbar Colors* section.

<img alt="Top Navigation and Beneath top nav Title/Toolbar Location" />

#### Side toolbar & title top of page: Top Navigation and Mega Menu

The title and toolbar get separated using this configuration.  The title moves inside a second navigation-like bar right
beneath your actual navigation. The toolbar moves to the right side of the screen, next to your Dashboard. Clicking a
button triggers a slide-out to view further actions. You can set the background, *Subnav Background Color*, and text
color, *Subnav Text Color*, in the *Toolbar Colors* section.

<img alt="Top Navigation and Side Slide-out Title/Toolbar Location" />

### Side Navigation

#### Top of page: Side Navigation

Have your title at the top of a page and the toolbar situated right beneath it. With this option, you can further adjust
your toolbar in the *Toolbar Styles* and *Toolbar Colors* sections.

<img alt="Side Navigation and Top of page Title/Toolbar Location" />

* *Hide Action Titles* - If enabled the toolbar buttons will not show any titles on a desktop screen. Hovering over a
  button will show the title to clarify functionalities.

* *Action Button Size* - Choose between large, medium, and small-sized buttons to save space or prevent wrapping. The
  default size is large.

#### Top nav bar: Side Navigation

Create a second navigation-like bar right beneath your actual navigation. The title and toolbar move next to each other
inside one row. You can set the background, *Subnav Background Color*, and text color, *Subnav Text Color*, in the
*Toolbar Colors* section.

<img alt="Side Navigation and Beneath top nav Title/Toolbar Location" />

The color of the toolbar buttons can be set under in the *Toolbar Colors* section.


# Email Formatting
Source: https://docs.curator.interworks.com/site_content_design/user_notifications_and_email/email_formatting

Customize email templates and formatting for automated notifications, reports, and user communications.

## Requirements

Before moving on, it's important that you follow the [steps to configure email](/setup/email/email_configuration)
on Curator.

## Email Template Formatting

When users from both the front-end and back-end are notified via Curator, they will be notified via e-mail.  This will
include all notifications such as password reset, welcome-messages on first log in, backend administrators gaining
access, and scheduled report emails.

In order to modify the background, body-color, as well as adding a header image to your emails, you can find all the
available controls for email formatting on the left-hand menu under **Settings** > **Mail** > **Mail branding**.

## Email Content

If you would like to change the messages inside of your emails, you *can* modify the templates on the backend via
the left-hand menu under **Settings** > **Mail** > **Mail templates**.  **Proceed with caution if you are modifying
these templates - they require very exact specifications**.  If you need to reset your templates and are unable to do so
please reach out to Curator support.


# Error Pages 
Source: https://docs.curator.interworks.com/site_content_design/user_notifications_and_email/error_pages

Configure custom error pages to provide helpful messaging when users encounter access issues or broken links.

When things go wrong, you want to be sure to send the right messages to your audience.  By default, Curator has error
pages that will let users know when they don't have access, they visit a broken link, or a system is down.
Communicating exactly what you'd like in these situations can be made even easier by sending your users to a custom-made
error page.

**NOTE**: You must [create a page](/site_content_design/pages/pages_overview)
first before setting it to your error page

## Setting up "Not Found" or "Access Denied" Pages

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).

2. Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.

3. Click on the "General" tab and expand the "Error Pages" section.

4. Using the dropdown, select a page from the list of pages you have created on Curator. You can set two pages here:

   * Access Denied (403) - Displays when a user does not have access to a specific link on Curator.
   * Not Found (404) - Displays when a user visits a link that does not exist on Curator, or visits an old deleted/moved link.

5. After making your selection from these dropdowns, save the Settings page.

## Setting up "Tableau Server Down" (503 error) Page

Occasionally your Tableau Server may go down for maintenance reasons, or even unplanned issues.  In this case it's
helpful to tell your users that things will be back shortly, and redirect them to useful resources.
Follow the steps below to ensure your custom page displays when your Tableau Server is unavailable.

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Tableau** > **Tableau Server Settings** section from the left-hand menu.
3. From the "General" tab expand the "Errors" section.
4. Using the "Tableau 503 Error Page" dropdown, select a page from the list of pages you have created on Curator.
5. After making your selection from this dropdown, save the Settings page.


# Notices 
Source: https://docs.curator.interworks.com/site_content_design/user_notifications_and_email/notices

Create and manage site-wide or page-specific notice banners to communicate important information to users.

Curator supports adding a text banner across the top of individual pages. These can either be created on a per-menu-item
basis, or set globally to appear across every page on your site.

***To create a notice:***

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Content** > **Notices** section from the left-hand menu.
3. Create the notice by filling out the title and body of the notice.
4. Click the checkboxes at the bottom of the page next to the menu links you would like the notice to be associated with.
5. Save the notice to create it.
6. (optional) After the notice has been saved/created, you can now check the "Set this as the Global Notice"checkbox and
   save again to set the global notice.


# Tutorials 
Source: https://docs.curator.interworks.com/site_content_design/user_notifications_and_email/tutorials

Create interactive tutorials and help documentation to guide users through dashboard features and site functionality.

Tutorials can be used to explain how to use a page, embedded visualization, or for any other supporting documentation
related to content on your Curator site.

They can be shown every time a Dashboard is viewed, a fixed number of times the Dashboard is viewed, or only when clicked
on by a user.

***To create a tutorial:***

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Content** > **Tutorials** in the left-hand menu. (or in earlier versions **Tableau** > **Tutorials**).
4. Click the "New Tutorial" button.
5. Enter the title, description and content of the tutorial in the appropriate fields. The content field allows for
   fully formatted content, including images, links, etc.
6. Enter the number of times the tutorial should be shown in the "Maximum Views" field.
   * Entering zero in this field means the tutorial will only be shown if the user clicks to see it.
   * Entering -1 in the field means the tutorial will be shown each time the user views the Dashboard until they click
     to not show it again.
7. You can control the size and location of the tutorial on the page by adjusting the pixel value for width, height,
   top position and left position. Leave blank to use the system default.
   * Top position is the number of pixels below the top of the page (0px is at the very top)
   * Left position is the number of pixels from the left of the page (0px is at the very left)
8. A highlighted image can be added by selecting an image from "Highlight Image". Once selected you can control the
   highlighted section by adjusting the pixel value for top position, left position, right position and bottom position.
   * Pixel value determines the size of highlighted area, starting from the top left. For example, if top position is
     10px and bottom position is 100px, the highlighted area will start 10px below the top of the image and end 100px
     below the top.
9. Multiple slides can be created by clicking "Add New Item"
10. Click the "Create" button.

## Setting Tutorials on Individual Content Pages

**Dashboards:**

1. While editing the Dashboard, click on the "Misc" tab.
2. Expand the "Education" section.
3. Select the desired tutorial.
4. Click the "Save" button.

**Pages:**

1. While editing a page, click on the "Misc" tab.
2. Scroll to the "Page Details" section at the bottom of the page.
3. Select the desired tutorial for the **Tutorial** field.
4. Click the "Save" button.

## Setting Tutorials Across Multiple Pages

**Global Tutorials\***(applied across every page of your Curator portal):

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on the **Settings** > **Curator** > **Portal Settings** in the left-hand menu.
4. In the Portal Settings page, click on the "General" tab at the top.
5. Select the desired tutorial in the "Global Tutorial" field under the "Global Settings" section.
6. Click the "Save" button.

\*NOTE: \*\*For versions prior to the **2023.05.31-10** release, "Global tutorials" were not truly global.
To enable a tutorial across all pages for these versions, you will also need to explicitly select a
homepage tutorial (instructions below).

\*NOTE: \*\*For versions prior to the **2023.05.31-10** release to set tutorials across *every single page*
on your Curator site, you will also need to explicitly select a homepage tutorial

**Homepage Tutorials:**

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on the **Settings** > **Curator** > **Portal Settings** in the left-hand menu.
4. In the Portal Settings page, click on the "General" tab at the top.
5. Select the desired tutorial in the "Homepage Tutorial" field under the "Global Settings" section.
6. Click the "Save" button.


# Backend Administration Tutorial: Adding Content
Source: https://docs.curator.interworks.com/tutorials/backend_administration/quick_start_adding_content

Step-by-step tutorial for adding content to Curator backend including dashboards and data sources.

<iframe title="YouTube video player" />


# Backend Administration Tutorial: Filters, Parameters, Tutorials & Loading Screens
Source: https://docs.curator.interworks.com/tutorials/backend_administration/quick_start_adding_content_filters_parameters_tutorials_loading_screens

Advanced tutorial covering filters, parameters, tutorials, and loading screens configuration in Curator backend.

<iframe title="YouTube video player" />


# Backend Administration Tutorial: Menu and Navigation
Source: https://docs.curator.interworks.com/tutorials/backend_administration/quick_start_adding_content_menu_and_navigation

Tutorial for creating menus and navigation structures in Curator backend for organized content access.

<iframe title="YouTube video player" />


# Backend Administration Tutorial: Styling
Source: https://docs.curator.interworks.com/tutorials/backend_administration/quick_start_styling

Backend tutorial for customizing visual styling, themes, and design elements in Curator.

<iframe title="YouTube video player" />


# Frontend Experience Tutorial: Dashboard
Source: https://docs.curator.interworks.com/tutorials/frontend_experience/quick_start_dashboard

Frontend tutorial for embedding and customizing dashboard presentations and user interactions.

<iframe title="YouTube video player" />


# Frontend Experience Tutorial: Homepage
Source: https://docs.curator.interworks.com/tutorials/frontend_experience/quick_start_homepage

Frontend tutorial focused on customizing and configuring the homepage layout and user experience.

<iframe title="YouTube video player" />


# Get Started with Curator in 5 Minutes
Source: https://docs.curator.interworks.com/tutorials/get_started_with_curator_in_5_minutes

Quick start guide to get up and running with Curator in just 5 minutes including essential setup steps.

<iframe title="Get Started with Curator in 5 Minutes" />


# Curator Backup
Source: https://docs.curator.interworks.com/upgrading_migration/backups/curator_backup

Learn about Curators comprehensive backup options beyond basic Import/Export functionality.

The Import / Export is a great way to backup your Curator data but sometimes a more complete backup is
needed. The Full Backup will export an entire snapshot of all your Curator data (it's a full database and
filesystem backup of the Curator webroot directory). Curator will even show you up-to-date stats on how much
free space you have available on your server to ensure you have room.

***Modifying the Full Backup Settings***

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Backups** in the left -hand menu.
3. Click on the gear icon to display a popup.  From here you can modify the location/frequency and retention options.

***To Manually Create a new Curator Backup:***

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Backups** in the left-hand menu.
3. Click the "Take New Backup" button to start a backup.  If you would like to check the status of the backup
   while it is running, you can view the active status under the
   **Settings** > **Curator** > **Queued Processes** in the left navigation.

***To Restore From a Full Backup:***

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Backups** in the left navigation.
3. Find the backup from the list view (NOTE: They are all appended with a timestamp from when they were
   taken), and click the "Restore Backup" icon (counter clockwise arrow) to restore Curator to exactly mirror
   the time the backup was taken.


# Manual Restoration of Curator Backup
Source: https://docs.curator.interworks.com/upgrading_migration/backups/manual_restoration_of_curator_backup

Step-by-step guide for manually restoring Curator from a full backup when automated restoration fails.

If you haven't attempted to use the Curator interface to restore from a full backup, go do that now
(Backend> Settings > Curator > Import/Export > Full Backup tab).
This guide is only needed if that fails for some hard-to-fix reason and it's an emergency to restore from a full backup.

It's also worth noting that, by default, Curator's full backups are stored on the same server as Curator.  If
something were to happen to the server, these could potentially disappear at the same time that Curator
does.  Please take steps to set up a server-level backup and/or store Curator's full backups in a safe, external location.

## Preface

Curator's full backups are a zip archive containing the following files:

* MySQL/MariaDB database dump (as a SQL script)
* The contents of Curator's web root directory, which contains all of the code, configuration, and uploads (as a zip archive)

The restoration process essentially overwrites all of the files on the server with the contents of the web
root directory and runs the SQL script to overwrite the database.  These are the steps you'll need to perform
when manually restoring from a full backup.

## Handling Different Database Connections

Curator stores the database connection details in `<web root>/config/database.php`.  The zip archive of the
web root within a full backup also contains these connection details.  If the database connection differs
from the system the backup originated from to the system being restored over, you'll need to perform these
steps prior to restoring:

1. Unzip the full backup zip archive to a temporary location (i.e. not inside either Curator portal’s actual web root).
2. Unzip the web root zip archive.
3. Modify the `config/database.php` file as needed in the extracted web root folder to match the connection
   details of the database you'll be restoring over.
4. Re-zip the extracted web root folder (use the same file name for the resulting zip archive).  DO NOT zip
   up the folder itself, just the contents (you should have a list of folders including plugins, storage, and vendor).
5. If the MySQL/MariaDB database name (not to be confused with host or username) differs, rename that part
   of the database dump SQL script.  Be sure to retain the date-stamp and file extension portions of the file
   name.  Also, open the file and update any references to the database name in the first \~30 lines.
6. Re-zip the web root zip archive (not to be confused with the extracted web root directory) and the
   database dump SQL script as the full backup (use the same file name for the resulting zip archive).
7. Transfer the updated full backup zip archive to the system you wish to restore over and place it in the
   directory where full backups are stored (default is `<web root>/storage/temp/`).

## Manually Restoring the Database

If you haven't already, unzip the full backup zip archive to extract the database dump and transfer that SQL
script to the system you'll be restoring over.

Make the following replacements in the commands below.  If you don't know the values, look at the
`<web root>/config/database.php` file on the system you'll be restoring over.

* `$host`: The database host.  This is normally localhost unless you have an external database.
* `$user`: The database username.
* `$port`: This is almost always 3306, unless you've customized your database configuration to run on a different port.
* `$name`: This is the database name.  Each MySQL/MariaDB host can store many different databases, usually
  this is Curator, but it could be different.
* `$dbDumpFilename`: This is the file name to the database dump file.  Include the full file path if running
  the command from a different directory that where the SQL script lives.

*NOTE: You will be prompted for the database password while the command runs.*

```MySQL theme={null}
mysql -h $host -u $user -p --port=$port --database $name < $dbDumpFilename
```

## Manually Restoring the File System

### Step 0 for Linux Systems

Before beginning on Linux systems, run the following commands to determine which system user and group owns
Curator's web root.  It will be needed during the process.

```Linux theme={null}
cd /var/www/html
ls -l
```

The user and group should either be `apache` or `www-data` and should be listed next to all of the files.
The commands below will assume apache, but replace it with www-data if your system lists it here instead.

### Restoration Process

1. If you haven't already, unzip the full backup zip archive to extract the web root directory backup and
   transfer that zip archive to the system you'll be restoring over.
2. In a temporary location on the Curator server outside of Curator's web root directory (make note of the
   location), unzip the web root directory backup (i.e. the file that matches the pattern: `webroot_YYYYMMDD_HHMMSS.zip`).
   * Linux Command:
     `sudo -u apache unzip webroot_YYYYMMDD_HHMM.zip`
   * On Windows systems, you should be able to utilize the built-in zip extract function, though
     alternatives like 7-zip may be faster.
3. In the web root directory, delete directories as follows:
   * Linux Command:
     `sudo rm -Rf /var/www/html/modules /var/www/html/plugins /var/www/html/themes /var/www/html/vendor`
   * On Windows systems, delete these folders using Windows Explorer:
     * modules
     * plugins
     * themes
     * vendor
4. Copy the contents of the extracted web root backup to the actual web root directory.
   * Linux Command:
     `sudo -u apache cp -a /path/to/extracted/webroot/backup/* /var/www/html/`
   * On Windows systems, use a copy/paste or select/drag operation within Windows Explorer.
5. Fix file permissions as needed.  See this document for details:
   [Filesystem Permissions](/server_management/system_administration/filesystem_permissions)


# Taking a Manual Full Backup
Source: https://docs.curator.interworks.com/upgrading_migration/backups/taking_a_manual_full_backup

Instructions for manually creating comprehensive Curator backups when built-in backup functionality is insufficient.

While we highly recommend using the built-in Full Backup functionality within Curator, there are times where
that isn't possible or when implementing your own full backup process.  This guide will cover the steps and
commands that Curator uses to take a full backup.  You may need to customize these steps for your own
purposes.

There are 2 sets of data that will need to be included in a full backup:

1. Curator's Database
2. Curator's File System

## Database Dump

The way Curator backs up its database is by dumping the structure and data contained in that database to a
SQL file. This SQL file will include the actual SQL code needed to recreate the tables and insert all of the data.

The command Curator runs is:

`mysqldump -h $host -u $user -p --port=$port --databases $databaseName > $backupFilename`

Where:

* `$host` is the host name where the database lives.  This is almost always localhost or 127.0.0.1.
* `$user` is the database user.  Get this from your *\<web root>*/config/database.php configuration file.
* `$port` is the port the database runs on.  This is almost always 3306.  Get this from your *\<web root>*
  config/database.php configuration file if it's something other than 3306.
* `$databaseName` is the name of the database inside of MariaDB/MySQL that houses Curator's data.  Get this
  from your *\<web root>*/config/database.php configuration file.
* `$backupFilename` is the file to save the SQL dump into.  Curator names this file `$databaseName`\_`$currentTimestamp`.sql

You will be prompted for the password when running this command.  Get the password from your *\<web root>*
config/database.php configuration file.

## Filesystem Backup

To back up Curator's files, Curator just zips the entire web root directory (i.e. /var/www/html or
C:\InterWorks\Curator), excluding any other full backup files.  Curator stores its full backup files in the
*\<web root>*/storage/temp directory as `full_backup_$currentTimestamp.zip` by default, but this backup
location may be configured to be a different directory.

## Curator Compatible Backups

If you are trying to create a backup that's compatible with Curator's Full Backup functionality so that it
can be restored with the click of a button, here are the details that will be important:

1. The full backup zip archive must follow this naming convention, where the the middle part is replaced by
   an appropriate timestamp: `full_backup_YYYYMMDD_HHMMSS.zip`.
2. The full backup zip archive must consist of 2 files:
   1. The database dump with the name of the database as the prefix (e.g. `curator_`), a timestamp that
      matches the full backup timestamp, and a `.sql` file extension.
      The name should look something like: `curator_YYYYMMDD_HHMMSS.sql`.
   2. The backup of the file system as a zip archive that must follow this naming convention, where the
      middle part is replaced by the same timestamp as the full backup: `webroot_YYYYMMDD_HHMMSS.zip`.
3. In order to be restored by Curator, this file must be placed in *\<web root>*/storage/temp/.


# Importing and Exporting
Source: https://docs.curator.interworks.com/upgrading_migration/migration/importing_and_exporting

Manual backup and migration process for transferring Curator content between installations.

We provide a simple manual backup process that can help with migrating your Curator content from one
environment to another, or to the server as a backup so you don't lose all that hard work.

## Migration Via File

This method to migrate data involves downloading a file from the source Curator and uploading it to the destination
Curator. These files can be used as backups or a simple way to pass data to the Curator support team for debugging
your specific content.

***To export your Curator metadata:***

1. Login to the backend of your source Curator instance (e.g. `https://curator.example.com/backend`).
2. Navigate to **Settings** > **Curator** > **Import/Export** section using the left-hand menu.
3. Check the necessary items you need to backup (or click 'Select All' at the top)
4. Click "Export" and this will download a file you can keep as a backup or use to import your settings
   to another Curator instance.

***To import your Curator metadata:***

1. Login to the backend of your destination Curator instance (e.g. `https://curator.example.com/backend`).
2. Navigate to **Settings** > **Curator** > **Import/Export** section using the left-hand menu.
3. Click on the "Import" tab at the top.
4. Click the "Upload" icon (upwards arrow) to locate the JSON file you exported using the steps above, then
   click "Preview Import".
5. Check the necessary items you need (or click 'Include All' at the top)
6. Click the "Import" button to complete the import process.

## Migration Via API

This method to migrate data involves using Curator's REST API from the destination Curator to request data from the
source Curator. This option can be convenient because it requires fewer steps after the initial setup.

***Retrieve an API key:***

1. Login to the backend of your source Curator instance (e.g. `https://curator.example.com/backend`).
2. Navigate to **Settings** > **Curator** > **API Keys** section using the left-hand menu.
3. Copy an API Key using the icon in the "ACTIONS" column. *Note: If the API Key has "Restrict Access" enabled, ensure
   the "export" endpoint in the "Portal Permissions" section is allowed.*

***To import your Curator metadata:***

1. Login to the backend of your destination Curator instance (e.g. `https://curator.example.com/backend`).
2. Navigate to **Settings** > **Curator** > **Import/Export** section using the left-hand menu.
3. Click on the "Import" tab at the top.
4. Click the "Use API" radio button.
5. Enter the source Curator's URL and API Key. *Note: After completing one import from the source Curator this info
   will be stored. The next time you need to migrate data you can simply select that stored data instead of re-entering
   it.*
6. Check the data types you'd like migrated. Every item of the selected types will be retrieved, but you can select
   specific items in the next page.
7. Click "Preview Import" at the bottom of the screen.
8. Check the necessary items you need (or click 'Include All' at the top)
9. Click the "Import" button to complete the import process.

## Permissions

Each backend user in Curator can be assigned permissions for handling certain content. If your user doesn't have
permissions to make changes to the content included in an import it will be filtered out of the data. You can
request these permissions be added by your Curator administrator or have them process the import.


# Dependency Updates
Source: https://docs.curator.interworks.com/upgrading_migration/upgrading/dependency_updates

Instructions for updating PHP, Apache, or MariaDB dependencies on your Curator webserver.

Curator's upstream dependencies (PHP, Apache, and MariaDB) require periodic updates to maintain security, performance,
and compatibility with the latest Curator features.

*Note: Before upgrading any dependencies, it is a good idea to ensure that you have a recent Curator backup available.*

## PHP Dependencies by Curator Version

| Curator Version | Minimum PHP Version | Maximum PHP Version |
| --------------- | ------------------- | ------------------- |
| 2023.03.01      | 8.0                 | 8.0                 |
| 2024.10.04      | 8.0                 | 8.1                 |
| 2025.07-03      | 8.0                 | 8.3                 |
| 2025.09-03      | 8.1                 | 8.3                 |
| 2026.04-01      | 8.3                 | 8.3                 |

### Important Notes

* Always ensure your PHP environment meets or exceeds the minimum version requirement for your Curator installation.
* Upgrading Curator may require upgrading your PHP version.
* Check your current PHP version with `php --version`.

## Windows

First and foremost: ensure all relevant Windows Updates have been applied to your server.

Next, update Curator dependencies.

Curator bundles PHP and Apache upgrades into a simple utility package to make updating them as easy as possible.

To update Curator's dependencies, simply download our **[Curator Dependency Update Utility](https://portals.interworks.com/Curator_PHP_Upgrade_Util.exe)**.

Once downloaded, simply double-click the utility to run updates.
PHP and Apache will be upgraded automatically by this utility.

**Note: Internet access is required for this process. Systems without internet access will need to upgrade manually.**

### Manual Dependency Updates

If your server has restrictions that prevent the utility from downloading files automatically, you can manually download
the required files and run the upgrade utility locally.

To manually upgrade dependencies:

1. Download the **[Curator Dependency Update Utility](https://portals.interworks.com/Curator_PHP_Upgrade_Util.exe)** on
   a system with internet access.

2. Download the following files to the same directory as the utility.
   <Warning>File names must match exactly as shown below for the utility to recognize them.</Warning>
   * **vc\_redist.exe** - VC Redistributables: [https://api.curator.interworks.com/file/vc\_redist](https://api.curator.interworks.com/file/vc_redist)
   * **php.zip** - PHP package: [https://api.curator.interworks.com/file/php\_apache](https://api.curator.interworks.com/file/php_apache)
   * **apache.zip** - Apache updates: [https://api.curator.interworks.com/file/apache](https://api.curator.interworks.com/file/apache)

3. Transfer all files (the utility and the three downloaded files) to your Curator server.

4. Ensure all five files are in the same directory, such as having them all on your Desktop,
   then double-click the utility to run the upgrade.

*Note: The utility will detect the locally available files and use them instead of attempting to download them. If the
file names do not match exactly, the utility will not recognize them and will attempt to download them from the internet.*

### Manual MariaDB Updates

To manually upgrade MariaDB, download the [MariaDB package](https://api.curator.interworks.com/file/mariadb) using
the link below.

*Note:* To upgrade MariaDB, you will need your root database password.
If you do not know this password, check your installation directory for an *Curator.txt* file, which contains
the default credentials.

### MariaDB on Windows

To upgrade MariaDB on Windows, first stop the *CuratorDB* Service, using Window's *Services* app.

You can open Window's *Services* by simply searching for *Services* using the Window's start bar.

To stop the *CuratorDB* process, find it in the *Services* list, then right click on it and click *Stop*.

Next, find Curator's MariaDB installation folder.

*Note:* This can usually be found in C:\InterWorks\Curator\libs\MariaDB.

Rename to MariaDB's *bin* folder to *bin.bkp*.

After a successful upgrade, you can delete this backup directory.

Then, download the latest [MariaDB](https://api.curator.interworks.com/file/mariadb) package.
Unzip this package over top of Curator's MariaDB installation.

Finally, open PowerShell in Administrative mode and run MariaDB's upgrade utility.
To open Powershell in Administrative mode, use the search widget in Window's start bar.
Search for Powershell, then Right-Click on Powershell and click "Run As Administrator".

Navigate to MariaDB's bin directory and run the upgrade utility.

```bash theme={null}
cd C:\InterWorks\Curator\libs\MariaDB\bin
mysql_upgrade_service.exe --service=CuratorDB
```

Note: if you have trouble with the MariaDB's *service* upgrade utility, you can also use the non-service version.
To do this, first restart MariaDB in Window's *Services* app, and then run this command:

```bash theme={null}
mysql_upgrade.exe -u root -p --force
```

## Linux

Linux's upstream repositories handle dependency updates, so first ensure you are running a recent version of your Linux distribution.

If you're not sure, you can take a look at our recommended distributions on the [Linux Installation page](/setup/installation/linux_installation).

To update Curator's Linux dependencies, SSH into your web server and cd into the webroot directory
(typically /var/www/html) and ensure you're using a user that has full sudo access, and run the command below.

This command will upgrade PHP, MariaDB, Apache, and any other operating system dependencies required by Curator:

```bash theme={null}
curl -s -o php_upgrade_util.sh https://api.curator.interworks.com/scripts/php_upgrade_util.sh && chmod +x ./php_upgrade_util.sh && ./php_upgrade_util.sh
```


# Disable Curator Upgrades
Source: https://docs.curator.interworks.com/upgrading_migration/upgrading/disable_curator_upgrades

Learn how to disable the upgrade functionality in Curator for servers without external network access.

Curator can be set up on a server that does not have access to outside networks. When you have this setup it
is advised to Disable Upgrades. This will prevent any issues if someone accidentally clicks the upgrade
button when Curator can't reach an out of network connection.

***To enable Disable Curator Upgrades:***

1. Login to the backend of your Curator instance (e.g. `https://curator.example.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Portal Settings** section using the left-hand menu..
3. Click on the "Features" tab at the top of the main page content.
4. Click to switch on the "Disable Curator Upgrades" setting under the "Functionality" section and click the "Save" button.


# Offline Upgrades (Air Gapped)
Source: https://docs.curator.interworks.com/upgrading_migration/upgrading/offline_upgrades_air_gapped

Guide for updating Curator on servers without internet access using manual update files.

If you've installed Curator on a server that is cut off from internet access, we provide a Manual Update
option. This requires enabling the Disable Curator Upgrades setting to be enabled so you can perform a Manual
Upgrade.

***To enable Allow Manual Curator Upgrades:***

1. Login to the backend of your Curator instance (e.g. `https://curator.example.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Portal Settings** section using the left-hand menu..
3. Click on the "Features" tab at the top of the main page content.
4. If "Disable Curator Upgrades" is set to OFF, click the switch to turn this feature ON
5. Click to switch the "Allow Manual Curator Upgrades" setting ON under the "Functionality" section and click
   the "Save" button.

***Click [Here](/upgrading_migration/upgrading/system_upgrade) for
Documentation on How to Manually Upgrade Curator***


# System Upgrade
Source: https://docs.curator.interworks.com/upgrading_migration/upgrading/system_upgrade

Learn about the various methods to update your Curator installation to the latest version.

There are several easy ways to update Curator.

To see if Curator needs an update, check the status of your Curator instance on the homepage of the backend,
or on the System Upgrade page.

The "Current Version" will show what software version Curator is currently running and the "Latest Version"
will show the latest release available.

**Attention: We recommend taking a Curator Backup before an upgrade. More details can be found [here](/upgrading_migration/backups/curator_backup).**

## Upgrading Curator

***One-click Upgrade:***

1. Login to the backend of your Curator instance (e.g. `https://curator.example.com/backend`).
2. Navigate to the **Settings** > **Curator** > **System Upgrade** section using the left-hand menu.
3. Click the "Start One-click Upgrade" button.

***Manual Upgrade:***

1. Login to the backend of your Curator instance (e.g. `https://curator.example.com/backend`).
2. Navigate to the **Settings** > **Curator** > **System Upgrade** section using the left-hand menu.
3. Click the "Manual Upgrade" button to display the Manual Upgrade links in the release notes section at the
   bottom of the page.
4. Click the link of the version you wish to upgrade to, this will download a .zip file containing the upgrade contents.
5. Upload the .zip file you just downloaded to the "Upgrade Zip Archive" section and click the "Submit" button.

***Curator API:***

1. Login to the backend of your Curator instance (e.g. `https://curator.example.com/backend`).
2. Navigate to the **Settings** > **Curator** > **API Keys** section using the left-hand menu.
3. Select an existing key or create a new key
4. If creating a new key, save the key.
5. From the REST API dropdowns, select 'Portal' in the left dropdown and 'Upgrade' in the right dropdown.
6. Click the link that was generated below the drop-downs.
7. This will open a new tab, when upgrade is successful a small success text display will populate.

## Troubleshooting

***Having Issues With the Upgrade?*** Try our [Upgrade Troubleshooting Documentation](/upgrading_migration/upgrading/troubleshooting_upgrades).

## Multi-version Upgrades (4+ versions)

We recommend upgrading no more than 3 versions at a time.

If you plan to make an upgrade to a Curator instance that is more than 4 versions out-of-date, use the
version-specific upgrades on the upgrade page, instead of the "One-click upgrade".


# Troubleshooting Upgrades
Source: https://docs.curator.interworks.com/upgrading_migration/upgrading/troubleshooting_upgrades

Common upgrade issues and solutions to help resolve problems during the Curator update process.

Occasionally, you may run into issues during the upgrade process. We've provided some common scenarios and
how to quickly resolve them below.

**NOTE:** While running updates, it is always a good idea to have someone on standby during your upgrade who
has access to the server that Curator is running on, as most of these debugging solutions require
server-level access.

## Re-run the Upgrade With an Alternate Method

Curator can be upgraded in several different ways, so if you run into an issue upgrading in a specific way,
try using an alternative method to upgrade.

For example, there may be an issue with running the "one click" upgrade on your system.

Try upgrading via the Curator API, or using the Manual Upgrade method.

Both of these upgrade methods are detailed in our [System Upgrade Guide](/upgrading_migration/upgrading/system_upgrade).

## Dependency Upgrades

If Curator requires dependency updates before upgrading, such as PHP, follow the steps provided in our
[dependency upgrades](/upgrading_migration/upgrading/dependency_updates)
documentation.

## Updating the Curator Database (Running Migrations)

Curator's database is often modified during the upgrade process, and if database changes are not completed
successfully database errors can occur.

If you run into any database errors after upgrading, or during the upgrade process, re-running Curator's
database migrations can resolve these errors.
You can safely rerun these migrations multiple times without any adverse effects.

**To Re-run the Curator Database Migrations From Your Browser:**

1. Visit your Curator url in a web browser, but add `/up` to your URL, for example: `https://curator.example.com/up`
2. You should be directed to a page that contains "success" followed by a list of the steps taken to finish
   the migration. If you see errors instead, make note of the errors seen and contact Curator support for
   further assistance.

**To Re-run the Curator Database Migrations From the Web Server:**

1. Open a command prompt/terminal.
2. *Double-check* that you are running the terminal/command prompt as the same user that is running Curator
   (you can find this information on the backend of Curator under **Settings** > **Curator** > **Status**).
3. Use the `cd` command to move the command prompt into your webroot (e.g. `cd /var/www/html` on Linux or
   `cd C:\InterWorks\Curator\htdocs` on Windows).
4. Type `php artisan winter:up` and then press ENTER.
5. Any remaining database migrations will run, and display status messages in green.
6. If there are any errors during this process, please take a screenshot and send it to Curator support.

## File System Permissions Issues

If Curator's logs contain errors relating to filesystem permissions on your Curator site, or the site itself
is rendering an error that says "failed to cache..." or "permission denied...", or "no such file found...",
use the following steps to resolve this issue:

1. Click the "clear cache" button on the backend of Curator
2. Use our [Filesystem Permissions Guide](/server_management/system_administration/filesystem_permissions)
   to fix any errant file permissions settings.

## Fix Corrupted Files

If Curator is displaying an error message stating "vendor files are missing" or some pages may throw a
warning message that some files were not able to be found, you can re-download the Curator system files to
your web server using the steps below:

***Fixing Corrupted File Systems on Linux:***

1. `cd` into your webroot directory (e.g. `/var/www/html`)
2. Run the commands below, replacing the `[curator_key]` in the URL with your Curator license key. If you
   don't know your license key, reach out to your account manager for more information.

   wget -O latest.zip "[https://api.curator.interworks.com/get\_version.php?key=\[curator\_key\]\&kernel=473\&version=latest](https://api.curator.interworks.com/get_version.php?key=\[curator_key]\&kernel=473\&version=latest)";
   unzip latest.zip;
   rm -Rf plugins/interworks;
   rm -Rf vendor;
   cp core/. . -Rf

   NOTE: You may replace `latest` in the URL above with a specific version
3. Manually rerun database migrations using the steps provided in the **Updating Curator Database** section.
4. Visit your Curator site in a web browser to confirm whether your site is back up and running.

***Fixing Corrupted File Systems on Windows:***

1. From a web-browser visit the URL below to download a .zip file with your Curator filesystem, replacing the
   `[curator_key]` in the URL with your Curator license key. If you don't know your license key, reach out to
   your account manager for more information.
   `https://api.curator.interworks.com/get_version.php?key=[curator_key]&kernel=473&version=latest`
2. Make a backup of your webroot in case of any errors that occur in the steps below.
3. Unzip the file that was downloaded from **Step 1** into your webroot (e.g. `C:\InterWorks\Curator\htdocs`)
   and replace all files with the newly extracted files.
4. Manually rerun database migrations using the steps provided in the **Updating Curator Database** section.
5. Visit your Curator site in a web browser to confirm whether your site is back up and running.

## Event Log Troubleshooting

***Event Log Retrieval if You Can Access the Curator Backend in a Web Browser:***

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Logs** > **Event Log** section using the left-hand menu.
3. Look for any "upgrade" related errors.
4. Reach out to support for further troubleshooting.

***Event Log Retrieval if You Cannot Access the Curator Backend in a Web Browser:***

1. Log on to the web server that hosts Curator.
2. Find the Curator event logs:
   * **Windows**: `C:\InterWorks\Curator\htdocs\storage\logs`
   * **Linux**: `/var/www/html/htdocs/storage/logs`
3. Find the log file with today's date (e.g. system-2025-03-17.log ).
4. Copy the file and send it to Curator support.


# Automatic License Provisioning 
Source: https://docs.curator.interworks.com/users_groups/user_management/automatic_license_provisioning

Automatically provision Tableau Server licenses for users when they access Curator for streamlined license management.

Tableau allows Administrators to manage their licenses in a way that all users can be added as unlicensed and only
[grant them a license][1] once they are logging into Tableau Server. You can now use this feature through your Curator.
All users that are currently unlicensed will receive a license when trying to log into Curator if you have this feature enabled.

## Note This feature is only available when you either use SAML or OAuth/OpenID for authentication

***To grant license on sign-in with SAML***

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Tableau** > **Tableau Server Settings** section from the left-hand menu.
3. In the Authentication tab, expand the **SAML Advanced** section and enable the "License Users if Unlicensed" toggle.

***To grant license on sign-in with OAuth/OpenID***

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Tableau** > **Tableau Server Settings** section from the left-hand menu.
3. In the Authentication tab, expand the **Customization** section and enable the "License Users if Unlicensed" toggle.

[1]: https://help.tableau.com/current/server/en-us/grant_role.htm


# Custom Attributes 
Source: https://docs.curator.interworks.com/users_groups/user_management/custom_attributes

Define and manage custom user attributes for enhanced user profiling and personalized content delivery.

With Tableau Cloud, and Tableau versions 2023.1 and above, you can now pass through User Attributes from Curator or your
SAML IdP (e.g. Okta, Azure AD) seamlessly through to your Tableau Dashboards.  This will allow you to use a new calculated
field `USERATTRIBUTE()` in your Dashboard to retrieve the value of the User Attribute and filter your data accordingly.

Note: When a conflict arises due to the same attribute being found in multiple locations, the User attributes will take
highest precedence, followed by Group attributes and then SAML attributes.

## View User's Attributes

1. Login to the backend of your Curator instance (e.g. `https://www.curatorexample.com/backend` ).
2. Navigate to the **Settings** > **Users** > **Frontend Users** section from the left-hand menu.
3. Find the user you would like to see from the list using the search options.
4. Expand the "Custom Attributes" section.  At the top you will see the "Resolved Attributes" that take into account
   inheritance from all sources.

## Enabling SAML Attribute Retrieval on Login

(/setup/authentication/overview)
\***NOTE:** [SAML Authentication](/setup/authentication/overview)
**must be enabled to retrieve these user details from an external source.**

1. Login to the backend of your Curator instance (e.g. `https://www.curatorexample.com/backend` ).
2. Navigate to the **Settings** > **Security** > **Authentication Settings** section from the left-hand menu.
3. Expand the "SAML Attributes" section, and enter User Attributes you would like Curator to detect from the user's SAML
   profile on login.
4. Click the "Save" button.

## Assigning User Attributes to a Group on Curator

1. Login to the backend of your Curator instance (e.g. `https://www.curatorexample.com/backend` ).
2. Navigate to the **Settings** > **Users** > **Frontend Group** section from the left-hand menu.
3. Find a user group and click on the group to edit details, or click the "New Frontend Group" button to create a new
   group on Curator.
4. Expand the "Custom Attributes" section, and enter the attribute and value you would like to assign to all users that
   belong to this group.
5. Click the "Save" button.

## Assigning User Attributes to a User on Curator

1. Login to the backend of your Curator instance (e.g. `https://www.curatorexample.com/backend` ).
2. Navigate to the **Settings** > **Users** > **Frontend Users** section from the left-hand menu.
3. Find the user you would like to assign an attribute to and click on their name to view the edit-user page.
4. Expand the "Custom Attributes" section, and find the "User Custom Attributes" fields.  Enter the attribute and value
   you would like to assign to the user.
5. Click the "Save" button.


# Frontend Users
Source: https://docs.curator.interworks.com/users_groups/user_management/frontend_users

Manage local Curator user accounts including creation, permissions and configuration for Curator Users authentication.

<Note> This is only relevant for use with the authentication setting **Curator Users** </Note>

If you're using [Curator Users](/setup/authentication/curator_users)
as the authentication source (or SAML IdP), the system will enable administrators to manage the
frontend users.

***To enable management of frontend users:***

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Settings** > **Security** > **Authentication Settings** in the left navigation.
4. Select "Curator Users" for the authentication type.
5. Click on the "Save" button.

***To manage frontend users:***

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on the **Settings** > **Users** > **Frontend Users** in the left navigation.
4. Click on the "New Frontend User" button to create a new user, or click on an existing user to modify user details or permissions.


# Just-in-time (JIT) Provisioning 
Source: https://docs.curator.interworks.com/users_groups/user_management/just_in_time_jit_provisioning

Configure just-in-time user provisioning to automatically create user accounts during first-time authentication.

## JIT Provisioning on Curator

When paired with externally managed authentication providers (SAML, Tableau Server, Active Directory, etc.), Curator will
automatically create a user record in its own database when they first log in.

If you need to disable this, the setting can be found under **Settings** > **Security** > **Authentication Settings** >
**Customization** section > *Disable Just-in-time Provisioning of Curator Users* setting.  Be sure to click the save button.

## JIT Provisioning on Tableau

Curator can also serve as an intermediary to that process and automatically create the users on Tableau Server after a
successful authentication with Okta or other SAML identity providers.  You will still be required to manually assign any
groups, or license levels (Explorer by default), in Tableau Server.  But this allows simple authentication into Curator if
the user does not yet exist on Tableau.
(/setup/authentication/okta\_saml)
To enable this, complete the steps for SAML setup ([instructions here](/setup/authentication/okta_saml))

Then on the backend under **Settings** > **Security** > **Authentication Settings**, open up the **SAML Advanced** section
and enable *Just-in-time (JIT) Provisioning* then Save your SAML settings.


# Reset User's Password
Source: https://docs.curator.interworks.com/users_groups/user_management/reset_users_password

Reset user passwords as an administrator when users cannot access their accounts or have forgotten credentials.

When managing users you may find a need to change a user's password on Curator.  The method used to change user's
passwords will depend on the [authentication type](/setup/authentication/overview)
you are using on Curator: when using *Tableau Server* or *Curator Users* authentication you can reset users passwords
within Curator.  For all other options you will need to use the source-system of your user store (your IdP) to change the
password there.

**To reset a user's password:**

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Tableau** > **Tableau Users** or **Settings** > **Users** > **Frontend Users** section
   from the left-hand menu.
3. Find the user in the list that you're looking for in the list of users, then click on the row to navigate to the
   edit-user page.
4. Type in a new password for the user, then click the save button
5. The end user will **NOT** be notified of this change, so be sure to let them know of the change made.


# User Sync and Membership Sync Overview 
Source: https://docs.curator.interworks.com/users_groups/user_management/user_sync_and_membership_sync_overview

Overview of user synchronization and membership sync processes between Curator and external authentication systems.

There are two different sync process that run in Curator: the user sync and the group membership sync. There used to be
one sync that did both, but we found bringing over every user and group resulted in very slow syncs and a lot of
redundancy. Separating the one sync into two has led to much greater efficiency but some confusion. This doc aims to
answer frequently asked questions about these syncs and will be updated as new questions are asked.

First, a quick primer on both syncs:

1. **User Sync**:
   * **What is it?**
     The user sync brings user details from your analytic platforms to Curator. This includes full display name, email
     address, user roles, etc. This does not include group membership.
   * **When does it happen?**
     The user sync always happens on login. You can also manually sync a specific user's details from the Curator
     backend > Settings > Users > Frontend Users > select a specific user and use the buttons in the "Platform Users"
     section to sync the details.
     *Note: If the user doesn't exist on Curator the user sync will create it. This results in having a lean user base of
     only the true Curator users.*
     *Note: You cannot disable the on-login user sync.*
2. **Group Membership Sync**:
   * **What is it?**
     The group membership sync builds Curator Frontend Group membership from a user's platform group membership. For
     instance, you can create an "Admins" Frontend Group in Curator and, instead of manually selecting numerous users, you
     can select the "Admins" group from one of your platform connections and Curator will automatically put those users in
     the Curator Frontend Group. This does not include user details.
     *Note: This is only relevant if you use Curator Frontend Groups for restricting access in the navigation or for
     Frontend Group Overrides. If you don't use these features then group membership is irrelevant to Curator.*
   * **When does it happen?**
     The group membership sync will happen on login by default. Some platforms can have slow response times when Curator
     requests the relevant membership, so you can disable the on-login membership sync to speed up the login. If you
     disable the on-login membership sync you can enable a sync to occur on a scheduled cadence to ensure users are in
     their groups by the time they login.
     *Note: If you disable the on-login membership sync, the scheduled membership sync will create users if they don't
     already exist on Curator. This is to preemptively ensure the user has their groups before logging in, which requires a
     Curator user. This is the **only scenario** where the group membership sync also syncs user details.*

**Where are my Users?**
You can find your Frontend Users at the Curator Backend > Settings > Users > Frontend Users. This page will also show the
associated platform-specific users.

**Where are my Groups?**
You can find your Frontend Groups at the Curator Backend > Settings > Users > Frontend Groups. You can trigger syncs and
change sync settings from this page.

**Why would I create groups?**
The primary features that leverage Curator Frontend Groups are:

1. **[Restrict Access](/site_content_design/menus/restrict_access)**
   You can deny permission to see content in Curator by restricting access in the navigation based on group membership. This
   is especially helpful for content created in Curator that doesn't have permissions to pull from an analytic platform (i.e.
   Pages, Files, external URL's, etc.). This can also be useful if your navigation has many items and the permission checks
   add copious load time by restricting access to a high-level menu item, which automatically denies access to all of the
   item's children.
2. **Frontend Group Overrides**
   Overrides are useful if you have groups of users who require a different look-and-feel in the Curator frontend. This is
   common if you have groups/departments or multiple tenants who use different logos, colors, etc. You can also present
   entirely different navigation structures and homepages to your various groups.

**How do I create groups?**
You can create a Frontend Group at Curator Backend > Settings > Users > Frontend Groups by using the "New Frontend Group"
button. You can build membership by either manually selecting uses from the "Group Membership" section or by using a group
from one of your connected analytic platforms. For instance, you can create an "Finance" group that uses a Tableau Group
and ThoughtSpot Group instead of manually selected every use who needs to see finance content.

**Curator used to automatically create Frontend Groups that were in Tableau, but not anymore. Why not?**
If your Curator instance doesn't leverage restricted access by group or Frontend Group Overrides then Tableau Groups are
irrelevant to Curator and syncing them is unnecessary. Even if you do use a couple Tableau Groups for Curator Frontend
Groups you don't need all of them. Now Curator's membership syncs are much leaner and more efficient, resulting in the
same functionality with much better performance.

**I created a user in Tableau, but it doesn’t show they are synced in Curator. How do I get Curator to sync a user?**
The user will be synced to Curator as soon as they log in. Users are always synced during login.
*Caveat: Tableau uses unique user records for each Site they are a member of. To avoid long login times, Curator only
syncs the Tableau User from the Site you've specified in the REST connection (Curator backend > Integrations >
Connections). The other Site users will be synced on a daily cadence.*
*Caveat to the caveat: If you've enabled the Tableau Repository connection every Site user will be synced on login.
Repository queries are much faster than REST API calls so the login time isn't as affected.*


# Username Mapping 
Source: https://docs.curator.interworks.com/users_groups/user_management/username_mapping

Map external user identifiers to local usernames for proper authentication and user synchronization across systems.

If your analytic infrastructure was built by several independent groups within your organization, it's possible that the
username formats don't match across the platforms. Authenticating to each platform can usually be solved with a single
sign-on solution, but the issue still exists for embedding these platforms. API's that are used to verify user
information, permission to analytic content, group membership, etc. rely on local platform users and can't leverage SSO
credentials. Curator solves this with a built-in platform username formatting.

<Note>
  Username mapping can only change the **format** of a username, not the username itself. For example, it can convert
  `first.last@example.com` to `example\first.last`, but it cannot convert `first.last@example.com` to
  `flast@example.com`.
</Note>

## How it Works

Curator's username formatting feature will take the username received from your authentication source (SAML IdP, Tableau
Server local auth, ThoughtSpot local auth, etc.) and map it to another format based on the API call being made. For
instance, if Okta is returning the username as an email address but Tableau Server users use the prefixed domain format
the following will happen (assuming the username is InterWorks\Curator in Tableau Server):

1. User logs into Curator via Okta using their Okta credentials.
2. Okta returns the username as `curator@interworks.com`.
3. Curator automatically re-formats the username to InterWorks\Curator in order to sync the Tableau Server user details.

## How to Configure

1. Navigate to the Curator Backend > Settings > Users > Username Formatting
2. Turn on the "Enable Username Mapping" switch
3. Specify the username format your authentication source is returning back to Curator using the "Curator Frontend
   Username Format" field.
4. Specify the username format for each Connection you've configured in Curator. You can use a different format per Connection.

## Supported Formats

The following are the supported username formats assuming the username is "Curator" and the domain is "InterWorks":

* Username Only > Curator
* Username with Prefixed Domain > InterWorks\Curator
* User Email > `curator@interworks.com`

## Domain Formatting

In addition to mapping username formats for multiple platforms, you may also need to map the domains. For instance,
*iw\Curator* doesn't match `curator@interworks.com` in format or domain. To handle this situation, you can configure
domain mapping:

1. Navigate to the Curator Backend > Settings > Users > Username Formatting
2. Turn on the "Enable Domain Mapping" switch
3. Use the "Domain Map" area to specify as many mappings as you need, specifically the following:
   * **Connection**: The connection being mapped to from your Frontend User
   * **Frontend User Domain**: The domain to find in the Frontend User name
   * **\[Platform] User Domain**: The replacement domain for the platform user name

## Example

My SSO system is returning *iw\Curator* but my Tableau user is `curator@interworks.com`. The following settings would
resolve this mismatch:

For the mismatch format

1. Turn on "Enable Username Mapping" switch
2. Choose "Username with Prefixed Domain" for the "Frontend User Username Format" field
3. Choose "User Email" for the "Tableau Username Format"

For the mismatch domain

1. Turn on "Enable Domain Mapping" switch
2. Add a new item under "Domain Map"
3. Choose "Tableau" for the "Connection" field
4. Type "iw" for the "Frontend User Domain"
5. Type "InterWorks" for the "Tableau User Domain"
6. Save all the settings


# Users and Groups Overview
Source: https://docs.curator.interworks.com/users_groups/user_management/users_and_groups_overview

Comprehensive guide to user management in Curator covering frontend users, groups, permissions and authentication methods.

## Frontend Users

"Frontend users" (or local Curator users) are responsible for bringing together your various platforms to create
individual frontend experiences. These users are matched based on their usernames, so it's crucial to ensure consistent
naming across your connected systems - if you do not have them matched exactly, see our [Username Mapping guide](/users_groups/user_management/username_mapping).

To view the list of frontend users, go to the backend and navigate to **Settings** > **Users** > **Frontend Users** from
the left-hand menu. Each user who has signed into Curator will have a corresponding record. Clicking on a user record
will display details about that user, including any connected platforms.

You can also get a [preview of the user's navigation](/users_groups/user_security/frontend_user_permissions)
near the top of this page.

## Platform Users

"Platform users" refer to the records maintained by Curator for users synced from your connected systems (e.g., Tableau
users, ThoughtSpot users, etc.). These platform users store synced information from the respective systems, which can be
leveraged by the Frontend User for permissions and platform-specific actions like favoriting or subscribing to a Tableau
Dashboard.

To access the list of platform users, go to the backend and navigate to
**Curator Backend** > **Settings** > ***\[PlatformName]*** > ***\[PlatformName] Users*** from the left-hand menu.
Some systems may have multiple records per user if they have multiple IDs
(e.g., Tableau has a user record with unique IDs ***per site***). Clicking into a user record will provide more details
about that user. You can also [sync a specific platform user](/users_groups/user_management/user_sync_and_membership_sync_overview)
from this page.

## Frontend Groups

Frontend groups are created within Curator and serve functionalities such as
[restricting access](/site_content_design/menus/restrict_access)
to navigation items or [overriding frontend styles based on group membership](/site_content_design/theme/group_overrides).
To access these groups, go to the backend and navigate to **Curator Backend** > **Settings** > **Users** > **Frontend Groups**.

### Creating Frontend Groups

Membership for frontend groups can be established by manually selecting users or by choosing one or more groups from
other platforms. If a group from another platform is chosen, the membership will automatically be reflected in the
frontend group.

For example, let's say you create a group called "Tableau Users" and select the "All Users" group from your Tableau
Server's default site. In this case, any user who logs in and has a Tableau user account from that site will be
automatically added to the "Tableau Users" frontend group.

#### Batch Create

If you want to create multiple Frontend Groups associated with one platform group each, you can use the batch create
functionality instead of repeating the create process:

1. Go to **Curator Backend** > **Settings** > **Users** > **Frontend Groups**.
2. Click the "Batch Create" button.
3. Select the sources from which you want to pull groups. This action doesn't create Frontend Groups; it only pulls in
   a list of available groups from the selected sources.
4. Click "Preview Available Frontend Groups".
5. Check the boxes next to each group you want to create. If you're having trouble finding the desired groups,
   you can sort the table by clicking on the column headers

## User and Membership Syncing

Curator needs to make API calls to your various platforms to keep the platform user information up to date.
This happens when a user logs into Curator to ensure they have the most current information. At the same time,
Curator checks if the user is in any platform groups associated with a frontend group and updates the membership accordingly.

Curator also provides the option to run a scheduled group sync for all frontend groups. You can find the settings for
this at **Curator Backend** > **Integrations** > **Global Settings**. By default, you can keep this set to "Never" as
the membership is updated on login.

Sometimes, the login process can be slow because the platform takes time to respond with the group information. If this
is the case, there is a feature called "Skip User Group Sync on Login" in **Integrations** > **Global Settings**.
Enabling this feature will skip the membership sync on login and only perform the platform user sync, which tends to be
quick across systems. When this feature is enabled, new users will be created during the scheduled group sync to ensure
they are already in their groups when they first log in to Curator.

***Note:*** We recommend **not** disabling the on-login membership sync unless the Curator login process is very slow.
Allowing the sync to happen on login ensures the most current membership for your users.

***Note:*** If you disable the on-login sync, you also **need to ensure a scheduled group sync is configured** to run.
Ideally, you should do this during low usage hours (e.g., midnight) to ensure group membership is fully synced by the
time users log in.


# Disabling Link-preview Security 
Source: https://docs.curator.interworks.com/users_groups/user_security/disabling_link_preview_security

Disable link preview security features when needed for specific use cases or legacy browser compatibility.

Curator will automatically check with the source system (e.g. Tableau) when a user logs in to determine their
access to linked content from those systems.  However, you can bypass this initial check and expose links to
all content to your users while still surfacing an
[Access Denied/403 page](/site_content_design/user_notifications_and_email/error_pages)
to prevent them from accessing content.

## Disabling link preview security

In order to disable security-checks on all content a user could see in the menu navigation system, or via a
tile/preview thumbnail:

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Tableau** > **Tableau Server Settings** section from the left-hand menu.
3. Click on the "Advanced" tab at the top of the page.
4. Enable the **Skip checking menu item's Dashboard permissions** and save your settings.
5. If you would like to set up a custom "access denied" page follow the instructions on the [Error Pages document](/site_content_design/user_notifications_and_email/error_pages).


# Frontend User Permissions
Source: https://docs.curator.interworks.com/users_groups/user_security/frontend_user_permissions

Configure and manage user access permissions for different content types and features within Curator.

In order to manage permissions on Curator, there are a few different ways to control access to content - it's largely
dependent upon which content type you're working with.  First, we'll begin with troubleshooting permission to discover
what a user should have access to.  Below that you'll find specific instructions on how to set permissions on specific content-types.

## Preview An Individual User's Access

In order to see what permissions a user has on Curator, you can preview a user's access via the Menu system.

1. Navigate to the backend of the system (e.g. `https://www.curatorexample.com/backend`).
2. Navigate to the **Settings** > **Users** > **Frontend Users** section from the left-hand menu.
3. Find the user that you would like to preview access for and click on the line containing their username.
4. On the Frontend User page click the "User Menu Access" button to view the a preview of the user's menu.  An icon next
   to each menu-link will show whether or not the user has access, and on hover will provide a reasoning why.

## Manage Permissions to Curator Content

Curator content does not have any inherent permissions - all automatic permissions are inherited from source systems that
Curator is connected to (e.g. Tableau permissions for embedded dashboards).  Creating a page without any embedded
analytic-content will result in global access for all your users.

When it comes to inheritance via the Menu, there is an exception to visible content: **Dropdown Placeholders** will only
display if the user has permissions to at least one item nested beneath the Dropdown.  If the user has access to none
of the items beneath the dropdown, it will not be visible to that user.  However, if you wish to apply permissions to a
specific piece of content, you can create a menu-link for that content and use the Group-based
[Restrict Access](/site_content_design/menus/restrict_access) option.  You
can find the steps below:

1. Navigate to the backend of the system (e.g. `https://www.curatorexample.com/backend`).
2. Navigate to the **Content** > **Navigation** section from the left-hand menu.
3. Click on the "+ New Menu Link" button to create a new menu item.
4. Fill out the form to select the content you'd like to link to, then scroll to the bottom of the page and enable the
   **[Restrict Access](/site_content_design/menus/restrict_access)** toggle.
5. Check the boxes next to the groups you would like to grant permission to.  **NOTE**: If you do not see any groups,
   see our [Groups document](/users_groups/user_management/users_and_groups_overview)
   on how to add new Frontend Groups.
6. Save the menu item to apply permissions.

With that said, if you would like Curator to assume all content is restricted by default, you can enable it globally by
visiting **Settings** > **Security** > **Authentication Settings** > **Customization** section >
**[Restrict Access](/site_content_design/menus/restrict_access) is Always Enabled**
setting.  You will still need to add groups to each piece of content to allow
users to access them.

## Manage Permissions to Analytic Content

When adding content from a source system (e.g. Tableau) Curator will automatically check the Analytic Connection when a
user logs in to determine their access.  If a user has been granted access in the source-system (e.g. Tableau Server),
then they will have access to it in Curator.  You can override these permissions using the steps in the
*Manage Permissions to Curator Content* above.

### Disabling security to preview content

You can expose all links to analytic content in Curator to your users by bypassing the initial security check, but then
expose an "access denied" message when they visit links.  For steps on how to set that up, see
[Preview Security Settings](users_groups/user_security/disabling_link_preview_security).

### Troubleshooting Access

If you believe a user is getting an incorrect permission-denial, visit the Event Logs on the backend and search the logs
for either "403" or the user's username.  Each time a user is denied access to a page Curator logs the reason why under
a 403 error.


# Password Change
Source: https://docs.curator.interworks.com/users_groups/user_security/password_change

Allow users to change their own passwords through the frontend interface for improved account security.

The Password Change feature allows frontend users to reset their password through Curator. *NOTE: This only works if you
have chosen Curator Users or Tableau Server as your Authentication Type in the* **Settings** > **Security** >
**Authentication Settings**.

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Settings** > **Curator** > **Portal Settings** in the left-hand menu.
4. On the **General** tab, scroll down to the **Security** section and expand it.
5. Toggle the switch **Password Change** on and click the "Save" button.


# Password Expiration and Complexity 
Source: https://docs.curator.interworks.com/users_groups/user_security/password_expiration_and_complexity

Configure password complexity requirements and expiration policies to enhance user account security.

For sites that use password change or password reset options you can now enable password expiration to force
frontend users to change their passwords on a frequent basis. To further bolster security, you can also
require users to have more complex passwords, requiring a specific length, numbers, and special characters.

***Please note that for these options to be able to be turned on, password reset or password change must be
enabled, and the site must be using Curator or Tableau for authentication.***

## Password Complexity Options

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
3. Click on the ‘General’ tab and expand the 'Security’ section.
4. Enable the toggle for **Password Complexity Options**.
5. Enter a minimum password length, and enable toggles for special character and require a number as desired.
6. Save your settings.

The new requirements will now appear on pages where you can change your password.

## Password Expiration

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
3. Click on the ‘General’ tab and expand the 'Security’ section.
4. Enable the toggle for **Enable Password Expiration**.
5. Enter the number of days until user passwords will expire
6. Save your settings.

Note, upon updating a Curator site to have these new settings password changed date will be set for all users
of the current day and time. This will prevent a flood of users having to change their passwords. Password
expiration is checked upon login.


# Password Reset 
Source: https://docs.curator.interworks.com/users_groups/user_security/password_reset

Enable self-service password reset functionality for users to regain account access without administrator intervention.

Some users want the ability to reset their Tableau Server account password from Curator. The Password Reset
feature can address that issue but will require some additional setup. To use this it is required that you
enable Tableau Server REST API, setup/configure an SMTP Server, enter the SMTP information into Curator and
ensure that the Tableau Server user has an associated email address on their Tableau Server account.

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Settings** > **Curator** > **Portal Settings** in the left-hand menu.
4. On the **General** tab, scroll to the **Security** section and expand it.
5. Toggle the **Password Reset** switch on and click the "Save" button.


# User Throttling 
Source: https://docs.curator.interworks.com/users_groups/user_security/user_throttling

Configure user request throttling and rate limiting to prevent system abuse and improve performance stability.

As a security measure, Curator throttles certain activities for a user to mitigate malicious activities.
Where possible, this blocks the logged in user.  If there is no logged in user, then it blocks the IP address
of the user.  For instance, logins only allow a limited number of failed attempts within a time period.  If
that limit is exceeded, the user's IP address is blocked for a period of time to help prevent someone from
brute forcing another user's password.

If Curator is behind a load balancer, reverse proxy, or some other network device that makes it look like all
users are sharing the same IP address, Curator won't be able to distinguish users by IP address so they'll
share the same throttle window when tracking activities that can't be tied to a logged in user.  In that
case, if there are several different users who all mistype their password within minutes of each other,
Curator will block all users from logging in.  If this becomes a recurring issue with your Curator site, the
potential fixes are:

* Fix your network device to pass through the IP address of each user instead of proxy-ing them as a single
  IP address.  See: [Reverse Proxy](/setup/proxy_configuration/reverse_proxy)
* Configure Curator's throttle to allow more failed attempts before triggering the throttle or a shorter
  suspension time after a throttle is triggered.

## Configuring Throttle

By default, Curator only allows 5 attempts within a 15 minute period and, if the throttle is triggered, there
is a 15 minute waiting period before the user is unblocked.

To customize these settings, navigate to **Backend** > **Settings** > **Security** >
**Authentication Settings** > **Customization** section.

The **activity throttle limit** determines how many attempts are allowed for throttle activities (failed
logins, password resets, etc.).

The **activity throttle reset period** determines how long the window is before the throttle count resets.
In other words, if the throttle limit is set to 5 and this setting is 15, then the user can only mistype
their password 5 times in a 15 minute window.  If they exceed that, then their account/IP address will be blocked.

The **activity suspension time** determines how long a user/IP address is blocked after the throttle is
triggered.  In other words, if the user is blocked due to failed login attempts and this setting is 30, the
user will need to wait 30 minutes before they are allowed to try logging in again.

## Clearing Suspensions

If you need to clear a suspension for any reason, you can do so by visiting **Backend** > **Settings** > **Security** >
**Suspensions**.  Find the record that needs to be cleared, check the box to the left of it, and click the delete button
at the top of the screen.


