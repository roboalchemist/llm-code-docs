# Source: https://docs.buildnatively.com/getting-started/other-platform-integrations/replit.md

# Replit

Replit helps you create and host your web apps, while BuildNatively wraps your project into a mobile app and unlocks powerful native features like push notifications, deep links, in-app purchases, geolocation, and more.

This guide will walk you step by step through everything you need to do in **Replit** and in **BuildNatively**, so your app works perfectly on iOS and Android.

***

### What You’ll Need Before You Start

* A **Replit web app** (already created and running).
* A **secure HTTPS link** to your Replit app.
* A **BuildNatively account**.
* Optional but recommended:
  * An **Apple Developer account** ($99/year).
  * A **Google Play Developer account** ($25 one-time).

***

### Part 1 — Prepare Your Replit App

Before connecting to BuildNatively, make sure your Replit app is set up correctly.

#### 1) Publish with HTTPS

* Replit apps must run over **https\://** (Replit provides this automatically for public web apps).
* Make sure every resource (images, scripts, APIs) also uses HTTPS.
* Apps that load **http\://** resources will not work in iOS/Android.

***

#### 2) Use a Single Domain

* Keep all of your app’s pages on one domain (the Replit-provided domain or a custom domain you’ve set).
* Avoid switching between multiple subdomains for important flows like login or checkout.
* If you must use an external domain (for payments, external services), you’ll mark it as **external** in BuildNatively later.

***

#### 3) Create Stable URLs for All Important Pages

* Every key part of your app (login, signup, profile, checkout, dashboard, orders, messages) should have its own **clean, shareable URL**.
* Examples:
  * `/login`
  * `/signup`
  * `/profile`
  * `/orders/123`
* These stable URLs are essential for deep links, notifications, and navigation.

***

#### 4) Avoid Popups for Critical Actions

* Popups or modals for login, signup, or checkout don’t generate unique URLs.
* This breaks deep linking, push notifications, and return flows after login.
* Instead, create **dedicated pages** for these flows in your Replit app.

***

#### 5) Test in a Mobile Browser

* Open your Replit app on both **iPhone (Safari)** and **Android (Chrome)**.
* Check that:
  * Text and buttons fit the screen.
  * Forms work without zooming.
  * Pages scroll smoothly.
  * Images and videos load quickly.
* Fix any layout issues directly in Replit before moving forward.

***

#### 6) Plan Your Login System

* **Email/password login**: If it works in mobile browsers, it will work in the app.
* **Social login (Google, Apple, Facebook)**:
  * Requires **deep links (Universal Links/App Links)** so users are returned to your app after login.
  * You’ll configure this in BuildNatively later.
* Make sure your login flow redirects back to your Replit domain.

***

#### 7) List Your External Links

* Identify any external sites your app uses (Stripe, PayPal, YouTube, Calendly, Help Docs, etc.).
* You’ll mark these as **external** in BuildNatively so they open in the device’s browser instead of inside the app.

***

#### 8) Optimize Performance

* Compress images and videos to reduce load times.
* Avoid very heavy scripts that slow down startup.
* Keep your homepage lightweight so the mobile app loads fast.

***

### Part 2 — Create Your Mobile App in BuildNatively

1. Log in to your **BuildNatively dashboard**.
2. Click **Create New App**.
3. Enter your app’s name.
4. Paste your Replit app’s **HTTPS URL**.
5. Save — your Replit app is now connected to BuildNatively.

***

### Part 3 — Customize Your App

* **App Icon**: Upload a **1024×1024 PNG** (no transparent background).
* **Splash Screen**: Upload a **2048×2048 PNG** (shown while your app loads).
* **Error Screen**: Upload another **2048×2048 PNG** (shown if the network fails).
* **Navigation**: Choose between Bottom Bar, Top Bar, or no navigation. Configure tabs if using Bottom Bar.
* **Colors & Style**: Adjust background, theme, and accent colors.
* **Permissions**: Add clear, user-friendly descriptions for any native features you enable (e.g., “We use your camera to let you upload photos”).

***

### Part 4 — Configure Links

* Add your **Replit domain** as an **internal link** so it stays inside the app.
* Add any external services (Stripe, PayPal, Calendly, YouTube, external docs) as **external links** so they open in the device’s browser.
* This prevents errors or users getting “stuck.”

***

### Part 5 — Enable Native Features

You can enable these anytime. Rebuild your app if you make changes.

* **Push Notifications**: Use OneSignal or Firebase. Include deeplinks so users land on the right screen when tapping a notification.
* **Deep Links**: Allow users to open specific screens (e.g., `/orders/123`) directly from links or notifications. Required for social login.
* **Social Login**: Enable Google, Apple, or Facebook login by turning on **Social Auth** + **Deep Links**.
* **In-App Purchases**: Use RevenueCat for digital subscriptions or content.
* **Other Features**: Enable geolocation, camera, QR scanning, contacts, analytics, and more as needed.

***

### Part 6 — Preview Your App

* Install the **BuildNatively Preview App** on your phone.
* Log in and preview your Replit app inside it.
* Use this to check layout, navigation, and styling.
* Remember: push, deep links, social login, in-app purchases, and some native features **only work after a full build**.

***

### Part 7 — Build & Publish

1. Build for **iOS and Android** inside your BuildNatively dashboard.
2. For iOS:
   * Connect your Apple Developer account.
   * Test in TestFlight.
   * Submit to the App Store.
3. For Android:
   * Connect your Google Play Developer account.
   * Upload the APK/AAB to Google Play Console.
   * Publish to the Play Store.

***

### Part 8 — After Publishing

* Update your Replit app anytime — changes appear instantly in your mobile app (no rebuild needed).
* If you change **native features** (push, payments, deep links, navigation), rebuild in BuildNatively.
* Use push notifications and deep links to engage users.
* Track analytics if enabled.

***

### Troubleshooting: Common Issues

#### Login & Auth

* **Problem:** Login opens in browser and doesn’t return.
* **Fix:** Enable Deep Links + Social Auth, rebuild app.
* **Problem:** Blank screen after login.
* **Fix:** Make sure login redirects to a full page with a URL, not a popup.

***

#### Payments

* **Problem:** Stripe/PayPal checkout doesn’t work.
* **Fix:** Mark checkout pages as external in BuildNatively.
* **Problem:** Apple rejected app for payment handling.
* **Fix:** Use In-App Purchases for digital goods/subscriptions.

***

#### Notifications & Deep Links

* **Problem:** Notification arrives but does nothing.
* **Fix:** Add a unique deeplink to the notification payload (e.g., `/messages/123`).
* **Problem:** Notifications don’t arrive.
* **Fix:** Check push config, rebuild app, and test again.

***

#### Layout & Display

* **Problem:** Pages cut off on small screens.
* **Fix:** Adjust layout in Replit for mobile-first design.
* **Problem:** iOS zooms in on forms.
* **Fix:** Use at least 16px font size on input fields.

***

#### App Store & Play Store Rejections

* **Problem:** “Just a website” rejection.
* **Fix:** Add native features like push notifications, deep links, or camera.
* **Problem:** Missing permission descriptions.
* **Fix:** Add clear permission texts in BuildNatively before rebuilding.
* **Problem:** Performance issues.
* **Fix:** Optimize images/videos in Replit and reduce heavy scripts.

***

### Quick Start Checklist

1. Replit app is live with HTTPS.
2. Each important screen has a unique URL (no popups for login/checkout).
3. Layout tested on real phones for mobile friendliness.
4. External links (Stripe, YouTube, Calendly) listed and configured as external in BuildNatively.
5. App icon (1024×1024 PNG) and splash/error screens (2048×2048 PNG) ready.
6. Optional: Push notifications, deep links, and social login configured.
7. Preview app tested, then full builds created.
8. Submitted to App Store and Google Play.

***

### Why This Works Well for Replit Users

Replit gives you a fast way to build and deploy web apps. BuildNatively takes those apps and makes them **installable mobile apps** with powerful native features and app store distribution. Together, they let you go from idea to a live mobile app — without needing advanced coding or app development tools.
