# Source: https://developers.kit.com/api-reference/upgrading-to-v4.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Upgrading to V4

> Helping you upgrade from V3 of the API to V4

## General updates

* The URLs for the API endpoints are now `api.kit.com/v4/...` instead of `api.convertkit.com/v3/...`. They are otherwise unchanged unless called out specifically below.
* V4 supports OAuth for applications and API Keys for automating simple tools and integrations for your personal account. V4 API Keys are not compatible with V3
* Our pagination mechanism has changed. We no longer support page or offset based pagination. All of [our pagination is now cursor based](/api-reference/pagination). This improves performance.
* All errors are now returned with a consistent response shape. The response is a JSON object with a single attribute `errors`, an array of strings.
* See below for a list of endpoints changed

## Endpoint specific updates

### Accounts

* Get current account
  * [The response shape has changed](/api-reference/accounts/get-current-account). User and account information is now nested under `user` and `account` objects, respectively.

### Broadcasts

* List broadcasts
  * The `page` parameter is no longer supported. To request next or previous pages, [use the `before` or `after` cursor](/api-reference/pagination)
* Create a broadcast
  * The `email_layout_template` param is no longer supported. To specify the email template, use the `email_template_id` param.
    * [Query your email templates](/api-reference/email-templates/list-email-templates) to get the correct id
  * [The response shape has changed](/api-reference/broadcasts/create-a-broadcast). We no longer return `email_layout_template` and return an object for `email_template`.
  * The error response shape has changed.
* Get a broadcast
  * [The response shape has changed](/api-reference/broadcasts/get-a-broadcast). We no longer return `email_layout_template` and return an object for `email_template`.
  * The error response shape has changed.
* Delete a broadcast
  * [The response shape has changed](/api-reference/broadcasts/delete-a-broadcast). We return a 204 empty response.
  * The error response shape has changed.
* Update a broadcast
  * The `email_layout_template` param is no longer supported. To specify the email template, use the `email_template_id` param.
    * [Query your email templates](/api-reference/email-templates/list-email-templates) to get the correct id
  * [The response shape has changed](/api-reference/broadcasts/update-a-broadcast). We no longer return `email_layout_template` and return an object for `email_template`.
  * The error response shape has changed.
* Get stats
  * The error response shape has changed.

### Subscribers

* List subscribers
  * The `page` parameter is no longer supported. To request next or previous pages, [use the `before` or `after` cursor](/api-reference/pagination)
  * The `from`  parameter is no longer supported. It has been replaced with `created_after`.
  * The `to`  parameter is no longer supported. It has been replaced with `created_before`.
  * The `updated_from`  parameter is no longer supported. It has been replaced with `updated_after`.
  * The `updated_to`  parameter is no longer supported. It has been replaced with `updated_before`.
* Get a subscriber
  * The error response shape has changed.
* Update a subscriber
  * The error response shape has changed.
* Unsubscribe a subscriber
  * The URL path has changed. `/v3/unsubscribe` -> `/v4/subscribers/:id/unsubscribe`
  * We now require you to unsubscribe the subscriber via their id
    * If you need to find their id by email address, you can query with [List subscribers](/api-reference/subscribers/list-subscribers), `/v4/subscribers?email_address=<email>`
  * [The response shape has changed](/api-reference/subscribers/unsubscribe-subscriber). It returns a 204 empty response instead of the subscriber.
  * The error response shape has changed.
* List tags for a subscriber
  * [The response shape has changed](/api-reference/subscribers/list-tags-for-a-subscriber). `created_at` has been replaced with `tagged_at`.
  * The error response shape has changed.

### Custom Fields

* Create a custom field
  * [The response shape has changed](/api-reference/custom-fields/create-a-custom-field). The created custom field is now returned nested under a `custom_field` attribute.
  * This endpoint no longer allows creating multiple custom fields. Use [Bulk create custom fields](/api-reference/custom-fields/bulk-create-custom-fields) instead.
  * The error response shape has changed.
* Update a custom field
  * [The response shape has changed](/api-reference/custom-fields/update-a-custom-field). The updated custom field is returned nested under a `custom_field` attribute.
  * The error response shape has changed.

### Forms

* List forms
  * [The response shape has changed](/api-reference/forms/list-forms).
* Add subscriber to a form by email address
  * The `email` parameter is no longer supported. To add a subscriber by email address,
    use the `email_address` parameter.
* List subscribers to a form
  * The URL path has changed. `/v3/forms/:id/subscriptions` -> `/v4/forms/:id/subscribers`
  * [The response shape has changed](/api-reference/forms/list-subscribers-for-a-form). Subscriber information is no longer nested under `subscription`.

### Purchases

* List purchases
  * The `page` parameter is no longer supported. To request next or previous pages, [use the `before` or `after` cursor](/api-reference/pagination)
* Create a purchase
  * The error response shape has changed.

### Sequences

* List sequences
  * [The response shape has changed](/api-reference/sequences/list-sequences). Sequences are nested under a `sequences` attributes (instead of a `courses` attribute).
* Add subscriber to a sequence by email address
  * The `email` parameter is no longer supported. To add a subscriber by email address, use the `email_address` parameter.
* List subscribers to a sequence
  * The URL path has changed. `/v3/sequences/:id/subscriptions` -> `/v4/sequences/:id/subscribers`
  * [The response shape has changed](/api-reference/sequences/list-subscribers-for-a-sequence). Subscriber information is no longer nested under `subscription`.

### Tags

* Create a tag
  * [The request shape has changed](/api-reference/tags/create-a-tag). Root `tag` attribute no longer required
  * [The response shape has changed](/api-reference/tags/create-a-tag). The returned tag is nested under a `tag` attribute.
  * The error response shape has changed.
  * This endpoint no longer allows creating multiple tags. Use [Bulk create tags](/api-reference/tags/bulk-create-tags) instead.
* List subscribers for a tag
  * The URL path has changed. `/v3/tags/:id/subscriptions` -> `/v4/tags/:id/subscribers`
  * The `page` parameter is no longer supported. To request next or previous pages, [use the `before` or `after` cursor](/api-reference/pagination)
  * The error response shape has changed.
  * [The response shape has changed](/api-reference/tags/list-subscribers-for-a-tag). The root object is `subscribers` instead of `subscriptions` along with other smaller changes.
* Tag a subscriber
  * The URL path has changed. `/v3/tags/:id/subscribe` -> `/v4/tags/:tag_id/subscribers/:id`
  * [The response shape has changed](/api-reference/tags/tag-a-subscriber). The root object is `subscriber` instead of `subscription` along with other smaller changes.
  * The error response shape has changed.
  * None of the optional params from V3 are supported in V4
* Tag a subscriber by email address
  * The URL path has changed. `/v3/tags/:id/subscribe` -> `/v4/tags/:tag_id/subscribers`
  * The `email` parameter is no longer supported. To add a subscriber by email address, use the `email_address` parameter.
  * [The response shape has changed](/api-reference/tags/tag-a-subscriber). The root object is `subscriber` instead of `subscription` along with other smaller changes.
  * The error response shape has changed.
  * None of the optional request params from V3 are supported in V4
* Remove tag from subscriber
  * The URL path and HTTP verb has changed. `POST /v3/tags/:id/unsubscribe` -> `DELETE /v4/tags/:tag_id/subscribers/:id`
  * [The response shape has changed](/api-reference/tags/remove-tag-from-subscriber). We return a 204 empty response
  * The error response shape has changed.
* Remove tag from subscriber by email address
  * The URL path and HTTP verb has changed. `POST /v3/tags/:id/unsubscribe` -> `DELETE /v4/tags/:tag_id/subscribers/:id`
  * [The response shape has changed](/api-reference/tags/remove-tag-from-subscriber-by-email-address). We return a 204 empty response.
  * The error response shape has changed.

### Webhooks

* The URL paths for webhooks have changed from `/automations/hooks` to `/webhooks`.
* Create a webhook
  * [The response shape has changed](/api-reference/webhooks/create-a-webhook). The root object is `webhook` instead of `rule`.
  * The error response shape has changed.
* Delete a webhook
  * [The response shape has changed](/api-reference/webhooks/delete-a-webhook). We return a 204 empty response.
  * The error response shape has changed.


Built with [Mintlify](https://mintlify.com).