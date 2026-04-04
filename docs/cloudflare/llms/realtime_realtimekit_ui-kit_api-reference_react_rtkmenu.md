# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmenu/index.md

---

title: RtkMenu · Cloudflare Realtime docs
description: API reference for RtkMenu component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmenu/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmenu/index.md
---

A menu component.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `offset` | `number` | ✅ | - | Offset in px |
| `placement` | `Placement` | ✅ | - | Placement of menu |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkMenu } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkMenu />;
}
```

### With Properties

```tsx
import { RtkMenu } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkMenu
      offset={42}
      placement={placement}
      size="md"
    />
  );
}
```
