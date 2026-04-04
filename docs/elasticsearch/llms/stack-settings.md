# Source: https://www.elastic.co/docs/deploy-manage/stack-settings

﻿---
title: Elastic Stack settings
description: Elastic Stack settings allow you to customize Elasticsearch, Kibana, and other Elastic Stack products to suit your needs. The available Elastic Stack...
url: https://www.elastic.co/docs/deploy-manage/stack-settings
products:
  - Elastic Stack
  - Elasticsearch
  - Kibana
applies_to:
  - Elastic Cloud Hosted: Generally available
  - Elastic Cloud on Kubernetes: Generally available
  - Elastic Cloud Enterprise: Generally available
  - Self-managed Elastic deployments: Generally available
---

# Elastic Stack settings
Elastic Stack settings allow you to customize Elasticsearch, Kibana, and other Elastic Stack products to suit your needs.
<admonition title="Serverless manages these settings for you">
  In Elastic Cloud Serverless, cluster-level settings and node-level settings are not required by end users, and are fully managed by Elastic.Certain [project settings](https://www.elastic.co/docs/deploy-manage/deploy/elastic-cloud/project-settings) allow you to customize your project’s performance and general data retention, and enable or disable project features.
</admonition>


## Available settings

The available Elastic Stack settings differ depending on your deployment type.

### Elasticsearch settings

Elasticsearch settings can be found in the [Elasticsearch configuration reference](https://www.elastic.co/docs/reference/elasticsearch/configuration-reference).

| Deployment type                              | Applicable settings                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Self managed                                 | All Elasticsearch settings can be applied to a self-managed cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Elastic Cloud EnterpriseElastic Cloud Hosted | Settings supported on Elastic Cloud Enterprise and Elastic Cloud Hosted are indicated by an Elastic Cloud icon (![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud")). However, some unmarked settings might also be supported.Elastic Cloud Hosted and Elastic Cloud Enterprise block the configuration of certain settings that could break your cluster if misconfigured. If a setting is not supported, you will get an error message when you try to save. We suggest changing one setting with each save, so you know which one is not supported. |
| Elastic Cloud on Kubernetes                  | Most Elasticsearch settings can be applied to an ECK-managed Elasticsearch cluster.Some settings are managed by ECK.  It is not recommended to change these managed settings. For a complete list, refer to [Settings managed by ECK](https://www.elastic.co/docs/deploy-manage/deploy/cloud-on-k8s/settings-managed-by-eck).                                                                                                                                                                                                                                                                              |


### Kibana settings

Kibana settings can be found in the [Kibana configuration reference](https://www.elastic.co/docs/reference/kibana/configuration-reference).

| Deployment type                              | Applicable settings                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Self managedElastic Cloud on Kubernetes      | All Kibana settings can be applied to a self-managed or ECK instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Elastic Cloud EnterpriseElastic Cloud Hosted | Settings supported on Elastic Cloud Enterprise and Elastic Cloud Hosted are indicated by an Elastic Cloud icon (![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud")). However, some unmarked settings might also be supported.Elastic Cloud Hosted and Elastic Cloud Enterprise block the configuration of certain settings that could break your cluster if misconfigured. If a setting is not supported, you will get an error message when you try to save. We suggest changing one setting with each save, so you know which one is not supported. |
| Elastic Cloud on Kubernetes                  | Most Elasticsearch settings can be applied to an ECK-managed Elasticsearch cluster.Some settings are managed by ECK.  It is not recommended to change these managed settings. For a complete list, refer to [Settings managed by ECK](https://www.elastic.co/docs/deploy-manage/deploy/cloud-on-k8s/settings-managed-by-eck).                                                                                                                                                                                                                                                                              |


### Other

For APM and Enterprise Search, refer to the product's documentation:
- [APM](https://www.elastic.co/docs/reference/apm/observability/apm-settings)
- [Enterprise Search](https://www.elastic.co/guide/en/enterprise-search/8.18/configuration.html)


## Configure Elastic Stack settings

The way that you configure your Elastic Stack settings is determined by your deployment type.
<warning>
  - [Dynamic Elasticsearch cluster settings](#dynamic-cluster-setting) can also be updated using Elasticsearch's [update cluster settings API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cluster-put-settings). However, Elastic Cloud Hosted and Elastic Cloud Enterprise don’t reject unsafe setting changes made using this API, and should be used with caution in these contexts.
  - If a feature requires both standard `elasticsearch.yml` settings and [secure settings](https://www.elastic.co/docs/deploy-manage/security/secure-settings), configure the secure settings first. Updating standard user settings can trigger a cluster rolling restart in self managed clusters and ECH and ECE deployments. If the required secure settings are not yet in place, the nodes might fail to start. Adding secure settings does not trigger a restart.
</warning>

<applies-switch>
  <applies-item title="{ ess:, ece: }" applies-to="Elastic Cloud Hosted: Generally available, Elastic Cloud Enterprise: Generally available">
    For Elastic Cloud Hosted and Elastic Cloud Enterprise deployments, you edit Elastic Stack settings through the Elastic Cloud Console or ECE Cloud UI. These settings are internally mapped to the appropriate YAML configuration files, such as `elasticsearch.yml` and `kibana.yml`, and they affect all users of that cluster.Elastic Cloud Hosted and Elastic Cloud Enterprise block the configuration of certain settings that could break your cluster if misconfigured. If a setting is not supported, you will get an error message when you try to save. We suggest changing one setting with each save, so you know which one is not supported.
    1. Log in to the [Elastic Cloud Console](https://cloud.elastic.co?page=docs&placement=docs-body) or ECE [Cloud UI](https://www.elastic.co/docs/deploy-manage/deploy/cloud-enterprise/log-into-cloud-ui).
    2. On the home page, find your deployment.
       <tip>
       If you have many deployments, you can instead go to the **Hosted deployments** (Elastic Cloud Hosted) or **Deployments** (Elastic Cloud Enterprise) page. On that page, you can narrow your deployments by name, ID, or choose from several other filters.
       </tip>
    3. Select **Manage**.

    1. Under the deployment's name in the navigation menu, select **Edit**.
    2. Look for the **Manage user settings and extensions** and **Edit user settings** links for each deployment, and select the one corresponding to the component you want to update, such as Elasticsearch or Kibana.
    3. Apply the necessary settings in the **Users Settings** tab of the editor and select **Back** when finished.
    4. Select **Save** to apply the changes to the deployment. Saving your changes initiates a configuration plan change that restarts the affected components for you.
    For further details and examples, refer to the resource for your deployment type:
    - [Elastic Cloud Hosted](https://www.elastic.co/docs/deploy-manage/deploy/elastic-cloud/edit-stack-settings)
    - [Elastic Cloud Enterprise](https://www.elastic.co/docs/deploy-manage/deploy/cloud-enterprise/edit-stack-settings)
  </applies-item>

  <applies-item title="eck:" applies-to="Elastic Cloud on Kubernetes: Generally available">
    Stack settings are defined as part of your resource specification.

    #### Elasticsearch

    Elasticsearch settings that are typically defined in the `elasticsearch.yml` configuration file can be specified for a set of nodes in the `spec.nodeSets[?].config` section of the Elasticsearch resource manifest.
    Some settings are managed by ECK. It is not recommended to change these managed settings. For a complete list, refer to [Settings managed by ECK](https://www.elastic.co/docs/deploy-manage/deploy/cloud-on-k8s/settings-managed-by-eck).
    ```yaml
    spec:
      nodeSets:
      - name: masters
        count: 3
        config:
          # On Elasticsearch versions before 7.9.0, replace the node.roles configuration with the following:
          # node.master: true
          node.roles: ["master"]
          xpack.ml.enabled: true
      - name: data
        count: 10
        config:
          # On Elasticsearch versions before 7.9.0, replace the node.roles configuration with the following:
          # node.master: false
          # node.data: true
          # node.ingest: true
          # node.ml: true
          # node.transform: true
          node.roles: ["data", "ingest", "ml", "transform"]
    ```

    <warning>
      ECK parses Elasticsearch configuration and normalizes it to YAML. Consequently, some Elasticsearch configuration schema are impossible to express with ECK and, therefore, must be set using [dynamic cluster settings](/docs/deploy-manage/deploy/self-managed/configure-elasticsearch#cluster-setting-types). For example:
      ```yaml
      spec:
        nodeSets:
        - name: data
          # ...
          config:
            cluster.max_shards_per_node: 1000
            cluster.max_shards_per_node.frozen: 1000
          # ...
      ```
    </warning>


    #### Kibana

    You can add your own Kibana settings to the `spec.config` section.
    The following example demonstrates how to set the [`elasticsearch.requestHeadersWhitelist`](https://www.elastic.co/docs/reference/kibana/configuration-reference/general-settings#elasticsearch-requestheaderswhitelist) configuration option.
    ```yaml
    apiVersion: kibana.k8s.elastic.co/v1
    kind: Kibana
    metadata:
      name: kibana-sample
    spec:
      version: 9.3.1
      count: 1
      elasticsearchRef:
        name: "elasticsearch-sample"
      config:
         elasticsearch.requestHeadersWhitelist:
         - authorization
    ```
  </applies-item>

  <applies-item title="self:" applies-to="Self-managed Elastic deployments: Generally available">
    The method and location where you can update your Elastic Stack settings depends on the component and installation method.

    #### Elasticsearch (`elasticsearch.yml`)Most settings can be changed on a running cluster using the [Cluster update settings](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cluster-put-settings) API.
    You can also set Elasticsearch settings in `elasticsearch.yml`.  Some settings require a cluster restart. To learn more, refer to [Dynamic and static Elasticsearch settings](#static-dynamic).To learn more about configuring Elasticsearch in a self-managed environment, refer to [Configure Elasticsearch](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/configure-elasticsearch).

    | Installation method                      | Default location                                                                                                                                        |
    |------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
    | Archive distribution (`tar.gz` or `zip`) | `$ES_HOME/config` ([override](/docs/deploy-manage/deploy/self-managed/configure-elasticsearch#archive-distributions))                                   |
    | Package distribution (Debian or RPM)     | `/etc/elasticsearch` ([override](/docs/deploy-manage/deploy/self-managed/configure-elasticsearch#package-distributions))                                |
    | Docker                                   | `/usr/share/elasticsearch/config/` ([Learn more](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/install-elasticsearch-docker-configure)) |


    #### Kibana (`kibana.yml`)To learn more about configuring Kibana in a self-managed environment, refer to [Configure Kibana](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/configure-kibana).


    | Installation method                      | Default location                                                                                                           |
    |------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
    | Archive distribution (`tar.gz` or `zip`) | `$KIBANA_HOME/config` ([override](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/configure-kibana))         |
    | Package distribution (Debian or RPM)     | `/etc/kibana` ([override](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/configure-kibana))                 |
    | Docker                                   | `/usr/share/kibana/config/` ([Learn more](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/configure-kibana)) |


    #### OtherFor APM and Enterprise Search, refer to the product's documentation:

    - [APM](https://www.elastic.co/docs/reference/apm/observability/apm-settings)
    - [Enterprise Search](https://www.elastic.co/guide/en/enterprise-search/8.18/configuration.html)


    #### Config file format

    The `elasticsearch.yml` configuration format is [YAML](https://yaml.org/). Here is an example of changing the path of the data and logs directories in Elasticsearch:
    ```yaml
    path:
        data: /var/lib/elasticsearch
        logs: /var/log/elasticsearch
    ```

    Settings can also be flattened as follows:
    ```yaml
    path.data: /var/lib/elasticsearch
    path.logs: /var/log/elasticsearch
    ```

    In YAML, you can format non-scalar values as sequences:
    ```yaml
    discovery.seed_hosts:
       - 192.168.1.10:9300
       - 192.168.1.11
       - seeds.mydomain.com
    ```

    Though less common, you can also format non-scalar values as arrays:
    ```yaml
    discovery.seed_hosts: ["192.168.1.10:9300", "192.168.1.11", "seeds.mydomain.com"]
    ```


    #### Environment variable substitution

    Environment variables referenced with the `${...}` notation within the `elasticsearch.yml` configuration file will be replaced with the value of the environment variable. For example:
    ```yaml
    node.name:    ${HOSTNAME}
    network.host: ${ES_NETWORK_HOST}
    ```

    Values for environment variables must be simple strings. Use a comma-separated string to provide values that the component will parse as a list. For example, Elasticsearch will split the following string into a list of values for the `${HOSTNAME}` environment variable:
    ```yaml
    export HOSTNAME="host1,host2"
    ```

    By default, configuration validation will fail if an environment variable used in the config file is not present when the component starts. This behavior can be changed by using a default value for the environment variable, using the `${MY_ENV_VAR:defaultValue}` syntax.
  </applies-item>
</applies-switch>


## Secure your settings

Some settings are sensitive, and relying on filesystem permissions to protect their values is not sufficient. For this use case, Elasticsearch and Kibana provide secure keystores to store sensitive configuration values such as passwords, API keys, and tokens.
Secure settings are often referred to as **keystore settings**, since they must be added to the product-specific keystore rather than the standard `elasticsearch.yml` or `kibana.yml` files. Unlike regular settings, they are encrypted and protected at rest, and they cannot be read or modified through the usual configuration files or environment variables.
If a feature requires both standard `elasticsearch.yml` settings and [secure settings](https://www.elastic.co/docs/deploy-manage/security/secure-settings), configure the secure settings first. Updating standard user settings can trigger a cluster rolling restart in self managed clusters and ECH and ECE deployments. If the required secure settings are not yet in place, the nodes might fail to start. Adding secure settings does not trigger a restart.
To learn how to interact with secure settings, refer to [Secure your settings](https://www.elastic.co/docs/deploy-manage/security/secure-settings).

## Dynamic and static Elasticsearch settings

Elasticsearch cluster and node settings can be categorized based on how they are configured:

### Dynamic

You can configure and update dynamic settings on a running cluster using the [cluster update settings API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cluster-put-settings). You can also configure dynamic settings locally on an unstarted or shut down node using `elasticsearch.yml`.
Updates made using the cluster update settings API can be *persistent*, which apply across cluster restarts, or *transient*, which reset after a cluster restart. You can also reset transient or persistent settings by assigning them a `null` value using the API.
If you configure the same setting using multiple methods, Elasticsearch applies the settings in following order of precedence:
1. Transient setting
2. Persistent setting
3. `elasticsearch.yml`setting
4. Default setting value

For example, you can apply a transient setting to override a persistent setting or `elasticsearch.yml` setting. However, a change to an `elasticsearch.yml` setting will not override a defined transient or persistent setting.
<warning>
  We no longer recommend using transient cluster settings. Use persistent cluster settings instead. If a cluster becomes unstable, transient settings can clear unexpectedly, resulting in a potentially undesired cluster configuration.
</warning>

In a self-managed cluster, you should use the [cluster update settings API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cluster-put-settings) to configure dynamic cluster settings, and only use `elasticsearch.yml` for static cluster settings and node settings. The API doesn’t require a restart and ensures a setting’s value is the same on all nodes.
Elastic Cloud Hosted and Elastic Cloud Enterprise don’t reject unsafe setting changes made using this API, and should be used with caution in these contexts.

### Static

Static settings can only be configured on an unstarted or shut down node using `elasticsearch.yml`.
Static settings must be set on every relevant node in the cluster.
`elasticsearch.yml` should contain settings which are node-specific (such as `node.name` and paths), or settings which a node requires in order to be able to join a cluster, such as `cluster.name` and `network.host`.