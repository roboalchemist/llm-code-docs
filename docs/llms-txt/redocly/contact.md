# Source: https://redocly.com/learn/openapi/openapi-visual-reference/contact.md

# `contact`

| Field Name | Type | Description |
|  --- | --- | --- |
| name | string | The identifying name of the contact person or organization. |
| url | string | The URL pointing to the contact information. |
| email | string | The email address of the contact person or organization. |


## Visuals

### `contact` example

The following example defines a contact object within the info object.


```yaml
info:
  title: Example
  version: ''
  description: |
    # My API description in Markdown

    This is a sample of an info description.
  contact:
    name: API team
    email: team@redocly.com
    url: https://redocly.com/contact-us/
```

![info contact](/assets/contact-1.94248b8cf308e851e605286d5f4f741c7841cfba6d902650497f066108acbd1a.6f948c6e.png)

## Types

- `Contact` (found in the [Info object](/learn/openapi/openapi-visual-reference/info))



```js
const Contact: NodeType = {
  properties: {
    name: { type: 'string' },
    url: { type: 'string' },
    email: { type: 'string' },
  },
};
```