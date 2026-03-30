# Source: https://docs.gitguardian.com/honeytoken/manage.md

# Manage your population of honeytokens

> Explains how to view, filter, and manage your population of honeytokens in the GitGuardian dashboard, including tagging and honeytoken limits.

## Overview

The Honeytoken module homepage presents the list of your honeytokens, displaying the main information as well as the status of each one.

![Overview](/img/honeytoken/overview.png)

You can filter the honeytokens based on a number of filters:

- Type of honeytokens
- Source (monitored repositories where the honeytoken is located)
- Status (Active, Triggered, Revoked)
- GitGuardian Tag (`Publicly exposed`)
- [Custom Tag](../platform/collaboration-and-sharing/custom-tags)

Clicking on the honeytoken name will direct you to its detail page.

![Honeytoken detailed page](/img/honeytoken/detailed-page.png)

- The Information section summarises the main information about your honeytoken and allows you to edit the name, description and custom tags.
- The Events section is where any usage of the honeytoken will get logged.
- The Timeline section provides the history of the honeytoken: when and where it was created, edited, deployed in a monitored source, triggeredâ¦ It is also possible to add comments there.

## Assigning Tags to Honeytokens

Each honeytoken can receive one or several custom tags. Please note that when assigning custom tags to a honeytoken, only one value from each key may be used.

## Number of allowed honeytokens

AWS honeytokens are available in a limited number. If you have reached this limitation, it is not possible to create new honeytokens anymore.

Revoked honeytokens are not included in the count of honeytokens. Only active and triggered honeytokens are included.

If you donât have enough honeytokens, you can reach out to GitGuardian to discuss extending your limitation.
