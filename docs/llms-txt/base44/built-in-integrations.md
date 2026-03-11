# Source: https://docs.base44.com/Integrations/built-in-integrations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Base44 built-in integrations

> Learn how to use Base44 built-in integrations to power smart features in your apps.

Built-in integrations are Base44 services you can call in your app without extra setup. They cover common needs such as sending email, generating images, handling file uploads, extracting data from files, and running large language model (LLM) calls. You can use them from the AI chat, in flows, or in your own backend functions.

Each call to a built-in integration uses integration credits, so it is important to understand what each integration does and when to use it.

***

## Understanding built-in integrations

Built-in integrations are ready-made actions that run inside Base44. They are available in every app, and you do not need to set up API keys, connectors, or your own infrastructure. You can add them wherever you design logic in your app, and Base44 takes care of hosting, scaling, and provider connections behind the scenes.

Use built-in integrations when you want Base44 to handle these shared tasks for you. For example, you can send emails without configuring an email service, generate images on demand, let people upload and store files in Base44, extract structured data from uploads into your entities, or call LLMs to power agents and data workflows while keeping all billing and provider management in one place.

<Tip>
  **Whats the difference between built-in integrations, connectors and custom integrations?**

  Connectors create OAuth connections to your own accounts in tools such as Gmail, Slack, or Google Drive. Custom integrations use your own API keys or OpenAPI specs. Built-in integrations rely on Base44’s own managed provider setup, so you do not handle API keys or other credentials yourself.

  Use connectors or custom integrations when you need to act through your own provider accounts, control scopes and identities, or connect to tools that built-in integrations do not cover yet.
</Tip>

***

## Sending emails

SendEmail is a built-in integration that sends transactional and workflow emails from your app, such as confirmations, alerts, digests, and other notifications that need to go out automatically.

You can trigger SendEmail from:

* Flows that Base44 builds from the AI chat.
* Backend functions that you edit in your app’s code.
* Agents or automations that need to notify people by email.

SendEmail is helpful for tasks like sending welcome messages, daily or weekly summaries, status change alerts, or passwordless access links.

<Card icon="envelope" title="Example prompts for SendEmail">
  * `Connect SendEmail so that when someone submits this form, they get a confirmation email with their details.`
  * `Add a daily flow that uses SendEmail to send me a summary of all new signups in this app.`
  * `When a task is marked as 'critical', use SendEmail to alert the ops team with a link to the record.`
</Card>

<Note>
  **Notes:**

  * SendEmail does not support sending to external mailing lists or adding file attachments.
  * Each email sent through SendEmail uses integration credits. The exact cost depends on how many messages you send and how often flows run.
</Note>

***

## Generating images

GenerateImage is a built-in integration that creates images using AI from text prompts or from flows in your app. It is useful for generating on-demand visuals such as covers, thumbnails, illustrations, or avatars without managing an external image provider.

GenerateImage can support scenarios like creating cover images for new content, generating temporary product images when photos are not ready yet, or producing simple marketing assets based on text descriptions.

<Card icon="image" title="Example prompts for GenerateImage">
  * `Whenever I add a new article, use GenerateImage to create a cover image that matches the title and theme.`
  * `When I create a new product, generate a simple placeholder image with the product name on a solid background and store its URL in the Products entity.`
  * `Add a page where I can enter a short description and use GenerateImage to create a marketing image I can download.`
</Card>

***

## Uploading files

UploadFile is a built-in integration that lets your app accept file uploads from people who use it. It powers file upload components in your UI so you can collect documents, images, and data files without building your own storage or upload endpoints.

UploadFile is a good choice when you want to gather receipts, contracts, screenshots, profile pictures, or data files such as CSVs and spreadsheets and keep them tied to records in your app.

<Card icon="file-arrow-up" title="Example prompts for UploadFile">
  * `Add a file upload field to this request page using UploadFile so people can attach a PDF when they submit.`
  * `Let people upload profile pictures, store the file using UploadFile, and save the image URL in the Members entity.`
  * `Create a page where I can drag and drop CSV files, upload them with UploadFile, and show a table of uploaded files.`
</Card>

<Note>
  For current file sizes and types, check the [Uploading files](/Building-your-app/Using-media) guide.
</Note>

***

## Extracting data from uploaded files

ExtractDataFromUploadedFile is a built-in integration that reads structured content from uploaded files and turns it into data your app can work with. It helps you move from “file storage” to “usable records” by pulling out key fields and rows for you. You can pull structured data from uploaded files (CSV, PNG, JPG, JPEG, PDF) using JSON schemas. It is particularly useful for importing data in bulk.

You can use ExtractDataFromUploadedFile to parse receipts, invoices, forms, or data files and convert them into clean entities, such as Contacts, Invoices, Expenses, or Metrics, without hand-writing parsing logic.

You can also combine UploadFile and ExtractDataFromUploadedFile. For example, someone uploads a CSV, Excel file, or PDF through UploadFile, then you use ExtractDataFromUploadedFile to transform the content into rows in your data tables.

<Card icon="database" title="Example prompts for ExtractDataFromUploadedFile">
  * `When I upload a CSV file of customers, use UploadFile and ExtractDataFromUploadedFile to import the records into a Customers entity.`
  * `Let me upload invoice PDFs and use ExtractDataFromUploadedFile to pull invoice number, vendor, date, subtotal, and total into an Invoices table.`
  * `Build a page where I can upload an Excel file with KPIs, then use ExtractDataFromUploadedFile to update the Metrics entity.`
</Card>

<Tip>
  Extraction quality depends on the file type, its structure, and how well the fields are labeled. For critical workflows, test with several real examples and adjust your entities or flows based on the results.
</Tip>

***

## Running LLM calls

invokeLLM is a built-in integration that runs large language model (LLM) calls from inside your app. It lets your app “think” with AI over your data and flows, and powers text generation, explanations, and decisions that depend on LLMs.

invokeLLM is a good fit when you want to build data agents, summarize or rewrite content, classify records, generate recommendations from dashboards, or add in-app assistants that help people complete tasks. It works like other built-in integrations in your flows and backend functions, but with an extra layer of control: you can choose which underlying model it uses.

<Card icon="computer-classic" title="Example prompts for invokeLLM">
  * `Add a data agent that uses invokeLLM so I can ask natural language questions about my Sales entity and see the answers in this app.`
  * `When a support ticket is created, use invokeLLM to summarize the description into a short overview and store it in a Summary field.`
  * `Create a flow that uses invokeLLM to classify each new lead into one of three segments based on their notes, and save the segment on the lead record.`
  * `Switch invokeLLM to use a stronger model for my agents so they can give better explanations on complex analytics dashboards, and update any flows that depend on invokeLLM.`
</Card>

### Choosing the model for invokeLLM

By default, invokeLLM uses a standard model that balances quality and cost. If you want, you can tell the AI chat inside Base44 to use any [supported model](https://docs.base44.com/Building-your-app/AI-chat-modes#choosing-your-ai-model) in your workspace as the underlying model for invokeLLM by asking the AI chat to switch it for you.

For example, you can say:`Switch invokeLLM to use <model-name> for this app`.

<Note>
  **Note:** When you change the model for invokeLLM, the style, reasoning ability, and quality of responses update to match that model. The number of integration credits each call uses also changes based on the new model’s cost, and any flows or agents that rely on invokeLLM start using the new model automatically.
</Note>

[Agents](/Getting-Started/ai-agent) you build on Base44 use invokeLLM behind the scenes, so when you switch the model, your agents update as well and their integration credit usage changes to match. Stronger models typically consume more credits per call than lighter models.


Built with [Mintlify](https://mintlify.com).