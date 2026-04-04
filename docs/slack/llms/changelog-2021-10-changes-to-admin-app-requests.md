Source: https://docs.slack.dev/changelog/2021-10-changes-to-admin-app-requests

# Changes to admin apps requests

October 30, 2021

`admin.apps.requests.list` API is enhanced to fetch Org AAA requests using **enterprise\_id** arg.

## What's changing {#changed}

* **enterprise\_id** arg is used to fetch Org AAA requests.
* **team\_id** arg is used to fetch Workspace AAA requests.

Either one of the arg (**enterprise\_id**, **team\_id**) should be populated.

## How to respond or prepare {#prepare}

If you don't plan to fetch organization AAA requests, you don't need to do anything.

## When is this happening {#when}

This change happens on Oct 29, 2021.

**Tags:**

* [New feature](/changelog/tags/new-feature)
