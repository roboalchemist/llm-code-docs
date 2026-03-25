# Source: https://documentation.onesignal.com/release-notes/changelog.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Changelog

> Learn about the latest updates to OneSignal.

Follow along with updates across OneSignal. We're launching new features and improving our product all the time!

<Update label="February 9 2026" tags={["Push"]}>
  Huawei Badge Parameter Support

  We now support app icon badges on Huawei (HMS) devices via both the API and dashboard.

* What's new: Three new parameters on `Notification#Create`
  * `huawei_badge_class` — the app's launcher activity class name (required for badge)
  * `huawei_badge_set_num` — set the badge to an exact number (0–99)
  * `huawei_badge_add_num` — increment the badge by a specific amount (1–99)

  On the dashboard, you'll see a new Badge option under Send to Huawei Android with "Don't set" / "Set to" / "Increase by" options.

* Good to know:
  * Setting `huawei_badge_set_num` to 0 clears the badge
  * If neither set nor add is specified, the badge increments by 1 by default
  * Huawei does not auto-clear badges when the app opens
</Update>

<Update label="January 29 2026" tags={["Segments", "Users", "Subscriptions"]}>
  API Documentation Improvements

* New API endpoint: [View Segment](/reference/view-segment) - Retrieve details of a specific segment by ID, including optional segment filter details.
* New API endpoint: [Update Segment](/reference/update-segment) - Update an existing segment's name and/or filters programmatically.
* Fixed JSON example formatting across multiple API reference pages for improved readability:
  * Segments API: view-segments, create-segments, delete-segments
  * Users API: create-user, view-user, update-user, delete-user
  * Subscriptions API: create-subscription, delete-subscription, transfer-subscription, unsubscribe-with-token, create-alias-by-subscription
</Update>

<Update label="January 26 2026" tags={["Dashboard", "Privacy", "Analytics"]}>
  Audit Logs are now available!

* Customers now have the ability to determine exactly what's happening across their OneSignal account. Audit Logs gives them a complete timeline of every action taken in their organization—who did what, when, and from where.
* Track 50+ action types including:
  * Authentication events (login, logout, API key operations)
  * Message activity (notifications sent, canceled, A/B tests, Journeys)
  * Team changes (member added, role changed, removed)
  * Configuration updates (webhooks, segments, templates, integrations)
  * Billing & subscription events
* Powerful filtering:
  * Search by team member email
  * Filter by action type, app, IP address, or item type
  * Custom date ranges with presets
  * Shareable filtered URLs—customers can collaborate with their team instantly
* Deep visibility:
  * Expandable rows reveal 30+ fields: IP address, browser, location, correlation ID, API version, and more
  * Available at both App and Organization levels
  * Quick-access links from Journeys, Segments, Templates, Notifications, and more
* Retention:
  * Legal & Security package: 90-day lookback
  * All other plans: 2-day lookback
* Perfect for security audits, debugging, and understanding team activity at a glance.
</Update>

<Update label="January 9 2026" tags={["Analytics"]}>

* Standardized time series for charts are now available for:
  * Event Streams and webhooks
  * Email delivery reports
  * SMS/RCS delivery reports
</Update>

<Update label="December 22 2025" tags={["Analytics", "Push"]}>

* Confirmed Delivery Now Available On Engagement Trends
  * Customers with access to confirmed delivery can now see confirmed delivery on the Engagement Trends Time Series Chart.
  * This missing data was a common point of confusion for customers. They could see confirmed delivery & click through rate, but had no access to the total confirmed deliveries metric.
  * This additional data point gives customers confidence in the rates we're showing and helps with confusion on the difference between "delivered" and "confirmed delivery" for push notifications.
</Update>

<Update label="December 12 2025" tags={["Integrations"]}>

* New integration - Self-serve Snowflake data export
  * OneSignal customers can now effortlessly sync their app’s message event data—including push, email, in-app, and SMS—directly to Snowflake without going through customer support
  * The legacy Snowflake documentation remains available for existing implementations
</Update>

<Update label="December 8 2025" tags={["Live Activities", "Integrations"]}>
  Live Activities in Event Streams & Integrations

  Live Activities Analytics provides two key capabilities to optimize customers' live activity strategy:

  1. Better Troubleshooting with Confirmed Delivery
     Gain visibility into whether devices actually received live activity updates. Confirmed delivery tracking identifies delivery issues quickly to understand the true reach of live activities.
     Available in:

* Individual message reports with per-device confirmation
* Data exports to BI tools (through event streams and integrations)

  1. Deeper Engagement Insights with data exports to integrations & event streams
     Answer critical questions about how users interact with your live activities:

* How many users engaged with my live activity over its duration?
* When did users drop off?
* What was the peak engagement time?
* When did users click? (coming soon)

  Export live activity data to BI tools to analyze engagement patterns, optimize timing, and improve future campaigns.
</Update>

<Update label="December 5 2025" tags={["Analytics", "Custom Events"]}>
  We've launched a new [Metrics Glossary](/docs/en/analytics-metrics-glossary) in our documentation. This resource provides a single source of truth for delivery metric definitions, helping both our team and customers understand our metrics consistently across dashboards, APIs, and exports.
  While we continue working toward unified terminology across all touch points, this glossary establishes clear mappings and definitions as they exist today, making it easier for customers to navigate our current analytics landscape.

  Custom Events in User Activity Timeline
  Custom events are now visible per User on their profile page in a dedicated tab. You can:

* Filter by event type and event source
* Filter by date, to any time window in the past. Only limiting factor is customer's own events retention window setting!
* Expand each event to see the full payload
* Click through to the events index to see that event type's config and full cross-user activity log

  This is important because:

* It helps paint the complete picture of user activity. At a basic level, customers ask the question, "what's going on with this user?" and this helps answer it.
* Especially useful for zoomed-in troubleshooting, auditing, what-happened analysis.
* Please note: this will only be visible to customers in Custom Events early access, but will be available to all as they gain access to Custom Events
</Update>

<Update label="November 26 2025" tags={["Dashboard"]}>
  UX Improvements Now Live

  1. Row-Level Linking
     You can now click anywhere on a table row to navigate to its destination, instead of having to click a specific cell. This makes navigation faster and more intuitive.
  2. Row Highlighting on Hover
     All tables now highlight the entire row on hover, helping users track data more easily and reducing visual strain when scanning wide tables.
  3. Improved Responsiveness
     The actions column has been narrowed to preserve horizontal space and is now right-aligned at the end of every table.
     It also features sticky, floating behavior — especially useful on smaller screens where horizontal scrolling is required.
     Some tables better truncate long text (e.g., lengthy message names) more effectively to maintain a clean layout.
  4. Refined Sorting UX
     Updated sort icons make the sort direction easier to interpret. Clicking anywhere on a column header now toggles sorting, improving ease of use.
  5. Unified Column Visibility Menu (Applies to Journeys, Users, Subscriptions)
     Tables with customizable columns now use a consistent, cleaner UI. Column changes update live as you toggle them.
  6. Updated Search Bar UI
     The search bar now aligns with design standards, featuring a left-aligned search icon, and a button that shows after typing for easy input clearing.
  7. Improved Pagination Formatting
     Pagination controls now use comma formatting for large numbers, improving scannability and readability.

  Core Component Update
  Many of the enhancements above come from migrating these tables to our core design system’s DataTable component. Sorting and filtering improvements for tables are consistently among the most requested features we receive. While these updates don’t introduce new sorting or filtering behavior yet, this component upgrade provides a more consistent experience for the functionality we have today, and does lay the foundation for Product teams to build more advanced table capabilities once those initiatives are prioritized.

  Coming Soon

* Most tables across the Dashboard already include these improvements. A few remaining areas still require component updates before they can adopt the full set of new enhancements:
  * In-app index
  * Templates index
  * Audience activity table
  * A/B tests stats table
</Update>

<Update label="November 12 2025" tags={["Templates", "Analytics"]}>
  UX Enhancement: Duplicate Templates Directly from the Editor
  In usability tests and dogfooding sessions, we noticed users often duplicate Journey nodes and then edit their templates. Previously, you had to exit the template editor and duplicate the template from the index view, an extra step that interrupted the workflow.
  Now, you can duplicate templates directly from the actions dropdown in the template editor. This small but meaningful improvement streamlines your editing experience and makes iteration faster. While our long-term goal is to enable template/content editing directly within Journeys, this enhancement is a great step in that direction.

  New Platform Filters for Engagement Trends & Subscription Trends
  You can now filter push engagement trend data by platform (iOS, Google Android, Huawei, etc.) to get a more granular view of performance across specific devices.
  In the spirit of our Analytics Consistency project, we've also brought this same filtering experience to Subscription Trends.

  Analytics Consistency: Standardized Time Series Chart Filters
  We're standardizing filter options across our time series charts, giving customers a consistent experience and clear access based on their plan.
  Key Changes:

* All charts will share the same set of granularity and look back filters
* Consistent casing and terminology used on all filters
* Consistent upgrade experience for customers on plans with limited access
    As an example, Subscription Trends now supports a 2 year look back after the change.

  Charts where we've already rolled out these changes:

* Engagement Trends
* Subscription Trends
* Global Outcomes
* Push Delivery
* All Template Reports
* Coming Soon:
* Email Delivery
* SMS Delivery
* Journeys Reports

  Look back access based on plan type:

* Free: 30 days
* Growth: 90 days
* Professional: 1 year
* Enterprise: 2 years
* Custom: Up to 90 days (based on plan types above)
</Update>

<Update label="October 6 2025" tags={["Journeys"]}>
  Nice UXE on Journey Settings. We’ve updated the Journeys Settings Side panel to be more user friendly by adding a side navigation to keep each section in focus. This is in tandem with the eventuality of having more settings available to the user as we look towards Journey Goals, and more.  We will accompany this release with an intercom slide letting the user know we have updated the settings area as to give them a heads up due to the abrupt pattern change.

  Every Setting, In Focus: Journey Settings are now grouped and spotlighted, helping you zero in on each choice without distraction.
</Update>

<Update label="October 2 2025" tags={["Journeys", "API"]}>
  Custom Events are now available to all customers on paid plans! You can now send custom events via our API or SDK, and use them to trigger actions in Journeys with your own event data.
</Update>

<Update label="September 21 2025" tags={["Segments"]}>
  Customers can now pause a segment that's counting towards their segments entitlement even though it's only being used in an archived journey or paused IAM. We also made it even easier to pause segments, if the user wants to pause a segment, we'll help the user pause or archive the active IAMs or journeys stopping the user from pausing a segment.
</Update>

<Update label="September 9 2025" tags={["Email"]}>
  Deactivate email senders

  Deactivate email domains that are no longer in use or were set up incorrectly. This includes fallback handling for your email templates and scheduled sends to make sure you don't break them by removing a domain, just in case it was being used more widely than you anticipated.
</Update>

<Update label="August 29 2025" tags={["Personalization", "Email", "Templates"]}>
  Personalize emails with real-time Data Feeds

  You can now use Data Feeds to pull live content from your APIs directly into emails at send time. No more static CSVs or preloaded tags — every message can include the latest account details, product recommendations, or order updates.

  Available in the email template composer for emails sent via Journeys, Data Feeds includes preview tools and error handling to keep sends smooth.

  👉 See how to set up [Data Feeds](/docs/en/data-feeds)
</Update>

<Update label="August 04 2025" tags={["Journeys", "Integrations", "AI"]}>
  You can now hold users in a Journey step until specific conditions are met before they move forward with the *Wait Until* action. This new feature allows you to:

* Hold users at a step until they enter a segment or trigger a message event (such as a specific message being delivered, opened, or clicked).
* Add multiple conditions and branch users based on whichever condition they meet first.
* Set an expiration path that moves users forward or removes them from the Journey if none of the conditions are met within your chosen timeframe. This gives you greater flexibility and control over how users progress through your Journeys. Learn more: [Journeys Actions](/docs/en/journeys-actions)

  AI Composer Push Notifications
  You can now generate or improve push notification message copy using the AI message composer. This update helps you craft high-performing content without leaving OneSignal. When creating a new push notification, select AI-generated push button to get started. To improve existing copy, select “Refine” in the Title, Subject, or Message fields.

  New [Integrations](/docs/en/integrations) index page contains the following enhancements:

* Filtering by type of integration
* Filtering by Inbound/Outbound directions of data flow
* Includes our new inbound DWH/Data ingestion options for custom events
</Update>

<Update label="July 07 2025" tags={["Segments"]}>

* Quickly identify and manage segments tied to campaigns
  * We’ve made it easier to clean up outdated segments.
  * Previously, you couldn’t delete a segment if it was tied to an In-App Message (IAM) or Journey, even if that campaign was paused or archived. Now, when you try to delete a segment, you’ll see a modal listing all IAMs and Journeys that are preventing deletion.
  * This helps you quickly locate and update the associated campaigns, so you can keep your workspace clean and organized without having to hunt through every Journey or IAM.
</Update>

<Update label="June 30 2025" tags={["Segments"]}>

* Segment users based on real message engagement
  * You can now create user segments based on how they interacted with previous messages across push, email, SMS and in-app.
  * This update adds a new Message Event filter that allows you to segment users based on events like email opens, push clicks, SMS failures, and more - without relying on tags or external tools.
  * Available on all paid plans.
  * See [Segmentation](/docs/en/segmentation#message-event-filters) for more details.
</Update>

<Update label="June 27 2025" tags={["Documentation"]}>

* New documentation with Mintlify!
  * We've updated our docs!
  * New AI features and easier readability.
  * Updated API reference and openapi spec.
  * New Tutorials page with common use cases and step-by-step details to get you setup quickly!
</Update>

<Update label="June 18 2025" tags={["In-app messages", "Analytics"]}>

* Track In-App engagement trends alongside push, email, and SMS
  * Customers can now see In-App Message impressions, clicks, and click-through rates directly in the Engagement Trends chart. This update gives marketers a unified view of how users are interacting with all message types over time—including In-App—making it easier to spot trends, report on performance, and optimize messaging across channels.
  * With this update, In-App engagement data is now included alongside push, email, and SMS across all views in the Engagement Trends chart. Stats are grouped by day and support up to two years of data (depending on plan). This data is exportable via CSV just like other channels, and can be filtered to look at specific date ranges or message types.
  * This feature is available to all customers.
</Update>

<Update label="June 12 2025" tags={["Email", "Analytics"]}>

* Unlock deeper email engagement insights with multi-link tracking
  * Customers can now track engagement on every individual link within their emails. This update gives customers a much clearer view into what content or messaging is working so they can improve email performance over time.
  * Previously, when customers included multiple links within an email, they could only view total click counts across all links. Now, they can see which specific links get the most engagement and how links perform inside journeys. This helps them refine content and messaging strategies.
  * Multi-link tracking is automatically applied to most emails created in the Drag & Drop or HTML editor. Link-level performance metrics will also be available for emails sent using a template and emails in a Journey.
  * This feature is available to all customers with access to email.
</Update>

<Update label="May 23 2025" tags={["Analytics"]}>

* View and optimize message performance with Template Analytics
  * OneSignal customers can quickly assess how individual templates are performing across all messages, without needing to download and stitch together separate reports.
  * When users click into a template, they now land on a detailed analytics view showing Delivered, Unique Opens, Unique Clicks, and Unsubscribes. They can track performance over time, filter by platform, explore delivery breakdowns like Failed or Capped, and review a list of messages that used the template.
  * Template analytics is especially useful for:
    * Marketers who test and iterate on message content
    * Developers who need visibility into transactional message delivery
    * High-volume senders seeking scalable insights
  * Transactional visibility is a key differentiator that sets us apart from Firebase and other open source solutions. Customers can now answer questions like “How many Account Confirmation emails did I send last week?” or “What was the click-through rate on my Password Reset messages?”
  * Important note: For templates created before April 17, 2025, enhanced metrics are only available for messages sent after that date. Customers can use the “Show historical data” toggle at the top of the page to see earlier performance data.
  * The feature is live and available by default. Reporting history varies by plan:
    * Free: 30 days
    * Growth: 90 days
    * Professional: 1 year
    * Enterprise: 2 years
</Update>

<Update label="May 16 2025" tags={["Users"]}>

* Add users manually from the dashboard
  * You can now create new users directly from the *Users* tab in your OneSignal dashboard using a simple form. This update makes it easy to manually add a user with an email address, phone number, or both without needing an SDK, API call or CSV upload.
  * This is especially helpful for quickly testing campaigns or adding users who aren’t yet in your system.
</Update>

<Update label="May 14 2025" tags={["SMS"]}>

* Track SMS link performance directly in OneSignal
  * Customers can now track SMS link performance directly in OneSignal without needing third-party tools like Bit.ly or custom UTM parameters. This feature gives our customers a more streamlined, built-in way to measure engagement and optimize messages faster, removing friction and helping drive better results from their SMS efforts.
  * When composing an SMS message, customers simply click “Insert Trackable Link” and enter the full URL they want to send users to. OneSignal automatically shortens the link using the 1sgnl.co domain so it fits within SMS character limits and can be tracked.
  * All SMS users will have access to trackable links as part of their existing plan.
</Update>

<Update label="May 07 2025" tags={["Dashboard"]}>

* Simplify message organization with easier label management
  * Now you can add labels to your messages to help you organize and manage them.
  * See [Labels](/docs/en/labels) for more details.
</Update>

<Update label="May 01 2025" tags={["Templates"]}>

* Template analytics
  * You can now view and optimize template performance from a centralized reporting view. Click into any message template to view detailed performance data across every message a template is used in.
</Update>

<Update label="Apr 25 2025" tags={["Users"]}>

* Improved CSV Importer
  * **Real-time validation:** Get instant feedback on formatting errors before upload.
  * **Smart column mapping:** Easily align your CSV headers with OneSignal fields.
  * **Email suppression support:** Add or manage your suppression list directly in the file.
  * **Upload history:** View the status of your past imports for up to 30 days.
  * **Helpful templates:** Start quickly with a pre-built CSV example.
</Update>

<Update label="Apr 21 2025" tags={["Live Activities"]}>

* Fine-tune your Live Activities with new API parameters
  * You can now add more control, reliability, and speed to your Live Activities with three new parameters in the OneSignal API: - ios\_relevance\_score: Helps determine which Live Activity displays most prominently on iOS. - include\_aliases: Allows you to target individual users directly rather than relying on segment-based delivery. - idempotency\_key: Prevents the creation of duplicate Live Activities when retrying start requests if not using the OneSignal SDK.
</Update>

<Update label="April 14 2025" tags={["Integrations"]}>

* New integration - Databricks data export
  * OneSignal customers can now effortlessly sync their app’s message event data—including push, email, in-app, and SMS—directly to Databricks. This integration enables secure, automatic data transfer, allowing teams to unify their OneSignal messaging data with broader funnel insights. By centralizing this data in Databricks, customers can unlock deeper analytics, measure the impact of their messaging, and make more data-driven decisions with ease.
</Update>

<Update label="April 08 2025" tags={["SMS"]}>

* View opt-out status by sender and support transactional messaging even with marketing opt-outs
  * You can now see SMS opt-out status by sender, giving you better visibility and control when managing marketing and transactional messages.
  * With this update, you can:
    * View subscription status by individual sender for any phone number
    * Continue sending transactional messages (like OTPs or alerts) even if a user has opted out of marketing
    * Maintain deliverability and avoid carrier filtering by respecting opt-out preferences
  * This is especially useful if you manage separate senders for promotional and transactional use cases.
  * To access this feature, go to **Consent Management > Advanced Opt-out Settings** and turn off the setting that globally unsubscribes a user when they reply with an opt-out keyword.
  * *Note: This option is only available to customers using advanced opt-out settings for SMS.*
</Update>

<Update label="March 19 2025" tags={["Templates"]}>

* Easily find and select the right templates with visual previews
  * Quickly identify and select your email and in-app message templates with the new updated card view.
  * Instead of relying on template names alone, you can now see clear visual previews, making it easier to choose the right template at a glance.
</Update>

<Update label="March 12 2025" tags={["Integrations", "Push", "Privacy", "SMS", "Email"]}>

* Create users in OneSignal via HubSpot workflows
  * Keep your users in sync across HubSpot and OneSignal! With this new workflow action, you can now create users in OneSignal whenever a HubSpot workflow trigger fires. This enables you to queue up personalization details (such as data tags) and plan engagement strategies before a user even interacts with your mobile platform. Additionally, you can trigger an SMS or email via HubSpot while simultaneously creating a user in OneSignal—ensuring seamless and immediate engagement.
  * [HubSpot Documentation](/docs/en/hubspot)
* Push preview accuracy improvements
  * As operating systems update, they often introduce new changes in their push designs.
  * We've updated our previews so they match latest and greatest push notification designs across iOS (18), Android (15), Windows (11), macOS (Sequoia). This ensures you see what your users will see when testing in OneSignal.
* PII Masking of Emails and Phone Numbers
  * Protect user privacy and reduce compliance risks by masking personally identifiable information (PII) such as emails and phone numbers. With PII masking, your team can work securely while still analyzing campaign performance and sharing insights across teams.
  * OneSignal automatically masks phone numbers and emails in the dashboard and any data exported directly from the platform. However, PII masking does not currently apply to data accessed via API requests, external IDs, or data tags.
</Update>

<Update label="March 07 2025" tags={["SMS"]}>

* Verify & Lookup Phone Numbers
  * Sends the user a one-time verification code to ensure the customer owns the phone #
  * Confirms the phone number entered by a user at onboarding is valid
</Update>

<Update label="February 28 2025" tags={["Integrations", "Dashboard"]}>

* Added New Integration - [BigQuery Data Export](/docs/en/bigquery)
  * OneSignal customers can now effortlessly sync their app’s message event data—including push, email, in-app, and SMS—directly to BigQuery. This integration enables secure, automatic data transfer, allowing teams to unify their OneSignal messaging data with broader funnel insights. By centralizing this data in BigQuery, customers can unlock deeper analytics, measure the impact of their messaging, and make more data-driven decisions with ease.
* Channel subscriber counts have moved
  * The counts of subscribed counts for each channel have moved from the dashboard to the Subscriptions page in OneSignal. Now you will see the number of *Subscribed* subscriptions for each channel at the top of the Subscriptions page under Audience to get an overview of audience reach per channel in the context of your subscriptions.
  * If you still wish to view this information on the Dashboard, you can filter your Subscriptions trends chart by channel.
</Update>

<Update label="February 14 2025" tags={["SMS"]}>

* Improvements to Keywords
  * We've made a couple of improvements to our SMS keywords.
    * Segment by subscription status when sending a keyword to encourage converting your customers who are not yet subscribed into opting in to your SMS marketing messages
    * Setup an auto-responder for unrecognized keywords
</Update>

<Update label="February 12 2025" tags={["Dashboard", "Analytics"]}>

* New Engagement Analytics on the OneSignal Dashboard

  * Are you curious to learn more about how your end users engage with the messages you send from OneSignal? Head to your Dashboard to see the new Engagement Trends report.
  * With this report you will gain insight into how users engage with your messages across Push, Email, and SMS. Track click-through-rate, unsubscribes, and monitor trends over time to refine your messaging strategy and optimize communication frequency. This comprehensive report consolidates data from all message types (Dashboard, API, Journeys) for a clearer view of performance. Now available in your OneSignal dashboard!

    <Frame caption="New Engagement Analytics on the OneSignal Dashboard">
      <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/changelog/new-engagement-analytics-on-the-onesignal-dashboard.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=8d7bb5d90df3d7ef758b0de45d2cf10d" alt="New Engagement Analytics on the OneSignal Dashboard" width="809" height="478" data-path="images/changelog/new-engagement-analytics-on-the-onesignal-dashboard.png" />
    </Frame>

</Update>

<Update label="January 29 2025" tags={["Segments"]}>

* Sort segments by Last edited, Created at and more
  * Finding and managing your segments just got easier!
  * You can now sort segments by Last edited, Created at and more.
    * This update is especially valuable for customers who:
      * Maintain numerous segments
      * Frequently update their segment configurations
      * Need to identify and clean up outdated segments
      * Want to quickly find recently modified segments
</Update>

<Update label="January 27 2025" tags={["Email", "In-app messages"]}>

* Email Senders (Multi-Domain Sending)
  * Create distinct senders for different types of communications:
    * Keep your marketing campaigns separate from crucial transactional emails
    * Maintain different brand voices for various product lines
    * Optimize sender reputation for each type of communication
    * [Email Senders](/docs/en/senders)
* Improved In-app Message Analytics for Event Streams
  * We've added a new In-app Message Analytics for Event Streams.
</Update>

<Update label="January 21 2025" tags={["Email"]}>

* Email Intelligent Delivery
  * We've added intelligent delivery to email.
  * Transform your email engagement with OneSignal's latest breakthrough: Intelligent Delivery. This powerful new feature automatically determines the optimal time to reach each individual user, maximizing your email campaign's impact.
  * Our algorithm continuously learns from:
    * User open patterns
    * Click-through behavior
    * Real human interactions (excluding bot activity)
</Update>

<Update label="January 16 2025" tags={["Journeys"]}>

* Retirement of Automated Message for Free apps
  * Automated Messages are no longer supported and the feature has been retired in the free plan. Paid apps will continue to have access to this feature until further notice.
  * Active automated messages will remain live and continue functioning as expected. However, you can no longer create new automated messages, or reactivate paused automated messages. To build new automated sequences and enhance your campaigns, we recommend using [Journeys](/docs/en/journeys-overview).
</Update>

<Update label="January 15 2025" tags={["Journeys", "Templates"]}>

* Customize how your users re-enter split branches
  * Now you can customize how your users re-enter split branches. This feature is available for all Journeys.
  * [Journey Entry Triggers](/docs/en/journeys-actions)
* Improving New Message Experience
  * We improved the new message experience by adding a library of templates (get inspiration for your next push, in-app, email, or SMS), or quickly start from a template you've made, or a previous message.
</Update>

<Update label="January 03 2025" tags={["Push"]}>

* message.url - New Push Event Stream Property
  * `message.url` is now a supported property for push events. It enables the retrieval of the launch URL directly from your event stream payload.
</Update>

<Update label="December 24 2024" tags={["Journeys"]}>

* Journeys Multi-split Branching
  * Now you can set up more personalized paths in your Journey. Create up to 20 branches to test channels, content, timing, ordering, and more. Assign different weights to each branch, or easily distribute audiences evenly across all branches. See how different paths perform against each other or against a control group.
</Update>

<Update label="December 20 2024" tags={["WordPress", "Push"]}>

* WordPress Plugin v3
  * We've upgraded our Wordpress Web Push plugin to v3+. What's changed:
    * Upgrades the OneSignal Web SDK from version 15 to 16.
    * Setup more new prompts within the OneSignal dashboard, including the following. No custom code is required anymore to configure these.
      * Category Prompt
      * Email/Phone Slide Prompt
      * Custom Link Prompt.
    * When publishing a new post, check the "Send notification when post is published" box to send a push notification.
    * Choose which audience segment should receive notifications for each post.
    * Web Topics are included by default.
    * Send to mobile app subscribers, with an option to direct them to a different URL (Deep Link).
</Update>

<Update label="December 11 2024" tags={["Users", "SMS", "Analytics"]}>

* Improved Logs in Event Streams
  * We've improved the Event Streams feature to make troubleshooting simpler and faster. Now, you’ll find dedicated tabs for successful and failed events, making it easier to spot issues at a glance. Clear empty states show when there’s no data in either tab, and updated messaging ensures you know the logs display a sample of your data.
* SMS Keywords
  * We've added keywords for SMS. Keyword engagement enables quick, two-way communication, enhancing personalization, accessibility, and user satisfaction. It drives conversions and higher engagement with your subscribers. Add a data tag to the keyword, and segment based on their preferences to send more targeted SMS.
* Quickstart Segments

  * We are thrilled to launch three new segment templates designed to help you hit the ground running with proven strategies:
    * First-Time audience
    * Regional audience
    * Custom Audience based on tags
  * Our analysis of 6.3 billion message deliveries uncovered powerful insights. These templates are built to help you:
    * Create high-performing segments from day one.
    * Use proven filter combinations that drive higher engagement.

    <Frame caption="Quickstart Segments">
      <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/changelog/quickstart-segments.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=d985894187aeb5c00407a71a1948ad8d" alt="Quickstart Segments" width="1489" height="284" data-path="images/changelog/quickstart-segments.png" />
    </Frame>

</Update>

<Update label="December 02 2024" tags={["Email"]}>

* Email Quickstart Templates
  * We've added a library of quickstart templates for email. Explore our library of professionally crafted email templates, designed to inspire your creativity and elevate your email campaigns. Use them as a starting point to create impactful messages that drive conversions and engage your audience effectively.
</Update>

<Update label="November 27 2024" tags={["Journeys", "Dashboard"]}>

* Scheduling Journeys
  * Now you can schedule Journeys to send at a specific time. This feature is available for all Journeys.
* Settings Overview Page
  * Now you can access and manage all your settings in a centralized setting overview page. Platform-specific settings have been reorganized under their relevant channels for better clarity.
</Update>

<Update label="November 20 2024" tags={["Journeys"]}>

* Bulk Archive and Delete Journeys

  * Now you can bulk archive or delete Journeys from the Journeys index. Select up to 20 Journeys, and then choose an action you'd like to take to clean up Journeys you're no longer using.

    <Frame caption="Bulk Archive and Delete Journeys">
      <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/changelog/bulk-archive-and-delete-journeys.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=29e7d825e16974308ad58ff5af5b41de" alt="Bulk Archive and Delete Journeys" width="656" height="314" data-path="images/changelog/bulk-archive-and-delete-journeys.png" />
    </Frame>

</Update>

<Update label="November 06 2024" tags={["Analytics", "Email", "SMS", "Dashboard"]}>

* Improved Export for Global Outcomes
  * We've improved the export for Global Outcomes to include more data and make it easier to use in your reporting.
* Preview allows you to preview the content of a message and can be very helpful when you have a message with personalization (i.e. data tags, dynamic content, custom data). With preview, you can preview content from a specific test user's perspective, or with example custom data.
* Settings for Email & Side Navigation Updates
  * In the side navigation, you can now easily see your Push, SMS, and Email settings. What was once "Messaging" is now "Push" settings, and SMS and Email Settings will take you directly to your channel's settings.
  * For email, we've created a dedicated place to manage your email provider and senders. If you are a OneSignal mail user, you'll also be able to see your reputation and suppression lists here.
* SMS Usage
  * We've added SMS Usage in the Usage page. We've also added a breakdown so you can see the message type, and a breakout by inbound and outbound. You may see an unknown country if a segment failed to send.
</Update>

<Update label="October 02 2024" tags={["Journeys"]}>

* Add Notes on your Journeys
  * Now you can add notes to the steps of your Journeys to keep reminders and more effectively collaborate and share information with your team. This feature is available for all Journeys.
</Update>

<Update label="September 27 2024" tags={["Journeys", "SMS"]}>

* New Quickstart Journeys
  * We've added a new Quickstart Journeys to help you get started with Journeys. This feature is available for all Journeys.
* SMS Text-to-Subscribe
  * It's now easier to set up double opt-in and text-to-subscribe phone number collection experiences for your customers!
</Update>

<Update label="September 12 2024" tags={["Analytics"]}>

* Confirmed Click-Through-Rate (CCTR) metric

  * We have added a new metric to measure the CTR using Confirmed Delivery. Confirmed Click-Through-Rate (CCTR) is measured by (total clicks/confirmed delivered) \* 100%

    <Frame caption="Confirmed Click-Through-Rate (CCTR) metric">
      <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/changelog/confirmed-click-through-rate-metric.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=af58bb0b10a185c80abd2b71522c6f44" alt="Confirmed Click-Through-Rate (CCTR) metric" width="1206" height="134" data-path="images/changelog/confirmed-click-through-rate-metric.png" />
    </Frame>

</Update>

<Update label="September 06 2024" tags={["Analytics", "Users"]}>

* Export your Subscription Trends
  * Now you can export the data from your Subscription Trends report as a CSV. If you apply filters to the report, OneSignal will export based on the filters you've applied so that you can fine-tune the data that you use to evaluate your messaging audience.
</Update>

<Update label="August 05 2024" tags={["Email"]}>

* Email Saved Rows
  * Saved Rows are reusable content blocks that help streamline email creation and management. Many companies, especially those that have a lot of templates, prefer to use saved rows in their emails for consistency and to save time. Saved Rows are easily attached to new emails so you don't have to create the same information from scratch each time. And when things change, you just have to update the saved row, and your updates will automatically sync across all campaigns that have that saved row attached.
  * Common use cases include:
    * headers (logo, slogan)
    * footers (company details, social media links, mailing addresses)
    * disclaimers
    * other elements that are used across multiple campaigns
  * You can now save Email Drag-and-Drop rows to use across many Campaigns or Templates. These re-suable **Saved Rows** make it easy to sync updates across many emails at once. Click on the **Rows** tab of a Drag-and-Drop email, to view your **Saved Rows**. To save your first row, click the save icon in the edit, in the top right corner of the row.
  * We recommend you set up all of your templates to use saved rows for your header and footer so that you need to update the branding or content; you only have to make those edits once.
</Update>

<Update label="July 30 2024" tags={["Journeys"]}>

* Journeys now target anonymous users
  * Now, Journeys do not require External IDs to be set on subscriptions. Instead, Journeys will target your entire user base within OneSignal, including anonymous users. We recommend still configuring External IDs to identify individual users who have subscribed to multiple channels.
</Update>

<Update label="July 25 2024" tags={["SMS"]}>

* Have more visibility into SMS unsubscribes, resubscribes, and help keywords
  * We now make it easier to manage your Consent Keywords within Onesignal. Reach out to support if you'd like to update the default consent keywords and replies.
</Update>

<Update label="July 19 2024" tags={["Email"]}>

* Email Reply-to field now supports custom properties
  * Now you can use [Message Personalization](/docs/en/message-personalization) within the `reply-to`field on an email. This allows you to direct message replies to the right inbox and can be helpful if you are sending from different brands or across different countries.
</Update>

<Update label="July 16 2024" tags={["Analytics"]}>

* Push Failures and Unsubscribes in Audience Activity
  * Obtain a list of subscriptions that have faced errors - failures or unsubscribes, for a specific push notification in the push report page.
</Update>

<Update label="July 03 2024" tags={["Integrations", "Analytics"]}>

* Integrations: OneSignal Message Events can be sent to Twilio Segment
  * Customers can now select and send message events from OneSignal to sync back to their Twilio Segment account, making the Segment integration bidirectional.
* Use Audience Activity for Live Activities to get a list of recipients
  * Get a list of subscriptions that successfully or failed to receive a Live Activity on a Live Activity report page, which is accessible through the Delivery - Sent Index. This list can be exported as well.
</Update>

<Update label="June 06 2024" tags={["In-app messages"]}>

* In-app message audience activity
  * In the report page of an in-app message, you can now see which mobile subscriptions viewed (impression) or clicked on an in-app message. Audience activity is available for 30 days from the time the message is displayed
</Update>

<Update label="May 15 2024" tags={["Push"]}>

* FCM Expired Tokens > Increased Android Unsubscribes
  * On May 15, 2024, Google's FCM service will start to expire stale push tokens for devices that have been inactive for more than 270 days. You may see a spike in Android unsubscribes when sending notifications due to this change. Don't panic! These are devices that have not been online in over 270 days and are part of Google's [Best practices for FCM registration token management](https://firebase.google.com/docs/cloud-messaging/manage-tokens). If the device does come back online and opens your app, OneSignal will automatically resubscribe them to push if they were previously subscribed already.
  * See [FCM Expired Token FAQ](/docs/en/fcm-expired-token-faq) for more details.
</Update>

<Update label="April 29 2024" tags={["Push"]}>

* Configure more granular Frequency Capping rates for Push
  * Push notifications can now be capped at a rate of x notifications per any time frame (less than 1 week). Navigate to Settings > Messaging > Push Frequency Capping > Custom (in the time dropdown) to view these settings.
  * Read [Frequency Capping Documentation](/docs/en/frequency-capping) for more details.
</Update>

<Update label="April 11 2024" tags={["Live Activities"]}>

* Added Android Live Notifications
  * Android's Live Notifications deliver live, dynamic content in notifications to enhance user engagement and app interactivity. This is a feature similar to iOS's Live Activities feature (introduced with iOS 16), but uses its own set of tools and APIs that enable similar functionalities.
  * See [Android Live Notifications](/docs/en/android-live-notifications) for more details.
* Major improvements to Android SDK
* Push to start Live Activities
  * Live Activities can now be launched on a user's screen when the mobile app is in the background (app is not open). Live Activities can both be started and updated by a remote push notification.
  * [How to start a Live Activity with a remote push notification](/docs/en/live-activities)
</Update>

<Update label="April 01 2024" tags={["Journeys"]}>

* Added Audience Activity reports for Journeys
  * We have added Audience Activity reports for Journeys so you can get a closer look at which subscriptions were sent messages during a Journey. To view this report, click into a message report on your Journey. [Learn more here](/docs/en/journeys-analytics#audience-activity).
</Update>

<Update label="March 18 2024" tags={["Analytics"]}>

* Added a new Setup guide for Analytics
  * We have added a new Analytics Setup guide to our product documentation detailing how to track Confirmed Deliveries and set up Custom Outcomes with support from your development team.
</Update>

<Update label="March 12 2024" tags={["Push"]}>

* Mobile SDK Updates
  * We recommend updating to the latest SDK versions listed below to benefit from critical bug fixes, stability improvements, and new features. These updates include key enhancements across all platforms, including iOS 5.1.3 and Android 5.1.6, which improve concurrency safety, crash resilience, and background thread handling. The updates also include important API adjustments like more accurate property handling in the `PushSubscriptionState`.
</Update>

<Update label="February 16 2024" tags={["Journeys"]}>

* Journeys is now available on the Growth plan
  * Journeys is now available on the Growth plan. This means you can now create and manage Journeys with up to 100,000 users.
  * See [Journeys](/docs/en/journeys-overview) for more details.
</Update>

<Update label="February 12 2024" tags={["Email"]}>

* Added Auto Warm Up
  * We have added a new feature that allows you to automatically warm up your app when a user opens it. This feature is available for all OneSignal customers.
  * See [Email Warm Up](/docs/en/email-warm-up) for more details.
</Update>

<Update label="February 02 2024" tags={["Journeys", "Email"]}>

* Journeys has easier targeting based on user activity
  * We've added support for Segments with time-based rules (e.g., first session, last session, etc.) and also simplified targeting inactive users. Now you can target your inactive users by including a segment based on last session behavior.
* Email: Schedule Sends Across Different Timezones
  * Email campaigns can now be scheduled to send across different timezones. This feature is available for all OneSignal customers.
</Update>

<Update label="January 30 2024" tags={["Email"]}>

* Email now supports One Click Unsubscribe
  * Inbox Service Providers (ISP) like Gmail, Outlook, iOS Mail, and Yahoo! Mail, AOL, and Verison Mail require senders to provide a One Click Unsubscribe option. The unsubscribe button is rendered at the discretion of the ISP based on sending criteria, which may include a daily sending volume greater than 5,000 emails.
</Update>

<Update label="December 18 2023" tags={["Analytics", "Users", "Email"]}>

* Filter your messages with labels
  * Now you can filter your messages with [labels](/docs/en/labels). This feature is available for all OneSignal customers.
* CSV Importer can now update properties
  * CSV Importer for email now enables updates to user properties `language`, `country`, and `timezone_id`.
* Send more personalized messages and multi-language emails
  * [Dynamic Content Documentation](/docs/en/dynamic-content)
</Update>

<Update label="December 14 2023" tags={["Dashboard", "Journeys"]}>

* All OneSignal apps now belong to an Organization
  * We have added a new feature that allows you to manage your OneSignal apps within an Organization. This feature is available for all OneSignal customers.
  * See [Apps, Orgs, and Accounts](/docs/en/apps-organizations)
* Journeys now has better analytics
  * We've added a new Journeys Report. See [Journeys Analytics](/docs/en/journeys-analytics) for more details.
</Update>

<Update label="November 22 2023" tags={["Journeys"]}>

* Removed Journey Notifications from Delivery Reports and the View Notifications endpoint
</Update>

<Update label="October 04 2023" tags={["Integrations"]}>

* Added new integration - [Snowflake](/docs/en/snowflake)
  * OneSignal customers can now effortlessly sync their app’s message event data—including push, email, in-app, and SMS—directly to Snowflake. This integration enables secure, automatic data transfer, allowing teams to unify their OneSignal messaging data with broader funnel insights. By centralizing this data in Snowflake, customers can unlock deeper analytics, measure the impact of their messaging, and make more data-driven decisions with ease.
</Update>

<Update label="September 27 2023" tags={["Dashboard"]}>

* You can now save and continue
  * Changed the default option for saving a message to save work without exiting the message.
</Update>

<Update label="September 13 2023" tags={["In-app messages"]}>

* Added the ability to adjust the default padding for IAM blocks
  * Learn more about [IAM blocks](/docs/en/design-your-in-app-message)
* Added the ability to edit entry triggers and re-entry rules for live Journeys
  * Learn more about [Journey entry triggers](/docs/en/journeys-overview)
</Update>

<Update label="September 05 2023" tags={["Push", "Email", "Journeys"]}>

* Added ability to create multi-language push messages by pasting your CSV
  * Learn more about [Multi-language messages](/docs/en/multi-language-messaging)
* Added new "Editor" role permissions
  * Learn more about [Managing team members](/docs/en/manage-team-members)
* Added enhanced Journey message stats and reports.
  * Learn more about [Journey message stats and reports](/docs/en/journeys-analytics)
</Update>

<Update label="September 01 2023" tags={["Push", "Email"]}>

* Added a new feature to forward email templates to an app
  * Learn more at [Email Template Forwarding](/docs/en/email-template-forwarding)
* Added FCM v1 API support for Android Push Notifications
  * Learn more about [Android Firebase credentials](/docs/en/android-firebase-credentials)
</Update>

<Update label="August 15 2022" tags={["Push"]}>

* Android 13 changes
  * Android 13 introduces a runtime notification permission, meaning users must opt in to receive push notifications. Apps targeting Android 13 must explicitly prompt for permission at a time of their choosing, or the system will display the permission prompt automatically on first launch—often resulting in lower opt-in rates.
  * See [Android 13 Push Notification Developer Update Guide](/release-notes/android-13-push-notification-developer-update-guide) or our [Prompt for Push Permissions](/docs/en/prompt-for-push-permissions) guide for details.
</Update>

Built with [Mintlify](https://mintlify.com).
