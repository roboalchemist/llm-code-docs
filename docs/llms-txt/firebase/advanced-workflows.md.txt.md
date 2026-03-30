# Source: https://firebase.google.com/docs/ai-logic/server-prompt-templates/advanced-workflows.md.txt

> [!WARNING]
> **Preview**: Using server prompt templates is a feature that's in Preview, which means that it isn't subject to any SLA or deprecation policy and could change in backwards-incompatible ways.

<br />

For Firebase AI Logic, the Firebase console provides a guided UI for you
to specify the contents of a template. However, there are several use cases
where you may need more advanced ways to set up a template, including:

- [Specify a location for a template](https://firebase.google.com/docs/ai-logic/server-prompt-templates/advanced-workflows#specify-location-for-template)

- [Provide the template as a file](https://firebase.google.com/docs/ai-logic/server-prompt-templates/advanced-workflows#provide-template-as-file)

The advanced workflows described in this page use the
[Firebase AI Logic REST API](https://firebase.google.com/docs/reference/ai-logic/rest).

**Be aware of the following when using the REST API:**

- If you provision a template in a specific location, then the request from your
  app must access the model in that same location. If the locations don't
  match, then the request will fail.

- The list of templates in the Firebase console only shows templates that are
  (at minimum) provisioned in the `global` location.

- If a template is unlocked, then you can overwrite the template by using the
  same template ID in your REST API call. A locked template cannot be
  overwritten.

## Specify a location for a template

This section is only applicable if you're using the Vertex AI Gemini API
and your use case requires location-based restrictions. Learn more about
[setting a location for accessing a model](https://firebase.google.com/docs/ai-logic/locations?api=vertex).

By default, when you use the guided UI in the Firebase console, we provision
the template in all
[available regions for Firebase AI Logic](https://firebase.google.com/docs/ai-logic/locations?api=vertex#available-locations).
We do this so that no matter what location you set in your request, the template
will be available.
However, if you want your template to
***only be available in a specific location***, then you need to create the
template using our REST API.

When you call the
[`projects.locations.templates.create` endpoint](https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/create),
specify the `location` of the template as part of creating a
[`PromptTemplate`](https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates).

## Provide the template as a file

You can provide the contents of a server prompt template file by calling the
[`projects.locations.templates.create` endpoint](https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/create).