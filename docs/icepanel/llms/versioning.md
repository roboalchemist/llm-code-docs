# Source: https://docs.icepanel.io/future-state-design/versioning.md

# Versioning

Versions let you create a snapshot of your design at a specific point in time so that you can track significant architectural decisions. You can create versions at **different levels of hierarchy, from landscapes to domains, systems, and apps.** Versions are static, and the diagrams and objects can't be edited or removed from your landscape.

{% hint style="warning" %}
On the Free plan, you can create up to 3 landscape versions. Versioning domains, systems, and apps is only available in Growth and Isolation plans.
{% endhint %}

## Versioning a landscape or domain

{% hint style="info" %}
Only Admins can version a landscape or domain.
{% endhint %}

To create a version of your landscape:

1. Click the `Current` button on the top left of the navigation beside the org name.
2. Click on the `Create version` button.
3. Select the level you want to version. By default, you are versioning the landscape. Select the drop down `Version` to version any other level. See below for more info on how to version system or app.
4. Enter a version number and add a note to help you track your changes.
5. Click on the `Create version` button to confirm.

You can view the version in the timeline or continue editing the latest version when complete.

{% hint style="info" %}
If your landscape contains many diagrams and objects, it may take up to 30 seconds to version.
{% endhint %}

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FIR6mfcuGr1znlUpJZfpX%2FClipboard-20250916-231201-138.gif?alt=media&#x26;token=955388a1-9c45-4631-b209-f28c5a457d42" alt=""><figcaption><p>Versioning</p></figcaption></figure>

You can only version a domain if you're in that specific domain.

### Scheduled landscape versions — Auto Version

{% hint style="info" %}
Only available on Growth plans and above.
{% endhint %}

You can schedule a landscape version to be created automatically once a week (every Friday at 8 pm in your timezone).

* Navigate to the version dropdown on the home page or diagram.
* Click the `auto version` checkbox

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FSWerr7mGslDgNoFBw6uf%2Fvid%202.gif?alt=media&#x26;token=581fb2ff-0e04-4928-bf91-a9ce19f35cfc" alt=""><figcaption><p>Auto Version</p></figcaption></figure>

## Versioning a system or app

{% hint style="info" %}
Only Admins and Editors on a team assigned ownership of the object can version systems or apps.
{% endhint %}

To version a domain, system or app:

1. Click the `Current` button on the top left of the navigation beside the org name.
2. Click on the `Create version` button.
3. Select the level you want to version. By default, you are versioning the landscape. Select the drop down `Version` to version any other level. You need to be at the level you are trying to version.
4. Enter a version number and add a note to help you track your changes.
5. Click on the `Create version` button to confirm.

{% hint style="warning" %}
You are only able to version an app-level diagram if you are at that level in IcePanel.
{% endhint %}

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2F2JWPdUqIgzfOZ6Sp2jd8%2FClipboard-20250916-233849-709.gif?alt=media&#x26;token=b3671928-05fb-48b9-b908-756540a22869" alt=""><figcaption><p>Versioning a domain, app or system</p></figcaption></figure>

## Viewing the version timeline

The version timeline is a visual way to track changes in your model. You can view a landscape's timeline to see how everything has changed, from domains to systems and apps, over time. This is useful for tracking significant changes in your architecture.

To view a landscape timeline:

1. Click the `Current` dropdown beside the landscape at the top left of the screen.
2. A timeline of your different versions will appear in the list ordered by the most recent.

Clicking on the dropdown of each version will show its notes. You can also rename the version, edit the notes, revert to the version, and share a link by clicking on the overflow menu.

{% hint style="warning" %}
You are only able to see the versions that have been created at the level you are currently looking at. To see domain/app/component level versions, you must to be at that level.
{% endhint %}

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FlykiQyZT0Eg3M6w7iKVU%2FClipboard-20250916-235124-970.gif?alt=media&#x26;token=ec808155-6aab-4481-ad91-fbbc106dc36c" alt=""><figcaption><p>Version timeline</p></figcaption></figure>

## Sharing a version

[sharing](https://docs.icepanel.io/collaboration/sharing "mention")

{% hint style="info" %}
Only available on Growth and Isolation plans.
{% endhint %}

You can share a specific version by selecting it from the home page or diagram and clicking the share link option. The version name will be labelled in the share link toggle.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FZCFs8kakK2WlZwsXqobW%2FScreenshot%202024-10-02%20at%202.20.43%E2%80%AFPM.png?alt=media&#x26;token=2ef7274c-2471-4cca-9699-bcaa5920fe33" alt=""><figcaption><p>Sharing a version</p></figcaption></figure>

## Reverting to a previous version

{% hint style="info" %}
Only available on Growth and Isolation plans.
{% endhint %}

To revert to a specific landscape or domain version:

1. Click on the `Current` dropdown in a landscape or diagram.
2. Expand the version to view more detail.
3. Click on the overflow menu and `Revert to this version` button.
4. Enter a reason for the reversion.
5. Click on `Revert to this version` to confirm.

{% hint style="warning" %}
Reverting can't be undone, and you'll lose your latest design. We recommend versioning your latest design before reverting.
{% endhint %}

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FCf8nLrJy5d1VY8gFzFcz%2FRevert-landscape-version.gif?alt=media&#x26;token=f7ba272c-82d0-4e33-89f9-a8d1d40ea606" alt=""><figcaption><p>Reverting to a landscape version</p></figcaption></figure>

## Versioning with drafts

[draft-current-vs-future-state](https://docs.icepanel.io/future-state-design/draft-current-vs-future-state "mention")

{% hint style="warning" %}
On free plans, you can create a maximum of 1 draft per diagram. To have unlimited drafts, upgrade to Growth or Isolation.
{% endhint %}

Any drafts you create will also be saved in the version. This allows you to see how ideas (as drafts) turn into permanent changes in your architecture in the timeline.
