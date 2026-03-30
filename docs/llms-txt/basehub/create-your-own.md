# Create Your Own

> Learn how to create your own template in this short guide.

## Requirements

In order to create your own template, you’ll need to:

*   **Make your BaseHub repository “public”.**  
    Go to the repository settings (bottom left), and make it public.
    
*   **Make your GitHub repository “public”.**  
    We assume you already know how to do that in GitHub.
    
*   Optionally, **edit your BaseHub repo’s “public info”**, also found in the repo settings (bottom left).
    

## Enabling playgrounds (example with v0)

Every public repo can be a playground. A playground is an environment in which non-authenticated visitors can play around with the contents of a repo, without altering the origin repo. Playgrounds expire in 5 days after being first initialized. Visitors will have a chance to claim them before that happens.

Environments like v0 are the perfect use case for this. Take our [Blog Template](https://v0.dev/community/blog-Oi5INHKYsqg), for instance.

![](https://assets.basehub.com/7b31fb4b/9305c8e945785253bb75ce49d6789e29/cleanshot-2025-06-30-at-16.49.202x.png?width=3840&quality=90&format=auto)

Right after forking, visitors can see (draft) content without authenticating

![](https://assets.basehub.com/7b31fb4b/eb68be4fe4b8f5aa6bf23ce773917815/cleanshot-2025-06-30-at-16.41.182x.png?width=3840&quality=90&format=auto)

In a popover, we link to the playground, so visitors can edit content right away, and see it refresh back in v0

To set this up, we do the following. In `basehub.config.ts` (this file could be named differently, it doesn’t matter), we call `setGlobalConfig` with `fallbackPlayground`.

```
import { setGlobalConfig } from "basehub"

const _vercel_url_env = "VERCEL_URL"
let v0Id = process.env[_vercel_url_env]
if (v0Id && v0Id.includes("vusercontent")) {
  v0Id = v0Id.split(".")[0]
}

const playgroundId = `${
  v0Id ? encodeURIComponent(v0Id) : "__dev"
}__rel_v0`

setGlobalConfig({
  fallbackPlayground: playgroundId
    ? { target: "basehub/nextjs-blog", id: playgroundId }
    : undefined,
})
```

The “fallbackPlayground” part is the critical part here (everything else is part of the v0 example itself): it tells our API, “if you don’t find a token in the request headers (cause the request is unauthenticated), fallback to a playground with this id”.

Then, you can render the “Open in playground” link to visitors by querying the playground info:

```
const playgroundData = await basehub().query({
  _sys: {
    playgroundInfo: {
      expiresAt: true,
      editUrl: true,
      claimUrl: true,
    },
  },
})

if (playgroundData._sys.playgroundInfo) {
  playgroundNotification = (
    <a href={playgroundInfo.editUrl} target="_blank">
      Open Playground
    </a>
  )
}
```

And, that’s really it.

## Bonus: “Rel” attribute

If you’re planning to put this in v0, you’ll want to suffix your playground IDs with `__rel_v0`, as we’ll pick that “rel” up and after visitors claim the repository, we’ll show a nice “Coming from v0?” callout to streamline onboarding.

![](https://assets.basehub.com/7b31fb4b/44d9cd5e1e8c95eecc490143c171fb7d/image.png?width=3840&quality=90&format=auto)