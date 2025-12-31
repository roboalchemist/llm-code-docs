# Source: https://planetscale.com/docs/postgres/cluster-configuration/maintenance-windows.md

# Maintenance windows

> Maintenance windows have been temporarily disabled for PlanetScale Postgres databases.

PlanetScale Postgres databases previously supported weekly maintenance windows, during which Postgres image upgrades would occur. These required connections to be terminated and re-established on upgraded nodes.

To ensure better connection stability for customers, we've moved to optional updates and have temporarily disabled maintenance windows for Postgres databases.

You can now [manually update your cluster](/docs/postgres/cluster-configuration/updates) to access new extensions and other software updates.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt