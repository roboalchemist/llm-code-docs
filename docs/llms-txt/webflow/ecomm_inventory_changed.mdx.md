# Source: https://developers.webflow.com/data/v1.0.0/reference/ecomm_inventory_changed.mdx

***

title: Inventory Changed
slug: data/reference/ecomm\_inventory\_changed
description: The information about the inventory item that changed
hidden: false
-------------

## Trigger Type

`ecomm_inventory_changed `

## Properties

| Field            | Type   | Description                                                |
| :--------------- | :----- | :--------------------------------------------------------- |
| `_id `           | string | Unique identifier for a SKU item                           |
| `quantity `      | number | Total quantity of items remaining in inventory (if finite) |
| `inventoryType ` | string | infinite or finite                                         |

## Example

```json
{
    "_id": "5bfedb42bab0ad90fa7dad39",
    "quantity": 83,
    "inventoryType": "finite"
}
```
