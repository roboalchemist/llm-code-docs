# Source: https://docs.axonius.com/docs/using-natural-language-to-create-queries.md

# Using AI Query Assistant to Create Queries

Use the **AI Query Assistant** to create a query by describing what you want in natural language or regular English. Your statement is then analyzed and expressed in the Query Wizard UI using the query statement elements.

For example, you can ask to see those assets that have been seen in the last 14 days and have no agent installed. The Query Wizard will display your request in query elements and filter the asset list accordingly.

<Callout icon="📘" theme="info">
  Notes

  * This feature is available only for Device assets.

  * Usage of natural language may be limited by token availability. You can view your account details by clicking **OpenAI account**.

  * [Allow GPT](/docs/configuring-chatgpt-settings) must be enabled in System Settings to use the AI Query Assistant.
</Callout>

<Callout icon="📘" theme="info">
  **Q\&A**

  * **What data is sent to the AI Query Assistant provider?**
    * Only the query text entered by the user (the prompt) is sent.
    * No other data, including any data from the environment itself, is transmitted.

  * **Is customer-related data sent to the AI Query Assistant provider?**
    * No customer related data is sent.
    * It is not possible to identify the user or the customer based on the query data sent, since only the query text is sent without any additional metadata.

  * **Can the AI Query Assistant provider save the data?**
    * No data can be saved by the AI Query Assistant provider.
    * There is no training of the model using the query data.
    * The lack of state prevents it from being saved in any way.
</Callout>

**To create a query with natural language:**

1. Open the Query Wizard from an asset page, an Enforcement Action or anywhere the Query Wizard is available.
2. In the natural language field, enter a description of the assets you want to find.

<Image align="center" alt="QueryWizardGPTStatement.png" border={false} width="1000px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/QueryWizardGPTStatement.png" />

If the statement cannot be evaluated, an error message is displayed. Rewrite the statement and try again.

3. Click **Go**. The statement is analyzed, translated into query elements, and applied.