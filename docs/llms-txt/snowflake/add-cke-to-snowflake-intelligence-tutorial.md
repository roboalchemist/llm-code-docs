# Source: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-knowledge-extensions/tutorials/add-cke-to-snowflake-intelligence-tutorial.md

Cortex Knowledge Extensions

Cortex Agent API

# Tutorial 3: Add a CKE to Snowflake Intelligence

## Step-by-step instructions

It’s easy to add a Cortex Knowledge Extension to Snowflake Intelligence. Once you have a CKE in your account, you can add it to Snowflake Intelligence by adding the CKE to an Agent in Snowsight.

> **Important:**
>
> Before you get started, make sure the Snowflake Intelligence has access to the CKE:
>
> ```sqlexample
> -- Grant Snowflake Intelligence the right access to the CKE so it can be added as an agent
> grant imported privileges on database <CKE_DATABASE_NAME> to role <SNOWFLAKE_INTELLIGENCE_ROLE>;
> ```

1. Sign in to [Snowsight](../../../ui-snowsight-gs.md).
2. In the navigation menu, select AI & ML » Agents.
3. In the Agents screen, select Create Agent and give the Agent a name.
4. Under Knowledge, click + Search service.
5. Select the Database that has the CKE, and select the Search Service for the CKE.
6. Give the CKE a display name.
7. Indicate the column in the CKE that references the URL of the underlying content. This is useful for giving users additional context and an opportunity to dig deeper into attribution.
8. Click Create.
9. Navigate to Snowflake Intelligence on the left side.
10. Select on the drop down under the textbox to select the new Agent with your CKE tied to it.
11. Ask a question with the selected Agent and see the cited answers with links back to the source content via the CKE.
