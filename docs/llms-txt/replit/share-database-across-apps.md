# Source: https://docs.replit.com/tutorials/share-database-across-apps.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.replit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Share a database across multiple apps

> Learn how to expose your Replit database as a REST API to share data securely across multiple apps and external services.

export const AiPrompt = ({children}) => {
  return <CodeBlock className="relative block font-sans whitespace-pre-wrap break-words">
      <div className="pr-7">
        {children}
      </div>
    </CodeBlock>;
};

Share your database across multiple apps by exposing it as a REST API. This lets other apps securely read and write your data through HTTP requests while keeping everything in one place.

## Add an API to your existing app

Ask **Agent** to create a REST API for your database. Agent will set up endpoints, add authentication, and protect your data.

<Steps>
  <Step title="Open your app">
    Open the app that contains the database you want to share.
  </Step>

  <Step title="Ask Agent to create the API">
    <AiPrompt>
      Expose my database as a REST API secured with an API key. Create endpoints for all CRUD operations on my existing tables. Use Drizzle ORM for safe database queries. Store the API key in Secrets as API\_KEY.
    </AiPrompt>

    Agent will set up everything you need automatically.
  </Step>

  <Step title="Add your API key">
    1. Open the **Secrets** tab
    2. Add a secret: `API_KEY` with a secure password
    3. This key protects your database from unauthorized access
  </Step>

  <Step title="Publish your app">
    1. Select **Run** to test your API
    2. Select **Publish** > **Autoscale** to get a public URL
    3. Your database is now accessible to other apps
  </Step>
</Steps>

## Example: Database API template

See a working example with the [Database API Example template](https://replit.com/@matt/Replit-Database-API-Example?utm_source=replit\&utm_medium=docs\&utm_campaign=database-helium). Fork it to start a new database API from scratch, or explore the code to understand how it works.

The template includes:

* Automatic database setup with sample data
* API endpoints for all CRUD operations
* API key authentication
* Drizzle ORM for safe queries

<Steps>
  <Step title="Fork the template">
    Open the [Database API Example template](https://replit.com/@matt/Replit-Database-API-Example?utm_source=replit\&utm_medium=docs\&utm_campaign=database-helium) and fork it.
  </Step>

  <Step title="Add an API key">
    1. Open the **Secrets** tab
    2. Add `API_KEY` with a secure password
  </Step>

  <Step title="Run and publish">
    1. Select **Run** to start the API
    2. Select **Publish** > **Autoscale** when ready
  </Step>
</Steps>

## Connect from other apps

Ask **Agent** to write the connection code in any of your other apps:

<AiPrompt>
  Create a backend endpoint that connects to my database API at https\://\[YOUR-APP].replit.app. Use the API key from secrets (API\_KEY) on the server side. Create routes to fetch and display data from the API.
</AiPrompt>

Be sure to replace \[YOUR-APP] with your app's name. Agent will handle authentication and error handling automatically, keeping your API key secure on the server.

### API endpoints reference

Your database uses standard REST endpoints. For an `items` table:

| Action   | Method | Endpoint         |
| -------- | ------ | ---------------- |
| List all | GET    | `/api/items`     |
| Get one  | GET    | `/api/items/:id` |
| Create   | POST   | `/api/items`     |
| Update   | PUT    | `/api/items/:id` |
| Delete   | DELETE | `/api/items/:id` |

All requests need an `X-API-KEY` header with your API key.

### Write your own connection code

If you prefer to code the connection yourself, use these backend examples:

<CodeGroup>
  ```javascript Node.js (Backend) theme={null}
  const API_URL = 'https://your-app.replit.app';
  const API_KEY = process.env.API_KEY;

  const response = await fetch(`${API_URL}/api/items`, {
    headers: { 'X-API-KEY': API_KEY }
  });
  const items = await response.json();
  ```

  ```python Python (Backend) theme={null}
  import os
  import requests

  API_URL = 'https://your-app.replit.app'
  API_KEY = os.environ['API_KEY']

  response = requests.get(
      f'{API_URL}/api/items',
      headers={'X-API-KEY': API_KEY}
  )
  items = response.json()
  ```
</CodeGroup>

<Warning>
  These examples are for **backend code only**. Never use API keys in frontend/browser code - they will be exposed to anyone viewing your page source. For frontend apps, create a backend endpoint that proxies requests to your database API.

  Always store your API key in **Secrets**, not in your code.
</Warning>

## Add more tables

Extend your database as your app grows:

<AiPrompt>
  Add a users table with email, name, and role columns. Create API endpoints for users with the same authentication as the existing endpoints.
</AiPrompt>

Agent will update your schema, create endpoints, and apply authentication automatically.

## How it works

Your API acts as a central hub. When an app needs data, it sends a request to your API. The API checks the API key, then reads or writes to your database. Multiple apps share one database securely.

## Security

Your API includes built-in protection:

* **API key authentication**: Only apps with the correct key can access your database
* **SQL injection protection**: Drizzle ORM prevents malicious queries
* **Data validation**: The API checks all data before saving

<Warning>
  Store your API key in **Secrets**, never in code.
</Warning>

Only share your API key with apps you trust.

## Troubleshooting

<AccordionGroup>
  <Accordion title="Can't connect from another app">
    * Publish your database API app (not just run it)
    * Use your published URL ending in `.replit.app`
    * Verify both apps have the same API key in Secrets
    * Check the secret is named `API_KEY` in both apps
  </Accordion>

  <Accordion title="Authentication errors">
    * Store the API key in **Secrets**, not in code
    * Verify the API key matches in both apps
    * Check the secret is named `API_KEY` (all caps)
  </Accordion>

  <Accordion title="Need help">
    Ask **Agent** to troubleshoot:

    <AiPrompt>
      I'm trying to connect to my database API but getting errors. Can you help me debug the connection?
    </AiPrompt>
  </Accordion>
</AccordionGroup>

## Next steps

* [Database](/cloud-services/storage-and-databases/sql-database) - Create and manage databases
* [Connect to a database](/getting-started/quickstarts/database-connection) - Learn connection methods
* [Production databases](/cloud-services/storage-and-databases/production-databases) - Set up production databases
