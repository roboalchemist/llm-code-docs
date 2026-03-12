# Source: https://clickhouse.ferndocs.com/cloud/manage/backups/configurable-backups.md

---
sidebar_label: Configure backup schedules
slug: /cloud/manage/backups/configurable-backups
description: Guide showing how to configure backups
title: Configure backup schedules
keywords:

- backups
- cloud backups
- restore
doc_type: guide

---

import {CloudNotSupportedBadge} from '../../../../../components/Badges/CloudNotSupportedBadge'
import {ScalePlanFeatureBadge} from '../../../../../components/Badges/ScalePlanFeatureBadge'

<ScalePlanFeatureBadge feature="Configurable Backups" linking_verb_are="True"/>

To configure the backup schedule for a service, go to the **Settings** tab in the console and click on **Change backup configuration**.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/39c5eb4f3b6fb9d8788e7cabbd3df2ffa4d2b35c95704e68cdb627c6ecd70aea/images/cloud/manage/backup-settings.png" alt="Configure backup settings"/>

This opens a tab to the right where you can choose values for retention, frequency, and start time. You will need to save the chosen settings for them to take effect.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/8c9be6eb3bf7b55d05ce5a89dd99f4d4987fb7ee4946e4201ba64a4465d71b90/images/cloud/manage/backup-configuration-form.png" alt="Select backup retention and frequency"/>

<Note>
Start time and frequency are mutually exclusive.
Start time takes precedence.
</Note>

<Note>
Changing the backup schedule can cause higher monthly charges for storage as some of the backups might not be covered in the default backups for the service.
See ["Understanding backup cost"](/cloud/manage/backups/overview#understanding-backup-cost) section below.
</Note>
