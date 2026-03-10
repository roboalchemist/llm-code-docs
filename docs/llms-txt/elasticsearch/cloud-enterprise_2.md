# Source: https://www.elastic.co/docs/release-notes/cloud-enterprise

﻿---
title: Elastic Cloud Enterprise release notes
description: Review the changes, fixes, and more in each version of Elastic Cloud Enterprise. To learn about security updates, go to Security announcements for the...
url: https://www.elastic.co/docs/release-notes/cloud-enterprise
products:
  - Elastic Cloud Enterprise
---

# Elastic Cloud Enterprise release notes
Review the changes, fixes, and more in each version of Elastic Cloud Enterprise.
To learn about security updates, go to [Security announcements for the Elastic stack](https://discuss.elastic.co/c/announcements/security-announcements/31).
<note>
  To view release notes for previous versions of Elastic Cloud Enterprise, refer to [this page](https://www.elastic.co/guide/en/cloud-enterprise/3.8/ece-release-notes-3.8.0.html).
</note>


## 4.0.3


### Features and enhancements

- Added fixes for potential security vulnerabilities. Refer to our [security advisory](https://discuss.elastic.co/c/announcements/security-announcements/31) for details.


## 4.0.2


### Features and enhancements

- Added fixes for potential security vulnerabilities. See our [security advisory](https://discuss.elastic.co/c/announcements/security-announcements/31) for details.


## 4.0.1


### Features and enhancements

- Added security updates through various dependencies upgrades.


## 4.0.0

This release introduces [breaking changes](https://www.elastic.co/docs/release-notes/cloud-enterprise/breaking-changes).

### Features and enhancements

- Compatibility updates: Refer to the [Elastic Cloud Enterprise compatibility matrix](https://www.elastic.co/support/matrix#elastic-cloud-enterprise) to view the supported OS and container engine combinations for this version.
- Upgraded system deployments to Elastic Stack 8.18.0.
- Upgraded metricbeat and filebeat for allocator-metricbeat and beats-runner to version 8.18.0.
- Support for Elastic Stack 9.0.0


### Fixes

- Improved range request download performance for large heap dumps.
- Fixed a warning error incorrectly displaying due to a cache issue when trying to upgrade a deployment to a newer version.