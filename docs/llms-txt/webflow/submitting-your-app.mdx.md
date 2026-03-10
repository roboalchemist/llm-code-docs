# Source: https://developers.webflow.com/data/v2.0.0-beta/docs/marketplace/submitting-your-app.mdx

***

title: Submitting Your App to the Webflow Marketplace
description: >-
Learn how to submit your app for review and make it publicly available in the
Webflow Marketplace.
--------------------

This guide walks you through the process of submitting your app for review. For details on configuring how your app appears in the Marketplace, see the [app listing guide](/apps/docs/marketplace/listing-your-app).

## Submission process

1. Prepare [technical requirements](#technical-requirements) and [submission assets](#submission-preparation)
2. Submit for review, using the [Webflow App submission form](https://developers.webflow.com/submit)
3. Respond to feedback (if needed)
4. Publicize and share your app upon approval and publication to the Webflow Marketplace

## Technical Requirements

Your app must meet the following technical requirements to be made publicly available in the Webflow Marketplace:

* Two-factor authentication is enabled for an admin account on the workspace
* Your app has been thoroughly tested and is fully functional
* Your app has clear documentation and error handling
* Your app follows Webflow's security best practices and privacy guidelines

## Submission preparation

Before submitting your app for review, ensure you have completed these essential preparation steps:

<Steps>
  <Step title="Test your app and onboarding flow">
    Ensure your app is fully functional and meets all technical requirements. If you're submitting a Data Client or Hybrid App, ensure that your onboarding flow is working as expected and [provide an installation URL](#installation-configuration) that allows users to connect your service with Webflow.

    If you're looking to test your app with users outside of the workspace where it's registered, you can [submit your app to be reviewed as a private app](/apps/docs/private-apps). [See the installation configuration guidance for more details.](#installation-configuration)
  </Step>

  <Step title="Upload your Designer Extension bundle">
    For Designer Extensions, developers must upload the `bundle.zip` file created using the Webflow CLI. Please review the guidance on [publishing a Designer Extension bundle](/apps/docs/publishing-your-app) for more details.
  </Step>

  <Step title="Grant Webflow access to your app">
    To enable a thorough review of your app, you must provide Webflow with complete access to test all features. This includes any of the following (if applicable):

    * An active demo account with full functionality
    * Access to any gated or premium features
    * Required test credentials (for example, API keys, login details)
    * Sample data or resources needed to evaluate core functionality
    * Any additional materials needed to test edge cases or special features

    The goal is to ensure reviewers can fully evaluate your app's functionality, security, and user experience.
  </Step>

  <Step title="Enable backend services">
    Your app's backend services and APIs must be fully operational and accessible throughout the review process. This includes any third-party integrations, databases, or microservices that power your app's core functionality. Having these services available ensures our reviewers can properly assess how your app integrates with and enhances the Webflow ecosystem.
  </Step>

  <Step title="Create a demo video">
    Create a comprehensive demo video (2-5 minutes) that demonstrates your app's key features and functionality, and shows a complete walkthrough of the user experience from installation to usage.
    You can provide the video via:

    * Loom (private link)
    * YouTube (unlisted or private)
    * Google Drive (shared link)
  </Step>

  <Step title="Document complex features and pricing">
    Document any complex features, pricing tiers, and in-app purchases thoroughly in your review notes and demo video. Explain how each feature works, demonstrate user interactions with premium features, and outline your pricing structure. Include relevant visuals and external documentation links to give reviewers a complete understanding of your app's functionality.
  </Step>

  <Step title="Create marketplace and submission assets">
    To ensure your app is listed correctly in the Marketplace, include all the required information and assets detailed in the [App listing guide](/apps/docs/marketplace/listing-your-app).
  </Step>
</Steps>

## Submit your app

Once you've prepared your submission assets, you can submit your app for review using our [App submission form](https://developers.webflow.com/submit). A complete submission with all required details will help expedite the review process.

<a href="https://developers.webflow.com/submit">
  <Button class="cc-primary">
    Submit your app
  </Button>
</a>

## Installation configuration

Your app's installation URL defines where users are directed after choosing to install your app from the Marketplace. This URL should provide a clear path to where your App will authorize with users' Webflow Sites. Since Webflow OAuth can be initiated on install or within your platform, there are a few options to set as the Install URL based on your app's intended user experience.

### Choosing your installation URL

<Tabs>
  <Tab title="Data Client">
    1. **Direct to Webflow OAuth** (Recommended)<br />
       Immediately initiates the Webflow OAuth flow when users install your app
       * Example URL: <br />
         `https://webflow.com/oauth/authorize?response_type=code&client_id=YOUR_CLIENT_ID&scope=YOUR_SCOPES`
       * After authorization, redirect users to your platform where your service can:
         1. Call the [Get User Info](/data/reference/token/authorized-by) endpoint to get user details
         2. Create an account or match to existing user in your system

    2. **Direct to your platform first**<br />
       Directs users to your platform to complete setup before initiating OAuth
       * Example URL: `https://your-app.com/signup`
       * After users authenticate with your service, provide a clear way to initiate the Webflow OAuth flow.

    <Note title="Scopes on the Install URL">
      Verify that the scopes requested in the Install URL are equal to or a subset of the scopes configured for your app in the app settings. If there's a mismatch where the Install URL requests scopes beyond what's configured in the app settings, users won't be able to install your app and an error will be displayed.
    </Note>
  </Tab>

  <Tab title="Hybrid App">
    1. **Direct to Webflow OAuth** (Recommended)<br />
       Immediately initiates the Webflow OAuth flow when users install your app
       * Example URL: <br />
         `https://webflow.com/oauth/authorize?response_type=code&client_id=YOUR_CLIENT_ID&scope=YOUR_SCOPES`
       * After authorization, users are redirected to the designer with your [app installed and opened on the canvas](/apps/deep-linking):
         1. Call the [Get ID Token](/designer/reference/get-user-id-token) method to create an ID Token
         2. Call the [Resolve Token](/data/v2.0.0-beta/reference/token/resolve) endpoint on the Data API to get user details
         3. Create an account or match to existing user in your system
            For more information, see [Authenticating Hybrid Apps](/apps/docs/authenticating-users-with-id-tokens) guide.

    2. **Direct to your platform first**<br />
       Directs users to your platform to complete setup before initiating OAuth
       * Example URL: `https://your-app.com/signup`
       * After users authenticate with your service, provide a clear way to initiate the Webflow OAuth flow.

    <Note title="Scopes on the Install URL">
      Verify that the scopes requested in the Webflow OAuth URL are equal to or a subset of the scopes configured for your app in the app settings. If there is a mismatch where the Install URL requests scopes beyond what's configured in the app settings, users won't be able to install your app and an error will be displayed.
    </Note>
  </Tab>

  <Tab title="Designer Extension">
    * No installation URL needed - Webflow handles the installation flow automatically
    * Users will be directed to authorize the app to their site(s)/workspace
  </Tab>
</Tabs>

#### Best practices for onboarding your users

* Test the full installation flow from start to finish
* For Hybrid Apps, consider [directing users to the designer using your app's deep link.](/apps/deep-linking)
* Minimize the number of steps users need to take
* Provide clear guidance at each step
* Handle error cases gracefully with helpful messages

## Post submission

Our goal is to provide a prompt decision, ideally within 10-15 business days. You will be notified of our decision via the email associated with your Webflow account.

If your App submission is rejected, we will send you an email with a brief explanation. You will have the opportunity to address any feedback and resubmit your App for review.

<Warning>
  Any attempts to exploit the Webflow APIs or Marketplace review process, such as providing false information, engaging in plagiarism, deceitful manipulation of user files, or data theft, will result in immediate removal. Additionally, you will be banned from publishing future apps in our community.
</Warning>

We look forward to reviewing what you’ve developed!

For more context, please reference our [Developer Terms of Service](https://webflow.com/legal/developer-terms-of-service).

### Updating your app on the Marketplace

To update the information on your app listing, you can submit a request to the Webflow team. App updates follow the same review process as the initial submission. Simply submit your updated details using the [Webflow App submission form](https://developers.webflow.com/submit) and select "App Update" as the "Submission Type."

For App Updates, only the App Name and Client ID fields are required; all other fields are optional. We recommend completing only the fields you wish to modify, leaving the rest unchanged to streamline the process.

Once your update is approved and published, you will be notified via email.

<Info title="Updating a Designer Extension?">
  Don’t forget to publish a new version of your Designer Extension from your workspace. For guidance, refer to our documentation on [publishing a Designer Extension bundle](/apps/docs/publishing-your-app).
</Info>
