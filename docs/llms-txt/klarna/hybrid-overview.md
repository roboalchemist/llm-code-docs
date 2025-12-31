# Source: https://docs.klarna.com/payments/mobile-payments/additional-resources/hybrid-overview.md

# Hybrid Overview

Our goal with the hybrid integration is to allow you to use your own web views and enhance your users’ experience when interacting with Klarna’s products.

## Four Steps to Integrate

Our iOS and Android SDKs hold weak references to your web views, don’t override any part of of your implementation or modify your web views in any way. Because of this, we ask you to perform some minor integration work to make your users’ experience as pleasant as possible. This consists of four steps:

1.  Initialization.
2.  Adding web views to the SDK.
3.  Notifying the SDK when something occurs in the web view.
4.  Handling events from the SDK.


![klarna docs image](39f92e36-336b-41c8-a5c2-45cbbfce93b1_INAPP_hybrid-diagram.jpeg)image

This guide will lead you through the steps below. If you’re ready to start your implementation, you can follow the [iOS guide here](https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/ios/hybrid.md), and the [Android guide here](https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/android/hybrid.md).

### STEP-BY-STEP

## Initializing the SDK

You can initialize the SDK by creating an instance of it. You’ll need to provide a return URL and an event listener. You’ll only need one instance, regardless of how many web views you have. Both for your convenience and ours (if debugging is necessary), try to initialize it as late in your application’s flow as possible.

## Adding Web Views

You should provide a reference to the web views that the SDK will observe. The SDK will hold a weak reference and it’ll stop running if it loses its reference to your web view.

## Notifying the SDK

There are two occasions in which we need you to notify the SDK:

### Before a Navigation Starts in Your Web View

The Klarna components you render in the web view contain links. If the components run in a web view associated with the SDK, these links will instead open:

- As native dialogs.
- In an in-app browser.
- If there’s no choice, in an external browser (Safari or Chrome).

This way, there is no possibility that a Klarna component performs a navigation inside your web view. However, there are cases when Klarna components might display 3rd-party content (e.g. some terms from a customer’s bank) which may also contain links. In these cases, Klarna can’t override the aforementioned navigation behavior. Because of this, we ask you to notify the SDK before a navigation occurs. If the SDK recognizes the URL as one that the customer should *not* navigate to, it’ll notify your app so it can stop this navigation from happening.

### After a Navigation Has Been Performed in Your Web View

The SDK communicates with the Klarna components in the web view in several ways: On iOS:

- Creating a bridging object in the UIWebView's JavaScript context.
- Adding a WKScriptMessageHandler to a WKWebView.

On Android:

- Creating a message channel (API 23 and above).
- Creating a bridging object in your WebViews's context (below API 23).

Some of these solutions stop working if the web view navigates to a new page. So, to “re-enable” communications between your web view and the SDK, we ask you to notify us when a new page has loaded.

## Handling Events

We ask you to implement an event listener so the SDK can notify your app when specific events have occurred in the web view. It’ll notify you of two types of events:

### Fullscreen Events

It’ll notify you when a Klarna component inside the web view will or did perform a transition to/from a full-screen state. You can read more about this [here](https://docs.klarna.com/payments/mobile-payments/before-you-start/fullscreen-in-hybrid).

### Errors

We will also notify you when an error has occurred.