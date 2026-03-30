# Source: https://docs.api7.ai/enterprise/3.2.16.7/best-practices/configure-sso-with-microsoft-entra-id.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/best-practices/configure-sso-with-microsoft-entra-id.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/best-practices/configure-sso-with-microsoft-entra-id.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/best-practices/configure-sso-with-microsoft-entra-id.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/best-practices/configure-sso-with-microsoft-entra-id.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/best-practices/configure-sso-with-microsoft-entra-id.md

# Source: https://docs.api7.ai/enterprise/3.7.x/best-practices/configure-sso-with-microsoft-entra-id.md

# Source: https://docs.api7.ai/enterprise/3.6.x/best-practices/configure-sso-with-microsoft-entra-id.md

# Source: https://docs.api7.ai/enterprise/3.5.x/best-practices/configure-sso-with-microsoft-entra-id.md

# Source: https://docs.api7.ai/enterprise/3.4.x/best-practices/configure-sso-with-microsoft-entra-id.md

# Source: https://docs.api7.ai/enterprise/3.3.x/best-practices/configure-sso-with-microsoft-entra-id.md

# Configure SSO with Microsoft Entra ID (Azure AD)

[Microsoft Entra ID (formerly Azure AD)](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id) is Microsoft's cloud-based identity and access management service. It allows organizations to securely manage and authenticate users and devices, ensuring that the right individuals have the appropriate access to company resources. Microsoft Entra ID offers features such as single sign-on (SSO), multi-factor authentication (MFA), and integration with various third-party applications.

The guide will show you how to integrate API7 Enterprise with Microsoft Entra ID to implement SSO and configure the needed access controls.

Below is an interactive demo that provides a hands-on introduction to integrating Microsoft Entra ID with API7 Enterprise.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

1. [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md).
2. [Have at least one gateway instance in your gateway group](https://docs.api7.ai/enterprise/3.3.x/getting-started/add-gateway-instance.md).
3. Have an [Azure](https://signup.azure.com/) account with an active subscription.

## Configure Azure[â](#configure-azure "Direct link to Configure Azure")

### Register an App[â](#register-an-app "Direct link to Register an App")

Log in to the [Azure portal](https://portal.azure.com/), go to **Microsoft Entra ID**, and select **App registrations**Â under the **Manage** dropdown to register a new app:

![azure-ad-register-an-app](https://static.api7.ai/uploads/2024/08/06/1984lYFs_azure-new-app-resgistration-btn.png)

Fill out the details for the app and click **Register**:

![fill-out-new-app-info](https://static.api7.ai/uploads/2024/08/06/pjM2IzhF_azure-register-new-app.png)

### Create an App Client Secret[â](#create-an-app-client-secret "Direct link to Create an App Client Secret")

Once the app is registered, select **Certificates & secrets** under the **Manage** dropdown to create a client secret:

![create-app-client-secret](https://static.api7.ai/uploads/2024/08/06/PBk3U44l_azure-create-app-client-secret.png)

Fill out the client secret details and click **Add**:

![fill-out-client-secret-details](https://static.api7.ai/uploads/2024/08/06/TRQorSBs_azure-fill-out-client-secret-details.png)

The client secret should now be generated. Save the secret to a secure location so that you can refer to it later for API7 Enterprise configuration. Note that you can only view the secret once.

![save-client-secret](https://static.api7.ai/uploads/2024/08/06/Mzj9BuGU_azure-app-copy-client-secret.png)

### Create an App Role[â](#create-an-app-role "Direct link to Create an App Role")

Select **App roles** under the **Manage** dropdown to create a new `SuperAdmin` app role. Fill out the role details and click **Apply**:

![create-app-role](https://static.api7.ai/uploads/2024/08/06/WIdPGRBl_azure-create-app-role.png)

You should see the role created and enabled.

### Assign the App Role to User[â](#assign-the-app-role-to-user "Direct link to Assign the App Role to User")

Select **Enterprise applications** under the **Manage** dropdown:

![select-enterprise-applications](https://static.api7.ai/uploads/2024/08/06/zgabhpPP_azure-enterprise-applications.png)

You should now be redirected to a page showing all apps. Select the app created earlier:

![select-the-enterprise-app](https://static.api7.ai/uploads/2024/08/06/VT091U0n_azure-view-created-app.png)

You should now be redirected to the app overview page. Select **Users and groups** under the **Manage** dropdown and click **Add user/group**:

![add-user-group](https://static.api7.ai/uploads/2024/08/06/4lGsDKg9_azure-add-users-groups.png)

Select the appropriate IAM user to be allowed to sign into API7 Dashboard as the super admin and assign the `SuperAdmin` role created earlier. Click **Assign**:

![assign-role-to-user](https://static.api7.ai/uploads/2024/08/06/yRhKP6ej_azure-assign-role-to-user.png)

You should see the role assigned:

![assigned-role](https://static.api7.ai/uploads/2024/08/06/IwWwN6UA_azure-super-admin-role-assigned-masked.png)

## Configure API7[â](#configure-api7 "Direct link to Configure API7")

Log into the API7 Dashboard using an account with admin rights.

### Add Login Option[â](#add-login-option "Direct link to Add Login Option")

Under **Organization** dropdown, click **Settings**, and select **Add Login Option**:

![add-login-option](https://static.api7.ai/uploads/2024/08/06/m7Bltn0z_dashboard-add-login-option.png)

Fill out the **Name**, select **OIDC** as the provider, and populate **Issuer** and **Client ID** based on the app information:

![fill-out-login-details](https://static.api7.ai/uploads/2024/08/20/SY5wQNX6_login-option-issuer.jpeg)

note

The issuer URL should not include `/.well-known/openid-configuration`.

The issuer can be found in Azure by clicking **Endpoints** and copying the **OpenID Connect metadata document**:

![dashboard-oidc-issuer-and-endpoint-in-azure](https://static.api7.ai/uploads/2024/08/06/5UAdCtml_azure-get-oidc-endpoint.png)

Continue to fill out the **Client Secret** previously saved:

![dashboard-oidc-client-secret](https://static.api7.ai/uploads/2024/08/06/LGjTLNPq_dashboard-enter-client-secret.png)

as well as the rest of the information:

![dashboard-oidc-scopes-root-url-attributes-mapping](https://static.api7.ai/uploads/2024/08/07/dWH6SMdA_dashboard-configure-oidc.png)

Once finished, click **Add**. You should see the login provider successfully provisioned.

### Enable Role Mapping[â](#enable-role-mapping "Direct link to Enable Role Mapping")

Enable **Role Mapping** for the newly created login provider:

![enable-role-mapping](https://static.api7.ai/uploads/2024/08/07/PCqIG4dU_dashboard-enable-role-mapping.png)

Fill out the details and click **Enable**:

![fill-out-role-mapping-details](https://static.api7.ai/uploads/2024/08/07/n0smXIOR_dashboard-role-mapping.png)

The roles should now have been updated.

## Update Callback URL[â](#update-callback-url "Direct link to Update Callback URL")

The callback URL is the address that the application redirects users to upon a successful authentication with Microsoft Entra ID.

Find the callback URL in the provider configuration:

![dashboard-find-callback-url](https://static.api7.ai/uploads/2024/08/07/ibttrqWh_dashboard-callback-url.png)

In Azure portal, navigate to the app overview and click **Add a Redirect URI**:

![azure-add-redirect-url](https://static.api7.ai/uploads/2024/08/06/bV2FJEkt_azure-app-registration-overview.png)

Click the **Authentication** tab and click **Add a platform**. Choose **Web** application type and enter the redirect URI:

![add-a-platform-web](https://static.api7.ai/uploads/2024/08/06/jMzG0LxU_configure-web.png)

## Verify SSO[â](#verify-sso "Direct link to Verify SSO")

Sign out from the API7 Dashboard and visit the login page again, you should now see an option to log in with Microsoft Entra ID:

![login box with SSO option](https://static.api7.ai/uploads/2024/08/08/MP9Kpx4L_entra-id.png)

You should now be able to sign in with your Microsoft account.

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts
  <!-- -->
  * [Roles and Permission Policies](https://docs.api7.ai/enterprise/3.3.x/key-concepts/roles-and-permission-policies.md)

* Getting Started
  <!-- -->
  * [Create Custom Role](https://docs.api7.ai/enterprise/3.3.x/getting-started/create-custom-role.md)

* Reference

  <!-- -->

  * [Permission Policy Actions and Resources](https://docs.api7.ai/enterprise/3.3.x/reference/permission-policy-action-and-resource.md)
  * [Permission Policy Examples](https://docs.api7.ai/enterprise/3.3.x/reference/permission-policy-examples.md)
