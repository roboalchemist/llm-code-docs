# Source: https://docs.intelligems.io/developer-resources/advanced-settings.md

# Advanced Settings

{% hint style="danger" %}
The advanced settings are located in the Settings page of the Intelligems App. If you do not see this in your app, please reach out to our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) to receive access to this section of the settings page.
{% endhint %}

## Intercept ATC XHR[​](https://docs.intelligems.io/docs/advanced-settings/#intercept-atc-xhr)

By default, this is turned on to correctly change your prices using checkout scripts. When a user presses 'Add to Cart' with this setting on, the XHR script sent from the site to Shopify is intercepted and modified by Intelligems before sending to Shopify.

## Currency Format[​](https://docs.intelligems.io/docs/advanced-settings/#currency-format)

Specifies format for how currencies are displayed on your website. When editing this field, make sure to press 'Validate' before pressing Save Configurations.

### **Currency Format Structure:**

```json
{
    "options": {
      "localeMatcher": "string",
      "style": "string",
      "currency": "string",
      "currencyDisplay": "string",
      "currencySign": "string",
      "useGrouping": boolean,
      "minimumIntegerDigits": number,
      "minimumFractionDigits": number,
      "maximumFractionDigits": number,
      "minimumSignificantDigits": number,
      "maximumSignificantDigits": number,
    }, 
    "symbol": "string",
    "suffix": "string",
    "removeTrailingZeros": boolean,
}
```

### **Currency Format Example**

```json
{
    "options": {
        "minimumFractionDigits": 0,
    }, 
  "symbol": "$",
  "suffix": " USD",
}
```

See documentation [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat) for more information on the options object.

## Currency Function[​](https://docs.intelligems.io/docs/advanced-settings/#currency-function)

Specifies which currency function to use when adding our prices to your site. If you use a standard formatMoney function in your window\.theme object (i.e. window\.theme.Currency.formatMoney), you can insert that into this field like this: window\.theme.Currency.formatMoney. You can also create a custom formatMoney function in your theme.liquid file.

## **Custom Currency Function**

```html
<head>
    ...
    <script>
        try {
          window.igCurrencyFn = (price) => {
            let code = "USD";
            const value = `; ${document.cookie}`;
            const parts = value.split(`; cart_currency=`);
            if (parts.length === 2) {
              code = parts.pop().split(";").shift();
            }
    
            const formatter = new Intl.NumberFormat("en-US", {
              style: "currency",
              currency: code,
            });
    
            return `<span class=money>${formatter.format(price/100)} ${code} </span>`;
          };
        } catch (error) {
          console.log(error);
        }
    </script>
    ...
</head>
```

\\
