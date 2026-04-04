# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/optimize-a-pentaho-data-service/apply-a-parameter-pushdown-optimization/set-up-parameter-pushdown-optimization.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/optimize-a-pentaho-data-service/apply-a-parameter-pushdown-optimization/set-up-parameter-pushdown-optimization.md

# Set up parameter pushdown optimization

Perform the following steps to set up the parameter pushdown optimization:

1. [Open the Data Service window](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/open-or-edit-a-pentaho-data-service), then click the **Parameter Pushdown** tab.
2. In the **WHERE Clause Column**, click in a cell and enter the Data Service Field name from the existing fields listed. The Data Service Field name is the virtual table field name in your `WHERE` clause. Press ENTER. Possible values are defaulted for **Transformation Parameter** and **Value Format**.
3. Adjust the name of the **Transformation Parameter** as needed. The name is something that you create; it must be unique in the data service. Type the name in the **Transformation Parameter** field or in the window transformation properties. (The parameter is created in the transformation properties or is something you specify in a field).
4. If needed, add a prefix or suffix to the default `%s` in **Value Format** field. For example, if you want to format a value, consider using `[value]=%s`. In most cases, the default `%s` is sufficient formatting.
5. Save the optimization and exit the window by clicking **OK**.
6. [Run an optimization test](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/test-a-pentaho-data-service/run-an-optimization-test).
7. [Publish a Pentaho Data Service](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/publish-a-pentaho-data-service).
