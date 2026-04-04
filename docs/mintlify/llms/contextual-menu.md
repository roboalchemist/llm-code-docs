# Source: https://www.mintlify.com/docs/ai/contextual-menu.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Contextual menu

> Add one-click AI integrations to your docs.

export const PreviewButton = ({children, href}) => {
  return <a href={href} className="text-sm font-medium text-white dark:!text-zinc-950 bg-zinc-900 hover:bg-zinc-700 dark:bg-zinc-100 hover:dark:bg-zinc-300 rounded-full px-3.5 py-1.5 not-prose">
        {children}
      </a>;
};

The contextual menu provides quick access to AI-optimized content and direct integrations with popular AI tools. When users select the contextual menu on any page, they can copy content as context for AI tools or open conversations in ChatGPT, Claude, Perplexity, or a custom tool of your choice with your documentation already loaded as context.

## Menu options

The contextual menu includes several pre-built options that you can enable by adding their identifier to your configuration.

| Option                  | Identifier   | Description                                                              |
| :---------------------- | :----------- | :----------------------------------------------------------------------- |
| **Copy page**           | `copy`       | Copies the current page as Markdown for pasting as context into AI tools |
| **View as Markdown**    | `view`       | Opens the current page as Markdown                                       |
| **Open in ChatGPT**     | `chatgpt`    | Creates a ChatGPT conversation with the current page as context          |
| **Open in Claude**      | `claude`     | Creates a Claude conversation with the current page as context           |
| **Open in Perplexity**  | `perplexity` | Creates a Perplexity conversation with the current page as context       |
| **Open in Grok**        | `grok`       | Creates a Grok conversation with the current page as context             |
| **Copy MCP server URL** | `mcp`        | Copies your MCP server URL to the clipboard                              |
| **Connect to Cursor**   | `cursor`     | Installs your hosted MCP server in Cursor                                |
| **Connect to VS Code**  | `vscode`     | Installs your hosted MCP server in VS Code                               |
| **Custom options**      | Object       | Add custom options to the contextual menu                                |

<Frame>
  <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/contextual-menu/contextual-menu.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=b37c2bfffdc0db86422a7f7e692adaf7" alt="The expanded contextual menu showing the Copy page, View as Markdown, Open in ChatGPT, and Open in Claude menu items." data-og-width="1396" width="1396" data-og-height="944" height="944" data-path="images/contextual-menu/contextual-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/contextual-menu/contextual-menu.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=1e033f7657ae1505264c11d2c2fdad75 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/contextual-menu/contextual-menu.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=7524bf8f46f496c49be56602b2baaab5 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/contextual-menu/contextual-menu.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=baac511161b31c496e0e6247a2264dc2 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/contextual-menu/contextual-menu.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=5eb1a550221b48cc99d2a9b39d49f715 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/contextual-menu/contextual-menu.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=e1a176c05eda0b2ebcba63d57631a57e 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/contextual-menu/contextual-menu.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=afe09bdac8c5f388deb1e0cc2ff423f0 2500w" />
</Frame>

## Enabling the contextual menu

Add the `contextual` field to your `docs.json` file and specify which options you want to include.

```json  theme={null}
{
 "contextual": {
   "options": [
     "copy",
     "view",
     "chatgpt",
     "claude",
     "perplexity",
     "grok",
     "mcp",
     "cursor",
     "vscode"
   ]
 }
}
```

## Adding custom options

Create custom options in the contextual menu by adding an object to the `options` array. Each custom option requires these properties:

<ResponseField name="title" type="string" required>
  The title of the option.
</ResponseField>

<ResponseField name="description" type="string" required>
  The description of the option. Displayed beneath the title when the contextual menu is expanded.
</ResponseField>

<ResponseField name="icon" type="string" required>
  The icon to display.

  Options:

  * [Font Awesome icon](https://fontawesome.com/icons) name, if you have the `icons.library` [property](/organize/settings#param-icons) set to `fontawesome` in your `docs.json`
  * [Lucide icon](https://lucide.dev/icons) name, if you have the `icons.library` [property](/organize/settings#param-icons) set to `lucide` in your `docs.json`
  * URL to an externally hosted icon
  * Path to an icon file in your project
</ResponseField>

<ResponseField name="iconType" type="string">
  The [Font Awesome](https://fontawesome.com/icons) icon style. Only used with Font Awesome icons.

  Options: `regular`, `solid`, `light`, `thin`, `sharp-solid`, `duotone`, `brands`.
</ResponseField>

<ResponseField name="href" type="string | object" required>
  The href of the option. Use a string for simple links or an object for dynamic links with query parameters.

  <Expandable title="href object">
    <ResponseField name="base" type="string" required>
      The base URL for the option.
    </ResponseField>

    <ResponseField name="query" type="object" required>
      The query parameters for the option.

      <Expandable title="query object">
        <ResponseField name="key" type="string" required>
          The query parameter key.
        </ResponseField>

        <ResponseField name="value" type="string" required>
          The query parameter value. We will replace the following placeholders with the corresponding values:

          * Use `$page` to insert the current page content in Markdown.
          * Use `$path` to insert the current page path.
          * Use `$mcp` to insert the hosted MCP server URL.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>

Example custom option:

```json {9-14} wrap theme={null}
{
    "contextual": {
        "options": [
            "copy",
            "view",
            "chatgpt",
            "claude",
            "perplexity",
            {
                "title": "Request a feature",
                "description": "Join the discussion on GitHub to request a new feature",
                "icon": "plus",
                "href": "https://github.com/orgs/mintlify/discussions/categories/feature-requests"
            }
        ]
    }
}
```

### Custom option examples

<AccordionGroup>
  <Accordion title="Simple link">
    ```json  theme={null}
    {
      "title": "Request a feature",
      "description": "Join the discussion on GitHub",
      "icon": "plus",
      "href": "https://github.com/orgs/mintlify/discussions/categories/feature-requests"
    }
    ```
  </Accordion>

  <Accordion title="Dynamic link with page content">
    ```json  theme={null}
    {
      "title": "Share on X",
      "description": "Share this page on X",
      "icon": "x",
      "href": {
        "base": "https://x.com/intent/tweet",
        "query": [
          {
          "key": "text",
          "value": "Check out this documentation: $page"
          }
        ]
      }
    }
    ```
  </Accordion>
</AccordionGroup>
