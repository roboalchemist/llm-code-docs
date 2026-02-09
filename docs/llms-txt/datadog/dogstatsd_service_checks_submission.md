# Source: https://docs.datadoghq.com/developers/service_checks/dogstatsd_service_checks_submission.md

---
title: 'Service Checks Submission: DogStatsD'
description: Overview of the features of DogStatsD, including data types and tagging.
breadcrumbs: 'Docs > Developers > Service Check > Service Checks Submission: DogStatsD'
---

# Service Checks Submission: DogStatsD

While StatsD accepts only metrics, DogStatsD accepts all three of the major Datadog data types: metrics, events, and service checks. This section shows typical use cases for service checks with code examples.

## Function{% #function %}

After [installing DogStatsD](https://docs.datadoghq.com/developers/dogstatsd/), you can send service checks to Datadog with the following function:

```text
service_check(<SERVICE_CHECK_NAME>, <STATUS>, <TAGS>, <HOSTNAME>, <MESSAGE>)
```

Service check function parameters:

| Parameter              | Type                    | Required | Default Value | Description                                                                                                |
| ---------------------- | ----------------------- | -------- | ------------- | ---------------------------------------------------------------------------------------------------------- |
| `<SERVICE_CHECK_NAME>` | String                  | Yes      | -             | The name of the service check.                                                                             |
| `<STATUS>`             | Int                     | Yes      | -             | A constant describing the service status: `0` for OK, `1` for WARN, `2` for CRITICAL, and `3` for UNKNOWN. |
| `<TAGS>`               | List of key:value pairs | No       | -             | A list of tags to associate with the service check.                                                        |
| `<HOSTNAME>`           | String                  | No       | Current host  | The hostname to associate with the service check.                                                          |
| `<MESSAGE>`            | String                  | No       | -             | Additional information or a description of why the status occurred.                                        |

### Code examples{% #code-examples %}

Run the following code to submit a service check through DogStatsD to Datadog. Remember to `flush`/`close` the client when it is no longer needed.

{% tab title="Python" %}

```python
from datadog import initialize, statsd

options = {"statsd_host": "127.0.0.1", "statsd_port": 8125}

initialize(**options)

statsd.service_check(
    check_name="application.service_check",
    status="0",
    message="Application is OK",
)
```

{% /tab %}

{% tab title="Ruby" %}

```ruby
require 'datadog/statsd'

statsd = Datadog::Statsd.new('localhost', 8125)

statsd.service_check('application.service_check', 0, {'message' => 'Application is OK'})
```

{% /tab %}

{% tab title="Go" %}

```go
package main

import (
    "log"
    "time"

    "github.com/DataDog/datadog-go/statsd"
)

func main() {

    dogstatsdClient, err := statsd.New("127.0.0.1:8125")

    if err != nil {
        log.Fatal(err)
    }

    for {
        dogstatsdClient.SimpleServiceCheck("application.service_check", 0)
        time.Sleep(10 * time.Second)
    }
}
```

{% /tab %}

{% tab title="Java" %}

```java
import com.timgroup.statsd.ServiceCheck;
import com.timgroup.statsd.NonBlockingStatsDClientBuilder;
import com.timgroup.statsd.StatsDClient;

public class DogStatsdClient {

    public static void main(String[] args) throws Exception {

        StatsDClient Statsd = new NonBlockingStatsDClientBuilder()
            .prefix("statsd").
            .hostname("localhost")
            .port(8125)
            .build();

        ServiceCheck sc = ServiceCheck.builder()
                          .withName("Service.check.name")
                          .withStatus(ServiceCheck.Status.OK)
                          .build();

        Statsd.serviceCheck(sc);
    }
}
```

{% /tab %}

{% tab title=".NET" %}

```csharp
using StatsdClient;

public class DogStatsdClient
{
    public static void Main()
    {
        var dogstatsdConfig = new StatsdConfig
        {
            StatsdServerName = "127.0.0.1",
            StatsdPort = 8125,
        };

        using (var dogStatsdService = new DogStatsdService())
        {
            if (!dogStatsdService.Configure(dogstatsdConfig))
                throw new InvalidOperationException("Cannot initialize DogstatsD. Set optionalExceptionHandler argument in the `Configure` method for more information.");
            dogStatsdService.ServiceCheck("Service.check.name", 0, message: "Application is OK.", tags: new[] { "env:dev" });
        }
    }
}
```

{% /tab %}

{% tab title="PHP" %}

```php
<?php

require __DIR__ . '/vendor/autoload.php';

use DataDog\DogStatsd;

$statsd = new DogStatsd(
    array('host' => '127.0.0.1',
          'port' => 8125,
     )
  );

$statsd->service_check('Service.check.name', 0);
```

{% /tab %}

After a service check is reported, use it to trigger a [service check monitor](https://docs.datadoghq.com/monitors/types/service_check/).

## Further reading{% #further-reading %}

- [Introduction to DogStatsD](https://docs.datadoghq.com/developers/dogstatsd/)
- [Official and Community created API and DogStatsD client libraries](https://docs.datadoghq.com/developers/community/libraries/)
