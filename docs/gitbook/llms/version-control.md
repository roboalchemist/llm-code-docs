# Source: https://gitbook.com/docs/documentation/ja-gitbook-documentation/creating-content/version-control.md

# Source: https://gitbook.com/docs/documentation/zh/creating-content/version-control.md

# Source: https://gitbook.com/docs/documentation/fr/creating-content/version-control.md

# Source: https://gitbook.com/docs/creating-content/version-control.md

# Version control

You can easily monitor all the changes people have made to your content using to the **Version history** side panel.

### Version history <a href="#see-the-activity-of-a-specific-draft" id="see-the-activity-of-a-specific-draft"></a>

In the Version history of a space, you can see a list of all the actions that changed the content within it. These include:

* When someone made [live edits](https://gitbook.com/docs/collaboration/live-edits) to the space.
* When someone merged a [change request](https://gitbook.com/docs/collaboration/change-requests).
* When someone performed a [Git Sync](https://gitbook.com/docs/getting-started/git-sync) operation.

### View historical versions of content

To view past versions of your content and see the changes that were made, click the **Version history** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F1Ntpa0YjoayuQOU0zbXt%2Fhistory%20-%20dark.svg?alt=media&#x26;token=a3d28850-951f-4a24-b4da-a44fe00b1319" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FVEyYlyeOFMIwGJkpdIWh%2Fhistory.svg?alt=media&#x26;token=60e30952-2289-4eec-b185-bcc7308347af" alt="The Version history icon in GitBook"></picture> button in the [space header](https://gitbook.com/docs/resources/gitbook-ui#space-header), or open the **Actions menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2Fpn5vEw7bYFrMPpdyvpSu%2Factions-horizontal%20-%20dark.svg?alt=media&#x26;token=ec39eefe-a391-4fe2-828a-082b79f2847d" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FPnnI41SqLSaKBNwT98fW%2Factions-horizontal.svg?alt=media&#x26;token=99754200-a354-4ffe-931e-aa6322ea7395" alt="The Actions menu icon in GitBook"></picture> next to the space or change request title and choose **Version history**.

Click on any item in the list to see how your content looked at the point this change was made. This is very similar to how you view [change requests](https://gitbook.com/docs/collaboration/change-requests).

### Show changes

When you are viewing an old version of your content, you can choose to highlight the differences between the old and current content — similar to [diff view in a change request](https://gitbook.com/docs/collaboration/change-requests#diff-mode).

To enable or disable this, use the **Show changes** toggle at the bottom of the **Version history** side panel.

With show changes enabled, content that has changed will be highlighted by an icon on the left of its content block.

### Viewing historical published versions

If you're investigating the version history of a published space, you can also view previews of what the previous versions looked like in the published context (i.e. what the end user would see).

You can do this by:

{% stepper %}
{% step %}
From the version history side panel, select the revision
{% endstep %}

{% step %}
Copy the ID at the end of the URL
{% endstep %}

{% step %}
Add it at the end of your published docs URL as `/~/revisions/<id>`
{% endstep %}
{% endstepper %}

### Roll back to a previous version

Rolling back allows you to revert a space’s content to the way it was at a previous point in time. This is helpful if you’ve accidentally made a breaking change or deleted content and need to quickly get back to a previous version of the space.

To roll back to a previous version of your space, hover over the version in the side panel, click the **Actions button** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> and select **Rollback**.
