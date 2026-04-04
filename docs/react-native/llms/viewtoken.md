# Source: https://reactnative.dev/docs/viewtoken.md

# ViewToken Object Type

`ViewToken` object is returned as one of the properties in the `onViewableItemsChanged` callback (for example, in the [FlatList](/docs/flatlist.md) component). It is exported by [`ViewabilityHelper.js`](https://github.com/facebook/react-native/blob/main/packages/react-native/Libraries/Lists/ViewabilityHelper.js).

## Example[​](#example "Direct link to Example")

js

```
{
  item: {key: "key-12"},
  key: "key-12",
  index: 11,
  isViewable: true
}
```

## Keys and values[​](#keys-and-values "Direct link to Keys and values")

### `index`[​](#index "Direct link to index")

Unique numeric identifier assigned to the data element.

| Type   | Optional |
| ------ | -------- |
| number | Yes      |

### `isViewable`[​](#isviewable "Direct link to isviewable")

Specifies if at least some part of list element is visible in the viewport.

| Type    | Optional |
| ------- | -------- |
| boolean | No       |

### `item`[​](#item "Direct link to item")

Item data

| Type | Optional |
| ---- | -------- |
| any  | No       |

### `key`[​](#key "Direct link to key")

Key identifier assigned to the data element extracted to the top level.

| Type   | Optional |
| ------ | -------- |
| string | No       |

### `section`[​](#section "Direct link to section")

Item section data when used with `SectionList`.

| Type | Optional |
| ---- | -------- |
| any  | Yes      |

## Used by[​](#used-by "Direct link to Used by")

* [`FlatList`](/docs/flatlist.md)
* [`SectionList`](/docs/sectionlist.md)
* [`VirtualizedList`](/docs/virtualizedlist.md)
