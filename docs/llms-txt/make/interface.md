# Source: https://developers.make.com/custom-apps-documentation/component-blocks/interface.md

# Source: https://developers.make.com/custom-apps-documentation/best-practices/output-parameters/interface.md

# Interface

The interface describes the structure of output bundles and specifies the parameters seen in the mapping modal. It should contain the full response from the API, including nested parameters.

You can generate an interface using our [Interface Generator](https://developers.make.com/custom-apps-documentation/component-blocks/interface#interface-generator).

## Dynamic interface according to user-defined fields

Retrieving all fields from the endpoint could be difficult, especially when integrating an ERP or other business-related backend that has hundreds of fields.

The solution to this varies across different platforms, but they are similar.

One method is to use a `select` parameter to retrieve only the fields that you need. For example, [Open Data Protocol (OData)](https://www.odata.org/getting-started/basic-tutorial/#select).

{% tabs %}
{% tab title="Source" %}

```javascript
GET serviceRoot/Airports?$select=Name,IcaoCode

{
    "@odata.context": "serviceRoot/$metadata#Airports(Name,IcaoCode)",
    "value": [
        {
            "@odata.id": "serviceRoot/Airports('KSFO')",
            "@odata.editLink": "serviceRoot/Airports('KSFO')",
            "Name": "San Francisco International Airport",
            "IcaoCode": "KSFO"
        },
        ......
    ]
}

```

{% hint style="info" %}
With `Name` and `IcaoCode` as the only output, adjust the interface to indicate to users that only these fields are available for mapping.
{% endhint %}
{% endtab %}
{% endtabs %}
