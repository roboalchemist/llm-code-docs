Source: https://docs.slack.dev/changelog/2019-03-wild-west-for-files-no-more

# Wild West no more (for file limits, at least)

March 1, 2019

Free teams feature a 5 GB limit on file uploads. However, as in the Wild Wild West of yore, the limit wasn't enforced. As of March 5, 2019, we're starting to enforce the file upload limit more firmly: only the last 5 GB of files will be visible to Free teams. In APIs that return file uploads, older files beyond the limit will be shown as 'tombstoned,' with redacted information and a `"hidden_by_limit"` field.

## What's changing {#what}

For **Free teams only**, the 5 GB file upload limit will be enforced. Expect tombstoned files in 3 sets of API endpoints:

1. [`conversations.history`](/reference/methods/conversations.history), [`pins.list`](/reference/methods/pins.list), and [`stars.list`](/reference/methods/stars.list)
2. [`search.all`](/reference/methods/search.all) and [`search.files`](/reference/methods/search.files)
3. [`files.list`](/reference/methods/files.list); [`files.info`](/reference/methods/files.info); [`files.revokePublicURL`](/reference/methods/files.revokePublicURL); [`files.sharedPublicURL`](/reference/methods/files.sharedPublicURL)

A redacted (or "tombstoned") file will be identified by the field `"mode": "hidden_by_limit"`. For example, the `conversations.history` method might return the following:

```json
{   "ok": "true",   "messages": [        {            "type": "message",            "text": "",            "files": [                {                    "id": "FEKKRPL9G",                    "mode": "hidden_by_limit",                }            ]        }   ],   "has_more": false,   "pin_count": 0}
```text

### Deleting or revoking tombstoned files {#deleting-or-revoking-tombstoned-files}

In order to gather information on tombstoned files, so that you can delete or revoke them, pass the `show_files_hidden_by_limit` parameter to [`files.list`](/reference/methods/files.list). While the returned files will still be redacted, you'll gain the `id` of the files so that you can delete or revoke them.

`files.delete` works as expected on tombstoned files. Also, the [`files.revokePublicURL`](/reference/methods/files.revokePublicURL) method will still work, even on tombstoned files. However, the response will contain the tombstoned version of the file, not the full version.

## How do I prepare? {#how}

Expect and prepare your app for tombstoned files by checking for `"mode": "hidden_by_limit"` on files that you wish to manipulate.

## When does this happen? {#when}

As of March 5, 2019. If you have a comment or concern, please [let us know](https://slack.com/help/requests/new).

## Tags:

* [Announcement](/changelog/tags/announcement)
