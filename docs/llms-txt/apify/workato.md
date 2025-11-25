# Source: https://docs.apify.com/platform/integrations/workato.md

# Workato integration

**Learn how to integrate your Apify Actors with Workato for automated workflows.**

***

https://www.workato.com/ is an automation platform where you can build recipes, automated workflows that connect your apps with no-code connectors. With the https://apify.com, you can run *Apify Actors* inside your recipes to launch web scraping and automation jobs, watch for run events, and further work with the results.

## Get started

To use the Apify integration with Workato, you will need:

* An https://console.apify.com/
* A https://www.workato.com/

## Install the Apify Connector

The Apify Workato Connector is available in the Workato Community library. Here's how to install it:

1. In your Workato workspace, navigate to **Community library**.
2. Click on **Custom connectors**.
3. Search for **Apify**.
4. Click on the connector and then click **Install**.

After installation, the Apify connector appears in **Connector SDK** under the **Tools** tab. After you release the connector, you can use it in your projects.

## Connect your Apify account

Before using the Apify connector in recipes, create a connection inside a Workato project.

### Create a project (if you don’t have one)

1. In Workato, go to **Workspace > Projects**.
2. Click **Create project**.
3. Choose either **Start from scratch** or **Build a workflow app**.
4. Name and create the project.

![Screenshot showing how to create a new project in Workato](/assets/images/create-project-9f04024de8d091a9b5e6f7a3f1be40cd.png)

### Create a connection in your project

1. Open your project.
2. Click the **Create** button.
3. Select **Connection**.
4. Search for **Apify** and choose the Apify connector.

![Screenshot showing how to search for the Apify connector in Workato](/assets/images/create-connection-find-connector-6f3486110e4b61af68b1eb5fb8481783.png)

![Screenshot of the connection selection interface in Workato](/assets/images/connection-selection-4cf599a24c6d9ae547cc100d08bfa1b4.png)

### Choose authentication type

You can authenticate the connection using either:

* **Apify API token**
* **Sign in with Apify** (OAuth 2.0)

#### Authenticate with API token

1. In the Apify connection dialog, select **Apify API token** as the authentication type.
2. Enter your **API Token**. In Apify Console, go to https://console.apify.com/account#/integrations and copy your API token.
3. Click **Connect**. Workato will test the connection by making an authenticated call to verify your credentials.

![Screenshot of the Workato API Key authentication form](/assets/images/create-connection-api-key-b6a8df7af65192d1eaae4ebbc67949ba.png) ![Screenshot showing successful API Key authentication in Workato](/assets/images/create-connection-api-success-6af3b796f545f349b9318aa5789ed137.png)

#### Authenticate with OAuth 2.0

1. In the Apify connection dialog, select **Sign in with Apify** as the authentication type.
2. Click **Connect** to start the OAuth flow.
3. Sign in to Apify and authorize Workato to access your account.
4. After authorizing, you'll be redirected back to Workato and the connection will be established.

![Screenshot of the Workato OAuth 2.0 authentication interface](/assets/images/create-connection-oauth-992e254d053bb0b8d6e3030c70fa5fe9.png) ![Screenshot showing successful OAuth authentication in Workato](/assets/images/create-connection-oauth-success-9f9fe10e9acaa04b889a492ea013325b.png)

Once the connection is created and authenticated, you can use it in any recipe.

## Create your first recipe

After connecting your Apify account, you can start creating recipes that use Apify triggers and actions. A recipe begins with a trigger (an event that starts the workflow) and includes one or more actions (operations to perform).

### Selection and input methods

*The Apify connector provides dynamic dropdown lists (pick lists) and flexible input methods to make configuration easier.*

### Pick lists and selection methods

* **Selection method (pick list vs. manual ID):** Choose from fetched lists or switch to manual and paste an ID. If an item doesn't appear, make sure it exists in your account and has been used at least once, or paste its ID manually.

* Available pick lists:

  <!-- -->

  * **Actors**: Lists your recently used Actors or Apify Store Actors, displaying the title and username/name
  * **Tasks**: Lists your saved tasks, displaying the task title and Actor name
  * **Datasets**: Lists available datasets, sorted by most recent first
  * **Key-value stores**: Lists available stores, sorted by most recent first
  * **Store Keys**: Dynamically shows keys available in the selected store

### Input types

* **Input type (schema‑based vs. JSON):** For Actor inputs, when you choose an Actor from the pick list, the connector fetches the input schema and renders dynamic fields based on the Actor's configuration. If schema fetching fails or you switch to manual input, a JSON input field appears where you can paste valid JSON instead. For Task inputs, you can optionally provide an override input as JSON to modify the task's pre-configured settings.

Copy the Actor/Task input JSON

Open the Actor or Task Input page in Apify Console, switch format to JSON, and copy the canonical structure: `https://console.apify.com/actors/<actor_id>/input` `https://console.apify.com/actors/tasks/<task_id>/input`

![Screenshot showing different input modes available in the Workato connector](/assets/images/input-modes-9741ef78bec9609201234b4541626b57.png)

#### Where to find your IDs

When using manual input instead of pick lists, you'll need to provide the correct resource IDs. Here's how to find them in Apify Console:

* **Actor ID**: https://console.apify.com/actors > API panel or URL.

  <!-- -->

  * Example URL: `https://console.apify.com/actors/<actorId>`
  * Actor name format: owner\~name (for example, `apify~website-scraper`)

* **Task ID**: https://console.apify.com/actors/tasks > API panel or URL.
  <!-- -->
  * Example URL: `https://console.apify.com/actors/tasks/<taskId>`

* **Dataset ID**: https://console.apify.com/storage/datasets > Dataset detail > API panel or URL.

  <!-- -->

  * Example URL: `https://console.apify.com/storage/datasets/<datasetId>`
  * Also available in the table on the `Storage > Datasets` page

* **Key-value store ID**: https://console.apify.com/storage/Key-value-stores > Store detail > API panel or URL.

  <!-- -->

  * Example URL: `https://console.apify.com/storage/Key-value-stores/<storeId>`
  * Also available in the table on the `Storage > Key-value stores` page

* **Webhook ID**: https://console.apify.com/actors > Actor > Integrations.
  <!-- -->
  * Example URL: `https://console.apify.com/actors/<actor_id>/integrations/<webhook_id>`

## Triggers

Inline documentation

Each connector trigger and action field in Workato includes inline help text describing the parameter and expected format.

The Apify connector provides the following triggers that monitor your Apify account for task completions:

### Actor Run Finished

*Triggers when an Apify Actor run finishes (succeeds, fails, times out, or gets aborted).*

This trigger monitors a specific Apify Actor and starts the recipe when any run of that Actor reaches a terminal status. You can:

* Select the Actor from recently used Actors or Apify store Actors
* Choose to trigger on specific statuses (`ACTOR.RUN.SUCCEEDED`, `ACTOR.RUN.FAILED`, `ACTOR.RUN.TIMED_OUT`, `ACTOR.RUN.ABORTED`)
* Access run details, status, and metadata in subsequent recipe steps

![Screenshot of the Actor Run Finished trigger configuration in Workato](/assets/images/trigger-actor-89021d81a515333cf895dcfa618b77c4.png)

### Task Run Finished

*Triggers when an Apify Task run finishes (succeeds, fails, times out, or gets aborted).*

This trigger creates a webhook in your Apify account that will notify Workato when the selected Task run finishes with the specified statuses. This trigger watches a specific saved task (an Actor with preset inputs) and fires when that task's run completes with any terminal status. You can choose specific statuses to monitor (`ACTOR.RUN.SUCCEEDED`, `ACTOR.RUN.FAILED`, `ACTOR.RUN.TIMED_OUT`, `ACTOR.RUN.ABORTED`). This is particularly useful for:

* Monitoring scheduled or recurring tasks
* Building workflows dependent on specific data collection tasks
* Processing results from tasks with predefined configurations

![Screenshot of the Task Run Finished trigger configuration in Workato](/assets/images/trigger-task-42c9a27fa1639368cc035f5e7edb7089.png)

## Actions

*The Apify connector offers comprehensive actions to interact with the Apify platform.*

### Run Actor

*Run an Apify Actor with customizable execution parameters.*

This action runs an Apify Actor with your specified input and execution parameters. You can choose to wait for completion or start the run asynchronously. Actors are reusable serverless programs that can scrape websites, process data, and automate workflows. You can:

* Select from your recently used Actors or Apify store Actors
* Provide input using dynamic schema-based fields or raw JSON
* Configure run options like memory allocation, timeout, and build version
* Choose between synchronous (wait for completion) or asynchronous execution

Input field descriptions

Each input field includes helpful descriptions that guide you toward the correct format and expected values.

Default values for input fields will be displayed as placeholders, giving you a starting point for configuration.

![Screenshot of the Run Actor action configuration interface in Workato](/assets/images/run-actor-5c60c29f131f1471c3dabc01211f89d5.png)

### Run Task

*Run an Apify Actor task with optional input overrides.*

This action runs an Apify Task with optional input overrides and execution parameters. Tasks are pre-configured Actor runs with saved input, making them ideal for repeated executions. You can optionally override the task's configured input. You can:

* Select from your saved tasks or input specific Task ID
* Override the task's pre-configured input with new JSON if needed
* Configure task options like memory, build version, or timeout

![Screenshot of the Run Task action configuration interface in Workato](/assets/images/run-task-48e0a9157a7fac1fdc833822d9f16888.png)

### Get Dataset Items

*Retrieves items from a dataset with dynamic field mapping.*

Select a dataset to dynamically generate output fields and retrieve its items. This action automatically analyzes the dataset structure and creates appropriate output fields for your recipe. Key features:

* Automatically detects and creates output fields based on dataset structure
* Retrieves data records from specified datasets with pagination support
* Returns structured data ready for downstream recipe steps

#### Dynamic Schema Detection

The connector samples your dataset to create appropriate output fields:

* *Works best with consistent data*: When all items have the same field names and data types
* *May have limitations with mixed data*: If items have different structures or field types
* *Samples up to 25 items*: Fields that only appear after the first 25 items won't be detected

Best practice

For optimal results, use datasets where all items follow a consistent structure. Test with a small sample to verify field mappings work as expected.

![Screenshot of the Get Dataset Items action configuration interface in Workato](/assets/images/get-dataset-493856c63cb47407f5ea2194d8abfeda.png)

### Get Key-value store Record

*Retrieves a single record from a Key-value store.*

Select a Key-value store and a key to retrieve the corresponding record as a text string or binary file. Key-value stores often contain metadata, logs, or files from Actor runs. This action:

* Fetches named entries by key from specified stores with dynamic key selection
* Accesses configuration data, screenshots, or custom outputs
* Supports both text and binary content types
* Enables flexible data retrieval for various use cases

![Screenshot of the Get Key-value store record action configuration interface in Workato](/assets/images/get-key-val-ab8da008cd8c9d8a4042738dc304ebee.png)

### Scrape Single URL

*Scrapes a single URL using a selected Apify crawler.*

Provide a single URL and a desired crawler type to get structured scraped data from that page as a JSON object. This action provides immediate, on-demand scraping capabilities:

* Scrapes content from a single specified URL
* Offers multiple crawler types (Adaptive, Firefox, Cheerio, JSDOM)
* Returns extracted content in structured format (text, markdown, HTML, metadata)
* Perfect for real-time data extraction triggered by recipes

![Screenshot of the Scrape Single URL action configuration interface in Workato](/assets/images/scrape-url-bd0f5dc2498efa7146e255fb258ed7b5.png)

## Long‑running scrapes and async pattern in Workato

Long-running scrapes can exceed typical step execution expectations. Use this asynchronous pattern to keep recipes reliable and scalable.

1. Start the run without waiting

   <!-- -->

   * In a recipe, add the **Run Actor** action and configure inputs as needed.
   * Run asynchronously (do not block downstream steps on completion).
   * ![Screenshot showing the Run Actor action configuration with async option in Workato](/assets/images/run-actor-5c60c29f131f1471c3dabc01211f89d5.png)

2. Continue when the run finishes

   <!-- -->

   * Build a separate recipe with the **Actor Run Finished** trigger.
   * Filter for the specific Actor or Task you started in Step 1.
   * ![Screenshot showing how to filter for specific Actor in the Run Finished trigger](/assets/images/trigger-actor-89021d81a515333cf895dcfa618b77c4.png)

3. Fetch results and process

   <!-- -->

   * In the triggered recipe, add **Get Dataset Items** (use the dataset ID from the trigger payload) and continue processing.
   * ![Screenshot showing how to use dataset ID from trigger payload in Get Dataset Items action](/assets/images/get-dataset-493856c63cb47407f5ea2194d8abfeda.png)

## Example use cases

### Data mapping and workflow design

Workato's visual interface makes it easy to connect Apify data with other business applications:

* *Data pills:* Use output fields from Apify triggers and actions as inputs for subsequent steps
* *Field mapping:* Visually map scraped data fields to CRM, database, or spreadsheet columns
* *Conditional logic:* Build workflows that respond differently based on Actor run status or data content
* *Data transformation:* Apply filters, formatting, and calculations to scraped data before sending to target systems

### Best practices

* *Use tasks for recurring workflows:* Create and use Apify tasks for consistent, repeatable scraping jobs
* *Handle async operations:* For long-running Actors, use asynchronous execution and separate triggers to monitor completion
* *Error handling:* Implement proper error handling for failed Actor runs using Workato's conditional logic
* *Rate limiting:* Be mindful of API rate limits when designing high-frequency workflows
* *Data validation:* Validate scraped data before sending to critical business systems

## Troubleshooting

* *Connection issues:* Verify your API token has the necessary permissions and hasn't expired
* *Actor selection:* If an Actor doesn't appear in dropdowns, ensure it has been run at least once
* *Timeout errors:* For long-running Actors, use asynchronous execution rather than waiting for completion
* *Data format:* Ensure JSON inputs are properly formatted and match expected Actor input schema
* *OAuth issues:* If using OAuth, make sure the redirect URI matches your Workato region (US or EU)
* *Resource not found errors:* Check that IDs are correct and case-sensitive
* *Dataset field mapping issues:* If you experience incorrect data types or missing fields in the Get Dataset Items action data pill, this may be caused by non-homogeneous data in your dataset. The connector samples only the first 25 items to determine field types, so inconsistent data structures can lead to mapping problems. Try to ensure your dataset has consistent field names and data types across all items.

If you have any questions or need help, feel free to reach out to us on our https://discord.com/invite/jyEM2PRvMU.
