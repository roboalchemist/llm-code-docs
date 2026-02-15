# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-virtualized-participant-list/index.md

---

title: rtk-virtualized-participant-list · Cloudflare Realtime docs
description: API reference for rtk-virtualized-participant-list component (Web
  Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-virtualized-participant-list/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-virtualized-participant-list/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `bufferedItemsCount` | `number` | ✅ | - | Buffer items to render before and after the visible area |
| `emptyListElement` | `HTMLElement` | ✅ | - | Element to render if list is empty |
| `itemHeight` | `number` | ✅ | - | Height of each item in pixels (assumed fixed) |
| `items` | `Peer1[]` | ✅ | - | Items to be virtualized |
| `renderItem` | `(item: Peer1, index: number)` | ✅ | - | Function to render each item |

## Usage Examples

### Basic Usage

```html
<rtk-virtualized-participant-list></rtk-virtualized-participant-list>
```

### With Properties

```html
<rtk-virtualized-participant-list>
</rtk-virtualized-participant-list>
```

```html
<script>
  const el = document.querySelector("rtk-virtualized-participant-list");


  el.bufferedItemsCount= 42;
  el.itemHeight= 42;
</script>
```
