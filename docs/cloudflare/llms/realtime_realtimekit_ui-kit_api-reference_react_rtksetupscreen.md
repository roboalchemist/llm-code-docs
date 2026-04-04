# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksetupscreen/index.md

---

title: RtkSetupScreen · Cloudflare Realtime docs
description: API reference for RtkSetupScreen component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksetupscreen/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksetupscreen/index.md
---

A screen shown before joining the meeting, where you can edit your display name, and media settings.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkSetupScreen } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkSetupScreen />;
}
```

### With Properties

```tsx
import { RtkSetupScreen } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkSetupScreen
      meeting={meeting}
      size="md"
    />
  );
}
```
