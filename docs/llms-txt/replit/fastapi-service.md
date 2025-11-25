# Source: https://docs.replit.com/getting-started/quickstarts/fastapi-service.md

# Create a FastAPI service

> Build and publish a high-performance API using FastAPI on Replit. Learn how to use autoscaling for reliable API hosting.

Learn how to create a modern API service using FastAPI's powerful features. This guide shows you how to publish a Python-based API with automatic scaling.

## What you'll learn

<CardGroup cols={2}>
  <Card title="FastAPI" icon="bolt">
    Build modern Python APIs
  </Card>

  <Card title="Autoscaling" icon="arrows-up-down">
    Publish with automatic scaling
  </Card>

  <Card title="Performance" icon="gauge-high">
    Create high-performance endpoints
  </Card>

  <Card title="Documentation" icon="book">
    Auto-generate API docs
  </Card>
</CardGroup>

## Create your API

<Steps>
  <Step title="Fork the template">
    Sign in to Replit and fork the [FastAPI template](https://replit.com/@replit/FastAPI?v=1#main.py). Select **+ Use Template** and follow the prompts to create your Replit App.

    <Tip>
      FastAPI automatically generates interactive API documentation at `/docs`.
    </Tip>
  </Step>

  <Step title="Set up publishing">
    1. Select **Publish** in the workspace header
    2. Choose **Autoscale** deployment
    3. Configure your API:
       * Machine: 1vCPU, 2 GiB RAM (default)
       * Max machines: 3 (default)
       * Run command: `uvicorn main:app --host 0.0.0.0`

    <Note>
      Autoscale deployments automatically adjust resources based on API traffic.
    </Note>
  </Step>

  <Step title="Launch">
    Select **Publish** to launch your API. It will be live in a few minutes!
  </Step>
</Steps>

## Customization options

<CardGroup cols={2}>
  <Card title="Endpoints">
    * Add new routes
    * Implement validation
    * Handle authentication
  </Card>

  <Card title="Documentation">
    * Customize API docs
    * Add examples
    * Define schemas
  </Card>
</CardGroup>

## Next steps

<CardGroup cols={3}>
  <Card title="Custom Domain" icon="globe" href="/cloud-services/deployments/custom-domains">
    Add your own domain
  </Card>

  <Card title="Databases" icon="database" href="/cloud-services/storage-and-databases/sql-database/">
    Add data persistent storage
  </Card>

  <Card title="Monitoring" icon="chart-line" href="/category/replit-deployments">
    Track performance
  </Card>
</CardGroup>

## Related guides

<CardGroup cols={2}>
  <Card title="Create a Flask app" icon="flask" href="/getting-started/quickstarts/flask-app">
    Build with Flask
  </Card>

  <Card title="Build with AI" icon="wand-magic-sparkles" href="/getting-started/quickstarts/build-with-ai">
    Create apps using Agent
  </Card>
</CardGroup>

<Note>
  Want to learn more about API development? Check out our [publishing documentation](/category/replit-deployments).
</Note>
