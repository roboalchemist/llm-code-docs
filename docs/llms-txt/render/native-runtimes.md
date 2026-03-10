# Source: https://render.com/docs/native-runtimes.md

# Native Runtimes

Render services provide *native runtimes* that enable you to build and deploy your application using common language environments.

Render's native runtimes include:

- Automated builds and deploys for supported languages in both public and private Git repositories
- [Infrastructure as Code](infrastructure-as-code) support with [`render.yaml`](blueprint-spec)
- Regular updates to native runtimes to improve functionality, security, and performance

All native runtimes come with standard Render features like:

- [Private networking](private-services), load balancing, and service discovery
- [Persistent block storage](disks)
- Automatic [Brotli](https://en.wikipedia.org/wiki/Brotli) and [gzip](https://en.wikipedia.org/wiki/Gzip) compression for faster responses
- Easy HTTP [health checks](/deploys#health-checks) and [zero-downtime deploys](/deploys#zero-downtime-deploys).
- Automatic [pull request previews](service-previews)
- Native HTTP/2 support
- [DDoS protection](ddos-protection)
- Automatic HTTP → HTTPS redirects

## Available Runtimes

Render provides native runtimes for Node.js / Bun, Python, Ruby, Go, Rust, and Elixir.

For details, see [Supported Languages](language-support).

### Changing a service's runtime

If you've recently created a service with an incorrect runtime, the fastest fix is usually to create a _new_ service with the correct runtime.

You can also change an existing service's runtime in any of the following ways:

- Make an HTTP call to the Render API's [Update service](https://api-docs.render.com/reference/update-service) endpoint.
  - Specify a new `runtime` via the `serviceDetails` parameter you provide in your request.
- If you're managing your service with [Render Blueprints](infrastructure-as-code), update the service's `runtime` field in your `render.yaml` file, then sync your Blueprint.

## Tools and utilities

The tools and utilities listed below are available for native builds and deploys.

If your build requires a tool that _isn't_ listed below, you can [deploy with Docker](docker) instead of building natively.

### Builds

- bun
- curl
- ffmpeg
- g++
- gcc
- gettext
- git
- gnupg2
- jq
- libvips-dev
- libvips-tools
- make
- nano
- node
- npm
- pandoc
- pigz
- pnpm
- postgresql-client
- princexml
- python3-dev
- python3-pip
- python3-setuptools
- rsync
- sqlite3
- swig
- typescript
- unzip
- vim
- webpack
- wget
- yarn
- zip

### Deploys

- bun
- curl
- ffmpeg
- g++
- gcc
- gettext
- ghostscript
- git
- gnupg2
- imagemagick
- jq
- libvips-dev
- libvips-tools
- make
- nano
- node
- npm
- pandoc
- pigz
- pnpm
- postgresql-client
- postgresql-client-12
- postgresql-client-13
- postgresql-client-14
- princexml
- python3-dev
- python3-pip
- python3-setuptools
- rsync
- sqlite3
- swig
- typescript
- unzip
- vim
- webpack
- wget
- yarn
- zip