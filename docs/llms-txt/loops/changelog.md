# Source: https://loops.so/docs/api-reference/changelog.md

# API Changelog

> Stay up-to-date with changes to our API and webhooks.

<Update label="October 17, 2025">
  New: an [`email.resubscribed`](/webhooks#email-resubscribed) webhook event for
  when contacts resubscribe to your marketing email from an email's
  "Unsubscribe" link.
</Update>

<Update label="October 13, 2025">
  New: an `optInStatus` field from [double opt-in](/contacts/double-opt-in) in
  the [Find contact](/api-reference/find-contact) endpoint and in
  `contact.created` [webhook events](/webhooks).
</Update>

<Update label="September 29, 2025">
  New: [webhooks](/webhooks) are now available to all users.
</Update>

<Update label="September 11, 2025">
  Improvement: all endpoints now return a `success` and `message` field in the error response bodies.

  `error` and `path` top-level keys are now deprecated but will continue to be supported for some time for backwards compatibility.
</Update>

<Update label="August 21, 2025">
  The docs have been updated to reflect that the `email` parameter is optional
  in the [Update contact](/api-reference/update-contact) endpoint if a `userId`
  is provided.
</Update>

<Update label="May 23, 2025">
  Improvement: data variables are now optional in the [Send transactional
  email](/api-reference/send-transactional-email) endpoint. [Read
  more](/transactional#optional-data-variables)
</Update>

<Update label="April 29, 2025">
  New: an `Idempotency-Key` header when [sending
  events](/api-reference/send-event).
</Update>

<Update label="March 28, 2025">
  New: an `Idempotency-Key` header when [sending transactional
  emails](/api-reference/send-transactional-email).
</Update>

<Update label="February 28, 2025">
  New: an endpoint for [listing transactional
  emails](/api-reference/list-transactional-emails) and their data variables.
</Update>

<Update label="February 5, 2025">
  New: [webhooks](/webhooks) are in Beta.
</Update>

<Update label="January 14, 2025">
  New: new endpoints for [creating contact properties](/api-reference/create-contact-property) and [listing contact properties](/api-reference/list-contact-properties).

  Depcrecation: the [List custom fields](/api-reference/list-custom-fields) endpoint is now deprecated in favor of the new [List contact properties](/api-reference/list-contact-properties) endpoint.
</Update>

<Update label="December 18, 2024">
  New: we added `description` to mailing list objects in the [List mailing
  lists](/api-reference/list-mailing-lists) endpoint.
</Update>

<Update label="November 5, 2024">
  Improvement: the maximum payload size for the transactional endpoint has been
  increased from 1MB to 4MB, allowing for more or larger attachments.
</Update>

<Update label="September 6, 2024">
  New: our new [Nuxt module](/sdks/nuxt) is now out!
</Update>

<Update label="August 16, 2024">
  New: our new [Ruby SDK](/sdks/ruby) is available!
</Update>

<Update label="August 15, 2024">
  New: we added an `isPublic` attribute to mailing list objects in the [List
  mailing lists](/api-reference/list-mailing-lists) endpoint.
</Update>

<Update label="June 28, 2024">
  New: there's a new `addToAudience` parameter in the [Send transactional
  email](/api-reference/send-transactional-email) endpoint can add contacts to
  your audience.
</Update>

<Update label="June 18, 2024">
  New: support for our new [mailing lists](/contacts/mailing-lists) feature.

  You can now add contacts to and remove contacts from mailing lists in the [Create contact](/api-reference/create-contact), [Update contact](/api-reference/update-contact) and [Send event](/api-reference/send-event) endpoints.

  There is also a [new endpoint](/api-reference/list-mailing-lists) for retrieving your mailing lists.
</Update>

<Update label="April 18, 2024">
  New: you can now [Find contacts](/api-reference/find-contact) by `userId`.
</Update>

<Update label="April 9, 2024">
  New: a new endpoint for testing your integration and/or API key: [API
  key](/api-reference/api-key).
</Update>

<Update label="March 21, 2024">
  New: you can now include [event properties](/events/properties) in requests to
  the [Send event](/api-reference/send-event) endpoint.
</Update>

<Update label="March 13, 2024">
  Improvement: we removed behavior that returned a `400 Bad Request` response if
  an unrecognized property was added to Contact endpoints.
</Update>

<Update label="February 9, 2024">
  Improvement: sending in a payload that contains an unrecognized property will
  now return a `400 Bad Request` response.
</Update>

<Update label="January 25, 2024">
  Clarification in the API docs that `userId` can be used in a [Send
  event](/api-reference/send-event) request.
</Update>

<Update label="November 6, 2023">
  New: we added a new endpoint for [querying custom contact
  properties](/api-reference/list-custom-fields).
</Update>

<Update label="October 30, 2023">
  Our [official JavaScript/TypeScript SDK](/sdks/javascript) is now available!
</Update>

<Update label="October 12, 2023">
  New: we now accept dates as a custom [contact property](/contacts/properties)
  type. [View the available formats](/contacts/properties#dates).
</Update>
