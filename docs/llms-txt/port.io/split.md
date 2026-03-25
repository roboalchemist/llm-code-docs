# Source: https://docs.port.io/build-your-software-catalog/custom-integration/webhook/examples/split.md

# Split

In this example you are going to create a webhook integration between [Split](https://www.split.io/) and Port, which will ingest impressions.

## Port configuration[â](#port-configuration "Direct link to Port configuration")

Create the following blueprint definition:

Split impression blueprint

Create in Port

```
{
  "identifier": "splitImpression",
  "description": "Blueprint for Split Impressions",
  "title": "Split Impression",
  "icon": "Webhook",
  "schema": {
    "properties": {
      "key": {
        "icon": "DefaultProperty",
        "title": "Key",
        "description": "Key of the Impression",
        "type": "string"
      },
      "split": {
        "title": "Split name",
        "description": "Feature flag name",
        "type": "string",
        "icon": "DefaultProperty"
      },
      "environment_id": {
        "icon": "DefaultProperty",
        "title": "Environment Id",
        "type": "string",
        "description": "Environment Id where feature flag was evaluated"
      },
      "environment_name": {
        "icon": "DefaultProperty",
        "title": "Environment Name",
        "type": "string",
        "description": "Environment name"
      },
      "label": {
        "title": "Label",
        "description": "The rule that was applied to return a treatment",
        "type": "string"
      },
      "sdk": {
        "title": "sdk",
        "description": "SDK language that evaluated",
        "type": "string"
      },
      "sdk_version": {
        "title": "SDK Version",
        "type": "string",
        "description": "the SDK version"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {}
}
```

Create the following webhook configuration [using Port's UI](/build-your-software-catalog/custom-integration/webhook/.md?operation=ui#configuring-webhook-endpoints)

Split webhook configuration

1. **Basic details** tab - fill the following details:

   1. Title : `Split Mapper`;
   2. Identifier : `split_mapper`;
   3. Description : `A webhook configuration to map Splitio impressions to Port`;
   4. Icon : `Jenkins`;

2. **Integration configuration** tab - fill the following JQ mapping:

   ```
   [
     {
       "blueprint": "splitImpression",
       "itemsToParse": ".body",
       "entity": {
         "identifier": ".item.key + \"-\" + (.item.time | tostring)",
         "title": ".item.split",
         "properties": {
          "environment_id": ".item.environmentId",
          "environment_name": ".item.environmentName",
          "label": ".item.label",
          "sdk": ".item.sdk",
          "sdk_version": ".item.sdkVersion"
         }
       }
     }
   ]
   ```

3. Click **Save** at the bottom of the page.

## Create a webhook in Split[â](#create-a-webhook-in-split "Direct link to Create a webhook in Split")

1. Go to Admin Settings.
2. Click Integrations.
3. Select your workspace.
4. Click Add next to Outgoing Webhook (Impressions).
5. Check the environments where you would like data sent from.
6. Enter the value of the `url` key you received after creating the webhook configuration.
7. Click Save.

Done! any time an impression is triggered, the webhook will send the data to Port and create a new `split impression` entity

info

To see all available data for an impression, visit [Split's documentation](https://help.split.io/hc/en-us/articles/360020700232-Webhook-impressions)
