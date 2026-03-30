# Source: https://learn.microsoft.com/en-us/power-automate/manage-flows-with-code

Title: Work with cloud flows using code - Power Automate

URL Source: https://learn.microsoft.com/en-us/power-automate/manage-flows-with-code

Published Time: Fri, 10 Oct 2025 05:19:20 GMT

Markdown Content:
All flows are stored in Dataverse and you can use either the Dataverse SDK for .NET or Web API to manage them.

This article covers the management of flows included on the **Solutions** tab in Power Automate. Currently, managing flows under **My Flows** aren't supported with code.

Dataverse provides equivalent capabilities using either the Dataverse SDK for .NET or Web API.

The best method depends on the project technology and the skills you have.

*   [SDK for .NET](https://learn.microsoft.com/en-us/power-automate/manage-flows-with-code#tabpanel_1_sdk)
*   [Web API](https://learn.microsoft.com/en-us/power-automate/manage-flows-with-code#tabpanel_1_webapi)

If your project uses .NET, we recommend using the SDK. The SDK simplifies your development experience by providing a typed object model and methods to authenticate.

More information: [Use the Organization service](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/org-service/overview)

How to connect depends on whether you're using the Dataverse SDK for .NET or Web API.

Cloud flows are stored in the [Process (Workflow) table](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/reference/entities/workflow) that is represented in the Web API as the [workflow EntityType](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/reference/workflow)

The following table describes important columns in the workflow table:

| Logical Name | Type | Description |
| --- | --- | --- |
| `category` | Choice | The category of the flow. Here are the different categories. `0` - Classic Dataverse workflows. `1` - Classic Dataverse dialogs. `2` - Business rules. `3` - Classic Dataverse actions. `4` - Business process flows. `5` - Modern Flow (Automated, instant or scheduled flows). `6` - Desktop flows. |
| `clientdata` | String | A string-encoded JSON of the flow definition and its connectionReferences. |
| `createdby` | Lookup | The user who created the flow. |
| `createdon` | DateTime | The date when the flow was created. |
| `description` | String | The user-provided description of the flow. |
| `ismanaged` | Bool | Indicates if the flow was installed via a managed solution. |
| `modifiedby` | Lookup | The last user who updated the flow. |
| `modifiedon` | DateTime | The last time the flow was updated. |
| `name` | String | The display name that you gave the flow. |
| `ownerid` | Lookup | The user or team who owns the flow. |
| `statecode` | Choice | The status of the flow. The status can be: `0` - Draft (Off) `1` - Activated (On) `2` - Suspended. |
| `type` | Choice | Indicates if the flow is a running flow, or a template that can be used to create more flows. `1` - Definition, `2` - Activation `3` - Template. |
| `workflowid` | Guid | The unique identifier for a cloud flow across all imports. |
| `workflowidunique` | Guid | The unique identifier for this installation of the flow. |

Note

With Web API, Lookup values are [single-valued navigation properties](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/web-api-navigation-properties#single-valued-navigation-properties) that can be expanded to get details from the related record.

Lookup columns also have corresponding GUID [lookup properties](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/web-api-properties#lookup-properties) that can be used in queries. Lookup properties have this naming convention: `_<logical name>_value`. For the workflow entitytype in Web API you can reference these lookup properties: `_createdby_value`, `_modifiedby_value`, and `_ownerid_value`.

To retrieve a list of cloud flows, you can query the workflow table. The following query returns the first automated, instant, or scheduled flow that is currently 'on':

*   [SDK for .NET](https://learn.microsoft.com/en-us/power-automate/manage-flows-with-code#tabpanel_3_sdk)
*   [Web API](https://learn.microsoft.com/en-us/power-automate/manage-flows-with-code#tabpanel_3_webapi)

This static `OutputFirstActiveFlow` method requires an authenticated client that implements the [IOrganizationService](https://learn.microsoft.com/en-us/dotnet/api/microsoft.xrm.sdk.iorganizationservice). It uses the [IOrganizationService.RetrieveMultiple](https://learn.microsoft.com/en-us/dotnet/api/microsoft.xrm.sdk.iorganizationservice.retrievemultiple) method.

```
/// <summary>
/// Outputs the first active flow
/// </summary>
/// <param name="service">Authenticated client implementing the IOrganizationService interface</param>
public static void OutputFirstActiveFlow(IOrganizationService service)
{
   var query = new QueryExpression("workflow")
   {
         ColumnSet = new ColumnSet("category",
                                    "createdby",
                                    "createdon",
                                    "description",
                                    "ismanaged",
                                    "modifiedby",
                                    "modifiedon",
                                    "name",
                                    "ownerid",
                                    "statecode",
                                    "type",
                                    "workflowid",
                                    "workflowidunique"),
         Criteria = new FilterExpression(LogicalOperator.And)
         {
            Conditions = {
            {  new ConditionExpression(
               "category",
                     ConditionOperator.Equal,
                     5) }, // Cloud Flow
            {  new ConditionExpression(
                     "statecode",
                     ConditionOperator.Equal,
                     1) } // Active
         }
         },
         TopCount = 1 // Limit to one record
   };

   EntityCollection workflows = service.RetrieveMultiple(query);

   Entity workflow = workflows.Entities.FirstOrDefault();

   Console.WriteLine($"category: {workflow.FormattedValues["category"]}");
   Console.WriteLine($"createdby: {workflow.FormattedValues["createdby"]}");
   Console.WriteLine($"createdon: {workflow.FormattedValues["createdon"]}");
   // Description may be null
   Console.WriteLine($"description: {workflow.GetAttributeValue<string>("description")}");
   Console.WriteLine($"ismanaged: {workflow.FormattedValues["ismanaged"]}");
   Console.WriteLine($"modifiedby: {workflow.FormattedValues["modifiedby"]}");
   Console.WriteLine($"modifiedon: {workflow.FormattedValues["modifiedon"]}");
   Console.WriteLine($"name: {workflow["name"]}");
   Console.WriteLine($"ownerid: {workflow.FormattedValues["ownerid"]}");
   Console.WriteLine($"statecode: {workflow.FormattedValues["statecode"]}");
   Console.WriteLine($"type: {workflow.FormattedValues["type"]}");
   Console.WriteLine($"workflowid: {workflow["workflowid"]}");
   Console.WriteLine($"workflowidunique: {workflow["workflowidunique"]}");
}
```

To retrieve more records, remove the [TopCount](https://learn.microsoft.com/en-us/dotnet/api/microsoft.xrm.sdk.query.queryexpression.topcount#microsoft-xrm-sdk-query-queryexpression-topcount) limit.

**Output**

```
category: Modern Flow
createdby: SYSTEM
createdon: 5/20/2020 9:37 PM
description:
ismanaged: Unmanaged
modifiedby: Kiana Anderson
modifiedon: 5/6/2023 3:37 AM
name: When an account is updated -> Create a new record
ownerid: Monica Thomson
statecode: Activated
type: Definition
workflowid: d9e875bf-1c9b-ea11-a811-000d3a122b89
workflowidunique: c17af45c-10a1-43ca-b816-d9cc352718cf
```

More information:

*   [Build queries with QueryExpression](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/org-service/build-queries-with-queryexpression)
*   [Access formatted values](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/org-service/entity-operations-query-data#access-formatted-values)

The required properties for automated, instant, and scheduled flows are: `category`, `name`, `type`, `primaryentity`, and `clientdata`. Use `none` for the `primaryentity` for these types of flows.

*   [SDK for .NET](https://learn.microsoft.com/en-us/power-automate/manage-flows-with-code#tabpanel_4_sdk)
*   [Web API](https://learn.microsoft.com/en-us/power-automate/manage-flows-with-code#tabpanel_4_webapi)

This static method requires an authenticated client that implements the [IOrganizationService](https://learn.microsoft.com/en-us/dotnet/api/microsoft.xrm.sdk.iorganizationservice). It uses the [IOrganizationService.Create](https://learn.microsoft.com/en-us/dotnet/api/microsoft.xrm.sdk.iorganizationservice.create) method.

```
/// <summary>
/// Creates a cloud flow
/// </summary>
/// <param name="service">Authenticated client implementing the IOrganizationService interface</param>
/// <returns>The workflowid</returns>
public static Guid CreateCloudFlow(IOrganizationService service)
{
   var workflow = new Entity("workflow")
   {
         Attributes = {
            {"category", new OptionSetValue(5) }, // Cloud flow
            {"name", "Sample flow name"},
            {"type", new OptionSetValue(1) }, //Definition
            {"description", "This flow reads some data from Dataverse." },
            {"primaryentity", "none" },
            {"clientdata", "{\"properties\":{\"connectionReferences\":{\"shared_commondataserviceforapps\":{\"impersonation\":{},\"runtimeSource\":\"embedded\",\"connection\":{\"name\":\"shared-commondataser-114efb88-a991-40c7-b75f-2693-b1ca6a0c\",\"connectionReferenceLogicalName\":\"crdcb_sharedcommondataserviceforapps_109ea\"},\"api\":{\"name\":\"shared_commondataserviceforapps\"}}},\"definition\":{\"$schema\":\"https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#\",\"contentVersion\":\"1.0.0.0\",\"parameters\":{\"$connections\":{\"defaultValue\":{},\"type\":\"Object\"},\"$authentication\":{\"defaultValue\":{},\"type\":\"SecureObject\"}},\"triggers\":{\"manual\":{\"metadata\":{\"operationMetadataId\":\"76f87a86-89b3-48b4-92a2-1b74539894a6\"},\"type\":\"Request\",\"kind\":\"Button\",\"inputs\":{\"schema\":{\"type\":\"object\",\"properties\":{},\"required\":[]}}}},\"actions\":{\"List_rows\":{\"runAfter\":{},\"metadata\":{\"operationMetadataId\":\"9725b30f-4a8e-4695-b6fd-9a4985808809\"},\"type\":\"OpenApiConnection\",\"inputs\":{\"host\":{\"apiId\":\"/providers/Microsoft.PowerApps/apis/shared_commondataserviceforapps\",\"connectionName\":\"shared_commondataserviceforapps\",\"operationId\":\"ListRecords\"},\"parameters\":{\"entityName\":\"accounts\",\"$select\":\"name\",\"$top\":1},\"authentication\":\"@parameters('$authentication')\"}}}}},\"schemaVersion\":\"1.0.0.0\"}" }
         }
   };

   return service.Create(workflow);
}
```

More information: [Create table rows using the Organization Service](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/org-service/entity-operations-create)

The `statecode` of all flows created this way are set to `0` (Draft or 'Off'). The flow needs to be enabled before it can be used.

The most important property is the `clientdata`, which contains the `connectionReferences` that the flow uses, and the [definition](https://learn.microsoft.com/en-us/azure/logic-apps/logic-apps-workflow-definition-language) of the flow. The `connectionReferences` are the mappings to each connection that the flow uses.

```
{
  "properties": {
    "connectionReferences": {
      "shared_commondataserviceforapps": {
        "runtimeSource": "embedded",
        "connection": {},
        "api": { 
         "name": "shared_commondataserviceforapps" 
         }
      }
    },
    "definition": {
      "$schema": "https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#",
      "contentVersion": "1.0.0.0",
      "parameters": {
        "$connections": { "defaultValue": {}, "type": "Object" },
        "$authentication": { "defaultValue": {}, "type": "SecureObject" }
      },
      "triggers": {
        "manual": {
          "metadata": {},
          "type": "Request",
          "kind": "Button",
          "inputs": {
            "schema": { "type": "object", "properties": {}, "required": [] }
          }
        }
      },
      "actions": {
        "List_rows": {
          "runAfter": {},
          "metadata": {},
          "type": "OpenApiConnection",
          "inputs": {
            "host": {
              "apiId": "/providers/Microsoft.PowerApps/apis/shared_commondataserviceforapps",
              "connectionName": "shared_commondataserviceforapps",
              "operationId": "ListRecords"
            },
            "parameters": {
              "entityName": "accounts",
              "$select": "name",
              "$top": 1
            },
            "authentication": "@parameters('$authentication')"
          }
        }
      }
    }
  },
  "schemaVersion": "1.0.0.0"
}
```

To update a flow, set only the properties you want to change.

*   [SDK for .NET](https://learn.microsoft.com/en-us/power-automate/manage-flows-with-code#tabpanel_5_sdk)
*   [Web API](https://learn.microsoft.com/en-us/power-automate/manage-flows-with-code#tabpanel_5_webapi)

This static method requires an authenticated client that implements the [IOrganizationService](https://learn.microsoft.com/en-us/dotnet/api/microsoft.xrm.sdk.iorganizationservice). It uses the [IOrganizationService.Update](https://learn.microsoft.com/en-us/dotnet/api/microsoft.xrm.sdk.iorganizationservice.update) method to update a flow description and set the owner.

```
/// <summary>
/// Updates a cloud flow
/// </summary>
/// <param name="service">Authenticated client implementing the IOrganizationService interface</param>
/// <param name="workflowid">The ID of the flow to update.</param>
/// <param name="systemuserid">The id of the user to assign the flow to.</param>
public static void UpdateCloudFlow(IOrganizationService service, Guid workflowid, Guid systemuserid) {

   var workflow = new Entity("workflow",workflowid)
   {
         Attributes = {

            {"description", "This flow will ensure consistency across systems." },
            {"ownerid", new EntityReference("systemuser",systemuserid)},
            {"statecode", new OptionSetValue(1) } //Turn on the flow.
         }
   };

   service.Update(workflow);
}
```

More information: [Update and delete table rows using the Organization Service > Basic update](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)

The following examples show how to delete the workflow record that represents a cloud flow.

*   [SDK for .NET](https://learn.microsoft.com/en-us/power-automate/manage-flows-with-code#tabpanel_6_sdk)
*   [Web API](https://learn.microsoft.com/en-us/power-automate/manage-flows-with-code#tabpanel_6_webapi)

The static `DeleteCloudFlow` method deletes a workflow record.

```
/// <summary>
/// Deletes a workflow
/// </summary>
/// <param name="service">Authenticated client implementing the IOrganizationService interface</param>
/// <param name="workflowId">The id of the cloud flow to delete.</param>
public static void DeleteCloudFlow(IOrganizationService service, Guid workflowId) { 

service.Delete(entityName:"workflow",id: workflowId);

}
```

More information: [Delete a record using the SDK](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/org-service/entity-operations-update-delete?tabs=late#delete)

Use the `RetrieveSharedPrincipalsAndAccess` message to get a list of all the users that a cloud flow is shared with.

With the SDK, use the [RetrieveSharedPrincipalsAndAccessRequest Class](https://learn.microsoft.com/en-us/dotnet/api/microsoft.crm.sdk.messages.retrievesharedprincipalsandaccessrequest), and with the Web API use the [RetrieveSharedPrincipalsAndAccess Function](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/reference/retrievesharedprincipalsandaccess).

More information: [Get principals with access to a record](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/security-access-coding#get-principals-with-access-to-a-record)

Share a cloud flow like any other Dataverse record using the `GrantAccess` message. With the SDK, use the [GrantAccessRequest Class](https://learn.microsoft.com/en-us/dotnet/api/microsoft.crm.sdk.messages.grantaccessrequest) and with the Web API use the [GrantAccess Action](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/reference/grantaccess). More information: [GrantAccess example](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/security-sharing-assigning#grantaccess-example)

If you want to change the access rights you grant when you share a record, use the `ModifyAccess` message. With the SDK, use the [ModifyAccessRequest Class](https://learn.microsoft.com/en-us/dotnet/api/microsoft.crm.sdk.messages.modifyaccessrequest) and with the Web API use the [ModifyAccess Action](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/reference/modifyaccess). More information: [ModifyAccess example](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/security-sharing-assigning#modifyaccess-example)

To unshare a record, use the `RevokeAccess` message. With the SDK, use the [RevokeAccessRequest Class](https://learn.microsoft.com/en-us/dotnet/api/microsoft.crm.sdk.messages.revokeaccessrequest) and with the Web API use the [RevokeAccess Action](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/reference/revokeaccess). More information: [Revoking access](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/security-sharing-assigning#revoking-access)

When a flow is part of a solution, you can export it by exporting the solution that contains the flow using the `ExportSolution` message.

*   [SDK for .NET](https://learn.microsoft.com/en-us/power-automate/manage-flows-with-code#tabpanel_7_sdk)
*   [Web API](https://learn.microsoft.com/en-us/power-automate/manage-flows-with-code#tabpanel_7_webapi)

The following static `ExportSolution` example method uses the [ExportSolutionRequest](https://learn.microsoft.com/en-us/dotnet/api/microsoft.crm.sdk.messages.exportsolutionrequest) to retrieve a `byte[]` containing the ZIP file of the unmanaged solution with the specified [UniqueName](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/reference/entities/solution#BKMK_UniqueName).

```
/// <summary>
/// Exports an unmanaged solution
/// </summary>
/// <param name="service">Authenticated client implementing the IOrganizationService interface</param>
/// <param name="solutionUniqueName">The uniquename of the solution.</param>
/// <returns></returns>
public static byte[] ExportSolution(
   IOrganizationService service, 
   string solutionUniqueName) 
{
   ExportSolutionRequest request = new() { 
         SolutionName = solutionUniqueName,
         Managed = false
   };

   var response = (ExportSolutionResponse)service.Execute(request);

   return response.ExportSolutionFile;
}
```

When you have a solution ZIP file, you can import it using the `ImportSolution` message.

When you import flows, you should set the following parameters:

| Property name | Description |
| --- | --- |
| `OverwriteUnmanagedCustomizations` | If there are existing instances of these flows in Dataverse, this flag needs to be set to `true` to import them. Otherwise they aren't overwritten. |
| `PublishWorkflows` | Indicates if classic Dataverse workflows are activated on import. This setting doesn't apply to other types of flows. |
| `CustomizationFile` | A base 64-encoded zip file that contains the solution. |

*   [SDK for .NET](https://learn.microsoft.com/en-us/power-automate/manage-flows-with-code#tabpanel_8_sdk)
*   [Web API](https://learn.microsoft.com/en-us/power-automate/manage-flows-with-code#tabpanel_8_webapi)

The static `ImportSolution` sample method shows how to import a solution file using the [ImportSolutionRequest Class](https://learn.microsoft.com/en-us/dotnet/api/microsoft.crm.sdk.messages.importsolutionrequest)

```
/// <summary>
/// Imports a solution.
/// </summary>
/// <param name="service">Authenticated client implementing the IOrganizationService interface</param>
/// <param name="solutionFile">The byte[] data representing a solution file. </param>
public static void ImportSolution(
   IOrganizationService service, 
   byte[] solutionFile) {

   ImportSolutionRequest request = new() { 
         OverwriteUnmanagedCustomizations = true,
         CustomizationFile = solutionFile
   };

   service.Execute(request);
}
```

The API at **api.flow.microsoft.com** isn't supported. Customers should instead use the Dataverse Web APIs for Power Automate documented previously in this article.

Alternatively, customers can use the management connectors: [Power Automate Management](https://learn.microsoft.com/en-us/connectors/flowmanagement/) or [Power Automate for Admins](https://learn.microsoft.com/en-us/connectors/microsoftflowforadmins/).

Customers can use the unsupported APIs at `api.flow.microsoft.com` at their own risk. These APIs are subject to change, so breaking changes could occur.

[Entity class operations using the Organization service](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/org-service/entity-operations)

[Perform operations using the Web API](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/perform-operations-web-api)

[Sharing and assigning](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/security-sharing-assigning)

[Verifying access in code](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/security-access-coding)

[Work with solutions using the Dataverse SDK](https://learn.microsoft.com/en-us/power-platform/alm/solution-api)
