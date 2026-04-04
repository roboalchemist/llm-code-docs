# Source: https://developers.cash.app/cash-app-afterpay/guides/platforms/big-commerce/cash-app-afterpay-site-messaging.mdx

***

## stoplight-id: 1gtx76sipgzqy

# Cash App Afterpay Site Messaging

**How can I add Cash App Afterpay Site Messaging to my product and cart pages?**

***

<Note>Be careful, as these instructions need you to edit code. Before you make any changes to theme template files, back up your current theme customizations.</Note>
There are two types of theme platform on BigCommerce; [Stencil](#stencil-theme) and [Blueprint](#blueprint-theme).

Follow the instructions below according to which theme platform your store uses.

If you are not sure what platform is used by your store, see [Which Theme Platform do I have?](https://support.bigcommerce.com/s/article/Which-Theme-Platform-do-I-have).

## Stencil Theme

1. Go to *Storefront* › *Script Manager*

2. Click **Create a Script**.

3. Set up the following:

   * **Name of Script:** Cash App Afterpay Messaging
   * **Description:** Place Cash App Afterpay Site Messaging on product and cart pages
   * **Location on page:** Footer
   * **Select pages where script will be added:** Store pages
   * **Script category:** Essential
   * **Script type:** Script
   * **Load method:** Default

4. Copy and paste the below script into Script Contents:

```javascript Stencil
<!-- Begin Afterpay Stencil Snippet for BigCommerce v3.1.2 -->
<script>
{{#or (if page_type '===' 'product') (if page_type '===' 'cart')}}
    (function(){
        const supported = ["AUD", "NZD", "USD"];
        const currency = '{{currency_selector.active_currency_code}}';
        if (supported.indexOf(currency) > -1) {
            {{#if page_type '===' 'product'}}
                let targetSelector = '.productView .productView-price';
            {{#if product.price.with_tax}}
                let priceSelector = '.productView-price .price--withTax';
                let cachedAmount = '{{product.price.with_tax.value}}';
            {{else}}
                let priceSelector = '.productView-price .price--withoutTax';
                let cachedAmount = '{{product.price.without_tax.value}}';
            {{/if}}
            {{else if page_type '===' 'cart'}}
                let targetSelector = 'ul.cart-totals li.cart-total:last-child';
                let priceSelector = '.cart-total-grandTotal';
                let cachedAmount = '{{cart.grand_total.value}}';
            {{/if}}
                const locales = {
                    AUD: 'en_AU',
                    NZD: 'en_NZ',
                    USD: 'en_US',
                };
                const init = function(){
                    Afterpay.createPlacements({
                        targetSelector: targetSelector,
                        attributes: {
                            locale: locales[currency],
                            currency: currency,
                            amount: cachedAmount,
                        }
                    });
                };
                const script = document.createElement('script');
                script.src = "https://js.afterpay.com/afterpay-1.x.js";
                script.dataset.min = "1.00";
                script.dataset.max = "2000.00";
                script.onload = function () {
                    init();
                    setInterval(() => {
                        if (cachedAmount != document.querySelector(priceSelector).innerText) {
                           cachedAmount = document.querySelector(priceSelector).innerText;
                           if (document.querySelector('afterpay-placement')) {
                               document.querySelector('afterpay-placement').dataset.amount = cachedAmount;
                           } else {
                               init();
                           }
                        }
                    }, 400);
                };
                document.head.appendChild(script);
        }
    })();
{{/or}}
</script>
<!-- End Afterpay Stencil Snippet for BigCommerce v3.1.2 -->
```

You can modify the script so that the banner will only display a price breakdown if the product meets your order minimum and maximum thresholds.

To do so, you will need to edit the following values within the script and set the minimum and maximum values to mirror your Cash App Afterpay account settings:

`script.dataset.min = "1.00";`\
`script.dataset.max = "800.00";`

<Note>
  Banner not showing up?

  Sometimes the script may not work because the HTML elements are named differently depending on your theme. Work with your developer to help update the script depending on your theme.
</Note>

## Blueprint Theme

1. Access your themes template files by going to *Storefront* › *Template Files*.

2. Find the file *Panels/ProductDetails.html*.

3. Copy the script below and paste it into the *Panels/ProductDetails.html* file:

```javascript Blueprint
<!-- Begin Afterpay Blueprint Snippet for BigCommerce v2.0.2 -->
<afterpay-placement></afterpay-placement>
<script>
    (function(){
        const supported = ["AUD", "NZD", "USD"];
        const currency = '%%GLOBAL_CurrentCurrencyCode%%';
        if (supported.indexOf(currency) > -1) {
            let priceSelector = '.ProductDetailsGrid .VariationProductPrice';
            let cachedAmount = '%%GLOBAL_RawProductPrice%%';
            const locales = {
                AUD: 'en_AU',
                NZD: 'en_NZ',
                USD: 'en_US',
            };
            const placement = document.querySelector('afterpay-placement');
            placement.dataset.locale = locales[currency];
            placement.dataset.currency = currency;
            placement.dataset.amount = cachedAmount;
            const script = document.createElement('script');
            script.src = "https://js.afterpay.com/afterpay-1.x.js";
            script.dataset.min = "1.00";
            script.dataset.max = "2000.00";
            script.onload = function () {
                setInterval(() => {
                    if (cachedAmount != document.querySelector(priceSelector).innerText) {
                       cachedAmount = document.querySelector(priceSelector).innerText;
                       placement.dataset.amount = cachedAmount;
                    }
                }, 400);
            };
            document.head.appendChild(script);
        }
    })();
</script>
<!-- End Afterpay Blueprint Snippet for BigCommerce v2.0.2 -->
```

You should now see Cash App Afterpay's messaging underneath the price of products and the cart total.
