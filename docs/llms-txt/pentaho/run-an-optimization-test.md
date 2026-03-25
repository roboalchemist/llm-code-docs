# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/test-a-pentaho-data-service/run-an-optimization-test.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/test-a-pentaho-data-service/run-an-optimization-test.md

# Run an optimization test

If you have [added an optimization](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Advanced%20Pentaho%20Data%20Integration%20topics/Advanced%20topics%20\(Pentaho%20Data%20Integration%20overview\)/Pentaho%20Data%20Services/Optimize%20a%20Pentaho%20Data%20Service=GUID-E041CF99-CE82-400A-BB2F-75325C079593=4=en=.md) of your data service, you will need to test it. First, follow the instructions in [Run a basic test](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/test-a-pentaho-data-service/run-a-basic-test) section, and then modify your query in the SQL area to pass a parameter for the optimization, as shown in the following example:

```sql
SELECT * FROM Mars WHERE rover=’Curiosity’

```

* To preview the optimization click **Preview Optimization** in the Test Data Service window.
* Use [Examine test results](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/test-a-pentaho-data-service/examine-test-results) instructions to help you interpret your test results.
