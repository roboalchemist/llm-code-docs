# Source: https://docs.pinot.apache.org/release-0.4.0/integrations/superset.md

# Source: https://docs.pinot.apache.org/release-0.9.0/integrations/superset.md

# Source: https://docs.pinot.apache.org/release-0.10.0/integrations/superset.md

# Source: https://docs.pinot.apache.org/release-0.11.0/integrations/superset.md

# Source: https://docs.pinot.apache.org/release-0.12.0/integrations/superset.md

# Source: https://docs.pinot.apache.org/release-0.12.1/integrations/superset.md

# Source: https://docs.pinot.apache.org/release-1.0.0/integrations/superset.md

# Source: https://docs.pinot.apache.org/release-1.1.0/integrations/superset.md

# Source: https://docs.pinot.apache.org/release-1.2.0/integrations/superset.md

# Source: https://docs.pinot.apache.org/release-1.3.0/integrations/superset.md

# Source: https://docs.pinot.apache.org/release-1.4.0/integrations/superset.md

# Source: https://docs.pinot.apache.org/integrations/superset.md

# Superset

## Start Superset with Docker Image

Start running [Superset Image](https://hub.docker.com/repository/docker/apachepinot/pinot-superset) with pre-built Superset Pinot connector.

{% tabs %}
{% tab title="Docker" %}
1\. Run below command to start a standalone Superset deployment

```
docker run \
  --network pinot-demo \
  --name=superset \
  -p 8088:8088 \
  -d apachepinot/pinot-superset:latest
```

2.1. (First time) Set up Admin account by running below command and follow instructions to set password.

```
docker exec -it superset superset fab create-admin \
               --username admin \
               --firstname Superset \
               --lastname Admin \
               --email admin@superset.com \
               --password admin
```

2.2. (First time) DB upgrade and Initialize Superset

```
docker exec -it superset superset db upgrade
docker exec -it superset superset init
```

3\. Import Pre-defined Pinot Datasources and Dashboard

```
docker exec \
    -t superset \
    bash -c 'superset import_datasources -p /etc/examples/pinot/pinot_example_datasource_quickstart.yaml && \
             superset import_dashboards -p /etc/examples/pinot/pinot_example_dashboard.json'
```

4\. Go to SuperSet UI: <http://localhost:8088/> to play around with dashboard.
{% endtab %}
{% endtabs %}

## Advanced Setup

### Adding Pinot Database

In order to add Pinot cluster as a database, a SQLAlchemy URI is required.

The format of URI is:

`pinot://<pinot-broker-host>:<pinot-broker-port><pinot-broker-path>?controller=<pinot-controller-host>:<pinot-controller-port>`

E.g.

> `pinot://pinot-broker:8099/query/sql?controller=http://pinot-controller:9000/`

Click `TEST CONNECTION` to check if the Pinot cluster is successfully connected.

### Adding Pinot Table

User can add an existing table into Superset:

![Add Table Definition](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LtH6nl58DdnZnelPdTc%2F-MGFyvyOXHyuXaJ_mkrN%2F-MGFzppclzuySrtCCaKK%2Fimage.png?alt=media\&token=1f0dd477-456e-4f56-8127-30fb977728ca)

![Table Definition](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LtH6nl58DdnZnelPdTc%2F-MGFyvyOXHyuXaJ_mkrN%2F-MGG-IwXjeprgMN4DHHv%2Fimage.png?alt=media\&token=a8e86c83-af31-4238-8ac2-287df6dc2bd5)

User can edit table/column definition by clicking the `edit` button left to the table name.

### Configuring time column

User can configure an existing column `mergedTimeMillis` as temporal and set `Datetime Format` accordingly.

![Configure time column](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LtH6nl58DdnZnelPdTc%2F-MGFyvyOXHyuXaJ_mkrN%2F-MGG0xLZRQOY2awTV9Os%2Fimage.png?alt=media\&token=63b82129-f57c-4e09-8234-c05a99e0c0ce)

### Adding a derived column

User can also add a new column by setting the expression.

![Add a simple derived column](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LtH6nl58DdnZnelPdTc%2F-MGFyvyOXHyuXaJ_mkrN%2F-MGG1Tj-Qv3uFunrZ-5U%2Fimage.png?alt=media\&token=7f601869-b9bc-4cb1-894b-b57b80ea0aab)

Another example:

![Add a derived column with Pinot UDFs](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LtH6nl58DdnZnelPdTc%2F-MGFyvyOXHyuXaJ_mkrN%2F-MGG1zRg_l60z3fC_36u%2Fimage.png?alt=media\&token=0b543ebe-fceb-4266-8dd0-59247dd01efb)
