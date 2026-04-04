# Source: https://docs.startree.ai/corecapabilities/security/idp/google.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Google

> Configure Google as your Identity Provider (IdP) with StarTree. Leverage your existing Google Workspace or Cloud Identity for centralized authentication, enhanced security, and streamlined user management for StarTree.

## Prerequisites

1. Admin access to Google Cloud Console.
2. Access to a StarTree environment.
3. Obtain the redirect URI from StarTree.

## Steps

### Create an OAuth client

1. Access your Google Cloud Console.
2. Create a new project or open an existing project.
3. Create an Oauth app:
   a. Open **APIs & Services.**
   b. Click on **Credentials.**
   c. Click on **Create Credentials** > **Oauth client ID.**
   d. Select **Web application** as the application type.
   e. Enter a name for the application.
   f. Enter the authorized redirect URI provided by StarTree (this will be in the form of `https://identity.<env-id>.<org-id>.startree.cloud/callback`)

   <img src="https://mintcdn.com/startree/xe5mTwlEdZc68KYh/corecapabilities/security/images/google-authorized-redirect-uri.png?fit=max&auto=format&n=xe5mTwlEdZc68KYh&q=85&s=ba73e97d3cc14d0398927cf53e3a7617" alt="idp-google-authorized-redirect-uri.png" className="mx-auto" style={{ width:"74%" }} title="" width="942" height="767" data-path="corecapabilities/security/images/google-authorized-redirect-uri.png" />

   g. Copy the **Client ID** under **Additional information**. You will need to provide this to StarTree. h. Click **Create.**

### Fetching Groups from Google

To allow StarTree to fetch group information from Google, configure a service account. This account needs Domain-Wide Delegation and permission to access the `https://www.googleapis.com/auth/admin.directory.group.readonly` API scope.

<Note>
  To complete these steps, you’ll need an administrator account for a managed Google service, such as Google Workspace or Cloud Identity. [Learn more about Google accounts](https://support.google.com/a/answer/6375836?hl=en).
</Note>

To set up group fetching:

1. Follow [this guide](https://developers.google.com/workspace/guides/create-credentials#service-account) to set up a **service account** with Domain-Wide Delegation. Make sure that you:
   a. Generate the key as a JSON file. You will need to share the key file with StarTree.
   b. When setting up domain-wide delegation of authority for the service account, set the OAuth scope to [https://www.googleapis.com/auth/admin.directory.group.readonly](https://www.googleapis.com/auth/admin.directory.group.readonly). Only include the scope shown above, otherwise the setup will not work.
2. Enable the [Admin SDK](https://console.developers.google.com/apis/library/admin.googleapis.com/).
3. In the Google Admin Console, create or identify a Google Workspace user with a minimum of the Groups Reader role assigned, and provide this user ID to StarTree. The service account you created earlier will impersonate this user when making calls to the admin API. A valid user should be able to retrieve a list of groups when [testing the API](https://developers.google.com/admin-sdk/directory/v1/reference/groups/list#try-it).

Built with [Mintlify](https://mintlify.com).
