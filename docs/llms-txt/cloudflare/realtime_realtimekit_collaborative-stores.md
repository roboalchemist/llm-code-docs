# Source: https://developers.cloudflare.com/realtime/realtimekit/collaborative-stores/index.md

---

title: Storage and Broadcast · Cloudflare Realtime docs
description: The RealtimeKit Stores API allows you to create multiple key-value
  pair realtime stores. Users can subscribe to changes in a store and receive
  real-time updates. Data is stored until a session is active.
lastUpdated: 2026-01-27T05:43:49.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/collaborative-stores/
  md: https://developers.cloudflare.com/realtime/realtimekit/collaborative-stores/index.md
---

The RealtimeKit Stores API allows you to create multiple key-value pair realtime stores. Users can subscribe to changes in a store and receive real-time updates. Data is stored until a [session](https://developers.cloudflare.com/realtime/realtimekit/concepts/meeting/#session) is active.

This page is not available for the **Flutter**platform.

### Create a Store

You can create a realtime store (changes are synced with other users):

| Param | Type | Description | Required |
| - | - | - | - |
| `name` | string | Name of the store | true |

To create a store:

Note

This method must be executed for every user.

### Update a Store

You can add, update or delete entires in a store:

| Param | Type | Description | Required |
| - | - | - | - |
| `key` | string | Unique identifier used to store/update a value in the store | Yes |
| `value` | StoreValue | Value that can be stored agains a key | Yes |

Note

The `set` method overwrites the existing value, while the `update` method updates the existing value.

For example, if the stored value is `['a', 'b']` and you call `update` with `['c']`, the final value will be `['a', 'b', 'c']`.

### Subscribe to a Store

You can attach event listeners on a store's key, which fire when the value changes.

### Fetch Store Data

You can fetch the data stored in the store:
