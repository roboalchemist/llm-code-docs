# Source: https://docs.beefree.io/beefree-sdk/builder-addons/partner-addons/installing-partner-addons.md

# Installing Partner AddOns

{% hint style="info" %}
Visit our [Partner AddOn directory](https://docs.beefree.io/beefree-sdk/builder-addons/partner-addons/partner-addons-directory) for a list of available and upcoming AddOns.
{% endhint %}

## Getting started <a href="#getting-started" id="getting-started"></a>

You can **use** ready-to-go AddOns to extend the functionality of Beefree SDK (you can also [build new AddOns](https://docs.beefree.io/beefree-sdk/builder-addons/custom-addons)).

To browse and install existing AddOns, log into the [Beefree SDK Console](https://developers.beefree.io/) and click on *Details* to navigate to the application details page.

In the lower part of the page, locate the **Application configuration** section and click on AddOns.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FmVvyHVrxvYs6tRE09kSG%2FCleanShot%202025-03-13%20at%2015.07.43.png?alt=media&#x26;token=3b801113-3753-44d1-b934-291ddd707bcc" alt=""><figcaption></figcaption></figure>

You will be taken to a page that lists the AddOns that have been installed for this application. If you are just getting started, the list will be empty.

Click on **Browse Partner AddOns** to get the list of ready-to-install AddOns. We call them **Partner AddOns** because they were developed by companies that partnered with us to extend Beefree SDK’s core functionality.

You will deal directly with those companies with regard to signing up for an account, cost, support, etc.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FAGwaeO1Jbpu7rejx7Zbu%2FCleanShot%202025-03-13%20at%2015.08.33.png?alt=media&#x26;token=18fc8966-5df2-44f6-a136-7b8fbe9c3ae6" alt=""><figcaption></figcaption></figure>

You will instead click on *Create a Custom AddOn* if you want to [build a new AddOn](https://docs.beefree.io/addon-development/) for Beefree SDK.

## Installing an AddOn <a href="#installing-an-addon" id="installing-an-addon"></a>

When you click on the **Browse Partner AddOns** button, a list of AddOns is displayed. You can browse them and select what you need to install.

After installing a Partner AddOn, you will need to configure it by clicking on the **Edit** action. A form will be displayed.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2F28g43gMtBlc7lDoyrmFP%2FCleanShot%202025-03-13%20at%2015.09.51.png?alt=media&#x26;token=5d81aa54-3765-4f8e-ba6a-200afccad4c1" alt=""><figcaption></figcaption></figure>

At the top of the form you will find the AddOn name and some links to the AddOn documentation. If any signup is required, that is the company that you will need to contact.

Below that, you will see the following form fields:

* **API Key**\
  Shown if this is an AddOn where a signup is required (you will be provided with an API key once you have signed up). Contact the provider of the AddOn if that is the case, so that you can learn about signing up, costs involved, the type of support they provide, etc.
* **Handle**\
  A unique identifier for this AddOn. You will use this unique identifier to pass information to the AddOn from your application, if and when needed.
* **Enabled**\
  A toggle element to enable and disable the AddOn. When toggled *OFF,* the AddOn is not visible to end users of the builder in your application.
* **Icon**\
  If you want to customize the icon associated with the *tile* shown in the builder *Content* tab, you canupload an image from your local PC. Choose an image that is small in size: we recommend a 64 x 64 pixel SVG file.
* **Labels**
  * Title: This is the name that will be used for the *tile* in the builder’s *Content* tab (e.g. “Countdown timer”).
  * Call-to-action button: The label for the call-to-action button (e.g. “Select a Countdown Timer”), which is shown to end users on the button to configure the AddOn.
  * Placeholder text: The message shown to end users in the builder stage when the tile is first dragged and dropped into it.

With the following setup…

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FKmWdag269HkQtcZr9uSu%2F4icon.labels.setup_-1024x194.png?alt=media&#x26;token=df1c770d-ad4b-4742-b55a-2fd84ac1b03f" alt=""><figcaption></figcaption></figure>

… you would get the following outcome:

## **Title for the content tile**

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2F2m22ja8Um1ajnS4fNmrN%2F5AddOn.tile_.png?alt=media&#x26;token=5b702319-3d61-4d02-b352-bfe02b6fda83" alt=""><figcaption></figcaption></figure>

## **Placeholder text and button**

It displays when the AddOn is added to the editing stage and invites the user to take the next step.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FWkFkiGcSuqN4BYNw7keU%2F6AddOn.placeholder-1024x298.png?alt=media&#x26;token=62744312-d048-4c04-9446-0750339de24c" alt=""><figcaption></figcaption></figure>

## **AddOn selection button in content properties**

When the AddOn content is selected, the same button is displayed in the content properties.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2Fy87qF4sBff5hgqOGTzsw%2F7AddOn.action.png?alt=media&#x26;token=a2311285-ee4e-4223-be68-dd6ae65274ef" alt=""><figcaption></figcaption></figure>

Visit our [AddOns Configuration](https://docs.beefree.io/beefree-sdk/builder-addons/addons-configuration) to learn more about how to configure custom and partner addons.
