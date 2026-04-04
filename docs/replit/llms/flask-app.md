# Source: https://docs.replit.com/getting-started/quickstarts/flask-app.md

# Create a Flask app

> Build and publish a web application using Flask on Replit. Learn how to use autoscaling for reliable web hosting.

Learn how to create a web application using Flask's simple yet powerful framework. This guide shows you how to publish a Python web app with automatic scaling.

## What you'll learn

<CardGroup cols={2}>
  <Card title="Flask" icon="flask">
    Build Python web apps
  </Card>

  <Card title="Autoscaling" icon="arrows-up-down">
    Publish with automatic scaling
  </Card>

  <Card title="Web Development" icon="browser">
    Create dynamic web pages
  </Card>

  <Card title="Deployment" icon="cloud">
    Host your application
  </Card>
</CardGroup>

## Create your app

<Steps>
  <Step title="Fork the template">
    V{/* vale off */}

    Sign in to Replit and fork the [Flask template](https://replit.com/@replit/Flask?v=1#main.py). Select **+ Use Template** and follow the prompts to create your Replit App.

    <Tip>
      Flask's development server automatically reloads when you make changes to your code.
    </Tip>
  </Step>

  <Step title="Set up publishing">
    1. Select **Publish** in the workspace header
    2. Choose **Autoscale** deployment
    3. Configure your app:
       * Machine: 1vCPU, 2 GiB RAM (default)
       * Max machines: 3 (default)
       * Run command: `python3 main.py`

    <Note>
      Autoscale deployments automatically adjust resources based on website traffic.
    </Note>
  </Step>

  <Step title="Launch">
    Select **Publish** to launch your website. It will be live in a few minutes!
  </Step>
</Steps>

## Customization options

<CardGroup cols={2}>
  <Card title="Routes">
    * Add new pages
    * Handle form submissions
    * Create API endpoints
  </Card>

  <Card title="Templates">
    * Design page layouts
    * Add dynamic content
    * Style your pages
  </Card>
</CardGroup>

## Next steps

<CardGroup cols={3}>
  <Card title="Databases" icon="database" href="/cloud-services/storage-and-databases/sql-database/">
    Add data persistence
  </Card>

  <Card title="Custom Domain" icon="globe" href="/cloud-services/deployments/custom-domains">
    Add your own domain
  </Card>
</CardGroup>

## Related guides

<CardGroup cols={2}>
  <Card title="Create a FastAPI service" icon="bolt" href="/getting-started/quickstarts/fastapi-service">
    Build with FastAPI
  </Card>

  <Card title="Build with AI" icon="wand-magic-sparkles" href="/getting-started/quickstarts/build-with-ai">
    Create apps using Agent
  </Card>
</CardGroup>

<Note>
  Want to learn more about web development? Check out our [publishing documentation](/category/replit-deployments).
</Note>
