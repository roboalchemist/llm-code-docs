# App Switch

## Overview

App Switch helps PayPal customers start a transaction in a browser or app and complete it in the PayPal app, streamlining checkout with strong multi-factor authentication. The buyer can use biometrics or a passkey to log in instead of entering their password.

The buyer experience falls back to the web flow in cases where App Switch isn't available.

## Buyer flow

![Buyer, is directed to the PayPal app, to complete the transaction.](https://www.paypalobjects.com/devdoc/app_switch_flow.gif)

1. The buyer selects the PayPal button from another app or website.
2. The PayPal app opens and uses biometrics or a passkey to log the buyer in.
3. The buyer reviews purchase details and completes the transaction in the PayPal app.
4. The buyer is returned to the app or website where they selected the PayPal button.

## Integration options

### API: One-time payments

Merchant’s manage the payer's interaction between their app or website and the PayPal app.

### API: Vaulted payments

Vaulting helps securely save a payer’s PayPal wallet, with the payer’s consent, for future use.

### App Switch for JS SDK

Enable App Switch in the JavaScript SDK for resume flows and error scenarios.