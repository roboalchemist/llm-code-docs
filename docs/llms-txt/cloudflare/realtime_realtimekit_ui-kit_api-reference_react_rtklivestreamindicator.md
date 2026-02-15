# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklivestreamindicator/index.md

---

title: RtkLivestreamIndicator · Cloudflare Realtime docs
description: API reference for RtkLivestreamIndicator component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklivestreamindicator/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklivestreamindicator/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkLivestreamIndicator } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkLivestreamIndicator />;
}
```

### With Properties

```tsx
import { RtkLivestreamIndicator } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkLivestreamIndicator
      meeting={meeting}
      size="md"
    />
  );
}
```
