# Source: https://documentation.onesignal.com/docs/en/wordpress.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# WordPress

> Complete setup and migration guide for OneSignal WordPress Web Push Plugin v3+. Configure push notifications, prompts, and segmentation through the OneSignal dashboard with streamlined setup process.

## Overview

This guide covers how to setup and configure OneSignal WordPress Web Push Plugin v3+.

<Info>
  For the older version 2.x.x WordPress documentation, see [WordPress Legacy plugin](./wordpress-legacy).
</Info>

### What's New in Version 3+

This release marks a significant upgrade by streamlining the setup and configuration process. With Version 3+, you can handle all your prompt settings in one place—the OneSignal Dashboard.

* 🚀 **SDK Upgrade**: Updates OneSignal Web SDK from version 15 to 16
* 💬 **Dashboard Prompts**: Configure all [permission prompts](./permission-requests) directly in the OneSignal dashboard—no custom code required
* ⏩ **One-Click Publishing**: Check "Send notification when post is published" to automatically send push notifications
* 🧑‍🤝‍🧑 **Audience Targeting**: Choose which [segments](./segmentation) receive notifications for each post
* 📲 **Mobile App Integration**: Send to mobile app subscribers with optional [deep linking](./links#deep-linking)

<Info>
  For the older version 2.x.x WordPress docs, see [WordPress Legacy plugin](./wordpress-legacy).
</Info>

***

## Setup

Before you begin, ensure you have:

* [OneSignal account](https://dashboard.onesignal.com/signup) (free to create)
* WordPress admin access to install and configure plugins
* HTTPS-enabled website (required for web push notifications)

### 1. Configure WordPress in OneSignal Dashboard

Navigate to **Settings > Push & In-App > Web > WordPress Plugin or Website Builder**

<Frame caption="Select WordPress from the Website Builder options in your OneSignal dashboard">
  <img src="https://mintcdn.com/onesignal/sCO1i1UqrWQxmZ28/images/dashboard/wordpress-integration-selection.png?fit=max&auto=format&n=sCO1i1UqrWQxmZ28&q=85&s=d48170c90c2d9e309769c430c1f8336d" width="1916" height="590" data-path="images/dashboard/wordpress-integration-selection.png" />
</Frame>

#### Site setup

* **Site Name**: The name of your site and default notification title.
* **Site URL**: Must match your WordPress site's exact URL (follow [Same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy))
* **Auto Resubscribe**: Enable this to automatically resubscribe users who clear their browser data when they return to your site (no new permission prompt required)
* **Default Icon URL**: Square `256x256px` PNG or JPG file for notifications and prompts – MacOS Safari will not show a notification prompt without an Icon.

<Frame caption="Enter your exact Site URL. https://your-site.com is different from https://www.your-site.com—use only one format consistently">
  <img src="https://mintcdn.com/onesignal/jFWn5xzleD8du3j6/images/docs/5a29a00c2808e8128e2cd822d743d14b472637f65fbde2aa64d9f16a8658d4a6-Screenshot_2025-02-13_at_3.06.28_PM.png?fit=max&auto=format&n=jFWn5xzleD8du3j6&q=85&s=535d1d4b6d579d0d296fbed60d5d669b" width="2046" height="1036" data-path="images/docs/5a29a00c2808e8128e2cd822d743d14b472637f65fbde2aa64d9f16a8658d4a6-Screenshot_2025-02-13_at_3.06.28_PM.png" />
</Frame>

<Info>
  Testing locally? See [Local Testing Guide](./web-sdk-setup#local-testing) for localhost development
</Info>

#### Permission prompts

Set up your [permission prompts](./permission-requests) for Push, Email, and/or SMS. The Push Slide Prompt is enabled by default, but you can customize or add additional prompts.

<Info>
  **Pro Tip**: Start with simple prompts and gradually add complexity. You can
  modify all prompt settings anytime through the OneSignal dashboard. Explore
  all available options in [Web permission prompts](./permission-requests).
</Info>

<Tabs>
  <Tab title="Basic Prompt Setup">
    <Steps>
      <Step title="Click on Push Slide Prompt to customize">
        <Frame caption="Access and customize your push slide prompt settings">
          <img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/32d2f36e12becd930037774ab376b1c65080fbb801e99f37f00964603371614e-Screenshot_2025-02-13_at_3.39.15_PM.png?fit=max&auto=format&n=_KaXe4GQkxsEfa17&q=85&s=fffa465720f34780e7c22b047a57ca4e" width="2534" height="452" data-path="images/docs/32d2f36e12becd930037774ab376b1c65080fbb801e99f37f00964603371614e-Screenshot_2025-02-13_at_3.39.15_PM.png" />
        </Frame>
      </Step>

      <Step title="Configure timing and text:">
        * Set **Auto Prompt** to `1` pageview and `1` second for initial testing
          * Customize prompt text and appearance
          * Adjust timing based on user behavior after launch

        <Frame caption="Configure auto-prompt timing and customize prompt appearance">
          <img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/3f3638ec5fa60f55fb8aa922ba0f7197aee508f11b242e0377a0a8e255a2b38d-Screenshot_2025-02-13_at_3.42.09_PM.png?fit=max&auto=format&n=_KaXe4GQkxsEfa17&q=85&s=33f5eb55da0cee00d1d8121bb3f66f89" width="1922" height="1594" data-path="images/docs/3f3638ec5fa60f55fb8aa922ba0f7197aee508f11b242e0377a0a8e255a2b38d-Screenshot_2025-02-13_at_3.42.09_PM.png" />
        </Frame>
      </Step>

      <Step title="Click Done when you've finished configuring the prompt." />
    </Steps>
  </Tab>

  <Tab title="Advanced: Category-Based Segmentation">
    For targeted messaging based on user interests, set up categories:

    <Steps>
      <Step title="Select Categories in your prompt settings" />

      <Step title="Configure each category with:">
        * **Label**: What users see in the prompt
        * **Tag Key**: Internal [tag key](./add-user-data-tags) for segmentation
      </Step>

      <Step title="Click Done when you've finished configuring the prompt." />
    </Steps>

    <Frame caption="Example: Setting up News and Deals categories creates tags 'news: 1' and 'deals: 1' for users who check these options">
      <img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/39ebfb19de43d53d6f07956c6e96bb101dca53dca81a58f6fc55a021f73ccdc9-Screenshot_2025-02-18_at_3.36.56_PM.png?fit=max&auto=format&n=_KaXe4GQkxsEfa17&q=85&s=3d0d41386891b9b84ed2619da519206d" width="1910" height="1604" data-path="images/docs/39ebfb19de43d53d6f07956c6e96bb101dca53dca81a58f6fc55a021f73ccdc9-Screenshot_2025-02-18_at_3.36.56_PM.png" />
    </Frame>

    **Tag Logic**: Checked categories set tag value to `1`, unchecked to `0`. These tags enable targeted messaging to specific user interests.
  </Tab>
</Tabs>

#### Welcome notification

Set up an immediate notification sent after users first subscribe. This:

* Thanks users for subscribing
* Demonstrates how notifications appear
* Increases engagement and reduces unsubscribes

Configure your welcome message text and timing, then scroll down and click **Save**.

<Tip>
  Skip the **Advanced Push Settings** section in the OneSignal Dashboard for now — these are for custom [Web SDK setup](./web-sdk-setup). Click **Save** to continue.
</Tip>

### 2. Configure WordPress plugin

After saving your dashboard configuration, you'll see your **App ID** and **API Key**. Copy these values to your WordPress plugin:

<Frame caption="Copy your App ID and API Key from the OneSignal dashboard">
  <img src="https://mintcdn.com/onesignal/sCO1i1UqrWQxmZ28/images/dashboard/wordpress-app-id-and-api-key.png?fit=max&auto=format&n=sCO1i1UqrWQxmZ28&q=85&s=90643a5aafc920c3785b42a093ae1773" width="1648" height="826" data-path="images/dashboard/wordpress-app-id-and-api-key.png" />
</Frame>

<Info>
  **Don't see an API Key?** Follow our [Keys & IDs guide](./keys-and-ids) to
  create one.
</Info>

<Steps>
  <Step title="In your WordPress admin, navigate to the OneSignal plugin settings" />

  <Step title="Paste the App ID and REST API Key exactly as shown in your dashboard" />
</Steps>

<Frame caption="Ensure your WordPress plugin App ID and REST API Key match your OneSignal dashboard exactly">
  <img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/c92c0ca5a7e910104a2c3e5d0fa87e63c2a9adb61aa20de072b41b49006a70c0-Screenshot_2025-02-13_at_3.49.16_PM.png?fit=max&auto=format&n=9_Q1FZLh6C0BFLq-&q=85&s=ba2996eacb58d914c34edc5884e5abb1" width="1828" height="1064" data-path="images/docs/c92c0ca5a7e910104a2c3e5d0fa87e63c2a9adb61aa20de072b41b49006a70c0-Screenshot_2025-02-13_at_3.49.16_PM.png" />
</Frame>

#### Advanced settings

Configure additional plugin options based on your needs:

<Frame caption="Advanced settings for enhanced functionality and analytics tracking">
  <img src="https://mintcdn.com/onesignal/bqiNDj5j2mpssdoy/images/push/wordpress-advanced-settings.png?fit=max&auto=format&n=bqiNDj5j2mpssdoy&q=85&s=a6142c3df995140d2927cbc7c6058149" width="1946" height="1410" data-path="images/push/wordpress-advanced-settings.png" />
</Frame>

**URL parameter tracking**

Add analytics parameters to notification URLs for tracking. **Important**: Escape special characters—input is added as-is to URLs.

**Example for Google Analytics:**

```
utm_medium=push&utm_source=onesignal&utm_campaign=wordpress-plugin
```

**Example with special characters:**

```
utm_medium=ppc&utm_source=adwords&utm_campaign=snow%20boots&utm_content=durable%20snow%20boots
```

**Additional settings**

* **Custom Post Types**: Add post types from plugins to enable notification options
* **Automatically send notifications when a post is published**: Automatically checks notification box when publishing posts so notifications are sent without having to check the box manually
* **Automatically send notifications when a post is updated**: Automatically checks notification box when updating posts so notifications are sent without having to check the box manually
* **Automatically send notifications when a page is published**: Automatically checks notification box when publishing pages so notifications are sent without having to check the box manually
* **Automatically send notifications when a page is updated**: Automatically checks notification box when updating pages so notifications are sent without having to check the box manually
* **Automatically send a push notification when I publish a post from 3rd party plugins**: Auto-send notifications from external publishing plugins
* **Mobile App Integration**: Send notifications to your mobile app subscribers using the same OneSignal App ID

### 3. Complete migration (Upgrading Users Only)

<Note>
  **New installations can skip this step. If you're upgrading from v2+, follow
  along...**
</Note>

<Warning>
  **Time-Sensitive**: Complete these steps ASAP to avoid users missing
  notifications during the transition.
</Warning>

<Steps>
  <Step title="After saving your OneSignal dashboard configuration, return to WordPress" />

  <Step title="Click Migration Completed in the plugin settings" />

  <Step title="Click Save Settings to finalize the upgrade" />
</Steps>

<Frame caption="Click Migration Completed to finalize your plugin upgrade">
  <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/docs/01ba2d812c5757d50ee60885c45f229e2bba4ff2da42ba3fb0098ac5b5621eba-Screenshot_2024-12-19_at_2.33.31_PM.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=2d55f565db10c116fed39ca3f5930cb4" width="1059" height="312" data-path="images/docs/01ba2d812c5757d50ee60885c45f229e2bba4ff2da42ba3fb0098ac5b5621eba-Screenshot_2024-12-19_at_2.33.31_PM.png" />
</Frame>

<Check>
  Setup complete! Click **Save Settings** to finish plugin configuration.
</Check>

***

## Testing your setup

<Tabs>
  <Tab title="Initial Test">
    1. **Visit your website** (avoid incognito/private browsing—users cannot
       subscribe in these modes) 2. **Look for the slidedown prompt** you
       configured

    <Frame caption="Your configured slidedown prompt should appear based on your timing settings">
      <img src="https://mintcdn.com/onesignal/jBdBk5XvQR5eKOks/images/docs/7aca650375517543ad8c80bedc0c75a224a51dd63e84c67798ab4b1812b01498-Screenshot_2025-02-24_at_9.58.05_AM.png?fit=max&auto=format&n=jBdBk5XvQR5eKOks&q=85&s=d937481d712d3340ba8ef9b25a274901" width="1600" height="700" data-path="images/docs/7aca650375517543ad8c80bedc0c75a224a51dd63e84c67798ab4b1812b01498-Screenshot_2025-02-24_at_9.58.05_AM.png" />
    </Frame>

    3. **Click the subscribe button** (labeled as "Subscribe" in this example)
    4. **Accept the browser permission** when prompted

    <Frame caption="Browser permission prompt (appearance varies by browser) is required for web push notifications">
      <img src="https://mintcdn.com/onesignal/KSCNwSpBCNSQ8xdF/images/docs/fac77534f9a5182d0a2351713a23f10f26f779ff5182c0c2c8a1289372dea9a9-Screenshot_2025-02-13_at_4.44.29_PM.png?fit=max&auto=format&n=KSCNwSpBCNSQ8xdF&q=85&s=60785d5a04fe7f2f5450fb05b414d5ee" width="1612" height="490" data-path="images/docs/fac77534f9a5182d0a2351713a23f10f26f779ff5182c0c2c8a1289372dea9a9-Screenshot_2025-02-13_at_4.44.29_PM.png" />
    </Frame>

    5. **Check for welcome notification** (if configured)

    <Frame caption="Welcome notification appears immediately after successful subscription">
      <img src="https://mintcdn.com/onesignal/tNi1OgLc_p9hiq7_/images/docs/1752c5e7341bbb505d93af428bba12e4042257cb518e281ccb887b1a415dbaee-Screenshot_2025-02-13_at_4.44.40_PM.png?fit=max&auto=format&n=tNi1OgLc_p9hiq7_&q=85&s=d9575a52cb6bfdb1ae770daf3bb82ed2" width="740" height="198" data-path="images/docs/1752c5e7341bbb505d93af428bba12e4042257cb518e281ccb887b1a415dbaee-Screenshot_2025-02-13_at_4.44.40_PM.png" />
    </Frame>
  </Tab>

  <Tab title="Verify Subscription">
    1. In your OneSignal dashboard, go to **Audience > Subscriptions** 2. You
       should see your web push [subscription](./subscriptions) marked as
       "Subscribed"

    <Frame caption="Successful subscriptions appear in your OneSignal dashboard audience">
      <img src="https://mintcdn.com/onesignal/4HyuQPBpu-4xjmQC/images/docs/cf9b6a27fb8a32c5228e9123646e6ad5ca5b3ceb4d74fd8cf42e016e36f67c5a-Screenshot_2025-02-13_at_4.52.19_PM.png?fit=max&auto=format&n=4HyuQPBpu-4xjmQC&q=85&s=b8152e5f84b8bcdda32888268bbede00" width="3006" height="788" data-path="images/docs/cf9b6a27fb8a32c5228e9123646e6ad5ca5b3ceb4d74fd8cf42e016e36f67c5a-Screenshot_2025-02-13_at_4.52.19_PM.png" />
    </Frame>
  </Tab>

  <Tab title="Send Test Message">
    1. Navigate to **Messages > Push** in your OneSignal dashboard 2. Create a
       **New Message** 3. Send a test notification to yourself 4. Verify the
       notification appears correctly See our [Push messaging guide](./push)
       for detailed instructions.
  </Tab>
</Tabs>

<Check>
  **Success!** Your WordPress site is now configured for web push notifications.
  Users will start appearing in your Subscriptions as they subscribe.
</Check>

**Next Steps:**

* Review [Web permission prompts](./permission-requests) for advanced customization
* Explore [Channel setup](./channel-setup) for email and SMS integration
* Set up [segmentation strategies](./segmentation) for targeted messaging

<Info>
  **Having Issues?** Check our [WordPress troubleshooting
  guide](./troubleshooting-wordpress-web-push) for common solutions.
</Info>

***

## Publishing notifications

When you schedule a post to be published, OneSignal will also schedule a push notification to be sent to your subscribers at the scheduled time. If you reschedule the post, the push notification will be canceled and a new push will be scheduled for the new time.

You can view your scheduled and cancelled notifications in the OneSignal dashboard under **Delivery > Scheduled Messages**. See [Push message reports](./push-notification-message-reports) for more details.

### Basic post notifications

When creating or editing a WordPress post, locate the **OneSignal Push Notifications** metabox (usually at the bottom or sidebar of the post editor).

<Frame caption="OneSignal Push Notifications metabox—drag to reposition if needed">
  <img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/bd1282759632bbd7226b5fe8edeaa67c43e812b08d3c4e76b2f355ba5e8d9ba6-Screenshot_2025-02-13_at_4.37.19_PM.png?fit=max&auto=format&n=9_Q1FZLh6C0BFLq-&q=85&s=0291719ad3fff0c69c77bcf606a4181d" width="2046" height="1326" data-path="images/docs/bd1282759632bbd7226b5fe8edeaa67c43e812b08d3c4e76b2f355ba5e8d9ba6-Screenshot_2025-02-13_at_4.37.19_PM.png" />
</Frame>

**To send a notification:**

* Check **"Send notification when post is published or updated"**
* Uncheck to skip sending a notification for that post

### Audience targeting

#### Send to all subscribers (default)

By default, notifications go to all push [subscribers](./subscriptions).

#### Send to specific segments

Target specific audiences using [segments](./segmentation) you create in **OneSignal Dashboard > Audience > Segments**.

**If you set up categories in Step 3**, create corresponding segments:

1. Go to **Audience > Segments** in your OneSignal dashboard
2. Create segments using your tag keys, eg:
   * **News Segment**: Tag `news` is `1`
   * **Deals Segment**: Tag `deals` is `1`

<Frame caption="Tags are case-sensitive! 'news' and 'News' are different tags">
  <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/e7c2b21714e2de8653ac569fc65eb929988f5ccede8429168a40cae0067d893d-Screenshot_2025-02-18_at_4.45.19_PM.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=361fb5f307e412e28b1f3da26c4682d3" width="1446" height="926" data-path="images/docs/e7c2b21714e2de8653ac569fc65eb929988f5ccede8429168a40cae0067d893d-Screenshot_2025-02-18_at_4.45.19_PM.png" />
</Frame>

1. After creating segments, refresh your WordPress post editor
2. Select your target segment from the dropdown

<Frame caption="Select specific segments to target relevant user groups">
  <img src="https://mintcdn.com/onesignal/6tscVAtiSqz353kV/images/docs/9cb2736bc8b318d1de60b5b40887db8adda8f7797289bb0ad00d8e98e9e9c902-Screenshot_2025-02-19_at_10.36.16_AM.png?fit=max&auto=format&n=6tscVAtiSqz353kV&q=85&s=551c8c99851ad4fc431abf0e30084aa5" width="2030" height="796" data-path="images/docs/9cb2736bc8b318d1de60b5b40887db8adda8f7797289bb0ad00d8e98e9e9c902-Screenshot_2025-02-19_at_10.36.16_AM.png" />
</Frame>

<Check>
  **Advanced Segmentation**: Create segments based on user behavior, location,
  device type, and more. [Tags](./add-user-data-tags) provide the most
  flexibility for custom user data and personalization.
</Check>

### Customizing notification content

#### Default behavior

* **Title**: Uses your WordPress site title (Settings > General)
* **Message**: Uses the post title
* **Image**: Uses the post's featured image (if set)
* **URL**: Links to the published post

#### Custom content

Check **"Customize notification content"** to override defaults:

<Frame caption="Customize notification title, content, and other elements">
  <img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/40837af4e6fefa7d4303f5a3d49992396eb152cec5fd2420d7064aecef32c1af-Screenshot_2025-02-19_at_10.48.18_AM.png?fit=max&auto=format&n=_KaXe4GQkxsEfa17&q=85&s=8fef18d9723782c41604c358d69723ee" width="2064" height="1114" data-path="images/docs/40837af4e6fefa7d4303f5a3d49992396eb152cec5fd2420d7064aecef32c1af-Screenshot_2025-02-19_at_10.48.18_AM.png" />
</Frame>

**Example result:**

<Frame caption="Customized push notification as it appears to users">
  <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/a5011ec82798e7b6b31a9c5e2a26d2fb98a2c17dbc3fb0cb9895453f74d3240a-Screenshot_2025-02-19_at_10.49.26_AM.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=f1bbce88aeba84939032658beef5cf4d" width="740" height="198" data-path="images/docs/a5011ec82798e7b6b31a9c5e2a26d2fb98a2c17dbc3fb0cb9895453f74d3240a-Screenshot_2025-02-19_at_10.49.26_AM.png" />
</Frame>

### Add a Custom Post Type to OneSignal WordPress Plugin

#### Find your custom post type name

Look at your browser's address bar when creating a new post. The URL will look like:

```
https://yoursite.com/wp-admin/post-new.php?post_type=your_custom_type
```

The value of the `post_type` parameter (for example, `your_custom_type`) is the exact name you'll need to add in the OneSignal plugin's settings.

#### Add to OneSignal settings

1. Go to **OneSignal > Settings** in WordPress admin
2. In **Advanced Settings**, add your custom post type names to the **Custom Post Types** field
3. Save settings

<Note>
  **Common examples:** `product` (WooCommerce), `tribe_events` (Events
  Calendar), `portfolio`{" "}
</Note>

## Mobile app integration

If you have a mobile app using the same OneSignal App ID:

1. Enable **"Send notification to Mobile app subscribers"** in plugin settings
2. In the post metabox, add a **Mobile URL** for [deep linking](./deep-linking)
3. Mobile users will be directed to your app instead of the web browser

<Check>
  **Ready to Scale**: Explore [advanced push strategies](./push) and
  [automated journeys](./journeys-overview) for sophisticated notification
  campaigns.
</Check>

<Warning>
  **Notifications Not Appearing?** Check our [Web push troubleshooting
  guide](./notifications-not-shown-web-push) for solutions.
</Warning>

***

## FAQ

<Accordion title="How do I disable prompts on specific pages?" icon="circle-chevron-down">
  **Note**: This method only works with slidedown and native permission prompts, not bell or custom link prompts.

  1. In your OneSignal dashboard, go to **Settings > Push & In-App > Web Settings**
  2. Select your prompt from the **Permission Prompt Setup** table
  3. Uncheck **Auto Prompt** and click **Done**

  <Frame caption="Disable Auto Prompt to manually control when prompts appear">
    <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/814f50f2de90ad37c5213f963cd9dca9214b5dcc708650269d139254d55a9985-Screenshot_2025-02-13_at_5.06.27_PM.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=bd44f572649f92e94a98dbe772f5973b" width="712" height="840" data-path="images/docs/814f50f2de90ad37c5213f963cd9dca9214b5dcc708650269d139254d55a9985-Screenshot_2025-02-13_at_5.06.27_PM.png" />
  </Frame>

  1. Scroll down, click **Save**, then **Finish**
  2. Add [custom JavaScript code](./web-sdk-reference#slidedown-prompts) to specific pages where you want prompts to appear

  This gives you complete control over prompt timing and placement. See [Web permission prompts](./permission-requests) for implementation details. here
</Accordion>

<Accordion title="Can I send notifications to mobile app subscribers?" icon="circle-chevron-down">
  Yes! If your mobile app uses the same OneSignal App ID:

  1. Enable **"Send notification to Mobile app subscribers"** in the WordPress plugin settings
  2. When publishing posts, use the **Mobile URL** field in the OneSignal metabox to specify deep links
  3. Without a custom Mobile URL, users will be directed to your website

  This feature enables cross-platform messaging from a single WordPress interface.
</Accordion>

<Accordion title="How do I send email or SMS from WordPress?" icon="circle-chevron-down">
  The WordPress plugin currently supports push notifications only. For email and SMS:

  1. **Email**: Follow our [Email setup guide](./email-setup), then use [Email messaging tools](./email-messaging)
  2. **SMS**: Follow our [SMS setup guide](./sms-setup), then use [SMS messaging tools](./sms-messaging)

  Both channels can be managed from the same OneSignal dashboard alongside your push notifications.
</Accordion>

<Accordion title="Why aren't my prompts working after migration?" icon="circle-chevron-down">
  **Caching Issues**: WordPress caching may delay migration changes.

  **Solution:**

  **Step 1:** Right-click on your website and select **Inspect**

  **Step 2:** Go to the **Network** tab

  **Step 3:** Check **"Disable cache"**

  <Frame caption="Disable browser cache to force loading updated files after migration">
    <img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/34b7e61edec0e1fec8954fec630ca0dc60459ad15d9472b5622b5e461b791256-Screenshot_2024-12-20_at_3.02.43_PM_1.png?fit=max&auto=format&n=_KaXe4GQkxsEfa17&q=85&s=9d7c9c09a6908cecf53578b1ba882342" width="777" height="156" data-path="images/docs/34b7e61edec0e1fec8954fec630ca0dc60459ad15d9472b5622b5e461b791256-Screenshot_2024-12-20_at_3.02.43_PM_1.png" />
  </Frame>

  **Step 4:** Refresh your website to see current configuration

  **Step 5:** Clear your WordPress cache plugin settings if applicable
</Accordion>

<Accordion title="What does `A bad HTTP response code (404)` error mean?" icon="circle-chevron-down">
  This error indicates incomplete migration:

  <Frame caption="404 error in browser console indicates incomplete migration process">
    <img src="https://mintcdn.com/onesignal/jFWn5xzleD8du3j6/images/docs/5cf024c8bd09be6d420f85f846feef7242302c2052046f283ddeed09f73562d1-Screenshot_2024-12-20_at_3.11.58_PM_1.png?fit=max&auto=format&n=jFWn5xzleD8du3j6&q=85&s=5cb3f5dac155fe97a0a1b3051a138242" width="1136" height="252" data-path="images/docs/5cf024c8bd09be6d420f85f846feef7242302c2052046f283ddeed09f73562d1-Screenshot_2024-12-20_at_3.11.58_PM_1.png" />
  </Frame>

  **Solution:**

  1. Ensure you've saved your OneSignal dashboard configuration
  2. In WordPress, click **"Migration Completed"** in the plugin settings
  3. Click **Save Settings** to finalize the upgrade

  **This error only affects users upgrading from version 2.x.x.**
</Accordion>

<Accordion title="Can I modify the notification parameters before sending?" icon="circle-chevron-down">
  Yes, you can use the `onesignal_send_notification` filter.

  <Info>
    Place custom PHP code in `wp-content/mu-plugins/onesignal-custom.php`. This
    ensures its loads correctly and prevents it from being overwritten by updates.
  </Info>

  ```php  theme={null}
  <?php

  add_filter('onesignal_send_notification', function($fields, $post_id) {

    // Include any properties mentioned in the Create Notification API Reference:
    // https://documentation.onesignal.com/reference/push-notification eg:

    // Add action buttons
    $fields['web_buttons'] = array(
      array(
        "id" => "read-more",
        "text" => "Read More",
        "url" => get_permalink($post->ID)
      )

    // Return the modified fields array
    return $fields;

  }, 10, 2);
  ```

</Accordion>

***

Built with [Mintlify](https://mintlify.com).
