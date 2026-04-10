# Source: https://developers.kit.com/plugins/component-library/dynamic-select-input.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Dynamic select input

The dynamic select input provides creators with a dropdown menu containing options fetched dynamically from your server. This component is specifically designed for filtering media gallery results in real-time. When a creator selects an option, it triggers a new request to refresh the media results based on the selected filter value.

<img width="300" alt="example dynamic select input" src="https://mintcdn.com/kit-314e57c1/ohR8KbVxvspIDffR/images/plugins/components/dynamic_select_input.png?fit=max&auto=format&n=ohR8KbVxvspIDffR&q=85&s=e079301bc39faed0c1cd6451799c6215" data-path="images/plugins/components/dynamic_select_input.png" />

<Note>
  Fields cannot be dependent on dynamic select inputs as they are only available for the media source, that has restricted component functionality. Check the [media source documentation](/plugins/media-source/plugin-settings) for more details.
</Note>

## Compatibility

| Plugin type    | Availability                 | Additional notes                                                                                                                                          |
| -------------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Content blocks | <Icon icon="square-xmark" /> |                                                                                                                                                           |
| Media source   | <Icon icon="square-check" /> | Available as part of the preset `filter` group functionality. Check [media source documentation](/plugins/media-source/plugin-settings) for more details. |

## Request URL behaviour

Kit makes POST requests to your `request_url` in the following scenarios:

* **Initial load**: Request to populate the dropdown options when the plugin loads
* **Filter selection**: Request with the selected value to return filtered media results

Your endpoint should return an array of label-value pairs for the dropdown options:

```json  theme={null}
{
  "options": [
    {
      "label": "Home",
      "value": "home"
    },
    {
      "label": "Favorites", 
      "value": "favorites"
    },
    {
      "label": "Shared",
      "value": "shared"
    }
  ]
}
```

## Properties

<ParamField body="type" type="string" required="true">
  `dynamicSelect` - the type of the component
</ParamField>

<ParamField body="name" type="string" required="true">
  A unique internal-only identifier that is posted to an app's plugin server to share values inputted by the creator
</ParamField>

<ParamField body="label" type="string" required="true">
  Creator-facing identifier that is shown in the plugin environment
</ParamField>

<ParamField body="request_url" type="string" required="true">
  The endpoint URL that Kit will call to fetch dynamic options and handle filter selections
</ParamField>

<ParamField body="required" type="boolean">
  Determines whether the creator must make a selection before proceeding
</ParamField>

<RequestExample>
  ```json JSON setting theme={null}
    {
      "type": "group",
      "name": "filter_group",
      "settings": [
        {
          "type": "dynamicSelect",
          "label": "Folders",
          "name": "folder",
          "request_url": "https://example-plugin.com/folders",
          "required": false
        }
      ]
    }
  ```
</RequestExample>

<ResponseExample>
  ```json Example response theme={null}
    {
      "settings": {
        "folder": "favorites"
        // ...additional plugin settings
      }
      // ...plugin-specific additional data
    }
  ```
</ResponseExample>


Built with [Mintlify](https://mintlify.com).