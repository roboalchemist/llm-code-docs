# Source: https://developers.webflow.com/data/v2.0.0-beta/docs/designer-extensions.mdx

***

title: Designer API & Extensions
slug: /docs/designer-extensions
hidden: false
layout: overview
hide-toc: true
'og:title': Webflow API Docs - Designer Extensions
'og:description': >-
An overview of how Webflow Apps work within the Designer to manipulate
Elements on the Canvas
----------------------

<img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/53e647a7afdd983ee0428ad7cd5475417a56edb0a62afe1b90499db3eb819c17/assets/images/7500640-New_Apps_Screengram.gif" alt="A Designer Extension creating elements on the canvas." />

Designer Extensions are web applications that run directly inside the Webflow Designer. Using the [Designer APIs](/designer/reference/introduction), you can create powerful new tools that integrate seamlessly with a user's workflow, helping them design, create, and optimize their sites faster than ever.

## What you can build

Using the [Designer APIs](/designer/reference/introduction), you can build extensions that programmatically interact with a user's design and content in real-time. This opens up a world of possibilities for workflow automation and creative tooling.

<CardGroup>
  <Card
    title="Automate layout and content creation"
    icon={
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Blog.svg" alt="" className="hidden dark:block" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Blog.svg" alt="" className="block dark:hidden" />
            </>
        }
    iconPosition="left"
    iconSize="12"
  >
    Generate complex components, populate data from third-party sources, or build entire page structures with a single click.
  </Card>

  <Card
    title="Manage design systems"
    icon={
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/DesignSystems.svg" alt="" className="hidden dark:block" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/DesignSystems.svg" alt="" className="block dark:hidden" />
            </>
        }
    iconPosition="left"
    iconSize="12"
  >
    Create tools that allow users to apply and maintain consistent branding, manage variables, and swap themes.
  </Card>

  <Card
    title="Streamline asset management"
    icon={
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/ImageControls.svg" alt="" className="hidden dark:block" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/ImageControls.svg" alt="" className="block dark:hidden" />
            </>
        }
    iconPosition="left"
    iconSize="12"
  >
    Build extensions that connect to external asset libraries, optimize images, or automate asset organization.
  </Card>

  <Card
    title="Create dynamic site structures"
    icon={
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Folders.svg" alt="" className="hidden dark:block" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Folders.svg" alt="" className="block dark:hidden" />
            </>
        }
    iconPosition="left"
    iconSize="12"
  >
    Programmatically add and organize pages and folders, perfect for sites with complex information architecture.
  </Card>
</CardGroup>

## How they work

Designer Extensions are single-page applications that run inside a secure `iframe` within the Webflow Designer. They use Webflow's client-side **Designer APIs** to communicate with the Designer, allowing your app to perform actions that would typically require manual user intervention. For more advanced use cases, your extension can also integrate with your own backend services and third-party APIs including Webflow's [Data APIs](/data/reference/introduction).

## The development workflow

From your first line of code to a public Marketplace launch, here's an overview of the development process.

<Steps>
  <Step title="Register your App in Webflow">
    Before you can start building, you need to register a new app within your Webflow Workspace settings.

    <a href="/data/docs/register-an-app">
      <button class="cc-primary">Register your App</button>
    </a>
  </Step>

  <Step title="Create a Designer Extension from the CLI">
    Use the Webflow CLI to scaffold a starter project and run a local development server for live testing.

    <a href="/apps/designer-extensions/getting-started">
      <button class="cc-primary">Create a Designer Extension from the CLI</button>
    </a>
  </Step>

  <Step title="Build with the Designer APIs">
    The Designer APIs are how your app will interact with the Webflow canvas, providing a robust interface to control the Designer.

    <a href="/designer/reference/introduction">
      <button class="cc-primary">Build with the Designer APIs</button>
    </a>
  </Step>

  <Step title="Publish to your Workspace">
    When you're ready, upload your extension to Webflow to share it with your team for testing and internal use in your Workspace.

    <a href="/apps/docs/publishing-your-app">
      <button class="cc-primary">Publish to your Workspace</button>
    </a>
  </Step>

  <Step title="Submit to the Marketplace">
    Share your creation with the world by submitting it to the Webflow Marketplace.

    <a href="/apps/docs/marketplace/submitting-your-app">
      <button class="cc-primary">Submit to the Marketplace</button>
    </a>
  </Step>
</Steps>

## FAQs

<Accordion title="Can I use the Data APIs in my Designer Extension?">
  Yes, you can use the [Data APIs](/data/reference/introduction) in your Designer Extension to access and update data from Webflow's servers. This is called a **Hybrid App**. When you setup your app, you'll need to select both the **Data Client** and **Designer Extension** options.
</Accordion>

<Accordion title="Which frameworks and libraries can I use to build my Designer Extension?">
  You can use any framework that outputs static resources and runs in a browser environment. Just make sure your extension fits within the iframe dimensions provided by Webflow.
</Accordion>

<Accordion title="How do I test my Designer Extension?">
  <Steps>
    <Step title="Install your extension on a test site">
      In the left sidebar of your workspace, navigate to <strong>Apps & Integrations</strong> > <strong>Develop</strong>. Click the "..." button next to your app and select <strong>Install App</strong>. You'll see an authorization screen where you can select the sites or workspace you want to install the app on.
    </Step>

    <Step title="Run the extension in development mode">
      In your terminal, navigate to your project folder and run the following command:

      ```bash
      webflow extension serve
      ```

      This will start development mode locally (port 1337).
    </Step>

    <Step title="Preview and interact with your extension in the Designer">
      On your test site, open the Apps pane and find your app. Click "Launch Development App" to preview and interact with your locally hosted extension in the Designer.
    </Step>
  </Steps>
</Accordion>

<Accordion title="Why isn't my extension interacting with Webflow as expected?">
  * Double-check your use of the [Designer APIs](/designer/reference/overview) and ensure you’re using the correct methods.
  * Check the browser console for errors and review our [error handling guidelines](/designer/reference/error-handling).
  * Designer APIs only access content on the current page, not other sites or pages.
  * Make sure your app has the right permissions and scopes.
  * For Data API issues, verify you’re using the correct endpoints and valid tokens.
</Accordion>

<Accordion title="Why does my app look different in Webflow than expected?">
  * Designer Extensions run in an iframe with controlled dimensions. Check your configuration and use [resizing methods](https://developers.webflow.com/designer/reference/resize-extension) if needed.
  * Use scoped CSS or scoped class names to avoid style conflicts with Webflow’s native styles.
  * Test at different viewport sizes to ensure responsive behavior.
</Accordion>

<Accordion title="Why can't I upload a new version of my Designer Extension Bundle?">
  Only Workspace admins can upload new bundles. If you’re not an admin, contact your Workspace administrator to upload the bundle or grant you the necessary permissions.
</Accordion>

<Accordion title="Why isn't my extension showing up in Webflow?">
  * Make sure you’ve [bundled your app with the Webflow CLI](/apps/docs/publishing-your-app#build-your-extension) and uploaded your Designer Extension via the Dashboard.
  * Confirm the app is installed on your site or workspace (check the App Development section in your workspace).
</Accordion>
