# Source: https://help.cloudsmith.io/docs/single-sign-on-with-azure-ad.md

# Single Sign-On with Microsoft Entra ID (formerly Azure Active Directory)

This guide provides step-by-step instructions on setting up [Microsoft Entra ID](https://www.microsoft.com/en-gb/security/business/identity-access/microsoft-entra-id) as a SAML IdP for your Cloudsmith Organization.

## Adding Cloudsmith to Azure AD

Cloudsmith is not (yet) an integrated application in Azure AD. You'll have to add Cloudsmith manually so you can configure SSO.

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">1</span></div>
  `}
</HTMLBlock>

Log into the Azure portal as an admin and click **Azure Active Directory** in the left menu, then **Enterprise Applications** in the menu that appears:

<Image align="center" width="80%" src="https://files.readme.io/eed4fe7-cloudsmith-azure-ad-1.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">2</span></div>
  `}
</HTMLBlock>

Choose + **New application** from the top menu:

<Image align="center" width="80%" src="https://files.readme.io/c5faa5f-cloudsmith-azure-ad-2.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">3</span></div>
  `}
</HTMLBlock>

Click **Non-gallery application** and enter "Cloudsmith" in the "Name" box:

<Image align="center" width="80%" src="https://files.readme.io/8bac474-cloudsmith-azure-ad-3.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">4</span></div>
  `}
</HTMLBlock>

Click the blue **Add** button at the bottom of the page. After a short processing delay, you'll be redirected to the overview page for your new application.

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">5</span></div>
  `}
</HTMLBlock>

Select **Single sign-on** from the left menu and choose **SAML**:

<Image align="center" width="80%" src="https://files.readme.io/76a302f-cloudsmith-azure-ad-4.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">6</span></div>
  `}
</HTMLBlock>

Next, we'll configure SAML settings. Click the pencil symbol beside **Basic SAML Configuration** to begin editing:

<Image align="center" width="80%" src="https://files.readme.io/19dfed2-cloudsmith-azure-ad-5.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">7</span></div>
  `}
</HTMLBlock>

To determine your **Identifier** and **Reply URL** (we use the same value for both) we use the following format: "[https://cloudsmith.io/orgs/MY\_ORG\_NAME/saml/acs/"](https://cloudsmith.io/orgs/MY_ORG_NAME/saml/acs/"), where "MY\_ORG\_NAME" is replaced with your organization's slug.

<Image align="center" width="80%" src="https://files.readme.io/10fe416cba7799cfdce5c61422b2591a55688a8738dee70e1c8fcc002835626e-482a011-cloudsmith-entra-id-6.png" />

Hit the **Save** button at the top of the page.

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">8</span></div>
  `}
</HTMLBlock>

Next, we'll configure Azure to also send the user's first and last names during sign-in. Click the pencil icon on the **User Attributes & Claims** section:

<Image align="center" width="80%" src="https://files.readme.io/66f29c5-cloudsmith-azure-ad-7.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">9</span></div>
  `}
</HTMLBlock>

Remove all attributes *except* the **Name identifier value**, the screen should look as below:

<Image align="center" width="80%" src="https://files.readme.io/5aabb6f-cloudsmith-azure-ad-8.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">10</span></div>
  `}
</HTMLBlock>

Next, we'll add first and last names to the attributes sent to Cloudsmith. Click + **Add new claim** at the top of the page, and add **FirstName** as follows:

<Image align="center" width="80%" src="https://files.readme.io/6a5ba58-cloudsmith-azure-ad-9.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">11</span></div>
  `}
</HTMLBlock>

Repeat the process for **LastName** and hit **Save**. The attributes screen should now look as below:

<Image align="center" width="80%" src="https://files.readme.io/d168a64-cloudsmith-azure-ad-10.png" />

<HTMLBlock>
  {`
  <div class="cs-step"><span class="cs-step-desc cs-swatch-midnight-blue">Step</span><span class="cs-step-number cs-swatch-action-blue">12</span></div>
  `}
</HTMLBlock>

Finally, we'll need to add any users that need to be able to access the application. Click **Users and groups** in the left sidebar and then **+Add user**. You can add as many users or groups as needed:

<Image align="center" width="80%" src="https://files.readme.io/6a260ed-cloudsmith-azure-ad-11.png" />

## Providing configuration to Cloudsmith

Once configured as above, you'll need to provide metadata to Cloudsmith to connect to your newly configured IdP.

Go back to the **Single sign-on** tab in the sidebar, you should see, in section **3 (SAML Signing Certificate)** a link that provides metadata for dynamic configuration, it is labelled **App Federation Metadata Url**.

Copy this link and add it to your SAML configuration in your [Cloudsmith organization settings](https://help.cloudsmith.io/docs/single-sign-on#enable-saml)

<Image align="center" width="80%" src="https://files.readme.io/fc07a79-cloudsmith-azure-ad-12.png" />

## SAML Group Sync

Once SAML has been setup, you can then use Azure AD and Cloudsmith's group mapping in order to import your teams into Cloudsmith.

To get started, head into your Cloudsmith Enterprise applicaiton on Azure and select "Single sign-on", then click on "Edit" under "Attributes & Claims":

<Image align="center" className="border" border={true} src="https://files.readme.io/9bcf573-Screenshot_2023-04-04_at_13.31.53.png" />

Select "Add a group claim":

<Image align="center" className="border" border={true} src="https://files.readme.io/7b4aac5-Screenshot_2023-04-04_at_13.36.03.png" />

Select "Security Groups" from the sidebar menu and click "Save", if your AD grouping is setup in a different way, you may choose the relevant fields that suit your infrastructure.

<Image align="center" className="border" border={true} src="https://files.readme.io/236c28f-Screenshot_2023-04-04_at_13.36.48.png" />

You should now see a new entry in the table under "Additional Claims" called `user.groups`:

<Image align="center" className="border" border={true} src="https://files.readme.io/0235d82-Screenshot_2023-04-04_at_13.38.39.png" />

Save the URL for later: `http://schemas.microsoft.com/ws/2008/06/identity/claims/groups`

Now go back to your main Active Directory view and select "Groups" tab:

<Image align="center" className="border" border={true} src="https://files.readme.io/83b07ab-Screenshot_2023-04-04_at_13.42.02.png" />

Copy the relevant "Object ID" for the group that you wish to sync Cloudsmith with:

<Image align="center" className="border" border={true} src="https://files.readme.io/9259a0d-Screenshot_2023-04-04_at_13.43.25.png" />

In your Cloudsmith workspace, go to "Settings" -> "Authentication" -> "SAML Group Syc", click "Enable SAML Group Sync" then "Create Group Sync Mapping":

<Image align="center" className="border" border={true} src="https://files.readme.io/97a8b842ef1d4f9591593e89e33727e0dd89279dc81ef9a4ea51dee493ee2df0-app.cloudsmith.com_demo_logsiPad_Pro_2.png" />

On the pop-up form, fill in the previously saved URL as the "Attribute Key" and the Object ID of the group as the value, click on "Create Group Sync Mapping":

<Image align="center" className="border" border={true} src="https://files.readme.io/423b58384411ad1aedae0d14f42f8901b4b228d5b88b0751d4ce9eae0c745b62-app.cloudsmith.com_demo_logsiPad_Pro_3.png" />

Now when a user re-logs with SAML, they will be placed in the assigned group based on the mapping.

General documentation on how SAML group sync works can be found [here](https://help.cloudsmith.io/docs/single-sign-on#saml-group-sync).

## SCIM De-provisioning

You can use SCIM to automatically de-provision users from your Cloudsmith organization whenever you remove a user assignment for the Cloudsmith application in Azure AD.

To set this up, you need to add an "Enterprise application" to your Active Directory on Azure:

<Image align="center" className="border" border={true} src="https://files.readme.io/8172851-Screenshot_2023-03-28_at_16.34.31.png" />

Click on "New Application":

<Image align="center" className="border" border={true} src="https://files.readme.io/6e7cf72-Screenshot_2023-03-28_at_16.36.00.png" />

Click on "Create your own application":

<Image align="center" className="border" border={true} src="https://files.readme.io/043acd5-Screenshot_2023-03-28_at_16.37.32.png" />

On the right side, a new tab should appear, fill in the details of the name and select the "...(Non-galler)" option and click "Create":

<Image align="center" className="border" border={true} src="https://files.readme.io/dff57a3-Screenshot_2023-03-28_at_16.39.27.png" />

Once the application is created, select "Provisioning":

<Image align="center" className="border" border={true} src="https://files.readme.io/23729bf-Screenshot_2023-03-28_at_16.42.10.png" />

Once the page loads, select "Provisioning" again, and select "Provisioning Mode" to "Automatic":

<Image align="center" className="border" border={true} src="https://files.readme.io/4995811-Screenshot_2023-03-28_at_16.44.01.png" />

In Cloudsmith navigate to the following link: `https://cloudsmith.io/orgs/<you_org_name>/settings/scim/`

Enable SCIM if it's not enabled and copy your SCIM Authentication token.

Go back to Azure AD and set the Tenatn URL to: `https://api.cloudsmith.io/scim/v2` and the "Secret token" to the copied token from Cloudsmith, click "Save" and "Test connection"

Now under the same "Provisioning tab", select "Mappings" dropdown and select "Provision Azure Active Directory Users"

<Image align="center" className="border" border={true} src="https://files.readme.io/4934353-Screenshot_2023-03-28_at_16.56.27.png" />

Under "Target Object Actions", select only "Updated, Delete" and click "Save":

<Image align="center" className="border" border={true} src="https://files.readme.io/1b6c2ec-Screenshot_2023-04-04_at_13.24.50.png" />

Azure AD should now have the necessary information to de-provision users from Cloudsmith

## All wrapped up!

Once you've added the link to your App Federation Metadata, and enabled SAML in your Cloudsmith organization settings, you will be able to access the landing page of your organization at the following URL:

[https://cloudsmith.io/orgs/ORG/saml/login/](https://cloudsmith.io/orgs/ORG/saml/login/)

Where *ORG* is your organization's slug/identifier (what you would normally see in the URL when accessing your organization within Cloudsmith).