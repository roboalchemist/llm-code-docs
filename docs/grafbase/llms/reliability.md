# Source: https://grafbase.com/docs/gateway/deployment/reliability.md

# Reliability

Grafbase Gateway is a single stateless binary. It communicates with the Grafbase platform in the following ways:

## Schema polling

When the gateway is started with a graph reference (`--graph-ref`) without an local schema file, the gateway will periodically, every 10s, poll the Object Storage service of the platform
for a schema update. If a new a schema is found, the gateway will load the new schema in the background and switch atomically to the new schema whenever it's ready
to accept requests. If the schema is passed explicitly as a file with `--schema`, this service will never be called.

Object Storage is a simple and independent service from the GraphQL API exposed by the platform. It acts as a proxy for S3. With a limited feature set it's conceived first and foremost for reliability and performance.
If it ever becomes unavailable, the gateway will continue operating normally but won't receive any schema update. The gateway will emit error logs for every poll error.

## OpenTelemetry

 By default, Grafbase Gateway sends OpenTelemetry data via gRPC to an OpenTelemetry endpoint we call Telemetry Sink. We ingest the data and compute field analytics and more from this. If this endpoint becomes unavailable, the gateway will continue operating normally but analytics and traces won't appear in the dashboard. It will not impact other OpenTelemetry exporters.