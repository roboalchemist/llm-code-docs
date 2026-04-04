---
---
title: UglifyJS
description: "Upload your source maps using UglifyJS and Sentry CLI."
---

In this guide, you'll learn how to successfully upload source maps for SystemJS using our `sentry-cli` tool.

### 1. Generate Source Maps

First, configure UglifyJS to output source maps:

```
uglifyjs app.js \
  -o app.min.js \
  --source-map url=app.min.js.map,includeSources
```

Generating source maps **may expose them to the public**, potentially causing your source code to be leaked. You can prevent this by configuring your server to deny access to `.js.map` files, or by deleting the sourcemaps before deploying your application.

