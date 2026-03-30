# Source: https://docs.axonius.com/docs/configuring-chatgpt-settings.md

# Configuring the AI Query Assistant

Use the AI Query Assistant to write a query using everyday natural language. The text is then interpreted by ChatGPT and the request is populated into the Query Wizard options.

Axonius provides a number of ways to integrate with ChatGPT:

* **Axonius Hosted** - For hosted Axonius instances only. The Microsoft Azure version of ChatGPT is integrated into the on-site environment. No connection outside the environment is needed.
* **OpenAI** - Integrates with the original ChatGPT supplier.
* **Microsoft Azure** - Integrates with the ChatGPT supplied by Microsoft Azure.

See [Using AI Query Assistant to Create Queries](/docs/using-natural-language-to-create-queries) for more about how to create queries with natural language.

<Callout icon="📘" theme="info">
  Note

  Usage of the Query Assistant may be limited by ChatGPT token availability. You can view your account details by clicking OpenAI account.
</Callout>

**To configure ChatGPT settings:**

1. In System Settings, navigate to **External Integrations**.

2. Select **GPT**.

3. Enable **AI Query Assistant**.

4. Each integration option has its own terms and conditions. Read the statements before saving the configuration and select the check box.

5. Select one of the integration types:
   * **Axonius Hosted**
   * **OpenAI**
   * **Microsoft Azure**

6. When OpenAI or Microsoft Azure are selected, fill in the additional fields.
   * For OpenAI:
     * Enter the API key provided by your company
   * For Microsoft Azure, enter the following:
     * Endpoint/Base Url in the form `https://TENANTNAME.openai.azure.com`
     * Deployment/Engine Name
     * API Key

7. Click **Save**.