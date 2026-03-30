# Source: https://docs.datadoghq.com/developers/guide/dogshell.md

---
title: Dogshell
description: Use Datadog's API from Terminal or Shell
breadcrumbs: Docs > Developers > Developer Guides > Dogshell
---

# Dogshell

You can use the Datadog API on the command line using a wrapper called Dogshell.

## Install Dogshell{% #install-dogshell %}

Dogshell comes with the officially supported [`datadogpy` Python library](https://github.com/DataDog/datadogpy), which is often used to send data to Datadog with [`DogStatsD`](https://docs.datadoghq.com/metrics/custom_metrics/dogstatsd_metrics_submission/). To install the library with PIP, run the following command:

```shell
pip install datadog
```

Depending on your environment, you might have to add the library to your PATH. See the [`datadogpy` GitHub repo](https://github.com/DataDog/datadogpy#installation) for alternative installation instructions.

## Configure Dogshell{% #configure-dogshell %}

Dogshell uses a configuration file called `.dogrc` to store your API key, application key, and Datadog site.

To configure Dogshell:

1. Create a `.dogrc` file in your home directory:

   ```shell
   touch ~/.dogrc
```



1. Add the following content to the file, replacing `MY_API_KEY` and `MY_APP_KEY` with your API key and application key respectively:

   ```
   [Connection]
   apikey = MY_API_KEY
   appkey = MY_APP_KEY
   api_host =
   ```
Important alert (level: info): You can create multiple configuration files if you need to run commands against different environments. Use the `--config` flag to specify the path to an alternative configuration file.
1. Test the `dogshell` command by posting a test metric:

   ```shell
   dog metric post test_metric 1
```

## Dogshell commands{% #dogshell-commands %}

Use the `-h` flag for a full list of the available Dogshell commands:

```shell
dog -h
```

You can append the `-h` option to the following commands to get more information on specific Dogshell usage:

- `dog metric`
- `dog event`
- `dog service_check`
- `dog monitor`
- `dog downtime`
- `dog timeboard`
- `dog screenboard`
- `dog dashboard`
- `dog host`
- `dog tag`
- `dog search`
- `dog comment`

For additional information, see the [Dogshell code](https://github.com/DataDog/datadogpy/tree/master/datadog/dogshell).

### Dogshell example{% #dogshell-example %}

The following syntax posts a metric to your Datadog account:

```shell
dog metric post MY_METRIC_NAME METRIC_VALUE --tags "TAG_KEY_1:TAG_VALUE_1,TAG_KEY_2:TAG_VALUE_2"
```

For example, the following command sends a metric named `test_dogshell_metric` to your account with a value of `1.0` and the tags `test:one` and `example:one`:

```shell
dog metric post test_dogshell_metric 1.0 --tags "test:one,example:one"
```

After you run the command, search for `test_dogshell_metric` using the [Metrics Explorer](https://app.datadoghq.com/metric/explorer).

{% image
   source="https://datadog-docs.imgix.net/images/developers/guide/dogshell_test1.2fa6be23fcb280b6e39d5f0f8eb9c89e.png?auto=format"
   alt="Observing test_dogshell_metric from the Metrics explorer" /%}
