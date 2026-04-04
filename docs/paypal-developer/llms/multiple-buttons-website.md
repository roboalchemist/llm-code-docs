# Multiple subscription buttons

You can let your buyers choose a subscription plan from multiple plans available from a single page of your website.

![Two, sets, of subscription buttons where a basic plan is $5 and a premium plan is $10](https://www.paypalobjects.com/ppdevdocs/img/docs/subscriptions/multi-subscription-buttons.svg)

## 1. Modify JavaScript SDK code

Modify the JavaScript SDK code to render multiple buttons on a single webpage.

Add the SDK script before the first PayPal button `div`. Add the SDK script only once on your web page ensure that the SDK doesn't render multiple times on your webpage.

```html
<script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&amp;vault=true&amp;intent=subscription"></script>
```

## 2. Add ID for each button

Add a unique container HTML `id` for each button code.

**Tip:** Use the same ID for the container ID that you used for the plan ID.

```html
<div id="paypal-button-container"></div> // A unique ID for each button
<script>
  paypal.Buttons({
    createSubscription: function(data, actions) {
      return actions.subscription.create({
        'plan_id': 'YOUR-PLAN-ID'
      });
    },
    onApprove: function(data, actions) {
      alert('You have successfully subscribed to ' + data.subscriptionID); // Optional message given to subscriber
    }
  }).render('#paypal-button-container'); // Renders the PayPal button. Replace with your plan ID
</script>
```

### Example

This sample creates 2 different plans:

- Basic plan priced at $5 per month with plan ID `P-89K58960WT101463BMA2QTGQ`.
- Premium plan priced at $10 per month with plan ID `P-8D325842DA922762MMA2QT6Q`.

```html
<!DOCTYPE html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1"> 
  <!-- Ensures optimal rendering on mobile devices. -->
  <meta http-equiv="X-UA-Compatible" content="IE=edge"> 
  <!-- Optimal Internet Explorer compatibility -->
  <style>
    body {
      display: flex;
      direction: 'column';
    }

    .column {
      border: 1px solid #ccc;
      margin: 20px;
      padding: 20px;
    }

    p {
      text-align: center;
      margin-bottom: 50px;
    }
  </style>
</head>
<body>
  <script src="https://www.paypal.com/sdk/js?CLIENT-ID=AUwAEZzkXUVAhmO10ESMB7i9jBlp9PlvrpgX1RGo5APTKMKFSRBNmCW98BxjzhAyDU0sIslCMdeOsDm3&amp;vault=true&amp;intent=subscription"></script>
  <div class="column">
    <p>$5 per month</p>
    <div id="paypal-button-container-P-89K58960WT101463BMA2QTGQ"></div> <!-- Replace with your plan ID -->
  </div>

  <script>
    paypal.Buttons({
      createSubscription: function(data, actions) {
        return actions.subscription.create({
          'plan_id': 'P-89K58960WT101463BMA2QTGQ' // Replace with your plan ID
        });
      },
      onApprove: function(data, actions) {
        alert('You have successfully subscribed to ' + data.subscriptionID); // Optional message given to subscriber
      }
    }).render('#paypal-button-container-P-89K58960WT101463BMA2QTGQ'); // Renders the PayPal button. Replace with your plan ID
  </script>

  <div class="column">
    <p>$10 per month</p>
    <div id="paypal-button-container-P-8D325842DA922762MMA2QT6Q"></div> <!-- Replace with your plan ID -->
  </div>
  <script>
    paypal.Buttons({
      createSubscription: function(data, actions) {
        return actions.subscription.create({
          'plan_id': 'P-8D325842DA922762MMA2QT6Q' // Replace with your plan ID
        });
      },
      onApprove: function(data, actions) {
        alert('You have successfully subscribed to ' + data.subscriptionID); // Optional message given to subscriber
      }
    }).render('#paypal-button-container-P-8D325842DA922762MMA2QT6Q'); // Replace with your plan ID
  </script>
</body>
</html>
```