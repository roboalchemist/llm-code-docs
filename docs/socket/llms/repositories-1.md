# Source: https://docs.socket.dev/docs/repositories-1.md

# Repositories

## Introduction

The Socket Repositories page provides a comprehensive overview of all the repositories being monitored by Socket for security vulnerabilities and other issues. This guide will walk you through the features and functionalities of the Repositories page, helping you understand how to manage and review your repositories efficiently.

## Overview

The Repositories page lists all the repositories associated with your organization, displaying critical information and allowing you to sort and filter the data to meet your needs.

### Key Features

1. **Repository List**: Displays all repositories being tracked, with options to sort and search.
2. **Scans**: Shows the scans generated for each repository, including details about vulnerabilities and issues found.
3. **Alerts**: Provides a detailed view of alerts categorized by severity and type.
4. **Dependencies**: Lists the dependencies identified within each repository, helping to track and manage third-party packages.
5. **Labels**: Custom organizational tags used to apply policies or segment repositories.

## Repository List

The repository list is the main section where all tracked repositories are displayed.

<Image align="center" src="https://files.readme.io/4ff2a33d9e3ec42614696f9f130c60da3613d1192dbe4d7ded75af81777222c2-Screenshot_2025-07-07_at_9.19.26_PM.png" />

### Repository Detail View

Each repository entry includes a Repository Detail View. Clicking a repository name opens the detail view, including:

* **Alerts**:
  * View open alerts grouped by action, priority, or severity. Each alert includes:
  * Severity badge
  * Type (e.g., CVE, Malware, License Violation)
  * Direct vs Transitive classification
  * Linked package, with quick access to deeper analysis
* **Dependencies**: See all direct and transitive dependencies used by the repository.
* **Scans**: Review historical scans (with timestamps and commit references).
* **Labels**: Manage repository categorization for targeted security or license policies.

<Image align="center" src="https://files.readme.io/4465458531db01e87d2e30aafb5456572769fbefd8581aeb64cf6abb35cc31f0-Screenshot_2025-07-07_at_9.21.34_PM.png" />

## Labels Tab

Use the Labels tab to:

* Organize repositories by team, function, or compliance tier
* Apply custom security or license policies to all repos with a specific label
* Toggle policy enforcement on or off per label group

<Image align="center" src="https://files.readme.io/21a06bac591e4a2a017184de3e862a858b491e7ea9fbba470e10590c86b58be3-Screenshot_2025-07-07_at_9.20.39_PM.png" />

<br />

### Sorting and Searching

You can sort the repositories by name or by label. Use the search bar to quickly find a specific repository.

## Scans

Each repository has an associated [Scans](https://docs.socket.dev/docs/scans) section, where you can view all the scans that have run for that repository. Scans provide detailed insights into the security posture of the repository, including any detected vulnerabilities or issues.

<Image align="center" src="https://files.readme.io/8b4908ea8f783cd84ad520292e37ee8e5f2d8c04df5bdf545b70e64ec2dc755e-Screenshot_2025-07-07_at_9.21.47_PM.png" />

### Scans Details

Clicking on a scan will open a detailed view where you can see:

* **Alerts**: Detailed information on alerts, categorized by severity (Critical, High, Medium, Low).
* **Dependencies**: A list of dependencies found in the repository.
* **Files**: The specific files within the repository where issues were detected.

<Image align="center" src="https://files.readme.io/9985faee8cdd814dbc055c29c10193318b07c197d4112e7ff04f04bdea726399-Screenshot_2025-07-07_at_9.47.17_PM.png" />

#### Alerts

The Alerts section within a report provides a comprehensive view of all the detected issues, allowing you to filter and sort by severity, category, and type. This helps in quickly identifying and prioritizing critical issues.

#### Dependencies

The Dependencies section lists transitive or direct dependencies used within the repository. This section is crucial for tracking and managing dependencies, ensuring that all packages are up-to-date and secure.

#### Files

The Files section lists files used within the repository. You can select individual files to view the contents.

<Image align="center" src="https://files.readme.io/8f2c9b6f830efb3a913c6f5dbea96292582840acd30795a37964e32cfa90f286-Screenshot_2025-07-07_at_9.48.03_PM.png" />

## Conclusion

The Socket Repositories page is a powerful tool for managing the security and compliance of your code repositories. By leveraging the features described in this guide, you can effectively monitor and address security issues, ensuring the integrity and safety of your software projects.