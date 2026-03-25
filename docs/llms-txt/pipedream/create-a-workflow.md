# Source: https://pipedream.com/docs/rest-api/api-reference/workflows/create-a-workflow.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a Workflow

<Tip>
  This endpoint is only available when using [user API keys](/rest-api/auth/#user-api-keys), not yet for workspace [OAuth tokens](/rest-api/auth/#oauth).
</Tip>

Creates a new workflow within an organization’s project. This endpoint allows defining workflow steps, triggers, and settings, based on a supplied template.

#### Endpoint

```
POST /workflows
```

#### Request Body

<ParamField body="org_id" type="string" required>
  [Switch to your workspace’s context](/workspaces/#switching-between-workspaces) and [find your org’s ID](/workspaces/#finding-your-workspaces-id).
</ParamField>

***

<ParamField body="project_id" type="string" required>
  The ID of the project where the new workflow will be created. To find your project ID, switch to your desired workspace, and click on Projects in the top left of the Pipedream dashboard.

  Click on the project where you’d like to create the new workflow, and the project ID can be found in the URL, starting with `proj_`.

  If the URL is [https://pipedream.com/@pd-testing/projects/proj\_GzsRY5N/tree](https://pipedream.com/@pd-testing/projects/proj_GzsRY5N/tree), your `project_id` is `proj_GzsRY5N`.
</ParamField>

***

<ParamField body="template_id" type="string" required>
  The ID of the workflow template to base the workflow on. To find a workflow’s `template_id`, navigate to your workflow that you’d like to create a template for, and click “Create share link”. If the URL created is [https://pipedream.com/new?h=tch\_Vdfl0l](https://pipedream.com/new?h=tch_Vdfl0l), your `template_id` is `tch_Vdfl01`.
</ParamField>

***

<ParamField body="steps" type="array" required>
  Definitions of the steps to include in the workflow. Each item in the array represents a step, with its namespace and `props`.
</ParamField>

***

<ParamField body="triggers" type="array" required>
  Definitions of the triggers that will start the workflow. Each item in the array represents a trigger, with its type and `props`.
</ParamField>

***

<ParamField body="settings" type="object" required>
  Additional settings for the workflow, such as `name` and `auto_deploy`.
</ParamField>

<RequestExample>
  ```json  theme={null}
  {
    "project_id": "proj_wx9sgy",
    "org_id": "o_BYDI5y",
    "template_id": "tch_3BXfWO",
    "steps": [
      {
        "namespace": "code",
        "props": {
          "stringProp": "asdf"
        }
      },
      {
        "namespace": "keyauth_hello_world",
        "props": {
          "keyauth": {
            "authProvisionId": "apn_Nb6h9v"
          }
        }
      }
    ],
    "triggers": [
      {
        "props": {
          "oauth": {
            "authProvisionId": "apn_qZWh4A"
          },
          "string": "jkl"
        }
      }
    ],
    "settings": {
      "name": "example workflow name",
      "auto_deploy": true
    }
  }
  ```
</RequestExample>

<ResponseExample>
  ```json  theme={null}
  {
    "data": {
      "id": "p_48rCxZ",
      "name": "example workflow name",
      "active": true,
      "steps": [
        {
          "id": "c_bDf10L",
          "type": "CodeCell",
          "namespace": "code",
          "disabled": false,
          "code_raw": null,
          "codeRaw": null,
          "codeConfigJson": null,
          "lang": "nodejs20.x",
          "text_raw": null,
          "appConnections": [],
          "flat_params_visibility_json": null,
          "params_json": "{}",
          "component": true,
          "savedComponent": {
            "id": "sc_PRYiAZ",
            "code": "export default defineComponent({\n  props: {\n    stringProp: {\n      type: \"string\"\n    },\n    intProp: {\n      type: \"integer\",\n    }\n  },\n  async run({ steps, $ }) {\n    console.log(this.stringProp)\n    return steps.trigger.event\n  },\n})",
            "codeHash": "1908045950f3c1a861e538b20d70732adb701a81174dc59f809398e43f85d132",
            "configurableProps": [
              {
                "name": "stringProp",
                "type": "string"
              },
              {
                "name": "intProp",
                "type": "integer"
              }
            ],
            "key": null,
            "description": null,
            "entryPath": null,
            "version": "",
            "apps": []
          },
          "component_key": null,
          "component_owner_id": null,
          "configured_props_json": "{\"intProp\":5,\"stringProp\":\"asdf\"}",
          "authProvisionIdMap": {},
          "authProvisionIds": []
        },
        {
          "id": "c_W3f0YV",
          "type": "CodeCell",
          "namespace": "python",
          "disabled": false,
          "code_raw": null,
          "codeRaw": null,
          "codeConfigJson": null,
          "lang": "python3.12",
          "text_raw": null,
          "appConnections": [],
          "flat_params_visibility_json": null,
          "params_json": "{}",
          "component": true,
          "savedComponent": {
            "id": "sc_mweiWO",
            "code": "def handler(pd: \"pipedream\"):\n    # Reference data from previous steps\n    print(pd.steps[\"trigger\"][\"context\"][\"id\"])\n    # Return data for use in future steps\n    return {\"foo\": {\"test\": True}}\n",
            "codeHash": "63b32f00f1bc0b594e7a109cced4bda5011ab4420e358f743058dc46de8c5270",
            "configurableProps": [],
            "key": null,
            "description": null,
            "entryPath": null,
            "version": "",
            "apps": []
          },
          "component_key": null,
          "component_owner_id": null,
          "configured_props_json": null,
          "authProvisionIdMap": {},
          "authProvisionIds": []
        },
        {
          "id": "c_D7feVN",
          "type": "CodeCell",
          "namespace": "keyauth_hello_world",
          "disabled": false,
          "code_raw": null,
          "codeRaw": null,
          "codeConfigJson": null,
          "lang": "nodejs20.x",
          "text_raw": null,
          "appConnections": [],
          "flat_params_visibility_json": null,
          "params_json": "{}",
          "component": true,
          "savedComponent": {
            "id": "sc_71Li4l",
            "code": "const keyauth = {\n  type: \"app\",\n  app: \"keyauth\",\n  propDefinitions: {},\n}\n\nexport default {\n  name: \"Key auth hello world\",\n  version: \"0.0.1\",\n  key: \"keyauth-hello-world\",\n  type: \"action\",\n  description: \"simple hello world with dev keyauth app.\",\n  props: {\n    keyauth,\n  },\n  async run() {\n    console.log(\"hello world\")\n    return \"hello world\"\n  },\n}\n",
            "codeHash": "b7d5c6540f60e63174a96d5e5ba4aa89bf45b7b9d9fdc01db0ee64c905962415",
            "configurableProps": [
              {
                "name": "keyauth",
                "type": "app",
                "app": "keyauth"
              }
            ],
            "key": "keyauth-hello-world",
            "description": "simple hello world with dev keyauth app.",
            "entryPath": null,
            "version": "0.0.1",
            "apps": [
              {
                "appId": "app_1xohQx",
                "nameSlug": "keyauth",
                "authType": "keys"
              }
            ]
          },
          "component_key": "keyauth-hello-world",
          "component_owner_id": null,
          "configured_props_json": "{\"keyauth\":{\"authProvisionId\":\"apn_Nb6h9v\"}}",
          "authProvisionIdMap": {},
          "authProvisionIds": []
        }
      ],
      "triggers": [
        {
          "id": "hi_0R3HKG",
          "key": "eohq5aaq8yr4sye",
          "endpoint_url": "http://eojq5abv8yr4sye.m.d.pipedream.net",
          "custom_response": false,
          "created_at": 1707418403,
          "updated_at": 1707418403
        },
        {
          "id": "dc_rmXuv3",
          "owner_id": "o_BYDI5y",
          "component_id": "sc_PgliBJ",
          "configured_props": {},
          "active": true,
          "created_at": 1707241571,
          "updated_at": 1707241571,
          "name": "Emit hello world",
          "name_slug": "emit-hello-world-6"
        },
        {
          "id": "ti_aPxTPY",
          "interval_seconds": 3600,
          "cron": null,
          "timezone": "America/New_York",
          "schedule_changed_at": 1707418408,
          "created_at": 1707418404,
          "updated_at": 1707418404
        },
        {
          "id": "dc_5nvuPv",
          "owner_id": "o_BYDI5y",
          "component_id": "sc_XGBiLw",
          "configured_props": {
            "oauth": {
              "authProvisionId": "apn_qZWh4A"
            },
            "string": "jkl"
          },
          "active": true,
          "created_at": 1707418404,
          "updated_at": 1707418404,
          "name": "oauth-test-source",
          "name_slug": "oauth-test-source-3"
        },
        {
          "id": "ei_QbGT3D",
          "email_address": "em5tdwgfgbw9piv@upload.pipedream.net",
          "created_at": 1707418407,
          "updated_at": 1707418407
        }
      ]
    }
  }
  ```
</ResponseExample>

Built with [Mintlify](https://mintlify.com).
