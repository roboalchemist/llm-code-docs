# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/troubleshooting-ael-cp/errors-when-using-hive-and-ael-on-an-amazon-emr-cluster-ael-troubleshooting/transformation-does-not-complete-execution-hive-and-ael-on-emr-ael-troubleshooting.md

# Transformation does not complete execution

If you are using the Hive 2/3 connector with both the Table Input step and the Table Output step in the same transformation, your transformation does not complete its execution.

To resolve this issue, split the original transformation into two new transforms where one contains the Table Input step and other contains the Table Output step. You can control the order of execution with a PDI job. If you try to use a child transformation to control the execution order, the same issue occurs.

See **Using Table input and Table output steps with AEL for managed tablles in Hive** in the **Pentaho Data Integration** document for further instructions.
