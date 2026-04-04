# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkgridpagination/index.md

---

title: RtkGridPagination · Cloudflare Realtime docs
description: API reference for RtkGridPagination component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkgridpagination/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkgridpagination/index.md
---

A component which allows you to change current page and view mode of active participants list. This is reflected in the `rtk-grid` component.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon Pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size Prop |
| `states` | `States` | ✅ | - | States |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `GridPaginationVariants` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkGridPagination } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkGridPagination />;
}
```

### With Properties

```tsx
import { RtkGridPagination } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkGridPagination
      meeting={meeting}
      size="md"
      variant={gridpaginationvariants}
    />
  );
}
```
