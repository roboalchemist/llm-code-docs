# Source: https://docs.curator.interworks.com/creating_integrations/tableau_connection/embed_authentication.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Embed Authentication

> Configure secure authentication methods for embedding Tableau dashboards in Curator with single sign-on options.

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
