# Source: https://documentation.onesignal.com/docs/en/abandoned-cart.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Abandoned cart tutorial

> Recover lost sales with abandoned cart notifications using OneSignal. Learn how to track cart activity, build the right segment, and send timely reminders with Journeys.

## Overview

Abandoned carts are one of the highest-impact opportunities to recover lost revenue. Most users who abandon a cart still intend to purchase — they just need a timely reminder.

This guide shows you how to build an **automated abandoned cart Journey** in OneSignal that:

* Detects cart activity
* Waits for a short period of inactivity
* Sends a personalized reminder
* Stops messaging immediately after purchase or cart removal

You can implement this using either:

* Custom Events (recommended for most implementations)
* Tags (simpler, limited use cases)

The right choice depends on the data you want to show in the message and where that data comes from.

### What you will build

By the end of this guide, you will have:

* Cart activity sent to OneSignal (via Tags or Custom Events)
* A clear, **code-defined** abandonment signal
* Message templates that personalize cart data
* A Journey that:
  * Starts when an abandonment signal is received
  * Waits before sending
  * Sends an abandoned cart message
  * Exits immediately when the cart is emptied or purchased
* Analytics to measure message and revenue performance

### Choose your tracking method

You can track cart activity using either **Custom Events** or **Tags**.

* **Use Custom Events** if you:
  * Can detect abandonment after a period of inactivity
  * Want rich cart data (items, images, prices)
  * Are comfortable ensuring events fire **once per abandonment**

* **Use Tags** if you:
  * Want state-based safety by default
  * Only need simple cart data
  * Prefer segment-controlled entry and exit

This guide shows both approaches. Custom Events offer more flexibility, but require more care.

### How abandoned carts are modeled

<Info>
  OneSignal does **not** automatically determine when a cart is abandoned.

  You decide when a cart becomes abandoned in your own code or system, and then notify OneSignal.
</Info>

**What `cart_abandoned` means**

The `cart_abandoned` event should represent a **state transition** - The cart was active → the user stopped engaging → the cart is now considered abandoned.

This event should be sent:

* After a meaningful period of inactivity (e.g. 1 hour)
* Only if the cart still contains items

<Warning>
  Do **not** send `cart_abandoned` on every cart update.

  Sending this event repeatedly will cause users to re-enter the Journey multiple times and may spam them.
</Warning>

#### How Journeys use abandonment signals

Once OneSignal receives `cart_abandoned`:

* The user becomes eligible to enter the Journey
* A wait period gives them time to return naturally
* A message is sent only if they do not exit
* The user exits immediately when `cart_emptied` is received

<Info>
  Journeys control **timing and repetition** — they do not determine abandonment.
</Info>

***

## Setup

### Step 1. Plan your cart data and source

Decide **what cart information you want to show** and **where that data comes from**.

Common cart data includes:

* Product name, image, price, and quantity
* Number of items in the cart
* A deep link back to the cart

Your data source determines how you send events:

| Data source          | Recommended method              |
| -------------------- | ------------------------------- |
| App or website       | OneSignal Frontend SDK          |
| Backend or database  | OneSignal REST API              |
| Third-party platform | Integration-based Custom Events |

<Check>
  By the end of this step, you know **what data you will send** and **how you will send it**.
</Check>

### Step 2. Send cart state signals to OneSignal

You must send signals that represent **cart state changes**.

| Signal           | Purpose                                 |
| ---------------- | --------------------------------------- |
| `cart_abandoned` | Cart activity detected and not resolved |
| `cart_updated`   | Cart contents change                    |
| `cart_emptied`   | Cart cleared or purchase completed      |

<Warning>
  Event and tag names must match **exactly** across SDK/API calls, Segments, Journey rules, and Liquid templates.
</Warning>

<Tabs>
  <Tab title="Frontend SDK">
    Use the OneSignal Web or Mobile SDKs to send Custom Events or Tags.

    | SDK Method   | Description                                                                                                            |
    | ------------ | ---------------------------------------------------------------------------------------------------------------------- |
    | `trackEvent` | Send a Custom Event ([Mobile SDK](./mobile-sdk-reference#custom-events), [Web SDK](./web-sdk-reference#custom-events)) |
    | `addTags`    | Add a Tag ([Mobile SDK](./mobile-sdk-reference#data-tags), [Web SDK](./web-sdk-reference#data-tags))                   |
    | `removeTags` | Remove a Tag ([Mobile SDK](./mobile-sdk-reference#data-tags), [Web SDK](./web-sdk-reference#data-tags))                |

    **Custom Event example**

    <Warning>
      The `cart_abandoned` event should be sent after a period of cart inactivity, not when the user enters or updates their cart.

      The `cart_emptied` event should be sent immediately when the cart is emptied or a purchase is completed.
    </Warning>

    <CodeGroup>
      ```javascript Custom Event: Cart Abandoned theme={null}
      OneSignal.User.trackEvent("cart_abandoned", {
        product_name: "24 Pack of Acorns",
        product_image: "https://i.imgur.com/ssPCfbC.png",
        product_price: 12.99,
        product_quantity: 1,
        cart_url: "https://yourdomain.com/cart"
      });
      ```

      ```javascript Custom Event: Cart Emptied theme={null}
      OneSignal.User.trackEvent("cart_emptied");
      ```
    </CodeGroup>

    **Tag example**

    <Info>
      This example sets the `cart_updated` tag to a Unix timestamp (in seconds) representing when the cart was last updated. You can also use a boolean value (true/false), but a timestamp provides more flexibility with [Time Operators](./time-operators).
    </Info>

    <CodeGroup>
      ```javascript Tag: Cart Updated theme={null}
      OneSignal.User.addTags({
        cart_updated: unix_timestamp_seconds,
        product_name: "24 Pack of Acorns", 
        product_image: "https://i.imgur.com/ssPCfbC.png",
        product_price: "$12.99",
        product_quantity: "1",
        cart_url: "https://yourdomain.com/username/cart"
      })
      ```

      ```javascript Tag: Cart Emptied (remove tags) theme={null}
        // Remove the tags
        OneSignal.User.removeTags([
          "cart_updated", "product_name", "product_image", "product_price","product_quantity", "cart_url"
        ])
      ```
    </CodeGroup>
  </Tab>

  <Tab title="REST API">
    Use the REST API when cart activity is tracked server-side.

    | API Endpoint                                                   | Description           |
    | -------------------------------------------------------------- | --------------------- |
    | [Custom Events API Reference](/reference/create-custom-events) | Create a Custom Event |
    | [Update User API Reference](/reference/update-user)            | Add and remove tags   |

    **Custom Event example**

    <Warning>
      The `cart_abandoned` event should be sent after a period of cart inactivity, not when the user enters or updates their cart.

      The `cart_emptied` event should be sent immediately when the cart is emptied or a purchase is completed.
    </Warning>

    <CodeGroup>
      ```json Custom Event: Cart Abandoned theme={null}
      {
        "events": [
          {
            "name": "cart_abandoned",
            "properties": {
              "product_name": "24 Pack of Acorns",
              "product_image": "https://i.imgur.com/ssPCfbC.png",
              "product_price": "$12.99",
              "product_quantity": "1",
              "cart_url": "https://yourdomain.com/username/cart"
            },
            "external_id": "ID_OF_THE_USER"
          }
        ]
      }
      ```

      ```json Custom Event: Cart Emptied theme={null}
      {
        "events": [
          {
            "name": "cart_emptied",
            "external_id": "ID_OF_THE_USER"
          }
        ]
      }
      ```
    </CodeGroup>

    **Tag example**

    <Info>
      This example sets the `cart_updated` tag to a Unix timestamp (in seconds) representing when the cart was last updated. You can also use a boolean value (true/false), but a timestamp provides more flexibility with [Time Operators](./time-operators).
    </Info>

    <CodeGroup>
      ```json Tag: Cart Updated theme={null}
      {
        "properties": {
          "tags": {
            "cart_updated": "unix_timestamp_seconds",
            "product_name": "24 Pack of Acorns",
            "product_image": "https://i.imgur.com/ssPCfbC.png",
            "product_price": "$12.99",
            "product_quantity": "1",
            "cart_url": "https://yourdomain.com/username/cart"
          }
        }
      }
      ```

      ```json Tag: Cart Emptied (remove tags) theme={null}
      {
        "properties": {
          "tags": {
            "cart_updated": "",
            "product_name": "",
            "product_image": "",
            "product_price": "",
            "product_quantity": "",
            "cart_url": ""
          }
        }
      }
      ```
    </CodeGroup>
  </Tab>

  <Tab title="3rd Party Integration">
    If you are tracking cart activity in a 3rd party Integration, you can send cart activity as Custom Events.

    Please refer to the specific [Integration](./integrations) documentation you are using for more details.
  </Tab>
</Tabs>

<Warning> If you do not send a `cart_emptied` signal, users may continue receiving abandoned cart messages after purchasing. </Warning>

***

### Step 3. Create abandoned cart message templates

Create message templates that reference cart data dynamically.

For more details on the concepts used in this section, see:

* [Liquid syntax](./using-liquid-syntax)
* [Message Personalization](./message-personalization)
* [Templates](./templates)

<Tabs>
  <Tab title="Custom Event Push Template">
    Reference event properties using liquid syntax format:

    ```liquid Liquid theme={null}
    {{journey.event.name.properties.property_name | default: "fallback_value"}}
    ```

    **Message**:

    ```liquid Liquid theme={null}
    You left {{journey.event.cart_abandoned.properties.product_name | default: "items"}} in your cart.
    ```

    **Image**:

    ```liquid Liquid theme={null}
    {{journey.event.cart_abandoned.properties.product_image | default: "https://i.imgur.com/ssPCfbC.png"}}
    ```

    **Launch URL**:

    ```liquid Liquid theme={null}
    {{journey.event.cart_abandoned.properties.cart_url | default: "https://yourdomain.com/cart"}}
    ```

    <Warning>
      The image will not display if `product_image` is not a **direct**, **publicly accessible** image URL.

      If your `product_image` is the name of an image file available online, you can reference the image using the following format:
      `https://yourdomain.com/images/{{journey.event.cart_abandoned.properties.product_image | default: "stock_image"}}.png`
    </Warning>

    <Frame caption="Abandoned cart template example with Custom Events">
      <img src="https://mintcdn.com/onesignal/i980ujIG34-OaGfp/images/abandoned-cart/abandoned_cart_custom_event.png?fit=max&auto=format&n=i980ujIG34-OaGfp&q=85&s=30545021f3e1b12cdc741b3112540234" alt="Abandoned cart template example with Custom Events" width="2526" height="2104" data-path="images/abandoned-cart/abandoned_cart_custom_event.png" />
    </Frame>
  </Tab>

  <Tab title="Tag Push Template">
    Reference tag properties using liquid syntax format:

    ```liquid Liquid theme={null}
    {{tag_key | default: "fallback_value"}}
    ```

    **Message**:

    ```liquid Liquid theme={null}
    You left {{product_name | default: "items"}} in your cart.
    ```

    **Image**:

    ```liquid Liquid theme={null}
    {{product_image | default: "https://i.imgur.com/ssPCfbC.png"}}
    ```

    **Launch URL**:

    ```liquid Liquid theme={null}
    {{cart_url | default: "https://yourdomain.com/cart"}}
    ```

    <Warning>
      The image will not display if `product_image` is not a **direct**, **publicly accessible** image URL.

      If your `product_image` is the name of an image file available online, you can reference the image using the following format:
      `https://yourdomain.com/images/{{journey.event.cart_updated.properties.product_image | default: "stock_image"}}.png`
    </Warning>

    <Frame caption="Abandoned cart template example with Tags">
      <img src="https://mintcdn.com/onesignal/i980ujIG34-OaGfp/images/abandoned-cart/abandoned_cart_tags.png?fit=max&auto=format&n=i980ujIG34-OaGfp&q=85&s=00ed42a9890a824c8c201415b8260bba" alt="Abandoned cart template example with Tags" width="2526" height="2104" data-path="images/abandoned-cart/abandoned_cart_tags.png" />
    </Frame>
  </Tab>
</Tabs>

**Need email examples, help, or just more inspiration?**

<Columns cols={2}>
  <Card title="Personalize messages with Custom Events" icon="bolt" href="./personalization-custom-event">
    Complete guide to using Custom Events in Journeys. Includes event storage, Journey configuration, abandoned cart example, best practices, and troubleshooting.
  </Card>

  <Card title="Personalize messages with Properties" icon="tags" href="./personalization-properties-and-tags">
    Complete guide to using Properties and Tags in Journeys. Includes event storage, Journey configuration, abandoned cart example, best practices, and troubleshooting.
  </Card>
</Columns>

### Step 4. Create abandoned cart Segment (Tags only)

<Warning>
  This step is only required if you are using Tags to track cart activity. If you are using Custom Events, you can skip this step.
</Warning>

The Segment will determine who can enter the Journey. See [Segments](./segmentation) for more details.

Select the **User Tag** filter to track users where the `cart_updated` tag `exists` **AND** select the **Last Session** filter is `less than` `7` `days ago`

<Frame caption="Abandoned Cart Segment with Tag Filter where the cart_updated tag exists and the last session is less than 7 days ago">
  <img src="https://mintcdn.com/onesignal/S9ays8OQNCtB_HtE/images/segments/tag-filter-cart-updated.png?fit=max&auto=format&n=S9ays8OQNCtB_HtE&q=85&s=cad98d453f9955591bfec8e9ef1c1ae8" alt="Abandoned Cart Segment with Tag Filter where the cart_updated tag exists and the last session is less than 7 days ago" width="2718" height="1414" data-path="images/segments/tag-filter-cart-updated.png" />
</Frame>

<Check>
  We can now track users that update their cart and have visited the app or website in the last 7 days.

  Users will be automatically removed from the segment when either of the following conditions are met:

* After 7 days have passed since they last visited the app/website
* When the `cart_updated` tag is removed
</Check>

### Step 5. Create the abandoned cart Journey

Create a Journey that reacts to cart activity. See [Journeys](./journeys-overview) for more details.

<Frame caption="New Abandoned Cart Journey create screen">
  <img src="https://mintcdn.com/onesignal/nGF0iEnzRCJ61U4u/images/journeys/new-journey-screen.png?fit=max&auto=format&n=nGF0iEnzRCJ61U4u&q=85&s=373c8bea9b7f399af4623fe18eb50f9b" alt="New Abandoned Cart Journey create screen" width="2234" height="930" data-path="images/journeys/new-journey-screen.png" />
</Frame>

#### Journey settings

Review the [Journey Settings](./journeys-settings) guide for more details on Entry, Exit, and Re-entry rules.

**Entry Rules**:

<Tabs>
  <Tab title="Custom Event: Entry Rules">
    * Select **Custom Event**
    * Custom Event Name: `cart_abandoned`

    <Warning> Users enter the Journey every time the `cart_abandoned` event is sent. Only send this event after a meaningful inactivity period. </Warning>

    <Frame caption="Abandoned Cart Journey Custom Event Entry Rules">
      <img src="https://mintcdn.com/onesignal/FtxZDfbFgMsm3lF9/images/journeys/journey-entry-rules-custom-event.png?fit=max&auto=format&n=FtxZDfbFgMsm3lF9&q=85&s=6b4d38c9ca2a58806fd16dc0bbf25fd7" alt="Abandoned Cart Journey Custom Event Entry Rules" width="2882" height="1826" data-path="images/journeys/journey-entry-rules-custom-event.png" />
    </Frame>
  </Tab>

  <Tab title="Tag: Entry Rules">
    * Select **Audience Segment**
    * Include Segment: **Abandoned Cart - cart\_updated**

    <Frame caption="Abandoned Cart Journey Entry Rules">
      <img src="https://mintcdn.com/onesignal/nGF0iEnzRCJ61U4u/images/journeys/journey-entry-rules-audience-segment.png?fit=max&auto=format&n=nGF0iEnzRCJ61U4u&q=85&s=d3f3cbd94f91fa80aaa293c5beb44ade" alt="Abandoned Cart Journey entry rules" width="2672" height="1586" data-path="images/journeys/journey-entry-rules-audience-segment.png" />
    </Frame>
  </Tab>
</Tabs>

**Exit Rules**:

<Tabs>
  <Tab title="Custom Event: Exit Rules">
    * Select **Meet a certain condition**
    * Check **Exit when custom event condition occurs**
    * Custom Event Name: `cart_emptied`

    <Frame caption="Abandoned Cart Journey Custom Event Exit Rules">
      <img src="https://mintcdn.com/onesignal/nGF0iEnzRCJ61U4u/images/journeys/journey-exit-rules-meet-certain-condition-custom-event.png?fit=max&auto=format&n=nGF0iEnzRCJ61U4u&q=85&s=d1becfc614fb291a8d506df8a04d8b98" alt="Abandoned Cart Journey Custom Event Exit Rules" width="2648" height="1488" data-path="images/journeys/journey-exit-rules-meet-certain-condition-custom-event.png" />
    </Frame>

    <Info>
      Users will exit the Journey when either:

      * The `cart_emptied` event (from step 3) is performed.
      * They complete the Journey.
    </Info>
  </Tab>

  <Tab title="Tag: Exit Rules">
    * Select **Meet a certain condition**
    * Check **Exit when a user no longer matches the audience conditions**

    <Frame caption="Abandoned Cart Journey Tag Exit Rules">
      <img src="https://mintcdn.com/onesignal/nGF0iEnzRCJ61U4u/images/journeys/journey-exit-rules-meet-certain-condition-tag.png?fit=max&auto=format&n=nGF0iEnzRCJ61U4u&q=85&s=e54a4770bccb5ad096602a2d2f826cc1" alt="Abandoned Cart Journey Tag Exit Rules" width="2672" height="1586" data-path="images/journeys/journey-exit-rules-meet-certain-condition-tag.png" />
    </Frame>

    <Info>
      Users will exit the Journey when either:

      * They leave the segment.
      * They complete the Journey.
    </Info>
  </Tab>
</Tabs>

**Re-entry Rules** (Tags only):

* Select **Yes, after a certain amount of time**
* Set the re-entry time to `1` `day`

<Frame caption="Abandoned Cart Journey Re-entry Rules">
  <img src="https://mintcdn.com/onesignal/nGF0iEnzRCJ61U4u/images/journeys/journey-re-entry-rules-after-certain-amount-of-time.png?fit=max&auto=format&n=nGF0iEnzRCJ61U4u&q=85&s=b4faa54340c9c6a274aaafe6baf231a9" alt="Abandoned Cart Journey Re-entry Rules" width="2644" height="1024" data-path="images/journeys/journey-re-entry-rules-after-certain-amount-of-time.png" />
</Frame>

<Check>
  If you have followed this guide completely so far, then users will:

  1. Enter the Journey when they abandon/update their cart
  2. Exit the Journey when they empty their cart or complete the Journey.
  3. Be eligible to re-enter the Journey:
     * **Custom Events**: Each time the `cart_abandoned` event is performed
     * **Tags**: After 1 day has passed since they last exited the Journey and are in the segment.

  Save the Journey Settings.
</Check>

#### Journey steps

Users will enter the Journey when they match the Segment. This typically happens within a few minutes after the event/tag is received.

Users will flow through the Journey step by step until they reach the end or an exit rule is met.

For a basic abandoned cart Journey, we want to do 2 things:

1. Give the user enough time to empty their cart (make a purchase or empty their cart manually)
2. If they do not empty their cart, send them a message reminding them about the items in their cart

Achieve this by first adding a **Wait** step to the Journey.

* Set the wait time to be as long as you want. We recommend setting it to `1` `hour` so you can message them while they still have the intent to purchase.

Add a **Message** step.

* Select the **Abandoned Cart** Push Notification template you created in Step 4.

<Frame caption="Basic Abandoned Cart Journey Steps">
  <img src="https://mintcdn.com/onesignal/FtxZDfbFgMsm3lF9/images/journeys/journey-steps-basic-abandoned-cart.png?fit=max&auto=format&n=FtxZDfbFgMsm3lF9&q=85&s=8af2e8a35043af3b053fda36f251c2c4" alt="Basic Abandoned Cart Journey Steps" width="2526" height="2104" data-path="images/journeys/journey-steps-basic-abandoned-cart.png" />
</Frame>

<Check>
  Basic Abandoned Cart Journey is now configured.

  When a user enters the Journey, they will wait for 1 hour. If they do not exit the Journey, they will receive the abandoned cart push notification.
</Check>

## Advanced Journey Setup

Using the knowledge you have gained from this guide, you can now extend the Journey to send more messages over time.

#### Message Sequence

A best practice timing sequence for a very common high-performing cadence is:

1. Send the first message after 1 hour (completed in this guide).
2. Add another **Wait** step for 1 day and send a second message (\~24 hours since they updated their cart).
3. Add another **Wait** step for 2 days and send a third message (\~72 hours since they updated their cart).

**Message Types and Content:**

Depending on which channels you setup with OneSignal, you will achive better results using an omnichannel approach.

1. This guide shows how to send a push notification message after the first hour. This is used as a helpful reminder to try capturing the sale while the user may still be online.
2. Consider using both a push and email for your 2nd message. Use this second message to highlight benefits and social proof with light urgency to encourage them to purchase.
3. For the final message of the sequence, use an email or maybe an SMS (depending on the use case) as a "last call". Consider using a discount code or other incentive to encourage them to purchase.

#### Fallback Messages

OneSignal's Journeys provide **Wait Until** branching logic that you can use to check if a message was confirmed delivered, clicked or opened and if not performed within a certain time period, send a fallback message.

This is extremely helpful for users who may have unsubscribed from a specific message channel. More details on how to setup fallback messages can be found in our [Fallback Messages](./push-fallback-method) guide.

### Track performance

[Journey analytics](./journeys-analytics) can be used to track how the Journey as a whole is performing. You can also track each message performance using [Template analytics](./template-analytics).

#### Track revenue with Outcomes

To track revenue from this Journey, you can use [Custom Outcomes](./custom-outcomes).

When a purchase is made, you can send the event as a "Custom Outcome" to track the revenue associated with the specific message sent.

Custom Outcomes can be sent via the [Mobile SDK](./mobile-sdk-reference#outcomes) or [Web SDK](./web-sdk-reference#outcomes).

```javascript Example: Send purchase outcome via frontend SDK theme={null}
// Example: capture total price and item count at checkout
const checkoutPriceTotal = document.querySelector(".checkout-price-total").innerText;
const checkoutItemsTotal = document.querySelector(".checkout-items-total").innerText;

function updateOSOnCartPurchase(checkoutPriceTotal, checkoutItemsTotal) {
  const purchasePriceTotal = parseFloat(checkoutPriceTotal);
  const purchasedItemCount = parseInt(checkoutItemsTotal);

  OneSignalDeferred.push(function (OneSignal) {
    OneSignal.Session.sendOutcome("Purchase", purchasePriceTotal);
    OneSignal.Session.sendOutcome("Purchased Item Count", purchasedItemCount);
  });
}

const submitPurchaseButton = document.querySelector(".submit-payment");
if (submitPurchaseButton) {
  submitPurchaseButton.addEventListener("click", () => {
    updateOSOnCartPurchase(checkoutPriceTotal, checkoutItemsTotal);
  });
}
```

<Info>
  Outcomes can attribute revenue to messages users clicked or were influenced by within a defined attribution window.
</Info>

<Check>
  You have successfully implemented an abandoned cart Journey. When you are ready to start sending messages, select **Set Live**.
</Check>

<Info>
  Need help?

  Chat with our Support team or email `support@onesignal.com`

  Please include:

* Details of the issue you're experiencing and steps to reproduce if available
* Your OneSignal App ID
* The External ID or Subscription ID if applicable
* The URL to the message you tested in the OneSignal Dashboard if applicable
* Any relevant [logs or error messages](/docs/en/capturing-a-debug-log)

  We're happy to help!
</Info>

***

Built with [Mintlify](https://mintlify.com).
