# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-upstream-dns-counters.md

Represents the count of queries, responses, failures handled by upstream DNS server. 

Requires `OPENTHREAD_CONFIG_DNS_UPSTREAM_QUERY_ENABLE`. 

## Public Attributes

### mQueries

```
uint32_t otUpstreamDnsCounters::mQueries
```

**Description:** The number of queries forwarded.

### mResponses

```
uint32_t otUpstreamDnsCounters::mResponses
```

**Description:** The number of responses forwarded.

### mFailures

```
uint32_t otUpstreamDnsCounters::mFailures
```

**Description:** The number of upstream DNS failures.