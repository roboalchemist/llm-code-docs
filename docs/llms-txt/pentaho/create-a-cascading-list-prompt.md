# Source: https://docs.pentaho.com/pba/pentaho-dashboard-designer-cp/advanced-topics/use-prompts-on-dashboards/other-prompt-types/create-a-list-prompt/create-a-cascading-list-prompt.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-dashboard-designer-cp/advanced-topics/use-prompts-on-dashboards/other-prompt-types/create-a-list-prompt/create-a-cascading-list-prompt.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-dashboard-designer-cp/advanced-topics/use-prompts-on-dashboards/other-prompt-types/create-a-list-prompt/create-a-cascading-list-prompt.md

# Create a cascading list prompt

A cascading prompt changes based on the value a user selects. For example, when the value in the drop-down list **Country** changes, this prompt is automatically applied to the second prompt, **City**, which changes its values.

This task uses the example of creating a country-city cascade prompt.

![Cascading prompt example](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-057d4315b41638dd9eb75a0f485dde5430563cb6%2FPDD_PROMPT_cascading_filter_sample_ONYX.png?alt=media)

1. For **Type**, select **Metadata List** to create the drop-down prompt `Country`.

   ![Filter from metadata list](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-df69243525ff444f1c6f2385002f6a67c560a2b1%2FPDD_PROMPTS_cascading_metadata_query_sample_filter_ONYX.png?alt=media)
2. For **Type**, select **SQL List** which includes a parameter,**${selected\_country}**, in its associated query for the check box prompt `City`.

   ![Filter from SQL list](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-d4a9abc68c92ffc2a1df19b0984b5791e41bda50%2FPDD_PROMPTS_cascading_sql_query_sample_filter_ONYX.png?alt=media)
3. Set the **Default Value** for the **selected\_country** parameter to `USA` with New York City (`NYC`) as the initially selected value for the check box prompt.

To link the **City** prompt to the **Country** prompt, another **Source** for the **selected\_country** parameter was chosen. The alternate source is the **Country** prompt. When the prompts are linked, users can choose a country and then choose a city (or cities) in the country of their choice.

Using this example, the report designer can now add a data table, chart, or other content in the dashboard which can be driven by the prompt he or she just created. If the designer adds a pie chart to the dashboard, the pie chart will display the percentage of sales per city. In the Query Editor, the report designer creates a parameter, **{City}**, with an extended default value: NYC|Las Vegas. The resulting pie chart displays values for New York City and Las Vegas. Under the **Parameters** tab associated with the pie chart, the **Source** value for the City parameter is changed to the City prompt.

When the report is saved, users of the dashboard can see results for a country and multiple cities in that country.
