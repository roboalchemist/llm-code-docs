# Source: https://help.cloudsmith.io/docs/single-sign-on-with-jumpcloud.md

# Single Sign-On with JumpCloud

This guide provides step-by-step instructions on setting up [JumpCloud](https://jumpcloud.com/) as a SAML IdP for your Cloudsmith Organization.

## Adding Cloudsmith to JumpCloud

Cloudsmith is not (yet) an integrated application in JumpCloud. You'll have to add Cloudsmith manually so you can configure SSO.

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">1</span></div>
  `}
</HTMLBlock>

Log in as an administrator to JumpCloud, choose **Applications** from the sidebar and use the green **+** icon to add a new application:

<Image align="center" width="80%" src="https://files.readme.io/c1598b2-pipFfKJ.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">2</span></div>
  `}
</HTMLBlock>

Choose the generic SAML connector (usually first in the list, labelled **SAML**) and hit **Configure**:

<Image align="center" width="80%" src="https://files.readme.io/b5ded7f-gSKo4qI.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">3</span></div>
  `}
</HTMLBlock>

On the configuration screen, enter the **Display Label** as "Cloudsmith", and optionally choose a colour for the application.

<Image align="center" width="80%" src="https://files.readme.io/5705a68-EvV1GHE.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">4</span></div>
  `}
</HTMLBlock>

Next, you'll need to choose an **IdP entity ID**, which is just a unique string used to identify this application/connector with JumpCloud. It doesn't matter what you use, so long as it's unique within your JumpCloud account. For example purposes we use "JumpCloud-Cloudsmith":

<Image align="center" width="80%" src="https://files.readme.io/4b4ae82-f5U5xlF.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">5</span></div>
  `}
</HTMLBlock>

For the next step, you'll need to generate a public and private key used to sign and secure communication between JumpCloud and Cloudsmith (if you don't already have them). JumpCloud have [their own docs](https://support.jumpcloud.com/customer/en/portal/articles/2775691-saml-configuration-notes#certs) on exactly how to generate these keys depending on your operating system. Once generated, upload the private and public keys using the next two fields in the form:

<Image align="center" width="80%" src="https://files.readme.io/010954d-HngkhoO.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">6</span></div>
  `}
</HTMLBlock>

Next, we'll fill in **SP Entity ID** and **ACS URL** with the same value. To determine the value we use the following format: `https://cloudsmith.io/orgs/MY_ORG_NAME/saml/acs/`, where "MY\_ORG\_NAME" is replaced with your organization's slug e.g. for the `cloudsmith` org we use `https://cloudsmith.io/orgs/cloudsmith/saml/acs/`:

<Image align="center" width="80%" src="https://files.readme.io/8e49768-hAcXDjT.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">7</span></div>
  `}
</HTMLBlock>

We then need to configure the SAML Name ID attribute. We want to choose `email` and the appropriate `emailAddress` format:

<Image align="center" width="80%" src="https://files.readme.io/6ac1691-dne84If.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">8</span></div>
  `}
</HTMLBlock>

Cloudsmith requires that users are identified by a first and last name, so we'll need to configure JumpCloud to send those too. Under **User Attributes** click **add attribute** and enter first/last name *exactly* as follows:

<Image align="center" width="80%" src="https://files.readme.io/c7d5fa2-tCKJUzh.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">9</span></div>
  `}
</HTMLBlock>

Almost there, we need to check the box labelled **Sign Assertion**:

<Image align="center" width="80%" src="https://files.readme.io/4f06940-YNKiBAY.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">10</span></div>
  `}
</HTMLBlock>

Check the box labelled **Declare redirect endpoint**:

<Image align="center" width="80%" src="https://files.readme.io/14d937d-Screen_Shot_2019-07-31_at_09.29.21.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">11</span></div>
  `}
</HTMLBlock>

And finally, choose an appropriate IdP URL, which must be unique in your account (`cloudsmith` is fine, unless you have more than one connector).

<Image align="center" width="80%" src="https://files.readme.io/12f15d0-eyaqxsG.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">12</span></div>
  `}
</HTMLBlock>

Hit the green **Activate** button in the bottom right to complete your configuration:

<Image align="center" width="80%" src="https://files.readme.io/6807aa0-HVGiBNc.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">13</span></div>
  `}
</HTMLBlock>

Your application is now configured on JumpCloud and you can add users and groups as required using the **Users** tab in the sidebar:

<Image align="center" width="80%" src="https://files.readme.io/7fddf0b-RaB77x7.png" />

## Providing configuration to Cloudsmith

Once configured as above, you'll need to provide metadata to Cloudsmith to connect to your newly configured IdP.

At the bottom-right of the form, right beside the **Activate** button from the previous step you'll see an **Export Metadata** button. Click it and an XML file containing metadata will be downloaded:

<Image align="center" width="80%" src="https://files.readme.io/78a10a8-MJw13iE.png" />

Take this file and add the XML contents to your [SAML settings](https://help.cloudsmith.io/docs/single-sign-on#enable-saml) in your Cloudsmith organization.

## All wrapped up!

The Cloudsmith application should now appear on the JumpCloud portal as normal:

<Image align="center" width="80%" src="https://files.readme.io/4bbef67-9T6Ib4y.png" />

You can then enable SAML in your Cloudsmith [SAML settings](https://help.cloudsmith.io/docs/single-sign-on#enable-saml).

You'll be able to access the landing page of your organization at the following URL:\
[https://cloudsmith.io/orgs/ORG/saml/login/](https://cloudsmith.io/orgs/ORG/saml/login/)

Where *ORG* is your organization's slug/identifier (what you would normally see in the URL when accessing your organization within Cloudsmith).