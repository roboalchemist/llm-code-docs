# Source: https://docs.nats.io/running-a-nats-service/nats_admin.md

# Managing and Monitoring your NATS Server Infrastructure

Managing a NATS Server is simple, typical lifecycle operations include:

* Using the [`nats`](https://docs.nats.io/using-nats/nats-tools/nats_cli) CLI tool to check server cluster connectivity and latencies, as well as get account information, and manage and interact with streams (and other NATS applications). Try the following examples to learn about the most common ways to use `nats`.
  * `nats cheat`
  * `nats cheat server`
  * `nats stream --help` to monitor, manage and interact with streams
  * `nats consumer --help` to monitor, manage stream consumers
  * `nats context --help` if you need to switch between servers, clusters or user credentials
* Using the [`nsc`](https://docs.nats.io/using-nats/nats-tools/nsc) CLI tool when using JWT based authentication and authorization, to create, revoke operators, accounts, and user (i.e. client applications) JWTs and keys.
* [Sending signals](https://docs.nats.io/running-a-nats-service/nats_admin/signals) to a server to reload a configuration or rotate log files
* [Upgrading](https://docs.nats.io/running-a-nats-service/nats_admin/upgrading_cluster) a server (or cluster)
* Understanding [slow consumers](https://docs.nats.io/running-a-nats-service/nats_admin/slow_consumers)
* Monitoring the server via:
  * The monitoring [endpoint](https://docs.nats.io/running-a-nats-service/nats_admin/monitoring) and tools like [nats-top](https://docs.nats.io/using-nats/nats-tools/nats_top)
  * By subscribing to [system events](https://docs.nats.io/running-a-nats-service/configuration/sys_accounts)
* Gracefully shut down a server with [Lame Duck Mode](https://docs.nats.io/running-a-nats-service/nats_admin/lame_duck_mode)
