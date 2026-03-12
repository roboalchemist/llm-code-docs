# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/optimize-a-pentaho-data-service/apply-a-parameter-pushdown-optimization/add-the-parameter-pushdown-parameter-to-the-step.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/optimize-a-pentaho-data-service/apply-a-parameter-pushdown-optimization/add-the-parameter-pushdown-parameter-to-the-step.md

# Add the parameter pushdown parameter to the step

Perform the following steps to add a parameter that will limit an input step (such as REST Client) in some way:

1. [Create a transformation](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/create-a-transformation).
2. [Run your transformation](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/run-your-transformation) to ensure it executes properly.
3. Add the parameter you want to optimize to one of the steps. Typically, you would want to specify the parameter in a JSON or REST Client step. If you use a filtered step, you would need to use the Get Variables step before the filtered step.
4. Click the **OK** button.
5. [Set up parameter pushdown optimization](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/optimize-a-pentaho-data-service/apply-a-parameter-pushdown-optimization/set-up-parameter-pushdown-optimization).
