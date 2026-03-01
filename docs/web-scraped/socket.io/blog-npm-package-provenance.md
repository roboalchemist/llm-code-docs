# Source: https://socket.io/blog/npm-package-provenance/

Title: npm package provenance | Socket.IO

URL Source: https://socket.io/blog/npm-package-provenance/

Published Time: 2024-07-25T00:00:00.000Z

Markdown Content:
Hello everyone!

We are happy to announce that Socket.IO packages will now be published with a provenance statement.

Starting today, new Socket.IO versions will be published directly from GitHub Actions and no longer from a maintainer machine.

The publication workflow can be found here: [`publish.yml`](https://github.com/socketio/socket.io/blob/main/.github/workflows/publish.yml)

There are a few notable differences from the [reference workflow](https://docs.npmjs.com/generating-provenance-statements):

### Workflow trigger[​](https://socket.io/blog/npm-package-provenance/#workflow-trigger "Direct link to Workflow trigger")

The workflow is triggered when pushing a tag to GitHub:

`on:  push:    tags:      - '**@*'`

The expected format is `<package>@<version>`, for example:

*   `socket.io@1.2.3`
*   `@socket.io/redis-adapter@3.4.5` (hence the `**` to match the `/` char)

The `<package>` part is then used to select the right workspace (since we are using [a monorepo](https://socket.io/blog/monorepo/)):

`jobs:  publish:    steps:      # [...]      - name: Publish package        run: npm publish --workspace=${GITHUB_REF_NAME%@*} --provenance --access public        env:          NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}`

Reference: [https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)

### Compilation step[​](https://socket.io/blog/npm-package-provenance/#compilation-step "Direct link to Compilation step")

A TypeScript compilation step is necessary, since some packages depend on the types of other packages:

`jobs:  publish:    steps:      # [...]      - name: Compile each package        run: npm run compile --workspaces --if-present      - name: Publish package      # [...]`

The latest version of the `engine.io-parser` package has been released this way.

On the [npmjs.com](https://www.npmjs.com/package/engine.io-parser) website, you can find:

*   the details of the build, at the bottom of the page:

![Image 1: Provenance details on www.npmjs.com](https://socket.io/assets/images/provenance-details-a3af0d987e0389724c5e0244055abe9a.png)

*   a checked badge, in the "Versions" tab

![Image 2: Provenance badge on www.npmjs.com](https://socket.io/assets/images/provenance-badge-a4562f3cf67c33da2090d3a2cbaaf4d7.png)

You can also verify the attestations of your dependencies:

`$ npm i socket.ioadded 22 packages, and audited 23 packages in 853msfound 0 vulnerabilities$ npm audit signaturesaudited 22 packages in 1s22 packages have verified registry signatures1 package has a verified attestation # <-- it's a good start!`

This is a big step forward in increasing trust in the JS ecosystem, congratulations to the npm team!

Some big names have already joined the club:

*   [axios](https://www.npmjs.com/package/axios)
*   [next](https://www.npmjs.com/package/next)
*   [vite](https://www.npmjs.com/package/vite)

That's all folks, thanks for reading!
