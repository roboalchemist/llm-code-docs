# Source: https://docs.apidog.com/x-apidog-orders-1981688m0.md

# x-apidog-orders

## Usage

Used to control the ordering of various fields within an `object` type, allowing for customization of the field sequence in JSON data structures.

## Example

```json
{
    "properties": {
        "id": { 
            "type": "string"
        },
        "name": {
            "type": "string"
        },
    },
    "x-apidog-orders": [ // Field ordering, used for display
        "id",
        "name"
    ]
}
```
