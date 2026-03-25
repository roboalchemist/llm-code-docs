# Source: https://docs.knock.app/mapi-reference/guides/schemas/guide_activation_url_pattern.md

### GuideActivationUrlPattern

A rule that controls when a guide should be shown based on the user's location in the application. At least one of `pathname` or `search` must be provided.

#### Attributes

- **directive** (string) *required* - Whether to allow or block the guide at the specified location.
- **pathname** (string) - The URL pathname pattern to match against. Must be a valid URI path.
- **search** (string) - The URL query string pattern to match against (without the leading '?'). Supports URLPattern API syntax.

#### Example

```json
{
  "directive": "allow",
  "pathname": "/dashboard/*",
  "search": "tab=settings"
}
```

