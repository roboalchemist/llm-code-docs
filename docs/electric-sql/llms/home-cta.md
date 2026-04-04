# Source: https://electric-sql.com/src/partials/home-cta.md

---
url: /src/partials/home-cta.md
---
## Get started now

You can start by adopting Electric incrementally,

one data fetch

at a time.


Using
our

HTTP API,


client libraries
and

framework hooks.


```tsx
import { useShape } from '@electric-sql/react'

const Component = () => {
  const { data } = useShape({
    url: `${BASE_URL}/v1/shape`,
    params: {
      table: `items`
    }
  })

  return (
    <pre>{ JSON.stringify(data) }<pre>
  )
}
```

And you can level-up

all the way
to syncing into a local embedded

[PGlite database](/products/pglite).

With

built-in [persistence](https://pglite.dev/docs/filesystems)
and

[live reactivity](https://pglite.dev/docs/live-queries).

<<< @/src/partials/sync-into-pglite.tsx
