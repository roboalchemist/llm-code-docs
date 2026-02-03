# Source: https://www.mintlify.com/docs/dashboard/sso.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Single sign-on (SSO)

> Set up SAML or OIDC with identity providers for team authentication.

<Info>
  SSO is available on [Enterprise plans](https://mintlify.com/pricing?ref=sso).
</Info>

Use single sign-on to your dashboard via SAML and OIDC. If you use Okta, Google Workspace, or Microsoft Entra, we have provider-specific documentation for setting up SSO. If you use another provider, please [contact us](mailto:support@mintlify.com).

## Okta

<Tabs>
  <Tab title="SAML">
    <Steps>
      <Step title="Create an application">
        Under `Applications`, click to create a new app integration using SAML 2.0.
      </Step>

      <Step title="Configure integration">
        Enter the following:

        * Single sign-on URL (provided by Mintlify)
        * Audience URI (provided by Mintlify)
        * Name ID Format: `EmailAddress`
        * Attribute Statements:
          | Name        | Name format | Value            |
          | ----------- | ----------- | ---------------- |
          | `firstName` | Basic       | `user.firstName` |
          | `lastName`  | Basic       | `user.lastName`  |
      </Step>

      <Step title="Send us your IdP information">
        Once the application is set up, navigate to the sign-on tab and send us the metadata URL.
        We'll enable the connection from our side using this information.
      </Step>
    </Steps>
  </Tab>

  <Tab title="OIDC">
    <Steps>
      <Step title="Create an application">
        Under `Applications`, click to create a new app integration using OIDC.
        You should choose the `Web Application` application type.
      </Step>

      <Step title="Configure integration">
        Select the authorization code grant type and enter the Redirect URI provided by Mintlify.
      </Step>

      <Step title="Send us your IdP information">
        Once the application is set up, navigate to the General tab and locate the client ID & client secret.
        Please securely provide us with these, along with your Okta instance URL (for example, `<your-tenant-name>.okta.com`). You can send these via a service like 1Password or SendSafely.
      </Step>
    </Steps>
  </Tab>
</Tabs>

## Google Workspace

<Tabs>
  <Tab title="SAML">
    <Steps>
      <Step title="Create an application">
        Under `Web and mobile apps`, select `Add custom SAML app` from the `Add app` dropdown.

        <Frame>
                    <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-add-custom-saml-app.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=2c06c394d98ccd65df92aefceaeb75bd" alt="Screenshot of the Google Workspace SAML application creation page with the &#x22;Add custom SAML app&#x22; menu item highlighted" data-og-width="3804" width="3804" data-og-height="1860" height="1860" data-path="images/gsuite-add-custom-saml-app.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-add-custom-saml-app.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=58b064984b59e740ca9582b2a38cb0b5 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-add-custom-saml-app.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=f75867bfc7b0e654f04279d7a00bdec2 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-add-custom-saml-app.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=7d0fd19fd1ac1179f7aabad274a68e99 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-add-custom-saml-app.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=07236708f5e41547a94a37e66c329eee 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-add-custom-saml-app.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=370f4a956ba1cdc9a68462b30dcafbe4 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-add-custom-saml-app.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=86bf0fe1bd0cc718d664de30562572ad 2500w" />
        </Frame>
      </Step>

      <Step title="Send us your IdP information">
        Copy the provided SSO URL, Entity ID, and x509 certificate and send it to the Mintlify team.

        <Frame>
                    <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-saml-metadata.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=e9e47998599205dc051e9402cba63756" alt="Screenshot of the Google Workspace SAML application page with the SSO URL, Entity ID, and x509 certificate highlighted. The specific values for each of these are blurred out." data-og-width="3800" width="3800" data-og-height="1850" height="1850" data-path="images/gsuite-saml-metadata.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-saml-metadata.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=a469394b3fbf66b8d441e2a3e863da09 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-saml-metadata.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=1a301ea732963fff823ddce7e2eef92f 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-saml-metadata.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=00000d64cf4aacf28853dec9c7c91196 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-saml-metadata.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=ce6f9c692ca3c1c44c8d4c78f0640c55 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-saml-metadata.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=5b4eb469d04332f194a0c7f36a17c81e 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-saml-metadata.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=4d2ec0991511cfd65f6fe159954d53db 2500w" />
        </Frame>
      </Step>

      <Step title="Configure integration">
        On the Service provider details page, enter the following:

        * ACS URL (provided by Mintlify)
        * Entity ID (provided by Mintlify)
        * Name ID format: `EMAIL`
        * Name ID: `Basic Information > Primary email`

        <Frame>
                    <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-sp-details.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=a410a25f000fe2bc4d735a6ebe7754da" alt="Screenshot of the Service provider details page with the ACS URL and Entity ID input fields highlighted." data-og-width="3788" width="3788" data-og-height="1864" height="1864" data-path="images/gsuite-sp-details.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-sp-details.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=9aa71205fdffa7fd1fa0ae6f3e62bc40 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-sp-details.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=fbf8277d0af0c0bbbc20f75cd59b0087 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-sp-details.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=0ef2f4b39b42c91fc26b34082dc9f928 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-sp-details.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=98d60575ac7013ac2632d505a4d66a32 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-sp-details.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=1f97959e4cad04acfb8741400a701694 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-sp-details.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=b76f846f6f82dcb3d897e21786c8dc24 2500w" />
        </Frame>

        On the next page, enter the following attribute statements:

        | Google Directory Attribute | App Attribute |
        | -------------------------- | ------------- |
        | `First name`               | `firstName`   |
        | `Last name`                | `lastName`    |

        Once this step is complete and users are assigned to the application, let our team know and we'll enable SSO for your account!
      </Step>
    </Steps>
  </Tab>
</Tabs>

## Microsoft Entra

<Tabs>
  <Tab title="SAML">
    <Steps>
      <Step title="Create an application">
        1. Under "Enterprise applications," select **New application**.
        2. Select **Create your own application** and choose "Integrate any other application you don't find in the gallery (Non-gallery)."
      </Step>

      <Step title="Configure SAML">
        Navigate to the Single Sign-On setup page and select **SAML**. Under "Basic SAML Configuration," enter the following:

        * Identifier (Entity ID): The Audience URI provided by Mintlify.
        * Reply URL (Assertion Consumer Service URL): The ACS URL provided by Mintlify.

        Leave the other values blank and select **Save**.
      </Step>

      <Step title="Configure Attributes & Claims">
        Edit the Attributes & Claims section:

        1. Select **Unique User Identifier (Name ID)** under "Required Claim."
        2. Change the Source attribute to use `user.primaryauthoritativeemail`.
        3. Under Additional claims, create the following claims:
           | Name        | Value            |
           | ----------- | ---------------- |
           | `firstName` | `user.givenname` |
           | `lastName`  | `user.surname`   |
      </Step>

      <Step title="Send Mintlify your IdP information">
        Once the application is set up, navigate to the "SAML Certificates" section and send us the App Federation Metadata URL.
        We'll enable the connection from our side using this information.
      </Step>

      <Step title="Assign Users">
        Navigate to "Users and groups" in your Entra application and add the users who should have access to your dashboard.
      </Step>
    </Steps>
  </Tab>
</Tabs>
