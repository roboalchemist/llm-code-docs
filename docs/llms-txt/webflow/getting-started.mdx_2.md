# Source: https://developers.webflow.com/webflow-cloud/getting-started.mdx

***

title: Getting Started
slug: getting-started
description: Build and deploy your first Webflow Cloud app
hidden: false
'og:title': Getting Started
'og:description': Build and deploy your first Webflow Cloud app
subtitle: Deploy your first project to Webflow Cloud using Next.js or Astro.
----------------------------------------------------------------------------

In this guide, you'll learn how to create projects and environments, deploy your app to your Webflow site, and integrate your Webflow design system with your app.

**Time Estimate:** 30 minutes

**Prerequisites:**

* A Webflow account
* A GitHub account
* Node.js 20.0.0 or higher and `npm` installed

## Getting started

### 1. Install the Webflow CLI

In your terminal, run the following command to use the CLI globally:

```bash
npm install -g @webflow/webflow-cli
```

You can run the command `webflow --version` to verify that the CLI tool installed successfully.

### 2. Create a new Webflow site

Create a new Webflow site by cloning the [Astral Fund template.](https://webflow.com/made-in-webflow/website/astralfund-919afdc1091df68b8dc1347f952a) This site is pre-configured with styles, variables, and components optimized for Webflow Cloud and DevLink.

<Steps>
  <Step title="Open the [Astral Fund template](https://webflow.com/made-in-webflow/website/astralfund-919afdc1091df68b8dc1347f952a)">
    View the AstralFund template in "Made in Webflow"
  </Step>

  <Step title="Clone the template">
    Click the "Clone in Webflow" button, then in the next window click "Create site."
  </Step>

  <Step title="Add site details">
    Give your site a name and determine who should have access to your site. Once you've created your site, it will open in Webflow.
  </Step>

  <Step title="Review styles, components, and variables">
    Optionally, review the [styles](https://help.webflow.com/hc/en-us/articles/33961362040723-Style-panel-overview), [variables](https://help.webflow.com/hc/en-us/articles/33961268146323-Variables), and [components](https://help.webflow.com/hc/en-us/articles/33961303934611-Components-overview) included in the site. You will export these to your new app in the following steps.
  </Step>

  <Frame>
    <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/91708b33e8f975a03d72eafa153c7ec0caf1804aec693b43e86944b652f97e02/products/webflow-cloud/pages/introduction/assets/astralfund.png" alt="Webflow site" />
  </Frame>
</Steps>

### 3. Create a new app

Use the Webflow CLI to create a new Astro or Next.js application. The CLI will generate a project scaffold that's synced with your Webflow site's design system through [DevLink.](/devlink/reference/overview)

<div>
  <Frame>
    <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/0303fa14075c25c3a2fa083cbb2de654fb6f9d09d646311cf9b2cd73b2b9bdd6/products/webflow-cloud/pages/introduction/assets/webflow-cli.png" alt="Webflow CLI" />
  </Frame>
</div>

<Steps>
  <Step title="Initialize your project">
    In your terminal, run the command

    ```bash
    webflow cloud init
    ```
  </Step>

  <Step title="Select your framework">
    When prompted in the terminal, choose a supported framework to create a starter project (Astro or Next.js)
  </Step>

  <Step title="Select your mount path">
    When prompted in the terminal, enter the path where you plan to mount your app on your Webflow site (for example, /app → mysite.webflow\.io/app).
  </Step>

  <Step title="Authenticate with Webflow">
    When prompted, authenticate with Webflow and select the site you just created for your Webflow Cloud project.
  </Step>

  <Step title="Import your Webflow design system">
    When prompted in the terminal, select the same Webflow site you used to authenticate. Once selected, the Webflow CLI will import any available styles, variables, and components via DevLink. DevLink will show a success message upon successful export to your app.
  </Step>

  <Step title="Publish your project to a GitHub repository">
    In your terminal, run the following commands to navigate to your new project, and create a git repository. [**Once created, publish the repository to GitHub.**](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github) You will need to publish your local project to GitHub to create a new Webflow Cloud project as outlined in the next step.

    ```bash
        cd your-project-name
        git init
    ```
  </Step>
</Steps>

### 4. Create a new Webflow Cloud project

Connect GitHub to Webflow Cloud, create a project, and configure an environment for automated deployments.

<div>
  <Frame>
    <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/f349396b97fbcd8de4691b6350fea896df1fef56a3c8dc7e0307119b9f38bf63/products/webflow-cloud/pages/introduction/assets/project-setup-05-20.png" alt="Webflow Cloud project creation" />
  </Frame>
</div>

<Steps>
  <Step title="Open Webflow Cloud">
    In Webflow, navigate to your site's settings and select "Webflow Cloud" from the sidebar.
  </Step>

  <Step title="Authenticate with Github">
    Click the "Login to GitHub" button to connect your GitHub account. Then click the "Install GitHub" button. Follow the instructions to enable Webflow Cloud to access your GitHub repositories.
  </Step>

  <Step title="Create a new Webflow Cloud project">
    Click "Create New Project"
  </Step>

  <Step title="Add project details">
    * Choose a **name** for your Webflow Cloud project.
    * Provide the URL of your newly created **GitHub repository.**
    * Optionally, enter a **description** and **directory** path for your app.
    * Click **"Create project"** to save your project.
  </Step>

  <Step title="Create a new Environment">
    <div>
      <Frame>
        <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/2036670eb1d95bef297542eeb93354e0f844a3a31ccf92d3f4841c2e5c114874/products/webflow-cloud/pages/introduction/assets/github-setup.png" alt="Webflow Cloud environment creation" />
      </Frame>
    </div>

    * Choose a **branch** to deploy your project from.
    * Choose a **mount path** for your project (for example, /admin → mysite.webflow\.io/admin).
    * Click **"Create environment"** to save a new environment for the project.
  </Step>

  <Step title="Publish your Webflow Site">
    If you have never published your site before, click the "Publish Site" button in the top right of your Webflow Dashboard. This will ensure your environment is properly set up.

    <Warning title="You won't see your app yet!">
      We need to build and deploy your Astro or Next.js before you see your project on your mount path. Follow the steps below to deploy your project.
    </Warning>
  </Step>
</Steps>

### 5. Add your Webflow design system to your Webflow Cloud app

Add Webflow components to your app by importing them from the DevLink folder, which contains assets synced from your Webflow design system.

Your scaffolded app already includes your global styles, and the [DevLinkProvider](/devlink/docs/component-export/whats-exported#devlinkprovider) to manage Webflow interactions in your project's layout files.

<Tabs>
  <Tab title="Astro">
    <Steps>
      <Step title="Install dependencies and run your project locally">
        Run the following commands in your terminal:

        ```bash
        npm install
        npm run dev
        ```

        <Note>
          Currently, Webflow Cloud only supports using the 

          `npm`

           package manager
        </Note>
      </Step>

      <Step title="Add Webflow components to your Astro project">
        In the `pages` directory, update `index.astro` to include the `Navbar` and `Footer` components from the `/devlink` folder in the root of your project. Import the components, and include them within the page structure.

        ```typescript title="index.astro" maxLines={15}
          ---
          import Layout from '../layouts/Layout.astro';
          import { Section, Container, Block, Link } from '../../devlink/_Builtin/Basic';
          import { Navbar } from '../../devlink/Navbar'; // Import the Navbar component
          import { Footer } from '../../devlink/Footer'; // Import the Footer component
          ---

          <Layout>
          {/* Add Navbar with props. Be sure to include the client load directive */}
            <Navbar
                navbarLinkFeatures="Hello"
                navbarLinkProducts="Webflow"
                navbarLinkResources="Cloud"
                navbarLinkContact=""
            client:load />
            <Section
              client:load
              tag="section"
              className="margin-bottom-24px"
              style={{
                minHeight: '100vh',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center'
              }}
            >
              <Container>
                <Block
                  tag="div"
                  className="hero-split"
                  style={{
                    textAlign: 'center',
                    maxWidth: '600px',
                    margin: '0 auto'
                  }}
                >
                  <h1 class="margin-bottom-24px">Welcome to Webflow Cloud</h1>
                  <p class="margin-bottom-24px">This is a simple test using Basic components with enhanced styling.</p>
                  <div>
                    <Link
                      button={true}
                      options={{
                        href: "#"
                      }}
                      className="button-primary"
                    >
                      Get Started
                    </Link>
                  </div>
                </Block>
              </Container>
            </Section>
            <Footer client:load /> {/* Add Footer with Client load directive */}
          </Layout>

          <style>
            h1 {
              font-size: 2.5rem;
              font-weight: 700;
              background: linear-gradient(83.21deg, #3245ff 0%, #bc52ee 100%);
              -webkit-background-clip: text;
              -webkit-text-fill-color: transparent;
              background-clip: text;
            }
          </style>

        ```

        <Note>
          Add the `client:load` directive to each component, to indicate Astro should load this component on the page.
        </Note>
      </Step>

      <Step title="Test your changes in a local preview environment">
        In your terminal, run the following command to start your project in a local preview environment that mimics your Webflow Cloud environment:

        ```bash
        npm run preview
        ```
      </Step>
    </Steps>
  </Tab>

  <Tab title="Next.js">
    <Steps>
      <Step title="Install dependencies and run your project locally">
        Run the following commands in your terminal:

        ```bash
        npm install
        npm run dev
        ```

        <Note>
          Currently, Webflow Cloud only supports using the 

          `npm`

           package manager
        </Note>
      </Step>

      <Step title="Add Webflow components to your Next.js project">
        Update `/src/page.tsx` to include the `Navbar` and `Footer` components from the `/devlink` folder. Import the components, and include them within the page structure.

        ```typescript title="page.tsx" maxLines={15}
        "use client";

        import { Section, Block, Link } from "@/devlink/_Builtin";
        import { Navbar } from "@/devlink/Navbar"; // Import the Navbar component
        import { Footer } from "@/devlink/Footer"; // Import the Footer component

        export default function Home() {
          return (
            <Section
              tag="section"
              style={{
                minHeight: "100vh",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
              }}
            >
              <Block tag="div" className="container">
              {/* Add Nav Bar with props*/}
                <Navbar
                  navbarLinkFeatures="Hello"
                  navbarLinkProducts="Webflow"
                  navbarLinkResources="Cloud"
                  navbarLinkContact=""
                />
                <Block
                  tag="div"
                  className="hero-split"
                  style={{
                    textAlign: "center",
                    maxWidth: "600px",
                    margin: "0 auto",
                  }}
                >
                  <h1
                    className="margin-bottom-24px"
                    style={{
                      fontSize: "2.5rem",
                      fontWeight: 700,
                      background: "linear-gradient(83.21deg, #3245ff 0%, #bc52ee 100%)",
                      WebkitBackgroundClip: "text",
                      WebkitTextFillColor: "transparent",
                      backgroundClip: "text",
                    }}
                  >
                    Welcome to Webflow Cloud
                  </h1>
                  <Block tag="p" className="margin-bottom-24px">
                    This is a simple test using Basic components with enhanced styling.
                  </Block>
                  <div>
                    <Link
                      button={true}
                      options={{
                        href: "#",
                      }}
                      className="button-primary"
                    >
                      Get Started
                    </Link>
                  </div>
                </Block>
                <Footer /> {/* Add Footer */}
              </Block>
            </Section>
          );
        }

        ```
      </Step>

      <Step title="Test your changes in a local preview environment">
        In your terminal, run the following command to start your project in a local preview environment that mimics your Webflow Cloud environment:

        ```bash
        npm run preview
        ```
      </Step>
    </Steps>
  </Tab>
</Tabs>

### 6. Deploy your project to Webflow Cloud

<Steps>
  <Step title="Authenticate with Webflow">
    In your terminal, run the following command to authenticate with Webflow:

    ```bash
    webflow auth login
    ```

    This command opens a browser window to authenticate your Webflow account. After you grant access, you'll be prompted in your terminal to select a site for deployment. The CLI then creates/updates a `.env` file at the root of your project with the necessary `WEBFLOW_SITE_ID` and `WEBFLOW_API_TOKEN`.
  </Step>

  <Step title="Deploy using the Webflow CLI">
    In your terminal, run the following command to deploy your project to Webflow Cloud:

    ```bash
    webflow cloud deploy
    ```

    Additionally, when you commit your changes to your GitHub branch, Webflow Cloud will automatically detect the changes and deploy your project to your environment. Learn more on [deployments in the documentation.](/webflow-cloud/deployments)

    <Warning title=" Your deployment may take up to 2 minutes to complete">
      Your deployment may take up to 2 minutes to complete. You can view the status of your deployment in your [Environment Details](/webflow-cloud/deployments#deployment-history) dashboard, and see details of your build and deployment in the [build logs.](/webflow-cloud/deployments#build-logs)
    </Warning>
  </Step>

  <Step title="View your app at your site's URL + mount path">
    Once your app has been successfully deployed, navigate to your site's domain and mount path to see your newly deployed Webflow Cloud app!

    **🎉Congratulations! 🎉**<br />
    You've successfully created and deployed a Webflow Cloud project that is seamlessly integrated with your Webflow design system. Pat yourself on the back!
  </Step>
</Steps>

## Next steps

Now that you've successfully created and deployed a Webflow Cloud project, here's what you can do next.

<CardGroup>
  <Card
    title="Bring your app to Webflow Cloud"
    href="/webflow-cloud/bring-your-own-app"
    iconSize="12"
    iconPosition="left"
    icon={
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Apps.svg" alt="" className="dark-icon" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Apps.svg" alt="" className="light-icon" />
            </>
        }
  >
    Learn about project configuration options to work seamlessly with Webflow Cloud, and add advanced functionality to your new project.
  </Card>

  <Card
    title="Optimize your workflow"
    href="/webflow-cloud/environments"
    iconSize="12"
    iconPosition="left"
    icon={
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Optimize.svg" alt="" className="dark-icon" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Optimize.svg" alt="" className="light-icon" />
            </>
        }
  >
    Learn how to manage environments for different stages of development
  </Card>

  <Card
    title="Manage deployments"
    href="/webflow-cloud/deployments"
    iconSize="12"
    iconPosition="left"
    icon={
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/CloudUpload.svg" alt="" className="dark-icon" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/CloudUpload.svg" alt="" className="light-icon" />
            </>
        }
  >
    Explore deployment options and Webflow Cloud's CI/CD integration with GitHub to streamline your release process
  </Card>

  <Card
    title="Add a SQLite database to your app"
    href="/webflow-cloud/add-sqlite"
    iconSize="12"
    iconPosition="left"
    icon={
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/CMS.svg" alt="" className="dark-icon" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/CMS.svg" alt="" className="light-icon" />
            </>
        }
  >
    Add a SQLite database to your app to store and retrieve user data.
  </Card>
</CardGroup>

## Troubleshooting

<Accordion title="I'm seeing a 404 error when I try to access my app">
  If you have never published your site before, publish it now. If you don't see the app, check your mount path, confirm the environment exists, and verify that the latest deployment succeeded.
</Accordion>

<Accordion title="A deployment doesn't start when I push to my Github repo">
  The [Webflow Cloud GitHub App](https://github.com/apps/webflow-cloud/installations/select_target) may not have access to your repository. To check, go to the `Webflow Cloud` tab in your Webflow site settings and click "Install GitHub App." Follow the prompts on GitHub to make sure Webflow has access to read from your repository. Once you grant access, try committing to the branch that Webflow Cloud should be monitoring for deployments in your app.
</Accordion>

<Accordion title="I can't see assets in my app">
  If you're referencing assets in your project, you'll need to reference the mount path of your project (`/app` → `mysite.webflow.io/app`) to serve them correctly.

  [See more on referencing assets →](/webflow-cloud/bring-your-own-app#manage-assets-and-apis)
</Accordion>
