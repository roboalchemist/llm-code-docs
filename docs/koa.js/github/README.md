# Koa.js Documentation

**Source:** https://github.com/koajs/koa (Master branch)  
**Framework:** Expressive middleware framework for Node.js  
**Node.js Version:** v18.0.0 or higher

## Overview

Koa is a new web framework designed by the team behind Express. It aims to be a smaller, more expressive, and more robust foundation for web applications and APIs. By leveraging async functions, Koa allows you to ditch callbacks and greatly increase error-handling.

Key features:
- Middleware stack flows in a stack-like manner (downstream then upstream)
- ~570 SLOC codebase with only common HTTP server methods
- No bundled middleware - only what you need
- Built on async/await (ES2017)

## Installation

```bash
npm install koa
```

## Documentation Structure

### Getting Started
- **[guide.md](guide.md)** - Complete guide to Koa fundamentals and usage
- **[faq.md](faq.md)** - Frequently asked questions

### API Reference
- **[api/index.md](api/index.md)** - Main API overview
- **[api/context.md](api/context.md)** - Context object documentation
- **[api/request.md](api/request.md)** - Request object API
- **[api/response.md](api/response.md)** - Response object API

### Advanced Topics
- **[error-handling.md](error-handling.md)** - Error handling patterns
- **[koa-vs-express.md](koa-vs-express.md)** - Comparison with Express
- **[troubleshooting.md](troubleshooting.md)** - Common issues and solutions

### Migration Guides
- **[migration-v1-to-v2.md](migration-v1-to-v2.md)** - Upgrading from Koa v1 to v2
- **[migration-v2-to-v3.md](migration-v2-to-v3.md)** - Upgrading from Koa v2 to v3

## Quick Start

```js
const Koa = require('koa');
const app = new Koa();

// Middleware
app.use(async (ctx, next) => {
  const start = Date.now();
  await next();
  const ms = Date.now() - start;
  console.log(`${ctx.method} ${ctx.url} - ${ms}ms`);
});

// Route
app.use(ctx => {
  ctx.body = 'Hello Koa';
});

app.listen(3000);
```

## Middleware Signature

Koa supports both async and common function middleware:

### Async Function (Recommended - Node v7.6+)
```js
app.use(async (ctx, next) => {
  // downstream
  await next();
  // upstream
});
```

### Common Function
```js
app.use((ctx, next) => {
  return next().then(() => {
    // upstream
  });
});
```

## Context, Request & Response

Each middleware receives a `Context` object encapsulating an HTTP request/response:

```js
app.use(async (ctx, next) => {
  ctx; // is the Context
  ctx.request; // is a Koa Request
  ctx.response; // is a Koa Response
  ctx.state; // recommended namespace for passing data
  await next();
});
```

## Core Concepts

### Cascading Middleware
Unlike Connect, Koa middleware invoke downstream, then control flows back upstream:

```js
app.use(async (ctx, next) => {
  console.log('1 start');
  await next();
  console.log('1 end');
});

app.use(async (ctx, next) => {
  console.log('2 start');
  await next();
  console.log('2 end');
});

app.use(ctx => {
  console.log('3 execute');
  ctx.body = 'ok';
});
// Output:
// 1 start
// 2 start
// 3 execute
// 2 end
// 1 end
```

### Application Settings
- `app.env` - NODE_ENV or "development"
- `app.keys` - Array of signed cookie keys
- `app.proxy` - Trust proxy header fields
- `app.subdomainOffset` - Subdomain ignore offset
- `app.asyncLocalStorage` - Enable AsyncLocalStorage support (v3+)

### Error Handling
```js
app.on('error', (err, ctx) => {
  log.error('server error', err, ctx);
});

// Or throw custom errors
ctx.throw(400, 'Bad Request');
ctx.throw(401, 'Unauthorized', { user: user });
```

### Cookies
```js
// Get
const token = ctx.cookies.get('name');

// Set
ctx.cookies.set('name', 'value', {
  maxAge: 24 * 60 * 60 * 1000, // 24 hours
  signed: true,
  httpOnly: true,
  sameSite: 'strict'
});
```

## Response Handling

Set response body as:
- `string` - written as text
- `Buffer` - written as binary
- `Stream` - piped
- `Object` or `Array` - JSON-stringified
- `null` or `undefined` - no content (204)

```js
ctx.body = 'Hello';           // string
ctx.body = { foo: 'bar' };    // JSON
ctx.body = fs.createReadStream('file.txt'); // stream
ctx.status = 200;
```

## Resources

- **GitHub:** https://github.com/koajs/koa
- **Examples:** https://github.com/koajs/examples
- **Middleware Wiki:** https://github.com/koajs/koa/wiki
- **Mailing List:** https://groups.google.com/forum/#!forum/koajs
