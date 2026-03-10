# Source: https://firebase.google.com/docs/ai-logic/server-prompt-templates/best-practices-and-considerations.md.txt

> [!WARNING]
> **Preview**: Using server prompt templates is a feature that's in Preview, which means that it isn't subject to any SLA or deprecation policy and could change in backwards-incompatible ways.

<br />

This page describes some [best practices](https://firebase.google.com/docs/ai-logic/server-prompt-templates/best-practices-and-considerations#best-practices) and considerations
for server prompt templates, including
[not-yet-supported features](https://firebase.google.com/docs/ai-logic/server-prompt-templates/best-practices-and-considerations#not-yet-supported). Note that many of these
features are only not available at the initial release of
server prompt templates, so check the
[release notes](https://firebase.google.com/support/releases) for updates!

## Best practices

Many of these best practices are also detailed in
[Manage your templates](https://firebase.google.com/docs/ai-logic/server-prompt-templates/manage-templates).

### Version your templates

- Create template IDs appended with a version that uses
  [semantic versioning (semver)](https://semver.org/).

- Use
  [Firebase Remote Config](https://firebase.google.com/docs/ai-logic/server-prompt-templates/versioning-with-remote-config)
  so that you can easily change the template and other values in your request.

### Protect your template

- Lock your template before going to production. And avoid editing templates
  that are used in production.

  - Locking a template acts as protection against unintentional editing, but
    locking *does **not** entirely block editing*. A project member with the
    appropriate permissions can always unlock a template to edit it.

  - We recommend locking templates that are actively being used by code --
    especially production code.

- Write strong
  [input validation](https://firebase.google.com/docs/ai-logic/server-prompt-templates/syntax-and-examples#gemini-input-validation-and-schema)
  for your input variables, which can help with the following:

  - Can help protect against prompt injection.
  - Can help ensure requests succeed and responses are as expected.

## Not-yet-supported features

Many of these not-yet-supported features are only not available at the initial
release, so check the [release notes](https://firebase.google.com/support/releases) for updates!

### Not-yet-supported capabilities of Firebase AI Logic

Server prompt templates do ***not*** yet support the following capabilities of
Firebase AI Logic. Several of these capabilities are coming soon!

- Chat
- Using tools (including function calling and grounding with Google Search)
- Iterative editing of images (chat) with Gemini models (requires chat)
- Editing images with Imagen models
- Bidirectional streaming (Gemini Live API)
- Hybrid or on-device inference
- Constraining the output to a list of enums

Also note that if you use AI monitoring in the Firebase console, the
template ID is not yet populated in any record.

### Not-yet-supported common elements of Dotprompt

Server prompt templates ***will likely soon*** support the following common
elements of Dotprompt:

- Using the
  [JSON schema specification](https://json-schema.org/)
  for input and output schemas in your frontmatter.

  - Note that this spec isn't supported in non-server template requests either. We currently only support the [OpenAPI schema specification](https://swagger.io/specification/).
- Declaring a wildcard field definition using `*`.

- Using `@key` or generally iterating over the fields of an object input
  (which is the case where `@key` is relevant).

- Using `@root`, which lets you reference the root variable context regardless
  of current `this`.

Server prompt templates ***will likely not*** support the following common
elements of Dotprompt:

- Using partials, which are reusable template snippets that can be included in other templates.

## Other considerations

- By default, when you use the guided UI in the Firebase console, we
  provision the template in all
  [available regions for Firebase AI Logic](https://firebase.google.com/docs/ai-logic/locations?api=vertex#available-locations).
  If you use the Vertex AI Gemini API and if your use case requires
  location-based restrictions, you can
  [specify the location for your template](https://firebase.google.com/docs/ai-logic/server-prompt-templates/advanced-workflows)
  using the REST API.

- If you want to
  [provide a server prompt template as a file](https://firebase.google.com/docs/ai-logic/server-prompt-templates/advanced-workflows)
  (instead of using the Firebase console's guided UI), you can use the
  REST API. Note that server prompt templates do *not* support schema defined in
  app code and passed into the template.

- Even though the template is on the server, it cannot ***directly*** interact
  with your Firebase project's other server-side resources (like a database)
  *except for Cloud Storage for Firebase URLs* (which can be provided as input
  variables).