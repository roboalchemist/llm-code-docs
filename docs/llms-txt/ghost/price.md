# Source: https://docs.ghost.org/themes/helpers/data/price.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# price

> Usage: `{{price plan}}`

***

The `{{price}}` helper formats monetary values from their smallest denomination to a human readable denomination with currency formatting. Example:

```handlebars  theme={"dark"}
{{price plan}}
```

This will output `$5`.

The `{{price}}` helper accepts a number of optional attributes:

* `currency` - defaults to `plan.currency` when passed a `plan` object
* `locale` - defaults to `@site.locale`
* `numberFormat` - defaults to “short”, and can be either “short” (\$5) or “long” (\$5.00)
* `currencyFormat` - defaults to “symbol” and can be one of “symbol” (\$5), “code” (EUR 5) or “name” (5 euros)

`{{price}}` can be used with static values as well, `{{price 4200}}` will output `42`.

The default behaviour of the `price` helper is the same as:

```handlebars  theme={"dark"}
{{price plan.amount
  currency=plan.currency
  locale=@site.locale
  numberFormat="short"
  currencyFormat="symbol"
}}
```

Passing a `currency` without a price will output the symbol for that currency:

```handlebars  theme={"dark"}
{{price currency="USD"}} <!-- Outputs: $ -->
```

### Example Code

Outputting prices for all tiers.

```handlebars  theme={"dark"}
{{#get "tiers" include="monthly_price,yearly_price,benefits" limit="100" as |tiers|}}
    {{! Loop through our tiers collection }}
    {{#foreach tiers}}
        {{#if monthly_price}}
            <div>
                <a href="javascript:" data-portal="signup/{{id}}/monthly">Monthly – {{price monthly_price currency=currency}}</a>
            </div>
        {{/if}}
          {{#if yearly_price}}
            <div>
                <a href="javascript:" data-portal="signup/{{id}}/monthly">Monthly – {{price yearly_price currency=currency}}</a>
            </div>
        {{/if}}

    {{/foreach}}
{{/get}}
```

Outputting prices for a member’s subscriptions.

```html  theme={"dark"}
<!-- account.hbs -->

{{#foreach @member.subscriptions}}
  <div class="subscription">
    <label class="subscriber-detail-label">Your plan</label>
    <span class="subscriber-detail-content">{{price plan}}/{{plan.interval}}</span>
  </div>
{{/foreach}}
```


Built with [Mintlify](https://mintlify.com).