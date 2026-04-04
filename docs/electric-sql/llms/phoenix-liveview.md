# Source: https://electric-sql.com/demos/phoenix-liveview.md

---
url: /demos/phoenix-liveview.md
description: Example of a Phoenix LiveView app using Electric.
---

# {{ $frontmatter.title }}

{{ $frontmatter.description }}

## Syncing into Phoenix LiveView using Electric

This is an example app using our [`Electric.Phoenix`](/docs/integrations/phoenix) integration library.

It uses Electric for read-path sync into a LiveView using [`electric_stream/4`](https://hexdocs.pm/electric_phoenix/Electric.Phoenix.LiveView.html#electric_stream/4) and standard Phoenix APIs for writes. This keeps the LiveView automatically in-sync with Postgres, without having to re-run queries or trigger any change handling yourself.

See e.g.: [`lib/electric_phoenix_example_web/live/todo_live/index.ex`](https://github.com/electric-sql/electric/blob/main/examples/phoenix-liveview/lib/electric_phoenix_example_web/live/todo_live/index.ex):

<<< @../../examples/phoenix-liveview/lib/electric\_phoenix\_example\_web/live/todo\_live/index.ex{elixir}
