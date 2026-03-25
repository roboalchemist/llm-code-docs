# Source: https://help.cloudsmith.io/docs/single-sign-on-with-onelogin.md

# Single Sign-On with OneLogin

This guide provides step-by-step instructions on setting up OneLogin as a SAML IdP for your Cloudsmith Organization.

This guide provides step-by-step instructions on setting up [OneLogin](https://www.onelogin.com/) as a SAML IdP for your Cloudsmith Organization.

## Adding Cloudsmith to OneLogin

Cloudsmith is not yet an integrated application in OneLogin. You'll have to add Cloudsmith manually so you can configure SSO.

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">1</span></div>
  `}
</HTMLBlock>

Log into OneLogin and click **Administration** in the top right:

<Image align="center" width="80%" src="https://files.readme.io/82cb58d-cloudsmith-one-login-1.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">2</span></div>
  `}
</HTMLBlock>

Choose **Applications** from the top menu:

<Image align="center" width="80%" src="https://files.readme.io/34b72c5-cloudsmith-one-login-2.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">3</span></div>
  `}
</HTMLBlock>

Click the blue **Add App** button in the top right:

<Image align="center" width="80%" src="https://files.readme.io/86bddab-cloudsmith-one-login-3.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">4</span></div>
  `}
</HTMLBlock>

Search for "SAML test connector" and choose "SAML Test Connector (Advanced)":

<Image align="center" width="80%" src="https://files.readme.io/0027387-cloudsmith-one-login-4.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">5</span></div>
  `}
</HTMLBlock>

On the next screen (**Add SAML Test Connector (Advanced)**), enter the **Display Name** as "Cloudsmith". (You can optionally add the Cloudsmith logo too for easier visibility, you can find hi-res versions of the logo [here](https://cloudsmith.com/company/brand)):

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">6</span></div>
  `}
</HTMLBlock>

Click the blue **Save** button in the top right:

<Image align="center" width="80%" src="https://files.readme.io/3e15f56-cloudsmith-one-login-6.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">7</span></div>
  `}
</HTMLBlock>

Once saved, a number of additional options will appear in the sidebar. Click "Configuration":

<Image align="center" width="80%" src="https://files.readme.io/adeced6-cloudsmith-one-login-7.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">8</span></div>
  `}
</HTMLBlock>

Next, we'll configure SAML settings. To determine your **Single sign on URL** we use the following format: "[https://cloudsmith.io/orgs/MY\_ORG\_NAME/saml/acs/"](https://cloudsmith.io/orgs/MY_ORG_NAME/saml/acs/"), where "MY\_ORG\_NAME" is replaced with your organization's slug.\
We use this URL for the **Audience**, **Recipient**, and **ACS (Consumer) URL** values in the form below.

For **ACS (Consumer) URL Validator** use ".\*".

<Image align="center" width="80%" src="https://files.readme.io/21f39b8-Screen_Shot_2019-07-16_at_00.26.21.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">9</span></div>
  `}
</HTMLBlock>

Further down the page, for **SAML signature element** choose "Assertion".

<Image align="center" width="80%" src="https://files.readme.io/9e74fe9-cloudsmith-one-login-9.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">10</span></div>
  `}
</HTMLBlock>

Hit the blue **Save** button at the top of the page.

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">11</span></div>
  `}
</HTMLBlock>

Next, we'll configure OneLogin to also send the user's first and last names during sign-in.

Click on **Parameters** in the sidebar, and then the small blue "+" symbol on the right:

<Image align="center" width="80%" src="https://files.readme.io/24cfb10-1.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">12</span></div>
  `}
</HTMLBlock>

Add a new parameter named "FirstName" and ensure the box labelled "Include in SAML assertion" is checked:

<Image align="center" width="80%" src="https://files.readme.io/af16926-11.png" />

Hit the blue **Save** button. Then choose **First Name** from the drop-down presented:

<Image align="center" width="80%" src="https://files.readme.io/faf1d96-cloudsmith-one-login-11.png" />

Hit the blue **Save** button.

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">13</span></div>
  `}
</HTMLBlock>

Repeat the above process for the "LastName" attribute.

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">14</span></div>
  `}
</HTMLBlock>

Hit the blue **Save** button in the top-right to save all changes. Once configured, the parameters should appear as below:

<Image align="center" width="80%" src="https://files.readme.io/08c9329-image.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">15</span></div>
  `}
</HTMLBlock>

Choose the **SSO** tab in the sidebar and change the **SAML Signature Algorithm** to "SHA-256".

<Image align="center" width="80%" src="https://files.readme.io/fa71597-cloudsmith-one-login-12.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">16</span></div>
  `}
</HTMLBlock>

Hit the blue **Save** button in the top-right to save all changes.

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">17</span></div>
  `}
</HTMLBlock>

Your application is now configured on OneLogin and you can add users groups as required using the **Users** tab in the sidebar:

<Image align="center" width="80%" src="https://files.readme.io/43482ad-cloudsmith-one-login-13.png" />

## Providing configuration to Cloudsmith

Once configured as above, you'll need to provide metadata to Cloudsmith to connect to your newly configured IdP.

In the **SSO** tab of your configuration screen you should see a link that provides metadata for dynamic configuration. This is named **Issuer URL**:

<Image align="center" width="80%" src="https://files.readme.io/32b32f1-cloudsmith-one-login-14.png" />

Copy this link and add it to your Cloudsmith organization [SAML settings](https://help.cloudsmith.io/docs/single-sign-on#enable-saml).

## All wrapped up!

Your application should now appear on the OneLogin portal.

You can then enable SAML authentication in your Cloudsmith [SAML settings](https://help.cloudsmith.io/docs/single-sign-on#enable-saml) and you can use OneLogin to begin logging in straight away.

You'll be able to access the landing page of your organization at the following URL:\
[https://cloudsmith.io/orgs/ORG/saml/login/](https://cloudsmith.io/orgs/ORG/saml/login/)

Where *ORG* is your organization's slug/identifier (what you would normally see in the URL when accessing your organization within Cloudsmith).