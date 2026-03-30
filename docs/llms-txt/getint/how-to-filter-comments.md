# Source: https://docs.getint.io/getintio-platform/workflows/filtering-items-for-integration-in-getint/how-to-filter-comments.md

# How to Filter Comments

With the introduction of the comments filtering feature in Getint (available from version 1.59), you can now further customize your integrations. This feature allows you to establish conditions to either include or exclude comments based on your selected criteria. For example, you can configure the system to exclude all comments that lack a certain value or to include all comments that contain specific values.

### Understanding the Filter Logic in Getint

The filters in our system currently use the **AND** operator, not **OR**. This means that when multiple filters are specified, all conditions must be met to filter the comment. However, some users may believe the filters operate using **OR** logic, where any single condition being true would be sufficient.

Using **OR** logic for a single condition that **contains one of** rule is possible. However, this will apply to only one attribute. If you have additional filters, you must still meet all the other conditions to sync the items.

At present, our system only supports **AND** logic. If users specify multiple filters, all conditions must be true for the filters to apply. This is crucial to understand, especially for users who have set many conditions, as it may lead them to assume the filters work with **OR** logic, which is not the case.

{% hint style="info" %}
**Note:** We plan to implement **OR** logic in the future. Until then, it is advisable only to use one condition for the left and right filters, or be aware that the current behavior applies **AND** logic. Therefore, you must meet all specified conditions.
{% endhint %}

### Where to Find the Comments Filtering Feature

Go to your integration and select the type mapping you want to modify, then click on **Comments & Attachments.** From this tab, you can set different parameters according to your needs:

{% embed url="<https://www.loom.com/share/042e66cf4f65437cb801d07c130370e6?sid=6d9b8516-7ea8-4305-8bb1-f2b73ab352be>" %}

1. You can synchronize comments in either direction or both directions. However, note that if you select one-way sync for an app, the option for the other direction will be greyed out.
2. In the next dropdown, you can add conditions to your filtering options, allowing you to exclude or permit comments that either match or do not match your specified criteria.
3. Select the **Attribute** and the **Condition** of your filters.
4. Click on **Apply,** and **SAVE** your integration to submit your changes.

#### Filtering by Date and Time

One of the most common use cases for this is filtering comments to include only those created before or after a specific date or time.

**Date format**: Use the format `YYYY-MM-DD`, for example: `2025-10-03`.

**Datetime format**: Use the same date format, followed by a **T** to separate date and time, then a time down to seconds, and a 4-digit UTC offset in hours and minutes: `YYYY-MM-DDThh:mm:ss.HHMM`, for example: `2025-09-25T12:00:00.0200`.

**Important notes**:

* Any trailing components can be omitted—starting with timezone, then seconds, minutes, etc.
* Omitted values will default to zero. For example:
  * `2025-09-25T12` → interpreted as `2025-09-25T12:00:00.0000`
  * `2025-09-25T12:30` → interpreted as `2025-09-25T12:30:00.0000`

This allows you to filter with just the level of precision you need.

#### Need Further Assistance?

Getint provides a robust and flexible way to filter comments in your integrated apps. By understanding how to use this feature, you can ensure that only the relevant comments get synced, enhancing the efficiency of your workflows.

Remember, if you encounter any issues or need further assistance, Getint’s [support team](https://getint.io/help-center) is always ready to help.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FpRuysXB9jr3WVOSLv549%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=f7443fab-03d0-4434-9144-cb386de8904c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
