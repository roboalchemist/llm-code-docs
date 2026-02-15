# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-paginated-list/index.md

---

title: rtk-paginated-list · Cloudflare Realtime docs
description: API reference for rtk-paginated-list component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-paginated-list/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-paginated-list/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `autoScroll` | `boolean` | ✅ | - | auto scroll list to bottom |
| `createNodes` | `(data: unknown[])` | ✅ | - | Create nodes |
| `emptyListLabel` | `string` | ✅ | - | label to show when empty |
| `fetchData` | `(timestamp: number, size: number, reversed: boolean)` | ✅ | - | Fetch the data |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `pageSize` | `number` | ✅ | - | Page Size |
| `pagesAllowed` | `number` | ✅ | - | Number of pages allowed to be shown |
| `rerenderList` | `()` | ✅ | - | Rerender paginated list |
| `reset` | `(timestamp?: number)` | ❌ | - | Resets the paginated list to a given timestamp |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-paginated-list></rtk-paginated-list>
```

### With Properties

```html
<!-- component.html -->
<rtk-paginated-list
 [autoScroll]="true"
 [createNodes]="[]"
 emptyListLabel="example">
</rtk-paginated-list>
```
