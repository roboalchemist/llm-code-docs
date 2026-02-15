# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkwaitingscreen/index.md

---

title: RtkWaitingScreen · Cloudflare Realtime docs
description: API reference for RtkWaitingScreen component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkwaitingscreen/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkwaitingscreen/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkWaitingScreen } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkWaitingScreen />;
}
```

### With Properties

```tsx
import { RtkWaitingScreen } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkWaitingScreen
      meeting={meeting}
    />
  );
}
```
