# Source: https://redocly.com/docs/realm/reunite/organization/sso/configure-auth0.md

# Configure SSO with Auth0 OIDC

Follow this guide to configure an SSO integration between Auth0 OpenID Connect protocol and Reunite.

**Important:** Before completing the Reunite setup, ensure you preserve the Owner organization role (see "Preserve the Owner organization role" section) to avoid getting locked out of your organization.

## Add Auth0 as a corporate identity provider in Reunite

1. In Reunite, navigate to your organization's **Overview** page.
2. Select **SSO and login** in the navigation menu on the left side of the page.
3. Click **Add** in the Guest or Corporate Identity Provider section.
4. Select **OpenID Connect**.
5. Enter a name for your identity provider.
6. Select the default **Organization Role** for users who log in with the identity provider.
7. (Optional) Enter the name of the **Default Team**.
8. Copy the **Callback URL**.
Keep this tab open and continue with the Auth0 configuration in a new tab.


## Create an application in Auth0

1. Log in to Auth0 and select **Applications** from the menu on the left side of the page.
2. Click **Create Application**.
3. Choose **Regular Web Applications**, and click **Create**.


## Copy settings between Auth0 and Reunite

1. In Auth0's **Application Settings** tab, scroll to **Application URIs** and paste the previously copied callback URL into the **Allowed Callback URLs** field.
2. Click the **Save Changes** button.
3. Scroll to **Advanced Settings** > **Endpoints**, copy the **OpenID Configuration**, and paste it in Reunite into the **Configuration (.well-known)** field.
4. In Auth0, scroll to **Basic Information**, copy the **Client ID** and **Client Secret**, and paste them into Reunite.
5. In Reunite's **RBAC Teams Claim Name** field, enter `https://redocly.com/sso/teams`.


## Preserve the Owner organization role

**Critical step:** Complete this step before clicking **Save** in Reunite to prevent getting locked out of your organization.

To prevent Auth0 from changing users' roles to the default organization role specified in the SSO settings:

1. In Auth0, navigate to **User Management** > **Roles**.
2. Create a role named `redocly.owners`.
3. Navigate to **Users** > **Roles** and assign the `redocly.owners` role to users with an Owner role in your organization.
4. Return to Reunite and click **Save** to complete the identity provider setup.


## Setup an Action for your application

1. In Auth0, navigate to **Actions** > **Library**, then click **Create Action** and select **Build from Scratch**.
2. Add a name for your action.
3. In the **Trigger** drop-down, select **Login/Post Login**.
4. Click **Create**.
5. Add the following code to the action and click **Deploy**:

```js
exports.onExecutePostLogin = async (event, api) => {
const namespace = 'https://redocly.com/sso';
if (event.authorization && event.authorization.roles) {
  api.idToken.setCustomClaim(`${namespace}/teams`, event.authorization.roles);
}
};
```
6. Navigate to **Actions** > **Triggers**, and select **post-login**.
7. Click **Add Action**, select the **Custom** tab, and drag and drop your action between **Start** and **Complete**.
8. Click **Apply**.


## Resources

- **[Single sign-on (SSO) concepts](/docs/realm/reunite/organization/sso/sso)** - Understand different identity provider types in Reunite and how they integrate with your project authentication
- **[Add an identity provider](/docs/realm/reunite/organization/sso/add-idp)** - Step-by-step guide for adding identity providers in Reunite for centralized authentication management
- **[Configure SSO](/docs/realm/reunite/organization/sso/configure-sso)** - Enable multiple identity provider types to give users flexible authentication options for your projects