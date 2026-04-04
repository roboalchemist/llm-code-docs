# Source: https://github.com/kuzzleio/kuzzle-plugin-prometheus

Title: GitHub - kuzzleio/kuzzle-plugin-prometheus: Monitor your Kuzzle application with Prometheus

URL Source: https://github.com/kuzzleio/kuzzle-plugin-prometheus

Markdown Content:
[![Image 1](https://user-images.githubusercontent.com/7868838/58807296-115aa100-8618-11e9-910f-8e2e1f3a893d.png)](https://user-images.githubusercontent.com/7868838/58807296-115aa100-8618-11e9-910f-8e2e1f3a893d.png)

[![Image 2](https://camo.githubusercontent.com/d0ad3905a8f1eefe0feb09e32efed58c6a685cf4d65639434ae5f5ac171f4834/68747470733a2f2f64617669642d646d2e6f72672f6b757a7a6c65696f2f6b757a7a6c652d706c7567696e2d70726f6d6574686575732e737667)](https://david-dm.org/kuzzleio/kuzzle-plugin-prometheus)[![Image 3: undefined](https://camo.githubusercontent.com/a5461423e6839196ba0fce18801dd120c1ba1a6e85700a766f32673c3448a58d/68747470733a2f2f7472617669732d63692e636f6d2f6b757a7a6c65696f2f6b757a7a6c652d706c7567696e2d70726f6d6574686575732e7376673f6272616e63683d6d6173746572)](https://travis-ci.com/kuzzleio/kuzzle-plugin-prometheus)[![Image 4](https://camo.githubusercontent.com/fb169cb5a3231043705d1248be4a04bd052529caf7bfe4b74cb7fc552954b331/68747470733a2f2f636f6465636f762e696f2f67682f6b757a7a6c65696f2f6b757a7a6c652d706c7567696e2d70726f6d6574686575732f6272616e63682f6d61737465722f67726170682f62616467652e737667)](https://codecov.io/gh/kuzzleio/kuzzle-plugin-prometheus)[![Image 5: undefined](https://camo.githubusercontent.com/7816b699bdebc8b9c58c424a31ea12b4c1c78d152b4a7a5e96cd979bc026762d/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f6b757a7a6c65696f2f6b757a7a6c652d706c7567696e2d70726f6d6574686575732e7376673f7374796c653d666c6174)](https://github.com/kuzzleio/kuzzle-plugin-prometheus/blob/master/LICENSE)

*   [About](https://github.com/kuzzleio/kuzzle-plugin-prometheus#about)
    *   [Kuzzle Prometheus Plugin](https://github.com/kuzzleio/kuzzle-plugin-prometheus#kuzzle-prometheus-plugin)
    *   [Kuzzle](https://github.com/kuzzleio/kuzzle-plugin-prometheus#kuzzle)
    *   [Compatibility matrix](https://github.com/kuzzleio/kuzzle-plugin-prometheus#compatibility-matrix)

*   [Installation](https://github.com/kuzzleio/kuzzle-plugin-prometheus#installation)
*   [Configuration](https://github.com/kuzzleio/kuzzle-plugin-prometheus#configuration)
    *   [Plugin](https://github.com/kuzzleio/kuzzle-plugin-prometheus#plugin)
    *   [Prometheus](https://github.com/kuzzleio/kuzzle-plugin-prometheus#prometheus)
        *   [With only one Kuzzle node](https://github.com/kuzzleio/kuzzle-plugin-prometheus#with-only-one-kuzzle-node)
        *   [With an authentified user](https://github.com/kuzzleio/kuzzle-plugin-prometheus#with-an-authentified-user)
        *   [With multiple Kuzzle nodes and using Docker Compose](https://github.com/kuzzleio/kuzzle-plugin-prometheus#with-multiple-kuzzle-nodes-and-using-docker-compose)
        *   [Using Kubernetes annotations](https://github.com/kuzzleio/kuzzle-plugin-prometheus#using-kubernetes-annotations)

    *   [Dashboards](https://github.com/kuzzleio/kuzzle-plugin-prometheus#dashboards)
        *   [Features](https://github.com/kuzzleio/kuzzle-plugin-prometheus#features)
        *   [Screenshots](https://github.com/kuzzleio/kuzzle-plugin-prometheus#screenshots)

*   [Local development](https://github.com/kuzzleio/kuzzle-plugin-prometheus#local-development)
*   [Migrations](https://github.com/kuzzleio/kuzzle-plugin-prometheus#migrations)
    *   [From version 3.x to 4.x](https://github.com/kuzzleio/kuzzle-plugin-prometheus#from-version-3x-to-4x)
        *   [Migration steps](https://github.com/kuzzleio/kuzzle-plugin-prometheus#migration-steps)

About
-----

[](https://github.com/kuzzleio/kuzzle-plugin-prometheus#about)
This is the official Prometheus monitoring plugin for the free and open-source backend Kuzzle. It provides you features such as:

*   [Kuzzle cluster mode](https://github.com/kuzzleio/kuzzle-plugin-cluster) compatibility.
*   Event based monitoring using [Kuzzle Events](https://docs.kuzzle.io/core/1/plugins/guides/events/intro/).
*   System metrics (CPU, RAM, I/O...).

Kuzzle
------

[](https://github.com/kuzzleio/kuzzle-plugin-prometheus#kuzzle)
Kuzzle is an open-source backend that includes a scalable server, a multiprotocol API, an administration console and a set of plugins that provide advanced functionalities like real-time pub/sub, blazing fast search and geofencing.

*   ![Image 6: :octocat:](https://github.githubassets.com/images/icons/emoji/octocat.png)**[Github](https://github.com/kuzzleio/kuzzle)**
*   🌍 **[Website](https://kuzzle.io/)**
*   📚 **[Documentation](https://docs.kuzzle.io/)**
*   📧 **[Gitter](https://gitter.im/kuzzleio/kuzzle)**

Compatibility matrix
--------------------

[](https://github.com/kuzzleio/kuzzle-plugin-prometheus#compatibility-matrix)
| Kuzzle Version | Plugin Version |
| --- | --- |
| 1.10.x | 1.x.x |
| 2.x.x | 2.x.x |
| 3.x.x | >= 2.11.x |
| 4.x.x | >= 2.16.9 |

Installation
------------

[](https://github.com/kuzzleio/kuzzle-plugin-prometheus#installation)
To install this plugin on your Kuzzle stack (for each of your Kuzzle nodes), you will first need a Kuzzle Application like so. (see [Getting Started](https://github.com/kuzzleio/kuzzle-plugin-prometheus/blob/master/core/2/guides/getting-started))

import { Backend } from 'kuzzle';

const app = new Backend('kuzzle');

app.start()
  .then(() => {
    app.log.info('Application started');
  })
  .catch(console.error);

Once you have it, you will need to:

*   Import the Prometheus plugin,
*   Create a new instance of the plugin
*   And then use it in your application.

You will end up with something like this:

import { Backend } from 'kuzzle';
import { PrometheusPlugin } from 'kuzzle-plugin-prometheus'; // Import the prometheus plugin

const app = new Backend('kuzzle');

const prometheusPlugin = new PrometheusPlugin(); // Create a new instance of the prometheus plugin

app.plugin.use(prometheusPlugin); // Add the plugin to your application

app.start()
  .then(() => {
    app.log.info('Application started');
  })
  .catch(console.error);

Configuration
-------------

[](https://github.com/kuzzleio/kuzzle-plugin-prometheus#configuration)
You can find sample configuration files for this plugin and the Prometheus scraping job in the `demo` folder.

Plugin
------

[](https://github.com/kuzzleio/kuzzle-plugin-prometheus#plugin)
This plugin is configurable using the `kuzzlerc` Kuzzle configuration file.

 {
 "plugins": {
    "prometheus": {
      "default": {
        "enabled": true,
        "prefix": "",
        "eventLoopMonitoringPrecision": 10,
        "gcDurationBuckets": [0.001, 0.01, 0.1, 1, 2, 5]
      },
      "core": {
        "monitorRequestDuration": true,
        "prefix": "kuzzle_"
      },
      "labels": {
        "project": "mySuperProject",
        "environment": "development"
      }
    }
  }
}

*   `default`: Default Node.js metrics retrieved by [the Prom Client library](https://github.com/siimon/prom-client/tree/master/lib/metrics)
    *   `enabled`: Enable/Disable the default Node.js metrics (default: `true`)
    *   `prefix`: String to use to prefix metrics name (default: an empty string to avoid conflicts when using official Grafana dashboards)
    *   `eventLoopMonitoringPrecision`: Node.js Event Loop sampling rate in milliseconds. Must be greater than zero (default: `10`)
    *   `gcDurationBuckets`: Custom Prometheus buckets for Node.js GC duration histogram in seconds (default: `[0.001, 0.01, 0.1, 1, 2, 5]`)

*   `core`: Kuzzle Core metrics directly extract from the `server:metrics` API action or from plugin inner logic. 
    *   `monitorRequestDuration`: Enable/Disable request duration sampling (default: `true`)
    *   `prefix`: String to use to prefix metrics name (default: `kuzzle_`)

*   `labels`: Additional labels to apply on all the different metrics (default: `{}`)

Prometheus
----------

[](https://github.com/kuzzleio/kuzzle-plugin-prometheus#prometheus)
### With only one Kuzzle node

[](https://github.com/kuzzleio/kuzzle-plugin-prometheus#with-only-one-kuzzle-node)

global:
  scrape_interval:     10s # Set the scrape interval to every 10 seconds. Default is every 1 minute.
  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.

scrape_configs:
  - job_name: 'kuzzle'
    metrics_path: /_metrics
    params:
      format: ['prometheus']
    static_configs:
      - targets: ['kuzzle:7512'] # the address of an application that exposes metrics for prometheus

### With an authentified user

[](https://github.com/kuzzleio/kuzzle-plugin-prometheus#with-an-authentified-user)
If you use an other user than `anonymous` to expose the `server:metrics` API action, you will need to create a Kuzzle API Key (see [API Keys](https://docs.kuzzle.io/core/2/guides/advanced/api-keys/)) and use it to authentify the Prometheus scaper:

global:
  scrape_interval:     10s # Set the scrape interval to every 10 seconds. Default is every 1 minute.
  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.

scrape_configs:
  - job_name: 'kuzzle'
    metrics_path: /_metrics
    params:
      format: ['prometheus']
    authorization:
      type: 'Bearer'
      credentials: 'my-api-key'
    static_configs:
      - targets: ['kuzzle:7512'] # the address of an application that exposes metrics for prometheus

### With multiple Kuzzle nodes and using Docker Compose

[](https://github.com/kuzzleio/kuzzle-plugin-prometheus#with-multiple-kuzzle-nodes-and-using-docker-compose)
If you use Docker Compose you'll need to provide the IP/Docker DNS name of each Kuzzle node as `targets`:

global:
  scrape_interval:     10s # Set the scrape interval to every 10 seconds. Default is every 1 minute.
  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.

scrape_configs:
  - job_name: 'kuzzle'
    metrics_path: /_metrics
    params:
      format: ['prometheus']
    static_configs:
      - targets: 
        - 'kuzzle-plugin-prometheus-kuzzle-1:7512' 
        - 'kuzzle-plugin-prometheus-kuzzle-2:7512'
        - 'kuzzle-plugin-prometheus-kuzzle-3:7512'

### Using Kubernetes annotations

[](https://github.com/kuzzleio/kuzzle-plugin-prometheus#using-kubernetes-annotations)
If your Prometheus inside a Kubernetes cluster, you must use the helper HTTP route `/_/metrics` since Prometheus `params` configuration is not supported. Your Pods annotations should look like this:

metadata:
  annotations:
    prometheus.io/scrape: "true"
    prometheus.io/path: /_/metrics
    prometheus.io/port: "7512"
spec:
...

Dashboards
----------

[](https://github.com/kuzzleio/kuzzle-plugin-prometheus#dashboards)
### Features

[](https://github.com/kuzzleio/kuzzle-plugin-prometheus#features)
You could find two dashboards in the `config/grafana/dashboards` folder:

*   `kuzzle.json`: a dashboard with all the metrics exposed by the `server:metrics` API action with a `nodeId` filter and including:

    *   Active connections
    *   Active Realtime subscriptions
    *   Concurrent requests
    *   Pending requests
    *   Request per second
    *   Request duration
    *   Internal Errors

*   `nodejs.json`: Node.js metrics dashboard with a `nodeId` filter and including:

    *   Process CPU Usage
    *   Process Memory Usage
    *   Process Restarts
    *   Event Loop Latency
    *   Heap Usage

You can import them both using the Grafana API, Web UI or the provisionning system (see the `docker-compose.yml` file).

### Screenshots

[](https://github.com/kuzzleio/kuzzle-plugin-prometheus#screenshots)
**Kuzzle dashboard**[![Image 7: image](https://user-images.githubusercontent.com/7868838/150335493-413808e8-d65a-4de9-a01f-34634c751e45.png)](https://user-images.githubusercontent.com/7868838/150335493-413808e8-d65a-4de9-a01f-34634c751e45.png)

**Node.js dashboard**[![Image 8: image](https://user-images.githubusercontent.com/7868838/150334423-5763ac48-f6ea-444f-ab78-2f776a9925a6.png)](https://user-images.githubusercontent.com/7868838/150334423-5763ac48-f6ea-444f-ab78-2f776a9925a6.png)

Local development
-----------------

[](https://github.com/kuzzleio/kuzzle-plugin-prometheus#local-development)
You can run a local development stack using Docker Compose

```
$ docker-compose up
```

This will start a demonstration stack composed with:

*   A Kuzzle server proxified by a Traefik router
*   A Prometheus container configured to scrap metrics.
*   A Grafana container.

Once started, go to `http://localhost:3000` and log in with the default Grafana credentials:

*   username: `admin`
*   password: `admin`

Make several requests using Kuzzle's HTTP API or SDKs, or by using the Admin Console.

> NOTE: You can also increase the number of Kuzzle nodes to test a cluster configuration. Use the Docker Compose `--scale` option to increase the number of replicas:
> 
> 
> 
> ```
> docker-compose up -d --scale kuzzle=<number-of-replicas>
> ```
> 
> 
> Notice that you need to update the `config/prometheus.yml` file to reflect the new number of nodes and restart the prometheus container using `docker restart <prometheus-container-id>`

Migrations
----------

[](https://github.com/kuzzleio/kuzzle-plugin-prometheus#migrations)
From version 3.x to 4.x
-----------------------

[](https://github.com/kuzzleio/kuzzle-plugin-prometheus#from-version-3x-to-4x)
This new version 4.0.0 introduce numerous changes in the way metrics are collected and reported:

*   The plugin now uses the `server:metrics` API action to retrieve metrics from Kuzzle Core. Calling the `server:metrics` API action with the `format` parameter set to `prometheus` will return metrics in the Prometheus format.
*   The configuration of the plugin is now more flexible (see [Configuration](https://github.com/kuzzleio/kuzzle-plugin-prometheus#configuration) section for more details): 
    *   More control on the default Node.js metrics (set the Event Loop sample precision to custom value or adapt the Garbage Collector Prometheus bucket rates to fit your usecase).
    *   You can set different prefixes for Kuzzle Core metrics and Node.js metrics.
    *   The `nodeIP`, `nodeMAC` and `nodeHost` labels have beem removed in favor of the `nodeId` label.
    *   You can now disable the request recording job.

*   Most of the metric names have been changed to be more consistent with Kuzzle Core metrics.

### Migration steps

[](https://github.com/kuzzleio/kuzzle-plugin-prometheus#migration-steps)

 Allow the user used by Prometheus to access `server:metrics` API action 
Add the following rule to your user role to allow the user `anonymous` to access the `server:metrics` API action:

{
  "controllers": {
    // Your others controllers rules
    "server": {
      "actions": {
        "metrics": true,
        // ...
      }
    }
  }
}
  

 Update the plugin configuration 
Here is the new default configuration file:

 {
 "plugins": {
    "prometheus": {
      "default": {
        "enabled": true,
        "prefix": "",
        "eventLoopMonitoringPrecision": 10,
        "gcDurationBuckets": [0.001, 0.01, 0.1, 1, 2, 5]
      },
      "core": {
        "monitorRequestDuration": true,
        "prefix": "kuzzle_"
      }
    }
  }
}
  

 Update your dashboards 
If you have previously imported the example Grafana dashboard, you will have to update it to use the new metrics names or use the new ones located in `config/grafana/dashboards`.
