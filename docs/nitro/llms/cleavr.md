# Source: https://nitro.build/raw/deploy/providers/cleavr.md

# Cleavr

> Deploy Nitro apps to Cleavr.

**Preset:** `cleavr`

<read-more title="cleavr.io" to="https://cleavr.io">

</read-more>

<note>

Integration with this provider is possible with [zero configuration](/deploy/#zero-config-providers).

</note>

## Set up your web app

In your project, set Nitro preset to `cleavr`.

```js
export default {
  nitro: {
    preset: 'cleavr'
  }
}
```

Push changes to your code repository.

**In your Cleavr panel:**

<steps level="4">

#### Provision a new server

#### Add a website, selecting **Nuxt 3** as the app type

#### In web app > settings > Code Repo, point to your project's code repository

</steps>

You're now all set to deploy your project!
