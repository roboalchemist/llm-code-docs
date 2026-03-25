# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers/variables/kettle-variables/set-the-lazy_repository-variable-in-the-pdi-client.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers/variables/kettle-variables/set-the-lazy_repository-variable-in-the-pdi-client.md

# Set the LAZY\_REPOSITORY variable in the PDI client

This variable restores the directory-loading behavior of the repository to be as it was before Pentaho 6.1. To set the **LAZY\_REPOSITORY** variable in the PDI client, complete these steps.

**Note:** Changing this variable to `false` will make repository loading more expensive.

1. Open the PDI client, then select **Edit** > **Edit the kettle.properties file**.
2. Look for **KETTLE\_LAZY\_REPOSITORY** and, if it is set to `false`, change the value to `true`.
3. Click **OK** and close the PDI client.
