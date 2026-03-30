# Source: https://developers.webflow.com/data/v2.0.0-beta/docs/cms-tutorial.mdx

***

title: Working with the CMS
slug: /data/docs/cms-tutorial
description: >-
Explore the complete guide to Webflow’s CMS API, including prerequisites, code
snippets, and examples for our endpoints.
hidden: false
layout: overview
'og:title': Working with the Webflow CMS API
'og:description': >-
Explore the complete guide to Webflow’s CMS API, including prerequisites, code
snippets, and examples for our endpoints.
-----------------------------------------

## What you'll build

This guide will walk you through using a Data Client app to interact with Webflow's CMS APIs. A Data Client enables you to make calls to Webflow's backend APIs, and through this guide, you'll learn how use the API to:

1. Create collections and fields
2. Create, read, update, and delete items
3. Publish and unpublish collection items

To make visualizing your Collections and Items easier, you'll also build a simple frontend using React.

## Prerequisites

* A Webflow site. If you’re not sure where to start, clone the [Astral Fund site](https://webflow.com/made-in-webflow/website/astralfund-919afdc1091df68b8dc1347f952a?searchValue=astral) with defined CMS collections.
* A registered [Webflow App](https://developers.webflow.com/data/docs/register-an-app) or a [Site Token](https://university.webflow.com/lesson/intro-to-webflow-apis?topics=cms-dynamic-content#how-to-create-an-api-token) with the following scopes: `sites:read`, `cms:read`, and `cms:write`
* An [Ngrok account](http://ngrok.com) and an authentication token
* [Node.js](https://nodejs.org/en) and an IDE of your choice
* Additionally, you should have basic knowledge of Node.js and Express

#

<AccordionGroup>
  <Accordion title="1. Quickstart">
    Reference the [starter code](https://github.com/Webflow-Examples/cms-examples) for to follow along with the guide. This code already takes care of the OAuth Handshake and initializes the Webflow Client as shown in the [Authentication guide.](https://developers.webflow.com/data/reference/authorization) You'll be able to start this App, authenticate the App, and start making requests to the Webflow CMS API.

    1. **Clone the starter code.**
       Run the following commands in your IDE to clone the [example repository](https://github.com/Webflow-Examples/cms-examples) and install dependencies:

       ```bash Shell
       git clone https://github.com/Webflow-Examples/cms-examples.git
       cd cms-examples
       npm install
       ```

    2. **Add Environment Variables**
       Add your credentials to the `.env` file. If you’re using an App, input your App’s `CLIENT_ID` and `CLIENT_SECRET`. If using a Site Token, input the token as `SITE_TOKEN`.

    3. **Add Ngrok Auth Token**
       Ngrok is required because Webflow Apps must run on `https://` URLs, and Ngrok provides a secure tunnel for your local server.

       Get your Ngrok auth token from the [Ngrok dashboard](https://dashboard.ngrok.com/tunnels/authtokens). Then, add your token to your environment variables in `.env`:

       ```bash Shell
       NGROK_AUTH_TOKEN=your-ngrok-auth-token
       ```

    4. **Start the Server**
       Start the server by running `npm start` in your terminal.

       This will output list of URLs in the terminal to access your server and your frontend.

       <Frame>
         <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/3b403fac67af05e1eec9531977b02025905c6956cf83abab190cdf4d92124070/assets/images/ngrok-table.png" />
       </Frame>

    5. **Update your Redirect URI in Webflow**
       Copy the redirect URI from your terminal output. Navigate to your App in the Webflow Dashboard Settings and update the Redirect URI to the URL of your server.
       <Frame>
         <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/433d258681d074363607a2cd3c805c34250c5bf2ab9b43b5997ab1661c7f1317/assets/images/update-redirect-uri.png" />
       </Frame>

    6. **Authenticate the App**
       Open the URL of your server in the browser. You'll be prompted to authenticate the App with Webflow. You have the option to authenticate a single site or all sites on a single workspace.

    7. **Start making requests**
       Once authenticated, you'll be redirected to the App frontend where you can select an authorized site and start making requests to the Webflow CMS API.
       <Frame>
         <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/e606a8b868fa7185c560569d20fb9b97a9c215a0fcd4a4a85516e9c9aa9b09d5/assets/images/cms-example-app.png" />
       </Frame>
  </Accordion>

  <Accordion title="2. Shaping requests">
    The backend is built using Express and Node.js, and designed to handle requests from the frontend.

    When a request the server receives a request, it's first passed to the middleware function defined in `webflowClientMiddleware.js`. This function initializes and authenticates the Webflow Client and attaches it to the request object, so you don't have to re-authenticate in each request. This client is then used in the controllers to make requests to the Webflow CMS API.

    In the controller files, **requests are prefixed with `req.`** followed by the standard Webflow SDK methods. For example, to interact with collections you would use `req.webflow.collections.items.listItems()`.

    ```javascript webflowClientMiddleware.js
    import { WebflowClient } from "webflow-api";
    import { getToken } from "./auth/tokens.js";

    // Middleware function to initialize the Webflow client and attach it to the request object
    const webflowClientMiddleware = async (req, res, next) => {
    try {
      // Retrieve the access token for the user using Auth Logic defined in our auth guide (https://developers.webflow.com/data/reference/authorization)
      const accessToken = await getToken("user");
      if (!accessToken) {
        // If the access token is not found, log an error and send a 401 Unauthorized response
        console.log("Access token not found for user");
        return res.status(401).send("Access token not found");
      }

      // Initialize the Webflow client with the retrieved access token
      req.webflow = new WebflowClient({ accessToken });
      // Proceed to the next middleware or route handler
      next();
    } catch (error) {
      // Log any errors that occur during initialization and send a 500 Internal Server Error response
      console.error("Error initializing Webflow client:", error);
      res.status(500).send("Failed to initialize Webflow client");
    }
    };

    // Export the middleware function for use in other parts of the application
    export default webflowClientMiddleware;

    ```
  </Accordion>

  <Accordion title="3. Creating collections and fields">
    Now that you've handled setting up authorized requests, take a look at how the app makes requests to interact with collections and fields. All of the logic for interacting with the Webflow CMS API is located in the `Controllers` folder.

    `collectionsController.js` has defined five methods for interacting with collections. Review each method in detail:

    <iframe width="100%" height="700" src="https://webflow-cms-api-docs.netlify.app/collections" />
  </Accordion>

  <Accordion title="4. Creating collection items">
    With our collections set up, we can start creating items within them. In `itemsController.js`, we've defined methods for creating, reading, updating, and deleting items.

    <iframe width="100%" height="700" src="https://webflow-cms-api-docs.netlify.app/collectionItems" />
  </Accordion>

  <Accordion title="5. Publishing items">
    Lastly, we'll take a look at how we can publish and unpublish items using the Webflow CMS API.

    ### Publishing items

    * **A full site publish**: When you publish your entire site, any collection items with `isDraft` set to `false` will be published. You can publish the site through Webflow or using the [publish site endpoint](/data/reference/sites/publish).
    * **Single-item publish**: You can publish an item immediately, without publishing the full site, using the [publish item endpoint](/data/reference/cms/collection-items/staged-items/publish-item). Even if an item is set to `isDraft: true`, it will be published when using this endpoint.
    * **Live Item Creation**: The CMS API offers two options for item creation, creating a [staged item](/data/reference/cms/collection-items/staged-items/create-item) or a [live item](/data/reference/cms/collection-items/live-items/create-item-live). Creating a staged item will set the `isDraft` property to `true`, while creating a live item will set it to `false` and immediately publish the item upon creation. This endpoint is useful for immediately publishing items from an external CMS or other data sources.

    ### Unpublishing items

    Webflow also allows you to **unpublish** collection items by using the [unpublish item endpoint](/data/reference/cms/collection-items/live-items/delete-item-live). This will remove the item from the live site, and set the `isDraft` property to `true`.

    <Note title="Updated publishing behavior">
      Starting December 2024, Webflow is introducing an improved publishing workflow for collection items. When a live item's `isDraft` property is set to `true`, it will continue to remain published on the live site even after a full site publish. This allows users to make updates to the collection item in a draft state without changing what is visible on the live site.

      To remove an item from the live site, you must now explicitly call the [unpublish endpoint](/data/reference/cms/collection-items/live-items/delete-item-live). This change gives developers more precise control over the publishing state of individual items.
    </Note>

    <Accordion title="Publishing 'Status' in Webflow">
      <Frame>
        <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/8a7ee36603bd9ecdeede8e5e8238d626f32c79f1dfc076c356221b404c135995/assets/images/webflow-statuses.png" />
      </Frame>

      The Webflow UI shows a status for each collection item. This status is derived from the `isDraft` and `lastPublished` properties of the item. See the table below for more details of which status is shown based on these properties.

      | lastPublished | isDraft | Derived status    |
      | ------------- | ------- | ----------------- |
      | `null`        | `false` | Queued to publish |
      | exists        | `false` | Queued to publish |
      | `null`        | `true`  | Draft             |
      | exists        | `true`  | Draft changes     |
    </Accordion>
  </Accordion>
</AccordionGroup>

## Conclusion

Congratulations! You've successfully navigated through the process of setting up and using the Webflow API with a fully functional backend and frontend application. Here's a quick recap of what you've accomplished:

1. **Webflow Client and Backend Configuration:** You configured the WebflowClient, set up middleware, and created routes and controllers for managing collections and items.
2. **Working with Collections:** You learned how to create, retrieve, and delete collections, including handling different field types.
3. **Working with Items:** You explored how to create, retrieve, update, and delete items within a collection, managing various item states and field types.
4. **Publishing and Unpublishing:** You learned how to publish and unpublish items, and how the `isDraft` property affects the publishing state of items.

## Next Steps

* **Extend Functionality:** Enhance your application by adding new endpoints - try updating an item - or incorporating additional data processing logic.
* **Explore Localization:** Managing content localization is a crucial part of working with the Webflow CMS. Check out our[ localization guide](https://developers.webflow.com/data/docs/working-with-localization) for more details on how to localize your content effectively.
