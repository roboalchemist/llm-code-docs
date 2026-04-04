# Source: https://docs.curator.interworks.com/creating_integrations/tableau_connection/tableau_connection_troubleshooting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Tableau Connection Troubleshooting

> Debug and resolve common Tableau connection issues including networking problems, authentication errors and API connectivity.

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

   ```xml  theme={null}
   <?xml version="1.0" encoding="utf-8"?><tsRequest><credentials name="" password=""><site contentUrl=""/></credentials></tsRequest>
   ```

   Personal Access Token (PAT):

   ```xml  theme={null}
   <?xml version="1.0" encoding="utf-8"?><tsRequest><credentials personalAccessTokenName="" personalAccessTokenSecret=""><site contentUrl=""/></credentials></tsRequest>
   ```

7. Fill in the username/password or PAT name/secret, and site content URL details within the above XML.

8. Click the **Send** button.

You should get back XML with a credentials session token and the site and user IDs.
<img src="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/creating_integrations/tableau_connection/postman-screenshot.png?fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=cd86ce78d8c1e36743268ed1bdd0ca5d" alt="Postman Screenshot" data-og-width="1005" width="1005" data-og-height="452" height="452" data-path="assets/images/creating_integrations/tableau_connection/postman-screenshot.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/creating_integrations/tableau_connection/postman-screenshot.png?w=280&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=83074158cfa7f673a1c62998e0cc919c 280w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/creating_integrations/tableau_connection/postman-screenshot.png?w=560&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=480a6e1ef1474a5ac173421a41b769ed 560w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/creating_integrations/tableau_connection/postman-screenshot.png?w=840&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=d86eb6974b2de7c55af95c1c2b9d30d6 840w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/creating_integrations/tableau_connection/postman-screenshot.png?w=1100&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=697a3dfaa7ecad84ef02a0450b92aab4 1100w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/creating_integrations/tableau_connection/postman-screenshot.png?w=1650&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=9cc47e60225dce55c59158efe46cd93c 1650w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/creating_integrations/tableau_connection/postman-screenshot.png?w=2500&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=17eb36430dc87817b25245dd7084c468 2500w" />

If needed, use the credentials session token from this response to make subsequent API calls to Tableau.  Open the
headers tab for the request and add an entry where the key is `X-Tableau-Auth` and the value is your credentials session
token.  If this token expires, you'll need to make a new request to the signin end point to get a new token.
