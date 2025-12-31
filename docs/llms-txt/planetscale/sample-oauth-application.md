# Source: https://planetscale.com/docs/api/reference/sample-oauth-application.md

# Sample OAuth application

> This sample OAuth application shows how to implement OAuth authentication with PlanetScale in a Next.js application.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/4b81ea4-green_lilman2x.png?fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=5cc2ad95133d1f57cde0278a66eb4a09" alt="PlanetPets mascot illustration" data-og-width="294" width="294" data-og-height="367" height="367" data-path="docs/images/reference/4b81ea4-green_lilman2x.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/4b81ea4-green_lilman2x.png?w=280&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=b6dcc17a519477db639724caadb6d927 280w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/4b81ea4-green_lilman2x.png?w=560&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=f94845fd94cf26810b35abc7df775f34 560w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/4b81ea4-green_lilman2x.png?w=840&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=bf97d218132f4e641b809a74772401f0 840w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/4b81ea4-green_lilman2x.png?w=1100&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=5392acbf9e1fb9165cfb268d9376a1ca 1100w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/4b81ea4-green_lilman2x.png?w=1650&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=911725a3c0b3bbcd2a3ec462bbf821e2 1650w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/4b81ea4-green_lilman2x.png?w=2500&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=829fd966d2b2cc41071e870dc337c50c 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/04dbe99-title2x.png?fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=2f95c74d56df7ebac31d38d280c45192" alt="PlanetPets logo" data-og-width="552" width="552" data-og-height="119" height="119" data-path="docs/images/reference/04dbe99-title2x.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/04dbe99-title2x.png?w=280&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=dd252fe491045b1094ef31e3439417d5 280w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/04dbe99-title2x.png?w=560&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=305175667db0d13b5b717599aeb1293a 560w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/04dbe99-title2x.png?w=840&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=eed8e6fe11e5349a0c892a74b463b3c8 840w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/04dbe99-title2x.png?w=1100&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=adfcc26d9bf47dc07c6a6f0fb83589ba 1100w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/04dbe99-title2x.png?w=1650&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=d5b390f9e5a6ec839cf919ba0fe4e523 1650w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/04dbe99-title2x.png?w=2500&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=0038b06959ee879b573533f013c8dd0c 2500w" />
</Frame>

PlanetPets is a simple app that users sign in to using their GitHub account. Afterward, users are prompted to give PlanetPets access to their PlanetScale account. The user's organizations are then presented as "gardens" where their databases are "trees." Within PlanetPets, users can water their "trees" to grow new branches, creating a new branch in their database with a randomly generated name.

If you want to test out the app, go to [planetpets.planetscale.vercel.app](https://planetpets.planetscale.vercel.app/).

If you want to read the code or set it up yourself, see the [PlanetPets GitHub repo](https://github.com/planetscale/planetpets).

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt