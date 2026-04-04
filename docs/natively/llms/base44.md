# Source: https://docs.buildnatively.com/getting-started/other-platform-integrations/base44.md

# Base44

This guide walks you step-by-step, explains what you need to change inside your Base44 project, and shows how to configure BuildNatively so everything “just works.”

***

### What You’ll Need Before You Start

* A Base44 web app that opens with a secure HTTPS link.
* A BuildNatively account.
* Apple Developer and Google Play Developer accounts (for publishing).

Tip: If your app works in a mobile browser like Safari or Chrome, it will work in a native app with BuildNatively.

***

### Part 1 — Prepare Your Base44 App (Important!)

These simple adjustments inside Base44 will save you time later.

#### 1) Use a Secure HTTPS URL

All content must load over HTTPS. If anything loads over plain HTTP, iOS and Android can block it. Publish your Base44 app to an HTTPS URL before connecting it to BuildNatively.

#### 2) Keep One Primary Domain

Use a single primary domain for your app. Avoid switching between multiple subdomains for key screens (example: moving from app.example.com to accounts.example.com during login), unless you plan to mark those as external in BuildNatively.

#### 3) Make Every Important Screen Reachable by a Stable URL

Pages like Login, Signup, Profile, Checkout, Messages, and Orders should each have their own clean, shareable URL (for example, `/login`, `/profile`, `/orders/123`). This makes deep links and push-to-page actions work reliably.

#### 4) Prefer Pages Over Popups for Critical Flows

If login, payment, or onboarding are only in popups or modals with no URL change, deep links and notifications can’t open them. Create real pages with routes for these flows.

#### 5) Test the App on a Real Phone Browser

Open your Base44 app on an iPhone and an Android phone. Check that text fits on small screens, buttons are easy to tap, forms scroll properly, and video/images load quickly. Fix any layout issues in Base44 first — BuildNatively will show the same web content.

#### 6) Decide How You’ll Handle Login

* If you use standard email/password and it works in a mobile browser, it will work in the app.
* If you plan to add Google, Apple, or Facebook login, you’ll need to enable Social Auth and Universal Links in BuildNatively later.

#### 7) Plan External Links

List any links that go outside your Base44 domain (payments, YouTube, Calendly, Help Center, external docs). You will mark these as external in BuildNatively so they open in the phone’s browser and don’t get “stuck” inside your app.

***

### Part 2 — Create Your Mobile App in BuildNatively

1. Create a new app. Enter your app name and paste your Base44 HTTPS URL.
2. Upload your app icon. Use a 1024×1024 PNG without transparency.
3. Set your loading and error screens. Use 2048×2048 PNG images. These show while your app loads or if the network drops.
4. Choose navigation. If you want a bottom tab bar, configure tabs and their URLs now. You can also show or hide it programmatically later.
5. Define internal and external links. Add your own domain(s) as internal so they stay inside the app. Add any third-party sites (payments, video, scheduling) as external so they open in the phone’s browser.

***

### Part 3 — Enable Native Features (Optional but Powerful)

You can enable these at any time. When you change native features, you’ll need to rebuild your app.

#### Push Notifications

* Choose OneSignal or Firebase.
* Store each user’s notification identifier in your database so you can target them later.
* For “tap to open a page” behavior, include a deep link to the exact screen (for example, `/orders/123`).

#### Deep Links (Universal Links / App Links)

Deep links let a tap open a specific screen in your app. For new projects, use Native deep links or Branch.

#### Social Auth (Google, Apple, Facebook)

Social login requires working deep links so the user is returned to your app after authorization. Turn on Social Auth and Universal Links, set your app domain, and follow the setup steps. Apple Sign In also needs to be enabled for your iOS bundle ID.

#### In-App Purchases and Subscriptions

If you sell digital content or subscriptions, enable Purchases via RevenueCat inside BuildNatively. Follow the setup guide to connect your products and entitlement logic.

Other popular features include geolocation, native camera, QR/barcode scanner, contacts, haptics, and analytics. You can add these later as your app grows.

***

### Part 4 — Preview and Test

Use the Natively Preview app to see your Base44 app running on a phone before building. This is perfect for checking layout, navigation, and content.\
Note: Some native features do not work in Preview (for example, deep links, Social Auth, Admob, background location, in-app purchases). Build a test version when you’re ready to validate those.

***

### Part 5 — Build and Publish

When your app looks good in Preview:

1. Build for iOS and Android in your BuildNatively dashboard.
2. iOS builds are delivered to TestFlight for testing, then submitted for App Store review.
3. Android builds are generated for upload in Google Play Console.
4. If you enable or change native features later, rebuild to ship the update.

***

### Base44-Specific Best Practices

* Keep forms and key actions on full pages, not just popups, so deep links and notifications can open them.
* Make input text at least 16px to prevent iOS auto-zoom on fields.
* Compress large images and videos to speed up mobile startup.
* If you add third-party tools in Base44 (chat widgets, schedulers, external docs), list their domains and mark them external in BuildNatively.

***

### Troubleshooting: Quick Fixes

**Login opens in the browser and doesn’t return to the app**\
Enable Universal Links, verify the app domain, and rebuild. Social Auth relies on deep links to return users to your app after authorization.

**Stripe or other checkout pages don’t work inside the app**\
Mark checkout pages as external so they open in the phone’s browser.

**Notification arrives but tapping it does nothing**\
Include a deep link in the notification payload to the exact screen (for example, a specific order or message thread). Ensure that screen has a stable URL in your Base44 app.

**Some native features work in the built app but not in Preview**\
That’s expected. Use Preview for layout checks; build a test version to validate deep links, Social Auth, in-app purchases, background features, and Admob.

**My changes in Base44 aren’t showing in the app**\
Close and reopen the app to clear cache. If you changed native settings or appearance (icon, splash, permissions), rebuild to apply them.

***

### Quick Start Checklist

1. Base44 app is live over HTTPS and looks good on a phone.
2. Each important screen has its own URL; critical flows are pages, not only popups.
3. In BuildNatively: icon (1024×1024 PNG), splash/error images (2048×2048 PNG).
4. Internal vs external links are configured.
5. Optional: enable Push and Deep Links; if using Social Auth, set up Universal Links.
6. Preview the app; then build for iOS and Android and publish.

***

### Why This Works Well for Base44 Creators

Base44 lets you go from idea to working web app fast, without code. BuildNatively takes that same app and adds the native layer — push notifications, deep links, secure app store delivery, and more — so your users can install it from the App Store and Google Play like any other app.
