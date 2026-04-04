---
---
title: WebWorker
description: "Connect Web Workers with the SDK running on the main thread"
---

_Import name: `Sentry.webWorkerIntegration`_

This integration, together with `Sentry.registerWebWorker()`, establishes communication between the browser's main thread and one or more [WebWorkers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API).
It listens to worker messages from the passed workers and forwards them to the main thread. 

Read our Web Worker Guide for more information. 

This integration listens to a message sent from the worker when it calls `Sentry.registerWebWorker({ self })`.
The purpose is to sync source map information (debugIds) between the main thread and the worker so that worker
errors caught by the main thread SDK are properly mapped to the worker's source code.

## Options

### `worker`

_Type: `Worker | Array`_

The web worker(s) to listen to. Every worker must call `Sentry.registerWebWorker({ self })` to register itself with the SDK.

## Methods

### `addWorker(worker: Worker)`

Adds a worker to the integration, after the integraion was already initialized and added to the SDK.
This is useful if you have workers that are initialized at later point in your application's lifecycle.
Note that every worker must call `Sentry.registerWebWorker({ self })` to register itself with the SDK.
