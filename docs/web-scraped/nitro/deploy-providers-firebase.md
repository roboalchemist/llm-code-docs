# Source: https://nitro.build/deploy/providers/firebase

-   [](/guide "Getting Started")

    ::: 
    []
    :::

    [Getting Started]
-   [](/deploy "Overview")

    ::: 
    []
    :::

    [Overview]
-   [](/config "Config")

    ::: 
    []
    :::

    [Config]

-   [[][Overview]](/deploy)
-   [[][Edge Workers]](/deploy/workers)
-   [Runtimes]

    ::: 
    -   [[][Node.js]](/deploy/runtimes/node)
    -   [[][WinterJS]](/deploy/runtimes/_winterjs)
    -   [[][Bun]](/deploy/runtimes/bun)
    -   [[][Deno]](/deploy/runtimes/deno)
    :::
-   [[][Custom Preset]](/deploy/custom-presets)
-   [Providers]

    ::: 
    -   [[Alwaysdata]](/deploy/providers/alwaysdata)
    -   [[AWS Lambda]](/deploy/providers/aws)
    -   [[AWS Amplify]](/deploy/providers/aws-amplify)
    -   [[Azure]](/deploy/providers/azure)
    -   [[Cleavr]](/deploy/providers/cleavr)
    -   [[Cloudflare]](/deploy/providers/cloudflare)
    -   [[Deno Deploy]](/deploy/providers/deno-deploy)
    -   [[DigitalOcean]](/deploy/providers/digitalocean)
    -   [[Edgio]](/deploy/providers/edgio)
    -   [[Firebase]](/deploy/providers/firebase)
    -   [[Flightcontrol]](/deploy/providers/flightcontrol)
    -   [[Genezio]](/deploy/providers/genezio)
    -   [[GitHub Pages]](/deploy/providers/github-pages)
    -   [[GitLab Pages]](/deploy/providers/gitlab-pages)
    -   [[Heroku]](/deploy/providers/heroku)
    -   [[IIS]](/deploy/providers/iis)
    -   [[Koyeb]](/deploy/providers/koyeb)
    -   [[Netlify]](/deploy/providers/netlify)
    -   [[Platform.sh]](/deploy/providers/platform-sh)
    -   [[Render.com]](/deploy/providers/render)
    -   [[StormKit]](/deploy/providers/stormkit)
    -   [[Vercel]](/deploy/providers/vercel)
    -   [[Zeabur]](/deploy/providers/zeabur)
    -   [[Zerops]](/deploy/providers/zerops)
    :::

1.  [[Providers]]

<div>

# Firebase 

Deploy Nitro apps to Firebase.

</div>

<div>

[]You will need to be on the [**Blaze plan**](https://firebase.google.com/pricing) (Pay as you go) to get started.

## [[[]]Firebase app hosting](#firebase-app-hosting) 

Preset: `firebase_app_hosting`

[[]](https://firebase.google.com/docs/app-hosting)[][] Read more in [Firebase App Hosting].

[]You can integrate with this provider using [zero configuration](/deploy/#zero-config-providers).

### [[[]]Project setup](#project-setup) 

#### Go to the Firebase [console](https://console.firebase.google.com/) and set up a new project. 

#### Select **Build \> App Hosting** from the sidebar. 

-   You may need to upgrade your billing plan at this step.

#### Click **Get Started**. 

-   Choose a region.
-   Import a GitHub repository (you'll need to link your GitHub account).
-   Configure deployment settings (project root directory and branch), and enable automatic rollouts.
-   Choose a unique ID for your backend.

#### Click Finish & Deploy to create your first rollout. 

When you deploy with Firebase App Hosting, the App Hosting preset will be run automatically at build time.

## [[[]]Firebase hosting (deprecated)](#firebase-hosting-deprecated) 

[]This deployment method is deprecated and is not recommended. Firebase App Hosting is the recommended way to deploy Nitro apps on Firebase.

**Preset:** `firebase`

[[]](https://firebase.google.com/docs/hosting)[][] Read more in [Firebase Hosting].

[]This preset will deploy to firebase functions 1st gen by default. If you want to deploy to firebase functions 2nd gen, see the [instructions below](#using-2nd-generation-firebase-functions).

### [[[]]Project Setup](#project-setup-1) 

#### [Using firebase CLI (recommended)](#using-firebase-cli-recommended) 

You may instead prefer to set up your project with the Firebase CLI, which will fetch your project ID for you, add required dependencies (see above) and even set up automated deployments via GitHub Actions (for hosting only). [Learn about installing the firebase CLI](https://firebase.google.com/docs/cli#windows-npm).

1.  Install firebase CLI globally

Always try to use the latest version of the Firebase CLI.

[]

``` 
npm install -g firebase-tools@latest
```

**Note**: You need to be on [\^11.18.0](https://github.com/firebase/firebase-tools/releases/tag/v11.18.0) to deploy a `nodejs18` function.

2.  Initialize your firebase project

[]

``` 
firebase login
firebase init hosting
```

When prompted, you can enter `.output/public` as the public directory. In the next step, **do not** configure your project as a single-page app.

Once complete, add the following to your `firebase.json` to enable server rendering in Cloud Functions:

[][firebase.json]

[]

``` 
,
  "hosting": [
    ]
    }
  ]
}
```

You can find more details in the [Firebase documentation](https://firebase.google.com/docs/hosting/quickstart).

#### [Alternative method](#alternative-method) 

If you don\'t already have a `firebase.json` in your root directory, Nitro will create one the first time you run it. In this file, you will need to replace `<your_project_id>` with the ID of your Firebase project. This file should then be committed to the git.

1.  Create a `.firebaserc` file

It is recommended to create a `.firebaserc` file so you don\'t need to manually pass your project ID to your `firebase` commands (with `--project <your_project_id>`):

[][.firebaserc]

[]

``` 

}
```

This file is usually generated when you initialize your project with the Firebase CLI. But if you don\'t have one, you can create it manually.

2.  Install firebase dependencies

Then, add Firebase dependencies to your project:

[][npm]

[][yarn]

[][pnpm]

[][bun]

[][deno]

[]

``` 
npm i firebase-admin firebase-functions firebase-functions-test
```

[]

``` 
yarn add firebase-admin firebase-functions firebase-functions-test
```

[]

``` 
pnpm i firebase-admin firebase-functions firebase-functions-test
```

[]

``` 
bun i firebase-admin firebase-functions firebase-functions-test
```

[]

``` 
deno i npm:firebase-admin firebase-functions firebase-functions-test
```

3.  Log into the firebase CLI

Make sure you are authenticated with the firebase cli. Run this command and follow the prompts:

[][npm]

[][yarn]

[][pnpm]

[][bun]

[][deno]

[]

``` 
npx firebase-tools login
```

[]

``` 
yarn dlx firebase-tools login
```

[]

``` 
pnpm dlx firebase-tools login
```

[]

``` 
bunx firebase-tools login
```

[]

``` 
deno run -A npm:firebase-tools login
```

### [[[]]Local preview](#local-preview) 

You can preview a local version of your site if you need to test things out without deploying.

[]

``` 
NITRO_PRESET=firebase npm run build
firebase emulators:start
```

### [[[]]Build and deploy](#build-and-deploy) 

Deploy to Firebase Hosting by running a Nitro build and then running the `firebase deploy` command.

[]

``` 
NITRO_PRESET=firebase npm run build
```

[][npm]

[][yarn]

[][pnpm]

[][bun]

[][deno]

[]

``` 
npx firebase-tools deploy
```

[]

``` 
yarn dlx firebase-tools deploy
```

[]

``` 
pnpm dlx firebase-tools deploy
```

[]

``` 
bunx firebase-tools deploy
```

[]

``` 
deno run -A npm:firebase-tools deploy
```

If you installed the Firebase CLI globally, you can also run:

[]

``` 
firebase deploy
```

### [[[]]Using 2nd generation firebase functions](#using-2nd-generation-firebase-functions) 

-   [Comparison between 1st and 2nd generation functions](https://firebase.google.com/docs/functions/version-comparison)

To switch to the more recent and, recommended generation of firebase functions, set the `firebase.gen` option to `2`:

[][nitro.config.ts]

[][nuxt.config.ts]

[]

``` 
export default defineNitroConfig(
})
```

[]

``` 
export default defineNuxtConfig(
  }
})
```

[]If you cannot use configuration for any reason, alternatively you can use `NITRO_FIREBASE_GEN` environment variable.

If you already have a deployed version of your website and want to upgrade to 2nd gen, [see the Migration process on Firebase docs](https://firebase.google.com/docs/functions/2nd-gen-upgrade). Namely, the CLI will ask you to delete your existing functions before deploying the new ones.

### [[[]]Options](#options) 

You can set options for the firebase functions in your `nitro.config.ts` file:

[][nitro.config.ts]

[][nuxt.config.ts]

[]

``` 
export default defineNitroConfig(,
  },
});
```

[]

``` 
export default defineNuxtConfig(,
    },
  },
});
```

You can also set options for 1st generation Cloud Functions if the `gen` option is set to `1`. Note these are different from the options for 2nd generation Cloud Functions.

#### [Runtime Node.js version](#runtime-nodejs-version) 

You can set custom Node.js version in configuration:

[][nitro.config.ts]

[][nuxt.config.ts]

[]

``` 
export default defineNitroConfig(,
});
```

[]

``` 
export default defineNuxtConfig(,
  },
});
```

Firebase tools use the `engines.node` version in `package.json` to determine which node version to use for your functions. Nitro automatically writes to the `.output/server/package.json` with configured Node.js version.

You might also need to add a runtime key to your `firebase.json` file:

[][firebase.json]

[]

``` 

}
```

You can read more about this in [Firebase Docs](https://firebase.google.com/docs/functions/manage-functions?gen=2nd#set_nodejs_version).

### [[[]]If your firebase project has other cloud functions](#if-your-firebase-project-has-other-cloud-functions) 

You may be warned that other cloud functions will be deleted when you deploy your nitro project. This is because nitro will deploy your entire project to firebase functions. If you want to deploy only your nitro project, you can use the `--only` flag:

[]

``` 
firebase deploy --only functions:server,hosting
```

### [[[]]Advanced](#advanced) 

#### [Renaming function](#renaming-function) 

When deploying multiple apps within the same Firebase project, you must give your server a unique name in order to avoid overwriting your functions.

You can specify a new name for the deployed Firebase function in your configuration:

[][nitro.config.ts]

[][nuxt.config.ts]

[]

``` 
export default defineNitroConfig(
})
```

[]

``` 
export default defineNuxtConfig(
  }
})
```

[]`firebase.serverFunctionName` must be a valid JS variable name and cannot include dashes (`-`).

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/2.deploy/20.providers/firebase.md)

[](/deploy/providers/edgio)

[]

Edgio

Deploy Nitro apps to Edgio.

[](/deploy/providers/flightcontrol)

[]

Flightcontrol

Deploy Nitro apps to AWS via Flightcontrol.

[On this page][[]]

[On this page][[]]

-   [[Firebase app hosting]](#firebase-app-hosting)
    -   [[Project setup]](#project-setup)
-   [[Firebase hosting (deprecated)]](#firebase-hosting-deprecated)
    -   [[Project Setup]](#project-setup-1)
    -   [[Local preview]](#local-preview)
    -   [[Build and deploy]](#build-and-deploy)
    -   [[Using 2nd generation firebase functions]](#using-2nd-generation-firebase-functions)
    -   [[Options]](#options)
    -   [[If your firebase project has other cloud functions]](#if-your-firebase-project-has-other-cloud-functions)
    -   [[Advanced]](#advanced)