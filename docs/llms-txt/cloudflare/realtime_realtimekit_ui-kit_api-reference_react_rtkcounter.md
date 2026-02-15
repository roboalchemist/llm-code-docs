# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcounter/index.md

---

title: RtkCounter · Cloudflare Realtime docs
description: API reference for RtkCounter component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcounter/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcounter/index.md
---

A number picker with increment and decrement buttons.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `minValue` | `number` | ✅ | - | Minimum value |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `value` | `number` | ✅ | - | Initial value |

## Usage Examples

### Basic Usage

```tsx
import { RtkCounter } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkCounter />;
}
```

### With Properties

```tsx
import { RtkCounter } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkCounter
      minValue={42}
      size="md"
      value={42}
    />
  );
}
```
