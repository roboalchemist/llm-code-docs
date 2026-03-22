# Source: https://docs.lost-pixel.com/docs/guides/getting-started/getting-started-1.md

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
