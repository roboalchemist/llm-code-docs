# Source: https://docs.luciq.ai/product-guides-and-integrations/product-guides/bug-reporting/bug-grouping.md

# Bug Grouping

## Overview

Bug Grouping helps teams stay focused by:

* **Detecting duplicate reports automatically** -> Reduces manual triage and repetitive review
* **Reflecting the true magnitude of an issue** -> See how many duplicates belong to the same underlying problem
* **Letting you act once on the master report** -> Key actions propagate across duplicates

This feature works **side-by-side** with manual duplication. Manual grouping continues to work as-is.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FyknsgT4ah5GLRy9iLp25%2Fimage.png?alt=media&#x26;token=9c375d9a-af5d-47a7-a15b-ca80e79d0c21" alt="" width="563"><figcaption></figcaption></figure>

***

### How it works

When a new report is received, Luciq evaluates it against recent reports and determines whether it belongs to an existing group or should remain ungrouped.

* **Semantic matching**: Reports are compared based on the meaning of their content to find likely duplicates.
* **Group assignment**: If a match is found, the report joins that group as a duplicate. If not, it stays ungrouped/single.
* **Fast fallback**: The grouping logic is done on our backend, so if an automatic grouping can’t complete quickly (with in 30-secs), the report is shown normally (ungrouped) so your workflow is never blocked.

{% hint style="info" %}

#### **Grouping Logic**

The grouping logic focuses primarily on:

* **Report description semantic similarity**, plus
* **Report category/type match** (e.g., Bug vs Question)

Notably:

* **Subcategory is not used** in grouping.
* Additional attributes (screen name, app version, etc.) **are not** part of the current grouping logic as well.
  {% endhint %}

***

### What you’ll see in the dashboard

#### Group types

Bug reports are presented as one of the following:

* **Ungrouped report**: not part of any group AKA Single report.
* **Manual grouping**: created by your team.
* **Automatic grouping**: detected and grouped automatically.

Automatic group masters are visually distinguished so you can tell what was auto-grouped vs manually grouped.

{% hint style="info" %}

#### Key concepts

* **Master report**: the parent report representing the group’s “canonical” issue.
* **Duplicate report**: a report automatically or manually marked as duplicate of a master.
* **Ungrouped/Single report**: not part of any group.
  {% endhint %}

#### Automatic group master details

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FPlG0Ur1YhOlrmoSvY1W8%2Fimage.png?alt=media&#x26;token=dc45a45e-f741-46b4-b2d8-952f2bc01bf1" alt="" width="563"><figcaption></figcaption></figure>

Automatic group masters include an “Automatic group master” section that provides:

* **Group summary**: A short description of the shared issue across duplicates
* **Grouping confidence**: A confidence indicator for the grouping decision
* **Number of grouped reports**: Total duplicates in the group
* **Show duplicates**: View all duplicates in a dedicated list/drawer

{% hint style="info" %}

#### **What to expect**

* **Group summary**: A concise description of the shared issue across the group. It may take a short time to appear after grouping.
* **Confidence**: A confidence indicator for automatic grouping decisions. Group-level confidence is derived from the duplicates within the group. Manual duplicates do not contribute to the confidence calculation.
  {% endhint %}

#### Automatic duplicate details

Automatic duplicates show a banner indicating they were automatically marked as duplicates, and provide a shortcut to view the master report.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FYqPg6T7lRSh5SjxTLUnQ%2Fimage.png?alt=media&#x26;token=bdf952c6-b688-4ac9-b92d-fbf1255fc440" alt="" width="563"><figcaption></figcaption></figure>

#### Actions & workflows

Automatic groups follow the same core workflow as manual duplicates:

* **Master-first actions**: Update status/assignee/priority on the master report and duplicates follow.
* **Duplicates are restricted**: You can’t apply master-level actions directly from duplicate reports.
* **Change group master / mark as duplicate**:
  * For ungrouped/single reports, you can mark them as duplicates of an existing master.
  * For master reports, you can change with another ungrouped or master reports. **Note:** When changing a master with another master, you’ll simply merge the two groups together.
  * For duplicate reports, you can unmark them as duplicates (removing them from the group).

#### Filtering & bulk actions

When Bug Grouping is enabled, the dashboard exposes a **Report Groups** filter that lets you view:

* **Ungrouped reports**
* **Automatic** -> Masters / Duplicates
* **Manual** -> Masters / Duplicate

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FBfviui5klrZzBDfYmjpB%2Fimage.png?alt=media&#x26;token=09298581-a0fe-4987-a407-c5bd7b18d369" alt="" width="312"><figcaption></figcaption></figure>

Bulk actions are intentionally limited to prevent accidental changes across duplicates. If your current filter selection includes duplicates or doesn’t target masters appropriately, bulk actions will be disabled with an explanatory tooltip.

***

## Tags (master vs duplicate)

Luciq tags reports when they are created so you can distinguish master vs duplicate reports consistently.

* **Master reports**: Master\_report
* **Duplicate reports**: Duplicate\_report

**Note:** If Tags Sync is disabled in your 3rd party integration, master reports tag may not appear in certain tracking views when forwarding automatically.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FvHntsYjYgaMoXBPyiYXd%2Fimage.png?alt=media&#x26;token=76795499-3803-4079-aca4-fc2992015a09" alt="" width="563"><figcaption></figcaption></figure>

***

## What to expect (and what not to expect)

**What to expect**

* Faster triage through automatic duplicate detection
* Clear distinction between manual and automatic groups
* Master-first workflow: one action on master updates the group

**What not to expect**

* New reports will not be automatically grouped into existing manual groups
* Perfect grouping in every case, yet. (you can always adjust groups manually)
* Duplicate grouping into closed/resolved issues (closed groups won’t continue collecting new duplicates)

***

## Enabling Bug Grouping

* Want to enable Bug Grouping? Please reach out to our support team or your Customer Success Manager.
* **Note:** After enabling the feature, **grouping will be applied only to reports that are received after the feature is enabled**; it won’t be applied retroactively to old bug reports.
