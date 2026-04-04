# Source: https://www.courier.com/docs/tutorials/sending/how-to-send-to-a-list-or-list-pattern-using-wildcarding.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How To Create And Send To A List Or List Pattern

> Learn how to structure Courier list IDs for wildcarding and send notifications to groups using lists or list patterns.

The Courier Lists API lets you create Lists and associate one or more recipients with them in the Courier database. Then send to a list or a list pattern. Following the list pattern guidelines outlined in this document enables wildcarding.

<iframe width="100%" height="400" src="https://www.youtube.com/embed/0k70TmgSK8o?si=dIL32x81U3lGtNvS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

## Why use Lists?

Many times there are groups of users you want to message with the same notification triggered by the same event. In the past, this meant tens or sometimes thousands of API calls, triggering the same notification over and over. With Courier’s Lists API, you’re able to create lists, subscribe recipient profiles to them and send to every user on the list with a single Send API call.

When you send to a list, Courier handles the message fan-out following user preferences and your channel priorities–to deliver across Push, Email, SMS, Messaging Apps, and more.

With the Lists API, you can easily do things like:

* Reach every user in a shared workspace.
* Notify all users who follow a specific project.
* Alert users subscribed to a blog category
* Message users who opt into specific notifications.

## What are Lists and Lists Patterns?

A list usually represents some kind object in your system. Once you've created a List, you can send a message to all the recipients you subscribed to that List with a single Send API call (Courier handles the fan-out).

When naming your Courier Lists, we recommend you follow our List Pattern guidelines. Using this pattern will allow you to use wildcarding to send to multiple Lists with a single Send API call.

## Understanding and defining List ID Patterns

Courier supports List IDs with up to four parts to enable wildcard sending.

Thinking about how to structure your List IDs according to Courier's List pattern support (up to four parts in a List) will allow you to send to multiple List parts within a related pattern using a single API call.

\*\*Follow this basic pattern when defining List IDs.

* `part1`
* `part1.part2`
* `part1.part2.part3`
* `part1.part2.part3.part4`

<Warning>
  You must specifically subscribe users to every list or list part that applies to them.
</Warning>

Each ID string is its own List. If you provide `part1.part2` as the List id when creating a List, that's a single List with the id of `part1.part2`

Example: subscribing a user to `part1.part2` *does not* automatically subscribe users to `part1`

## List Pattern Examples

**As an example, let's apply this relational pattern to Pokémon:**

* `pokemon`
* `pokemon.type`
* `pokemon.type.generation`
* `pokemon.type.generation.evolution`

**So a list of List IDs following this pattern could be:**

* `pokemon`
* `pokemon.grass`
* `pokemon.fire`
* `pokemon.grass.gen1`
* `pokemon.grass.gen2`
* `pokemon.fire.gen1`
* `pokemon.fire.gen2`
* `pokemon.grass.gen1.evolution1`
* `pokemon.fire.gen1.evolution1`

## Using Patterns and wildcards to send to multiple Lists at a time

Following this four-part List pattern allows you to send to more than one List at the same time by using wildcards. You can wildcard up to 3 of the 4 parts within a List pattern.
Using a single asterisk `*` will wildcard every List within that part.

Using a double asterisk `**` will wildcard every List in every part that follows the first part. IE it's like saying "all List that start with".

**Here are a few wildcard examples using our Pokemon Lists:**

**pokemon.\*.gen1**

`pokemon.*.gen1` would ***only*** send to the ***unique*** users subscribed to ***these exact lists:***

* `pokemon.grass.gen1`
* `pokemon.fire.gen1`

\*\*pokemon.grass.\* \*\*

`pokemon.grass.*` would ***only*** send to the ***unique*** users subscribed to ***these exact lists:***

* `pokemon.grass.gen1`
* `pokemon.grass.gen2`

**pokemon.fire.\*\***

`pokemon.fire.**` would ***only*** send to the ***unique*** users subscribed to ***these exact lists:***

* `pokemon.fire.gen1`
* `pokemon.fire.gen2`
* `pokemon.fire.gen1.evolution1`

**pokemon.\*\***
While `pokemon.**` would send to every ***unique*** user subscribed to any list below `pokemon`.

* `pokemon.grass`
* `pokemon.fire`
* `pokemon.grass.gen1`
* `pokemon.grass.gen2`
* `pokemon.fire.gen1`
* `pokemon.fire.gen2`
* `pokemon.grass.gen1.evolution1`
* `pokemon.fire.gen1.evolution1`

## Invalid Lists, List Patterns and Wildcards

<Warning>
  Examples of invalid list IDs, patterns and wildcarding
  The following are examples of invalid List IDs, Patterns and wildcarding that Courier List and Patterns do not support.

  **Invalid List IDs:**

  * Empty strings.
  * List IDs may not include \* or # in the in the name.
  * List IDs my not start or end with a period . or include consecutive periods ..
  * List IDs may not include spaces ex: list name would be invalid while, list\_name would be valid.
  * List IDs may not include more than four parts. ie root\_part.part.part.part.part etc. would be invalid.

  **Examples of Invalid List Patterns and wildcards**

  `**` : List Patterns cannot match all Lists. It is not possible to send to all Lists using wildcards, so sending a request with only (\*\*) will fail.

  `**.part` : List Pattern cannot include a starts with (\*\*) anywhere but at the end.

  `*.**` : List Pattern cannot include an asterisk (\*) followed by asterisks (\*\*)

  `part.*.` : List Pattern cannot end with a period (.).

  `.part.part` : List Pattern cannot start with a period (.).

  `..part.*` :List Pattern cannot include consecutive periods (..).

  `part.part.part` List Pattern cannot include spaces.

  `part.***` : List Pattern cannot include more than two consecutive asterisks.

  `poke**`, `pokemon.fire.g*` : The wildcard (\*) or (\*\*) must replace the entire part name within the List pattern.
</Warning>

## Sending to a list or list pattern

To send to a list or list pattern use the `POST /send` endpoint with the `message.to` object.

<Note>
  See the [Send API reference](/api-reference/send/send-a-message) for the full endpoint documentation.
</Note>

**Sending to a list**

<CodeGroup>
  ```bash cURL icon="terminal" wrap theme={null}
  curl -X POST https://api.courier.com/send \
    -H "Authorization: Bearer $COURIER_AUTH_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "message": {
        "to": {
          "list_id": "pokemon.grass"
        },
        "template": "YOUR_TEMPLATE_ID",
        "data": {
          "event_name": "New Pokémon discovered"
        }
      }
    }'
  ```

  ```javascript Node.js icon="node-js" theme={null}
  import Courier from "@trycourier/courier";

  const client = new Courier({ apiKey: "your_api_key" });

  await client.send.message({
    message: {
      to: { list_id: "pokemon.grass" },
      template: "YOUR_TEMPLATE_ID",
      data: { event_name: "New Pokémon discovered" },
    },
  });
  ```

  ```python Python icon="python" theme={null}
  from courier import Courier

  client = Courier(api_key="your_api_key")

  client.send.message(
      message={
          "to": {"list_id": "pokemon.grass"},
          "template": "YOUR_TEMPLATE_ID",
          "data": {"event_name": "New Pokémon discovered"},
      },
  )
  ```
</CodeGroup>

**Sending to a list pattern**

<CodeGroup>
  ```bash cURL icon="terminal" wrap theme={null}
  curl -X POST https://api.courier.com/send \
    -H "Authorization: Bearer $COURIER_AUTH_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "message": {
        "to": {
          "list_pattern": "pokemon.fire.**"
        },
        "template": "YOUR_TEMPLATE_ID",
        "data": {
          "event_name": "Fire-type tournament"
        }
      }
    }'
  ```

  ```javascript Node.js icon="node-js" theme={null}
  await client.send.message({
    message: {
      to: { list_pattern: "pokemon.fire.**" },
      template: "YOUR_TEMPLATE_ID",
      data: { event_name: "Fire-type tournament" },
    },
  });
  ```

  ```python Python icon="python" theme={null}
  client.send.message(
      message={
          "to": {"list_pattern": "pokemon.fire.**"},
          "template": "YOUR_TEMPLATE_ID",
          "data": {"event_name": "Fire-type tournament"},
      },
  )
  ```
</CodeGroup>

## What's Next

<CardGroup cols={2}>
  <Card title="Send Bulk Notifications" icon="envelopes-bulk" href="/tutorials/sending/how-to-send-bulk-notifications">
    Send notifications to many recipients with the Bulk API
  </Card>

  <Card title="Configure User Preferences" icon="sliders" href="/tutorials/preferences/how-to-configure-user-preferences">
    Let recipients control their notification preferences
  </Card>

  <Card title="Lists API Reference" icon="code" href="/api-reference/lists/get-all-lists">
    Full API documentation for creating and managing lists
  </Card>

  <Card title="Send API Reference" icon="paper-plane" href="/api-reference/send/send-a-message">
    Full API documentation for the Send endpoint
  </Card>
</CardGroup>
