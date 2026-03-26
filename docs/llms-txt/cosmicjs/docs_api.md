# Source: https://www.cosmicjs.com/docs/api/index.md

# API Reference

We offer a powerful REST API to interact with your Cosmic content. We recommend using one of the available SDKs which provide an enhanced development experience.

## API base URL

The base URL for all requests is noted below.
```bash {{ language: 'js' }}
http://api.cosmicjs.com

```
## API status

You can check the API status at the following endpoint. You can also subscribe to status updates on the [Cosmic status page](http://cosmicstatus.com).
```bash {{ language: 'js' }}
http://api.cosmicjs.com/v3/status

```
{/*  */}

## Install the JavaScript SDK

The following examples include methods using the [Cosmic JavaScript SDK](https://www.npmjs.com/package/@cosmicjs/sdk). To run the examples, first install the NPM module using one of the following commands. Make sure you have [Node.js](https://nodejs.org/en) installed on your machine (recomended version: `v18.*`).
```bash {{ language: 'js' }}
yarn add @cosmicjs/sdk
# OR
pnpm add @cosmicjs/sdk
# OR
npm install @cosmicjs/sdk
# OR
bun add @cosmicjs/sdk

```
## Install the Swift SDK

In certain cases, there are also methods that use the [Cosmic Swift SDK](https://github.com/cosmicjs/cosmic-sdk-swift). To run the examples, first install the Swift package using Swift Package Manager.
```bash {{ language: 'swift' }}
.package(url: "https://github.com/cosmicjs/cosmic-sdk-swift.git", from: "1.0.0")

```