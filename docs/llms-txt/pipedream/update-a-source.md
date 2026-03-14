# Source: https://pipedream.com/docs/rest-api/api-reference/sources/update-a-source.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a source

#### Endpoint

```
PUT /sources/{id}
```

#### Parameters

<ParamField body="component_id" type="string">
  The ID of a component previously created in your account. [See the component endpoints](/rest-api/#components) for information on how to retrieve this ID.
</ParamField>

***

<ParamField body="component_code" type="string">
  The full code for a [Pipedream component](/components/contributing/api/).
</ParamField>

***

<ParamField body="component_url" type="string">
  A reference to the URL where the component is hosted.
</ParamField>

For example, to create an RSS component, pass `https://github.com/PipedreamHQ/pipedream/blob/master/components/rss/sources/new-item-in-feed/new-item-in-feed.ts`.

***

One of `component_id`, `component_code`, or `component_url` is required. If all are present, `component_id` is preferred and `component_url` will be used only as metadata to identify the location of the code.

***

<ParamField body="name" type="string">
  The name of the source.
</ParamField>

If absent, this defaults to using the [name slug](/components/contributing/api/#component-structure) of the component used to create the source.

***

<ParamField body="active" type="boolean">
  The active state of a component. To disable a component, set to `false`. To enable a component, set to `true`.

  Default: `true`.
</ParamField>

Built with [Mintlify](https://mintlify.com).
