# Source: https://docs.lost-pixel.com/docs/guides/getting-started/getting-started-2.md

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
