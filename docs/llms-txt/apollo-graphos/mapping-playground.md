# Source: https://www.apollographql.com/docs/graphos/connectors/tooling/mapping-playground.md

# Connectors Mapping Playground

The [Connectors Mapping Playground](https://www.apollographql.com/connectors-mapping-playground/?referrer=docs-content)
is an easy way to experiment with the Connectors mapping language and directives. It's useful for getting started with and tweaking complex Connectors.

## Playground modes

You can set the playground to one of two modes, **Basic** or **Connector**, using the toggle at the top of the page:

When embedded in a page, this mode toggle is usually not available.
Instead, the playground is set to whichever mode makes sense for the example.

* The **API Response** and **Variables** panels on the left are input panels shared between both modes, so you can quickly flip back and forth.
* The central input panel changes depending on the mode.
* The **Results** panel on the right corresponds to the playground mode and input.

### Basic mode

Basic mode focuses on a particular mapping expression, allowing you to iterate with better diagnostics on your Connector's selection mapping.

You enter a sample response into the **API Response** panel and a mapping expression into the **Mapping** panel to experiment with the results. You can copy the mapping expression from your IDE or fine tune one from Connector mode.

### Connector mode

Connector mode builds off of Basic mode. Instead of just providing a mapping expression, you can simulate an entire Connector using `@connect` and (optionally) `@source` directives.

Including both `@source` and `@connect` allows you to visualize how an HTTP request will be created by combining the components of each.

The request will be presented as a `curl` command in the right panel. After running the `curl` command, you can copy the response into the **API Response** panel to test your Connector and `selection`.

#### Differences between the Connector mode and an IDE

This mode is a quick way to iterate on a *single* Connector, so there are some important differences between what you see here and what you get in an IDE:

* Only the *first* `@connect` instance is considered, so only paste the relevant parts of your schema.
* While the GraphQL schema you input must be valid, most of it will be ignored
  * Specifically, `$args`, `$this`, and `$batch` aren't schema-aware.
  * You must fill in the desired values in the **Variables** panel.
* Most validations are turned off, so even if something is working in the playground, you may get errors in your IDE.

## Sharing examples

The entire state of the playground is saved in the URL.
If you want to share an example with someone, just copy the URL and send it to them.

Because URLs encode the full state of the playground (including **API Response** and **Variables**), do not share playground URLs that contain sensitive values.
