# Source: https://redocly.com/docs/realm/content/markdoc-tags/connect-mcp.md

# Connect MCP tag

The `connect-mcp` tag renders a button that allows users to connect to the MCP (Model Context Protocol) server through various MCP clients.
When clicked or hovered, it displays a dropdown menu with options to connect via Cursor, VS Code, or copy the MCP configuration.

The Connect MCP button requires a properly configured Docs MCP server to function.
See the [MCP configuration documentation](/docs/realm/config/mcp) for setup instructions.

## Syntax and usage

Add the `connect-mcp` tag where you want the button to appear.


```markdoc
{% connect-mcp /%}
```

The button opens a dropdown menu on hover with connection options.
Users can click to connect their editor or copy the configuration.

## Attributes

| Attribute | Type | Description |
|  --- | --- | --- |
| placement | string | Sets the vertical placement of the dropdown menu relative to the button.
Accepts `top` or `bottom`.
**Default:** `bottom`. |
| alignment | string | Sets the horizontal alignment of the dropdown menu relative to the button.
Accepts `start` or `end`.
**Default:** `start`. |
| options | array | Specifies which connection options to display in the dropdown.
Accepts an array containing any combination of: `cursor`, `vscode`, `copy`.
**Default:** `["cursor", "vscode", "copy"]`. |


## Examples

### Basic usage

Display the **Connect MCP** button with all default options:


```markdoc
{% connect-mcp /%}
```

### Dropdown placement

Display the dropdown above the button:


```markdoc
{% connect-mcp placement="top" /%}
```

### Dropdown alignment

Align the dropdown to the end (right side) of the button:


```markdoc
{% connect-mcp alignment="end" /%}
```

### Display specific options

Display only the Cursor connection option:


```markdoc
{% connect-mcp options=["cursor"] /%}
```

Display only the Copy option configuration:


```markdoc
{% connect-mcp options=["copy"] /%}
```

### Combined attributes

Customize multiple attributes:


```markdoc
{% connect-mcp placement="top" alignment="end" options=["vscode", "copy"] /%}
```

## Best practices

**Use placement strategically**

Use `placement="top"` when the button appears near the bottom of the page to prevent the dropdown from extending beyond the viewport.

**Choose appropriate alignment**

Use `alignment="start"` for inline usage in content to align the dropdown with the left side of the button.
Use `alignment="end"` for navbar or right-aligned layouts to align the dropdown with the right side of the button.

**Display relevant options**

Customize the `options` array to display only the connection methods relevant to your audience.
If your users primarily use Cursor, consider showing only that option to reduce cognitive load.

## Related resources

- **[MCP configuration](/docs/realm/config/mcp)** - Configure the MCP server and Connect MCP button visibility
- **[MCP servers overview](/docs/realm/customization/mcp-server)** - Learn about MCP servers and integration with AI tools