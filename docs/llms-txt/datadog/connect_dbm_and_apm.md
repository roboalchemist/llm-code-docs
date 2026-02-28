# Source: https://docs.datadoghq.com/database_monitoring/connect_dbm_and_apm.md

---
title: Correlate Database Monitoring and Traces
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Database Monitoring > Correlate Database Monitoring and Traces
---

# Correlate Database Monitoring and Traces

This guide assumes that you have configured [Database Monitoring](https://docs.datadoghq.com/database_monitoring/#getting-started) and are using [APM](https://docs.datadoghq.com/tracing/). Connecting APM and DBM injects APM trace identifiers into DBM data collection, which allows for correlation of these two data sources. This enables product features showing database information in the APM product, and APM data in the DBM product.

## Before you begin{% #before-you-begin %}

{% dl %}

{% dt %}
Supported databases
{% /dt %}

{% dd %}
Postgres, MySQL, SQL Server, Oracle, MongoDB
{% /dd %}

{% dt %}
Supported Agent versions
{% /dt %}

{% dd %}
7.46+
{% /dd %}

{% dt %}
Data privacy
{% /dt %}

{% dd %}
Enabling SQL comment propagation results in potentially confidential data (service names) being stored in the databases which can then be accessed by other third parties that have been granted access to the database.
{% /dd %}

{% /dl %}

APM tracer integrations support a *Propagation Mode*, which controls the amount of information passed from applications to the database.

- `full` mode sends full trace information to the database, allowing you to investigate individual traces within DBM. This is the recommended solution for most integrations.
- `service` mode sends the service name, allowing you to understand which services are the contributors to database load.
- `disabled` mode disables propagation and does not send any information from applications.

| DD_DBM_PROPAGATION_MODE | Postgres | MySQL | SQL Server | Oracle | MongoDB |
| ----------------------- | -------- | ----- | ---------- | ------ | ------- |
| `full`                  | yes      | yes * | yes        | yes ** | yes     |
| `service`               | yes      | yes   | yes        | yes    | yes     |

\* Full propagation mode on Aurora MySQL requires version 3.

\** Full propagation mode on Oracle is only supported when using Java.

**Supported application tracers and drivers**

| Language                                                                                                                      | Library or Framework | Postgres | MySQL               | SQL Server          | Oracle | MongoDB |
| ----------------------------------------------------------------------------------------------------------------------------- | -------------------- | -------- | ------------------- | ------------------- | ------ | ------- |
| **Go:** [dd-trace-go](https://pkg.go.dev/gopkg.in/DataDog/dd-trace-go.v1) >= 1.44.0                                           |
| [database/sql](https://pkg.go.dev/database/sql)                                                                               | yes                  | yes      | `service` mode only | `service` mode only |
| [sqlx](https://pkg.go.dev/github.com/jmoiron/sqlx)                                                                            | yes                  | yes      | `service` mode only | `service` mode only |
| **Java** [dd-trace-java](https://github.com/DataDog/dd-trace-java) >= 1.11.0                                                  |
| [jdbc](https://docs.oracle.com/javase/8/docs/technotes/guides/jdbc/)                                                          | yes                  | yes      | yes **              | yes ***             |
| **Ruby:** [dd-trace-rb](https://github.com/dataDog/dd-trace-rb) >= 1.8.0                                                      |
| [pg](https://github.com/ged/ruby-pg)                                                                                          | yes                  |
| [mysql2](https://github.com/brianmario/mysql2)                                                                                | yes                  |
| **Python:** [dd-trace-py](https://github.com/DataDog/dd-trace-py) >= 1.9.0                                                    |
| [psycopg2](https://www.psycopg.org/docs/index.html)                                                                           | yes                  |
| [psycopg](https://www.psycopg.org/psycopg3/)                                                                                  | yes                  |
| [dd-trace-py](https://github.com/DataDog/dd-trace-py) >= 2.9.0                                                                |
| [asyncpg](https://pypi.org/project/asyncpg/)                                                                                  | yes                  |
| [aiomysql](https://pypi.org/project/aiomysql/)                                                                                | yes                  |
| [mysql-connector-python](https://pypi.org/project/mysql-connector-python/)                                                    | yes                  |
| [mysqlclient](https://pypi.org/project/mysqlclient/)                                                                          | yes                  |
| [pymysql](https://github.com/PyMySQL/PyMySQL)                                                                                 | yes                  |
| [pymongo](https://pymongo.readthedocs.io/en/stable/)                                                                          | yes *****            |
| **.NET** [dd-trace-dotnet](https://github.com/DataDog/dd-trace-dotnet) >= 2.35.0                                              |
| [Npgsql](https://www.nuget.org/packages/npgsql) *                                                                             | yes                  |
| [MySql.Data](https://www.nuget.org/packages/MySql.Data) *                                                                     | yes                  |
| [MySqlConnector](https://www.nuget.org/packages/MySqlConnector) *                                                             | yes                  |
| [System.Data.SqlClient](https://learn.microsoft.com/sql/connect/ado-net/microsoft-ado-net-sql-server) *                       | yes **               |
| [Microsoft.Data.SqlClient](https://learn.microsoft.com/sql/connect/ado-net/introduction-microsoft-data-sqlclient-namespace) * | yes **               |
| **PHP** [dd-trace-php](https://github.com/DataDog/dd-trace-php) >= 0.86.0                                                     |
| [pdo](https://www.php.net/manual/en/book.pdo.php)                                                                             | yes                  | yes      |
| [MySQLi](https://www.php.net/manual/en/book.mysqli.php)                                                                       | yes                  |
| **Node.js:** [dd-trace-js](https://github.com/DataDog/dd-trace-js) >= 3.17.0                                                  |
| [postgres](https://node-postgres.com/)                                                                                        | yes                  |
| [mysql](https://github.com/mysqljs/mysql)                                                                                     | yes                  |
| [mysql2](https://github.com/sidorares/node-mysql2)                                                                            | yes                  |
| [mongodb](https://github.com/mongodb/node-mongodb-native)                                                                     | yes ****             |

\* [CommandType.StoredProcedure](https://learn.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlcommand.commandtype?view=dotnet-plat-ext-7.0#remarks:~:text=[%e2%80%a6]%20should%20set) not supported

\** Full mode SQL Server for Java/.NET:

{% alert level="danger" %}
If your application uses `context_info` for instrumentation, the APM tracer overwrites it.
{% /alert %}

- The instrumentation executes a `SET context_info` command when the client issues a query, which makes an additional round-trip to the database.
- Prerequisites:
  - Agent version 7.55.0 or greater
  - Java tracer version 1.39.0 or greater
  - .NET tracer version 3.3 or greater

\*** Full mode Oracle for Java:

- The instrumentation overwrites `V$SESSION.ACTION`.
- Prerequisite: Java tracer 1.45 or greater

\**** Service/Full mode MongoDB for Node.js:

- Prerequisite:
  - Node.js tracer 5.80.0 or greater

\***** Service/Full mode MongoDB for Python:

- Prerequisite:
  - Python tracer 3.5.0 or greater

## Setup{% #setup %}

For the best user experience, ensure the following environment variables are set in your application:

```
DD_SERVICE=(application name)
DD_ENV=(application environment)
DD_VERSION=(application version)
```

Datadog recommends setting the obfuscation mode to `obfuscate_and_normalize` for Agent versions `7.63` and higher. Add the following parameter in the `apm_config` section of your APM Agent configuration file:

```
  sql_obfuscation_mode: "obfuscate_and_normalize"
```

{% alert level="warning" %}
Changing the obfuscation mode may alter the normalized SQL text. If you have monitors based on SQL text in APM traces, you may need to update them.
{% /alert %}

{% tab title="Go" %}
Update your app dependencies to include [dd-trace-go@v1.44.0](https://pkg.go.dev/gopkg.in/DataDog/dd-trace-go.v1) or greater. **Note**: This documentation uses v2 of the Go tracer, which Datadog recommends for all users. If you are using v1, see the [migration guide](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/go/migration) to upgrade to v2.

```shell
go get github.com/DataDog/dd-trace-go/v2 # 2.x
```

Update your code to import the `contrib/database/sql` package:

```go
import (
   "database/sql"
   "github.com/DataDog/dd-trace-go/v2/ddtrace/tracer"
   sqltrace "github.com/DataDog/dd-trace-go/contrib/database/sql/v2"
)
```

Enable the database monitoring propagation feature using one of the following methods:

- Env variable: `DD_DBM_PROPAGATION_MODE=full`

- Using code during the driver registration:

  ```go
  sqltrace.Register("postgres", &pq.Driver{}, sqltrace.WithDBMPropagation(tracer.DBMPropagationModeFull), sqltrace.WithService("my-db-service"))
  ```

- Using code on `sqltrace.Open`:

  ```go
  sqltrace.Register("postgres", &pq.Driver{}, sqltrace.WithService("my-db-service"))

  db, err := sqltrace.Open("postgres", "postgres://pqgotest:password@localhost/pqgotest?sslmode=disable", sqltrace.WithDBMPropagation(tracer.DBMPropagationModeFull))
  if err != nil {
      log.Fatal(err)
  }
  ```

Full example:

```go
import (
    "database/sql"
    "github.com/DataDog/dd-trace-go/v2/ddtrace/tracer"
   sqltrace "github.com/DataDog/dd-trace-go/contrib/database/sql/v2"
)

func main() {
    // The first step is to set the dbm propagation mode when registering the driver. Note that this can also
    // be done on sqltrace.Open for more granular control over the feature.
    sqltrace.Register("postgres", &pq.Driver{}, sqltrace.WithDBMPropagation(tracer.DBMPropagationModeFull))

    // Followed by a call to Open.
    db, err := sqltrace.Open("postgres", "postgres://pqgotest:password@localhost/pqgotest?sslmode=disable")
    if err != nil {
        log.Fatal(err)
    }

    // Then, we continue using the database/sql package as we normally would, with tracing.
    rows, err := db.Query("SELECT name FROM users WHERE age=?", 27)
    if err != nil {
        log.Fatal(err)
    }
    defer rows.Close()
}
```

{% /tab %}

{% tab title="Java" %}
Follow the [Java tracing](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/java/) instrumentation instructions and install the `1.11.0` version, or greater, of the Agent.

You must also enable the `jdbc-datasource` [instrumentation](https://docs.datadoghq.com/tracing/trace_collection/compatibility/java/#data-store-compatibility).

Enable the database monitoring propagation feature using **one** of the following methods:

- Set the system property `dd.dbm.propagation.mode=full`
- Set the environment variable `DD_DBM_PROPAGATION_MODE=full`

Full example:

```
# Start the Java Agent with the required system properties
java -javaagent:/path/to/dd-java-agent.jar -Ddd.dbm.propagation.mode=full -Ddd.integration.jdbc-datasource.enabled=true -Ddd.service=my-app -Ddd.env=staging -Ddd.version=1.0 -jar path/to/your/app.jar
```

Test the feature in your application:

```java
public class Application {
    public static void main(String[] args) {
        try {
            Connection connection = DriverManager
                    .getConnection("jdbc:postgresql://127.0.0.1/foobar?preferQueryMode=simple", "user", "password");
            Statement stmt = connection.createStatement();
            String sql = "SELECT * FROM foo";
            stmt.execute(sql);
            stmt.close();
            connection.close();
        } catch (SQLException exception) {
            //  exception logic
        }
    }
}
```

**Tracer versions 1.44 and above**: Enable the prepared statements tracing for Postgres using **one** of the following methods:

- Set the system property `dd.dbm.trace_prepared_statements=true`
- Set the environment variable `export DD_DBM_TRACE_PREPARED_STATEMENTS=true`

**Note**: The prepared statements instrumentation overwrites the `Application` property with the text `_DD_overwritten_by_tracer`, and causes an extra round trip to the database. This additional round trip normally has a negligible impact on the SQL statement execution time.

{% alert level="danger" %}
Enabling prepared statements tracing may cause increased connection pinning when using Amazon RDS Proxy, which reduces connection pooling efficiency. For more information, see [Connection pinning on RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-pinning.html).
{% /alert %}

**Tracer versions below 1.44**: Prepared statements are not supported in `full` mode for Postgres and MySQL, and all JDBC API calls that use prepared statements are automatically downgraded to `service` mode. Since most Java SQL libraries use prepared statements by default, this means that **most** Java applications are only able to use `service` mode.
{% /tab %}

{% tab title="Ruby" %}
In your Gemfile, install or update [dd-trace-rb](https://github.com/dataDog/dd-trace-rb) to version `1.8.0` or greater:

```rb
source 'https://rubygems.org'
gem 'datadog' # Use `'ddtrace', '>= 1.8.0'` if you're using v1.x

# Depends on your usage
gem 'mysql2'
gem 'pg'
```

Enable the database monitoring propagation feature using one of the following methods:

1. Env variable: `DD_DBM_PROPAGATION_MODE=full`

1. Option `comment_propagation` (default: `ENV['DD_DBM_PROPAGATION_MODE']`), for [mysql2](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/ruby/#mysql2) or [pg](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/ruby/#postgres):

   ```rb
    Datadog.configure do |c|
        c.tracing.instrument :mysql2, comment_propagation: 'full'
        c.tracing.instrument :pg, comment_propagation: 'full'
    end
   ```

Full example:

```rb
require 'mysql2'
require 'ddtrace'

Datadog.configure do |c|
    c.service = 'billing-api'
    c.env = 'production'
    c.version = '1.3-alpha'

    c.tracing.instrument :mysql2, comment_propagation: ENV['DD_DBM_PROPAGATION_MODE']
end

client = Mysql2::Client.new(:host => "localhost", :username => "root")
client.query("SELECT 1;")
```

{% /tab %}

{% tab title="Python" %}
Update your app dependencies to include [dd-trace-py>=1.9.0](https://ddtrace.readthedocs.io/en/stable/release_notes.html):

```
pip install "ddtrace>=1.9.0"
```

For Postgres, install [psycopg2](https://ddtrace.readthedocs.io/en/stable/integrations.html#module-ddtrace.contrib.psycopg):

```
pip install psycopg2
```

For MongoDB (requires dd-trace-py>=3.5.0), install pymongo:

```
pip install pymongo
```

Enable the database monitoring propagation feature by setting the following environment variable:

- `DD_DBM_PROPAGATION_MODE=full`

Postgres example:

```python
import psycopg2

POSTGRES_CONFIG = {
    "host": "127.0.0.1",
    "port": 5432,
    "user": "postgres_user",
    "password": "postgres_password",
    "dbname": "postgres_db_name",
}

# connect to postgres db
conn = psycopg2.connect(**POSTGRES_CONFIG)
cursor = conn.cursor()
# execute sql queries
cursor.execute("select 'blah'")
cursor.executemany("select %s", (("foo",), ("bar",)))
```

MongoDB example:

```python
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['test_database']
collection = db['test_collection']

# Insert a document
collection.insert_one({"name": "test", "value": 1})

# Query documents
results = collection.find({"name": "test"})
for doc in results:
    print(doc)
```

{% /tab %}

{% tab title=".NET" %}

{% alert level="danger" %}
This feature requires automatic instrumentation to be enabled for your .NET service.
{% /alert %}

Follow the [.NET Framework tracing instructions](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/dotnet-framework) or the [.NET Core tracing instructions](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/dotnet-core) to install the automatic instrumentation package and enable tracing for your service.

Ensure that you are using a supported client library. For example, `Npgsql`.

Enable the database monitoring propagation feature by setting the following environment variable:

- For Postgres and MySQL: `DD_DBM_PROPAGATION_MODE=full`
- For SQL Server: `DD_DBM_PROPAGATION_MODE=service` or `DD_DBM_PROPAGATION_MODE=full` with Java and .NET tracers
- For Oracle: `DD_DBM_PROPAGATION_MODE=service`

{% /tab %}

{% tab title="PHP" %}

{% alert level="danger" %}
This feature requires the tracer extension to be enabled for your PHP service.
{% /alert %}

Follow the [PHP tracing instructions](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/php?tab=containers) to install the automatic instrumentation package and enable tracing for your service.

Ensure that you are using a supported client library. For example, `PDO`.

Enable the database monitoring propagation feature by setting the following environment variable:

- `DD_DBM_PROPAGATION_MODE=full`

{% /tab %}

{% tab title="Node.js" %}
Install or update [dd-trace-js](https://github.com/DataDog/dd-trace-js) to a version greater than `3.17.0` (or `2.30.0` if using end-of-life Node.js version 12):

```
npm install dd-trace@^3.17.0
```

Update your code to import and initialize the tracer:

```javascript
// This line must come before importing any instrumented module.
const tracer = require('dd-trace').init();
```

Enable the database monitoring propagation feature using one of the following methods:

- Set the following env variable:

  ```
  DD_DBM_PROPAGATION_MODE=full
  ```

- Set the tracer to use the `dbmPropagationMode` option (default: `ENV['DD_DBM_PROPAGATION_MODE']`):

  ```javascript
  const tracer = require('dd-trace').init({ dbmPropagationMode: 'full' })
  ```

- Enable only at the integration level:

  ```javascript
  const tracer = require('dd-trace').init();
  tracer.use('pg', {
     dbmPropagationMode: 'full'
  })
  ```

Full example:

```javascript
const pg = require('pg')
const tracer = require('dd-trace').init({ dbmPropagationMode: 'full' })

const client = new pg.Client({
    user: 'postgres',
    password: 'postgres',
    database: 'postgres'
})

client.connect(err => {
    console.error(err);
    process.exit(1);
});

client.query('SELECT $1::text as message', ['Hello world!'], (err, result) => {
    // handle result
})
```

{% /tab %}

## Explore the APM Connection in DBM{% #explore-the-apm-connection-in-dbm %}

### Attribute active database connections to the calling APM services{% #attribute-active-database-connections-to-the-calling-apm-services %}

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/dbm_apm_active_connections_breakdown.8dc3c9b02346f88c0fcf75c6bc142c4f.png?auto=format"
   alt="View active connections to a database broken down by the APM Service they originate from." /%}

Break down active connections for a given host by the upstream APM services making the requests. You can attribute load on a database to individual services to understand which services are most active on the database. Pivot to the most active upstream service's service page to continue the investigation.

### Filter your database hosts by the APM services that call them{% #filter-your-database-hosts-by-the-apm-services-that-call-them %}

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/dbm_filter_by_calling_service.1abf3918d1d7f38343e666fa7b380f40.png?auto=format"
   alt="Filter your database hosts by the APM services that call them." /%}

Quickly filter the Database List to display only the database hosts that your specific APM services depend on. Easily identify if any of your downstream dependencies have blocking activity that may impact service performance.

### View the associated trace for a query sample{% #view-the-associated-trace-for-a-query-sample %}

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/dbm_query_sample_trace_preview.f11dbc07d1e77d39d3c14f8808343376.png?auto=format"
   alt="Preview the sampled APM trace that the query sample being inspected was generated from." /%}

When viewing a Query Sample in Database Monitoring, if the associated trace has been sampled by APM, you can view the DBM Sample in the context of the APM Trace. This allows you to combine DBM telemetry, including the explain plan and historical performance of the query, alongside the lineage of the span within your infrastructure to understand if a change on the database is responsible for poor application performance.

## Explore the DBM Connection in APM{% #explore-the-dbm-connection-in-apm %}

### Visualize the downstream database hosts of APM services{% #visualize-the-downstream-database-hosts-of-apm-services %}

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/dbm_apm_service_page_db_host_list.56f6553bd4dae3e2cd0c43ebf88bc4b9.png?auto=format"
   alt="Visualize the downstream database hosts that your APM Services depend on from the Service Page." /%}

On the APM page for a given service, view the direct downstream database dependencies of the service as identified by Database Monitoring. Quickly determine if any hosts have disproportionate load that may be caused by noisy neighbors. To view a service's page, click on the service in the [Software Catalog](https://app.datadoghq.com/services) to open a details panel, then click **View Service Page** in the panel.

### Identify potential optimizations using explain plans for database queries in traces{% #identify-potential-optimizations-using-explain-plans-for-database-queries-in-traces %}

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/explain_plans_in_traces_update.b873c027bcb75ad2542f30a4d74ff3fa.png?auto=format"
   alt="Identify inefficiencies using explain plans for database queries within traces." /%}

View historical performance of similar queries to those executed in your trace, including sampled wait events, average latency, and recently captured explain plans, to contextualize how a query is expected to perform. Determine if the behavior is abnormal and continue the investigation by pivoting to Database Monitoring for additional context about the underlying database hosts.

## Further Reading{% #further-reading %}

- [Seamlessly correlate DBM and APM telemetry to understand end-to-end query performance](https://www.datadoghq.com/blog/link-dbm-and-apm/)
