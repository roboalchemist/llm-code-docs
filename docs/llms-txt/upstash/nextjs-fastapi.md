# Source: https://upstash.com/docs/workflow/quickstarts/nextjs-fastapi.md

# Next.js & FastAPI

<Card title="GitHub Repository" icon="github" href="https://github.com/upstash/workflow-py/tree/master/examples/nextjs-fastapi" horizontal>
  You can find the project source code on GitHub.
</Card>

This guide provides detailed, step-by-step instructions on how to use and deploy Upstash Workflow with Next.js & FastAPI. You can also explore [the source code](https://github.com/upstash/workflow-py/tree/master/examples/nextjs-fastapi) for a detailed, end-to-end example and best practices.

## Prerequisites

1. An Upstash QStash API key.
2. Node.js and npm (or another package manager) installed.
3. Python and pip installed.

If you haven't obtained your QStash API key yet, you can do so by [signing up](https://console.upstash.com/login) for an Upstash account and navigating to your QStash dashboard.

## Step 1: Setup

Clone the [Next.js & FastAPI example](https://github.com/upstash/workflow-py/tree/master/examples/nextjs-fastapi):

```bash  theme={"system"}
git clone https://github.com/upstash/workflow-py.git
cd workflow-py/examples/nextjs-fastapi
```

## Step 2: Installation

Create a virtual environment and activate it:

```bash Terminal theme={"system"}
python -m venv venv
source venv/bin/activate
```

Install the dependencies:

```bash  theme={"system"}
npm install
```

## Step 3: Configure Environment Variables

Create a `.env` file in your project root and add your QStash token. This token is used to authenticate your application with the QStash service.

```bash Terminal theme={"system"}
touch .env
```

Upstash Workflow is powered by [QStash](/qstash/overall/getstarted), which requires access to your endpoint to execute workflows. When your app is deployed, QStash will use the app's URL. However, for local development, you have two main options: [use a local QStash server or set up a local tunnel](/workflow/howto/local-development).

### Option 1: Local QStash Server

To start the local QStash server, run:

```bash  theme={"system"}
npx @upstash/qstash-cli dev
```

Once the command runs successfully, you’ll see `QSTASH_URL` and `QSTASH_TOKEN` values in the console. Add these values to your `.env` file:

```bash .env theme={"system"}
export QSTASH_URL="http://127.0.0.1:8080"
export QSTASH_TOKEN="<QSTASH_TOKEN>"
```

This approach allows you to test workflows locally without affecting your billing. However, runs won't be logged in the Upstash Console.

### Option 2: Local Tunnel

Alternatively, you can set up a local tunnel. For this option:

1. Copy the `QSTASH_TOKEN` from the Upstash Console.
2. Update your `.env` file with the following:

```bash .env theme={"system"}
export QSTASH_TOKEN="***"
export UPSTASH_WORKFLOW_URL="<UPSTASH_WORKFLOW_URL>"
```

* Replace `***` with your actual QStash token.
* Set `UPSTASH_WORKFLOW_URL` to the public URL provided by your local tunnel.

Here’s where you can find your QStash token:

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_token.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=df12ba48119bcdd13a675e53b43ab74d" data-og-width="1211" width="1211" data-og-height="833" height="833" data-path="img/qstash-workflow/qstash_token.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_token.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=c251f0eeb0a6973ff498f9e9930aed70 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_token.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=d452c08e1a638dff258d938aa8544f25 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_token.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=6b197538fe5190c7936b751ec228ef39 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_token.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=63da8b3df03c88ff0a7700af7a5db6fb 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_token.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=8df98665037cf63deb6b48d5c22d3f6b 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_token.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=b3ef0ab4137bdec59b7cb772550933e1 2500w" />
</Frame>

Using a local tunnel connects your endpoint to the production QStash, enabling you to view workflow logs in the Upstash Console.

## Step 4: Start the Development Server

Upstash Workflow is powered by [QStash](/qstash/overall/getstarted), and QStash needs a publicly accessible URL to run your workflows. Here's how to [set up your workflow endpoint for local development](/workflow/howto/local-development).

In a nutshell, in local development, you can either use the QStash development server or use a local tunnel to make your workflow endpoint publicly accessible.

Don't forget to source your environment file to set your environment variables:

```bash Terminal theme={"system"}
source .env
```

After defining the endpoint, you can trigger your workflow by starting your app:

```bash Terminal theme={"system"}
npm run dev
```

Navigate to [http://localhost:3000](http://localhost:3000) to see your Next.js app in action.
FastAPI will be running on [http://localhost:8000](http://localhost:8000).

<Frame>
  <img src="https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/quickstarts/nextjs-fastapi/workflow-nextjs-fastapi.png?fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=b7edc924355a9e8bf65e098796250bf6" data-og-width="2880" width="2880" data-og-height="1554" height="1554" data-path="img/workflow/quickstarts/nextjs-fastapi/workflow-nextjs-fastapi.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/quickstarts/nextjs-fastapi/workflow-nextjs-fastapi.png?w=280&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=7cc6dda64c2c28ece85b1e7e97a45a1d 280w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/quickstarts/nextjs-fastapi/workflow-nextjs-fastapi.png?w=560&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=c7663bd8f2b05fa4cb2cf6fbfa98e010 560w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/quickstarts/nextjs-fastapi/workflow-nextjs-fastapi.png?w=840&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=a8c125c57f05efd9e7c602232abdd14b 840w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/quickstarts/nextjs-fastapi/workflow-nextjs-fastapi.png?w=1100&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=59b255e6e39b9b38b4d1566c4dcf5ece 1100w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/quickstarts/nextjs-fastapi/workflow-nextjs-fastapi.png?w=1650&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=96845f903d22b7dbece95b9105a46522 1650w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/quickstarts/nextjs-fastapi/workflow-nextjs-fastapi.png?w=2500&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=251e147ef824ddd40aa28dcef3e5ed15 2500w" />
</Frame>

## Step 5: Deploying the Project at Vercel

To deploy the project at vercel and try the endpoints, you should start with setting up the project by running:

```bash Terminal theme={"system"}
vercel
```

Next, you shoud go to vercel.com, find your project and add `QSTASH_TOKEN`, to the project as environment variables. You can find this env variables from the [Upstash Console](https://console.upstash.com/qstash). To learn more about other env variables and their use in the context of Upstash Workflow, you can read [the Secure your Endpoint in our documentation](/workflow/howto/security#using-qstashs-built-in-request-verification-recommended).

Once you add the env variables, you can deploy the project with:

```bash Terminal theme={"system"}
vercel --prod
```

Note that the project won't work in preview. It should be deployed to production like above. This is because preview requires authentication.

Once you have the app deployed, you can go to the deployment and call the endpoints using the form on the page.

You can observe the logs at [Upstash console under the Worfklow tab](https://console.upstash.com/qstash?tab=workflow) or vercel.com to see your workflow operate.

## Next Steps

1. Learn how to protect your workflow endpoint from unauthorized access by [securing your workflow endpoint](/workflow/howto/security).

2. Explore \[the source code]\([https://github.com/upstash/workflow-js/tree/main/examples/nextjs-fastapi](https://github.com/upstash/workflow-js/tree/main/examples/nextjs-fastapi) for a detailed, end-to-end example and best practices.

3. For setting up and testing your workflows in a local environment, check out our [local development guide](/workflow/howto/local-development).
