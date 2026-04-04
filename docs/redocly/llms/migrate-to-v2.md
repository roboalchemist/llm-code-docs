# Source: https://redocly.com/docs/cli/guides/migrate-to-v2.md

# Migrate to Redocly CLI v2.x from v1.x

Redocly CLI v2 introduces improved architecture and removes deprecated features to make the tool easier to maintain and extend.
This guide covers the essential changes you need to make when upgrading from v1.x.

## Prerequisites

**Node.js version**: Update to Node.js 20.19.0+, 22.12.0+, or later.

## Breaking changes

### Module system migration

The codebase has been rewritten from CommonJS to ES Modules.
This affects [plugins](/docs/cli/configuration/reference/plugins): update your plugin syntax to use ES Modules, or use the `.cjs` extension for CommonJS files.

### Configuration changes

The only default configuration file name is now `redocly.yaml`.
If you still use the legacy `.redocly.yaml`, please rename it.
You can still use a different file name, but you must explicitly specify it with the `--config` flag.

Several deprecated configuration options have been removed:


```yaml
# â Removed - use 'apis' instead
apiDefinitions:
  - openapi.yaml

# â Use this instead
apis:
  main: openapi.yaml
```


```yaml
# â Removed - use 'openapi' directly
features.openapi:
  theme:
    colors:
      primary:
        main: '#ff0000'

# â Removed - use 'openapi' directly
theme:
  openapi:
    theme:
      colors:
        primary:
          main: '#ff0000'

# â Use this instead
openapi:
  theme:
    colors:
      primary:
        main: '#ff0000'
```


```yaml
# â Removed - use 'rule/' prefix
rules:
  assert/name: error

# â Use this instead
rules:
  rule/name: error
```

### Rule changes

The `spec` rule has been replaced with `struct`:


```yaml
# â Removed
rules:
  spec: error

# â Use this instead
rules:
  struct: error
```

Or use the new `spec` ruleset for specification compliance:


```yaml
extends:
  - spec
```

Removed rule `path-excludes-patterns`.
Use a configurable rule instead.
You may refer to [this Cookbook recipe](https://github.com/Redocly/redocly-cli-cookbook/tree/main/configurable-rules/path-excludes-pattern).

Removed rule `info-license-url`.
Use `info-license-strict` which better complies with the new [OpenAPI 3.1 specification](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0.md#license-object).

### Configurable rules changes

The `undefined` assertion has been removed:


```yaml
# â Removed
rules:
  rule/check-property:
    subject:
      type: Operation
      property: summary
    assertions:
      undefined: false

# â Use this instead
rules:
  rule/check-property:
    subject:
      type: Operation
      property: summary
    assertions:
      defined: true
```

### Changes in the `join` command server handling (since v2.0.5)

The `join` command no longer merges `servers` into the root level.
Each path item now retains the `servers` from its source description, so that joined descriptions remain unmodified.
This fixes incorrect behavior but may break workflows that relied on root-level server inheritance.

To restore root-level `servers`, use a custom [decorator](/docs/cli/custom-plugins/custom-decorators) like the following:


```js
export default function plugin() {
  return {
    id: 'my-plugin',
    decorators: {
      oas3: {
        'add-servers': () => ({
          Root: {
            leave: (root) => {
              root.servers = [{ url: 'https://your-server-url.com' }];
            },
          },
        }),
      },
    },
  };
}
```

Register the plugin in `redocly.yaml` and run `join` followed by `bundle` to apply it:


```bash
redocly join foo.yaml bar.yaml -o tmp.yaml
redocly bundle tmp.yaml -o joined.yaml
```

### Platform changes

- **Legacy Registry**: Support for the legacy Redocly API Registry has been removed in favor of [Reunite](https://app.cloud.redocly.com/).
- **Commands**: The `preview-docs` command has been removed - use `preview` instead.
- **Labels**: The `labels` field in the `apis` section has been removed.


## New features

### Spec ruleset

A new `spec` ruleset is available that enforces OpenAPI specification compliance:


```yaml
extends:
  - spec
```

### Duplicate tag detection

The `no-duplicated-tag-names` rule checks for duplicate tag names in your API description.

### JSON schema format validation

Now Redocly CLI supports JSON schema formats:


```yaml
openapi: 3.1.0
paths:
  /users/{id}:
    get:
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  email:
                    type: string
                    format: email
              examples:
                Correct:
                  value:
                    email: correct@email.com
                Incorrect:
                  value:
                    email: wrong-email # Will fail validation
```

## Migration checklist

1. **Update Node.js** to a supported version (20.19.0+, 22.12.0+, or 23+).
2. **Rename configuration file name** to `redocly.yaml` (if it differs).
3. **Replace `spec` rule** with `struct`.
4. **Update configurable rules** to use `rule/` prefix instead of `assert/`.
5. **Replace `undefined` assertions** with `defined: true`.
6. **Revise `join` command usage** if your workflow relies on root-level `servers` in joined output.
7. **Update configuration structure**:
  - Replace `apiDefinitions` with `apis`
  - Move `features.openapi.*` to `openapi.*`
  - Remove `labels` from `apis` section
8. **Update plugins** to ES Modules syntax or use `.cjs` extension.
9. **Test your configuration** with `redocly check-config`.


## Next steps

- Explore the [changelog](https://redocly.com/docs/cli/changelog) for detailed information about all changes.
- Check out the v2 [documentation](https://redocly.com/docs/cli/).