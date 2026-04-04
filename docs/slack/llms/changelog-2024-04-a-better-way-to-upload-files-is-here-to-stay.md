Source: https://docs.slack.dev/changelog/2024-04-a-better-way-to-upload-files-is-here-to-stay

# The files.upload method is retiring, to be replaced by sequenced Web API methods

April 9, 2024

The original web API method for uploading files to Slack, [`files.upload`](/reference/methods/files.upload), is being sunset on **March 11, 2025** **November 12, 2025**.

As of **May 16, 2024**, newly-created apps are no longer able to use this API method.

Existing apps & integrations should migrate away from `files.upload` and instead leverage a combination of two APIs: [`files.getUploadURLExternal`](/reference/methods/files.getUploadURLExternal) and [`files.completeUploadExternal`](/reference/methods/files.completeUploadExternal). The use of these two methods is more reliable, especially when uploading large files.

A detailed breakdown of how to use these two API methods is described in our [Uploading files documentation](/messaging/working-with-files#uploading_files).

* [What’s changing?](#change)
* [How do I prepare?](#prepare)
* [What if I do nothing?](#nothing)

## What’s changing? {#change}

Over the past several years, the files uploaded by users have grown larger and the underlying stacks serving Slack have evolved. To best serve the file upload trends of today and tomorrow, we're moving completely to a more asynchronous upload and processing system.

Instead of uploading a file using a multipart POST to `files.upload` and waiting for an affirmative response at the end of the HTTP request, you'll now send the file upload data to our optimized [`files.getUploadURLExternal`](/reference/methods/files.getUploadURLExternal) method and then fill us in on what you sent with [`files.completeUploadExternal`](/reference/methods/files.completeUploadExternal).

You must complete these changes with these key schedule points to keep in mind:

1. As of May 16, 2024, newly-created Slack apps are no longer able to access the `files.upload` API. Existing apps will be able to continue using `files.upload` until it is sunset.
2. Between June 2024 and February 2025, we will send a series of email reminders to app developers using `files.upload` and Slack workspace admins managing apps that use `files.upload`.
3. On March 11, 2025 November 12, 2025, `files.upload` will be sunset and no longer accessible.

## How do I prepare? {#prepare}

A detailed breakdown of how to stop using `files.upload` and start using the two new methods is described in our [Uploading files documentation](/messaging/working-with-files#uploading_files).

If you already use [our developer tooling](/tools) like our node.js, Python or Java SDKs, including the Bolt framework, then the migration should be made easier: these libraries provide a “v2” `upload` convenience method that wraps around the [`files.getUploadURLExternal`](/reference/methods/files.getUploadURLExternal) and [`files.completeUploadExternal`](/reference/methods/files.completeUploadExternal) methods.

In particular:

* The [node.js `@slack/web-api` package](https://npmjs.com/package/@slack/web-api) exposes [a `uploadV2` method](/tools/node-slack-sdk/web-api#upload-a-file), which is also available within [Bolt JS’s `client` handler parameter](/tools/bolt-js/concepts/web-api).
* The [Python python-slack-sdk package](/tools/python-slack-sdk/web) exposes [a `files_upload_v2` method](/tools/python-slack-sdk/web#files), which is also available within [Bolt for Python’s `client` handler parameter](/tools/bolt-python/concepts/web-api).
* The [Java Slack SDK](https://github.com/slackapi/java-slack-sdk) exposes a [`FilesUploadV2Request` class](https://javadoc.io/doc/com.slack.api/slack-api-client/latest/com/slack/api/methods/request/files/FilesUploadV2Request.html) utilizing the new methods.

## What if I do nothing? {#nothing}

As of May 16, 2024, newly-created Slack apps are no longer able to access the `files.upload` API. Existing apps created prior to May 16, 2024 will be able to continue using `files.upload` until March 11, 2025 November 12, 2025.

If you choose to do absolutely nothing before March 11, 2025 November 12, 2025, and your app continues to attempt to use `files.upload`, your app may quite possibly break or become unusable. At the very least, it won't be uploading files.

## When does this happen? {#when-does-this-happen}

There are two keys dates to keep in mind:

1. As of **May 16, 2024**, newly-created Slack apps are no longer able to access the `files.upload` API. All new apps must use the new methods.
2. On March 11, 2025 November 12, 2025, the `files.upload` API will be sunset and no longer available. All apps, new and old, must use the new methods by this date.

* * *

If you have questions or concerns about the deprecation and retirement of our `files.upload` method, please contact us.

**Tags:**

* [Deprecation](/changelog/tags/deprecation)
* [breaking change](/changelog/tags/breaking-change)
