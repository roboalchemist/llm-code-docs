Source: https://docs.slack.dev/changelog/2019/02/01/cemented-fate-for-file-comments

# Cemented fate for file comments

February 1, 2019

File threads superseded file comments in [July 2018](/changelog/2018-05-file-threads-soon-tread). On **May 22nd, 2019**, we will permanently retire the `files.comments.add` and `files.comments.edit` API methods.

Vintage file comments remain accessible and deletable with `files.comments.get` and `file.comments.delete`.

## What's changing? {#what}

On May 22nd, 2019, `files.comments.add` and `files.comments.edit` will cease functioning. You won't be able to add or edit file comments.

`file.comments.add`, in particular, will no longer transmute your comments into [message threads](/messaging#threading).

In consequence, the documentation for these methods will no longer be made available.

## What isn't changing? {#not_changing}

`files.comments.get` and `files.comments.delete` will continue to function. Use them to retrieve and delete historical file comments. `files.comments.get` just might be the last place on the internet where it's safe to read the comments. And if it isn't — well you still have `files.comments.delete`.

## How do I prepare? {#how}

If you're still using `files.comments.add`, your business logic will need alteration to support file threads. Our [July 2018 changelog](/changelog/2018-05-file-threads-soon-tread) details the migration path to replying to file thread parent messages with \[`chat.postMessage`\] instead.

You won't be able to edit vintage file comments with `file.comments.edit`. As file comments are no longer _created_, this limitation effects only your ability to edit historically created comments. If you want to edit threaded messages in reply to a message about a file instead, use [`chat.update`](/reference/methods/chat.update).

## When is this happening? {#when}

We'll finish retiring these dusty methods on **May 22nd, 2019**.

[Let us know](https://slack.com/help/requests/new) if you have a comment or concern. Thank you!

**Tags:**

* [Deprecation](/changelog/tags/deprecation)
