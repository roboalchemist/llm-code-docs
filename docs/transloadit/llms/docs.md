# Source: https://transloadit.com/docs.md

# Transloadit Docs

This guide aims to provide a clear understanding of our API and the core concepts behind our platform. Let's get started!

## Core concepts

* **Robots** are tools that perform specific actions on files. For example the 🤖/http/import Robot can import files from any http URL, the 🤖/s3/store Robot can export files to Amazon S3 and the 🤖/video/encode Robot can resize, convert and watermark videos. We offer**84 Robots** for all your file processing requirements.
* **Templates** are JSON-based configurations that define what should be done with your files. These Instructions consist of *Steps* that each use one of these *Robots*. Templates are securely stored in your Transloadit account. There are tons of copy/pasteable examples to get you started.
* **Assemblies** are executions of your Templates triggered via a `POST` API call to`https://api2.transloadit.com/assemblies` referencing your `template_id`. An Assembly contains references to your uploads and processing results. By accessing the Assembly's result JSON, you can retrieve file metadata and result URLs for use on your website or app in real-time.

## Quickstart

We recommend you to go through our [My first App](/docs/getting-started/my-first-app.md) guide. It highlights the essential steps to get started with the API, providing examples and explanations to help you understand the basic concepts.

## Authentication

To ensure secure usage of our APIs, authentication is required for all your requests. We auto-create API keys for you once you create your first Workspace when logged in — allowing you to start building and testing Templates right away. However, once you are ready to go live with your app, visit our [API Authentication page](/docs/api/authentication.md) to learn more about properly authorizing your requests with signatures.

## Three ways to integrate

* **Handling uploads**: If your users upload or import files from the browser, then our open-source file uploader [Uppy](https://uppy.io) is the best choice for your integration. With over30,000 stargazers on GitHub, it's the most popular file uploader in the world!
* **Smart CDN**: For URL-based conversion and delivery, [our Smart CDN](/services/content-delivery/)is the perfect integration option.
* **Batch processing**: To handle large volumes of files and for building mobile apps, we provide[SDKs](/docs/sdks.md) for popular languages and platforms.

## Found a bug or have feedback?

We're always looking to improve our platform and value feedback from our users. If you encounter a bug, have questions, or want to share suggestions, don't hesitate to[reach out](mailto:support@transloadit.com).

We hope you enjoy using Transloadit for your file processing needs!
