# Source: https://docs.snowflake.com/en/connectors/microsoft/powerapps/collect-azure-ad-info.md

# Snowflake Connector for Microsoft Power Platform: Collect Azure AD information for Snowflake

To collect Azure AD information for Snowflake, follow these steps:

1. Navigate to the [Microsoft Azure Portal](https://portal.azure.com/) and authenticate.
2. Navigate to Azure Active Directory.
3. Select App Registrations.
4. Select the **Snowflake OAuth Resource** that was created in [Snowflake Connector for Microsoft Power Platform: Configure the OAuth resource in Microsoft Entra ID](configure-oauth.md).
5. In the Overview interface select Endpoints
6. On the right-hand side, copy the **OAuth 2.0 token endpoint (v2)** and note the URLs for **OpenID Connect metadata** and **Federation Connect metadata**.

   * The OAuth 2.0 token endpoint (v2) will be known as the `<AZURE_AD_OAUTH_TOKEN_ENDPOINT>` in the following configuration steps.
     The endpoint should be similar to `https://login.microsoftonline.com/<tenant-id>/oauth2/v2.0/token`.
   * For the **OpenID Connect metadata**, open in a new browser window.

     * Locate the `jwks_uri` parameter and copy its value.
     * This parameter value will be known as the `<AZURE_AD_JWS_KEY_ENDPOINT>` in the following configuration steps.
       :   The endpoint should be similar to `https://login.microsoftonline.com/<tenant-id>/discovery/v2.0/keys`.
   * For the Federation metadata document, open the URL in a new browser window.
   * Locate the `"entityID"` parameter in the `XML Root Element` and copy its value.
   * This parameter value will be known as the `<AZURE_AD_ISSUER>` in the following configuration steps. The entityID value should be similar to `https://sts.windows.net/<tenant-id>/`.

## Next steps

After completing these procedures, follow the steps in [Snowflake Connector for Microsoft Power Platform: Create a security integration](create-security-integration.md).
