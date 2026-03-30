# Source: https://docs.axonius.com/docs/creating-a-generic-webhook-event.md

# Creating a Generic Webhook Event

The Generic Webhook Event enables you to connect a Workflow to any external service that sends data via a webhook, providing flexibility to trigger automations based on custom events from your unique tools and systems.

If a needed event isn't available in your Workflow, you can create a custom one using the **Create Generic Webhook Event** wizard.

The **Create Generic Webhook Event** wizard guides you through these steps:

* **General** - Assign a name for the Event and enter a Private Secure Key. The system automatically generates a unique, non-configurable webhook URL for the Event.

* **Schema** - Paste or upload a JSON schema to define the expected structure of your payloads. Generic Event schemas support complex and nested fields of all types (nested JSON objects or arrays) and any number of nesting layers. The system automatically parses a valid schema and displays a preview of the Output Fields, which helps with data mapping.

* **Asset Mapping** - Map incoming event data fields to Axonius asset fields for accurate identification. This action allows the Event to retrieve data for the selected asset type.

**To create a Generic Webhook Event**

1. In the **Trigger Type** pane (for triggering Events) or the **Event** pane (for non-triggering Events), click **Create Generic Webhook Event**.
2. In the **General** step (1) that opens, configure these basic webhook details and click  **Next**.
   * **Name** - Enter a name for your Generic Webhook Event.
   * **Private secure key (X-API-Key)** - Enter a secure key for authentication.
3. In the  **Schema** step (2) that opens, in the **JSON schema** box, paste or upload a JSON schema to define the expected structure of your payloads, and then click  **Next**.
   1. If the schema entered is valid, the system automatically parses it and displays a preview of the **Output Fields**, which helps with data mapping.
4. In the **Asset Mapping** step (3) that opens, map incoming Event data fields to Axonius asset fields for accurate asset identification and retrieval.
   1. In the **Module** dropdown, choose the asset type (e.g., Devices, Users) for which the Event should retrieve data.
   2. Fill in the query to map incoming Event data to a specific Axonius asset field (e.g., matching the Event's *user.email* field to an Axonius User's *email* field).
   3. Ensure Assets are returned: Your mapping must successfully return assets. An Event that does not return assets will not trigger the Workflow (as there are no assets for the Workflow to run on).
   4. Click **+ Add asset** to map an additional asset, if your Workflow requires it.
5. Click **Create Generic Event**.
   * A toast notification confirms that the Event has been successfully created.
   * The newly created Event appears in the **Trigger Type** or **Event** pane under **Generic Webhook Events**.