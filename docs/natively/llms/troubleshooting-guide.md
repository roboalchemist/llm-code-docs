# Source: https://docs.buildnatively.com/getting-started/other-platform-integrations/replit/troubleshooting-guide.md

# Source: https://docs.buildnatively.com/getting-started/other-platform-integrations/base44/troubleshooting-guide.md

# Source: https://docs.buildnatively.com/getting-started/other-platform-integrations/lovable.dev/troubleshooting-guide.md

# Troubleshooting Guide

Here’s a detailed list of the **most common issues** you may encounter when turning your Lovable.dev app into a mobile app with BuildNatively, along with their solutions.

***

### 1. Login & Authentication Issues

#### 1.1 My login opens in Safari/Chrome instead of inside the app

* **Why it happens:** Social login (Google, Apple, or Facebook) requires special setup to return users to the app instead of a browser.
* **How to fix:**
  1. In BuildNatively, enable **Universal Links (Deeplinks)** under the Features section.
  2. Make sure your Lovable.dev app redirects users back to your domain after login.
  3. Rebuild your app after enabling Universal Links.

***

#### 1.2 My Google/Apple login doesn’t work at all

* **Why it happens:** Social Auth requires both your Lovable.dev settings and BuildNatively’s Deeplinks to be configured correctly.
* **How to fix:**
  * Confirm that **Social Auth** is turned on in BuildNatively.
  * Enable **Associated Domains** for iOS in your Apple Developer account.
  * Verify your redirect URL matches your Lovable.dev app’s domain.

***

#### 1.3 Email/password login works in Lovable.dev but fails in the app

* **Why it happens:** Sometimes authentication cookies don’t carry over correctly in the mobile app.
* **How to fix:**
  * Check that your Lovable.dev app is running under **HTTPS** (not HTTP).
  * Test login in a mobile browser first. If it works there, it should work in the app.

***

### 2. Payments & Checkout Issues

#### 2.1 Stripe or checkout pages don’t load inside the app

* **Why it happens:** Payment providers like Stripe or PayPal open in secure external pages. If the app tries to load them internally, they may break.
* **How to fix:**
  * Mark your checkout links as **external links** in the BuildNatively dashboard.
  * This ensures they open in the user’s default browser, where payments complete correctly.

***

#### 2.2 Apple/Google reject my app because of Stripe payments

* **Why it happens:** For digital goods/services, Apple and Google require **In-App Purchases (IAP)**. Stripe can only be used for physical products, real-world services, or P2P payments.
* **How to fix:**
  * If you sell **digital goods/subscriptions**, enable **In-App Purchases** in BuildNatively (powered by RevenueCat).
  * If you sell **physical goods/services**, you may keep using Stripe.

***

### 3. Push Notifications & Deeplinks

#### 3.1 Notifications show, but nothing happens when I tap them

* **Why it happens:** Notifications need a **deeplink** to know which screen to open.
* **How to fix:**
  * In BuildNatively, configure notifications with a specific page URL (e.g., `/messages/123`).
  * Ensure your Lovable.dev app has that page accessible.

***

#### 3.2 Notifications send me to the wrong page

* **Why it happens:** The deeplink used may not match your Lovable.dev app’s routing.
* **How to fix:**
  * Double-check that the link in your notification exactly matches the structure in your Lovable.dev app.

***

#### 3.3 Notifications don’t arrive at all

* **Why it happens:** Push notifications require setup with **OneSignal** or **Firebase**.
* **How to fix:**
  * Check that you’ve uploaded the correct config files in BuildNatively.
  * Rebuild your app after enabling notifications.

***

### 4. Layout & Display Issues

#### 4.1 Some pages look broken or cut off on mobile

* **Why it happens:** Your Lovable.dev design may not be fully optimized for small screens.
* **How to fix:**
  * Open your Lovable.dev app on your phone and test every key page.
  * Adjust layouts in Lovable.dev (resize elements, stack content vertically).

***

#### 4.2 My app looks different in the BuildNatively Preview App

* **Why it happens:** The Preview App does not support all native features.
* **How to fix:**
  * Use it mainly to check **design, navigation, and content flow**.
  * Do a full build to test native features like notifications, in-app purchases, or deeplinks.

***

#### 4.3 Scroll or zoom issues on forms

* **Why it happens:** iOS automatically zooms in on text fields with small font sizes.
* **How to fix:**
  * In your Lovable.dev design, increase input font sizes to at least **16px**.

***

### 5. Links & Navigation

#### 5.1 External links (YouTube, Calendly, Help Docs) don’t work

* **Why it happens:** BuildNatively assumes all links are internal unless marked otherwise.
* **How to fix:**
  * Add these links as **external** in the BuildNatively dashboard so they open in the browser.

***

#### 5.2 Clicking a link sometimes reloads the entire app

* **Why it happens:** If the link structure isn’t set correctly, the app may think you’re leaving the app.
* **How to fix:**
  * Ensure your internal links all use the **same root domain** as your Lovable.dev app.

***

### 6. Publishing Issues

#### 6.1 Apple rejected my app for missing permission descriptions

* **Why it happens:** Apple requires you to explain why your app asks for permissions (camera, location, microphone, etc.).
* **How to fix:**
  * In BuildNatively, fill out the **Permission Description** fields under each enabled feature. Example: *“We use your location to show nearby events.”*

***

#### 6.2 My app was rejected for using the wrong payment system

* **Why it happens:** Apple and Google require **In-App Purchases** for digital goods.
* **How to fix:**
  * If you sell digital items, enable RevenueCat integration.
  * If you sell physical goods, Stripe is fine.

***

#### 6.3 Google flagged my app for unsupported memory pages (NDK)

* **Why it happens:** Google is updating requirements for Android builds.
* **How to fix:**
  * No action needed now — BuildNatively will handle this automatically in future updates.

***

### 7. Other Common Issues

#### 7.1 My app loads very slowly

* **Why it happens:** Your Lovable.dev app may have heavy images or scripts.
* **How to fix:**
  * Optimize images and videos inside Lovable.dev.
  * Use fewer large plugins or animations.

***

#### 7.2 My changes in Lovable.dev don’t appear in the app

* **Why it happens:** You may be looking at a cached version of your app.
* **How to fix:**
  * Close and reopen your app.
  * If you changed something in **BuildNatively** (like features, style, or permissions), you’ll need to **rebuild**.

***

#### 7.3 The app works in the browser but breaks inside BuildNatively

* **Why it happens:** Some features behave differently inside mobile apps (compared to browsers).
* **How to fix:**
  * Check if the feature is listed as **unsupported in Preview**.
  * Contact BuildNatively support if it persists after a full build.

***

## Quick Checklist Before Submitting to App Stores

* ✅ HTTPS link is used.
* ✅ Internal/external links are set correctly.
* ✅ Login/signup flows tested (with Universal Links if needed).
* ✅ Layout looks good on small screens.
* ✅ Payment flow matches Apple/Google rules.
* ✅ Permission descriptions are filled out.
* ✅ Push notifications and deeplinks tested.
