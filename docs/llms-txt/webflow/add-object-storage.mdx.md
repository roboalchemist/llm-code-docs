# Source: https://developers.webflow.com/webflow-cloud/add-object-storage.mdx

***

title: Add Object Storage to your app
slug: add-object-storage
description: Add Object Storage to your app
subtitle: Upload large files to bucket in your Webflow Cloud app
----------------------------------------------------------------

This guide will show you how to add [Object Storage](/webflow-cloud/storing-data/object-storage) to your project and use it to store and serve files. You'll learn how to:

* Set up an Object Storage binding
* List and display files from your bucket
* Upload files to your bucket with proper validation
* Handle large file uploads using multipart uploads

## Prerequisites

Before you begin, make sure you have:

* A GitHub account
* A code editor like [Cursor](https://www.cursor.com/) or [VS Code](https://code.visualstudio.com/)
* Node.js 20+ and npm 10+
* Basic familiarity with JavaScript/TypeScript

## Set up your project

This tutorial uses a repository with pre-built UI, backend endpoints, and helper utilities for file uploads and management. Follow along with the steps below and reference the code in the example project to see how Object Storage is used in this Webflow Cloud app. You may need to make some code changes to the project to get it working with your Webflow Cloud environment.

<Steps>
  <Step title="Fork and clone the example repository">
    To start, [fork the project on Github](https://github.com/Webflow-Examples/webflow-cloud-object-storage/fork) so you have your own copy to work with.

    Next, clone your fork of the starter repository to your local machine and install dependencies:

    ```bash
    git clone https://github.com/<YOUR-GITHUB-USERNAME>/webflow-cloud-object-storage.git
    cd webflow-cloud-object-storage
    npm install
    ```

    The project uses Astro with TypeScript and includes all necessary dependencies for Object Storage operations.
  </Step>

  <Step title="Create a new Webflow Cloud project">
    Go to the Webflow Cloud dashboard in your site settings and create a new Webflow Cloud project.

    1. Go to your Webflow Cloud dashboard
    2. Click "Install Github app" to authorize Webflow Cloud for your fork of this repo - follow the prompts on Github
    3. Click "Create new project"
    4. Name your project
    5. Choose the `webflow-cloud-object-storage` repository
    6. Click "Create project"

    <Note title="Repository linking">
      Once the project is created, it will automatically deploy when you push changes to the linked GitHub repository.
    </Note>
  </Step>

  <Step title="Create an environment">
    Create a new environment for the main branch

    1. In the same modal, choose the `main` branch
    2. Choose a mount path for the environment (for example, /app → mysite.webflow\.io/app)
    3. Click "Create environment"
    4. A new row should appear in the table with your new environment. Click into it to see the environment details
    5. If you have never published your site before, publish it now.

    <Note title="Mount paths">
      Mount paths are unique to each environment and are used to route traffic to the correct environment. Each mount path must be unique across all environments within a project.
    </Note>
  </Step>

  <Step title="Add environment variables">
    On your environment page, click the "Environment Variables" tab and add the following environment variable:

    * `Variable Key`: ORIGIN
    * `Variable Value`: Your Webflow Cloud domain (for example, `https://your-site-name.webflow.io`)

    Click "Add variable" to save the variable.
  </Step>

  <Step title="Update your project configuration">
    Now, with your locally cloned project, open it in your preferred code editor and update the following files:

    * `astro.config.mjs` to include the base path for your environment and the `assetsPrefix` to match the mount path of your environment.
    * Create a new `.env` file at the root of the project to include the `ORIGIN` environment variable.

    <CodeBlocks>
      ```ts title="astro.config.mjs"
      export default defineConfig({
        base: "/YOUR_MOUNT_PATH",
        build: {
          assetsPrefix: "/YOUR_MOUNT_PATH",
        },

        // Additional configuration options...
      });
      ```

      ```bash title=".env"
      ORIGIN=YOUR_WEBFLOW_CLOUD_DOMAIN
      ```
    </CodeBlocks>
  </Step>
</Steps>

## Add Object Storage binding

Before you can use Object Storage in your Webflow Cloud app, you need to declare a binding in your project's configuration. This binding tells your app how to connect to the storage resource.

Once the binding is declared, your app can use simple methods like `.list()`, `.put()`, and `.delete()` to read from and write to the Object Storage bucket directly in your code.

<Steps>
  <Step title="Declare a binding in `wrangler.json`">
    Open your project's `wrangler.json` file and add an `r2_buckets` array to define your Object Storage buckets with the following information:

    * `binding`: The variable name you'll use to access the bucket in your code. This must be a valid JavaScript variable name.
    * `bucket_name`: The name of the bucket wher you'll store files

    ```json title={"wrangler.json"}
    {
        "r2_buckets": [
           {
              "binding": "CLOUD_FILES",
              "bucket_name": "cloud-files"
           }
        ]
     }
    ```
  </Step>

  <Step title="Generate type definitions for your binding.">
    Update your project's type definitions to enable autocomplete and type safety:

    ```bash
    npx wrangler types
    ```

    This ensures your code editor recognizes the Object Storage binding.
  </Step>

  <Step title="Deploy your app">
    Commit and push any local changes to your remote Github repo to automatically deploy your app.

    <Warning title="CLI deployments will not apply changes to binding configurations">
      To create a new binding, you'll need to commit and push your changes to your linked repository.
    </Warning>
  </Step>

  <Step title="Access your binding in your Environment Dashboard">
    In Webflow, navigate to your site's settings and click on the "Webflow Cloud" tab. Navigate to your project's environment dashboard. Once your project is deployed, you'll see a "Storage" tab appear in the dashboard.

    <Frame>
      <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/38e6be519c147a1dc02afa5b59d2288301a14742a50f1218cb991420e87ad3f6/products/webflow-cloud/pages/concepts/storing-data/assets/storage-cloud-files.png" alt="Upload files to Object Storage bucket" />
    </Frame>

    Click on the "Storage" tab and you'll see your Object Storage binding listed.
  </Step>

  <Step title="Add test files to your bucket">
    Add a couple of test files to your bucket using the Webflow Cloud dashboard. Click on the "Upload" button and select the files you want to upload. Later, you'll create a route to upload files to your bucket.

    <Frame>
      <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/37df4e368cb6fe9f0cd40a920a315ecf76da2701c2df8d10cf8bc0acb63a0c2d/products/webflow-cloud/pages/concepts/storing-data/assets/upload-object.png" alt="Upload files to Object Storage bucket" />
    </Frame>

    You'll see the file appear in your bucket in the dashboard.

    <Accordion title="Uploading files to your local bucket">
      In your local project, you can upload files to a local bucket by running the following command in your terminal:

      ```bash
      npx wrangler r2 object put <YOUR_BUCKET_NAME>/<YOUR_FILE_NAME> --file=<PATH_TO_YOUR_FILE>
      ```

      This will upload the file to your local bucket, which you can then access when developing your project.
    </Accordion>
  </Step>
</Steps>

## List files in your bucket

Get familiar with accessing your Object Storage bucket in your code by creating a new route that lists the files in your bucket. This route will return all files stored in your bucket with their metadata.

<Steps>
  <Step title="Create an API directory">
    In your project's `src/pages` directory, create an `api` directory.
  </Step>

  <Step title="Create a list files route">
    In your `api` directory, create a new file called `list-assets.ts`. This file will contain the logic for listing the files in your bucket.

    <iframe src="https://webflow-cms-api-docs.netlify.app/object-storage/list" allow="clipboard-write" loading="lazy" />
  </Step>
</Steps>

## Serve files from your bucket

Now that you can list files, create a route to serve individual files from your bucket. This route will handle file requests and return the file content with appropriate headers.

<Steps>
  <Step title="Create a file serving route">
    In your `api` directory, create a new file called `asset.ts`. This file will contain the logic for serving individual files from your bucket.

    <iframe src="https://webflow-cms-api-docs.netlify.app/object-storage/asset" allow="clipboard-write" loading="lazy" />
  </Step>

  <Step title="(Optional) View files in your app">
    If you added assets to your [local bucket](#uploading-files-to-your-local-bucket) in your local project, you can view them now.

    To see your app locally, run the following command:

    ```bash
    npm run dev
    ```

    This will start the development server and you can view your app at `http://localhost:4321/YOUR_BASE_PATH`.

    You should see the files you added to your bucket appear in the list of files.

    <div>
      <Frame>
        <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/dfd2bcb44f569f4d412e8d26ad019173cd93e5d5949187b67af26a0d22bf0738/products/webflow-cloud/pages/concepts/storing-data/examples/file-uploader.png" alt="View files in your app" />
      </Frame>
    </div>
  </Step>

  <Step title="Deploy your app">
    To deploy your app to Webflow Cloud, commit and push your changes to your GitHub repository.

    <CodeBlocks>
      ```bash
      git add .
      git commit -m "Add asset endpoints"
      git push
      ```
    </CodeBlocks>

    Go to your environment in Webflow Cloud to see your app deployed. Once deployed, you can access your app at `https://<YOUR_DOMAIN>/<YOUR_BASE_PATH>` and see the files you uploaded via the Webflow Cloud dashboard.

    To upload files from the App, you'll create a new upload route in the next step.
  </Step>
</Steps>

## Upload files to your bucket

Next you'll walk through the route to handle file uploads from your frontend. This route will process form data, validate files, and store them in your bucket. **This approach is best for smaller files less than 1MB.** For larger files, see the multipart upload route in the next section.

<Warning title="File uploads should be executed on the domain of your worker">
  To avoid size upload limits, file upload endpoints should be executed on the domain of your worker using the `ASSETS_PREFIX` environment variable, and not your custom Webflow Cloud domain. Because of this, you'll need to handle CORS requests for this route.
</Warning>

<Steps>
  <Step title="Create an upload route">
    In your `api` directory, step into the file called `upload.ts`. This file will contain the logic for uploading files to your bucket.

    <iframe src="https://webflow-cms-api-docs.netlify.app/object-storage/upload" allow="clipboard-write" loading="lazy" />
  </Step>

  <Step title="Test your upload route">
    The frontend is already set up to use the upload route. You can test it by navigating to the file uploader page and uploading a file in your development environment. You should see the file appear in the list of files.
  </Step>

  <Step title="Deploy your app">
    Deploy your app to Webflow Cloud to start uploading files from the frontend. Commit and push your changes to your GitHub repository to start a deployment.

    ```bash
    git add .
    git commit -m "Add upload endpoints"
    git push
    ```

    Once your app is deployed, navigate to the file uploader page and upload a file. You should see the file appear in the list of files.

    <div>
      <Frame>
        <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/dfd2bcb44f569f4d412e8d26ad019173cd93e5d5949187b67af26a0d22bf0738/products/webflow-cloud/pages/concepts/storing-data/examples/file-uploader.png" alt="Test your upload route" />
      </Frame>
    </div>

    <Note>
      You may see a `413 Content Too Large` error if you attempt to upload large files. For these cases, see the multipart upload route in the next section.
    </Note>
  </Step>
</Steps>

<br />

## Handle large files with multipart uploads

Webflow Cloud apps have a [500MB request body limit](/webflow-cloud/limits) and require requests to complete within 20 seconds. The direct upload approach from the previous section is good for small files. For larger files, use the multipart upload approach shown below.

Multipart uploads break large files into smaller chunks that can be uploaded concurrently, improving upload performance and reliability. This approach allows browsers to upload multiple parts simultaneously and resume interrupted uploads. To achieve this, you'll need to set up logic on both the server and the browser to handle the multipart upload process.

### Create the server endpoints

The **server** handles three main operations:

* **Create** - Initialize upload session and get upload ID from the bucket
* **Upload Parts** - Accept individual file chunks
* **Complete** - Combine all parts into final file and return the file metadata

This guide will cover the creation of the POST and PUT endpoints on the `src/pages/api/multipart-upload.ts` file to handle these operations.

<Steps>
  <Step title="Create the POST endpoint">
    First, review the POST endpoint that handles the creation of a new multipart upload session, as well as the completion once all parts are uploaded.

    <iframe src="https://webflow-cms-api-docs.netlify.app/object-storage/multipart-post" allow="clipboard-write" loading="lazy" />
  </Step>

  <Step title="Create the PUT endpoint">
    Next, observe how the PUT endpoint handles the uploading of individual file parts.

    <iframe src="https://webflow-cms-api-docs.netlify.app/object-storage/multipart-put" allow="clipboard-write" loading="lazy" />
  </Step>
</Steps>

### Create the browser logic

The browser handles the chunking of the file and the uploading of the parts to the server. To do this, the client-side logic will need to:

* **Initiate** - Get an `uploadId` from the server
* **Upload Parts** - Send file chunks with the `uploadId`
* **Complete** - Tell the server to combine all parts

The example repository already implements this logic, however below is a walk through of the code to understand how it works.

<iframe src="https://webflow-cms-api-docs.netlify.app/object-storage/utility-class" allow="clipboard-write" loading="lazy" />

### Test your multipart upload route

Now that your routes are setup, you can test your multipart upload route by uploading a large file.

<Steps>
  <Step title="Start your development server">
    Start your development server by running the following command:

    ```bash
    npm run dev
    ```

    Your server should be running at `http://localhost:4321/YOUR_BASE_PATH`.
  </Step>

  <Step title="Upload a large file">
    Navigate to the file uploader page and upload a large file. You should see the file appear in the list of files.

    <div>
      <Frame>
        <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/dfd2bcb44f569f4d412e8d26ad019173cd93e5d5949187b67af26a0d22bf0738/products/webflow-cloud/pages/concepts/storing-data/examples/file-uploader.png" alt="Test your upload route" />
      </Frame>
    </div>
  </Step>

  <Step title="Deploy your app">
    Deploy your app to Webflow Cloud to start uploading large files. Commit and push your changes to your GitHub repository to start a deployment.

    ```bash
    git add .
    git commit -m "Add multipart upload endpoints"
    git push
    ```
  </Step>

  <Step title="Test your multipart upload route in your Webflow Cloud environment">
    Navigate to the file uploader page in your Webflow Cloud environment and upload a large file. You should see the file appear in the list of files.
  </Step>
</Steps>

## FAQs

<Accordion title="How do I handle CORS requests for the upload route?">
  Since upload requests are made directly to the worker domain (not your Webflow Cloud domain), you need to handle CORS properly. Add these headers to your response:

  ```
  Access-Control-Allow-Origin: <YOUR_WEBFLOW_CLOUD_DOMAIN>
  Access-Control-Allow-Methods: POST, PUT, DELETE, OPTIONS
  Access-Control-Allow-Headers: Content-Type
  ```

  If you're looking to upload files from an authenticated user with session credentials, you'll need to generate temporary upload URLs with embedded authentication tokens. Since CORS prevents passing session cookies directly, you can create a secure token that contains user information and embed it in the upload URL.

  This approach involves:

  * Generating a temporary upload URL with an embedded authentication token
  * Validating the token on the upload endpoint
  * Using the worker domain for the actual file upload
</Accordion>

<Accordion title="What's the difference between the `BASE_URL` and `ASSETS_PREFIX` environment variables?">
  Both the `BASE_URL` and `ASSETS_PREFIX` environment variables are automatically set by Webflow Cloud to help with routing logic in your app. You can access these variables as you would any other environment variable in your app.

  * `BASE_URL` is automatically set to the [mount path](/webflow-cloud/environments#mount-paths) of your environment (for example, `/app`). This is useful for setting up redirects and other routing logic in your app.
  * `ASSETS_PREFIX` is set to the domain of the Worker your app is deployed to (for example, `https://YOUR_ENV_HASH.wf-app-prod.cosmic.webflow.services`). This link is essential for uploading large files to your bucket, and serving files directly from your app. Because this link will always be a different domain than your app's domain, you'll need to handle CORS requests for the upload route.

  Learn more about [built in environment variables in Webflow Cloud](/webflow-cloud/environment/configuration#mount-path-configuration).
</Accordion>

<Accordion title="Can I create presigned URLs to upload directly to my bucket?">
  No, presigned URLs require credentials that aren't available in Webflow Cloud's secure environment. Instead, use the multipart upload endpoints to upload files through your app's API routes.
</Accordion>

<Accordion title="Can I expose a public bucket to the web?">
  No, public buckets aren't supported in Webflow Cloud. All bucket access must go through your app's API routes, which gives you control over access permissions and allows you to implement proper authentication and authorization.
</Accordion>

<Accordion title="Why do I get a 413 Content Too Large error when uploading to my bucket?">
  Likely the file being uploaded is hitting current Webflow Cloud request limits. You should upload these larger files through the multipart upload strategy.
</Accordion>
