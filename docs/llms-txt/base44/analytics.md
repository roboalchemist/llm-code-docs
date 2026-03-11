# Source: https://docs.base44.com/developers/references/sdk/docs/interfaces/analytics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# analytics

***

## Overview

Analytics module for tracking custom events in your app.

Use this module to track specific user actions. Track things like button clicks, form submissions, purchases, and feature usage.

<Note> Analytics events tracked with this module appear as custom event cards in the [Analytics dashboard](/documentation/performance-and-seo/app-analytics).</Note>

### Best Practices

When tracking events:

* Choose clear, descriptive event names in snake\_case like `signup_button_click` or `purchase_completed` rather than generic names like `click`.
* Include relevant context in your properties such as identifiers like `product_id`, measurements like `price`, and flags like `is_first_purchase`.

### Authentication Modes

This module is only available in user authentication mode (`base44.analytics`).

## Methods

### track()

> **track**(`params`): `void`

Tracks a custom event that appears as a card in your Analytics dashboard.

Each unique event name becomes its own card showing total count and trends over time. This method returns immediately and events are sent in batches in the background.

#### Parameters

<ParamField body="params" type="TrackEventParams" required>
  Event parameters.
</ParamField>

<Accordion title="Properties">
  <ParamField body="eventName" type="string" required>
    Name of the event to track.

    Use descriptive names like `button_click`, `form_submit`, or `purchase_completed`.
  </ParamField>

  <ParamField body="properties" type="TrackEventProperties">
    Optional key-value pairs with additional event data.

    Values can be strings, numbers, booleans, or null.
  </ParamField>
</Accordion>

#### Returns

`void`

#### Examples

<CodeGroup>
  ```typescript Track a button click theme={null}
  base44.analytics.track({
    eventName: 'signup_button_click'
  });
  ```

  ```typescript Track with properties theme={null}
  base44.analytics.track({
    eventName: 'add_to_cart',
    properties: {
      product_id: 'prod_123',
      product_name: 'Premium Widget',
      price: 29.99,
      quantity: 2,
      is_first_purchase: true
    }
  });
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).