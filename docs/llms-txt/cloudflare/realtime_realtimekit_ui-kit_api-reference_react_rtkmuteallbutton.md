# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmuteallbutton/index.md

---

title: RtkMuteAllButton · Cloudflare Realtime docs
description: API reference for RtkMuteAllButton component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmuteallbutton/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmuteallbutton/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkMuteAllButton } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkMuteAllButton />;
}
```

### With Properties

```tsx
import { RtkMuteAllButton } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkMuteAllButton
      meeting={meeting}
      size="md"
      variant="button"
    />
  );
}
```
