# Bull Documentation

Source: https://docs.bullmq.io/llms-full.txt

---

# What is BullMQ

General description of BullMQ and its features

BullMQ is a [Node.js](https://nodejs.org) library that implements a fast and robust queue system built on top of [Redis](https://redis.io) that helps in resolving many modern age micro-services architectures.

The library is designed so that it will fulfill the following goals:

* Exactly once queue semantics, i.e., attempts to deliver every message exactly one time, but it will deliver at least once in the worst case scenario\*.
* Easy to scale horizontally. Add more workers for processing jobs in parallel.
* Consistent.
* High performant. Try to get the highest possible throughput from Redis by combining efficient .lua scripts and pipelining.

View the repository, see open issues, and contribute back [on GitHub](https://github.com/taskforcesh/bullmq)!

## **Features**

If you are new to Message Queues, you may wonder why they are needed after all. Queues can solve many different problems in an elegant way, from smoothing out processing peaks to creating robust communication channels between micro-services or offloading heavy work from one server to many smaller workers, and many other use cases. Check the [Patterns](https://docs.bullmq.io/patterns/adding-bulks) section for getting some inspiration and information about best practices.

* [x] **Minimal CPU usage due to a polling-free design**
* [x] **Distributed job execution based on Redis**
* [x] **LIFO and FIFO jobs**
* [x] **Priorities**
* [x] **Delayed jobs**
* [x] **Scheduled and repeatable jobs according to cron specifications**
* [x] **Retries of failed jobs**
* [x] **Concurrency setting per worker**
* [x] **Threaded (sandboxed) processing functions**
* [x] **Automatic recovery from process crashes**
* [x] **Parent-Child dependencies**

### Used by

BullMQ is used by many organizations big and small, here are some notable examples:

![](https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-7eabf625a2932b111c2a5b7a651e2eaae6ad1b7a%2Fclipart1565701.png?alt=media)

![](https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-7ffcd73605e901be045c7cf43cb61eb9a7a00ee4%2Fwordmark-logo.png?alt=media)

![](https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-33c0c65bd9d6936b8ac33f4be7cbba2814b83ead%2Fdatawrapper-logo.png?alt=media)

![](https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-2038c9549e2aa39e1e8ce1a1017074c98953a7f4%2Fcurri-small.png?alt=media)


# Quick Start

This is a basic guide to get your first queue working.

## Install

Install using npm:

```
$ npm install bullmq
```

Install using yarn:

```
$ yarn add bullmq
```

{% hint style="info" %}
BullMQ is written in TypeScript, and although it can be used in vanilla JavaScript, all examples in this guide will be written in TypeScript.
{% endhint %}

Import into your project and add some jobs:

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('foo');

async function addJobs() {
  await myQueue.add('myJobName', { foo: 'bar' });
  await myQueue.add('myJobName', { qux: 'baz' });
}

await addJobs();
```

{% hint style="danger" %}
You need to have a Redis service running in your local computer to run these examples successfully. You can read more about Redis connections [here](https://docs.bullmq.io/guide/connections).
{% endhint %}

Jobs are added to the queue and can be processed at any time, with at least one Node.js process running a worker:

```typescript
import { Worker } from 'bullmq';
import IORedis from 'ioredis';

const connection = new IORedis({ maxRetriesPerRequest: null });

const worker = new Worker(
  'foo',
  async job => {
    // Will print { foo: 'bar'} for the first job
    // and { qux: 'baz' } for the second.
    console.log(job.data);
  },
  { connection },
);
```

{% hint style="info" %}
You can have as many worker processes as you want, BullMQ will distribute the jobs across your workers in a round robin fashion.
{% endhint %}

You can listen to completed (or failed) jobs by attaching listeners to the workers:

```typescript
worker.on('completed', job => {
  console.log(`${job.id} has completed!`);
});

worker.on('failed', (job, err) => {
  console.log(`${job.id} has failed with ${err.message}`);
});
```

{% hint style="info" %}
There are many other events available, check the [Guide](https://github.com/taskforcesh/bullmq/blob/master/docs/gitbook/guide/events.md) or the [API reference](https://api.docs.bullmq.io/) for more information.
{% endhint %}

Sometimes you need to listen to all the workers events in a given place, for this you need to use a special class [`QueueEvents`](https://api.docs.bullmq.io/classes/v5.QueueEvents.html):

```typescript
import { QueueEvents } from 'bullmq';

const queueEvents = new QueueEvents("my-queue-name");

queueEvents.on('waiting', ({ jobId }) => {
  console.log(`A job with ID ${jobId} is waiting`);
});

queueEvents.on('active', ({ jobId, prev }) => {
  console.log(`Job ${jobId} is now active; previous status was ${prev}`);
});

queueEvents.on('completed', ({ jobId, returnvalue }) => {
  console.log(`${jobId} has completed and returned ${returnvalue}`);
});

queueEvents.on('failed', ({ jobId, failedReason }) => {
  console.log(`${jobId} has failed with reason ${failedReason}`);
});
```

You may also access the timestamp of the event, which looks like "1580456039332-0".

```typescript
import { QueueEvents } from 'bullmq';

const queueEvents = new QueueEvents("my-queue-name");

queueEvents.on('progress', ({ jobId, data }, timestamp) => {
  console.log(`${jobId} reported progress ${data} at ${timestamp}`);
});
```

{% hint style="danger" %}
For performance reasons, the events emitted by a `QueueEvents` instance do not contain the `Job` instance, only the `jobId`. Use the [`Job.fromId`](https://api.docs.bullmq.io/classes/v5.Job.html#fromid) method if you need the `Job` instance.
{% endhint %}


# Changelogs

## [5.71.0](https://github.com/taskforcesh/bullmq/compare/v5.70.4...v5.71.0) (2026-03-11)

#### Features

* **otel:** support gauge metric when counting jobs by state ([#3811](https://github.com/taskforcesh/bullmq/issues/3811)) ([1283ac7](https://github.com/taskforcesh/bullmq/commit/1283ac716b0551bd7e3248a5c3e8f8d804310c33))

### [5.70.4](https://github.com/taskforcesh/bullmq/compare/v5.70.3...v5.70.4) (2026-03-06)

#### Bug Fixes

* **flow:** allow deduplication from root parent (python) (elixir) ([#3817](https://github.com/taskforcesh/bullmq/issues/3817)) fixes [#3761](https://github.com/taskforcesh/bullmq/issues/3761) ([6cd60a7](https://github.com/taskforcesh/bullmq/commit/6cd60a79249a665270cf0723f43eb98f773f4b83))

### [5.70.3](https://github.com/taskforcesh/bullmq/compare/v5.70.2...v5.70.3) (2026-03-06)

#### Bug Fixes

* **otel:** use job timestamps for process span attributes ([#3832](https://github.com/taskforcesh/bullmq/issues/3832)) ([450253c](https://github.com/taskforcesh/bullmq/commit/450253c3457f500d7f4e5aeebaa4ddfc937a1f39))

### [5.70.2](https://github.com/taskforcesh/bullmq/compare/v5.70.1...v5.70.2) (2026-03-05)

#### Bug Fixes

* **auto-remove:** remove orphaned jobs when auto-remove is enabled ([#3853](https://github.com/taskforcesh/bullmq/issues/3853)) ([504b536](https://github.com/taskforcesh/bullmq/commit/504b53689a29b3b4ddc902d25211a92da6a4d7af))

### [5.70.1](https://github.com/taskforcesh/bullmq/compare/v5.70.0...v5.70.1) (2026-02-23)

#### Bug Fixes

* **deps:** update dependency ioredis to v5.9.3 ([#3821](https://github.com/taskforcesh/bullmq/issues/3821)) fixes [#3793](https://github.com/taskforcesh/bullmq/issues/3793) ([0fafcc0](https://github.com/taskforcesh/bullmq/commit/0fafcc0950698f6a8a55a2b77ef1b82af5d5712f))

## [5.70.0](https://github.com/taskforcesh/bullmq/compare/v5.69.4...v5.70.0) (2026-02-21)

#### Features

* **worker:** add cancelation support to sandboxed processors ([#3806](https://github.com/taskforcesh/bullmq/issues/3806)) ([0d3879b](https://github.com/taskforcesh/bullmq/commit/0d3879b02ec9738d90213e1a479d53359f3a71aa))

### [5.69.4](https://github.com/taskforcesh/bullmq/compare/v5.69.3...v5.69.4) (2026-02-21)

#### Bug Fixes

* **sandbox:** ensure non-bullmq messages are ignored ([#3704](https://github.com/taskforcesh/bullmq/issues/3704)) fixes [#3703](https://github.com/taskforcesh/bullmq/issues/3703) ([9c72258](https://github.com/taskforcesh/bullmq/commit/9c722585bd9873561fae3f32971d65cf00a7d092))

### [5.69.3](https://github.com/taskforcesh/bullmq/compare/v5.69.2...v5.69.3) (2026-02-16)

#### Bug Fixes

* **job-scheduler:** handle empty scheduler hash fallback ([#3797](https://github.com/taskforcesh/bullmq/issues/3797)) fixes [#3796](https://github.com/taskforcesh/bullmq/issues/3796) ([87386ca](https://github.com/taskforcesh/bullmq/commit/87386ca88e29755fc68e6cc8fcfebfb7f8f8237f))

### [5.69.2](https://github.com/taskforcesh/bullmq/compare/v5.69.1...v5.69.2) (2026-02-14)

#### Bug Fixes

* **queue:** forward error from repeat or job-scheduler instances ([#3775](https://github.com/taskforcesh/bullmq/issues/3775)) fixes [#3774](https://github.com/taskforcesh/bullmq/issues/3774) ([a62241f](https://github.com/taskforcesh/bullmq/commit/a62241f5831a1d3bb6c328a9037ea852be7832cd))

### [5.69.1](https://github.com/taskforcesh/bullmq/compare/v5.69.0...v5.69.1) (2026-02-13)

#### Bug Fixes

* **utils:** use exact import of DatabaseType ([#3786](https://github.com/taskforcesh/bullmq/issues/3786)) ([d249301](https://github.com/taskforcesh/bullmq/commit/d249301ddc9afc607c9e86a8a44312af682e6be0))

## [5.69.0](https://github.com/taskforcesh/bullmq/compare/v5.68.0...v5.69.0) (2026-02-12)

#### Features

* **otel:** enable metrics ([#3769](https://github.com/taskforcesh/bullmq/issues/3769)) ([f85e870](https://github.com/taskforcesh/bullmq/commit/f85e87032a822826cbeed19eedff7ccb1e6ce085))

## [5.68.0](https://github.com/taskforcesh/bullmq/compare/v5.67.3...v5.68.0) (2026-02-11)

#### Features

* **connection:** add datatype for version differentiation ([#3746](https://github.com/taskforcesh/bullmq/issues/3746)) ([af9197d](https://github.com/taskforcesh/bullmq/commit/af9197d16941d49c9e3d86f10d96681beea676bc))

### [5.67.3](https://github.com/taskforcesh/bullmq/compare/v5.67.2...v5.67.3) (2026-02-05)

#### Bug Fixes

* **connection:** merge redisOptions when duplicating cluster ([#3759](https://github.com/taskforcesh/bullmq/issues/3759)) ([afb878f](https://github.com/taskforcesh/bullmq/commit/afb878f97ebeaf89c1308b7dde0b5a440381d113))

### [5.67.2](https://github.com/taskforcesh/bullmq/compare/v5.67.1...v5.67.2) (2026-01-28)

#### Bug Fixes

* **deps:** use caret versioning for ioredis dependency ([#3719](https://github.com/taskforcesh/bullmq/issues/3719)) fixes [#3718](https://github.com/taskforcesh/bullmq/issues/3718) ([de0fca8](https://github.com/taskforcesh/bullmq/commit/de0fca894f47d8aa2b2c66ca9475e526ca477508))

### [5.67.1](https://github.com/taskforcesh/bullmq/compare/v5.67.0...v5.67.1) (2026-01-24)

#### Bug Fixes

* fix worker connection name on cluster [#3340](https://github.com/taskforcesh/bullmq/issues/3340) (elixir) (python) ([#3660](https://github.com/taskforcesh/bullmq/issues/3660)) ([fa22e84](https://github.com/taskforcesh/bullmq/commit/fa22e844d29961db95df58f2ae63b440d71c11f6))

## [5.67.0](https://github.com/taskforcesh/bullmq/compare/v5.66.7...v5.67.0) (2026-01-24)

#### Features

* **job:** add job name and id as telemetry attributes in complete, retry, delay and failed spans ([#3707](https://github.com/taskforcesh/bullmq/issues/3707)) ref [#3692](https://github.com/taskforcesh/bullmq/issues/3692) ([6294b36](https://github.com/taskforcesh/bullmq/commit/6294b36f775c20f7d43387d9bde3185629e88df4))

### [5.66.7](https://github.com/taskforcesh/bullmq/compare/v5.66.6...v5.66.7) (2026-01-23)

#### Bug Fixes

* **deps:** update dependency ioredis to v5.9.2 ([#3713](https://github.com/taskforcesh/bullmq/issues/3713)) ([87e74b5](https://github.com/taskforcesh/bullmq/commit/87e74b5713b5017c29789094d6ac6ff26bfe79c1))

### [5.66.6](https://github.com/taskforcesh/bullmq/compare/v5.66.5...v5.66.6) (2026-01-22)

#### Performance Improvements

* **job:** apply limit when removing jobs by max age (python) (elixir) ([#3694](https://github.com/taskforcesh/bullmq/issues/3694)) fixes [#3672](https://github.com/taskforcesh/bullmq/issues/3672) ([a8fc316](https://github.com/taskforcesh/bullmq/commit/a8fc316c0989bd3edb54577ceb02bff0c600aa93))

### [5.66.5](https://github.com/taskforcesh/bullmq/compare/v5.66.4...v5.66.5) (2026-01-12)

#### Bug Fixes

* **deps:** update dependency ioredis to v5.9.1 ([#3676](https://github.com/taskforcesh/bullmq/issues/3676)) fixes [#3667](https://github.com/taskforcesh/bullmq/issues/3667) ([661c581](https://github.com/taskforcesh/bullmq/commit/661c581270186bc405967b91326daff061370d03))

### [5.66.4](https://github.com/taskforcesh/bullmq/compare/v5.66.3...v5.66.4) (2025-12-27)

#### Bug Fixes

* **flow:** remove debounce option from flow producer ([#3646](https://github.com/taskforcesh/bullmq/issues/3646)) ([cc74805](https://github.com/taskforcesh/bullmq/commit/cc74805d5eda14ed684e2111c91de8890e752768))

### [5.66.3](https://github.com/taskforcesh/bullmq/compare/v5.66.2...v5.66.3) (2025-12-26)

#### Bug Fixes

* **flow:** remove deduplication option from flow producer ([#3637](https://github.com/taskforcesh/bullmq/issues/3637)) ([f60c172](https://github.com/taskforcesh/bullmq/commit/f60c172725ab29c0159b804ae0b9d691105689c4))

### [5.66.2](https://github.com/taskforcesh/bullmq/compare/v5.66.1...v5.66.2) (2025-12-19)

#### Bug Fixes

* **telemetry:** send most updated attemptsMade value when finishing ([#3623](https://github.com/taskforcesh/bullmq/issues/3623)) ([1380a16](https://github.com/taskforcesh/bullmq/commit/1380a16fa45c70f0bc5b938efdf178b33a19cac1))

### [5.66.1](https://github.com/taskforcesh/bullmq/compare/v5.66.0...v5.66.1) (2025-12-17)

#### Bug Fixes

* **deps:** pin dependencies ([#3609](https://github.com/taskforcesh/bullmq/issues/3609)) ([5fbf778](https://github.com/taskforcesh/bullmq/commit/5fbf778f0b8f58b90e82f9020c041f3248b0b269))

## [5.66.0](https://github.com/taskforcesh/bullmq/compare/v5.65.1...v5.66.0) (2025-12-11)

#### Features

* **job:** allow resetting attemptsMade and attemptsStarted attributes on retry ([#3596](https://github.com/taskforcesh/bullmq/issues/3596)) ref [#2152](https://github.com/taskforcesh/bullmq/issues/2152) ([241d847](https://github.com/taskforcesh/bullmq/commit/241d847fbc798d957bf25ccfaa5c9ec96928a4ae))

### [5.65.1](https://github.com/taskforcesh/bullmq/compare/v5.65.0...v5.65.1) (2025-12-01)

#### Bug Fixes

* **stalled:** prevent lock errors while job is not longer in active state ([#3579](https://github.com/taskforcesh/bullmq/issues/3579)) ([a8b9d76](https://github.com/taskforcesh/bullmq/commit/a8b9d76496afa5e913f823cf8c68eb428f6dd757))

## [5.65.0](https://github.com/taskforcesh/bullmq/compare/v5.64.1...v5.65.0) (2025-11-26)

#### Features

* **job:** support removeDeduplicationKey method ([#3575](https://github.com/taskforcesh/bullmq/issues/3575)) ([b059cfc](https://github.com/taskforcesh/bullmq/commit/b059cfcba48524446a62fd29785142c3d1edc30d))

### [5.64.1](https://github.com/taskforcesh/bullmq/compare/v5.64.0...v5.64.1) (2025-11-21)

#### Performance Improvements

* **worker:** promote delayed jobs while queue is rate limited ([#3561](https://github.com/taskforcesh/bullmq/issues/3561)) ([a474801](https://github.com/taskforcesh/bullmq/commit/a47480111a2f1238a57ea9bfbab44f7de958227f))

## [5.64.0](https://github.com/taskforcesh/bullmq/compare/v5.63.2...v5.64.0) (2025-11-20)

#### Features

* **worker:** add job cancellation ([#3564](https://github.com/taskforcesh/bullmq/issues/3564)) ([f41f5d0](https://github.com/taskforcesh/bullmq/commit/f41f5d0c64afe7707ad8c23a86cb9228c4d45671))

### [5.63.2](https://github.com/taskforcesh/bullmq/compare/v5.63.1...v5.63.2) (2025-11-15)

#### Bug Fixes

* **connection:** consider error code when checking connection error ([#3537](https://github.com/taskforcesh/bullmq/issues/3537)) ([045f3e7](https://github.com/taskforcesh/bullmq/commit/045f3e7a5d8edb85e1adbe82eb9e20ef33ad491b))

### [5.63.1](https://github.com/taskforcesh/bullmq/compare/v5.63.0...v5.63.1) (2025-11-13)

#### Bug Fixes

* **job-scheduler:** changing every in upsert resets the iterations ([#3551](https://github.com/taskforcesh/bullmq/issues/3551)) ([b4c7c65](https://github.com/taskforcesh/bullmq/commit/b4c7c6579b430b53d135b7a21d20d01d14c1814e))

## [5.63.0](https://github.com/taskforcesh/bullmq/compare/v5.62.2...v5.63.0) (2025-10-31)

#### Bug Fixes

* **queue:** emit progress event when calling updateJobProgress ([#3528](https://github.com/taskforcesh/bullmq/issues/3528)) ([c82df83](https://github.com/taskforcesh/bullmq/commit/c82df834dc83b3cf889b6a1aba9d18ec8b5eaf70))

#### Features

* **queue:** support getMeta method ([#3513](https://github.com/taskforcesh/bullmq/issues/3513)) ([e212d1c](https://github.com/taskforcesh/bullmq/commit/e212d1c8f0945dbff2d95309afe1376366910482))

### [5.62.2](https://github.com/taskforcesh/bullmq/compare/v5.62.1...v5.62.2) (2025-10-30)

#### Bug Fixes

* upsertJobScheduler does not apply change on existing scheduled job ([#3524](https://github.com/taskforcesh/bullmq/issues/3524)) ([98f73b3](https://github.com/taskforcesh/bullmq/commit/98f73b3f33aa79cdd67d0c4090cc86a8e4cfeb4c)), closes [#3500](https://github.com/taskforcesh/bullmq/issues/3500)

### [5.62.1](https://github.com/taskforcesh/bullmq/compare/v5.62.0...v5.62.1) (2025-10-30)

#### Performance Improvements

* **worker:** call moveToActive after special errors ([#3497](https://github.com/taskforcesh/bullmq/issues/3497)) ([37e9db5](https://github.com/taskforcesh/bullmq/commit/37e9db52a67b4e120139c1d2620cc0f73a08c006))

## [5.62.0](https://github.com/taskforcesh/bullmq/compare/v5.61.2...v5.62.0) (2025-10-28)

#### Features

* **queue:** support getGlobalRateLimit method ([#3511](https://github.com/taskforcesh/bullmq/issues/3511)) ([6a31e0a](https://github.com/taskforcesh/bullmq/commit/6a31e0aeab1311d7d089811ede7e11a98b6dd408))

### [5.61.2](https://github.com/taskforcesh/bullmq/compare/v5.61.0...v5.61.2) (2025-10-23)

#### Bug Fixes

* **worker:** only emit error when moveToActive failed ([0aa7cc5](https://github.com/taskforcesh/bullmq/commit/0aa7cc57db27a4e7b9fe3c5f52600abba749b053))
* **queue:** emit removed event when calling remove method ([#3492](https://github.com/taskforcesh/bullmq/issues/3492)) fixes [#2668](https://github.com/taskforcesh/bullmq/issues/2668) ([7a3f2fa1](https://github.com/taskforcesh/bullmq/commit/7a3f2fa131e20de80c45877a1018e1ccdf8a6506))
* **worker:** emit error once when failure happens in moveToFinished ([#3498](https://github.com/taskforcesh/bullmq/issues/3498)) ([4b4bd97e](https://github.com/taskforcesh/bullmq/commit/4b4bd97ee78af861121e2ccb90f210e4a74fbd26))

### [5.61.0](https://github.com/taskforcesh/bullmq/compare/v5.60.0...v5.61.0) (2025-10-06)

#### Features

* **queue:** add removeGlobalRateLimit method ([#3481](https://github.com/taskforcesh/bullmq/issues/3481)) ([d3fff80](https://github.com/taskforcesh/bullmq/commit/d3fff80f7135251db65e22cba8852a5584030cb1))

#### Bug Fixes

* **worker:** do not retry processor when connection errors happen ([#3482](https://github.com/taskforcesh/bullmq/issues/3482)) ([f1573b3](https://github.com/taskforcesh/bullmq/commit/f1573b3023807aab9a68ea6b2ce16a58afe4402b))

### [5.60.0](https://github.com/taskforcesh/bullmq/compare/v5.59.0...v5.60.0) (2025-10-03)

#### Features

* **queue:** support global rate limit ([#3468](https://github.com/taskforcesh/bullmq/issues/3468)) ref [#3019](https://github.com/taskforcesh/bullmq/issues/3019) ([bef57a0](https://github.com/taskforcesh/bullmq/commit/bef57a0e252a5d8bd0bf319d0bca3b1ad0e6519f))

### [5.59.0](https://github.com/taskforcesh/bullmq/compare/v5.58.9...v5.59.0) (2025-09-29)

#### Features

* **deduplication:** support replace option in single mode ([#3472](https://github.com/taskforcesh/bullmq/issues/3472)) ([eea35b7](https://github.com/taskforcesh/bullmq/commit/eea35b763c0965e129cf0ef4a104d05aa1f65f74))
* **sandbox:** support mjs files ([#3476](https://github.com/taskforcesh/bullmq/issues/3476)) ref [#3474](https://github.com/taskforcesh/bullmq/issues/3474) ([2e2b214](https://github.com/taskforcesh/bullmq/commit/2e2b21454cc6125fcf3abfec939d6d6d8d02c40b))
* **worker:** support maxStartedAttempts option ([#3331](https://github.com/taskforcesh/bullmq/issues/3331)) ([9384a64](https://github.com/taskforcesh/bullmq/commit/9384a64d6d48718220e472c26d0c03e7b7e8e555))

#### Performance Improvements

* **worker:** only consider infinity retry on connection errors ([#3473](https://github.com/taskforcesh/bullmq/issues/3473)) ([9d5a678](https://github.com/taskforcesh/bullmq/commit/9d5a678660f6bb927ad375d7de58814d392dbe9d))

### [5.58.9](https://github.com/taskforcesh/bullmq/compare/v5.58.8...v5.58.9) (2025-09-26)

#### Performance Improvements

* **metrics:** use lua script when calling getMetrics ([#3459](https://github.com/taskforcesh/bullmq/issues/3459)) ([61987c6](https://github.com/taskforcesh/bullmq/commit/61987c62ca71ec11a84b98e6dd51a6d5ebf1737d))

### [5.58.8](https://github.com/taskforcesh/bullmq/compare/v5.58.7...v5.58.8) (2025-09-25)

#### Bug Fixes

* **job-scheduler:** fix unstable upsert ([#3446](https://github.com/taskforcesh/bullmq/issues/3446)) ([2241101](https://github.com/taskforcesh/bullmq/commit/22411010beca628d172790cfbac45e3cd3d102ed))

### [5.58.7](https://github.com/taskforcesh/bullmq/compare/v5.58.6...v5.58.7) (2025-09-19)

#### Bug Fixes

* **job:** add custom jobId validation to prevent : inclusion ([#3384](https://github.com/taskforcesh/bullmq/issues/3384)) fixes [#3382](https://github.com/taskforcesh/bullmq/issues/3382) ([845a6f5](https://github.com/taskforcesh/bullmq/commit/845a6f5fdede9ecf4050e8b5617feb56dbb3c9a1))

### [5.58.6](https://github.com/taskforcesh/bullmq/compare/v5.58.5...v5.58.6) (2025-09-19)

#### Bug Fixes

* **deps:** upgrade uuid to v11 ([#3452](https://github.com/taskforcesh/bullmq/issues/3452)) ([bd8fbc1](https://github.com/taskforcesh/bullmq/commit/bd8fbc164caaa01f665d0c7e94177d0584d04f8c))
* **events:** set prev param as active when calling retryJob script ([#3426](https://github.com/taskforcesh/bullmq/issues/3426)) ([e0ebd15](https://github.com/taskforcesh/bullmq/commit/e0ebd15e47b95f9300d6683475ec5d2176f07c95))
* **deduplication:** validate id option is provided ([#3443](https://github.com/taskforcesh/bullmq/issues/3443)) fixes [#3432](https://github.com/taskforcesh/bullmq/issues/3432) ([533b844](https://github.com/taskforcesh/bullmq/commit/533b84461a908a3d0182002f16e9c0c0a0260014))

### [5.58.5](https://github.com/taskforcesh/bullmq/compare/v5.58.4...v5.58.5) (2025-09-04)

#### Bug Fixes

* **queue:** preserve Job type inference when no explicit type for JobBase ([#3423](https://github.com/taskforcesh/bullmq/issues/3423)) fixes [#3421](https://github.com/taskforcesh/bullmq/issues/3421) ([f642818](https://github.com/taskforcesh/bullmq/commit/f6428188f39f054e8b94579435b16e260aff27cd))

### [5.58.4](https://github.com/taskforcesh/bullmq/compare/v5.58.3...v5.58.4) (2025-08-30)

#### Bug Fixes

* **types:** export Processor type ([#3418](https://github.com/taskforcesh/bullmq/issues/3418)) ([70e8a3f](https://github.com/taskforcesh/bullmq/commit/70e8a3f91595dcdc2d21122170ef4af1f53972ad))

### [5.58.3](https://github.com/taskforcesh/bullmq/compare/v5.58.2...v5.58.3) (2025-08-29)

#### Bug Fixes

* **job-scheduler:** consider undefined type in getJobScheduler return type ([#3412](https://github.com/taskforcesh/bullmq/issues/3412)) ([ffc6e26](https://github.com/taskforcesh/bullmq/commit/ffc6e26eb66533fc6eae4c406bb4b9a9f7590d9b))

### [5.58.2](https://github.com/taskforcesh/bullmq/compare/v5.58.1...v5.58.2) (2025-08-26)

#### Bug Fixes

* **job:** consider parent update when retrying ([#3402](https://github.com/taskforcesh/bullmq/issues/3402)) (python) fixes [#3320](https://github.com/taskforcesh/bullmq/issues/3320) ([316d1ed](https://github.com/taskforcesh/bullmq/commit/316d1ed32680e690b1d2ab92c79a53e0d4c00c2d))

### [5.58.1](https://github.com/taskforcesh/bullmq/compare/v5.58.0...v5.58.1) (2025-08-23)

#### Bug Fixes

* **job:** prevent unnecessary tryCatch calls in getTraces ([#3400](https://github.com/taskforcesh/bullmq/issues/3400)) ([d71b872](https://github.com/taskforcesh/bullmq/commit/d71b87245c8196d19dfeaf82e6ef14c91fb9a7c5))

## [5.58.0](https://github.com/taskforcesh/bullmq/compare/v5.57.0...v5.58.0) (2025-08-15)

#### Features

* **worker:** adds jobName and attemptsMade span attributes when processJob is called ([#3199](https://github.com/taskforcesh/bullmq/issues/3199)) ([db0a922](https://github.com/taskforcesh/bullmq/commit/db0a922741d8c7eae8d5119a0831cd734aba02a2))

## [5.57.0](https://github.com/taskforcesh/bullmq/compare/v5.56.10...v5.57.0) (2025-08-13)

#### Features

* **sandbox:** support moveToWaitingChildren method ([#3389](https://github.com/taskforcesh/bullmq/issues/3389)) ([0fecc6c](https://github.com/taskforcesh/bullmq/commit/0fecc6cd0d0dea06f486ab0b0fe760d866f1fc34))

### [5.56.10](https://github.com/taskforcesh/bullmq/compare/v5.56.9...v5.56.10) (2025-08-10)

#### Bug Fixes

* **scheduler:** consider startDate to generate nextMillis when using pattern ([#3385](https://github.com/taskforcesh/bullmq/issues/3385)) fixes [#3378](https://github.com/taskforcesh/bullmq/issues/3378) ([53754fb](https://github.com/taskforcesh/bullmq/commit/53754fb239cf1b021ffc55391990d879d363dcf7))

### [5.56.9](https://github.com/taskforcesh/bullmq/compare/v5.56.8...v5.56.9) (2025-07-31)

#### Bug Fixes

* **worker:** emit failed event when children are failed in moveToWaitingChildren ([#3346](https://github.com/taskforcesh/bullmq/issues/3346)) ([93df852](https://github.com/taskforcesh/bullmq/commit/93df852f97f04023d791546d30a6af24fbca6114))

### [5.56.8](https://github.com/taskforcesh/bullmq/compare/v5.56.7...v5.56.8) (2025-07-27)

#### Bug Fixes

* **queue:** add support for 'waiting' parameter in clean method ([#3338](https://github.com/taskforcesh/bullmq/issues/3338)) fixes [#3125](https://github.com/taskforcesh/bullmq/issues/3125) ([edb7147](https://github.com/taskforcesh/bullmq/commit/edb714764066b06c068c8c8a5140b010f27c3b9a))

### [5.56.7](https://github.com/taskforcesh/bullmq/compare/v5.56.6...v5.56.7) (2025-07-25)

#### Bug Fixes

* **flow:** remove parent from active when there are unsuccessful children ([#3348](https://github.com/taskforcesh/bullmq/issues/3348)) ([34ee339](https://github.com/taskforcesh/bullmq/commit/34ee33955a660b0696f4b6cff6d8d39fdcd160db))
* **worker:** do not keep active jobs when pausing or closing ([#3350](https://github.com/taskforcesh/bullmq/issues/3350)) fixes [#3349](https://github.com/taskforcesh/bullmq/issues/3349) ([424d155](https://github.com/taskforcesh/bullmq/commit/424d15508172a028479059920ed6bfcf1c54a389))

### [5.56.6](https://github.com/taskforcesh/bullmq/compare/v5.56.5...v5.56.6) (2025-07-25)

#### Bug Fixes

* **repeat:** use legacy updateRepeatableJob script when old format is present ([#3364](https://github.com/taskforcesh/bullmq/issues/3364)) fixes [#3275](https://github.com/taskforcesh/bullmq/issues/3275) ([1e221d5](https://github.com/taskforcesh/bullmq/commit/1e221d5404dcea750a08342c832a682e454135a3))

### [5.56.5](https://github.com/taskforcesh/bullmq/compare/v5.56.4...v5.56.5) (2025-07-19)

#### Bug Fixes

* **rate-limit:** throw right error message if job does not exist ([#3354](https://github.com/taskforcesh/bullmq/issues/3354)) ([83d9695](https://github.com/taskforcesh/bullmq/commit/83d969541f19fa9703eb73ff0006cd29a358c1e7))

### [5.56.4](https://github.com/taskforcesh/bullmq/compare/v5.56.3...v5.56.4) (2025-07-11)

#### Bug Fixes

* **connection:** ignore info command when skipVersionCheck is provided as true ([#3342](https://github.com/taskforcesh/bullmq/issues/3342)) fixes [#3341](https://github.com/taskforcesh/bullmq/issues/3341) ([b94d7ed](https://github.com/taskforcesh/bullmq/commit/b94d7ed5602e366b4401051b236f31ac2dd2a90d))

### [5.56.3](https://github.com/taskforcesh/bullmq/compare/v5.56.2...v5.56.3) (2025-07-10)

#### Bug Fixes

* **scheduler:** take offset into the startMillis calculation ([#2944](https://github.com/taskforcesh/bullmq/issues/2944)) fixes [#247](https://github.com/taskforcesh/bullmq/issues/247) ([1e3f3c5](https://github.com/taskforcesh/bullmq/commit/1e3f3c507a7ceb8d8147941adc9de69367947a5e))

### [5.56.2](https://github.com/taskforcesh/bullmq/compare/v5.56.1...v5.56.2) (2025-07-08)

#### Performance Improvements

* **woker:** keep lower blockTimeout when consuming delayed markers ([#3333](https://github.com/taskforcesh/bullmq/issues/3333)) ([e687d7c](https://github.com/taskforcesh/bullmq/commit/e687d7cf86108138bbd5e911b11ab3c5717fc23c))

### [5.56.1](https://github.com/taskforcesh/bullmq/compare/v5.56.0...v5.56.1) (2025-07-03)

#### Performance Improvements

* **worker:** do not wait rate limit when fetching jobs ([#3322](https://github.com/taskforcesh/bullmq/issues/3322)) ([c32e6a0](https://github.com/taskforcesh/bullmq/commit/c32e6a0ff6df8bc34c9c13238c192974a93f7ddb))

## [5.56.0](https://github.com/taskforcesh/bullmq/compare/v5.55.0...v5.56.0) (2025-06-22)

#### Features

* **deduplication:** add support for replace and extend options ([#3260](https://github.com/taskforcesh/bullmq/issues/3260)) ref [#2767](https://github.com/taskforcesh/bullmq/issues/2767) [#3151](https://github.com/taskforcesh/bullmq/issues/3151) [#3250](https://github.com/taskforcesh/bullmq/issues/3250) ([4a53609](https://github.com/taskforcesh/bullmq/commit/4a5360936c1a543a1ff31ebbb6ab1289cc8ddf07))

## [5.55.0](https://github.com/taskforcesh/bullmq/compare/v5.54.3...v5.55.0) (2025-06-21)

#### Features

* **worker:** allow calling moveToWait when job is processing ([#3302](https://github.com/taskforcesh/bullmq/issues/3302)) ref [#3296](https://github.com/taskforcesh/bullmq/issues/3296) ([e742511](https://github.com/taskforcesh/bullmq/commit/e742511baf35225718c01e621623eab661f37284))

### [5.54.3](https://github.com/taskforcesh/bullmq/compare/v5.54.2...v5.54.3) (2025-06-18)

#### Bug Fixes

* **scheduler:** fix slot calculation when using every ([#3307](https://github.com/taskforcesh/bullmq/issues/3307)) ([588719e](https://github.com/taskforcesh/bullmq/commit/588719ee49c7615affeb69d3a431025757115c10))

### [5.54.2](https://github.com/taskforcesh/bullmq/compare/v5.54.1...v5.54.2) (2025-06-17)

#### Bug Fixes

* avoid circular reference between scripts and queue ([#3301](https://github.com/taskforcesh/bullmq/issues/3301)) ([fb65677](https://github.com/taskforcesh/bullmq/commit/fb65677f2d636e1aca3cc75cb3b740b8729b3358))

### [5.54.1](https://github.com/taskforcesh/bullmq/compare/v5.54.0...v5.54.1) (2025-06-17)

#### Performance Improvements

* **scheduler:** save offset value when every is provided ([#3142](https://github.com/taskforcesh/bullmq/issues/3142)) ([98f35bc](https://github.com/taskforcesh/bullmq/commit/98f35bc1eabb3ab1010737869c310d2001a84fac))

## [5.54.0](https://github.com/taskforcesh/bullmq/compare/v5.53.3...v5.54.0) (2025-06-15)

#### Features

* **backoff:** add jitter option ([#3291](https://github.com/taskforcesh/bullmq/issues/3291)) ([86c4c6d](https://github.com/taskforcesh/bullmq/commit/86c4c6dd25ef868f1f37c917ab11cb663e330e2f))

### [5.53.3](https://github.com/taskforcesh/bullmq/compare/v5.53.2...v5.53.3) (2025-06-13)

#### Bug Fixes

* **worker:** avoid dangling jobs to hang the queue with rate limit ([#3297](https://github.com/taskforcesh/bullmq/issues/3297)) fixes [#3289](https://github.com/taskforcesh/bullmq/issues/3289) ([263d33d](https://github.com/taskforcesh/bullmq/commit/263d33d536a92daf578c56cbb58765917046e052))

### [5.53.2](https://github.com/taskforcesh/bullmq/compare/v5.53.1...v5.53.2) (2025-06-02)

#### Performance Improvements

* **stalled:** fail stalled jobs in a lazy way ([#3266](https://github.com/taskforcesh/bullmq/issues/3266)) ([5cbf064](https://github.com/taskforcesh/bullmq/commit/5cbf0647e106d45d78318a5e5e9fb017261374c9))

### [5.53.1](https://github.com/taskforcesh/bullmq/compare/v5.53.0...v5.53.1) (2025-05-30)

#### Bug Fixes

* **job:** do not parse ignored failures in getDependencies ([#3284](https://github.com/taskforcesh/bullmq/issues/3284)) fixes [#3283](https://github.com/taskforcesh/bullmq/issues/3283) ([04ca6b5](https://github.com/taskforcesh/bullmq/commit/04ca6b55c15698aab3ceaf72bd2ed9c589d76197))
* **scheduler:** remove current job when it is in delayed state ([#3269](https://github.com/taskforcesh/bullmq/issues/3269)) fixes [#3262](https://github.com/taskforcesh/bullmq/issues/3262) [#3272](https://github.com/taskforcesh/bullmq/issues/3272) ([1ca4cbd](https://github.com/taskforcesh/bullmq/commit/1ca4cbd17a58c7eba83030bd6440d0f5e5d69633))

## [5.53.0](https://github.com/taskforcesh/bullmq/compare/v5.52.3...v5.53.0) (2025-05-21)

#### Features

* **sandbox:** add getIgnoredChildrenFailures method in job's wrapper ([#3263](https://github.com/taskforcesh/bullmq/issues/3263)) ([5d2723d](https://github.com/taskforcesh/bullmq/commit/5d2723dd82e636846e2ff886abb4c0161c15a441))

### [5.52.3](https://github.com/taskforcesh/bullmq/compare/v5.52.2...v5.52.3) (2025-05-19)

#### Bug Fixes

* **flow:** add new error code when parent has failed children ([#3268](https://github.com/taskforcesh/bullmq/issues/3268)) ([b8fba5e](https://github.com/taskforcesh/bullmq/commit/b8fba5e937a41d0c7ddc97443e9fa8d0f0de566b))

#### Features

* **job:** add moveToCompleted method \[python] ([#3251](https://github.com/taskforcesh/bullmq/issues/3251)) ([6a8e3e2](https://github.com/taskforcesh/bullmq/commit/6a8e3e206384b56063c6f5a46ca030d2b330c712))

### [5.52.2](https://github.com/taskforcesh/bullmq/compare/v5.52.1...v5.52.2) (2025-05-08)

#### Bug Fixes

* **worker:** maxStalledCount no less than 0 ([#3249](https://github.com/taskforcesh/bullmq/issues/3249)) fixes [#3248](https://github.com/taskforcesh/bullmq/issues/3248) ([34dcb8c](https://github.com/taskforcesh/bullmq/commit/34dcb8c3d01a822b07852bc928d882bd6e4049d2))

### [5.52.1](https://github.com/taskforcesh/bullmq/compare/v5.52.0...v5.52.1) (2025-05-02)

#### Bug Fixes

* **remove:** pass correct children meta references ([#3245](https://github.com/taskforcesh/bullmq/issues/3245)) ([01c62ad](https://github.com/taskforcesh/bullmq/commit/01c62ada0cea80c73ba28d79fd14ea5ba78fdc7d))

## [5.52.0](https://github.com/taskforcesh/bullmq/compare/v5.51.1...v5.52.0) (2025-05-01)

#### Bug Fixes

* **connection:** add str type in connection option \[python] ([#3212](https://github.com/taskforcesh/bullmq/issues/3212)) ([72fac42](https://github.com/taskforcesh/bullmq/commit/72fac4297f5a60e0c2ae0831507cb16ce8baed5f))

#### Features

* **flow:** support failed children in getFlow and getDependencies methods ([#3243](https://github.com/taskforcesh/bullmq/issues/3243)) ([d3b1cff](https://github.com/taskforcesh/bullmq/commit/d3b1cff4cf02aad8ae0812b1d465316a067118d0))

### [5.51.1](https://github.com/taskforcesh/bullmq/compare/v5.51.0...v5.51.1) (2025-04-26)

#### Bug Fixes

* **queue-events:** omit telemetry options ([#3239](https://github.com/taskforcesh/bullmq/issues/3239)) ([e4dac2c](https://github.com/taskforcesh/bullmq/commit/e4dac2c39fac0c8cce34fbcb98a0c72c1619ed4e))

## [5.51.0](https://github.com/taskforcesh/bullmq/compare/v5.50.0...v5.51.0) (2025-04-25)

#### Bug Fixes

* **job-scheduler:** remove next delayed job if present even if scheduler does not exist ([#3203](https://github.com/taskforcesh/bullmq/issues/3203)) ref [#3197](https://github.com/taskforcesh/bullmq/issues/3197) ([61395bf](https://github.com/taskforcesh/bullmq/commit/61395bf0b2fc656d1cdaf094fc62a03920ebe07d))

#### Features

* **flow:** support ignored children in getFlow and getDependencies methods ([#3238](https://github.com/taskforcesh/bullmq/issues/3238)) ref [#3213](https://github.com/taskforcesh/bullmq/issues/3213) ([2927803](https://github.com/taskforcesh/bullmq/commit/2927803b4b1eaddb77d3690634beb9c071b5adf7))

## [5.50.0](https://github.com/taskforcesh/bullmq/compare/v5.49.2...v5.50.0) (2025-04-25)

#### Bug Fixes

* **deduplication:** remove deduplication key only when jobId matches with the last one being saved ([#3236](https://github.com/taskforcesh/bullmq/issues/3236)) ([192e82c](https://github.com/taskforcesh/bullmq/commit/192e82caa0f7f530ed495740ec2ade37fe89b43b))

#### Features

* **queue:** add getIgnoredChildrenFailures method ([#3194](https://github.com/taskforcesh/bullmq/issues/3194)) ([4affb11](https://github.com/taskforcesh/bullmq/commit/4affb11be26afad9f867db19a210c361ba64dd4b))

### [5.49.2](https://github.com/taskforcesh/bullmq/compare/v5.49.1...v5.49.2) (2025-04-21)

#### Performance Improvements

* **flow:** change parent failure in a lazy way ([#3228](https://github.com/taskforcesh/bullmq/issues/3228)) ([6b37a37](https://github.com/taskforcesh/bullmq/commit/6b37a379cc65abe7b4c60ba427065957c9080a08))

### [5.49.1](https://github.com/taskforcesh/bullmq/compare/v5.49.0...v5.49.1) (2025-04-17)

#### Bug Fixes

* **flow-producer:** use FlowProducer prefix by default when calling getFlow ([#3224](https://github.com/taskforcesh/bullmq/issues/3224)) ([bd17aad](https://github.com/taskforcesh/bullmq/commit/bd17aad64ec73917548e1bb45ee611b799363cc0))

## [5.49.0](https://github.com/taskforcesh/bullmq/compare/v5.48.1...v5.49.0) (2025-04-16)

#### Features

* **job:** expose stalledCounter attribute ([#3218](https://github.com/taskforcesh/bullmq/issues/3218)) ([9456472](https://github.com/taskforcesh/bullmq/commit/94564724593699d13bc0ac238e23c13737edbbf2))

### [5.48.1](https://github.com/taskforcesh/bullmq/compare/v5.48.0...v5.48.1) (2025-04-10)

#### Bug Fixes

* made line split more compatible ([#3208](https://github.com/taskforcesh/bullmq/issues/3208)) ([3c2349a](https://github.com/taskforcesh/bullmq/commit/3c2349a2936d0c59cfa8d136585a0c0156de3212)), closes [#3204](https://github.com/taskforcesh/bullmq/issues/3204)

## [5.48.0](https://github.com/taskforcesh/bullmq/compare/v5.47.3...v5.48.0) (2025-04-08)

#### Features

* add removeUnprocessedChildren ([#3190](https://github.com/taskforcesh/bullmq/issues/3190)) ([4b96266](https://github.com/taskforcesh/bullmq/commit/4b96266d4a7e2fe4b1b3eba12e9e7cc5a64fc044))

### [5.47.3](https://github.com/taskforcesh/bullmq/compare/v5.47.2...v5.47.3) (2025-04-08)

#### Bug Fixes

* **job-scheduler:** fix endDate presence validation ([#3195](https://github.com/taskforcesh/bullmq/issues/3195)) ([339f13e](https://github.com/taskforcesh/bullmq/commit/339f13e277c7c087adc9023f5a433d9a21c661a2))

### [5.47.2](https://github.com/taskforcesh/bullmq/compare/v5.47.1...v5.47.2) (2025-04-06)

#### Bug Fixes

* **flow:** remove job from dependencies when failParentOnFailure or continueParentOnFailure ([#3201](https://github.com/taskforcesh/bullmq/issues/3201)) ([1fbcbec](https://github.com/taskforcesh/bullmq/commit/1fbcbec56969fc4aa628f77e4b05d2c6844894ae))

### [5.47.1](https://github.com/taskforcesh/bullmq/compare/v5.47.0...v5.47.1) (2025-04-05)

#### Bug Fixes

* **flow-producer:** fix queueName otel attribute when passing it to addNode ([#3198](https://github.com/taskforcesh/bullmq/issues/3198)) ([758ea26](https://github.com/taskforcesh/bullmq/commit/758ea2647b3dad683796351919b0380172fa717f))

## [5.47.0](https://github.com/taskforcesh/bullmq/compare/v5.46.1...v5.47.0) (2025-04-04)

#### Features

* **flows:** add continueParentOnFailure option ([#3181](https://github.com/taskforcesh/bullmq/issues/3181)) ([738d375](https://github.com/taskforcesh/bullmq/commit/738d3752934746a347fd04e59e9dcd4726777508))

### [5.46.1](https://github.com/taskforcesh/bullmq/compare/v5.46.0...v5.46.1) (2025-04-03)

#### Bug Fixes

* **queue-events:** pass right path for JobProgress type ([#3192](https://github.com/taskforcesh/bullmq/issues/3192)) fixes [#3191](https://github.com/taskforcesh/bullmq/issues/3191) ([33c62e6](https://github.com/taskforcesh/bullmq/commit/33c62e67268daf24d92653abb5b857ac2241b3aa))

## [5.46.0](https://github.com/taskforcesh/bullmq/compare/v5.45.2...v5.46.0) (2025-04-02)

#### Features

* **updateProgress:** allow more types to be used as progress ([#3187](https://github.com/taskforcesh/bullmq/issues/3187)) ([f16b748](https://github.com/taskforcesh/bullmq/commit/f16b748d7e3af2535ccdc54e12500af74874a235))

### [5.45.2](https://github.com/taskforcesh/bullmq/compare/v5.45.1...v5.45.2) (2025-03-29)

#### Bug Fixes

* **flow:** validate pending dependencies before removing lock ([#3182](https://github.com/taskforcesh/bullmq/issues/3182)) ([8d59e3b](https://github.com/taskforcesh/bullmq/commit/8d59e3b8084c60afad16372b4f7fc22f1b9d3f4e))

### [5.45.1](https://github.com/taskforcesh/bullmq/compare/v5.45.0...v5.45.1) (2025-03-29)

#### Bug Fixes

* **job-scheduler:** emit duplicated event when next delayed job exists ([#3172](https://github.com/taskforcesh/bullmq/issues/3172)) ([d57698f](https://github.com/taskforcesh/bullmq/commit/d57698f9af64fd1bb85f571f22b7fd663c3e05ee))

## [5.45.0](https://github.com/taskforcesh/bullmq/compare/v5.44.4...v5.45.0) (2025-03-27)

#### Features

* add deduplicated job id to the deduplicated event ([0f21c10](https://github.com/taskforcesh/bullmq/commit/0f21c10bc9fd9a2290e8dde3c9b43bc366fcb15a))

### [5.44.4](https://github.com/taskforcesh/bullmq/compare/v5.44.3...v5.44.4) (2025-03-24)

#### Bug Fixes

* **scheduler:** remove next delayed job when possible ([#3153](https://github.com/taskforcesh/bullmq/issues/3153)) ([219c0db](https://github.com/taskforcesh/bullmq/commit/219c0dba7180143b19b4a21dc96db45af941ca7d))

### [5.44.3](https://github.com/taskforcesh/bullmq/compare/v5.44.2...v5.44.3) (2025-03-22)

#### Bug Fixes

* **flow:** only validate pending dependencies when moving to completed ([#3164](https://github.com/taskforcesh/bullmq/issues/3164)) ([d3c397f](https://github.com/taskforcesh/bullmq/commit/d3c397fa3f122287026018aaae5ed2c5dfad19aa))

### [5.44.2](https://github.com/taskforcesh/bullmq/compare/v5.44.1...v5.44.2) (2025-03-22)

#### Performance Improvements

* **flow:** validate parentKey existence before trying to move it to failed ([#3163](https://github.com/taskforcesh/bullmq/issues/3163)) ([5a88e47](https://github.com/taskforcesh/bullmq/commit/5a88e4745d9449e41c5e2c467b5d02ca21357703))

### [5.44.1](https://github.com/taskforcesh/bullmq/compare/v5.44.0...v5.44.1) (2025-03-21)

#### Bug Fixes

* **flow:** consider prioritized state when moving a parent to failed ([#3160](https://github.com/taskforcesh/bullmq/issues/3160)) ([d91d9f4](https://github.com/taskforcesh/bullmq/commit/d91d9f4398584506f5af8b46e4d47b769beaa212))

## [5.44.0](https://github.com/taskforcesh/bullmq/compare/v5.43.1...v5.44.0) (2025-03-18)

#### Features

* **prometheus export:** expose global variables ([0325a39](https://github.com/taskforcesh/bullmq/commit/0325a39f4243f3bea682bcfc20dc43b62d3f9fd9))

### [5.43.1](https://github.com/taskforcesh/bullmq/compare/v5.43.0...v5.43.1) (2025-03-15)

#### Bug Fixes

* **job-scheduler:** add marker when upserting job scheduler if needed ([#3145](https://github.com/taskforcesh/bullmq/issues/3145)) ([0e137b2](https://github.com/taskforcesh/bullmq/commit/0e137b2e78882b6206b3fa47d4a6babb4fcfc484))

## [5.43.0](https://github.com/taskforcesh/bullmq/compare/v5.42.0...v5.43.0) (2025-03-13)

#### Features

* **job:** support ignored and failed counts in getDependenciesCount ([#3137](https://github.com/taskforcesh/bullmq/issues/3137)) ref [#3136](https://github.com/taskforcesh/bullmq/issues/3136) ([83953db](https://github.com/taskforcesh/bullmq/commit/83953db54cad80e4ec0a7659f41cb5bc086ccacf))

## [5.42.0](https://github.com/taskforcesh/bullmq/compare/v5.41.9...v5.42.0) (2025-03-12)

#### Bug Fixes

* **flow:** consider to fail a parent not in waiting-children when failParentOnFailure is provided ([#3098](https://github.com/taskforcesh/bullmq/issues/3098)) ([589adb4](https://github.com/taskforcesh/bullmq/commit/589adb4f89bcb7d7721200333c2d605eb6ba7864))
* **job-scheduler:** restore iterationCount attribute ([#3134](https://github.com/taskforcesh/bullmq/issues/3134)) ([eec7114](https://github.com/taskforcesh/bullmq/commit/eec711468de39ec10da9206d7f8c5ad1eb0df882))

#### Features

* **job:** add complete span in moveToCompleted method ([#3132](https://github.com/taskforcesh/bullmq/issues/3132)) ([c37123c](https://github.com/taskforcesh/bullmq/commit/c37123cc84632328d8c4e251641688eb36ac1a8a))

#### Performance Improvements

* **worker:** optimize job retrieval for failed jobs in chunks ([#3127](https://github.com/taskforcesh/bullmq/issues/3127)) ([e0f02ce](https://github.com/taskforcesh/bullmq/commit/e0f02ceb00ced5ca00a6c73d96801a040c40d958))

### [5.41.9](https://github.com/taskforcesh/bullmq/compare/v5.41.8...v5.41.9) (2025-03-11)

#### Bug Fixes

* **scheduler:** remove multi when updating a job scheduler ([#3108](https://github.com/taskforcesh/bullmq/issues/3108)) ([4b619ca](https://github.com/taskforcesh/bullmq/commit/4b619cab9a6bf8d25efec83dcdf0adaaa362e12a))

### [5.41.8](https://github.com/taskforcesh/bullmq/compare/v5.41.7...v5.41.8) (2025-03-08)

#### Bug Fixes

* **job:** deserialize priority in fromJSON ([#3126](https://github.com/taskforcesh/bullmq/issues/3126)) ([c3269b1](https://github.com/taskforcesh/bullmq/commit/c3269b11e2def4e2acd4eafc02ce7958a8fcf63e))
* **worker:** cast delay\_until to integer \[python] ([#3116](https://github.com/taskforcesh/bullmq/issues/3116)) ([db617e4](https://github.com/taskforcesh/bullmq/commit/db617e48ef1dd52446bfd73e15f24957df2ca315))

### [5.41.7](https://github.com/taskforcesh/bullmq/compare/v5.41.6...v5.41.7) (2025-02-27)

#### Bug Fixes

* **scheduler:** validate repeatKey if present when cleaning failed jobs ([#3115](https://github.com/taskforcesh/bullmq/issues/3115)) fixes [#3114](https://github.com/taskforcesh/bullmq/issues/3114) ([d4cad84](https://github.com/taskforcesh/bullmq/commit/d4cad8402628f1773299c9cf33e6cc6a0e694037))

### [5.41.6](https://github.com/taskforcesh/bullmq/compare/v5.41.5...v5.41.6) (2025-02-26)

#### Bug Fixes

* **flow:** consider delayed state when moving a parent to failed ([#3112](https://github.com/taskforcesh/bullmq/issues/3112)) ([6a28b86](https://github.com/taskforcesh/bullmq/commit/6a28b861346a3efa89574a78b396954d6c4ed113))
* **telemetry:** fix span name for moveToFailed logic ([#3113](https://github.com/taskforcesh/bullmq/issues/3113)) ([7a4b500](https://github.com/taskforcesh/bullmq/commit/7a4b500dc63320807e051d8efd2b8fee07bb0db5))

### [5.41.5](https://github.com/taskforcesh/bullmq/compare/v5.41.4...v5.41.5) (2025-02-21)

#### Bug Fixes

* **job-scheduler:** consider removing current job from wait, paused or prioritized ([#3066](https://github.com/taskforcesh/bullmq/issues/3066)) ([97cd2b1](https://github.com/taskforcesh/bullmq/commit/97cd2b147d541e0984d1c2e107110e1a9d56d9b5))

### [5.41.4](https://github.com/taskforcesh/bullmq/compare/v5.41.3...v5.41.4) (2025-02-21)

#### Performance Improvements

* **delayed:** add marker once when promoting delayed jobs ([#3096](https://github.com/taskforcesh/bullmq/issues/3096)) (python) ([38912fb](https://github.com/taskforcesh/bullmq/commit/38912fba969d614eb44d05517ba2ec8bc418a16e))

### [5.41.3](https://github.com/taskforcesh/bullmq/compare/v5.41.2...v5.41.3) (2025-02-19)

#### Bug Fixes

* **worker:** do not execute run method when no processor is defined when resuming ([#3089](https://github.com/taskforcesh/bullmq/issues/3089)) ([4a66933](https://github.com/taskforcesh/bullmq/commit/4a66933496db68a84ec7eb7c153fcedb7bd14c7b))

### [5.41.2](https://github.com/taskforcesh/bullmq/compare/v5.41.1...v5.41.2) (2025-02-16)

#### Bug Fixes

* **worker:** do not resume when closing ([#3080](https://github.com/taskforcesh/bullmq/issues/3080)) ([024ee0f](https://github.com/taskforcesh/bullmq/commit/024ee0f3f0e808c256712d3ccb1bcadb025eb931))

### [5.41.1](https://github.com/taskforcesh/bullmq/compare/v5.41.0...v5.41.1) (2025-02-15)

#### Bug Fixes

* **job:** set processedBy when moving job to active in moveToFinished ([#3077](https://github.com/taskforcesh/bullmq/issues/3077)) fixes [#3073](https://github.com/taskforcesh/bullmq/issues/3073) ([1aa970c](https://github.com/taskforcesh/bullmq/commit/1aa970ced3c55949aea6726c4ad29531089f5370))

## [5.41.0](https://github.com/taskforcesh/bullmq/compare/v5.40.5...v5.41.0) (2025-02-14)

#### Features

* **job:** add moveToWait method for manual processing ([#2978](https://github.com/taskforcesh/bullmq/issues/2978)) ([5a97491](https://github.com/taskforcesh/bullmq/commit/5a97491a0319df320b7858657e03c357284e0108))
* **queue:** support removeGlobalConcurrency method ([#3076](https://github.com/taskforcesh/bullmq/issues/3076)) ([ece8532](https://github.com/taskforcesh/bullmq/commit/ece853203adb420466dfaf3ff8bccc73fb917147))

#### Performance Improvements

* **add-job:** add job into wait or prioritized state when delay is provided as 0 ([#3052](https://github.com/taskforcesh/bullmq/issues/3052)) ([3e990eb](https://github.com/taskforcesh/bullmq/commit/3e990eb742b3a12065110f33135f282711fdd7b9))

### [5.40.5](https://github.com/taskforcesh/bullmq/compare/v5.40.4...v5.40.5) (2025-02-14)

#### Bug Fixes

* **drain:** pass delayed key for redis cluster ([#3074](https://github.com/taskforcesh/bullmq/issues/3074)) ([05ea32b](https://github.com/taskforcesh/bullmq/commit/05ea32b7e4f0cd4099783fd81d2b3214d7a293d5))

### [5.40.4](https://github.com/taskforcesh/bullmq/compare/v5.40.3...v5.40.4) (2025-02-13)

#### Bug Fixes

* **job-scheduler:** restore limit option to be saved ([#3071](https://github.com/taskforcesh/bullmq/issues/3071)) ([3e649f7](https://github.com/taskforcesh/bullmq/commit/3e649f7399514b343447ed2073cc07e4661f7390))

### [5.40.3](https://github.com/taskforcesh/bullmq/compare/v5.40.2...v5.40.3) (2025-02-12)

#### Bug Fixes

* **job-scheduler:** return undefined in getJobScheduler when it does not exist ([#3065](https://github.com/taskforcesh/bullmq/issues/3065)) fixes [#3062](https://github.com/taskforcesh/bullmq/issues/3062) ([548cc1c](https://github.com/taskforcesh/bullmq/commit/548cc1ce8080042b4b44009ea99108bd24193895))

### [5.40.2](https://github.com/taskforcesh/bullmq/compare/v5.40.1...v5.40.2) (2025-02-07)

#### Bug Fixes

* fix return type of getNextJob ([b970281](https://github.com/taskforcesh/bullmq/commit/b9702812e6961f0f5a834f66d43cfb2feabaafd8))

### [5.40.1](https://github.com/taskforcesh/bullmq/compare/v5.40.0...v5.40.1) (2025-02-07)

#### Bug Fixes

* **worker:** wait fetched jobs to be processed when closing ([#3059](https://github.com/taskforcesh/bullmq/issues/3059)) ([d4de2f5](https://github.com/taskforcesh/bullmq/commit/d4de2f5e88d57ea00274e62ab23d09f4806196f8))

## [5.40.0](https://github.com/taskforcesh/bullmq/compare/v5.39.2...v5.40.0) (2025-02-02)

#### Features

* **job-scheduler:** revert add delayed job and update in the same script ([9f0f1ba](https://github.com/taskforcesh/bullmq/commit/9f0f1ba9b17874a757ac38c1878792c0df3c5a9a))

### [5.39.2](https://github.com/taskforcesh/bullmq/compare/v5.39.1...v5.39.2) (2025-02-02)

#### Bug Fixes

* **worker:** evaluate if a job needs to be fetched when moving to failed ([#3043](https://github.com/taskforcesh/bullmq/issues/3043)) ([406e21c](https://github.com/taskforcesh/bullmq/commit/406e21c9aadd7670f353c1c6b102a401fc327653))

### [5.39.1](https://github.com/taskforcesh/bullmq/compare/v5.39.0...v5.39.1) (2025-01-30)

#### Bug Fixes

* **retry-job:** consider updating failures in job ([#3036](https://github.com/taskforcesh/bullmq/issues/3036)) ([21e8495](https://github.com/taskforcesh/bullmq/commit/21e8495b5f2bf5418d86f60b59fad25d306a0298))

## [5.39.0](https://github.com/taskforcesh/bullmq/compare/v5.38.0...v5.39.0) (2025-01-29)

#### Features

* **job-scheduler:** save limit option ([#3033](https://github.com/taskforcesh/bullmq/issues/3033)) ([a1571ea](https://github.com/taskforcesh/bullmq/commit/a1571ea03be6c6c41794fa272c38c29588351bbf))

## [5.38.0](https://github.com/taskforcesh/bullmq/compare/v5.37.0...v5.38.0) (2025-01-28)

#### Bug Fixes

* **flow-producer:** add support for skipWaitingForReady ([6d829fc](https://github.com/taskforcesh/bullmq/commit/6d829fceda9f204f193c533ffc780962692b8f16))

#### Features

* **queue:** add option to skip wait until connection ready ([e728299](https://github.com/taskforcesh/bullmq/commit/e72829922d4234b92290346dce5d33f5b98ee373))

## [5.37.0](https://github.com/taskforcesh/bullmq/compare/v5.36.0...v5.37.0) (2025-01-25)

#### Features

* **queue-getters:** add prometheus exporter ([078ae9d](https://github.com/taskforcesh/bullmq/commit/078ae9db80f6ca64ff0a8135b57a6dc71d71cb1e))

## [5.36.0](https://github.com/taskforcesh/bullmq/compare/v5.35.1...v5.36.0) (2025-01-24)

#### Features

* **job-scheduler:** save iteration count ([#3018](https://github.com/taskforcesh/bullmq/issues/3018)) ([ad5c07c](https://github.com/taskforcesh/bullmq/commit/ad5c07cc7672a3f7a7185310b1250763a5fef76b))

### [5.35.1](https://github.com/taskforcesh/bullmq/compare/v5.35.0...v5.35.1) (2025-01-23)

#### Bug Fixes

* **worker:** avoid possible hazard in closing worker ([0f07467](https://github.com/taskforcesh/bullmq/commit/0f0746727176d7ff285ae2d1f35048109b4574c5))

## [5.35.0](https://github.com/taskforcesh/bullmq/compare/v5.34.10...v5.35.0) (2025-01-22)

#### Features

* **sandbox:** add support for getChildrenValues ([dcc3b06](https://github.com/taskforcesh/bullmq/commit/dcc3b0628f992546d7b93f509795e5d4eb3e1b15))

### [5.34.10](https://github.com/taskforcesh/bullmq/compare/v5.34.9...v5.34.10) (2025-01-14)

#### Bug Fixes

* **job-scheduler:** use delayed job data when template data is not present ([#3010](https://github.com/taskforcesh/bullmq/issues/3010)) fixes [#3009](https://github.com/taskforcesh/bullmq/issues/3009) ([95edb40](https://github.com/taskforcesh/bullmq/commit/95edb4008fcd32f09ec0953d862692d4ac7608c0))

### [5.34.9](https://github.com/taskforcesh/bullmq/compare/v5.34.8...v5.34.9) (2025-01-12)

#### Bug Fixes

* **job-scheduler:** add next delayed job only when prevMillis matches with producerId ([#3001](https://github.com/taskforcesh/bullmq/issues/3001)) ([4ea35dd](https://github.com/taskforcesh/bullmq/commit/4ea35dd9e16ff0197f204210696f41c0c5bd0e30))

### [5.34.8](https://github.com/taskforcesh/bullmq/compare/v5.34.7...v5.34.8) (2025-01-08)

#### Performance Improvements

* **job-scheduler:** add delayed job and update scheduler in same script ([#2997](https://github.com/taskforcesh/bullmq/issues/2997)) ([9be28a0](https://github.com/taskforcesh/bullmq/commit/9be28a0c4a907798a447d02ca50662c12333dd82))

### [5.34.7](https://github.com/taskforcesh/bullmq/compare/v5.34.6...v5.34.7) (2025-01-06)

#### Performance Improvements

* **job-scheduler:** add delayed job and scheduler in same script ([#2993](https://github.com/taskforcesh/bullmq/issues/2993)) ([95718e8](https://github.com/taskforcesh/bullmq/commit/95718e888ba64b4071f21bbe0823b55a51ab145c))

### [5.34.6](https://github.com/taskforcesh/bullmq/compare/v5.34.5...v5.34.6) (2024-12-31)

#### Bug Fixes

* **job-scheduler:** avoid duplicates when upserting in a quick sequence ([#2991](https://github.com/taskforcesh/bullmq/issues/2991)) ([e8cdb99](https://github.com/taskforcesh/bullmq/commit/e8cdb99881bc7cebbc48cb7834da5eafa289712f))

### [5.34.5](https://github.com/taskforcesh/bullmq/compare/v5.34.4...v5.34.5) (2024-12-25)

#### Bug Fixes

* **dynamic-rate-limit:** validate job lock cases ([#2975](https://github.com/taskforcesh/bullmq/issues/2975)) ([8bb27ea](https://github.com/taskforcesh/bullmq/commit/8bb27ea4438cbd11e85fa4d0aa516bd1c0e7d51b))

### [5.34.4](https://github.com/taskforcesh/bullmq/compare/v5.34.3...v5.34.4) (2024-12-21)

#### Bug Fixes

* **sandbox:** fix issue where job could stay in active forever ([#2979](https://github.com/taskforcesh/bullmq/issues/2979)) ([c0a6bcd](https://github.com/taskforcesh/bullmq/commit/c0a6bcdf9594540ef6c8ec08df28550f4f5e1950))

### [5.34.3](https://github.com/taskforcesh/bullmq/compare/v5.34.2...v5.34.3) (2024-12-18)

#### Bug Fixes

* **sandboxed:** fix detecting special errors by sending default messages ([#2967](https://github.com/taskforcesh/bullmq/issues/2967)) fixes [#2962](https://github.com/taskforcesh/bullmq/issues/2962) ([52b0e34](https://github.com/taskforcesh/bullmq/commit/52b0e34f0a38ac71ebd0667a5fa116ecd73ae4d2))

### [5.34.2](https://github.com/taskforcesh/bullmq/compare/v5.34.1...v5.34.2) (2024-12-14)

#### Bug Fixes

* **scripts:** make sure jobs fields are not empty before unpack ([4360572](https://github.com/taskforcesh/bullmq/commit/4360572745a929c7c4f6266ec03d4eba77a9715c))

### [5.34.1](https://github.com/taskforcesh/bullmq/compare/v5.34.0...v5.34.1) (2024-12-13)

#### Bug Fixes

* guarantee every repeatable jobs are slotted ([9917df1](https://github.com/taskforcesh/bullmq/commit/9917df166aff2e2f143c45297f41ac8520bfc8ae))
* **job-scheduler:** avoid duplicated delayed jobs when repeatable jobs are retried ([af75315](https://github.com/taskforcesh/bullmq/commit/af75315f0c7923f5e0a667a9ed4606b28b89b719))

## [5.34.0](https://github.com/taskforcesh/bullmq/compare/v5.33.1...v5.34.0) (2024-12-10)

#### Features

* **telemetry:** add option to omit context propagation on jobs ([#2946](https://github.com/taskforcesh/bullmq/issues/2946)) ([6514c33](https://github.com/taskforcesh/bullmq/commit/6514c335231cb6e727819cf5e0c56ed3f5132838))

### [5.33.1](https://github.com/taskforcesh/bullmq/compare/v5.33.0...v5.33.1) (2024-12-10)

#### Bug Fixes

* **job-scheduler:** omit deduplication and debounce options from template options ([#2960](https://github.com/taskforcesh/bullmq/issues/2960)) ([b5fa6a3](https://github.com/taskforcesh/bullmq/commit/b5fa6a3208a8f2a39777dc30c2db2f498addb907))

## [5.33.0](https://github.com/taskforcesh/bullmq/compare/v5.32.0...v5.33.0) (2024-12-09)

#### Features

* replace multi by lua scripts in moveToFailed ([#2958](https://github.com/taskforcesh/bullmq/issues/2958)) ([c19c914](https://github.com/taskforcesh/bullmq/commit/c19c914969169c660a3e108126044c5152faf0cd))

## [5.32.0](https://github.com/taskforcesh/bullmq/compare/v5.31.2...v5.32.0) (2024-12-08)

#### Features

* **queue:** enhance getJobSchedulers method to include template information ([#2956](https://github.com/taskforcesh/bullmq/issues/2956)) ref [#2875](https://github.com/taskforcesh/bullmq/issues/2875) ([5b005cd](https://github.com/taskforcesh/bullmq/commit/5b005cd94ba0f98677bed4a44f8669c81f073f26))

### [5.31.2](https://github.com/taskforcesh/bullmq/compare/v5.31.1...v5.31.2) (2024-12-06)

#### Bug Fixes

* **worker:** catch connection error when moveToActive is called ([#2952](https://github.com/taskforcesh/bullmq/issues/2952)) ([544fc7c](https://github.com/taskforcesh/bullmq/commit/544fc7c9e4755e6b62b82216e25c0cb62734ed59))

### [5.31.1](https://github.com/taskforcesh/bullmq/compare/v5.31.0...v5.31.1) (2024-12-04)

#### Bug Fixes

* **scheduler-template:** remove console.log when getting template information ([#2950](https://github.com/taskforcesh/bullmq/issues/2950)) ([3402bfe](https://github.com/taskforcesh/bullmq/commit/3402bfe0d01e5e5205db74d2106cd19d7df53fcb))

## [5.31.0](https://github.com/taskforcesh/bullmq/compare/v5.30.1...v5.31.0) (2024-12-02)

#### Features

* **queue:** enhance getJobScheduler method to include template information ([#2929](https://github.com/taskforcesh/bullmq/issues/2929)) ref [#2875](https://github.com/taskforcesh/bullmq/issues/2875) ([cb99080](https://github.com/taskforcesh/bullmq/commit/cb990808db19dd79b5048ee99308fa7d1eaa2e9f))

### [5.30.1](https://github.com/taskforcesh/bullmq/compare/v5.30.0...v5.30.1) (2024-11-30)

#### Bug Fixes

* **flow:** allow using removeOnFail and failParentOnFailure in parents ([#2947](https://github.com/taskforcesh/bullmq/issues/2947)) fixes [#2229](https://github.com/taskforcesh/bullmq/issues/2229) ([85f6f6f](https://github.com/taskforcesh/bullmq/commit/85f6f6f181003fafbf75304a268170f0d271ccc3))

## [5.30.0](https://github.com/taskforcesh/bullmq/compare/v5.29.1...v5.30.0) (2024-11-29)

#### Bug Fixes

* **job-scheduler:** upsert template when same pattern options are provided ([#2943](https://github.com/taskforcesh/bullmq/issues/2943)) ref [#2940](https://github.com/taskforcesh/bullmq/issues/2940) ([b56c3b4](https://github.com/taskforcesh/bullmq/commit/b56c3b45a87e52f5faf25406a2b992d1bfed4900))

#### Features

* **queue:** add getJobSchedulersCount method ([#2945](https://github.com/taskforcesh/bullmq/issues/2945)) ([38820dc](https://github.com/taskforcesh/bullmq/commit/38820dc8c267c616ada9931198e9e3e9d2f0d536))

### [5.29.1](https://github.com/taskforcesh/bullmq/compare/v5.29.0...v5.29.1) (2024-11-23)

#### Bug Fixes

* **scheduler:** remove deprecation warning on immediately option ([#2923](https://github.com/taskforcesh/bullmq/issues/2923)) ([14ca7f4](https://github.com/taskforcesh/bullmq/commit/14ca7f44f31a393a8b6d0ce4ed244e0063198879))

## [5.29.0](https://github.com/taskforcesh/bullmq/compare/v5.28.2...v5.29.0) (2024-11-22)

#### Features

* **queue:** refactor a protected addJob method allowing telemetry extensions ([09f2571](https://github.com/taskforcesh/bullmq/commit/09f257196f6d5a6690edbf55f12d585cec86ee8f))

### [5.28.2](https://github.com/taskforcesh/bullmq/compare/v5.28.1...v5.28.2) (2024-11-22)

#### Bug Fixes

* **queue:** change \_jobScheduler from private to protected for extension ([#2920](https://github.com/taskforcesh/bullmq/issues/2920)) ([34c2348](https://github.com/taskforcesh/bullmq/commit/34c23485bcb32b3c69046b2fb37e5db8927561ce))

### [5.28.1](https://github.com/taskforcesh/bullmq/compare/v5.28.0...v5.28.1) (2024-11-20)

#### Bug Fixes

* **scheduler:** use Job class from getter for extension ([#2917](https://github.com/taskforcesh/bullmq/issues/2917)) ([5fbb075](https://github.com/taskforcesh/bullmq/commit/5fbb075dd4abd51cc84a59575261de84e56633d8))

## [5.28.0](https://github.com/taskforcesh/bullmq/compare/v5.27.0...v5.28.0) (2024-11-19)

#### Features

* **job-scheduler:** add telemetry support to the job scheduler ([72ea950](https://github.com/taskforcesh/bullmq/commit/72ea950ea251aa12f879ba19c0b5dfeb6a093da2))

## [5.27.0](https://github.com/taskforcesh/bullmq/compare/v5.26.2...v5.27.0) (2024-11-19)

#### Features

* **queue:** add rateLimit method ([#2896](https://github.com/taskforcesh/bullmq/issues/2896)) ([db84ad5](https://github.com/taskforcesh/bullmq/commit/db84ad51a945c754c3cd03e5e718cd8d0341a8b4))
* **queue:** add removeRateLimitKey method ([#2806](https://github.com/taskforcesh/bullmq/issues/2806)) ([ff70613](https://github.com/taskforcesh/bullmq/commit/ff706131bf642fb7544b9d15994d75b1edcb27dc))

#### Performance Improvements

* **marker:** add base markers while consuming jobs to get workers busy ([#2904](https://github.com/taskforcesh/bullmq/issues/2904)) fixes [#2842](https://github.com/taskforcesh/bullmq/issues/2842) ([1759c8b](https://github.com/taskforcesh/bullmq/commit/1759c8bc111cab9e43d5fccb4d8d2dccc9c39fb4))

### [5.26.2](https://github.com/taskforcesh/bullmq/compare/v5.26.1...v5.26.2) (2024-11-15)

#### Bug Fixes

* **telemetry:** do not set span on parent context if undefined ([c417a23](https://github.com/taskforcesh/bullmq/commit/c417a23bb28d9effa42115e954b18cc41c1fc043))

### [5.26.1](https://github.com/taskforcesh/bullmq/compare/v5.26.0...v5.26.1) (2024-11-14)

#### Bug Fixes

* **queue:** fix generics to be able to properly be extended ([f2495e5](https://github.com/taskforcesh/bullmq/commit/f2495e5ee9ecdb26492da510dc38730718cb28c5))

## [5.26.0](https://github.com/taskforcesh/bullmq/compare/v5.25.6...v5.26.0) (2024-11-14)

#### Features

* improve queue getters to use generic job type ([#2905](https://github.com/taskforcesh/bullmq/issues/2905)) ([c9531ec](https://github.com/taskforcesh/bullmq/commit/c9531ec7a49126a017611eb2fd2eaea8fcb5ada5))

### [5.25.6](https://github.com/taskforcesh/bullmq/compare/v5.25.5...v5.25.6) (2024-11-11)

#### Bug Fixes

* **job-scheculer:** avoid hazards when upserting job schedulers concurrently ([022f7b7](https://github.com/taskforcesh/bullmq/commit/022f7b7d0a0ce14387ed2b9fed791e1f56e34770))

### [5.25.5](https://github.com/taskforcesh/bullmq/compare/v5.25.4...v5.25.5) (2024-11-11)

#### Bug Fixes

* **connection:** do not allow to set blockingConnection option ([#2851](https://github.com/taskforcesh/bullmq/issues/2851)) ([9391cc2](https://github.com/taskforcesh/bullmq/commit/9391cc22200914ecc8958972ebc580862a70f63c))

### [5.25.4](https://github.com/taskforcesh/bullmq/compare/v5.25.3...v5.25.4) (2024-11-10)

#### Bug Fixes

* **repeatable:** only apply immediately in the first iteration ([f69cfbc](https://github.com/taskforcesh/bullmq/commit/f69cfbcbc5516a854adbbc29b259d08e65a19705))

### [5.25.3](https://github.com/taskforcesh/bullmq/compare/v5.25.2...v5.25.3) (2024-11-08)

#### Bug Fixes

* **scripts:** set package version by default for extension ([#2887](https://github.com/taskforcesh/bullmq/issues/2887)) ([b955340](https://github.com/taskforcesh/bullmq/commit/b955340b940e4c1e330445526cd572e0ab25daa9))

### [5.25.2](https://github.com/taskforcesh/bullmq/compare/v5.25.1...v5.25.2) (2024-11-08)

#### Bug Fixes

* **worker:** allow retrieving concurrency value ([#2883](https://github.com/taskforcesh/bullmq/issues/2883)) fixes [#2880](https://github.com/taskforcesh/bullmq/issues/2880) ([52f6317](https://github.com/taskforcesh/bullmq/commit/52f6317ecd2080a5c9684a4fe384e20d86f21de4))

### [5.25.1](https://github.com/taskforcesh/bullmq/compare/v5.25.0...v5.25.1) (2024-11-07)

#### Bug Fixes

* **connection:** set packageVersion as protected attribute for extension ([#2884](https://github.com/taskforcesh/bullmq/issues/2884)) ([411ccae](https://github.com/taskforcesh/bullmq/commit/411ccae9419e008d916be6cf71c4d57dd2a07b2b))

## [5.25.0](https://github.com/taskforcesh/bullmq/compare/v5.24.0...v5.25.0) (2024-11-06)

#### Features

* **queue-events:** add QueueEventsProducer for publishing custom events ([#2844](https://github.com/taskforcesh/bullmq/issues/2844)) ([5eb03cd](https://github.com/taskforcesh/bullmq/commit/5eb03cd7f27027191eb4bc4ed7386755fd9be1fb))

## [5.24.0](https://github.com/taskforcesh/bullmq/compare/v5.23.1...v5.24.0) (2024-11-05)

#### Features

* **flows:** add telemetry support ([#2879](https://github.com/taskforcesh/bullmq/issues/2879)) ([5ed154b](https://github.com/taskforcesh/bullmq/commit/5ed154ba240dbe9eb5c22e27ad02e851c0f3cf69))

### [5.23.1](https://github.com/taskforcesh/bullmq/compare/v5.23.0...v5.23.1) (2024-11-05)

#### Bug Fixes

* **deps:** bump msgpackr to 1.1.2 to resolve ERR\_BUFFER\_OUT\_OF\_BOUNDS error ([#2882](https://github.com/taskforcesh/bullmq/issues/2882)) ref [#2747](https://github.com/taskforcesh/bullmq/issues/2747) ([4d2136c](https://github.com/taskforcesh/bullmq/commit/4d2136cc6ba340e511a539c130c9a739fe1055d0))

## [5.23.0](https://github.com/taskforcesh/bullmq/compare/v5.22.0...v5.23.0) (2024-11-02)

#### Features

* **scheduler:** add getJobScheduler method ([#2877](https://github.com/taskforcesh/bullmq/issues/2877)) ref [#2875](https://github.com/taskforcesh/bullmq/issues/2875) ([956d98c](https://github.com/taskforcesh/bullmq/commit/956d98c6890484742bb080919c70692234f28c69))

## [5.22.0](https://github.com/taskforcesh/bullmq/compare/v5.21.2...v5.22.0) (2024-10-31)

#### Features

* **queue:** add a telemetry interface ([#2721](https://github.com/taskforcesh/bullmq/issues/2721)) ([273b574](https://github.com/taskforcesh/bullmq/commit/273b574e6b5628680990eb02e1930809c9cba5bb))

### [5.21.2](https://github.com/taskforcesh/bullmq/compare/v5.21.1...v5.21.2) (2024-10-22)

#### Bug Fixes

* proper way to get version ([b4e25c1](https://github.com/taskforcesh/bullmq/commit/b4e25c13cafc001748ee6eb590133feb8ee24d7b))

### [5.21.1](https://github.com/taskforcesh/bullmq/compare/v5.21.0...v5.21.1) (2024-10-18)

#### Bug Fixes

* **scripts:** add missing wait in isJobInList ([9ef865c](https://github.com/taskforcesh/bullmq/commit/9ef865c7de6086cb3c906721fd046aeed1e0d27f))

## [5.21.0](https://github.com/taskforcesh/bullmq/compare/v5.20.1...v5.21.0) (2024-10-18)

#### Features

* **queue:** add option to skip metas update ([b7dd925](https://github.com/taskforcesh/bullmq/commit/b7dd925e7f2a4468c98a05f3a3ca1a476482b6c0))

### [5.20.1](https://github.com/taskforcesh/bullmq/compare/v5.20.0...v5.20.1) (2024-10-18)

#### Bug Fixes

* **redis:** use version for naming loaded lua scripts ([fe73f6d](https://github.com/taskforcesh/bullmq/commit/fe73f6d4d776dc9f99ad3a094e5c59c5fafc96f1))

## [5.20.0](https://github.com/taskforcesh/bullmq/compare/v5.19.1...v5.20.0) (2024-10-13)

#### Features

* **queue:** add queue version support ([#2822](https://github.com/taskforcesh/bullmq/issues/2822)) ([3a4781b](https://github.com/taskforcesh/bullmq/commit/3a4781bf7cadf04f6a324871654eed8f01cdadae))

### [5.19.1](https://github.com/taskforcesh/bullmq/compare/v5.19.0...v5.19.1) (2024-10-12)

#### Bug Fixes

* **sandbox:** fix serialization of error with circular references are present ([#2815](https://github.com/taskforcesh/bullmq/issues/2815)) fix [#2813](https://github.com/taskforcesh/bullmq/issues/2813) ([a384d92](https://github.com/taskforcesh/bullmq/commit/a384d926bee15bffa84178a8fad7b94a6a08b572))

## [5.19.0](https://github.com/taskforcesh/bullmq/compare/v5.18.0...v5.19.0) (2024-10-11)

#### Features

* **repeat:** deprecate immediately on job scheduler ([ed047f7](https://github.com/taskforcesh/bullmq/commit/ed047f7ab69ebdb445343b6cb325e90b95ee9dc5))

## [5.18.0](https://github.com/taskforcesh/bullmq/compare/v5.17.1...v5.18.0) (2024-10-09)

#### Features

* **job:** expose priority value ([#2804](https://github.com/taskforcesh/bullmq/issues/2804)) ([9abec3d](https://github.com/taskforcesh/bullmq/commit/9abec3dbc4c69f2496c5ff6b5d724f4d1a5ca62f))

### [5.17.1](https://github.com/taskforcesh/bullmq/compare/v5.17.0...v5.17.1) (2024-10-07)

#### Bug Fixes

* **repeat:** also consider startDate when using "every" ([25bbaa8](https://github.com/taskforcesh/bullmq/commit/25bbaa81af87f9944a64bc4fb7e0c76ef223ada4))

## [5.17.0](https://github.com/taskforcesh/bullmq/compare/v5.16.0...v5.17.0) (2024-10-07)

#### Bug Fixes

* **sandbox:** catch exit errors ([#2800](https://github.com/taskforcesh/bullmq/issues/2800)) ([6babb9e](https://github.com/taskforcesh/bullmq/commit/6babb9e2f355feaf9bd1a8ed229c1001e6de7144))

#### Features

* **job:** add deduplication logic ([#2796](https://github.com/taskforcesh/bullmq/issues/2796)) ([0a4982d](https://github.com/taskforcesh/bullmq/commit/0a4982d05d27c066248290ab9f59349b802d02d5))

## [5.16.0](https://github.com/taskforcesh/bullmq/compare/v5.15.0...v5.16.0) (2024-10-06)

#### Features

* **queue:** add new upsertJobScheduler, getJobSchedulers and removeJobSchedulers methods ([dd6b6b2](https://github.com/taskforcesh/bullmq/commit/dd6b6b2263badd8f29db65d1fa6bcdf5a1e9f6e2))

## [5.15.0](https://github.com/taskforcesh/bullmq/compare/v5.14.0...v5.15.0) (2024-10-01)

#### Features

* **worker-fork:** allow passing fork options ([#2795](https://github.com/taskforcesh/bullmq/issues/2795)) ([f7a4292](https://github.com/taskforcesh/bullmq/commit/f7a4292e064b41236f4489b3d7785a4c599a6435))

## [5.14.0](https://github.com/taskforcesh/bullmq/compare/v5.13.2...v5.14.0) (2024-09-30)

#### Features

* **worker-thread:** allow passing Worker options ([#2791](https://github.com/taskforcesh/bullmq/issues/2791)) ref [#1555](https://github.com/taskforcesh/bullmq/issues/1555) ([6a1f7a9](https://github.com/taskforcesh/bullmq/commit/6a1f7a9f0303561d6ec7b2005ba0227132b89e07))

### [5.13.2](https://github.com/taskforcesh/bullmq/compare/v5.13.1...v5.13.2) (2024-09-20)

#### Bug Fixes

* **repeatable:** avoid delayed job deletion if next job already existed ([#2778](https://github.com/taskforcesh/bullmq/issues/2778)) ([6a851c1](https://github.com/taskforcesh/bullmq/commit/6a851c1140b336f0e458b6dfe1022470ac41fceb))

### [5.13.1](https://github.com/taskforcesh/bullmq/compare/v5.13.0...v5.13.1) (2024-09-18)

#### Bug Fixes

* **connection:** allow passing connection string into IORedis ([#2746](https://github.com/taskforcesh/bullmq/issues/2746)) ([73005e8](https://github.com/taskforcesh/bullmq/commit/73005e8583110f43914df879aef3481b42f3b3af))

## [5.13.0](https://github.com/taskforcesh/bullmq/compare/v5.12.15...v5.13.0) (2024-09-11)

#### Features

* **queue:** add getDebounceJobId method ([#2717](https://github.com/taskforcesh/bullmq/issues/2717)) ([a68ead9](https://github.com/taskforcesh/bullmq/commit/a68ead95f32a7d9dabba602895d05c22794b2c02))

### [5.12.15](https://github.com/taskforcesh/bullmq/compare/v5.12.14...v5.12.15) (2024-09-10)

#### Bug Fixes

* **metrics:** differentiate points in different minutes to be more accurate ([#2766](https://github.com/taskforcesh/bullmq/issues/2766)) (python) ([7cb670e](https://github.com/taskforcesh/bullmq/commit/7cb670e1bf9560a24de3da52427b4f6b6152a59a))
* **pattern:** do not save offset when immediately is provided ([#2756](https://github.com/taskforcesh/bullmq/issues/2756)) ([a8cb8a2](https://github.com/taskforcesh/bullmq/commit/a8cb8a21ea52437ac507097994ef0fde058c5433))

### [5.12.14](https://github.com/taskforcesh/bullmq/compare/v5.12.13...v5.12.14) (2024-09-05)

#### Performance Improvements

* **metrics:** save zeros as much as max data points ([#2758](https://github.com/taskforcesh/bullmq/issues/2758)) ([3473054](https://github.com/taskforcesh/bullmq/commit/347305451a9f5d7f2c16733eb139b5de96ea4b9c))

### [5.12.13](https://github.com/taskforcesh/bullmq/compare/v5.12.12...v5.12.13) (2024-09-03)

#### Bug Fixes

* **repeat:** replace delayed job when updating repeat key ([88029bb](https://github.com/taskforcesh/bullmq/commit/88029bbeab2a58768f9c438318f540010cd286a7))

### [5.12.12](https://github.com/taskforcesh/bullmq/compare/v5.12.11...v5.12.12) (2024-08-29)

#### Bug Fixes

* **flows:** throw error when queueName contains colon ([#2719](https://github.com/taskforcesh/bullmq/issues/2719)) fixes [#2718](https://github.com/taskforcesh/bullmq/issues/2718) ([9ef97c3](https://github.com/taskforcesh/bullmq/commit/9ef97c37663e209f03c501a357b6b1a662b24d99))

### [5.12.11](https://github.com/taskforcesh/bullmq/compare/v5.12.10...v5.12.11) (2024-08-28)

#### Bug Fixes

* **sandboxed:** properly update data on wrapped job ([#2739](https://github.com/taskforcesh/bullmq/issues/2739)) fixes [#2731](https://github.com/taskforcesh/bullmq/issues/2731) ([9c4b245](https://github.com/taskforcesh/bullmq/commit/9c4b2454025a14459de47b0586a09130d7a93cae))

### [5.12.10](https://github.com/taskforcesh/bullmq/compare/v5.12.9...v5.12.10) (2024-08-22)

#### Bug Fixes

* **flow:** remove debounce key when parent is moved to fail ([#2720](https://github.com/taskforcesh/bullmq/issues/2720)) ([d51aabe](https://github.com/taskforcesh/bullmq/commit/d51aabe999a489c285f871d21e36c3c84e2bef33))

### [5.12.9](https://github.com/taskforcesh/bullmq/compare/v5.12.8...v5.12.9) (2024-08-17)

#### Performance Improvements

* **fifo-queue:** use linked list structure for queue ([#2629](https://github.com/taskforcesh/bullmq/issues/2629)) ([df74578](https://github.com/taskforcesh/bullmq/commit/df7457844a769e5644eb11d31d1a05a9d5b4e084))

### [5.12.8](https://github.com/taskforcesh/bullmq/compare/v5.12.7...v5.12.8) (2024-08-17)

#### Bug Fixes

* **flow:** recursive ignoreDependencyOnFailure option ([#2712](https://github.com/taskforcesh/bullmq/issues/2712)) ([53bc9eb](https://github.com/taskforcesh/bullmq/commit/53bc9eb68b5bb0a470a8fe64ef78ece5cde44632))

### [5.12.7](https://github.com/taskforcesh/bullmq/compare/v5.12.6...v5.12.7) (2024-08-16)

#### Bug Fixes

* **job:** throw error if removeDependencyOnFailure and ignoreDependencyOnFailure are used together ([#2711](https://github.com/taskforcesh/bullmq/issues/2711)) ([967632c](https://github.com/taskforcesh/bullmq/commit/967632c9ef8468aab59f0b36d1d828bcde1fbd70))

### [5.12.6](https://github.com/taskforcesh/bullmq/compare/v5.12.5...v5.12.6) (2024-08-14)

#### Bug Fixes

* **job:** change moveToFinished return type to reflect jobData ([#2706](https://github.com/taskforcesh/bullmq/issues/2706)) ref [#2342](https://github.com/taskforcesh/bullmq/issues/2342) ([de094a3](https://github.com/taskforcesh/bullmq/commit/de094a361a25886acbee0112bb4341c6b285b1c9))
* **stalled:** support removeDependencyOnFailure option when job is stalled ([#2708](https://github.com/taskforcesh/bullmq/issues/2708)) ([e0d3790](https://github.com/taskforcesh/bullmq/commit/e0d3790e755c4dfe31006b52f177f08b40348e61))

### [5.12.5](https://github.com/taskforcesh/bullmq/compare/v5.12.4...v5.12.5) (2024-08-13)

#### Bug Fixes

* **connection:** remove unnecessary process.env.CI reference ([#2705](https://github.com/taskforcesh/bullmq/issues/2705)) ([53de304](https://github.com/taskforcesh/bullmq/commit/53de3049493ef79e02af40e8e450e2056c134155))

### [5.12.4](https://github.com/taskforcesh/bullmq/compare/v5.12.3...v5.12.4) (2024-08-12)

#### Bug Fixes

* **worker:** fix close sequence to reduce risk for open handlers ([#2656](https://github.com/taskforcesh/bullmq/issues/2656)) ([8468e44](https://github.com/taskforcesh/bullmq/commit/8468e44e5e9e39c7b65691945c26688a9e5d2275))

### [5.12.3](https://github.com/taskforcesh/bullmq/compare/v5.12.2...v5.12.3) (2024-08-10)

#### Bug Fixes

* **flow:** validate parentData before ignoreDependencyOnFailure when stalled check happens ([#2702](https://github.com/taskforcesh/bullmq/issues/2702)) (python) ([9416501](https://github.com/taskforcesh/bullmq/commit/9416501551b1ad464e59bdba1045a5a9955e2ea4))

### [5.12.2](https://github.com/taskforcesh/bullmq/compare/v5.12.1...v5.12.2) (2024-08-09)

#### Performance Improvements

* **worker:** promote delayed jobs while queue is rate limited ([#2697](https://github.com/taskforcesh/bullmq/issues/2697)) ref [#2582](https://github.com/taskforcesh/bullmq/issues/2582) ([f3290ac](https://github.com/taskforcesh/bullmq/commit/f3290ace2f117e26357f9fae611a255af26b950b))

### [5.12.1](https://github.com/taskforcesh/bullmq/compare/v5.12.0...v5.12.1) (2024-08-07)

#### Bug Fixes

* **job:** consider passing stackTraceLimit as 0 ([#2692](https://github.com/taskforcesh/bullmq/issues/2692)) ref [#2487](https://github.com/taskforcesh/bullmq/issues/2487) ([509a36b](https://github.com/taskforcesh/bullmq/commit/509a36baf8d8cf37176e406fd28e33f712229d27))

## [5.12.0](https://github.com/taskforcesh/bullmq/compare/v5.11.0...v5.12.0) (2024-08-01)

#### Features

* **queue-events:** pass debounceId as a param of debounced event ([#2678](https://github.com/taskforcesh/bullmq/issues/2678)) ([97fb97a](https://github.com/taskforcesh/bullmq/commit/97fb97a054d6cebbe1d7ff1cb5c46d7da1c018d8))

## [5.11.0](https://github.com/taskforcesh/bullmq/compare/v5.10.4...v5.11.0) (2024-07-29)

#### Features

* **job:** allow passing debounce as option ([#2666](https://github.com/taskforcesh/bullmq/issues/2666)) ([163ccea](https://github.com/taskforcesh/bullmq/commit/163ccea19ef48191c4db6da27638ff6fb0080a74))

### [5.10.4](https://github.com/taskforcesh/bullmq/compare/v5.10.3...v5.10.4) (2024-07-26)

#### Bug Fixes

* **repeatable:** remove repeat hash when removing repeatable job ([#2676](https://github.com/taskforcesh/bullmq/issues/2676)) ([97a297d](https://github.com/taskforcesh/bullmq/commit/97a297d90ad8b27bcddb7db6a8a158acfb549389))

### [5.10.3](https://github.com/taskforcesh/bullmq/compare/v5.10.2...v5.10.3) (2024-07-19)

#### Bug Fixes

* **repeatable:** keep legacy repeatables if it exists instead of creating one with new structure ([#2665](https://github.com/taskforcesh/bullmq/issues/2665)) ([93fad41](https://github.com/taskforcesh/bullmq/commit/93fad41a9520961d0e6814d82454bc916a039501))

### [5.10.2](https://github.com/taskforcesh/bullmq/compare/v5.10.1...v5.10.2) (2024-07-19)

#### Performance Improvements

* **worker:** fetch next job on failure ([#2342](https://github.com/taskforcesh/bullmq/issues/2342)) ([f917b80](https://github.com/taskforcesh/bullmq/commit/f917b8090f306c0580aac12f6bd4394fd9ef003d))

### [5.10.1](https://github.com/taskforcesh/bullmq/compare/v5.10.0...v5.10.1) (2024-07-18)

#### Bug Fixes

* **repeatable:** consider removing legacy repeatable job ([#2658](https://github.com/taskforcesh/bullmq/issues/2658)) fixes [#2661](https://github.com/taskforcesh/bullmq/issues/2661) ([a6764ae](https://github.com/taskforcesh/bullmq/commit/a6764aecb557fb918d061f5e5c2e26e4afa3e8ee))
* **repeatable:** pass custom key as an args in addRepeatableJob to prevent CROSSSLOT issue ([#2662](https://github.com/taskforcesh/bullmq/issues/2662)) fixes [#2660](https://github.com/taskforcesh/bullmq/issues/2660) ([9d8f874](https://github.com/taskforcesh/bullmq/commit/9d8f874b959e09662985f38c4614b95ab4d5e89c))

## [5.10.0](https://github.com/taskforcesh/bullmq/compare/v5.9.0...v5.10.0) (2024-07-16)

#### Features

* **repeatable:** new repeatables structure ([#2617](https://github.com/taskforcesh/bullmq/issues/2617)) ref [#2612](https://github.com/taskforcesh/bullmq/issues/2612) fixes [#2399](https://github.com/taskforcesh/bullmq/issues/2399) [#2596](https://github.com/taskforcesh/bullmq/issues/2596) ([8376a9a](https://github.com/taskforcesh/bullmq/commit/8376a9a9007f58ac7eab1a3a1c2f9e7ec373bbd6))

## [5.9.0](https://github.com/taskforcesh/bullmq/compare/v5.8.7...v5.9.0) (2024-07-15)

#### Features

* **queue:** support global concurrency ([#2496](https://github.com/taskforcesh/bullmq/issues/2496)) ref [#2465](https://github.com/taskforcesh/bullmq/issues/2465) ([47ba055](https://github.com/taskforcesh/bullmq/commit/47ba055c1ea36178b684fd11c1e82cde7ec93ac8))

### [5.8.7](https://github.com/taskforcesh/bullmq/compare/v5.8.6...v5.8.7) (2024-07-11)

#### Performance Improvements

* **delayed:** keep moving delayed jobs to waiting when queue is paused ([#2640](https://github.com/taskforcesh/bullmq/issues/2640)) (python) ([b89e2e0](https://github.com/taskforcesh/bullmq/commit/b89e2e0913c0886561fc1c2470771232f17f5b3b))

### [5.8.6](https://github.com/taskforcesh/bullmq/compare/v5.8.5...v5.8.6) (2024-07-11)

#### Bug Fixes

* **delayed:** avoid using jobId in order to schedule delayed jobs ([#2587](https://github.com/taskforcesh/bullmq/issues/2587)) (python) ([228db2c](https://github.com/taskforcesh/bullmq/commit/228db2c780a1ca8323900fc568156495a13355a3))

### [5.8.5](https://github.com/taskforcesh/bullmq/compare/v5.8.4...v5.8.5) (2024-07-10)

#### Bug Fixes

* **parent:** consider re-adding child that is in completed state using same jobIds ([#2627](https://github.com/taskforcesh/bullmq/issues/2627)) (python) fixes [#2554](https://github.com/taskforcesh/bullmq/issues/2554) ([00cd017](https://github.com/taskforcesh/bullmq/commit/00cd0174539fbe1cc4628b9b6e1a7eb87a5ef705))

### [5.8.4](https://github.com/taskforcesh/bullmq/compare/v5.8.3...v5.8.4) (2024-07-05)

#### Bug Fixes

* **queue-getters:** consider passing maxJobs when calling getRateLimitTtl ([#2631](https://github.com/taskforcesh/bullmq/issues/2631)) fixes [#2628](https://github.com/taskforcesh/bullmq/issues/2628) ([9f6609a](https://github.com/taskforcesh/bullmq/commit/9f6609ab1856c473b2d5cf0710068ce2751d708e))

### [5.8.3](https://github.com/taskforcesh/bullmq/compare/v5.8.2...v5.8.3) (2024-06-28)

#### Bug Fixes

* **job:** consider changing priority to 0 ([#2599](https://github.com/taskforcesh/bullmq/issues/2599)) ([4dba122](https://github.com/taskforcesh/bullmq/commit/4dba122174ab5173315fca7fdbb7454761514a53))

### [5.8.2](https://github.com/taskforcesh/bullmq/compare/v5.8.1...v5.8.2) (2024-06-15)

#### Bug Fixes

* **priority:** consider paused state when calling getCountsPerPriority (python) ([#2609](https://github.com/taskforcesh/bullmq/issues/2609)) ([6e99250](https://github.com/taskforcesh/bullmq/commit/6e992504b2a7a2fa76f1d04ad53d1512e98add7f))

### [5.8.1](https://github.com/taskforcesh/bullmq/compare/v5.8.0...v5.8.1) (2024-06-12)

#### Bug Fixes

* **priority:** use module instead of bit.band to keep order (python) ([#2597](https://github.com/taskforcesh/bullmq/issues/2597)) ([9ece15b](https://github.com/taskforcesh/bullmq/commit/9ece15b17420fe0bee948a5307e870915e3bce87))

## [5.8.0](https://github.com/taskforcesh/bullmq/compare/v5.7.15...v5.8.0) (2024-06-11)

#### Features

* **queue:** add getCountsPerPriority method ([#2595](https://github.com/taskforcesh/bullmq/issues/2595)) ([77971f4](https://github.com/taskforcesh/bullmq/commit/77971f42b9fc425ad66e0b581e800ea429fc254e))

### [5.7.15](https://github.com/taskforcesh/bullmq/compare/v5.7.14...v5.7.15) (2024-06-04)

#### Performance Improvements

* **job:** set processedBy using hmset ([#2592](https://github.com/taskforcesh/bullmq/issues/2592)) (python) ([238680b](https://github.com/taskforcesh/bullmq/commit/238680b84593690a73d542dbe1120611c3508b47))

### [5.7.14](https://github.com/taskforcesh/bullmq/compare/v5.7.13...v5.7.14) (2024-05-29)

#### Bug Fixes

* **worker:** properly cancel blocking command during disconnections ([2cf12b3](https://github.com/taskforcesh/bullmq/commit/2cf12b3622b0517f645971ece8acdcf673bede97))

### [5.7.13](https://github.com/taskforcesh/bullmq/compare/v5.7.12...v5.7.13) (2024-05-28)

#### Bug Fixes

* extendlock, createbulk use pipeline no multi command ([#2584](https://github.com/taskforcesh/bullmq/pull/2584)) ([a053d9b](https://github.com/taskforcesh/bullmq/commit/a053d9b87e9799b151e2563b499dbff309b9d2e5))

### [5.7.12](https://github.com/taskforcesh/bullmq/compare/v5.7.11...v5.7.12) (2024-05-24)

#### Bug Fixes

* **repeat:** throw error when endDate is pointing to the past ([#2574](https://github.com/taskforcesh/bullmq/issues/2574)) ([5bd7990](https://github.com/taskforcesh/bullmq/commit/5bd79900ea3ace8ec6aa00525aff81a345f8e18e))

### [5.7.11](https://github.com/taskforcesh/bullmq/compare/v5.7.10...v5.7.11) (2024-05-23)

#### Bug Fixes

* **retry-job:** throw error when job is not in active state ([#2576](https://github.com/taskforcesh/bullmq/issues/2576)) ([ca207f5](https://github.com/taskforcesh/bullmq/commit/ca207f593d0ed455ecc59d9e0ef389a9a50d9634))

### [5.7.10](https://github.com/taskforcesh/bullmq/compare/v5.7.9...v5.7.10) (2024-05-21)

#### Bug Fixes

* **sandboxed:** ensure DelayedError is checked in Sandboxed processors ([#2567](https://github.com/taskforcesh/bullmq/issues/2567)) fixes [#2566](https://github.com/taskforcesh/bullmq/issues/2566) ([8158fa1](https://github.com/taskforcesh/bullmq/commit/8158fa114f57619b31f101bc8d0688a09c6218bb))

### [5.7.9](https://github.com/taskforcesh/bullmq/compare/v5.7.8...v5.7.9) (2024-05-16)

#### Bug Fixes

* **job:** validate job existence when adding a log ([#2562](https://github.com/taskforcesh/bullmq/issues/2562)) ([f87e3fe](https://github.com/taskforcesh/bullmq/commit/f87e3fe029e48d8964722da762326e531c2256ee))

### [5.7.8](https://github.com/taskforcesh/bullmq/compare/v5.7.7...v5.7.8) (2024-05-01)

#### Bug Fixes

* **worker:** make sure clearTimeout is always called after bzpopmin ([782382e](https://github.com/taskforcesh/bullmq/commit/782382e599218024bb9912ff0572c4aa9b1f22a3))

### [5.7.7](https://github.com/taskforcesh/bullmq/compare/v5.7.6...v5.7.7) (2024-04-30)

#### Bug Fixes

* **worker:** force timeout on bzpopmin command ([#2543](https://github.com/taskforcesh/bullmq/issues/2543)) ([ae7cb6c](https://github.com/taskforcesh/bullmq/commit/ae7cb6caefdbfa5ca0d28589cef4b896ffcce2db))

### [5.7.6](https://github.com/taskforcesh/bullmq/compare/v5.7.5...v5.7.6) (2024-04-27)

#### Performance Improvements

* **worker:** do not call bzpopmin when blockDelay is lower or equal 0 ([#2544](https://github.com/taskforcesh/bullmq/issues/2544)) ref [#2466](https://github.com/taskforcesh/bullmq/issues/2466) ([9760b85](https://github.com/taskforcesh/bullmq/commit/9760b85dfbcc9b3c744f616961ef939e8951321d))

### [5.7.5](https://github.com/taskforcesh/bullmq/compare/v5.7.4...v5.7.5) (2024-04-24)

#### Bug Fixes

* **stalled:** consider ignoreDependencyOnFailure option (python) ([#2540](https://github.com/taskforcesh/bullmq/issues/2540)) fixes [#2531](https://github.com/taskforcesh/bullmq/issues/2531) ([0140959](https://github.com/taskforcesh/bullmq/commit/0140959cabd2613794631e41ebe4c2ddee6f91da))

### [5.7.4](https://github.com/taskforcesh/bullmq/compare/v5.7.3...v5.7.4) (2024-04-21)

#### Performance Improvements

* **worker:** reset delays after generating blockTimeout value ([#2529](https://github.com/taskforcesh/bullmq/issues/2529)) ([e92cea4](https://github.com/taskforcesh/bullmq/commit/e92cea4a9d7c99f649f6626d1c0a1e1e994179d6))

### [5.7.3](https://github.com/taskforcesh/bullmq/compare/v5.7.2...v5.7.3) (2024-04-20)

#### Bug Fixes

* **worker:** return minimumBlockTimeout depending on redis version (python) ([#2532](https://github.com/taskforcesh/bullmq/issues/2532)) ([83dfb63](https://github.com/taskforcesh/bullmq/commit/83dfb63e72a1a36a4dfc40f122efb54fbb796339))

### [5.7.2](https://github.com/taskforcesh/bullmq/compare/v5.7.1...v5.7.2) (2024-04-18)

#### Bug Fixes

* **stalled:** consider failParentOnFailure when moving child into failed ([#2526](https://github.com/taskforcesh/bullmq/issues/2526)) fixes [#2464](https://github.com/taskforcesh/bullmq/issues/2464) (python) ([5e31eb0](https://github.com/taskforcesh/bullmq/commit/5e31eb096169ea57350db591bcebfc2264a6b6dc))

### [5.7.1](https://github.com/taskforcesh/bullmq/compare/v5.7.0...v5.7.1) (2024-04-10)

#### Bug Fixes

* **worker:** use 0.002 as minimum timeout for redis version lower than 7.0.8 ([#2515](https://github.com/taskforcesh/bullmq/issues/2515)) fixes [#2466](https://github.com/taskforcesh/bullmq/issues/2466) ([44f7d21](https://github.com/taskforcesh/bullmq/commit/44f7d21850747d9c636c78e08b9e577d684fb885))

## [5.7.0](https://github.com/taskforcesh/bullmq/compare/v5.6.0...v5.7.0) (2024-04-09)

#### Features

* allow arbitrary large drainDelay ([9693321](https://github.com/taskforcesh/bullmq/commit/96933217bf79658e5bb23fd7afe47e0b1150a40d))

## [5.6.0](https://github.com/taskforcesh/bullmq/compare/v5.5.4...v5.6.0) (2024-04-08)

#### Features

* Nothing changed, triggered by a python version release

### [5.5.4](https://github.com/taskforcesh/bullmq/compare/v5.5.3...v5.5.4) (2024-04-07)

#### Performance Improvements

* **stalled:** remove jobId from stalled after removing lock when moved from active ([#2512](https://github.com/taskforcesh/bullmq/issues/2512)) (python) ([64feec9](https://github.com/taskforcesh/bullmq/commit/64feec91b0b034fe640a846166bd95b546ff6d71))

### [5.5.3](https://github.com/taskforcesh/bullmq/compare/v5.5.2...v5.5.3) (2024-04-07)

#### Bug Fixes

* **deps:** remove script loader from dist as it is used only when building package ([#2503](https://github.com/taskforcesh/bullmq/issues/2503)) ([6f9ca23](https://github.com/taskforcesh/bullmq/commit/6f9ca23a400e573c3ecb97246c1dda36ce1549ec))

### [5.5.2](https://github.com/taskforcesh/bullmq/compare/v5.5.1...v5.5.2) (2024-04-06)

#### Bug Fixes

* **client:** try catch list command as it's not supported in GCP ([#2506](https://github.com/taskforcesh/bullmq/issues/2506)) ([ca68a9e](https://github.com/taskforcesh/bullmq/commit/ca68a9eff070e8dc09c484b1fb298c7afaa18f6f))

### [5.5.1](https://github.com/taskforcesh/bullmq/compare/v5.5.0...v5.5.1) (2024-04-03)

#### Bug Fixes

* **connection:** ignore error when setting custom end status ([#2473](https://github.com/taskforcesh/bullmq/issues/2473)) ([3e17e45](https://github.com/taskforcesh/bullmq/commit/3e17e459a89a6ca9bccda64c5f06f91e70b372e4))

## [5.5.0](https://github.com/taskforcesh/bullmq/compare/v5.4.6...v5.5.0) (2024-03-31)

#### Features

* **getters:** add getWorkersCount ([743c7aa](https://github.com/taskforcesh/bullmq/commit/743c7aa8f979760bc04f7b8f55844020559038e1))

### [5.4.6](https://github.com/taskforcesh/bullmq/compare/v5.4.5...v5.4.6) (2024-03-26)

#### Bug Fixes

* **job:** stack trace limit ([#2487](https://github.com/taskforcesh/bullmq/issues/2487)) ([cce3bc3](https://github.com/taskforcesh/bullmq/commit/cce3bc3092eb7cf56c2a6c68e9fd8980f5f1f26a))

### [5.4.5](https://github.com/taskforcesh/bullmq/compare/v5.4.4...v5.4.5) (2024-03-22)

#### Bug Fixes

* **scripts:** use command name in error message when moving to finished ([#2483](https://github.com/taskforcesh/bullmq/issues/2483)) ([3c335d4](https://github.com/taskforcesh/bullmq/commit/3c335d49ba637145648c1ef0864d8e0d297dd890))

### [5.4.4](https://github.com/taskforcesh/bullmq/compare/v5.4.3...v5.4.4) (2024-03-21)

#### Bug Fixes

* **queue:** use QueueOptions type in opts attribute ([#2481](https://github.com/taskforcesh/bullmq/issues/2481)) ([51a589f](https://github.com/taskforcesh/bullmq/commit/51a589f7e07b5336eb35ed00a1b795501b24f254))

### [5.4.3](https://github.com/taskforcesh/bullmq/compare/v5.4.2...v5.4.3) (2024-03-17)

#### Bug Fixes

* **worker:** validate drainDelay must be greater than 0 ([#2477](https://github.com/taskforcesh/bullmq/issues/2477)) ([ab43693](https://github.com/taskforcesh/bullmq/commit/ab436938d895125635aef0393ae2fb5c77c16c1f))

### [5.4.2](https://github.com/taskforcesh/bullmq/compare/v5.4.1...v5.4.2) (2024-03-06)

#### Bug Fixes

* move fast-glob and minimatch as dev-dependencies ([#2452](https://github.com/taskforcesh/bullmq/issues/2452)) ([cf13b31](https://github.com/taskforcesh/bullmq/commit/cf13b31ca552bcad53f40fe5668a907cf02e0a2e))

### [5.4.1](https://github.com/taskforcesh/bullmq/compare/v5.4.0...v5.4.1) (2024-03-01)

#### Bug Fixes

* **worker:** set blockTimeout as 0.001 when reach the time to get delayed jobs ([#2455](https://github.com/taskforcesh/bullmq/issues/2455)) fixes [#2450](https://github.com/taskforcesh/bullmq/issues/2450) ([2de15ca](https://github.com/taskforcesh/bullmq/commit/2de15ca1019517f7ce11f3734fff316a3e4ab894))

## [5.4.0](https://github.com/taskforcesh/bullmq/compare/v5.3.3...v5.4.0) (2024-02-27)

#### Features

* **job:** add removeChildDependency method ([#2435](https://github.com/taskforcesh/bullmq/issues/2435)) ([1151022](https://github.com/taskforcesh/bullmq/commit/1151022e4825fbb20cf1ef6ce1ff3e7fe929de5c))

### [5.3.3](https://github.com/taskforcesh/bullmq/compare/v5.3.2...v5.3.3) (2024-02-25)

#### Bug Fixes

* **deps:** replaced glob by fast-glob due to security advisory ([91cf9a9](https://github.com/taskforcesh/bullmq/commit/91cf9a9253370ea76df48c27a7e0fcf8d7504c81))

### [5.3.2](https://github.com/taskforcesh/bullmq/compare/v5.3.1...v5.3.2) (2024-02-24)

#### Bug Fixes

* **sandbox:** extend SandboxedJob from JobJsonSandbox ([#2446](https://github.com/taskforcesh/bullmq/issues/2446)) fixes [#2439](https://github.com/taskforcesh/bullmq/issues/2439) ([7606e36](https://github.com/taskforcesh/bullmq/commit/7606e3611f1cc18b1585c08b0f7fd9cb90749c9c))

### [5.3.1](https://github.com/taskforcesh/bullmq/compare/v5.3.0...v5.3.1) (2024-02-22)

#### Bug Fixes

* **add-job:** fix parent job cannot be replaced error message ([#2441](https://github.com/taskforcesh/bullmq/issues/2441)) ([1e9a13f](https://github.com/taskforcesh/bullmq/commit/1e9a13fc0dc9de810ef75a042fbfeeae5b571ffe))

## [5.3.0](https://github.com/taskforcesh/bullmq/compare/v5.2.1...v5.3.0) (2024-02-20)

#### Features

* **worker:** add support for naming workers ([7ba2729](https://github.com/taskforcesh/bullmq/commit/7ba27293615e443903cfdf7d0ff8be0052d061c4))

### [5.2.1](https://github.com/taskforcesh/bullmq/compare/v5.2.0...v5.2.1) (2024-02-17)

#### Bug Fixes

* **flow:** remove failed children references on auto removal ([#2432](https://github.com/taskforcesh/bullmq/issues/2432)) ([8a85207](https://github.com/taskforcesh/bullmq/commit/8a85207cf3c552ebab37baca3c395821b9804b37))

## [5.2.0](https://github.com/taskforcesh/bullmq/compare/v5.1.12...v5.2.0) (2024-02-17)

#### Features

* **flow:** add ignoreDependencyOnFailure option ([#2426](https://github.com/taskforcesh/bullmq/issues/2426)) ([c7559f4](https://github.com/taskforcesh/bullmq/commit/c7559f4f0a7fa51764ad43b4f46bb9d55ac42d0d))

### [5.1.12](https://github.com/taskforcesh/bullmq/compare/v5.1.11...v5.1.12) (2024-02-16)

#### Bug Fixes

* **redis-connection:** close redis connection even when initializing ([#2425](https://github.com/taskforcesh/bullmq/issues/2425)) fixes [#2385](https://github.com/taskforcesh/bullmq/issues/2385) ([1bc26a6](https://github.com/taskforcesh/bullmq/commit/1bc26a64871b85a2d1f6799a9b73b60f8bf9fa90))

### [5.1.11](https://github.com/taskforcesh/bullmq/compare/v5.1.10...v5.1.11) (2024-02-13)

#### Bug Fixes

* **flow:** parent job cannot be replaced (python) ([#2417](https://github.com/taskforcesh/bullmq/issues/2417)) ([2696ef8](https://github.com/taskforcesh/bullmq/commit/2696ef8200058b7f616938c2166a3b0454663b39))

### [5.1.10](https://github.com/taskforcesh/bullmq/compare/v5.1.9...v5.1.10) (2024-02-10)

#### Performance Improvements

* **marker:** differentiate standard and delayed markers (python) ([#2389](https://github.com/taskforcesh/bullmq/issues/2389)) ([18ebee8](https://github.com/taskforcesh/bullmq/commit/18ebee8c242f66f1b5b733d68e48c574b1f1fdef))

### [5.1.9](https://github.com/taskforcesh/bullmq/compare/v5.1.8...v5.1.9) (2024-02-05)

#### Performance Improvements

* **change-delay:** add delay marker when needed ([#2411](https://github.com/taskforcesh/bullmq/issues/2411)) ([8b62d28](https://github.com/taskforcesh/bullmq/commit/8b62d28a06347e9dd04757807fce1b511ace79bc))

### [5.1.8](https://github.com/taskforcesh/bullmq/compare/v5.1.7...v5.1.8) (2024-02-03)

#### Performance Improvements

* **flow:** add marker when moving parent to wait (python) ([#2408](https://github.com/taskforcesh/bullmq/issues/2408)) ([6fb6896](https://github.com/taskforcesh/bullmq/commit/6fb6896701ae7595e1cb5e2cdbef44625c48d673))

### [5.1.7](https://github.com/taskforcesh/bullmq/compare/v5.1.6...v5.1.7) (2024-02-02)

#### Bug Fixes

* **reprocess-job:** add marker if needed ([#2406](https://github.com/taskforcesh/bullmq/issues/2406)) ([5923ed8](https://github.com/taskforcesh/bullmq/commit/5923ed885f5451eee2f14258767d7d5f8d80ae13))

### [5.1.6](https://github.com/taskforcesh/bullmq/compare/v5.1.5...v5.1.6) (2024-01-31)

#### Bug Fixes

* **rate-limit:** move job to wait even if ttl is 0 ([#2403](https://github.com/taskforcesh/bullmq/issues/2403)) ([c1c2ccc](https://github.com/taskforcesh/bullmq/commit/c1c2cccc7c8c05591f0303e011d46f6efa0942a0))

### [5.1.5](https://github.com/taskforcesh/bullmq/compare/v5.1.4...v5.1.5) (2024-01-23)

#### Performance Improvements

* **move-to-active:** check rate limited once ([#2391](https://github.com/taskforcesh/bullmq/issues/2391)) ([ca6c17a](https://github.com/taskforcesh/bullmq/commit/ca6c17a43e38d5339e62471ea9f59c62a169b797))

### [5.1.4](https://github.com/taskforcesh/bullmq/compare/v5.1.3...v5.1.4) (2024-01-20)

#### Bug Fixes

* **stalled:** consider adding marker when moving job back to wait ([#2384](https://github.com/taskforcesh/bullmq/issues/2384)) ([4914df8](https://github.com/taskforcesh/bullmq/commit/4914df87e416711835291e81da93b279bd758254))

### [5.1.3](https://github.com/taskforcesh/bullmq/compare/v5.1.2...v5.1.3) (2024-01-16)

#### Bug Fixes

* **retry-jobs:** add marker when needed ([#2374](https://github.com/taskforcesh/bullmq/issues/2374)) ([1813d5f](https://github.com/taskforcesh/bullmq/commit/1813d5fa12b7db69ee6c8c09273729cda8e3e3b5))

### [5.1.2](https://github.com/taskforcesh/bullmq/compare/v5.1.1...v5.1.2) (2024-01-15)

#### Bug Fixes

* **security:** upgrade msgpackr <https://github.com/advisories/GHSA-7hpj-7hhx-2fgx> ([7ae0953](https://github.com/taskforcesh/bullmq/commit/7ae095357fddbdaacc286cbe5782946b95160d55))

### [5.1.1](https://github.com/taskforcesh/bullmq/compare/v5.1.0...v5.1.1) (2024-01-02)

#### Bug Fixes

* **worker:** worker can be closed if Redis is down ([#2350](https://github.com/taskforcesh/bullmq/issues/2350)) ([888dcc2](https://github.com/taskforcesh/bullmq/commit/888dcc2dd40571e05fe1f4a5c81161ed062f4542))

## [5.1.0](https://github.com/taskforcesh/bullmq/compare/v5.0.0...v5.1.0) (2023-12-27)

#### Features

* **repeatable:** allow saving custom key ([#1824](https://github.com/taskforcesh/bullmq/issues/1824)) ([8ea0e1f](https://github.com/taskforcesh/bullmq/commit/8ea0e1f76baf36dab94a66657c0f432492cb9999))

## [5.0.0](https://github.com/taskforcesh/bullmq/compare/v4.17.0...v5.0.0) (2023-12-21)

#### Bug Fixes

* **worker:** throw error if connection is missing ([6491a18](https://github.com/taskforcesh/bullmq/commit/6491a185268ae546baa9b95a20b95d63c0e27915))

#### Features

* **job:** provide skipAttempt option when manually moving a job ([#2203](https://github.com/taskforcesh/bullmq/issues/2203)) ([0e88e4f](https://github.com/taskforcesh/bullmq/commit/0e88e4fe4ed940487dfc79d1345d0686de22d0c6))
* **worker:** improved markers handling ([73cf5fc](https://github.com/taskforcesh/bullmq/commit/73cf5fc1e6e13d8329e1e4e700a8db92173e0624)) ([0bac0fb](https://github.com/taskforcesh/bullmq/commit/0bac0fbb97afa968aa7644f1438b86d7bc18bbc5))

#### BREAKING CHANGES

* **connection:** require connection to be passed ([#2335](https://github.com/taskforcesh/bullmq/issues/2335)) ([1867dd1](https://github.com/taskforcesh/bullmq/commit/1867dd107d7edbd417bf6918354ae4656480a544))
* **job:** revert console warn custom job ids when they represent integers ([#2312](https://github.com/taskforcesh/bullmq/issues/2312)) ([84015ff](https://github.com/taskforcesh/bullmq/commit/84015ffa04216c45d8f3181a7f859b8c0792c80d))
* **worker:** markers use now a dedicated key in redis instead of using a special Job ID. ([`73cf5fc`](https://github.com/taskforcesh/bullmq/commit/73cf5fc1e6e13d8329e1e4e700a8db92173e0624)) ([`0bac0fb`](https://github.com/taskforcesh/bullmq/commit/0bac0fbb97afa968aa7644f1438b86d7bc18bbc5))
* references:
  * [Better Queue Markers](https://bullmq.io/news/231204/better-queue-markers/)
  * [BullMQ v5 Migration Notes](https://bullmq.io/news/231221/bullmqv5-release/)


# v4

### [4.18.3](https://github.com/taskforcesh/bullmq/compare/v4.18.2...v4.18.3) (2025-07-19)

#### Performance Improvements

* **delayed:** add marker once when promoting delayed jobs ([#3312](https://github.com/taskforcesh/bullmq/issues/3312)) ([c4a4ada](https://github.com/taskforcesh/bullmq/commit/c4a4adaf5db970d042efe0853145974c62aabdfe))

### [4.18.2](https://github.com/taskforcesh/bullmq/compare/v4.18.1...v4.18.2) (2024-10-24)

#### Bug Fixes

* proper way to get version ([1a433d2](https://github.com/taskforcesh/bullmq/commit/1a433d2a17b58ba8d30f0ecf52d9091f8377978f))

### [4.18.1](https://github.com/taskforcesh/bullmq/compare/v4.18.0...v4.18.1) (2024-10-19)

#### Bug Fixes

* use versions for lua commands ([b0a216d](https://github.com/taskforcesh/bullmq/commit/b0a216deacb0295e77b039ea67c100e57b045037))

## [4.18.0](https://github.com/taskforcesh/bullmq/compare/v4.17.0...v4.18.0) (2024-10-14)

#### Features

* **queue:** add version support ([a600463](https://github.com/taskforcesh/bullmq/commit/a6004639612118ce5adc2a87f0402386ba8e1c2f))

## [4.17.0](https://github.com/taskforcesh/bullmq/compare/v4.16.0...v4.17.0) (2023-12-21)

#### Features

* **sandbox:** support URL (local files) as processor file ([7eea670](https://github.com/taskforcesh/bullmq/commit/7eea6700b33bfd7f36b030b647b819a4c5fd9606))

## [4.16.0](https://github.com/taskforcesh/bullmq/compare/v4.15.4...v4.16.0) (2023-12-18)

#### Features

* **queue:** add a paginated getDependencies ([#2327](https://github.com/taskforcesh/bullmq/issues/2327)) ([c5b8ba3](https://github.com/taskforcesh/bullmq/commit/c5b8ba318b12a84a3a6a928345377fa0eaa08ee3))

### [4.15.4](https://github.com/taskforcesh/bullmq/compare/v4.15.3...v4.15.4) (2023-12-14)

#### Bug Fixes

* **flows:** update constructor and methods to match queue base ([#2324](https://github.com/taskforcesh/bullmq/issues/2324)) ([d6c2064](https://github.com/taskforcesh/bullmq/commit/d6c2064b1fdd88bd4cc61e049ce055ff620b0062))

### [4.15.3](https://github.com/taskforcesh/bullmq/compare/v4.15.2...v4.15.3) (2023-12-13)

#### Bug Fixes

* **sandboxed:** better compatibility with esbuild ([8eaf955](https://github.com/taskforcesh/bullmq/commit/8eaf9550fe8b322df624893c507c55d2cce34b11))

### [4.15.2](https://github.com/taskforcesh/bullmq/compare/v4.15.1...v4.15.2) (2023-12-07)

#### Bug Fixes

* **child-processor:** preserve dynamic imports in commonjs ([d97a5e0](https://github.com/taskforcesh/bullmq/commit/d97a5e06816cff04d86facdb8d32b512f29c6fb9))

### [4.15.1](https://github.com/taskforcesh/bullmq/compare/v4.15.0...v4.15.1) (2023-12-06)

#### Bug Fixes

* **flows:** add meta key to queues created with flows ([272ec69](https://github.com/taskforcesh/bullmq/commit/272ec69557f601a138e1aaba739f7e7878d5344b))

## [4.15.0](https://github.com/taskforcesh/bullmq/compare/v4.14.4...v4.15.0) (2023-12-05)

#### Features

* **sandboxes:** use the more compatible dynamic import instead of require ([6d2fe6e](https://github.com/taskforcesh/bullmq/commit/6d2fe6e7c0473b75aeb9a6d3080b0676f9521065))

### [4.14.4](https://github.com/taskforcesh/bullmq/compare/v4.14.3...v4.14.4) (2023-11-28)

#### Bug Fixes

* **repeat-strategy:** add missing Promise return type ([#2301](https://github.com/taskforcesh/bullmq/issues/2301)) ([6f8f534](https://github.com/taskforcesh/bullmq/commit/6f8f5342cc8aa03f596d9ed5b8831f96a1d4c736))

### [4.14.3](https://github.com/taskforcesh/bullmq/compare/v4.14.2...v4.14.3) (2023-11-27)

#### Bug Fixes

* **update-progress:** remove old updateProgress script to prevent conflict ([#2298](https://github.com/taskforcesh/bullmq/issues/2298)) (python) ([e65b819](https://github.com/taskforcesh/bullmq/commit/e65b819101f8e0e8fdef8c51cfdf9a52f5e73f13))
* **worker:** get dirname by using module.filename ([#2296](https://github.com/taskforcesh/bullmq/issues/2296)) fixes [#2288](https://github.com/taskforcesh/bullmq/issues/2288) ([6e4db5a](https://github.com/taskforcesh/bullmq/commit/6e4db5a3f3648c6a7e10991f2e18f3dab96fb1d7))

### [4.14.2](https://github.com/taskforcesh/bullmq/compare/v4.14.1...v4.14.2) (2023-11-24)

#### Bug Fixes

* **worker:** should cap update progress events ([2cab9e9](https://github.com/taskforcesh/bullmq/commit/2cab9e94f65c7bdd053e3fb5944bcda6e3ebaa39))

### [4.14.1](https://github.com/taskforcesh/bullmq/compare/v4.14.0...v4.14.1) (2023-11-23)

#### Bug Fixes

* **worker:** do not wait for slow jobs fixes [#2290](https://github.com/taskforcesh/bullmq/issues/2290) ([568d758](https://github.com/taskforcesh/bullmq/commit/568d7585edb1f2ef15991d4ae4a2425e6834046a))

## [4.14.0](https://github.com/taskforcesh/bullmq/compare/v4.13.3...v4.14.0) (2023-11-18)

#### Features

* **worker:** better handling of concurrency when fetching jobs ([#2242](https://github.com/taskforcesh/bullmq/issues/2242)) ([d2e2035](https://github.com/taskforcesh/bullmq/commit/d2e203588878ee64cb21e67141f73b32867dfb40))

### [4.13.3](https://github.com/taskforcesh/bullmq/compare/v4.13.2...v4.13.3) (2023-11-16)

#### Bug Fixes

* **utils:** use EventEmitter as a type instead of a namespace ([#2283](https://github.com/taskforcesh/bullmq/issues/2283)) ([41c9d1d](https://github.com/taskforcesh/bullmq/commit/41c9d1d05eedc7351272708e667e8d65eb6773fc))

### [4.13.2](https://github.com/taskforcesh/bullmq/compare/v4.13.1...v4.13.2) (2023-11-09)

#### Bug Fixes

* **job:** set delay value on current job instance when it is retried ([#2266](https://github.com/taskforcesh/bullmq/issues/2266)) (python) ([76e075f](https://github.com/taskforcesh/bullmq/commit/76e075f54d5745b6cec3cb11305bf3110d963eae))

### [4.13.1](https://github.com/taskforcesh/bullmq/compare/v4.13.0...v4.13.1) (2023-11-08)

#### Bug Fixes

* **connection:** better handling of attached listeners ([02474ad](https://github.com/taskforcesh/bullmq/commit/02474ad59a7b340d7bb2a7415ae7a88e14200398))
* **connection:** move redis instance check to queue base ([13a339a](https://github.com/taskforcesh/bullmq/commit/13a339a730f46ff22acdd4a046e0d9c4b7d88679))

## [4.13.0](https://github.com/taskforcesh/bullmq/compare/v4.12.10...v4.13.0) (2023-11-05)

#### Features

* **queue:** improve clean to work iteratively ([#2260](https://github.com/taskforcesh/bullmq/issues/2260)) ([0cfa66f](https://github.com/taskforcesh/bullmq/commit/0cfa66fd0fa0dba9b3941f183cf6f06d8a4f281d))

### [4.12.10](https://github.com/taskforcesh/bullmq/compare/v4.12.9...v4.12.10) (2023-11-05)

#### Bug Fixes

* update delay job property when moving to delayed set ([#2261](https://github.com/taskforcesh/bullmq/issues/2261)) ([69ece08](https://github.com/taskforcesh/bullmq/commit/69ece08babd7716c14c38c3dd50630b44c7c1897))

### [4.12.9](https://github.com/taskforcesh/bullmq/compare/v4.12.8...v4.12.9) (2023-11-05)

#### Bug Fixes

* **add-job:** trim events when waiting-children event is published ([#2262](https://github.com/taskforcesh/bullmq/issues/2262)) (python) ([198bf05](https://github.com/taskforcesh/bullmq/commit/198bf05fa5a4e1ce50081296033a2e0f26ece498))

### [4.12.8](https://github.com/taskforcesh/bullmq/compare/v4.12.7...v4.12.8) (2023-11-03)

#### Bug Fixes

* **worker:** keep extending locks while closing workers ([#2259](https://github.com/taskforcesh/bullmq/issues/2259)) ([c4d12ea](https://github.com/taskforcesh/bullmq/commit/c4d12ea3a9837ffd7f58e2134796137c4181c3de))

### [4.12.7](https://github.com/taskforcesh/bullmq/compare/v4.12.6...v4.12.7) (2023-10-29)

#### Performance Improvements

* **redis-connection:** check redis version greater or equal than v6 only once ([#2252](https://github.com/taskforcesh/bullmq/issues/2252)) ([a09b15a](https://github.com/taskforcesh/bullmq/commit/a09b15af0d5dedfa83bce7130ee9094f3fb69e10))

### [4.12.6](https://github.com/taskforcesh/bullmq/compare/v4.12.5...v4.12.6) (2023-10-26)

#### Bug Fixes

* **sandbox:** do not return empty object result when it is undefined ([#2247](https://github.com/taskforcesh/bullmq/issues/2247)) ([308db7f](https://github.com/taskforcesh/bullmq/commit/308db7f58758a72b8abb272da8e92509813a2178))

### [4.12.5](https://github.com/taskforcesh/bullmq/compare/v4.12.4...v4.12.5) (2023-10-18)

#### Performance Improvements

* **events:** trim events when removing jobs ([#2235](https://github.com/taskforcesh/bullmq/issues/2235)) (python) ([889815c](https://github.com/taskforcesh/bullmq/commit/889815c412666e5fad8f32d2e3a2d41cf650f001))

### [4.12.4](https://github.com/taskforcesh/bullmq/compare/v4.12.3...v4.12.4) (2023-10-13)

#### Bug Fixes

* **events:** do not publish removed event on non-existent jobs ([#2227](https://github.com/taskforcesh/bullmq/issues/2227)) ([c134606](https://github.com/taskforcesh/bullmq/commit/c1346064c6cd9f93c59b184f150eac11d51c91b4))

### [4.12.3](https://github.com/taskforcesh/bullmq/compare/v4.12.2...v4.12.3) (2023-10-10)

#### Bug Fixes

* **events:** trim events when retrying a job ([#2224](https://github.com/taskforcesh/bullmq/issues/2224)) ([1986b05](https://github.com/taskforcesh/bullmq/commit/1986b05ac03fe4ee48861aa60caadcc9df8170a6))

### [4.12.2](https://github.com/taskforcesh/bullmq/compare/v4.12.1...v4.12.2) (2023-10-05)

#### Bug Fixes

* **sandbox:** update progress value on job instance ([#2214](https://github.com/taskforcesh/bullmq/issues/2214)) fixes [#2213](https://github.com/taskforcesh/bullmq/issues/2213) ([3d0f36a](https://github.com/taskforcesh/bullmq/commit/3d0f36a134b7f5c6b6de26967c9d71bcfb346e72))

### [4.12.1](https://github.com/taskforcesh/bullmq/compare/v4.12.0...v4.12.1) (2023-10-04)

#### Bug Fixes

* **delayed:** trim events when moving jobs to delayed (python) ([#2211](https://github.com/taskforcesh/bullmq/issues/2211)) ([eca8c2d](https://github.com/taskforcesh/bullmq/commit/eca8c2d4dfeafbd8ac36a49764dbd4897303628c))

## [4.12.0](https://github.com/taskforcesh/bullmq/compare/v4.11.4...v4.12.0) (2023-09-29)

#### Features

* expose addJobLog and updateJobProgress to the Queue instance ([#2202](https://github.com/taskforcesh/bullmq/issues/2202)) ([2056939](https://github.com/taskforcesh/bullmq/commit/205693907a4d6c2da9bd0690fb552b1d1e369c08))

### [4.11.4](https://github.com/taskforcesh/bullmq/compare/v4.11.3...v4.11.4) (2023-09-22)

#### Bug Fixes

* **queue:** batched unpack now uses range ([#2188](https://github.com/taskforcesh/bullmq/issues/2188)) ([b5e97f4](https://github.com/taskforcesh/bullmq/commit/b5e97f420bc0c4bc82772f3e87883ee522be43d9))

### [4.11.3](https://github.com/taskforcesh/bullmq/compare/v4.11.2...v4.11.3) (2023-09-22)

#### Bug Fixes

* **worker:** forward skipVersionCheck to blockingConnection ([#2189](https://github.com/taskforcesh/bullmq/issues/2189)) ref [#2149](https://github.com/taskforcesh/bullmq/issues/2149) ([c8aa9a3](https://github.com/taskforcesh/bullmq/commit/c8aa9a36224cba8ecb19af1bf652f4f1c4c20d40))

### [4.11.2](https://github.com/taskforcesh/bullmq/compare/v4.11.1...v4.11.2) (2023-09-20)

#### Bug Fixes

* **worker:** throw exception with NaN as concurrency ([#2184](https://github.com/taskforcesh/bullmq/issues/2184)) ([f36ac8b](https://github.com/taskforcesh/bullmq/commit/f36ac8b61dcd4bb3d9e283278310cd50cfc83fae))

### [4.11.1](https://github.com/taskforcesh/bullmq/compare/v4.11.0...v4.11.1) (2023-09-20)

#### Bug Fixes

* **queue:** differentiate score purpose per state in clean method ([#2133](https://github.com/taskforcesh/bullmq/issues/2133)) fixes [#2124](https://github.com/taskforcesh/bullmq/issues/2124) ([862f10b](https://github.com/taskforcesh/bullmq/commit/862f10b586276314d9bffff2a5e6caf939399f7e))

## [4.11.0](https://github.com/taskforcesh/bullmq/compare/v4.10.0...v4.11.0) (2023-09-16)

#### Features

* **sandbox:** convert wrapJob method as protected for extension ([#2182](https://github.com/taskforcesh/bullmq/issues/2182)) ([1494b55](https://github.com/taskforcesh/bullmq/commit/1494b5566573356e0248b4a5cab48ae21d82f1da))

## [4.10.0](https://github.com/taskforcesh/bullmq/compare/v4.9.0...v4.10.0) (2023-09-12)

#### Bug Fixes

* **move-to-finished:** consider addition of prioritized jobs when processing last active job ([#2176](https://github.com/taskforcesh/bullmq/issues/2176)) (python) ([4b01f35](https://github.com/taskforcesh/bullmq/commit/4b01f359c290cfc62ea74ff3ab0b43ccc6956a02))
* **remove:** change error message when job is locked (python) ([#2175](https://github.com/taskforcesh/bullmq/issues/2175)) ([2f5628f](https://github.com/taskforcesh/bullmq/commit/2f5628feffab66cdcc78abf4d7bb608bdcaa65bb))

## [4.9.0](https://github.com/taskforcesh/bullmq/compare/v4.8.0...v4.9.0) (2023-09-05)

#### Features

* **connection:** provide skipVersionCheck option for shared connections ([#2149](https://github.com/taskforcesh/bullmq/issues/2149)) ref [#2148](https://github.com/taskforcesh/bullmq/issues/2148) ([914820f](https://github.com/taskforcesh/bullmq/commit/914820f720cbc48b49f4bd1c46d148eb2bb5b79c))

## [4.8.0](https://github.com/taskforcesh/bullmq/compare/v4.7.4...v4.8.0) (2023-08-20)

#### Features

* **sandbox:** emulate moveToDelayed method ([#2122](https://github.com/taskforcesh/bullmq/issues/2122)) ref [#2118](https://github.com/taskforcesh/bullmq/issues/2118) ([4c4559b](https://github.com/taskforcesh/bullmq/commit/4c4559b3c678313b3727c9781a6d3f963bcfda4e))

### [4.7.4](https://github.com/taskforcesh/bullmq/compare/v4.7.3...v4.7.4) (2023-08-19)

#### Bug Fixes

* **sandbox:** ignore extra params on processor ([#2142](https://github.com/taskforcesh/bullmq/issues/2142)) ([3602c20](https://github.com/taskforcesh/bullmq/commit/3602c20ab80cbe0a0d3de66210a01ad119e1090b))

### [4.7.3](https://github.com/taskforcesh/bullmq/compare/v4.7.2...v4.7.3) (2023-08-17)

#### Bug Fixes

* **worker:** abort rate-limit delay when closing worker ([264a81c](https://github.com/taskforcesh/bullmq/commit/264a81ca5f4e4f88c361d507312324b5f6c3225c))

### [4.7.2](https://github.com/taskforcesh/bullmq/compare/v4.7.1...v4.7.2) (2023-08-12)

#### Bug Fixes

* **queue:** throw error when name is not provided ([#2123](https://github.com/taskforcesh/bullmq/issues/2123)) ([78fb0e2](https://github.com/taskforcesh/bullmq/commit/78fb0e2a93cfa59a43a0fb337f857e78f1c6fcf4))

### [4.7.1](https://github.com/taskforcesh/bullmq/compare/v4.7.0...v4.7.1) (2023-08-10)

#### Performance Improvements

* **rate-limit:** get pttl only if needed ([#2129](https://github.com/taskforcesh/bullmq/issues/2129)) ([12ce2f3](https://github.com/taskforcesh/bullmq/commit/12ce2f3746626a81ea961961bb1a629077eed68a))

## [4.7.0](https://github.com/taskforcesh/bullmq/compare/v4.6.3...v4.7.0) (2023-08-03)

#### Features

* **queue:** add getRateLimitTtl method ([#2105](https://github.com/taskforcesh/bullmq/issues/2105)) ([7426c64](https://github.com/taskforcesh/bullmq/commit/7426c64b109f1beacf742d57a987282597385469))

### [4.6.3](https://github.com/taskforcesh/bullmq/compare/v4.6.2...v4.6.3) (2023-07-28)

#### Performance Improvements

* **job:** generate priority limit constant once ([#2102](https://github.com/taskforcesh/bullmq/issues/2102)) ([8880f9f](https://github.com/taskforcesh/bullmq/commit/8880f9f2983282d343d603a89abe5e1e6bff78e5))

### [4.6.2](https://github.com/taskforcesh/bullmq/compare/v4.6.0...v4.6.2) (2023-07-26)

#### Performance Improvements

* **retry:** compare prev state instead of regex expression ([#2099](https://github.com/taskforcesh/bullmq/issues/2099)) ([c141283](https://github.com/taskforcesh/bullmq/commit/c1412831903d1fae0955af097e0be049024839fe))

## [4.6.0](https://github.com/taskforcesh/bullmq/compare/v4.5.0...v4.6.0) (2023-07-19)

#### Features

* **queue:** add promoteJobs to promote all delayed jobs ([6074592](https://github.com/taskforcesh/bullmq/commit/6074592574256ec4b1c340126288e803e56b1a64))

## [4.5.0](https://github.com/taskforcesh/bullmq/compare/v4.4.0...v4.5.0) (2023-07-18)

#### Features

* **job:** add option for removing children in remove method (python) ([#2064](https://github.com/taskforcesh/bullmq/issues/2064)) ([841dc87](https://github.com/taskforcesh/bullmq/commit/841dc87a689897df81438ad1f43e45a4da77c388))

## [4.4.0](https://github.com/taskforcesh/bullmq/compare/v4.3.0...v4.4.0) (2023-07-17)

#### Features

* **job:** add removeDependencyOnFailure option ([#1953](https://github.com/taskforcesh/bullmq/issues/1953)) ([ffd49e2](https://github.com/taskforcesh/bullmq/commit/ffd49e289c57252487200d47b92193228ae7451f))

## [4.3.0](https://github.com/taskforcesh/bullmq/compare/v4.2.1...v4.3.0) (2023-07-14)

#### Features

* **worker:** add id as part of token ([#2061](https://github.com/taskforcesh/bullmq/issues/2061)) ([e255356](https://github.com/taskforcesh/bullmq/commit/e2553562271e1e4143a8fef616349bb30de4899d))

### [4.2.1](https://github.com/taskforcesh/bullmq/compare/v4.2.0...v4.2.1) (2023-07-10)

#### Bug Fixes

* **flow:** emit delayed event when parent is moved to delayed ([#2055](https://github.com/taskforcesh/bullmq/issues/2055)) ([f419ff1](https://github.com/taskforcesh/bullmq/commit/f419ff1ec5cb34986fe4b79402c727a6487e949c))

## [4.2.0](https://github.com/taskforcesh/bullmq/compare/v4.1.0...v4.2.0) (2023-07-03)

#### Features

* **common:** add option to change repeatable jobs redis key hash algorithm ([#2023](https://github.com/taskforcesh/bullmq/issues/2023)) ([ca17364](https://github.com/taskforcesh/bullmq/commit/ca17364cc2a52f6577fb66f09ec3168bbf9f1e07))

## [4.1.0](https://github.com/taskforcesh/bullmq/compare/v4.0.0...v4.1.0) (2023-06-23)

#### Features

* **queue:** add getPrioritized and getPrioritizedCount methods ([#2005](https://github.com/taskforcesh/bullmq/issues/2005)) ([7363abe](https://github.com/taskforcesh/bullmq/commit/7363abebce6e3bcf067fc7c220d845807ebb1489))

## [4.0.0](https://github.com/taskforcesh/bullmq/compare/v3.15.8...v4.0.0) (2023-06-21)

#### Features

* **queue:** add removeDeprecatedPriorityKey method

#### Performance Improvements

* **priority:** add prioritized as a new state ([#1984](https://github.com/taskforcesh/bullmq/issues/1984)) (python) ([42a890a](https://github.com/taskforcesh/bullmq/commit/42a890a2bfe45b29348030f886766400f5d41aa3))

#### BREAKING CHANGES

* **priority:** priority is separeted in its own zset, no duplication needed
* **job:** change job method name update to updateData

ref [faster priority jobs](https://bullmq.io/news/062123/faster-priority-jobs/)


# v3

### [3.15.8](https://github.com/taskforcesh/bullmq/compare/v3.15.7...v3.15.8) (2023-06-16)

#### Bug Fixes

* **rate-limit:** keep priority fifo order ([#1991](https://github.com/taskforcesh/bullmq/issues/1991)) fixes [#1929](https://github.com/taskforcesh/bullmq/issues/1929) (python) ([56bd7ad](https://github.com/taskforcesh/bullmq/commit/56bd7ad8c4daffcfb1f9f199abfc5d6495eb291e))

### [3.15.7](https://github.com/taskforcesh/bullmq/compare/v3.15.6...v3.15.7) (2023-06-16)

#### Bug Fixes

* **worker:** set redis version always in initialization ([#1989](https://github.com/taskforcesh/bullmq/issues/1989)) fixes [#1988](https://github.com/taskforcesh/bullmq/issues/1988) ([a1544a8](https://github.com/taskforcesh/bullmq/commit/a1544a8c0f29522cd33772b14f559969db852d1d))

### [3.15.6](https://github.com/taskforcesh/bullmq/compare/v3.15.5...v3.15.6) (2023-06-13)

#### Bug Fixes

* **worker:** use timeout as integer for redis lower than v6.0.0 (python) ([#1981](https://github.com/taskforcesh/bullmq/issues/1981)) ([0df6afa](https://github.com/taskforcesh/bullmq/commit/0df6afad5e71a693b721ba52ffa6be733ee45ccb))

### [3.15.5](https://github.com/taskforcesh/bullmq/compare/v3.15.4...v3.15.5) (2023-06-11)

#### Bug Fixes

* **retry-job:** consider priority when moving job to wait (python) ([#1969](https://github.com/taskforcesh/bullmq/issues/1969)) ([e753855](https://github.com/taskforcesh/bullmq/commit/e753855eef248da73a5e9f6b18f4b79319dc2f86))

### [3.15.4](https://github.com/taskforcesh/bullmq/compare/v3.15.3...v3.15.4) (2023-06-08)

#### Bug Fixes

* **job:** import right reference of QueueEvents ([#1964](https://github.com/taskforcesh/bullmq/issues/1964)) ([689c845](https://github.com/taskforcesh/bullmq/commit/689c84567f3a9fea51f349ca93b3008d5c187f62))

### [3.15.3](https://github.com/taskforcesh/bullmq/compare/v3.15.2...v3.15.3) (2023-06-08)

#### Bug Fixes

* **job:** use QueueEvents type for waitUntilFinished ([#1958](https://github.com/taskforcesh/bullmq/issues/1958)) ([881848c](https://github.com/taskforcesh/bullmq/commit/881848c1ee3835dac24daf6807b1f35da967f68b))

### [3.15.2](https://github.com/taskforcesh/bullmq/compare/v3.15.1...v3.15.2) (2023-06-06)

#### Bug Fixes

* **worker:** better worker client naming ([c5f63af](https://github.com/taskforcesh/bullmq/commit/c5f63affe72f7b6616f4c5f3aafde858dcc0b200))

### [3.15.1](https://github.com/taskforcesh/bullmq/compare/v3.15.0...v3.15.1) (2023-06-05)

#### Bug Fixes

* **rate-limit:** consider paused queue ([#1931](https://github.com/taskforcesh/bullmq/issues/1931)) ([d97864a](https://github.com/taskforcesh/bullmq/commit/d97864a550992aeb8673557c7d8f186ab4ccb5bf))

## [3.15.0](https://github.com/taskforcesh/bullmq/compare/v3.14.2...v3.15.0) (2023-05-31)

#### Features

* **job:** add changePriority method ([#1901](https://github.com/taskforcesh/bullmq/issues/1901)) ref [#1899](https://github.com/taskforcesh/bullmq/issues/1899) ([9485ad5](https://github.com/taskforcesh/bullmq/commit/9485ad567e2d8c78d601cc9eb2b7dd37f96d00c9))

### [3.14.2](https://github.com/taskforcesh/bullmq/compare/v3.14.1...v3.14.2) (2023-05-30)

#### Bug Fixes

* **rate-limit:** take in count priority ([#1919](https://github.com/taskforcesh/bullmq/issues/1919)) fixes [#1915](https://github.com/taskforcesh/bullmq/issues/1915) ([b8157a3](https://github.com/taskforcesh/bullmq/commit/b8157a3424ceb60e662e80a3b0db918241b87ecc))

### [3.14.1](https://github.com/taskforcesh/bullmq/compare/v3.14.0...v3.14.1) (2023-05-27)

#### Performance Improvements

* **retry-job:** get target queue list once ([#1921](https://github.com/taskforcesh/bullmq/issues/1921)) ([8a7a9dd](https://github.com/taskforcesh/bullmq/commit/8a7a9ddd793161a8591485ed18a191ece37026a8))

## [3.14.0](https://github.com/taskforcesh/bullmq/compare/v3.13.4...v3.14.0) (2023-05-22)

#### Features

* **worker:** make extendLocks overridable ([7b1386b](https://github.com/taskforcesh/bullmq/commit/7b1386bb823562d9666a1ad6e206e1deb63e57ec))

### [3.13.4](https://github.com/taskforcesh/bullmq/compare/v3.13.3...v3.13.4) (2023-05-11)

#### Performance Improvements

* **rate-limit:** call pttl in script moveJobFromActiveToWait ([#1889](https://github.com/taskforcesh/bullmq/issues/1889)) ([e0d2992](https://github.com/taskforcesh/bullmq/commit/e0d2992eb757d437dede52054c049470d986ad44))

### [3.13.3](https://github.com/taskforcesh/bullmq/compare/v3.13.2...v3.13.3) (2023-05-10)

#### Bug Fixes

* **child:** use named import for EventEmitter ([#1887](https://github.com/taskforcesh/bullmq/issues/1887)) ([1db396d](https://github.com/taskforcesh/bullmq/commit/1db396d1f54154dc94c796ae8b570336fc341f02))

### [3.13.2](https://github.com/taskforcesh/bullmq/compare/v3.13.1...v3.13.2) (2023-05-09)

#### Bug Fixes

* **rate-limit:** consider paused queue when dynamic rate limit ([#1884](https://github.com/taskforcesh/bullmq/issues/1884)) ([a23f37e](https://github.com/taskforcesh/bullmq/commit/a23f37e4079d34c8589efc85e4d726a62244f0d2))

### [3.13.1](https://github.com/taskforcesh/bullmq/compare/v3.13.0...v3.13.1) (2023-05-07)

#### Bug Fixes

* **retry:** consider when queue is paused ([#1880](https://github.com/taskforcesh/bullmq/issues/1880)) ([01b621f](https://github.com/taskforcesh/bullmq/commit/01b621fea0cbdae602482ff61361c05646823223))

## [3.13.0](https://github.com/taskforcesh/bullmq/compare/v3.12.1...v3.13.0) (2023-05-06)

#### Features

* **worker:** add worker threads support ([0820985](https://github.com/taskforcesh/bullmq/commit/0820985e073582fdf841affad38ecc7ab64691ec))

### [3.12.1](https://github.com/taskforcesh/bullmq/compare/v3.12.0...v3.12.1) (2023-05-05)

#### Bug Fixes

* **worker:** close open handles after closing ([#1861](https://github.com/taskforcesh/bullmq/issues/1861)) fixes [#1312](https://github.com/taskforcesh/bullmq/issues/1312) ([39286e8](https://github.com/taskforcesh/bullmq/commit/39286e87e8ffabf641f229cf2da3db4c280f4637))

## [3.12.0](https://github.com/taskforcesh/bullmq/compare/v3.11.0...v3.12.0) (2023-04-20)

#### Features

* upgrade ioredis to 5.3.2 ([375b1be](https://github.com/taskforcesh/bullmq/commit/375b1be52035e93c5fef6024e0d06aa723f602a9))

## [3.11.0](https://github.com/taskforcesh/bullmq/compare/v3.10.4...v3.11.0) (2023-04-17)

#### Features

* **upstash:** don't throw an error when detecting an upstash host ([2e06bca](https://github.com/taskforcesh/bullmq/commit/2e06bca3615aafecd725d093045a510a67053fed))

### [3.10.4](https://github.com/taskforcesh/bullmq/compare/v3.10.3...v3.10.4) (2023-04-05)

#### Bug Fixes

* **flow:** do not remove completed children results ([#1788](https://github.com/taskforcesh/bullmq/issues/1788)) fixes [#1778](https://github.com/taskforcesh/bullmq/issues/1778) ([04b547a](https://github.com/taskforcesh/bullmq/commit/04b547ad3df02cb94c499f7f26678e19c6797e7e))

### [3.10.3](https://github.com/taskforcesh/bullmq/compare/v3.10.2...v3.10.3) (2023-03-30)

#### Bug Fixes

* **flow:** consider removing dependency on removeOnFail true ([#1753](https://github.com/taskforcesh/bullmq/issues/1753)) ([de5a299](https://github.com/taskforcesh/bullmq/commit/de5a299f109834ab0235ae6fb6286fd94fcef961))

### [3.10.2](https://github.com/taskforcesh/bullmq/compare/v3.10.1...v3.10.2) (2023-03-22)

#### Bug Fixes

* **job:** avoid error when job is moved when processing ([#1354](https://github.com/taskforcesh/bullmq/issues/1354)) fixes [#1343](https://github.com/taskforcesh/bullmq/issues/1343) [#1602](https://github.com/taskforcesh/bullmq/issues/1602) ([78085e4](https://github.com/taskforcesh/bullmq/commit/78085e4304357dd3695df61057f91e706c3a52bf))

### [3.10.1](https://github.com/taskforcesh/bullmq/compare/v3.10.0...v3.10.1) (2023-03-06)

#### Bug Fixes

* **worker:** throw error with invalid concurrency fixes [#1723](https://github.com/taskforcesh/bullmq/issues/1723) ([2a1cdbe](https://github.com/taskforcesh/bullmq/commit/2a1cdbe3e871309f460aadc14b4d632238c32aa9))

## [3.10.0](https://github.com/taskforcesh/bullmq/compare/v3.9.0...v3.10.0) (2023-03-02)

#### Bug Fixes

* **worker:** close lock extended timer ([7995f18](https://github.com/taskforcesh/bullmq/commit/7995f18bb7712bd50d0fa3d17c4ab565b16ab379))
* **worker:** correct lock extender logic ([6aa3569](https://github.com/taskforcesh/bullmq/commit/6aa3569db0fe0137790e61a4b5982d2b35ee5646))
* **worker:** start stalled check timer ([4763be0](https://github.com/taskforcesh/bullmq/commit/4763be028b0c7b0460fd0804d4569c446a06ef4a))

#### Features

* **worker:** replace Promise.race with efficient an async fifo ([0d94e35](https://github.com/taskforcesh/bullmq/commit/0d94e35e805b09c3b4c7404b8a2eeb71a1aff5c4))
* **worker:** simplify lock extension to one call independent of concurrency ([ebf1aeb](https://github.com/taskforcesh/bullmq/commit/ebf1aeb2400383d0ae90ab68aeb4822aea03ba44))

#### Performance Improvements

* **scripts:** reuse keys array to avoid allocations ([feac7b4](https://github.com/taskforcesh/bullmq/commit/feac7b4070a6a3720597af36c43d095e9ea37173))
* **worker:** improve worker memory consumption ([4846cf1](https://github.com/taskforcesh/bullmq/commit/4846cf1fe3f9ea35f58a679c11706e1a7101c898))

## [3.9.0](https://github.com/taskforcesh/bullmq/compare/v3.8.0...v3.9.0) (2023-02-25)

#### Features

* **worker:** add remove on complete and fail options ([#1703](https://github.com/taskforcesh/bullmq/issues/1703)) ([cf13494](https://github.com/taskforcesh/bullmq/commit/cf1349471dcbf0e43feea9972eaa71d2299d619f))

## [3.8.0](https://github.com/taskforcesh/bullmq/compare/v3.7.2...v3.8.0) (2023-02-23)

#### Bug Fixes

* **worker:** run stalled check directly first time ([f71ec03](https://github.com/taskforcesh/bullmq/commit/f71ec03111a22897cbf2fad39073185e4aeac6d6))

#### Features

* **worker:** add a public method to run the stalled checker ([3159266](https://github.com/taskforcesh/bullmq/commit/3159266ccb002d4fc71b7ee7ac63c465c536dbd1))
* **worker:** add support to disable stalled checks ([49e860c](https://github.com/taskforcesh/bullmq/commit/49e860c6675853971e992c2945b445660504e3b2))

### [3.7.2](https://github.com/taskforcesh/bullmq/compare/v3.7.1...v3.7.2) (2023-02-23)

#### Bug Fixes

* **worker:** restore failed event job parameter typing ([#1707](https://github.com/taskforcesh/bullmq/issues/1707)) ([44c2203](https://github.com/taskforcesh/bullmq/commit/44c2203ab65d406be9a913254600fe07c83e62d5))

### [3.7.1](https://github.com/taskforcesh/bullmq/compare/v3.7.0...v3.7.1) (2023-02-22)

#### Bug Fixes

* **worker:** failed event receives an optional job parameter ([#1702](https://github.com/taskforcesh/bullmq/issues/1702)) fixes [#1690](https://github.com/taskforcesh/bullmq/issues/1690) ([6009906](https://github.com/taskforcesh/bullmq/commit/6009906355765bf00cba5c1505e9e0c6bf8f14db))

## [3.7.0](https://github.com/taskforcesh/bullmq/compare/v3.6.6...v3.7.0) (2023-02-16)

#### Performance Improvements

* **move-to-active:** remove deprecated limiter reference ([#1673](https://github.com/taskforcesh/bullmq/issues/1673)) ([a97b22f](https://github.com/taskforcesh/bullmq/commit/a97b22f518a9f6c5d9c30a77bfd03cafdcbc57ff))

### [3.6.6](https://github.com/taskforcesh/bullmq/compare/v3.6.5...v3.6.6) (2023-02-15)

#### Bug Fixes

* **job:** check jobKey when saving stacktrace ([#1681](https://github.com/taskforcesh/bullmq/issues/1681)) fixes [#1676](https://github.com/taskforcesh/bullmq/issues/1676) ([1856c76](https://github.com/taskforcesh/bullmq/commit/1856c7684c377ca4fd36294cca8e128404be27b8))

### [3.6.5](https://github.com/taskforcesh/bullmq/compare/v3.6.4...v3.6.5) (2023-02-11)

#### Bug Fixes

* infinite worker process spawned for invalid JS file ([a445ba8](https://github.com/taskforcesh/bullmq/commit/a445ba8b7a261b370dec7d88091ae5f5af8b2728))

### [3.6.4](https://github.com/taskforcesh/bullmq/compare/v3.6.3...v3.6.4) (2023-02-09)

#### Bug Fixes

* **worker:** add a maximum block time ([1a2618b](https://github.com/taskforcesh/bullmq/commit/1a2618bc5473288a62dddb85e3cb78d6cdb4f39f))

### [3.6.3](https://github.com/taskforcesh/bullmq/compare/v3.6.2...v3.6.3) (2023-02-07)

#### Bug Fixes

* **master:** copy type declaration ([23ade6e](https://github.com/taskforcesh/bullmq/commit/23ade6e3e45df14bd3fbc2c3e7be47307b642872))

### [3.6.2](https://github.com/taskforcesh/bullmq/compare/v3.6.1...v3.6.2) (2023-02-03)

#### Bug Fixes

* **redis:** increase minimum default retry time ([d521531](https://github.com/taskforcesh/bullmq/commit/d521531e22ba9eda8ad8d6e8eddf450fdc3f50f4))

### [3.6.1](https://github.com/taskforcesh/bullmq/compare/v3.6.0...v3.6.1) (2023-01-31)

#### Bug Fixes

* **connection:** apply console.warn in noeviction message ([95f171c](https://github.com/taskforcesh/bullmq/commit/95f171cbc8cdd7d04865618b715dd21229f36a4a))

## [3.6.0](https://github.com/taskforcesh/bullmq/compare/v3.5.11...v3.6.0) (2023-01-31)

#### Features

* **job:** allow clearing job's log ([#1600](https://github.com/taskforcesh/bullmq/issues/1600)) ([0ded2d7](https://github.com/taskforcesh/bullmq/commit/0ded2d7709322bf105e0decac44d801ece5615f2))

### [3.5.11](https://github.com/taskforcesh/bullmq/compare/v3.5.10...v3.5.11) (2023-01-27)

#### Bug Fixes

* **error:** remove global prototype toJSON ([#1642](https://github.com/taskforcesh/bullmq/issues/1642)) fixes [#1414](https://github.com/taskforcesh/bullmq/issues/1414) ([d4e7108](https://github.com/taskforcesh/bullmq/commit/d4e7108a37aeabdd3085a26c9daf09cea5976f3e))

### [3.5.10](https://github.com/taskforcesh/bullmq/compare/v3.5.9...v3.5.10) (2023-01-24)

#### Bug Fixes

* **move-to-finished:** return correct delayUntil ([#1643](https://github.com/taskforcesh/bullmq/issues/1643)) ([c4bf9fa](https://github.com/taskforcesh/bullmq/commit/c4bf9fa6563eda1630d8eb2189b16e9324b01c7f))

### [3.5.9](https://github.com/taskforcesh/bullmq/compare/v3.5.8...v3.5.9) (2023-01-19)

#### Bug Fixes

* **worker:** fix delayed jobs with concurrency fixes [#1627](https://github.com/taskforcesh/bullmq/issues/1627) ([99a8e6d](https://github.com/taskforcesh/bullmq/commit/99a8e6d3a339be51fb46f69c8afac4ecdebff6d3))

### [3.5.8](https://github.com/taskforcesh/bullmq/compare/v3.5.7...v3.5.8) (2023-01-18)

#### Bug Fixes

* **move-to-active:** delete marker when it is moved to active ([#1634](https://github.com/taskforcesh/bullmq/issues/1634)) ([ad1fcea](https://github.com/taskforcesh/bullmq/commit/ad1fcea4500d4ceed51d5d5b0a03dbb5e1735a42))

### [3.5.7](https://github.com/taskforcesh/bullmq/compare/v3.5.6...v3.5.7) (2023-01-17)

#### Bug Fixes

* **move-to-active:** validate next marker and return delayUntil ([#1630](https://github.com/taskforcesh/bullmq/issues/1630)) ([3cd3305](https://github.com/taskforcesh/bullmq/commit/3cd33052fc711a9ba560c9a431630be5cdd02193))

### [3.5.6](https://github.com/taskforcesh/bullmq/compare/v3.5.5...v3.5.6) (2023-01-13)

#### Bug Fixes

* **worker:** add max concurrency from the beginning ([#1597](https://github.com/taskforcesh/bullmq/issues/1597)) fixes [#1589](https://github.com/taskforcesh/bullmq/issues/1589) ([6f49db3](https://github.com/taskforcesh/bullmq/commit/6f49db3fb15119d13f99cd83d49f2a7bdcb614cd))

### [3.5.5](https://github.com/taskforcesh/bullmq/compare/v3.5.4...v3.5.5) (2023-01-10)

#### Bug Fixes

* circular references ([#1622](https://github.com/taskforcesh/bullmq/issues/1622)) ([f607ec7](https://github.com/taskforcesh/bullmq/commit/f607ec7530fb4430e8cab7ed325583bd9d171ccf))

### [3.5.4](https://github.com/taskforcesh/bullmq/compare/v3.5.3...v3.5.4) (2023-01-09)

#### Bug Fixes

* [#1603](https://github.com/taskforcesh/bullmq/issues/1603) performance issues in `remove()` ([#1607](https://github.com/taskforcesh/bullmq/issues/1607)) ([2541215](https://github.com/taskforcesh/bullmq/commit/2541215bcf81dcd52eaefa02530c3812a5135fbf))

### [3.5.3](https://github.com/taskforcesh/bullmq/compare/v3.5.2...v3.5.3) (2023-01-07)

#### Bug Fixes

* **delayed:** remove marker after being consumed ([#1620](https://github.com/taskforcesh/bullmq/issues/1620)) fixes [#1615](https://github.com/taskforcesh/bullmq/issues/1615) ([9fce0f0](https://github.com/taskforcesh/bullmq/commit/9fce0f05e5acc1918a276b03e8cb9c16083cb509))

### [3.5.2](https://github.com/taskforcesh/bullmq/compare/v3.5.1...v3.5.2) (2023-01-04)

#### Performance Improvements

* **get-dependencies:** replace slow object destructuring with single object ([#1612](https://github.com/taskforcesh/bullmq/issues/1612)) ([621748e](https://github.com/taskforcesh/bullmq/commit/621748ec7727b46ce57eb9d2b46ef981874cdf4c))

### [3.5.1](https://github.com/taskforcesh/bullmq/compare/v3.5.0...v3.5.1) (2022-12-23)

#### Bug Fixes

* **connection:** throw exception if using keyPrefix in ioredis ([eb6a130](https://github.com/taskforcesh/bullmq/commit/eb6a1305541547725e1717eefe2b678bc445f4d0))
* **connection:** use includes to check for upstash more reliably ([12efb5c](https://github.com/taskforcesh/bullmq/commit/12efb5c539cb6f031ea6f3a80e4128d2e556e627))

## [3.5.0](https://github.com/taskforcesh/bullmq/compare/v3.4.2...v3.5.0) (2022-12-20)

#### Bug Fixes

* **job:** fetch parent before job moves to complete ([#1580](https://github.com/taskforcesh/bullmq/issues/1580)) ([6a6c0dc](https://github.com/taskforcesh/bullmq/commit/6a6c0dca30bb0a2417e0c62d4c80202c750322dd))
* **sandbox:** throw error when no exported function ([#1588](https://github.com/taskforcesh/bullmq/issues/1588)) fixes [#1587](https://github.com/taskforcesh/bullmq/issues/1587) ([c031891](https://github.com/taskforcesh/bullmq/commit/c03189184c8eeeb324f005b86e93d114abbe2154))

#### Features

* **queue:** add getJobState method ([#1593](https://github.com/taskforcesh/bullmq/issues/1593)) ref [#1532](https://github.com/taskforcesh/bullmq/issues/1532) ([b741e84](https://github.com/taskforcesh/bullmq/commit/b741e8456f262b51aa7c68f571c76a3c54d02d37))

### [3.4.2](https://github.com/taskforcesh/bullmq/compare/v3.4.1...v3.4.2) (2022-12-15)

#### Performance Improvements

* **counts:** delete delayed marker when needed ([#1583](https://github.com/taskforcesh/bullmq/issues/1583)) ([cc26f1c](https://github.com/taskforcesh/bullmq/commit/cc26f1cd550de76c7588d3a98187b80ee78c40c4))
* **get-children-values:** replace slow object destructuring with single object ([#1586](https://github.com/taskforcesh/bullmq/issues/1586)) ([857d403](https://github.com/taskforcesh/bullmq/commit/857d40377a6eb2c0101e6d16d9085ecd4b52b016))

### [3.4.1](https://github.com/taskforcesh/bullmq/compare/v3.4.0...v3.4.1) (2022-12-10)

#### Bug Fixes

* **exponential:** respect exponential backoff delay ([#1581](https://github.com/taskforcesh/bullmq/issues/1581)) ([145dd32](https://github.com/taskforcesh/bullmq/commit/145dd329bb9f8254b404f4c5fbf7a50359202d37))
* **get-jobs:** filter marker ([#1551](https://github.com/taskforcesh/bullmq/issues/1551)) ([4add0ef](https://github.com/taskforcesh/bullmq/commit/4add0efa7857cc2f7b6d3c0c78a7f82cb7a46933))

## [3.4.0](https://github.com/taskforcesh/bullmq/compare/v3.3.5...v3.4.0) (2022-12-09)

#### Features

* **worker:** add ready event for blockingConnection ([#1577](https://github.com/taskforcesh/bullmq/issues/1577)) ([992cc9e](https://github.com/taskforcesh/bullmq/commit/992cc9e9b3046185d3b67f2cc956f30337f458e1))

### [3.3.5](https://github.com/taskforcesh/bullmq/compare/v3.3.4...v3.3.5) (2022-12-08)

#### Bug Fixes

* **worker:** add token postfix ([#1575](https://github.com/taskforcesh/bullmq/issues/1575)) ([1d3e368](https://github.com/taskforcesh/bullmq/commit/1d3e368021041bb9861761c86fe3e04914b0c52f))

### [3.3.4](https://github.com/taskforcesh/bullmq/compare/v3.3.3...v3.3.4) (2022-12-07)

#### Bug Fixes

* **worker:** try catch setname call ([#1576](https://github.com/taskforcesh/bullmq/issues/1576)) fixes [#1574](https://github.com/taskforcesh/bullmq/issues/1574) ([0c42fd8](https://github.com/taskforcesh/bullmq/commit/0c42fd8c07dbac7ace81e97e45440af93fc622a5))

### [3.3.3](https://github.com/taskforcesh/bullmq/compare/v3.3.2...v3.3.3) (2022-12-07)

#### Bug Fixes

* do not allow move from active to wait if not owner of the job ([dc1a307](https://github.com/taskforcesh/bullmq/commit/dc1a3077d1521c5dc99824a7fc05d17da03906bc))

### [3.3.2](https://github.com/taskforcesh/bullmq/compare/v3.3.1...v3.3.2) (2022-12-05)

#### Bug Fixes

* floor pexpire to integer ([1d5de42](https://github.com/taskforcesh/bullmq/commit/1d5de425a19ebf879a8f9a7e0543d87a4d358be1))

### [3.3.1](https://github.com/taskforcesh/bullmq/compare/v3.3.0...v3.3.1) (2022-12-05)

#### Bug Fixes

* **get-workers:** set name when ready event in connection ([#1564](https://github.com/taskforcesh/bullmq/issues/1564)) ([de93c17](https://github.com/taskforcesh/bullmq/commit/de93c172901650e1666c48423a39076f2c7b9c7b))
* **job:** console warn custom job ids when they represent integers ([#1569](https://github.com/taskforcesh/bullmq/issues/1569)) ([6e677d2](https://github.com/taskforcesh/bullmq/commit/6e677d2800957b368bef4247b8e4328c5758f262))

## [3.3.0](https://github.com/taskforcesh/bullmq/compare/v3.2.5...v3.3.0) (2022-12-04)

#### Features

* **queue-events:** support duplicated event ([#1549](https://github.com/taskforcesh/bullmq/issues/1549)) ([18bc4eb](https://github.com/taskforcesh/bullmq/commit/18bc4eb50432f8aa27f2395750a7617317b66ca1))

### [3.2.5](https://github.com/taskforcesh/bullmq/compare/v3.2.4...v3.2.5) (2022-12-04)

#### Bug Fixes

* **add-job:** throw error when jobId represents an integer ([#1556](https://github.com/taskforcesh/bullmq/issues/1556)) ([db617d7](https://github.com/taskforcesh/bullmq/commit/db617d79e8f55b5c9e0df4b6bfd4247612016da1))

### [3.2.4](https://github.com/taskforcesh/bullmq/compare/v3.2.3...v3.2.4) (2022-11-29)

#### Bug Fixes

* **add-job:** do not update job that already exist ([#1550](https://github.com/taskforcesh/bullmq/issues/1550)) ([26f6311](https://github.com/taskforcesh/bullmq/commit/26f6311cd0d2b936e404d0abebca9637f314a209))

### [3.2.3](https://github.com/taskforcesh/bullmq/compare/v3.2.2...v3.2.3) (2022-11-29)

#### Bug Fixes

* **rate-limit:** delete rateLimiterKey when 0 ([#1553](https://github.com/taskforcesh/bullmq/issues/1553)) ([0b88e5b](https://github.com/taskforcesh/bullmq/commit/0b88e5b94b4a0dc0d4000f7fd4b327f402248ad2))

### [3.2.2](https://github.com/taskforcesh/bullmq/compare/v3.2.1...v3.2.2) (2022-11-15)

#### Bug Fixes

* **rate-limit:** check job is active before moving to wait ([9502167](https://github.com/taskforcesh/bullmq/commit/9502167bb0d9008fc8811ff7980dc8126fbc5ac2))

### [3.2.1](https://github.com/taskforcesh/bullmq/compare/v3.2.0...v3.2.1) (2022-11-15)

#### Bug Fixes

* **worker:** consider removed jobs in failed event ([#1500](https://github.com/taskforcesh/bullmq/issues/1500)) ([8704b9a](https://github.com/taskforcesh/bullmq/commit/8704b9a10575fd7df738296f7156057123592b86))

## [3.2.0](https://github.com/taskforcesh/bullmq/compare/v3.1.3...v3.2.0) (2022-11-09)

#### Features

* **flow:** move parent to delayed when delay option is provided ([#1501](https://github.com/taskforcesh/bullmq/issues/1501)) ([2f3e5d5](https://github.com/taskforcesh/bullmq/commit/2f3e5d54f0797bf0d1adf14dbb2b51ad9f9183ca))

### [3.1.3](https://github.com/taskforcesh/bullmq/compare/v3.1.2...v3.1.3) (2022-11-04)

#### Bug Fixes

* **delayed:** better handling of marker id ([816376e](https://github.com/taskforcesh/bullmq/commit/816376e7880ae0eafe85a1f9a5aef9fdfe3031a9))
* **delayed:** notify workers a delayed job is closer in time fixes [#1505](https://github.com/taskforcesh/bullmq/issues/1505) ([6ced4d0](https://github.com/taskforcesh/bullmq/commit/6ced4d06c5c9c8342c9e4f7920a21826871eac1b))
* **job:** better error message in moveToFailed ([4e9f5bb](https://github.com/taskforcesh/bullmq/commit/4e9f5bb90f87c66eca959ffc9b7a09e05908c2d9))
* **moveToFinish:** always promote delayed jobs ([7610cc3](https://github.com/taskforcesh/bullmq/commit/7610cc37d4695a885043c251990e153d4ce4440f))
* **moveToFinished:** revert move promoteDelayedJobs ([7d780db](https://github.com/taskforcesh/bullmq/commit/7d780dbc1d7728ab7b762a5578871b31f27ff80c))

### [3.1.2](https://github.com/taskforcesh/bullmq/compare/v3.1.1...v3.1.2) (2022-11-04)

#### Bug Fixes

* **repeat:** allow easy migration from bullmq <3 to >=3 ([e17b886](https://github.com/taskforcesh/bullmq/commit/e17b886d3e2978e25f23f1a99b88562537a08576))

### [3.1.1](https://github.com/taskforcesh/bullmq/compare/v3.1.0...v3.1.1) (2022-11-03)

#### Bug Fixes

* **change-delay:** remove delayed stream ([#1509](https://github.com/taskforcesh/bullmq/issues/1509)) ([6e4809e](https://github.com/taskforcesh/bullmq/commit/6e4809e5d8f7ef35bc0871d21bfcdcb0f1f316c6))
* **worker:** restore dynamic concurrency change ([#1515](https://github.com/taskforcesh/bullmq/issues/1515)) ([fdac5c2](https://github.com/taskforcesh/bullmq/commit/fdac5c27607dfaaaad1c1256c47f2ae448efcd21))

## [3.1.0](https://github.com/taskforcesh/bullmq/compare/v3.0.1...v3.1.0) (2022-11-02)

#### Features

* **workers:** better error message for missing lock ([bf1d086](https://github.com/taskforcesh/bullmq/commit/bf1d0860c70bcc2b604d02ca47e5db64f962d71d))

### [3.0.1](https://github.com/taskforcesh/bullmq/compare/v3.0.0...v3.0.1) (2022-11-02)

#### Bug Fixes

* **move-to-delayed:** consider promoting delayed jobs ([#1493](https://github.com/taskforcesh/bullmq/issues/1493)) ([909da2b](https://github.com/taskforcesh/bullmq/commit/909da2bc2718a588379b3fdd9791bc8e51ad1dad))
* **retry-job:** consider promoting delayed jobs ([#1508](https://github.com/taskforcesh/bullmq/issues/1508)) ([d0b3412](https://github.com/taskforcesh/bullmq/commit/d0b3412d222449c24ab36068a791d08ea19ed922))

## [3.0.0](https://github.com/taskforcesh/bullmq/compare/v2.4.0...v3.0.0) (2022-10-25)

#### Bug Fixes

* **backoff:** handle backoff strategy as function ([#1463](https://github.com/taskforcesh/bullmq/issues/1463)) ([3640269](https://github.com/taskforcesh/bullmq/commit/36402691a3c7fa500f07e2e11a28318099bdb909))
* **repeat:** remove cron in favor of pattern option ([#1456](https://github.com/taskforcesh/bullmq/issues/1456)) ([3cc150e](https://github.com/taskforcesh/bullmq/commit/3cc150e32cb5971ad4ba6ff91246aaf75296c165))

#### Features

* add support for dynamic rate limiting ([2d51d2b](https://github.com/taskforcesh/bullmq/commit/2d51d2b33ef49059503e1bca7a582c71f6861ef4))
* **rate-limit:** remove group key support and improve global rate limit ([81f780a](https://github.com/taskforcesh/bullmq/commit/81f780aeed81e670107d01d01265d407a30e2a62))

#### BREAKING CHANGES

* **rate-limit:** limit by group keys has been removed in favor of a much simpler and efficent rate-limit implementation.
* **backoff:** object mapping is replaced by single function


# v2

## [2.4.0](https://github.com/taskforcesh/bullmq/compare/v2.3.2...v2.4.0) (2022-10-24)

#### Features

* **flows:** allow parent on root jobs in addBulk method ([#1488](https://github.com/taskforcesh/bullmq/issues/1488)) ref [#1480](https://github.com/taskforcesh/bullmq/issues/1480) ([92308e5](https://github.com/taskforcesh/bullmq/commit/92308e53acf14e0ce108d94ecd616633ac93e35d))

### [2.3.2](https://github.com/taskforcesh/bullmq/compare/v2.3.1...v2.3.2) (2022-10-18)

#### Bug Fixes

* **job:** send failed event when failParentOnFailure ([#1481](https://github.com/taskforcesh/bullmq/issues/1481)) fixes [#1469](https://github.com/taskforcesh/bullmq/issues/1469) ([b20eb6f](https://github.com/taskforcesh/bullmq/commit/b20eb6f65c7e2c4593d5f9f4d4b940f780bf26d2))

### [2.3.1](https://github.com/taskforcesh/bullmq/compare/v2.3.0...v2.3.1) (2022-10-13)

#### Bug Fixes

* **redis:** replace throw exception by console.error ([fafa2f8](https://github.com/taskforcesh/bullmq/commit/fafa2f89e796796f950e6c4abbdda4d3d71ad1b0))

## [2.3.0](https://github.com/taskforcesh/bullmq/compare/v2.2.1...v2.3.0) (2022-10-13)

#### Features

* **redis-connection:** allow providing scripts for extension ([#1472](https://github.com/taskforcesh/bullmq/issues/1472)) ([f193cfb](https://github.com/taskforcesh/bullmq/commit/f193cfb1830e127f9fd47a969baad30011a0e3a4))

### [2.2.1](https://github.com/taskforcesh/bullmq/compare/v2.2.0...v2.2.1) (2022-10-11)

#### Performance Improvements

* **scripts:** pre-build scripts ([#1441](https://github.com/taskforcesh/bullmq/issues/1441)) ([7f72603](https://github.com/taskforcesh/bullmq/commit/7f72603d463f705d0617898cb221f832c49a4aa3))

## [2.2.0](https://github.com/taskforcesh/bullmq/compare/v2.1.3...v2.2.0) (2022-10-10)

#### Bug Fixes

* **connection:** validate array of strings in Cluster ([#1468](https://github.com/taskforcesh/bullmq/issues/1468)) fixes [#1467](https://github.com/taskforcesh/bullmq/issues/1467) ([8355182](https://github.com/taskforcesh/bullmq/commit/8355182a372b68ec62e9c3953bacbd69e0abfc74))

#### Features

* **flow-producer:** allow parent opts in root job when adding a flow ([#1110](https://github.com/taskforcesh/bullmq/issues/1110)) ref [#1097](https://github.com/taskforcesh/bullmq/issues/1097) ([3c3ac71](https://github.com/taskforcesh/bullmq/commit/3c3ac718ad84f6bd0cc1575013c948e767b46f38))

### [2.1.3](https://github.com/taskforcesh/bullmq/compare/v2.1.2...v2.1.3) (2022-09-30)

#### Bug Fixes

* **worker:** clear stalled jobs timer when closing worker ([1567a0d](https://github.com/taskforcesh/bullmq/commit/1567a0df0ca3c8d43a18990fe488888f4ff68040))

### [2.1.2](https://github.com/taskforcesh/bullmq/compare/v2.1.1...v2.1.2) (2022-09-29)

#### Bug Fixes

* **getters:** fix return type of getJobLogs ([d452927](https://github.com/taskforcesh/bullmq/commit/d4529278c59b2c94eee604c7d4455acc490679e9))

### [2.1.1](https://github.com/taskforcesh/bullmq/compare/v2.1.0...v2.1.1) (2022-09-28)

#### Bug Fixes

* **sandbox:** get open port using built-in module instead of get-port ([#1446](https://github.com/taskforcesh/bullmq/issues/1446)) ([6db6288](https://github.com/taskforcesh/bullmq/commit/6db628868a9d64c5a3e47d1c9201017e6d05c1ae))

## [2.1.0](https://github.com/taskforcesh/bullmq/compare/v2.0.2...v2.1.0) (2022-09-23)

#### Features

* **job-options:** add failParentOnFailure option ([#1339](https://github.com/taskforcesh/bullmq/issues/1339)) ([65e5c36](https://github.com/taskforcesh/bullmq/commit/65e5c3678771f26555c9128bdb908dd62e3584f9))

### [2.0.2](https://github.com/taskforcesh/bullmq/compare/v2.0.1...v2.0.2) (2022-09-22)

#### Bug Fixes

* **job:** update delay value when moving to wait ([#1436](https://github.com/taskforcesh/bullmq/issues/1436)) ([9560915](https://github.com/taskforcesh/bullmq/commit/95609158c1800cf661f22ad7995541fb9474826a))

### [2.0.1](https://github.com/taskforcesh/bullmq/compare/v2.0.0...v2.0.1) (2022-09-21)

#### Bug Fixes

* **connection:** throw error when no noeviction policy ([3468390](https://github.com/taskforcesh/bullmq/commit/3468390dd6331291f4cf71a54c32028a06d1d99e))

#### Performance Improvements

* **events:** remove data and opts from added event ([e13d4b8](https://github.com/taskforcesh/bullmq/commit/e13d4b8e0c4f99203f4249ccc86e369d124ff483))

## [2.0.0](https://github.com/taskforcesh/bullmq/compare/v1.91.1...v2.0.0) (2022-09-21)

#### Bug Fixes

* **compat:** remove Queue3 class ([#1421](https://github.com/taskforcesh/bullmq/issues/1421)) ([fc797f7](https://github.com/taskforcesh/bullmq/commit/fc797f7cd334c19a95cb1290ddb6611cd3417179))
* **delayed:** promote delayed jobs instead of picking one by one ([1b938af](https://github.com/taskforcesh/bullmq/commit/1b938af75069d69772ddf2b03f95db7f53eada68))
* **delayed:** remove marker when promoting delayed job ([1aea0dc](https://github.com/taskforcesh/bullmq/commit/1aea0dcc5fb29086cef3d0c432c387d6f8261963))
* **getters:** compensate for "mark" job id ([231b9aa](https://github.com/taskforcesh/bullmq/commit/231b9aa0f4781e4493d3ea272c33b27c0b7dc0ab))
* **sandbox:** remove progress method ([b43267b](https://github.com/taskforcesh/bullmq/commit/b43267be50f9eade8233500d189d46940a01cc29))
* **stalled-jobs:** handle job id 0 ([829e6e0](https://github.com/taskforcesh/bullmq/commit/829e6e0252e78bf2cbc55ab1d3bd153faa0cee4c))
* **worker:** do not allow stalledInterval to be less than zero ([831ffc5](https://github.com/taskforcesh/bullmq/commit/831ffc520ccd3c6ea63af6b04ddddc9f7829c667))
* **workers:** use connection closing to determine closing status ([fe1d173](https://github.com/taskforcesh/bullmq/commit/fe1d17321f1eb49bd872c52965392add22729941))

#### Features

* improve delayed jobs and remove QueueScheduler ([1f66e5a](https://github.com/taskforcesh/bullmq/commit/1f66e5a6c891d52e0671e58a685dbca511e45e7e))
* move stalled jobs check and handling to Worker class from QueueScheduler ([13769cb](https://github.com/taskforcesh/bullmq/commit/13769cbe38ba22793cbc66e9706a6be28a7f1512))

#### BREAKING CHANGES

* **compat:** The compatibility class for Bullv3 is no longer available.
* The QueueScheduler class is removed since it is not necessary anymore. Delayed jobs are now handled in a much simpler and robust way, without the need of a separate process.
* Failed and stalled events are now produced by the Worker class instead of by the QueueScheduler.
* The minimum Redis recommended version is 6.2.0.


# v1

### [1.91.1](https://github.com/taskforcesh/bullmq/compare/v1.91.0...v1.91.1) (2022-09-18)

#### Bug Fixes

* **drain:** consider empty active list ([#1412](https://github.com/taskforcesh/bullmq/issues/1412)) ([f919a50](https://github.com/taskforcesh/bullmq/commit/f919a50b2f4972dcb9ecd5848b0f7fd9a0e137ea))

## [1.91.0](https://github.com/taskforcesh/bullmq/compare/v1.90.2...v1.91.0) (2022-09-16)

#### Features

* **sandbox:** support update method ([#1416](https://github.com/taskforcesh/bullmq/issues/1416)) ([606b75d](https://github.com/taskforcesh/bullmq/commit/606b75d53e12dfc109f01eda38736c07e829e9b7))

### [1.90.2](https://github.com/taskforcesh/bullmq/compare/v1.90.1...v1.90.2) (2022-09-12)

#### Performance Improvements

* **script-loader:** use cache to read script once ([#1410](https://github.com/taskforcesh/bullmq/issues/1410)) ([f956e93](https://github.com/taskforcesh/bullmq/commit/f956e937ae3488cdcd0e2eacbe3e096c8066ebd1))

### [1.90.1](https://github.com/taskforcesh/bullmq/compare/v1.90.0...v1.90.1) (2022-09-02)

#### Performance Improvements

* **add-job:** handle parent split on js ([#1397](https://github.com/taskforcesh/bullmq/issues/1397)) ([566f074](https://github.com/taskforcesh/bullmq/commit/566f0747110679e5b07e7642fef793744565fffe))

## [1.90.0](https://github.com/taskforcesh/bullmq/compare/v1.89.2...v1.90.0) (2022-08-30)

#### Features

* **repeat:** allow passing a cron strategy ([#1248](https://github.com/taskforcesh/bullmq/issues/1248)) ref [#1245](https://github.com/taskforcesh/bullmq/issues/1245) ([7f0534f](https://github.com/taskforcesh/bullmq/commit/7f0534f72449ae14a7415fa17a2eb2a70136a8b0))

### [1.89.2](https://github.com/taskforcesh/bullmq/compare/v1.89.1...v1.89.2) (2022-08-23)

#### Bug Fixes

* **job:** update delay when changeDelay ([#1389](https://github.com/taskforcesh/bullmq/issues/1389)) fixes [#1160](https://github.com/taskforcesh/bullmq/issues/1160) ([d9b100d](https://github.com/taskforcesh/bullmq/commit/d9b100d04112c518ef2efbcf5586aa1226ccccab))

### [1.89.1](https://github.com/taskforcesh/bullmq/compare/v1.89.0...v1.89.1) (2022-08-19)

#### Bug Fixes

* revert "chore: allow esm imports through exports field" ([#1388](https://github.com/taskforcesh/bullmq/issues/1388)) ([8e51272](https://github.com/taskforcesh/bullmq/commit/8e512724b1e8145bceb0152b70a934decf6d6864))

## [1.89.0](https://github.com/taskforcesh/bullmq/compare/v1.88.2...v1.89.0) (2022-08-18)

#### Features

* **job:** expose delay in instance ([#1386](https://github.com/taskforcesh/bullmq/issues/1386)) ([d4d0d2e](https://github.com/taskforcesh/bullmq/commit/d4d0d2e737c7ceb5eb34a2c50d53bd1081e0ad4a))

### [1.88.2](https://github.com/taskforcesh/bullmq/compare/v1.88.1...v1.88.2) (2022-08-18)

#### Bug Fixes

* revert "feat(sandbox): experimental support ESM" ([#1384](https://github.com/taskforcesh/bullmq/issues/1384)) ([7d180eb](https://github.com/taskforcesh/bullmq/commit/7d180eb18daa41062dcbca72213bc9d9f40153db))

### [1.88.1](https://github.com/taskforcesh/bullmq/compare/v1.88.0...v1.88.1) (2022-08-17)

#### Bug Fixes

* fix husky install ([edee918](https://github.com/taskforcesh/bullmq/commit/edee918e84ba895ed4ef63cabcc26b97d9c52d8d))

## [1.88.0](https://github.com/taskforcesh/bullmq/compare/v1.87.2...v1.88.0) (2022-08-17)

#### Bug Fixes

* **clean:** consider priority when cleaning waiting jobs ([#1357](https://github.com/taskforcesh/bullmq/issues/1357)) ([ced5be1](https://github.com/taskforcesh/bullmq/commit/ced5be1c9531953baa9cf87d6bda3faa5863270d))
* **parent-priority-check:** use tonumber on priority ([#1370](https://github.com/taskforcesh/bullmq/issues/1370)) ([e2043c6](https://github.com/taskforcesh/bullmq/commit/e2043c6f4b8ad5faea8c13edde76aea60612fec6))

#### Features

* **sandbox:** experimental support ESM ([ed0faff](https://github.com/taskforcesh/bullmq/commit/ed0faff3c67c436116eb625ffacb03e435caee3f))

### [1.87.2](https://github.com/taskforcesh/bullmq/compare/v1.87.1...v1.87.2) (2022-08-13)

#### Bug Fixes

* **move-parent-to-wait:** emit waiting instead of active event ([#1356](https://github.com/taskforcesh/bullmq/issues/1356)) ([53578dd](https://github.com/taskforcesh/bullmq/commit/53578dd1cbe31b49361a833b1aca449486f3b925))

### [1.87.1](https://github.com/taskforcesh/bullmq/compare/v1.87.0...v1.87.1) (2022-08-09)

#### Bug Fixes

* **job:** declare discarded as protected ([#1352](https://github.com/taskforcesh/bullmq/issues/1352)) ([870e01c](https://github.com/taskforcesh/bullmq/commit/870e01c4ab602c1e6e351cc369f3eac5f7afa083))

## [1.87.0](https://github.com/taskforcesh/bullmq/compare/v1.86.10...v1.87.0) (2022-08-05)

#### Features

* **flow:** consider priority when parent is moved ([#1286](https://github.com/taskforcesh/bullmq/issues/1286)) ([d49760d](https://github.com/taskforcesh/bullmq/commit/d49760d09420c5fcc99ab06c8fe36168755fd397))

### [1.86.10](https://github.com/taskforcesh/bullmq/compare/v1.86.9...v1.86.10) (2022-07-29)

#### Performance Improvements

* **clean-jobs-in-set:** use ZRANGEBYSCORE when limit > 0 ([#1338](https://github.com/taskforcesh/bullmq/issues/1338)) ([f0d9985](https://github.com/taskforcesh/bullmq/commit/f0d998541f03778ca2a092080a19e6bf7b7d0af1))

### [1.86.9](https://github.com/taskforcesh/bullmq/compare/v1.86.8...v1.86.9) (2022-07-27)

#### Bug Fixes

* **get-flow:** consider groupKey ([#1336](https://github.com/taskforcesh/bullmq/issues/1336)) fixes [#1334](https://github.com/taskforcesh/bullmq/issues/1334) ([9f31272](https://github.com/taskforcesh/bullmq/commit/9f31272fa8b3f5b8ab26f15e21bd80537c5baef0))

### [1.86.8](https://github.com/taskforcesh/bullmq/compare/v1.86.7...v1.86.8) (2022-07-26)

#### Bug Fixes

* **promote:** consider empty queue when paused ([#1335](https://github.com/taskforcesh/bullmq/issues/1335)) ([9f742e8](https://github.com/taskforcesh/bullmq/commit/9f742e88d6338ce9ac7e0413bdac411ab6cf675c))

### [1.86.7](https://github.com/taskforcesh/bullmq/compare/v1.86.6...v1.86.7) (2022-07-15)

#### Bug Fixes

* **sandboxed-process:** consider UnrecoverableError ([#1320](https://github.com/taskforcesh/bullmq/issues/1320)) fixes [#1317](https://github.com/taskforcesh/bullmq/issues/1317) ([c1269cc](https://github.com/taskforcesh/bullmq/commit/c1269cc772c6cec84d82ff790b9a7c9cc4242dcb))

### [1.86.6](https://github.com/taskforcesh/bullmq/compare/v1.86.5...v1.86.6) (2022-07-14)

#### Bug Fixes

* **retry-jobs:** consider paused queue ([#1321](https://github.com/taskforcesh/bullmq/issues/1321)) ([3e9703d](https://github.com/taskforcesh/bullmq/commit/3e9703d17fc9dc601d5d77e999f3e9a137f20843))

### [1.86.5](https://github.com/taskforcesh/bullmq/compare/v1.86.4...v1.86.5) (2022-07-09)

#### Bug Fixes

* **retry-job:** consider paused queue ([#1314](https://github.com/taskforcesh/bullmq/issues/1314)) ([907ae1d](https://github.com/taskforcesh/bullmq/commit/907ae1d7e3504f31c625ec8a09e32785f08357ff))

### [1.86.4](https://github.com/taskforcesh/bullmq/compare/v1.86.3...v1.86.4) (2022-06-29)

#### Bug Fixes

* **parent:** emit waiting event when no pending children ([#1296](https://github.com/taskforcesh/bullmq/issues/1296)) ([aa8fa3f](https://github.com/taskforcesh/bullmq/commit/aa8fa3f8cd5ab6d7d309d87ae45c558249b1c29c))

### [1.86.3](https://github.com/taskforcesh/bullmq/compare/v1.86.2...v1.86.3) (2022-06-26)

#### Bug Fixes

* avoid calling delay() if queue is being closed ([#1295](https://github.com/taskforcesh/bullmq/issues/1295)) ([52a5045](https://github.com/taskforcesh/bullmq/commit/52a5045b903ed6e0e73dd747748787a6389f12f7))

### [1.86.2](https://github.com/taskforcesh/bullmq/compare/v1.86.1...v1.86.2) (2022-06-16)

#### Bug Fixes

* **queue:** get rid of repeat options from defaultJobOptions ([#1284](https://github.com/taskforcesh/bullmq/issues/1284)) ([cdd2a20](https://github.com/taskforcesh/bullmq/commit/cdd2a20c2c4ca47042ecd1da525ecb72941e4910))

### [1.86.1](https://github.com/taskforcesh/bullmq/compare/v1.86.0...v1.86.1) (2022-06-12)

#### Bug Fixes

* unpack empty metrics in batches ([96829db](https://github.com/taskforcesh/bullmq/commit/96829db839fad4489415f7dbb047abdca5566e78))

## [1.86.0](https://github.com/taskforcesh/bullmq/compare/v1.85.4...v1.86.0) (2022-06-10)

#### Features

* **repeat:** save repeatJobKey reference ([#1214](https://github.com/taskforcesh/bullmq/issues/1214)) ([4d5a8e3](https://github.com/taskforcesh/bullmq/commit/4d5a8e33b614cf099369c18298e5b2963b434b1b))

### [1.85.4](https://github.com/taskforcesh/bullmq/compare/v1.85.3...v1.85.4) (2022-06-08)

#### Bug Fixes

* **error-prototype:** define custom name for toJSON method ([#1272](https://github.com/taskforcesh/bullmq/issues/1272)) ([66d80da](https://github.com/taskforcesh/bullmq/commit/66d80da4a6043755c7d296addb31857816ea4da3))

### [1.85.3](https://github.com/taskforcesh/bullmq/compare/v1.85.2...v1.85.3) (2022-06-03)

#### Bug Fixes

* **queue:** fix addBulk signature ResultType ([#1268](https://github.com/taskforcesh/bullmq/issues/1268)) ([f6770cc](https://github.com/taskforcesh/bullmq/commit/f6770cc383b68bf7b2fa655cd9eda713a06835aa))

### [1.85.2](https://github.com/taskforcesh/bullmq/compare/v1.85.1...v1.85.2) (2022-06-01)

#### Bug Fixes

* **job:** save finishedOn attribute on instance ([#1267](https://github.com/taskforcesh/bullmq/issues/1267)) ([4cf6a63](https://github.com/taskforcesh/bullmq/commit/4cf6a63d197e6095841bb87cef297a9533ac79c3))

### [1.85.1](https://github.com/taskforcesh/bullmq/compare/v1.85.0...v1.85.1) (2022-05-31)

#### Performance Improvements

* **remove-job:** send prefix key instead of jobKey ([#1252](https://github.com/taskforcesh/bullmq/issues/1252)) ([452856a](https://github.com/taskforcesh/bullmq/commit/452856a6c8c6e67ffda595c26c30988a15c1c1a4))

## [1.85.0](https://github.com/taskforcesh/bullmq/compare/v1.84.1...v1.85.0) (2022-05-30)

#### Features

* **worker:** change the number of concurrent processes ([#1256](https://github.com/taskforcesh/bullmq/issues/1256)) ref [#22](https://github.com/taskforcesh/bullmq/issues/22) ([940dc8f](https://github.com/taskforcesh/bullmq/commit/940dc8f34d9a46dc9c8384661461bf0558e97600))

### [1.84.1](https://github.com/taskforcesh/bullmq/compare/v1.84.0...v1.84.1) (2022-05-27)

#### Bug Fixes

* **waiting-children:** pass right timestamp value in moveToWaitingChildren ([#1260](https://github.com/taskforcesh/bullmq/issues/1260)) ([0f993f7](https://github.com/taskforcesh/bullmq/commit/0f993f71ed481b02a3f859a2109177352336cb9a))

## [1.84.0](https://github.com/taskforcesh/bullmq/compare/v1.83.2...v1.84.0) (2022-05-26)

#### Features

* **flow-producer:** add event listener types ([#1257](https://github.com/taskforcesh/bullmq/issues/1257)) ([19ed099](https://github.com/taskforcesh/bullmq/commit/19ed099905cbb4f071370b2b6d67d9a378e3a8f8))

### [1.83.2](https://github.com/taskforcesh/bullmq/compare/v1.83.1...v1.83.2) (2022-05-24)

#### Bug Fixes

* **close:** emit ioredis:close event instead of error ([#1251](https://github.com/taskforcesh/bullmq/issues/1251)) fixes [#1231](https://github.com/taskforcesh/bullmq/issues/1231) ([74c1c38](https://github.com/taskforcesh/bullmq/commit/74c1c38f7ff468da1adc63aff160e31940d682a9))

### [1.83.1](https://github.com/taskforcesh/bullmq/compare/v1.83.0...v1.83.1) (2022-05-24)

#### Bug Fixes

* **get-workers:** use blockingConnection client to set clientName ([#1255](https://github.com/taskforcesh/bullmq/issues/1255)) fixes [#1254](https://github.com/taskforcesh/bullmq/issues/1254) ([df796bd](https://github.com/taskforcesh/bullmq/commit/df796bd0c085aff72cef001395809b3f1a8045e4))

## [1.83.0](https://github.com/taskforcesh/bullmq/compare/v1.82.3...v1.83.0) (2022-05-20)

#### Features

* **flow-producer:** easier to build extension ([#1250](https://github.com/taskforcesh/bullmq/issues/1250)) ([aaf637e](https://github.com/taskforcesh/bullmq/commit/aaf637e74b9610651fd9e4efc5ff349971b7bb26))

### [1.82.3](https://github.com/taskforcesh/bullmq/compare/v1.82.2...v1.82.3) (2022-05-19)

#### Bug Fixes

* **redis-connection:** save cluster opts and coerse redis version ([#1247](https://github.com/taskforcesh/bullmq/issues/1247)) ref [#1246](https://github.com/taskforcesh/bullmq/issues/1246) fixes [#1243](https://github.com/taskforcesh/bullmq/issues/1243) ([acb69b5](https://github.com/taskforcesh/bullmq/commit/acb69b57d7a6417b8ca9fe1576a94d16e41f12d7))

### [1.82.2](https://github.com/taskforcesh/bullmq/compare/v1.82.1...v1.82.2) (2022-05-17)

#### Bug Fixes

* **job:** add job helper attribute for extension ([#1242](https://github.com/taskforcesh/bullmq/issues/1242)) ([4d7ae9e](https://github.com/taskforcesh/bullmq/commit/4d7ae9e3fda23650e802ebac6b33ff3350f116f6))

### [1.82.1](https://github.com/taskforcesh/bullmq/compare/v1.82.0...v1.82.1) (2022-05-16)

#### Bug Fixes

* **remove-job:** pass right prev param in removed event ([#1237](https://github.com/taskforcesh/bullmq/issues/1237)) ([54df47e](https://github.com/taskforcesh/bullmq/commit/54df47edf715a0a2a42687bf827e0a62c03951a5))

## [1.82.0](https://github.com/taskforcesh/bullmq/compare/v1.81.4...v1.82.0) (2022-05-11)

#### Features

* **remove-repeatable:** return boolean depending on job existence ([#1239](https://github.com/taskforcesh/bullmq/issues/1239)) ref [#1235](https://github.com/taskforcesh/bullmq/issues/1235) ([59b0da7](https://github.com/taskforcesh/bullmq/commit/59b0da7d0e979e4f9e8a5b042acbdce433790611))

### [1.81.4](https://github.com/taskforcesh/bullmq/compare/v1.81.3...v1.81.4) (2022-05-05)

#### Bug Fixes

* **repeatable:** emit removed event when removing ([#1229](https://github.com/taskforcesh/bullmq/issues/1229)) ([7d2de8d](https://github.com/taskforcesh/bullmq/commit/7d2de8d075e5ee7774501429c5177b729c430c20))

### [1.81.3](https://github.com/taskforcesh/bullmq/compare/v1.81.2...v1.81.3) (2022-05-04)

#### Bug Fixes

* **remove-parent:** check removed record from waiting-children ([#1227](https://github.com/taskforcesh/bullmq/issues/1227)) ([e7b25d0](https://github.com/taskforcesh/bullmq/commit/e7b25d00acb860ee3df36c6214a7162b2cf79635))

### [1.81.2](https://github.com/taskforcesh/bullmq/compare/v1.81.1...v1.81.2) (2022-05-03)

#### Bug Fixes

* **stalled:** consider removeOnFail when failing jobs ([#1225](https://github.com/taskforcesh/bullmq/issues/1225)) fixes [#1171](https://github.com/taskforcesh/bullmq/issues/1171) ([38486cb](https://github.com/taskforcesh/bullmq/commit/38486cb4d7cbfc78bd64d71f19d8bfbc908f3fc7))

### [1.81.1](https://github.com/taskforcesh/bullmq/compare/v1.81.0...v1.81.1) (2022-04-29)

#### Bug Fixes

* **add-bulk:** use for loop and throw if error is present ([#1223](https://github.com/taskforcesh/bullmq/issues/1223)) fixes [#1222](https://github.com/taskforcesh/bullmq/issues/1222) ([564de4f](https://github.com/taskforcesh/bullmq/commit/564de4f907648f5a5667a845c5366f73cff1d384))

## [1.81.0](https://github.com/taskforcesh/bullmq/compare/v1.80.6...v1.81.0) (2022-04-26)

#### Features

* **move-to-delayed:** allow passing token ([#1213](https://github.com/taskforcesh/bullmq/issues/1213)) ([14f0e4a](https://github.com/taskforcesh/bullmq/commit/14f0e4a33d9ddfbaa1f86dbe7598e20a516a9d09))

### [1.80.6](https://github.com/taskforcesh/bullmq/compare/v1.80.5...v1.80.6) (2022-04-22)

#### Bug Fixes

* **job:** delete token when moving to delayed ([#1208](https://github.com/taskforcesh/bullmq/issues/1208)) ([37acf41](https://github.com/taskforcesh/bullmq/commit/37acf4109d17090dfaef992267e48130d34f7187))

### [1.80.5](https://github.com/taskforcesh/bullmq/compare/v1.80.4...v1.80.5) (2022-04-21)

#### Bug Fixes

* **queue-base:** emit close error when no closing ([#1203](https://github.com/taskforcesh/bullmq/issues/1203)) fixes [#1205](https://github.com/taskforcesh/bullmq/issues/1205) ([4d76582](https://github.com/taskforcesh/bullmq/commit/4d7658272af94b57a09486e1141b0e15a7bac3ba))

### [1.80.4](https://github.com/taskforcesh/bullmq/compare/v1.80.3...v1.80.4) (2022-04-19)

#### Bug Fixes

* **queue-scheduler:** apply isNotConnectionError ([#1189](https://github.com/taskforcesh/bullmq/issues/1189)) fixes [#1181](https://github.com/taskforcesh/bullmq/issues/1181) ([605d685](https://github.com/taskforcesh/bullmq/commit/605d68595d8fa1d9d47348a3fa9e0d7a4e28c706))

### [1.80.3](https://github.com/taskforcesh/bullmq/compare/v1.80.2...v1.80.3) (2022-04-15)

#### Bug Fixes

* **cluster:** check correct Upstash host ([#1195](https://github.com/taskforcesh/bullmq/issues/1195)) fixes [#1193](https://github.com/taskforcesh/bullmq/issues/1193) ([69f2863](https://github.com/taskforcesh/bullmq/commit/69f28632408c741219c1ba49304d36f49cf5cb83))

### [1.80.2](https://github.com/taskforcesh/bullmq/compare/v1.80.1...v1.80.2) (2022-04-15)

#### Bug Fixes

* **job:** remove Error from Promise return in moveToWaitingChildren ([#1197](https://github.com/taskforcesh/bullmq/issues/1197)) ([180a8bf](https://github.com/taskforcesh/bullmq/commit/180a8bf8fb2fe62b9929765a6dfd084574c77936))

### [1.80.1](https://github.com/taskforcesh/bullmq/compare/v1.80.0...v1.80.1) (2022-04-14)

#### Bug Fixes

* **worker:** restore worker suffix to empty string ([#1194](https://github.com/taskforcesh/bullmq/issues/1194)) fixes [#1185](https://github.com/taskforcesh/bullmq/issues/1185) ([2666ea5](https://github.com/taskforcesh/bullmq/commit/2666ea5b8532645da24482cf01c5692da5f2ceda))

## [1.80.0](https://github.com/taskforcesh/bullmq/compare/v1.79.1...v1.80.0) (2022-04-12)

#### Features

* **worker-listener:** use generics in events ([#1190](https://github.com/taskforcesh/bullmq/issues/1190)) ref [#1188](https://github.com/taskforcesh/bullmq/issues/1188) ([2821193](https://github.com/taskforcesh/bullmq/commit/28211937d9ed405330eede5ad7d4b0b817accf39))

### [1.79.1](https://github.com/taskforcesh/bullmq/compare/v1.79.0...v1.79.1) (2022-04-12)

#### Bug Fixes

* **connection:** remove Queue reconnect overrides ([#1119](https://github.com/taskforcesh/bullmq/issues/1119)) ([83f1c79](https://github.com/taskforcesh/bullmq/commit/83f1c797b8a5272028c8d78d5ce464236e90909e))

## [1.79.0](https://github.com/taskforcesh/bullmq/compare/v1.78.2...v1.79.0) (2022-04-08)

#### Features

* **queue-getters:** add getQueueEvents ([#1085](https://github.com/taskforcesh/bullmq/issues/1085)) ([f10a20a](https://github.com/taskforcesh/bullmq/commit/f10a20a90ab6dbf2d9f3f75ba99dacbdc797c329))

### [1.78.2](https://github.com/taskforcesh/bullmq/compare/v1.78.1...v1.78.2) (2022-03-31)

#### Bug Fixes

* **clean:** consider processedOn and finishedOn attributes ([#1158](https://github.com/taskforcesh/bullmq/issues/1158)) ([8c3cb72](https://github.com/taskforcesh/bullmq/commit/8c3cb72235ec6123da389553f37433c2943e0f57))

### [1.78.1](https://github.com/taskforcesh/bullmq/compare/v1.78.0...v1.78.1) (2022-03-24)

#### Bug Fixes

* **queue:** close repeat connection when calling close ([#1154](https://github.com/taskforcesh/bullmq/issues/1154)) ([7d79616](https://github.com/taskforcesh/bullmq/commit/7d796167229048ec79660ca5d3ac8a7c85d125e7))

## [1.78.0](https://github.com/taskforcesh/bullmq/compare/v1.77.3...v1.78.0) (2022-03-23)

#### Features

* **cron-parser:** upgrades version to 4.2.1 ([#1149](https://github.com/taskforcesh/bullmq/issues/1149)) fixes [#1147](https://github.com/taskforcesh/bullmq/issues/1147) ([88a6c9c](https://github.com/taskforcesh/bullmq/commit/88a6c9c437172035173628842909f5170eb481f7))

### [1.77.3](https://github.com/taskforcesh/bullmq/compare/v1.77.2...v1.77.3) (2022-03-22)

#### Bug Fixes

* **async-send:** check proc.send type ([#1150](https://github.com/taskforcesh/bullmq/issues/1150)) ([4f44173](https://github.com/taskforcesh/bullmq/commit/4f44173f0a3cc54705ca9a7e1730aeff26ea1c5a))

### [1.77.2](https://github.com/taskforcesh/bullmq/compare/v1.77.1...v1.77.2) (2022-03-20)

#### Bug Fixes

* **trim-events:** consider maxLenEvents as 0 ([#1137](https://github.com/taskforcesh/bullmq/issues/1137)) ([bc58a49](https://github.com/taskforcesh/bullmq/commit/bc58a49fba1b6f4e3595a0371ecf8410000a9021))

#### Performance Improvements

* **clean:** speed up clean operation using deletion marker ([#1144](https://github.com/taskforcesh/bullmq/issues/1144)) ([5fb32ef](https://github.com/taskforcesh/bullmq/commit/5fb32ef2c60843d8d1f2cbc000aacf4df3388b7e))

### [1.77.1](https://github.com/taskforcesh/bullmq/compare/v1.77.0...v1.77.1) (2022-03-17)

#### Bug Fixes

* **flow:** remove processed children ([#1060](https://github.com/taskforcesh/bullmq/issues/1060)) fixes [#1056](https://github.com/taskforcesh/bullmq/issues/1056) ([6b54e86](https://github.com/taskforcesh/bullmq/commit/6b54e86c12f287a13da036f3ec7801b8656f0434))

## [1.77.0](https://github.com/taskforcesh/bullmq/compare/v1.76.6...v1.77.0) (2022-03-16)

#### Features

* allow QueueScheduler to be extended ([289beb8](https://github.com/taskforcesh/bullmq/commit/289beb87d2ef3e3dd7583159f7be2b5450f7de3c))

### [1.76.6](https://github.com/taskforcesh/bullmq/compare/v1.76.5...v1.76.6) (2022-03-15)

#### Bug Fixes

* **master:** do not export master file ([#1136](https://github.com/taskforcesh/bullmq/issues/1136)) fixes [#1125](https://github.com/taskforcesh/bullmq/issues/1125) ref [#1129](https://github.com/taskforcesh/bullmq/issues/1129) ([6aa2f96](https://github.com/taskforcesh/bullmq/commit/6aa2f9657b8787aa791ab5af7267a6d27d7d7869))

### [1.76.5](https://github.com/taskforcesh/bullmq/compare/v1.76.4...v1.76.5) (2022-03-15)

#### Bug Fixes

* **queue:** sanitize job types in getJobs and getJobsCount ([#1113](https://github.com/taskforcesh/bullmq/issues/1113)) fixes [#1112](https://github.com/taskforcesh/bullmq/issues/1112) ([d452b29](https://github.com/taskforcesh/bullmq/commit/d452b29773cead153a73b8322adda3164fb610d8))

### [1.76.4](https://github.com/taskforcesh/bullmq/compare/v1.76.3...v1.76.4) (2022-03-13)

#### Performance Improvements

* **move-to-finished:** avoid an extra roundtrip when using rate limit ([#1131](https://github.com/taskforcesh/bullmq/issues/1131)) ([1711547](https://github.com/taskforcesh/bullmq/commit/171154707bf5cbcb750ea9d2a9957128c1abc044))

### [1.76.3](https://github.com/taskforcesh/bullmq/compare/v1.76.2...v1.76.3) (2022-03-10)

#### Bug Fixes

* **drained:** emit event only once when queue has drained the waiting list ([#1123](https://github.com/taskforcesh/bullmq/issues/1123)) fixes [#1121](https://github.com/taskforcesh/bullmq/issues/1121) ref [#1070](https://github.com/taskforcesh/bullmq/issues/1070) ([b89b4e8](https://github.com/taskforcesh/bullmq/commit/b89b4e8a83fe4c9349ac5a9c439fc07374ff1e63))

### [1.76.2](https://github.com/taskforcesh/bullmq/compare/v1.76.1...v1.76.2) (2022-03-09)

#### Bug Fixes

* **utils:** fix proc.send type ([#1122](https://github.com/taskforcesh/bullmq/issues/1122)) fixes [#1120](https://github.com/taskforcesh/bullmq/issues/1120) ([da23977](https://github.com/taskforcesh/bullmq/commit/da239774379825d9f0a51c118740bc0fefa568bd))

### [1.76.1](https://github.com/taskforcesh/bullmq/compare/v1.76.0...v1.76.1) (2022-03-04)

#### Bug Fixes

* **get-waiting-children-count:** consider waiting-children status only ([#1117](https://github.com/taskforcesh/bullmq/issues/1117)) ([1820df7](https://github.com/taskforcesh/bullmq/commit/1820df73c17ce119d2fdb0f526fc95f99845a5ec))

## [1.76.0](https://github.com/taskforcesh/bullmq/compare/v1.75.1...v1.76.0) (2022-03-02)

#### Features

* **metrics:** add metrics support ([ab51326](https://github.com/taskforcesh/bullmq/commit/ab51326cf318b4b48e37a1a77f5609e405eecb45))

### [1.75.1](https://github.com/taskforcesh/bullmq/compare/v1.75.0...v1.75.1) (2022-02-26)

#### Bug Fixes

* **rate-limiter:** move job to wait after retry when groupKey is missed ([#1103](https://github.com/taskforcesh/bullmq/issues/1103)) fixes [#1084](https://github.com/taskforcesh/bullmq/issues/1084) ([8aeab37](https://github.com/taskforcesh/bullmq/commit/8aeab37ac5a5c1c760be21bff2ba8752a485577c))

## [1.75.0](https://github.com/taskforcesh/bullmq/compare/v1.74.3...v1.75.0) (2022-02-24)

#### Bug Fixes

* **cluster:** check for host presence in Upstash validation ([#1102](https://github.com/taskforcesh/bullmq/issues/1102)) fixes [#1101](https://github.com/taskforcesh/bullmq/issues/1101) ([54d4eac](https://github.com/taskforcesh/bullmq/commit/54d4eac52cfe13d4be99410932c0226c8d06d5d5))

#### Features

* **retry-jobs:** allow to retry completed jobs ([#1082](https://github.com/taskforcesh/bullmq/issues/1082)) ([e17b3f2](https://github.com/taskforcesh/bullmq/commit/e17b3f21606757a16630988a69c9607e8c843bd2))

### [1.74.3](https://github.com/taskforcesh/bullmq/compare/v1.74.2...v1.74.3) (2022-02-24)

#### Bug Fixes

* **connection:** throw error when Upstash host is provided ([#1098](https://github.com/taskforcesh/bullmq/issues/1098)) fixes [#1087](https://github.com/taskforcesh/bullmq/issues/1087) ([5156d0a](https://github.com/taskforcesh/bullmq/commit/5156d0a4812d8c649a3b41bd98e3e0efb41d0491))

### [1.74.2](https://github.com/taskforcesh/bullmq/compare/v1.74.1...v1.74.2) (2022-02-23)

#### Bug Fixes

* **move-to-finished:** increment attemptsMade when moving job to active ([#1095](https://github.com/taskforcesh/bullmq/issues/1095)) fixes [#1094](https://github.com/taskforcesh/bullmq/issues/1094) ([321b0e1](https://github.com/taskforcesh/bullmq/commit/321b0e1d515d01c5b3f1ca9f404cd571e3f753b7))

### [1.74.1](https://github.com/taskforcesh/bullmq/compare/v1.74.0...v1.74.1) (2022-02-20)

#### Bug Fixes

* **flow:** respect defaultJobOptions from queue opts ([#1080](https://github.com/taskforcesh/bullmq/issues/1080)) fixes [#1034](https://github.com/taskforcesh/bullmq/issues/1034) ([0aca072](https://github.com/taskforcesh/bullmq/commit/0aca072f805302e660b6675fd4097ba893c91eb0))

## [1.74.0](https://github.com/taskforcesh/bullmq/compare/v1.73.0...v1.74.0) (2022-02-19)

#### Features

* **retry-jobs:** pass timestamp as option ([#1054](https://github.com/taskforcesh/bullmq/issues/1054)) ([1522359](https://github.com/taskforcesh/bullmq/commit/15223590b235f749af9cb229fc784760d4b3add2))

## [1.73.0](https://github.com/taskforcesh/bullmq/compare/v1.72.0...v1.73.0) (2022-02-16)

#### Features

* **job:** add prefix getter ([#1077](https://github.com/taskforcesh/bullmq/issues/1077)) ([db9ef10](https://github.com/taskforcesh/bullmq/commit/db9ef105a7a524d7502664d52bd9f9c7dfa9477f))
* **queue-getters:** add getQueueSchedulers ([#1078](https://github.com/taskforcesh/bullmq/issues/1078)) ref [#1075](https://github.com/taskforcesh/bullmq/issues/1075) ([0b3b1c4](https://github.com/taskforcesh/bullmq/commit/0b3b1c4382de34bd68733d162c2fa2ba9417f79c))

## [1.72.0](https://github.com/taskforcesh/bullmq/compare/v1.71.0...v1.72.0) (2022-02-15)

#### Features

* **backoff:** validate UnrecoverableError presence ([#1074](https://github.com/taskforcesh/bullmq/issues/1074)) ([1defeac](https://github.com/taskforcesh/bullmq/commit/1defeac3f251a13aad57f3027d8eb8f857e40acb))

## [1.71.0](https://github.com/taskforcesh/bullmq/compare/v1.70.0...v1.71.0) (2022-02-14)

#### Features

* **get-job-counts:** add default values ([#1068](https://github.com/taskforcesh/bullmq/issues/1068)) ([1c7f841](https://github.com/taskforcesh/bullmq/commit/1c7f841a52b3ea18fa7878f10986b362ccc6c4fe))

## [1.70.0](https://github.com/taskforcesh/bullmq/compare/v1.69.1...v1.70.0) (2022-02-11)

#### Features

* **sandbox:** pass parent property ([#1065](https://github.com/taskforcesh/bullmq/issues/1065)) ([1fd33f6](https://github.com/taskforcesh/bullmq/commit/1fd33f6fd3a3af17753de8c4d48e14ef86c7409c))

### [1.69.1](https://github.com/taskforcesh/bullmq/compare/v1.69.0...v1.69.1) (2022-02-10)

#### Bug Fixes

* **move-to-finished:** validate lock first ([#1064](https://github.com/taskforcesh/bullmq/issues/1064)) ([9da1b29](https://github.com/taskforcesh/bullmq/commit/9da1b29486c6c6e2b097ec2f6107494a36525495))

## [1.69.0](https://github.com/taskforcesh/bullmq/compare/v1.68.4...v1.69.0) (2022-02-08)

#### Features

* **job:** pass queueName into sandbox ([#1053](https://github.com/taskforcesh/bullmq/issues/1053)) fixes [#1050](https://github.com/taskforcesh/bullmq/issues/1050) ref [#1051](https://github.com/taskforcesh/bullmq/issues/1051) ([12bb19c](https://github.com/taskforcesh/bullmq/commit/12bb19c1586d8755b973a80be97f407630827d4f))

### [1.68.4](https://github.com/taskforcesh/bullmq/compare/v1.68.3...v1.68.4) (2022-02-05)

#### Bug Fixes

* **clean:** consider checking parent jobs when cleaning ([#1048](https://github.com/taskforcesh/bullmq/issues/1048)) ([0708a24](https://github.com/taskforcesh/bullmq/commit/0708a24c7f4cb6d1cda776ed983d3f20fc3261f1))

### [1.68.3](https://github.com/taskforcesh/bullmq/compare/v1.68.2...v1.68.3) (2022-02-04)

#### Bug Fixes

* **drain:** delete priority queueKey ([#1049](https://github.com/taskforcesh/bullmq/issues/1049)) ([2e6129a](https://github.com/taskforcesh/bullmq/commit/2e6129a4a08783eeafa2f0b69c10ac810f53d085))

### [1.68.2](https://github.com/taskforcesh/bullmq/compare/v1.68.1...v1.68.2) (2022-02-03)

#### Performance Improvements

* **remove-parent-dependency:** do not emit wait event in hard deletions ([#1045](https://github.com/taskforcesh/bullmq/issues/1045)) ([4069821](https://github.com/taskforcesh/bullmq/commit/40698218d13a880615f832a9926f0f057b1c33f9))

### [1.68.1](https://github.com/taskforcesh/bullmq/compare/v1.68.0...v1.68.1) (2022-02-01)

#### Bug Fixes

* **update:** throw error when missing job key ([#1042](https://github.com/taskforcesh/bullmq/issues/1042)) ([a00ae5c](https://github.com/taskforcesh/bullmq/commit/a00ae5c9b3f6d51cb0229adca29d13d932fc5601))

## [1.68.0](https://github.com/taskforcesh/bullmq/compare/v1.67.3...v1.68.0) (2022-01-29)

#### Features

* **queue:** add retryJobs method for failed jobs ([#1024](https://github.com/taskforcesh/bullmq/issues/1024)) ([310a730](https://github.com/taskforcesh/bullmq/commit/310a730ed322501cc19cdd5cf5244bc8eee6fee2))

#### Performance Improvements

* **lua:** call del command with multiple keys ([#1035](https://github.com/taskforcesh/bullmq/issues/1035)) ([9cfaab8](https://github.com/taskforcesh/bullmq/commit/9cfaab8965d0c9f92460d31d6c3083839c36447f))

### [1.67.3](https://github.com/taskforcesh/bullmq/compare/v1.67.2...v1.67.3) (2022-01-28)

#### Bug Fixes

* **drain:** consider checking parent jobs when draining ([#992](https://github.com/taskforcesh/bullmq/issues/992)) ([81b7221](https://github.com/taskforcesh/bullmq/commit/81b72213a9ff31d6b297825391de77557598ebd1))

### [1.67.2](https://github.com/taskforcesh/bullmq/compare/v1.67.1...v1.67.2) (2022-01-28)

#### Bug Fixes

* **repeat:** consider immediately option with cron ([#1030](https://github.com/taskforcesh/bullmq/issues/1030)) fixes [#1020](https://github.com/taskforcesh/bullmq/issues/1020) ([b9e7488](https://github.com/taskforcesh/bullmq/commit/b9e748870385a88b2384df40f50df3144c11d7e0))

### [1.67.1](https://github.com/taskforcesh/bullmq/compare/v1.67.0...v1.67.1) (2022-01-27)

#### Bug Fixes

* **retry:** pass state in error message ([#1027](https://github.com/taskforcesh/bullmq/issues/1027)) ([c646a45](https://github.com/taskforcesh/bullmq/commit/c646a45377fdfaff340185d1f7bedceb80c214c2))

#### Performance Improvements

* **retry:** delete props in retryJob lua script ([#1016](https://github.com/taskforcesh/bullmq/issues/1016)) ([547cedd](https://github.com/taskforcesh/bullmq/commit/547cedd5ecd30c9a73d37e4053b9e518cb3fbe53))

## [1.67.0](https://github.com/taskforcesh/bullmq/compare/v1.66.1...v1.67.0) (2022-01-26)

#### Features

* add support for removeOn based on time ([6c4ac75](https://github.com/taskforcesh/bullmq/commit/6c4ac75bb3ac239cc83ef6144d69c04b2bba1311))

### [1.66.1](https://github.com/taskforcesh/bullmq/compare/v1.66.0...v1.66.1) (2022-01-25)

#### Bug Fixes

* **job:** increase attemptsMade when moving job to active ([#1009](https://github.com/taskforcesh/bullmq/issues/1009)) fixes [#1002](https://github.com/taskforcesh/bullmq/issues/1002) ([0974ae0](https://github.com/taskforcesh/bullmq/commit/0974ae0ff6db73c223be4b18fb2aab53b6a23c88))

## [1.66.0](https://github.com/taskforcesh/bullmq/compare/v1.65.1...v1.66.0) (2022-01-23)

#### Features

* **queue-events:** add retries-exhausted event ([#1010](https://github.com/taskforcesh/bullmq/issues/1010)) ([e476f35](https://github.com/taskforcesh/bullmq/commit/e476f35f5c3f9b1baf2bbc3d46712b8ba597f73c))

### [1.65.1](https://github.com/taskforcesh/bullmq/compare/v1.65.0...v1.65.1) (2022-01-21)

#### Bug Fixes

* dont loop through empty modules paths ([#1013](https://github.com/taskforcesh/bullmq/issues/1013)) fixes [#1012](https://github.com/taskforcesh/bullmq/issues/1012) ([86e84df](https://github.com/taskforcesh/bullmq/commit/86e84df933c2662380b00a11b5f4000f2618d218))

## [1.65.0](https://github.com/taskforcesh/bullmq/compare/v1.64.4...v1.65.0) (2022-01-21)

#### Features

* **queue:** add JobType and JobState unions for better typing ([#1011](https://github.com/taskforcesh/bullmq/issues/1011)) ([3b9b79d](https://github.com/taskforcesh/bullmq/commit/3b9b79dbdd754ab66c3948e7e16380f2d5513262))

### [1.64.4](https://github.com/taskforcesh/bullmq/compare/v1.64.3...v1.64.4) (2022-01-19)

#### Bug Fixes

* **queue:** use 0 as initial value for getJobCountByTypes reducer ([#1005](https://github.com/taskforcesh/bullmq/issues/1005)) ([f0e23ef](https://github.com/taskforcesh/bullmq/commit/f0e23ef01b97d36c775db0bf8c9dd2f63f6cb194))

### [1.64.3](https://github.com/taskforcesh/bullmq/compare/v1.64.2...v1.64.3) (2022-01-17)

#### Bug Fixes

* **worker:** blockTime must be integer on older Redis ([6fedc0a](https://github.com/taskforcesh/bullmq/commit/6fedc0a03bdb217ef0dbae60d49fccb0f2a5dbdb))

### [1.64.2](https://github.com/taskforcesh/bullmq/compare/v1.64.1...v1.64.2) (2022-01-14)

#### Bug Fixes

* **remove-job:** consider removing parent dependency key in lua scripts ([#990](https://github.com/taskforcesh/bullmq/issues/990)) ([661abf0](https://github.com/taskforcesh/bullmq/commit/661abf0921e663c9ea2fa7d59c12da35950637dc))

### [1.64.1](https://github.com/taskforcesh/bullmq/compare/v1.64.0...v1.64.1) (2022-01-14)

#### Bug Fixes

* **sandbox:** exit uncaughtException instead of throwing error ([013d6a5](https://github.com/taskforcesh/bullmq/commit/013d6a5ee0c70266ae740abfa596ca9e506de71b))

## [1.64.0](https://github.com/taskforcesh/bullmq/compare/v1.63.3...v1.64.0) (2022-01-07)

#### Features

* **sanboxed-process:** support .cjs files ([#984](https://github.com/taskforcesh/bullmq/issues/984)) ([531e4de](https://github.com/taskforcesh/bullmq/commit/531e4de1525f2cf322e0b97f5537ed43276ff72b))

### [1.63.3](https://github.com/taskforcesh/bullmq/compare/v1.63.2...v1.63.3) (2022-01-06)

#### Bug Fixes

* **job:** throw error when delay and repeat are provided together ([#983](https://github.com/taskforcesh/bullmq/issues/983)) ([07b0082](https://github.com/taskforcesh/bullmq/commit/07b008273ead9360fc43564fa9ff1a7503616ceb))

### [1.63.2](https://github.com/taskforcesh/bullmq/compare/v1.63.1...v1.63.2) (2022-01-04)

#### Bug Fixes

* **queue:** add missing error event typing ([#979](https://github.com/taskforcesh/bullmq/issues/979)) ([afdaac6](https://github.com/taskforcesh/bullmq/commit/afdaac6b072c7af5973222cc7fb69f3f138f3b0b))

### [1.63.1](https://github.com/taskforcesh/bullmq/compare/v1.63.0...v1.63.1) (2022-01-04)

#### Bug Fixes

* **update-progress:** throw error if job key is missing ([#978](https://github.com/taskforcesh/bullmq/issues/978)) ref [#977](https://github.com/taskforcesh/bullmq/issues/977) ([b03aaf1](https://github.com/taskforcesh/bullmq/commit/b03aaf10ca694745d143def2129f952b9bac18a6))

## [1.63.0](https://github.com/taskforcesh/bullmq/compare/v1.62.0...v1.63.0) (2021-12-31)

#### Features

* **job:** use generic types for static methods ([#975](https://github.com/taskforcesh/bullmq/issues/975)) ([f78f4d0](https://github.com/taskforcesh/bullmq/commit/f78f4d0f75adb5c73558b3e8cf511db22f972791))

## [1.62.0](https://github.com/taskforcesh/bullmq/compare/v1.61.0...v1.62.0) (2021-12-31)

#### Bug Fixes

* add deprecated tag in progress and Queue3 class ([#973](https://github.com/taskforcesh/bullmq/issues/973)) ([6abdf5b](https://github.com/taskforcesh/bullmq/commit/6abdf5b66717cc8bc8ddb048029f7d9b92509942))

#### Features

* **queue:** add better event typing ([#971](https://github.com/taskforcesh/bullmq/issues/971)) ([596fd7b](https://github.com/taskforcesh/bullmq/commit/596fd7b260f2e95607f0eb4ff9553fb35137ec54))

## [1.61.0](https://github.com/taskforcesh/bullmq/compare/v1.60.0...v1.61.0) (2021-12-29)

#### Features

* **queue:** reuse generic typing for jobs ([5c10818](https://github.com/taskforcesh/bullmq/commit/5c10818d90724cccdf510f0358c01233aeac77e4))
* **worker:** reuse generic typing for jobs ([9adcdb7](https://github.com/taskforcesh/bullmq/commit/9adcdb798b4ee55835123a9f3d04c1397b176dc1))

## [1.60.0](https://github.com/taskforcesh/bullmq/compare/v1.59.4...v1.60.0) (2021-12-29)

#### Features

* **queue-scheduler:** add better event typing ([#963](https://github.com/taskforcesh/bullmq/issues/963)) ([b23c006](https://github.com/taskforcesh/bullmq/commit/b23c006e2bfce8a0709f0eb8e8739261b68c2f48))

### [1.59.4](https://github.com/taskforcesh/bullmq/compare/v1.59.3...v1.59.4) (2021-12-21)

#### Bug Fixes

* downgrade typescript to 3.9.10 fixes [#917](https://github.com/taskforcesh/bullmq/issues/917) ([#960](https://github.com/taskforcesh/bullmq/issues/960)) ([4e51fe0](https://github.com/taskforcesh/bullmq/commit/4e51fe00751092ee8f521039a3f2b41d881b71ae))

### [1.59.3](https://github.com/taskforcesh/bullmq/compare/v1.59.2...v1.59.3) (2021-12-21)

#### Bug Fixes

* **worker:** fix undefined moveToActive ([87e8cab](https://github.com/taskforcesh/bullmq/commit/87e8cab16dad6f8bd9e9ec369ef7e79f471180be))

### [1.59.2](https://github.com/taskforcesh/bullmq/compare/v1.59.1...v1.59.2) (2021-12-17)

#### Bug Fixes

* **package:** add jsnext:main prop ([#953](https://github.com/taskforcesh/bullmq/issues/953)) ([1a92bf7](https://github.com/taskforcesh/bullmq/commit/1a92bf7d41860f758841c5a833c1192d9a84a25f))

### [1.59.1](https://github.com/taskforcesh/bullmq/compare/v1.59.0...v1.59.1) (2021-12-17)

#### Bug Fixes

* copy lua files to correct location ([2be1120](https://github.com/taskforcesh/bullmq/commit/2be1120974692ee57ec00e30d6dbbef670d88a1e))

## [1.59.0](https://github.com/taskforcesh/bullmq/compare/v1.58.0...v1.59.0) (2021-12-17)

#### Bug Fixes

* correct dist path ([067d4c2](https://github.com/taskforcesh/bullmq/commit/067d4c2009b877f8bf6e6145507a41a53e5f7af3))

#### Features

* also export bullmq as an ESM ([e97e5b5](https://github.com/taskforcesh/bullmq/commit/e97e5b52b079adf2ed79f7cb61699e40a91e34e8))

## [1.58.0](https://github.com/taskforcesh/bullmq/compare/v1.57.4...v1.58.0) (2021-12-15)

#### Features

* **worker:** add better event typing ([#940](https://github.com/taskforcesh/bullmq/issues/940)) ([a326d4f](https://github.com/taskforcesh/bullmq/commit/a326d4f27e96ffa462a908ac14356d29839ff073))

### [1.57.4](https://github.com/taskforcesh/bullmq/compare/v1.57.3...v1.57.4) (2021-12-14)

#### Bug Fixes

* **move-to-active:** add try catch in moveToActive call ([#933](https://github.com/taskforcesh/bullmq/issues/933)) ([bab45b0](https://github.com/taskforcesh/bullmq/commit/bab45b05d08c625557e2df65921e12f48081d39c))
* **redis-connection:** consider cluster redisOptions config ([#934](https://github.com/taskforcesh/bullmq/issues/934)) ([5130f63](https://github.com/taskforcesh/bullmq/commit/5130f63ad969efa9649ab8f9abf36a72e8f553f4))

### [1.57.3](https://github.com/taskforcesh/bullmq/compare/v1.57.2...v1.57.3) (2021-12-14)

#### Bug Fixes

* remove debug console.error ([#932](https://github.com/taskforcesh/bullmq/issues/932)) ([271aac3](https://github.com/taskforcesh/bullmq/commit/271aac3417bc7f76ac02435b456552677b2847db))

### [1.57.2](https://github.com/taskforcesh/bullmq/compare/v1.57.1...v1.57.2) (2021-12-11)

#### Bug Fixes

* **connection:** check instance options to console log deprecation message ([#927](https://github.com/taskforcesh/bullmq/issues/927)) ([fc1e2b9](https://github.com/taskforcesh/bullmq/commit/fc1e2b9f3f20db53f9dc7ecdfa4644f02acc9f83))

#### Performance Improvements

* **add-job:** save parent data as json ([#859](https://github.com/taskforcesh/bullmq/issues/859)) ([556d4ee](https://github.com/taskforcesh/bullmq/commit/556d4ee427090f60270945a7fd438e2595bb43e9))

### [1.57.1](https://github.com/taskforcesh/bullmq/compare/v1.57.0...v1.57.1) (2021-12-11)

#### Bug Fixes

* **worker:** better handling of block timeout ([be4c933](https://github.com/taskforcesh/bullmq/commit/be4c933ae0a7a790d24a081b2ed4e7e1c0216e47))

## [1.57.0](https://github.com/taskforcesh/bullmq/compare/v1.56.0...v1.57.0) (2021-12-08)

#### Features

* **queue-events:** add better event typing ([#919](https://github.com/taskforcesh/bullmq/issues/919)) ([e980080](https://github.com/taskforcesh/bullmq/commit/e980080767bc56ae09a5c5cf33728a85a023bb42))

## [1.56.0](https://github.com/taskforcesh/bullmq/compare/v1.55.1...v1.56.0) (2021-12-06)

#### Bug Fixes

* emit drain event if no jobs left when completing ([9ad78a9](https://github.com/taskforcesh/bullmq/commit/9ad78a91c0a4a74cf84bd77d351d98195104f0b6))
* **worker:** use client for setting worker name ([af65c2c](https://github.com/taskforcesh/bullmq/commit/af65c2cd0d3fb232c617b018d4991f3276db11ea))

#### Features

* **worker:** make moveToActive protected ([d2897ee](https://github.com/taskforcesh/bullmq/commit/d2897ee7bbf4aee5251ac4fb28705f2bebbe7bfe))

### [1.55.1](https://github.com/taskforcesh/bullmq/compare/v1.55.0...v1.55.1) (2021-12-03)

#### Bug Fixes

* **worker:** always try to move to active after waiting for job ([#914](https://github.com/taskforcesh/bullmq/issues/914)) ([97b7084](https://github.com/taskforcesh/bullmq/commit/97b708451bf4ce14a461a50f8a24d14b0e40dd4b))

## [1.55.0](https://github.com/taskforcesh/bullmq/compare/v1.54.6...v1.55.0) (2021-12-02)

#### Features

* **script-loader:** lua script loader with include support ([#897](https://github.com/taskforcesh/bullmq/issues/897)) ([64b6ccf](https://github.com/taskforcesh/bullmq/commit/64b6ccf2a373b40d7ea763b3d35cf34f36ba11da))

### [1.54.6](https://github.com/taskforcesh/bullmq/compare/v1.54.5...v1.54.6) (2021-11-30)

#### Bug Fixes

* **stalled:** save finishedOn when job stalled more than allowable limit ([#900](https://github.com/taskforcesh/bullmq/issues/900)) ([eb89edf](https://github.com/taskforcesh/bullmq/commit/eb89edf2f4eb85dedb1485de32e79331940a654f))

### [1.54.5](https://github.com/taskforcesh/bullmq/compare/v1.54.4...v1.54.5) (2021-11-26)

#### Bug Fixes

* **tsconfig:** only include node types ([#895](https://github.com/taskforcesh/bullmq/issues/895)) ([5f4fdca](https://github.com/taskforcesh/bullmq/commit/5f4fdca5f416f2cd9d83eb0fba84e56c24320b63))

### [1.54.4](https://github.com/taskforcesh/bullmq/compare/v1.54.3...v1.54.4) (2021-11-24)

#### Bug Fixes

* **child-processor:** add deprecation warning for progress method ([#890](https://github.com/taskforcesh/bullmq/issues/890)) ([f80b19a](https://github.com/taskforcesh/bullmq/commit/f80b19a5aa85413b8906aa0fac1bfd09bec990cb))

### [1.54.3](https://github.com/taskforcesh/bullmq/compare/v1.54.2...v1.54.3) (2021-11-22)

#### Bug Fixes

* **clean:** use range values in lua script ([#885](https://github.com/taskforcesh/bullmq/issues/885)) ([02ef63a](https://github.com/taskforcesh/bullmq/commit/02ef63a8163e627a270a1c1bd74989a67c3f15f7))

### [1.54.2](https://github.com/taskforcesh/bullmq/compare/v1.54.1...v1.54.2) (2021-11-20)

#### Bug Fixes

* **job:** use this when use new operators ([#884](https://github.com/taskforcesh/bullmq/issues/884)) ([7b84283](https://github.com/taskforcesh/bullmq/commit/7b842839e1d30967ebf15b901033e3b31e929df8))

### [1.54.1](https://github.com/taskforcesh/bullmq/compare/v1.54.0...v1.54.1) (2021-11-19)

#### Bug Fixes

* **job:** change private attributes to protected for extensions ([#882](https://github.com/taskforcesh/bullmq/issues/882)) ([ffcc3f0](https://github.com/taskforcesh/bullmq/commit/ffcc3f083c23e6de3587c38fb7aacb2e19085351))

## [1.54.0](https://github.com/taskforcesh/bullmq/compare/v1.53.0...v1.54.0) (2021-11-17)

#### Features

* **load-includes:** export includes to be reused in extensions ([#877](https://github.com/taskforcesh/bullmq/issues/877)) ([b56c4a9](https://github.com/taskforcesh/bullmq/commit/b56c4a9cf2ecebb44481618026589162be61680a))

## [1.53.0](https://github.com/taskforcesh/bullmq/compare/v1.52.2...v1.53.0) (2021-11-16)

#### Features

* **queue-events:** add cleaned event ([#865](https://github.com/taskforcesh/bullmq/issues/865)) ([b3aebad](https://github.com/taskforcesh/bullmq/commit/b3aebad8a62311e135d53be2e7c5e47740547465))

### [1.52.2](https://github.com/taskforcesh/bullmq/compare/v1.52.1...v1.52.2) (2021-11-14)

#### Bug Fixes

* **worker:** change private attributes to protected for pro extension ([#874](https://github.com/taskforcesh/bullmq/issues/874)) ([1c73881](https://github.com/taskforcesh/bullmq/commit/1c738819b49f206688ed7b3b9d103077045e1b05))

### [1.52.1](https://github.com/taskforcesh/bullmq/compare/v1.52.0...v1.52.1) (2021-11-12)

#### Performance Improvements

* **clean:** speed up clean method when called with limit param ([#864](https://github.com/taskforcesh/bullmq/issues/864)) ([09b5cb4](https://github.com/taskforcesh/bullmq/commit/09b5cb45a79c4bc53a52d540918c22477a066e16))

## [1.52.0](https://github.com/taskforcesh/bullmq/compare/v1.51.3...v1.52.0) (2021-11-11)

#### Features

* **queue:** add waiting event type declaration ([#872](https://github.com/taskforcesh/bullmq/issues/872)) ([f29925d](https://github.com/taskforcesh/bullmq/commit/f29925da3b12f573582ea188ec386e86023cefc9))

### [1.51.3](https://github.com/taskforcesh/bullmq/compare/v1.51.2...v1.51.3) (2021-11-04)

#### Bug Fixes

* **move-to-failed:** delete closing check that prevents script execution ([#858](https://github.com/taskforcesh/bullmq/issues/858)) fixes [#834](https://github.com/taskforcesh/bullmq/issues/834) ([d50814f](https://github.com/taskforcesh/bullmq/commit/d50814f864448c10fec8e93651a2095fa4ef3f4e))

### [1.51.2](https://github.com/taskforcesh/bullmq/compare/v1.51.1...v1.51.2) (2021-11-03)

#### Bug Fixes

* **flow:** remove repeat option from FlowJob opts ([#853](https://github.com/taskforcesh/bullmq/issues/853)) fixes [#851](https://github.com/taskforcesh/bullmq/issues/851) ([c9ee2f1](https://github.com/taskforcesh/bullmq/commit/c9ee2f100a23aa24034598b7d452c69720d7aabd))

### [1.51.1](https://github.com/taskforcesh/bullmq/compare/v1.51.0...v1.51.1) (2021-10-29)

#### Bug Fixes

* **commands:** copy includes lua scripts ([#843](https://github.com/taskforcesh/bullmq/issues/843)) fixes [#837](https://github.com/taskforcesh/bullmq/issues/837) ([cab33e0](https://github.com/taskforcesh/bullmq/commit/cab33e08bc78bd3c45b86158a818100beeb06d81))

## [1.51.0](https://github.com/taskforcesh/bullmq/compare/v1.50.7...v1.51.0) (2021-10-28)

#### Features

* **flow:** consider continually adding jobs ([#828](https://github.com/taskforcesh/bullmq/issues/828)) fixes [#826](https://github.com/taskforcesh/bullmq/issues/826) ([b0fde69](https://github.com/taskforcesh/bullmq/commit/b0fde69f4370160a891e4654485c09745066b80b))

### [1.50.7](https://github.com/taskforcesh/bullmq/compare/v1.50.6...v1.50.7) (2021-10-28)

#### Bug Fixes

* override enableReadyCheck, maxRetriesPerRequest fixes reconnection ([09ba358](https://github.com/taskforcesh/bullmq/commit/09ba358b6f761bdc52b0f5b2aa315cc6c2a9db6e))
* **queue-base:** deprecation warning on missing connection ([2f79802](https://github.com/taskforcesh/bullmq/commit/2f79802378d7e015b5d0702945a71c1c2073251e))

### [1.50.6](https://github.com/taskforcesh/bullmq/compare/v1.50.5...v1.50.6) (2021-10-28)

#### Bug Fixes

* **queue-base:** show connection deprecation warning ([#832](https://github.com/taskforcesh/bullmq/issues/832)) fixes [#829](https://github.com/taskforcesh/bullmq/issues/829) ([5d023fe](https://github.com/taskforcesh/bullmq/commit/5d023fe7b671a2547398fd68995ccd85216cc7a5))

### [1.50.5](https://github.com/taskforcesh/bullmq/compare/v1.50.4...v1.50.5) (2021-10-21)

#### Bug Fixes

* **child-pool:** pipe process stdout and stderr([#822](https://github.com/taskforcesh/bullmq/issues/822)) fixes [#821](https://github.com/taskforcesh/bullmq/issues/821) ([13f5c62](https://github.com/taskforcesh/bullmq/commit/13f5c62174925e4638acda6a9de379668048189d))

### [1.50.4](https://github.com/taskforcesh/bullmq/compare/v1.50.3...v1.50.4) (2021-10-20)

#### Bug Fixes

* properly pass sharedConnection option to worker base class ([56557f1](https://github.com/taskforcesh/bullmq/commit/56557f1c0c3fb04bc3dd8824819c2d4367324c3b))

### [1.50.3](https://github.com/taskforcesh/bullmq/compare/v1.50.2...v1.50.3) (2021-10-18)

#### Bug Fixes

* **msgpackr:** upgrade version to 1.4.6 to support esm bundlers ([#818](https://github.com/taskforcesh/bullmq/issues/818)) fixes [#813](https://github.com/taskforcesh/bullmq/issues/813) ([913d7a9](https://github.com/taskforcesh/bullmq/commit/913d7a9a892d2c7e2fa5822367355c2dee888583))

### [1.50.2](https://github.com/taskforcesh/bullmq/compare/v1.50.1...v1.50.2) (2021-10-12)

#### Bug Fixes

* **msgpack:** replace msgpack by msgpackr ([dc13a75](https://github.com/taskforcesh/bullmq/commit/dc13a75374bbd29fefbf3e56f822e763df3712d9))

### [1.50.1](https://github.com/taskforcesh/bullmq/compare/v1.50.0...v1.50.1) (2021-10-12)

#### Bug Fixes

* **queue-getters:** only getting the first 2 jobs ([653873a](https://github.com/taskforcesh/bullmq/commit/653873a6a86dd6c3e1afc3142efbe11014d80557))

## [1.50.0](https://github.com/taskforcesh/bullmq/compare/v1.49.0...v1.50.0) (2021-10-12)

#### Features

* easier to build extensions on top of BullMQ ([b1a9e64](https://github.com/taskforcesh/bullmq/commit/b1a9e64a9184addc0b8245a04013e1c896e9c2bc))

## [1.49.0](https://github.com/taskforcesh/bullmq/compare/v1.48.3...v1.49.0) (2021-10-08)

#### Features

* **sandboxed-process:** handle init-failed error ([#797](https://github.com/taskforcesh/bullmq/issues/797)) ([5d2f553](https://github.com/taskforcesh/bullmq/commit/5d2f55342b19ee99d34f8d8003f09359cfe17d4f))

### [1.48.3](https://github.com/taskforcesh/bullmq/compare/v1.48.2...v1.48.3) (2021-10-05)

#### Bug Fixes

* **change-delay:** add current time to delay ([#789](https://github.com/taskforcesh/bullmq/issues/789)) fixes [#787](https://github.com/taskforcesh/bullmq/issues/787) ([4a70def](https://github.com/taskforcesh/bullmq/commit/4a70def6e85cf9ea384ec5f38c3c4f83e4eb523c))

### [1.48.2](https://github.com/taskforcesh/bullmq/compare/v1.48.1...v1.48.2) (2021-09-24)

#### Performance Improvements

* **obliterate:** do not pass unused variables ([#766](https://github.com/taskforcesh/bullmq/issues/766)) ([e9abfa6](https://github.com/taskforcesh/bullmq/commit/e9abfa6f821064901770a9b72adfb00cac96154c))

### [1.48.1](https://github.com/taskforcesh/bullmq/compare/v1.48.0...v1.48.1) (2021-09-23)

#### Bug Fixes

* **obliterate:** consider dependencies and processed keys ([#765](https://github.com/taskforcesh/bullmq/issues/765)) ([fd6bad8](https://github.com/taskforcesh/bullmq/commit/fd6bad8c7444c21e6f1d67611a28f8e4aace293d))

## [1.48.0](https://github.com/taskforcesh/bullmq/compare/v1.47.2...v1.48.0) (2021-09-23)

#### Features

* **queue:** add drain lua script ([#764](https://github.com/taskforcesh/bullmq/issues/764)) ([2daa698](https://github.com/taskforcesh/bullmq/commit/2daa698a7cc5dc8a6cd087b2d29356bc02fb4944))

### [1.47.2](https://github.com/taskforcesh/bullmq/compare/v1.47.1...v1.47.2) (2021-09-22)

#### Bug Fixes

* **flow-producer:** use default prefix in add method ([#763](https://github.com/taskforcesh/bullmq/issues/763)) fixes [#762](https://github.com/taskforcesh/bullmq/issues/762) ([fffdb55](https://github.com/taskforcesh/bullmq/commit/fffdb55f37917776494a4471673ef4564e0faab5))

### [1.47.1](https://github.com/taskforcesh/bullmq/compare/v1.47.0...v1.47.1) (2021-09-17)

#### Bug Fixes

* **running:** move running attribute before first async call ([#756](https://github.com/taskforcesh/bullmq/issues/756)) ([f7f0660](https://github.com/taskforcesh/bullmq/commit/f7f066076bbe6cbcbf716ae622d55c6c1ae9b270))

## [1.47.0](https://github.com/taskforcesh/bullmq/compare/v1.46.7...v1.47.0) (2021-09-16)

#### Features

* **queue-events:** launch without launching process ([#750](https://github.com/taskforcesh/bullmq/issues/750)) ([23a2360](https://github.com/taskforcesh/bullmq/commit/23a23606e727ca13b24924a1e867c6b557d6a09d))

### [1.46.7](https://github.com/taskforcesh/bullmq/compare/v1.46.6...v1.46.7) (2021-09-16)

#### Bug Fixes

* **wait-for-job:** add catch block and emit error ([#749](https://github.com/taskforcesh/bullmq/issues/749)) ([b407f9a](https://github.com/taskforcesh/bullmq/commit/b407f9ac429c825984856eebca58bbfd16feb9d3))

### [1.46.6](https://github.com/taskforcesh/bullmq/compare/v1.46.5...v1.46.6) (2021-09-15)

#### Bug Fixes

* **connection:** fail only if redis connection does not recover ([#751](https://github.com/taskforcesh/bullmq/issues/751)) ([8d59ced](https://github.com/taskforcesh/bullmq/commit/8d59ced27831a636f40ed4233eba3d4ac0654534))

### [1.46.5](https://github.com/taskforcesh/bullmq/compare/v1.46.4...v1.46.5) (2021-09-12)

#### Bug Fixes

* **is-finished:** reject when missing job key ([#746](https://github.com/taskforcesh/bullmq/issues/746)) fixes [#85](https://github.com/taskforcesh/bullmq/issues/85) ([bd49bd2](https://github.com/taskforcesh/bullmq/commit/bd49bd20492676559072e5e16adb6d4e47afb22b))

### [1.46.4](https://github.com/taskforcesh/bullmq/compare/v1.46.3...v1.46.4) (2021-09-10)

#### Bug Fixes

* **wait-until-finished:** isFinished return failedReason or returnValue ([#743](https://github.com/taskforcesh/bullmq/issues/743)) fixes [#555](https://github.com/taskforcesh/bullmq/issues/555) ([63acae9](https://github.com/taskforcesh/bullmq/commit/63acae98cb083ec978ea17833819d1a21086be33))

### [1.46.3](https://github.com/taskforcesh/bullmq/compare/v1.46.2...v1.46.3) (2021-09-08)

#### Bug Fixes

* **add-job:** throw error when missing parent key ([#739](https://github.com/taskforcesh/bullmq/issues/739)) ([d751070](https://github.com/taskforcesh/bullmq/commit/d751070f4ab6553c782341270574ccd253d309b8))

### [1.46.2](https://github.com/taskforcesh/bullmq/compare/v1.46.1...v1.46.2) (2021-09-07)

#### Bug Fixes

* **queue-events:** duplicate connection ([#733](https://github.com/taskforcesh/bullmq/issues/733)) fixes [#726](https://github.com/taskforcesh/bullmq/issues/726) ([e2531ed](https://github.com/taskforcesh/bullmq/commit/e2531ed0c1dc195f210f8cf996e9ffe04c9e4b7d))

### [1.46.1](https://github.com/taskforcesh/bullmq/compare/v1.46.0...v1.46.1) (2021-09-06)

#### Bug Fixes

* **redis-connection:** improve closing fixes [#721](https://github.com/taskforcesh/bullmq/issues/721) ([9d8eb03](https://github.com/taskforcesh/bullmq/commit/9d8eb0306ef5e63c9d34ffd5c96fc15491da639d))

## [1.46.0](https://github.com/taskforcesh/bullmq/compare/v1.45.0...v1.46.0) (2021-09-02)

#### Features

* **worker:** launch without launching process ([#724](https://github.com/taskforcesh/bullmq/issues/724)) ([af689e4](https://github.com/taskforcesh/bullmq/commit/af689e4e3945b9bc68bfc08c8f0ad57644206c5b)), closes [#436](https://github.com/taskforcesh/bullmq/issues/436)

## [1.45.0](https://github.com/taskforcesh/bullmq/compare/v1.44.3...v1.45.0) (2021-09-02)

#### Features

* **queue-scheduler:** launch without launching process ([#729](https://github.com/taskforcesh/bullmq/issues/729)) ([f1932a7](https://github.com/taskforcesh/bullmq/commit/f1932a789af13da9b705a72d6f633f984a218862)), closes [#436](https://github.com/taskforcesh/bullmq/issues/436)

### [1.44.3](https://github.com/taskforcesh/bullmq/compare/v1.44.2...v1.44.3) (2021-09-02)

#### Bug Fixes

* **queuescheduler:** handle shared connections fixes [#721](https://github.com/taskforcesh/bullmq/issues/721) ([32a2b2e](https://github.com/taskforcesh/bullmq/commit/32a2b2eccfa3ba1516eacd71e334cae6c787ce4c))

### [1.44.2](https://github.com/taskforcesh/bullmq/compare/v1.44.1...v1.44.2) (2021-08-29)

#### Bug Fixes

* **worker:** use spread operator in processing map keys ([#720](https://github.com/taskforcesh/bullmq/issues/720)) ([32f1e57](https://github.com/taskforcesh/bullmq/commit/32f1e570a9a3369174a228f729f1d1330dcb6965))

### [1.44.1](https://github.com/taskforcesh/bullmq/compare/v1.44.0...v1.44.1) (2021-08-29)

#### Bug Fixes

* **retry:** throw error when retry non failed job ([#717](https://github.com/taskforcesh/bullmq/issues/717)) ([bb9b192](https://github.com/taskforcesh/bullmq/commit/bb9b192e9a1a4f3c25374fcb8c0fb2159eb3f779))

## [1.44.0](https://github.com/taskforcesh/bullmq/compare/v1.43.0...v1.44.0) (2021-08-27)

#### Features

* **queue-events:** add waiting-children event ([#704](https://github.com/taskforcesh/bullmq/issues/704)) ([18b0b79](https://github.com/taskforcesh/bullmq/commit/18b0b7954313274a61fcc058380bfb9d682c059d))

## [1.43.0](https://github.com/taskforcesh/bullmq/compare/v1.42.1...v1.43.0) (2021-08-25)

#### Features

* **events:** add added event when job is created ([#699](https://github.com/taskforcesh/bullmq/issues/699)) ([f533cc5](https://github.com/taskforcesh/bullmq/commit/f533cc55a43cf6ea78a60e85102f15b1c1ff69a0))

### [1.42.1](https://github.com/taskforcesh/bullmq/compare/v1.42.0...v1.42.1) (2021-08-23)

#### Bug Fixes

* protect emit calls with throw/catch ([79f879b](https://github.com/taskforcesh/bullmq/commit/79f879bf1bca1acea19485def361cc36f1d13b7e))

## [1.42.0](https://github.com/taskforcesh/bullmq/compare/v1.41.0...v1.42.0) (2021-08-20)

#### Features

* **flows:** add queuesOptions for rate limit ([#692](https://github.com/taskforcesh/bullmq/issues/692)) ([6689ec3](https://github.com/taskforcesh/bullmq/commit/6689ec3fadd21904d9935f932c047f540ed8caf0)), closes [#621](https://github.com/taskforcesh/bullmq/issues/621)

## [1.41.0](https://github.com/taskforcesh/bullmq/compare/v1.40.4...v1.41.0) (2021-08-20)

#### Features

* **flow:** add bulk ([dc59fe6](https://github.com/taskforcesh/bullmq/commit/dc59fe62e57b6e761fe4d2ab6179a69dc4792399))

### [1.40.4](https://github.com/taskforcesh/bullmq/compare/v1.40.3...v1.40.4) (2021-08-06)

#### Bug Fixes

* **rate-limiter:** check groupKey is not undefined ([999b918](https://github.com/taskforcesh/bullmq/commit/999b91868814caf4c5c1ddee40798178b71e0ea8))

### [1.40.3](https://github.com/taskforcesh/bullmq/compare/v1.40.2...v1.40.3) (2021-08-06)

#### Bug Fixes

* **redis-connection:** add error event in waitUntilReady ([ac4101e](https://github.com/taskforcesh/bullmq/commit/ac4101e3e798110c022d6c9f10f3b98f5e86b151))

### [1.40.2](https://github.com/taskforcesh/bullmq/compare/v1.40.1...v1.40.2) (2021-08-06)

#### Bug Fixes

* move clientCommandMessageReg to utils ([dd5d555](https://github.com/taskforcesh/bullmq/commit/dd5d5553fe768eb18b17b53c7f75e7066024e382))

### [1.40.1](https://github.com/taskforcesh/bullmq/compare/v1.40.0...v1.40.1) (2021-07-24)

#### Bug Fixes

* connection hangs with failed connection fixes [#656](https://github.com/taskforcesh/bullmq/issues/656) ([c465611](https://github.com/taskforcesh/bullmq/commit/c465611ed76afd2adfd0e05a8babd6e369f5c310))

## [1.40.0](https://github.com/taskforcesh/bullmq/compare/v1.39.5...v1.40.0) (2021-07-22)

#### Features

* **worker:** retry with delay errors in run loop ([409fe7f](https://github.com/taskforcesh/bullmq/commit/409fe7fc09b87b7916a3362a463bb9e0f17ecea8))

### [1.39.5](https://github.com/taskforcesh/bullmq/compare/v1.39.4...v1.39.5) (2021-07-21)

#### Bug Fixes

* **move-to-finished:** remove stalled jobs when finishing ([3867126](https://github.com/taskforcesh/bullmq/commit/38671261ccc00ca7fefa677663e45a40a92df555))

### [1.39.4](https://github.com/taskforcesh/bullmq/compare/v1.39.3...v1.39.4) (2021-07-21)

#### Bug Fixes

* **repeatable:** validate endDate when adding next repeatable job ([1324cbb](https://github.com/taskforcesh/bullmq/commit/1324cbb4effd55e98c29d95a21afca7cd045b46c))

### [1.39.3](https://github.com/taskforcesh/bullmq/compare/v1.39.2...v1.39.3) (2021-07-16)

#### Bug Fixes

* connect if redis client has status "wait" ([f711717](https://github.com/taskforcesh/bullmq/commit/f711717f56822aef43c9fd0440e30fad0876ba62))

### [1.39.2](https://github.com/taskforcesh/bullmq/compare/v1.39.1...v1.39.2) (2021-07-15)

#### Bug Fixes

* **queue:** ensure the Queue constructor doesn't try to set queue options if the client is closed ([b40c6eb](https://github.com/taskforcesh/bullmq/commit/b40c6eb931a71d0ae9f6454eb70d84259a6981b7))

### [1.39.1](https://github.com/taskforcesh/bullmq/compare/v1.39.0...v1.39.1) (2021-07-15)

#### Bug Fixes

* **sandbox:** use updateProgress method name ([27d62c3](https://github.com/taskforcesh/bullmq/commit/27d62c32b2fac091b2700d6077de593c9fda4c22))

## [1.39.0](https://github.com/taskforcesh/bullmq/compare/v1.38.1...v1.39.0) (2021-07-13)

#### Features

* **worker+scheduler:** add a "running" attribute for healthchecking ([aae358e](https://github.com/taskforcesh/bullmq/commit/aae358e067a0b6f20124751cffcdeaebac6eb7fd))

### [1.38.1](https://github.com/taskforcesh/bullmq/compare/v1.38.0...v1.38.1) (2021-07-12)

#### Bug Fixes

* **reprocess:** do not store job.id in added list ([9c0605e](https://github.com/taskforcesh/bullmq/commit/9c0605e10f0bbdce94153d3f318d56c23bfd3269))

## [1.38.0](https://github.com/taskforcesh/bullmq/compare/v1.37.1...v1.38.0) (2021-07-12)

#### Features

* **queue:** add missing events typings ([b42e78c](https://github.com/taskforcesh/bullmq/commit/b42e78c36cb6a6579a4c7cce1d7e969b230ff5b6))

### [1.37.1](https://github.com/taskforcesh/bullmq/compare/v1.37.0...v1.37.1) (2021-07-02)

#### Bug Fixes

* **stalled-jobs:** move stalled jobs to wait in batches ([a23fcb8](https://github.com/taskforcesh/bullmq/commit/a23fcb82d4ca20cbc4b8cd8b544b2d2eaddd86c3)), closes [#422](https://github.com/taskforcesh/bullmq/issues/422)

## [1.37.0](https://github.com/taskforcesh/bullmq/compare/v1.36.1...v1.37.0) (2021-06-30)

#### Features

* **job:** add changeDelay method for delayed jobs ([f0a9f9c](https://github.com/taskforcesh/bullmq/commit/f0a9f9c6479062413abc0ac9a6f744329571a618))

### [1.36.1](https://github.com/taskforcesh/bullmq/compare/v1.36.0...v1.36.1) (2021-06-22)

#### Bug Fixes

* **worker:** change active event typing ([220b4f6](https://github.com/taskforcesh/bullmq/commit/220b4f619b30a8f04979e9abd0139e46d89b424d))

## [1.36.0](https://github.com/taskforcesh/bullmq/compare/v1.35.0...v1.36.0) (2021-06-20)

#### Bug Fixes

* **queue-events:** fix drained typing ([9cf711d](https://github.com/taskforcesh/bullmq/commit/9cf711d4d4e7d8214dfd93a243c35d0bf135cdaf))

#### Features

* **worker:** add active event typing ([5508cdf](https://github.com/taskforcesh/bullmq/commit/5508cdf7cf372ae2f4af0ef576016eb901580671))
* **worker:** add progress event typing ([119cb7c](https://github.com/taskforcesh/bullmq/commit/119cb7cd7a91c0f1866f5957faf2850afadbe709))

## [1.35.0](https://github.com/taskforcesh/bullmq/compare/v1.34.2...v1.35.0) (2021-06-19)

#### Features

* **worker:** add drained event typing ([ed5f315](https://github.com/taskforcesh/bullmq/commit/ed5f3155415693d2a6dbfb779397d53d74b704e2))

### [1.34.2](https://github.com/taskforcesh/bullmq/compare/v1.34.1...v1.34.2) (2021-06-18)

#### Bug Fixes

* **worker:** await for processing functions ([0566804](https://github.com/taskforcesh/bullmq/commit/056680470283f134b447a8ba39afa29e1e113585))

### [1.34.1](https://github.com/taskforcesh/bullmq/compare/v1.34.0...v1.34.1) (2021-06-18)

#### Bug Fixes

* **redis-connection:** remove error event listener from client ([2d70fe7](https://github.com/taskforcesh/bullmq/commit/2d70fe7cc7d43673674ec2ba0204c10661b34e95))

## [1.34.0](https://github.com/taskforcesh/bullmq/compare/v1.33.1...v1.34.0) (2021-06-11)

#### Features

* **job:** expose queueName ([8683bd4](https://github.com/taskforcesh/bullmq/commit/8683bd470cc7304f087d646fd40c5bc3acc1263c))

### [1.33.1](https://github.com/taskforcesh/bullmq/compare/v1.33.0...v1.33.1) (2021-06-10)

#### Bug Fixes

* **job:** destructure default opts for pagination ([73363a5](https://github.com/taskforcesh/bullmq/commit/73363a551f56608f8936ad1f730d0a9c778aafd2))

## [1.33.0](https://github.com/taskforcesh/bullmq/compare/v1.32.0...v1.33.0) (2021-06-10)

#### Features

* **job:** add getDependenciesCount method ([ae39a4c](https://github.com/taskforcesh/bullmq/commit/ae39a4c77a958242cb445dbb32ae27b15a953653))

## [1.32.0](https://github.com/taskforcesh/bullmq/compare/v1.31.1...v1.32.0) (2021-06-07)

#### Features

* **flow-producer:** add getFlow method ([ce93d04](https://github.com/taskforcesh/bullmq/commit/ce93d04c962686aff34f670f2decadadbf1cf4ca))

### [1.31.1](https://github.com/taskforcesh/bullmq/compare/v1.31.0...v1.31.1) (2021-06-07)

#### Bug Fixes

* **worker:** remove processed key when removeOnComplete ([4ec1b73](https://github.com/taskforcesh/bullmq/commit/4ec1b739d6aeeb2fc21887b58f5978027ddcdb50))

## [1.31.0](https://github.com/taskforcesh/bullmq/compare/v1.30.2...v1.31.0) (2021-06-04)

#### Features

* **job:** extend getDependencies to support pagination ([9b61bbb](https://github.com/taskforcesh/bullmq/commit/9b61bbb9160358f629cd458fa8dc4c9b6ebcd9f5))

### [1.30.2](https://github.com/taskforcesh/bullmq/compare/v1.30.1...v1.30.2) (2021-06-03)

#### Bug Fixes

* **job:** parse results in getDependencies for processed jobs ([6fdc701](https://github.com/taskforcesh/bullmq/commit/6fdc7011ba910e5ca9c6d87926cc523ef38ef3ca))

### [1.30.1](https://github.com/taskforcesh/bullmq/compare/v1.30.0...v1.30.1) (2021-06-02)

#### Bug Fixes

* **move-to-waiting-children:** make opts optional ([33bd76a](https://github.com/taskforcesh/bullmq/commit/33bd76a2cac9be450b5d76c6cfe16751c7569ceb))

## [1.30.0](https://github.com/taskforcesh/bullmq/compare/v1.29.1...v1.30.0) (2021-06-02)

#### Features

* add some event typing ([934c004](https://github.com/taskforcesh/bullmq/commit/934c0040b0802bb67f44a979584405d795a8ab5e))

### [1.29.1](https://github.com/taskforcesh/bullmq/compare/v1.29.0...v1.29.1) (2021-05-31)

#### Bug Fixes

* **move-stalled-jobs-to-wait:** send failedReason to queueEvents ([7c510b5](https://github.com/taskforcesh/bullmq/commit/7c510b542558bd4b1330371b73331f37b97a818d))

## [1.29.0](https://github.com/taskforcesh/bullmq/compare/v1.28.2...v1.29.0) (2021-05-31)

#### Features

* add move to waiting children for manual processing ([#477](https://github.com/taskforcesh/bullmq/issues/477)) ([f312f29](https://github.com/taskforcesh/bullmq/commit/f312f293b8cac79af9c14848ffd1b11b65a806c3))

### [1.28.2](https://github.com/taskforcesh/bullmq/compare/v1.28.1...v1.28.2) (2021-05-31)

#### Bug Fixes

* **obliterate:** remove job logs ([ea91895](https://github.com/taskforcesh/bullmq/commit/ea918950d7696241047a23773cc13cd675209c4b))

### [1.28.1](https://github.com/taskforcesh/bullmq/compare/v1.28.0...v1.28.1) (2021-05-31)

#### Bug Fixes

* **get-workers:** use strict equality on name fixes [#564](https://github.com/taskforcesh/bullmq/issues/564) ([4becfa6](https://github.com/taskforcesh/bullmq/commit/4becfa66e09dacf9830804898c45cb3317dcf438))

## [1.28.0](https://github.com/taskforcesh/bullmq/compare/v1.27.0...v1.28.0) (2021-05-24)

#### Features

* **flow-producer:** expose client connection ([17d4263](https://github.com/taskforcesh/bullmq/commit/17d4263abfa57797535cd8773c4cc316ff5149d2))

## [1.27.0](https://github.com/taskforcesh/bullmq/compare/v1.26.5...v1.27.0) (2021-05-24)

#### Features

* **repeat:** add immediately opt for repeat ([d095573](https://github.com/taskforcesh/bullmq/commit/d095573f8e7ce5911f777df48368382eceb99d6a))

### [1.26.5](https://github.com/taskforcesh/bullmq/compare/v1.26.4...v1.26.5) (2021-05-21)

#### Bug Fixes

* **movetofinished:** use parent queue for events ([1b17b62](https://github.com/taskforcesh/bullmq/commit/1b17b62a794728a318f1079e73d07e33fe65c9c7))

### [1.26.4](https://github.com/taskforcesh/bullmq/compare/v1.26.3...v1.26.4) (2021-05-20)

#### Bug Fixes

* **removejob:** delete processed hash ([a2a5058](https://github.com/taskforcesh/bullmq/commit/a2a5058f18ab77ed4d0114d48f47e6144d632cbf))

### [1.26.3](https://github.com/taskforcesh/bullmq/compare/v1.26.2...v1.26.3) (2021-05-19)

#### Bug Fixes

* ensure connection reconnects when pausing fixes [#160](https://github.com/taskforcesh/bullmq/issues/160) ([f38fee8](https://github.com/taskforcesh/bullmq/commit/f38fee84def75dd8a38cbb8bfb5aa662485ddf91))

### [1.26.2](https://github.com/taskforcesh/bullmq/compare/v1.26.1...v1.26.2) (2021-05-18)

#### Bug Fixes

* **getjoblogs:** no reversed pagination ([fb0c3a5](https://github.com/taskforcesh/bullmq/commit/fb0c3a50f0d37851a8f35cb4c478259a63d93461))

### [1.26.1](https://github.com/taskforcesh/bullmq/compare/v1.26.0...v1.26.1) (2021-05-17)

#### Bug Fixes

* **flow-producer:** use custom jobId as parentId for children fixes [#552](https://github.com/taskforcesh/bullmq/issues/552) ([645b576](https://github.com/taskforcesh/bullmq/commit/645b576c1aabd8426ab77a68c199a594867cd729))

## [1.26.0](https://github.com/taskforcesh/bullmq/compare/v1.25.1...v1.26.0) (2021-05-16)

#### Features

* **custombackoff:** provide job as third parameter ([ddaf8dc](https://github.com/taskforcesh/bullmq/commit/ddaf8dc2f95ca336cb117a540edd4640d5d579e4))

### [1.25.2](https://github.com/taskforcesh/bullmq/compare/v1.25.1...v1.25.2) (2021-05-16)

#### Bug Fixes

* **flow-producer:** process parent with children as empty array fixes [#547](https://github.com/taskforcesh/bullmq/issues/547) ([48168f0](https://github.com/taskforcesh/bullmq/commit/48168f07cbaed7ed522c68d127a0c7d5e4cb380e))

### [1.25.1](https://github.com/taskforcesh/bullmq/compare/v1.25.0...v1.25.1) (2021-05-13)

#### Bug Fixes

* **addbulk:** should not consider repeat option ([c85357e](https://github.com/taskforcesh/bullmq/commit/c85357e415b9ea66f845f751a4943b5c48c2bb18))

## [1.25.0](https://github.com/taskforcesh/bullmq/compare/v1.24.5...v1.25.0) (2021-05-11)

#### Features

* **job:** add sizeLimit option when creating a job ([f10aeeb](https://github.com/taskforcesh/bullmq/commit/f10aeeb62520d20b31d35440524d147ac4adcc9c))

### [1.24.5](https://github.com/taskforcesh/bullmq/compare/v1.24.4...v1.24.5) (2021-05-08)

#### Bug Fixes

* **deps:** upgrading lodash to 4.17.21 ([6e90c3f](https://github.com/taskforcesh/bullmq/commit/6e90c3f0a3d2735875ebf44457b342629aa14572))

### [1.24.4](https://github.com/taskforcesh/bullmq/compare/v1.24.3...v1.24.4) (2021-05-07)

#### Bug Fixes

* **cluster:** add redis cluster support ([5a7dd14](https://github.com/taskforcesh/bullmq/commit/5a7dd145bd3ae11850cac6d1b4fb9b01af0e6766))
* **redisclient:** not reference types from import ([022fc04](https://github.com/taskforcesh/bullmq/commit/022fc042a17c1754af7d74acabb7dd5c397576ab))

### [1.24.3](https://github.com/taskforcesh/bullmq/compare/v1.24.2...v1.24.3) (2021-05-05)

#### Bug Fixes

* **sandbox:** properly redirect stdout ([#525](https://github.com/taskforcesh/bullmq/issues/525)) ([c8642a0](https://github.com/taskforcesh/bullmq/commit/c8642a0724dc3d2f77abc4b5d6d24efa67c1e592))

### [1.24.2](https://github.com/taskforcesh/bullmq/compare/v1.24.1...v1.24.2) (2021-05-05)

#### Bug Fixes

* **sandbox:** handle broken processor files ([2326983](https://github.com/taskforcesh/bullmq/commit/23269839af0be2f7cf2a4f6062563d30904bc259))

### [1.24.1](https://github.com/taskforcesh/bullmq/compare/v1.24.0...v1.24.1) (2021-05-05)

#### Bug Fixes

* **queueevents:** add active type fixes [#519](https://github.com/taskforcesh/bullmq/issues/519) ([10af883](https://github.com/taskforcesh/bullmq/commit/10af883db849cf9392b26724903f88752d9be92c))

## [1.24.0](https://github.com/taskforcesh/bullmq/compare/v1.23.1...v1.24.0) (2021-05-03)

#### Features

* add option for non-blocking getNextJob ([13ce2cf](https://github.com/taskforcesh/bullmq/commit/13ce2cfd4ccd64f45567df31de11af95b0fe67d9))

### [1.23.1](https://github.com/taskforcesh/bullmq/compare/v1.23.0...v1.23.1) (2021-05-03)

#### Bug Fixes

* add return type for job.waitUntilFinished() ([59ede97](https://github.com/taskforcesh/bullmq/commit/59ede976061a738503f70d9eb0c92a4b1d6ae4a3))

## [1.23.0](https://github.com/taskforcesh/bullmq/compare/v1.22.2...v1.23.0) (2021-04-30)

#### Features

* **job:** pass parent opts to addBulk ([7f21615](https://github.com/taskforcesh/bullmq/commit/7f216153293e45c4f33f2592561c925ca4464d44))

### [1.22.2](https://github.com/taskforcesh/bullmq/compare/v1.22.1...v1.22.2) (2021-04-29)

#### Bug Fixes

* add missing Redis Cluster types fixes [#406](https://github.com/taskforcesh/bullmq/issues/406) ([07743ff](https://github.com/taskforcesh/bullmq/commit/07743ff310ad716802afdd5bdc6844eb5296318e))

### [1.22.1](https://github.com/taskforcesh/bullmq/compare/v1.22.0...v1.22.1) (2021-04-28)

#### Bug Fixes

* **addjob:** fix redis cluster CROSSSLOT ([a5fd1d7](https://github.com/taskforcesh/bullmq/commit/a5fd1d7a0713585d11bd862bfe2d426d5242bd3c))

## [1.22.0](https://github.com/taskforcesh/bullmq/compare/v1.21.0...v1.22.0) (2021-04-28)

#### Features

* **jobcreate:** allow passing parent in job.create ([ede3626](https://github.com/taskforcesh/bullmq/commit/ede3626b65fb5d3f4cebc55c813e9fa4b482b887))

## [1.21.0](https://github.com/taskforcesh/bullmq/compare/v1.20.6...v1.21.0) (2021-04-26)

#### Features

* add typing for addNextRepeatableJob ([a3be937](https://github.com/taskforcesh/bullmq/commit/a3be9379e29ae3e01264e2269e8b03aa614fd42c))

### [1.20.6](https://github.com/taskforcesh/bullmq/compare/v1.20.5...v1.20.6) (2021-04-25)

#### Bug Fixes

* **movetocompleted:** should not complete before children ([812ff66](https://github.com/taskforcesh/bullmq/commit/812ff664b3e162dd87831ca04ebfdb783cc7ae5b))

### [1.20.5](https://github.com/taskforcesh/bullmq/compare/v1.20.4...v1.20.5) (2021-04-23)

#### Bug Fixes

* **obliterate:** correctly remove many jobs ([b5ae4ce](https://github.com/taskforcesh/bullmq/commit/b5ae4ce92aeaf000408ffbbcd22d829cee20f2f8))

### [1.20.4](https://github.com/taskforcesh/bullmq/compare/v1.20.3...v1.20.4) (2021-04-23)

#### Bug Fixes

* remove internal deps on barrel fixes [#469](https://github.com/taskforcesh/bullmq/issues/469) ([#495](https://github.com/taskforcesh/bullmq/issues/495)) ([60dbeed](https://github.com/taskforcesh/bullmq/commit/60dbeed7ff1d9b6cb0e35590713fee8a7be09477))

### [1.20.3](https://github.com/taskforcesh/bullmq/compare/v1.20.2...v1.20.3) (2021-04-23)

#### Bug Fixes

* **flows:** correct typings fixes [#492](https://github.com/taskforcesh/bullmq/issues/492) ([a77f80b](https://github.com/taskforcesh/bullmq/commit/a77f80bc07e7627f512323f0dcc9141fe408809e))

### [1.20.2](https://github.com/taskforcesh/bullmq/compare/v1.20.1...v1.20.2) (2021-04-22)

#### Bug Fixes

* **movetodelayed:** check if job is in active state ([4e63f70](https://github.com/taskforcesh/bullmq/commit/4e63f70aac367d4dd695bbe07c72a08a82a65d97))

### [1.20.1](https://github.com/taskforcesh/bullmq/compare/v1.20.0...v1.20.1) (2021-04-22)

#### Bug Fixes

* **worker:** make token optional in processor function fixes [#490](https://github.com/taskforcesh/bullmq/issues/490) ([3940bd7](https://github.com/taskforcesh/bullmq/commit/3940bd71c6faf3bd5fce572b9c1f11cb5b5d2123))

## [1.20.0](https://github.com/taskforcesh/bullmq/compare/v1.19.3...v1.20.0) (2021-04-21)

#### Features

* **worker:** passing token in processor function ([2249724](https://github.com/taskforcesh/bullmq/commit/2249724b1bc6fbf40b0291400011f201fd02dab3))

### [1.19.3](https://github.com/taskforcesh/bullmq/compare/v1.19.2...v1.19.3) (2021-04-20)

#### Bug Fixes

* **movetocompleted:** throw an error if job is not in active state ([c2fe5d2](https://github.com/taskforcesh/bullmq/commit/c2fe5d292fcf8ac2e53906c30282df69d43321b1))

### [1.19.2](https://github.com/taskforcesh/bullmq/compare/v1.19.1...v1.19.2) (2021-04-19)

#### Bug Fixes

* **worker:** close base class connection [#451](https://github.com/taskforcesh/bullmq/issues/451) ([0875306](https://github.com/taskforcesh/bullmq/commit/0875306ae801a7cbfe04758dc2481cb86ca2ef69))

### [1.19.1](https://github.com/taskforcesh/bullmq/compare/v1.19.0...v1.19.1) (2021-04-19)

#### Bug Fixes

* remove repeatable with obliterate ([1c5e581](https://github.com/taskforcesh/bullmq/commit/1c5e581a619ba707863c2a6e9f3e5f6eadfbe64f))

## [1.19.0](https://github.com/taskforcesh/bullmq/compare/v1.18.2...v1.19.0) (2021-04-19)

#### Features

* add workerDelay option to limiter ([9b6ab8a](https://github.com/taskforcesh/bullmq/commit/9b6ab8ad4bc0a94068f3bc707ad9c0ed01596068))

### [1.18.2](https://github.com/taskforcesh/bullmq/compare/v1.18.1...v1.18.2) (2021-04-16)

#### Bug Fixes

* add parentKey property to Job ([febc60d](https://github.com/taskforcesh/bullmq/commit/febc60dba94c29b85be3e1bc2547fa83ed932806))

### [1.18.1](https://github.com/taskforcesh/bullmq/compare/v1.18.0...v1.18.1) (2021-04-16)

#### Bug Fixes

* rename Flow to FlowProducer class ([c64321d](https://github.com/taskforcesh/bullmq/commit/c64321d03e2af7cee88eaf6df6cd2e5b7840ae64))

## [1.18.0](https://github.com/taskforcesh/bullmq/compare/v1.17.0...v1.18.0) (2021-04-16)

#### Features

* add remove support for flows ([4e8a7ef](https://github.com/taskforcesh/bullmq/commit/4e8a7efd53f918937478ae13f5da7dee9ea9d8b3))

## [1.17.0](https://github.com/taskforcesh/bullmq/compare/v1.16.2...v1.17.0) (2021-04-16)

#### Features

* **job:** consider waiting-children state ([2916dd5](https://github.com/taskforcesh/bullmq/commit/2916dd5d7ba9438d2eae66436899d32ec8ac0e91))

### [1.16.2](https://github.com/taskforcesh/bullmq/compare/v1.16.1...v1.16.2) (2021-04-14)

#### Bug Fixes

* read lua scripts serially ([69e73b8](https://github.com/taskforcesh/bullmq/commit/69e73b87bc6855623240a7b1a45368a7914b23b7))

### [1.16.1](https://github.com/taskforcesh/bullmq/compare/v1.16.0...v1.16.1) (2021-04-12)

#### Bug Fixes

* **flow:** relative dependency path fixes [#466](https://github.com/taskforcesh/bullmq/issues/466) ([d104bf8](https://github.com/taskforcesh/bullmq/commit/d104bf802d6d1000ac1ccd781fa7a07bce2fe140))

## [1.16.0](https://github.com/taskforcesh/bullmq/compare/v1.15.1...v1.16.0) (2021-04-12)

#### Features

* add support for flows (parent-child dependencies) ([#454](https://github.com/taskforcesh/bullmq/issues/454)) ([362212c](https://github.com/taskforcesh/bullmq/commit/362212c58c4be36b5435df862503699deb8bb79c))

### [1.15.1](https://github.com/taskforcesh/bullmq/compare/v1.15.0...v1.15.1) (2021-03-19)

#### Bug Fixes

* **obliterate:** safer implementation ([82f571f](https://github.com/taskforcesh/bullmq/commit/82f571f2548c61c776b897fd1c5050bb09c8afca))

## [1.15.0](https://github.com/taskforcesh/bullmq/compare/v1.14.8...v1.15.0) (2021-03-18)

#### Features

* add method to "obliterate" a queue, fixes [#430](https://github.com/taskforcesh/bullmq/issues/430) ([624be0e](https://github.com/taskforcesh/bullmq/commit/624be0ed48159c2aa405025938925a723330e0c2))

### [1.14.8](https://github.com/taskforcesh/bullmq/compare/v1.14.7...v1.14.8) (2021-03-06)

#### Bug Fixes

* specify promise type to make TS 4.1 and 4.2 happy. ([#418](https://github.com/taskforcesh/bullmq/issues/418)) ([702f609](https://github.com/taskforcesh/bullmq/commit/702f609b410d8b0652c2d0504a8a67526966fdc3))

### [1.14.7](https://github.com/taskforcesh/bullmq/compare/v1.14.6...v1.14.7) (2021-02-16)

#### Bug Fixes

* remove "client" property of QueueBaseOptions ([#324](https://github.com/taskforcesh/bullmq/issues/324)) ([e0b9e71](https://github.com/taskforcesh/bullmq/commit/e0b9e71c4da4a93af54c4386af461c61ab5f146c))

### [1.14.6](https://github.com/taskforcesh/bullmq/compare/v1.14.5...v1.14.6) (2021-02-16)

#### Bug Fixes

* remove next job in removeRepeatableByKey fixes [#165](https://github.com/taskforcesh/bullmq/issues/165) ([fb3a7c2](https://github.com/taskforcesh/bullmq/commit/fb3a7c2f429d535dd9f038687d7230d61201defc))

### [1.14.5](https://github.com/taskforcesh/bullmq/compare/v1.14.4...v1.14.5) (2021-02-16)

#### Bug Fixes

* add jobId support to repeatable jobs fixes [#396](https://github.com/taskforcesh/bullmq/issues/396) ([c2dc669](https://github.com/taskforcesh/bullmq/commit/c2dc6693a4546e547245bc7ec1e71b4841829619))

### [1.14.4](https://github.com/taskforcesh/bullmq/compare/v1.14.3...v1.14.4) (2021-02-08)

#### Bug Fixes

* reconnect at start fixes [#337](https://github.com/taskforcesh/bullmq/issues/337) ([fb33772](https://github.com/taskforcesh/bullmq/commit/fb3377280b3bda04a15a62d2901bdd78b869e08c))

### [1.14.3](https://github.com/taskforcesh/bullmq/compare/v1.14.2...v1.14.3) (2021-02-07)

#### Bug Fixes

* **worker:** avoid possible infinite loop fixes [#389](https://github.com/taskforcesh/bullmq/issues/389) ([d05566e](https://github.com/taskforcesh/bullmq/commit/d05566ec0153f31a1257f7338399fdb55c959487))

### [1.14.2](https://github.com/taskforcesh/bullmq/compare/v1.14.1...v1.14.2) (2021-02-02)

#### Bug Fixes

* improve job timeout notification by giving the job name and id in the error message ([#387](https://github.com/taskforcesh/bullmq/issues/387)) ([ca886b1](https://github.com/taskforcesh/bullmq/commit/ca886b1f854051aed0888f5b872a64b052b2383e))

### [1.14.1](https://github.com/taskforcesh/bullmq/compare/v1.14.0...v1.14.1) (2021-02-01)

#### Bug Fixes

* job finish queue events race condition ([355bca5](https://github.com/taskforcesh/bullmq/commit/355bca5ee128bf4ff37608746f9c6f7cca580eb0))

## [1.14.0](https://github.com/taskforcesh/bullmq/compare/v1.13.0...v1.14.0) (2021-01-06)

#### Features

* **job:** expose extendLock as a public method ([17e8431](https://github.com/taskforcesh/bullmq/commit/17e8431af8bba58612bf9913c63ab5d38afecbb9))

## [1.13.0](https://github.com/taskforcesh/bullmq/compare/v1.12.3...v1.13.0) (2020-12-30)

#### Features

* add support for manually processing jobs fixes [#327](https://github.com/taskforcesh/bullmq/issues/327) ([e42bfd2](https://github.com/taskforcesh/bullmq/commit/e42bfd2814fc5136b175470c3085355090cc2e01))

### [1.12.3](https://github.com/taskforcesh/bullmq/compare/v1.12.2...v1.12.3) (2020-12-28)

#### Bug Fixes

* correctly handle "falsy" data values fixes [#264](https://github.com/taskforcesh/bullmq/issues/264) ([becad91](https://github.com/taskforcesh/bullmq/commit/becad91350fd4ac01037e5b0d4a8a93724dd8dbd))
* **worker:** setname on worker blocking connection ([645b633](https://github.com/taskforcesh/bullmq/commit/645b6338f5883b0c21ae78007777d86b45422615))

### [1.12.2](https://github.com/taskforcesh/bullmq/compare/v1.12.1...v1.12.2) (2020-12-23)

#### Bug Fixes

* catch errors from Repeat ([#348](https://github.com/taskforcesh/bullmq/issues/348)) ([09a1a98](https://github.com/taskforcesh/bullmq/commit/09a1a98fc42dc1a9ae98bfb29c0cca3fac02013f))

### [1.12.1](https://github.com/taskforcesh/bullmq/compare/v1.12.0...v1.12.1) (2020-12-21)

#### Bug Fixes

* correctly handle "falsy" data values fixes [#264](https://github.com/taskforcesh/bullmq/issues/264) ([cf1dbaf](https://github.com/taskforcesh/bullmq/commit/cf1dbaf7e60d74fc8443a5f8a537455f28a8dba3))

## [1.12.0](https://github.com/taskforcesh/bullmq/compare/v1.11.2...v1.12.0) (2020-12-16)

#### Features

* add ability to get if queue is paused or not ([e98b7d8](https://github.com/taskforcesh/bullmq/commit/e98b7d8973df830cc29e0afc5d86e82c9a7ce76f))

### [1.11.2](https://github.com/taskforcesh/bullmq/compare/v1.11.1...v1.11.2) (2020-12-15)

#### Bug Fixes

* promote jobs to the right "list" when paused ([d3df615](https://github.com/taskforcesh/bullmq/commit/d3df615d37b1114c02eacb45f23643ee2f05374d))

### [1.11.1](https://github.com/taskforcesh/bullmq/compare/v1.11.0...v1.11.1) (2020-12-15)

#### Bug Fixes

* clientCommandMessageReg to support GCP memorystore v5 ([8408dda](https://github.com/taskforcesh/bullmq/commit/8408dda9fa64fc0b968e88fb2726e0a30f717ed7))

## [1.11.0](https://github.com/taskforcesh/bullmq/compare/v1.10.0...v1.11.0) (2020-11-24)

#### Bug Fixes

* add generic type to processor ([d4f6501](https://github.com/taskforcesh/bullmq/commit/d4f650120804bd6161f0eeda5162ad5a96811a05))

#### Features

* add name and return types to queue, worker and processor ([4879715](https://github.com/taskforcesh/bullmq/commit/4879715ec7c917f11e3a0ac3c5f5126029340ed3))

## [1.10.0](https://github.com/taskforcesh/bullmq/compare/v1.9.0...v1.10.0) (2020-10-20)

#### Bug Fixes

* **job:** remove listeners before resolving promise ([563ce92](https://github.com/taskforcesh/bullmq/commit/563ce9218f5dd81f2bc836f9e8ccdedc549f09dd))
* **worker:** continue processing if handleFailed fails. fixes [#286](https://github.com/taskforcesh/bullmq/issues/286) ([4ef1cbc](https://github.com/taskforcesh/bullmq/commit/4ef1cbc13d53897b57ae3d271afbaa1b213824aa))
* **worker:** fix memory leak on Promise.race ([#282](https://github.com/taskforcesh/bullmq/issues/282)) ([a78ab2b](https://github.com/taskforcesh/bullmq/commit/a78ab2b362e54f897eec6c8b16f16ecccf7875c2))
* **worker:** setname on worker blocking connection ([#291](https://github.com/taskforcesh/bullmq/issues/291)) ([50a87fc](https://github.com/taskforcesh/bullmq/commit/50a87fcb1dab976a6a0273d2b0cc4b31b63c015f))
* remove async for loop in child pool fixes [#229](https://github.com/taskforcesh/bullmq/issues/229) ([d77505e](https://github.com/taskforcesh/bullmq/commit/d77505e989cd1395465c5222613555f79e4d9720))

#### Features

* **sandbox:** kill child workers gracefully ([#243](https://github.com/taskforcesh/bullmq/issues/243)) ([4262837](https://github.com/taskforcesh/bullmq/commit/4262837bc67e007fe44606670dce48ee7fec65cd))

## [1.9.0](https://github.com/taskforcesh/bullmq/compare/v1.8.14...v1.9.0) (2020-07-19)

#### Features

* add grouped rate limiting ([3a958dd](https://github.com/taskforcesh/bullmq/commit/3a958dd30d09a049b0d761679d3b8d92709e815e))

### [1.8.14](https://github.com/taskforcesh/bullmq/compare/v1.8.13...v1.8.14) (2020-07-03)

#### Bug Fixes

* **typescript:** fix typings, upgrade ioredis dependencies ([#220](https://github.com/taskforcesh/bullmq/issues/220)) ([7059f20](https://github.com/taskforcesh/bullmq/commit/7059f2089553a206ab3937f7fd0d0b9de96aa7b7))
* **worker:** return this.closing when calling close ([b68c845](https://github.com/taskforcesh/bullmq/commit/b68c845c77de6b2973ec31d2f22958ab60ad87aa))

### [1.8.13](https://github.com/taskforcesh/bullmq/compare/v1.8.12...v1.8.13) (2020-06-05)

#### Bug Fixes

* **redis-connection:** run the load command for reused redis client ([fab9bba](https://github.com/taskforcesh/bullmq/commit/fab9bba4caee8fd44523febb3bde588b151e8514))

### [1.8.12](https://github.com/taskforcesh/bullmq/compare/v1.8.11...v1.8.12) (2020-06-04)

#### Bug Fixes

* remove unused options ([23aadc3](https://github.com/taskforcesh/bullmq/commit/23aadc300b947693f4afb22296d236a924bd11ca))

### [1.8.11](https://github.com/taskforcesh/bullmq/compare/v1.8.10...v1.8.11) (2020-05-29)

#### Bug Fixes

* **scheduler:** remove unnecessary division by 4096 ([4d25e95](https://github.com/taskforcesh/bullmq/commit/4d25e95f9522388bd85e932e04b6668e3da57686))

### [1.8.10](https://github.com/taskforcesh/bullmq/compare/v1.8.9...v1.8.10) (2020-05-28)

#### Bug Fixes

* **scheduler:** divide timestamp by 4096 in update set fixes [#168](https://github.com/taskforcesh/bullmq/issues/168) ([0c5db83](https://github.com/taskforcesh/bullmq/commit/0c5db8391bb8994bee19f25a33efb9dfee792d7b))

### [1.8.9](https://github.com/taskforcesh/bullmq/compare/v1.8.8...v1.8.9) (2020-05-25)

#### Bug Fixes

* **scheduler:** divide next timestamp by 4096 ([#204](https://github.com/taskforcesh/bullmq/issues/204)) ([9562d74](https://github.com/taskforcesh/bullmq/commit/9562d74625e20b7b6de8750339c85345ba027357))

### [1.8.8](https://github.com/taskforcesh/bullmq/compare/v1.8.7...v1.8.8) (2020-05-25)

#### Bug Fixes

* **queue-base:** error event is passed through ([ad14e77](https://github.com/taskforcesh/bullmq/commit/ad14e777171c0c44b7e50752d9847dec23f46158))
* **redis-connection:** error event is passed through ([a15b1a1](https://github.com/taskforcesh/bullmq/commit/a15b1a1824c6863ecf3e5132e22924fc3ff161f6))
* **worker:** error event is passed through ([d7f0374](https://github.com/taskforcesh/bullmq/commit/d7f03749ce300e917399a435a3f426e66145dd8c))

### [1.8.7](https://github.com/taskforcesh/bullmq/compare/v1.8.6...v1.8.7) (2020-04-10)

#### Bug Fixes

* **worker:** do not use global child pool fixes [#172](https://github.com/taskforcesh/bullmq/issues/172) ([bc65f26](https://github.com/taskforcesh/bullmq/commit/bc65f26dd47c59d0a7277ac947140405557be9a5))

### [1.8.6](https://github.com/taskforcesh/bullmq/compare/v1.8.5...v1.8.6) (2020-04-10)

#### Bug Fixes

* **workers:** do not call super.close() ([ebd2ae1](https://github.com/taskforcesh/bullmq/commit/ebd2ae1a5613d71643c5a7ba3f685d77585de68e))
* make sure closing is returned in every close call ([88c5948](https://github.com/taskforcesh/bullmq/commit/88c5948d33a9a7b7a4f4f64f3183727b87d80207))
* **scheduler:** duplicate connections fixes [#174](https://github.com/taskforcesh/bullmq/issues/174) ([011b8ac](https://github.com/taskforcesh/bullmq/commit/011b8acfdec54737d94a9fead2423e060e3364db))
* **worker:** return this.closing when calling close ([06d3d4f](https://github.com/taskforcesh/bullmq/commit/06d3d4f476444a2d2af8538d60cb2561a1915868))

### [1.8.5](https://github.com/taskforcesh/bullmq/compare/v1.8.4...v1.8.5) (2020-04-05)

#### Bug Fixes

* removed deprecated and unused node-uuid ([c810579](https://github.com/taskforcesh/bullmq/commit/c810579029d33ef47d5a7563e63126a69c62fd87))

### [1.8.4](https://github.com/taskforcesh/bullmq/compare/v1.8.3...v1.8.4) (2020-03-17)

#### Bug Fixes

* **job:** added nullable/optional properties ([cef134f](https://github.com/taskforcesh/bullmq/commit/cef134f7c4d87e1b80ba42a5e06c3877956ff4cc))

### [1.8.3](https://github.com/taskforcesh/bullmq/compare/v1.8.2...v1.8.3) (2020-03-13)

#### Bug Fixes

* **sandbox:** If the child process is killed, remove it from the pool. ([8fb0fb5](https://github.com/taskforcesh/bullmq/commit/8fb0fb569a0236b37d3bae06bf58a2a1da3221c6))

### [1.8.2](https://github.com/taskforcesh/bullmq/compare/v1.8.1...v1.8.2) (2020-03-03)

#### Bug Fixes

* restore the Job timestamp when deserializing JSON data ([#138](https://github.com/taskforcesh/bullmq/issues/138)) ([#152](https://github.com/taskforcesh/bullmq/issues/152)) ([c171bd4](https://github.com/taskforcesh/bullmq/commit/c171bd47f7b75378e75307a1decdc0f630ac1cd6))

### [1.8.1](https://github.com/taskforcesh/bullmq/compare/v1.8.0...v1.8.1) (2020-03-02)

#### Bug Fixes

* modified imports to work when esModuleInterop is disabled ([#132](https://github.com/taskforcesh/bullmq/issues/132)) ([01681f2](https://github.com/taskforcesh/bullmq/commit/01681f282bafac2df2c602edb51d6bde3483896c))

## [1.8.0](https://github.com/taskforcesh/bullmq/compare/v1.7.0...v1.8.0) (2020-03-02)

#### Bug Fixes

* cleanup signatures for queue add and addBulk ([#127](https://github.com/taskforcesh/bullmq/issues/127)) ([48e221b](https://github.com/taskforcesh/bullmq/commit/48e221b53909079a4def9c48c1b69cebabd0ed74))
* exit code 12 when using inspect with child process ([#137](https://github.com/taskforcesh/bullmq/issues/137)) ([43ebc67](https://github.com/taskforcesh/bullmq/commit/43ebc67cec3e8f283f9a555b4466cf918226687b))

#### Features

* **types:** add sandboxed job processor types ([#114](https://github.com/taskforcesh/bullmq/issues/114)) ([a50a88c](https://github.com/taskforcesh/bullmq/commit/a50a88cd1658fa9d568235283a4c23a74eb8ed2a))

## [1.7.0](https://github.com/taskforcesh/bullmq/compare/v1.6.8...v1.7.0) (2020-03-02)

#### Features

* made queue name publicly readable for [#140](https://github.com/taskforcesh/bullmq/issues/140) ([f2bba2e](https://github.com/taskforcesh/bullmq/commit/f2bba2efd9d85986b01bb35c847a232b5c42ae57))

### [1.6.8](https://github.com/taskforcesh/bullmq/compare/v1.6.7...v1.6.8) (2020-02-22)

#### Bug Fixes

* modified QueueGetters.getJob and Job.fromId to also return null to ([65183fc](https://github.com/taskforcesh/bullmq/commit/65183fcf542d0227ec1d4d6637b46b5381331787))
* modified QueueGetters.getJob and Job.fromId to return undefined ([ede352b](https://github.com/taskforcesh/bullmq/commit/ede352be75ffe05bf633516db9eda88467c562bf))

### [1.6.7](https://github.com/taskforcesh/bullmq/compare/v1.6.6...v1.6.7) (2020-01-16)

#### Bug Fixes

* don't fail a job when the worker already lost the lock ([23c0bf7](https://github.com/taskforcesh/bullmq/commit/23c0bf70eab6d166b0483336f103323d1bf2ca64))

### [1.6.6](https://github.com/taskforcesh/bullmq/compare/v1.6.5...v1.6.6) (2020-01-05)

#### Bug Fixes

* remove duplicate active entry ([1d2cca3](https://github.com/taskforcesh/bullmq/commit/1d2cca38ee61289adcee4899a91f7dcbc93a7c05))

### [1.6.5](https://github.com/taskforcesh/bullmq/compare/v1.6.4...v1.6.5) (2020-01-05)

#### Bug Fixes

* get rid of flushdb/flushall in tests ([550c67b](https://github.com/taskforcesh/bullmq/commit/550c67b25de5f6d800e5e317398044cd16b85924))

### [1.6.4](https://github.com/taskforcesh/bullmq/compare/v1.6.3...v1.6.4) (2020-01-05)

#### Bug Fixes

* delete logs when cleaning jobs in set ([b11c6c7](https://github.com/taskforcesh/bullmq/commit/b11c6c7c9f4f1c49eac93b98fdc93ac8f861c8b2))

### [1.6.3](https://github.com/taskforcesh/bullmq/compare/v1.6.2...v1.6.3) (2020-01-01)

#### Bug Fixes

* add tslib dependency fixes [#65](https://github.com/taskforcesh/bullmq/issues/65) ([7ad7995](https://github.com/taskforcesh/bullmq/commit/7ad799544a9c30b30aa96df8864119159c9a1185))

### [1.6.2](https://github.com/taskforcesh/bullmq/compare/v1.6.1...v1.6.2) (2019-12-16)

#### Bug Fixes

* change default QueueEvents lastEventId to $ ([3c5b01d](https://github.com/taskforcesh/bullmq/commit/3c5b01d16ee1442f5802a0fe4e7675c14f7a7f1f))
* ensure QE ready before adding test events ([fd190f4](https://github.com/taskforcesh/bullmq/commit/fd190f4be792b03273481c8aaf73be5ca42663d1))
* explicitly test the behavior of .on and .once ([ea11087](https://github.com/taskforcesh/bullmq/commit/ea11087b292d9325105707b53f92ac61c334a147))

### [1.6.1](https://github.com/taskforcesh/bullmq/compare/v1.6.0...v1.6.1) (2019-12-16)

#### Bug Fixes

* check of existing redis instance ([dd466b3](https://github.com/taskforcesh/bullmq/commit/dd466b332b03b430108126531d59ff9e66ce9521))

## [1.6.0](https://github.com/taskforcesh/bullmq/compare/v1.5.0...v1.6.0) (2019-12-12)

#### Features

* add generic type to job data and return value ([87c0531](https://github.com/taskforcesh/bullmq/commit/87c0531efc2716db37f8a0886848cdb786709554))

## [1.5.0](https://github.com/taskforcesh/bullmq/compare/v1.4.3...v1.5.0) (2019-11-22)

#### Features

* remove delay dependency ([97e1a30](https://github.com/taskforcesh/bullmq/commit/97e1a3015d853e615ddd623af07f12a194ccab2c))
* remove dependence on Bluebird.delay [#67](https://github.com/taskforcesh/bullmq/issues/67) ([bedbaf2](https://github.com/taskforcesh/bullmq/commit/bedbaf25af6479e387cd7548e246dca7c72fc140))

### [1.4.3](https://github.com/taskforcesh/bullmq/compare/v1.4.2...v1.4.3) (2019-11-21)

#### Bug Fixes

* check in moveToFinished to use default val for opts.maxLenEvents ([d1118aa](https://github.com/taskforcesh/bullmq/commit/d1118aab77f755b4a65e3dd8ea2e195baf3d2602))

### [1.4.2](https://github.com/taskforcesh/bullmq/compare/v1.4.1...v1.4.2) (2019-11-21)

#### Bug Fixes

* avoid Job<->Queue circular json error ([5752727](https://github.com/taskforcesh/bullmq/commit/5752727a6294e1b8d35f6a49e4953375510e10e6))
* avoid the .toJSON serializer interface [#70](https://github.com/taskforcesh/bullmq/issues/70) ([5941b82](https://github.com/taskforcesh/bullmq/commit/5941b82b646e46d53970197a404e5ea54f09d008))

### [1.4.1](https://github.com/taskforcesh/bullmq/compare/v1.4.0...v1.4.1) (2019-11-08)

#### Bug Fixes

* default job settings [#58](https://github.com/taskforcesh/bullmq/issues/58) ([667fc6e](https://github.com/taskforcesh/bullmq/commit/667fc6e00ae4d6da639d285a104fb67e01c95bbd))

## [1.4.0](https://github.com/taskforcesh/bullmq/compare/v1.3.0...v1.4.0) (2019-11-06)

#### Features

* job.progress() return last progress for sandboxed processors ([5c4b146](https://github.com/taskforcesh/bullmq/commit/5c4b146ca8e42c8a29f9db87326a17deac30e10e))

## [1.3.0](https://github.com/taskforcesh/bullmq/compare/v1.2.0...v1.3.0) (2019-11-05)

#### Features

* test worker extends job lock while job is active ([577efdf](https://github.com/taskforcesh/bullmq/commit/577efdfb1d2d3140be78dee3bd658b5ce969b16d))

## [1.2.0](https://github.com/taskforcesh/bullmq/compare/v1.1.0...v1.2.0) (2019-11-03)

#### Bug Fixes

* only run coveralls after success ([bd51893](https://github.com/taskforcesh/bullmq/commit/bd51893c35793657b65246a2f5a06469488c8a06))

#### Features

* added code coverage and coveralls ([298cfc4](https://github.com/taskforcesh/bullmq/commit/298cfc48e35e648e6a22ac0d1633ac16c7b6e3de))
* added missing deps for coverage ([6f3ab8d](https://github.com/taskforcesh/bullmq/commit/6f3ab8d78ba8503a76447f0db5abf0c1c4f8e185))
* ignore commitlint file in coverage ([f874441](https://github.com/taskforcesh/bullmq/commit/f8744411a1b20b95e568502be15ec50cf8520926))
* only upload coverage once after all tests pass ([a7f73ec](https://github.com/taskforcesh/bullmq/commit/a7f73ecc2f51544f1d810de046ba073cb7aa5663))

## [1.1.0](https://github.com/taskforcesh/bullmq/compare/v1.0.1...v1.1.0) (2019-11-01)

#### Bug Fixes

* failing build ([bb21d53](https://github.com/taskforcesh/bullmq/commit/bb21d53b199885dcc97e7fe20f60caf65e55e782))
* fix failing tests ([824eb6b](https://github.com/taskforcesh/bullmq/commit/824eb6bfb2b750b823d057c894797ccb336245d8))

#### Features

* initial version of job locking mechanism ([1d4fa38](https://github.com/taskforcesh/bullmq/commit/1d4fa383e39f4f5dcb69a71a1359dd5dea75544c))

### [1.0.1](https://github.com/taskforcesh/bullmq/compare/v1.0.0...v1.0.1) (2019-10-27)

#### Bug Fixes

* save job stacktrace on failure ([85dfe52](https://github.com/taskforcesh/bullmq/commit/85dfe525079a5f89c1901dbf35c7ddc6663afc24))
* simplify logic for stackTraceLimit ([296bd89](https://github.com/taskforcesh/bullmq/commit/296bd89514d430a499afee934dcae2aec41cffa2))

## 1.0.0 (2019-10-20)

#### Bug Fixes

* add compilation step before running tests ([64abc13](https://github.com/taskforcesh/bullmq/commit/64abc13681f8735fb3ee5add5b271bb4da618047))
* add extra client to worker fixes [#34](https://github.com/taskforcesh/bullmq/issues/34) ([90bd891](https://github.com/taskforcesh/bullmq/commit/90bd891c7514f5e9e397d7aad15069ee55bebacd))
* add missing dependency ([b92e330](https://github.com/taskforcesh/bullmq/commit/b92e330aad35ae54f43376f92ad1b41209012b76))
* check closing after resuming from pause ([7b2cef3](https://github.com/taskforcesh/bullmq/commit/7b2cef3677e2b3af0370e0023aec4b971ad313fe))
* default opts ([333c73b](https://github.com/taskforcesh/bullmq/commit/333c73b5819a263ae92bdb54f0406c19db5cb64f))
* do not block if blockTime is zero ([13b2df2](https://github.com/taskforcesh/bullmq/commit/13b2df20cf045c069b8b581751e117722681dcd4))
* do not exec if closing ([b1d1c08](https://github.com/taskforcesh/bullmq/commit/b1d1c08a2948088eeb3dd65de78085329bac671b))
* do not trim if maxEvents is undefined ([7edd8f4](https://github.com/taskforcesh/bullmq/commit/7edd8f47b392c8b3a7369196befdafa4b29421d1))
* emit wait event in add job ([39cba31](https://github.com/taskforcesh/bullmq/commit/39cba31a30b7ef762a8d55d4bc34efec636207bf))
* fix a couple of job tests ([e66b97b](https://github.com/taskforcesh/bullmq/commit/e66b97be4577d5ab373fff0f3f45d73de7842a37))
* fix compiling error ([3cf2617](https://github.com/taskforcesh/bullmq/commit/3cf261703292d263d1e2017ae30eb490121dab4e))
* fix more tests ([6a07b35](https://github.com/taskforcesh/bullmq/commit/6a07b3518f856e8f7158be032110c925ed5c924f))
* fix progress script ([4228e27](https://github.com/taskforcesh/bullmq/commit/4228e2768c0cf404e09642ebb4053147d0badb56))
* fix retry functionality ([ec41ea4](https://github.com/taskforcesh/bullmq/commit/ec41ea4e0bd88b10b1ba434ef5ceb0952bb59f7b))
* fix several floating promises ([590a4a9](https://github.com/taskforcesh/bullmq/commit/590a4a925167a7c7d6c0d9764bbb5ab69235beb7))
* fixed reprocess lua script ([b78296f](https://github.com/taskforcesh/bullmq/commit/b78296f33517b8c5d79b300fef920edd03149d2f))
* improve concurrency mechanism ([a3f6148](https://github.com/taskforcesh/bullmq/commit/a3f61489e3c9891f42749ff85bd41064943c62dc))
* improve disconnection for queue events ([56b53a1](https://github.com/taskforcesh/bullmq/commit/56b53a1aca1e527b50f04d906653060fe8ca644e))
* initialize events comsumption in constructor ([dbb66cd](https://github.com/taskforcesh/bullmq/commit/dbb66cda9722d44eca806fa6ad1cabdaabac846a))
* make ioredis typings a normal dependency ([fb80b90](https://github.com/taskforcesh/bullmq/commit/fb80b90b12931a12a1a93c5e204dbf90eed4f48f))
* minor fixes ([7791cda](https://github.com/taskforcesh/bullmq/commit/7791cdac2bfb6a7fbbab9c95c5d89b1eae226a4c))
* parse progres and return value in events ([9e43d0e](https://github.com/taskforcesh/bullmq/commit/9e43d0e30ab90a290942418718cde1f5bfbdcf56))
* properly emit event for progress ([3f70175](https://github.com/taskforcesh/bullmq/commit/3f701750b1c957027825ee90b58141cd2556694f))
* reduce drain delay to 5 seconds ([c6cfe7c](https://github.com/taskforcesh/bullmq/commit/c6cfe7c0b50cabe5e5eb31f4b631a8b1d3706611))
* remove buggy close() on redis-connection (fixes 5 failing tests) ([64c2ede](https://github.com/taskforcesh/bullmq/commit/64c2edec5e738f43676d0f4ca61bdea8609203fc))
* remove unused dependencies ([34293c8](https://github.com/taskforcesh/bullmq/commit/34293c84bb0ed54f18d70c86821c3ac627d376a5))
* replace init by waitUntilReady ([4336161](https://github.com/taskforcesh/bullmq/commit/43361610de5b1a993a1c65f3f21ac745b8face21))
* reworked initialization of redis clients ([c17d4be](https://github.com/taskforcesh/bullmq/commit/c17d4be5a2ecdda3efcdc6b9d7aecdfaccd06d83))
* several fixes to make the lib work on other ts projects ([3cac1b0](https://github.com/taskforcesh/bullmq/commit/3cac1b0715613d9df51cb1ed6fe0859bcfbb8e9b))
* throw error messages instead of codes ([9267541](https://github.com/taskforcesh/bullmq/commit/92675413f1c3b9564574dc264ffcab0d6089e70e))
* update tests after merge ([51f75a4](https://github.com/taskforcesh/bullmq/commit/51f75a4929e7ae2704e42fa9035e335fe60d8dc0))
* wait until ready before trying to get jobs ([f3b768f](https://github.com/taskforcesh/bullmq/commit/f3b768f251ddafa207466af552376065b35bec8f))
* **connections:** reused connections ([1e808d2](https://github.com/taskforcesh/bullmq/commit/1e808d24018a29f6611f4fccd2f5754de0fa3e39))
* waitUntilFinished improvements ([18d4afe](https://github.com/taskforcesh/bullmq/commit/18d4afef08f04d19cb8d931e02fff8f962d07ee7))

#### Features

* add cleaned event ([c544775](https://github.com/taskforcesh/bullmq/commit/c544775803626b5f03cf6f7c3cf18ed1d92debab))
* add empty method ([4376112](https://github.com/taskforcesh/bullmq/commit/4376112369d869c0a5c7ab4a543cfc50200e1414))
* add retry errors ([f6a7990](https://github.com/taskforcesh/bullmq/commit/f6a7990fb74585985729c5d95e2238acde6cf74a))
* add script to generate typedocs ([d0a8cb3](https://github.com/taskforcesh/bullmq/commit/d0a8cb32ef9090652017f8fbf2ca42f0960687f7))
* add some new tests for compat class, more minor fixes ([bc0f653](https://github.com/taskforcesh/bullmq/commit/bc0f653ecf7aedd5a46eee6f912ecd6849395dca))
* add support for adding jobs in bulk ([b62bddc](https://github.com/taskforcesh/bullmq/commit/b62bddc054b266a809b4b1646558a095a276d6d1))
* add trimEvents method to queue client ([b7da7c4](https://github.com/taskforcesh/bullmq/commit/b7da7c4de2de81282aa41f8b7624b9030edf7d15))
* automatically trim events ([279bbba](https://github.com/taskforcesh/bullmq/commit/279bbbab7e96ad8676ed3bd68663cb199067ea67))
* emit global stalled event fixes [#10](https://github.com/taskforcesh/bullmq/issues/10) ([241f229](https://github.com/taskforcesh/bullmq/commit/241f229761691b9ac17124da005f91594a78273d))
* get rid of Job3 in favor of bullmq Job class ([7590cea](https://github.com/taskforcesh/bullmq/commit/7590ceae7abe32a8824e4a265f95fef2f9a6665f))
* implement close in redis connection fixes [#8](https://github.com/taskforcesh/bullmq/issues/8) ([6de8b48](https://github.com/taskforcesh/bullmq/commit/6de8b48c9612ea39bb28db5f4130cb2a2bb5ee90))
* make delay in backoffs optional ([30d59e5](https://github.com/taskforcesh/bullmq/commit/30d59e519794780a8198222d0bbd88779c623275))
* move async initialization to constructors ([3fbacd0](https://github.com/taskforcesh/bullmq/commit/3fbacd088bc3bfbd61ed8ff173e4401193ce48ec))
* port a lot of functionality from bull 3.x ([ec9f3d2](https://github.com/taskforcesh/bullmq/commit/ec9f3d266c1aca0c27cb600f056d813c81259b4c))
* port more features from bull 3.x ([75bd261](https://github.com/taskforcesh/bullmq/commit/75bd26158678ee45a14e04fd7c3a1f96219979a2))
* ported tests and functionality from bull 3 ([1b6b192](https://github.com/taskforcesh/bullmq/commit/1b6b1927c7e8e6b6f1bf0bbd6c74eb59cc17deb6))
* **workers:** support for async backoffs ([c555837](https://github.com/taskforcesh/bullmq/commit/c55583701e5bdd4e6436a61c833e506bc05749de))
* remove support of bull3 config format in compat class ([d909486](https://github.com/taskforcesh/bullmq/commit/d9094868e34c2af21f810aaef4542951a509ccf8))
* support global:progress event ([60f4d85](https://github.com/taskforcesh/bullmq/commit/60f4d85d332b3be4a80db7aa179f3a9ceeb1d6f8))
* trim option to event stream [#21](https://github.com/taskforcesh/bullmq/issues/21) & fix [#17](https://github.com/taskforcesh/bullmq/issues/17) ([7eae653](https://github.com/taskforcesh/bullmq/commit/7eae65340820043101fadf1f87802f506020d553))

### 4.0.0-beta.2

#### Fixed

* Removed humans, they weren't doing fine with animals.

#### Changed

* Animals are now super cute, all of them.

### 4.0.0-beta.1

#### Added

* Introduced animals into the world, we believe they're going to be a neat addition.

### 4.0.0-beta.0


# Introduction

BullMQ is based in 4 classes that together can be used to resolve many different problems. These classes are [***Queue***](https://api.docs.bullmq.io/classes/v5.Queue.html), [***Worker***](https://api.docs.bullmq.io/classes/v5.Worker.html), [***QueueEvents***](https://api.docs.bullmq.io/classes/v5.QueueEvents.html) and [***FlowProducer***](https://api.docs.bullmq.io/classes/v5.FlowProducer.html).

The first class you should know about is the *Queue* class. This class represents a queue and can be used for adding ***jobs*** to the queue as well as some other basic manipulation such as pausing, cleaning or getting data from the queue.

Jobs in BullMQ are basically a user created data structure that can be stored in the queue. Jobs are processed by ***workers***. A *Worker* is the second class you should be aware about. Workers are instances capable of processing jobs. You can have many workers, either running in the same Node.js process, or in separate processes as well as in different machines. They will all consume jobs from the queue and mark the jobs as completed or failed.


# Connections

In order to start working with a Queue, a connection to a Redis instance is necessary. BullMQ uses the node module [ioredis](https://github.com/luin/ioredis), and the options you pass to BullMQ are just passed to the constructor of ioredis. If you do not provide any options, it will default to port 6379 and localhost.

Every class will consume at least one Redis connection, but it is also possible to reuse connections in some situations. For example, the *Queue* and *Worker* classes can accept an existing ioredis instance, and by that reusing that connection, however *QueueScheduler* and *QueueEvents* cannot do that because they require blocking connections to Redis, which makes it impossible to reuse them.

Some examples:

```typescript
import { Queue, Worker } from 'bullmq';

// Create a new connection in every instance
const myQueue = new Queue('myqueue', {
  connection: {
    host: 'myredis.taskforce.run',
    port: 32856,
  },
});

const myWorker = new Worker('myqueue', async job => {}, {
  connection: {
    host: 'myredis.taskforce.run',
    port: 32856,
  },
});
```

```typescript
import { Queue } from 'bullmq';
import IORedis from 'ioredis';

const connection = new IORedis();

// Reuse the ioredis instance in 2 different producers
const myFirstQueue = new Queue('myFirstQueue', { connection });
const mySecondQueue = new Queue('mySecondQueue', { connection });
```

```typescript
import { Worker } from 'bullmq';
import IORedis from 'ioredis';

const connection = new IORedis({ maxRetriesPerRequest: null });

// Reuse the ioredis instance in 2 different consumers
const myFirstWorker = new Worker('myFirstWorker', async job => {}, {
  connection,
});
const mySecondWorker = new Worker('mySecondWorker', async job => {}, {
  connection,
});
```

Note that in the third example, even though the ioredis instance is being reused, the worker will create a duplicated connection that it needs internally to make blocking connections. Consult the [ioredis](https://github.com/luin/ioredis/blob/master/API.md) documentation to learn how to properly create an instance of `IORedis`.

#### `maxRetriesPerRequest`

This setting tells the ioredis client how many times to try a command that fails before throwing an error. So even though Redis is not reachable or offline, the command will be retried until this situation changes or the maximum number of attempts is reached.

This guarantees that the workers will keep processing forever as long as there is a working connection. If you create a Redis client manually, BullMQ will throw an exception if this setting is not set to null when it is passed into worker instances.

### Queue

Also note that simple Queue instance used for managing the queue such as adding jobs, pausing, using getters, etc. usually has different requirements from the worker.

For example, say that you are adding jobs to a queue as the result of a call to an HTTP endpoint - producer service. The caller of this endpoint cannot wait forever if the connection to Redis happens to be down when this call is made. Therefore the `maxRetriesPerRequest` setting should either be left at its default (which currently is 20) or set it to another value, maybe 1 so that the user gets an error quickly and can retry later.

On the other hand, if you are adding jobs inside a Worker processor, this process is expected to happen in the background - consumer service. In this case you can share the same connection.

For more details, refer to the [persistent connections](https://docs.bullmq.io/bull/patterns/persistent-connections) page.

{% hint style="danger" %}
When using ioredis connections, be careful not to use the "keyPrefix" option in [ioredis](https://redis.github.io/ioredis/interfaces/CommonRedisOptions.html#keyPrefix) as this option is not compatible with BullMQ, which provides its own key prefixing mechanism by using [prefix](https://api.docs.bullmq.io/interfaces/v5.QueueOptions.html#prefix) option.
{% endhint %}

If you can afford many connections, by all means just use them. Redis connections have quite low overhead, so you should not need to care about reusing connections unless your service provider imposes hard limitations.

{% hint style="danger" %}
Make sure that your redis instance has the setting

`maxmemory-policy=noeviction`

in order to avoid automatic removal of keys which would cause unexpected errors in BullMQ
{% endhint %}


# Queues

A Queue is nothing more than a list of jobs waiting to be processed. The jobs can be small, message like, so that the queue can be used as a message broker, or they can be larger long running jobs.

Queues are controlled with the `Queue` class. As all classes in BullMQ, this is a lightweight class with a handful of methods that gives you control over the queue:

```typescript
const queue = new Queue('Cars');
```

{% hint style="info" %}
See [Connections](https://docs.bullmq.io/guide/connections) for details on how to pass Redis details to use by the queue.
{% endhint %}

When you instantiate a Queue, BullMQ will just *upsert* a small "meta-key", so if the queue existed before it will just pick it up and you can continue adding jobs to it.

The most important method is probably the [***add***](https://api.docs.bullmq.io/classes/v5.Queue.html#add) method. This method allows you to add jobs to the queue in different fashions:

```typescript
await queue.add('paint', { color: 'red' });
```

The code above will add a job named *paint* to the queue, with payload `{ color: 'red' }`. This job will now be stored in Redis in a list waiting for some worker to pick it up and process it. Workers may not be running when you add the job, however as soon as one worker is connected to the queue it will pick the job and process it.

When adding a job you can also specify an options object. This options object can dramatically change the behaviour of the added jobs. For example you can add a job that is delayed:

```typescript
await queue.add('paint', { color: 'blue' }, { delay: 5000 });
```

The job will now wait **at** **least** 5 seconds before it is processed.

{% hint style="danger" %}
Prior to BullMQ 2.0, in order for delay jobs to work you need to have at least one `QueueScheduler` somewhere in your infrastructure. Read more [here](https://docs.bullmq.io/guide/queuescheduler).

From BullMQ 2.0 and onwards, the `QueueScheduler` is not needed anymore.
{% endhint %}

There are many other options available such as priorities, backoff settings, lifo behaviour, remove-on-complete policies, etc. Please check the remainder of this guide for more information regarding these options.

## Read more:

* 💡 [Queue API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html)


# Auto-removal of jobs

By default, when your queue jobs are completed (or failed), they are stored in two special sets, the "completed" and the "failed" set. This is useful so that you can examine the results of your jobs, particularly in the early stages of development. However, as the solution reaches a production-grade level, we usually need to restrict the number of finished jobs to be kept, so that we do not fill Redis with data that is not particularly useful.

BullMQ supports different strategies for auto-removing finalized jobs. These strategies are configured on the Job's options [`removeOnComplete`](https://api.docs.bullmq.io/interfaces/v5.BaseJobOptions.html#removeoncomplete) and [`removeOnFail`](https://api.docs.bullmq.io/interfaces/v5.BaseJobOptions.html#removeonfail).

### Remove all finalized jobs

The simplest option is to set `removeOnComplete`/`removeOnFail` to `true`, in this case, all jobs will be removed automatically as soon as they are finalized:

```typescript
await myQueue.add(
  'test',
  { foo: 'bar' },
  { removeOnComplete: true, removeOnFail: true },
);
```

{% hint style="warning" %}
Jobs will be deleted regardless of their names.
{% endhint %}

### Keep a certain number of jobs

It is also possible to specify a maximum number of jobs to keep. A good practice is to keep a handful of completed jobs and a much larger value of failed jobs:

```typescript
await myQueue.add(
  'test',
  { foo: 'bar' },
  { removeOnComplete: 1000, removeOnFail: 5000 },
);
```

### Keep jobs based on their age

Another possibility is to keep jobs up to a certain age. The `removeOn` option accepts a [`KeepJobs`](https://api.docs.bullmq.io/interfaces/v5.KeepJobs.html) object, that includes an `age` and a `count` fields. The `age` is used to specify how old jobs to keep (in seconds), and the `count` can be used to limit the total amount to keep. The `count` option is useful in cases we get an unexpected amount of jobs in a very short time, in this case we may just want to limit to a certain amount to avoid running out of memory.

```typescript
await myQueue.add(
  'test',
  { foo: 'bar' },
  {
    removeOnComplete: {
      age: 3600, // keep up to 1 hour
      count: 1000, // keep up to 1000 jobs
    },
    removeOnFail: {
      age: 24 * 3600, // keep up to 24 hours
    },
  },
);
```

{% hint style="info" %}
The auto removal of jobs works lazily. This means that jobs are not removed unless a new job completes or fails, since that is when the auto-removal takes place.
{% endhint %}

### What about idempotence?

One of the strategies to implement idempotence with BullMQ is to use unique job ids. When you add a job with an id that exists already in the queue, the new job is ignored and a **duplicated** event is triggered. It is important to keep this in mind when activating auto removal of jobs, since a job that has been removed will not be considered part of the queue anymore, and will not affect any future jobs that could have the same Id.

## Read more:

* 💡 [Duplicated Event Reference](https://api.docs.bullmq.io/interfaces/v5.QueueEventsListener.html#duplicated)


# Adding jobs in bulk

Sometimes it is necessary to add many jobs atomically. For example, there could be a requirement that all the jobs must be placed in the queue or none of them. Also, adding jobs in bulk can be faster since it reduces the number of roundtrips to Redis:

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import { Queue } from 'bullmq';

const queue = new Queue('paint');

const name = 'jobName';
const jobs = await queue.addBulk([
  { name, data: { paint: 'car' } },
  { name, data: { paint: 'house' } },
  { name, data: { paint: 'boat' } },
]);
```

{% endtab %}

{% tab title="Python" %}

```python
from bullmq import Queue

queue = Queue("paint")

jobs = await queue.addBulk([
  { "name": "jobName", "data": { "paint": "car" } },
  { "name": "jobName", "data": { "paint": "house" } },
  { "name": "jobName", "data": { "paint": "boat" } }
])
```

{% endtab %}
{% endtabs %}

This call can only succeed or fail, and all or none of the jobs will be added.

## Read more:

* 💡 [Add Bulk API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#addbulk)


# Global Concurrency

The global concurrency factor is a queue option that determines how many jobs are allowed to be processed in parallel across all your worker instances.

```typescript
import { Queue } from 'bullmq';

await queue.setGlobalConcurrency(4);
```

And in order to get this value:

```typescript
const globalConcurrency = await queue.getGlobalConcurrency();
```

{% hint style="info" %}
Note that if you choose a concurrency level in your workers, it will not override the global one, it will just be the maximum jobs a given worker can process in parallel but never more than the global one.
{% endhint %}

### Remove Global Concurrency

It can be done using the following method:

```typescript
await queue.removeGlobalConcurrency();
```

## Read more:

* 💡 [Set Global Concurrency API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#setglobalconcurrency)
* 💡 [Get Global Concurrency API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#getglobalconcurrency)
* 💡 [Remove Global Concurrency API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#removeglobalconcurrency)


# Global Rate Limit

The global rate limit config is a queue option that determines how many jobs are allowed to be processed in a specific period of time.

```typescript
import { Queue } from 'bullmq';

// 1 job per second
await queue.setGlobalRateLimit(1, 1000);
```

In order to get these values:

```typescript
const { max, duration } = await queue.getGlobalRateLimit();
```

And in order to get current ttl:

```typescript
const ttl = await queue.getRateLimitTtl();
```

{% hint style="info" %}
Note that if you choose a rate limit level in your workers, it won't override the global one.
{% endhint %}

### Remove Global Rate Limit

It can be done using the following method:

```typescript
await queue.removeGlobalRateLimit();
```

## Read more:

* 💡 [Set Global Rate Limit API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#setglobalratelimit)
* 💡 [Get Global Rate Limit API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#getglobalratelimit)
* 💡 [Get Rate Limit Ttl API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#getratelimitttl)
* 💡 [Remove Global Rate Limit API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#removeglobalratelimit)


# Meta

The meta data of any queue can be retrieved in the following way:

```typescript
import { Queue } from 'bullmq';

const { concurrency, max, duration, maxLenEvents, paused, version } =
  await queue.getMeta();
```

## Read more:

* 💡 [Get Meta API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#getmeta)
* 💡 [Global Concurrency](https://docs.bullmq.io/guide/queues/global-concurrency)
* 💡 [Global Rate Limit](https://docs.bullmq.io/guide/queues/global-rate-limit)


# Removing Jobs

Currently we have 3 available methods in queue class:

## Drain

Removes all jobs that are waiting or delayed, but not active, waiting-children, completed or failed.

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import { Queue } from 'bullmq';

const queue = new Queue('paint');

await queue.drain();
```

{% endtab %}

{% tab title="Python" %}

```python
import asyncio
from bullmq import Queue

async def main():
    queue = Queue('paint')

    await queue.drain()
    await queue.close()

asyncio.run(main())
```

{% endtab %}

{% tab title="Elixir" %}

```elixir
alias BullMQ.Queue

:ok = Queue.drain("paint", connection: :redis)
```

{% endtab %}

{% tab title="PHP" %}

```php
<?php
use BullMQ\Queue;

$queue = new Queue('paint');

$queue->drain();

$queue->close();
?>
```

{% endtab %}
{% endtabs %}

You can also drain delayed jobs by setting the delayed parameter:

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import { Queue } from 'bullmq';

const queue = new Queue('paint');

// Also drain delayed jobs
await queue.drain(true);
```

{% endtab %}

{% tab title="Python" %}

```python
import asyncio
from bullmq import Queue

async def main():
    queue = Queue('paint')

    # Also drain delayed jobs
    await queue.drain(delayed=True)
    await queue.close()

asyncio.run(main())
```

{% endtab %}

{% tab title="Elixir" %}

```elixir
alias BullMQ.Queue

# Also drain delayed jobs
:ok = Queue.drain("paint", delayed: true, connection: :redis)
```

{% endtab %}

{% tab title="PHP" %}

```php
<?php
use BullMQ\Queue;

$queue = new Queue('paint');

// Also drain delayed jobs
$queue->drain(true);

$queue->close();
?>
```

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Parent jobs that belong to the queue being drained will be kept in **waiting-children** status if they have pending children, but if they do not have any pending children they will just be removed.
{% endhint %}

{% hint style="warning" %}
Parent jobs in queues different from the one being drained will either stay in **waiting-children** if they have pending children in other queues, or just moved to wait.
{% endhint %}

## Clean

Removes jobs in a specific state, but keeps jobs within a certain grace period.

```typescript
import { Queue } from 'bullmq';

const queue = new Queue('paint');

const deletedJobIds = await queue.clean(
  60000, // 1 minute
  1000, // max number of jobs to clean
  'paused',
);
```

## Obliterate

Completely obliterates a queue and all of its contents.

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import { Queue } from 'bullmq';

const queue = new Queue('paint');

await queue.obliterate();
```

{% endtab %}

{% tab title="Python" %}

```python
import asyncio
from bullmq import Queue

async def main():
    queue = Queue('paint')

    await queue.obliterate()
    await queue.close()

asyncio.run(main())
```

{% endtab %}

{% tab title="Elixir" %}

```elixir
alias BullMQ.Queue

:ok = Queue.obliterate("paint", connection: :redis)
```

{% endtab %}

{% tab title="PHP" %}

```php
<?php
use BullMQ\Queue;

$queue = new Queue('paint');

$queue->obliterate();

$queue->close();
?>
```

{% endtab %}
{% endtabs %}

For more advanced scenarios where you need to force obliteration even with active jobs:

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import { Queue } from 'bullmq';

const queue = new Queue('paint');

// Force obliteration even with active jobs
await queue.obliterate({ force: true });
```

{% endtab %}

{% tab title="Python" %}

```python
import asyncio
from bullmq import Queue

async def main():
    queue = Queue('paint')

    # Force obliteration even with active jobs
    await queue.obliterate(force=True)
    await queue.close()

asyncio.run(main())
```

{% endtab %}

{% tab title="Elixir" %}

```elixir
alias BullMQ.Queue

# Force obliteration even with active jobs
:ok = Queue.obliterate("paint", force: true, connection: :redis)
```

{% endtab %}

{% tab title="PHP" %}

```php
<?php
use BullMQ\Queue;

$queue = new Queue('paint');

// Force obliteration even with active jobs
$queue->obliterate(['force' => true]);

$queue->close();
?>
```

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Parent jobs in queues different from the one being obliterated will either stay in **waiting-children** if they have pending children in other queues, or just moved to wait.
{% endhint %}

### Read more:

* 💡 [Drain API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#drain)
* 💡 [Clean API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#clean)
* 💡 [Obliterate API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#obliterate)


# Workers

Workers are the actual instances that perform some job based on the jobs that are added in the queue. A worker is equivalent to a "message" receiver in a traditional message queue. The worker's duty is to complete the job. If it succeeds, the job will be moved to the "completed" status. If the worker throws an exception during its processing, the job will automatically be moved to the "failed" status.

{% hint style="info" %}
Failed jobs can be automatically retried, see [Retrying failing jobs](https://docs.bullmq.io/guide/retrying-failing-jobs)
{% endhint %}

A worker is instantiated with the `Worker` class, and the work itself will be performed in the *process function*. Process functions are meant to be asynchronous, using either the `async` keyword or returning a promise.

```typescript
import { Worker, Job } from 'bullmq';

const worker = new Worker(queueName, async (job: Job) => {
  // Optionally report some progress
  await job.updateProgress(42);

  // Optionally sending an object as progress
  await job.updateProgress({ foo: 'bar' });

  // Do something with job
  return 'some value';
});
```

The processor function can also receive an optional third parameter for job cancellation support:

```typescript
const worker = new Worker(
  queueName,
  async (job: Job, token?: string, signal?: AbortSignal) => {
    // signal can be used to detect when a job has been cancelled
    return 'some value';
  },
);
```

{% hint style="info" %}
Learn more about [cancelling jobs](https://docs.bullmq.io/guide/workers/cancelling-jobs) in the dedicated guide.
{% endhint %}

{% hint style="info" %}
When a worker instance is created, it launches the processor immediately
{% endhint %}

In order to decide when your processor should start its execution, pass `autorun: false` as part of worker options:

```typescript
import { Worker, Job } from 'bullmq';

const worker = new Worker(
  queueName,
  async (job: Job) => {
    // Optionally report some progress
    await job.updateProgress(42);

    // Optionally sending an object as progress
    await job.updateProgress({ foo: 'bar' });

    // Do something with job
    return 'some value';
  },
  { autorun: false },
);

worker.run();
```

Note that a processor can optionally return a value. This value can be retrieved either by getting the job and accessing the `returnvalue` property or by listening to the `completed` event:

```typescript
worker.on('completed', (job: Job, returnvalue: any) => {
  // Do something with the return value.
});
```

#### Progress

Inside the worker process function it is also possible to emit progress events. Calling `job.progress` you can specify a number or an object if you have more complex needs. The `progress` event can be listened for in the same way as the `completed` event:

```typescript
worker.on('progress', (job: Job, progress: number | object) => {
  // Do something with the return value.
});
```

Finally, when the process fails with an exception it is possible to listen for the `failed` event too:

```typescript
worker.on('failed', (job: Job | undefined, error: Error, prev: string) => {
  // Do something with the return value.
});
```

It is also possible to listen to global events in order to get notifications of job completions, progress and failures:

```typescript
import { QueueEvents } from 'bullmq';

const queueEvents = new QueueEvents('Paint');

queueEvents.on('completed', ({ jobId, returnvalue }) => {
  // Called every time a job is completed by any worker.
});

queueEvents.on('failed', ({ jobId, failedReason }) => {
  // Called whenever a job is moved to failed by any worker.
});

queueEvents.on('progress', ({ jobId, data }) => {
  // jobId received a progress event
});
```

Finally, you should attach an error listener to your worker to avoid NodeJS raising an unhandled exception when an error occurs. For example:

```typescript
worker.on('error', err => {
  // log the error
  console.error(err);
});
```

{% hint style="danger" %}
If the error handler is missing, your worker may stop processing jobs when an error is emitted! Find more info [here](https://nodejs.org/api/events.html#events_error_events).
{% endhint %}

## Typescript typings

It is also possible to specify the data types for the Job data and return value using generics:

```typescript
const worker = new Worker<MyData, MyReturn>(queueName, async (job: Job) => {});
```

## Read more:

* 💡 [Worker API Reference](https://api.docs.bullmq.io/classes/v5.Worker.html)
* 💡 [Queue Events API Reference](https://api.docs.bullmq.io/classes/v5.QueueEvents.html)


# Auto-removal of jobs

By default, when your queue jobs are completed (or failed), they are stored in two special sets, the "completed" and the "failed" set. This is useful so that you can examine the results of your jobs, particularly in the early stages of development. However, as the solution reaches a production-grade level, we usually need to restrict the number of finished jobs to be kept, so that we do not fill Redis with data that is not particularly useful.

BullMQ supports different strategies for auto-removing finalized jobs. These strategies are configured on the Worker's options [`removeOnComplete`](https://api.docs.bullmq.io/interfaces/v5.WorkerOptions.html#removeoncomplete) and [`removeOnFail`](https://api.docs.bullmq.io/interfaces/v5.WorkerOptions.html#removeonfail).

### Remove all finalized jobs

The simplest option is to set `removeOnComplete`/`removeOnFail` to `{count: 0}`, in this case, all jobs will be removed automatically as soon as they are finalized:

{% tabs %}
{% tab title="TypeScript" %}

```typescript
const myWorker = new Worker(
  'myQueueName',
  async job => {
    // do some work
  },
  {
    connection,
    removeOnFail: { count: 0 },
  },
);
```

{% endtab %}

{% tab title="Python" %}

```python
from bullmq import Worker

def process_job(job):
    # do some work
    pass

worker = Worker(
    'myQueueName',
    process_job,
    {
        "connection": connection,
        "removeOnFail": {"count": 0},
    },
)
```

{% endtab %}

{% tab title="Elixir" %}

```elixir
defmodule MyWorker do
  use BullMQ.Worker

  def process_job(_job) do
    # do some work
    :ok
  end
end

{:ok, worker} = BullMQ.Worker.start_link(
  queue: "myQueueName",
  processor: &MyWorker.process_job/1,
  connection: connection,
  remove_on_fail: %{count: 0}
)
```

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Jobs will be deleted regardless of their names.
{% endhint %}

### Keep a certain number of jobs

It is also possible to specify a maximum number of jobs to keep. A good practice is to keep a handful of completed jobs and a much larger value of failed jobs:

{% tabs %}
{% tab title="TypeScript" %}

```typescript
const myWorker = new Worker(
  'myQueueName',
  async job => {
    // do some work
  },
  {
    connection,
    removeOnComplete: { count: 1000 },
    removeOnFail: { count: 5000 },
  },
);
```

{% endtab %}

{% tab title="Python" %}

```python
from bullmq import Worker

def process_job(job):
    # do some work
    pass

worker = Worker(
    'myQueueName',
    process_job,
    {
        "connection": connection,
        "removeOnComplete": {"count": 1000},
        "removeOnFail": {"count": 5000},
    },
)
```

{% endtab %}

{% tab title="Elixir" %}

```elixir
defmodule MyWorker do
  use BullMQ.Worker

  def process_job(_job) do
    # do some work
    :ok
  end
end

{:ok, worker} = BullMQ.Worker.start_link(
  queue: "myQueueName",
  processor: &MyWorker.process_job/1,
  connection: connection,
  remove_on_complete: %{count: 1000},
  remove_on_fail: %{count: 5000}
)
```

{% endtab %}
{% endtabs %}

### Keep jobs based on their age

Another possibility is to keep jobs up to a certain age. The `removeOn` option accepts a [`KeepJobs`](https://api.docs.bullmq.io/interfaces/v5.KeepJobs.html) object, that includes `age`, `count`, and `limit` fields. The `age` is used to specify how old jobs to keep (in seconds), the `count` can be used to limit the total amount to keep, and the `limit` controls how many jobs are removed per cleanup iteration. The `count` option is useful in cases we get an unexpected amount of jobs in a very short time, in this case we may just want to limit to a certain amount to avoid running out of memory. The `limit` option helps control the performance impact of cleanup operations by limiting how many jobs are processed at once.

{% tabs %}
{% tab title="TypeScript" %}

```typescript
const myWorker = new Worker(
  'myQueueName',
  async job => {
    // do some work
  },
  {
    connection,
    removeOnComplete: {
      age: 3600, // keep up to 1 hour
      count: 1000, // keep up to 1000 jobs
      limit: 100, // remove up to 100 jobs per cleanup iteration
    },
    removeOnFail: {
      age: 24 * 3600, // keep up to 24 hours
      limit: 50, // remove up to 50 jobs per cleanup iteration
    },
  },
);
```

{% endtab %}

{% tab title="Python" %}

```python
from bullmq import Worker

def process_job(job):
    # do some work
    pass

worker = Worker(
    'myQueueName',
    process_job,
    {
        "connection": connection,
        "removeOnComplete": {
            "age": 3600,  # keep up to 1 hour
            "count": 1000,  # keep up to 1000 jobs
            "limit": 100,  # remove up to 100 jobs per cleanup iteration
        },
        "removeOnFail": {
            "age": 24 * 3600,  # keep up to 24 hours
            "limit": 50,  # remove up to 50 jobs per cleanup iteration
        },
    },
)
```

{% endtab %}

{% tab title="Elixir" %}

```elixir
defmodule MyWorker do
  use BullMQ.Worker

  def process_job(_job) do
    # do some work
    :ok
  end
end

{:ok, worker} = BullMQ.Worker.start_link(
  queue: "myQueueName",
  processor: &MyWorker.process_job/1,
  connection: connection,
  remove_on_complete: %{
    age: 3600,    # keep up to 1 hour
    count: 1000,  # keep up to 1000 jobs
    limit: 100    # remove up to 100 jobs per cleanup iteration
  },
  remove_on_fail: %{
    age: 24 * 3600,  # keep up to 24 hours
    limit: 50        # remove up to 50 jobs per cleanup iteration
  }
)
```

{% endtab %}
{% endtabs %}

{% hint style="info" %}
The auto removal of jobs works lazily. This means that jobs are not removed unless a new job completes or fails, since that is when the auto-removal takes place.
{% endhint %}


# Concurrency

There are basically two ways to achieve concurrency with BullMQ using Worker instances. You can run a worker with a concurrency factor larger than 1 (which is the default value), or you can run several workers in different node processes.

#### Local Concurrency factor

The local concurrency factor is a worker option that determines how many jobs are allowed to be processed concurrently (or in parallel if using sandboxed processors) for that instance. This means that the same worker is able to process several jobs at the same time and still provide guarantees such as "at-least-once" and order of processing.

```typescript
import { Worker, Job } from 'bullmq';

const worker = new Worker(
  queueName,
  async (job: Job) => {
    // Do something with job
    return 'some value';
  },
  { concurrency: 50 },
);
```

{% hint style="info" %}
Note that the concurrency is only possible when workers perform asynchronous operations such as a call to a database or a external HTTP service, as this is how node supports concurrency natively. If your workers are very CPU intensive it is better to use [Sandboxed processors](https://docs.bullmq.io/guide/workers/sandboxed-processors).
{% endhint %}

In addition, you can update the concurrency value as you need while your worker is running:

```typescript
worker.concurrency = 5;
```

#### Multiple workers

The other way to achieve concurrency is to provide multiple workers. This is the recommended way to setup BullMQ as besides providing concurrency it also provides higher availability for your workers. You can easily launch a fleet of workers running in many different machines in order to execute the jobs in parallel in a predictable and robust way.

{% hint style="info" %}
If you need to achieve a global concurrency of at most 1 job at a time, refer to [Global concurrency](https://docs.bullmq.io/guide/queues/global-concurrency).
{% endhint %}

You can still (and it is a perfectly good practice to) choose a high concurrency factor for every worker, so that the resources of every machine where the worker is running are used more efficiently.


# Graceful shutdown

BullMQ supports graceful shutdowns of workers. This is important so that we can minimize stalled jobs when a worker for some reason must be shutdown. But note that even in the event of a "ungraceful shutdown", the stalled mechanism in BullMQ allows for new workers to pick up stalled jobs and continue working on them.

{% hint style="danger" %}
Prior to BullMQ 2.0, in order for stalled jobs to be picked up by other workers you need to have a [`QueueScheduler`](https://docs.bullmq.io/guide/queuescheduler) class running in the system.

From BullMQ 2.0 and onwards, the `QueueScheduler` is not needed anymore, so the information above is only valid for older versions.
{% endhint %}

In order to perform a shutdown just call the ***`close`*** method:

```typescript
await worker.close();
```

The above call will mark the worker as *closing* so it will not pick up new jobs, and at the same time it will wait for all the current jobs to be processed (or failed). This call will not timeout by itself, so you should make sure that your jobs finalize in a timely manner. If this call fails for some reason or it is not able to complete, the pending jobs will be marked as stalled and processed by other workers (if correct stalled options are configured on the [`QueueScheduler`](https://api.docs.bullmq.io/interfaces/v1.QueueSchedulerOptions.html)).


# Cancelling jobs

The job cancellation feature allows you to gracefully cancel jobs that are currently being processed by a worker. This is implemented using the standard `AbortController` and `AbortSignal` APIs.

## How It Works

When a worker processes a job, it can receive an optional `AbortSignal` as the third parameter in the processor function. This signal can be used to detect when a job has been cancelled and perform cleanup operations.

```typescript
import { Worker } from 'bullmq';

const worker = new Worker('myQueue', async (job, token, signal) => {
  // The signal parameter is optional and provides cancellation support
  // Your job processing logic here
});
```

## Cancelling Jobs

The `Worker` class provides methods to cancel jobs:

```typescript
// Cancel a specific job by ID
const cancelled = worker.cancelJob('job-id-123');
console.log('Job cancelled:', cancelled); // true if job was active, false otherwise

// Cancel with a reason (useful for debugging)
worker.cancelJob('job-id-456', 'User requested cancellation');

// Cancel all active jobs
worker.cancelAllJobs();

// Cancel all with a reason
worker.cancelAllJobs('System shutdown');

// Get list of active jobs from queue
const activeJobs = await queue.getActive();
console.log(
  'Active jobs:',
  activeJobs.map(j => j.id),
);
```

### Cancellation Reasons

When you provide a cancellation reason, it's passed to the `AbortController.abort(reason)` method and can be accessed via `signal.reason`:

```typescript
const worker = new Worker('myQueue', async (job, token, signal) => {
  return new Promise((resolve, reject) => {
    signal?.addEventListener('abort', () => {
      // Access the cancellation reason
      const reason = signal.reason || 'No reason provided';
      console.log(`Job ${job.id} cancelled: ${reason}`);

      reject(new Error(`Cancelled: ${reason}`));
    });

    // Your processing logic
  });
});

// Later, cancel with a descriptive reason
worker.cancelJob(job.id, 'Resource limit exceeded');
```

## Handling Cancellation (Recommended Pattern)

The **event-based approach** is the recommended pattern as it provides immediate response to cancellation:

```typescript
import { Worker } from 'bullmq';

const worker = new Worker('myQueue', async (job, token, signal) => {
  return new Promise((resolve, reject) => {
    // Listen for abort event
    signal?.addEventListener('abort', () => {
      console.log(`Job ${job.id} cancellation requested`);

      // Clean up resources
      clearInterval(interval);

      // Reject with error
      reject(new Error('Job was cancelled'));
    });

    // Your processing logic
    const interval = setInterval(() => {
      // Do work
      processNextItem();
    }, 100);
  });
});
```

### Why Event-Based?

* ✅ **Immediate response** - No polling delay
* ✅ **More efficient** - No CPU wasted checking in loops
* ✅ **Cleaner code** - Separation of concerns
* ✅ **Standard pattern** - Matches Web APIs like `fetch()`

## Using with Native APIs (Recommended)

Many Web APIs natively support `AbortSignal`. The signal is **composable** - you can pass it to APIs and still listen to it yourself:

```typescript
const worker = new Worker('fetchQueue', async (job, token, signal) => {
  return new Promise(async (resolve, reject) => {
    // Set up abort listener - handles cancellation for the job
    signal?.addEventListener('abort', () => {
      reject(new Error('Job was cancelled'));
    });

    // Pass the SAME signal to fetch - it will abort the network request
    const response = await fetch(job.data.url, {
      signal, // ✅ Cancels the HTTP request at network level
      method: 'GET',
      headers: job.data.headers,
    });

    const data = await response.json();
    resolve(data);
  });
});
```

**Why this pattern is better:**

* ✅ **Simpler** - One abort listener handles everything
* ✅ **Composable** - Signal passed to `fetch()` AND listened to in job
* ✅ The HTTP request is **truly cancelled** at the network level
* ✅ The job is **properly marked as failed** when cancelled
* ✅ No complex error checking needed

### APIs That Support AbortSignal

Many modern APIs accept `signal` directly:

* `fetch(url, { signal })` - HTTP requests
* `addEventListener(event, handler, { signal })` - Auto-removes listener on abort
* Many database clients (Postgres, MongoDB drivers)
* File system operations in newer Node.js APIs

## Cancelling Custom Operations

For operations that don't natively support `AbortSignal`, implement proper cleanup:

```typescript
const worker = new Worker('customQueue', async (job, token, signal) => {
  // Start your operation
  const operation = startLongRunningOperation(job.data);

  // Set up cancellation handler that actually stops the operation
  signal?.addEventListener('abort', () => {
    operation.cancel(); // ✅ Actually stops the work
  });

  try {
    const result = await operation.promise;
    return result;
  } catch (error) {
    if (signal?.aborted) {
      throw new Error('Operation cancelled');
    }
    throw error;
  }
});
```

## Async Cleanup on Cancellation

Perform cleanup operations before rejecting the promise:

```typescript
const worker = new Worker('dbQueue', async (job, token, signal) => {
  // Acquire resources
  const db = await connectToDatabase();
  const cache = await connectToCache();

  return new Promise(async (resolve, reject) => {
    // Set up cleanup handler
    signal?.addEventListener('abort', async () => {
      try {
        console.log('Cleaning up resources...');

        // Close connections gracefully
        await db.close();
        await cache.disconnect();

        console.log('Cleanup complete');
        reject(new Error('Cancelled after cleanup'));
      } catch (cleanupError) {
        console.error('Cleanup failed:', cleanupError);
        reject(new Error('Cleanup failed during cancellation'));
      }
    });

    try {
      // Do your work
      const result = await processWithDatabase(db, job.data);
      await cache.set(`job:${job.id}`, result);
      resolve(result);
    } catch (error) {
      // Cleanup on error too
      await db.close();
      await cache.disconnect();
      throw error;
    }
  });
});
```

## Alternative: Polling Pattern

You can also check `signal.aborted` periodically (less efficient but simpler for some use cases):

```typescript
const worker = new Worker('batchQueue', async (job, token, signal) => {
  const items = job.data.items;
  const results = [];

  for (let i = 0; i < items.length; i++) {
    // Check if job has been cancelled
    if (signal?.aborted) {
      throw new Error(`Cancelled after processing ${i} items`);
    }

    const result = await processItem(items[i]);
    results.push(result);

    // Update progress
    await job.updateProgress(((i + 1) / items.length) * 100);
  }

  return { results, total: results.length };
});
```

## Job State After Cancellation

### With Regular Error (Will Retry)

When you throw a regular `Error` upon cancellation:

* **Job state**: Moves to `failed`
* **Retries**: Job WILL be retried if `attempts` remain
* **Use case**: When you want the job to be retried later

```typescript
const worker = new Worker('retryQueue', async (job, token, signal) => {
  return new Promise((resolve, reject) => {
    signal?.addEventListener('abort', () => {
      // Regular Error - job will retry if attempts remain
      reject(new Error('Cancelled, will retry'));
    });

    // Your work...
  });
});

// Set attempts when adding jobs
await queue.add('task', data, { attempts: 3 });
```

### With UnrecoverableError (No Retry)

When you throw an `UnrecoverableError`:

* **Job state**: Moves to `failed`
* **Retries**: Job will NOT be retried
* **Use case**: When cancellation should be permanent

```typescript
import { Worker, UnrecoverableError } from 'bullmq';

const worker = new Worker('noRetryQueue', async (job, token, signal) => {
  return new Promise((resolve, reject) => {
    signal?.addEventListener('abort', () => {
      // UnrecoverableError - no retries
      reject(new UnrecoverableError('Cancelled permanently'));
    });

    // Your work...
  });
});
```

## Handling Lock Renewal Failures

When a worker loses its lock on a job (due to network issues, Redis problems, or long-running operations), you can gracefully handle this situation using the `lockRenewalFailed` event:

```typescript
const worker = new Worker(
  'myQueue',
  async (job, token, signal) => {
    return new Promise(async (resolve, reject) => {
      signal?.addEventListener('abort', async () => {
        console.log('Job cancelled - cleaning up resources');
        await cleanupResources();
        reject(new Error('Job cancelled'));
      });

      // Your work...
    });
  },
  { connection },
);

// Cancel jobs when lock renewal fails
worker.on('lockRenewalFailed', (jobIds: string[]) => {
  console.log('Lock renewal failed for jobs:', jobIds);
  jobIds.forEach(jobId => worker.cancelJob(jobId));
});
```

{% hint style="warning" %}
**Important:** When a worker loses the lock on a job, it cannot move that job to the `failed` state (as it no longer owns the lock). Instead:

1. The `cancelJob()` aborts the signal, allowing the processor to clean up resources
2. The job remains in `active` state temporarily
3. BullMQ's **stalled job checker** will detect the job and move it back to `waiting`
4. Another worker (or the same worker) will pick it up and retry

This is the correct and intended behavior - trust BullMQ's stalled job mechanism to handle lost locks.
{% endhint %}

### Why This Pattern Works

* ✅ **Immediate cleanup**: The processor detects `signal.aborted` and can release resources
* ✅ **No wasted work**: The processor stops processing when it loses the lock
* ✅ **Automatic recovery**: The stalled job checker moves the job back to waiting
* ✅ **No data loss**: The job will be retried according to its `attempts` setting
* ✅ **Works with existing infrastructure**: Uses BullMQ's built-in stalled job handling

## Multi-Phase Work with Cancellation

Check cancellation at strategic points in multi-phase operations:

```typescript
const worker = new Worker('multiPhaseQueue', async (job, token, signal) => {
  return new Promise(async (resolve, reject) => {
    signal?.addEventListener('abort', () => {
      reject(new Error('Cancelled'));
    });

    try {
      // Phase 1: Download
      if (signal?.aborted) throw new Error('Cancelled before download');
      const data = await downloadData(job.data.url);
      await job.updateProgress(33);

      // Phase 2: Process
      if (signal?.aborted) throw new Error('Cancelled before processing');
      const processed = await processData(data);
      await job.updateProgress(66);

      // Phase 3: Upload
      if (signal?.aborted) throw new Error('Cancelled before upload');
      const result = await uploadResults(processed);
      await job.updateProgress(100);

      resolve(result);
    } catch (error) {
      reject(error);
    }
  });
});
```

## Backward Compatibility

The `signal` parameter is optional. Existing processors that don't use it will continue to work normally:

```typescript
// Old processor - still works
const worker = new Worker('myQueue', async job => {
  return await processJob(job);
});

// New processor - with cancellation support
const worker = new Worker('myQueue', async (job, token, signal) => {
  // Can now handle cancellation
});
```

{% hint style="info" %}
The cancellation feature is fully backward compatible. You only need to add signal handling when you want cancellation support.
{% endhint %}

## Best Practices

1. **Use event-based cancellation** for immediate response
2. **Clean up resources** in the abort handler
3. **Use UnrecoverableError** when cancellation should be permanent
4. **Combine with timeouts** for better control
5. **Check `signal.aborted` at strategic points** in long operations
6. **Handle cleanup errors** gracefully to avoid leaving resources open

## Read more:

* 💡 [Worker API Reference](https://api.docs.bullmq.io/classes/v5.Worker.html)
* 💡 [AbortController MDN](https://developer.mozilla.org/en-US/docs/Web/API/AbortController)
* 💡 [AbortSignal MDN](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal)


# Stalled Jobs

Due to the nature of NodeJS, which is (in general) single threaded and consists of an event loop to handle the asynchronous operations, the process function needs to be written carefully so that the CPU is not occupied for a long time.

When a job reaches a worker and starts to be processed, BullMQ will place a lock on this job to protect the job from being modified by any other client or worker. At the same time, the worker needs to periodically notify BullMQ that it is still working on the job.

{% hint style="info" %}
This period is configured with the `stalledInterval` setting, which normally you should not need to modify.
{% endhint %}

However if the CPU is very busy (due to the process being very CPU intensive), the worker may not have time to renew the lock and tell the queue that it is still working on the job, which is likely to result in the job being marked as *stalled*.

A stalled job is moved back to the waiting status and will be processed again by another worker, or if it has reached its maximum number of stalls, it will be moved to the *failed* set.

Therefore, it is very important to make sure the workers return control to the NodeJS event loop often enough to avoid this kind of problem.


# Sandboxed processors

Running jobs in isolated processes

It is also possible to define workers to run on a separate process. We call these processors *sandboxed*, because they run isolated from the rest of the code.

When your workers perform CPU-heavy operations, they will inevitably keep the NodeJS event loop busy, which prevents BullMQ from doing job bookkeeping such as extending job locks, ultimately leading to "stalled" jobs.

Since *sandboxed* workers run the processor in a different process than the bookkeeping code, they will not result in stalled jobs as easily as standard workers. Make sure that you keep your concurrency factor within sane numbers for this not to happen.

In order to use a sandboxed processor, define the processor in a separate file:

```typescript
import { SandboxedJob } from 'bullmq';

module.exports = async (job: SandboxedJob) => {
    // Do something with job
};
```

and pass its path to the worker constructor:

```typescript
import { Worker } from 'bullmq'

const processorFile = path.join(__dirname, 'my_procesor.js');
worker = new Worker(queueName, processorFile);
```

A tutorial with code examples on how to use sandboxed processors using Typescript can be found [here](https://blog.taskforce.sh/using-typescript-with-bullmq/).

### URL Support

Processors can be defined using URL instances:

```typescript
import { pathToFileURL } from 'url';

const processorUrl = pathToFileURL(__dirname + '/my_procesor.js');

worker = new Worker(queueName, processorUrl);
```

{% hint style="warning" %}
Recommended for Windows OS.
{% endhint %}

### Worker Threads

The default mechanism for launching sandboxed workers is using Node's spawn process library. From BullMQ version v3.13.0, it is also possible to launch the workers using Node's new Worker Threads library. These threads are supposed to be less resource-demanding than the previous approach, however, they are still not as lightweight as we could expect since Node's runtime needs to be duplicated by every thread.

In order to enable worker threads support use the `useWorkerThreads` option when defining an external processor file:

```typescript
import { Worker } from 'bullmq'

const processorFile = path.join(__dirname, 'my_procesor.js');
worker = new Worker(queueName, processorFile, { useWorkerThreads: true });
```

## Read more:

* 💡 [Worker API Reference](https://api.docs.bullmq.io/classes/v5.Worker.html)


# Pausing queues

BullMQ supports pausing queues *globally* or *locally*. When a queue is paused *globally* no workers will pick up any jobs from the queue. When you pause a queue, the workers that are currently busy processing a job will continue working on that job until it completes (or fails), and then will keep idling until the queue is unpaused.

Pausing a queue is performed by calling the ***`pause`*** method on a [queue](https://api.docs.bullmq.io/classes/v5.Queue.html) instance:

```typescript
await myQueue.pause();
```

It is also possible to *locally* pause a given worker instance. This pause works in a similar way as the global pause in the sense that the worker will conclude processing the jobs it has already started but will not process any new ones:

```typescript
await myWorker.pause();
```

The call above will wait for all the jobs currently being processed by this worker to complete (or fail). If you do not want to wait for current jobs to complete before the call completes you can pass `true` to pause the worker **ignoring any running jobs**:

```typescript
await myWorker.pause(true);
```

## Read more:

* 💡 [Pause Queue API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#pause)
* 💡 [Pause Worker API Reference](https://api.docs.bullmq.io/classes/v5.Worker.html#pause)


# Jobs

Queues can hold different types of jobs, which determine how and when they are processed. In this section, we will describe them in detail.

An important thing to consider is that you can mix the different job types in the same queue, so you can add FIFO jobs, and at any moment add a LIFO or a delayed job.

## Read more:

* 💡 [Job API Reference](https://api.docs.bullmq.io/classes/v5.Job.html)


# FIFO

First-In, First-Out

The first type of job we are going to describe is the FIFO (*First-In, First-Out*) type. This is the standard type when adding jobs to a queue. The jobs are processed in the same order as they are inserted into the queue.

This order is preserved independently on the number of processors you have; however, if you have more than one worker or a concurrency factor larger than 1, even though the workers will start the jobs in order, they may be completed in a slightly different order, since some jobs may take more time to complete than others.

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('Paint');

// Add a job that will be processed after all others
await myQueue.add('wall', { color: 'pink' });
```

When you add jobs to the queue there are several options that you can use. For example, you can specify how many jobs you want to keep when the jobs are completed or failed:

```typescript
await myQueue.add(
  'wall',
  { color: 'pink' },
  { removeOnComplete: true, removeOnFail: 1000 },
);
```

In the example above all completed jobs will be removed automatically and the last 1000 failed will be kept in the queue.

## Default job options

Quite often, you will want to provide the same job options to all the jobs that you add to the queue. In this case, you can use the `defaultJobOptions` option when instantiating the `Queue` class:

```typescript
const queue = new Queue('Paint', { defaultJobOptions: {
  removeOnComplete: true, removeOnFail: 1000
});
```

## Read more:

* 💡 [Add Job API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#add)


# LIFO

Last-in, First Out

In some cases, it is useful to process jobs in a LIFO (*Last-in, First-Out*) fashion. This means that the newest jobs added to the queue will be processed **before** the older ones.

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('Paint');

// Add a job that will be processed before all others
await myQueue.add('wall', { color: 'pink' }, { lifo: true });
```


# Job Ids

All jobs in BullMQ need to have a unique job id. This id is used to construct a key to store the data in Redis, and as a pointer to the job as it is moved between the different states it can be in during its lifetime.

By default, job ids are generated automatically as an increasing counter, however it is also possible to specify a *custom id*.

{% hint style="info" %}
The uniqueness requirement is scoped by queue, i.e. you can have the same job id in different queues without any issues. The counter for automatically generated ids is also scoped by queue.
{% endhint %}

The main reason to be able to specify a custom id is in cases when you want to avoid duplicated jobs. Since ids must be unique, if you add a job with an existing id then that job will just be ignored and not added to the queue at all.

{% hint style="danger" %}
Jobs that are removed from the queue (either manually, or when using settings such as `removeOnComplete`/`removeOnFailed`) will **not** be considered as duplicates, meaning that you can add the same job id many times over as long as the previous job has already been removed from the queue.
{% endhint %}

In order to specify a custom job id, use the `jobId` option when adding jobs to the queue:

```typescript
await myQueue.add(
  'wall',
  { color: 'pink' },
  {
    jobId: customJobId,
  },
);
```

{% hint style="danger" %}
Custom job ids must not contain the **:** separator as it will be translated in 2 different values, since we are also following Redis naming convention. So if you need to add a separator, use a different value, for example **-**, **\_**.
{% endhint %}

## Read more:

* 💡 [Duplicated Event Reference](https://api.docs.bullmq.io/interfaces/v5.QueueEventsListener.html#duplicated)


# Job Data

Every job can have its own custom data. The data is stored in the **`data`** attribute of the job:

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('paint');

const job = await myQueue.add('wall', { color: 'red' });

job.data; // { color: 'red' }
```

{% endtab %}

{% tab title="Python" %}

```python
from bullmq import Queue

queue = Queue('paint')

job = await queue.add('wall', {'color': 'red'})

job.data # { color: 'red' }
```

{% endtab %}
{% endtabs %}

## Update data

If you want to change the data after inserting a job, just use the **`updateData`** method. For example:

{% tabs %}
{% tab title="TypeScript" %}

```typescript
const job = await Job.create(queue, 'wall', { color: 'red' });

await job.updateData({
  color: 'blue',
});

job.data; // { color: 'blue' }
```

{% endtab %}

{% tab title="Python" %}

```python
from bullmq import Queue

queue = Queue('paint')

job = await queue.add('wall', {'color': 'red'})

await job.updateData({'color': 'blue'})
job.data # { color: 'blue' }
```

{% endtab %}
{% endtabs %}

## Read more:

* 💡 [Update Data API Reference](https://api.docs.bullmq.io/classes/v5.Job.html#updatedata)


# Deduplication

Deduplication in BullMQ is a process where job execution is delayed and deduplicated based on specific identifiers. It ensures that within a specified period, or until a specific job is completed or failed, no new jobs with the same identifier will be added to the queue. Instead, these attempts will trigger a deduplicated event.

## Simple Mode

The Simple Mode extends the deduplication duration until the job's completion or failure. This means that as long as the job remains in an incomplete state (neither succeeded nor failed), any subsequent job with the same deduplication ID will be ignored.

```typescript
// Add a job that will be deduplicated as this record is not finished (completed or failed).
await myQueue.add(
  'house',
  { color: 'white' },
  { deduplication: { id: 'customValue' } },
);
```

While this job is not moved to completed or failed state, next jobs added with same **deduplication id** will be ignored and a *deduplicated* event will be triggered by our QueueEvent class.

This mode is particularly useful for jobs that have a long running time or those that must not be duplicated until they are resolved, such as processing a file upload or performing a critical update that should not be repeated if the initial attempt is still in progress.

## Throttle Mode

In the Throttle Mode, deduplication works by assigning a delay (Time to Live, TTL) to a job upon its creation. If a similar job (identified by a unique deduplication ID) is added during this delay period, it is ignored. This prevents the queue from being overwhelmed with multiple instances of the same task, thus optimizing the processing time and resource utilization.

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('Paint');

// Add a job that will be deduplicated for 5 seconds.
await myQueue.add(
  'house',
  { color: 'white' },
  { deduplication: { id: 'customValue', ttl: 5000 } },
);
```

In this example, after adding the house painting job with the deduplicated parameters (id and ttl), any subsequent job with the same deduplication ID customValue added within 5 seconds will be ignored. This is useful for scenarios where rapid, repetitive requests are made, such as multiple users or processes attempting to trigger the same job.

## Debounce Mode

Debounce Mode can be achieved by delaying a job upon creation while providing a matching TTL as well as having extend and replace options set as true. Debounce is achieved because if another job with the same deduplication ID is added during this delay (and TTL period) it will replace the previous job with the new one, as well as reseting the TTL, thus ensuring that only the most recent job is kept. This mechanism avoids flooding the queue with duplicates while maintaining the latest job's data.

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('Paint');

const worker = new Worker('Paint', async () => {});

worker.once('completed', job => {
  // only one instance is completed and
  // 9 additions were ignored
  console.log(job.data.color); // `white 10`
});

// Add 10 jobs with deduplication option in debounce mode.
for (let i = 1; i < 11; i++) {
  await myQueue.add(
    'house1',
    { color: `white ${i}` },
    {
      deduplication: {
        id: 'customValue',
        ttl: 5000,
        extend: true,
        replace: true,
      },
      delay: 5000,
    },
  );
}
```

In this example, after adding the house painting job with the deduplicated parameters (id, ttl and replace) and 5 seconds as delay, any subsequent job with the same deduplication options added within 5 seconds will replace previous job information. This is useful for scenarios where rapid, repetitive requests are made, such as multiple users or processes attempting to trigger the same job but with different payloads, this way you will get the last updated data when processing a job.

Note that you must provide a deduplication id that should represent your job. You can hash your entire job data or a subset of attributes for creating this identifier.

{% hint style="warning" %}
Any manual deletion will disable the deduplication. For example, when calling *job.remove* method.
{% endhint %}

## The Deduplicated Event

The **deduplicated** event is emitted whenever a job is deduplicated (ignored or replaced) due to deduplication in Simple Mode, Throttle Mode, or Debounce Mode. This event allows you to monitor deduplication activity and take action if needed, such as logging the occurrence or notifying a user that their request was ignored.

### Listening for the Deduplicated Event

To listen for the **deduplicated** event, use the `QueueEvents` class from BullMQ:

```typescript
import { QueueEvents } from 'bullmq';

const queueEvents = new QueueEvents('myQueue');

queueEvents.on(
  'deduplicated',
  ({ jobId, deduplicationId, deduplicatedJobId }, id) => {
    console.log(`Job ${deduplicatedJobId} was deduplicated due to existing job ${jobId} 
  with deduplication ID ${deduplicationId}`);
  },
);
```

In this example:

* `jobId`: The Id of the job that will be retained in the queue.
* `deduplicationId`: The deduplication Id that caused the deduplication.
* `deduplicatedJobId`: The Id of the job that was deduplicated (ignored or replaced).

## Get Deduplication Job Id

If you need to know the id of the job that started the deduplicated state, you can call the **getDeduplicationJobId** method.

```typescript
const jobId = await myQueue.getDeduplicationJobId('customValue');
```

## Remove Deduplication Key

If you need to stop deduplication before ttl finishes or before finishing a job, you can call the **queue.removeDeduplicationKey** method.

```typescript
await myQueue.removeDeduplicationKey('customValue');
```

Or if you want to stop deduplication only if a specific job is the one that caused the deduplication

```typescript
const isDeduplicatedKeyRemoved = await job.removeDeduplicationKey();
```

## Read more:

* 💡 [Add Job API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#add)
* 💡 [Queue Remove Deduplication Key API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#removededuplicationkey)
* 💡 [Job Remove Deduplication Key API Reference](https://api.docs.bullmq.io/classes/v5.Job.html#removededuplicationkey)
* 💡 [Deduplication Patterns](https://docs.bullmq.io/patterns/deduplication)


# Delayed

Delayed jobs are a special type of job that is placed into a special "delayed set", instead of being processed as fast as possible. After the delay time has passed, the job is processed as a regular job.

In order to add delayed jobs to the queue, use the `delay` option with the amount of time (in milliseconds) that you want to delay the job with.

Note that it is not guaranteed that the job will be processed at the *exact* delayed time specified, as it depends on how busy the workers are when the time has passed, and how many other delayed jobs are scheduled at that exact time. In practice, however, the delay time is quite accurate in most cases.

This is an example of how to add delayed jobs to a queue:

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('Paint');

// Add a job that will be delayed by at least 5 seconds.
await myQueue.add('house', { color: 'white' }, { delay: 5000 });
```

If you want to process the job after a specific point in time, just add the time remaining to that point in time. For example, let's say you want to process the job on the third of July 2035 at 10:30:

```typescript
const targetTime = new Date('03-07-2035 10:30');
const delay = Number(targetTime) - Number(new Date());

await myQueue.add('house', { color: 'white' }, { delay });
```

## Change delay

If you want to reschedule a delayed job *after* inserting it, use the **`changeDelay`** method. This method reschedules the job to execute after the specified number of milliseconds from the current time, regardless of the original delay. For example:

```typescript
const job = await Job.create(queue, 'test', { foo: 'bar' }, { delay: 2000 });

// Reschedule the job to execute 4000ms (4 seconds) from now
await job.changeDelay(4000);
```

{% hint style="warning" %}
Only jobs currently in the **delayed** state can have their delay changed.
{% endhint %}

## Read more:

* 💡 [Change Delay API Reference](https://api.docs.bullmq.io/classes/v5.Job.html#changedelay)


# Repeatable

{% hint style="danger" %}
Note: from BullMQ version 5.16.0 and onwards, we have deprecated these APIs in favor of ["Job Schedulers"](https://docs.bullmq.io/guide/job-schedulers), which provide a more cohesive and more robust API for handling repeatable jobs.
{% endhint %}

There is a special type of *meta* job called **repeatable**. These jobs are special in the sense that even though you only add one job to the queue, they will keep repeating according to a predefined schedule.

Adding a job with the `repeat` option set will actually do two things immediately: create a Repeatable Job configuration, and schedule a regular delayed job for the job's first run. This first run will be scheduled "on the hour", that is if you create a job that repeats every 15 minutes at 4:07, the job will first run at 4:15, then 4:30, and so on.

The Repeatable Job configuration is not a job, so it will not show up in methods like `getJobs()`. To manage Repeatable Job configurations, use [`getRepeatableJobs()`](https://api.docs.bullmq.io/classes/v5.Queue.html#getrepeatablejobs) and similar. This also means repeated jobs do **not** participate in evaluating `jobId` uniqueness - that is, a non-repeatable job can have the same `jobId` as a Repeatable Job configuration, and two Repeatable Job configurations can have the same `jobId` as long as they have different repeat options.

Every time a repeatable job is picked up for processing, the next repeatable job is added to the queue with a proper delay. Repeatable jobs are thus nothing more than delayed jobs that are added to the queue according to some settings.

{% hint style="info" %}
As Repeatable jobs are just delayed jobs, prior to BullMQ 2.0 you also need a `QueueScheduler` instance to schedule the jobs accordingly.

However, from BullMQ 2.0 onwards, the `QueueScheduler` is not needed anymore.
{% endhint %}

There are two ways to specify a repeatable's job repetition pattern, either with a cron expression (using [cron-parser](https://www.npmjs.com/package/cron-parser)'s "unix cron w/ optional seconds" format), or specifying a fixed amount of milliseconds between repetitions.

```typescript
import { Queue, QueueScheduler } from 'bullmq';

const myQueueScheduler = new QueueScheduler('Paint');
const myQueue = new Queue('Paint');

// Repeat job once every day at 3:15 (am)
await myQueue.add(
  'submarine',
  { color: 'yellow' },
  {
    repeat: {
      pattern: '0 15 3 * * *',
    },
  },
);

// Repeat job every 10 seconds but no more than 100 times
await myQueue.add(
  'bird',
  { color: 'bird' },
  {
    repeat: {
      every: 10000,
      limit: 100,
    },
  },
);
```

There are some important considerations regarding repeatable jobs:

* Bull is smart enough not to add the same repeatable job if the repeat options are the same.
* If there are no workers running, repeatable jobs will not accumulate next time a worker is online.
* Repeatable jobs can be removed using the [`removeRepeatable`](https://api.docs.bullmq.io/classes/v5.Queue.html#removerepeatable) or [`removeRepeatableByKey`](https://api.docs.bullmq.io/classes/v5.Queue.html#removerepeatablebykey) methods.

```typescript
import { Queue } from 'bullmq';

const repeat = { pattern: '*/1 * * * * *' };

const myQueue = new Queue('Paint');

const job1 = await myQueue.add('red', { foo: 'bar' }, { repeat });
const job2 = await myQueue.add('blue', { foo: 'baz' }, { repeat });

const isRemoved1 = await myQueue.removeRepeatableByKey(job1.repeatJobKey);
const isRemoved2 = await queue.removeRepeatable('blue', repeat);
```

All repeatable jobs have a repeatable job key that holds some metadata of the repeatable job itself. It is possible to retrieve all the current repeatable jobs in the queue calling [`getRepeatableJobs`](https://api.docs.bullmq.io/classes/v5.Queue.html#getrepeatablejobs):

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('Paint');

const repeatableJobs = await myQueue.getRepeatableJobs();
```

The standard `jobId` option does not work the same as with regular jobs. Because repeatable jobs are *delayed* jobs, and the repetition is achieved by generating a new delayed job precisely before the current job starts processing, the jobs require unique ids to avoid being considered duplicates. Therefore, with repeatable jobs, the `jobId` option is used to *generate* the unique ids (rather than itself being the unique id). For instance, if you have two repeatable jobs with the same name and options, you could use distinct `jobId`s to differentiate them:

```typescript
import { Queue, QueueScheduler } from 'bullmq';

const myQueueScheduler = new QueueScheduler('Paint');
const myQueue = new Queue('Paint');

// Repeat job every 10 seconds but no more than 100 times
await myQueue.add(
  'bird',
  { color: 'bird' },
  {
    repeat: {
      every: 10000,
      limit: 100,
    },
    jobId: 'colibri',
  },
);

await myQueue.add(
  'bird',
  { color: 'bird' },
  {
    repeat: {
      every: 10000,
      limit: 100,
    },
    jobId: 'pigeon',
  },
);
```

### Slow repeatable jobs

It is worth mentioning the case where the repeatable frequency is greater than the time it takes to process a job.

For instance, let's say that you have a job that is repeated every second, but the process of the job itself takes 5 seconds. As explained above, repeatable jobs are just delayed jobs, so this means that the next repeatable job will be added as soon as the next job is starting to be processed.

In this particular example, the worker will pick up the next job and also add the next repeatable job delayed 1 second since that is the repeatable interval. The worker will require 5 seconds to process the job, and if there is only 1 worker available then the next job will need to wait a full 5 seconds before it can be processed.

On the other hand, if there were 5 workers available, then they will most likely be able to process all the repeatable jobs with the desired frequency of one job per second.

### Repeat Strategy

By default, we are using [cron-parser](https://www.npmjs.com/package/cron-parser) in the default repeat strategy for cron expressions.

It is possible to define a different strategy to schedule repeatable jobs. For example we can create a custom one for RRULE:

```typescript
import { Queue, QueueScheduler, Worker } from 'bullmq';
import { rrulestr } from 'rrule';

const settings = {
  repeatStrategy: (millis, opts) => {
    const currentDate =
      opts.startDate && new Date(opts.startDate) > new Date(millis)
        ? new Date(opts.startDate)
        : new Date(millis);
    const rrule = rrulestr(opts.pattern);
    if (rrule.origOptions.count && !rrule.origOptions.dtstart) {
      throw new Error('DTSTART must be defined to use COUNT with rrule');
    }

    const next_occurrence = rrule.after(currentDate, false);
    return next_occurrence?.getTime();
  },
};

const myQueueScheduler = new QueueScheduler('Paint');
const myQueue = new Queue('Paint', { settings });

// Repeat job every 10 seconds
await myQueue.add(
  'bird',
  { color: 'green' },
  {
    repeat: {
      pattern: 'RRULE:FREQ=SECONDLY;INTERVAL=;WKST=MO',
    },
    jobId: 'colibri',
  },
);

await myQueue.add(
  'bird',
  { color: 'gray' },
  {
    repeat: {
      pattern: 'RRULE:FREQ=SECONDLY;INTERVAL=;WKST=MO',
    },
    jobId: 'pigeon',
  },
);

const worker = new Worker(
  'Paint',
  async () => {
    doSomething();
  },
  { settings },
);
```

{% hint style="warning" %}
As you may notice, the repeat strategy setting should be provided in `Queue` and `Worker` classes. The reason we need in **both** places is because the first time we add the job to the `Queue` we need to calculate when is the next iteration, but after that the `Worker` takes over and we use the worker settings.
{% endhint %}

{% hint style="info" %}
The repeat strategy function receives an optional `jobName` third parameter.
{% endhint %}

### Custom Repeatable Key

By default, we are generating repeatable keys base on repeat options and job name.

In some cases, it is desired to pass a custom key to be able to differentiate your repeatable jobs even when they have same repeat options:

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('Paint', { connection });

// Repeat job every 10 seconds
await myQueue.add(
  'bird',
  { color: 'gray' },
  {
    repeat: {
      every: 10_000,
      key: 'colibri',
    },
  },
);

// Repeat job every 10 seconds
await myQueue.add(
  'bird',
  { color: 'brown' },
  {
    repeat: {
      every: 10_000,
      key: 'eagle',
    },
  },
);
```

#### Updating repeatable job's options

Using custom keys allows to update existing repeatable jobs by just adding a new repeatable job using the same key, so for instance, if we wanted to change the repetition interval of the previous job that used the key "eagle" we could just a new job like this:

```typescript
// Repeat job every 25 seconds instead of 10 seconds
await myQueue.add(
  'bird',
  { color: 'turquoise' },
  {
    repeat: {
      every: 25_000,
      key: 'eagle',
    },
  },
);
```

The code above will not create a new repeatable meta job, it will just update the existing meta job's interval from 10 seconds to 25 seconds. Note that if there is already a job delayed for running within the 10 seconds it will be replaced by a new job using the new repeatable job's settings.

### Read more:

* 💡 [Repeat Strategy API Reference](https://api.docs.bullmq.io/types/v5.RepeatStrategy.html)
* 💡 [Remove Repeatable Job API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#removerepeatable)
* 💡 [Remove Repeatable Job by Key API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#removerepeatablebykey)


# Prioritized

Jobs can also include a `priority` option. Using priorities, job processing order will be affected by the specified `priority` instead of following a FIFO or LIFO pattern.

{% hint style="warning" %}
Adding prioritized jobs is a slower operation than the other types of jobs, with a complexity `O(log(n))` relative to the number of jobs in the prioritized set in the queue.
{% endhint %}

Note that the priorities go from `1` to `2 097 152`, where a lower number is always a **higher** priority than higher numbers.

{% hint style="danger" %}
Jobs without a `priority` assigned will get the highest priority, being processed before jobs with priorities assigned to them.
{% endhint %}

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('Paint');

await myQueue.add('wall', { color: 'pink' }, { priority: 10 });
await myQueue.add('wall', { color: 'brown' }, { priority: 5 });
await myQueue.add('wall', { color: 'blue' }, { priority: 7 });

// The wall will be painted first brown, then blue and
// finally pink.
```

If several jobs are added with the same priority value, then the jobs within that priority will be processed in [FIFO (*First in, first out*)](https://docs.bullmq.io/guide/jobs/fifo) fashion.

## Change priority

If you want to change the `priority` after inserting a job, use the **`changePriority`** method. For example, let's say that you want to change the `priority` from `16` to `1`:

```typescript
const job = await Job.create(queue, 'test2', { foo: 'bar' }, { priority: 16 });

await job.changePriority({
  priority: 1,
});
```

or if you want to use the [LIFO (*Last In, First Out*)](https://docs.bullmq.io/guide/jobs/lifo) option:

```typescript
const job = await Job.create(queue, 'test2', { foo: 'bar' }, { priority: 16 });

await job.changePriority({
  lifo: true,
});
```

## Get Prioritized jobs

As prioritized is a new state. You must use **`getJobs`** or **`getPrioritized`** method as:

```typescript
const jobs = await queue.getJobs(['prioritized']);

const jobs2 = await queue.getPrioritized();
```

## Get Counts per Priority

If you want to get the `count` of jobs in `prioritized` status (priorities higher than 0) or in `waiting` status (priority 0), use the **`getCountsPerPriority`** method. For example, let's say that you want to get counts for `priority` `1` and `0`:

```typescript
const counts = await queue.getCountsPerPriority([1, 0]);
/*
{
  '1': 11,
  '0': 10
}
*/
```

## Read more:

* 📋 [Faster Priority jobs](https://bullmq.io/news/062123/faster-priority-jobs/)
* 💡 [Change Priority API Reference](https://api.docs.bullmq.io/classes/v5.Job.html#changepriority)
* 💡 [Get Prioritized API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#getprioritized)
* 💡 [Get Counts per Priority API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#getcountsperpriority)


# Removing jobs

Sometimes it is necessary to remove a job. For example, there could be a job that has bad data.

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import { Queue } from 'bullmq';

const queue = new Queue('paint');

const job = await queue.add('wall', { color: 1 });

await job.remove();
```

{% endtab %}

{% tab title="Python" %}

```python
from bullmq import Queue

queue = Queue('paint')

job = await queue.add('wall', {'color': 1})

await job.remove()
```

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Locked jobs (in active state) can not be removed. An error will be thrown.
{% endhint %}

## Having a parent job

There are 2 possible cases:

1. There are not pending dependencies; in this case the parent is moved to wait status, we may try to process this job.
2. There are pending dependencies; in this case the parent is kept in waiting-children status.

{% hint style="info" %}
Take into consideration that processed values will be kept in processed `hset` from the parent if this child is in **completed** state at the time when it's removed.
{% endhint %}

## Having pending dependencies

We may try to remove all its pending descendants first.

{% hint style="warning" %}
If any of the children are locked, the deletion process will be stopped.
{% endhint %}

### Read more:

* 💡 [Remove API Reference](https://api.docs.bullmq.io/classes/v5.Job.html#remove)


# Retrying jobs

BullMQ provides a `retry` method that allows you to programmatically retry jobs that have already completed or failed. This is different from the automatic retry mechanism (configured via the `attempts` option) - the `retry` method lets you manually move a job back to the waiting queue at any time.

## When to use Job.retry()

The `retry` method is useful in scenarios such as:

* **Manual intervention**: When a job failed due to a temporary external issue that has been resolved
* **Re-processing completed jobs**: When you need to run a completed job again with the same data
* **Workflow recovery**: When recovering from system failures or bugs that caused jobs to fail incorrectly

{% hint style="info" %}
Only jobs in the `completed` or `failed` state can be retried. Active, waiting, or delayed jobs cannot be retried.
{% endhint %}

## Basic Usage

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import { Queue, Job } from 'bullmq';

const queue = new Queue('my-queue');

// Get a failed job by ID
const job = await Job.fromId(queue, 'job-id');

// Retry a failed job (default state is 'failed')
await job.retry();

// Retry a completed job
await job.retry('completed');
```

{% endtab %}

{% tab title="Python" %}

```python
from bullmq import Queue, Job

queue = Queue('my-queue')

# Get a failed job by ID
job = await Job.fromId(queue, 'job-id')

# Retry a failed job (default state is 'failed')
await job.retry()

# Retry a completed job
await job.retry('completed')

await queue.close()
```

{% endtab %}

{% tab title="Elixir" %}

```elixir
# Get a job reference (must have connection set)
job = %Job{id: "job-id", queue_name: "my-queue", prefix: "bull", connection: conn}

# Retry a failed job (default state is :failed)
{:ok, updated_job} = Job.retry(job)

# Retry a completed job
{:ok, updated_job} = Job.retry(job, :completed)
```

{% endtab %}
{% endtabs %}

## Retry Options

The `retry` method accepts options to reset attempt counters. This is useful when you want the retried job to behave as if it's being processed for the first time.

### Reset Attempts Made

The `attemptsMade` counter tracks how many times a job has been processed. Resetting it allows the job to use its full retry allowance again.

{% tabs %}
{% tab title="TypeScript" %}

```typescript
// Retry and reset the attempts counter
await job.retry('failed', { resetAttemptsMade: true });
```

{% endtab %}

{% tab title="Python" %}

```python
# Retry and reset the attempts counter
await job.retry('failed', {"resetAttemptsMade": True})
```

{% endtab %}

{% tab title="Elixir" %}

```elixir
# Retry and reset the attempts counter
{:ok, updated_job} = Job.retry(job, :failed, reset_attempts_made: true)
```

{% endtab %}
{% endtabs %}

### Reset Attempts Started

The `attemptsStarted` counter tracks how many times a job has been moved to the active state. This can be useful for tracking purposes.

{% tabs %}
{% tab title="TypeScript" %}

```typescript
// Retry and reset both counters
await job.retry('failed', { 
  resetAttemptsMade: true,
  resetAttemptsStarted: true 
});
```

{% endtab %}

{% tab title="Python" %}

```python
# Retry and reset both counters
await job.retry('failed', {
    "resetAttemptsMade": True,
    "resetAttemptsStarted": True
})
```

{% endtab %}

{% tab title="Elixir" %}

```elixir
# Retry and reset both counters
{:ok, updated_job} = Job.retry(job, :failed, 
  reset_attempts_made: true,
  reset_attempts_started: true
)
```

{% endtab %}
{% endtabs %}

## What happens when you retry

When a job is retried, the following occurs:

1. **Job is moved to waiting queue**: The job is removed from the completed/failed set and added back to the waiting queue
2. **Properties are cleared**: The following job properties are reset:
   * `failedReason` / `failed_reason` → `null` / `nil`
   * `finishedOn` / `finished_on` → `null` / `nil`
   * `processedOn` / `processed_on` → `null` / `nil`
   * `returnvalue` / `return_value` → `null` / `nil`
3. **Events are emitted**: A `waiting` event is emitted when the job is successfully moved
4. **Parent dependencies restored**: If the job is a child in a flow, its dependency relationship with the parent is restored

{% hint style="warning" %}
If you retry a job without resetting `attemptsMade`, and the job has already exhausted its retry attempts, it will fail immediately when processed again.
{% endhint %}

## Error Handling

The `retry` method can fail in the following cases:

| Error Code | Description                             |
| ---------- | --------------------------------------- |
| `-1`       | Job does not exist                      |
| `-3`       | Job was not found in the expected state |

{% tabs %}
{% tab title="TypeScript" %}

```typescript
try {
  await job.retry('failed');
} catch (error) {
  console.error('Failed to retry job:', error.message);
}
```

{% endtab %}

{% tab title="Python" %}

```python
try:
    await job.retry('failed')
except Exception as error:
    print(f'Failed to retry job: {error}')
```

{% endtab %}

{% tab title="Elixir" %}

```elixir
case Job.retry(job, :failed) do
  {:ok, updated_job} ->
    IO.puts("Job retried successfully")
    
  {:error, {:reprocess_failed, -1}} ->
    IO.puts("Job does not exist")
    
  {:error, {:reprocess_failed, -3}} ->
    IO.puts("Job was not in the expected state")
    
  {:error, reason} ->
    IO.puts("Failed to retry: #{inspect(reason)}")
end
```

{% endtab %}
{% endtabs %}

## Read More

* 💡 [Retry API Reference](https://api.docs.bullmq.io/classes/v5.Job.html#retry)
* 💡 [Retrying Failing Jobs](https://docs.bullmq.io/guide/retrying-failing-jobs) - Automatic retry configuration with backoff strategies
* 💡 [Stop Retrying Jobs](https://github.com/taskforcesh/bullmq/blob/master/docs/gitbook/guide/patterns/stop-retrying-jobs.md) - How to prevent further retries


# Stalled

{% hint style="danger" %}
From BullMQ 2.0 and onwards, the `QueueScheduler` is not needed anymore. For manually fetching jobs check this [pattern](https://docs.bullmq.io/patterns/manually-fetching-jobs#checking-for-stalled-jobs)
{% endhint %}

When a job is in an active state (i.e. it is being processed by a worker), it needs to continuously update the queue to notify that the worker is still working on the job. This mechanism prevents a worker that crashes or enters an endless loop from keeping a job in an active state forever.

When a worker is not able to notify the queue that it is still working on a given job, that job is moved back to the waiting list, or to the failed set. We then say that the job has stalled and the queue will emit the 'stalled' event.

{% hint style="info" %}
There is not a 'stalled' state, only a 'stalled' event emitted when a job is automatically moved from *active* to *waiting* state.
{% endhint %}

If a job stalls more than a predefined limit (see the [`maxStalledCount` option](https://api.docs.bullmq.io/interfaces/v5.WorkerOptions.html#maxstalledcount)), the job will be failed permanently with the error "*job stalled more than allowable limit*". The default is 1, as stalled jobs should be a rare occurrence, but you can increase this number if needed.

In order to avoid stalled jobs, make sure that your worker does not keep the Node.js event loop too busy. The default max stalled check duration is 30 seconds, so as long as you do not perform CPU operations exceeding that value you should not get stalled jobs.

Another way to reduce the chance of stalled jobs is using so-called "sandboxed" processors. In this case, the workers will spawn new separate Node.js processes, running separately from the main process.

{% code title="main.ts" %}

```typescript
import { Worker } from 'bullmq';

const worker = new Worker('Paint', painter);
```

{% endcode %}

{% code title="painter.ts" %}

```typescript
export default = (job) => {
    // Paint something
}
```

{% endcode %}

## Read more:

* 💡 [Queue Scheduler API Reference](https://api.docs.bullmq.io/classes/v1.QueueScheduler.html)


# Getters

When jobs are added to a queue, they will be in different statuses during their lifetime. BullMQ provides methods to retrieve information and jobs from the different statuses.

<figure><img src="https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-8ccf86e0633ddb1016f5f56af5dbe0decc412aa3%2Fsimple-architecture.png?alt=media" alt="Diagram of the lifecycle of a BullMQ job in the queue"><figcaption><p>Lifecycle of a job</p></figcaption></figure>

#### Job Counts

It is often necessary to know how many jobs are in a given status:

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('Paint');

const counts = await myQueue.getJobCounts('wait', 'completed', 'failed');

// Returns an object like this { wait: number, completed: number, failed: number }
```

{% endtab %}

{% tab title="Python" %}

```python
from bullmq import Queue

myQueue = Queue('Paint')

counts = await myQueue.getJobCounts('wait', 'completed', 'failed')

# Returns an object like this { wait: number, completed: number, failed: number }
```

{% endtab %}
{% endtabs %}

The available status are:

* *completed*,
* *failed*,
* *delayed*,
* *active*,
* *wait*,
* *waiting-children*,
* *prioritized*,
* *paused*, and
* *repeat*.

#### Get Jobs

It is also possible to retrieve the jobs with pagination style semantics. For example:

{% tabs %}
{% tab title="TypeScript" %}

```typescript
const completed = await myQueue.getJobs(['completed'], 0, 100, true);

// returns the oldest 100 jobs
```

{% endtab %}

{% tab title="Python" %}

```python
completed = await myQueue.getJobs(['completed'], 0, 100, True)

# returns the oldest 100 jobs
```

{% endtab %}
{% endtabs %}

## Read more:

* 💡 [Get Job Counts API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#getjobcounts)
* 💡 [Get Jobs API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#getjobs)


# Job Schedulers

Job Schedulers replace "repeatable jobs", and are available in v5.16.0 and onwards

A Job Scheduler acts as a factory , producing jobs based on specified "repeat" settings. The Job Scheduler is highly flexible, accommodating various scenarios, including jobs produced at fixed intervals, according to cron expressions, or based on custom requirements. For historical reasons, jobs produced by the Job Scheduler are often referred to as ‘Repeatable Jobs’.

To create a scheduler, simply use the "upsertJobScheduler" method as demonstrated in the following example:

```typescript
// Creates a new Job Scheduler that generates a job every 1000 milliseconds (1 second)
const firstJob = await queue.upsertJobScheduler('my-scheduler-id', {
  every: 1000,
});
```

This example will create a new Job Scheduler that will produce a new job every second. It will also return the first job created for this Job Scheduler, which will be in "delayed" status waiting to be processed after 1 second.

Now there are also a few important considerations that need to be explained here.:

* **Upsert vs. Add:** the 'upsert' is used instead of 'add' to simplify management of recurring jobs, especially in production deployments. It ensures the scheduler is updated or created without duplications.
* **Job Production Rate:** The scheduler will only generate new jobs when the last job begins processing. Therefore, if your queue is very busy, or if you do not have enough workers or concurrency, it is possible that you will get the jobs less frequently than the specified repetition interval.
* **Job Status:** As long as a Job Scheduler is producing jobs, there will be always one job associated to the scheduler in the "Delayed" status.

### Using Job Templates

You can also define a template with standard names, data, and options for jobs added to a queue. This ensures that all jobs produced by the Job Scheduler inherit these settings:

```typescript
// Create jobs every day at 3:15 (am)
const firstJob = await queue.upsertJobScheduler(
  'my-scheduler-id',
  { pattern: '0 15 3 * * *' },
  {
    name: 'my-job-name',
    data: { foo: 'bar' },
    opts: {
      backoff: 3,
      attempts: 5,
      removeOnFail: 1000,
    },
  },
);
```

All jobs produced by this scheduler will use the given settings. Note that in the future you could call "upsertJobScheduler" again with the given "my-scheduler-id" in order to update any settings of this particular job scheduler, such as the repeat options or/and the job's template settings.

{% hint style="info" %}
Since jobs produced by the Job Scheduler will get a special job ID in order to guarantee that jobs will never be created more often than the given repeat settings, you cannot choose a custom job id. However you can use the job's name if you need to discriminate these jobs from other jobs.
{% endhint %}

## Read more:

* 💡 [Upsert Job Scheduler API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#upsertjobscheduler)


# Repeat Strategies

BullMQ comes with two predefined strategies for creating repeatable jobs. The ‘every’ strategy is straightforward, allowing you to schedule jobs to repeat at specific intervals, measured in seconds. The more complex ‘cron’ strategy uses cron expressions, as defined by the [cron-parser](https://www.npmjs.com/package/cron-parser) to schedule jobs in intricate patterns. Additionally, BullMQ lets you create custom strategies, giving you the flexibility to define your own logic for setting job intervals.

### "Every" strategy

The every strategy is used when we simply want to produce repeatable jobs at specific intervals:

```typescript
const { Queue, Worker } = require('bullmq');

const connection = {
  host: 'localhost',
  port: 6379,
};

const myQueue = new Queue('my-repeatable-jobs', { connection });

// Upserting a repeatable job in the queue
await myQueue.upsertJobScheduler(
  'repeat-every-10s',
  {
    every: 10000, // Job will repeat every 10000 milliseconds (10 seconds)
  },
  {
    name: 'every-job',
    data: { jobData: 'data' },
    opts: {}, // Optional additional job options
  },
);

// Worker to process the jobs
const worker = new Worker(
  'my-repeatable-jobs',
  async job => {
    console.log(`Processing job ${job.id} with data: ${job.data.jobData}`);
  },
  { connection },
);
```

### "Cron" strategy

The “cron” strategy in BullMQ leverages the [cron-parser](https://www.npmjs.com/package/cron-parser) library to use cron expressions for scheduling jobs with greater specificity. This approach is ideal for jobs requiring execution at precise times or intervals, such as automated reports or maintenance tasks.

Below is the supported format for cron expressions in cron-parser:

```
*    *    *    *    *    *
┬    ┬    ┬    ┬    ┬    ┬
│    │    │    │    │    │
│    │    │    │    │    └ day of week (0 - 7, 1L - 7L, where 0 or 7 is Sunday)
│    │    │    │    └───── month (1 - 12)
│    │    │    └────────── day of month (1 - 31, L for the last day of the month)
│    │    └─────────────── hour (0 - 23)
│    └──────────────────── minute (0 - 59)
└───────────────────────── second (0 - 59, optional)
```

This format includes the optional second field, which is not typically available in standard cron schedules, allowing for even more precise scheduling.

Cron expressions are quite powerful as in they support seemless handling timezone differences and daylight saving time transitions, crucial for tasks that depend on local times. And also because of the use of special characters to denote specific days or things like the last day of the month, providing flexibility for monthly and weekly tasks.

If you are new to Cron expressions, [Wikipedia](https://en.wikipedia.org/wiki/Cron) is an excelent starting point to learn how to use them.

Here follows an example that sets up a job to execute at 9:00 AM from Monday to Friday:

```typescript
const { Queue, Worker } = require('bullmq');

const connection = {
  host: 'localhost',
  port: 6379,
};

const myQueue = new Queue('my-cron-jobs', { connection });

// Upserting a job with a cron expression
await myQueue.upsertJobScheduler(
  'weekday-morning-job',
  {
    pattern: '0 0 9 * * 1-5', // Runs at 9:00 AM every Monday to Friday
  },
  {
    name: 'cron-job',
    data: { jobData: 'morning data' },
    opts: {}, // Optional additional job options
  },
);

// Worker to process the jobs
const worker = new Worker(
  'my-cron-jobs',
  async job => {
    console.log(
      `Processing job ${job.id} at ${new Date()} with data: ${
        job.data.jobData
      }`,
    );
  },
  { connection },
);
```

### Custom Strategy

It is possible to define a different strategy to schedule repeatable jobs. The idea is that the repeat strategy, based on a pattern and the latest job's milliseconds, return the next desired timestamp. Although not used in the following example, you could have different behaviours on your repeat strategies based on the current job's name if you want to. However note that **only** **one** repeatStrategy can be defined for a given queue.

For example we can create a custom one for [RRULE](https://jkbrzt.github.io/rrule/) like this:

```typescript
import { Queue, Worker } from 'bullmq';
import { rrulestr } from 'rrule';

const settings = {
  repeatStrategy: (millis: number, opts: RepeatOptions, _jobName: string) => {
    const currentDate =
      opts.startDate && new Date(opts.startDate) > new Date(millis)
        ? new Date(opts.startDate)
        : new Date(millis);

    const rrule = rrulestr(opts.pattern);

    if (rrule.origOptions.count && !rrule.origOptions.dtstart) {
      throw new Error('DTSTART must be defined to use COUNT with rrule');
    }

    const next_occurrence = rrule.after(currentDate, false);
    return next_occurrence?.getTime();
  },
};

const myQueue = new Queue('Paint', { settings });

// Repeat job every 10 seconds
await myQueue.upsertJobScheduler(
  'collibris',
  {
    pattern: 'RRULE:FREQ=SECONDLY;INTERVAL=10;WKST=MO',
  },
  {
    data: { color: 'green' },
  },
);

// Repeat job every 20 seconds
await myQueue.upsertJobScheduler(
  'pingeons',
  {
    pattern: 'RRULE:FREQ=SECONDLY;INTERVAL=20;WKST=MO',
  },
  {
    data: { color: 'gray' },
  },
);

const worker = new Worker(
  'Paint',
  async () => {
    doSomething();
  },
  { settings },
);
```

{% hint style="danger" %}
As you may have noticed, the repeat strategy setting should be provided in **both** the Queue and Worker classes. The reason we need it in both places is that when we first add the job to the Queue, we need to calculate when the next iteration will occur. After that, the Worker takes over, and we use the settings configured in the Worker.
{% endhint %}


# Repeat options

There are some options that can be used on all Job Schedulers, to control some aspects of the repetitions. Lets review them one by one:

#### Start date

This option sets a future date from which the job will start being scheduled. This can be useful for setting up jobs that should begin repeating on a specific day.

```typescript
const { Queue } = require('bullmq');
const connection = { host: 'localhost', port: 6379 };
const myQueue = new Queue('my-dated-jobs', { connection });

await myQueue.upsertJobScheduler(
  'start-later-job',
  {
    every: 60000, // every minute
    startDate: new Date('2024-10-15T00:00:00Z'), // start on October 15, 2024
  },
  {
    name: 'timed-start-job',
    data: { message: 'Starting later' },
  },
);
```

#### End Date

Use this to specify when the job should stop being scheduled, effectively setting an expiration date for the job repetitions.

```typescript
await myQueue.upsertJobScheduler(
  'end-soon-job',
  {
    every: 60000, // every minute
    endDate: new Date('2024-11-01T00:00:00Z'), // end on November 1, 2024
  },
  {
    name: 'timed-end-job',
    data: { message: 'Ending soon' },
  },
);
```

#### Limit

This setting is used to limit the number of times a job will be repeated. When the count reaches this limit, no more jobs will be produced for the given job scheculer.

```typescript
await myQueue.upsertJobScheduler(
  'limited-job',
  {
    every: 10000, // every 10 seconds
    limit: 10, // limit to 10 executions
  },
  {
    name: 'limited-execution-job',
    data: { message: 'Limited runs' },
  },
);
```

#### immediately

This setting forces the job to execute as soon as it is added, regardless of the schedule. This can help in situations where an immediate action is required before entering a regular cycle.

When you use the every option in BullMQ, it schedules jobs based on fixed time intervals, which might seem a bit counterintuitive initially. For instance, if you set an interval of 2000ms, jobs will be triggered at every even second—such as 0, 2, 4, 6, 8 seconds, and so on. This means the scheduling aligns with the clock, regardless of when you actually added the job.

If you need a job to begin processing immediately after you add a job scheduler, regardless of the interval’s alignment with the clock, you can use the immediately setting. This is especially crucial for long intervals. For example, if you set the job to repeat monthly, normally it would wait to start until the first second of the next month. If you add the job mid-month, it would not start until the beginning of the following month. Using immediately ensures the first instance of the job runs as soon as it’s added, bypassing the wait until the scheduled interval begins.

```typescript
await myQueue.upsertJobScheduler(
  'immediate-job',
  {
    every: 86400000, // once a day
    immediately: true, // execute the first one immediately
  },
  {
    name: 'instant-job',
    data: { message: 'Immediate start' },
  },
);
```

{% hint style="danger" %}
From version 5.19.0 and onwards the "immediately" option has been deprecated. The current behaviour is as if "immediately" was always true, in other words, the first repetition will always be immediately for a new inserted job scheduler, and then repeat according to the "every" setting. Subsequent calls to upsertJobScheduler for **existing** schedulers will not lead to immediate repetitions and will instead follow the "every" interval.
{% endhint %}


# Manage Job Schedulers

In BullMQ, managing the lifecycle and inventory of job schedulers is crucial for maintaining efficient and organized background tasks. In addition to the upsertJobScheduler method—which allows for the addition and updating of job schedulers—two other methods play essential roles: removeJobScheduler and getJobSchedulers. These functions enable the removal of schedulers and retrieval of all existing schedulers, respectively, providing comprehensive control over your job scheduling environment.

#### Remove job scheduler

The **removeJobScheduler** method is designed to delete a specific job scheduler from the queue. This is particularly useful when a scheduled task is no longer needed or if you wish to clean up inactive or obsolete schedulers to optimize resource usage.

```typescript
// Remove a job scheduler with ID 'scheduler-123'
const result = await queue.removeJobScheduler('scheduler-123');
console.log(
  result ? 'Scheduler removed successfully' : 'Missing Job Scheduler',
);
```

The method will return true if there was a Job Scheduler to remove with the given ID, or false if there wasn't any.

#### Get Job Schedulers

The **getJobSchedulers** method retrieves a list of all configured job schedulers within a specified range. This is invaluable for monitoring and managing multiple job schedulers, especially in systems where jobs are dynamically scheduled and require frequent reviews or adjustments.

```typescript
// Retrieve the first 10 job schedulers in ascending order of their next execution time
const schedulers = await queue.getJobSchedulers(0, 9, true);
console.log('Current job schedulers:', schedulers);
```

This method can be particularly useful for generating reports or dashboards that provide insights into when jobs are scheduled to run, aiding in system monitoring and troubleshooting.

#### Get Job Scheduler

The **getJobScheduler** method retrieves a job scheduler by id. This is invaluable for inspecting dedicated configurations.

```typescript
const scheduler = await queue.getJobScheduler('test');
console.log('Current job scheduler:', scheduler);
```

## Read more:

* 💡 [Remove Job Scheduler API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#removejobscheduler)
* 💡 [Get Job Schedulers API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#getjobschedulers)
* 💡 [Get Job Scheduler API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#getjobscheduler)


# Flows

BullMQ supports parent - child relationships between jobs. The basic idea is that a parent job will not be moved to the wait status (i.e. where it could be picked up by a worker) until all its children jobs have been processed successfully. Apart from that, a parent or a child job are no different from regular jobs.

This functionality enables the creation of flows where jobs are the node of trees of arbitrary depth.

{% hint style="warning" %}
Flows are added to a queue using the `FlowProducer` class.
{% endhint %}

In order to create "flows" you must use the [`FlowProducer`](https://api.docs.bullmq.io/classes/v5.FlowProducer.html) class. The [***`add`***](https://api.docs.bullmq.io/classes/v5.FlowProducer.html#add) method accepts an object with the following interface:

```typescript
interface FlowJobBase<T> {
  name: string;
  queueName: string;
  data?: any;
  prefix?: string;
  opts?: Omit<T, 'debounce' | 'deduplication' | 'repeat'>;
  children?: FlowChildJob[];
}

type FlowChildJob = FlowJobBase<
  Omit<JobsOptions, 'debounce' | 'deduplication' | 'parent' | 'repeat'>
>;

type FlowJob = FlowJobBase<JobsOptions>;
```

So we can add a flow like this one:

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import { FlowProducer } from 'bullmq';

// A FlowProducer constructor takes an optional "connection"
// object otherwise it connects to a local redis instance.
const flowProducer = new FlowProducer();

const flow = await flowProducer.add({
  name: 'renovate-interior',
  queueName: 'renovate',
  children: [
    { name: 'paint', data: { place: 'ceiling' }, queueName: 'steps' },
    { name: 'paint', data: { place: 'walls' }, queueName: 'steps' },
    { name: 'fix', data: { place: 'floor' }, queueName: 'steps' },
  ],
});
```

{% endtab %}

{% tab title="Python" %}

```python
from bullmq import FlowProducer

# A FlowProducer constructor takes an optional "connection"
# object otherwise it connects to a local redis instance.
flowProducer = FlowProducer()

flow = await flowProducer.add({
  "name": "renovate-interior",
  "queueName": "renovate",
  "children": [
    { "name": "paint", "data": { "place": "ceiling" }, "queueName": "steps" },
    { "name": "paint", "data": { "place": "walls" }, "queueName": "steps" },
    { "name": "fix", "data": { "place": "floor" }, "queueName": "steps" },
  ],
})
```

{% endtab %}
{% endtabs %}

The above code will atomically add 4 jobs: one to the "renovate" queue, and 3 to the "steps" queue. When the 3 jobs in the "steps" queue are completed, the parent job in the "renovate" queue will be processed as a regular job.

The above call will return instances for all the jobs added to the queue.

{% hint style="info" %}
Note that the parent queue does not need to be the same queue as the one used for the children.
{% endhint %}

{% hint style="warning" %}
If a jobId option is provided, make sure that it does not contain a colon **:** as this is considered a separator.
{% endhint %}

When the parent job is processed it is possible to access the results generated by its child jobs. For example, lets assume the following worker for the child jobs:

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import { Worker } from 'bullmq';

const stepsWorker = new Worker('steps', async job => {
  await performStep(job.data);

  if (job.name === 'paint') {
    return 2500;
  } else if (job.name === 'fix') {
    return 1750;
  }
});
```

{% endtab %}

{% tab title="Python" %}

```python
from bullmq import Worker

async def process(job: Job, token: str):
  await performStep(job.data)
  if job.name == 'paint':
    return 2500
  elif job.name == 'fix':
    return 1750

stepsWorker = Worker("steps", process, {"connection": connection})
```

{% endtab %}
{% endtabs %}

We can implement a parent worker that sums the costs of the children's jobs using the `getChildrenValues` method. This method returns an object with *job keys* as keys and the *result of that given job* as a value:

```typescript
import { Worker } from 'bullmq';

const renovateWorker = new Worker('renovate', async job => {
  const childrenValues = await job.getChildrenValues();

  const totalCosts = Object.values(childrenValues).reduce(
    (prev, cur) => prev + cur,
    0,
  );

  await sendInvoice(totalCosts);
});
```

It is possible to add as deep job hierarchies as needed. See the following example where jobs are depending on each other, allowing serial execution of jobs:

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import { FlowProducer } from 'bullmq';
const flowProducer = new FlowProducer();

const queueName = 'assembly-line';
const chain = await flowProducer.add({
  name: 'car',
  data: { step: 'engine' },
  queueName,
  children: [
    {
      name: 'car',
      data: { step: 'wheels' },
      queueName,
      children: [{ name: 'car', data: { step: 'chassis' }, queueName }],
    },
  ],
});
```

{% endtab %}

{% tab title="Python" %}

```python
from bullmq import FlowProducer

flowProducer = FlowProducer()

queueName = 'assembly-line'
chain = await flowProducer.add({
  "name": "car",
  "data": { "step": "engine" },
  "queueName": queueName,
  "children": [
    {
      "name": "car",
      "data": { "step": "wheels" },
      "queueName": queueName,
      "children": [{ "name": "car", "data": { "step": "chassis" }, "queueName": queueName }],
    },
  ],
})
```

{% endtab %}
{% endtabs %}

In this case one job will be processed after the previous one has been completed.

{% hint style="info" %}
The order of processing would be: `chassis`, `wheels` and finally `engine`.
{% endhint %}

## Getters

There are some special getters that can be used in order to get jobs related to a flow. First, we have a method in the `Job` class to get all the dependencies for a given job:

```typescript
const dependencies = await job.getDependencies();
```

it will return all the **direct** **dependencies** (i.e. the children of a given job).

Or if you want to get specific types of children:

```typescript
// cursors are used in pagination
const { processed, nextProcessedCursor } = await job.getDependencies({
  processed: {
    count: 5,
    cursor: 0,
  },
});

const { unprocessed, nextUnprocessedCursor } = await job.getDependencies({
  unprocessed: {
    count: 5,
    cursor: 0,
  },
});

const { failed, nextFailedCursor } = await job.getDependencies({
  failed: {
    count: 5,
    cursor: 0,
  },
});

const { ignored, nextIgnoredCursor } = await job.getDependencies({
  ignored: {
    count: 5,
    cursor: 0,
  },
});
```

The `Job` class also provides some other methods that we presented above

## Get Dependencies Count

To get all the different counts of children by type:

```typescript
const { failed, ignored, processed, unprocessed } =
  await job.getDependenciesCount();
```

Or if you want to be specific:

```typescript
const { failed } = await job.getDependenciesCount({
  failed: true,
});

const { ignored, processed } = await job.getDependenciesCount({
  ignored: true,
  processed: true,
});

const { unprocessed } = await job.getDependenciesCount({
  unprocessed: true,
});
```

## Get Children Values

To get all the values produced by the children of a given job:

```typescript
const values = await job.getChildrenValues();
```

Also, a new property is available in the `Job` class, ***`parentKey`,*** with a fully qualified key for the job parent.

Finally, there is also a new state which a job can be in, "waiting-children", for parent jobs that have not yet had their children completed:

```typescript
const state = await job.getState();
// state will be "waiting-children"
```

## Provide options

When adding a flow it is also possible to provide an extra object **`queueOptions`** object, in which you can add your specific options for every queue that is used in the flow. These options would affect each one of the jobs that are added to the flow using the `FlowProducer`.

```typescript
import { FlowProducer } from 'bullmq';
const flowProducer = new FlowProducer();

const queueName = 'assembly-line';
const chain = await flowProducer.add(
  {
    name: 'car',
    data: { step: 'engine' },
    queueName,
    children: [
      {
        name: 'car',
        data: { step: 'wheels' },
        queueName,
      },
    ],
  },
  {
    queuesOptions: {
      [queueName]: {
        defaultJobOptions: {
          removeOnComplete: true,
        },
      },
    },
  },
);
```

{% hint style="warning" %}
Queue options are defined in the context of their instances. You should provide your configurations in the second parameter in order to avoid unexpected behaviors.
{% endhint %}

## Jobs removal

BullMQ also provides seamless removal functionality for jobs that are part of a flow.

When removing a job that is part of the flow there are several important considerations:

1. If a parent job is removed, all its children will also be removed.
2. If a child job is removed, its parent dependency to said child is also removed, and if the child was the last child in the dependencies list, the parent job will be completed.
3. Since a job can be both a parent and a child in a large flow, both 1 and 2 will occur if removing such a job.
4. If any of the jobs that would be removed happen to be locked, none of the jobs will be removed, and an exception will be thrown.

Apart from the considerations above, removing a job can simply be done by either using the `Job` or the `Queue` class:

```typescript
await job.remove();
// or
await queue.remove(job.id);
```

## Read more:

* 📋 [Divide large jobs using flows](https://blog.taskforce.sh/splitting-heavy-jobs-using-bullmq-flows/)
* 💡 [FlowProducer API Reference](https://api.docs.bullmq.io/classes/v5.FlowProducer.html)
* 💡 [Job API Reference](https://api.docs.bullmq.io/classes/v5.Job.html)
* 💡 [Get Children Values API Reference](https://api.docs.bullmq.io/classes/v5.Job.html#getchildrenvalues)
* 💡 [Get Dependencies API Reference](https://api.docs.bullmq.io/classes/v5.Job.html#getdependencies)
* 💡 [Get Dependencies Count API Reference](https://api.docs.bullmq.io/classes/v5.Job.html#getdependenciescount)


# Adding flows in bulk

Sometimes it is necessary to atomically add flows in bulk. For example, there could be a requirement that all the flows must be created or none of them. Also, adding flows in bulk can be faster since it reduces the number of roundtrips to Redis:

```typescript
import { FlowProducer } from 'bullmq';

const flow = new FlowProducer({ connection });

const trees = await flow.addBulk([
  {
    name: 'root-job-1',
    queueName: 'rootQueueName-1',
    data: {},
    children: [
      {
        name,
        data: { idx: 0, foo: 'bar' },
        queueName: 'childrenQueueName-1',
      },
    ],
  },
  {
    name: 'root-job-2',
    queueName: 'rootQueueName-2',
    data: {},
    children: [
      {
        name,
        data: { idx: 1, foo: 'baz' },
        queueName: 'childrenQueueName-2',
      },
    ],
  },
]);
```

This call can only succeed or fail, and all or none of the jobs will be added.

## Read more:

* 💡 [Add Bulk API Reference](https://api.docs.bullmq.io/classes/v5.FlowProducer.html#addbulk)


# Get Flow Tree

In some situations, you need to get a job and all of its children, grandchildren, and so on.

The pattern to solve this requirement consists of using the [`getFlow`](https://api.docs.bullmq.io/classes/v5.FlowProducer.html#getflow) method.

```typescript
const flow = new FlowProducer({ connection });

const originalTree = await flow.add({
  name: 'root-job',
  queueName: 'topQueueName',
  data: {},
  children: [
    {
      name,
      data: { idx: 0, foo: 'bar' },
      queueName: 'childrenQueueName',
      children: [
        {
          name,
          data: { idx: 4, foo: 'baz' },
          queueName: 'grandchildrenQueueName',
        },
      ],
    },
    {
      name,
      data: { idx: 2, foo: 'foo' },
      queueName: 'childrenQueueName',
    },
    {
      name,
      data: { idx: 3, foo: 'bis' },
      queueName: 'childrenQueueName',
    },
  ],
});

const { job: topJob } = originalTree;

const tree = await flow.getFlow({
  id: topJob.id,
  queueName: 'topQueueName',
});

const { children, job } = tree;
```

{% hint style="info" %}
Each *child* may have a `job` property and in the case they have children as well, they would have the `children` property
{% endhint %}

You may also need a way to limit that information if you have many children for one of the job nodes.

```typescript
const limitedTree = await flow.getFlow({
  id: topJob.id,
  queueName: 'topQueueName',
  depth: 1, // get only the first level of children
  maxChildren: 2, // get only 2 children per node
});

const { children, job } = limitedTree;
```

## Read more:

* 💡 [Get Flow API Reference](https://api.docs.bullmq.io/classes/v5.FlowProducer.html#getflow)


# Fail Parent

Make parents fail is any of its children fails

In certain workflows, you may need a parent job to fail immediately if any of its child jobs fail. The `failParentOnFailure` option allows you to achieve this behaviour. When set to true on a child job, it ensures that if the child fails, its parent job is also marked as failed. This effect can propagate recursively up the job hierarchy, potentially causing grandparents or higher-level ancestors to fail as well, depending on the configuration.

### Key Points

* Selective Application: Only child jobs with failParentOnFailure: true will trigger the failure of their parent job upon failing. Child jobs without this option will not affect the parent's state if they fail.
* Recursive Behavior: If a child with this option fails, and its parent also has failParentOnFailure: true, the failure propagates upward through the job tree, potentially affecting grandparents and beyond.
* Immediate Effect: As soon as a qualifying child job fails, the parent job is moved to the failed state.

### Example

```typescript
import { FlowProducer } from 'bullmq';

const flow = new FlowProducer({ connection });

const originalTree = await flow.add({
  name: 'root-job',
  queueName: 'topQueueName',
  data: {},
  children: [
    {
      name: 'child-job',
      data: { idx: 0, foo: 'bar' },
      queueName: 'childrenQueueName',
      // This child will fail its parent if it fails
      opts: { failParentOnFailure: true },
      children: [
        {
          name,
          data: { idx: 1, foo: 'bah' },
          queueName: 'grandChildrenQueueName',
          // This grandchild will fail its parent if it fails
          opts: { failParentOnFailure: true },
        },
        {
          name,
          data: { idx: 2, foo: 'baz' },
          queueName: 'grandChildrenQueueName',
          // No failParentOnFailure; its failure won't affect the parent
        },
      ],
    },
    {
      name,
      data: { idx: 3, foo: 'foo' },
      queueName: 'childrenQueueName',
      // No failParentOnFailure; its failure won't affect the parent
    },
  ],
});
```

{% hint style="info" %}
As soon as a *child* with this option fails, the parent job will be marked as failed lazily. A worker must process the parent job before it transitions to the failed state. The failure will result in an *UnrecoverableError* with the message **child {childKey} failed**. Additionally, this option will be validated recursively, meaning a grandparent or higher-level ancestor could also fail depending on the configuration.
{% endhint %}

### How it Works

* If grandchild-job-1 fails, its parent (child-job-1) will fail because of failParentOnFailure: true. Since child-job-1 also has failParentOnFailure: true, the root job (root-job) will fail as well.
* If grandchild-job-2 fails, its parent (child-job-1) will not fail because failParentOnFailure is not set on this grandchild.
* Similarly, if child-job-2 fails, the root job will remain unaffected since failParentOnFailure is not enabled for that child.

### Use Case

This option is particularly useful in workflows where the success of a parent job depends critically on specific child jobs, allowing you to enforce strict dependencies and fail fast when necessary.

## Read more:

* 💡 [Add Flow API Reference](https://api.docs.bullmq.io/classes/v5.FlowProducer.html#add)


# Continue Parent

Process parent if any children fails.

{% hint style="info" %}
Available since v5.58.0
{% endhint %}

The `continueParentOnFailure` option allows a parent job to start processing as soon as a child job fails, while the `removeUnprocessedChildren` method enables dynamic cleanup of unprocessed child jobs. Additionally, you can use the `getFailedChildrenValues`() method to determine whether the parent is processing due to a child failure or because all children completed successfully, allowing you to define distinct logic paths.

### continueParentOnFailure

When set to `true` on a child job, the `continueParentOnFailure` option causes the parent job to begin processing immediately if that child fails. This contrasts with the default behavior, where the parent waits for all children to finish.

* **Key Behavior**: The parent moves to the active state as soon as a child with this option fails, even if other children are still running or unprocessed.
* **Use Case**: Ideal for scenarios where a child’s failure requires immediate parent intervention, such as aborting the workflow or performing cleanup.

### removeUnprocessedChildren

This method, available on a job instance, removes all unprocessed child jobs (those in waiting or delayed states) from the queue. It’s particularly useful when paired with `continueParentOnFailure` to get rid of remaining children after a failure.

* **Key Behavior**: Only affects children that haven’t started processing; **active, completed or failed** children remain intact.
* **Usage**: Call within the parent’s processor to clean up dynamically.

### getFailedChildrenValues

The `getFailedChildrenValues()` method returns an object mapping the IDs of failed child jobs to their failure error messages. This allows the parent job to determine why it’s processing—whether due to a child failure (triggered by `continueParentOnFailure`) or because all children completed successfully.

* **Return Value**: An object where keys are job IDs and values are error messages (e.g., { "job-id-1": "Upload failed" }). If no children failed, the object is empty.
* **Usage**: Use this in the parent’s processor to branch logic based on the presence of failed children.

### Example

The following example shows how to combine these features, with the parent job reacting differently based on whether a child failed or all children succeeded:

```typescript
const { FlowProducer } = require('bullmq');
const flow = new FlowProducer({ connection });

// Define the flow
const originalTree = await flow.add({
  name: 'root-job',
  queueName: 'topQueueName',
  data: {},
  children: [
    {
      name: 'child-job-1',
      data: { idx: 0, foo: 'bar' },
      queueName: 'childrenQueueName',
      opts: { continueParentOnFailure: true }, // Parent processes if this child fails
    },
    {
      name: 'child-job-2',
      data: { idx: 1, foo: 'baz' },
      queueName: 'childrenQueueName',
    },
    {
      name: 'child-job-3',
      data: { idx: 2, foo: 'qux' },
      queueName: 'childrenQueueName',
    },
  ],
});

// Processor for the parent job
const processor = async (job) => {
  // Check if any children failed
  const failedChildren = await job.getFailedChildrenValues();
  const hasFailedChildren = Object.keys(failedChildren).length > 0;

  if (hasFailedChildren) {
    // Path 1: A child failed, triggering continueParentOnFailure
    console.log(`Parent job ${job.name} triggered by child failure(s):`, failedChildren);
    
    // Remove unprocessed children
    await job.removeUnprocessedChildren();
    console.log('Unprocessed child jobs have been removed.');
    
    // Additional cleanup or error handling can go here
  } else {
    // Path 2: All children completed successfully
    console.log(`Parent job ${job.name} processing after all children completed successfully.`);
    
    // Proceed with normal parent logic (e.g., aggregating results)
  }
};

```

### Practical use case

Consider a workflow where child jobs upload files to different servers. If one upload fails (e.g., `child-job-1`), the parent can use continueParentOnFailure to react immediately, check `getFailedChildrenValues()` to confirm the failure, and call `removeUnprocessedChildren()` to cancel remaining uploads. If all uploads succeed, the parent might aggregate the results instead.


# Remove Dependency

In some situations, you may have a parent job and need to remove the relationship when one of its children fail.

The pattern to solve this requirement consists on using the **removeDependencyOnFailure** option. This option will make sure that when a job fails, the dependency is removed from the parent, so the parent will complete without waiting for the failed children.

```typescript
const flow = new FlowProducer({ connection });

const originalTree = await flow.add({
  name: 'root-job',
  queueName: 'topQueueName',
  data: {},
  children: [
    {
      name,
      data: { idx: 0, foo: 'bar' },
      queueName: 'childrenQueueName',
      opts: { removeDependencyOnFailure: true },
      children: [
        {
          name,
          data: { idx: 1, foo: 'bah' },
          queueName: 'grandChildrenQueueName',
        },
        {
          name,
          data: { idx: 2, foo: 'baz' },
          queueName: 'grandChildrenQueueName',
        },
      ],
    },
    {
      name,
      data: { idx: 3, foo: 'foo' },
      queueName: 'childrenQueueName',
    },
  ],
});
```

{% hint style="info" %}
As soon as a **child** with this option fails, the parent job will be moved to a waiting state only if there are no more pending children.
{% endhint %}

## Read more:

* 💡 [Add Flow API Reference](https://api.docs.bullmq.io/classes/v5.FlowProducer.html#add)


# Ignore Dependency

In some situations, you may have a parent job and need to ignore when one of its children fail.

The pattern to solve this requirement consists on using the **ignoreDependencyOnFailure** option. This option will make sure that when a job fails, the dependency is ignored from the parent, so the parent will complete without waiting for the failed children.

```typescript
const flow = new FlowProducer({ connection });

const originalTree = await flow.add({
  name: 'root-job',
  queueName: 'topQueueName',
  data: {},
  children: [
    {
      name,
      data: { idx: 0, foo: 'bar' },
      queueName: 'childrenQueueName',
      opts: { ignoreDependencyOnFailure: true },
      children: [
        {
          name,
          data: { idx: 1, foo: 'bah' },
          queueName: 'grandChildrenQueueName',
        },
        {
          name,
          data: { idx: 2, foo: 'baz' },
          queueName: 'grandChildrenQueueName',
        },
      ],
    },
    {
      name,
      data: { idx: 3, foo: 'foo' },
      queueName: 'childrenQueueName',
    },
  ],
});
```

{% hint style="info" %}
As soon as a **child** with this option fails, the parent job will be moved to a waiting state only if there are no more pending children.
{% endhint %}

Failed children using this option can be retrieved by **getIgnoredChildrenFailures** method:

```typescript
const ignoredChildrenFailures =
  await originalTree.job.getIgnoredChildrenFailures();
```

## Read more:

* 💡 [Add Flow API Reference](https://api.docs.bullmq.io/classes/v5.FlowProducer.html#add)


# Remove Child Dependency

In some situations, you may have a parent job and need to remove the dependency of one of its children.

The pattern to solve this requirement consists on using the **removeChildDependency** method. It will make sure that if the job is the last pending child, to move its parent to *waiting* and it won't be listed in unprocessed list of the parent.

```typescript
const flow = new FlowProducer({ connection });

const originalTree = await flow.add({
  name: 'root-job',
  queueName: 'topQueueName',
  data: {},
  children: [
    {
      name,
      data: { idx: 0, foo: 'bar' },
      queueName: 'childrenQueueName',
      opts: {},
    },
  ],
});

await originalTree.children[0].job.removeChildDependency();
```

{% hint style="info" %}
As soon as a **child** calls this method, it will verify if it has an existing parent, if not, it'll throw an error.
{% endhint %}

Failed or completed children using this option won't generate any removal as they won't be part of unprocessed list.


# Metrics

Built-in Metrics for your queues.

BullMQ provides a simple metrics gathering functionality that allows you to track the performance of your queues. Workers can count the number of jobs they have processed **per minute** and store this data in a list inside Redis so that it can be queried later.

You enable it on the worker settings by specifying how many data points you want to keep, which basically are counters of the number of jobs that have been processed either completed or failed during 1 minute intervals.

As the metrics are aggregated in 1 minute intervals, using the recommended duration of 2 weeks of data should take a very small amount of total space, just around 120Kb of RAM per queue. The metrics will dispose older data points automatically so this RAM consumption will never increase after it reaches the maximum number of data points.

Check in this example how to enable metrics on a worker:

```typescript
import { Worker, MetricsTime } from 'bullmq';

const myWorker = new Worker('Paint', {
  connection,
  metrics: {
    maxDataPoints: MetricsTime.ONE_WEEK * 2,
  },
});
```

{% hint style="warning" %}
You need to use the same setting on all your workers to get consistent metrics.
{% endhint %}

In order to query the metrics, use the `getMetrics` method on the `Queue` class. You can choose to gather the metrics for the *completed* or *failed* jobs:

```typescript
import { Queue } from 'bullmq';
const myQueue = new Queue('Paint', {
  connection,
});

const metrics = await queue.getMetrics('completed', 0, MetricsTime.ONE_WEEK * 2);

/* Returns a Metrics object:
{
    data: number[];
    count: number;
    meta: {
      count: number;
      prevTS: number;
      prevCount: number;
    };
  }
*/
```

Let's analyze what data we are getting back. First we have the `meta` field. The `prevTS` and `prevCount` subfields are used internally by the metrics system and should not be used, however you can use the`count` subfield to get a total number for all completed or failed jobs, this counter is not just the number of completed jobs in the given interval, but since the queue started processing jobs.

The query also returns a `data` field which is an array where every position in the array represents 1 minute of time and has the total number of jobs that completed (or failed) in that minute.

Note that the `getMetrics` method also accepts a `start` and `end` argument (`0` and `-1` by default), that you can use if you want to implement pagination.

## Read more:

* 💡 [Get Metrics API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#getmetrics)


# Prometheus

How to use the built-in prometheus exporter

BullMQ provides a simple API to export metrics to Prometheus. To use it, create an endpoint in your web server that calls `exportPrometheusMetrics()`, and configure Prometheus to scrape metrics from this endpoint.

#### Basic Usage

Below is an example using vanilla Node.js:

```typescript
import http from 'http';
import { Queue } from 'bullmq';

const queue = new Queue('my-queue');

const server = http.createServer(
  async (req: http.IncomingMessage, res: http.ServerResponse) => {
    try {
      if (req.url === '/metrics' && req.method === 'GET') {
        const metrics = await queue.exportPrometheusMetrics();

        res.writeHead(200, {
          'Content-Type': 'text/plain',
          'Content-Length': Buffer.byteLength(metrics),
        });
        res.end(metrics);
      } else {
        res.writeHead(404);
        res.end('Not Found');
      }
    } catch (err: unknown) {
      res.writeHead(500);
      res.end(`Error: ${err instanceof Error ? err.message : 'Unknown error'}`);
    }
  },
);

const PORT = process.env.PORT || 3000;

server.listen(PORT, () => {
  console.log(`Prometheus metrics server running on port ${PORT}`);
  console.log(`Metrics available at http://localhost:${PORT}/metrics`);
});
```

Test the endpoint with:

```bash
curl http://localhost:3000/metrics
```

This will return an output like:

```
HELP bullmq_job_count Number of jobs in the queue by state
TYPE bullmq_job_count gauge
bullmq_job_count{queue="my-queue", state="waiting"} 5
bullmq_job_count{queue="my-queue", state="active"} 3
bullmq_job_count{queue="my-queue", state="completed"} 12
bullmq_job_count{queue="my-queue", state="failed"} 2
```

For a simpler setup with Express.js:

```typescript
import express from 'express';
import { Queue } from './src/queue';

const app = express();
const queue = new Queue('my-queue');

app.get('/metrics', async (req, res) => {
  try {
    const metrics = await queue.exportPrometheusMetrics();
    res.set('Content-Type', 'text/plain');
    res.send(metrics);
  } catch (err) {
    res.status(500).send(err.message);
  }
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`Prometheus metrics server running on port ${PORT}`);
  console.log(`Metrics available at http://localhost:${PORT}/metrics`);
});
```

#### Advanced Usage: Adding Global Variables as Labels

The `exportPrometheusMetrics` function also supports an optional globalVariables parameter. This allows you to include additional labels (e.g., env, server) in your metrics, which is particularly useful when aggregating metrics from multiple environments (like production or staging) in tools like Grafana. The globalVariables parameter accepts a record of key-value pairs that are added as labels to each metric.

#### Example with Global Variables

Here’s how to use this feature in vanilla Node.js:

```typescript
import http from 'http';
import { Queue } from 'bullmq';

const queue = new Queue('my-queue');

const server = http.createServer(
  async (req: http.IncomingMessage, res: http.ServerResponse) => {
    try {
      if (req.url === '/metrics' && req.method === 'GET') {
        const globalVariables = { env: 'Production', server: '1' };
        const metrics = await queue.exportPrometheusMetrics(globalVariables);

        res.writeHead(200, {
          'Content-Type': 'text/plain',
          'Content-Length': Buffer.byteLength(metrics),
        });
        res.end(metrics);
      } else {
        res.writeHead(404);
        res.end('Not Found');
      }
    } catch (err: unknown) {
      res.writeHead(500);
      res.end(`Error: ${err instanceof Error ? err.message : 'Unknown error'}`);
    }
  },
);

const PORT = process.env.PORT || 3000;

server.listen(PORT, () => {
  console.log(`Prometheus metrics server running on port ${PORT}`);
  console.log(`Metrics available at http://localhost:${PORT}/metrics`);
});
```

With globalVariables = { env: 'Production', server: '1' }, the output becomes:

```plaintext
# HELP bullmq_job_count Number of jobs in the queue by state
# TYPE bullmq_job_count gauge
bullmq_job_count{queue="my-queue", state="waiting", env="Production", server="1"} 5
bullmq_job_count{queue="my-queue", state="active", env="Production", server="1"} 3
bullmq_job_count{queue="my-queue", state="completed", env="Production", server="1"} 12
bullmq_job_count{queue="my-queue", state="failed", env="Production", server="1"} 2
```

These additional labels allow you to filter and group metrics in Prometheus or Grafana, making it easier to distinguish between different environments or servers.

## Read more:

* 💡 [Export Prometheus Metrics API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#exportprometheusmetrics)


# Rate limiting

BullMQ provides queue rate limiting. It is possible to configure workers so that they obey a given rate limiting option:

```typescript
import { Worker, QueueScheduler } from 'bullmq';

const worker = new Worker('painter', async job => paintCar(job), {
  limiter: {
    max: 10,
    duration: 1000,
  },
});

const scheduler = new QueueScheduler('painter');
```

{% hint style="warning" %}
Jobs that get rate limited will actually stay in the waiting state.
{% endhint %}

{% hint style="danger" %}
From BullMQ 2.0 and onwards, the `QueueScheduler` is not needed anymore.
{% endhint %}

{% hint style="info" %}
The rate limiter is global, so if you have for example 10 workers for one queue with the above settings, still only 10 jobs will be processed by second.
{% endhint %}

### Group keys

{% hint style="danger" %}
From BullMQ 3.0 and onwards, group keys support is removed to improve global rate limit, so the information below is only valid for older versions.
{% endhint %}

It is also possible to define a rate limiter based on group keys, for example you may want to have a rate limiter per *customer* instead of a global rate limiter for all customers:

```typescript
import { Queue, Worker, QueueScheduler } from 'bullmq';

const queue = new Queue('painter', {
  limiter: {
    groupKey: 'customerId',
  },
});

const worker = new Worker('painter', async job => paintCar(job), {
  limiter: {
    max: 10,
    duration: 1000,
    groupKey: 'customerId',
  },
});

const scheduler = new QueueScheduler('painter');

// jobs will be rate limited by the value of customerId key:
await queue.add('rate limited paint', { customerId: 'my-customer-id' });
```

### Manual rate-limit

Sometimes is useful to rate-limit a queue manually instead of based on some static options. For example, you may have an API that returns `429 Too Many Requests`, and you want to rate-limit the queue based on that response.

For this purpose, you can use the worker method **`rateLimit`** like this:

```typescript
import { Worker } from 'bullmq';

const worker = new Worker(
  'myQueue',
  async () => {
    const [isRateLimited, duration] = await doExternalCall();
    if (isRateLimited) {
      await worker.rateLimit(duration);
      // Do not forget to throw this special exception,
      // since we must differentiate this case from a failure
      // in order to move the job to wait again.
      throw Worker.RateLimitError();
    }
  },
  {
    connection,
    limiter: {
      max: 1,
      duration: 500,
    },
  },
);
```

{% hint style="warning" %}
Don't forget to pass limiter options into your worker's options as *limiter.max* is used to determine if we need to execute the rate limit validation.
{% endhint %}

### Get Queue Rate Limit Ttl

Sometimes is useful to know if our queue is rate limited.

For this purpose, you can use the **`getRateLimitTtl`** method like this:

```typescript
import { Queue } from 'bullmq';

const queue = new Queue('myQueue', { connection });
const maxJobs = 100;

const ttl = await queue.getRateLimitTtl(maxJobs);

if (ttl > 0) {
  console.log('Queue is rate limited');
}
```

### Remove Rate Limit Key

Sometimes is useful to stop a rate limit delay.

For this purpose, you can use the **`removeRateLimitKey`** method like this:

```typescript
import { Queue } from 'bullmq';

const queue = new Queue('myQueue', { connection });

await queue.removeRateLimitKey();
```

By removing rate limit key, workers will be able to pick jobs again and your rate limit counter is reset to zero.

## Read more:

* 💡 [Rate Limit API Reference](https://api.docs.bullmq.io/classes/v5.Worker.html#ratelimit)
* 💡 [Get Rate Limit Ttl API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#getratelimitttl)
* 💡 [Remove Rate Limit Key API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#removeratelimitkey)


# Parallelism and Concurrency

In this chapter we would like to clean up some misconceptions regarding parallel execution and concurrency, how these two terms are applied to BullMQ queues, and how they can be used to maximize throughput depending on the kind of jobs that you need to process.

## Parallelism

Parallelism is the simplest of these two concepts as it means basically what your intuition will tell you: that two or more tasks can be run in parallel, independently of each other. This is the case when you have a multi-core processor, or if you have several machines running at the same time. There is a chance that tasks are running in parallel. However, running in parallel does not guarantee that the CPU time is maximized, mainly because most software is continually being blocked by slow IO operations such as reading from the network, writing to disk, sending and receiving data via peripherals, and so on.

If tasks are very CPU intensive though, then being able to run them 100% in parallel will give you the biggest performance, as there will be very little overhead, but this is the exception rather than the norm, thats why in modern computers most tasks are instead run concurrently.

## Concurrency

In the context of computer science, concurrency refers to the ability of different tasks to run at the same time by dividing the available CPU into small slices so that all the tasks can advance in their processing, giving the impression that they are being executed independently in parallel. So when we say that we have 100 tasks running concurrently, it means that they are all advancing their processing but never at exactly the same time.

#### NodeJS Event Loop

One of the features that makes NodeJS very efficient at dispatching requests in an HTTP server is the fact that it has one single loop and is capable of running a huge amount of microtasks concurrently by exploiting the async nature of IO calls. So for example, if a call is performed to a database for querying some data, that call will not block the entire NodeJS, instead it will go and execute some other piece of code and then at the end of the current event loop, check if any of the async calls have completed so that they can continue running in the next iteration.

This gives the effect of parallel execution, however, it is not the case, and the only reason it is efficient is that the code is IO heavy thus we can better utilize the CPU time by executing code instead of just being idle waiting for an asynchronous call to finish.

#### BullMQ concurrency

BullMQ allows you to set a concurrency setting on your workers. This setting is local for the worker and exploits the NodeJS event loop so that jobs that are IO-heavy will benefit from higher throughput, as the worker does not need to wait for a job to complete before it can pick the next one. But it is very important to understand that if the jobs are not IO-heavy but instead are CPU intensive, increasing concurrency will decrease the overall throughput as we will just be adding overhead when there is not a lot that can be done to run concurrently.

#### What about threading?

Threads are a mechanism used by the operating system to provide concurrent (and parallel) execution, by pre-empting a given thread by another one (in the case of threads running in the same CPU), or by running threads in parallel if there are several CPU cores available. In practice however, a modern OS runs hundreds if not thousands of threads at any given time, so actually no guarantee running code in several threads will indeed run in parallel, there is just a chance they will, and this depends a lot on how the given OS has implemented its scheduler, this can be quite complex but as a rule of thumb we can say that if there are 2 threads that consume a lot of CPU, and there are at least 2 cores, then most likely these two threads will run each on its dedicated CPU.

NodeJS has thread support, but it is important to note that these threads are pretty heavy and almost consume the same amount of memory as if they were running in two different OS processes. The reason for this is that every NodeJS thread requires a complete V8 VM, with a lot of built-in libraries, which will add up to several dozens of megabytes.

## How to best use BullMQ's concurrency then?

You have 2 ways to increase parallelism and concurrency with BullMQ: you can specify the concurrency factor per worker, and you can have several workers running in parallel.

The concurrency factor will just take advantage of NodeJS's event loop so that the worker can process several jobs concurrently while the jobs are doing IO operations. If your jobs require IO operations, then you can increase this number quite a lot. Something between 100 and 300 is a quite standard setting, the only way to finetune this value is by observing how the worker processes the production workload.

If the jobs are very CPU intensive without IO calls, then there is no point in having a large concurrency number as it will just add overhead. Still, since BullMQ itself also performs IO operations (when updating Redis and fetching new jobs), there is a chance that a slight concurrency factor may even improve the throughput of CPU-intensive jobs.

Secondly, you can run as many workers as you want. Every worker will run in parallel if it has a CPU at its disposal. You can run several workers in a given machine if the machine has more than one core, but you can also run workers in totally different machines. The jobs running on different workers will be running in parallel, so even if the job is CPU-intensive you will be able to increase the throughput which will normally scale linearly with the number of workers.


# Retrying failing jobs

As your queues process jobs, it is inevitable that over time some of these jobs will fail. In BullMQ, a job is considered failed in the following scenarios:

* The processor function defined in your [`Worker`](https://docs.bullmq.io/guide/workers) has thrown an exception.
* The job has become [*stalled*](https://docs.bullmq.io/guide/jobs/stalled) and it has consumed the "max stalled count" setting.

{% hint style="danger" %}
The exceptions thrown in a processor must be an [`Error`](https://nodejs.org/api/errors.html#class-error) object for BullMQ to work correctly.

In general, as a best practice, it is better to always throw `Error` objects. There is even an [ESLint rule](https://eslint.org/docs/latest/rules/no-throw-literal) if you want to enforce it.
{% endhint %}

## Retrying failing jobs

When a processor throws an exception, the worker will catch it and move the job to the failed set. Depending on your [Queue settings](https://docs.bullmq.io/guide/queues/auto-removal-of-jobs), the job may stay in the failed set forever, or it could be automatically removed.

Often it is desirable to automatically retry failed jobs so that we do not give up until a certain amount of retries have failed. In order to activate automatic job retries you should use the [`attempts`](https://api.docs.bullmq.io/interfaces/v5.BaseJobOptions.html#attempts) setting with a value larger than 1 (see the examples below).

BullMQ supports retries of failed jobs using back-off functions. It is possible to use the **built-in** backoff functions or provide **custom** ones. If you do not specify a back-off function, the jobs will be retried without delay as soon as they fail.

{% hint style="info" %}
Retried jobs will respect their priority when they are moved back to waiting state.
{% endhint %}

### Built-in backoff strategies

The current built-in backoff functions are **fixed** and **exponential**.

#### Fixed

With a fixed backoff, it will retry after `delay` milliseconds, so with a delay of 3000 milliseconds, it will retry *every* attempt 3000 milliseconds after the previous attempt.

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('foo');

await queue.add(
  'test-retry',
  { foo: 'bar' },
  {
    attempts: 3,
    backoff: {
      type: 'fixed',
      delay: 1000,
    },
  },
);
```

You can also provide a [jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/) option, it will generate random delays between `delay` and 0 milliseconds depending on the percentage of jitter usage. For example, you can provide a jitter value of 0.5 value and a delay of 1000 milliseconds, it will generate a delay between `1000` milliseconds = 1 second and `1000 * 0.5` milliseconds = 500ms.

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('foo');

await queue.add(
  'test-retry',
  { foo: 'bar' },
  {
    attempts: 8,
    backoff: {
      type: 'fixed',
      delay: 1000,
      jitter: 0.5,
    },
  },
);
```

#### Exponential

With exponential backoff, it will retry after `2 ^ (attempts - 1) * delay` milliseconds. For example, with a delay of 3000 milliseconds, for the 7th attempt, it will retry `2^6 * 3000` milliseconds = 3.2 minutes after the previous attempt.

The code below shows how to specify the built-in "exponential" backoff function with a 1-second delay as a seed value, so it will retry at most 2 times (after the first attempt, reaching a total 3 attempts) spaced after 1 second, 2 seconds, and 4 seconds respectively:

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('foo');

await queue.add(
  'test-retry',
  { foo: 'bar' },
  {
    attempts: 3,
    backoff: {
      type: 'exponential',
      delay: 1000,
    },
  },
);
```

You can also provide a [jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/) option, it will generate random delays between `2 ^ (attempts - 1) * delay` and 0 milliseconds depending on the percentage of jitter usage. For example, you can provide a jitter value of 0.5 value and a delay of 3000 milliseconds, for the 7th attempt, it will generate a delay between `2^6 * 3000` milliseconds = 192000ms and `2^6 * 3000 * 0.5` milliseconds = 96000ms after the previous attempt.

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('foo');

await queue.add(
  'test-retry',
  { foo: 'bar' },
  {
    attempts: 8,
    backoff: {
      type: 'exponential',
      delay: 3000,
      jitter: 0.5,
    },
  },
);
```

You can also define the back-off strategy in the queue's `defaultJobOptions`, and it will apply to all jobs added to the queue unless overridden when adding the job. For example:

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('foo', {
  defaultJobOptions: {
    attempts: 3,
    backoff: {
      type: 'exponential',
      delay: 1000,
    },
  },
});

await queue.add('test-retry', { foo: 'bar' });
```

{% hint style="info" %}
Jitter percentage option value must be between 0 and 1. 0 percentage means no randomness is applied (default behavior), while 1 means that random delays will be generated beween 0 and max generated value by any of our built-in strategies.
{% endhint %}

### Custom back-off strategies

If you want to define your custom backoff function, you need to define it in the worker settings:

```typescript
import { Worker } from 'bullmq';

const worker = new Worker('foo', async job => doSomeProcessing(), {
  settings: {
    backoffStrategy: (attemptsMade: number) => {
      return attemptsMade * 1000;
    },
  },
});
```

{% hint style="info" %}
If your backoffStrategy returns 0, jobs will be moved at the end of our waiting list (priority 0) or moved back to prioritized state (priority > 0).

If your backoffStrategy returns -1, jobs won't be retried, instead they will be moved to failed state.
{% endhint %}

You can then use your custom strategy when adding jobs:

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('foo');

await queue.add(
  'test-retry',
  { foo: 'bar' },
  {
    attempts: 3,
    backoff: {
      type: 'custom',
    },
  },
);
```

If you want to define multiple custom backoff types you need to define them like in the following example:

```typescript
import { Worker } from 'bullmq';

const worker = new Worker('foo', async job => doSomeProcessing(), {
  settings: {
    backoffStrategy: (
      attemptsMade: number,
      type: string,
      err: Error,
      job: Job,
    ) => {
      switch (type) {
        case 'custom1': {
          return attemptsMade * 1000;
        }
        case 'custom2': {
          return attemptsMade * 2000;
        }
        default: {
          throw new Error('invalid type');
        }
      }
    },
  },
});
```

## Read more:

* 💡 [Stop Retrying Jobs](https://docs.bullmq.io/patterns/stop-retrying-jobs)


# Returning job data

When a worker is done processing, sometimes it is convenient to return some data. This data can then be accessed for example by listening to the `completed` event. This return data is available at the job's `returnvalue` property.

Imagine a simple worker that performs some async processing:

```typescript
import { Queue, Worker } from 'bullmq';

const myWorker = new Worker('AsyncProc', async job => {
  const result = await doSomeAsyncProcessing();
  return result;
});
```

{% hint style="info" %}
Note, in the example above we could just directly return the result of `doSomeAsyncProcessing`, we just use a temporary variable to make the example more explicit.
{% endhint %}

We can now listen to the completed event in order to get the result value:

```typescript
import { QueueEvents } from 'bullmq';

const queueEvents = new QueueEvents('AsyncProc');

queueEvents.on('completed', ({ returnvalue }) => {
  console.log(returnvalue);
});
```

If you want to store the result of the processing function it is still much more robust to do it in the process function itself, as that will guarantee that if the job is completed the return value would be stored as well. Storing data on the completed event on the other hand could fail and still the job would complete without detecting the error.

## Using a "results" Queue

Another common practice to send job results robustly is to have a special "results" queue to which results are sent. The worker for this "results" queue can reliably do something with the data such as storing it in a database. This approach is useful for designing robust micro-service architectures, where data is sent between services using queues. Even if the service that processes the result is down at the time the results queue receives the data, the result will still be processed as soon as the service come up online again.


# Events

All classes in BullMQ emit useful events that inform on the lifecycles of the jobs that are running in the queue. Every class is an `EventEmitter` and emits different events.

Some examples:

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('Paint');

myQueue.on('waiting', (job: Job) => {
  // Job is waiting to be processed.
});
```

```typescript
import { Worker } from 'bullmq';

const myWorker = new Worker('Paint');

myWorker.on('drained', () => {
  // Queue is drained, no more jobs left
});

myWorker.on('completed', (job: Job) => {
  // job has completed
});

myWorker.on('failed', (job: Job) => {
  // job has failed
});
```

The events above are local for the workers that actually completed the jobs. However, in many situations you want to listen to all the events emitted by all the workers in one single place. For this you can use the [`QueueEvents`](https://api.docs.bullmq.io/classes/v5.QueueEvents.html) class:

```typescript
import { QueueEvents } from 'bullmq';

const queueEvents = new QueueEvents('Paint');

queueEvents.on('completed', ({ jobId }) => {
  // Called every time a job is completed in any worker.
});

queueEvents.on(
  'progress',
  ({ jobId, data }: { jobId: string; data: number | object }) => {
    // jobId received a progress event
  },
);
```

The `QueueEvents` class is implemented using [Redis streams](https://redis.io/topics/streams-intro). This has some nice properties, for example, it provides guarantees that the events are delivered and not lost during disconnections such as it would be the case with standard pub-sub.

{% hint style="danger" %}
The event stream is auto-trimmed so that its size does not grow too much, by default it is \~10.000 events, but this can be configured with the `streams.events.maxLen` option.
{% endhint %}

### Manual trim events

In case you need to trim your events manually, you can use **`trimEvents`** method:

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import { Queue } from 'bullmq';

const queue = new Queue('paint');

await queue.trimEvents(10); // leaves 10 events
```

{% endtab %}

{% tab title="Python" %}

```python
from bullmq import Queue

queue = Queue('paint')

await queue.trimEvents(10) # leaves 10 events
```

{% endtab %}
{% endtabs %}

## Read more:

* 💡 [Queue Events API Reference](https://api.docs.bullmq.io/classes/v5.QueueEvents.html)
* 💡 [Queue Events Listener API Reference](https://api.docs.bullmq.io/interfaces/v5.QueueEventsListener.html)
* 💡 [Queue Listener API Reference](https://api.docs.bullmq.io/interfaces/v5.QueueListener.html)
* 💡 [Worker Listener API Reference](https://api.docs.bullmq.io/interfaces/v5.WorkerListener.html)


# Create Custom Events

In BullMQ, creating a generic distributed realtime event emitter is possible by using our **QueueEventsProducer** class.

Consumers must use **QueueEvents** class to subscribe to those events that they are interested in.

```typescript
const queueName = 'customQueue';
const queueEventsProducer = new QueueEventsProducer(queueName, {
  connection,
});
const queueEvents = new QueueEvents(queueName, {
  connection,
});

interface CustomListener extends QueueEventsListener {
  example: (args: { custom: string }, id: string) => void;
}
queueEvents.on<CustomListener>('example', async ({ custom }) => {
  // custom logic
});

interface CustomEventPayload {
  eventName: string;
  custom: string;
}

await queueEventsProducer.publishEvent<CustomEventPayload>({
  eventName: 'example',
  custom: 'value',
});
```

Only eventName attribute is required.

{% hint style="warning" %}
Some event names are reserved from [Queue Listener API Reference](https://api.docs.bullmq.io/interfaces/v5.QueueListener.html).
{% endhint %}

## Read more:

* 💡 [Queue Events API Reference](https://api.docs.bullmq.io/classes/v5.QueueEvents.html)
* 💡 [Queue Events Listener API Reference](https://api.docs.bullmq.io/interfaces/v5.QueueEventsListener.html)
* 💡 [Queue Events Producer API Reference](https://api.docs.bullmq.io/classes/v5.QueueEventsProducer.html)


# Telemetry

Enabling Telemetry for your BullMQ based applications

BullMQ provides a Telemetry interface that can be used to integrate it with any external telemetry backends. Currently we support the [OpenTelemetry](https://opentelemetry.io) specification, which is the new de-facto standard for telemetry purposes, however the interface if flexible enough to support any other backends in the future.

Telemetry is very useful for large applications where you want to get a detailed and general overview of the system. For BullMQ it helps to gain insight in the different statuses a job may be during its complete lifecycle. In a large application it helpts tracking the source of the jobs and all the interactions the jobs or messages may perform with other parts of the system.


# Getting started

In this guide we will show how to setup a local telemetry facility for BullMQ that should serve you as a good basis for how to integrate it in larger applications. As OpenTelemetry is a well supported standard there are many third party UIs for visualizing the traces and spans generated when running an application, for this guide we will use [Jaeger](https://www.jaegertracing.io).

We assume that you have a working BullMQ project that you want to add telemetry to it, so lets start by adding the `bullmq-otel` package to the project:

```
npm add --save bullmq-otel
```

This module provides a working implementation of BullMQ's telemetry interface for the OpenTelemetry standard. Adding it to your existing Queue's instances and Workers is quite straightforward:

```typescript
import { Queue } from 'bullmq'
import { BullMQOtel } from "bullmq-otel";

const queue = new Queue("myQueue", {
  connection: {
    host: "127.0.0.1",
    port: 6379,
  },
  telemetry: new BullMQOtel("simple-guide"),
});
```

```typescript
import { Worker } from "bullmq";
import { BullMQOtel } from "bullmq-otel";

const worker = new Worker(
  "myQueue",
  async (job) => {
    return 'some value'
  },
  {
    name: "myWorker",
    connection: {
      host: "127.0.0.1",
      port: 6379,
    },
    telemetry: new BullMQOtel("simple-guide"),
  }
);
```

This is all that is needed in order to start producing traces and spans to observe your code.


# Traces

BullMQ provides comprehensive distributed tracing support through OpenTelemetry. Traces allow you to track the flow of jobs through your system, identify bottlenecks, and debug issues across distributed services.

## Enabling Traces

To enable tracing, pass a telemetry instance when creating Queue, Worker, or FlowProducer:

```typescript
import { Queue, Worker } from 'bullmq';
import { BullMQOtel } from 'bullmq-otel';

const telemetry = new BullMQOtel({
  tracerName: 'my-app',
  version: '1.0.0',
});

const queue = new Queue('myQueue', {
  connection: {
    host: '127.0.0.1',
    port: 6379,
  },
  telemetry,
});

const worker = new Worker(
  'myQueue',
  async job => {
    return 'some value';
  },
  {
    connection: {
      host: '127.0.0.1',
      port: 6379,
    },
    telemetry,
  },
);
```

## Span Kinds

BullMQ uses different span kinds to categorize operations:

| Span Kind  | Description                                                         |
| ---------- | ------------------------------------------------------------------- |
| `PRODUCER` | Operations that add jobs to a queue (producing work)                |
| `CONSUMER` | Operations that process jobs from a queue (consuming work)          |
| `INTERNAL` | Internal operations like pausing, resuming, or managing queue state |

## Available Traces

BullMQ automatically creates spans for the following operations:

### Queue Class

| Operation                | Span Name                            | Span Kind | Description                          |
| ------------------------ | ------------------------------------ | --------- | ------------------------------------ |
| `add`                    | `{queueName}.add`                    | PRODUCER  | Adding a single job to the queue     |
| `addBulk`                | `{queueName}.addBulk`                | PRODUCER  | Adding multiple jobs to the queue    |
| `pause`                  | `{queueName}.pause`                  | INTERNAL  | Pausing the queue                    |
| `resume`                 | `{queueName}.resume`                 | INTERNAL  | Resuming the queue                   |
| `close`                  | `{queueName}.close`                  | INTERNAL  | Closing the queue connection         |
| `rateLimit`              | `{queueName}.rateLimit`              | INTERNAL  | Setting rate limit on the queue      |
| `removeRepeatable`       | `{queueName}.removeRepeatable`       | INTERNAL  | Removing a repeatable job by options |
| `removeRepeatableByKey`  | `{queueName}.removeRepeatableByKey`  | INTERNAL  | Removing a repeatable job by key     |
| `removeDebounceKey`      | `{queueName}.removeDebounceKey`      | INTERNAL  | Removing a debounce key              |
| `removeDeduplicationKey` | `{queueName}.removeDeduplicationKey` | INTERNAL  | Removing a deduplication key         |
| `remove`                 | `{queueName}.remove`                 | INTERNAL  | Removing a job from the queue        |
| `updateJobProgress`      | `{queueName}.updateJobProgress`      | INTERNAL  | Updating job progress                |
| `drain`                  | `{queueName}.drain`                  | INTERNAL  | Draining the queue                   |
| `clean`                  | `{queueName}.clean`                  | INTERNAL  | Cleaning jobs from the queue         |
| `obliterate`             | `{queueName}.obliterate`             | INTERNAL  | Obliterating the queue (all data)    |
| `retryJobs`              | `{queueName}.retryJobs`              | PRODUCER  | Retrying failed jobs                 |
| `promoteJobs`            | `{queueName}.promoteJobs`            | INTERNAL  | Promoting delayed jobs               |
| `trimEvents`             | `{queueName}.trimEvents`             | INTERNAL  | Trimming events from the queue       |

### Worker Class

| Operation                | Span Name                            | Span Kind | Description                            |
| ------------------------ | ------------------------------------ | --------- | -------------------------------------- |
| `getNextJob`             | `{queueName}.getNextJob`             | INTERNAL  | Fetching the next job to process       |
| `rateLimit`              | `{queueName}.rateLimit`              | INTERNAL  | Worker rate limiting                   |
| `processJob`             | `{queueName}.{jobName}`              | CONSUMER  | Processing a job (main processor span) |
| `pause`                  | `{queueName}.pause`                  | INTERNAL  | Pausing the worker                     |
| `resume`                 | `{queueName}.resume`                 | INTERNAL  | Resuming the worker                    |
| `close`                  | `{queueName}.close`                  | INTERNAL  | Closing the worker                     |
| `startStalledCheckTimer` | `{queueName}.startStalledCheckTimer` | INTERNAL  | Starting stalled job check timer       |
| `moveStalledJobsToWait`  | `{queueName}.moveStalledJobsToWait`  | INTERNAL  | Moving stalled jobs back to waiting    |
| `extendLocks`            | `{queueName}.extendLocks`            | INTERNAL  | Extending locks on active jobs         |

### Job Class

| Operation         | Span Name              | Span Kind | Description                                      |
| ----------------- | ---------------------- | --------- | ------------------------------------------------ |
| `moveToCompleted` | `{queueName}.complete` | INTERNAL  | Completing a job successfully                    |
| `moveToFailed`    | `{queueName}.{state}`  | INTERNAL  | Job failure handling (state: fail, delay, retry) |

### JobScheduler Class

| Operation | Span Name                        | Span Kind | Description               |
| --------- | -------------------------------- | --------- | ------------------------- |
| `add`     | `{queueName}.upsertJobScheduler` | PRODUCER  | Upserting a job scheduler |

### FlowProducer Class

| Operation | Span Name             | Span Kind | Description                        |
| --------- | --------------------- | --------- | ---------------------------------- |
| `add`     | `{queueName}.addFlow` | PRODUCER  | Adding a flow (tree of jobs)       |
| `addBulk` | `addBulkFlows`        | PRODUCER  | Adding multiple flows              |
| `addNode` | `{queueName}.addNode` | PRODUCER  | Adding a node in a flow (internal) |

## Trace Attributes

Traces include various attributes for filtering and debugging:

### Common Attributes

| Attribute       | Key                      | Description                       |
| --------------- | ------------------------ | --------------------------------- |
| Queue Name      | `bullmq.queue.name`      | Name of the queue                 |
| Queue Operation | `bullmq.queue.operation` | Type of operation being performed |

### Job Attributes

| Attribute               | Key                                     | Description                                    |
| ----------------------- | --------------------------------------- | ---------------------------------------------- |
| Job Name                | `bullmq.job.name`                       | Name of the job                                |
| Job ID                  | `bullmq.job.id`                         | Unique identifier of the job                   |
| Job Key                 | `bullmq.job.key`                        | Redis key of the job                           |
| Job IDs                 | `bullmq.job.ids`                        | Multiple job IDs (bulk ops)                    |
| Job Options             | `bullmq.job.options`                    | Serialized job options                         |
| Job Progress            | `bullmq.job.progress`                   | Current job progress value                     |
| Job Type                | `bullmq.job.type`                       | Type/state of the job                          |
| Job Attempts Made       | `bullmq.job.attempts.made`              | Number of attempts made                        |
| Job Result              | `bullmq.job.result`                     | Result returned by the job                     |
| Job Failed Reason       | `bullmq.job.failed.reason`              | Reason for job failure                         |
| Job Attempt Finished    | `bullmq.job.attempt_finished_timestamp` | When the processing attempt ended              |
| Job Finished Timestamp  | `bullmq.job.finished.timestamp`         | When the processing attempt ended (deprecated) |
| Job Processed Timestamp | `bullmq.job.processed.timestamp`        | When the job was processed                     |
| Deduplication Key       | `bullmq.job.deduplication.key`          | Deduplication key if set                       |

### Bulk Operation Attributes

| Attribute  | Key                     | Description                      |
| ---------- | ----------------------- | -------------------------------- |
| Bulk Count | `bullmq.job.bulk.count` | Number of jobs in bulk operation |
| Bulk Names | `bullmq.job.bulk.names` | Comma-separated job names        |

### Worker Attributes

| Attribute            | Key                                  | Description                     |
| -------------------- | ------------------------------------ | ------------------------------- |
| Worker Name          | `bullmq.worker.name`                 | Name of the worker              |
| Worker ID            | `bullmq.worker.id`                   | Unique identifier of the worker |
| Worker Options       | `bullmq.worker.options`              | Serialized worker options       |
| Worker Rate Limit    | `bullmq.worker.rate.limit`           | Rate limit duration             |
| Do Not Wait Active   | `bullmq.worker.do.not.wait.active`   | Whether to wait for active jobs |
| Force Close          | `bullmq.worker.force.close`          | Whether closing is forced       |
| Stalled Jobs         | `bullmq.worker.stalled.jobs`         | Number of stalled jobs detected |
| Failed Jobs          | `bullmq.worker.failed.jobs`          | Number of failed stalled jobs   |
| Jobs to Extend Locks | `bullmq.worker.jobs.to.extend.locks` | Jobs needing lock extension     |

### Queue Operation Attributes

| Attribute        | Key                             | Description                 |
| ---------------- | ------------------------------- | --------------------------- |
| Drain Delay      | `bullmq.queue.drain.delay`      | Whether to delay drain      |
| Grace Period     | `bullmq.queue.grace`            | Grace period for clean op   |
| Clean Limit      | `bullmq.queue.clean.limit`      | Maximum jobs to clean       |
| Rate Limit       | `bullmq.queue.rate.limit`       | Rate limit settings         |
| Queue Options    | `bullmq.queue.options`          | Serialized queue options    |
| Event Max Length | `bullmq.queue.event.max.length` | Maximum event stream length |

### Flow Attributes

| Attribute | Key                | Description      |
| --------- | ------------------ | ---------------- |
| Flow Name | `bullmq.flow.name` | Name of the flow |

### Scheduler Attributes

| Attribute        | Key                       | Description             |
| ---------------- | ------------------------- | ----------------------- |
| Job Scheduler ID | `bullmq.job.scheduler.id` | ID of the job scheduler |

## Context Propagation

BullMQ automatically propagates trace context when jobs are added and processed. This allows you to track jobs across services:

1. **Producer side**: When adding a job, the trace context is captured and stored with the job data
2. **Consumer side**: When processing a job, the trace context is extracted and used to continue the trace

### Controlling Context Propagation

You can control context propagation per job using the `telemetry` job option:

```typescript
// Include trace context (default behavior)
await queue.add('job', data);

// Explicitly include context
await queue.add('job', data, {
  telemetry: {
    omitContext: false,
  },
});

// Omit trace context (start fresh trace when processing)
await queue.add('job', data, {
  telemetry: {
    omitContext: true,
  },
});

// Provide custom metadata
await queue.add('job', data, {
  telemetry: {
    metadata: customContextData,
  },
});
```

## Exporting Traces

To export traces to an observability backend, configure an OpenTelemetry trace exporter:

```typescript
import { NodeTracerProvider } from '@opentelemetry/sdk-trace-node';
import { SimpleSpanProcessor } from '@opentelemetry/sdk-trace-base';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http';
import { trace } from '@opentelemetry/api';

// Configure the trace exporter
const traceExporter = new OTLPTraceExporter({
  url: 'http://localhost:4318/v1/traces',
});

const provider = new NodeTracerProvider();
provider.addSpanProcessor(new SimpleSpanProcessor(traceExporter));
provider.register();

// Now BullMQOtel will automatically use the registered provider
```

## Example Trace Visualization

When properly configured, you can see traces in your observability platform showing the complete lifecycle of jobs:

```
├─ myQueue.add (PRODUCER)
│  └─ myQueue.myJob (CONSUMER)
│     └─ myQueue.complete (INTERNAL)
```

For flows with parent-child relationships:

```
├─ myQueue.addFlow (PRODUCER)
│  ├─ childQueue.addNode (PRODUCER)
│  │  └─ childQueue.childJob (CONSUMER)
│  │     └─ childQueue.complete (INTERNAL)
│  └─ parentQueue.addNode (PRODUCER)
│     └─ parentQueue.parentJob (CONSUMER)
│        └─ parentQueue.complete (INTERNAL)
```


# Metrics

In addition to traces, BullMQ also supports collecting metrics through OpenTelemetry. Metrics provide quantitative data about your job processing, such as counts of completed/failed jobs and processing durations.

## Enabling Metrics

To enable metrics collection, pass the `enableMetrics` option when creating the `BullMQOtel` instance:

```typescript
import { Queue } from 'bullmq';
import { BullMQOtel } from 'bullmq-otel';

const telemetry = new BullMQOtel({
  tracerName: 'my-app',
  meterName: 'my-app',
  version: '1.0.0',
  enableMetrics: true,
});

const queue = new Queue('myQueue', {
  connection: {
    host: '127.0.0.1',
    port: 6379,
  },
  telemetry,
});
```

```typescript
import { Worker } from 'bullmq';
import { BullMQOtel } from 'bullmq-otel';

const telemetry = new BullMQOtel({
  tracerName: 'my-app',
  meterName: 'my-app',
  version: '1.0.0',
  enableMetrics: true,
});

const worker = new Worker(
  'myQueue',
  async job => {
    return 'some value';
  },
  {
    connection: {
      host: '127.0.0.1',
      port: 6379,
    },
    telemetry,
  },
);
```

## Available Metrics

BullMQ automatically records the following metrics:

### Counters

| Metric Name                    | Description                                                    |
| ------------------------------ | -------------------------------------------------------------- |
| `bullmq.jobs.completed`        | Number of jobs that completed successfully                     |
| `bullmq.jobs.failed`           | Number of jobs that failed (after all retries exhausted)       |
| `bullmq.jobs.delayed`          | Number of jobs moved to delayed state (including retry delays) |
| `bullmq.jobs.retried`          | Number of jobs that were retried immediately                   |
| `bullmq.jobs.waiting`          | Number of jobs moved back to waiting state                     |
| `bullmq.jobs.waiting_children` | Number of jobs moved to waiting-children state                 |

### Histograms

| Metric Name           | Description             | Unit         |
| --------------------- | ----------------------- | ------------ |
| `bullmq.job.duration` | Job processing duration | milliseconds |

### Gauges

| Metric Name         | Description                          | Unit     |
| ------------------- | ------------------------------------ | -------- |
| `bullmq.queue.jobs` | Number of jobs in the queue by state | `{jobs}` |

Gauges are recorded when calling `recordJobCountsMetric()`. The `bullmq.queue.jobs` gauge includes a `bullmq.queue.jobs.state` attribute indicating which job state was counted (e.g., `waiting`, `active`, `completed`, `failed`, `delayed`, `prioritized`, `paused`, `waiting-children`).

## Metric Attributes

Different metrics include different attributes for filtering and grouping:

### Common Attributes (all metrics)

| Attribute           | Description       |
| ------------------- | ----------------- |
| `bullmq.queue.name` | Name of the queue |

### Job Metric Attributes (counters and histograms only)

| Attribute           | Description                                                                        |
| ------------------- | ---------------------------------------------------------------------------------- |
| `bullmq.job.name`   | Name of the job                                                                    |
| `bullmq.job.status` | Status of the job (completed, failed, delayed, retried, waiting, waiting-children) |

### Gauge Attributes (`bullmq.queue.jobs` only)

| Attribute                 | Description                                                            |
| ------------------------- | ---------------------------------------------------------------------- |
| `bullmq.queue.jobs.state` | Job state for gauge metrics (waiting, active, completed, failed, etc.) |

## Configuration Options

The `BullMQOtel` constructor accepts the following options:

```typescript
interface BullMQOtelOptions {
  /**
   * Name for the tracer (default: 'bullmq')
   */
  tracerName?: string;

  /**
   * Name for the meter (default: 'bullmq')
   */
  meterName?: string;

  /**
   * Version string for both tracer and meter
   */
  version?: string;

  /**
   * Enable metrics collection. When true, a meter will be created
   * to record job metrics like completed/failed counts and durations.
   * @default false
   */
  enableMetrics?: boolean;
}
```

## Custom Metric Options

BullMQOtel allows you to pre-configure counters, histograms, and gauges with custom options before passing the telemetry instance to a Worker or Queue. Once a metric is created with custom options, BullMQ will reuse it and the default options defined internally will be ignored.

This is useful when you want to customize metric descriptions, units, or other OpenTelemetry metric options:

```typescript
import { BullMQOtel } from 'bullmq-otel';
import { Queue, Worker } from 'bullmq';

const telemetry = new BullMQOtel({
  tracerName: 'my-app',
  meterName: 'my-app',
  version: '1.0.0',
  enableMetrics: true,
});

// Pre-configure a counter with custom options
// This will be reused by BullMQ, ignoring its default options
telemetry.meter.createCounter('bullmq.jobs.completed', {
  description: 'Custom description for completed jobs',
  unit: '1',
});

// Pre-configure the duration histogram with custom options
telemetry.meter.createHistogram('bullmq.job.duration', {
  description: 'Custom job processing duration',
  unit: 's', // Using seconds instead of default milliseconds
});

// Pre-configure a gauge for queue job counts
telemetry.meter.createGauge('bullmq.queue.jobs', {
  description: 'Current number of jobs in the queue by state',
  unit: '{jobs}',
});

const queue = new Queue('myQueue', {
  connection: {
    host: '127.0.0.1',
    port: 6379,
  },
  telemetry,
});

const worker = new Worker(
  'myQueue',
  async job => {
    return 'some value';
  },
  {
    connection: {
      host: '127.0.0.1',
      port: 6379,
    },
    telemetry,
  },
);

// When calling recordJobCountsMetric(), gauge metrics are recorded
const jobCounts = await queue.recordJobCountsMetric();
```

{% hint style="info" %}
The `BullMQOTelMeter` caches all created counters, histograms, and gauges by name. When BullMQ internally calls `createCounter`, `createHistogram`, or `createGauge` with the same name, the cached instance is returned, effectively ignoring the default options passed by BullMQ.
{% endhint %}

## Backward Compatibility

The original constructor signature is still supported for backward compatibility:

```typescript
// Old style (traces only)
const telemetry = new BullMQOtel('my-app', '1.0.0');

// New style with options object (traces + optional metrics)
const telemetry = new BullMQOtel({
  tracerName: 'my-app',
  version: '1.0.0',
  enableMetrics: true,
});
```

## Exporting Metrics

To export metrics to an observability backend, you need to configure an OpenTelemetry metrics exporter. Here's an example using the OTLP exporter:

```typescript
import {
  MeterProvider,
  PeriodicExportingMetricReader,
} from '@opentelemetry/sdk-metrics';
import { OTLPMetricExporter } from '@opentelemetry/exporter-metrics-otlp-http';
import { metrics } from '@opentelemetry/api';

// Configure the metrics exporter
const metricExporter = new OTLPMetricExporter({
  url: 'http://localhost:4318/v1/metrics',
});

const meterProvider = new MeterProvider({
  readers: [
    new PeriodicExportingMetricReader({
      exporter: metricExporter,
      exportIntervalMillis: 10000, // Export every 10 seconds
    }),
  ],
});

// Set the global meter provider
metrics.setGlobalMeterProvider(meterProvider);

// Now create your BullMQ instances with metrics enabled
const telemetry = new BullMQOtel({
  tracerName: 'my-app',
  enableMetrics: true,
});
```

{% hint style="info" %}
Make sure to set up the meter provider before creating BullMQ instances with telemetry enabled.
{% endhint %}


# Running Jaeger

The easiest way to run Jaeger is by using Docker compose. If you have docker installed, it is a matter of running this docker-compose.yaml file:

```yaml
services:
  jaeger:
    image: jaegertracing/all-in-one:latest
    container_name: BullMQ_with_opentelemetry_jaeger
    ports:
      - '4318:4318'
      - '16686:16686'

```

Note that we need to expose 2 ports here, the first (4318) one is the endpoint to export our traces and the second one (16686) is our UI.

You can now just run this service with:

```
docker-compose up
```

In a few seconds the image will be up and running. You can verify that is working by opening a browser window and pointing it to [http://localhost:16686](http://localhost:16686/search)

As no traces has been created yet you will get a quite empty dashboard:

<figure><img src="https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-b6d84aedee561e5f859913f40391c6938c23cfab%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>


# Running a simple example

### Creating a producer

For this simple example we will create a producer that will add a couple of jobs, but it will add them in bulks instead of one by one, this will help us demonstrate how spans are linked between the consumers and the producers:

{% code title="producer.ts" %}

```typescript
import { Queue } from "bullmq";
import { BullMQOtel } from "bullmq-otel";

const queue = new Queue("myQueue", {
  connection: {
    host: "127.0.0.1",
    port: 6379,
  },
  telemetry: new BullMQOtel("simple-guide"),
});

const jobsBulk = Array.from({ length: 5 }, (_, i) => i);

(async () => {
  for (let i = 0; i < 10; i++) {
    await queue.addBulk(
      jobsBulk.map((j) => ({
        name: `myJob ${j}`,
        data: { i: j },
        opts: { attempts: 2, backoff: 1000 },
      }))
    );
  }
})();
```

{% endcode %}

### Creating a consumer

The consumer will be just a simple instance, we will use concurrency 10, so that jobs can be processed concurrently, and therefore create overlapping spans. We will also simulate jobs failures so that we can get retries, to show how spans are generated as the job gets failed, retried and finally completed:

{% code title="consumer.ts" %}

```typescript
import { Worker } from "bullmq";
import { BullMQOtel } from "bullmq-otel";

(async () => {
  const worker = new Worker(
    "myQueue",
    async (job) => {
      console.log("processing job", job.id, job.attemptsMade);
      await new Promise(async (res) => {
        setTimeout(() => res({}), 200);
      });

      if (job.attemptsMade < 1) {
        throw new Error("This was an error");
      }

      return "my result value";
    },
    {
      name: "myWorker",
      connection: {
        host: "127.0.0.1",
        port: 6379,
      },
      telemetry: new BullMQOtel("simple-guide"),
      concurrency: 10,
    }
  );
})();
```

{% endcode %}

### Creating the instrumentation files

To test the telemetry functionality we can run a simple example. For that we also need to instantiate the OpenTelemetry SDK using a so called OpenTelemetry Protocol (OTLP) exporter.

We must install the following modules that are part of the OpenTelemetry SDK:

```
npm install @opentelemetry/exporter-trace-otlp-proto \
  @opentelemetry/exporter-metrics-otlp-proto
```

And now we must create so called "instrumentation" files. We will create one for our "producer" service, which is the service actually taking care of producing jobs, it will look like this. Note that we use localhost (127.0.0.1) where our jaeger service is running:

{% code title="producer.inst.otlp.ts" %}

```typescript
import { NodeSDK } from '@opentelemetry/sdk-node';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-proto';
import { OTLPMetricExporter } from '@opentelemetry/exporter-metrics-otlp-proto';
import { PeriodicExportingMetricReader } from '@opentelemetry/sdk-metrics';

const sdk = new NodeSDK({
  serviceName: 'producer',
  traceExporter: new OTLPTraceExporter({
    url: 'http://127.0.0.1:4318/v1/traces'
  }),
  metricReader: new PeriodicExportingMetricReader({
    exporter: new OTLPMetricExporter({
      url: 'http://127.0.0.1:4318/v1/metrics'
    }),
  }),
});

sdk.start();
```

{% endcode %}

Likewise we will create another instrumentation file for our "consumer" service, this is where the workers will run and consume the jobs produced by the "Queue" instance:

{% code title="consumer.inst.otlp.ts" %}

```typescript
import { NodeSDK } from '@opentelemetry/sdk-node';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-proto';
import { OTLPMetricExporter } from '@opentelemetry/exporter-metrics-otlp-proto';
import { PeriodicExportingMetricReader } from '@opentelemetry/sdk-metrics';

const sdk = new NodeSDK({
  serviceName: 'consumer',
  traceExporter: new OTLPTraceExporter({
    url: 'http://127.0.0.1:4318/v1/traces'
  }),
  metricReader: new PeriodicExportingMetricReader({
    exporter: new OTLPMetricExporter({
      url: 'http://127.0.0.1:4318/v1/metrics'
    }),
  }),
});

sdk.start();
```

{% endcode %}

Both services looks basically the same, just the service name will differ in this case.

### Launching the services

In order to guarantee that the OpenTelemetry instrumentation is run first, before everything else, and performs any required internal patching (even though BullMQ does not rely on patching other modules may do), we need to launch it like this (note that we use tsx in this example but Node runtime will do as well:

```
tsx --import producer.inst.otlp.ts producer.ts
tsx --import consumer.inst.otlp.ts consumer.ts
```

{% hint style="info" %}
You can also use Node runtime directly if you are using javascript (or building from Typescript to javascript): `node --import producer.inst.otlp.js producer.js`
{% endhint %}

As the services are launched we will see that the consumers starts processing the jobs and produce some logs on the console:

```
> tsx --import consumer.inst.otlp.ts consumer.ts

processing job 1 0
processing job 2 0
processing job 3 0
processing job 4 0
processing job 5 0
processing job 6 0
...
processing job 43 1
processing job 44 1
processing job 45 1
processing job 46 1
processing job 47 1
processing job 48 1
processing job 49 1
processing job 50 1
```

These are just the logs that we wrote ourselves on the "process" function in our worker, so nothing special here. However if we go to Jaeger we will find the following:

<figure><img src="https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-d7aa018eb4f0700b7d3a940fc7665693e46dd4a3%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

We have now 2 services to choose from, consumer and producer. If we search for traces in the producer we will be able to see all the traces where the producer is involved:

<figure><img src="https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-c7c1340ba53ba9197045d49ae55b0c1a6af4f287%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

Here we can see as even though we are searching for the producer traces, we also get the consumer spans, and this is because jobs are linked between producers and consumers, so that we can trace all the way from the creation of a job to its final processing.

If we look into the consumer spans for example, there are some interesting things to see:

<figure><img src="https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-7d53b02677bd41f82b0e3e67d09b9c558a1232ec%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

First of all, note how the producer span "addBulk myQueue", is the root of this trace. Since this was an addBulk, it means that several jobs were added to the queue in one go, 5 in this case. So the spans created by the consumer are therefore linked to this one producer span. The consumer spans "process myQueue" are generated for every job that is being processed, and since we had a concurrency factor larger than 5, all 5 jobs are processed concurrently, which we can see in the spans all starting at the same time.

But we also forced the jobs to fail 1 time, so that they would be retried with a small backoff (delay), which is why we can see a "delay myQueue" span and then a final "process myQueue" span.

If we open the spans we can find other useful information:

<figure><img src="https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-31a8a702b6c3ecbc6d167a54225837a08410be5e%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

We have some useful tags related to this particular job, and also logs that shows events that happened during the span lifetime, for instance here we can see that the job failed with the given error message.

If we go to the last span of the trace we can see that the job was finally completed after being delayed a bit before its last retry:

<figure><img src="https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-656753225f7817cf8989d26e84a0ff30cfc7c819%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>


# QueueScheduler

{% hint style="danger" %}
The `QueueScheduler` is deprecated from BullMQ 2.0 and onwards. The information below is only relevant for older versions.
{% endhint %}

The `QueueScheduler` is a helper class used to manage stalled and delayed jobs for a given Queue.

```typescript
import { QueueScheduler } from 'bullmq';

const queueScheduler = new QueueScheduler('test');

// Later, when shuting down gracefully
await queueScheduler.close();
```

This class automatically moves delayed jobs back to the waiting queue when it is the right time to process them. It also automatically checks for stalled jobs (i.e. detects jobs that are active but where the worker has either crashed or stopped working properly). [Stalled jobs](https://docs.bullmq.io/guide/jobs/stalled) are moved back or failed depending on the settings selected when instantiating the class.

{% hint style="info" %}
You need at least one `QueueScheduler` running somewhere for a given queue if you require functionality such as delayed jobs, retries with backoff, and rate limiting.
{% endhint %}

The reason for having this functionality in a separate class instead of in the workers (as in Bull 3.x) is because whereas you may want to have a large number of workers for parallel processing, for the scheduler you probably only want a couple of instances for each queue that requires delayed or stalled checks. One will be enough but you can have more just for redundancy.

{% hint style="warning" %}
It is ok to have as many `QueueScheduler` instances as you want, just keep in mind that every instance will perform some bookkeeping so it may create some noticeable CPU and IO usage in your Redis instances.
{% endhint %}

## Read more:

* 💡 [Queue Scheduler API Reference](https://api.docs.bullmq.io/classes/v1.QueueScheduler.html)


# Redis™ Compatibility

There are several alternatives for Redis and even though BullMQ is full Redis™ compliant with version 6.2.0 or newer, not all the alternatives are going to work properly. In this section we present the vendors that officially support BullMQ and that we regularly test to verify they keep staying compatible.


# Dragonfly

[Dragonfly](https://www.dragonflydb.io/) offers a drop-in replacement for Redis™, boasting a much faster and more memory-efficient implementation of several data structures used by BullMQ. It also enables the utilization of all available cores in your CPUs. Check [this article](https://bullmq.io/news/101023/dragonfly-compatibility/) for some performance results.

To fully leverage Dragonfly's capabilities, specific steps are necessary. Primarily, you should name your queues using curly braces. This naming convention allows Dragonfly to assign a thread to each queue. For instance, if your queue is named `myqueue,`rename it to `{myqueue}`.

If you manage multiple queues, this approach enables you to allocate different CPU cores to each queue, significantly enhancing performance. Even with a single queue, you can still exploit multi-core advantages in some cases. Consider splitting your queue into multiple ones, like`{myqueue-1}`, `{myqueue-2}`, etc., and distribute jobs randomly or using a round-robin method.

{% hint style="info" %}
Be aware that certain features like priorities and rate-limiting might not function across multiple queues. Your specific requirements will determine whether you can divide a single queue in this manner.
{% endhint %}

For comprehensive instructions and the necessary flags to optimize your Dragonfly instance for BullMQ, please consult the [official integration guide](https://www.dragonflydb.io/docs/integrations/bullmq).


# Redis™ hosting

For BullMQ you are going to need a proper Redis™ hosting solution. In this section we provide instructions on how to use some of the most popular ones.


# AWS MemoryDB

AWS provides a Redis™ 7 compatible managed database that is easy to use and is fully compatible with BullMQ.

There are some considerations to take care when using MemoryDB though.

* MemoryDB only works in Cluster mode. So you need to use "hash tags" so that the queues get attached to a given cluster node ([read more here](https://docs.bullmq.io/bull/patterns/redis-cluster)).
* MemoryDB can only be accessed within an AWS VPC, so you cannot access the Redis™ cluster outside of AWS.

The easiest way to use MemoryDB with BullMQ is to first instantiate a IORedis Cluster instance, and then use that connection as an option to your workers or queue instances, for example:

```typescript
import { Cluster } from 'ioredis';
import { Worker } from 'bullmq';

const connection = new Cluster(
  [
    {
      host: 'clustercfg.xxx.amazonaws.com',
      port: 6379,
    },
  ],
  {
    tls: {},
  },
);

const worker = new Worker(
  'myqueue',
  async (job: Job) => {
    // Do some usefull stuff
  },
  { connection },
);

// ...

// Do not forget to close the connection as well as the worker when shutting down
await worker.close();
await connection.quit();
```


# AWS Elasticache

Elasticache is a managed caching service offered by Amazon Web Services (AWS), and it can be a good option when using BullMQ within the AWS infrastructure.

Here are some points to consider when using Elasticache with BullMQ within AWS:

1. Use the standard cache-nodes setup (i.e. not the serverless version, as serverless for the moment uses an incompatible maxmemory-policy)
2. In order to access your Elasticache instance you will need to create a security group that allows the instance to be accessible to the services running BullMQ instances.
3.

<figure><img src="https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-b5e688395c2061a69a970890d35e77fa217a460a%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

4\. You will need to specify a VPC and an Inbound rule. Most likely just a custom TCP with port range 6379 and some suitable source (anywhere works well for testing and in some simpler cases), remember that the cluster will not be accessible outside from AWS in any case. 5. Attach the security group to your Elasticache cluster and to the services that need to access it. 6. Make sure that you are using maxmemory-policy: noeviction in your Redis parameters. As you cannot modify any default parameter group you will need to create a new one.

```
1. Go to Elasticache > Parameter Groups and click on Create.
2. Fill name, description, and Family, at the time of writing redis7 is the newest and the recommended one.

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>
```

7\. Click on "Create". Then find the parameter group in the list. Click on Edit parameter values and then search for maxmemory-policy:

<figure><img src="https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-6305ad6bc21de4aa7e6e56ea7d8ee9772d895226%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

8. Change the value to "noeviction":

<figure><img src="https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-556e6c2decabcb31969d8e0913077e2ba118142b%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

9. Save changes. Now you can go to your elasticache cluster and change the parameter group to your custom group. Just find your instance, click on modify and go to cluster settings where you can change the parameter group:

<figure><img src="https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-837ae979da2ee9a9ed1405a576068d3dfbab2ea9%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

10. Preview changes and Modify. After this your cluster is ready to be used with BullMQ.


# Architecture

In this page we give an architecture overview on how BullMQ is implemented on top of Redis.

In order to use the full potential of Bull queues, it is important to understand the lifecycle of a job. From the moment a producer calls the [`add`](https://api.docs.bullmq.io/classes/v5.Queue.html#add) method on a `Queue` instance, a job enters a lifecycle where it will be in different states, until its completion or failure (although technically a failed job could be retried and get a new lifecycle).

<figure><img src="https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-8ccf86e0633ddb1016f5f56af5dbe0decc412aa3%2Fsimple-architecture.png?alt=media" alt="Diagram showing the lifecycle of a job in a queue, including wait, prioritized, delayed, active, completed, and failed states"><figcaption><p>Lifecycle of a job - Queue</p></figcaption></figure>

When a job is added to a queue it can be in one of three states:

* **“wait”**: a waiting list, where all jobs must enter before they can be processed.
* **“prioritized”**: implies that a job with higher priority will be processed first.
* **“delayed”**: implies that the job is waiting for some timeout or to be promoted for being processed. These jobs are not processed directly, but instead are placed at the beginning of the waiting list, or in a prioritized set, and processed as soon as a worker is idle.

{% hint style="warning" %}
Note that priorities go from `0` to `2^21`, where 0 is the highest priority. This follows a similar standard as processed in Unix (<https://en.wikipedia.org/wiki/Nice\\_(Unix)>, where a higher number means less priority).
{% endhint %}

The next state for a job is the **“active”** state. The active state is represented by a set, and are jobs that are currently being processed (i.e. they are running in the `process` function explained in the previous chapter). A job can be in the active state for an unlimited amount of time until the process is completed or an exception is thrown so that the job will end in either the **“completed”** or the **“failed”** status.

Another way to add a job is by the [`add`](https://api.docs.bullmq.io/classes/v5.FlowProducer.html#add) method on a flow producer instance.

<figure><img src="https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-72f32539e4167247ee0da7bcae189dc085ea6ec2%2Fflow-architecture.png?alt=media" alt="Diagram showing the lifecycle of a job in a flow producer, including wait, prioritized, delayed, waiting-children, active, completed, and failed states"><figcaption><p>Lifecycle of a job - Flow Producer</p></figcaption></figure>

When a job is added by a flow producer, it can be in one of three states, it can either be in the **“wait”** or **“prioritized“** or **“delayed“** status, when there aren't children, or it can be in a **“waiting-children”** status: a waiting-children status implies that the job is waiting for all its children to be completed, however, a waiting-children job will not be processed directly, instead it will be placed at the waiting list or at delayed set (if `delay` is provided) or at prioritized set (if `delay` is 0 and `priority` is greater than 0) as soon as the last child is marked as completed.


# NestJs

There is a compatible module to be used in [NestJs](https://github.com/nestjs/nest).

```bash
npm i @nestjs/bullmq
```

Once the installation process is complete, we can import the **`BullModule`** into the root **`AppModule`**.

```typescript
import { Module } from '@nestjs/common';
import { BullModule } from '@nestjs/bullmq';

@Module({
  imports: [
    BullModule.forRoot({
      connection: {
        host: 'localhost',
        port: 6379,
      },
    }),
  ],
})
export class AppModule {}
```

To register a queue, import the **`BullModule.registerQueue()`** dynamic module, as follows:

```typescript
BullModule.registerQueue({
  name: 'queueName',
});
```

To register a flow producer, import the **`BullModule.registerFlowProducer()`** dynamic module, as follows:

```typescript
BullModule.registerFlowProducer({
  name: 'flowProducerName',
});
```

## Processor

To register a processor, you may need to use the **`Processor`** decorator:

```typescript
import { Processor, WorkerHost, OnWorkerEvent } from '@nestjs/bullmq';
import { Job } from 'bullmq';

@Processor('queueName')
class TestProcessor extends WorkerHost {
  async process(job: Job<any, any, string>): Promise<any> {
    // do some stuff
  }

  @OnWorkerEvent('completed')
  onCompleted() {
    // do some stuff
  }
}
```

And then register it as a provider:

```typescript
@Module({
  imports: [
    BullModule.registerQueue({
      name: 'queueName',
      connection: {
        host: '0.0.0.0',
        port: 6380,
      },
    }),
    BullModule.registerFlowProducer({
      name: 'flowProducerName',
      connection: {
        host: '0.0.0.0',
        port: 6380,
      },
    }),
  ],
  providers: [TestProcessor],
})
export class AppModule {}
```

### Read more:

* 💡 [Queues Technique](https://docs.nestjs.com/techniques/queues)


# Producers

Job producers add jobs to queues. Producers are typically application services (Nest providers). To add jobs to a queue, first inject the queue into the service as follows:

```typescript
import { Injectable } from '@nestjs/common';
import { InjectQueue } from '@nestjs/bullmq';
import { Queue } from 'bullmq';

@Injectable()
export class AudioService {
  constructor(@InjectQueue('audio') private audioQueue: Queue) {}
}
```

{% hint style="info" %}
The **`@InjectQueue()`** decorator identifies the queue by its name, as provided in the **`registerQueue()`**.
{% endhint %}

Now, add a job by calling the queue's add() method.

```typescript
const job = await this.audioQueue.add('sample', {
  foo: 'bar',
});
```

## Flow Producers

To add flows, first inject the flow producer into the service as follows:

```typescript
import { Injectable } from '@nestjs/common';
import { InjectFlowProducer } from '@nestjs/bullmq';
import { FlowProducer } from 'bullmq';

@Injectable()
export class FlowService {
  constructor(
    @InjectFlowProducer('flow') private fooFlowProducer: FlowProducer,
  ) {}
}
```

{% hint style="info" %}
The **`@InjectFlowProducer()`** decorator identifies the flow producer by its `name`, as provided in the **`registerFlowProducer()`**.
{% endhint %}

Now, add a flow by calling the flow producer's \`add()\`\` method.

```typescript
const job = await this.fooFlowProducer.add({
  name: 'root-job',
  queueName: 'topQueueName',
  data: {},
  children: [
    {
      name,
      data: { idx: 0, foo: 'bar' },
      queueName: 'childrenQueueName',
    },
  ],
});
```

### Read more:

* 💡 [Queues Technique](https://docs.nestjs.com/techniques/queues)


# Queue Events Listeners

To register a QueueEvents instance, you need to use the **`QueueEventsListener`** decorator:

```typescript
import {
  QueueEventsListener,
  QueueEventsHost,
  OnQueueEvent,
} from '@nestjs/bullmq';

@QueueEventsListener('queueName')
export class TestQueueEvents extends QueueEventsHost {
  @OnQueueEvent('completed')
  onCompleted({
    jobId,
  }: {
    jobId: string;
    returnvalue: string;
    prev?: string;
  }) {
    // do some stuff
  }
}
```

And then register it as a provider:

```typescript
@Module({
  imports: [
    BullModule.registerQueue({
      name: 'queueName',
      connection: {
        host: '0.0.0.0',
        port: 6380,
      },
    }),
  ],
  providers: [TestQueueEvents],
})
export class AppModule {}
```

## Read more:

* 💡 [Queues Technique](https://docs.nestjs.com/techniques/queues)
* 💡 [Register Queue API Reference](https://nestjs.bullmq.pro/classes/BullModule.html#registerQueue)
* 💡 [Queue Events Listener API Reference](https://api.docs.bullmq.io/interfaces/v5.QueueEventsListener.html)


# Going to production

In this chapter, we will offer crucial considerations and tips to help you achieve a robust solution when deploying your BullMQ-based application to production.

### Persistence

Since BullMQ is based on Redis, persistence needs to be configured manually. Many hosting solutions do not offer persistence by default; instead, it needs to be configured per instance. We recommend enabling [AOF (*Append Only File*)](https://redis.io/docs/management/persistence/#aof-advantages), which provides a robust and fast solution. Usually, 1 second per write is enough for most applications.

Even though persistence is very fast, it will have some effect on performance, so please make the proper benchmarks to know that it is not impacting your solution in a way that is not acceptable to you.

### Max memory policy

Redis is used quite often as a cache, meaning that it will remove keys according to some defined policy when it reaches several levels of memory consumption. BullMQ on the other hand cannot work properly if Redis evicts keys arbitrarily. **Therefore is very important to configure the `maxmemory-policy` setting to `noeviction`.** This is the **only** setting that guarantees the correct behavior of the queues.

### Automatic reconnections

In a production setting, one of the things that are crucial for system robustness is to be able to recover automatically after connection issues. It is impossible to guarantee that a connection between BullMQ and Redis will always stay online. However, the important thing is that it recovers as fast as possible when the connection can be re-established without any human intervention.

In order to understand how to properly handle disconnections it is important to understand some options provided by [IORedis](https://www.npmjs.com/package/ioredis#Auto-reconnect). The ones interesting for us are:

* `retryStrategy`
* `maxRetriesPerRequest`
* `enableOfflineQueue`

It is also important to understand the difference in behavior that is often desired for `Queue` and `Worker` classes. Normally the operations performed using the `Queue` class should [fail quickly](https://docs.bullmq.io/patterns/failing-fast-when-redis-is-down) if there is a temporal disconnection, whereas for `Worker`s we want to wait indefinitely without raising any exception.

#### `retryStrategy`

This option is used to determine the function used to perform retries. The retries will continue forever until the reconnection has been accomplished. For IORedis connections created inside BullMQ we use the following strategy:

```ts
 retryStrategy: function (times: number) {
    return Math.max(Math.min(Math.exp(times), 20000), 1000);
 }
```

In other words, it will retry using exponential backoff, with a minimum 1-second retry time and max of 20 seconds. This `retryStrategy` can easily be overridden by passing a custom one defining custom IORedis options.

#### `maxRetriesPerRequest`

This option sets a limit on the number of times a retry on a failed request will be performed. For `Worker`s, it is important to set this option to **`null`**. Otherwise, the exceptions raised by Redis when calling certain commands could break the worker functionality. When instantiating a `Worker` this option will always be set to `null` by default, but it could be overridden, either if passing an existing IORedis instance or by passing a different value for this option when instantiating the `Worker`. In both cases BullMQ will output a warning; please make sure to address this warning as it can have several unintended consequences.

#### `enableOfflineQueue`

IORedis provides a small offline queue that is used to queue commands while the connection is offline. You will probably want to disable this queue for the `Queue` instance, but leave it as is for `Worker` instances. That will make the `Queue` calls [fail quickly](https://docs.bullmq.io/patterns/failing-fast-when-redis-is-down) while leaving the `Worker`s to wait as needed until the connection has been re-established.

### Log errors

It is really useful to attach a handler for the error event which will be triggered when there are connection issues. This will be helpful when debugging your queues and prevent "unhandled errors".

```typescript
worker.on("error", (err) => {
  // Log your error.
})
```

```typescript
queue.on("error", (err) => {
  // Log your error.
})
```

### Gracefully shut-down workers

Since your workers will run on servers, it is unavoidable that these servers will need to be restarted from time to time. As your workers may be processing jobs when the server is about to restart, it is important to properly close the workers to minimize the risk of stalled jobs. If a worker is killed without waiting for their jobs to complete, these jobs will be marked as stalled and processed automatically when new workers come online (with a waiting time of about 30 seconds by default). However it is better to avoid having stalled jobs, and as mentioned this can be done by closing the workers when the server is going to be restarted.

In a Node.js server, it is considered good practice to listen for both `SIGINT` and `SIGTERM` signals to close gracefully. Here's why:

* `SIGINT` is typically sent when a user types Ctrl+C in the terminal to interrupt a process. Your server should listen to this signal during development or when it's running in the foreground, so you can shut it down properly when this key combination is pressed.
* `SIGTERM` is the signal that is usually sent to a process to request its termination. Unlike `SIGKILL`, this signal can be caught by the process (which can then clean up resources and exit gracefully). This is the signal that system daemons, orchestration tools like Kubernetes, or process managers like PM2 typically use to stop a service.

Here is an example on how you accomplish this:

```typescript

const gracefulShutdown = async (signal) => {
  console.log(`Received ${signal}, closing server...`);
  await worker.close();
  // Other asynchronous closings
  process.exit(0);
}

process.on('SIGINT', () => gracefulShutdown('SIGINT'));

process.on('SIGTERM', () => gracefulShutdown('SIGTERM'));

```

Keep in mind that the code above does not guarantee that the jobs will never end up being stalled, as the job may take longer time than the grace period for the server to restart.

### Auto-job removal

By default, all jobs processed by BullMQ will be either *completed*, or *failed* and kept forever. This behavior is not usually the most desired, so you will likely want to configure a maximum number of jobs to keep. The most common configuration is to keep a handful of completed jobs, just to have some visibility of the latest completed, whereas you can keep either all of the failed jobs or a very large number in case you want to manually retry them or perform a deeper debugging study on the reason why the jobs failed.

You can read more about how to configure auto removal [here](https://docs.bullmq.io/guide/queues/auto-removal-of-jobs).

### Protecting data

Another important point to think about when deploying for production is the fact that the data field of the jobs is stored in clear text. **The best is to avoid storing sensitive data in the job altogether.** However, if this is not possible, then it is highly recommended to encrypt the part of the data that is sensitive before it is added to the queue.

**Please do not take security lightly as it should be a major concern today, and the risks of losing data and economic damage to your business are real and very serious.**

### Unhandled exceptions and rejections

Another common issue, especially in production environments, is the fact that NodeJS by default will break if there are unhandled exceptions. This is not unique for BullMQ-based applications, but a general rule for all NodeJS applications. We recommend that somewhere in your service you make sure that you handle the unhandled exceptions gracefully, and so you can fix them when they arise without any risk of the application breaking when they happen:

```typescript
process.on("uncaughtException", function (err) {
  // Handle the error safely
  logger.error(err, "Uncaught exception");
});

process.on("unhandledRejection", (reason, promise) => {
  // Handle the error safely
  logger.error({ promise, reason }, "Unhandled Rejection at: Promise");
});
```


# Migrations

Tips and hints on how to migrate your current BullMQ version to a newer one.

BullMQ's team regularly releases new versions packed with bug fixes, new features, or occasionally, breaking changes. As a user operating in a production environment, you might find upgrading to these new versions while maintaining service continuity challenging. This guide offers tips and advice to ease your transition.

The strategies needed vary depending on the nature of the upgrade. Regardless, we urge you to read this guide thoroughly, irrespective of the upgrade you're pursuing.

## General advice

When upgrading BullMQ, always consult the *Changelog*. It helps determine the extent of the changes and flags crucial considerations before upgrading.

Avoid making large leaps between versions. If you're currently on version 1.3.7, for instance, a jump to version 4.2.6 may not be advisable. Upgrade incrementally whenever possible. Start with as many bugfix releases as possible, then proceed to new features, and finally, the major releases that encompass breaking changes.

## Bugfix upgrade

Bugfix releases increase only the micro version number according to [SemVer (*Semantic Versioning*)](https://semver.org/) (for instance, an upgrade from 3.14.4 to 3.14.7). Bugfix upgrades require no special strategies; simply update your instances to the latest version without changing your code or deployment. While it's not critical that all instances run on the same version, we recommend it for consistency.

## New feature upgrade

Following the SemVer specification, new features result in an increase in the minor version number (like going from 3.14.7 to 3.20.5). Generally, you can treat feature upgrades like bugfix upgrades — update all your instances to the latest version.

However, if you're also upgrading your code to utilize a new feature, ensure it's backward compatible with the older BullMQ version. Otherwise, an older `Worker` might stop functioning if a new `Queue` adds jobs leveraging a feature the older `Worker` doesn't understand.

The strategy here is to first upgrade all your instances to the version featuring the new functionality. After confirming all instances run the new version, proceed to deploy your code depending on those new features.

## Breaking changes

Occasionally, unavoidable changes incompatible with previous versions are made. We strive to minimize these, classifying them into two types: API-breaking changes and data structure-breaking changes.

### API breaking changes

API breaking changes could involve altered method parameters, removals, or different operational methods. These changes are usually straightforward to apply — you can run your BullMQ-dependent unit tests and address issues based on these changes. If you're using TypeScript, compilation errors will likely surface. Always read the [changelog](https://github.com/taskforcesh/bullmq/blob/master/docs/gitbook/guide/changelog.md) for essential information about these changes.

### Data structure breaking changes

Data structure changes, which alter the queue's underlying structure, are more challenging. They can be either

* **additive** (introducing new data structures that older BullMQ versions don't understand), or
* **destructive** (changing or eradicating older data structures).

For additive changes, you could simply upgrade all instances to the new version — they should apply the change and continue working without issues, akin to a [new feature upgrade](#new-features-upgrade).

Destructive changes are the most demanding, as these fundamental alterations may make older versions unworkable, making rollback impossible if the upgrade fails. The [changelog](https://github.com/taskforcesh/bullmq/blob/master/docs/gitbook/guide/changelog.md) will provide crucial information to guide you through this type of upgrade.

## Some general strategies

For the most demanding upgrades, you might find these strategies useful:

### Pause/Upgrade/Unpause

Since BullMQ supports global pause, one possible strategy, if suitable for your business case, is to pause the queue(s), wait until all current queued jobs have been processed, then perform the upgrade. Once all instances running BullMQ have been upgraded, you can unpause and let new jobs be processed by the new workers. Be aware this strategy is less useful if breaking changes affect `Queue` instances. Always consult the changelog for this type of information.

### Use new queues altogether

This drastic solution involves discontinuing use of older queues and creating new ones. You could rename older queues (e.g., "myQueueV2"), use a new Redis host, or maintain two versions of the service—one running an older BullMQ version with old queues, and a newer one with the latest BullMQ and a different set of queues. When the older version has no more jobs to process, it can be retired, leaving only the upgraded version.


# Bull to BullMQ

Tips and hints on how to migrate from Bull package to BullMQ.

Bull and BullMQ have diverged too much now to actually give any guarantee of backwards compatibility.

So the safest would be to use new queues for BullMQ and deprecate the old ones.

New queues in this context mean using different queue names or passing a custom prefix option. You can have a period where bull and bullmq workers are running in parallel until all the jobs from the old queues are completed. Take into account that producers should add jobs in bullmq queues in this period. When all queues from bull are drained, you can deprecate them.

You can use a dashboard tool such as <https://taskforce.sh> for monitoring this process and make sure the old queues are completely empty before removing them.

## Read more:

* 💡 [Worker Prefix Option Reference](https://api.docs.bullmq.io/interfaces/v5.WorkerOptions.html#prefix)
* 💡 [Queue Prefix Option Reference](https://api.docs.bullmq.io/interfaces/v5.QueueOptions.html#prefix)


# Troubleshooting

In this section, you will be able to find hints and solutions for some common errors you might encounter when using BullMQ.

### Missing Locks

An error that can be thrown by the workers has the following structure: “Missing lock for job 1234. moveToFinished.” This error occurs when a job being processed by a worker unexpectedly loses its “lock.”

When a worker processes a job, it requires a special lock key to ensure that the job is currently “owned” by that worker, preventing other workers from picking up the same job. However, this lock can be deleted, and such a deletion may not be detected until the worker tries to move the job to a completed or failed status.

A lock can be deleted for several reasons, the most common being:

* The worker is consuming too much CPU and has no time to renew the lock every 30 seconds (which is the default expiration time for locks)
* The worker has lost communication with Redis and cannot renew the lock in time.
* The job has been forcefully removed using one of BullMQ's APIs to remove jobs (or by removing the entire queue).
* The Redis instance has a wrong [maxmemory](https://docs.bullmq.io/guide/going-to-production#max-memory-policy) policy; it should be no-eviction to avoid Redis removing keys with the expiration date before hand.

### Invalid or Undefined Environment Variables

If you rely on environment variables (e.g., for queue names or job data), a common pitfall is passing them directly to BullMQ methods when those environment variables are:

* Undefined (not set at all)
* Empty strings (i.e., "")
* Non-string values (e.g., inadvertently passing objects or arrays)

This can cause BullMQ’s internal Lua scripts to throw ERR Error running script ... Lua redis() command arguments must be strings or integers. It typically happens when a parameter passed into the Redis command ends up being something other than a valid string or number.

**Best Practices to Avoid This Error**

1. Validate Environment Variables Early

   In your application’s initialization code, check all required environment variables:

```typescript
const queueName = process.env.QUEUE_NAME;
if (!queueName) {
  throw new Error("QUEUE_NAME is not defined or is empty.");
}

const queue = new Queue(queueName, { ... });
```

This ensures you fail fast if a variable isn’t set, instead of causing hidden Lua script errors.

2. Use TypeScript Strictness

If you’re using TypeScript, enable strictNullChecks and explicitly type environment variables as string | undefined. That way, any code that attempts to use them without proper checks will cause a compile-time error.

3. Provide Defaults Where Appropriate

In some cases, you may want a fallback value if an environment variable is missing:

```typescript
const queueName = process.env.QUEUE_NAME ?? 'defaultQueue';
```

But be sure this fallback is actually valid in your production workflow.

Following these guidelines helps prevent obscure Lua script errors in BullMQ that stem from passing undefined or invalid arguments into Redis commands.


# Adding jobs in bulk across different queues

Sometimes it is necessary to atomically add jobs to different queues in bulk. For example, there could be a requirement that all the jobs must be created or none of them. Also, adding jobs in bulk can be faster, since it reduces the number of roundtrips to Redis:

You may be think of [`queue.addBulk`](https://api.docs.bullmq.io/classes/v5.Queue.html#addbulk), but this method only adds jobs to a single queue. Another option is [`flowProducer.addBulk`](https://api.docs.bullmq.io/classes/v5.FlowProducer.html#addbulk), so let's see an example:

```typescript
import { FlowProducer } from 'bullmq';

const flow = new FlowProducer({ connection });

const trees = await flow.addBulk([
  {
    name: 'job-1',
    queueName: 'queueName-1',
    data: {}
  },
  {
    name: 'job-2',
    queueName: 'queueName-2',
    data: {}
  },
]);
```

It is possible to add individual jobs without children.

This call can only succeed or fail, and all or none of the jobs will be added.

## Read more:

* 💡 [Add Bulk API Reference](https://api.docs.bullmq.io/classes/v5.FlowProducer.html#addbulk)


# Deduplication

Sometimes, you may want to decide when you want to stop deduplicating jobs.

## Until job is active

As soon as job is moved to active, you must call **removeDeduplicationKey** method:

```typescript
import { Job, Queue, Worker } from 'bullmq';

const myQueue = new Queue('Paint');

const worker = new Worker('Paint', async (job: Job) => {
  await job.removeDeduplicationKey();
  console.log('Do something with job');
  return 'some value';
});

myQueue.add('house', { color: 'white' }, { deduplication: { id: 'house' } });
```

{% hint style="info" %}
Previous example uses [Simple Mode](https://docs.bullmq.io/guide/jobs/deduplication#simple-mode) but it can be combined with [Throttle Mode](https://docs.bullmq.io/guide/jobs/deduplication#throttle-mode) or [Debounce Mode](https://docs.bullmq.io/guide/jobs/deduplication#debounce-mode).
{% endhint %}

## Using job schedulers

Sometimes it is desired to deduplicate jobs that are generated by job schedulers to save resources and avoid unnecessary work:

Deduplication options are not available in [`JobSchedulerTemplateOptions`](https://api.docs.bullmq.io/types/v5.JobSchedulerTemplateOptions.html) because they could interfere with job creation from scheduler templates. Since a new job is added as soon as the previous one moves to the active state, deduplication could disrupt this process by preventing the addition of this new record. However, there is an alternative to handle this. Let's look at an example:

```typescript
import { Queue, Worker } from 'bullmq';

const myQueue = new Queue('Paint');

const worker = new Worker(
  'Paint',
  async job => {
    if (job.name === 'paint-trigger') {
      // Add a job that will be deduplicated for 90 seconds.
      await myQueue.add(
        'house',
        { color: 'white' },
        { deduplication: { id: 'customValue', ttl: 90000 } },
      );
    }
  },
  { connection },
);

await myQueue.upsertJobScheduler('repeat', {
  pattern: '* * * * *', // every minute
  template: {
    name: 'paint-trigger',
    data: {},
  },
});
```

In this way, you can deduplicate a job when using job schedulers.

## Read more:

* 💡 [Add Job API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#add)
* 💡 [Deduplication Reference](https://docs.bullmq.io/guide/jobs/deduplication)
* 💡 [Remove Deduplication Key API Reference](https://api.docs.bullmq.io/classes/v5.Job.html#removededuplicationkey)
* 💡 [Upsert Job Scheduler API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#upsertJobScheduler)


# Manually processing jobs

When a Worker is instantiated, the most common usage is to specify a process function so that the worker will automatically process the jobs that arrive to the queue.

Sometimes however it is useful to be able to fetch the jobs manually. Just instantiate the worker without a processor and call getNextJob to fetch the next job:

```typescript
const worker = new Worker('my-queue');

// Specify a unique token
const token = 'my-token';

const job = (await worker.getNextJob(token)) as Job;

// Access job.data and do something with the job
// processJob(job.data)
if (succeeded) {
  await job.moveToCompleted('some return value', token, false);
} else {
  await job.moveToFailed(new Error('my error message'), token, false);
}

await worker.close();
```

There is an important consideration regarding job "locks" when processing manually. Locks prevent workers from fetching a job that is already being processed by another worker. The ownership of the lock is determined by the "token" that is sent when getting the job.

{% hint style="info" %}
the lock duration setting is called "visibility window" in other queue systems.
{% endhint %}

Normally a job gets locked as soon as it is fetched from the queue with a max duration of the specified `lockDuration` worker option. The default is 30 seconds but can be changed to any value easily. For example, to change it to 60 seconds:

```typescript
const worker = new Worker('my-queue', null, { lockDuration: 60000 });
```

When using standard worker processors, the lock is renewed automatically after half the lock duration time has passed. However, this mechanism does not exist when processing jobs manually, so to avoid the job being moved back to the waiting list of the queue, you need to make sure to process the job faster than the `lockDuration`, or manually extend the lock:

```typescript
const job = (await worker.getNextJob(token)) as Job;

// Extend the lock 30 more seconds
await job.extendLock(token, 30000);
```

### Choosing a token

A token represents ownership by given worker currently working on a given job. If the worker dies unexpectedly, the job could be picked up by another worker when the lock expires. A good approach for generating tokens for jobs is simply to generate a UUID for every new job, but it all depends on your specific use case.

## Checking for stalled jobs

When processing jobs manually you may also want to start the stalled jobs checker. This checker is needed to move stalled jobs (whose lock has expired) back to the *wait* status (or *failed* if they have exhausted the maximum number of [stalled attempts](https://api.docs.bullmq.io/interfaces/v5.WorkerOptions.html#maxstalledcount), which is 1 by default).

```typescript
await worker.startStalledCheckTimer()
```

The checker will run periodically (based on the [`stalledInterval`](https://api.docs.bullmq.io/interfaces/v5.WorkerOptions.html#stalledinterval) option) until the worker is closed.

## Looping through jobs

In many cases, you will have an "infinite" loop that processes jobs one by one like the following example. Note that the third parameter in `job.moveToCompleted`/`job.moveToFailed` is not used, signalling that the next job should be returned automatically.

```typescript
const worker = new Worker('my-queue');

const token = 'my-token';
let job;

while (1) {
  let jobData = null,
    jobId,
    success;

  if (job) {
    // Use job.data to process this particular job.
    // and set success variable if succeeded

    if (success) {
      [jobData, jobId] = await job.moveToCompleted('some return value', token);
    } else {
      await job.moveToFailed(new Error('some error message'), token);
    }

    if (jobData) {
      job = Job.fromJSON(worker, jobData, jobId);
    } else {
      job = null;
    }
  } else {
    if (!job) {
      job = await worker.getNextJob(token);
    }
  }
}
```

## Rate Limiting

If you want to move a job back to wait because your queue is rate limited.

```typescript
const worker = new Worker('my-queue', null, { connection, prefix });
const token = 'my-token';
await Job.create(queue, 'test', { foo: 'bar' });
const job = (await worker.getNextJob(token)) as Job;

await queue.rateLimit(60000);
await job.moveToWait(token);
```

## Read more:

* 💡 [Get Next Job API Reference](https://api.docs.bullmq.io/classes/v5.Worker.html#getnextjob)
* 💡 [Move To Completed API Reference](https://api.docs.bullmq.io/classes/v5.Job.html#movetocompleted)
* 💡 [Move To Failed API Reference](https://api.docs.bullmq.io/classes/v5.Job.html#movetofailed)
* 💡 [Move To Wait API Reference](https://api.docs.bullmq.io/classes/v5.Job.html#movetowait)


# Named Processor

When a Worker is instantiated, the most common usage is to specify a process function.

Sometimes however, it is useful to be able to specify more than one function to process a job for a specific condition:

```typescript
const worker = new Worker(
  'queueName',
  async job => {
    switch (job.name) {
      case 'taskType1': {
        await doSomeLogic1();
        break;
      }
      case 'taskType2': {
        await doSomeLogic2();
        break;
      }
    }
  },
  { connection },
);
```

You could use a simple switch case to differentiate your logic, in this example we are using the job name.

{% hint style="warning" %}
This was a feature in the Bull package, but it creates a lot of confusion, so in order to provide an alternative, you can use this pattern. See [#297](https://github.com/taskforcesh/bullmq/issues/297) and [#69](https://github.com/taskforcesh/bullmq/issues/69) as reference
{% endhint %}


# Flows

{% hint style="warning" %}
The following pattern, although still useful, has been mostly super-seeded by the new [Flows](https://docs.bullmq.io/guide/flows) functionality
{% endhint %}

In some situations, you may need to execute a flow of several actions, any of which could fail. For example, you may need to update a database, make calls to external services, or any other kind of asynchronous call.

Sometimes it may not be possible to create an [idempotent job](https://docs.bullmq.io/patterns/idempotent-jobs) that can execute all these actions again in the case one of them failed for any reason. Instead, we may want to be able to only re-execute the action that failed and continue executing the rest of the actions that have not yet been executed.

The pattern to solve this issue consists of dividing the flow of actions into one queue for every action. When the first action completes, it places the next action as a job in its corresponding queue.


# Idempotent jobs

In order to take advantage of [the ability to retry failed jobs](https://docs.bullmq.io/guide/retrying-failing-jobs), your jobs should be designed with failure in mind.

This means that it should not make a difference to the final state of the system if a job successfully completes on its first attempt, or if it fails initially and succeeds when retried. This is called *Idempotence*.

To achieve this behaviour, your jobs should be as atomic and simple as possible. Performing many different actions (such as database updates, API calls, ...) at once makes it hard to keep track of the process flow and, if needed, rollback partial progress when an exception occurs.

Simpler jobs also means simpler debugging, identifying bottlenecks, etc.

If necessary, split complex jobs [as described in the flow pattern](https://docs.bullmq.io/patterns/flows).


# Throttle jobs

Sometimes, you may want to enqueue a job in reaction to a frequently occurring event, without running that job for *every* event. For example, you may want to send an email to a user when they update their profile, but you don't want to send an email for every single update if they make many changes in rapid succession.

You can achieve this by setting an identical `jobId` (using `JobsOptions.jobId?: string` to override the default unique integer) so **"identical" jobs are considered duplicates and not added to the queue**. If you use this option, it is up to you to ensure the `jobId` is unique.

{% hint style="warning" %}
Hint: Be careful if using `removeOnComplete`/`removeOnFailed` options, since a removed job will not count as existing and a new job with the same job ID could be added to the queue without being detected as a duplicate.
{% endhint %}

example:

```typescript
import { Job, Queue, Worker } from 'bullmq';

const myQueue = new Queue('Paint');

const worker = new Worker('Paint', async (job: Job) => {
  console.log('Do something with job');
  return 'some value';
});

worker.on('completed', (job: Job, returnvalue: any) => {
  console.log('worker done painting', new Date());
});

worker.on('failed', (job: Job, error: Error) => {
  console.error('worker fail painting', job, error, new Date());
});

// Add only one job that will be delayed at least 1 second.
myQueue.add('house', { color: 'white' }, { delay: 1000, jobId: 'house' });
myQueue.add('house', { color: 'white' }, { delay: 1000, jobId: 'house' });
myQueue.add('house', { color: 'white' }, { delay: 1000, jobId: 'house' });
myQueue.add('house', { color: 'white' }, { delay: 1000, jobId: 'house' });
myQueue.add('house', { color: 'white' }, { delay: 1000, jobId: 'house' });
myQueue.add('house', { color: 'white' }, { delay: 1000, jobId: 'house' });
myQueue.add('house', { color: 'white' }, { delay: 1000, jobId: 'house' });
```


# Manual retrying

There are situations when it is useful to retry a job right away when it is being processed.

This can be handled using the `moveToWait` method. However, it is important to note that when a job is being processed by a worker, the worker keeps a lock on this job with a certain token value. For the `moveToWait` method to work, we need to pass said token so that it can unlock without error. Finally, we need to exit from the processor by throwing a special error (`WaitingError`) that will signal to the worker that the job has been retried so that it does not try to complete (or fail the job) instead.

```typescript
import { WaitingError, Worker } from 'bullmq';

const worker = new Worker(
  'queueName',
  async (job: Job, token?: string) => {
    try {
      await doSomething();
    } catch (error) {
      await job.moveToWait(token);
      throw new WaitingError();
    }
  },
  { connection },
);
```

## Read more:

* 💡 [Move To Wait API Reference](https://api.docs.bullmq.io/classes/v5.Job.html#movetowait)


# Process Step Jobs

Sometimes, it is useful to break processor functions into small pieces that will be processed depending on the previous executed step. One way to handle this kind of logic is by using switch statements:

{% tabs %}
{% tab title="TypeScript" %}

```typescript
enum Step {
  Initial,
  Second,
  Finish,
}

const worker = new Worker(
  'queueName',
  async job => {
    let step = job.data.step;
    while (step !== Step.Finish) {
      switch (step) {
        case Step.Initial: {
          await doInitialStepStuff();
          await job.updateData({
            step: Step.Second,
          });
          step = Step.Second;
          break;
        }
        case Step.Second: {
          await doSecondStepStuff();
          await job.updateData({
            step: Step.Finish,
          });
          step = Step.Finish;
          return Step.Finish;
        }
        default: {
          throw new Error('invalid step');
        }
      }
    }
  },
  { connection },
);
```

{% endtab %}

{% tab title="Python" %}

```python
class Step(int, Enum):
  Initial = 1
  Second = 2
  Finish = 3

async def process(job: Job, token: str):
  step = job.data.get("step")
  while step != Step.Finish:
    if step == Step.Initial:
      await doInitialStepStuff()
      await job.updateData({
          "step": Step.Second
      })
      step = Step.Second
    elif step == Step.Second:
      await doSecondStepStuff()
      await job.updateData({
          "step": Step.Finish
      })
      step = Step.Finish
    else:
      raise Exception("invalid step")

worker = Worker("queueName", process, {"connection": connection})
```

{% endtab %}
{% endtabs %}

By saving the next step value every time we complete the previous step (here, saving it in the job's data), we can ensure that if the job errors and retries, it does so starting from the correct step.

## Delaying

There are situations when it is useful to delay a job when it is being processed.

This can be handled using the `moveToDelayed` method. However, it is important to note that when a job is being processed by a worker, the worker keeps a lock on this job with a certain token value. For the `moveToDelayed` method to work, we need to pass said token so that it can unlock without error. Finally, we need to exit from the processor by throwing a special error (`DelayedError`) that will signal to the worker that the job has been delayed so that it does not try to complete (or fail the job) instead.

```typescript
import { DelayedError, Worker } from 'bullmq';

enum Step {
  Initial,
  Second,
  Finish,
}

const worker = new Worker(
  'queueName',
  async (job: Job, token?: string) => {
    let step = job.data.step;
    while (step !== Step.Finish) {
      switch (step) {
        case Step.Initial: {
          await doInitialStepStuff();
          await job.moveToDelayed(Date.now() + 200, token);
          await job.updateData({
            step: Step.Second,
          });
          throw new DelayedError();
        }
        case Step.Second: {
          await doSecondStepStuff();
          await job.updateData({
            step: Step.Finish,
          });
          step = Step.Finish;
        }
        default: {
          throw new Error('invalid step');
        }
      }
    }
  },
  { connection },
);
```

## Waiting Children

A common use case is to add children at runtime and then wait for the children to complete.

This can be handled using the `moveToWaitingChildren` method. However, it is important to note that when a job is being processed by a worker, the worker keeps a lock on this job with a certain token value. For the `moveToWaitingChildren` method to work, we need to pass said token so that it can unlock without error. Finally, we need to exit from the processor by throwing a special error (`WaitingChildrenError`) that will signal to the worker that the job has been moved to *waiting-children*, so that it does not try to complete (or fail) the job instead.

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import { WaitingChildrenError, Worker } from 'bullmq';

enum Step {
  Initial,
  Second,
  Third,
  Finish,
}

const worker = new Worker(
  'parentQueueName',
  async (job: Job, token?: string) => {
    let step = job.data.step;
    while (step !== Step.Finish) {
      switch (step) {
        case Step.Initial: {
          await doInitialStepStuff();
          await childrenQueue.add(
            'child-1',
            { foo: 'bar' },
            {
              parent: {
                id: job.id,
                queue: job.queueQualifiedName,
              },
            },
          );
          await job.updateData({
            step: Step.Second,
          });
          step = Step.Second;
          break;
        }
        case Step.Second: {
          await doSecondStepStuff();
          await childrenQueue.add(
            'child-2',
            { foo: 'bar' },
            {
              parent: {
                id: job.id,
                queue: job.queueQualifiedName,
              },
            },
          );
          await job.updateData({
            step: Step.Third,
          });
          step = Step.Third;
          break;
        }
        case Step.Third: {
          const shouldWait = await job.moveToWaitingChildren(token);
          if (!shouldWait) {
            await job.updateData({
              step: Step.Finish,
            });
            step = Step.Finish;
            return Step.Finish;
          } else {
            throw new WaitingChildrenError();
          }
        }
        default: {
          throw new Error('invalid step');
        }
      }
    }
  },
  { connection },
);
```

{% endtab %}

{% tab title="Python" %}

```python
from bullmq import Worker, WaitingChildrenError
from enum import Enum

class Step(int, Enum):
  Initial = 1
  Second = 2
  Third = 3
  Finish = 4

async def process(job: Job, token: str):
  step = job.data.get("step")
  while step != Step.Finish:
    if step == Step.Initial:
      await doInitialStepStuff()
      await children_queue.add('child-1', {"foo": "bar" },{
        "parent": {
            "id": job.id,
            "queue": job.queueQualifiedName
        }
      })
      await job.updateData({
          "step": Step.Second
      })
      step = Step.Second
    elif step == Step.Second:
      await doSecondStepStuff()
      await children_queue.add('child-2', {"foo": "bar" },{
        "parent": {
          "id": job.id,
          "queue": job.queueQualifiedName
        }
      })
      await job.updateData({
          "step": Step.Third
      })
      step = Step.Third
    elif step == Step.Third:
      should_wait = await job.moveToWaitingChildren(token, {})
      if not should_wait:
        await job.updateData({
            "step": Step.Finish
        })
        step = Step.Finish
        return Step.Finish
      else:
        raise WaitingChildrenError
    else:
      raise Exception("invalid step")

worker = Worker("parentQueueName", process, {"connection": connection})
```

{% endtab %}
{% endtabs %}

{% hint style="info" %}
Bullmq-Pro: this pattern could be handled by using observables; in that case, we do not need to save next step.
{% endhint %}

## Chaining Flows

Another use case is to add flows at runtime and then wait for the children to complete.

For example, we can add children dynamically in the worker's processor function:

```typescript
import { FlowProducer, WaitingChildrenError, Worker } from 'bullmq';

enum Step {
  Initial,
  Second,
  Third,
  Finish,
}

const flow = new FlowProducer({ connection });
const worker = new Worker(
  'parentQueueName',
  async (job, token) => {
    let step = job.data.step;
    while (step !== Step.Finish) {
      switch (step) {
        case Step.Initial: {
          await doInitialStepStuff();
          await flow.add({
            name: 'child-job',
            queueName: 'childrenQueueName',
            data: {},
            children: [
              {
                name,
                data: { idx: 0, foo: 'bar' },
                queueName: 'grandchildrenQueueName',
              },
              {
                name,
                data: { idx: 1, foo: 'baz' },
                queueName: 'grandchildrenQueueName',
              },
            ],
            opts: {
              parent: {
                id: job.id,
                queue: job.queueQualifiedName,
              },
            },
          });

          await job.updateData({
            step: Step.Second,
          });
          step = Step.Second;
          break;
        }
        case Step.Second: {
          await doSecondStepStuff();
          await job.updateData({
            step: Step.Third,
          });
          step = Step.Third;
          break;
        }
        case Step.Third: {
          const shouldWait = await job.moveToWaitingChildren(token);
          if (!shouldWait) {
            await job.updateData({
              step: Step.Finish,
            });
            step = Step.Finish;
            return Step.Finish;
          } else {
            throw new WaitingChildrenError();
          }
        }
        default: {
          throw new Error('invalid step');
        }
      }
    }
  },
  { connection },
);
```

{% hint style="info" %}
Manually moving jobs using special errors does **not** increment the attemptsMade property. This property is incremented on regular job completion or failure (this includes retries using a backoff strategy). To control how many times a job is allowed to skip an attempt made using one of our special errors like: **DelayedError**, **RateLimitError**, **WaitingChildrenError** or **WaitingError**. To control how many times a job is allowed to start processing, use the **maxStartedAttempts** option.
{% endhint %}

## Read more:

* 💡 [Move To Delayed API Reference](https://api.docs.bullmq.io/classes/v5.Job.html#movetodelayed)
* 💡 [Move To Waiting Children API Reference](https://api.docs.bullmq.io/classes/v5.Job.html#movetowaitingchildren)


# Failing fast when Redis is down

By design, BullMQ reconnects to Redis automatically. If jobs are added to a queue while the queue instance is disconnected from Redis, the `add` command will not fail; instead, the call will keep waiting for a reconnection to occur until it can complete.

This behavior is not always desirable; for example, if you have implemented a REST API that results in a call to `add`, you do not want to keep the HTTP call busy while `add` is waiting for the queue to reconnect to Redis. In this case, you can pass the option `enableOfflineQueue: false`, so that `ioredis` do not queue the commands and instead throws an exception:

```typescript
const myQueue = new Queue("transcoding", {
  connection: {
    enableOfflineQueue: false,
  },
});

app.post("/jobs", async (req, res) => {
  try {
    const job = await myQueue.add("myjob", { req.body });
    res.status(201).json(job.id);
  }catch(err){
    res.status(503).send(err);
  }
})
```

Using this approach, the caller can catch the exception and act upon it depending on its requirements (for example, retrying the call or giving up).

{% hint style="danger" %}
Currently, there is a limitation in that the Redis instance must at least be online while the queue is being instantiated.
{% endhint %}


# Stop retrying jobs

When a processor throws an exception that is considered unrecoverable, you should use the `UnrecoverableError` class. In this case, BullMQ will just move the job to the failed set without performing any retries, overriding any `attempts` settings used when adding the job to the queue.

```typescript
import { Worker, UnrecoverableError } from 'bullmq';

const worker = new Worker(
  'foo',
  async job => {
    doSomeProcessing();
    throw new UnrecoverableError('Unrecoverable');
  },
  { connection },
);

await queue.add(
  'test-retry',
  { foo: 'bar' },
  {
    attempts: 3,
    backoff: 1000,
  },
);
```

## Fail job when manual rate-limit

When a job is rate limited using `RateLimitError` and tried again, the `attempts` check is ignored, as rate limiting is not considered a real error. However, if you want to manually check the attempts and avoid retrying the job, you can check `job.attemptsStarted` as following:

```typescript
import { Worker, RateLimitError, UnrecoverableError } from 'bullmq';

const worker = new Worker(
  'myQueue',
  async job => {
    const [isRateLimited, duration] = await doExternalCall();
    if (isRateLimited) {
      await queue.rateLimit(duration);
      if (job.attemptsStarted >= job.opts.attempts) {
        throw new UnrecoverableError('Unrecoverable');
      }
      // Do not forget to throw this special exception,
      // since we must differentiate this case from a failure
      // in order to move the job to wait again.
      throw new RateLimitError();
    }
  },
  {
    connection,
    limiter: {
      max: 1,
      duration: 500,
    },
  },
);
```

{% hint style="info" %}
`job.attemptsMade` is increased when any error different than `RateLimitError`, `DelayedError` or `WaitingChildrenError` is thrown. While `job.attemptsStarted` is increased every time that a job is moved to active.
{% endhint %}

## Read more:

* 💡 [Rate Limit API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#ratelimit)


# Timeout jobs

BullMQ does not provide a specific mechanism to timeout jobs, however this can be accomplished in many cases with a custom timeout code in the worker's process function.

The basic concept is to set up a timeout callback that will abort the job processing, and throw an UnrecoverableError (to avoid retries, although this may not alway be the desired behaviour, if so just throw a normal Error). Note how we specified the timeout as a property of the job's data, in case we want to have different timeouts depending on the job, but we could also have a fixed constant timeout for all jobs if we wanted.

```typescript
const worker = new Worker('foo', async job => {
  let controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), job.data.timeout);
    
  try {
    await doSomethingAbortable(controller.signal);
  } catch(err) {
     if (err.name == "AbortError") {
      throw new UnrecoverableError("Timeout");
    } else {
      throw err;
    }
  } finally {
    clearTimeout(timer);
  }
});
```

In this simple example we assume that doSomethingAbortable is an asynchronous function that can handle abort signals and abort itself gracefully.

Now let's see another case when we want to timeout a fetch call, it would look like this:

```typescript
const worker = new Worker("foo", async (job) => { 
  let controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), job.data.timeout);
  try {
    let response = await fetch("/slowserver.com", {
      signal: controller.signal,
    }); 
    const result = await response.text();
  } catch (err) {
    if (err.name == "AbortError") {
      throw new UnrecoverableError("Timeout");
    } else {
      throw err;
    }
  } finally {
    clearTimeout(timer)
  }
});
```

In this example we are aborting the fetch call using [AbortController](https://developer.mozilla.org/en-US/docs/Web/API/AbortController), which is the default mechanism provided by fetch to abort calls. Note that abort will even cause the async call to response.text() to also throw an Abort exception.

In summary, while it is possible to implement timeout in your jobs, the mechanism to do it may vary depending on the type of asynchronous operations your jobs is performing, but in many cases using AbortController in combination with a setTimeout is more than enough.


# Timeout for Sandboxed processors

A pattern for applying time-to-live to sandboxed processors.

When you are working with sandboxed processors, every job is run in a separate process. This opens the possibility to implement a time-to-live (TTL) mechanism, that kills the process if it has not been able to complete in a reasonable time.

It is important to understand that killing a process can have unintented consecuences, for instance it could be killed in the middle of a writing transaction to a file, that would most likely result in a corrupt file. However, this is kind of the best that is possible to achieve in a runtime as NodeJS which based on asynchronous calls within an event loop. There is currently no known method to achieve this functionality in a more robust way.

This pattern tries to be as possible, but please, keep in mind the trade-offs mentioned above. The pattern uses two timeouts so that it is possible to have a cleanup operation to minimize the effects of a hard kill of the process. Obviously if the cleanup itself hangs, or if the cleanup is not correctly implemented, we can still end killing some database connections or writing operantions right in the middle, with the potential negative outcomes.

```typescript
// This processor will timeout in 30 seconds.
const MAX_TTL = 30_000;

// The processor will have a cleanup timeout of 5 seconds.
const CLEANUP_TTL = 5_000;

// We use a custom exit code to mark the TTL, but any would do in practice
// as long as it is < 256 (Due to Unix limitation to 8 bits per exit code)
const TTL_EXIT_CODE = 10;

module.exports = async function (job) {
  let hasCompleted = false;
  const harKillTimeout = setTimeout(() => {
    if (!hasCompleted) {
      process.exit(TTL_EXIT_CODE);
    }
  }, MAX_TTL);

  const softKillTimeout = setTimeout(async () => {
    if (!hasCompleted) {
      await doCleanup(job);
    }
  }, CLEANUP_TTL);

  try {
    // If doAsyncWork is CPU intensive and blocks NodeJS loop forever,
    // the timeout will never be triggered either.
    await doAsyncWork(job);
    hasCompleted = true;
  } finally {
    // Important to clear the timeouts before returning as this process will be reused.
    clearTimeout(harKillTimeout);
    clearTimeout(softKillTimeout);
  }
};

const doAsyncWork = async job => {
  // Simulate a long running operation.
  await new Promise(resolve => setTimeout(resolve, 10000));
};

const doCleanup = async job => {
  // Simulate a cleanup operation.
  await job.updateProgress(50);
};

```

There are some very important points to consider with this pattern.

* If the processor has hanged because there is an infinite loop that does not let the NodeJS event loop to run, the TTL timeouts will never be called.
* We keep a `hasCompleted` flag so that we can cover the edge case where the async work has just completed at the same time the timeout is triggered.
* When using this pattern it is very useful to put debug logs in strategic places to see where the job actually gets stuck when it is killed due to the TTL being exceeded.


# Redis Cluster

Important considerations when using Redis™ Cluster mode.

Bull internals require atomic operations that span different keys. This behavior breaks Redis's rules for cluster configurations. However, it is still possible to use a cluster environment by using the proper bull prefix option as a cluster "hash tag". Hash tags are used to guarantee that certain keys are placed in the same hash slot, read more about hash tags in the [redis cluster tutorial](https://redis.io/topics/cluster-tutorial). A hash tag is defined with brackets. I.e. a key that has a substring inside brackets will use that substring to determine in which hash slot the key will be placed.

In summary, to make bull compatible with Redis cluster, use a queue prefix inside brackets. For example:

You can use two approaches in order to make the Queues compatible with Cluster. Either define a queue prefix:

```typescript
const queue = new Queue('cluster', {
  prefix: '{myprefix}',
});
```

or wrap the queue name itself:

```typescript
const queue = new Queue('{cluster}');
```

Note that If you use several queues in the same cluster, you should use different prefixes so that the queues are evenly placed in the cluster nodes, potentially increasing performance and memory usage.


# Introduction

The commercial supported version of BullMQ

BullMQ Pro, the commercial version of BullMQ, boasts advanced features and offers dedicated support from the library's authors. You can easily install this package as a drop-in replacement for the standard BullMQ to access these new features.

The BullMQ Pro version continues to evolve, with more features being added regularly. You can check the [roadmap](https://github.com/taskforcesh/bullmq-pro-support/projects/1) section to gain insight into what to expect in the forthcoming months.

![](https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-20555d6090e111c93a562c459a1a35bb41f9b28f%2Fimage.png?alt=media)

### Commercial License

BullMQ Pro uses a per-organization licensing model, allowing unlimited use across all your projects. You can request a free trial token on [this page](https://taskforce.sh/account/bullmqpro), allowing you to evaluate its value. If you find it beneficial, consider subscribing under the '[Subscriptions](https://taskforce.sh/account/subscriptions)' tab.


# Install

In order to install BullMQ Pro you need to use a NPM token from [taskforce.sh](https://taskforce.sh).

With the token at hand just update or create a `.npmrc` file in your app repository with the following contents:

```
@taskforcesh:registry=https://npm.taskforce.sh/
//npm.taskforce.sh/:_authToken=${NPM_TASKFORCESH_TOKEN}
always-auth=true
```

where `NPM_TASKFORCESH_TOKEN` is an environment variable pointing to your token.

Then just install the `@taskforcesh/bullmq-pro` package as you would install any other package, with `npm`, `yarn` or `pnpm`:

```
yarn add @taskforcesh/bullmq-pro
```

In order to use BullMQ Pro just import the *Pro* versions of the classes. These classes are subclasses of the open source BullMQ library with new functionality:

```typescript
import { QueuePro, WorkerPro } from '@taskforcesh/bullmq-pro';

const queue = new QueuePro('myQueue');

const worker = new WorkerPro('myQueue', async job => {
  // Process job
});
```

### Using Docker

If you use docker you must make sure that you also add the `.npmrc` file above in your `Dockerfile`:

```docker
WORKDIR /app

ADD .npmrc /app/.npmrc
```


# Observables

Instead of returning regular promises, your workers can also return an `Observable`, this allows for some more advanced uses cases:

* It makes it possible to cleanly cancel a running job.
* You can define a "Time to live" (TTL) so that jobs that take too long will be automatically canceled.
* Since the last value returned by the observable is persisted, you could retry a job and continue where you left off, for example, if the job implements a state machine or similar.

If you are new to `Observables` you may want to read this [introduction](https://www.learnrxjs.io/learn-rxjs/concepts/rxjs-primer). The two biggest advantages that `Observables` have over `Promises` are that they can emit more than 1 value and that they are *cancelable*.

Let's see a silly example of a worker making use of `Observables`:

```typescript
import { WorkerPro } from "@taskforcesh/bullmq-pro"
import { Observable } from "rxjs"

const processor = async () => {
  return new Observable<number>(subscriber => {
    subscriber.next(1);
    subscriber.next(2);
    subscriber.next(3);
    const intervalId = setTimeout(() => {
      subscriber.next(4);
      subscriber.complete();
    }, 500);

    // Provide a way of canceling and disposing the interval resource
    return function unsubscribe() {
      clearInterval(intervalId);
    };
  });
};

const worker = new WorkerPro(queueName, processor, { connection });
```

In the example above, the observable will emit 4 values, the first 3 directly and then a 4th after 500 ms. Also note that the `subscriber` returns a `unsubscribe` function. This is the function that will be called if the `Observable` is cancelled, so this is where you would do the necessary clean up.

You may be asking what the use of returning several values from a worker is. One case that comes to mind is if you have a larger processor and you want to make sure that if the process crashes you can continue from the latest value. You could do this with a `switch` statement on the return value, something like this:

```typescript
import { WorkerPro } from "@taskforcesh/bullmq-pro"
import { Observable } from "rxjs"

const processor = async (job) => {
  return new Observable<number>(subscriber => {
    switch(job.returnvalue){
      default:
        subscriber.next(1);
      case 1:
        subscriber.next(2);
      case 2:
        subscriber.next(3);
      case 3:
        subscriber.complete();
    }
  });
};

const worker = new WorkerPro(queueName, processor, { connection });
```


# Cancelation

As mentioned, `Observables` allow for clean cancellation. Currently we support a TTL value that defines the maximum processing time before the job is finally cancelled:

```typescript
import { WorkerPro } from '@taskforcesh/bullmq-pro';

const worker = new WorkerPro(queueName, processor, {
  ttl: 100,
  connection,
});
```

This parameter allows to provide `ttl` values per job name too:

```typescript
const worker = new WorkerPro(queueName, processor, {
  ttl: { test1: 100, test2: 200 },
  connection,
});
```


# Groups

Groups allows you to use a single queue while distributing the jobs among groups so that the jobs are processed one by one relative to the group they belong to.

For example, imagine that you have 1 queue for processing video transcoding for all your users, you may have thousands of users in your application. You need to offload the transcoding operation since it is lengthy and CPU consuming. If you have many users that want to transcode many files, then in a non-grouped queue one user could fill the queue with jobs and the rest of the users will need to wait for that user to complete all its jobs before their jobs get processed.

Groups resolves this problem since jobs will be processed in a "[round-robin](https://en.wikipedia.org/wiki/Round-robin_item_allocation)" fashion among all the users.

![](https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-b189f3837a876d50e4cf025f25bc64c7025fb1c8%2Fimage.png?alt=media)

If you have several workers or a concurrency factor larger than one, jobs will be processed in parallel, but they will be picked up from the groups as mentioned before following a round-robin ordering.

Of course you can have as many workers as you want and also scale up/down the amount of workers depending on how many jobs you have waiting in the queue.

If you only use grouped jobs in a queue, the waiting jobs list will not grow, instead it will just keep the next job to be processed if any. But you can add non-grouped jobs to the same queue, and they will get precedence from the jobs waiting in their respective groups.

{% hint style="info" %}
There is no hard limit on the amount of groups that you can have, nor do they have any impact on performance. When a group is empty, the group itself does not consume any resources in Redis.
{% endhint %}

Another way to see groups is like "virtual" queues. So instead of having one queue per "user", you have a "virtual" queue per user so that all users get their jobs processed in a more predictable way.

In order to use the group functionality, use the group property in the job options when adding a job:

```typescript
import { QueuePro } from '@taskforcesh/bullmq-pro';

const queue = new QueuePro();

const job1 = await queue.add(
  'test',
  { foo: 'bar1' },
  {
    group: {
      id: 1,
    },
  },
);

const job2 = await queue.add(
  'test',
  { foo: 'bar2' },
  {
    group: {
      id: 2,
    },
  },
);
```

In order to process the jobs, use a pro worker as you normally do with standard workers:

```typescript
import { WorkerPro } from '@taskforcesh/bullmq-pro';

const worker = new WorkerPro('test', async job => {
  // Do something usefull.

  // You can also do something different depending on the group
  await doSomethingSpecialForMyGroup(job.opts.group);
});
```


# Getters

#### Job Counts

It is often necessary to know how many jobs are in any group:

```typescript
import { QueuePro } from '@taskforcesh/bullmq-pro';

const queue = new QueuePro('myQueue', { connection });
const groupId = 'my group';
const count = await queue.getGroupsJobsCount(1000); // 1000 groups in each iteration
```

{% hint style="info" %}
This count value includes prioritized and non-prioritized jobs included groups.
{% endhint %}

Or if you want to get active jobs count for an specific group

```typescript
const activeCount = await queue.getGroupActiveCount(groupId);
```

#### Get Jobs

It is also possible to retrieve the jobs with pagination style semantics in a given group. For example:

```typescript
const jobs = await queue.getGroupJobs(groupId, 0, 100);
```

## Read more:

* 💡 [Get Groups Jobs Count API Reference](https://api.bullmq.pro/classes/v7.QueuePro.html#getgroupsjobscount)
* 💡 [Get Group Active Count API Reference](https://api.bullmq.pro/classes/v7.QueuePro.html#getgroupactivecount)
* 💡 [Get Group Jobs API Reference](https://api.bullmq.pro/classes/v7.QueuePro.html#getgroupjobs)


# Rate limiting

A useful feature when using groups is to be able to rate limit the groups independently of each other, so you can evenly process the jobs belonging to many groups and still limit how many jobs per group are allowed to be processed by unit of time.

The way the rate limiting works is that when the jobs for a given group exceed the maximum amount of jobs per unit of time, that particular group gets rate limited. The jobs that belong to this particular group will not be processed until the rate limit expires.

For example "group 2" is rate limited in the following chart:

![Rate limited group](https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-f99cb4797afb865d39a87c94a92595743d1ba93a%2Fimage.png?alt=media)

While one or more groups are rate limited, the rest of the jobs belonging to non rate limited groups will continue to be consumed normally or until they also get rate limited.

The rate limit is configured on the worker instances:

```typescript
import { WorkerPro } from '@taskforcesh/bullmq-pro';

const worker = new WorkerPro('myQueue', processFn, {
    group: {
      limit: {
        max: 100,  // Limit to 100 jobs per second per group
        duration: 1000,
      }
    },
    connection
});
```

### Manual rate-limit

Sometimes it's useful to rate-limit a group manually instead of based on some static options. For example, if you have an API that returns `429 Too Many Requests`, and you want to rate-limit the group based on that response.

For this purpose, you can use the worker method `rateLimitGroup` like this:

```typescript
import { WorkerPro } from '@taskforcesh/bullmq-pro';

const worker = new WorkerPro(
  'myQueue',
  async job => {
    const groupId = job.opts.group.id;
    const [isRateLimited, duration] = await doExternalCall(groupId);
    if (isRateLimited) {
      await worker.rateLimitGroup(job, duration);
      // Do not forget to throw this special exception,
      // since the job is no longer active after being rate limited.
      throw Worker.RateLimitError();
    }
  },
  {
    connection,
  },
);
```

### Get Group Rate Limit Ttl

Sometimes is useful to know if our group is rate limited.

For this purpose, you can use the **`getGroupRateLimitTtl`** method like this:

```typescript
import { QueuePro } from '@taskforcesh/bullmq-pro';

const queue = new QueuePro('myQueue', { connection });
const groupId = '0';
const maxJobs = 100;

const ttl = await queue.getGroupRateLimitTtl(groupId, maxJobs);

if (ttl > 0) {
  console.log('Group is rate limited');
}
```

## Read more:

* 💡 [Rate Limit Group API Reference](https://api.bullmq.pro/classes/v7.QueuePro.html#ratelimitgroup)
* 💡 [Get Group Rate Limit Ttl API Reference](https://api.bullmq.pro/classes/v7.QueuePro.html#getgroupratelimitttl)


# Local group rate limit

How to rate-limit each group with a different limit per group.

Sometimes it is required that different groups have different rate limits, this could be the case for example if a group represents a given user in the system, and depending on the user's quota or other factors we would like to have a different rate-limit for it.

You can use a local group rate limit, which would be used only for the specific group that have the rate-limit setup. For example:

```typescript
import { QueuePro, WorkerPro } from '@taskforcesh/bullmq-pro';

const queue = new QueuePro('myQueue', { connection });
const groupId = 'my group';
const maxJobsPerDuration = 100;

const duration = 1000; // duration in ms.
await queue.setGroupRateLimit(groupId, maxJobsPerDuration, duration);

const worker = new WorkerPro(
  'myQueue',
  async () => {
    // do something
  },
  {
    group: {
      limit: {
        // default rate limit configuration
        max: 1000,
        duration: 1000,
      },
    },
    connection,
  },
);
```

This code would set a specific rate limit on the group "my group" of max 100 jobs per second. Note that you can still have a ["default" rate-limit](https://docs.bullmq.io/bullmq-pro/groups/rate-limiting) specified for the rest of the groups, the call to `setGroupRateLimit` will therefore allow you to override that rate-limit.

{% hint style="warning" %}
You must specify a default rate limit by passing group.limit option in each Worker instance. In this way, workers are allowed to check if groups are rate limited or not.
{% endhint %}

### Read more:

* 💡 [Local Rate Limit Group API Reference](https://api.bullmq.pro/classes/v7.QueuePro.html#setgroupratelimit)


# Concurrency

By default, there is no limit on the number of jobs that workers can run in parallel for every group. Even using a rate limit, that would only limit the processing speed, but still you could have an unbounded number of jobs processed simultaneously in every group.

It is possible to constrain how many jobs are allowed to be processed concurrently per group. For example, if you choose 3 as max concurrency factor, the workers will never work on more than 3 jobs at the same time for any given group. This limits only the group; you could have any number of concurrent jobs as long as they are not from the same group.

The concurrency factor is configured as follows:

```typescript
import { WorkerPro } from '@taskforcesh/bullmq-pro';

const worker = new WorkerPro('myQueue', processFn, {
  group: {
    concurrency: 3, // Limit to max 3 parallel jobs per group
  },
  concurrency: 100,
  connection,
});
```

The concurrency factor is global, so in the example above, independently of the concurrency factor per worker or the number of workers that you instantiate in your application, it will never process more than 3 jobs per group at any given time.




---

[Next Page](/llms-full.txt/1)

