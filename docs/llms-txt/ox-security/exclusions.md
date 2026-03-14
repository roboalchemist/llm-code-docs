# Source: https://docs.ox.security/exclusions-and-sla/scope-policy-and-sla-compliance/exclusions.md

# Exclusions

{% hint style="success" %}
**At a glance:** Review the applications, issues, detection rules, and policies manually marked as irrelevant or excluded from scans. Remove exclusions as necessary to include these entities in future scans.
{% endhint %}

<div align="left"><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-9b67658ce6014e099b3b258c9c7cc18bc46a11de%2Fexclusions.png?alt=media" alt=""></div>

## Overview

The **Exclusions** page displays a summary of all applications, issues, detection rules, and policies ("entities") manually marked as irrelevant or excluded from scans. These entities will be excluded from all future scans unless the exclusion is removed.

* See the [table](#entity-types-and-available-actions) below for a detailed list of entity types that can appear on the **Exclusions** page.

## Removing an exclusion (and other actions)

From the **Exclusions** page, you can remove an entity's exclusion (so that it is considered in future scans) and perform other actions depending on the entity type.

* See the [table](#entity-types-and-available-actions) below for the actions that can be performed on the **Exclusions** page for each entity type.

**To remove an entity's exclusion or perform other actions:**

1. Click the **Actions** icon <img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-22a02bc32aa25670ae35904e534bf6ad83dfb84c%2Factions_icon.png?alt=media" alt="" data-size="line"> on the far right side of the entity's row.
2. Select the action you want to perform.
3. In the dialog, confirm that you want to perform the action.

{% hint style="warning" %}
When an entity's exclusion is removed, that entity is immediately removed from the **Exclusions** page. However, issues related to that entity are not included in scan results until a new scan is performed.
{% endhint %}

## Entity types and available actions

| Entity type         | Details                                                                                                                                                                                                                                                                                                                                                                                      | Actions available from the Exclusions page                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Applications**    | <p>The <strong>Exclusions</strong> page displays only applications manually marked as irrelevant from the <strong>Applications</strong> or <strong>Issues</strong> pages.</p><ul><li><strong>Not listed:</strong> Applications automatically determined by OX to be irrelevant. (These applications can be seen and managed on the <strong>Irrelevant applications</strong> page.)</li></ul> | <ul><li><p><strong>Make app relevant: always</strong></p><ul><li>The app is included in all future scans</li></ul></li><li><p><strong>Make app relevant: OX dynamic</strong></p><ul><li>The app is included in future scans unless is automatically determined by OX to be irrelevant</li></ul></li></ul><p><em>See the note below for additional information about what makes an app irrelevant.</em></p>                                                    |
| **Issues**          | The **Exclusions** page displays issues excluded from the **Issues** page.                                                                                                                                                                                                                                                                                                                   | <ul><li><strong>Remove exclusion</strong></li><li><p><strong>Update exclusion expiry date</strong></p><ul><li>Allows you add an expiration date to an excluded issue without one</li><li>Allows you to change the expiration date of an excluded issue with one</li></ul></li><li><p><strong>Remove snooze</strong></p><ul><li>Option is available only if the excluded issue currently has an expiration date</li></ul></li></ul>                            |
| **Detection rules** | <p>The <strong>Exclusions</strong> page displays detection rules excluded from the <strong>Issues</strong> page:</p><ul><li>For a single app</li><li>For all apps</li></ul>                                                                                                                                                                                                                  | <ul><li><strong>Remove exclusion</strong></li><li><p><strong>Update exclusion expiry date</strong></p><ul><li>Allows you add an expiration date to an excluded detection rule without one</li><li>Allows you to change the expiration date of an excluded detection rule with one</li><li><p><strong>Remove snooze</strong></p><ul><li>Option is available only if the excluded detection rule currently has an expiration date</li></ul></li></ul></li></ul> |
| **Policies**        | <p>The <strong>Exclusions</strong> page displays policies excluded from the <strong>Issues</strong> page.</p><ul><li><strong>Not listed:</strong> Policies that have been turned off from the <strong>Policies</strong> page. (These applications can be seen and managed on the <strong>Policies</strong> page).</li></ul>                                                                  | <ul><li><strong>Enable policy</strong></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                              |

{% hint style="info" %}
**What makes an app irrelevant?**

OX automatically designates an app as irrelevant when:

* The app's repo has been archived
* The app is inaccessible for cloning
* No relevant files are identified in the repo
* There have been no code changes during the past 6 months
  {% endhint %}
