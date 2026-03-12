# Source: https://docs.pinot.apache.org/release-0.11.0/developers/advanced/v2-multi-stage-query-engine.md

# Source: https://docs.pinot.apache.org/release-0.12.0/developers/advanced/v2-multi-stage-query-engine.md

# Source: https://docs.pinot.apache.org/release-0.12.1/developers/advanced/v2-multi-stage-query-engine.md

# Source: https://docs.pinot.apache.org/release-1.0.0/for-developers/advanced/v2-multi-stage-query-engine.md

# Source: https://docs.pinot.apache.org/release-1.1.0/for-developers/advanced/v2-multi-stage-query-engine.md

# Source: https://docs.pinot.apache.org/release-1.2.0/for-developers/advanced/v2-multi-stage-query-engine.md

# Source: https://docs.pinot.apache.org/release-1.3.0/for-developers/advanced/v2-multi-stage-query-engine.md

# Source: https://docs.pinot.apache.org/release-1.4.0/for-developers/advanced/v2-multi-stage-query-engine.md

# Source: https://docs.pinot.apache.org/developers/advanced/v2-multi-stage-query-engine.md

# Use the multi-stage query engine (v2)

To query using distributed joins, window functions, and other multi-stage operators in real time, you must enable the multi-stage query engine (v2). To enable v2, do any of the following:

* Enable the multi-stage query engine [in the Query Console](#enable-the-multi-stage-query-engine-in-the-query-console)
* Programmatically access the multi-stage query engine:
  * Query [using REST APIs](#use-rest-apis)
  * Query outside of the APIs [using the query option](#use-the-query-option)

To learn more about what the multi-stage query engine is, see [Multi-stage query engine (v2)](https://docs.pinot.apache.org/reference/multi-stage-engine).

## Enable the multi-stage query engine in the Query Console

* To enable the multi-stage query engine, in the Pinot Query Console, select the **Use Multi-Stage Engine** check box.

<figure><img src="https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2FS9xgXsMqp4PWEJ7fgdwd%2FScreenshot%202023-09-14%20at%209.59.22%20AM.png?alt=media&#x26;token=f09688df-9bd8-4aa8-9f00-dbb55f2d9eff" alt=""><figcaption><p>Pinot Query Console with Use Multi Stage Engine enabled</p></figcaption></figure>

## Programmatically access the multi-stage query engine

To query the Pinot multi-stage query engine, use REST APIs or the query option:

### Use REST APIs

The Controller admin API and the Broker query API allow optional JSON payload for configuration. For example:

* [For Controller Admin API](https://docs.pinot.apache.org/users/api/pinot-rest-admin-interface)

```bash
curl -X POST http://localhost:9000/sql -d 
'
{
  "sql": "select * from baseballStats limit 10",
  "trace": false,
  "queryOptions": "useMultistageEngine=true"
}
'
```

* [For Broker Query API](https://docs.pinot.apache.org/users/api/querying-pinot-using-standard-sql)

```bash
curl -X POST http://localhost:8000/query/sql -d '
{
  "sql": "select * from baseballStats limit 10",
  "trace": false,
  "queryOptions": "useMultistageEngine=true"
}
'
```

### Use the query option

To enable the multi-stage engine via a query outside of the API, add the `useMultistageEngine=true` option to the top of your query.

For example:

<pre class="language-sql"><code class="lang-sql"><strong>SET useMultistageEngine=true; -- indicator to enable the multi-stage engine.
</strong>SELECT * from baseballStats limit 10
</code></pre>
