# Source: https://docs.replit.com/extensions/development/full-stack.md

# Full-Stack

> Learn how to build a full-stack extension by creating a separate backend API server to handle requests from your extension client on Replit.

# Create a full-stack Extension

While full-stack extensions are not supported within a single Replit App (aka a monorepo) at this time, you can always call out from your Extension client Replit App to any outside API endpoints.

Until we have full Deployments support, you can use this simple workaround to create your own server API for your extension:

1. [Create your Extension Client Replit App →](https://replit.com/new/extension)
2. [Create a separate Replit App](https://replit.com/new) for your backend. This should expose an API. For example it could be a [Node](https://replit.com/new/nodejs) or [Ruby](https://replit.com/new/ruby) API server, or even a [Next.js](https://replit.com/new?template=482b2b7d-6b3e-4b9d-863c-d51c1d5cf6f0) site with a serverless function.
3. Make fetch requests from your extension client to your backend\
   <Tip>Make sure to enable CORS requests on your extension backend API, since the extension client and API will run on different subdomains</Tip>

If you’re using Next.js to build your extension, we recommend [exporting it statically](https://nextjs.org/pages/building-your-application/deploying/static-exports) and pointing your releases to the build directory.
