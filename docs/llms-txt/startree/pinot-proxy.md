# Source: https://docs.startree.ai/corecapabilities/query_data/query_interfaces/pinot-proxy.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Pinot Proxy

> The Pinot Proxy routes requests to brokers while ensuring broker isolation

### **Proxy URL**

You can query the Startree Proxy using the following URL:

```
https://proxy.broker.XXXX.startree.cloud/
```

where broker.XXXX is your regular Broker URL.

The Pinot Proxy is used to isolate the broker from tables, by using broker tenants. When there are multiple tenants, the proxy takes care of routing queries to the correct broker, reducing the load on the customer end.

> A table can be mapped to one broker tenant. Multiple tables can be mapped to the same broker tenant.

> A broker can be mapped to multiple tenants.

<img src="https://mintcdn.com/startree/qZwmUU4Se8wDV-BE/corecapabilities/query_data/images/pinot_proxy_tenant.png?fit=max&auto=format&n=qZwmUU4Se8wDV-BE&q=85&s=a801f6797c7658ebcfb42e2c3f943d39" alt="Pinot Proxy" title="" className="mx-auto" style={{ width:"44%" }} width="1125" height="1182" data-path="corecapabilities/query_data/images/pinot_proxy_tenant.png" />

## Request Routing

To ensure isolation, a query will be routed to a broker only **if the broker can serve all the tables** in that query. This means that the broker must be mapped to all tenants for all tables of the query.

In the example diagram:

* A *Table 1 join Table 2* query can be routed to either **Broker 1** or **Broker 2**.
* A *Table 1 join Table 3* query can be routed only to **Broker 2**.
* A *Table 1 join Table 4* query **cannot be routed**. Such a query will fail.

By default, Pinot parses the query and determines the tables in the query. This consumes additional compute reqources, depending on the query to be parsed. The Pinot proxy is part of the broker service itself, so the overhead is added to the broker pod.

To avoid the overhead, pass the table names in the request headers. The header key is `FORWARD TABLE` and the value is the table name.

<Note>
  * For multiple tables, add multiple headers with the same `FORWARD TABLE` key and add each table name as a separate value.
  * If using databases, the table name should be \<database> + "." + \<table name>
  * The OFFLINE / REALTIME suffix is not required. Ensure they are mapped to the same tenant.
</Note>

### Example

```
curl -H 'FORWARD_TABLE: <table_name_1>' -H 'FORWARD_TABLE: <table_name_2>' -H
'Authorization: Bearer <bearer_token>' https://<broker_url>/query/sql -d
'{"sql":"SET useMultistageEngine=true;<sql_query>"}'
```

### Testing

To test if the header values are used to route the query rather than the actual SQL query, pass a different table name in the header than what is used in the query.

For the table/tenant/broker setup shown in the example diagram, the following query returns an error because it is redirected to Broker 1 or Broker 2 that cannot handle a request for Table 4.

```
curl -H 'FORWARD_TABLE: Table1' -H 'FORWARD_TABLE: Table2' -H 'Authorization:
Bearer <bearer_token>' https://<broker_url>/query/sql -d '{"sql":"SET
useMultistageEngine=true;select * from Table4 limit 10"}'
```

## Usage Considerations

* In the current version, a single header value is read. This works if a broker is mapped to not more than one tenant. Starting Startree 0.11.0 release, all header values will be read. This will enable a broker to be mapped to multiple tenants. Users can still pass all the table names in the query as part of the headers. This will make the client future-compatible and work in the current version as long as no broker is mapped to more than one tenant.
* Maintain consistency between the table names in the header and the tables used in the query. If they are not consistent, queries can fail because of incorrect routing.

Built with [Mintlify](https://mintlify.com).
