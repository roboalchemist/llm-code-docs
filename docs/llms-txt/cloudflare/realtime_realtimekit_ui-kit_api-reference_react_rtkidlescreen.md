# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkidlescreen/index.md

---

title: RtkIdleScreen · Cloudflare Realtime docs
description: API reference for RtkIdleScreen component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkidlescreen/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkidlescreen/index.md
---

A screen that handles the idle state, i.e; when you are waiting for data about the meeting, specifically the `meeting` object.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkIdleScreen } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkIdleScreen />;
}
```

### With Properties

```tsx
import { RtkIdleScreen } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkIdleScreen
      meeting={meeting}
    />
  );
}
```
