# Source: https://developers.kit.com/kit-app-store/building-apps.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Building apps

> Building an app for the Kit App Store

Kit is opening up a world of opportunities and functionality for our creators by empowering third-party developers like you to build on top of our application and better integrate the creator’s toolkit in one place.

Building an app on Kit is completely self-serve. Here's how you can build, test, and publish an app in your Kit account.

## Creating your app

Visit the Kit App Store by going to **"Automate"** in the top navigation menu, followed by [Apps](https://app.kit.com/apps). From there, select the [Build tab](https://app.kit.com/apps?is=created), and click + New app at the top right.

<img width="800" alt="creating-a-new-app" src="https://mintcdn.com/kit-314e57c1/dSCrspkEWxNDV3Va/images/kit_app_store/creating-a-new-app.png?fit=max&auto=format&n=dSCrspkEWxNDV3Va&q=85&s=cacc8df43082e4e41b48b45c292b0997" data-path="images/kit_app_store/creating-a-new-app.png" />

A form will pop up. Fill it out with your app's name, and click "Save".

Once you do this, you'll be directed to an **app details** settings page for your newly created app.

<img width="800" alt="app details settings" src="https://mintcdn.com/kit-314e57c1/dSCrspkEWxNDV3Va/images/kit_app_store/app-details-page.png?fit=max&auto=format&n=dSCrspkEWxNDV3Va&q=85&s=3beb2789a6784441c305f9e0a0ca3f3f" data-path="images/kit_app_store/app-details-page.png" />

The details you provide here will be shown on the app details page that appears when users click your app's "Learn more" option in the Kit App Store.

<img width="400" alt="learn more Kit App Store button" src="https://mintcdn.com/kit-314e57c1/dSCrspkEWxNDV3Va/images/kit_app_store/learn-more-button.png?fit=max&auto=format&n=dSCrspkEWxNDV3Va&q=85&s=66102567a2bc5ba81990c82f29b3e591" data-path="images/kit_app_store/learn-more-button.png" />

<Note>Preview the app details page by clicking your app's "Preview" option in the ["Build" tab](https://app.kit.com/apps?is=created) of the Kit App Store. <img width="400" alt="app preview button" src="https://mintcdn.com/kit-314e57c1/dSCrspkEWxNDV3Va/images/kit_app_store/app-preview-button.png?fit=max&auto=format&n=dSCrspkEWxNDV3Va&q=85&s=60955b4ef8b71fd32dbdb4adebfc81b5" data-path="images/kit_app_store/app-preview-button.png" /></Note>

Only the `App name` field is required when you create and test your app. But you'll need to provide more information before you can publish the app to the Kit App Store. This information includes:

* Icon
* Summary
* Description
* Resource links

Click "Save" to save the changes to your app's details.

## API and plugin access

An app can contain either API access, one or many plugins, or both. Here are the key differences:

* **API access:** You can allow creators to install apps that can link together external platforms to work in harmony. We control authentication here and developers have to request access on behalf of a creator to us to approve. This is all built upon V4 of our API.
  * An example API only app would be TeachKit - that solely utilizes the Kit APIs to manage subscribers that use TeachKit's free online courses.
* **Plugins:** You can add content directly into the Kit app UI. Kit needs to authenticate against the third party to be able to pull the data required to be rendered within Kit.
  * An example plugin only app would be GIPHY - which utlises the [media source plugin](/plugins/media-source/overview) to allow creators to insert gifs directly from GIPHY into their email content. No additional API access is required for this app.
* **Both:** You can also have apps that combine API and plugin access, with apps such as Mighty Networks offering subscriber and tag syncing alongside [content block plugins](/plugins/content-blocks/overview), helping creators manage and promote their communities through Kit.

To set up your app authentication strategies, visit the "Authentication" tab, where you can configure and toggle API and plugin access on and off.

<img width="800" alt="app authentication" src="https://mintcdn.com/kit-314e57c1/dSCrspkEWxNDV3Va/images/kit_app_store/app-authentication.png?fit=max&auto=format&n=dSCrspkEWxNDV3Va&q=85&s=60dfc3922e3b324ce16de29877ee9acb" data-path="images/kit_app_store/app-authentication.png" />

For more details on authentication, visit our [app authentication guide](/kit-app-store/authentication), or visit the API and plugin specific pages:

* [API](/api-reference/authentication)
* [Plugins](/plugins/oauth-authorization)

## Testing your app

View your apps on the ["Build" tab](https://app.kit.com/apps?is=created) of the Kit App Store. You'll be able to see:

* Whether you have installed the app—from the display of the green installed tick, or
* Whether it is a draft, from the "Draft" badge in the bottom corner. When is the "Draft" status, only you are able to see the app in your own account.

<img width="400" alt="testing your app" src="https://mintcdn.com/kit-314e57c1/ohR8KbVxvspIDffR/images/kit_app_store/testing-your-app.png?fit=max&auto=format&n=ohR8KbVxvspIDffR&q=85&s=838190d743f9841766014ffdd0d084f4" data-path="images/kit_app_store/testing-your-app.png" />

From here, click Preview to view your app's app details page, as well as install it within your own account.

<img width="800" alt="GIPHY app details page" src="https://mintcdn.com/kit-314e57c1/dSCrspkEWxNDV3Va/images/kit_app_store/giphy-app-details-page.png?fit=max&auto=format&n=dSCrspkEWxNDV3Va&q=85&s=69dcccc3f0c91577696d32dc6cc635ed" data-path="images/kit_app_store/giphy-app-details-page.png" />

<Note>The app will not be publically discoverable for other Kit users to install until you've published it.</Note>

### V4 API Keys

Though all apps accessing our API require OAuth authentication before they can be published, a great way of prototyping and testing our API's functionality is to use V4 API keys.

More details on creating and managing API keys [can be found here](/api-reference/authentication).

<Note>API keys are meant for individual use only. If you're creating something for people to use, you'll need to build an app—giving you access to plugins, bulk and purchase endpoints, higher rate limits, and more.</Note>


Built with [Mintlify](https://mintlify.com).