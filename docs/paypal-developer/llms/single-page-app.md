# PayPal payments with single-page applications

Use this guide if your integration uses a single-page application to accept payments, built on a library or framework such as React, Vue, or Angular.

## Know before you code

### PayPal Checkout
This feature modifies an existing PayPal Checkout integration and uses the following:

- [JavaScript SDK:](/sdk/js/) Adds PayPal-supported payment methods.
- [Orders REST API:](/docs/api/orders/v2/) Create, update, retrieve, authorize, and capture orders.

### You need a developer account to get sandbox credentials
PayPal uses the following REST API credentials, which you can get from the developer dashboard:

- Client ID : Authenticates your account with PayPal and identifies an app in your sandbox.
- Client secret : Authorizes an app in your sandbox. Keep this secret safe and don't share it.

### Explore PayPal APIs with Postman
You can use Postman to explore and test PayPal APIs. Learn more in our [Postman guide](/api/rest/postman).

The JavaScript SDK shows your payer's available payment methods on your checkout page.

Set up the PayPal checkout for your application by using the JavaScript SDK and handling the payer's interactions with the PayPal checkout button. Place the following script tag in your index.html page based on how you plan to render payment buttons, so the paypal object is available when you need it in the checkout flow. You can render the payment buttons either immediately, or after user action, navigation, or other page change:

### Sample request for Immediate

#### **`Sample request for Immediate `**

```javascript
<script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID">
</script>
```

### Sample request for On change

#### **`Sample request for On change`**

```javascript
<script defer src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID">
</script>
```

### Modify the code

Copy the sample request and modify it as follows:

- Copy the sample JavaScript SDK code and paste it into your checkout page.
- In the SDK code, replace YOUR_CLIENT_ID with your client ID.
- Pass parameters to replace default values, such as USD for currency. To learn more about the default values, see the [JavaScript SDK script configuration](https://developer.paypal.com/sdk/js/configuration/).

**info**
Note: This sample code is optimized for JavaScript performance. To learn more about how to optimize the JavaScript SDK, see [JavaScript SDK performance optimization](/sdk/js/performance/).

## Add JavaScript SDK

### React sample request

```javascript
const PayPalButton = paypal.Buttons.driver("react", {
    React,
    ReactDOM
});
```

### Angular sample request

```javascript
paypal.Buttons.driver("angular", window.angular);
```

### Angular 2 sample request

```javascript
paypal.Buttons.driver("angular2", ng.core);
```

### Vue

```javascript
paypal.Buttons.driver("vue", window.Vue);
```

## Choose your JavaScript library or framework

- React.
- Angular
- Angular 2
- Angular 2 using TypeScript
- Vue

## React

The React samples are separated into a component implementation and a functional implementation.

### Component implementation

```javascript
import React from "react";
import ReactDOM from "react-dom"
const PayPalButton = paypal.Buttons.driver("react", {
    React,
    ReactDOM
});
class YourComponent extends React.Component {
    createOrder(data) {
        // Order is created on the server and the order id is returned
        return fetch("/my-server/create-paypal-order", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": "Bearer ACCESS-TOKEN",
                    "PayPal-Partner-Attribution-Id": "BN-CODE",
                    "PayPal-Auth-Assertion": "AUTH-ASSERTION-JWT",
                },
                // use the "body" param to optionally pass additional order information
                // like product skus and quantities
                body: JSON.stringify({
                    cart: [{
                        sku: "YOUR-PRODUCT-STOCK-KEEPING-UNIT",
                        quantity: "YOUR-PRODUCT-QUANTITY",
                    }],
                }),
            })
            .then((response) => response.json())
            .then((order) => order.id);
    }
    onApprove(data) {
        // Order is captured on the server
        return fetch("/my-server/capture-paypal-order", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    orderID: data.orderID
                })
            })
            .then((response) => response.json());
    }
    render() {
        return (
            <PaypalButton createOrder={this.createOrder}
                onApprove={this.onApprove}
            />
        );
    }
}
```

### Functional implementation

```javascript
import React from "react";
import ReactDOM from "react-dom"
const PayPalButton = paypal.Buttons.driver("react", {
    React,
    ReactDOM
});

function YourComponent() {
    const createOrder = (data) => {
        // Order is created on the server and the order id is returned
        return fetch("/my-server/create-paypal-order", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": "Bearer ACCESS-TOKEN",
                    "PayPal-Partner-Attribution-Id": "BN-CODE",
                    "PayPal-Auth-Assertion": "AUTH-ASSERTION-JWT",
                },
                // use the "body" param to optionally pass additional order information
                // like product skus and quantities
                body: JSON.stringify({
                    cart: [{
                        sku: "YOUR-PRODUCT-STOCK-KEEPING-UNIT",
                        quantity: "YOUR-PRODUCT-QUANTITY",
                    }],
                }),
            })
            .then((response) => response.json())
            .then((order) => order.id);
    };
    const onApprove = (data) => {
        // Order is captured on the server and the response is returned to the browser
        return fetch("/my-server/capture-paypal-order", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    orderID: data.orderID
                })
            })
            .then((response) => response.json());
    };
    return (
        <PaypalButton createOrder={this.createOrder}
            onApprove={this.onApprove}
        />
    );
}
```

### Angular

```javascript
paypal.Buttons.driver("angular", window.angular);
angular
    .module("app", ["paypal-buttons"])
    .controller("appController", function($scope) {
        $scope.opts = {
            createOrder: function(data) {
                // Order is created on the server and the order id is returned
                return fetch("/my-server/create-paypal-order", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                            "Authorization": "Bearer ACCESS-TOKEN",
                            "PayPal-Partner-Attribution-Id": "BN-CODE",
                            "PayPal-Auth-Assertion": "AUTH-ASSERTION-JWT",
                        },
                        // use the "body" param to optionally pass additional order information
                        // like product skus and quantities
                        body: JSON.stringify({
                            cart: [{
                                sku: "YOUR-PRODUCT-STOCK-KEEPING-UNIT",
                                quantity: "YOUR-PRODUCT-QUANTITY",
                            }],
                        }),
                    })
                    .then((response) => response.json())
                    .then((order) => order.id);
            },
            onApprove: function(data) {
                // Order is captured on the server
                return fetch("/my-server/capture-paypal-order", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            orderID: data.orderID
                        })
                    })
                    .then((response) => response.json());
            },
        };
    });
```

### Angular 2

```javascript
(function() {
        const PayPalButton = paypal.Buttons.driver("angular2", ng.core);
        const appComponent = ng.core
            .Component({
                    selector: "my-app",
                    template:
                        <div id="app">
                        <paypal-buttons props="opts">
                        </paypal-buttons>
                      </div>, 
            })
    .Class({
            constructor: function() {
                this.createOrder = (function(data) {
                    // Order is created on the server and the order id is returned
                    return fetch("/my-server/create-paypal-order", {
                            method: "POST",
                            headers: {
                               "Content-Type": "application/json",
                               "PayPal-Partner-Attribution-Id": "BN-CODE",
                               "Authorization": "Bearer ACCESS-TOKEN",
                               "PayPal-Auth-Assertion": "AUTH-ASSERTION-JWT",
                            },
                            // use the "body" param to optionally pass additional order information
                            // like product skus and quantities
                            body: JSON.stringify({
                                cart: [{
                                    sku: "YOUR-PRODUCT-STOCK-KEEPING-UNIT",
                                    quantity: "YOUR-PRODUCT-QUANTITY",
                                }],
                            }),
                        })
                        .then((response) => response.json())
                        .then((order) => order.id);
                }).bind(this);
                this.onApprove = (function(data, actions) {
                    // Order is captured on the server
                    return fetch("/my-server/capture-paypal-order", {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/json",
                            },
                            body: JSON.stringify({
                                orderID: data.orderID
                            })
                        })
                        .then((response) => response.json());
                }).bind(this);
            });
    })
});
const appModule = ng.core
    .NgModule({
        imports: [ng.platformBrowser.BrowserModule, PayPalButton],
        declarations: [appComponent],
        bootstrap: [appComponent],
    })
    .Class({
        constructor: function() {},
    });
document.addEventListener("DOMContentLoaded", function() {
ng.platformBrowserDynamic
    .platformBrowserDynamic()
    .bootstrapModule(appModule);
});
})();
```

### Angular 2 using TypeScript

```javascript
@ng.core.Component({
    selector: 'my-app',
    template:
        <div id="app">
        <paypal-buttons props="{ createOrder: createOrder, onApprove: onApprove }">
        </paypal-buttons>
      </div>,
    })
class AppComponent {
    createOrder(data) {
        // Order is created on the server and the order id is returned
        return fetch("/my-server/create-paypal-order", {
                method: "POST",
                headers: {
                   "Content-Type": "application/json",
                   "PayPal-Partner-Attribution-Id": "BN-CODE",
                   "Authorization": "Bearer ACCESS-TOKEN",
                   "PayPal-Auth-Assertion": "AUTH-ASSERTION-JWT",
                },
                // use the "body" param to optionally pass additional order information
                // like product skus and quantities
                body: JSON.stringify({
                    cart: [{
                        sku: "YOUR-PRODUCT-STOCK-KEEPING-UNIT",
                        quantity: "YOUR-PRODUCT-QUANTITY",
                    }],
                }),
            })
            .then((response) => response.json())
            .then((order) => order.id);
    }
    onApprove(data, actions) {
        // Order is captured on the server
        return fetch("/my-server/capture-paypal-order", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    orderID: data.orderID
                })
            })
            .then((response) => response.json());
    }
}
@ng.core.NgModule({
    imports: [
        ng.platformBrowser.BrowserModule,
        paypal.Buttons.driver('angular2', ng.core)
    ],
    declarations: [
        AppComponent
    ],
    bootstrap: [
        AppComponent
    ]
})
const AppModule {}
ng.platformBrowserDynamic
    .platformBrowserDynamic()
    .bootstrapModule(AppModule);
```

### Vue

```javascript
<div id="container">
    <app></app>
</div>
<script>
    const PayPalButton = paypal.Buttons.driver('vue', window.Vue)

    Vue.component("app", {
        // The style prop for the PayPal button should be passed in as `style-object` or `styleObject` to avoid conflict with Vue's `style` reserved prop.
        template: `
            <paypal-buttons :on-approve="onApprove" :create-order="createOrder" :on-shipping-address-change="onShippingAddressChange" :on-shipping-options-change="onShippingOptionsChange" :on-error="onError" :style-object="style" />
          `,
        components: {
            "paypal-buttons": PayPalButton,
        },

        computed: {
            createOrder: function() {
                return (data) => {
                    // Order is created on the server and the order id is returned
                    return fetch("/my-server/create-paypal-order", {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/json",
                                "Authorization": "Bearer ACCESS-TOKEN",
                                "PayPal-Partner-Attribution-Id": "BN-CODE",
                                "PayPal-Auth-Assertion": "AUTH-ASSERTION-JWT",
                            },
                            // use the "body" param to optionally pass additional order information
                            // like product skus and quantities
                            body: JSON.stringify({
                                cart: [{
                                    sku: "YOUR-PRODUCT-STOCK-KEEPING-UNIT",
                                    quantity: "YOUR-PRODUCT-QUANTITY",
                                }],
                            }),
                        })
                        .then((response) => response.json())
                        .then((order) => order.id);
                }
            },
            onApprove: function() {
                return (data) => {
                    // Order is captured on the server
                    return fetch("/my-server/capture-paypal-order", {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/json",
                            },
                            body: JSON.stringify({
                                orderID: data.orderID
                            })
                        })
                        .then((response) => response.json());
                }
            },
            onShippingAddressChange(data, actions) {
                if (data.shippingAddress.countryCode !== 'US') {
                    return actions.reject(data.errors.COUNTRY_ERROR);
                }
            },
            onShippingOptionsChange(data, actions) {
                if (data.selectedShippingOption.type === 'PICKUP') {
                    return actions.reject(data.errors.STORE_UNAVAILABLE);
                }
            },
            onError: function() {
                return (err) => {
                    console.error(err);
                    window.location.href = "/your-error-page-here";
                }
            },
            style: function() {
                return {
                    shape: 'pill',
                    color: 'gold',
                    layout: 'horizontal',
                    label: 'paypal',
                    tagline: false,
                }
            },
        },
    });

    const vm = new Vue({
        el: "#container",
    });
</script>
```

## Next steps

### Test in sandbox
Test in the PayPal sandbox.

### Go live
Move from PayPal's production environment to go live.