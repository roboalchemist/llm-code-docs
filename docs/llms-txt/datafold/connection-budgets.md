# Source: https://docs.datafold.com/data-diff/connection-budgets.md

# Connection Budgets

> How connection budgets are enforced across data diffs in Datafold

## Overview

Datafold now supports **shared connection budgeting** across

* in-database diffs
* cross-database diffs
* in-memory diffs

This feature ensures consistent, predictable behavior for database usage across the system—particularly important in environments with limited database connection capacity.

***

## ✨ Shared Connection Budgeting

Datafold now enforces a **shared connection limit per database** across all supported diff runs.

When a maximum number of connections is configured on a data source, this limit is respected **collectively** across all running diffs that target that source—regardless of the type of diff.

This ensures that no combination of diff runs will exceed the specified connection cap for the database, providing:

* ✅ More predictable resource usage
* ✅ Protection against overloading the database
* ✅ Simpler configuration and expectation management

Connection limits are enforced automatically once set—no need to configure them at the individual diff level.

***

## ✅ Scope of This Feature

| Jobs                 | Connection Budget Applied? |
| -------------------- | -------------------------- |
| in-database diffs    | ✅ Yes                      |
| cross-database diffs | ✅ Yes                      |
| in-memory diffs      | ✅ Yes                      |
| Schema Fetching      | ❌ No                       |
| Lineage & Profiling  | ❌ No                       |
| SQL History          | ❌ No                       |
| Monitors             | ❌ No                       |

***

## ⚙️ Configuration

Shared connection budgeting is controlled via your **data source configuration**.

Once a `Max Connections` limit is set, it will be automatically enforced **across all supported diff runs** targeting that database.

## 📬 Feedback

Questions, suggestions, or unexpected behavior? Reach out to the Datafold team via your usual support or engineering channels.

***
