# Source: https://braintrust.dev/docs/guides/traces/extend.md

# Extend traces

## Custom rendering for span fields

Although the built-in span viewers cover a variety of different span field display types— `YAML`, `JSON`, `Markdown`, LLM calls, and more—you may
want to further customize the display of your span data. For example, you could include the id of an internal database
and want to fetch and display its contents in the span viewer. Or, you may want to reformat the data in the span in a way
that's more useful for your use case than the built-in options.

Span iframes provide complete control over how you visualize span data, making them particularly valuable for when you have custom visualization needs or want to incorporate data from external sources. They also support interactive features - for example, you can implement custom human review feedback mechanisms like thumbs up/down buttons on image search results and write the scores directly to the `expected` or `metadata` fields.

To enable a span iframe, visit the **Configuration**
tab of a project, and create one. You can define the URL, and then customize its behavior:

* Provide a title, which is displayed at the top of the section.
* Provide, via [mustache](https://mustache.github.io/mustache.5.html), template parameters to the URL. These parameters are
  in terms of the top-level span fields, e.g. `{{input}}`, `{{output}}`, `{{expected}}`, etc. or their subfields, e.g.
  `{{input.question}}`.
* Allow Braintrust to send a message to the iframe with the span data, which is useful when the data may be very large and
  not fit in a URL.
* Send messages from the iframe back to Braintrust to update the span data.

### Quickstart

Since span iframes run your custom code, you need to host them somewhere. Tools like [val.town](https://www.val.town/) or [v0.dev](https://v0.dev/) make it easy to do this.

You can use [https://v0-render-iframe-data.vercel.app/](https://v0-render-iframe-data.vercel.app/) as a quick test. It renders a JSON object which shows you all of
the fields that are available in the span.

<img src="https://mintcdn.com/braintrust/NeSEVxg9fvrqX9MW/guides/traces/span-iframe-config.gif?s=87e1b910f868ef15fbfdf7896f186a54" alt="Span iframe" data-og-width="800" width="800" data-og-height="695" height="695" data-path="guides/traces/span-iframe-config.gif" data-optimize="true" data-opv="3" />

### iframe message format

In Zod format, the message schema looks like this:

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { z } from "zod";

export const settingsMessageSchema = z.object({
  type: z.literal("settings"),
  settings: z.object({
    theme: z.enum(["light", "dark"]),
    readOnly: z.boolean(),
  }),
});

export const iframeUpdateMessageSchema = z.object({
  type: z.literal("update"),
  field: z.string(),
  data: z.any(),
});

export const dataMessageSchema = z.object({
  type: z.literal("data"),
  data: z.object({
    input: z.array(z.record(z.unknown())),
  }),
});

export const messageSchema = z.union([
  settingsMessageSchema,
  dataMessageSchema,
]);
```

There are cases when the span data will be sent before the page is fully loaded. You can manually request span data by sending a message with `{ "type": "request-data" }` from your frame code.

### Sample workflow

Say you want to render the `input`, `output`, `expected`, and `id` fields for a given span in a table format for easier parsing.

<video className="border rounded-md" muted autoPlay poster="/images/guides/span-iframe-poster.png">
  <source src="https://mintlify.s3.us-west-1.amazonaws.com/braintrust/images/guides/span-iframes.mp4" type="video/mp4" />
</video>

<Steps>
  <Step>
    The first thing you'll need to do is choose where to host your table. Span iframes are externally hosted, either in your own infrastructure or a cloud hosting service. In this example, we'll use Val Town. Navigate to [val.town](https://www.val.town/) and create an account if you don't already have one.
  </Step>

  <Step>
    Next, you'll need to write the code for the component you'd like to render inside of your span, making sure that it uses the correct message handling to allow communication with Braintrust. To speed things up, we can go to [Townie](https://www.val.town/townie), Val Town's AI assistant that helps you get pages up and running quickly. Prompt the AI to generate your table code for you, keeping these few things in mind:

    * You'll want to add the message handling that allows the iframe to send messages back to Braintrust

    <Note>
      To do this, we use the [window.postMessage()](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) method behind the scenes.
    </Note>

    * You'll want to use some hardcoded span data to illustrate what it might look like in the preview before you ship

    For example, your prompt might look something like this:

    ```
    Create a table component in React that uses this type of message handling:

    "use client";

    import {
      Table,
      TableBody,
      TableCell,
      TableHead,
      TableHeader,
      TableRow,
    } from "@/components/ui/table";
    import { useEffect, useMemo, useState } from "react";
    import { z } from "zod";

    export const dataMessageSchema = z.object({
      type: z.literal("data"),
      data: z.object({
        input: z.array(z.record(z.string())),
      }),
    });

    export const settingsMessageSchema = z.object({
      type: z.literal("settings"),
      settings: z.object({
        theme: z.enum(["light", "dark"]),
        readOnly: z.boolean(),
      }),
    });

    export const messageSchema = z.union([
      dataMessageSchema,
      settingsMessageSchema,
    ]);

    export type Message = z.infer<typeof messageSchema>;

    export default function TablePage() {
      const [data, setData] = useState<Record<string, unknown>[]>([]);

      useEffect(() => {
        const handleMessage = (event: MessageEvent) => {
          try {
            const message = messageSchema.parse(event.data);
            if (message.type === "data") {
              setData(message.data.input);
            }
          } catch (error) {
            console.error("Invalid message received:", error);
          }
        };

        window.addEventListener("message", handleMessage);

        return () => {
          window.removeEventListener("message", handleMessage);
        };
      }, []);

      const headers = useMemo(
        () => (data.length > 0 ? Object.keys(data[0]) : []),
        [data]
      );

      if (data.length === 0) {
        return <div>No data</div>;
      }

      return (
        <Table>
          <TableHeader>
            <TableRow>
              {headers.map((header) => (
                <TableHead key={header}>{header}</TableHead>
              ))}
            </TableRow>
          </TableHeader>
          <TableBody>
            {data.map((row, i) => (
              <TableRow key={i}>
                {headers.map((header) => (
                  <TableCell key={header}>
                    {typeof row[header] === "string" ? row[header] : "N/A"}
                  </TableCell>
                ))}
              </TableRow>
            ))}
          </TableBody>
        </Table>
      );
    }

    Here's an example of how the data should look:
    {
      type: 'data',
      data: {
        span_id: 'd42cbeb6-aaff-43d6-8517-99bbbd82b941',
        input: "Some input text",
        output: "Some output text",
        expected: 1,
        metadata: { some: "additional info" }
      }
    }

    Use this sample span data to illustrate how the table will look:
    ID: initial-sample
    Input: An orphaned boy discovers he's a wizard on his 11th birthday when Hagrid escorts him to magic-teaching Hogwarts School.
    Output: Harry Potter and the Philosopher's Stone
    Expected: Harry Potter and the Sorcerer's Stone
    Metadata: null

    Make sure the Zod schema is flexible for different data types and make sure all the properties from the message are included. Also be sure to handle any undefined values.
    ```
  </Step>

  <Step>
    Townie will generate some code for you and automatically deploy it to a URL. Check it out and make sure the table looks how you'd like, then copy the URL.
  </Step>

  <Step>
    Lastly, go back to Braintrust and visit the **Configuration**
    tab of your project, then navigate down to the span iframe section. Paste in the URL of your hosted table.

        <img src="https://mintcdn.com/braintrust/NeSEVxg9fvrqX9MW/guides/traces/configure-span-iframe.png?fit=max&auto=format&n=NeSEVxg9fvrqX9MW&q=85&s=6eb43d87fa2ced4f0fb76656336e8cff" alt="Configure span iframe" data-og-width="3066" width="3066" data-og-height="1896" height="1896" data-path="guides/traces/configure-span-iframe.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/NeSEVxg9fvrqX9MW/guides/traces/configure-span-iframe.png?w=280&fit=max&auto=format&n=NeSEVxg9fvrqX9MW&q=85&s=d177f5812d657944056af54bcf6664e8 280w, https://mintcdn.com/braintrust/NeSEVxg9fvrqX9MW/guides/traces/configure-span-iframe.png?w=560&fit=max&auto=format&n=NeSEVxg9fvrqX9MW&q=85&s=57cab3a7ac2eb06c724119e50c1f8a6c 560w, https://mintcdn.com/braintrust/NeSEVxg9fvrqX9MW/guides/traces/configure-span-iframe.png?w=840&fit=max&auto=format&n=NeSEVxg9fvrqX9MW&q=85&s=941e066fda2ac524e13c40b5ba1eb9f4 840w, https://mintcdn.com/braintrust/NeSEVxg9fvrqX9MW/guides/traces/configure-span-iframe.png?w=1100&fit=max&auto=format&n=NeSEVxg9fvrqX9MW&q=85&s=008d544793c5fc19f43a27ea941f841a 1100w, https://mintcdn.com/braintrust/NeSEVxg9fvrqX9MW/guides/traces/configure-span-iframe.png?w=1650&fit=max&auto=format&n=NeSEVxg9fvrqX9MW&q=85&s=8e95ef827223777bb148a785dcefe3e9 1650w, https://mintcdn.com/braintrust/NeSEVxg9fvrqX9MW/guides/traces/configure-span-iframe.png?w=2500&fit=max&auto=format&n=NeSEVxg9fvrqX9MW&q=85&s=d9db4ee663ae433295222903779658d9 2500w" />
  </Step>
</Steps>

Now, when you go to a span in your project, you should see the table you created, but populated with the corresponding data for each span.

<img src="https://mintcdn.com/braintrust/NeSEVxg9fvrqX9MW/guides/traces/rendered-table-iframe.png?fit=max&auto=format&n=NeSEVxg9fvrqX9MW&q=85&s=529620b672d2805a92666f817975b087" alt="Rendered table iframe" data-og-width="2738" width="2738" data-og-height="1782" height="1782" data-path="guides/traces/rendered-table-iframe.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/NeSEVxg9fvrqX9MW/guides/traces/rendered-table-iframe.png?w=280&fit=max&auto=format&n=NeSEVxg9fvrqX9MW&q=85&s=2ce9437b4dbc24484003033c19326df5 280w, https://mintcdn.com/braintrust/NeSEVxg9fvrqX9MW/guides/traces/rendered-table-iframe.png?w=560&fit=max&auto=format&n=NeSEVxg9fvrqX9MW&q=85&s=de7912540b2b83cef9ba33d1da6c5e59 560w, https://mintcdn.com/braintrust/NeSEVxg9fvrqX9MW/guides/traces/rendered-table-iframe.png?w=840&fit=max&auto=format&n=NeSEVxg9fvrqX9MW&q=85&s=fb334259a454cf0a66e12d1e37a9b143 840w, https://mintcdn.com/braintrust/NeSEVxg9fvrqX9MW/guides/traces/rendered-table-iframe.png?w=1100&fit=max&auto=format&n=NeSEVxg9fvrqX9MW&q=85&s=0f29e337a16332f15c193e19821a0538 1100w, https://mintcdn.com/braintrust/NeSEVxg9fvrqX9MW/guides/traces/rendered-table-iframe.png?w=1650&fit=max&auto=format&n=NeSEVxg9fvrqX9MW&q=85&s=b6eb23015b7f7776c7ac25f05be3b84b 1650w, https://mintcdn.com/braintrust/NeSEVxg9fvrqX9MW/guides/traces/rendered-table-iframe.png?w=2500&fit=max&auto=format&n=NeSEVxg9fvrqX9MW&q=85&s=0aef850912e1e1b34dbea1cb2231e4c6 2500w" />

### Example code

To help you get started, check out the [braintrustdata/braintrust-viewers](https://github.com/braintrustdata/braintrust-viewers)
repository on Github, which contains example code for rendering a table, X/Tweet, and more.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt