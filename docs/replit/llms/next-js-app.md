# Source: https://docs.replit.com/getting-started/quickstarts/next-js-app.md

# Create a Next.js app

> Build and publish a modern React application using Next.js on Replit. Learn how to use server-side rendering and static generation.

Learn how to create a Next.js application with server-side rendering capabilities. This guide shows you how to publish a React app using Replit's autoscaling published apps.

## What you'll learn

<CardGroup cols={2}>
  <Card title="Next.js" icon="react">
    Build modern React applications
  </Card>

  <Card title="Server-Side Rendering" icon="server">
    Enable SSR for better performance
  </Card>

  <Card title="Autoscaling" icon="arrows-up-down">
    Publish with automatic scaling
  </Card>

  <Card title="Performance" icon="gauge-high">
    Optimize for production
  </Card>
</CardGroup>

## Create your app

<Steps>
  <Step title="Fork the template">
    Sign in to Replit and fork the [Next.js template](https://replit.com/@replit/Nextjs?v=1#README). Select **+ Use Template** and follow the prompts to create your Replit App.
  </Step>

  <Step title="Set up publishing">
    1. Select **Publish** in the workspace header
    2. Choose **Autoscale** deployment
    3. Configure your app:
       * Machine: 1vCPU, 2 GiB RAM (default)
       * Max machines: 3 (default)
       * Build command: `npm run build`
       * Run command: `npm run start`

    <Note>
      Autoscale deployments automatically adjust resources based on traffic.
    </Note>
  </Step>

  <Step title="Launch">
    Select **Publish** to launch your app. It will be live in a few minutes!
  </Step>
</Steps>

## Next steps

<CardGroup cols={3}>
  <Card title="Custom Domain" icon="globe" href="/cloud-services/deployments/custom-domains">
    Add your own domain
  </Card>

  <Card title="Autoscaling" icon="server" href="/cloud-services/deployments/autoscale-deployments">
    Learn about scaling
  </Card>

  <Card title="Performance" icon="gauge-high" href="/category/replit-deployments">
    Optimize your app
  </Card>
</CardGroup>

## Related guides

<CardGroup cols={2}>
  <Card title="Create a static blog" icon="newspaper" href="/getting-started/quickstarts/static-blog-astro">
    Build a blog with Astro
  </Card>

  <Card title="Build with AI" icon="wand-magic-sparkles" href="/getting-started/quickstarts/build-with-ai">
    Create apps using Agent
  </Card>
</CardGroup>

<Note>
  Want to learn more about web development? Check out our [publishing documentation](/category/replit-deployments).
</Note>
