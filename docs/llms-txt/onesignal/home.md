# Source: https://documentation.onesignal.com/docs/en/home.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# OneSignal Documentation

> Start building faster with OneSignal. Explore quickstarts, SDKs, messaging channels, API references, and advanced features like Journeys and Live Activities.

export const HomepageBanner = ({imgSrc, imgAlt, title, description}) => {
  return <div style={{
    height: "280px"
  }} class="relative flex items-center justify-center mb-3">
      <img style={{
    height: "280px",
    width: "100%"
  }} src={imgSrc} alt={imgAlt} class="absolute top-0 left-0 w-100 object-cover rounded-none" noZoom />
      <div class="z-10 text-center text-gray-200 flex flex-col items-center justify-center gap-4 h-min px-6">
        <h1 role="heading" aria-level="1" class="inline-block text-4xl sm:text-6xl font-extrabold text-color-white">
          {title}
        </h1>
        <p class="text-md sm:text-lg font-normal">{description}</p>
      </div>
    </div>;
};

<HomepageBanner imgSrc="/images/docs/docs-header-image.png" imgAlt="abstract graphic" title="OneSignal Documentation" description="Start building faster with comprehensive guides, example code, and platform overviews for omnichannel messaging." />

<div
  style={{
padding: '0 clamp(1rem, 10vw, 20rem)',
maxWidth: '100%',
boxSizing: 'border-box',
paddingBottom: '5rem'
}}
>
  <Columns cols={3}>
    <Card href="./quickstart-guide">
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '1rem' }}>
        <div style={{ flexShrink: 0, width: '40px', height: '40px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <img src="https://mintcdn.com/onesignal/s4WC_KzLxf8ornqq/images/svg/docs-icn-browser.svg?fit=max&auto=format&n=s4WC_KzLxf8ornqq&q=85&s=9d706254f1d14b7083e25c69918f735d" style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain' }} width="48" height="48" data-path="images/svg/docs-icn-browser.svg" />
        </div>

        <div>
          <div style={{ fontWeight: '800', fontSize: '1.1rem', marginBottom: '0.25rem' }}>
            Dashboard setup
          </div>

          <div>
            Set up your OneSignal project, configure platforms, and start sending notifications quickly.
          </div>
        </div>
      </div>
    </Card>

    <Card href="./developers">
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '1rem' }}>
        <div style={{ flexShrink: 0, width: '40px', height: '40px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <img src="https://mintcdn.com/onesignal/s4WC_KzLxf8ornqq/images/svg/docs-icn-sdk.svg?fit=max&auto=format&n=s4WC_KzLxf8ornqq&q=85&s=4f14b67a2d6a0a02bc4131093d066ed8" style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain' }} width="48" height="48" data-path="images/svg/docs-icn-sdk.svg" />
        </div>

        <div>
          <div style={{ fontWeight: '800', fontSize: '1.1rem', marginBottom: '0.25rem' }}>
            SDK setup
          </div>

          <div>
            Install and integrate the OneSignal SDK with your app to enable messaging capabilities.
          </div>
        </div>
      </div>
    </Card>

    <Card href="/reference/rest-api-overview">
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '1rem' }}>
        <div style={{ flexShrink: 0, width: '40px', height: '40px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <img src="https://mintcdn.com/onesignal/s4WC_KzLxf8ornqq/images/svg/docs-icn-code.svg?fit=max&auto=format&n=s4WC_KzLxf8ornqq&q=85&s=d6cc289d815972a037dafb35d24e41a8" style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain' }} width="48" height="48" data-path="images/svg/docs-icn-code.svg" />
        </div>

        <div>
          <div style={{ fontWeight: '800', fontSize: '1.1rem', marginBottom: '0.25rem' }}>
            API reference
          </div>

          <div>
            Explore our full API reference to automate messaging, manage users, and track delivery.
          </div>
        </div>
      </div>
    </Card>

    <Card href="./push">
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '1rem' }}>
        <div style={{ flexShrink: 0, width: '40px', height: '40px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <img src="https://mintcdn.com/onesignal/s4WC_KzLxf8ornqq/images/svg/docs-icn-push.svg?fit=max&auto=format&n=s4WC_KzLxf8ornqq&q=85&s=a9f9de833ba6090a599044decaed4fef" style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain' }} width="48" height="48" data-path="images/svg/docs-icn-push.svg" />
        </div>

        <div>
          <div style={{ fontWeight: '800', fontSize: '1.1rem', marginBottom: '0.25rem' }}>
            Push
          </div>

          <div>
            Set up and send mobile and web push notifications with advanced targeting and automation.
          </div>
        </div>
      </div>
    </Card>

    <Card href="./email-messaging">
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '1rem' }}>
        <div style={{ flexShrink: 0, width: '40px', height: '40px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <img src="https://mintcdn.com/onesignal/s4WC_KzLxf8ornqq/images/svg/docs-icn-email.svg?fit=max&auto=format&n=s4WC_KzLxf8ornqq&q=85&s=4a4d97ed68983fd3281c4bc4d7dda23f" style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain' }} width="48" height="48" data-path="images/svg/docs-icn-email.svg" />
        </div>

        <div>
          <div style={{ fontWeight: '800', fontSize: '1.1rem', marginBottom: '0.25rem' }}>
            Email
          </div>

          <div>
            Build, personalize, and send transactional and marketing emails using OneSignal.
          </div>
        </div>
      </div>
    </Card>

    <Card href="./sms-messaging">
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '1rem' }}>
        <div style={{ flexShrink: 0, width: '40px', height: '40px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <img src="https://mintcdn.com/onesignal/s4WC_KzLxf8ornqq/images/svg/docs-icn-sms.svg?fit=max&auto=format&n=s4WC_KzLxf8ornqq&q=85&s=cb9c97c4e56196ecf09291521e636cbc" style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain' }} width="48" height="48" data-path="images/svg/docs-icn-sms.svg" />
        </div>

        <div>
          <div style={{ fontWeight: '800', fontSize: '1.1rem', marginBottom: '0.25rem' }}>
            SMS & RCS
          </div>

          <div>
            Send time-sensitive SMS and RCS messages using OneSignal's powerful messaging engine.
          </div>
        </div>
      </div>
    </Card>

    <Card href="./in-app-messages-setup">
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '1rem' }}>
        <div style={{ flexShrink: 0, width: '40px', height: '40px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <img src="https://mintcdn.com/onesignal/s4WC_KzLxf8ornqq/images/svg/docs-icn-inapp-message.svg?fit=max&auto=format&n=s4WC_KzLxf8ornqq&q=85&s=052c7c7b516e4887bba4a88086750180" style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain' }} width="48" height="48" data-path="images/svg/docs-icn-inapp-message.svg" />
        </div>

        <div>
          <div style={{ fontWeight: '800', fontSize: '1.1rem', marginBottom: '0.25rem' }}>
            In-app messages
          </div>

          <div>
            Create in-app messages to engage users while they're active in your app.
          </div>
        </div>
      </div>
    </Card>

    <Card href="./live-activities">
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '1rem' }}>
        <div style={{ flexShrink: 0, width: '40px', height: '40px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <img src="https://mintcdn.com/onesignal/s4WC_KzLxf8ornqq/images/svg/docs-icn-live-activity.svg?fit=max&auto=format&n=s4WC_KzLxf8ornqq&q=85&s=6487af5944b550bd1f0c10b4abb88582" style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain' }} width="48" height="48" data-path="images/svg/docs-icn-live-activity.svg" />
        </div>

        <div>
          <div style={{ fontWeight: '800', fontSize: '1.1rem', marginBottom: '0.25rem' }}>
            Live Activities
          </div>

          <div>
            Deliver real-time updates to iOS Live Activities using OneSignal's SDK and API.
          </div>
        </div>
      </div>
    </Card>

    <Card href="./journeys-overview">
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '1rem' }}>
        <div style={{ flexShrink: 0, width: '40px', height: '40px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <img src="https://mintcdn.com/onesignal/s4WC_KzLxf8ornqq/images/svg/docs-icn-journey.svg?fit=max&auto=format&n=s4WC_KzLxf8ornqq&q=85&s=2b1b041cbe425007cc5b3b547f1bc246" style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain' }} width="48" height="48" data-path="images/svg/docs-icn-journey.svg" />
        </div>

        <div>
          <div style={{ fontWeight: '800', fontSize: '1.1rem', marginBottom: '0.25rem' }}>
            Journeys
          </div>

          <div>
            Design no-code messaging journeys across channels to onboard, retain, and re-engage users.
          </div>
        </div>
      </div>
    </Card>

    <Card href="./ab-testing">
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '1rem' }}>
        <div style={{ flexShrink: 0, width: '40px', height: '40px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <img src="https://mintcdn.com/onesignal/s4WC_KzLxf8ornqq/images/svg/docs-icn-filter.svg?fit=max&auto=format&n=s4WC_KzLxf8ornqq&q=85&s=4e7a8076805270fa53972287df561cd3" style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain' }} width="48" height="48" data-path="images/svg/docs-icn-filter.svg" />
        </div>

        <div>
          <div style={{ fontWeight: '800', fontSize: '1.1rem', marginBottom: '0.25rem' }}>
            A/B Testing
          </div>

          <div>
            Optimize your messaging with A/B tests to improve engagement and conversion rates.
          </div>
        </div>
      </div>
    </Card>

    <Card href="./analytics-overview">
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '1rem' }}>
        <div style={{ flexShrink: 0, width: '40px', height: '40px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <img src="https://mintcdn.com/onesignal/6fCcLQvxHVWEktgW/images/svg/docs-icn-analytics.svg?fit=max&auto=format&n=6fCcLQvxHVWEktgW&q=85&s=26c9741283ad0a724bf74193be86b03c" style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain' }} width="48" height="48" data-path="images/svg/docs-icn-analytics.svg" />
        </div>

        <div>
          <div style={{ fontWeight: '800', fontSize: '1.1rem', marginBottom: '0.25rem' }}>
            Analytics
          </div>

          <div>
            Track the success of your messaging campaigns with detailed analytics.
          </div>
        </div>
      </div>
    </Card>

    <Card href="./integrations">
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '1rem' }}>
        <div style={{ flexShrink: 0, width: '40px', height: '40px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <img src="https://mintcdn.com/onesignal/s4WC_KzLxf8ornqq/images/svg/docs-icn-puzzle.svg?fit=max&auto=format&n=s4WC_KzLxf8ornqq&q=85&s=c4d1c3152fd1a9c360d2fbae31fa4bcf" style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain' }} width="48" height="48" data-path="images/svg/docs-icn-puzzle.svg" />
        </div>

        <div>
          <div style={{ fontWeight: '800', fontSize: '1.1rem', marginBottom: '0.25rem' }}>
            Integrations
          </div>

          <div>
            Connect OneSignal to 3rd party tools, CRMs, data pipelines, and more via SDKs or webhooks.
          </div>
        </div>
      </div>
    </Card>
  </Columns>

  <div class="text-center text-gray-900 dark:text-gray-200 pt-10 mt-24 sm:mt-32 md:mt-40 pt-12 sm:pt-16 md:pt-20">
    <div role="heading" aria-level="1" class="inline-block text-2xl sm:text-3xl font-bold tracking-tight">
      Essential Concepts
    </div>

    <p class="mt-4 mb-12">Master these fundamental concepts to build effective messaging campaigns and understand OneSignal's core capabilities.</p>
  </div>

  <Columns cols={4}>
    <Card href="./add-user-data-tags">
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '1rem' }}>
        <div style={{ flexShrink: 0, width: '40px', height: '40px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <img src="https://mintcdn.com/onesignal/s4WC_KzLxf8ornqq/images/svg/docs-icn-people.svg?fit=max&auto=format&n=s4WC_KzLxf8ornqq&q=85&s=1e059dc850a7ca8e23799da5956943f2" style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain' }} width="48" height="48" data-path="images/svg/docs-icn-people.svg" />
        </div>

        <div>
          <div style={{ fontWeight: '800', fontSize: '1.1rem', marginBottom: '0.25rem' }}>
            User Tags
          </div>

          <div>
            Custom metadata attached to users to store preferences, behaviors, and properties for targeting.
          </div>
        </div>
      </div>
    </Card>

    <Card href="./segmentation">
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '1rem' }}>
        <div style={{ flexShrink: 0, width: '40px', height: '40px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <img src="https://mintcdn.com/onesignal/s4WC_KzLxf8ornqq/images/svg/docs-icn-people.svg?fit=max&auto=format&n=s4WC_KzLxf8ornqq&q=85&s=1e059dc850a7ca8e23799da5956943f2" style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain' }} width="48" height="48" data-path="images/svg/docs-icn-people.svg" />
        </div>

        <div>
          <div style={{ fontWeight: '800', fontSize: '1.1rem', marginBottom: '0.25rem' }}>
            Segmentation
          </div>

          <div>
            Dynamic groups of users based on criteria like behavior, location, tags, and subscription status.
          </div>
        </div>
      </div>
    </Card>

    <Card href="./users">
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '1rem' }}>
        <div style={{ flexShrink: 0, width: '40px', height: '40px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <img src="https://mintcdn.com/onesignal/s4WC_KzLxf8ornqq/images/svg/docs-icn-people.svg?fit=max&auto=format&n=s4WC_KzLxf8ornqq&q=85&s=1e059dc850a7ca8e23799da5956943f2" style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain' }} width="48" height="48" data-path="images/svg/docs-icn-people.svg" />
        </div>

        <div>
          <div style={{ fontWeight: '800', fontSize: '1.1rem', marginBottom: '0.25rem' }}>
            Users
          </div>

          <div>
            A User represents an individual with one or more subscriptions to messaging channels like push, email, and SMS.
          </div>
        </div>
      </div>
    </Card>

    <Card href="./subscriptions">
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '1rem' }}>
        <div style={{ flexShrink: 0, width: '40px', height: '40px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <img src="https://mintcdn.com/onesignal/s4WC_KzLxf8ornqq/images/svg/docs-icn-checkmark.svg?fit=max&auto=format&n=s4WC_KzLxf8ornqq&q=85&s=d99d35a8ae2bde356d35f447b8927019" style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain' }} width="48" height="48" data-path="images/svg/docs-icn-checkmark.svg" />
        </div>

        <div>
          <div style={{ fontWeight: '800', fontSize: '1.1rem', marginBottom: '0.25rem' }}>
            Subscriptions
          </div>

          <div>
            A subscription in OneSignal represents the specific channel or device through which a user can receive messages.
          </div>
        </div>
      </div>
    </Card>

    <Card href="./users#external-id">
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '1rem' }}>
        <div style={{ flexShrink: 0, width: '40px', height: '40px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <img src="https://mintcdn.com/onesignal/s4WC_KzLxf8ornqq/images/svg/docs-icn-people.svg?fit=max&auto=format&n=s4WC_KzLxf8ornqq&q=85&s=1e059dc850a7ca8e23799da5956943f2" style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain' }} width="48" height="48" data-path="images/svg/docs-icn-people.svg" />
        </div>

        <div>
          <div style={{ fontWeight: '800', fontSize: '1.1rem', marginBottom: '0.25rem' }}>
            External ID
          </div>

          <div>
            A unique identifier you assign to link a OneSignal user with your own user system or database.
          </div>
        </div>
      </div>
    </Card>

    <Card href="./users#onesignal-id">
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '1rem' }}>
        <div style={{ flexShrink: 0, width: '40px', height: '40px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <img src="https://mintcdn.com/onesignal/s4WC_KzLxf8ornqq/images/svg/docs-icn-people.svg?fit=max&auto=format&n=s4WC_KzLxf8ornqq&q=85&s=1e059dc850a7ca8e23799da5956943f2" style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain' }} width="48" height="48" data-path="images/svg/docs-icn-people.svg" />
        </div>

        <div>
          <div style={{ fontWeight: '800', fontSize: '1.1rem', marginBottom: '0.25rem' }}>
            OneSignal ID
          </div>

          <div>
            A unique UUID automatically generated by OneSignal to identify each user in the system.
          </div>
        </div>
      </div>
    </Card>

    <Card href="./message-personalization">
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '1rem' }}>
        <div style={{ flexShrink: 0, width: '40px', height: '40px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <img src="https://mintcdn.com/onesignal/s4WC_KzLxf8ornqq/images/svg/docs-icn-personalize.svg?fit=max&auto=format&n=s4WC_KzLxf8ornqq&q=85&s=fda3bc803bb703718dbe1d793a9f4d5d" style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain' }} width="48" height="48" data-path="images/svg/docs-icn-personalize.svg" />
        </div>

        <div>
          <div style={{ fontWeight: '800', fontSize: '1.1rem', marginBottom: '0.25rem' }}>
            Personalization
          </div>

          <div>
            The ability to customize message content using user data, tags, and dynamic content for relevant experiences.
          </div>
        </div>
      </div>
    </Card>

    <Card href="./deep-linking">
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '1rem' }}>
        <div style={{ flexShrink: 0, width: '40px', height: '40px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <img src="https://mintcdn.com/onesignal/s4WC_KzLxf8ornqq/images/svg/docs-icn-browser.svg?fit=max&auto=format&n=s4WC_KzLxf8ornqq&q=85&s=9d706254f1d14b7083e25c69918f735d" style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain' }} width="48" height="48" data-path="images/svg/docs-icn-browser.svg" />
        </div>

        <div>
          <div style={{ fontWeight: '800', fontSize: '1.1rem', marginBottom: '0.25rem' }}>
            Deep Linking
          </div>

          <div>
            Direct users to specific app screens or web pages with custom deep links and URLs.
          </div>
        </div>
      </div>
    </Card>

    <Card href="./multi-language-messaging">
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '1rem' }}>
        <div style={{ flexShrink: 0, width: '40px', height: '40px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <img src="https://mintcdn.com/onesignal/s4WC_KzLxf8ornqq/images/svg/docs-icn-web-push.svg?fit=max&auto=format&n=s4WC_KzLxf8ornqq&q=85&s=36cf63e17c920440a2ab409936962c7f" style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain' }} width="48" height="48" data-path="images/svg/docs-icn-web-push.svg" />
        </div>

        <div>
          <div style={{ fontWeight: '800', fontSize: '1.1rem', marginBottom: '0.25rem' }}>
            Multi-Language
          </div>

          <div>
            Send messages in multiple languages to reach global audiences effectively.
          </div>
        </div>
      </div>
    </Card>

    <Card href="./confirmed-delivery">
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '1rem' }}>
        <div style={{ flexShrink: 0, width: '40px', height: '40px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <img src="https://mintcdn.com/onesignal/s4WC_KzLxf8ornqq/images/svg/docs-icn-checkmark.svg?fit=max&auto=format&n=s4WC_KzLxf8ornqq&q=85&s=d99d35a8ae2bde356d35f447b8927019" style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain' }} width="48" height="48" data-path="images/svg/docs-icn-checkmark.svg" />
        </div>

        <div>
          <div style={{ fontWeight: '800', fontSize: '1.1rem', marginBottom: '0.25rem' }}>
            Confirmed Delivery
          </div>

          <div>
            Verification that a push notification was successfully delivered to and displayed on a user's device.
          </div>
        </div>
      </div>
    </Card>

    <Card href="./custom-outcomes">
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '1rem' }}>
        <div style={{ flexShrink: 0, width: '40px', height: '40px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <img src="https://mintcdn.com/onesignal/6fCcLQvxHVWEktgW/images/svg/docs-icn-analytics.svg?fit=max&auto=format&n=6fCcLQvxHVWEktgW&q=85&s=26c9741283ad0a724bf74193be86b03c" style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain' }} width="48" height="48" data-path="images/svg/docs-icn-analytics.svg" />
        </div>

        <div>
          <div style={{ fontWeight: '800', fontSize: '1.1rem', marginBottom: '0.25rem' }}>
            Custom Outcomes
          </div>

          <div>
            Track custom conversion events and measure the impact of your messaging campaigns.
          </div>
        </div>
      </div>
    </Card>

    <Card href="./event-streams">
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '1rem' }}>
        <div style={{ flexShrink: 0, width: '40px', height: '40px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <img src="https://mintcdn.com/onesignal/s4WC_KzLxf8ornqq/images/svg/docs-icn-sdk.svg?fit=max&auto=format&n=s4WC_KzLxf8ornqq&q=85&s=4f14b67a2d6a0a02bc4131093d066ed8" style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain' }} width="48" height="48" data-path="images/svg/docs-icn-sdk.svg" />
        </div>

        <div>
          <div style={{ fontWeight: '800', fontSize: '1.1rem', marginBottom: '0.25rem' }}>
            Event Streams
          </div>

          <div>
            Stream real-time messaging events to external systems for advanced analytics and automation.
          </div>
        </div>
      </div>
    </Card>
  </Columns>
</div>

Built with [Mintlify](https://mintlify.com).
