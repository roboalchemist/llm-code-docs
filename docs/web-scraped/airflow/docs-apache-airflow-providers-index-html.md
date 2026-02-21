# Source: https://airflow.apache.org/docs/apache-airflow-providers/index.html

Title: Providers — apache-airflow-providers Documentation

URL Source: https://airflow.apache.org/docs/apache-airflow-providers/index.html

Markdown Content:
Apache Airflow 2 is built in modular way. The “Core” of Apache Airflow provides core scheduler functionality which allow you to write some basic tasks, but the capabilities of Apache Airflow can be extended by installing additional packages, called `providers`.

Providers can contain operators, hooks, sensor, and transfer operators to communicate with a multitude of external systems, but they can also extend Airflow core with new capabilities.

You can install those providers separately in order to interface with a given service. The providers for `Apache Airflow` are designed in the way that you can write your own providers easily. The `Apache Airflow Community` develops and maintain more than 80 providers, but you are free to develop your own providers - the providers you build have exactly the same capability as the providers written by the community, so you can release and share those providers with others.

If you want to learn how to build your own custom provider, you can find all the information about it at [How to create your own provider](https://airflow.apache.org/docs/apache-airflow-providers/howto/create-custom-providers.html).

Extending Airflow core functionality[¶](https://airflow.apache.org/docs/apache-airflow-providers/index.html#extending-airflow-core-functionality "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Providers give you the capability of extending core Airflow with extra capabilities. The Core airflow provides basic and solid functionality of scheduling, the providers extend its capabilities. Here we describe all the custom capabilities.

Airflow automatically discovers which providers add those additional capabilities and, once you install provider package and re-start Airflow, those become automatically available to Airflow Users.

The summary of all the core functionalities that can be extended are available in [Core Extensions](https://airflow.apache.org/docs/apache-airflow-providers/core-extensions/index.html).

Configuration[¶](https://airflow.apache.org/docs/apache-airflow-providers/index.html#configuration "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------

Providers can have their own configuration options which allow you to configure how they work:

You can see all community-managed providers with their own configuration in [Configurations](https://airflow.apache.org/docs/apache-airflow-providers/core-extensions/configurations.html)

Command Line Interface[¶](https://airflow.apache.org/docs/apache-airflow-providers/index.html#command-line-interface "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

Note

The Airflow Core version must be `3.2.0` or newer to be able to use CLI commands provided by providers.

Providers can add their own custom CLI commands to Airflow CLI. Those commands will be available once you install the provider package.

You can see all community-managed providers with their own CLI commands in [Command Line Interface](https://airflow.apache.org/docs/apache-airflow-providers/core-extensions/cli-commands.html).

Custom connections[¶](https://airflow.apache.org/docs/apache-airflow-providers/index.html#custom-connections "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------

The providers can add custom connection types, extending connection form and handling custom form field behaviour for the connections defined by the provider.

You can see all the custom connections available via community-managed providers in [Connections](https://airflow.apache.org/docs/apache-airflow-providers/core-extensions/connections.html).

Logging[¶](https://airflow.apache.org/docs/apache-airflow-providers/index.html#logging "Link to this heading")
--------------------------------------------------------------------------------------------------------------

The providers can add additional task logging capabilities. By default `Apache Airflow` saves logs for tasks locally and make them available to Airflow UI via internal http server. However, providers can add extra logging capabilities, where Airflow Logs can be written to a remote service and retrieved from those services.

You can see all task loggers available via community-managed providers in [Writing logs](https://airflow.apache.org/docs/apache-airflow-providers/core-extensions/logging.html).

Secret backends[¶](https://airflow.apache.org/docs/apache-airflow-providers/index.html#secret-backends "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------

Airflow has the capability of reading connections, variables and configuration from Secret Backends rather than from its own Database.

You can see all the secret backends available via community-managed providers in [Secret backends](https://airflow.apache.org/docs/apache-airflow-providers/core-extensions/secrets-backends.html).

Notifications[¶](https://airflow.apache.org/docs/apache-airflow-providers/index.html#notifications "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------

The providers can add custom notifications, that allow you to configure the way how you would like to receive notifications about the status of your tasks/dags.

You can see all the notifications available via community-managed providers in [Notifications](https://airflow.apache.org/docs/apache-airflow-providers/core-extensions/notifications.html).

Installing and upgrading providers[¶](https://airflow.apache.org/docs/apache-airflow-providers/index.html#installing-and-upgrading-providers "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Separate providers give the possibilities that were not available in 1.10:

1.   You can upgrade to latest version of particular providers without the need of Apache Airflow core upgrade.

2.   You can downgrade to previous version of particular provider in case the new version introduces some problems, without impacting the main Apache Airflow core package.

3.   You can release and upgrade/downgrade providers incrementally, independent from each other. This means that you can incrementally validate each of the provider package update in your environment, following the usual tests you have in your environment.

Types of providers[¶](https://airflow.apache.org/docs/apache-airflow-providers/index.html#types-of-providers "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------

Providers have the same capacity - no matter if they are provided by the community or if they are third-party providers. This chapter explains how community managed providers are versioned and released and how you can create your own providers.

Community maintained providers[¶](https://airflow.apache.org/docs/apache-airflow-providers/index.html#community-maintained-providers "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------

From the point of view of the community, Airflow is delivered in multiple, separate packages. The core of Airflow scheduling system is delivered as `apache-airflow` package and there are more than 80 providers which can be installed separately as so called `Airflow providers`. Those packages are available as `apache-airflow-providers` packages - for example there is an `apache-airflow-providers-amazon` or `apache-airflow-providers-google` package).

Community maintained providers are released and versioned separately from the Airflow releases. We are following the [Semver](https://semver.org/) versioning scheme for the packages. Some versions of the providers might depend on particular versions of Airflow, but the general approach we have is that unless there is a good reason, new version of providers should work with recent versions of Airflow 2.x. Details will vary per-provider and if there is a limitation for particular version of particular provider, constraining the Airflow version used, it will be included as limitation of dependencies in the provider package.

Each community provider has corresponding extra which can be used when installing Airflow to install the provider together with `Apache Airflow` - for example you can install Airflow with those extras: `apache-airflow[google,amazon]` (with correct constraints -see [Installation of Airflow®](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html "(in apache-airflow v3.2.0)")) and you will install the appropriate versions of the `apache-airflow-providers-amazon` and `apache-airflow-providers-google` packages together with `Apache Airflow`.

Some of the community providers have cross-provider dependencies as well. Those are not required dependencies, they might simply enable certain features (for example transfer operators often create dependency between different providers. Again, the general approach here is that the providers are backwards compatible, including cross-dependencies. Any kind of breaking changes and requirements on particular versions of other providers are automatically documented in the release notes of every provider.

Note

For Airflow 1.10 We also provided `apache-airflow-backport-providers` packages that could be installed with those versions Those were the same providers as for 2.0 but automatically back-ported to work for Airflow 1.10. The last release of backport providers was done on March 17, 2021 and the backport providers will no longer be released, since Airflow 1.10 has reached End-Of-Life as of June 17, 2021.

If you want to contribute to `Apache Airflow`, you can see how to build and extend community managed providers in `https://github.com/apache/airflow/blob/main/providers/MANAGING_PROVIDERS_LIFECYCLE.rst`.
