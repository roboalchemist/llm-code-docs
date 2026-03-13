# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/column/CurrencyColumn.md

# [CurrencyColumn](https://bryntum.com/docs/gantt/api/Grid/column/CurrencyColumn)

A column for showing/editing money values.

Example:

```
new Grid({
    columns : [
        {
            type     : 'currency',
            text     : 'Good Price in EUR',
            currency : 'EUR',
            field    : 'price'
        }
    ]
})
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[currency](https://bryntum.com/docs/gantt/api/Grid/column/CurrencyColumn#config-currency)
The currency to use for rendering values. Possible values are the ISO 4217 currency codes, such as "USD" for the US dollar (default).

[hideZeros](https://bryntum.com/docs/gantt/api/Grid/column/CurrencyColumn#config-hideZeros)
When `true` (default) then zero values (like `$0.00`) are not rendered. Provide `false` to render such values too.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isCurrencyColumn](https://bryntum.com/docs/gantt/api/Grid/column/CurrencyColumn#property-isCurrencyColumn)
Identifies an object as an instance of [CurrencyColumn](https://bryntum.com/docs/gantt/api/#Grid/column/CurrencyColumn) class, or subclass thereof.

[isCurrencyColumn](https://bryntum.com/docs/gantt/api/Grid/column/CurrencyColumn#property-isCurrencyColumn-static)
Identifies an object as an instance of [CurrencyColumn](https://bryntum.com/docs/gantt/api/#Grid/column/CurrencyColumn) class, or subclass thereof.

[currency](https://bryntum.com/docs/gantt/api/Grid/column/CurrencyColumn#property-currency)
The currency to use for rendering values. Possible values are the ISO 4217 currency codes, such as "USD" for the US dollar (default).

[hideZeros](https://bryntum.com/docs/gantt/api/Grid/column/CurrencyColumn#property-hideZeros)
When `true` (default) then zero values (like `$0.00`) are not rendered. Provide `false` to render such values too.
