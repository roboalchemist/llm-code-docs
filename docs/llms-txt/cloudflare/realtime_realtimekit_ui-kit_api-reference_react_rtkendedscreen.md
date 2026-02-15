# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkendedscreen/index.md

---

title: RtkEndedScreen · Cloudflare Realtime docs
description: API reference for RtkEndedScreen component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkendedscreen/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkendedscreen/index.md
---

A screen which shows a meeting has ended.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Global states |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | Global states |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkEndedScreen } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkEndedScreen />;
}
```

### With Properties

```tsx
import { RtkEndedScreen } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkEndedScreen
      meeting={meeting}
      size="md"
    />
  );
}
```
