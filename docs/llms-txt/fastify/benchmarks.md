# Source: https://fastify.io/benchmarks.md

# Benchmarks

Leveraging our experience with Node.js performance, Fastify has been built from the ground up to be **as fast as possible**.

All the code used for our benchmarks is [available on GitHub](https://github.com/fastify/benchmarks/).

Here's a brief summary on how Fastify overhead performed against the some other well known Node.js web frameworks (last updated on <!-- -->January 1, 2026<!-- -->):

## [Fastify](https://github.com/fastify/benchmarks/blob/main/benchmarks/fastify.cjs)

[](https://github.com/fastify/fastify)

46664 req/sec

99.32948764341513%

## [H3](https://github.com/fastify/benchmarks/blob/main/benchmarks/h3.cjs)

[](https://github.com/unjs/h3)

43674 req/sec

92.96409033823623%

## [Hono](https://github.com/fastify/benchmarks/blob/main/benchmarks/hono.mjs)

[](https://github.com/honojs/hono)

36694 req/sec

78.10766512697161%

## [Koa](https://github.com/fastify/benchmarks/blob/main/benchmarks/koa.cjs)

[](https://github.com/koajs/koa)

35086 req/sec

74.68358202601162%

## [Restify](https://github.com/fastify/benchmarks/blob/main/benchmarks/restify.cjs)

[](https://github.com/restify/node-restify)

34347 req/sec

73.11096447348817%

## [Hapi](https://github.com/fastify/benchmarks/blob/main/benchmarks/hapi.cjs)

[](https://github.com/hapijs/hapi)

32030 req/sec

68.17939930607292%

## [Express](https://github.com/fastify/benchmarks/blob/main/benchmarks/express.cjs)

[](https://github.com/expressjs/express)

9433 req/sec

20.079397177462273%

Please note that this is a synthetic, "hello world" benchmark that aims to evaluate the framework overhead. The overhead that each framework has on your application depends on your application, **you should always benchmark if performance matters to you**.

Do you want to provide feedback on our benchmarks? [Open an issue on GitHub](https://github.com/fastify/benchmarks/issues) and we will get back to you!
