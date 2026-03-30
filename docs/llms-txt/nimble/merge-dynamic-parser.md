# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/data-parsing/merge-dynamic-parser.md

# Merge Dynamic Parser

## Merge Dynamic Parsers&#x20;

The "Merge Dynamics" feature in Nimble's Web API provides users with the ability to seamlessly integrate Nimble's AI-powered parsing with custom parsing logic into a single, unified response.&#x20;

This feature is particularly useful for advanced use cases where the out-of-the-box AI parsing might need further refinement, customization, or additional context provided by user-defined parsing rules. By combining both AI and custom parsing, users can achieve a more accurate and tailored data extraction process.

### **Benefits**

* **Enhanced Flexibility**: Users can extend and customize the default AI parsing to meet specific data requirements, ensuring that all necessary information is captured in one go.
* **Unified Output**: The merging of AI and custom parsing ensures that the final output is consistent, organized, and ready for further processing or analysis.
* **Improved Accuracy**: By adding custom parsing, users can refine the data extraction process to capture niche or specialized information that might be missed by general AI parsing.

## Request Options

<table><thead><tr><th width="189">Parameter</th><th width="265">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>parser</code></td><td>Required as <code>true</code> (default = <code>false</code>)</td><td>Enum: <code>true</code> | <code>false</code><br>True - the page's content will be parsed and returned in a JSON format. <br>False - Response will include page headers and raw data (without parsing). </td></tr><tr><td><code>parse_options</code></td><td>Required to enable merge dynamic feature</td><td>Object | For advanced parsing options such as merge_dynamic</td></tr><tr><td><code>parse_options.merge_dynamic</code></td><td>Required as <code>true</code> (default = <code>false</code>)</td><td>Bool |  when set to true, the custom parser results would merge into the AI parsing results under new entity named <code>DynamicEntity</code></td></tr><tr><td><code>parser</code></td><td>Required</td><td>Object | The custom parser template to be merge</td></tr></tbody></table>

#### Example Request

{% tabs %}
{% tab title="cURL" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/web' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.yelp.com/biz/7-eleven-pembroke-pines-7",
    "country": "US",
    "parse": true,
    "render": true,
    "parse_options": {
        "merge_dynamic": true
    },
    "parser": {
        "YelpBusiness": {
            "selectors": ["html"],
            "type": "object-list",
            "fields": {
                "business_id": {
                    "selectors": [
                        "meta[name='yelp-biz-id']"
                    ],
                    "extractor": "[content]"
                }
            }
        }
    }
}'
```

{% endtab %}
{% endtabs %}

#### Example Response

* The merged results of the custom parser could be found under `DynamicEntity` entity

```json
{
    ...
    "parsing":
    {
        "entities":
        {
            "BreadcrumbList": [...],
            "DynamicEntity":
            [
                {
                    "YelpBusiness":
                    [
                        {
                            "business_id": "Z6VUesj0B7wJX3_yqKKPgA"
                        }
                    ],
                    "entity_type": "Dynamic"
                }
            ],
            "ItemList": [...],
            "LocalBusiness": [...]
        },
        "total_entities_count": 6,
        "entities_count":
        {
            "BreadcrumbList": 3,
            "DynamicEntity": 1,
            "ItemList": 1,
            "LocalBusiness": 1
        },
        "metrics":
        {}
    }
}
```
