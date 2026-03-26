# Source: https://docs.socket.dev/docs/socket-for-github.md

# Guide to Socket for GitHub

Socket for GitHub help hundreds of thousands of developers protect their apps from software supply chain attacks.

> 📘 Today, thousands of organizations rely on Socket to prevent bad packages from infiltrating their software supply chain.

## Quick overview of Socket for GitHub

Socket watches for changes to “package manifest” files such as package.json, package-lock.json, and yarn.lock. Whenever a new dependency is added in a pull request, Socket analyzes the package's behavior and leaves a comment if it is a security risk.

By statically analyzing open source packages and their dependencies, Socket detects the tell-tale signs of a supply chain attack. Socket alerts developers when packages change in security-relevant ways, highlighting events such as the introduction of install scripts, obfuscated code, or usage of privileged APIs such as shell, network, filesystem, and environment variables.

Socket automatically monitors GitHub pull requests for these software supply chain risks and many more:

✅ Detect potential typo squats\
✅ Detect install scripts\
✅ Detect telemetry\
✅ Detect native code\
✅ Detect known malware\
✅ Detect shell script overrides\
✅ Detect mutable git/http dependencies\
✅ Detect invalid package manifests\
✅ Detect protestware/troll packages

### Install scripts

The npm package manager allows a package to specify an ["install script"](https://socket.dev/npm/issue/installScripts) – an arbitrary shell command – that will run immediately when a package is installed. Install scripts are commonly used to build native code, print donation banners, or do other post-install tasks. However, this (anti-)feature is quite easy to abuse.

The vast majority of malware on npm uses an install script to deliver its payload. In fact, a [2022 paper](https://arxiv.org/abs/2112.10165) found nearly 94% of malicious packages had at least one install script.

> 📘 We found 93.9% \[...] of malicious packages had at least one install script, indicating that malicious attackers use install scripts frequently
>
> Nusrat Zahan, et al

Despite the pervasive use by malware, install scripts are in fact quite rare across the npm ecosystem. Most apps have only a handful of dependencies that use this powerful feature.

Socket can now identify when a newly-added package contains an install script, or more worryingly, when a new version of an existing package introduces a new install script. When Socket identifies a new install script – a relatively rare and highly suspicious event – it will alert the developer via a GitHub comment so they can evaluate whether the install script is safe.

In this real example from a user's repo, Socket detected that the popular `styled-components` package decided to add a "protestware" install script in version 5.3.5:

![](https://files.readme.io/0b4b9de-install-script.png "install-script.png")

To help the developer investigate, Socket helpfully includes a link to [the exact script](https://socket.dev/npm/package/styled-components/files/5.3.5/postinstall.js) that will run in the installation step.

![](https://files.readme.io/0c13b9f-protestware.png "protestware.png")

In this case, the install script is a benign instance of protestware, though some protestware is [much more destructive](https://www.bleepingcomputer.com/news/security/big-sabotage-famous-npm-package-deletes-files-to-protest-ukraine-war/).

### Telemetry

Websites or apps often include a telemetry system that collects data about how users interact with a product. This data can help improve the product, catch bugs, or even detect abuse. While telemetry in apps is relatively common, [telemetry](https://socket.dev/npm/issue/telemetry) in open source packages is quite unusual.

We've heard from our users that they do not expect their dependencies to be collecting telemetry and sending it off to remote servers. **Unfortunately, telemetry in open source dependencies is becoming more common.**

Socket can now detect packages that collect telemetry, alert the developer, and provide actionable information about how to disable the telemetry.

In this real example, Socket detected that a newly introduced dependency, [`angular-calendar`](https://socket.dev/npm/package/angular-calendar), is collecting telemetry:

![](https://files.readme.io/955a9f7-telemetry.png "telemetry.png")

Socket helpfully identifies the package collecting the telemetry, [`@scarf/scarf`](https://socket.dev/npm/package/@scarf/scarf), and provides information on how to opt-out of the telemetry system.

Teams can now use Socket to keep dependencies that collect telemetry out of their codebases, or disable the telemetry functionality.

### Native code

Packages which contain [native code](https://socket.dev/npm/issue/hasNativeCode), i.e. compiled executable files, are rare on npm, but there are some. Native code is often used in packages that interface with a database, are performance-critical, or provide JavaScript bindings around native code.

From a security perspective, native code is not ideal. Packages that include binaries are harder to audit since the source code may not be available, and you may need a binary disassembler to understand the package behavior. To complicate matters, packages may include different binaries for each supported platform and processor architecture. Worse still, a malicious actor may use native code to obscure their malware from JavaScript static analysis tools such as Socket or ESLint.

At a more fundamental level, native code may prevent a package from running in certain environments such as browsers, Vercel Edge Functions, Cloudflare Workers, or Deno.

Socket can now detect packages that contain native code and alert the developer, providing actionable information about how to disable the native code in cases where it's optional.

![](https://files.readme.io/edaf42e-native-code.png "native-code.png")

This detection also finds packages which do odd things, such as turning async functions into sync using a native code dependency like [`deasync`](https://socket.dev/npm/package/deasync).

### Known Malware

When Socket confirms that a package contains malware, we report it to npm and add it to our list of [known malware on npm](https://socket.dev/npm/issue/malware). Our #1 priority is getting the malware removed from npm to protect the JavaScript ecosystem, whether those users use Socket or not.

While npm is investigating the package, the malware remains available on npm.

Socket can now protect users from known malware by detecting when a bad package version is installed and reporting it to the developer directly in a GitHub pull request. The [Socket CLI](/integrations) (coming soon!) will also give developers a way to protect their own devices from known malware by intercepting bad `npm install` commands.

Related: Socket tracks [packages removed from npm for security reasons](https://socket.dev/npm/category/removed) which is quite interesting to look through. It's also a great way to see what package issues Socket would have detected in real historical instances of npm malware.

### Troll Packages

npm contains many packages which are low-quality, jokes, parodies, or otherwise contain code not meant to be used in production.

For example, there's a package called [`bowserify`](https://socket.dev/npm/package/bowserify) that's a Bowser-themed version of [`browserify`](https://socket.dev/npm/package/browserify). This parody package makes a few changes to the package such as including an image of Bowser (yes, the Nintendo character) and adding extra code into any JavaScript bundle that it produces – yikes!

Some npm packages are named in a way designed to trick or confuse users, such as the package [`standardjs`](https://socket.dev/npm/package/standardjs) which is designed to confuse users of [`standard`](https://socket.dev/npm/package/standard). Other packages, such as [`-`](https://socket.dev/npm/package/-) (yes, the actual package name is a dash character), are frequently installed by accident when a user typos a command line flag to `npm install`.

Socket can now protect users from misleading packages like these by reporting them directly to the developer inline in a GitHub pull request.

![](https://files.readme.io/4c68611-troll.png "troll.png")

### Typosquats

The most common attack vector is typosquatting.

Typosquatting is when an attacker publishes a package which has a very similar name to a legitimate and popular package. Take these two packages with very similar names, for instance:

```
npm install noblox.js-proxied
npm install noblox.js-proxy
```

One of these is legitimate and one of these is malware. But which is which? And what if you can't remember and so you just take a guess?

With the Socket GitHub App in place, the developer who opened the pull request (or the developer reviewing it) will have their attention drawn to this [potential typosquat](https://socket.dev/npm/issue/didYouMean).

![](https://files.readme.io/cacee13-typosquat.png "typosquat.png")