# Source: https://docs.socket.dev/reference/historical-data-endpoints.md

# Historical Data Endpoints

Historical data endpoints provide access to historical data that is collected via periodic snapshots and other events

The Socket platform periodically collects historical data and stores this data as *historical snapshots*. Historical snapshots are automatically collected at least once a day but customers can request on-demand snapshots (within the limits of their pricing plan).

Historical data is automatically "bucketed" to the nearest day by truncating the scan date to the nearest day based on the UTC time zone. For example, if a scan occurs at January 1, 2025 3:15pm UTC then the data collected for that scan will be associated with the day starting at January 1, 2025 12am UTC. This approach to bucketing data impacts how data is aggregated by day when fetching trend data. Also, when fetching historical data, the returned data is filtered to include only the data based on the *last scan of each day* for a given source code repository. For example, if a specific repository is scanned 5 times on January 1, 2025, the only the data for the last scan on January 1, 2025 will be returned.

The Socket API provides the following endpoints for accessing and managing historical data:

* [List historical alerts](https://docs.socket.dev/reference/historicalalertslist)
* [Fetch trend data for historical alerts](https://docs.socket.dev/reference/historicalalertstrend)
* [List details of periodic historical data snapshots](https://docs.socket.dev/reference/historicalsnapshotslist)
* [Start historical data snapshot job](https://docs.socket.dev/reference/historicalsnapshotsstart)

The Socket platform strives to provide consistent ingestion of historical data but there may be delays or gaps when collecting historical data. Customers should use the API endpoint for [listing recent historical snapshots](https://docs.socket.dev/reference/historicalsnapshotslist)  to review the history of snapshots.