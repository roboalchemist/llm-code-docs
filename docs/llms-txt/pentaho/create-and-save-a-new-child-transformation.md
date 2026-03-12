# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/kinesis-consumer/general/create-and-save-a-new-child-transformation.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/kafka-consumer/general/create-and-save-a-new-child-transformation.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/jms-consumer/general-jms-consumer/create-and-save-a-new-child-transformation.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/kinesis-consumer/general/create-and-save-a-new-child-transformation.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/kafka-consumer/general/create-and-save-a-new-child-transformation.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/jms-consumer/general-jms-consumer/create-and-save-a-new-child-transformation.md

# Create and save a new child transformation

If you do not already have a child transformation, you can create one while setting up the JMS Consumer step. When you click the **New** button, a new child transformation will automatically generate the required Get Records from Stream step in a new canvas tab. All your fields and types are customized in the child transformation's Get Records from Stream step to match the fields and types specified in the **Fields** tab of the parent JMS Consumer step.

1. In the JMS Consumer step, click **New**.

   The Save As dialog box appears.
2. Navigate to the location where you want to save your new child transformation, then type in the file name.
3. Click **Save**.

   A notification box displays informing you that the child transformation has been created and opened in a new tab. If you do not want to see this notification in the future, select the **Don't show me this again** check box.
4. Click the new transformation tab to view and edit the child transformation.

   It automatically contains the Get Records from Stream step. Optionally, you can continue to build this transformation and save it.
5. When finished, return to the JMS Consumer step.
