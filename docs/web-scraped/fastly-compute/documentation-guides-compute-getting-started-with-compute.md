# Source: https://www.fastly.com/documentation/guides/compute/getting-started-with-compute/

Title: Getting started with Compute | Fastly Documentation

URL Source: https://www.fastly.com/documentation/guides/compute/getting-started-with-compute/

Markdown Content:

1. [Home](https://www.fastly.com/documentation/)
2. [Guides](https://www.fastly.com/documentation/guides/)
3. [Compute](https://www.fastly.com/documentation/guides/compute/)

Experiment with Fastly's edge computing platform.

The Fastly Compute platform is an advanced edge computing system that runs your code, in your favorite language, on our global [edge network](https://www.fastly.com/network-map). Security and portability are provided by compiling your code to [WebAssembly](https://webassembly.org/). We run your code using [Wasmtime](https://wasmtime.dev/).

With the Compute platform you have access to Fastly edge primitives like data stores, dynamic configuration, and real-time messaging. The platform is completely language agnostic at every layer of the stack, and you can include dependencies from your preferred package registry.

Whether it's authentication, personalization, geofencing, SEO, observability, templating, APIs, or even your entire application, whatever you can conceive, you can probably run on the Compute platform.

[](https://www.fastly.com/documentation/guides/compute/getting-started-with-compute/#getting-started)Getting started
--------------------------------------------------------------------------------------------------------------------

To use the Compute platform, you must [create a Fastly account](https://www.fastly.com/signup) if you don't already have one.

### [](https://www.fastly.com/documentation/guides/compute/getting-started-with-compute/#generate-an-api-token)Generate an API token

To authenticate the [Fastly CLI](https://github.com/fastly/cli), [create an API token](https://www.fastly.com/documentation/reference/api#authentication) for your account. Make sure the token has a `global` scope, and make a note of the token.

### [](https://www.fastly.com/documentation/guides/compute/getting-started-with-compute/#set-up-the-development-environment)Set up the development environment

[Install the Fastly CLI](https://www.fastly.com/documentation/reference/tools/cli#installing), and then verify that everything works by running [fastly version](https://www.fastly.com/documentation/reference/cli/version/). For example:

`$ fastly versionFastly CLI version vX.Y.Z (abc0001)Built with go version go1.20.1 linux/amd64`

Configure the CLI to act on your behalf using the API token you created:

`$ fastly profile create`

This will store your API token credential in a configuration file and remember it for subsequent commands. There are [other ways of authenticating the CLI](https://www.fastly.com/documentation/reference/tools/cli/#configuring) if you prefer.

### [](https://www.fastly.com/documentation/guides/compute/getting-started-with-compute/#choose-a-language-to-use)Choose a language to use

We provide SDKs for multiple languages that can compile to Compute-compatible WebAssembly packages. Here is a comparison of SDK-exposed features that can differ among languages:

|  | ![Image 1: Rust logo](https://www.fastly.com/documentation/icons/languages/rust.svg) | ![Image 2: JavaScript logo](https://www.fastly.com/documentation/icons/languages/javascript.svg) | ![Image 3: Go logo](https://www.fastly.com/documentation/icons/languages/go.svg) |
| --- |
| Current SDK version | [0.11.13](https://docs.rs/fastly) | [3.40.1](https://js-compute-reference-docs.edgecompute.app/) | [1.7.0](https://pkg.go.dev/github.com/fastly/compute-sdk-go) |
| Equally supported | [Geolocation](https://www.fastly.com/documentation/guides/concepts/geolocation/),[Auto decompression](https://www.fastly.com/documentation/guides/concepts/compression),[Dynamic compression](https://www.fastly.com/documentation/guides/concepts/compression),[Environment variables](https://www.fastly.com/documentation/reference/compute/ecp-env/),[Cache override](https://www.fastly.com/documentation/guides/concepts/cache/cache-freshness/#overriding-cache-behavior-on-requests), [Real time logging](https://www.fastly.com/documentation/guides/integrations/non-fastly-services/developer-guide-logging),[Access control lists](https://www.fastly.com/documentation/guides/concepts/dynamic-config/#access-control-lists),[KV stores](https://www.fastly.com/documentation/guides/compute/edge-data-storage/about-edge-data-stores/),[Config stores](https://www.fastly.com/documentation/guides/concepts/dynamic-config/#config-stores),[Secret stores](https://www.fastly.com/documentation/guides/concepts/dynamic-config/#secret-stores),[WebSockets passthrough](https://www.fastly.com/documentation/guides/concepts/real-time-messaging/websockets-tunnel/),[Fanout](https://www.fastly.com/documentation/guides/concepts/real-time-messaging/fanout/),[Dynamic backends](https://www.fastly.com/documentation/guides/integrations/non-fastly-services/developer-guide-backends/#dynamic-backends), [Readthrough (HTTP) cache](https://www.fastly.com/documentation/guides/concepts/cache/#readthrough-http-cache),[Simple cache](https://www.fastly.com/documentation/guides/concepts/cache/#simple-cache),[Core cache](https://www.fastly.com/documentation/guides/concepts/cache/#core-cache) |
| Core feature differences |
| Next-Gen WAF | ✅ | - | - |
| Mutual TLS for origin fetch | ✅ | - | - |
| Readthrough (HTTP) cache - customize cache behavior[ℹ️](https://www.fastly.com/documentation/guides/concepts/cache/#customizing-cache-interaction-with-the-backend) | ✅ | ✅ see note below | ✅ see note below |
| Pre-release feature differences |
| Purging see note below | ✅ | - | - |
| Backend health | ✅ | ✅ | - |
| Device Detection | ✅ | ✅ | ✅ |
| Edge rate limiting [ℹ️](https://www.fastly.com/documentation/guides/concepts/rate-limiting) | ✅ | ✅ | ✅ |
|  | [More about Rust »](https://www.fastly.com/documentation/guides/compute/developer-guides/rust) | [More about JavaScript »](https://www.fastly.com/documentation/guides/compute/developer-guides/javascript) | [More about Go »](https://www.fastly.com/documentation/guides/compute/developer-guides/go) |

1. Purging from edge code allows purge operations to be triggered when processing edge requests. Purging via our API is available regardless of which SDK is used.

1. **JavaScript and Go SDKs:** Customizing cache behavior with the readthrough (HTTP) cache is an opt-in feature; see[this note](https://www.fastly.com/documentation/guides/concepts/cache#customizing-cache-interaction-with-the-backend) for details.

We recommend the use of official Fastly SDKs (available for [Rust](https://www.fastly.com/documentation/solutions/starters/compute-starter-kit-rust-default/), [JavaScript](https://www.fastly.com/documentation/solutions/starters/compute-starter-kit-javascript-default/), and [Go](https://www.fastly.com/documentation/solutions/starters/compute-starter-kit-go-default/)), but you can also create your own for a language of your choice, or use a community-created SDK. [Learn more about custom SDKs](https://www.fastly.com/documentation/guides/compute/developer-guides/custom/).

### [](https://www.fastly.com/documentation/guides/compute/getting-started-with-compute/#install-language-tooling)Install language tooling

To build your project, the Fastly CLI requires your local toolchain to be available and up to date. To install the toolchain for your chosen language, follow these instructions:

1. Rust
2. JavaScript
3. Go

Compiling Rust applications for the Compute platform requires that you have `rustup` installed. If you don't have `rustup` installed, download and install `rustup`:

`$ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y`

`rustup` itself will ensure that the necessary toolchain and components are installed by using the contents of the `rust-toolchain.toml` file in the Compute project, whenever any `cargo` command is executed.

As new versions of Rust are released, consult the [Rust on the Compute platform](https://www.fastly.com/documentation/guides/compute/developer-guides/rust) page to determine whether those versions are compatible with the Compute platform.

### [](https://www.fastly.com/documentation/guides/compute/getting-started-with-compute/#create-a-new-project)Create a new project

1. Rust
2. JavaScript
3. Go

To create a Compute application in Rust, follow the steps listed below for initializing a Compute application.

Type [fastly compute init](https://www.fastly.com/documentation/reference/cli/compute/init/) to scaffold a new Fastly Compute project. The CLI will generate source code for your project in the current working directory.

You will be asked to choose a language and then a starter kit to use as the starting point for your project. There are many [starter kits available](https://www.fastly.com/documentation/solutions/starters). If this is your first project, we recommend choosing the default starter for your chosen language.

`$ mkdir example && cd example$ fastly compute init`

Follow the prompts to configure your new project:

`Creating a new Fastly Compute project.Press ^C at any time to quit.✓ Validating directory permissionsName: [example]Description: My new Rust-based app!Author (email): jo.test@example.comLanguage:[1] Rust[2] JavaScript[3] Go[5] Other ('bring your own' Wasm binary)Choose option: [1] 1Starter kit:[1] Default starter for Rust    A basic starter kit that demonstrates routing, simple synthetic responses and    overriding caching rules.    https://github.com/fastly/compute-starter-kit-rust-default[2] Empty starter for Rust    An empty starter kit project template.    https://github.com/fastly/compute-starter-kit-rust-empty...Choose option or paste git URL: [1]`

At the prompts, provide details about the service you're creating:

* **Name**: Enter a name for your service. By default, the CLI uses the name of the current directory.
* **Description**: Optionally enter a short description for your service, or leave it blank.
* **Author**: Enter an email address or accept the default, which is the email associated with your API token.
* **Language**: Select the language you want to use to write your code.
* **Starter kit**: Choose from the available [starter kits](https://www.fastly.com/documentation/solutions/starters) or press enter to accept the default. You can also enter the URL of a GitHub repository to use a compatible template that's not in the list of starter kits.

A local development environment and a [fastly.toml](https://www.fastly.com/documentation/reference/compute/fastly-toml) package manifest will be generated based on your selections:

`✓ Fetching package template✓ Reading package manifest✓ Setting package name in manifest to "example"✓ Setting description in manifest✓ Setting authors in manifest to 'jo.example@example.com'✓ Setting language in manifest to 'rust'✓ Saving manifest changes✓ Initializing packageInitialized package example to:    /home/jo/repos/exampleTo publish the package (build and deploy), run:    fastly compute publishSUCCESS: Initialized package example`

**HINT:** See the [fastly compute init](https://www.fastly.com/documentation/reference/cli/compute/init/) command's reference page for full options (e.g., if you want to use a directory other than the current one).

### [](https://www.fastly.com/documentation/guides/compute/getting-started-with-compute/#compile-to-webassembly)Compile to WebAssembly

You already have a complete, functional Compute project at this point. A default starter kit will run fine without any code changes, but if you want to dive in to the code right now, check out the language-specific guides on [Rust](https://www.fastly.com/documentation/guides/compute/developer-guides/rust), [JavaScript](https://www.fastly.com/documentation/guides/compute/developer-guides/javascript) or [Go](https://www.fastly.com/documentation/guides/compute/developer-guides/go).

To run the Compute project on Fastly, it needs to be compiled into a WebAssembly module that can be packaged for Fastly use. The CLI runs the appropriate compiler for the language you're using by executing the `scripts.build` command defined in your project's [fastly.toml](https://www.fastly.com/documentation/reference/compute/fastly-toml) file, and generates the necessary WebAssembly binary.

**IMPORTANT:** The default [fastly.toml](https://www.fastly.com/documentation/reference/compute/fastly-toml) build command for JavaScript _assumes dependencies are already installed_. To make sure this is done, run the dependency manager of your choice to install the dependencies listed in `package.json`. For example, `npm` or `yarn`:

`$ npm install`

The compilers for Rust and Go automatically resolve and install dependencies, so those will usually be taken care of when you run `fastly compute build`.

Type [fastly compute build](https://www.fastly.com/documentation/reference/cli/compute/build/) when you're ready to build:

`$ fastly compute build✓ Verifying package manifest✓ Identifying package name✓ Identifying toolchain✓ Running [scripts.build]✓ Creating package archiveSUCCESS: Built package (pkg/<name>.tar.gz)`

### [](https://www.fastly.com/documentation/guides/compute/getting-started-with-compute/#deploy-to-a-fastly-service)Deploy to a Fastly service

To deploy the project to Fastly, run [fastly compute deploy](https://www.fastly.com/documentation/reference/cli/compute/deploy/).

**IMPORTANT:** Deploying your first Compute project will start a Compute free trial. While on a free trial, Compute services in your account are subject to [lower limits](https://www.fastly.com/documentation/guides/compute/getting-started-with-compute/#limitations-and-constraints) and cannot be used for production traffic. When you're ready to use your Compute service for production traffic, [contact our sales team](mailto:sales@fastly.com) or your Fastly account contact.

If you already have a Fastly service you want to deploy the package to you can add the service ID into the `service_id` property in [fastly.toml](https://www.fastly.com/documentation/reference/compute/fastly-toml) before running the deploy command; otherwise the CLI will lead you through creation of a service automatically.

`$ fastly compute deployThere is no Fastly service associated with this package. To connect to an existing serviceadd the Service ID to the fastly.toml file, otherwise follow the prompts to create aservice now.Create new service: [y/N] yService name: [example]✓ Creating serviceDomain: [random-funky-words.edgecompute.app]Backend (hostname or IP address, or leave blank to stop adding backends):✓ Creating domain 'random-funky-words.edgecompute.app'✓ Uploading package✓ Activating service (version 1)✓ Checking service availability (status: 200)Manage this service at:    https://manage.fastly.com/configure/services/PS1Z4isxPaoZGVKVdv0eYView this service at:    https://random-funky-words.edgecompute.appSUCCESS: Deployed package (service PS1Z4isxPaoZGVKVdv0eY, version 1)`

At the prompts, provide details about the service you're creating:

* **Domains**: Press enter to accept the [automatically generated domain name](https://www.fastly.com/documentation/guides/concepts/routing-traffic-to-fastly/#fastly-assigned-domains). We'll take care of the TLS and DNS and give you a working domain immediately. It's a good idea to accept the default now and add more domains to the service later.
* **Backends**: If you want to configure an origin server for your service, enter a valid hostname, or an IPv4 or IPv6 address. Alternatively, leave the prompt blank to create a service with no origin server. Such services cannot forward requests to your servers, but they can respond to client requests with a response composed within your Compute package.

The output includes a link to manage your service in the Fastly web interface. You can use this link to perform more complex configuration of the service, such as adding or removing domains, changing origin server settings, and setting up logging endpoints.

After the command completes, it may take up to a minute before the new service begins handling requests, and if you're replacing a previous version of the package, the earlier version may continue to handle requests for that period.

### [](https://www.fastly.com/documentation/guides/compute/getting-started-with-compute/#test-and-celebrate)Test and celebrate

Open a browser and head over to the domain that was assigned to the service, such as `random-funky-words.edgecompute.app`, and you should see a working site. If you used the default starter kit, it will look something like this:

![Image 4: Compute welcome content](https://www.fastly.com/documentation/static/38290a2158da09174eec51f99bec1143/success-precomposed.png)

### [](https://www.fastly.com/documentation/guides/compute/getting-started-with-compute/#add-your-own-domain)Add your own domain

Now that your working project is deployed, you may want to assign a domain name to it. We have a lot of [TLS options](https://www.fastly.com/documentation/guides/concepts/routing-traffic-to-fastly). As a starting point, it's a good idea to create a **TLS Subscription** so that Fastly will generate a certificate for you.

* [Setting up a custom domain with a TLS subscription](https://www.fastly.com/documentation/guides/concepts/#setting-up-a-domain).

[](https://www.fastly.com/documentation/guides/compute/getting-started-with-compute/#go-further)Go further
----------------------------------------------------------------------------------------------------------

If you would like to **learn** more about how the Compute platform integrates with your preferred language, read our getting started guides for each of our officially supported languages:

* [Using Rust](https://www.fastly.com/documentation/guides/compute/developer-guides/rust)
* [Using JavaScript](https://www.fastly.com/documentation/guides/compute/developer-guides/javascript)
* [Using Go](https://www.fastly.com/documentation/guides/compute/developer-guides/go)

If you are already familiar with [VCL](https://www.fastly.com/documentation/guides/full-site-delivery/fastly-vcl) and want to **migrate** an existing VCL service to the Compute platform, try the [VCL to Compute migration guide](https://www.fastly.com/documentation/guides/compute/developer-guides/migrate), which shows examples of the most common use cases in VCL and how to implement the same functionality using the Compute platform's supported languages.

Or maybe you have an idea in mind and want to **experiment** with examples? Try cloning a [starter kit](https://www.fastly.com/documentation/solutions/starters), copy and pasting code from our [code examples](https://www.fastly.com/documentation/solutions/examples), or following a [tutorial](https://www.fastly.com/documentation/solutions/tutorials).

[](https://www.fastly.com/documentation/guides/compute/getting-started-with-compute/#limitations-and-constraints)Limitations and constraints
--------------------------------------------------------------------------------------------------------------------------------------------

Compute services accept client connections on port 443 only. This is different from VCL services, which support client connections on port 80.

**HINT:** If your Compute service receives a request on port 80, Fastly automatically returns a `308` ("Permanent Redirect") response status with the `Location` header indicating the HTTPS version of the same URL in a `Location` header.

The following default limits apply to Compute services. If you need to exceed any other limits, please speak to your Fastly contact or contact [Fastly support](https://support.fastly.com/):

| Item | Limit | Scope |
| --- | --- | --- |
| Maximum compiled package size | 100MB | per service |
| Maximum cached object size | 100MB | per object |
| Maximum CPU time available to a single request instance | 50ms | per execution |
| Maximum runtime for a single request instance | 2 min (60s for [free trials](https://www.fastly.com/documentation/guides/account-info/billing/account-types)) | per execution |
| Maximum memory consumption | 1M bytes stack, 128MB heap | per execution |
| Maximum number of dictionary lookups | 32 | per execution |
| Maximum number of backend requests | 32 (10 for [free trials](https://www.fastly.com/documentation/guides/account-info/billing/account-types)) | per execution |
| Maximum length of a header name | 8192 bytes | per header |
| Maximum length of a header value | 8192 bytes | per header |
| Maximum length of a method name | 8192 bytes | per request |
| Maximum length of a URL | 8192 bytes | per request |

An 'execution' refers to a single instance of a Compute program being executed, normally in response to a client HTTP request. Separate limits also apply to the use of [log tailing](https://www.fastly.com/documentation/guides/compute/developer-guides/testing/#live-log-monitoring-in-your-console) with Compute services.

**IMPORTANT:** Compute services are also affected by limits that apply to products or platform services that you access through your application code. Refer to their own documentation for information on how those limits might interact with your application:

* [Fastly cache](https://www.fastly.com/documentation/guides/concepts/cache/#limitations-and-constraints)
* [Service chaining](https://www.fastly.com/documentation/guides/concepts/service-chaining/#loop-detection)
