# Source: https://docs.skypack.dev/skypack-cdn/api-reference/package-metadata.md

# Package Metadata

## Package Meta

<mark style="color:blue;">`GET`</mark> `https://cdn.skypack.dev/:packageSpecifier?meta`

View metadata about any package. Replace `:packageSpecifier` with any package name and optionally a version, like so: `https://cdn.skypack.dev/preact?meta` or `https://cdn.skypack.dev/preact@10.5.7?meta`.

#### Path Parameters

| Name             | Type   | Description                                                     |
| ---------------- | ------ | --------------------------------------------------------------- |
| packageSpecifier | string | Specify `[package]@[version]`or simply `[package]` for “latest“ |

#### Query Parameters

| Name | Type    | Description                                                                            |
| ---- | ------- | -------------------------------------------------------------------------------------- |
| meta | boolean | This is required in order to display metadata (without, you’ll trigger the Lookup URL) |

{% tabs %}
{% tab title="200 Cake successfully retrieved." %}

```javascript
{
  "name": "preact",
  "version": "10.5.7",
  "buildId": "apbTSlqiCbFCw96Kpm6e",
  "buildStatus": "SUCCESS",
  "packageExports": {  
    ".": {
      "id": "./dist/preact.module.js",
      "optimized": true,
      "hasDefaultExport": false,
      "namedExports": [
        "__u",
        "cloneElement",
        "Component",
        "createContext",
        "createElement",
        "createRef",
        "Fragment",
        "h",
        "hydrate",
        "isValidElement",
        "options",
        "render",
        "toChildArray"
      ],
      "type": "JS"
    },
    "./compat": {
      "id": "./compat/dist/compat.module.js",
      "namedExports": [
        "__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED",
        "Children",
        "cloneElement",
        "Component",
        "createContext",
        "createElement",
        "createFactory",
        "createPortal",
        "createRef",
        "findDOMNode",
        "forwardRef",
        "Fragment",
        "hydrate",
        "isValidElement",
        "lazy",
        "memo",
        "PureComponent",
        "render",
        "StrictMode",
        "Suspense",
        "SuspenseList",
        "unmountComponentAtNode",
        "unstable_batchedUpdates",
        "useCallback",
        "useContext",
        "useDebugValue",
        "useEffect",
        "useErrorBoundary",
        "useImperativeHandle",
        "useLayoutEffect",
        "useMemo",
        "useReducer",
        "useRef",
        "useState",
        "version"
      ],
      "hasDefaultExport": true,
      "type": "JS",
      "optimized": true
    },
    "./debug": {
      "namedExports": [
        "resetPropWarnings"
      ],
      "type": "JS",
      "hasDefaultExport": false,
      "id": "./debug/dist/debug.module.js",
      "optimized": true
    },
    "./devtools": {
      "hasDefaultExport": false,
      "type": "JS",
      "id": "./devtools/dist/devtools.module.js",
      "namedExports": [],
      "optimized": true
    },
    "./hooks": {
      "id": "./hooks/dist/hooks.module.js",
      "optimized": true,
      "hasDefaultExport": false,
      "type": "JS",
      "namedExports": [
        "useCallback",
        "useContext",
        "useDebugValue",
        "useEffect",
        "useErrorBoundary",
        "useImperativeHandle",
        "useLayoutEffect",
        "useMemo",
        "useReducer",
        "useRef",
        "useState"
      ]
    },
    "./jsx-dev-runtime": {
      "optimized": true,
      "namedExports": [
        "Fragment",
        "jsx",
        "jsxDEV",
        "jsxs"
      ],
      "type": "JS",
      "id": "./jsx-runtime/dist/jsxRuntime.module.js",
      "hasDefaultExport": false
    },
    "./jsx-runtime": {
      "hasDefaultExport": false,
      "optimized": true,
      "id": "./jsx-runtime/dist/jsxRuntime.module.js",
      "namedExports": [
        "Fragment",
        "jsx",
        "jsxDEV",
        "jsxs"
      ],
      "type": "JS"
    },
    "./package.json": {
      "type": "ASSET",
      "id": "./package.json"
    },
    "./test-utils": {
      "hasDefaultExport": false,
      "type": "JS",
      "namedExports": [
        "act",
        "setupRerender",
        "teardown"
      ],
      "id": "./test-utils/dist/testUtils.module.js",
      "optimized": true
    }
  }
}
```

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Even though this API shares a base URL with the [Lookup API](https://docs.skypack.dev/skypack-cdn/api-reference/lookup-urls), not all functions of the Lookup API are supported (e.g. you can‘t specify `?meta&min`). For this reason, it‘s considered its own API.
{% endhint %}
