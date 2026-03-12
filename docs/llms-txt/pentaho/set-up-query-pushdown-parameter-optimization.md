# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/optimize-a-pentaho-data-service/apply-a-query-pushdown-optimization/set-up-query-pushdown-parameter-optimization.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/optimize-a-pentaho-data-service/apply-a-query-pushdown-optimization/set-up-query-pushdown-parameter-optimization.md

# Set up query pushdown parameter optimization

To set up this optimization, complete these steps:

1. **Open the Data Service window**, then click the **Query Pushdown** tab.
2. Click the Plus Sign button near the **Parameters** label.
3. In the Create Parameter window add the name of an optimization parameter you created in the input step’s SQL query.
4. Click **OK**.
5. Select the step that contains the parameter from **Step Name**.
6. In the **Definitions** area of the window, enter the **Data Service Field** and the **Step Field** you want to parameterize.
   * The **Data Service Field** contains the transformation's name of the field you want to parameterize. The name should be as it appears in the transformation's output field. For example, you might have renamed the `cty` field from your data source to `country`. You would enter `country` in the **Data Service Field**.
   * The **Step Field** should contain the data source's name of the field you want to parameterize. For example, if you wanted to parameterize the `cty` field in a MySQL database, enter `cty` in the **Step Field**.
7. Optionally, you can click the **Get Optimizations** button to automatically generate input step optimizations based on the output fields for the step on which you have created the data service and input fields.
8. Click the **OK** button to save and close the window.
9. **Test the optimization**.
10. **Publish the Pentaho Data Service**.
