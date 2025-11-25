# Source: https://dub.co/docs/conversions/leads/hubspot.md

# HubSpot

> Learn how to track lead conversion events with HubSpot and Dub

<Note>
  Conversion tracking requires a [Business plan](https://dub.co/pricing)
  subscription or higher.
</Note>

When it comes to [conversion tracking](/conversions/quickstart), a `lead` event happens when a user performs an action that indicates interest in your product or service. This could be anything from:

* Signing up for an account
* Booking a demo meeting
* Joining a mailing list

<Frame>
  <img className="rounded-lg border border-gray-100" src="https://assets.dub.co/help/conversion-lead-event.png" alt="A diagram showing how lead events are tracked in the conversion funnel" />
</Frame>

This guide shows you how to track lead conversion events with HubSpot as your CRM.

## Prerequisites

First, you'll need to enable conversion tracking for your Dub links to be able to start tracking conversions:

<Tip>
  If you're using [Dub Partners](/partners/quickstart), you can skip this step
  since partner links will have conversion tracking enabled by default.
</Tip>

<AccordionGroup>
  <Accordion title="Option 1: On a workspace-level">
    To enable conversion tracking for all future links in a workspace, you can do the following:
    To enable conversion tracking for all future links in a workspace, you can do the following:

    1. Navigate to your [workspace's Analytics settings page](https://app.dub.co/settings/analytics).
    2. Toggle the **Workspace-level Conversion Tracking** switch to enable conversion tracking for the workspace.

    <Frame>
      <img src="https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/enable-conversion-tracking-workspace.png?fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=f810945d33a42f45de3e06647b2cfd15" alt="Enabling conversion tracking for a workspace" data-og-width="3082" width="3082" data-og-height="1529" height="1529" data-path="images/conversions/enable-conversion-tracking-workspace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/enable-conversion-tracking-workspace.png?w=280&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=514f7549b9a65a40fc4224ea68859e06 280w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/enable-conversion-tracking-workspace.png?w=560&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=9c002882f7093efb76ae4be72e5f0312 560w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/enable-conversion-tracking-workspace.png?w=840&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=d4da71527556174d30b71c0f9acdad6f 840w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/enable-conversion-tracking-workspace.png?w=1100&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=c887363f92b258c3493267e2f4a3dd8e 1100w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/enable-conversion-tracking-workspace.png?w=1650&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=e1b23eb5cf148df63105fdc572e6936b 1650w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/enable-conversion-tracking-workspace.png?w=2500&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=1623f4206427342d87df828a17d66438 2500w" />
    </Frame>

    This option will enable conversion tracking in the [Dub Link Builder](https://dub.co/help/article/dub-link-builder) for all future links.
  </Accordion>

  <Accordion title="Option 2: On a link-level">
    If you don't want to enable conversion tracking for all your links in a workspace, you can also opt to enable it on a link-level.

    To enable conversion tracking for a specific link, open the [Dub Link Builder](https://dub.co/help/article/dub-link-builder) for a link and toggle the **Conversion Tracking** switch.

    <Frame>
      <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/enable-conversion-tracking.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=4153d4a981e2a13324464ca3d30625cd" alt="Enabling conversion tracking for a link" data-og-width="2345" width="2345" data-og-height="908" height="908" data-path="images/conversions/enable-conversion-tracking.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/enable-conversion-tracking.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=0984b50a4b6987e7bc4f8f3975559d0e 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/enable-conversion-tracking.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=673093d978579d5cd19e22b2c786f6a4 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/enable-conversion-tracking.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=94cb269be979162dd8bb74b2a5b614e9 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/enable-conversion-tracking.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=4572ec2e03c96b50d1da93f8b3f04636 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/enable-conversion-tracking.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=f0a017e718cc81ae682e89809e4dab25 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/enable-conversion-tracking.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=078ec13ca0166c3b751d24271c1d2171 2500w" />
    </Frame>

    <Tip>
      You can also use the `C` keyboard shortcut when inside the link builder to
      quickly enable conversion tracking for a given link.
    </Tip>
  </Accordion>

  <Accordion title="Option 3: Via the API">
    Alternatively, you can also enable conversion tracking programmatically via the [Dub API](/api-reference/introduction). All you need to do is pass `trackConversion: true` when creating or updating a link:

    <CodeGroup>
      ```javascript Node.js theme={null}
      const link = await dub.links.create({
        url: "https://dub.co",
        trackConversion: true,
      });
      ```

      ```python Python theme={null}
      link = d.links.create(url="https://dub.co", track_conversion=True)
      ```

      ```go Go theme={null}
      link, err := d.Links.Create(ctx, &dub.CreateLinkRequest{
          URL: "https://dub.co",
          TrackConversion: true,
      })
      ```

      ```ruby Ruby theme={null}
      s.links.create_many(
        ::OpenApiSDK::Operations::CreateLinkRequest.new(
          url: "https://dub.co",
          track_conversion: true,
        )
      )
      ```
    </CodeGroup>
  </Accordion>
</AccordionGroup>

Then, you'd want to install the `@dub/analytics` script to your website to track conversion events.

You can install the `@dub/analytics` script in several different ways:

<CardGroup>
  <Card title="React" icon="react" href="/sdks/client-side/installation-guides/react" horizontal />

  <Card title="Manual installation" icon="browser" href="/sdks/client-side/installation-guides/manual" horizontal />

  <Card
    title="Framer"
    icon={
    <svg
      width="74"
      height="111"
      viewBox="0 0 74 111"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      className="w-7 h-7"
    >
      <path d="M0 0H73.8374V36.9892H36.9187L0 0Z" fill="#eb5611" />
      <path d="M0 36.989H36.9187L73.8374 73.9796H0V36.989Z" fill="#eb5611" />
      <path d="M0 73.9797H36.9187V110.97L0 73.9797Z" fill="#eb5611" />
    </svg>
  }
    href="/sdks/client-side/installation-guides/framer"
    horizontal
  />

  <Card title="Shopify" icon="shopify" href="/sdks/client-side/installation-guides/shopify" horizontal />

  <Card title="WordPress" icon="wordpress" href="/sdks/client-side/installation-guides/wordpress" horizontal />

  <Card title="Webflow" icon="webflow" href="/sdks/client-side/installation-guides/webflow" horizontal />

  <Card title="Google Tag Manager" icon="google" href="/sdks/client-side/installation-guides/google-tag-manager" horizontal />
</CardGroup>

<Check>
  You can **verify the installation** with the following tests:

  1. Open the browser console and type in `_dubAnalytics` – if the script is installed correctly, you should see the `_dubAnalytics` object in the console.
  2. Add the `?dub_id=test` query parameter to your website URL and make sure that the `dub_id` cookie is being set in your browser.

  If both of these checks pass, the script is installed correctly. Otherwise, please make sure:

  * The analytics script was added to the `<head>` section of the page
  * If you're using a content delivery network (CDN), make sure to purge any cached content
</Check>

Finally, install the [HubSpot Dub Integration](https://app.dub.co/integrations/hubspot) to your workspace.

<Frame>
  <img src="https://mintcdn.com/dub/4atD6Qmc1QmxgkWq/images/conversions/hubspot/installed-hubspot-integration.png?fit=max&auto=format&n=4atD6Qmc1QmxgkWq&q=85&s=2cbc22a672f1eaecb50d83439f84b722" alt="HubSpot Dub Integration" data-og-width="1026" width="1026" data-og-height="659" height="659" data-path="images/conversions/hubspot/installed-hubspot-integration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/4atD6Qmc1QmxgkWq/images/conversions/hubspot/installed-hubspot-integration.png?w=280&fit=max&auto=format&n=4atD6Qmc1QmxgkWq&q=85&s=3f2d54f69fd7c316fc89e87982c6f12d 280w, https://mintcdn.com/dub/4atD6Qmc1QmxgkWq/images/conversions/hubspot/installed-hubspot-integration.png?w=560&fit=max&auto=format&n=4atD6Qmc1QmxgkWq&q=85&s=2efb80c5d22973ab27f5cc2130fa3edb 560w, https://mintcdn.com/dub/4atD6Qmc1QmxgkWq/images/conversions/hubspot/installed-hubspot-integration.png?w=840&fit=max&auto=format&n=4atD6Qmc1QmxgkWq&q=85&s=75c99431c912d9e9a3fa7cdaa8f9d2b4 840w, https://mintcdn.com/dub/4atD6Qmc1QmxgkWq/images/conversions/hubspot/installed-hubspot-integration.png?w=1100&fit=max&auto=format&n=4atD6Qmc1QmxgkWq&q=85&s=f31d229d93355adc7478ff571d139c6d 1100w, https://mintcdn.com/dub/4atD6Qmc1QmxgkWq/images/conversions/hubspot/installed-hubspot-integration.png?w=1650&fit=max&auto=format&n=4atD6Qmc1QmxgkWq&q=85&s=e8553163eb46c7295931cab24cf977d8 1650w, https://mintcdn.com/dub/4atD6Qmc1QmxgkWq/images/conversions/hubspot/installed-hubspot-integration.png?w=2500&fit=max&auto=format&n=4atD6Qmc1QmxgkWq&q=85&s=8772aff2eee6d22f67e5bf8219541324 2500w" />
</Frame>

### Integration Setup

During the installation, Dub will create 3 properties to your contact object on HubSpot:

* **Dub Id** - Unique identifier that Dub uses to track clicks
* **Dub Link** - The short link that the contact clicked to reach your site
* **Dub Partner Email** - Email address of the partner associated with the short link

<Frame>
  <img src="https://mintcdn.com/dub/FXRjcdT3tyFnZPLN/images/conversions/hubspot/hubspot-dub-properties.png?fit=max&auto=format&n=FXRjcdT3tyFnZPLN&q=85&s=1aea7bc62a2bb2fdf275c64957449422" alt="HubSpot Contact Properties Created by Dub Integration" data-og-width="2516" width="2516" data-og-height="1008" height="1008" data-path="images/conversions/hubspot/hubspot-dub-properties.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/FXRjcdT3tyFnZPLN/images/conversions/hubspot/hubspot-dub-properties.png?w=280&fit=max&auto=format&n=FXRjcdT3tyFnZPLN&q=85&s=2af8372316360c207a3ca24411cfbc4f 280w, https://mintcdn.com/dub/FXRjcdT3tyFnZPLN/images/conversions/hubspot/hubspot-dub-properties.png?w=560&fit=max&auto=format&n=FXRjcdT3tyFnZPLN&q=85&s=356677ea1f0783350cceb0b62d8017f8 560w, https://mintcdn.com/dub/FXRjcdT3tyFnZPLN/images/conversions/hubspot/hubspot-dub-properties.png?w=840&fit=max&auto=format&n=FXRjcdT3tyFnZPLN&q=85&s=ed4ab5f10e84ec87f919c1e7e921b72f 840w, https://mintcdn.com/dub/FXRjcdT3tyFnZPLN/images/conversions/hubspot/hubspot-dub-properties.png?w=1100&fit=max&auto=format&n=FXRjcdT3tyFnZPLN&q=85&s=0fbb976e8780249aa7c04d8bdd936285 1100w, https://mintcdn.com/dub/FXRjcdT3tyFnZPLN/images/conversions/hubspot/hubspot-dub-properties.png?w=1650&fit=max&auto=format&n=FXRjcdT3tyFnZPLN&q=85&s=97bd90ccc638223db2585b3e9ce25746 1650w, https://mintcdn.com/dub/FXRjcdT3tyFnZPLN/images/conversions/hubspot/hubspot-dub-properties.png?w=2500&fit=max&auto=format&n=FXRjcdT3tyFnZPLN&q=85&s=b4e867d986ed81719db2c0669146df85 2500w" />
</Frame>

<Tip>
  If you can't see these properties in your HubSpot contact object after
  installation, something went wrong with the integration setup. Please [contact
  us](mailto:support@dub.co) for assistance.
</Tip>

### Set Your Closed Won Deal Stage ID

You can define which HubSpot deal stage should be treated as **Closed Won** for automatic sales tracking in Dub.

If you've customized your pipeline (i.e. changed or added deal stages in HubSpot), enter the stage ID corresponding to your custom **Closed Won** stage in the [HubSpot Integration Settings](https://app.dub.co/settings/integrations/hubspot).

Once set, any HubSpot deal marked as **Closed Won** will automatically be tracked in Dub as a sale conversion event, including its deal value.

<Frame>
  <img src="https://mintcdn.com/dub/FXRjcdT3tyFnZPLN/images/conversions/hubspot/hubspot-custom-deal-stage-id.png?fit=max&auto=format&n=FXRjcdT3tyFnZPLN&q=85&s=4d4b14da0cc8552a28dc1b230df9d41f" alt="Add custom deal stage ID to HubSpot Integration Settings" data-og-width="1356" width="1356" data-og-height="522" height="522" data-path="images/conversions/hubspot/hubspot-custom-deal-stage-id.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/FXRjcdT3tyFnZPLN/images/conversions/hubspot/hubspot-custom-deal-stage-id.png?w=280&fit=max&auto=format&n=FXRjcdT3tyFnZPLN&q=85&s=526cdc560f2bc198a4fe849b04c5dd10 280w, https://mintcdn.com/dub/FXRjcdT3tyFnZPLN/images/conversions/hubspot/hubspot-custom-deal-stage-id.png?w=560&fit=max&auto=format&n=FXRjcdT3tyFnZPLN&q=85&s=2a2787bd3d01779899f38df95a2ca504 560w, https://mintcdn.com/dub/FXRjcdT3tyFnZPLN/images/conversions/hubspot/hubspot-custom-deal-stage-id.png?w=840&fit=max&auto=format&n=FXRjcdT3tyFnZPLN&q=85&s=662f9109703e696e1fe25aa80f96f14c 840w, https://mintcdn.com/dub/FXRjcdT3tyFnZPLN/images/conversions/hubspot/hubspot-custom-deal-stage-id.png?w=1100&fit=max&auto=format&n=FXRjcdT3tyFnZPLN&q=85&s=c7bcc39e043f1ac24b0350466d255020 1100w, https://mintcdn.com/dub/FXRjcdT3tyFnZPLN/images/conversions/hubspot/hubspot-custom-deal-stage-id.png?w=1650&fit=max&auto=format&n=FXRjcdT3tyFnZPLN&q=85&s=a9215f01ea6d1e5fd3ca6dde5ca31193 1650w, https://mintcdn.com/dub/FXRjcdT3tyFnZPLN/images/conversions/hubspot/hubspot-custom-deal-stage-id.png?w=2500&fit=max&auto=format&n=FXRjcdT3tyFnZPLN&q=85&s=f384b7535bfbd8a9a35af39bbfb474b3 2500w" />
</Frame>

## Option 1: Using HubSpot Forms

[HubSpot Forms](https://www.hubspot.com/products/marketing/forms) help you capture lead information and track conversions. By integrating with Dub, you can attribute each form submission back to the specific Dub link that drove the conversion.

To make attribution work, you need to capture the `dub_id` cookie in your HubSpot form. This ensures each lead is tied back to the exact Dub link they came from.

Here's how you can set it up:

<Steps>
  <Step title="Add a hidden field to your form">
    In the HubSpot form builder, add a hidden field and map it to the **Dub Id** contact property.

    This makes sure the value captured by your script is stored on the contact record. Without mapping to a property, HubSpot won’t persist the `dub_id` value.

    <Frame>
      <img src="https://mintcdn.com/dub/4atD6Qmc1QmxgkWq/images/conversions/hubspot/hubspot-forms-setup.png?fit=max&auto=format&n=4atD6Qmc1QmxgkWq&q=85&s=a8a09cc8a620d07eb4c3ff22ce80a33f" alt="Segment Dub (Actions) Mapping" width="1440" height="1024" data-og-width="1769" data-og-height="1405" data-path="images/conversions/hubspot/hubspot-forms-setup.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/4atD6Qmc1QmxgkWq/images/conversions/hubspot/hubspot-forms-setup.png?w=280&fit=max&auto=format&n=4atD6Qmc1QmxgkWq&q=85&s=4252100b9d5a1df6caf6f61a6404d43b 280w, https://mintcdn.com/dub/4atD6Qmc1QmxgkWq/images/conversions/hubspot/hubspot-forms-setup.png?w=560&fit=max&auto=format&n=4atD6Qmc1QmxgkWq&q=85&s=c11a91e54af80f284ed847f5c64b5948 560w, https://mintcdn.com/dub/4atD6Qmc1QmxgkWq/images/conversions/hubspot/hubspot-forms-setup.png?w=840&fit=max&auto=format&n=4atD6Qmc1QmxgkWq&q=85&s=d12b8f1ed0639e3f1bc10b0582ca8fc4 840w, https://mintcdn.com/dub/4atD6Qmc1QmxgkWq/images/conversions/hubspot/hubspot-forms-setup.png?w=1100&fit=max&auto=format&n=4atD6Qmc1QmxgkWq&q=85&s=f60fcab04f3acff5d3a48eb7d376682b 1100w, https://mintcdn.com/dub/4atD6Qmc1QmxgkWq/images/conversions/hubspot/hubspot-forms-setup.png?w=1650&fit=max&auto=format&n=4atD6Qmc1QmxgkWq&q=85&s=d533cd7216d6e6ede0d0ee827838542a 1650w, https://mintcdn.com/dub/4atD6Qmc1QmxgkWq/images/conversions/hubspot/hubspot-forms-setup.png?w=2500&fit=max&auto=format&n=4atD6Qmc1QmxgkWq&q=85&s=0569b8daa55b13091197d637e97af824 2500w" />
    </Frame>
  </Step>

  <Step title="Add the script to your site">
    Finally, add the following snippet to your site. The script reads the `dub_id` cookie and, if found, automatically fills the hidden Dub Id form field with its value.

    <CodeGroup>
      ```html HTML expandable theme={null}
      <script src="https://js.hsforms.net/forms/embed/47839131.js" defer></script>

      <div
        class="hs-form-frame"
        data-region="na1"
        data-form-id="YOUR_FORM_ID"
        data-portal-id="YOUR_PORTAL_ID"
      ></div>

      <script>
        // A helper function to get the value of a cookie
        function getCookie(name) {
          const value = `; ${document.cookie}`;
          const parts = value.split(`; ${name}=`);

          if (parts.length === 2) {
            return parts.pop().split(";").shift();
          }

          return null;
        }

        // Listen for the form ready event
        window.addEventListener("hs-form-event:on-ready", (event) => {
          const clickId = getCookie("dub_id");

          if (!clickId) {
            console.debug("clickId not found. Skipping lead tracking.");
            return;
          }

          // Populate the hidden field with the dub_id
          HubSpotFormsV4.getForms()[0].setFieldValue("0-1/dub_id", clickId);
        });
      </script>
      ```
    </CodeGroup>

    When a prospect submits the form, the `dub_id` is captured and passed to HubSpot, ensuring the lead is attributed back to the original Dub link.
  </Step>
</Steps>

## Option 2: Using HubSpot Meeting Scheduler

[HubSpot's Meeting Scheduler](https://www.hubspot.com/products/sales/schedule-meeting) lets prospects book time directly with you or your team.

Since HubSpot doesn't let you add a hidden field to the scheduling form, you should handle initial lead tracking through [deferred lead tracking](/conversions/leads/deferred) on the client side.

<Steps>
  <Step title="Generate your publishable key">
    Before you can track conversions on the client-side, you need to generate a publishable key from your Dub workspace.

    To do that, navigate to your [workspace's Analytics settings page](https://app.dub.co/settings/analytics) and generate a new publishable key under the **Publishable Key** section.

    <Frame>
      <img src="https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/publishable-key.png?fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=76add1f30a997ba897f10acdc21b51b5" alt="Enabling conversion tracking for a workspace" data-og-width="2985" width="2985" data-og-height="2021" height="2021" data-path="images/conversions/publishable-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/publishable-key.png?w=280&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=f0f995d217914793d81c0a42ccda502a 280w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/publishable-key.png?w=560&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=62a390272e2b24b6ae8cf3ba98dac66f 560w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/publishable-key.png?w=840&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=cdb86db75f933f33be21d4a0e8293227 840w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/publishable-key.png?w=1100&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=ab9b7ec6577587e197e1fefeaa250216 1100w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/publishable-key.png?w=1650&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=ab5f37e61472d2c6118f7b640a5fdb50 1650w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/publishable-key.png?w=2500&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=6d83d47d0988ee0d895606f8b2e683c6 2500w" />
    </Frame>
  </Step>

  <Step title="Allowlist your site's domain">
    Then, you'll need to allowlist your site's domain to allow the client-side conversion events to be ingested by Dub.

    To do that, navigate to your [workspace's Analytics settings page](https://app.dub.co/settings/analytics) and add your site's domain to the **Allowed Hostnames** list.

    This provides an additional layer of security by ensuring only authorized domains can track conversions using your publishable key.

    <Frame>
      <img src="https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/allowed-hostnames.png?fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=da26eba128e89211e7bfd7cf46ba32e0" alt="Enabling conversion tracking for a workspace" data-og-width="2979" width="2979" data-og-height="2018" height="2018" data-path="images/conversions/allowed-hostnames.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/allowed-hostnames.png?w=280&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=58dbd9580cedff38a40a0f6ad6fe7188 280w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/allowed-hostnames.png?w=560&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=ace60f5cf513d21281be79ead24189e6 560w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/allowed-hostnames.png?w=840&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=33fff99044f2b77702dcc24ade6f67d7 840w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/allowed-hostnames.png?w=1100&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=134d6038e2ad8da21e39a7b8e797fee2 1100w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/allowed-hostnames.png?w=1650&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=b3051b73df5fdf2bd16b5db5aa4d34a5 1650w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/allowed-hostnames.png?w=2500&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=e3f56a578de0f460c8a77f08aa33e437 2500w" />
    </Frame>

    You can group your hostnames when adding them to the allow list:

    * `example.com`: Tracks traffic **only** from `example.com`.
    * `*.example.com`: Tracks traffic from **all subdomains** of `example.com`, but **not** from `example.com` itself.

    <Tip>
      When testing things out locally, you can add `localhost` to the **Allowed
      Hostnames** list temporarily. This will allow local events to be ingested by
      Dub. Don't forget to remove it once you're ready to go live!
    </Tip>
  </Step>

  <Step title="Add the tracking code to your site">
    Use the following code to track lead conversions when meetings are booked through the HubSpot scheduler.

    The script listens for booking events from HubSpot, extracts the customer's details (name and email), and then calls `dubAnalytics.trackLead()` with [deferred lead tracking](/conversions/leads/deferred).

    This way, the lead is only tracked after the meeting is confirmed, ensuring accurate attribution.

    <CodeGroup>
      ```html HTML expandable theme={null}

      <!-- Load Dub analytics script -->
      <script>
        !(function(w, n) {
          w[n] = w[n] || function() { (w[n].q = w[n].q || []).push(arguments); };
          ["trackClick","trackLead","trackSale"].forEach(t => w[n][t] = (...a) => w[n](t, ...a));
          var s = document.createElement("script");
          s.defer = true;
          s.src = "https://www.dubcdn.com/analytics/script.conversion-tracking.js";
          s.setAttribute("data-publishable-key", "YOUR_PUBLISHABLE_KEY");
          s.setAttribute("data-domains", '{"refer":"YOUR_SHORT_DOMAIN"}');
          document.head.appendChild(s);
        })(window, "dubAnalytics");
      </script>

      <div
        class="meetings-iframe-container"
        data-src="https://meetings.hubspot.com/YOUR_USERNAME?embed=true"
      ></div>

      <script
        type="text/javascript"
        src="https://static.hsappstatic.net/MeetingsEmbed/ex/MeetingsEmbedCode.js"
      ></script>

      <script>
        // Listen for the message event
        window.addEventListener("message", function (event) {
          // Check if the message is from the scheduling widget
          if (event.origin === "https://meetings.hubspot.com") {
            // Get the data from the event
            const data = event.data;

            if (data.meetingBookSucceeded) {
              // Get the scheduled contact
              const contact =
                data.meetingsPayload.bookingResponse.postResponse.contact;

              if (!contact) {
                console.debug("contact not found. Skipping lead tracking.");
                return;
              }

              // Track the lead with the scheduled contact
              const customerName = [contact.firstName, contact.lastName]
                .filter(Boolean)
                .join(" ");

              dubAnalytics.trackLead({
                mode: "deferred",
                eventName: "Meeting scheduled",
                customerExternalId: contact.email,
                customerName: customerName,
                customerEmail: contact.email,
              });
            }
          }
        });
      </script>
      ```
    </CodeGroup>
  </Step>
</Steps>

## Tracking sale conversion events

After a prospect attends your demo call, you'll typically create a deal in HubSpot to track the sales opportunity.

Dub's HubSpot integration automatically sets up webhooks to track both deal creation and deal closure events, providing complete visibility into your sales funnel.

### When a deal is created

When you create a deal in HubSpot for a contact who came through your Dub links, the integration automatically tracks this as a lead conversion event in Dub.

### When a deal is closed

When a deal moves to a **Closed Won** status in HubSpot, the integration automatically tracks a sale event in Dub using the deal amount as the sale value.

If a deal is not being tracked as a sale in Dub, make sure you've set the correct Closed Won Deal Stage ID in your [HubSpot Integration Settings](#set-your-closed-won-deal-stage-id).
