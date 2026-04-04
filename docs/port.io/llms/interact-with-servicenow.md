# Source: https://docs.port.io/guides/all/interact-with-servicenow.md

# Interact with ServiceNow records

This guide demonstrates how to implement self-service actions that interact with any ServiceNow record and delete ServiceNow incidents directly from Port using **synced webhooks**.

## Use cases[â](#use-cases "Direct link to Use cases")

* Provide developers and managers with safe, self-serve CRUD operations on ServiceNow records.
* Automate table record creation, updates, or removal as part of CI/CD or maintenance workflows.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* Complete the [onboarding process](/getting-started/overview.md).
* Access to your ServiceNow account with permissions to manage records in relevant tables.

## Implementation[â](#implementation "Direct link to Implementation")

To enable interaction with ServiceNow from Port, we will configure four self-service actions:

1. Create a ServiceNow record
2. Update a ServiceNow record
3. Delete a ServiceNow record
4. Delete a ServiceNow incident

These actions use Portâs **synced webhooks** to communicate with ServiceNowâs REST API and rely on Port's **secret manager** to securely store authentication credentials.

### Add Port secrets[â](#add-port-secrets "Direct link to Add Port secrets")

To add a secret to your portal:

1. Click on the `...` button in the top right corner of your Port application.

2. Click on **Credentials**.

3. Click on the `Secrets` tab.

4. Click on `+ Secret` and add the following secrets:

   * `SERVICENOW_INSTANCE_URL` - The ServiceNow instance URL. For example <https://example-id.service-now.com>.

   * `SERVICENOW_API_TOKEN`: A base64 encoded string of your servicenow instance credentials generated as:

     ```
     echo -n "your-instance-username:your-instance-password" | base64
     ```

### Set up self-service action[â](#set-up-self-service-action "Direct link to Set up self-service action")

The following steps will walk you through configuring each self-service action, starting with creating a record, then updating, and finally deleting it from ServiceNow.

#### Create a ServiceNow record[â](#create-a-servicenow-record "Direct link to Create a ServiceNow record")

1. Head to the [self-service](https://app.getport.io/self-serve) page.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Create a ServiceNow record (Click to expand)**

   Create in Port

   ```
   {
       "identifier": "create_servicenow_record",
       "title": "Create ServiceNow Record",
       "icon": "Servicenow",
       "description": "Create a new record in a specified table in ServiceNow using a JSON payload",
       "trigger": {
           "type": "self-service",
           "operation": "CREATE",
           "userInputs": {
           "properties": {
               "table_name": {
               "icon": "DefaultProperty",
               "type": "string",
               "title": "Table Name",
               "description": "Name of the table in ServiceNow"
               },
               "request_body": {
               "type": "object",
               "title": "Request Body ",
               "description": "JSON payload for the new record. The payload must follow the table schema in ServiceNow"
               }
           },
           "required": [
               "request_body",
               "table_name"
           ],
           "order": [
               "table_name",
               "request_body"
           ]
           }
       },
       "invocationMethod": {
           "type": "WEBHOOK",
           "url": "{{.secrets.SERVICENOW_INSTANCE_URL}}/api/now/table/{{.inputs.table_name}}",
           "agent": false,
           "synchronized": true,
           "method": "POST",
           "headers": {
           "RUN_ID": "{{ .run.id }}",
           "Content-Type": "application/json",
           "Accept": "application/json",
           "Authorization": "Basic {{.secrets.SERVICENOW_API_TOKEN}}"
           },
           "body": {
           "{{ spreadValue() }}": "{{ .inputs.request_body }}"
           }
       },
       "requiredApproval": false
   }
   ```

5. Click `Save`.

Now you should see the `Create ServiceNow Record` action in the [self-service](https://app.getport.io/self-serve) page. ð

#### Update a ServiceNow record[â](#update-a-servicenow-record "Direct link to Update a ServiceNow record")

1. Head to the [self-service](https://app.getport.io/self-serve) page.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Update a ServiceNow record (Click to expand)**

   Create in Port

   ```
   {
       "identifier": "update_service_now_record",
       "title": "Update ServiceNow Record",
       "icon": "Servicenow",
       "description": "Update an existing record in a specified table in ServiceNow based on system ID and a JSON payload",
       "trigger": {
           "type": "self-service",
           "operation": "DAY-2",
           "userInputs": {
           "properties": {
               "table_name": {
               "type": "string",
               "title": "Table Name",
               "description": "Name of the table in ServiceNow"
               },
               "request_body": {
               "type": "object",
               "title": "Request Body ",
               "description": "JSON payload containing the fields and values to update in the record. Must follow the table schema in ServiceNow"
               },
               "system_id": {
               "type": "string",
               "title": "System ID",
               "description": "Globally Unique ID (GUID) of the record in ServiceNow"
               }
           },
           "required": [
               "table_name",
               "request_body",
               "system_id"
           ],
           "order": [
               "table_name",
               "system_id",
               "request_body"
           ]
           }
       },
       "invocationMethod": {
           "type": "WEBHOOK",
           "url": "{{.secrets.SERVICENOW_INSTANCE_URL}}/api/now/table/{{.inputs.table_name}}/{{.inputs.system_id}}",
           "agent": false,
           "synchronized": true,
           "method": "PATCH",
           "headers": {
           "RUN_ID": "{{ .run.id }}",
           "Content-Type": "application/json",
           "Accept": "application/json",
           "Authorization": "Basic {{.secrets.SERVICENOW_API_TOKEN}}"
           },
           "body": {
           "{{ spreadValue() }}": "{{ .inputs.request_body }}"
           }
       },
       "requiredApproval": false
   }
   ```

5. Click `Save`.

Now you should see the `Update ServiceNow Record` action in the [self-service](https://app.getport.io/self-serve) page. ð

#### Delete a ServiceNow record[â](#delete-a-servicenow-record "Direct link to Delete a ServiceNow record")

1. Head to the [self-service](https://app.getport.io/self-serve) page.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Delete a ServiceNow record (Click to expand)**

   Create in Port

   ```
   {
       "identifier": "delete_service_now_record",
       "title": "Delete ServiceNow Record",
       "icon": "Servicenow",
       "description": "Delete a record based on system ID from a specified table in ServiceNow",
       "trigger": {
           "type": "self-service",
           "operation": "DELETE",
           "userInputs": {
           "properties": {
               "table_name": {
               "icon": "DefaultProperty",
               "type": "string",
               "title": "Table Name",
               "description": "Name of the table in ServiceNow"
               },
               "system_id": {
               "type": "string",
               "title": "System ID",
               "description": "Globally Unique ID (GUID) of the record in ServiceNow"
               }
           },
           "required": [
               "system_id",
               "table_name"
           ],
           "order": [
               "table_name",
               "system_id"
           ]
           }
       },
       "invocationMethod": {
           "type": "WEBHOOK",
           "url": "{{.secrets.SERVICENOW_INSTANCE_URL}}/api/now/table/{{.inputs.table_name}}/{{.inputs.system_id}}",
           "agent": false,
           "synchronized": true,
           "method": "DELETE",
           "headers": {
           "RUN_ID": "{{ .run.id }}",
           "Content-Type": "application/json",
           "Accept": "application/json",
           "Authorization": "Basic {{.secrets.SERVICENOW_API_TOKEN}}"
           },
           "body": {}
       },
       "requiredApproval": false
   }
   ```

5. Click `Save`.

Now you should see the `Delete ServiceNow Record` action in the [self-service](https://app.getport.io/self-serve) page. ð

#### Delete a ServiceNow incident[â](#delete-a-servicenow-incident "Direct link to Delete a ServiceNow incident")

1. Head to the [self-service](https://app.getport.io/self-serve) page.

2. Click on the `+ New Action` button.

3. Click on the `{...} Edit JSON` button.

4. Copy and paste the following JSON configuration into the editor.

   **Delete ServiceNow Incident (Click to expand)**

   Create in Port

   ```
   {
       "identifier": "delect_servicenow_incident",
       "title": "Delect ServiceNow Incident",
       "icon": "Servicenow",
       "description": "Deletes an incident from the ServiceNow incident table using a unique system ID",
       "trigger": {
           "type": "self-service",
           "operation": "DELETE",
           "userInputs": {
           "properties": {},
           "required": [],
           "order": []
           },
           "blueprintIdentifier": "servicenowIncident"
       },
       "invocationMethod": {
           "type": "WEBHOOK",
           "url": "{{.secrets.SERVICENOW_INSTANCE_URL}}/api/now/table/incident/{{.entity.identifier}}",
           "agent": false,
           "synchronized": true,
           "method": "DELETE",
           "headers": {
           "RUN_ID": "{{ .run.id }}",
           "Content-Type": "application/json",
           "Accept": "application/json",
           "Authorization": "Basic {{.secrets.SERVICENOW_API_TOKEN}}"
           },
           "body": {}
       },
       "requiredApproval": false
   }
   ```

5. Click `Save`.

Now you should see the `Delect ServiceNow Incident` action in the [self-service](https://app.getport.io/self-serve) page. ð

#### Create an automation to remove entity from Port

Once the incident is deleted from ServiceNow, we want to automatically remove the corresponding entity in Port. To achieve this behaviour:

1. Head to the [automations](https://app.getport.io/settings/automations) page.

2. Click on the `+ Automation` button.

3. Copy and paste the following JSON configuration into the editor.

   **Delete ServiceNow incident in Port automation (Click to expand)**

   Create in Port

   ```
   {
       "identifier": "servicenow_incident_delete_sync_status",
       "title": "Remove Deleted Incident from Port",
       "description": "Removes the deleted entity in Port when after it is deleted from ServiceNow",
       "trigger": {
           "type": "automation",
           "event": {
           "type": "RUN_UPDATED",
           "actionIdentifier": "delect_servicenow_incident"
           },
           "condition": {
           "type": "JQ",
           "expressions": [
               ".diff.after.status == \"SUCCESS\""
           ],
           "combinator": "and"
           }
       },
       "invocationMethod": {
           "type": "WEBHOOK",
           "url": "https://api.port.io/v1/blueprints/{{.event.diff.after.blueprint.identifier}}/entities/{{.event.diff.after.entity.identifier}}",
           "agent": false,
           "synchronized": true,
           "method": "DELETE",
           "headers": {
           "RUN_ID": "{{.event.diff.after.id}}",
           "Content-Type": "application/json",
           "Accept": "application/json"
           },
           "body": {}
       },
       "publish": true
   }
   ```

4. Click `Save`.

Now, whenever a user runs the `Delete ServiceNow Incident` action:

1. The incident is deleted directly from ServiceNow via webhook.
2. The corresponding entity in Port is automatically removed, keeping your catalog clean and consistent.
