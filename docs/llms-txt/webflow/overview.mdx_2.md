# Source: https://developers.webflow.com/webflow-cloud/storing-data/overview.mdx

***

title: Storing data in Webflow Cloud
slug: /storing-data/overview
description: Overview of storage options and setup in Webflow Cloud.
hidden: false
max-toc-depth: 2
'og:title': Storing data in Webflow Cloud
'og:description': Overview of storage options and setup in Webflow Cloud.
subtitle: 'Webflow Cloud provides built-in, flexible storage for modern web apps'
---------------------------------------------------------------------------------

Webflow Cloud lets you build and deploy modern web applications with built-in support for persistent data storage. Whether you need to store structured records or simple key-value pairs, Webflow Cloud provides flexible options to match your app’s needs.

## Storage options in Webflow Cloud

Webflow Cloud offers three storage solutions, each designed for different types of data and use cases:

<CardGroup cols={2}>
  <Card
    title="SQLite"
    href="/webflow-cloud/storing-data/sqlite"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/CMS.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/CMS.svg" alt="" className="block dark:hidden" />
        </>
    }
    iconPosition="left"
    iconSize="12"
  >
    Best for structured, relational data - like user profiles, product catalogs, or transactional records.
  </Card>

  <Card
    title="Key Value Store"
    href="/webflow-cloud/storing-data/key-value-store"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/DeveloperToolsSDK.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/DeveloperToolsSDK.svg" alt="" className="block dark:hidden" />
        </>
    }
    iconPosition="left"
    iconSize="12"
  >
    Best for unstructured, dynamic data - like user preferences, session data, or temporary settings.
  </Card>

  <Card
    title="Object Storage"
    href="/webflow-cloud/storing-data/object-storage"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/App.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/App.svg" alt="" className="block dark:hidden" />
        </>
    }
    iconPosition="left"
    iconSize="12"
  >
    Best for large files and unstructured data - like images, videos, or PDF files.
  </Card>
</CardGroup>

***

<Card
  title="Add a database to your app"
  icon={
    <>
      <img
        src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Code.svg"
        alt=""
        className="hidden dark:block"
      />
      <img
        src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Code.svg"
        alt=""
        className="block dark:hidden"
      />
    </>
  }
  iconPosition="left"
  iconSize="12"
>
  Ready to add your first database to your app? Jump into the quickstart and
  start building with real data in minutes.

  <div>
    <a href="/webflow-cloud/add-sqlite">
      <button class="button cc-primary">
        Start building
      </button>
    </a>
  </div>
</Card>

## How storage works in Webflow Cloud

Webflow Cloud connects your app to storage resources using **bindings.**

A binding is a configuration that grants your app secure, direct access to a specific resource managed by Webflow Cloud. When you declare a binding in your `wrangler.json` file and deploy your app, Webflow Cloud automatically creates a resource and grants your app permission to use it.

With bindings, you can:

* **Access resources automatically.** No secret keys required.
* **Reference bindings** as environment variables in your app.
* **Maintain isolated environments.** Each binding is specific to a project's [environment](/webflow-cloud/environments).
* **Manage bindings and resources** in the Webflow Cloud dashboard.

Bindings combine permission and API access in a single step, so you can read and write data securely and efficiently.

## Declaring a binding

Declaring a binding is the first step to using storage in your app. You can declare a binding in the Webflow Cloud dashboard or in your `wrangler.json` file.

### Before you start

Before you can declare a binding, you need to have a project in Webflow Cloud and an environment for your app. If you don't have a project or an environment, you can create by following the steps in the [getting started guide](/webflow-cloud/getting-started).

<Tabs>
  <Tab title="Dashboard">
    <Steps>
      <Step title="Open the environment dashboard">
        In Webflow Cloud, select your project and the environment where you plan to deploy your app.

        <Frame>
          <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/515b2971296baca2447480b5d065beeaed449637c70df5f8cbb2cdaf17d365f2/products/webflow-cloud/pages/concepts/storing-data/assets/environment-dashboard.png" alt="Example screenshot of the environment dashboard" />
        </Frame>
      </Step>

      <Step title="Go to the storage tab">
        In the environment dashboard, click the **Storage** tab to view all storage resources for the selected environment.

        <Frame>
          <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/9378d34e2be97f453e399771630e599672bd5db3d75413f35526b9830fc505dc/products/webflow-cloud/pages/concepts/storing-data/assets/storage-tab.png" alt="Example screenshot of the Storage tab in the environment dashboard" />
        </Frame>
      </Step>

      <Step title="Add a storage resource">
        Click the **Add Storage** button to add a new storage resource. Choose the storage type you want to use from the dropdown menu.

        <div>
          <Frame>
            <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/3550764fd2c30eb6d0ae20beffda45e3a6e4a474647c00310daac00cdc4c09c6/products/webflow-cloud/pages/concepts/storing-data/assets/storage-quickstart.png" alt="Example screenshot of adding a storage resource in the Webflock 1app" />
          </Frame>
        </div>
      </Step>

      <Step title="Copy the provided snippet to `wrangler.json`">
        Copy the provided snippet, and paste it into the `wrangler.json` file in your project's root. Replace the placeholder values with values you want to use.

        <Tabs>
          <Tab title="SQLite">
            <div class="my-6">
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 sm:gap-6 items-center">
                {" "}

                <Frame>
                  <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/862cafba68f0c97dcb23fea6f14a3a1664fe1569320eb3a54fc420e46f41c70a/products/webflow-cloud/pages/concepts/storing-data/assets/sql-snippet.png" alt="Example snippet for adding a SQLite database" />
                </Frame>

                <div>
                  | Property         | Description                                                                                                     |
                  | ---------------- | --------------------------------------------------------------------------------------------------------------- |
                  | `binding`        | The name of the binding to use in your app.                                                                     |
                  | `database_name`  | The name of the database to create.                                                                             |
                  | `database_id`    | The ID of the database to create. **Webflow Cloud will generate a unique ID for you once you deploy your app.** |
                  | `migrations_dir` | The directory containing your migration files.                                                                  |

                  <Tip title="Prepare your database schema">
                    Before deploying your app, [you need to prepare your database schema and create a migration file](http://localhost:3000/webflow-cloud/storing-data/sqlite#manage-schema-and-migrations). You can create SQL migration files manually or generate them with a migration tool such as [Drizzle ORM](https://orm.drizzle.team/). On each deployment, Webflow Cloud will apply the migrations to your database.
                  </Tip>
                </div>
              </div>
            </div>
          </Tab>

          <Tab title="Key Value Store">
            <div class="my-6">
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 sm:gap-6 items-center">
                {" "}

                <Frame>
                  <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/079cb135119c8c59694408e459378b72e85e9c6bf8f9c040852a3ecbfef28915/products/webflow-cloud/pages/concepts/storing-data/assets/kv-snippet.png" alt="Example snippet for adding a Key Value Store" />
                </Frame>

                <div>
                  | Property  | Description                                                                                                      |
                  | --------- | ---------------------------------------------------------------------------------------------------------------- |
                  | `binding` | The name of the binding to use in your app.                                                                      |
                  | `id`      | The ID of the Key Value Store to create. **Webflow will generate a unique ID for you once you deploy your app.** |
                </div>
              </div>
            </div>
          </Tab>

          <Tab title="Object Storage">
            <div class="my-6">
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 sm:gap-6 items-center">
                {" "}

                <Frame>
                  <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/d260bb849338ce8cc9bf5240777271939e8ea0c7b653eab4154f049b4c1af08a/products/webflow-cloud/pages/concepts/storing-data/assets/object-snippet.png" alt="Example snippet for adding a Object Storage" />
                </Frame>

                <div>
                  | Property      | Description                                                                                                   |
                  | ------------- | ------------------------------------------------------------------------------------------------------------- |
                  | `binding`     | The name of the binding to use in your app.                                                                   |
                  | `bucket_name` | The name of the bucket to create.                                                                             |
                  | `bucket_id`   | The ID of the bucket to create. **Webflow Cloud will generate a unique ID for you once you deploy your app.** |
                </div>
              </div>
            </div>
          </Tab>
        </Tabs>
      </Step>

      <Step title="Generate types for your binding">
        Generate TypeScript types for your bindings to enable autocomplete and type safety in your code editor:

        ```bash
        npx wrangler types
        ```

        This creates/updates a `worker-configuration.d.ts` file with your binding types.
      </Step>

      <Step title="Deploy your app">
        Deploy your app to Webflow Cloud by committing and pushing your changes to your linked GitHub repository. After deployment, you can [view and manage your storage resources in the Webflow Cloud dashboard](/webflow-cloud/storing-data/overview#managing-storage-in-the-webflow-cloud-dashboard).
      </Step>
    </Steps>
  </Tab>

  <Tab title="wrangler.json">
    <Steps>
      <Step title="Add a binding to your `wrangler.json` file">
        In your `wrangler.json` file, add a binding for the storage resource you want to use.

        <Tabs>
          <Tab title="SQLite">
            To use SQLite, add a `d1_databases` array to your `wrangler.json` file. Declare a binding for each database you want to use inside the array.

            **Note:** Webflow Cloud will assign a unique ID for each resource on deployment.

            ```json title="wrangler.json"
            {
            "d1_databases": [
                {
                "binding": "DB",
                "database_name": "MY_DATABASE",
                "database_id": "1234567890" // Webflow Cloud will assign a unique ID for each resource on deployment
                }
            ]
            }
            ```

            See the [SQLite overview](/webflow-cloud/storing-data/sqlite) for full details.
          </Tab>

          <Tab title="Key Value Store">
            To use a Key Value Store, add a `kv_namespaces` array to your `wrangler.json` file. Declare a binding for each namespace you want to use inside the array.

            **Note:** Webflow Cloud will assign a unique ID for each resource on deployment.

            ```json title="wrangler.json"
            {
            "kv_namespaces": [
                {
                "binding": "CACHE",
                "id": "8e83a86e33b541338700795162251e43" // Replace after deployment
                }
            ]
            }
            ```

            See the [Key Value Store overview](/webflow-cloud/storing-data/key-value-store) for full details.
          </Tab>

          <Tab title="Object Storage">
            To use Object Storage, add a `r2_buckets` array to your `wrangler.json` file. Declare a binding for each bucket you want to use inside the array.

            **Note:** Webflow Cloud will assign a unique ID for each resource on deployment.

            ```json title="wrangler.json"
            {
                "r2_buckets": [
                    {
                    "binding": "WEBFLOW_CLOUD_MEDIA",
                    "bucket_name": "Media",
                    }
                ]
            }
            ```
          </Tab>
        </Tabs>
      </Step>

      <Step title="Generate types for your binding">
        Generate TypeScript types for your bindings to enable autocomplete and type safety in your code editor:

        ```bash
        npx wrangler types
        ```

        This creates/updates a `worker-configuration.d.ts` file with your binding types.
      </Step>

      <Step title="Deploy your app">
        Deploy your app to Webflow Cloud. After deployment, you can view and manage your storage resources in the Webflow Cloud dashboard.
      </Step>
    </Steps>
  </Tab>
</Tabs>

For a complete walkthrough of using storage in your app, see the guides on [adding a SQLite database to your app](/webflow-cloud/add-sqlite) and [adding a Key Value Store to your app](/webflow-cloud/add-key-value-store).

## Accessing storage in your app

Once you've declared a binding, access the resource in your app using the binding name as an environment variable. Environment variables for bindings are automatically available in your app and don't need to be manually created in your environment dashboard.

<Tabs>
  <Tab title="Next.js">
    In a Next.js app, you must access the environment variables for your bindings through the [Workers runtime](/webflow-cloud/environment) using the `getCloudflareContext()` function.

    #### How to use `getCloudflareContext()`

    * **Always** call `getCloudflareContext()` inside a function (not at the top level of your module) to ensure the binding is available in the correct context.
    * **For static routes or use outside of request handlers** (such as Incremental Static Regeneration or Static Site Generation), use `getCloudflareContext({ async: true })` and await the result. This ensures the environment bindings are correctly resolved in all environments.

    {/* <!-- vale off --> */}

    ```javascript title="src/db/getDB.ts" {7-10}
    import { getCloudflareContext } from "@opennextjs/cloudflare"; // Import the function
    import { drizzle } from "drizzle-orm/d1";
    import { cache } from "react";
    import * as schema from "./schema";

    // Use in a request handler (e.g. API route)
    export const getDb = cache(() => {
      const { env } = getCloudflareContext(); // Access the cloudflare environment
      return drizzle(env.DB, { schema }); // Access the DB binding
    });

    // Use for static routes (i.e. ISR/SSG)
    export const getDbAsync = cache(async () => {
      const { env } = await getCloudflareContext({ async: true });
      return drizzle(env.DB, { schema });
    });
    ```

    {/* <!-- vale on --> */}
  </Tab>

  <Tab title="Astro">
    Access your storage resource using the binding name as an environment variable.

    ```javascript title="src/pages/index.astro" {5} maxLines=10
    import { desc } from "drizzle-orm";
    import { drizzle } from "drizzle-orm/d1";
    import { linkShare } from "../schema";

    const db = drizzle(Astro.locals.runtime.env.DB);

    const links = await db
    	.select()
    	.from(linkShare)
    	.orderBy(desc(linkShare.created));
    ---

    <html lang="en">
    	<head>
    		<meta charset="utf-8" />
    		<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    		<meta name="viewport" content="width=device-width" />
    		<meta name="generator" content={Astro.generator} />
    		<title>Astro</title>
    	</head>
    	<body>
    		<h1>Shared Links</h1>
    		<ul>
    			{
    				links.map((link) => (
    					<li>
    						<a href={link.url}>{link.title}</a>
    					</li>
    				))
    			}
    		</ul>
    	</body>
    </html>

    ```
  </Tab>
</Tabs>

<Card
  title="Start working with real data"
  icon={
    <>
      <img
        src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Code.svg"
        alt=""
        className="hidden dark:block"
      />
      <img
        src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Code.svg"
        alt=""
        className="block dark:hidden"
      />
    </>
  }
  iconPosition="left"
  iconSize="12"
>
  Ready to add your first database to your app? Jump into the quickstart and
  start building with real data in minutes.

  <div>
    <a href="/webflow-cloud/add-sqlite">
      <button class="button cc-primary">
        Start building
      </button>
    </a>
  </div>
</Card>

## Managing storage in the Webflow Cloud dashboard

Once you've deployed your app with the declared bindings, you can view and manage your storage resources directly in the Webflow Cloud dashboard:

<Steps>
  <Step title="Open the environment dashboard">
    In Webflow Cloud, select your project and environment where your app is
    deployed with storage bindings configured in `wrangler.json`.
  </Step>

  <Step title="Go to the storage tab">
    In the environment dashboard, click the **Storage** tab to view all storage
    resources for the selected environment. Each storage binding shows its name, type,
    and creation date.

    <Frame>
      <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/9378d34e2be97f453e399771630e599672bd5db3d75413f35526b9830fc505dc/products/webflow-cloud/pages/concepts/storing-data/assets/storage-tab.png" alt="Storage tab in Webflow Cloud environment dashboard" />
    </Frame>
  </Step>

  <Step title="View and manage data">
    Click a binding to open the database viewer. You can: - Create, read,
    update, and delete records (CRUD) - Search and sort data

    <Frame>
      <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/29730530f2a03935c0930c5f7c7a4a8c5ac70f3d892e15408572a49717914399/products/webflow-cloud/pages/concepts/assets/database-viewer.png" alt="Database viewer in Webflow Cloud" />
    </Frame>
  </Step>
</Steps>

## Next steps

* [Learn more about SQLite](/webflow-cloud/storing-data/sqlite)
* [Learn more about Key Value Store](/webflow-cloud/storing-data/key-value-store)
* [See how to configure storage bindings in your project](/webflow-cloud/storing-data/overview#declaring-a-binding)
* [Learn about storage limits in Webflow Cloud](/webflow-cloud/limits)

## FAQs

<Accordion title="Where can I see my storage resources?">
  Once you've deployed your app with the declared bindings, you can view and manage your storage resources directly in the Webflow Cloud dashboard.

  <Frame>
    <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/3f00ba97f6c70901fbe87e4b568038f47e1a2a4972ff65811de42db817fba2b2/products/webflow-cloud/pages/concepts/assets/bindings-tab.png" alt="Storage tab in Webflow Cloud environment dashboard" />
  </Frame>
</Accordion>

<Accordion title="I declared a binding in my `wrangler.json` file, but I can't see it in the dashboard.">
  If you have an existing Webflow Cloud project, you may need to edit your project settings to enable storage

  1. Go to your project in the Webflow Cloud dashboard.
  2. Select the "..." icon in the "Actions" section of the menu.
  3. Select "Edit" (you don't actually need to edit anything).
  4. Press "Save Changes" to update your project.

  <Frame>
    <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/0996c151f75ca00b6658a1728cd0b48dfe9f037c925307371d99ebf54d039219/products/webflow-cloud/pages/concepts/assets/edit-project.png" alt="Project settings in Webflow Cloud" />
  </Frame>

  Save the changes and redeploy your app. Once your app deploys you should see the storage tab in the dashboard.
</Accordion>

<Accordion title="I can't access the API methods on my binding">
  After declaring a binding, make sure you've generated the types for your binding. After running the following command, you'll be able to access the API methods on your binding.

  <CodeBlocks>
    ```bash title="Astro"
    wrangler types
    ```

    ```bash title="Next.js"
    npm run cf-typegen
    ```
  </CodeBlocks>

  This creates/updates a `worker-configuration.d.ts` file with your binding types.
</Accordion>
