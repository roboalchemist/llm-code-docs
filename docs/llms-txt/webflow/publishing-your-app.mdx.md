# Source: https://developers.webflow.com/data/v2.0.0-beta/docs/publishing-your-app.mdx

***

title: How to bundle and upload your Designer Extension to Webflow
slug: docs/publishing-your-app
description: >-
A step-by-step guide to building, bundling, and uploading your Designer
Extension to a Webflow Workspace.
hidden: false
-------------

Once you've tested your Designer Extension locally, the next step is to upload it to Webflow to share with your Workspace. Each time you're ready to share a new version, you can upload it by following this guide.

### Before you begin

Make sure you have the following:

* A complete and tested Designer Extension.
* The [Webflow CLI](https://www.npmjs.com/package/@webflow/webflow-cli) installed.
* Admin access to the Webflow Workspace where your app is registered.
* Two-Factor Authentication (2FA) enabled on your Webflow account.

<Steps>
  <Step title="Build and bundle your extension">
    First, create a production-ready build of your extension. In your terminal, run the build command for your project. If you used `webflow extension init` to start your project, you can run:

    ```bash
    npm run build
    ```

    Depending on your project setup, this command compiles your code into a `build` or `dist` folder. You can specify this output directory in your `webflow.json` file. Learn more in our [App Settings guide](/designer/reference/app-settings).

    Next, use the Webflow CLI to bundle your build directory into a `bundle.zip` file. Run the following command from your project's root directory:

    ```bash
    webflow extension bundle
    ```

    This creates a `bundle.zip` file that is ready to be uploaded. **The bundle must not exceed 5MB.**

    <Note title="Working with Frameworks">
      If you're using a framework like Next.js or Astro, run the framework's production build command first, then run `webflow extension bundle` on the output directory. You can streamline this by combining these steps into a single script in your `package.json`.
    </Note>
  </Step>

  <Step title="Upload your extension bundle">
    With your `bundle.zip` file ready, you can upload it to Webflow.

    1. Navigate to your Workspace settings and click the **Apps & Integrations** tab.
    2. Under the **Develop** section, find your app and click **Publish extension version**.

       <Frame>
         <img alt="Publish extension version button in App settings" src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/47388dd9b18511fcce24cf965dfb55060b558faf3861c3c77c1b4662a33466af/products/data/pages/Apps/designer-extensions/assets/publish-extension-version.png" />
       </Frame>
    3. In the file dialog, select the `bundle.zip` file and add notes about the changes in this version.

    After the upload is complete, you'll see a confirmation message, and a new version will appear in your app's version history.
  </Step>

  <Step title="Test your uploaded extension">
    Once your extension is uploaded, test it in your Workspace to ensure it works as expected.

    1. Open a Webflow site in your Workspace.
    2. Open your app and click the **Launch App** button.
    3. Verify that everything works as expected.

    <Frame>
      <img alt="Launch app button in App settings" src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/b186e6075c18d9c7f491bb2ea8cfe5066df02499bf8fb0c636984bdc9ce73fbf/products/data/pages/Apps/designer-extensions/assets/launch-development-app.png" />
    </Frame>

    <Note>
      Be sure to click **Launch App** to test the uploaded version, not **Launch development app**, which loads your extension from your local development URL.
    </Note>
  </Step>
</Steps>

## Submitting to the Marketplace

Once your extension is tested in your Workspace, you can submit it to the Webflow App Marketplace. The [submission process](/apps/docs/marketplace/submitting-your-app) involves providing marketing assets, support information, and a description of your app.

The Webflow team will review your submission to ensure it follows our [Developer Terms of Service](/apps/developer-terms-of-service) and meets our [Marketplace Guidelines](/apps/docs/marketplace-guidelines). This process can take a few days, and you'll receive an email notification once it's approved.

Learn more in our [Marketplace Submission Guide](/apps/docs/marketplace/submitting-your-app).

## Frequently asked questions

<Accordion title="Are uploads to Webflow versioned?">
  Yes. Every time you upload a `bundle.zip` file, Webflow creates a new, versioned instance of your extension. You can add notes with each version to track new features, changes, and bug fixes. To see your version history, click the **...** button in your app's settings and select **Version History**.

  <Frame>
    <img alt="A list of Designer Extension versions with notes for each update." src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/e870b53f77caa26d7d7836ee10ca500aa9aa974f9bdd003ff990816f357b2ae6/products/data/pages/Apps/designer-extensions/assets/designer-extension-versions.png" />
  </Frame>
</Accordion>

<Accordion title="Can I revert to a previous version?">
  Webflow does not have a one-click rollback feature. However, since your `bundle.zip` files are generated from your local codebase, you can use your version control system (like Git) to check out a previous version of your code, generate a new bundle from it, and upload that bundle to Webflow.
</Accordion>

<Accordion title="Why is the 'Publish extension version' button disabled?">
  This button is disabled if you are not an admin of the Workspace or if you do not have Two-Factor Authentication (2FA) enabled on your account.
</Accordion>

<Accordion title="How can I share my extension outside my Workspace?">
  You can share your extension outside of your Workspace by submitting it to the Webflow Marketplace. If you want to test with a limited group of users before a full public release, you can also [submit your app to be reviewed as a private app](/apps/docs/private-apps).
</Accordion>

<Accordion title="Where is my production app hosted?">
  Your production app is hosted on Webflow's servers. When you upload your `bundle.zip` file, Webflow compiles your extension and serves it from a unique URL within an iframe in the Designer.

  You can find this URL in your app's settings by clicking the **...** button and selecting **Edit App -> Building Blocks -> Designer Extension** and see the section for Designer Extension URI.
</Accordion>
