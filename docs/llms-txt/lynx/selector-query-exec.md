# Source: https://lynxjs.org/api/lynx-api/selector-query/selector-query-exec.md

# SelectorQuery: exec() method

<APISummary />

Execute all submitted operations. Note that no node search and UI operations will actually be executed until `exec()` is called.

## Syntax

```ts
exec(): void;
```

### Parameters

None.

### Return Value

None (`undefined`).

## Example

Get the position and size of the specified `text` node:

```tsx
lynx
  .createSelectorQuery()
  .select('#my-id')
  .invoke({
    method: 'boundingClientRect',
    success: function (res) {
      console.log(res);
    },
    fail: function (res) {
      console.log(res.code, res.data);
    },
  })
  .exec();
```

## Compatibility

**Compatibility Table**
**Query:** `lynx-api.selector-query.exec`

**Platform Support**

| Platform | Version Added | Notes |
|----------|---------------|-------|
| Android | 2.2 | - |
| iOS | 2.2 | - |
| HarmonyOS | 3.4 | - |
| Web | ✅ Yes | - |

**Description:** Execute all submitted operations.

