# Source: https://redocly.com/docs/realm/customization/api-functions.md

# Source: https://redocly.com/docs/realm/config/api-functions.md

# `apiFunctions`

Use the `apiFunctions` option to set paths where Redocly detects and hosts API functions.

By default, API functions are hosted at the `@api` folder and the path is served at `/api`.

## Options

| Option | Type | Description |
|  --- | --- | --- |
| folders | [string] | List of paths where the API functions are stored.
Default value: `/@api` |


## Example


```yaml redocly.yaml
apiFunctions:
  folders:
    - /my/api/folder/path/
    - /my/second/api/folder/path/
```

When you add this configuration to your project, the API functions are located in the `/my/api/folder/path/` and `/my/second/api/folder/path/` folders as well as the `/@api` folder.
All the endpoints in these folders are available at `/my/api/folder/path/...` and `/my/second/api/folder/path/...`, respectively.

This configuration describes the following folder structure:


```treeview
/
âââ my/api/folder/path/
â   âââ hello.ts
â   âââ communities/
â       âââ [id].get.ts
âââ my/second/api/folder/path/
â   âââ world.ts
â   âââ books/
â       âââ [id].get.ts
```

The corresponding API endpoints are:

- `/my/api/folder/path/hello`
- `/my/api/folder/path/communities/[id]`
- `/my/second/api/folder/path/world`
- `/my/second/api/folder/path/books/[id]`


## Resources

- **[API functions reference](/docs/realm/customization/api-functions/api-functions-reference)** - Complete reference for available API functions and their implementation in your documentation projects