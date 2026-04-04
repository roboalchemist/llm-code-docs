# Source: https://docs.pinecone.io/guides/assistant/quickstart/n8n-quickstart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Pinecone Assistant: n8n quickstart

> Create an n8n workflow to chat with documents using Pinecone Assistant and OpenAI.

Create an [n8n](https://docs.n8n.io/choose-n8n/) workflow that that downloads files via HTTP, uploads them to Pinecone Assistant, and enables you to chat with documents using OpenAI.

## 1. Get API keys

Your n8n workflow will need API keys for Pinecone and OpenAI.

<Steps>
  <Step title="Get a Pinecone API key">
    Create a new API key in the [Pinecone console](https://app.pinecone.io/organizations/-/keys), or use the widget below to generate a key. If you don't have a Pinecone account, the widget will sign you up for the free [Starter plan](https://www.pinecone.io/pricing/).

    <div style={{minWidth: '450px', minHeight:'152px'}}>
      <div id="pinecone-connect-widget">
        <div class="connect-widget-skeleton">
          <div class="skeleton-content" />
        </div>
      </div>
    </div>

    Your generated API key:

    ```shell  theme={null}
    "{{YOUR_API_KEY}}"
    ```
  </Step>

  <Step title="Get an OpenAI API key">
    Create a new API key in the [OpenAI console](https://platform.openai.com/api-keys).
  </Step>
</Steps>

## 2. Create an assistant

[Create an assistant](https://app.pinecone.io/organizations/-/projects/-/assistant) in the Pinecone console:

* Name your assistant `n8n-assistant`.

## 3. Set up n8n

<Steps>
  <Step title="Install the Pinecone Assistant node">
    In your n8n account, [install the Pinecone Assistant node](https://docs.n8n.io/integrations/community-nodes/installation/verified-install/) using the nodes panel.

    <Note>
      Restart your n8n instance if the Pinecone Assistant node doesn't appear in the nodes panel.
    </Note>
  </Step>

  <Step title="Create a new workflow">
    In your n8n account, [create a new workflow](https://docs.n8n.io/workflows/create/).
  </Step>

  <Step title="Import a workflow template">
    Copy this workflow template URL:

    ```shell  theme={null}
    https://raw.githubusercontent.com/pinecone-io/n8n-templates/refs/heads/main/assistant-quickstart/assistant-quickstart.json
    ```

    Paste the URL anywhere in the workflow editor and then click **Import** to add the workflow.
  </Step>

  <Step title="Add credentials to the workflow">
    * Add your Pinecone credentials:
      * In the **Upload file to Assistant** node, select **Credential to connect with > Create new credential** and paste in your Pinecone API key.

    * Add your OpenAI credentials:
      * In the **OpenAI Chat Model** node, select **Credential to connect with > Create new credential** and paste in your OpenAI API key.
  </Step>

  <Step title="Execute the workflow">
    By default, the workflow downloads recent Pinecone release notes and uploads them to your assistant. Click **Execute workflow** to start uploading documents.

    <Tip>
      You can add your own files to the workflow by changing the URLs in the **Set file urls** node.
    </Tip>
  </Step>
</Steps>

## 4. Chat with your docs

Once the documents are uploaded, you can chat with your assistant. In the n8n workflow, use the **Chat input** node to ask questions like:

```
What support does Pinecone have for MCP?
```

## Next steps

* Customize the workflow for your own use case:
  * Change the urls in the **Set file urls** node to use your own files.
  * Customize the system message on the **AI Agent** node to indicate what kind of knowledge is stored in Pinecone Assistant.
  * To help manage token consumption, add the Top K and/or Snippet Size parameters to the **Get context from Assistant** node.
  * Filter the context snippets even further by adding metadata filters to the **Get context from Assistant** node.
* Use n8n, Pinecone Assistant, and OpenAI to [chat with your Google Drive documents](https://n8n.io/workflows/9942-rag-powered-document-chat-with-google-drive-openai-and-pinecone-assistant/).
* Learn more about [Pinecone Assistant](/guides/assistant/overview).
* Get help in the [Pinecone Discord community](https://discord.gg/tJ8V62S3sH).
