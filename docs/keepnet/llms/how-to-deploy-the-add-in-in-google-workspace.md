# Source: https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/phishing-reporter-deployment/how-to-deploy-the-add-in-in-google-workspace.md

# How to Deploy the Add-in in Google Workspace

This document explains how to deploy **Keepnet's Phishing Reporter** button in Google Workspace to **all employees** or to **specific Organisation Units/Groups**.

{% hint style="warning" %}
This installation requires a Google Workspace Admin account.
{% endhint %}

## Keepnet Phishing Reporter Settings

1. First, [customise the Keepnet Phishing Reporter ](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/phishing-reporter-customization)button to match your organisation's needs, including logo, text, and other settings.
2. Second, on the **Phishing Reporter customisation page**, scroll to the bottom and click **'Manage and Download'** to download the **Google Workspace zip file**. The zip file contains two files used in the Google Workspace deployment steps.

## Google Workspace Deployment Steps

### Step 1: Create Script

To deploy the Phishing Reporter add-in to users in Google Workspace, follow these steps:

* Go to[ script.google.com](http://script.google.com) and click on the **New Project** button.
* **Enter a name** for your new project (e.g Keepnet Phishing Reporter Button)
* Open the downloaded Keepnet zip file, **edit the Code.gs** **file**, copy all the code, paste it into the **Code.gs file of the new project,** and click the **Save** button to save the changes.
* While on the project page, on the left-hand side, click the **Project** **Settings** button, then enable the **'Show 'appsscript.json' manifest file in editor'** option under the **General Settings** tab.
* Open the downloaded Keepnet zip file, **edit the Appscript.json** **file**, copy all the code, return to the **Editor** page, paste it into the **Appsscript.json file of the new project**, and click the **Save** button to save the changes.

### Step 2: Create Project

* Go to [console.cloud.google.com](https://console.cloud.google.com/) and create **a New Project**.
* **Name your project** (e.g Keepnet Phishing Reporter Button) and select the location. Then click on **Create** to start your project.
* Go to the **APIs and Services** page. Open the **OAuth content screen** page from the left menu and click the **Get Started** button.
* **Step 1: App Information**, please fill in the following fields, then click **Next**.
  * **App Name:** Enter a name (e.g Keepnet Phishing Reporter Button)
  * **User Support Email:** Select an email account that is listed on this option.
* **Step 2: Audience,** please select **Internal** option, then click **Next**.
* **Step 3: Contact Information**, you can add your email address or the security team's email account.
* **Step 4: Finish**, accept the **Agreement** and click **Create**.

### Step 3: OAuth Content Screen Configuration

* While you are on the **OAuth Consent Screen** page, click the **Branding** option on the left menu.
* Fill in the required fields below.
  * **App Name:** Enter a name (e.g Keepnet Phishing Reporter Button)
  * **User Support Email:** Select an email account that is listed on this option.
  * **App Logo:** You can upload your company logo or use Keepnet's default logo; see the attachment below.
  * **Developer Contact Information:** Add your email address or the security team's email address.
* Click the **Save** button to apply changes.
* Go to **API & Services,** open the **Library** page to search **Gmail API,** and then **enable it**.
* Go to the project's main page by clicking the **Google Cloud logo** at the top of the page on the left, then **copy the Project Number** (save it).

{% file src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2F9xzaaZyrmqMvJ6Avh7Ca%2FApp%20Logo.png?alt=media&token=dab978ad-6598-4d7e-b7a1-67d93c932d42>" %}

### Step 4: Change the Project Number of Script Project

* Go to [script.google.com](https://script.google.com/) and open your project.
* Click the **settings icon** on the left menu, then select **Project** **Settings**.
* Find the '**Google Cloud Platform (GCP) project'** title, click the **Change** **Project** button, **paste the** **project number,** then click **Set** **Project**.

### Step 5: Testing the Add-in

If you don't want to test the add-in in your Gmail account, please go to the "**Enable Google Workspace Marketplace SDK"** part to deploy the add-in to the organization-wide or specific groups.

If you want to test and see the add-in functionality, logos, add-in name, description, and more information, you can deploy the add-in to your Gmail account for test purposes and remove it anytime.

* Go to [script.google.com](https://script.google.com/)
* Select the add-in project.
* Click on **Deploy** **> Test Deployments > Install** butto&#x6E;**.**
* Click **Done**.

The add-in will appear on your Gmail account shortly. You can remove the add-in from the same page.

### Step 6: Enable Google Workspace Marketplace SDK

* From the **Library** page, search for the **Google Workspace Marketplace SDK** and click on it.
* Click the **Enable** button and activate the **Google Workspace Marketplace SDK**.
* Go back to [script.google.com](https://script.google.com/) and click on the **Deploy** **> New Deployment** button.
* Enter information in the **Description** field (e.g Keepnet Phishing Reporter Button), click the **Deploy** button, and copy the **Deployment ID** (save it).
* Go back to the **Console** **Cloud**. Go to the **API & Services** page, click **Library** and search for **“Google Workspace Marketplace SDK”** and click on it.
* Go to the **App Configuration** tab, and fill in the required information below.
  * **App visibility:** Select the **Private** option.
  * **Installation settings:** Select the option that suits you best, e.g., the **admin-only installation** option.
  * **App integrations:** Select the **Google Workspace Add-on**, then select **Apps Script**. Please paste the **Deployment ID** into the deployment id field.
  * **Developer information:** Fill in the following options:
    * **Developer Name:** Keepnet
    * **Developer Website URL:** <https://keepnetlabs.com/>
    * **Developer Email:** <support@keepnetlabs.com>
  * Click the **Save** **Draft** to apply the changes.
* While on the **Google Workspace Marketplace SDK** page, click the **Store** **Listing** tab and follow the steps below.
  * **App Details:** Extend this option and follow the steps below.
    * **Language:** Select a language such as **English**.
    * **Application Name:** Keepnet Phishing Reporter Button
    * **Short Description:** Keepnet Phishing Reporter helps you to report suspicious emails to the security team.
    * **Detailed Description:** Keepnet Phishing Reporter helps you to report suspicious emails to the security team for automated or manual analysis. Thank you for reporting suspicious emails to protect our organization against email-based attacks.
    * Click the **Done** button.
  * **Pricing:** Select the **Paid** option.
  * **Category:** Select the **Web Development** option.
  * **Graphic Assets:** Download the following add-in logos.zip file and upload each image for this option.
  * **Screenshots:** You can use the **'Add-in Logo 220x140.png'** logo for this option from the zip file.
  * **Support links:** Please use the following info for each field.
    * **Terms of Service URL:** <https://doc.keepnetlabs.com/legal-hub/for-everyone/website/terms-of-use>
    * **Privacy Policy URL:** <https://doc.keepnetlabs.com/legal-hub/for-everyone/website/privacy-policy>
    * **Support URL:** <https://support.keepnetlabs.com/>
  * **Distribution:** Select your **Regions** or **All** **Regions** where you will deploy the add-in.
  * Click the **Save** **Draft** button and then click the **Publish** button.

{% file src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2FUFzdLep9bKD4ewpAcgqh%2FAdd-In%20Logos.zip?alt=media&token=2831f677-ba20-4e51-8387-6047a34ebb57>" %}
Default Phishing Reporter Add-In Logos
{% endfile %}

### Step 7: Deploy Add-in

Please follow the following steps to deploy the add-in to your target users.

* To deploy the add-in, go to [mail.google.com](https://mail.google.com/) and click on the **Google Apps** icon in the top right-hand corner of the screen.
* Scroll down to [**More from Google Workspace Marketplace**](https://workspace.google.com/u/1/marketplace) and click on it.
* Click **Internal Apps** and find the add-in. If you don't see the add-in, wait a few minutes for it to appear.
* Click the **Admin Install** button to start the deployment process.
* Click **Continue** to start the distribution of the reporter button. You can deploy the add-in to the organisation as a whole or to specific groups/organisation units.
* Accept the required permissions to complete the deployment.

{% hint style="warning" %}
It may take up to 24 hours for this app to be installed for your entire Google Workspace domain or organisational unit.
{% endhint %}

### Step 8: Uninstall the Add-in

If you wish to uninstall the Keepnet Phishing Reporter button from all users' inboxes, please follow the steps below.

* Go to Google **Admin > Apps > Google Workspace Marketplace apps >** [App list](https://admin.google.com/u/3/ac/apps/gmail/marketplace/domaininstall) on the left menu.
* Click on the **Phishing Reporter** add-in you want to uninstall.
* Click the **Delete** **App** to complete the process.

{% hint style="warning" %}
It may take up to 24 hours for this app to be uninstalled for your entire Google Workspace domain or organizational unit.
{% endhint %}

## FAQs

### Q: Does Google charge if we deploy the add-in?

A: No, there is no charge by Google.

### Q: Can I use my phishing reporter add-in in the Gmail app on iOS or Android?

A: Yes, you can use the Phishing Reporter add-in in the Gmail App on Android or IOS.

### Q: Where do reported emails go?

A: If you purchased the Incident Responder product, the reported email will be sent to the [Incident Responder](https://doc.keepnetlabs.com/next-generation-product/platform/incident-responder) product for analysis. If you enabled the ['Information Email'](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter-customization#information-email) option, the reported email's original copy will be sent to the email address that is set on the related page.

### Q: Do I need to redeploy the add-in if I make add-in changes on Keepnet? (e.g. logo change)

A: Yes, if you have already deployed the Phishing Reporter button on Google Workspace for your employees and if you need to change the logo, texts or any other settings on the Phishing Reporter page on the platform, you need to download a new file and [re-deploy the button](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/phishing-reporter-deployment/how-to-deploy-the-add-in-in-google-workspace).

### Q: Is there a quick way to redeploy the add-in if I've made changes?

A: No, you need to remove your current Phishing Reporter button from all employees and follow all the steps in the [document here](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/phishing-reporter-deployment/how-to-deploy-the-add-in-in-google-workspace) to re-deploy the new reporter button.

### Q: Do I need to accept the permissions required for the reporter button to use?

A: Yes, once you deploy the button to your employees, when they click the reporter button to use, for a one-time purpose, they need to approve the required permissions to be able to use the reporter button.
