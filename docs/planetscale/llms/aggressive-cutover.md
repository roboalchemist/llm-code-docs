# Source: https://planetscale.com/docs/vitess/schema-changes/aggressive-cutover.md

# Aggressive deploy request cutover

## Overview

Cutover is the critical final step in an online schema migration where Vitess atomically replaces the original table with a newly created "shadow" table that contains the updated schema. This process involves acquiring metadata locks, preventing writes to the original table, ensuring complete data synchronization, and renaming tables to complete the migration.

The cutover process can fail or time out when the table is locked by long-running queries or transactions, preventing Vitess from acquiring the necessary metadata locks. When this happens, Vitess will retry the cutover operation until it succeeds.

Aggressive cutover is a setting that forces the cutover to complete immediately by killing any queries or transactions that are blocking the operation. When enabled, the system will prioritize schema migration completion over preserving running queries.

## When to enable aggressive cutover

You should consider enabling aggressive cutover in these scenarios:

1. **Migration delayed due to long-running transactions**: If you receive the "Migration delayed due to long-running transactions" notice on your deploy requests, this indicates that the cutover cannot complete because there are long-running transactions on the table. Enabling aggressive cutover will force the cutover to happen by killing those blocking queries.

2. **Application has slow queries or long-running transactions**: If your application consistently runs slow queries or long-running transactions that prevent migrations from completing, aggressive cutover may be necessary. This setting is disabled by default because well-optimized applications should not require it.

## How it works

Aggressive deploy request cutover can be enabled for a database by admins only. To enable the setting, visit the database settings page and look under "Advanced settings".

When aggressive cutover is enabled, the system immediately begins killing queries and transactions that are using or locking the migrated table on the very first cutover attempt. This aggressive approach ensures the migration completes without waiting for blocking operations to finish naturally.

**Normal cutover behavior:**

* Vitess attempts to acquire locks on the table
* If blocked by ongoing queries/transactions, it waits and retries
* This process continues until the cutover succeeds or 1 hour elapses
* After 1 hour the cutover will be forced

**Aggressive cutover behavior:**

* Vitess immediately kills any queries or transactions blocking the cutover
* The cutover proceeds without waiting for blocking operations to complete

**Important considerations:**

* Having retry logic or a strategy to handle re-running the killed queries is advised
* Once enabled, this setting applies to all future deploy requests

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt