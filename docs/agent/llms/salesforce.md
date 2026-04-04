# Source: https://docs.agent.ai/recipes/salesforce.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Calling Agents from Salesforce (SFDC)

This guide walks you through integrating [Agent.ai](http://Agent.ai)'s intelligent agents directly within Salesforce without requiring external code. By setting up Named Credentials and creating a Flow with HTTP callouts, you'll enable your Salesforce instance to seamlessly communicate with [Agent.ai](http://Agent.ai)'s services. This integration allows your agents to respond to record creation events, process data from your Salesforce objects, and write results back to your records—all while maintaining the security and governance controls of your Salesforce environment. Follow these step-by-step instructions to set up this powerful integration in under 30 minutes.

## Before You Begin

Before setting up the Salesforce integration with [Agent.ai](http://Agent.ai), ensure you have:

**Tested Your Agent with cURL:**

Verify your [Agent.ai](http://Agent.ai) webhook is functional by testing it with cURL first. This confirms the endpoint is working and helps you understand the expected request/response format:

```bash  theme={null}
curl -L -X POST -H 'Content-Type: application/json' \
'https://api-lr.agent.ai/v1/agent/YOUR_AGENT_ID/webhook/YOUR_WEBHOOK_ID' \
-d '{"input_name":"Test User"}'
```

Save this cURL command and response for reference during setup.

1. **API Access in Salesforce**: Ensure the Salesforce users who will be configuring and using this integration have:
   * "API Enabled" permission
   * "Modify All Data" or appropriate object-level permissions
   * Access to create and modify Flows
   * Permission to create Named Credentials
2. **Required Information**:
   * Your complete [Agent.ai](http://Agent.ai) webhook URL
   * The expected request payload structure
   * The response format from your agent
   * Salesforce fields you want to use for input/output
3. **Salesforce Edition**: Confirm you're using a Salesforce edition that supports Named Credentials and Flows (Enterprise, Unlimited, Developer, or Performance).

Taking these preparatory steps will significantly streamline the integration process and help avoid common setup issues.

## Creating Credentials

### **1. Create External Credentials**

1. Navigate to Setup → Named Credentials → External Credentials (Tab) → New
2. Fill in the required fields (remember: Name must NOT contain spaces)
3. Select **No Authentication** from the dropdown
4. Save your settings

### **2. Create Named Credentials**

1. Navigate to **Setup → Named Credentials → Named Credentials (Tab) → New**
2. Complete the form with:
   * Label: A descriptive name (e.g., "AgentAI Named Credential")
   * Name: Same as label without spaces
   * URL: Your [Agent.ai](http://Agent.ai) endpoint (e.g., "[<u>https://api-lr.agent.ai</u>](https://api-lr.agent.ai)")
   * Enable "Enabled for Callouts"
   * Select your External Credential from the dropdown
   * Check "Generate Authorization Header"
   * Set Outbound Network Connection to "--None--"
   * Save your settings

### **3. Create Principal for Named Credentials**

1. Navigate to **Setup → Named Credentials → "AgentAI External Credential" → Principals → New**
2. Complete the form:
   * Parameter Name: A descriptive name
   * Sequence Number: 1
   * Identity Type: "Named Principal"
   * Save your settings

### **4. Create a Permission Set for External Credentials**

1. Navigate to **Setup → Permission Sets → New**
2. Enter permission set details:
   * Label: "AgentAI External Credentials Permissions"
   * API Name: Should auto-populate
   * Save your settings

### **5. Assign Permissions**

1. Navigate to Setup → Permission Sets → "AgentAI External Credentials Permissions" → Manage Assignments
2. Click **Add Assignment**
3. Select users who need access
4. Click **Next** (no expiration date needed)
5. Click **Assign**

### **6. Manage Permissions in Permission Set**

1. Navigate to **Setup → Permission Sets → "AgentAI External Credentials Permissions" → External Credential Principal Access**
2. Click **Edit**
3. Enable the Credential Principal
4. Save your settings
5. *Verify your configuration*

## Creating The Flow

### **1. Create Record Triggered Flow**

1. Navigate to **Setup → Flows → New Flow**
2. Select **Record Triggered Flow**
3. Choose **When A Record Is Created**
4. Set to optimize for "Action and Related Records"
5. Check "Include a Run Asynchronously path to access an external system after the original transaction for the triggering record is successfully committed"

### **2. Create HTTP Callout Action**

1. Click **Add Element**
2. Select **Action**
3. Find and select **Create HTTP Callout** (scroll to the bottom of the list)

### **3. Create External Service**

* Give your service a name (alphanumeric values only)

  **Note:** Use version names if creating multiple services
* Select your Named Credential from the dropdown
* Save your settings

### **4. Create Invokable Action**

1. Set Method to **POST**
2. Enter URL Path to your Agent webhook endpoint
   * Example: /v1/agent/kkmiv48izo6wo7fk/webhook/b45b7a8e
3. For Sample JSON Request, copy from your webhook example:
   * Example: `{"input_name":"REPLACE_ME"}`
4. Ignore any error that appears
5. Click **Review**
6. Confirm data structure is detected (input\_name as String)
7. Click **Connect for Schema**
8. Click **Connect**
9. Review return types match what your Agent returns
10. Name the Action for your external service

### **6. Assign Body Payload Parameters**

1. Click **Assign → Set Variable Values**
2. Select data to pass to agent:
   * Variable: agentRequestBody > input\_name
   * Operator: Equals
   * Value: Choose your field (e.g., Triggering Lead > First Name)
3. Save your settings

### **7. Save and Refresh The Page**

1. Save your flow to update the UI with new values

### **8. Set Up Response Handling**

1. Select the **Flow Action → Show Advanced Options → Store Output Values**
2. For 2XX responses, create a new resource
3. For Default Exception, create a new resource (Text type)
4. For Response Code, create a new resource (Number, 0 decimal places)
5. Save to finalize resource names

### **9. Assign Values from API Call to Objects**

1. After the HTTP Request Action, create an Assignment
2. Update the triggering record:
   * **Field:** The field you want to update (e.g., Greeting\_Phrase\_\_c)
   * **Value:** responseBodyOut2XX > response
3. **Note:** responseBodyOut2XX contains all output objects from your Agent

### **10. Test Your Flow**

1. Save your flow
2. Click **Debug**
3. Select **Run Asynchronously**
4. Select a record to test with
5. Run the flow and verify the results

## Debug Checklist

Use this checklist to troubleshoot if your [Agent.ai](http://Agent.ai) integration isn't working properly:

* **External Credentials**: Verify name contains no spaces and "No Authentication" is selected
* **Named Credentials**: Confirm URL is correct and "Enabled for Callouts" is checked
* **Principal**: Check that Principal is created with correct sequence number
* **Permission Set**: Ensure External Credential Principal is enabled
* **User Assignments**: Confirm relevant users have the permission set assigned
* **Flow Trigger**: Verify flow is set to trigger on the correct object and event
* **HTTP Callout**: Check that the webhook URL path is correct
* **Request Body**: Confirm input parameters match what your Agent expects (e.g., "input\_name")
* **Response Handling**: Ensure output variables are correctly mapped
* **Field Updates**: Verify targeted fields exist and are accessible for updates
* **Asynchronous Execution**: Confirm "Include to Run Asynchronously" is checked
* **External Service**: Check Named Credential is properly selected in External Service
* **Flow Activation**: Make sure the flow is activated after testing
* **Agent Webhook**: Verify your [Agent.ai](http://Agent.ai) webhook endpoint is active and responding
* **SFDC Logs**: Review debug logs for any callout errors

If issues persist, check your SFDC debug logs for specific error messages and verify that your [Agent.ai](http://Agent.ai) webhook is responding as expected with proper formatting.

## Conclusion

Congratulations! You've successfully integrated [Agent.ai](http://Agent.ai) with Salesforce using native SFDC capabilities, eliminating the need for middleware or custom code. This integration creates a powerful automation pipeline that leverages AI agents to enhance your Salesforce experience. As records are created in your system, they now automatically trigger intelligent processing through your [Agent.ai](http://Agent.ai) webhooks, with results flowing seamlessly back into your Salesforce records. This approach maintains Salesforce's security model while expanding its capabilities with [Agent.ai](http://Agent.ai)'s intelligence.

Consider extending this implementation by creating additional flows for different record types, implementing decision branches based on agent responses, or adding more complex data transformations. As you grow comfortable with this integration, you can enhance it to support increasingly sophisticated business processes, bringing the power of [Agent.ai](http://Agent.ai) to all aspects of your Salesforce implementation. Remember to monitor your usage and performance to ensure optimal operation as your integration scales.
