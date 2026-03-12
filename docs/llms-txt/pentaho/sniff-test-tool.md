# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring/monitor-performance/sniff-test-tool.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring/monitor-performance/sniff-test-tool.md

# Sniff Test tool

The Sniff Test displays data as it travels from one step to another in the stream. The Sniff Test is designed to be used as a supplement to logs so that you can debug complex situations.

**Note:** Applying a Sniff Test slows transformation run speed, so use with care.

To use this, complete these steps:

1. Right-click a step in the transformation as it runs.
2. Select **Sniff Test During Execution**.

   There are three options in this menu:

   * **Sniff test input rows** - Shows the data inputted into the step.
   * **Sniff test output rows** - Shows the data outputted from the step.
   * **Sniff test error handling** - Shows error handling data.

After you have selected an option, values in the data stream appear. You are also able to observe throughput.
