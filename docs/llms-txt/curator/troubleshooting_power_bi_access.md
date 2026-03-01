# Source: https://docs.curator.interworks.com/creating_integrations/power_bi_connection/troubleshooting_power_bi_access.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting Power BI Access

> Common issues and solutions for Power BI connection problems in both frontend and backend access scenarios.

export const BackendNavPath = ({levelOne, levelTwo, levelThree, tab, section}) => {
  const levels = [levelOne, levelTwo, levelThree].filter(Boolean);
  const lastLevel = levels.length ? levels[levels.length - 1] : '';
  return <span>
      In the <a href="/setup/installation/linux_installation">backend of Curator</a> using the left-hand navigation,
      navigate to the
      {levelOne && <strong>{" " + levelOne}</strong>}
      {levelOne && levelTwo && " > "}
      {levelTwo && <strong>{levelTwo}</strong>}
      {levelTwo && levelThree && " > "}
      {levelThree && <strong>{levelThree}</strong>} page.
      {(tab || section) && <>
          {" "}On the {lastLevel} page
          {tab && <> click the <strong>{tab}</strong> tab</>}
          {tab && section && " and"}
          {section && <> expand the <strong>{section}</strong> section</>}.
        </>}
    </span>;
};

Power BI connections have separate frontend and backend functionality, even though everything is configured from the
backend connection. When troubleshooting issues, it's important to test each area separately since one might work
perfectly while the other fails completely.

***

## Backend Troubleshooting

The backend integration with Power BI is straightforward - there's one reliable way to test it and only a few common
failure points.

### Test if Backend is Working

Follow these steps to verify your backend connection:

1. <BackendNavPath levelOne="Power BI" levelTwo="Reports" />

2. Click the **Clear Cache** button (top right) to ensure fresh data.

3. Click the **New Report** button to navigate to the "Create Report" page.

4. Use the dropdown menus to select a workspace and report

   * **Success:** If you can select both workspace and report, your backend is working! Skip to the
     [Frontend section](#frontend-troubleshooting)
   * **Problem:** If either dropdown is empty when it shouldn't be, continue to the troubleshooting steps below

<img src="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/creating_integrations/power_bi_connection/troubleshooting_power_bi_access_success.png?fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=f913983afee72a2a025ec879dfadc93b" alt="Power BI Backend Success" data-og-width="1114" width="1114" data-og-height="764" height="764" data-path="assets/images/creating_integrations/power_bi_connection/troubleshooting_power_bi_access_success.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/creating_integrations/power_bi_connection/troubleshooting_power_bi_access_success.png?w=280&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=bcf0767f6b8e82620deecc9dfd78d526 280w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/creating_integrations/power_bi_connection/troubleshooting_power_bi_access_success.png?w=560&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=55f3c8fb3e9246425e800d9a4bc81f0f 560w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/creating_integrations/power_bi_connection/troubleshooting_power_bi_access_success.png?w=840&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=5a989d2341de843debde19fb7ba0961e 840w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/creating_integrations/power_bi_connection/troubleshooting_power_bi_access_success.png?w=1100&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=8591e6eb3fe75299da03684df0bc9069 1100w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/creating_integrations/power_bi_connection/troubleshooting_power_bi_access_success.png?w=1650&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=dceb9beae854241ede2cd1c3f7bf4c3d 1650w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/creating_integrations/power_bi_connection/troubleshooting_power_bi_access_success.png?w=2500&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=34b0374fe8c34d2b79ed304872e4c12a 2500w" />

### Debug Backend Issues

When the backend isn't working, you need to see what Power BI is actually telling Curator.

#### Enable Debug Mode

1. <BackendNavPath levelOne="Integrations" levelTwo="Connections" /> Find your Power BI connection and click the one you'd like to troubleshoot.

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
   1. <BackendNavPath levelOne="Settings" levelTwo="Logs" levelThree="Event Logs" />

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

1. <BackendNavPath levelOne="Integrations" levelTwo="Connections" /> From this list, find the Power BI connection you're troubleshooting and click to open it.  Enable the
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
   * <BackendNavPath levelOne="Settings" levelTwo="Logs" levelThree="Event Logs" />
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
