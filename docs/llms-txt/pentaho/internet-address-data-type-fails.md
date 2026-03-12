# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/troubleshooting-ael-cp/internet-address-data-type-fails.md

# Internet Address data type fails

When running an AEL transformation using an input step with the data type 'Internet Address' selected for a URL field, your transformation may not complete properly.

When you are using the Spark engine to run an AEL transformation, do not use the data type 'Internet Address' when entering a URL in a step. Instead, use the data type 'String' for the URL.
