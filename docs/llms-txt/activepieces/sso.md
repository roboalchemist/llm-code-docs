# Source: https://www.activepieces.com/docs/security/sso.md

# Single Sign-On

<Snippet file="enterprise-feature.mdx" />

## Enforcing SSO

You can enforce SSO by specifying the domain. As part of the SSO configuration, you have the option to disable email and user login. This ensures that all authentication is routed through the designated SSO provider.

<img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/sso.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=36f19b78f46392cf25a2dd8656d3d90f" alt="SSO" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/sso.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/sso.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=f4bd7b419d0fadb83d39982bb589e86c 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/sso.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=65958659542c0230d5ca1891617dd2f6 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/sso.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=03431f73ceb60577d149ecb8f7de8c83 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/sso.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=a79b56ec6c0f486748f9c87b74ebf501 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/sso.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=96f01414d4221451bcd4b5576f600cff 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/sso.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=55b6a93c69bfee31129c6bdea8235112 2500w" />

## Supported SSO Providers

You can enable various SSO providers, including Google and GitHub, to integrate with your system by configuring SSO.

### Google:

<Steps>
  <Step title="Go to the Developer Console" />

  <Step title="Create an OAuth2 App" />

  <Step title="Copy the Redirect URL from the Configure Screen into the Google App" />

  <Step title="Fill in the Client ID & Client Secret in Activepieces" />

  <Step title="Click Finish" />
</Steps>

### GitHub:

<Steps>
  <Step title="Go to the GitHub Developer Settings" />

  <Step title="Create a new OAuth App" />

  <Step title="Fill in the App details and click Register a new application" />

  <Step title="Use the following Redirect URL from the Configure Screen" />

  <Step title="Fill in the Homepage URL with the URL of your application" />

  <Step title="Click Register application" />

  <Step title="Copy the Client ID and Client Secret and fill them in Activepieces" />

  <Step title="Click Finish" />
</Steps>

### SAML with OKTA:

<Steps>
  <Step title="Go to the Okta Admin Portal and create a new app" />

  <Step title="Select SAML 2.0 as the Sign-on method" />

  <Step title="Fill in the App details and click Next" />

  <Step title="Use the following Single Sign-On URL from the Configure Screen" />

  <Step title="Fill in Audience URI (SP Entity ID) with 'Activepieces'" />

  <Step title="Add the following attributes (firstName, lastName, email)" />

  <Step title="Click Next and Finish" />

  <Step title="Go to the Sign On tab and click on View Setup Instructions" />

  <Step title="Copy the Identity Provider metadata and paste it in the Idp Metadata field" />

  <Step title="Copy the Signing Certificate and paste it in the Signing Key field" />

  <Step title="Click Save" />
</Steps>

### SAML with JumpCloud:

<Steps>
  <Step title="Go to the JumpCloud Admin Portal and create a new app" />

  <Step title="Create SAML App" />

  <Step title="Copy the ACS URL from Activepieces and paste it in the ACS urls">
        <img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/acl-url.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=d7f62e7318652bbe11537dda4ddca5f3" alt="JumpCloud ACS URL" data-og-width="608" width="608" data-og-height="263" height="263" data-path="resources/screenshots/jumpcloud/acl-url.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/acl-url.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=9a1191ab5bde4eb2eba360ba7af814db 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/acl-url.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=9344cf812f7a202a51981fbeac50544d 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/acl-url.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=96f3c402c5d280d86b74a91082743c9a 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/acl-url.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=7015a842ce73840f1b7c07f482e8a438 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/acl-url.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=7aa35de4f66ff7864b7998affa7013eb 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/acl-url.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=c7e3856dd592069ad300d0188b6d7624 2500w" />
  </Step>

  <Step title="Fill in Audience URI (SP Entity ID) with 'Activepieces'" />

  <Step title="Add the following attributes (firstName, lastName, email)">
        <img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/user-attribute.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=0243c183611ae3ab374208725f7814ed" alt="JumpCloud User Attributes" data-og-width="599" width="599" data-og-height="368" height="368" data-path="resources/screenshots/jumpcloud/user-attribute.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/user-attribute.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=9fb7f5b67fc82613aeff7d7c3f0ceede 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/user-attribute.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=674e1f8521feb2bcf4553e8f8feac308 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/user-attribute.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=32104d11cd660681c84af754dc9036fc 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/user-attribute.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=b8894c36701e917f179bb9cb27a70173 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/user-attribute.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=1555a1c74092ef42d822823a2d58411e 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/user-attribute.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=7aed8876641785c56c8949a28cd275df 2500w" />
  </Step>

  <Step title="Include the HTTP-Redirect binding and export the metadata">
    JumpCloud does not provide the `HTTP-Redirect` binding by default. You need to tick this box.
    <img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/declare-login.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=891bb41c7e66420ab976016959bc2f22" alt="JumpCloud Redirect Binding" data-og-width="597" width="597" data-og-height="243" height="243" data-path="resources/screenshots/jumpcloud/declare-login.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/declare-login.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=d1148fa680d295d13064d86852d7d3cc 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/declare-login.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=7b97005f2b0ab717d8cf0d2193c2d3e3 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/declare-login.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=5614ad2fc17cf5b83dd35923b3043402 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/declare-login.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=9a23ecb850326cac6b7a1c716c460461 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/declare-login.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=0bfa94531658cac50b0f2a4c0e75bd7f 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/declare-login.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=bdbadbe645d0a25aaaa3aa03ec1cb4e1 2500w" />

    Make sure you press `Save` and then Refresh the Page and Click on `Export Metadata`

        <img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/export-metadata.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=3ba991481241c93ca5be2fe2d32174c1" alt="JumpCloud Export Metadata" data-og-width="618" width="618" data-og-height="250" height="250" data-path="resources/screenshots/jumpcloud/export-metadata.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/export-metadata.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=048119e60b4f613cb90f6c76e2d2d2f5 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/export-metadata.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=b2ca2a0fc41bf696785958707a740076 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/export-metadata.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=1e8182bab4cf800d1aedf46f43b63c2a 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/export-metadata.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=9bdec90ed3a27901439c9f280eaeddeb 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/export-metadata.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=c22cc7cd4197a6775995482a761a4aeb 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/export-metadata.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=00915125e7b80014525eda44ead8cc56 2500w" />

    <Tip>
      Please Verify ` Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect"` inside the xml.
    </Tip>

    After you export the metadata, paste it in the `Idp Metadata` field.
  </Step>

  <Step title="Copy the Certificate and paste it in the Signing Key field">
    Find the `<ds:X509Certificate>` element in the IDP metadata and copy its value. Paste it between these lines:

    ```
    -----BEGIN CERTIFICATE-----
    [PASTE THE VALUE FROM IDP METADATA]
    -----END CERTIFICATE-----
    ```
  </Step>

  <Step title="Make sure you Assigned the App to the User">
        <img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/user-groups.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=ec58a49538b08a0d97a72ab7a3dbdd66" alt="JumpCloud Assign App" data-og-width="939" width="939" data-og-height="526" height="526" data-path="resources/screenshots/jumpcloud/user-groups.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/user-groups.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=22b8ecba77376c52a043559ec8c5cbd3 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/user-groups.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=d9539e73d13f585eb444d72b14e638ae 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/user-groups.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=dff266c6731286720c420d6cb047267c 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/user-groups.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=ed455d0c87abd7e4f41c53b28367c62b 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/user-groups.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=3d9b6c62fa7ce2778a80504e6dad350e 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/user-groups.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=b22832eaec8cf2fbe46567a08c9c1f7f 2500w" />
  </Step>

  <Step title="Click Next and Finish" />
</Steps>
