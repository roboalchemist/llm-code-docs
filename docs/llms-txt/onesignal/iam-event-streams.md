# Source: https://documentation.onesignal.com/docs/en/iam-event-streams.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# In-app message event streams

> How to utilize event streams to capture in-app message metrics

This document explains the capabilities and usage of our [In-App Messages](./in-app-messages-setup) events. You can track essential engagement statistics each time a user clicks or views these messages including block-level clicks and page-specific displays.

## In-app message events

There are three kinds [`event.kind`](./event-streams-data#event-kind) of In-App Message Events:

* In-app Impression - `message.iam.impression`
* In-app Clicked - `message.iam.clicked`
* In-app Page Displayed - `message.iam.page_displayed`

These events are fired upon a user opening and interacting with an in-app message on device.

### In-app impression

This event fires as soon as the message finishes loading and displayed on screen.

When using [carousels](./design-your-in-app-message#carousels), you can get the name and UUID of the specific page that is shown by using `event.data.page_name` and `event.data.page_id`.

### In-app clicked

This event is applicable to any element or block with a click action (also referred to as “target”). You can get the name and UUID of the specific target that is clicked on by using `event.data.target_name` and `event.data.target_id`, as well as the page the target belongs to using `event.data.page_name` and `event.data.page_id`.

See [In-app click actions](./iam-click-actions) for details.

### In-app page displayed

This is an event that is only applicable to [carousels](./design-your-in-app-message#carousels). You can get the name and UUID of the specific page or card that is shown by using `event.data.page_name` and `event.data.page_id`. The impression for the first card is fired as soon as the document finishes loading. Subsequent page impressions are fired upon swipe.

## In-app message event data

Each `event.kind` can have additional event data depending on how you create the in-app message.

<ParamField path="event.data.page_name" type="string">
  The name of the page or card that is displayed when the `event.kind` is `clicked` or `page_displayed`. Not available for `impression` events.

  The `page_name` is helpful to know which page was displayed and what was clicked on that page.

  Page names default to "Card 1", "Card 2", etc. but you can change the names within the Block Editor.

  <Frame>
    <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/e0862074b7ea2c064808035d2028410dae6aecc4bdf9ae4c4c83eeee1ac8d643-Screenshot_2025-01-17_at_1.30.34_PM.png?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=44d2b05d410b28b9e6fec94fd979ec5b" width="1040" height="826" data-path="images/docs/e0862074b7ea2c064808035d2028410dae6aecc4bdf9ae4c4c83eeee1ac8d643-Screenshot_2025-01-17_at_1.30.34_PM.png" />
  </Frame>
</ParamField>

<ParamField path="event.data.page_id" type="string UUID v4">
  A unique identifier for the page. Helpful for cases of using a [carousel](./design-your-in-app-message#carousels) and an old card is deleted or replaced with a new card.
</ParamField>

<ParamField path="event.data.target_name" type="string">
  The name of the button or image block element. You must set a [click actions](./iam-click-actions).
</ParamField>

<ParamField path="event.data.target_id" type="string UUID v4">
  A unique identifier for the button or image block element. You must set a [click actions](./iam-click-actions). This is helpful when using a [carousel](./design-your-in-app-message#carousels) and an old card is deleted or replaced with a new card.
</ParamField>

## Create your in-app message Event Stream

### Setup event streams

Review the [Event Stream Setup](./event-streams#setup) instructions for guidance on setting up and personalizing your event stream. The following provides IAM-specific steps for configuring your event stream (step 3).

## Ensure the target you want to track is set up correctly

In order to leverage custom names in the body of an event streams request you must manually specify a new custom name in the Block or HTML editor. In-App Messages that have existed prior to the release of custom names will not be able to expose `page_name` and `target_name` values in the event stream until the In-App is updated with custom names for each page or block.

After the In-App has been updated, event stream requests that are triggered from that moment on will have access to those values. At any given time, the `page_name` and `target_name` values will reflect the custom names state of the In-App at that moment, which may change if the In-App is ever updated again.

<Tabs>
  <Tab title="Block editor">
    All three events can be used with this editor. When using the block editor, ensure that the target contains an [In-app click action](./iam-click-actions). A target includes images, buttons, the close button, and the background block. Text blocks do not currently support click actions and are not included.

    Target custom names should be unique to avoid confusion in the dashboard experience.
  </Tab>

  <Tab title="HTML editor">
    Only In-app Impression and Clicked events can be used with this editor. When using the HTML editor, you can track clicks on any element type, not just buttons and images. There are 2 requirements:

    1. The element must have the `data-onesignal-unique-label="<insert_value>"` attribute to track a target
    2. The element must have an event listener applied to it that calls a method from the embedded [In-app JS library](./in-app-message-api) aka `OneSignalIamAPI`.

    Note: To avoid confusion, ensure target names are unique. For critical uniqueness, such as custom internal reporting, use the `target_id`, which is guaranteed unique by OneSignal. Note that using `data-onesignal-unique-label` attributes with the same label on multiple elements will merge their analytics. Changing these labels retains previous data under the original label, with new data assigned to the new label. For precise tracking, prioritize `target_id`.

    For example:

    <CodeGroup>
      ```html html theme={null}
      // For elements that do something like tag a user or prompt a push do something like this:

      <body>
        <button data-onesignal-unique-label="my-tag-user-button">Tag User</button>
      </body>
      <script>
        document
          .querySelector("button[data-onesignal-unique-label="my-tag-user-button")
          .addEventListener("click", function(e) {
            OneSignalIamApi.tagUser(e, { fiz: "baz" });
           });
      </script>

      // or for elements that don't require any specific functionality of the OneSignalIamApi other than click tracking, just call trackClick

      <body>
        <button data-onesignal-unique-label="my-button">Click Here</button>
      </body>
      <script>
        document
          .querySelector("button[data-onesignal-unique-label="my-button")
          .addEventListener("click", function(e) {
            OneSignalIamApi.trackClick(e);
           });
      </script>
      ```
    </CodeGroup>

    **Sample Input:**

    <CodeGroup>
      ```json json theme={null}
      {
        "page_name":"{{ event.data.page_name }}",
        "page_id":"{{ event.data.page_id }}",
        "target_id":"{{ event.data.target_id }}",
        "target_name":"{{ event.data.target_name }}",
        "iam_id":"{{ message.id }}",
        "iam_name":"{{ message.name }}",
        "event_kind": "{{ event.kind }}"
      }
      ```
    </CodeGroup>

    **Sample Output:**

    <CodeGroup>
      ```json json theme={null}
      {
        "page_name" : "html_page",
        "page_id": "d8b28eda-add3-59f8-a12d-07c70642363b" ,
        "target_id": "6bab1bd9-4de6-557b-b5ed-ecb85baed f89",
        "target_name": "my-location-prompt-button",
        "iam_id": "bb6329b6-f81a-44aa-a571-30ef6746de0c",
        "iam_name": "html iam naming",
        "event_kind": "message. iam.clicked"
      }
      ```
    </CodeGroup>
  </Tab>
</Tabs>

### Utilize unique IDs

Best Practice: When using Event Streams for analytics purposes, use `message.id`, `page_id`, and `target_id` to validate uniqueness. Custom names can be used but are meant to help differentiate between elements in one IAM in a human-readable format. If you have multiple in-app messages, use `message.id` to differentiate them.

### Use clear names in the block editor

Use meaningful and unique names for all in-app message titles, cards, and blocks to simplify data analysis. To rename a card in a carousel, select the tab you want to update, and select the “Options” dropdown next to the card tabs. You’ll see an option to rename the card.

To rename a block, select the three-dot options menu on the top right-hand corner of each block to open up the renaming modal. All custom names will be reflected in the dashboard report and event stream, if applicable. Custom names will not appear in even streams unless they are set and saved. If you have active IAMs and have recently set up a new IAM event stream, you will want to ensure these IAMs have meaningful custom names for cleaner analysis.

***

Built with [Mintlify](https://mintlify.com).
