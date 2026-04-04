# Source: https://docs.buildnatively.com/guides/integration.md

# Source: https://docs.buildnatively.com/getting-started/other-platform-integrations/replit/integration.md

# Source: https://docs.buildnatively.com/getting-started/other-platform-integrations/base44/integration.md

# Source: https://docs.buildnatively.com/getting-started/other-platform-integrations/lovable.dev/integration.md

# Integration

In addition to creating your app in BuildNatively, there are a few things you’ll need to set up inside your **Lovable.dev project**. These adjustments make sure your app behaves properly inside a mobile app environment and that all features (like logins, links, and payments) work as expected.

#### 1. Make Sure Your Lovable.dev App is Published Securely

* Your app must be published with a **secure HTTPS link** (e.g., `https://myapp.lovable.dev`).
* iOS and Android **do not allow** apps to load insecure (HTTP) websites.
* If you’re testing with a temporary link, switch to the secure version before connecting it to BuildNatively.

***

#### 2. Organize Internal and External Links

* **Internal Links (inside your app):** These are links to your app’s own pages (like `/dashboard`, `/shop`, or `/profile`).
  * These should stay inside the app when clicked.
  * No changes are needed here if you’re using Lovable’s built-in navigation.
* **External Links (outside your app):** These include links to websites like Stripe Checkout, Calendly, YouTube, or help docs.
  * If you don’t configure these, users may get “stuck” inside your app or see errors.
  * In BuildNatively, you’ll need to **mark these links as external**, so they open in the user’s phone browser instead of inside the app.

👉 **Action for You:** Review your Lovable app and make a list of any links that point outside your own site. These will need to be added as “external” in BuildNatively’s settings.

***

#### 3. Adjust Login & Authentication Settings

If your app has login or signup features, here’s what you need to check:

* **Test standard email/password login** in your Lovable app on mobile (Safari/Chrome). If it works in the browser, it will work inside your app.
* If you’re using **Social Login (Google, Apple, Facebook)**:
  * You must enable **Universal Links / Deeplinks** in BuildNatively.
  * Lovable.dev should redirect back to your app correctly after authentication.
  * Without this step, logins may redirect users to a browser instead of back into your app.

👉 **Action for You:** If you use social login, plan to configure Universal Links in BuildNatively as part of your setup.

***

#### 4. Optimize the Layout for Mobile Screens

* Even though BuildNatively wraps your Lovable app as-is, the design still comes from Lovable.dev.
* That means you need to make sure your Lovable app looks good on small screens:
  * Avoid very wide tables, large popups, or elements that don’t resize properly.
  * Test important flows (like checkout, signup, and dashboard pages) on a real phone browser before connecting it to BuildNatively.

👉 **Action for You:** Open your Lovable app on your own phone and go through it like a user would. If anything looks too big or hard to use, adjust it in Lovable.dev before publishing.

***

#### 5. Prepare for Push Notifications & Deeplinks

If you plan to send push notifications (for example, “New message received” or “Lesson unlocked”), you’ll want them to open the right screen in your app when tapped.

* BuildNatively supports **deeplinks**, which means you can link directly to a page inside your Lovable app (e.g., `/messages/123`).
* To make this work, your Lovable app must be able to handle these URLs properly.

👉 **Action for You:** Make sure each important page in your app has a unique, shareable URL (not just hidden behind popups). This way, notifications can link directly to it.

***

#### 6. Payments & Checkout Pages

If you’re using Stripe or another payment system inside Lovable.dev:

* Test your checkout flow on mobile browsers first.
* If your checkout redirects users to an **external payment page** (like Stripe Checkout), make sure that page is marked as an **external link** in BuildNatively.
* Otherwise, users may not be able to complete their payment inside the app.

***

#### Summary of What You Need to Do in Lovable.dev

Before wrapping your Lovable app with BuildNatively, make sure to:

1. Publish it with a **secure HTTPS link**.
2. Separate **internal vs. external links** and prepare to configure them.
3. Test your **login/signup flows**, especially social login.
4. Adjust layouts so the app looks good on **small mobile screens**.
5. Make sure important pages have unique URLs for **deeplinks and notifications**.
6. Test **checkout flows** if you’re selling products or services.

***

👉 Once these steps are done in Lovable.dev, your app will be fully ready to integrate with BuildNatively and take advantage of native features like push notifications, social login, and app store publishing.

***
