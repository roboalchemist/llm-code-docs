# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkspotlightindicator/index.md

---

title: RtkSpotlightIndicator · Cloudflare Realtime docs
description: API reference for RtkSpotlightIndicator component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkspotlightindicator/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkspotlightindicator/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkSpotlightIndicator } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkSpotlightIndicator />;
}
```

### With Properties

```tsx
import { RtkSpotlightIndicator } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkSpotlightIndicator
      meeting={meeting}
      size="md"
    />
  );
}
```
