# Source: https://docs.asapp.com/messaging-platform/integrations/web-sdk/web-features.md

# Web Features

This section describes various features that are unique to the ASAPP Web SDK:

* [Triggers](#triggers "Triggers")
* [Deeplinks](#deeplinks-11865 "Deeplinks")

In addition, please see [Chat Instead](/messaging-platform/integrations/chat-instead/web "Web").

## Triggers

A Trigger is an ASAPP feature that allows you to specify which pages display the ASAPP Chat UI. You may choose to show the ASAPP Chat UI on all pages where the ASAPP Chat SDK is [embedded and loaded](/messaging-platform/integrations/web-sdk/web-quick-start "Web Quick Start"), or on just a subset of those pages.

<Note>
  You must enable at least one Trigger in order for the ASAPP Chat UI to display anywhere on your site. Until you define at least one Trigger, the ASAPP Chat UI will not display on your site.
</Note>

<Frame>
  <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3a889a32-4401-ec1b-0f96-b73a2243d09a.png?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=1ff5ea2b8397950374873dbe0202a0c3" data-og-width="632" width="632" data-og-height="884" height="884" data-path="image/uuid-3a889a32-4401-ec1b-0f96-b73a2243d09a.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3a889a32-4401-ec1b-0f96-b73a2243d09a.png?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=8518e4e6111704b81700fb71a9dc96ff 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3a889a32-4401-ec1b-0f96-b73a2243d09a.png?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=b78cab6753a77335c0dc7825c9a3ac3d 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3a889a32-4401-ec1b-0f96-b73a2243d09a.png?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=9302afa5632a899f8480d9152f407c77 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3a889a32-4401-ec1b-0f96-b73a2243d09a.png?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=900b9c026c22d5110bc7d3cb29f5f680 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3a889a32-4401-ec1b-0f96-b73a2243d09a.png?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=9b6f90f484968532937c5f9ff6750dcd 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3a889a32-4401-ec1b-0f96-b73a2243d09a.png?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=007cf78f9b947a72178db960b97efd1c 2500w" />
</Frame>

Once you've [embedded](/messaging-platform/integrations/web-sdk/web-quick-start#1-embed-the-script "1. Embed the Script") and [loaded](/messaging-platform/integrations/web-sdk/web-javascript-api#load "'load'") the Chat SDK on your web pages, ASAPP will determine whether or not to display the Chat UI on the user's current URL.

URLs that are enabled for displaying the UI are configured by a feature known as Triggers.

<Note>
  You will need to be set up as a user of the ASAPP Admin Control Panel in order to make the changes described below.

  Once you are granted permissions, you may utilize the Triggers as a means of specifying which pages are eligible to show the ASAPP Chat UI.
</Note>

### Creating a Trigger

<Frame>
  <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7f1adc53-5b8e-a1f0-2e83-7d85a4b59989.png?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=645efbf00139baf4c3344b97270dc3df" data-og-width="1080" width="1080" data-og-height="642" height="642" data-path="image/uuid-7f1adc53-5b8e-a1f0-2e83-7d85a4b59989.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7f1adc53-5b8e-a1f0-2e83-7d85a4b59989.png?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=8b749d91d105421caf66eb935b0e87b5 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7f1adc53-5b8e-a1f0-2e83-7d85a4b59989.png?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=63d3aafa3fdbd5fdd6fb06e9971b6dca 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7f1adc53-5b8e-a1f0-2e83-7d85a4b59989.png?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=5dc07bbcc00f6d02174a56196f852df5 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7f1adc53-5b8e-a1f0-2e83-7d85a4b59989.png?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=1cdb4385e9cf6b8a7589a896ad1ce3f6 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7f1adc53-5b8e-a1f0-2e83-7d85a4b59989.png?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=73c0922e0e4a028f220ea9d9a783d5de 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7f1adc53-5b8e-a1f0-2e83-7d85a4b59989.png?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=826d11eefad6a68e47a9feddc18a0856 2500w" />
</Frame>

1. Visit the **Admin > Triggers** section of your Admin Desk.
2. Click the **Add +** button from the Triggers settings page.
3. In the **URL Link** field, enter the URL for the page where you would like to display the ASAPP Chat UI. (See the **Types of Triggers** section below for some example values.)
4. Click **Next >**.
5. Give the Trigger a display name. (Display names are used only on the Triggers settings page to help you organize and manage your triggers.)
6. Click **Save**.
7. You should now see the new entry on your Trigger settings page.
8. Visit the newly configured page on your site to double-check that the ASAPP Chat UI is loading or hiding as you expect.

### Types of Triggers

You may finely control the display of the ASAPP Chat UI on your site by adding as many Triggers as you like.

Triggers can be defined in two different ways: as **Wildcard** and as **Single-Page Triggers**.

#### Wildcard Triggers

You can use the wildcard character in the URL Link field of a Trigger to enable the display of the Chat SDK pages that follow a URL pattern.

The asterisk (i.e., `/*` is the wildcard character you use when defining a Trigger. When you use an asterisk in the URL Link of your Trigger definition, that character will match any sequence of one or more characters.

To set a wildcard for your entire domain, enter a **URL Link** value for your domain name, followed by `/*` (e.g., `example.com/*` ). This will enable the display of the ASAPP Chat UI on all pages of your site.

To enable the ASAPP Chat UI to appear on a more limited set of pages, enter a **URL Link** value that includes the appropriate sub-route path, followed by the `/*` wildcard (e.g., `example.com/settings/*`).

This will cause the Chat UI to display on any pages that start with the URL and sub-route `example.com/settings/`, such as `example.com/settings/profile` and `example.com/settings/payment`.

#### Single-Page Triggers

If you want the ASAPP Chat UI to display on only a few specific pages, you can create a separate Trigger for each of those pages, one at a time, by entering the exact URL for the page you wish to enable in the URL Link field of the Trigger definition.

For example, entering `example.com/customer-support/shipping.html` in the URL Link field of your Trigger definition will enable the ASAPP Chat UI to display on that single page.

## Deeplinks

A feature that defines how the SDK opens hyperlinks when a user clicks a link to another document. In the ASAPP Web SDK, we use the browser's `window.location.origin` API to determine whether the link should open in the same window or a new window.

In order for a link to open in the same window as the user's current SDK window, the `window.location.origin` must return a matching protocol and hostname.

<Note>
  For example, if a user is on `https://www.example.com` and clicks a link to `https://www.example.com/page-two`, the SDK changes the current page to the destination page in the same window.
</Note>

A link opens in a *new* window if there is any difference between the current page and the destination page origin. When a user clicks a link from `https://www.example.com` to `https://subdomain.example.com` , the SDK opens the destination page in a new window due to hostname variation.

A link from `https://example.com` to `http://example.com` also opens a new window due to a mismatched protocol. When a link opens a new window, the user's SDK window remains open.
