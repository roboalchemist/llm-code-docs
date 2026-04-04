# Lost Pixel Documentation

Source: https://docs.lost-pixel.com/docs/llms-full.txt

---

# What is Lost Pixel?

Lost Pixel Platform & Lost Pixel(OSS)

Lost Pixel is an open-source tool to run visual regression tests on your software project. Currently supported modes include [Storybook](https://storybook.js.org/), [Ladle](https://ladle.dev/), [Histoire](https://histoire.dev/) Page Screenshots(Web app pages) & Custom Screenshots(your own way of making screenshots, e.g. Cypress or Playwright).

Like other tests in software development (e.g., unit and integration tests), visual regression tests exist to detect regressions after changes to the code base have been made. In this case, the focus is on the visual aspect of unintended changes.

Lost Pixel consists of the [Lost Pixel engine(OSS)](https://github.com/lost-pixel/lost-pixel) & [Lost Pixel Platform(SaaS)](https://lost-pixel.com); learn which one fits your needs the best:

{% content-ref url="readme-1" %}
[readme-1](https://docs.lost-pixel.com/docs/readme-1)
{% endcontent-ref %}

### Why Do I Need Visual Regression Tests?

Visual regression tests do not replace unit and integration tests. They complement them and improve the quality of your delivery.

{% embed url="<https://lost-pixel.com/blog/post/visual-regression-testing-101>" %}
Learn what is Visual Regression Testing and how you can benefit from it
{% endembed %}

The fact that the user interface is what your customers will see makes it even more important to have these quality checks in place.

Developers must be confident that an introduced code change will not break the app. Manually visiting your app's page (and state) to check if everything is rendered correctly is neither pleasant nor effective. This is a process of the past.

> Humans are great at many things - finding visual differences is not one of them.

### Use Cases

Here are a few examples that visual regression tests could help with:

#### Differences In Environments

Developer machines often carry history setups that keep being updated but rarely get a new setup state. They can sometimes deviate from staging and production environments. Catching the resulting differences in production is something that could be prevented.

#### Review Process

If your team has designers and UX people, reviewing code changes by approving visual updates could be of great value. Lost Pixel enables the review process by providing a screenshot of the version before and after the code change. This makes it super easy to understand what impact the change will have.

#### Big Engineering Teams

In bigger engineering teams, it is impossible to know and remember each change to the UI introduced by each developer. With good visual regression tests, developers stop worrying about what they might have broken on the other end of the application.

{% embed url="<https://lost-pixel.com/blog/post/visual-regression-testing-101>" %}
Lean the Case Studies for Visual Regression testing
{% endembed %}

{% embed url="<https://lost-pixel.com/blog/post/5-reasons-to-write-visual-regression-tests>" %}
Learn 5 main reasons to add Visual Regression Testing to your test suite
{% endembed %}

### Case studies:

{% embed url="<https://lost-pixel.com/blog/post/case-study-prisma>" %}
Top-notch teams like prisma.io are using Lost Pixel to overcome their challenges. Learn from their experience.
{% endembed %}

{% embed url="<https://lost-pixel.com/blog/post/lost-pixel-adverity-case-study>" %}
Teams like Adverity run millions of shots per month and make sure their clients are always looking at impeccable UI
{% endembed %}

### Guides: Jump right in

Follow our handy guides to get started on the basics as quickly as possible:

{% content-ref url="guides/getting-started/getting-started" %}
[getting-started](https://docs.lost-pixel.com/docs/guides/getting-started/getting-started)
{% endcontent-ref %}

{% content-ref url="guides/getting-started/getting-started-1" %}
[getting-started-1](https://docs.lost-pixel.com/docs/guides/getting-started/getting-started-1)
{% endcontent-ref %}

{% content-ref url="guides/getting-started/getting-started-2" %}
[getting-started-2](https://docs.lost-pixel.com/docs/guides/getting-started/getting-started-2)
{% endcontent-ref %}


# Lost Pixel Platform | Lost Pixel OSS

Lost Pixel Platform & Lost Pixel(OSS)

### Lost Pixel Platform | Lost Pixel(OSS) - how to choose?

[Lost Pixel Engine ](https://github.com/lost-pixel/lost-pixel)is the OSS part of Lost Pixel, and [Lost Pixel Platform](https://lost-pixel.com) is the cloud testing offering. We use our OSS engine to power our platform. Our mission is to democratise **Visual Regression Testing** and allow more people to use it in a way top companies are having their VRT setups - absolutely for free.

Lost Pixel Platform is a way to supercharge your visual testing workflow & make it leaner, quicker & more pleasant to work with.\
\
Here are the main differences between our two core offerings:

#### Lost Pixel(OSS)

* tiny team
* little collaboration needs
* no need for speed
* surface review process
* no monorepo support
* no collaborative integrations(comments, notifications)

#### Lost Pixel Platform

* mid-sized/large team
* high collaboration needs
* speed of execution
* review & maintenance workflow trusted by top teams
* **monorepo support**
* collaborative integrations(comments, notifications)


# Project Configuration

Each project needs a configuration file that lives inside the Git repo of the project.

To get started, you can use the init command to create an initial configuration which uses storybook by default, you can [change the mode](https://docs.lost-pixel.com/docs/setup/project-configuration/modes) in the config file later:

```bash
npx lost-pixel init-js
```

This will create a new file `lostpixel.config.js` that looks the following way:

{% code overflow="wrap" %}

```javascript
module.exports = {
  storybookShots: {
    storybookUrl: 'examples/storybook-build/storybook-static',
  },
  // OSS mode 
  generateOnly: true,
  
  // Lost Pixel Platform (to use in Platform mode, comment out the OSS mode and uncomment this part )
  // lostPixelProjectId: "xxxx",
  // process.env.LOST_PIXEL_API_KEY,
};
```

{% endcode %}

### TypeScript

In case you prefer TypeScript (recommended), you will need to do a bit more but will benefit from a much better experience when it comes to configuring the project.

To initialize the configuration run this command:

```bash
npx lost-pixel init-ts
```

We will also need the `lost-pixel` NPM package to get access to the configuration types. Run this command to add it as a developer dependency:

```bash
npm i -D lost-pixel
```

Finally, we can take a look at the created configuration file `lostpixel.config.ts`. You can notice that it includes types already, which makes writing the configuration so much easier (IDE IntelliSense, type safety, ...).

```typescript
import { CustomProjectConfig } from 'lost-pixel';

export const config: CustomProjectConfig = {
  storybookShots: {
    storybookUrl: 'examples/storybook-build/storybook-static',
  },
 // OSS mode 
  generateOnly: true,
  
  // Lost Pixel Platform (to use in Platform mode, comment out the OSS mode and uncomment this part )
  // lostPixelProjectId: "xxxx",
  // process.env.LOST_PIXEL_API_KEY,
};
```

{% hint style="info" %}
Don't forget to include the configuration file in your `tsconfig.json`
{% endhint %}


# Modes

Lost Pixel can run in different modes to base your visual regression tests on one of the currently available options:

* Storybook(needs built Storybook)
* Ladle(needs built Ladle or running Ladle)
* Histoire(needs built Histoire)
* Page shots
* Custom shots

### Storybook

{% code title="lostpixel.config.ts" %}

```typescript
import { CustomProjectConfig } from 'lost-pixel';

export const config: CustomProjectConfig = {
  storybookShots: {
    storybookUrl: './storybook-static',
  },
  // OSS mode 
  generateOnly: true,
  failOnDifference: true
  
  // Lost Pixel Platform (to use in Platform mode, comment out the OSS mode and uncomment this part )
  // lostPixelProjectId: "xxxx",
  // process.env.LOST_PIXEL_API_KEY,
};
```

{% endcode %}

### Ladle

{% code title="lostpixel.config.ts" %}

```typescript
import { CustomProjectConfig } from 'lost-pixel';

export const config: CustomProjectConfig = {
  ladleShots: {
  // IP should be localhost when running locally & 172.17.0.1 when running in GitHub action
    baseUrl: 'http://172.17.0.1:61000',
  },
  // OSS mode 
  generateOnly: true,
  failOnDifference: true
  
  // Lost Pixel Platform (to use in Platform mode, comment out the OSS mode and uncomment this part )
  // lostPixelProjectId: "xxxx",
  // process.env.LOST_PIXEL_API_KEY,
};
```

{% endcode %}

### Histoire

{% code title="lostpixel.config.ts" %}

```typescript
import { CustomProjectConfig } from 'lost-pixel';

export const config: CustomProjectConfig = {
  histoireShots: {
    histoireUrl: './.histoire/dist',
  },
  // OSS mode 
  generateOnly: true,
  failOnDifference: true
  
  // Lost Pixel Platform (to use in Platform mode, comment out the OSS mode and uncomment this part )
  // lostPixelProjectId: "xxxx",
  // process.env.LOST_PIXEL_API_KEY,
};
```

{% endcode %}

### Page shots

Page screenshots presume any frontend application that can run in the browser. This example uses Next.js

{% code title="lostpixel.config.ts" %}

```typescript
import { CustomProjectConfig } from 'lost-pixel';

export const config: CustomProjectConfig = {
  pageShots: {
    pages: [
      { path: '/app', name: 'app' },
      { path: '/next-app', name: 'next-app' },
      { path: '/next-app?name=App', name: 'next-app-with-query-param' },
      { path: '/fetch', name: 'fetch-static-props' },
      { path: '/client-fetch', name: 'fetch-client' },
    ],
    // IP should be localhost when running locally & 172.17.0.1 when running in GitHub action

    baseUrl: 'http://localhost:3000',
  },
  // OSS mode 
  generateOnly: true,
  failOnDifference: true
  
  // Lost Pixel Platform (to use in Platform mode, comment out the OSS mode and uncomment this part )
  // lostPixelProjectId: "xxxx",
  // process.env.LOST_PIXEL_API_KEY,
};
```

{% endcode %}

### Custom shots

Custom screenshots presume that you take the screenshots on your side & Lost Pixel Platform runs them for Visual Regression tests. In this example, you can use **Cypress** or **Playwright** to make the screenshots during the tests and forward them to the **lost-pixel** folder.

{% code title="lostpixel.config.ts" %}

```typescript
import { CustomProjectConfig } from 'lost-pixel';

export const config: CustomProjectConfig = {
 customShots: {
    currentShotsPath: "./lost-pixel",
  },
  // OSS mode 
  generateOnly: true,
  failOnDifference: true
  
  // Lost Pixel Platform (to use in Platform mode, comment out the OSS mode and uncomment this part )
  // lostPixelProjectId: "xxxx",
  // process.env.LOST_PIXEL_API_KEY,
};
```

{% endcode %}

### Holistic Visual Regression Testing mode

Lost Pixel supports simultaneously using several modes to achieve visual regression testing needs. In the following example, we presume that your app packages some components you want to test with **Ladle** & some **full-page screenshots** that incorporate those components.

{% code title="lostpixel.config.ts" %}

```typescript
import { CustomProjectConfig } from 'lost-pixel';

export const config: CustomProjectConfig = {
  pageShots: {
    pages: [
      { path: '/app', name: 'app' },
      { path: '/next-app', name: 'next-app' },
    ],
    // IP should be localhost when running locally & 172.17.0.1 when running in GitHub action
    baseUrl: 'http://172.17.0.1:3000',

  },
  ladleShots: {
    // IP should be localhost when running locally & 172.17.0.1 when running in GitHub action
    ladleUrl: 'http://172.17.0.1:61000',
  },
  // OSS mode 
  generateOnly: true,
  failOnDifference: true
  
  // Lost Pixel Platform (to use in Platform mode, comment out the OSS mode and uncomment this part )
  // lostPixelProjectId: "xxxx",
  // process.env.LOST_PIXEL_API_KEY,
};
```

{% endcode %}


# Baseline images

{% hint style="danger" %}
This part of the documentation is only relevant for Lost Pixel(OSS) mode
{% endhint %}

Lost Pixel works through the concept of baseline images. A baseline image is something that is accepted to be the agreed desired state of the resulting component/page snapshot. Lost Pixel keeps the baseline images in a dedicated folder in `.png` format. `current` & `difference`\
paths are utility and used during the run of the action.

\
You could adapt the relative paths to the images in the config file:

{% code title="lostpixel.config.ts" %}

```typescript
import { CustomProjectConfig } from 'lost-pixel';

export const config: CustomProjectConfig = {
  ladleShots: {
    ladleUrl: 'http://localhost:61000',
  },
  imagePathBaseline: "./baseline-images",
  imagePathCurrent: "./current-images",
  imagePathDifference: "./difference-images",
  generateOnly: true,
};
```

{% endcode %}


# Integrating With GitHub Actions

Lost Pixel has first-class support for GitHub Actions, offering a dedicated action in the GitHub Action Marketplace:

```
- name: Lost Pixel
  uses: lost-pixel/lost-pixel@v3.22.0
```

As outlined in [modes](https://docs.lost-pixel.com/docs/setup/project-configuration/modes), Lost Pixel can run in different modes or all of them simultaneously. You would need to build the respective provider and serve it in the action to make it available for the Lost Pixel, e.g. build & serve storybook, build & serve ladle, build & serve next app

Here's an example of a complete workflow file that builds the Storybook before continuing with Lost Pixel. To make it run, you need to place `vis-reg-test.yml` it into `.github/workflows` at the root of your project. This will execute the Lost Pixel visual regression tests on every commit:

{% code title="vis-reg-test.yml" %}

```yaml
on: [push]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Setup Node
        uses: actions/setup-node@v3
        with:
          node-version: 18.x
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Build Storybook
        run: npm run build-storybook

      - name: Lost Pixel
        uses: lost-pixel/lost-pixel@v3.22.0
```

{% endcode %}

{% hint style="info" %}
Using Lost Pixel in **Platform Mode,** you need to provide the `LOST_PIXEL_API_KEY`

`to the action:`

```
- name: Lost Pixel
  uses: lost-pixel/lost-pixel@v3.22.0
  env:
      LOST_PIXEL_API_KEY: ${{ secrets.LOST_PIXEL_API_KEY }}
```

{% endhint %}


# Lost Pixel Platform

Setting up Lost Pixel Platform - managed version of Lost Pixel

[Lost Pixel Platform](https://lost-pixel.com) offers a managed service with a user-friendly interface for a more efficient visual regression testing workflow.

The platform version provides additional features like collaboration tools, automated test runs, and detailed reporting. Upgrading to the Lost Pixel Platform allows you to streamline your visual regression testing process, improve collaboration with your team, and gain access to valuable insights and analytics.

Lost Pixel Platform has first-class integration with **GitHub** & **GitHub Actions** but can be set up with any CI provider, **`given it runs on GitHub`**

{% embed url="<https://lost-pixel.com/blog/post/storybook-visual-regression-testing-with-lost-pixel-platform>" %}
Storybook + Lost Pixel Platform
{% endembed %}

{% embed url="<https://lost-pixel.com/blog/post/visual-regression-testing-with-ladle>" %}
Ladle + Lost Pixel Platform
{% endembed %}

{% embed url="<https://lost-pixel.com/blog/post/playwright-visual-regression-testing>" %}
Playwright + Lost Pixel Platform
{% endembed %}

### Create Lost Pixel related files

We need to create `lostpixel.config.js|ts` file that will run the whole setup. We will use the example of [lost-pixel.com](https://www.lost-pixel.com) as it is set up on our own platform 😊

{% code title="lostpixel.config.ts" %}

```typescript
import { CustomProjectConfig } from 'lost-pixel';

export const config: CustomProjectConfig = {
  pageShots: {
    pages: [
      { path: '/', name: 'landing' },
      {
        path: '/blog',
        name: 'blog',
      },
    ],
    baseUrl: 'http://172.17.0.1:3000',
  },
  lostPixelProjectId: 'we_will_paste_id_here_later',
  apiKey: process.env.LOST_PIXEL_API_KEY,
};
```

{% endcode %}

Next up is the GitHub action declaration file that lives in `.github/workflows`. We are building & serving our Next.js application & run Lost Pixel on it's pages(defined in the above file):

{% code title="visual-regression.yml" %}

```yaml
on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    name: Lost Pixel

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Setup Node
        uses: actions/setup-node@v3
        with:
          node-version: 16.x

      - name: Instal pnpm
        uses: pnpm/action-setup@v2
        with:
          version: 7.17.1

      - name: Install dependencies
        run: pnpm install

      - name: Build next
        run: pnpm run build

      - name: Start next
        run: pnpm run start &

      - name: Lost Pixel
        uses: lost-pixel/lost-pixel@v3.22.0
        env:
          LOST_PIXEL_API_KEY: ${{ secrets.LOST_PIXEL_API_KEY }}
```

{% endcode %}

### Set up the Lost Pixel platform

Visit the [Lost Pixel installation page](https://github.com/apps/lost-pixel/installations/new) and install Lost Pixel App on organisations & repositories you want to have visual tests on

<figure><img src="https://354517992-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tpFIKHmNw4YdppgU75t%2Fuploads%2Fgit-blob-373a257836120ab8d506fab1a53131721a9495f1%2FSCR-20230114-p4f%20(2).png?alt=media" alt=""><figcaption></figcaption></figure>

Sign in using **GitHub** into [app.lost-pixel.com](https://app.lost-pixel.com), switch to the correct organisation & select which repositories selected in the previous step should be visible on the Lost Pixel Platform:

<figure><img src="https://354517992-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tpFIKHmNw4YdppgU75t%2Fuploads%2Fgit-blob-a0256c9dbd97bb4ea05edd9fc49dc69815571a8e%2FSCR-20230114-pbf.png?alt=media" alt=""><figcaption><p>app.lost-pixel.com/app/repos/manage</p></figcaption></figure>

From the onboarding-screen copy your **`project id`** and replace it in the `lostpixel.config.ts` created in the first step

```
lostPixelProjectId: 'clcuk66iz005wp41h3cauveb2',
```

Copy the **Lost Pixel API key**, we will need to do the final step to provide it as a GitHub Action secret.

<figure><img src="https://354517992-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tpFIKHmNw4YdppgU75t%2Fuploads%2Fgit-blob-d828b40e297f79c8afe5fbab3d8595f5d85365da%2FSCR-20230114-phf.png?alt=media" alt=""><figcaption><p>app.lost-pixel.com/app/repos/lost-pixel-landing</p></figcaption></figure>

### Set Lost Pixel API key on GitHub

<figure><img src="https://354517992-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tpFIKHmNw4YdppgU75t%2Fuploads%2Fgit-blob-f490f388dcdf52c29f39db04c9b75b86d06c4bc4%2FSCR-20230114-oyx.png?alt=media" alt=""><figcaption><p>Setting LOST_PIXEL_API_KEY as Action Secret</p></figcaption></figure>

### Your visual regression testing workflow is done 🎊

All new pushes to your repository are triggering visual tests that you can conveniently manage yourself or collaboratively with your team!

<figure><img src="https://354517992-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tpFIKHmNw4YdppgU75t%2Fuploads%2Fgit-blob-008a2a69f554c8c5376a93b4ae7bd67f302b0b8f%2Fimage%20(2).png?alt=media" alt=""><figcaption><p>lost-pixel.com visual test managed on Lost Pixel Platform</p></figcaption></figure>


# Getting started

Lost Pixel is simple to setup with the most popular frontend component frameworks and applications. Check out some useful guides:

{% content-ref url="getting-started/getting-started-1" %}
[getting-started-1](https://docs.lost-pixel.com/docs/guides/getting-started/getting-started-1)
{% endcontent-ref %}

{% content-ref url="getting-started/getting-started" %}
[getting-started](https://docs.lost-pixel.com/docs/guides/getting-started/getting-started)
{% endcontent-ref %}

{% content-ref url="getting-started/getting-started-2" %}
[getting-started-2](https://docs.lost-pixel.com/docs/guides/getting-started/getting-started-2)
{% endcontent-ref %}


# Getting started with Storybook

### Prerequisites

* storybook that holds stories to be tested
* lost-pixel configuration file

1. Follow this [storybook guide](https://storybook.js.org/docs/react/get-started/install) to add it to your project in minutes
2. Add lost-pixel [configuration file](https://docs.lost-pixel.com/docs/setup/project-configuration/modes#storybook)
3. Add action file in the root of your project. In `.github/workflows/ci.yml`

   ```
   on: [push]
   jobs:
     build:
       runs-on: ubuntu-latest

       steps:
         - name: Checkout
           uses: actions/checkout@v3

         - name: Setup Node
           uses: actions/setup-node@v3
           with:
             node-version: 18.x
             cache: "npm"

         - name: Install dependencies
           run: npm install

         - name: Build Storybook
           run: npm run build-storybook

         - name: Lost Pixel
           uses: lost-pixel/lost-pixel@v3.22.0
   ```
4. *(Optional)* Add [automatic PR for easy baseline update](https://docs.lost-pixel.com/docs/recipes/lost-pixel-oss/automatic-baseline-update-pr)

{% content-ref url="../../recipes/lost-pixel-oss/automatic-baseline-update-pr" %}
[automatic-baseline-update-pr](https://docs.lost-pixel.com/docs/recipes/lost-pixel-oss/automatic-baseline-update-pr)
{% endcontent-ref %}

{% hint style="info" %}
Note that your `lostpixel.config.js|ts|cjs|mjs` should point to the correct **relative path to the built storybook** or to **served storybook URL**
{% endhint %}

After writing your first stories, you can adopt the visual regression testing by following the [*visual regression testing* workflow](https://docs.lost-pixel.com/docs/guides/testing-workflow-github-actions)

{% hint style="info" %}
You can see some popular integrations in the [lost-pixel-examples](https://github.com/lost-pixel/lost-pixel-examples) directory
{% endhint %}


# Getting started with Ladle

### Prerequisites

* ladle that holds stories to be tested
* lost-pixel configuration file

1. Follow this [handy ladle guide ](https://ladle.dev/docs/setup)to add it to your project in minutes
2. Add lost-pixel [configuration file](https://docs.lost-pixel.com/docs/setup/project-configuration/modes#ladle)
3. Add action file in the root of your project. In `.github/workflows/ci.yml`

   <pre data-overflow="wrap"><code>on: [push]
   jobs:
     build:
       runs-on: ubuntu-latest


      steps:
        - name: Checkout
          uses: actions/checkout@v3

        - name: Setup Node
          uses: actions/setup-node@v3
          with:
            node-version: 18.x
            cache: "npm"

        - name: Install dependencies
          run: npm install

        - name: Build ladle
          run: npm run build

        - name: Serve ladle
          run: npm run serve &#x26;

        - name: Lost Pixel
          uses: lost-pixel/lost-pixel@v3.22.0
   </code></pre>
4. *(Optional)* Add [automatic PR for easy baseline update](https://docs.lost-pixel.com/docs/recipes/lost-pixel-oss/automatic-baseline-update-pr)

{% content-ref url="../../recipes/lost-pixel-oss/automatic-baseline-update-pr" %}
[automatic-baseline-update-pr](https://docs.lost-pixel.com/docs/recipes/lost-pixel-oss/automatic-baseline-update-pr)
{% endcontent-ref %}

After writing your first stories you can adopt the visual regression testing by following [*visual regression testing* workflow](https://docs.lost-pixel.com/docs/guides/testing-workflow-github-actions)

{% hint style="info" %}
This example is available [here](https://github.com/lost-pixel/lost-pixel-examples/tree/main/example-ladle). You can see some other popular integrations in the [lost-pixel-examples](https://github.com/lost-pixel/lost-pixel-examples) directory.
{% endhint %}


# Getting started with Next js

### Prerequisites

* storybook that holds stories to be tested
* lost-pixel configuration file

1. Follow this [next.js quickstart doc](https://nextjs.org/docs) to have a basic example up and running
2. Add lost-pixel [configuration file](https://docs.lost-pixel.com/docs/setup/project-configuration/modes#page-shots)
3. Add action file in the root of your project. In `.github/workflows/ci.yml`

   <pre><code>on: [push]
   <strong>jobs:
   </strong>  build:
       runs-on: ubuntu-latest

       steps:
         - name: Checkout
           uses: actions/checkout@v3

         - name: Setup Node
           uses: actions/setup-node@v3
           with:
             node-version: 18.x
             cache: "npm"

         - name: Install dependencies
           run: npm install

         - name: Build ladle
           run: npm run build

         - name: Serve ladle
           run: npm run serve &#x26;

         - name: Lost Pixel
           uses: lost-pixel/lost-pixel@v3.22.0
   </code></pre>
4. *(Optional)* Add [automatic PR for easy baseline update](https://docs.lost-pixel.com/docs/recipes/lost-pixel-oss/automatic-baseline-update-pr)

{% content-ref url="../../recipes/lost-pixel-oss/automatic-baseline-update-pr" %}
[automatic-baseline-update-pr](https://docs.lost-pixel.com/docs/recipes/lost-pixel-oss/automatic-baseline-update-pr)
{% endcontent-ref %}

After writing your first stories you can adopt the visual regression testing by following [*visual regression testing* workflow](https://docs.lost-pixel.com/docs/guides/testing-workflow-github-actions)

{% hint style="info" %}
You can see some popular integrations in the [lost-pixel-examples](https://github.com/lost-pixel/lost-pixel-examples) directory
{% endhint %}


# Testing workflow (GitHub Actions)

Whenever your frontend code changes, there is a possibility of a visual regression being introduced. Lost Pixel automates the testing process and reduces manual labor and blocking tasks.

<figure><img src="https://354517992-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tpFIKHmNw4YdppgU75t%2Fuploads%2Fgit-blob-bba7b321c3bfdf4acf840324e7cf80b89e5fec9f%2F9442aab8e86a1d9b4a9d20a80ffe20d83830c314-2151x1572%20(1).png?alt=media" alt="" width="338"><figcaption><p>VIsual Testing Process</p></figcaption></figure>

Follow the GitHub Actions configuration instructions to set up the CI job. Every run will result in either a **green state** ✅ (no visual differences between the baseline image & image resulting from the change) or a **red state** ❌ (visual difference between the baseline image & image resulting from the change).\
\
✅ - you are doing great; your changes have not resulted in a difference in the visual appearance of your components/pages

❌ - there was either an intended or **unintended** change in the visual appearance of your components/pages. If the change was *intended*, you need to [update the baseline image](https://docs.lost-pixel.com/docs/guides/testing-and-updating-baseline-locally) for that particular story, **OR** if it was *unintended,* you need to investigate the change and try to bring the visuals back to baseline


# Updating baseline images

{% hint style="warning" %}
The Open Source edition of Lost Pixel aims to give you building blocks for creating your visual regression testing pipelines with some limitations.
{% endhint %}

In the `open-source edition` of Lost Pixel, the updates of baselines is something that engineers need to take care of. If you have failed visual regression tests ❌ with an **intended** change in the visual appearance of your components/pages according to the [visual regression testing workflow ](https://docs.lost-pixel.com/docs/guides/testing-workflow-github-actions)you need to **update the baseline** to reflect the intended change. After the code modifications, you will need to run the Lost Pixel update and commit new baselines to the git repository:

* You need to update the baselines on intended changes manually
* <mark style="color:green;background-color:green;">RECOMMENDED local flow:</mark> You can run the baseline update locally with `npx lost-pixel docker update`. This will ensure that there are no operating system-related differences and will update your baselines.
* <mark style="color:green;background-color:green;">RECOMMENDED CI flow:</mark> Lost Pixel provides a [useful recipe to create automatic PR with updated baselines](https://docs.lost-pixel.com/docs/recipes/lost-pixel-oss/automatic-baseline-update-pr) in case of visual regression
* GitHub split view is your most straightforward way of comparing the before/after images.

{% hint style="info" %}
You can use **Lost Pixel Platform** to reduce the complexity of your testing workflow & drastically increase the speed and turnaround of the baseline updates.
{% endhint %}

{% embed url="<https://lost-pixel.com>" %}
Lost Pixel Platform
{% endembed %}


# Lost Pixel Platform

This section focuses on [Lost Pixel Platform](https://lost-pixel.com) - cloud visual regression testing provider


# Working with baseline images

Baseline approval flow

1. On the first run of Lost Pixel, you will always get visual snapshots to be added to the platform as a baseline.
2. After each new run, you will have a couple of options for the actions to be performed on the images:
   1. **Remove image**(if it has been deleted from visual tests)
   2. **Approve** the new baseline of the existing image(if the visual snapshot changed in a way we expected it to change)
   3. **Reject** the new baseline(this does not affect the baseline and is done for informational purposes to identify for future reviewers that that snapshot is a **result of a regression**)
3. After you approve all images for the particular build on the Lost Pixel Platform, we will automatically make the **status check on GitHub** **green**.
4. If they are not introducing changes that affect the front end, your subsequent commits shall be green on the Lost Pixel Platform and GitHub.
5. When regression has happened, there will be a **red status check on GitHub and Lost Pixel Platform** - fix it on the side of the product, commit the code, and the new build of Lost Pixel Platform shall be **green again**.


# Local debugging

Run lost-pixel locally to debug visual testing issues easier

If you are setting up the Lost Pixel platform for the project for the first time, there are high chances that you will need to make sure everything looks good for your baselines and tweak a thing or two. Waiting for CI to finish to look at how your changes have affected the visual testing is tedious. We provide a utility via \`lost-pixel\` CLI to help streamline it.

{% code title="lostpixel.config.ts" %}

````
```typescript
import { CustomProjectConfig } from 'lost-pixel';

export const config: CustomProjectConfig = {
	pageShots: {
		pages: [
			{ path: '/', name: 'landing' },
			{
				path: '/blog',
				name: 'blog',
			},
		],
		baseUrl: 'http://172.17.0.1:3000',
		breakpoints: [640, 1024],
	},
	lostPixelProjectId: 'YOUR_PROJECT_ID',
	apiKey: process.env.LOST_PIXEL_API_KEY,
};

```
````

{% endcode %}

For this config, just run `npx lost-pixel local`\
\
This will ensure that the `platform mode` is overridden by `oss mode` and you can see your screenshots done locally.

Under the hood `local` flag overrides `lostPixelProjectId` with `genereateOnly:true` and for **`pageShots`** replaces anything in your **host** part of `baseUrl` with **localhost.** The above example becomes `baseUrl: 'http://localhost:3000'`


# Integrations

Making the team aware of Lost Pixel runs

Lost Pixel Platform supports various integrations that help your team collaborate on visual issues.

### Slack

You can enable the **Slack** notification on the platform and be notified in the select channel of your Slack workspace whenever there are failed builds of Lost Pixel & when somebody comments on the issues on the Lost Pixel Platform.

<figure><img src="https://354517992-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tpFIKHmNw4YdppgU75t%2Fuploads%2Fgit-blob-4fa747cc912723c62947cbfab4fe64164b6c6e8a%2Fimage%20(6).png?alt=media" alt=""><figcaption><p>Connect Slack Notification</p></figcaption></figure>

<figure><img src="https://354517992-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tpFIKHmNw4YdppgU75t%2Fuploads%2Fgit-blob-e08ac8faf8cc5b5e72cd5313268a62e3541d2e1d%2Fimage.png?alt=media" alt=""><figcaption><p>Manage Slack notificaitons</p></figcaption></figure>

### GitHub

You can enable the **GitHub** notification on the platform and be notified in the select channel of your Slack workspace whenever there are failed builds(which are part of the PR) of Lost Pixel & when somebody comments on the visual issues(which are part of the PR on GitHub) on the Lost Pixel Platform.

<figure><img src="https://354517992-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tpFIKHmNw4YdppgU75t%2Fuploads%2Fgit-blob-961e57610e655c5a048d47eefaf2cae308bd1880%2Fimage%20(7).png?alt=media" alt=""><figcaption><p>Connect GitHub notifications</p></figcaption></figure>

{% hint style="info" %}
Note that when you want to receive GitHub notifications on the **private repositories** you will need to add **lost-pixel-signals** machine user to your repository
{% endhint %}

<figure><img src="https://354517992-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tpFIKHmNw4YdppgU75t%2Fuploads%2Fgit-blob-a1a1438bec4f4d580c46b8cd1a1974cb529217aa%2Fimage%20(1).png?alt=media" alt=""><figcaption><p>Lost Pixel GitHub notifications - private repos instructions</p></figcaption></figure>


# Monorepo

Set up Lost Pixel Platform with Monorepo (GitHub Actions)

Follow a comprehensive tutorial covering the Lost Pixel + Turborepo setup(WIP)

\
The GitHub action below focuses on running Lost Pixel in monorepo mode on the Lost Pixel Platform. You need to enable this on the Platform UI first in the repository settings:\\

<figure><img src="https://354517992-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tpFIKHmNw4YdppgU75t%2Fuploads%2Fgit-blob-a7974454ee070bd98e0336751f34e2bd83a8bb9a%2Fimage%20(8).png?alt=media" alt=""><figcaption><p>Lost Pixel Platform - monorepo mode in settings</p></figcaption></figure>

{% code title=".github/workflows/vrt.yml" %}

```yaml
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  lost_pixel:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        config:
          - {
              package: "apps/web",
              name: "Lost Pixel for Web",
              command: "pnpm run dev",
            }
          - {
              package: "apps/docs",
              name: "Lost Pixel for Docs",
              command: "pnpm run dev",
            }
    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Setup Node
        uses: actions/setup-node@v3
        with:
          node-version: 16.x

      - name: Install pnpm
        uses: pnpm/action-setup@v2
        with:
          version: 7.17.1

      - name: Install dependencies
        run: pnpm install

      - name: Cache Build
        uses: actions/cache@v2
        with:
          path: |
            apps/web/.next
            apps/docs/.next
          key: ${{ runner.os }}-build-${{ github.sha }}
          restore-keys: |
            ${{ runner.os }}-build-${{ github.sha }}

      - name: Start App
        run: cd ${{ matrix.config.package }} && ${{ matrix.config.command }} &
        env:
          CI: true

      - name: ${{ matrix.config.name }}
        uses: lost-pixel/lost-pixel@v3.22.0
        env:
          LOST_PIXEL_API_KEY: ${{ secrets.LOST_PIXEL_API_KEY }}
          LOST_PIXEL_CONFIG_DIR: ${{ matrix.config.package }}
  finalize:
    needs: [lost_pixel]
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Lost Pixel Finalize
        uses: lost-pixel/lost-pixel@v3.22.0
        env:
          LOST_PIXEL_API_KEY: ${{ secrets.LOST_PIXEL_API_KEY }}
          LOST_PIXEL_CONFIG_DIR: apps/web
        with:
          FINALIZE: true
```

{% endcode %}

To run Lost Pixel in monorepo, you must ensure that you have two[ lostpixel.config.ts|js](https://docs.lost-pixel.com/docs/api-reference/lostpixel.config.js-or-ts) files in respective monorepo packages.

#### FInalise action

As seen above, a Lost Pixel Finalize step is required to wrap up the Lost Pixel run and create respective GitHub commit checks. The final step needs to point to any of the monorepo [lostpixel.config.js|ts](https://docs.lost-pixel.com/docs/api-reference/lostpixel.config.js-or-ts), in this case, it is `apps/web` but we can easily replace it with `apps/docs` with no effect on the run


# Automatic baseline updates on selected branches

Automatically update baselines when they hit a specific branch

Sometimes your team uses Visual Regression Testing flow in a non-enforcement way, meaning that Lost Pixel checks don't need to pass for a PR to be qualified for a merge.

In this case, to speed up your review flow, you can set up the automatic approval of baselines in Lost Pixel Platform whenever PR is merged into a defined branch. In this case, the branch is defined as `main` but Lost Pixel Platform supports regex syntax, and you can easily use multiple branches here or even branches that follow some regex pattern, e.g.: `main|master|develop`\\

<figure><img src="https://354517992-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tpFIKHmNw4YdppgU75t%2Fuploads%2Fgit-blob-c835b4681dc29793f312642e81f149bb57022389%2Fimage%20(5).png?alt=media" alt=""><figcaption><p>Lost Pixel Platform automatic baseline updates settings</p></figcaption></figure>

In this setup, whenever somebody merges a PR containing unapproved visual tests, they will be automatically approved on the main branch and will not appear in the next runs unless they have new changes.


# lost-pixel(OSS)

This section focuses on [lost-pixel open-source engine](https://github.com/lost-pixel/lost-pixel)


# Failing GitHub Action check

By default, Lost Pixel does not exit the action with a non-zero exit code when there is a failing lost-pixel run(**differences found** ❌), but you can easily configure it.\
\
In [lostpixel.config.js|ts|cjs|mjs](https://docs.lost-pixel.com/docs/setup/project-configuration) add the following config value:

```
...
failOnDifference: true,
...
```


# Automatic baseline update PR

Lost Pixel offers and easy GitHub action integration that will help you to automate the baseline update process by creating the PR with updated images. You will just need to accept it and merge into the original branch.

Assuming you are using [Ladle example](https://docs.lost-pixel.com/docs/guides/getting-started/getting-started), in the root of your repo let's add a new action file that runs on demand:\
`.github/workflows/update-baselines.yml`

{% hint style="info" %}
You need to [create a new personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) to use it in the workflow and you can extend the automatic pr action by following guides [in the original repo](https://github.com/peter-evans/create-pull-request) of **create-pull-request**
{% endhint %}

```yaml
on: workflow_dispatch

jobs:
  lost-pixel-update:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Setup Node
        uses: actions/setup-node@v2
        with:
          node-version: 18.x
          cache: 'npm'

      - name: Install dependencies
        run: npm install

      - name: Build ladle
        run: npm run build

      - name: Serve ladle
        run: npm run serve &

      - name: Lost Pixel
        id: lp
        uses: lost-pixel/lost-pixel@v3.22.0
        env:
          LOST_PIXEL_MODE: update
      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v4
        if: ${{ failure() && steps.lp.conclusion == 'failure' }}
        with:
          token: ${{ secrets.GH_TOKEN }}
          commit-message: update lost-pixel baselines
          delete-branch: true
          branch: 'lost-pixel-update/${{ github.ref_name }}'
          title: 'Lost Pixel update - ${{ github.ref_name }}'
          body: Automated baseline update PR created by Lost Pixel
```

![Run the action this way](https://354517992-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tpFIKHmNw4YdppgU75t%2Fuploads%2Fgit-blob-cd87a8718f957045155a99b0c61f3388b3cae2e8%2Fimage%20\(1\).png?alt=media)

The action run will generate a new PR against the original branch that will contain updated baselines, merge it and expect your tests to be **green again**:green\_circle:

![Automatically generated PR](https://354517992-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tpFIKHmNw4YdppgU75t%2Fuploads%2Fgit-blob-fcfdcbd661c2beae13273af8463bd2f865a46f8d%2Fimage.png?alt=media)


# Access test run images

When using the `open source edition` of Lost Pixel, you might want to look at your failed tests that were [happening on CI](https://docs.lost-pixel.com/docs/guides/getting-started/getting-started). While Lost Pixel provides extensive logging, you would not be able to see the images in the output of the action by default.\
\
To access the generated images you would need to use [GitHub Actions Artefacts](https://docs.github.com/en/rest/actions/artifacts). Presuming you [did not change the relative paths to the images](https://docs.lost-pixel.com/docs/setup/project-configuration/baseline-images) extend [GitHub action](https://docs.lost-pixel.com/docs/setup/integrating-with-github-actions) with the following step that takes place after `lost-pixel`:

```
...

  - uses: actions/upload-artifact@v3
    with:
      name: lost-pixel-artefacts
      path: .lostpixel
```

This step will ensure that everything that will be generated during the Lost Pixel action run on CI will be accessible for the download later after the workflow is finished:

![](https://354517992-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tpFIKHmNw4YdppgU75t%2Fuploads%2Fgit-blob-438dde13d5cd054a14f345e100554840ff4c579b%2FSCR-20220527-evp.png?alt=media)


# General recipes

This section showcases general recipes for making the most use of [Lost Pixel Platform](https://docs.lost-pixel.com/docs/setup/lost-pixel-platform) & [Lost Pixel(OSS)](https://docs.lost-pixel.com/docs/guides/getting-started)


# Thresholds

The thresholds value is set in [lostpixel.config.js-or-ts](https://docs.lost-pixel.com/docs/api-reference/lostpixel.config.js-or-ts "mention")

Values `between 0 and 1` are interpreted as percentage of the image size.

Values `greater or equal to 1` are interpreted as absolute pixel count.

### Example:

Based on an image with a size of `1,280` x `800` pixels we have a total amount of `1,024,000` pixels.

Here are a few threshold values and their corresponding pixel percentages and amounts:

| <p>Threshold Value<br>(config)</p> | <p>Percentage<br>(logs)</p> | <p>Actual Pixels<br>(logs)</p> |
| ---------------------------------- | --------------------------- | ------------------------------ |
| 1                                  | N/A                         | 1 px                           |
| 20                                 | N/A                         | 20 px                          |
| 300                                | N/A                         | 300 px                         |
| 0.0005                             | 0.05%                       | 512 px                         |
| 0.005                              | 0.5%                        | 5,120 px                       |
| 0.05                               | 5%                          | 51,200 px                      |
| 0.5                                | 50%                         | 512,000 px                     |

## Which mode to choose

Fixed values (starting from `1`) are great if you want to limit the pixel amount to a certain value. This is useful for situations where e.g. rounded corners are causing unwanted regressions. Usually, it makes sense to stay in the range of 1 to 100 pixels.

Percentage values (lower than `1`) are great for situations where you want to cover regression more from a statistical point of view. Percentage values scale perfectly with the image sizes. But there also lies the danger. If the image size is bigger, even a small percentage would turn into a big number. (e.g. 1% of an image of 1280 x 5000 px in size would create a threshold of 640 px) That would render such regression tests ineffective.

The best practice is to start with zero tolerance (`0`). When the first flaky regressions show up, try to find an absolute value of pixels that would cover a good threshold. Sometimes, there's no value in testing flaky areas of the page. It could make sense to [mask](https://docs.lost-pixel.com/docs/api-reference/mask) such areas. Setting percentage values will make sense for stories or pages where content is being added over time.

Finding the right balance for the threshold setting will depend on your strategy on visual regression testing. You can go with a rather strict approach or choose to adopt a more flexible process.


# Flakiness

{% embed url="<https://lost-pixel.com/blog/post/handling-flaky-visual-regression-tests-with-lost-pixel-platform>" %}
Blogpost related to managing flaky visual tests
{% endembed %}

## Retries

By default, only a single screenshot of the page is taken.

The [lostpixel.config.ts|js](https://docs.lost-pixel.com/docs/api-reference/lostpixel.config.js-or-ts) file has a number property called `flakynessRetries`. If set and greater than 0, at least 2 screenshots of the page will be taken.

If the hash of second screenshot differs from the hash of the first one, it will wait the time defined by `waitBetweenFlakynessRetries` (default 2000ms) to take another screenshot and repeat this process, until the same hash is obtained or the number of retries is reached. The last image obtained in this process will then be compared to the baseline image.

If `flakynessRetries` is 2, it will take **at most** 3 screenshots.


# Viewport tests

Lost Pixel supports testing different viewports. You can use the **breakpoints** option in the config. Page/story level breakpoints will override the top-level breakpoints.

{% hint style="info" %}
Breakpoint tests are supported in both OSS and Platform versions of Lost Pixel
{% endhint %}

{% code title="lostpixel.config.ts" %}

```typescript

import { CustomProjectConfig } from 'lost-pixel';

export const config: CustomProjectConfig = {
    pageShots: {
        pages: [
            { path: '/', name: 'landing' },
            {
                path: '/blog',
                name: 'blog',
                breakpoints: [800, 1400],
            },
        ],
        baseUrl: 'http://172.17.0.1:3000',
        breakpoints: [640, 1024],
    },
    waitBeforeScreenshot: 3500,
    lostPixelProjectId: 'YOUR_PROJECT_ID',
    apiKey: process.env.LOST_PIXEL_API_KEY,
};
```

{% endcode %}

<figure><img src="https://354517992-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tpFIKHmNw4YdppgU75t%2Fuploads%2Fgit-blob-f4061f0efddbd9c09881399fa14a6411adc7e7f3%2FScreenshot%202023-10-26%20at%2014.51.55.png?alt=media" alt=""><figcaption></figcaption></figure>


# Masking page elements

Lost Pixel supports masking elements that can be flaky during visual tests. Lazy-loaded images, animated components, and other parts of pages are all good candidates for masking them out.

You can use any selectors to mask the elements on the page. Refer to api reference for more details:

[mask](https://docs.lost-pixel.com/docs/api-reference/mask "mention")

{% code title="lostpixel.config.ts" %}

```typescript

import { CustomProjectConfig } from 'lost-pixel';

export const config: CustomProjectConfig = {
  pageShots: {
    pages: [
      { path: '/app', name: 'app' },
      {
        path: '/app',
        name: 'app-masked',
        mask: [{ selector: 'code' }, { selector: 'h2' }],
        breakpoints: [360, 500],
      },
      { path: '/next-app', name: 'next-app' },
    ],
    baseUrl: 'http://127.0.0.1:3000',
  },
  generateOnly: true,
  failOnDifference: true,
};
```

{% endcode %}

<figure><img src="https://354517992-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tpFIKHmNw4YdppgU75t%2Fuploads%2Fgit-blob-355b49ec61e455df23673c376d6f4bca722bc6c3%2Fapp-masked__%5Bw500px%5D.png?alt=media" alt="" width="250"><figcaption></figcaption></figure>


# Executing arbitrary code before tests runs

Lost Pixel supports arbitrary code execution through Playwright `page.evaluate() & page.addStyleTag()`. This will ensure that you isolate all the changes in the browser execution to Lost Pixel runs; **your normal code & customers will not be affected by this.**

{% code title="lostpixel.config.js" %}

```javascript
module.exports = {
  pageShots: {
    baseUrl: 'http://172.17.0.1:9000',
    mask: [{ selector: 'span.gatsby-resp-image-background-image' }],
  },
  lostPixelProjectId: 'YOUR_PROJECT_ID',
  apiKey: process.env.LOST_PIXEL_API_KEY,
  beforeScreenshot: async (page) => {
    await page.addStyleTag({
      content: `iframe {
          visibility: hidden;
        }

        /* do not show underline animation */
        #toc-holder  a {
          background-size: 0 !important;
          background-image: none !important;
        }
        /* skip image display within section */
        section img {
          visibility: hidden;
        }

        /* hide cookie banner */
        #onetrust-consent-sdk {
          display: none;
        }
        
        /* reset menu item alignment */
        #sidebar-holder li a {
          vertical-align: baseline;
        }
        `,
    })
  },
}
```

{% endcode %}

It is possible to change rendered screenshot after it was written to the file system. The most common scenario is to trim empty spaces (for example by using [Sharp](https://sharp.pixelplumbing.com)).

{% code title="lostpixel.config.js" %}

```javascript
const fs = require("node:fs/promises")
const path = require("node:path")
const sharp = require("sharp")

module.exports = {
  pageShots: {
    baseUrl: 'http://172.17.0.1:9000',
  },
  lostPixelProjectId: 'YOUR_PROJECT_ID',
  apiKey: process.env.LOST_PIXEL_API_KEY,
  afterScreenshot: async (_, { filePathCurrent }) => {
    const { base, dir } = path.parse(filePathCurrent)
    const tmpShotPath = path.join(dir, `tmp.${base}`)
    await sharp(filePathCurrent).trim().toFile(tmpShotPath)
    await fs.rename(tmpShotPath, filePathCurrent)
  },
}
```

{% endcode %}


# Programmatically generated pages

Lost Pixel config can reduce boilerplate in your Page shots. If you can programmatically generate the list of pages and make them accessible to Lost Pixel, it will function as well as providing them manually:

{% code title="lostpixel.config.js" %}

```
module.exports = {
  pageShots: {
    pagesJsonUrl: 'http://172.17.0.1:9000/lost-pixel.json',
    baseUrl: 'http://172.17.0.1:9000',

  },
  lostPixelProjectId: 'YOUR_PROJECT_ID',
  apiKey: process.env.LOST_PIXEL_API_KEY,
  },
}
```

{% endcode %}

`pagesJsonUrl` In this case, it returns the list of pages like Lost Pixel expects them:

```
 pages: [{ path: '/app', name: 'app' },{ path: '/blog', name: 'blog' }],
```


# Telemetry data

### **Overview**

The term **telemetry** refers to the collection of certain usage data to help *improve the quality of a piece of software*. Lost Pixel uses telemetry in one and single scenario:

* collecting usage data of the action

This page describes the overall telemetry approach for Lost Pixel, what kind of data is collected and how to opt-out of data collection.

### **Why does Lost Pixel collect metrics?**

Telemetry helps us better understand *how many users* are using our product, *how often* they are using our product and which mode is the most popular among usages. Our telemetry implementation is intentionally limited in scope:

* We use telemetry to answer one question: how many monthly active developers are using **`lost-pixel`**

### **When is data collected?**

Data is collected whenever Lost Pixel engine is ran.

#### **Usage data**

Invocations of the `**lost-pixel**` action results in data being sent to our event collection tool. Note that:

* The data does **NOT** include your images, repository name, organisation or anything that identifies you

Here is an overview of the data that's being submitted:

| Name         | Example   | Description                                                 |
| ------------ | --------- | ----------------------------------------------------------- |
| mode         | storybook | The mode in which lost pixel is running, could be multiple. |
| version      | 2.15.0    | Current version of lost-pixel                               |
| run-duraiton | 9.3       | The time it took to run the action                          |
| shots-number | 24        | The number of screenshots that we made during the .process  |

### Opt out

\
You can opt-out of this behavior by setting the `**LOST_PIXEL_DISABLE_TELEMETRY**` environment variable to **`1`**, e.g.:

```
LOST_PIXEL_DISABLE_TELEMETRY=1
```


# lostpixel.config.js|ts

Use typescript version for smart autocompletion and static type check of your config file

#### Options

* **browser**: `'chromium' | 'firefox' | 'webkit' | Array<'chromium' | 'firefox' | 'webkit'>`
  * **Required**
  * Defaults to `'chromium'`
  * This option specifies which browser(s) will be used for capturing screenshots.
  * Accepted values are **chromium**, **firefox**, and **webkit**, which can be used individually or as an array for multiple browsers.
* **lostPixelPlatform**: `string`
  * **Required**
  * Defaults to `'https://api.lost-pixel.com'` if not provided
  * URL of the Lost Pixel API endpoint
  * The endpoint URL is the location of the Lost Pixel platform which will be used for the visual regression testing.
* **apiKey**: `string` | `undefined`
  * **Optional**
  * API key for the Lost Pixel platform
  * The API key is used to authenticate with the Lost Pixel platform. Only used when using Lost Pixel Platform managed version.
* **storybookShots**: `{ storybookUrl: string, mask?:` [`Mask`](https://docs.lost-pixel.com/docs/api-reference/mask)`[] , elementLocator?: string}` | `undefined`
  * **Optional**
  * Enable Storybook mode
  * Allows for specifying the URL of the Storybook instance or local folder and any areas for all stories where differences will be ignored with `mask.`See reference for `Mask` below
  * Default value for `storybookUrl` is `'storybook-static'`
* **ladleShots**: `{ ladleUrl: string, mask?:` [`Mask`](https://docs.lost-pixel.com/docs/api-reference/mask)`[] }` | `undefined`
  * **Optional**
  * Enable Ladle mode
  * Allows for specifying the URL of the Ladle served instance and any areas for all stories where differences will be ignored with `mask.`See reference for `Mask` below
  * Default value for `ladleUrl` is `'http://localhost:61000'`
* **pageShots**: `{ pages:` [`PageScreenshotParameter`](https://docs.lost-pixel.com/docs/api-reference/pagescreenshotparameter)`[], pagesJsonUrl?: string, baseUrl: string, mask?:` [`Mask`](https://docs.lost-pixel.com/docs/api-reference/mask)`[] }` | `undefined`
  * **Optional**
  * Enable Page mode
  * Allows for specifying the paths to take screenshots of, the URL that must return a JSON compatible with [`PageScreenshotParameter`](https://docs.lost-pixel.com/docs/api-reference/pagescreenshotparameter)`[]`, the base URL of the running application, and any areas for all pages where differences will be ignored with `mask.`See reference for `Mask` below
  * if `pagesJsonUrl` is provided lost-pixel will try to make a call to the supplied url to fetch the pages from there. It will be composed together with `pages` provided. This is useful for running lost-pixel on the generated list of pages.
* **customShots**: `{ currentShotsPath: string }` | `undefined`
  * **Optional**
  * Enable Custom mode
  * Allows for specifying the path to current shots folder.
* **imagePathBaseline**: `string`
  * **Required**
  * Defaults to `'.lostpixel/baseline/'`
  * Path to the baseline image folder
  * The baseline image folder is where the original, or "reference" images are stored. These images will be used as a comparison point for future runs of the visual regression tests.
* **imagePathCurrent**: `string`
  * **Required**
  * Defaults to `'.lostpixel/current/'`
  * Path to the current image folder
  * The current image folder is where the images taken during the current run of the visual regression tests will be stored.
* **imagePathDifference**: `string`
  * **Required**
  * Defaults to `'.lostpixel/difference/'`
  * Path to the difference image folder
  * The difference image folder is where the images highlighting the differences between the baseline and current images will be stored.
* **shotConcurrency**: `number`
  * **Required**
  * Defaults to `5`
  * Number of concurrent shots to take
  * This determines how many images will be taken at the same time during the visual regression testing.
* **compareConcurrency**: `number`
  * **Required**
  * Defaults to `10`
  * Number of concurrent screenshots to compare
  * This determines how many images will be compared at the same time during the visual regression testing.
* **compareEngine**: `'pixelmatch' | 'odiff'`
  * **Required**
  * Defaults to `'pixelmatch'`
  * Which comparison engine to use for diffing images
  * The comparison engine is the algorithm used to compare the images and identify differences.
* **timeouts**: `{ fetchStories?: number, loadState?: number, networkRequests?: number }`
  * **Required**
  * Timeouts for various stages of the test
  * Allows for specifying timeouts for fetching stories from Storybook, loading the state of the page and waiting for network requests to finish.
  * Default value for `fetchStories` is `30000`, for `loadState` is `30000`, and for `networkRequests` is `30000`
* **waitBeforeScreenshot**: `number`
  * **Required**
  * Defaults to `1000`
  * Time to wait before taking a screenshot
  * The time to wait before taking a screenshot is used to ensure that the page is fully loaded and rendered before the image is captured.
* **waitForFirstRequest**: `number`
  * **Required**
  * Defaults to `1000`
  * Time to wait for the first network request to start
  * The time to wait for the first network request to start is used to ensure that any initial network requests have been made before the image is captured.
* **waitForLastRequest**: `number`
  * **Required**
  * Defaults to `1000`
  * Time to wait for the last network request to start
  * The time to wait for the last network request to start is used to ensure that any final network requests have been made before the image is captured.
* **threshold**: `number`

  * **Required**
  * Threshold for the difference between the baseline and current image
  * **Values between 0 and 1 are interpreted as percentage of the image size.**
  * **Values greater or equal to 1 are interpreted as absolute pixel count.**
  * This threshold is used to determine whether an image is considered different or not. It means that if the difference between the images is greater than the threshold, the test will fail.\\

  Use [thresholds](https://docs.lost-pixel.com/docs/recipes/general-recipes/thresholds "mention") recipe to get started quickly!
* **flakynessRetries**: `number`
  * **Optional**
  * Defaults to `0`
  * How many times to retry a shot for a stable result.
* **waitBetweenFlakynessRetries**: `number`
  * **Optional**
  * Defaults to `2000`
  * Time to wait between flakyness retries.


# PageScreenshotParameter

Values that can be provided to pages

* **path**: `string`
  * **Required**
  * Path to the page to take a screenshot of (e.g. '/login')
  * This is the URL path of the page that you want to take a screenshot of.
* **name**: `string`
  * **Required**
  * Unique name for the page
  * This is used to give a unique name to the page, so it can be easily identified in the results.
* **waitBeforeScreenshot**: `number`
  * **Optional**
  * Defaults to `1000`
  * Time to wait before taking a screenshot
  * The time to wait before taking a screenshot is used to ensure that the page is fully loaded and rendered before the image is captured.
* **threshold**: `number`
  * **Optional**
  * Defaults to `0`
  * Threshold for the difference between the baseline and current image
  * **Values between 0 and 1 are interpreted as percentage of the image size.**
  * **Values greater or equal to 1 are interpreted as absolute pixel count.**
  * This threshold is used to determine whether an image is considered different or not. It means that if the difference between the images is greater than the threshold, the test will fail.
* **viewport**: `{ width?: number; height?: number; }`
  * **Optional**
  * Defaults to `{ width: 1280, height: 720 }`
  * Define a custom viewport for the page
  * Allows for specifying a custom width and height for the viewport when taking the screenshot.
* **mask**: `Mask[]`
  * **Optional**
  * Define areas for the page where differences will be ignored
  * Allows for specifying areas of the image that should be ignored when comparing for differences.


# Mask

Values that can be provided to mask

* **selector**: `string`
  * **Required**
  * CSS selector for the element to mask
  * Allows you to select an element on the page by its CSS selector. This allows you to specify an area of the image that should be ignored when comparing for differences.
  * Examples:
    * `#my-id`: Selects the element with the id `my-id`
    * `.my-class`: Selects all elements with the class `my-class`
    * `div`: Selects all `div` elements
    * `div.my-class`: Selects all `div` elements with the class `my-class`
    * `li:nth-child(2n)`: Selects all even `li` elements
    * `[data-testid="hero-banner"]`: Selects all elements with the attribute `data-testid` set to `hero-banner`
    * `div > p`: Selects all `p` elements that are direct children of a `div` element

This type `Mask` is used to define areas of the image that should be ignored when comparing for differences. It allow you to specify an area of the image to be ignored by providing a CSS selector that targets the specific element on the page.


