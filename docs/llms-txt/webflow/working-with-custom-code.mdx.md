# Source: https://developers.webflow.com/data/docs/working-with-custom-code.mdx

***

title: Working with Custom Code
hidden: false
hide-toc: true
'og:description': >-
This document provides a step-by-step guide on how to add custom scripts to a
Webflow site using the API, allowing for enhanced functionality and
interactive features.
---------------------

This guide will demonstrate how to add custom code to a pre-configured example site. You will learn how to register scripts to a site, apply them to a page, and publish the site, illustrating the complete process of managing scripts via the API.

## Prerequisites

* A clone of our [Code Example Site.](https://webflow.com/made-in-webflow/website/webflow-developers---script-ex-097863)

* A [Webflow App](https://developers.webflow.com/data/docs/register-an-app) or a [Site Token](https://university.webflow.com/lesson/intro-to-webflow-apis?topics=cms-dynamic-content#how-to-create-an-api-token) with the following scopes: `sites:read`, `sites:write`, `pages:read`, `pages:write`, `custom_code:read`, and `custom_code:write`

* An [Ngrok account and authentication token](http://ngrok.com/). We use Ngrok to set up a secure tunnel for our App.

<Accordion title="1. Clone the Example Site">
  1. **Clone the Example Webflow Project:** Clone the example Webflow site where scripts will be applied.
  2. **Publish the site:** Publish the site and explore it in your browser.
  3. **Navigate to the "Pointer Tracking" example:** The page will have an overview description of the example, and instructions on how to implement the code. In our finished version, once custom code is applied to the page, the "Pointer Tracking" example will show an animation that follows your pointer across the page.

  <Tabs>
    <Tab title="Without Custom Code">
      <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/883b8c617cdfbb25c4db118cc8e9827ef89b2fc0d0ea63f5ee407800f5b4264e/assets/images/6d4b083-Large_GIF_1230x624.gif" alt="Without Custom Code" />
    </Tab>

    <Tab title="With Custom Code">
      <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/11612b6401a78443be52441d5fe6083bbb8ead9a81029acc6731d1d2cf77504e/assets/images/0fbf9c8-Large_GIF_1238x662.gif" alt="With Custom Code" />
    </Tab>
  </Tabs>
</Accordion>

<Accordion title="2. Setup the Development Environment">
  1. **Clone the Project Repository**
     Run the following commands in your IDE to clone the example repository and install dependencies:

     ```bash Bash
     git clone https://github.com/Webflow-Examples/custom-code-examples/tree/main
     cd custom-code-examples
     npm install
     npm run install-project
     ```

  2. **Configure Environment Variables**
     Fill out a `.env` file with the necessary environment variables:

     ```env .env
     WEBFLOW_CLIENT_ID=YOUR_CLIENT_ID
     WEBFLOW_CLIENT_SECRET=YOUR_CLIENT_SECRET
     NGROK_AUTH_TOKEN=YOUR_NGROK_AUTH_TOKEN
     PORT=8080
     ```
</Accordion>

<Accordion title="3. Start and Authorize Your App">
  1. **Start the Project**
     Run the following command in your IDE to start the project:
     ```bash Bash
     npm run dev
     ```

  2. **Update App's Redirect URI**
     Once the server is running, copy the Redirect URI provided in the terminal. Navigate to your Webflow Workspace dashboard, go to "Apps & Integrations," and update the Redirect URI in your App settings. Save the changes.

     <Tabs>
       <Tab title="Terminal Output">
         <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/b5a2cec6e0eb22c2d167d1d11c423825cbe3f099608f79d941f16d8d771544bb/assets/images/f684278-Screenshot_2024-06-25_at_3.07.27_PM.png" alt="Terminal Output" />
       </Tab>

       <Tab title="Update App Redirect URI">
         <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/42e1699df2021d780a22362b803636c2ff30b663a41ea3df18fa87e54aec05bf/assets/images/cf5b0e1-Large_GIF_1320x708.gif" alt="Update App Redirect URI" />
       </Tab>
     </Tabs>

  3. **Authorize App**
     We'll need to authorize the App to access the newly cloned example site. We've already set up the authorization flow in this example App. Navigate to `localhost:8080` and choose the workspaces or sites you want your App to access. Once authorized, you'll be redirected to the App's frontend.

     To see how we configured authorization for this App, navigate to the `backend` folder and review `controllers/authController.js`, `routes/authRoutes.js`, and `webflowClientMiddleware.js`. For more information on setting up authorization, [read through our authorization guide.](https://developers.webflow.com/data/reference/authorization)
</Accordion>

<Accordion title="4. Register Scripts">
  In this step, you will register scripts necessary for implementing custom functionality on your Webflow site. The App provides three example scripts that correspond to functionalities you can implement on the example site. We'll start with <strong>Pointer Tracking</strong>, a script that enables an animation to follow your pointer around on the screen. We’d like to give Jeff McAvoy at RiveFlow a special thanks for contributing this example to the Webflow developer community.

  1. **Choose the Pointer Tracking Example**<br />
     From the list of example scripts, select "Pointer Tracking." Once selected, you’ll see a list of scripts to register that are marked inline or hosted.

     <Tabs>
       <Tab title="Hosted Scripts">
         Hosted scripts require a `hostedLocation` (the URL where the script is hosted) and an `integrityHash` to verify the script's contents.

         The following controller logic in the example app automates this process:

         * it fetches the script from the `hostedLocation`
         * generates an `integrityHash` to ensure the script hasn't been tampered with
         * and then uploads this information to the Webflow endpoint.

         This verification step ensures the script's integrity before it's applied to your Webflow site.

         <CodeBlocks>
           ```javascript backend/controllers/scriptController.js
           export const registerHostedScript = async (req, res) => {
             try {
               const siteId = req.params.siteId;

               async function generateSRI(url) {
                 const response = await fetch(url);
                 const data = await response.text();
                 const integrity = Sri(data, ["sha256"]);
                 return integrity;
               }

               const hostedLocation = req.body.hostedLocation;
               const integrityHash = await generateSRI(hostedLocation);

               const script = {
                 hostedLocation: hostedLocation,
                 integrityHash: integrityHash,
                 canCopy: true,
                 version: req.body.version,
                 displayName: req.body.displayName
               };

               const data = await req.webflow.scripts.registerHosted(siteId, script);
               res.json(data);
             } catch (error) {
               console.error("Error registering hosted script:", error);
               res.status(500).send("Failed to register hosted script");
             }
           };
           ```
         </CodeBlocks>
       </Tab>

       <Tab title="Inline Scripts">
         Inline scripts require the actual JavaScript `sourceCode` to be provided. Each inline script has a limit of 10,000 characters. When providing the source code, do not include \<script> tags; Webflow will handle that for you.

         The example app automates this process by capturing the `sourceCode` object from the request body and registering it with Webflow. This ensures that your inline scripts are correctly formatted and within the character limit before being applied to your Webflow site.

         <CodeBlocks>
           ```javascript backend/controllers/scriptController.js
           export const registerInlineScript = async (req, res) => {
             try {
               const siteId = req.params.siteId;

               const request = {
                 sourceCode: req.body.sourceCode,
                 canCopy: req.body.canCopy !== undefined ? req.body.canCopy : true,
                 version: req.body.version,
                 displayName: req.body.displayName,
               };

               const data = await req.webflow.scripts.registerInline(siteId, request);
               res.json(data);
             } catch (error) {
               console.error("Error registering inline script:", error);
               res.status(500).send("Failed to register inline script");
             }
           };
           ```
         </CodeBlocks>
       </Tab>
     </Tabs>

  2. **Provide script details**<br />
     To upload a script via the API, you’ll need to provide the following details:

     * **`displayName`** (*string*): The name of your script
     * **`version`** (*string*): The semantic version of your script. Each script must have a unique combination of `displayName` and `version`. You cannot overwrite scripts at this time.
     * **`canCopy`** (*Boolean*): Define whether the script can be copied on site duplication and transfer

     For the example we’ve already included the `hostedLocation` if it’s a hosted script, or the `sourceCode` if it’s an inline script.

  3. **Click register**<br />
     Depending on the type of script, inline or hosted, this button will send your script to the backend server, and then to the appropriate Webflow endpoint.
     * POST [https://api.webflow.com/v2/sites/\{site\_id}/registered\_scripts/inline](https://developers.webflow.com/data/reference/custom-code/custom-code/register-inline)
     * POST [https://api.webflow.com/v2/sites/\{site\_id}/registered\_scripts/hosted](https://developers.webflow.com/data/reference/custom-code/custom-code/register-hosted)

  4. Once you’re finished registering your scripts, click the “Next” button.
</Accordion>

<Accordion title="5. Apply Scripts">
  Now that a script has been registered to the Webflow site, you can use the API to apply scripts to either the entire site or a specific page. In this step, you will apply each script to the appropriate page for the chosen example.

  Scripts can be applied to one of two locations:

  * **Header**: Within the `<head>` tag.
  * **Footer**: Right before the closing `</body>` tag.

  1. **Select a Page**
     Choose the page where you'll apply the script. For this example, we'll select the "Pointer Tracking" page.

  2. **View Registered Scripts**
     You will see a list of scripts that have been registered to your site, populated by the [Get Scripts](https://developers.webflow.com/data/reference/custom-code/custom-code/list) endpoint.
     * The list includes the script ID, version, and `hostedLocation`.
     * Note that even inline scripts have `hostedLocation` URLs, as Webflow uploads these scripts to its CDN for serving.

  3. **Apply Scripts**

     * **Header**: Apply the Rive.js script to the header.
     * **Footer**: Apply the pointer-tracking.js script to the footer.

     To apply the scripts we've registered to the page, we'll use the [Add/Update Custom Code](https://developers.webflow.com/data/reference/custom-code/custom-code-pages/upsert-custom-code) endpoint. This endpoint requires you to add all custom code blocks to the page. Therefore, we'll also use the [Get Custom Code](https://developers.webflow.com/data/reference/custom-code/custom-code-pages/get-custom-code) endpoint to retrieve any existing applied scripts, also known as custom code blocks, and upload a complete list of code that should be on the site.

     We've applied this logic in our example app in `backend/controllers/scriptControllers.js`

     <CodeBlocks>
       ```javascript JavaScript
       export const upsertPageCustomCode = async (req, res) => {
         const pageId = req.params.pageId;
         const { selectedScript, version } = req.body;

         const applyScripts = async (scriptApplyList) => {
           try {
             const data = await req.webflow.pages.scripts.upsertCustomCode(pageId, scriptApplyList);
             res.json(data);
           } catch (error) {
             console.error("Error adding/updating page-level custom code:", error);
             res.status(500).send("Failed to add/update page-level custom code");
           }
         };

         try {
           const response = await req.webflow.pages.scripts.getCustomCode(pageId);
           const existingScripts = response.scripts || [];
           const newScript = {
             id: selectedScript,
             location: req.query.location,
             version: version,
           };
           existingScripts.push(newScript);
           const scriptApplyList = {
             scripts: existingScripts,
           };

           console.log(scriptApplyList);
           await applyScripts(scriptApplyList);
         } catch (error) {
           console.error("Failed to fetch scripts", error);
           const scriptApplyList = {
             scripts: [
               {
                 id: selectedScript,
                 location: req.query.location,
                 version: version,
               },
             ],
           };
           await applyScripts(scriptApplyList);
         }
       };
       ```
     </CodeBlocks>

  4. **Bonus: Check the Page in the Designer**<br />
     The Webflow Designer allows users to see how apps integrate code into their sites. After applying a script to a site or page, you can view it in the Designer's settings.
     * Open the Webflow Designer.
     * Go to the page settings for "Pointer Tracking."
     * Scroll down to the Custom Code section to see the script your app added.
     <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/0f769666641e6102080d8f47abb1a46931d4b9dcd8f762615f575981027e1d2a/assets/images/c8671c0-Google_Keep.png" alt="custom-code-app-details" />
</Accordion>

<Accordion title="6. Publish and View Your Site">
  Before you can see your scripts in action, you'll need to publish your entire site. Click the "Publish Site" button to publish your site using the [Publish Site](https://developers.webflow.com/data/reference/sites/publish) endpoint.

  Once your site is published, click "View Page" to go directly to your Pointer Tracking page. You should now see a fun animation that follows your pointer around the page.

  <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/11612b6401a78443be52441d5fe6083bbb8ead9a81029acc6731d1d2cf77504e/assets/images/0fbf9c8-Large_GIF_1238x662.gif" alt="With Custom Code" />
</Accordion>

# Next Steps

Awesome! Now that you’ve got the hang of custom code, here are some other cool things you can do:

* **Apply More Examples**: Use the app to explore and apply more example scripts.
* **Add Your Own Custom Code**: Use the API to add your own custom code examples and see them in action on your Webflow site.

Keep experimenting and enhancing your Webflow site with custom scripts!
