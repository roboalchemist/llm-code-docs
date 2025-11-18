# Source: https://docs.klarna.com/platform-solutions/acquiring-partners/adyen/payments/accept-a-klarna-payment-through-adyen.md

# Accept a Klarna payment through Adyen

## You can choose from multiple integration options to accept a Klarna payment through Adyen. Pick the method best suited to your Adyen integration and contracts.

## Klarna for API only

Klarna for API only lets you control the look and feel of your checkout page and display specific payment methods, including Klarna. This integration option lets you integrate Klarna payments through an inline integration or through Klarna's Hosted payment page. Learn how to add Klarna to your existing Adyen API-only integration from [Adyen’s documentation on Klarna for API only](https://docs.adyen.com/payment-methods/klarna/api-only). If you haven't performed this integration yet, first refer to the Adyen checkout [API-only integration guide](https://docs.adyen.com/online-payments/api-only). [Take a look at the diagram illustrating the data flow in direct API integration](https://static.swimlanes.io/e51e7a6a687e0855cc968ee60bb6439a.png). If you want to use the Klarna inline integration (Adyen checkout API), to comply with [GDPR regulations](https://eur-lex.europa.eu/eli/reg/2016/679/oj), make sure you’re sending [the payments request](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments) to Klarna after the customer selects Klarna as the payment method. In the request, the customer details are sent to Adyen who, in turn, forwards the data to Klarna.

## Web drop-in or component

Web drop-in or component uses Klarna's hosted checkout, with Adyen managing the display of different payment methods (including Klarna), logos, and payment descriptors. You can manage the payment method availability in your Adyen Customer Area. Adyen automatically returns the Klarna products in the markets that are enabled in your merchant account settings. For more information, see [Adyen's documentation on Klarna for web drop-in or component](https://docs.adyen.com/payment-methods/klarna/web). If you haven’t yet integrated Web drop-in or component into Adyen, first refer to the [Web Drop-in integration guide](https://docs.adyen.com/online-payments/web-drop-in) or [Web Components integration guide](https://docs.adyen.com/online-payments/web-components). [Take a look at the diagram illustrating the data flow in web drop-in or component integration](https://static.swimlanes.io/a57fc5d58a1f6e8dfd57a69c17e2f198.png).

## Mobile apps

You can integrate Klarna into your mobile application in two ways:

- If you have the Adyen Checkout API integration and want to integrate Klarna into your iOS or Android mobile app, follow the [Klarna In-app SDK integration guide](https://docs.klarna.com/platform-solutions/acquiring-partners/adyen/payments/accept-a-klarna-payment-through-adyen/). Since you own the user interface of the checkout, the In-app SDK integration doesn’t require any other changes.
- If you have the web drop-in component integration, you can integrate the [drop-in](https://docs.adyen.com/online-payments/ios/drop-in) and [component](https://docs.adyen.com/online-payments/ios/components) objects. Klarna is displayed as a payment method within Adyen’s hosted solution, allowing Adyen to take care of redirecting the customer to Klarna’s hosted payment page.