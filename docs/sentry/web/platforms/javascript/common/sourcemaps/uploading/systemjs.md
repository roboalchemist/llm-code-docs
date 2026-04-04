---
---
title: SystemJS
description: "Upload your source maps using SystemJS and Sentry CLI."
---

In this guide, you'll learn how to successfully upload source maps for SystemJS using our `sentry-cli` tool.

### 1. Generate Source Maps

First, configure SystemJS to output source maps:

```
builder.bundle("src/app.js", "dist/app.min.js", {
  minify: true,
  sourceMaps: true,
  sourceMapContents: true,
});
```

Generating source maps **may expose them to the public**, potentially causing your source code to be leaked. You can prevent this by configuring your server to deny access to `.js.map` files, or by deleting the sourcemaps before deploying your application.

