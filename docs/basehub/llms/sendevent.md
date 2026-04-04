# sendEvent

> The events method to send data through BaseHub. Flexible, type-safe and scoped by block.

```
import { sendEvent } from 'basehub/events'
```

## Parameters

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Key

Type

Description

`ingestKey`

`EventBlock['ingestKey']`

**Required.** The event unique key for ingest actions. It defines which schema is used in the second parameter (or none at all if the schema is empty)

`data`

`Record<string, unknown>`

Dynamically typed based on the `ingestKey` provided.  
Accepts every field in the schema defined on your Event Block.

## Example

![](https://assets.basehub.com/7b31fb4b/9f8668081556d4ac5971bd493e6be165/screenshot-2024-12-19-at-2.03.45-pm.png?width=3840&quality=90&format=auto)

We create an Event block called "Feedback Events" with a checkbox field

```
'use client'
// you'll need to run basehub before importing this type 👇🏼
import type { FeedbackEvents['ingestKey'] } from '~/.basehub/schema' 
import { sendEvent } from 'basehub/events'
import { Card, IconButton } from '@radix-ui/themes'
import { ThumbsDown, ThumbsUp } from 'lucide-react'
import * as React from 'react'

export const Feedback = ({
  ingestKey,
}: {
  ingestKey: FeedbackEvents['ingestKey']
}) => {
  const [sentFeedback, setSentFeedback] = React.useState<
    'positive' | 'negative' | null
  >(null)

  const handleFeedback = (type: 'positive' | 'negative') => {
    if (sentFeedback === type) return
    sendEvent(ingestKey, { positive: type === 'positive' }) 

    setSentFeedback(type)
  }

  return (
    <Card variant="classic" size="3">
      <IconButton onClick={() => handleFeedback('negative')}>
        <ThumbsDown fill={sentFeedback === 'negative' ? 'var(--accent-12)' : 'none'} />
      </IconButton>
      <IconButton onClick={() => handleFeedback('positive')}>
        <ThumbsUp fill={sentFeedback === 'positive' ? 'var(--accent-12)' : 'none'} />
      </IconButton>
    </Card>
  )
}
```

![](https://assets.basehub.com/7b31fb4b/ee950463ede06ed84ba1ae9b03d19017/screenshot-2024-12-19-at-2.04.26-pm.png?width=3840&quality=90&format=auto)

Events received will look like this