# Source: https://developers.webflow.com/webflow-cloud/environment.mdx

***

title: About the Webflow Cloud edge environment
slug: environment
description: Learn about Webflow Cloud's edge runtime environment
hidden: false
max-toc-depth: 2
'og:title': About the Webflow Cloud edge environment
'og:description': Learn about Webflow Cloud's edge runtime environment
----------------------------------------------------------------------

Webflow Cloud runs your app on [Cloudflare Workers](https://developers.cloudflare.com/workers/), executing code at edge locations worldwide using the [Workers runtime](https://developers.cloudflare.com/workers/runtime-apis/). While it shares some concepts with traditional serverless platforms, Workers differs from Node.js environments.

This guide outlines those key differences and provides best practices to prepare your code for deployment on Webflow Cloud.

## Understanding the workers runtime

Unlike traditional serverless platforms built on containers or virtual machines, [Workers use lightweight V8 isolates](https://developers.cloudflare.com/workers/reference/how-workers-works/) to deliver fast, scalable, and secure performance. The Workers runtime is designed to start code instantly with minimal overhead, allowing each function to run in its own isolated environment. This reduces cold start times and provides strong security boundaries between executions.

Because of this architecture, there are important differences in how your app runs—especially around API support, state management, resource limits, and deployment workflows. The guides below outline what to expect and how to prepare your code for Webflow Cloud.

<Note title="Edge runtime vs Workers runtime">
  Throughout the documentation, you may encounter the term "edge runtime." The Workers runtime is a specific implementation of the edge runtime, and the terms are often used interchangeably.
</Note>

<CardGroup cols={2}>
  <Card title="Configuration" href="/webflow-cloud/environment/configuration">
    Configure your project for deployment on Webflow Cloud.
  </Card>

  <Card title="Framework setup" href="/webflow-cloud/environment/framework-customization">
    Some frameworks need additional configuration to run as expected on Webflow Cloud.
  </Card>

  <Card title="Node.js compatibility" href="/webflow-cloud/environment/nodejs-compatibility">
    Webflow Cloud partially supports Node.js APIs. Review your code and dependencies for compatibility.
  </Card>

  <Card title="Environment variables" href="/webflow-cloud/environments/#managing-environment-variables">
    Define environment variables in <a href="/webflow-cloud/environments">Webflow Cloud Environments</a>.
  </Card>

  <Card title="Resource limits" href="/webflow-cloud/limits">
    The runtime enforces strict limits on memory, CPU, and bundle size.
  </Card>
</CardGroup>

Before deploying, review your code and dependencies for compatibility. If you're migrating, pay close attention to API routes, authentication, and third-party libraries.
