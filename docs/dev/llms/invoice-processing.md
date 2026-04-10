# Source: https://dev.writer.com/agent-builder/invoice-processing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Process invoices and send to Slack

This tutorial walks through building an agent that processes PDF invoices, extracts structured data, and sends the results to Slack. The agent takes an uploaded invoice PDF, extracts key information like vendor details and line items, and posts a formatted summary to a Slack channel.

<CardGroup cols={3}>
  <Card title="Interface">
        <img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/invoice-processing-ui.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=91e1504d0e0b0fed6beaee4e3613ab0d" alt="Invoice processing interface" data-og-width="3456" width="3456" data-og-height="1812" height="1812" data-path="images/agent-builder/invoice-processing/invoice-processing-ui.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/invoice-processing-ui.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=f46ca9356480600bae6baa6321a82c1d 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/invoice-processing-ui.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=040e526aad341c7947cb92dfa874d608 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/invoice-processing-ui.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=4d1cce99cba05ed92a6d764bea1be799 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/invoice-processing-ui.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=e0dda655ba5e64af44c4531b838626c2 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/invoice-processing-ui.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=23046f0e821324a4f997eec2c44fa7dd 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/invoice-processing-ui.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=66c91a8386807d01c3f51b9dd331e563 2500w" />
  </Card>

  <Card title="Blueprint">
        <img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/invoice-processing-blueprint.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=f2ca546cce690c54f94b5dd564982278" alt="Invoice processing blueprint" data-og-width="3456" width="3456" data-og-height="1800" height="1800" data-path="images/agent-builder/invoice-processing/invoice-processing-blueprint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/invoice-processing-blueprint.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=9fbf3e07c6db5581b61482a7332024dd 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/invoice-processing-blueprint.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=bd449de73548eca0c4a40a3fd6a1abd3 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/invoice-processing-blueprint.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=c438f074f3439a72dd49c8d8bfbab772 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/invoice-processing-blueprint.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=7c22860a3c414100fb98ecea91c9398f 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/invoice-processing-blueprint.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=4ed43624e12ef197a8bfb9cbcb617da9 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/invoice-processing-blueprint.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=6267021bb940c573379a98b385763d84 2500w" />
  </Card>

  <Card title="Slack message">
        <img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/slack-message.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=3dd999da4d1e2abb49fa4417de707cc3" alt="Invoice processing Slack message" data-og-width="1172" width="1172" data-og-height="308" height="308" data-path="images/agent-builder/invoice-processing/slack-message.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/slack-message.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=96a6357bd0d87a475bbc54ab20026bdf 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/slack-message.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=346fc7e4f0231663fb27fd24ecdd3d50 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/slack-message.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=c94d92cc685d4d0e7204b0e67c22fdae 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/slack-message.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=8b0768872f4ae4cd5a39a44964e91a88 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/slack-message.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=fc26d4bb060a382f7cf56c47b0631b86 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/slack-message.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=ecdc156592b1efd92bda9be5788ff7fc 2500w" />
  </Card>
</CardGroup>

This pattern is useful for automating accounts payable workflows, expense processing, and any scenario where you need to extract structured data from documents and route it to business systems. Once you complete this tutorial, you can continue enhancing the agent by adding [tool calling](/agent-builder/tool-calling-tutorial) with behaviors like validating invoices, flagging potential issues, and comparing invoices against historical data.

## Prerequisites

Before building this agent, you need to set up a Slack webhook to send the invoice data to a Slack channel.

Follow the instructions in the [Slack documentation](https://api.slack.com/messaging/webhooks) to set up a webhook. The general steps are:

1. Go to [Slack API](https://api.slack.com/apps) and create a new app
2. Select "From scratch" and provide a name for your app
3. Choose the Slack workspace where you want to build the agent
4. Navigate to "Incoming Webhooks" in the left sidebar of the new app and activate webhooks
5. Click "Add New Webhook to Workspace" and select the channel where invoices should be posted. You might need administrator permissions to add a webhook to a channel, depending on your Slack workspace settings.
6. Copy the webhook URL - you'll need this for the HTTP request block. The webhook URL will look like: `https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX`

## Agent overview

This agent processes invoices through the following steps:

1. User uploads a PDF invoice file
2. File is uploaded to Writer Cloud storage
3. PDF content is extracted and parsed
4. AI extracts structured invoice data such as vendor, amounts, line items.
5. Formatted invoice summary is sent to Slack

## Build the UI

The agent's UI contains a file input for uploading invoices and a submit button.

<img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/invoice-processing-ui.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=91e1504d0e0b0fed6beaee4e3613ab0d" alt="UI" data-og-width="3456" width="3456" data-og-height="1812" height="1812" data-path="images/agent-builder/invoice-processing/invoice-processing-ui.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/invoice-processing-ui.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=f46ca9356480600bae6baa6321a82c1d 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/invoice-processing-ui.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=040e526aad341c7947cb92dfa874d608 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/invoice-processing-ui.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=4d1cce99cba05ed92a6d764bea1be799 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/invoice-processing-ui.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=e0dda655ba5e64af44c4531b838626c2 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/invoice-processing-ui.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=23046f0e821324a4f997eec2c44fa7dd 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/invoice-processing-ui.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=66c91a8386807d01c3f51b9dd331e563 2500w" />

<Steps>
  <Step title="Add a file input">
    Drag a **File Input** block to the canvas. In the block's configuration menu, update the following:

    * **Label**: `Invoice`
    * **Allowed file types**: `.pdf`
    * **Link variable** under **Binding**: `invoice`

    This allows users to upload PDF files and stores the file in the `invoice` state variable.
  </Step>

  <Step title="Add a button to submit the request">
    Drag a **Button** block to the canvas. In the block's configuration menu, update the following:

    * **Label**: `Submit`
  </Step>
</Steps>

## Build the blueprint

The logic of the blueprint is as follows:

1. The **UI Trigger** block starts the agent when the user clicks the submit button
2. The **Add files to Writer Cloud** block uploads the invoice file to cloud storage
3. The **Parse PDF** block extracts text content from the uploaded file
4. The **Structured Output** block processes the PDF text and extracts invoice data as JSON
5. The **HTTP Request** block sends the structured data to Slack

The finished blueprint contains the following blocks:
<img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/invoice-processing-blueprint.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=f2ca546cce690c54f94b5dd564982278" alt="Finished blueprint" data-og-width="3456" width="3456" data-og-height="1800" height="1800" data-path="images/agent-builder/invoice-processing/invoice-processing-blueprint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/invoice-processing-blueprint.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=9fbf3e07c6db5581b61482a7332024dd 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/invoice-processing-blueprint.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=bd449de73548eca0c4a40a3fd6a1abd3 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/invoice-processing-blueprint.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=c438f074f3439a72dd49c8d8bfbab772 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/invoice-processing-blueprint.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=7c22860a3c414100fb98ecea91c9398f 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/invoice-processing-blueprint.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=4ed43624e12ef197a8bfb9cbcb617da9 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/invoice-processing-blueprint.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=6267021bb940c573379a98b385763d84 2500w" />

<Steps>
  <Step title="Add a UI Trigger block">
    Drag a **UI Trigger** block to the canvas. In the block's configuration menu, update the following:

    * **Component Id**: select the **Submit** button from the dropdown
    * **Trigger**: `wf-click`

    This triggers the blueprint when the user clicks the Process Invoice button.
  </Step>

  <Step title="Add an Add files to Writer Cloud block">
    Drag an **Add files to Writer Cloud** block to the canvas. In the block's configuration menu, update the following:

    * **Files**: `@{invoice}`

    This uploads the invoice file from the `invoice` state variable to Writer Cloud storage.
  </Step>

  <Step title="Add a Parse PDF block">
    Drag a **Parse PDF tool** block to the canvas. In the block's configuration menu, update the following:

    * **File**: `@{result.0.id}`

    This extracts the text content from the uploaded PDF file using the file information returned from the Add files to Writer Cloud block.
  </Step>

  <Step title="Add a Structured Output block">
    Drag a **Structured Output** block to the canvas. In the block's configuration menu, update the following:

    * **Prompt**:

    ```
    Extract the following information from this invoice:

    - Invoice number
    - Vendor name and address
    - Invoice date and due date
    - Bill-to company and address  
    - Total amount, subtotal, and tax amount
    - Currency
    - All line items with descriptions, quantities, unit prices, and totals
    - Payment terms
    - Purchase order number (if present)

    If any information is not clearly stated in the invoice, use null for that field.
    ```

    * **Input**: `@{result}`
    * **Model**: `Palmyra X5`
    * **JSON Schema**: The following is an example JSON schema for the structured output. You can use this as a starting point, or create your own schema based on the invoice format you'd like to extract.

    ```json  theme={null}
    {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "title": "Invoice Processing Data",
      "description": "Schema for structured invoice data extracted from PDF documents",
      "properties": {
        "invoiceNumber": {
          "type": "string",
          "description": "Unique invoice identifier"
        },
        "vendorName": {
          "type": "string",
          "description": "Name of the company or vendor issuing the invoice"
        },
        "vendorAddress": {
          "type": "string",
          "description": "Full address of the vendor"
        },
        "invoiceDate": {
          "type": "string",
          "format": "date",
          "description": "Date the invoice was issued (YYYY-MM-DD format)"
        },
        "dueDate": {
          "type": "string",
          "format": "date",
          "description": "Payment due date (YYYY-MM-DD format)"
        },
        "billToCompany": {
          "type": "string",
          "description": "Company name being billed"
        },
        "billToAddress": {
          "type": "string",
          "description": "Billing address"
        },
        "totalAmount": {
          "type": "number",
          "description": "Total invoice amount including tax",
          "minimum": 0
        },
        "subtotal": {
          "type": "number",
          "description": "Subtotal before tax",
          "minimum": 0
        },
        "taxAmount": {
          "type": "number",
          "description": "Total tax amount",
          "minimum": 0
        },
        "currency": {
          "type": "string",
          "description": "Currency code (e.g., USD, EUR, GBP)",
          "default": "USD"
        },
        "lineItems": {
          "type": "array",
          "description": "Individual items or services on the invoice",
          "items": {
            "type": "object",
            "properties": {
              "description": {
                "type": "string",
                "description": "Description of the product or service"
              },
              "quantity": {
                "type": "number",
                "description": "Quantity of items",
                "minimum": 0
              },
              "unitPrice": {
                "type": "number",
                "description": "Price per unit",
                "minimum": 0
              },
              "totalPrice": {
                "type": "number",
                "description": "Total price for this line item",
                "minimum": 0
              }
            },
            "required": ["description", "totalPrice"],
            "additionalProperties": false
          }
        },
        "paymentTerms": {
          "type": "string",
          "description": "Payment terms (e.g., 'Net 30', 'Due on receipt')"
        },
        "purchaseOrderNumber": {
          "type": "string",
          "description": "Purchase order number if referenced on invoice"
        }
      },
      "required": [
        "invoiceNumber",
        "vendorName",
        "invoiceDate",
        "totalAmount",
        "currency",
        "lineItems"
      ],
      "additionalProperties": false
    }
    ```

    This processes the PDF text and extracts structured invoice data according to the JSON schema. The AI will identify and extract the relevant information from the invoice text.
  </Step>

  <Step title="Add an HTTP Request block to send to Slack">
    Drag an **HTTP Request** block to the canvas. In the block's configuration menu, update the following:

    * **Method**: `POST`
    * **URL**: Your [Slack webhook URL](/agent-builder/invoice-processing#prerequisites)
    * **Body**:

    ```json  theme={null}
    {
      "text": "New Invoice Processed",
      "blocks": [
        {
          "type": "header",
          "text": {
            "type": "plain_text",
            "text": "📄 Invoice Processed"
          }
        },
        {
          "type": "section",
          "fields": [
            {
              "type": "mrkdwn",
              "text": "*Invoice #:* @{result.invoiceNumber}"
            },
            {
              "type": "mrkdwn",
              "text": "*Vendor:* @{result.vendorName}"
            },
            {
              "type": "mrkdwn",
              "text": "*Date:* @{result.invoiceDate}"
            },
            {
              "type": "mrkdwn",
              "text": "*Due Date:* @{result.dueDate}"
            },
            {
              "type": "mrkdwn",
              "text": "*Amount:* @{result.currency} @{result.totalAmount}"
            },
            {
              "type": "mrkdwn",
              "text": "*Bill To:* @{result.billToCompany}"
            }
          ]
        }
      ]
    }
    ```

    This sends a formatted message to Slack with the key invoice details. The message uses Slack's block kit format to create a structured, readable invoice summary.
  </Step>
</Steps>

## Preview the agent

Navigate to the **Preview** tab to test the agent.

Upload a PDF invoice and click the Process Invoice button. The agent will upload the file, extract the invoice data, and send a summary to your configured Slack channel.

You can see the agent's progress in the **Logs** tab, including the extracted JSON data and the Slack API response.

You should see a message in the Slack channel with the invoice data.

<img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/slack-message.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=3dd999da4d1e2abb49fa4417de707cc3" alt="Slack message" data-og-width="1172" width="1172" data-og-height="308" height="308" data-path="images/agent-builder/invoice-processing/slack-message.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/slack-message.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=96a6357bd0d87a475bbc54ab20026bdf 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/slack-message.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=346fc7e4f0231663fb27fd24ecdd3d50 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/slack-message.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=c94d92cc685d4d0e7204b0e67c22fdae 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/slack-message.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=8b0768872f4ae4cd5a39a44964e91a88 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/slack-message.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=fc26d4bb060a382f7cf56c47b0631b86 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/invoice-processing/slack-message.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=ecdc156592b1efd92bda9be5788ff7fc 2500w" />

## Add tool calling for invoice validation

You can enhance this agent by adding [tool calling](/agent-builder/tool-calling) to validate invoices and flag potential issues. Here are some ways to extend the functionality:

* Check for missing required fields like tax ID or payment terms
* Compare against previous invoices from the same vendor to detect price discrepancies
* Validate amounts against purchase orders and company spending policies
* Flag duplicate invoice numbers or unusual payment terms
* Verify vendor details against your approved vendor list

To add these capabilities:

1. Add a tool calling block after the structured output to analyze the extracted data
2. Configure validation rules and checks in your custom Python code
3. Update the Slack message to include any validation warnings or approvals
4. Optionally trigger different workflows based on the validation results

Check out the [tool calling tutorial](/agent-builder/tool-calling-tutorial) to learn how to add these validation capabilities to your invoice processing agent.

<feedback />
