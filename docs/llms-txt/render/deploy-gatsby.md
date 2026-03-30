# Source: https://render.com/docs/deploy-gatsby.md

# Deploy a Gatsby Static Site

You can deploy a [Gatsby](https://www.gatsbyjs.org/) static site on Render in under a minute. Your site is served over a *lightning-fast global CDN*, comes with *fully managed TLS* certificates, and supports *custom domains* out of the box. Best of all, it's free!

The sample app in this guide is based on Gatsby's official [default starter](https://github.com/gatsbyjs/gatsby-starter-default).

1. Use your existing Gatsby repository, or fork our sample Gatsby repo on [GitHub](https://github.com/render-examples/gatsby-starter-default) or [GitLab](https://gitlab.com/render-examples/gatsby).
2. Create a new *Static Site* on Render, and give Render permission to access your new repo.
3. Use the following values during creation:

   |                       |                |
   | --------------------- | -------------- |
   | *Build Command*     | `gatsby build` |
   | *Publish Directory* | `public`       |

That's it! Your app will be live on your Render URL as soon as the build finishes.

See [Specifying a Node Version](node-version) if you need to customize the version of Node.js used for your site.

#### Caching Gatsby builds (optional)

Gatsby requires the `.cache` and `public` directories to persist in order to take advantage of [Incremental Builds](https://www.gatsbyjs.com/docs/reference/release-notes/v3.0/#incremental-builds-in-oss). Render starts each build in a fresh environment, and only cache the `.cache` directory. There is no `public` directory present in the new build.

> The reason we don’t persist the `public` directory is to ensure if you remove a file, it doesn’t get copied to the new build. Gatsby does not remove items from `public` during the build process. If you remove a file you'll need to do a manual deploy in the Render Dashboard with the `Clear build cache & deploy` option to remove the entire build cache.

Using the following build script will allow your `public` directory to be cached as well.

```bash
#!/usr/bin/env bash

build_with_cache() {
  if [[ -d "$XDG_CACHE_HOME"/public ]]; then
    echo "Copying cached public dir"
    rsync -a "$XDG_CACHE_HOME"/public/ public
  else
    echo "No cached public dir found"
  fi

  echo "Building"

  gatsby build

  echo "Done, caching public dir"
  rsync -a public/ "$XDG_CACHE_HOME"/public
}

if [[ "$RENDER" ]]; then
  build_with_cache
else
  gatsby build
fi
```

Save this to file in your repository: `build.sh`

Then change the permissions to allow the file to be executable: `chmod u+x ./build.sh`

Replace the build command in your `package.json` with the following: `./build.sh`