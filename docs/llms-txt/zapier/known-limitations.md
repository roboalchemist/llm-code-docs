# Source: https://docs.zapier.com/powered-by-zapier/zap-creation/known-limitations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Known Limitations

> Creating workflows using the Zapier Workflow API is a recent addition, and there are some known limitations.

* Zaps can only be created with Public Apps. Private Apps are not currently supported.
* More complex Action types, such as Searches, Filters, and Paths, are not supported.
* The API does not currently have an endpoint to turn off/on a user's Zaps. If your Zapier app uses [Webhook Subscriptions](https://platform.zapier.com/build/hook-trigger), you can send a `DELETE` to the unique target URL that was provided when the subscription was created and that will then pause/turn off a Zap.
* Webhook `READ` actions are not currently supported.

If you've got a use case that you think *should* be supported, let us know!
