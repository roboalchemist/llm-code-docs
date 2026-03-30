# Source: https://help.aikido.dev/code-scanning/connect-your-source-code/connect-gitlab-account-to-aikido/code-scanning-with-a-service-account-access-token.md

# Code Scanning with a Service Account Access Token

### ⚠️ Disclaimer

This guide is only available for **Gitlab Premium &** **Gitlab Ultimate** users. Check out our the setup with [personal access tokens](https://help.aikido.dev/code-scanning/connect-your-source-code/connect-gitlab-account-to-aikido/code-scanning-with-a-personal-access-token) for **Gitlab Free** users

### Introduction

You can use service account tokens which Aikido uses to perform the code scanning. You can update this token on the [update workspace access token](https://app.aikido.dev/onboarding/gitlab/update-workspace-access-token) page.

### Creating a Service Account and Access Token <a href="#creating-a-personal-access-token" id="creating-a-personal-access-token"></a>

1. Navigate to the "Service Accounts" settings page. Group > Settings > Service accounts

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FexZlH0U1ZIwXGlPdeewY%2Fimage.png?alt=media&#x26;token=185d5cc8-de72-486c-b753-e0d6adfadde3" alt="Gitlab group sidebar: highlighting &#x22;Service accounts&#x22; under the &#x22;Settings&#x22; option"><figcaption></figcaption></figure>

2. Click on "**Add service account**"

3. Give a **Name** and **Username** to the Service Account and click **Create**

4. Click the options of the newly created service account and select **Manage access tokens**

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FYKpNvN0JgtysQMCxsPbo%2Fimage.png?alt=media&#x26;token=0affb51b-44f0-4aa7-9f37-232f692a20a2" alt="Gitlab Service Accounts overview"><figcaption></figcaption></figure>

5. Click on "**Add new token**"

6. Enter a name for the token, remove the expiration date or set it to the max value and select the **api** scope

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fk7E9OtnoLgQOFdze1iMq%2FScherm%C2%ADafbeelding%202025-12-11%20om%2012.11.34.png?alt=media&#x26;token=8833dde6-ed95-4225-aa43-4eddea5f3a40" alt=""><figcaption></figcaption></figure>

7. Click on "**Create token**"

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FUrQEqurtCGh5y4ZdSQFB%2FScherm%C2%ADafbeelding%202025-12-11%20om%2012.15.09.png?alt=media&#x26;token=69832055-017e-4d4e-8989-00e3061e206a" alt=""><figcaption></figcaption></figure>

8. Copy the token and keep it for the "[update workspace access token](https://app.aikido.dev/onboarding/gitlab/update-workspace-access-token)" page

9. Go to the members page: **Group** > **Manage** > **Members**

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FJT588D1d6YCZREQyboZ3%2Fimage.png?alt=media&#x26;token=f455025a-ba12-46e1-85e0-b2781a2f9ec8" alt="Gitlab Group sidebar; showing members under the manage option"><figcaption></figcaption></figure>

10. Click "**Invite Members**"

11. Search for your new Service account created earlier and set role to "**Maintainer**"

    <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F8mKYveigtRhAs6s9H6cL%2Fimage.png?alt=media&#x26;token=835e40f5-43c2-4782-8edd-c3bdf2ced2bd" alt=""><figcaption></figcaption></figure>
