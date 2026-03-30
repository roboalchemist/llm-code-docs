# Source: https://docs.beefree.io/beefree-sdk/visual-builders/popup-builder/testing-and-integrating.md

# Testing and Integrating

## Creating an application <a href="#creating-an-application" id="creating-an-application"></a>

When you log into the [Beefree SDK Console](https://developers.beefree.io/) you can immediately see what type of applications you have already created under your Beefree SDK subscriptions. To create a Popup application, head over to the **Popup Builder Application** section and click on **Activate**.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2Fve8ErU4ozn20Sardyfhz%2FCleanShot%202025-03-13%20at%2014.09.44.png?alt=media&#x26;token=8d72c5c3-61d6-41ad-b657-3f12020430ff" alt=""><figcaption></figcaption></figure>

Once created, head over to “Details” for all server-side configurations. Paid applications allow you to create child [development applications](https://docs.beefree.io/beefree-sdk/getting-started/readme/development-applications), to ease new feature testing, development, and maintenance.

All builders share the same **core functionalities**, including authentication and configuration. If you have already integrated our Email builder, you can re-use most of your work using the same configuration and callbacks.

## Integrating the Popup Builder

Out-of-the-box, the setup and configuration are the same as [Email and Page Builder](https://docs.beefree.io/beefree-sdk/getting-started/readme/installation). This section will cover the settings specific to Popup Builder. Check out our [Getting Started guide](https://docs.beefree.io/beefree-sdk/getting-started/readme/installation) if you’re new to Beefree SDK or unfamiliar with the configuration basics (as seen in the example below).

```json

beeConfig: {
  container: 'bee-plugin-container', // [mandatory]
  ...
}

```

Loading Popup Builder with no additional settings will give the end-user a beautifully designed popup and workspace to design their content. However, Popup Builder comes with an additional, robust set of configuration options to customize the workspace. This allows the host application to build a workspace that matches their popup’s look and feel and that of the destination page.

For example, the host app can customize…

* The popup workspace background to view how the popup will look “in context” on the destination page.
* The theme and position of the popup for both desktop and mobile design modes.

Continue reading to learn more on how to customize the workspace, starting with the common settings and working up to a full custom layout.

## HTML output <a href="#html-output" id="html-output"></a>

In Email and Page Builder, the Beefree SDK HTML parser service converts your template into an HTML document customized for email or pages, respectively. However, the Popup Builder will not return a full HTML page because the host application is the final destination. In addition, Beefree SDK Popup Builder doesn’t provide the scripts to control the popup’s behavior, such as opening and closing. Rather, Popup Builder provides the HTML “partials” to embed within your popup’s content area or body.

The HTML partial will come with all the CSS required to look as it did in the preview mode. The parser service will wrap the content with a special container to clear all the host application styles and prevent style conflicts. The HTML output is designed to be embedded into any popup framework or application and still render the way it appears in the builder.

## Developer resources <a href="#developer-resources" id="developer-resources"></a>

Our Github account has some resources that might help you out when testing and integrating the Popup Builder.

[**Sample code**](https://github.com/BeefreeSDK/beefree-sdk-sample-client)

Examples of different implementations and configurations that you can draw from to speed up your development.

[**Popup templates**](https://dam.beefree.io/popuptemplates)

A collection of ready-made templates that you can use right away and add to your application.
