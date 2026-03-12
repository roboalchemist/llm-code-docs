# Source: https://docs.getint.io/getintio-platform/workflows/filtering-items-for-integration-in-getint/troubleshooting-sync-issues-unmet-filter-conditions.md

# Troubleshooting Sync Issues: Unmet Filter Conditions

There can be instances where syncs do not occur due to unmet filter conditions. This article aims to guide you on how to handle such situations better, how to find the item that did not meet the condition, how to edit filters, and how to resync items.

When a sync does not happen, it’s often due to certain conditions not being met. These conditions are usually defined by filters that are set up to ensure that only relevant data is synced. If an item does not meet these filter conditions, it will not be synced.

&#x20;

1. Go to your integration and click on **Latest synced items.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0jIUZuu3vRUgBPXYxkxI%2F26e510e8-2e6b-4b67-bbf3-a2e531b8bada.png?alt=media&#x26;token=43abd94f-71ee-49a3-98ff-939d0c1cf1b8" alt=""><figcaption></figcaption></figure>

1. Identify which items didn’t meet the filter conditions. Filter rules will be verified at the beginning of the sync, and if they do not match, the sync will be broken due to the unmet condition.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9zrUecwUw7nFNiBZeelx%2FLocate%20filtered%20items%20(2).png?alt=media&#x26;token=afc3b88b-6eda-457a-9c96-25ffb3db6644" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F4wwDYUs5u2qx024FJVTQ%2FFilters%20parameters%20were%20not%20met%20(2).jpg?alt=media&#x26;token=797dabb7-73ec-4f59-9b33-88b0d81540f7" alt=""><figcaption></figcaption></figure>

1. Check the **logs** to find the source of the issue. For the below example, Getint couldn’t find the items containing the following conditions: "Labels contains one of Spam, Duplicated Case, Introduction". Our labels didn’t have any of these values and due to this, the flow breaks, and the sync process is interrupted.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9DhzXisl1WWirsU1u6jO%2Fb997c47fb4feaf01df52bc7512e199f4%20(2).png?alt=media&#x26;token=2b577e07-29b8-496f-8d86-5c4b25f5891e" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FHQLHQhfp7nGNnS7ICkuJ%2F690df0b778eee4515dcb03567e5877e61%20(2).png?alt=media&#x26;token=f2505098-3703-4002-87be-3daf745e7932" alt=""><figcaption></figcaption></figure>

1. Review the filter settings, and adjust the conditions for the filters, making sure that the defined values are compatible. For this specific scenario, instead of "contains one of", the condition should be "not contains". After finalizing the rule definitions, click on **Apply** to maintain the item filtering for the specific application. Don’t forget to hit **Save** to secure the changes made to the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FbFpDCSLZkWwuCdYuoQMt%2F6b9186dab505d1521b532e18932b9585%20(2).png?alt=media&#x26;token=1d98432e-b506-4b22-b747-a7df4be9aa3a" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F7vbGwRGtc1cVa9YpYAiN%2Ffee02590dba77c69fa4f192e5126218e%20(2).png?alt=media&#x26;token=68850762-e52d-44c3-b64c-f467390727c1" alt=""><figcaption></figcaption></figure>

1. Go back to your latest synced items, locate the items that did not meet conditions before and you want to update, click on the 3-dot button, and resync them.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FbZbQZx74lpdfpzaKvRBI%2FResync%20(2).png?alt=media&#x26;token=63665b4d-4d0c-490e-8266-0faf87051019" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9HLoW9myF0yQtFDPpLNY%2F9ba90523cccf64161c221dd9e7904be1%20(2).png?alt=media&#x26;token=e5180c41-6c51-4677-be52-728bd93f177d" alt=""><figcaption></figcaption></figure>

As you can see, the items are now syncing due to the recent changes. Please remember that if you establish multiple rules within a single category (ALL / NEW / SYNCED), they will be interconnected with the AND operator. This means an item must fulfill all the rules to qualify for further synchronization.

If you continue to experience difficulties, consider contacting our [support team.](https://getint.io/help-center) At Getint, we’re equipped to assist you in resolving any specific issues you may encounter.
