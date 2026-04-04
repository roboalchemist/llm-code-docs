# Custom Style for Payment Wall

**Important:** PayPal Plus for Mexico is not available for new integrations. PayPal provides this documentation to support existing integrations.

For PayPal Plus for Brazil, see the [Brazilian integration](/docs/regional/br/) guide.

To create a customized payment form experience that matches existing styles and layout, merchants can pass a set of specified CSS selectors and their respective attributes in the form of a JSON string.

## Available CSS selectors

The following selectors are optional and can be passed based on requirement, and only specific attributes can be modified.

| CSS selector | Applicable element(s) in payment wall | Supported attributes |
| --- | --- | --- |
| pppTextInput | Credit Card Input: - FirstName - LastName - CVV | - background color - color - border-color - border-width - font-size - font-family - font-style |
| pppDropdown | - Expiry Date dropdown button - Installments dropdown button upon hover | - background color - color - border-color - border-width - font-size - font-family - font-style |
| pppDropdownHover | - Expiry Date dropdown button - Installments dropdown button upon hover | - background color - color - border-color - border-width - font-size - font-family - font-style |
| pppDropdownMenu | - Expiry Date dropdown button - Installments dropdown button upon hover | - background color - color - border-color - min-width |
| pppLabel | - Expiry label - CVV label | - color - font-size - font-family - font-style |
| pppCheckboxLabel | Labels present beside checkboxes | - color - font-size - font-family - font-style |
| pppAlertMessage | Warning message div | - background color - color - border-color - border-width - font-size - font-family - font-style |
| pppErrorFields | Error message div | border-color |

## Attribute Values

The attributes defined above accept the following values. Any invalid or unaccepted values will result in schema validation errors.

| CSS attribute | Accepted values |
| --- | --- |
| - background-color | Any valid HEX pair, short HEX, RBG, or color name. For example, - #ff0000 - #f00 - rgb(255, 0, 0) - red |
| - border-color | Any valid HEX pair, short HEX, RBG, or color name. For example, - #ff0000 - #f00 - rgb(255, 0, 0) - red |
| - color | Any valid HEX pair, short HEX, RBG, or color name. For example, - #ff0000 - #f00 - rgb(255, 0, 0) - red |
| - border-width | Any valid HEX pair, short HEX, RBG, or color name. For example, - #ff0000 - #f00 - rgb(255, 0, 0) - red |
| - font-size | Any size in these ranges: - 12-16px - 0.75-1.0em |
| - font-family | - Arial - Helvetica - Times New Roman - Times - Courier New - Courier - Sans Serif |
| - font-style | - normal - italic |
| - border-width | Any valid HEX pair, short HEX, RBG, or color name. For example, - #ff0000 - #f00 - rgb(255, 0, 0) - red |