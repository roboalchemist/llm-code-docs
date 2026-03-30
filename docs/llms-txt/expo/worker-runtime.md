# Source: https://docs.expo.dev/eas/hosting/reference/worker-runtime

---
modificationDate: October 22, 2025
title: EAS Hosting worker runtime
description: Learn about EAS Hosting worker runtime and Node.js compatibility.
---

# EAS Hosting worker runtime

Learn about EAS Hosting worker runtime and Node.js compatibility.

EAS Hosting is built on [Cloudflare Workers](https://developers.cloudflare.com/workers/), a modern and powerful platform for serverless APIs that's been built for seamless scalability, high reliability, and exceptional performance globally.

The Cloudflare Workers runtime runs on the V8 JavaScript engine, the same powering JavaScript in Node.js and Chromium. However, its runtime has a few key differences from what you might be used to in traditional serverless Node.js deployments.

Instead of each request running in a full JavaScript process, Workers are designed to run them in small V8 isolates, a feature of the V8 runtime. Think of them as micro-containers in a single JavaScript process.

For more information on how Workers work, see [Cloudflare Workers](https://developers.cloudflare.com/workers/reference/how-workers-works/) documentation.

## Node.js compatibility

Cloudflare is part of [Winter TC](https://wintertc.org/), is more similar to the JavaScript environments in browsers and service workers rather than in Node.js. Restrictions like these provide a leaner runtime than Node.js, which is still familiar. This common runtime is a minimal standard supported by many JavaScript runtime these days.

This means, many Node.js APIs that you might be used to or some dependencies you utilize, aren't directly available in the EAS Hosting runtime. To ease this transition, as not all dependencies will have first-class support for Web APIs yet, Node.js compatibility modules exist and can be used in your API routes.

| Node.js built-in module | Supported | Implementation notes |
| --- | --- | --- |
| `node:assert` | ✓ |  |
| `node:async_hooks` | ✓ |  |
| `node:buffer` | ✓ |  |
| `node:crypto` | ✓ | Select deprecated algorithms are not available |
| `node:console` |  | Provided as partially functional JS shims |
| `node:constants` | ✓ |  |
| `node:diagnostics_channel` | ✓ | Select deprecated algorithms are not implemented |
| `node:dns` | ✓ | `Resolver` is unimplemented, all DNS requests are sent to Cloudflare |
| `node:events` | ✓ |  |
| `node:fs` | ✓ | Supported, with in-memory filesystem |
| `node:http` | ✓ | Supported, except for server functionality |
| `node:http2` |  | Partially supported. Server functionality unsupported |
| `node:https` | ✓ | Supported, except for server functionality |
| `node:module` |  | `SourceMap` is unimplemented, partially supported otherwise |
| `node:net` |  | `Server` and `BlockList` are unimplemented, client sockets are partially supported |
| `node:os` | ✓ | Provided as JS stubs that provide mock values matching Node.js on Linux |
| `node:path` | ✓ |  |
| `node:path/posix` | ✓ |  |
| `node:path/win32` | ✓ |  |
| `node:process` | ✓ | Provided as JS stubs |
| `node:punycode` | ✗ |  |
| `node:querystring` | ✓ |  |
| `node:readline` | ✗ | Provided as non-functional JS stubs, since workers have no `stdin` |
| `node:stream` | ✓ |  |
| `node:stream/consumers` | ✓ |  |
| `node:stream/web` | ✓ |  |
| `node:string_decoder` | ✓ |  |
| `node:test` | ✓ |  |
| `node:timers` | ✓ |  |
| `node:tls` | ✓ | Supported, except for server functionality |
| `node:trace_events` |  | Provided as non-functional JS stubs |
| `node:tty` | ✓ | Provided as JS shims redirecting output to the Console API |
| `node:url` | ✓ |  |
| `node:util` | ✓ |  |
| `node:util/types` | ✓ |  |
| `node:worker_threads` | ✗ | Provided as non-functional JS stubs, since workers don't support threading |
| `node:zlib` | ✓ |  |

These modules generally provide a lower-accuracy polyfill or approximation of their Node.js counterparts. For example, the `fs`, `http`, and `https` modules have additional restrictions in place and are Node.js compatibility layers, which aren't equivalent to running them in a Node.js process.

Any of the above listed Node.js modules can be used in API routes or dependencies of your API routes as usual and will use appropriate compatibility modules. However, some of these modules may not provide any practical functionality and only exist to shim APIs to prevent runtime crashes.

Any modules that aren't mentioned here are unavailable or unsupported, and your code and none of your dependencies should rely on them being provided.

> More Node.js compatibility shims may be added in the future, but all Node.js APIs that are not documented in this non-exhaustive list are not expected to work.

## Globals

| JavaScript runtime globals | Supported | Implementation notes |
| --- | --- | --- |
| `origin` | ✓ | Will always be the same as the incoming request's `Origin` header |
| `process` | ✓ |  |
| `process.env` | ✓ | Populated with EAS Hosting environment variables |
| `process.stdout` | ✓ | Will redirect output to the Console API (`console.log`) for logging |
| `process.stderr` | ✓ | Will redirect output to the Console API (`console.error`) for logging |
| `setImmediate` | ✓ |  |
| `clearImmediate` | ✓ |  |
| `Buffer` | ✓ | Set to `Buffer` from `node:buffer` |
| `EventEmitter` | ✓ | Set to `EventEmitter` from `node:events` |
| `global` | ✓ | Set to `globalThis` |
| `WeakRef` | ✓ |  |
| `FinalizationRegistry` | ✓ |  |
| `require` |  | External requires are supported but limited to deployed JS files and built-in modules. Node module resolution is unsupported. |
| `require.cache` | ✗ |  |
