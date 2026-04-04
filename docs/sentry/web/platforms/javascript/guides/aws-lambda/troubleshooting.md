---
---
title: Troubleshooting
description: >-
---

Events might be missing right after a Lambda function coldstart. This is a [known issue](https://github.com/getsentry/sentry-javascript/issues/18107) which we are still investigating. Events are sent for subsequent function invocations.

When using `@sentry/aws-serverless` with Express, span names are based on the AWS Lambda function name from the Lambda context, rather than the HTTP request path. This differs from `@sentry/node` behavior where span names show the request path.

This is expected behavior for the AWS Lambda SDK. See the [related GitHub issue](https://github.com/getsentry/sentry-javascript/issues/15788) for more details.

When using Infrastructure as Code frameworks (e.g. CDK, Serverless, SST, etc.) that bundle everything into a single file, third-party libraries that need to be instrumented by Sentry (such as `express`, `pg`, etc.) must be marked as external and excluded from the bundle. If these libraries are bundled, Sentry cannot instrument them properly, resulting in missing tracing data.

You can include them via a Lambda layer so that your function can still access them at runtime.

