# Source: https://docs.exa.ai/websets/dashboard/get-started.md

# Source: https://docs.exa.ai/websets/api/get-started.md

# Source: https://docs.exa.ai/websets/dashboard/get-started.md

# Source: https://docs.exa.ai/websets/api/get-started.md

# Source: https://docs.exa.ai/websets/dashboard/get-started.md

# Source: https://docs.exa.ai/websets/api/get-started.md

# Source: https://docs.exa.ai/websets/dashboard/get-started.md

# Source: https://docs.exa.ai/websets/api/get-started.md

# Get started

> Create your first Webset

## Create and setup your API key

1. Go to the [Exa Dashboard](https://dashboard.exa.ai)
2. Click on "API Keys" in the left sidebar
3. Click "Create API Key"
4. Give your key a name and click "Create"
5. Copy your API key and store it securely - you won't be able to see it again!

<Card title="Get your Exa API key" icon="key" horizontal href="https://dashboard.exa.ai/api-keys" />

<br />

## Create a .env file

Create a file called `.env` in the root of your project and add the following line.

```bash  theme={null}
EXA_API_KEY=your api key without quotes
```

<br />

## Make an API request

Use our Python or JavaScript SDKs, or call the API directly with cURL.

<Tabs>
  <Tab title="Python">
    Install the latest version of the python SDK with pip. If you want to store your API key in a `.env` file, make sure to install the dotenv library.

    ```bash  theme={null}
    pip install exa-py
    pip install python-dotenv
    ```

    Create a file called `webset.py` and add the code below:

    ```python python theme={null}
    from exa_py import Exa
    from dotenv import load_dotenv
    from exa_py.websets.types import CreateWebsetParameters, CreateEnrichmentParameters

    import os

    load_dotenv()
    exa = Exa(os.getenv('EXA_API_KEY'))

    # Create a Webset with search and enrichments
    webset = exa.websets.create(
        params=CreateWebsetParameters(
            search={
                "query": "Top AI research labs focusing on large language models",
                "count": 5
            },
            enrichments=[
                CreateEnrichmentParameters(
                    description="LinkedIn profile of VP of Engineering or related role",
                    format="text",
                ),
            ],
        )
    )

    print(f"Webset created with ID: {webset.id}")

    # Wait until Webset completes processing
    webset = exa.websets.wait_until_idle(webset.id)

    # Retrieve Webset Items
    items = exa.websets.items.list(webset_id=webset.id)
    for item in items.data:
        print(f"Item: {item.model_dump_json(indent=2)}")
    ```
  </Tab>

  <Tab title="JavaScript">
    Install the latest version of the JavaScript SDK with npm or pnpm:

    ```bash  theme={null}
    npm install exa-js
    ```

    Create a file called `webset.js` and add the code below:

    ```javascript javascript theme={null}
    import * as dotenv from "dotenv";
    import Exa, { CreateWebsetParameters, CreateEnrichmentParameters } from "exa-js";

    // Load environment variables
    dotenv.config();

    async function main() {
      const exa = new Exa(process.env.EXA_API_KEY);

      try {
        // Create a Webset with search and enrichments
        const webset = await exa.websets.create({
          search: {
            query: "Top AI research labs focusing on large language models",
            count: 10
          },
          enrichments: [
            {
              description: "Estimate the company'\''s founding year",
              format: "number"
            }
          ],
        });

        console.log(`Webset created with ID: ${webset.id}`);

        // Wait until Webset completes processing
        const idleWebset = await exa.websets.waitUntilIdle(webset.id, {
          timeout: 60000,
          pollInterval: 2000,
          onPoll: (status) => console.log(`Current status: ${status}...`)
        });

        // Retrieve Webset Items
        const items = await exa.websets.items.list(webset.id, { limit: 10 });
        for (const item of items.data) {
          console.log(`Item: ${JSON.stringify(item, null, 2)}`);
        }
      } catch (error) {
        console.error("Error:", error);
      }
    }

    main();
    ```
  </Tab>

  <Tab title="cURL">
    Pass the following command to your terminal to create a Webset:

    ```bash bash theme={null}
    curl --request POST \
      --url https://api.exa.ai/websets/v0/websets/ \
      --header 'accept: application/json' \
      --header 'content-type: application/json' \
      --header "x-api-key: ${EXA_API_KEY}" \
      --data '{
        "search": {
          "query": "Top AI research labs focusing on large language models",
          "count": 5
        },
        "enrichments": [
          {
            "description": "Find the company'\''s founding year",
            "format": "number"
          }
        ]
      }'
    ```

    To check the status of your Webset:

    ```bash bash theme={null}
    curl --request GET \
      --url https://api.exa.ai/websets/v0/websets/{WEBSET_ID} \
      --header 'accept: application/json' \
      --header "x-api-key: ${EXA_API_KEY}"
    ```

    To list items in your Webset:

    ```bash bash theme={null}
    curl --request GET \
      --url https://api.exa.ai/websets/v0/websets/{WEBSET_ID}/items \
      --header 'accept: application/json' \
      --header "x-api-key: ${EXA_API_KEY}"
    ```

    Or you can use the `expand` parameter to get the latest 100 within your Webset:

    ```bash bash theme={null}
    curl --request GET \
      --url https://api.exa.ai/websets/v0/websets/{WEBSET_ID}?expand=items \
      --header 'accept: application/json' \
      --header "x-api-key: ${EXA_API_KEY}"
    ```
  </Tab>
</Tabs>

***

## What's next?

* Learn [how Websets work](/websets/api/how-it-works) and understand the event-driven process
* Configure [Monitors](/websets/api/monitors/create-a-monitor) to automatically receive continuous updates for your Websets
* Configure [webhooks](/websets/api/webhooks) to receive real-time updates as items are added into your Websets
* Learn about [Enrichments](/websets/api/websets/enrichments) to extract specific data points
* See how to [Manage Items](/websets/api/websets/items) in your Webset


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt