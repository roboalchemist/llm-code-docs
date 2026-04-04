# Source: https://electric-sql.com/demos/burn.md

---
url: /demos/burn.md
description: Agentic system built on Postgres and a real-time sync stack.
---

# 🔥 Burn

Agentic system demo using Postgres with a [real-time sync stack](/blog/2025/08/12/bringing-agents-back-down-to-earth).

## Agentic sync

Burn is a multi-user, multi-agent demo app built on [TanStack DB](/products/tanstack-db) and [Phoenix.Sync](https://hexdocs.pm/phoenix_sync).

It shows how to build an agentic system on real-time sync, where:

* users and agents are automatically kept in sync
* memory means rows in a Postgres database
* context engineering is a representation of that database state

### Stack

Agentic memory and shared state are both [just rows in the database](https://pg-memories.netlify.app).

[ TanStack DB](/products/tanstack-db)

* provides a super fast client store for instant reactivity and local writes
* with live queries syncing data into standard React components

[ Phoenix.Sync](https://hexdocs.pm/phoenix_sync)

* exposes sync endpoints
* handles auth and writes
* runs agents as OTP processes

### Context

There's a lot of hype around agentic system development. Concepts like agentic memory, instruction routing, retrieval and context engineering.

When you dig into it, these all collapse down to processes and database state. You can build agentic systems with a database, standard web tooling and real-time sync.
