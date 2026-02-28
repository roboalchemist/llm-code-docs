# Harbor docs | Configure the Harbor YML File

**Source:** https://goharbor.io/docs/2.14.0/install-config/configure-yml-file/

Configure the Harbor YML File

[Harbor version 2.14.0](/docs/2.14.0)

[Harbor Installation and Configuration](/docs/2.14.0/install-config/)

* [Test Harbor with the Demo Server](/docs/2.14.0/install-config/demo-server/)
* [Harbor Compatibility List](/docs/2.14.0/install-config/harbor-compatibility-list/)
* [Harbor Installation Prerequisites](/docs/2.14.0/install-config/installation-prereqs/)
* [Download the Harbor Installer](/docs/2.14.0/install-config/download-installer/)
* [Configure HTTPS Access to Harbor](/docs/2.14.0/install-config/configure-https/)
* [Configure Internal TLS communication between Harbor Component](/docs/2.14.0/install-config/configure-internal-tls/)
* [Configure the Harbor YML File](/docs/2.14.0/install-config/configure-yml-file/)
* [Run the Installer Script](/docs/2.14.0/install-config/run-installer-script/)
* [Deploying Harbor with High Availability via Helm](/docs/2.14.0/install-config/harbor-ha-helm/)
* [Troubleshooting Harbor Installation](/docs/2.14.0/install-config/troubleshoot-installation/)
* [Reconfigure Harbor and Manage the Harbor Lifecycle](/docs/2.14.0/install-config/reconfigure-manage-lifecycle/)
* [Customize the Harbor Token Service](/docs/2.14.0/install-config/customize-token-service/)
* [Harbor Configuration](/docs/2.14.0/install-config/configure-system-settings-cli/)

[Harbor Administration](/docs/2.14.0/administration/)

[Working with Projects](/docs/2.14.0/working-with-projects/)

[Building, Customizing, and Contributing to Harbor](/docs/2.14.0/build-customize-contribute/)

You set system level parameters for Harbor in the `harbor.yml` file that is contained in the installer package. These parameters take effect when you run the `install.sh` script to install or reconfigure Harbor.

After the initial deployment and after you have started Harbor, you perform additional configuration in the Harbor Web Portal.

## Required Parameters

The table below lists the parameters that must be set when you deploy Harbor. By default, all of the required parameters are uncommented in the `harbor.yml` file. The optional parameters are commented with `#`. You do not necessarily need to change the values of the required parameters from the defaults that are provided, but these parameters must remain uncommented. At the very least, you must update the `hostname` parameter.

**IMPORTANT**: Harbor does not ship with any certificates. In versions up to and including 1.9.x, by default Harbor uses HTTP to serve registry requests. This is acceptable only in air-gapped test or development environments. In production environments, always use HTTPS.

You can use certificates that are signed by a trusted third-party CA, or you can use self-signed certificates. For information about how to create a CA, and how to use a CA to sign a server certificate and a client certificate, see
[Configuring Harbor with HTTPS Access](/docs/2.14.0/install-config/configure-https/).

Required Parameters for Harbor Deployment

| Parameter | Sub-parameters | Description and Additional Parameters |
| `hostname` | None | Specify the IP address or the fully qualified domain name (FQDN) of the target host on which to deploy Harbor. This is the address at which you access the Harbor Portal and the registry service. For example, `192.168.1.10` or `reg.yourdomain.com`. The registry service must be accessible to external clients, so do not specify `localhost`, `127.0.0.1`, or `0.0.0.0` as the hostname. |
| `http` |  | Do not use HTTP in production environments. Using HTTP is acceptable only in air-gapped test or development environments that do not have a connection to the external internet. Using HTTP in environments that are not air-gapped exposes you to man-in-the-middle attacks. |
|  | `port` | Port number for HTTP, for both Harbor portal and Docker commands. The default is 80. |
| `https` |  | Use HTTPS to access the Harbor Portal and the token/notification service. Always use HTTPS in production environments and environments that are not air-gapped. |
|  | `port` | The port number for HTTPS, for both Harbor portal and Docker commands. The default is 443. |
|  | `certificate` | The path to the SSL certificate. |
|  | `private_key` | The path to the SSL key. |
| `internal_tls` |  | Use HTTPS to communicate between harbor components |
|  | `enabled` | Set this flag to `true` means internal tls is enabled |
|  | `dir` | The path to the directory that contains internal certs and keys |
| `harbor_admin_password` | None | Set an initial password for the Harbor system administrator. This password is only used on the first time that Harbor starts. On subsequent logins, this setting is ignored and the administrator's password is set in the Harbor Portal. The default username and password are `admin` and `Harbor12345`. |
| `database` |  | Use a local PostgreSQL database. You can optionally configure an external database, in which case you can deactivate this option. |
|  | `password` | Set the root password for the local database. You must change this password for production deployments. |
|  | `max_idle_conns` | The maximum number of connections in the idle connection pool. If it <=0, no idle connections are retained. |
|  | `max_open_conns` | The maximum number of open connections to the database. If it <= 0, then there is no limit on the number of open connections. |
|  | `conn_max_lifetime` | The maximum amount of time a connection may be reused. If it <= 0, connections are not closed due to a connection's age. |
|  | `conn_max_idle_time` | The maximum amount of time a connection may be idle. If it <= 0, connections are not closed due to a connection's idle time. |
| `data_volume` | None | The location on the target host in which to store Harbor's data. This data remains unchanged even when Harbor's containers are removed and/or recreated. You can optionally configure external storage, in which case deactivate this option and enable `storage_service`. The default is `/data`. |
| `trivy` |  | Configure Trivy scanner. |
|  | `ignore_unfixed` | Set the flag to `true` to display only fixed vulnerabilities. The default value is `false` |
|  | `security_check` | Comma-separated list of what security issues to detect. Possible values are `vuln`, `config` and `secret`. Defaults to `vuln`. |
|  | `skip_update` | You might want to enable this flag in test or CI/CD environments to avoid GitHub rate limiting issues. If the flag is enabled you have to download the `trivy-offline.tar.gz` archive manually, extract and the `trivy.db` and `metadata.json` files and mount them in the `/home/scanner/.cache/trivy/db/trivy.db` path in container. The default value is `false` |
|  | `insecure` | Set the flag to `true` to skip verifying registry certificate. The default value is `false` |
|  | `github_token` | Set the GitHub access token to download Trivy DB. Trivy DB is downloaded by Trivy from the GitHub release page. Anonymous downloads from GitHub are subject to the limit of 60 requests per hour. Normally such rate limit is enough for production operations. If, for any reason, it's not enough, you could increase the rate limit to 5000 requests per hour by specifying the GitHub access token. For more details on GitHub rate limiting please consult https://developer.github.com/v3/#rate-limiting .You can create a GitHub token by following the instructions in https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line |
| `jobservice` | `max_job_workers` | The maximum number of replication workers in the job service. For each image replication job, a worker synchronizes all tags of a repository to the remote destination. Increasing this number allows more concurrent replication jobs in the system. However, since each worker consumes a certain amount of network/CPU/IO resources, set the value of this attribute based on the hardware resource of the host. The default is 10. |
| `notification` | `webhook_job_max_retry` | Set the maximum number of retries for web hook jobs. The default is 10. |
| `log` |  | Configure logging. Harbor uses `rsyslog` to collect the logs for each container. |
|  | `level` | Set the logging level to `debug`, `info`, `warning`, `error`, or `fatal`. The default is `info`. |
|  | `local` | Set the log retention parameters:  * `rotate_count`: Log files are rotated `rotate_count` times before being removed. If count is 0, old versions are removed rather than rotated. The default is 50. * `rotate_size`: Log files are rotated only if they grow bigger than `rotate_size` bytes. Use `k` for kilobytes, `M` for megabytes, and `G` for gigabytes. `100`, `100k`, `100M` and `100G` are all valid values. The default is 200M. * `location`: Set the directory in which to store the logs. The default is `/var/log/harbor`. |
|  | `external_endpoint` | Enable this option to forward logs to a syslog server.  * `protocol`: Transport protocol for the syslog server. Default is TCP. * `host`: The URL of the syslog server. * `port`: The port on which the syslog server listens |
| `proxy` |  | Configure proxies to be used by trivy-adapter, the replication jobservice, and Harbor. Leave blank if no proxies are required. Some proxies have whitelist settings, if Trivy is enabled, you need to add the following urls to the proxy server whitelist: `github.com`, `github-releases.githubusercontent.com`, and `*.s3.amazonaws.com.` |
|  | `http_proxy` | Configure an HTTP proxy, for example, `http://my.proxy.com:3128`. |
|  | `https_proxy` | Configure an HTTPS proxy, for example, `http://my.proxy.com:3128`. |
|  | `no_proxy` | Configure when not to use a proxy, for example, `127.0.0.1,localhost,core,registry`. |
| `cache` |  | Configure cache layer for your Harbor instance. When enabled, Harbor will cache some Harbor resources (for example, artifacts, projects, or project metadata) using Redis, reducing the amount of time and resources used for repeated requests for the same Harbor resource. It's strongly recommended that you enable this feature on Harbor instances with high concurrent pull request rates to improve Harbor's overall performance. For more details on the cache layer implementation and performance improvements, see the [Cache Layer wiki page](https://github.com/goharbor/perf/wiki/Cache-layer). |
|  | `enabled` | Default is `false`, set to `true` to enable Harbor's cache layer. |
|  | `expire_hours` | Configure the cache expiration limit in hours. Default is 24. |

## Optional Parameters

The following table lists the additional, optional parameters that you can set to configure your Harbor deployment beyond the minimum required settings. To enable a setting, you must uncomment it in `harbor.yml` by deleting the leading `#` character.

Optional Parameters for Harbor

| Parameter | Sub-Parameters | Description and Additional Parameters |
| `external_url` | None | Enable this option to use an external proxy. When enabled, the hostname is no longer used. |
||  |  |  |
| --- | --- | --- |
| `storage_service` |  | By default, Harbor stores images and charts on your local filesystem. In a production environment, you might want to use another storage backend instead of the local filesystem. The parameters listed below are the configurations for the registry. See \*Configuring Storage Backend\* below for more information about how to configure a different backend. |
|  | `ca_bundle` | The path to the custom root CA certificate, which is injected into the trust store of registry and chart repository containers. This is usually needed if internal storage uses a self signed certificate. |
|  | `filesystem` | The default is `filesystem`, but you can set `azure`, `gcs`, `s3`, `swift` and `oss`. For information about how to configure other backends, see [Configuring a Storage Backend](#backend) below. Set `maxthreads` to limit the number of threads to the external provider. The default is 100. |
|  | `redirect` | Set `deactivate` to `true` when you want to deactivate registry redirect |
| `external_database` |  | Configure external database settings, if you deactivate the local database option. Currently, Harbor only supports PostgreSQL database. You must create a database for Harbor core. The tables are generated automatically when Harbor starts up. |
|  | `harbor` | Configure an external database for Harbor data.   * `host`: Hostname of the Harbor database. * `port`: Database port. * `db_name`: Database name. * `username`: Username to connect to the core Harbor database. * `password`: Password for the account you set in `username`. * `ssl_mode`: Enable SSL mode. * `max_idle_conns`: The maximum number of connections in the idle connection pool. If <=0 no idle connections are retained. The default value is 2. * `max_open_conns`: The maximum number of open connections to the database. If <= 0 there is no limit on the number of open connections. The default value is 0. |
| `external_redis` |  | Configure an external Redis instance. |
|  | `host` | redis\_host:redis\_port of the external Redis instance. If you are using Sentinel mode, this part should be host\_sentinel1:port\_sentinel1,host\_sentinel2:port\_sentinel2 |
|  | `sentinel_master_set` | Only set this when using Sentinel mode |
|  | `password` | Password to connect to the external Redis instance. |
|  | `registry_db_index` | Database index for Harbor registry. |
|  | `jobservice_db_index` | Database index for jobservice. |
|  | `chartmuseum_db_index` | Database index for Chart museum. |
|  | `trivy_db_index` | Database index for Trivy adapter. |
| `metric` |  | Configure exposing Harbor instance metrics to a specified port and path |
|  | `enabled` | Enable exposing metrics on your Harbor instance by setting this to `true`. Default is `false` |
|  | `port` | Port metrics are exposed on. Default is `9090` |
|  | `path` | Path metrics are exposed on. Default is `/metrics` |
| `trace` |  | Configure exposing Distributed tracing data |
|  | `enabled` | Enable exposing tracing on your Harbor instance by setting this to `true`. Default is `false` |
|  | `sample_rate` | Set the sample rate of tracing. For example, set sample\_rate to `1` if you wanna sampling 100% of trace data; set `0.5` if you wanna sampling 50% of trace data, and so forth |
|  | `namespace` | Namespace used to differentiate different harbor services, which will set to attribute with key `service.namespace` |
|  | `attributes` | The attributes is a key value dict contains user defined customized attributes used to initialize trace provider, and all of these attributes will added to trace data |
|  | `jaeger` | * `endpoint`: The url of endpoint(for example `http://127.0.0.1:14268/api/traces`). set endpoint means export to jaeger collector via http. * `username:`: Username used to connect endpoint. Left empty if not needed. * `password:`: Password used to connect endpoint. Left empty if not needed. * `agent_host`: The host name of jaeger agent. Set agent\_host means export data to jaeger agent via udp. * `agent_port:`: The port name of jaeger agent. |
|  | `otel` | * `endpoint`: The hostname and port for otel compatible backend(for example `127.0.0.1:4318`). * `url_path:`: The url path of endpoint(for example `127.0.0.1:4318`) * `compression:`: If enabling data compression * `insecure`: Ignore cert verification for otel backend * `timeout:`: The timeout of data transfer |

The `harbor.yml` file includes options to configure a UAA CA certificate. This authentication mode is not recommended and is not documented.

## Configuring a Storage Backend

By default Harbor uses local storage for the registry, but you can optionally configure the `storage_service` setting so that Harbor uses external storage. For information about how to configure the storage backend of a registry for different storage providers, see the
[Distribution Configuration Reference](https://distribution.github.io/distribution/about/configuration/) in the Distribution Registry (previously Docker Registry) documentation. For example, if you use Openstack Swift as your storage backend, the parameters might resemble the following:

```
storage_service:
  ca_bundle:
  swift:
    username: admin
    password: ADMIN_PASS
    authurl: http://keystone_addr:35357/v3/auth
    tenant: admin
    domain: default
    region: regionOne
    container: docker_images
  redirect:
    disabled: false
```

## What to Do Next

To install Harbor,
[Run the Installer Script](/docs/2.14.0/install-config/run-installer-script/).

On this page

  
  

Contributing

[Page source](https://github.com/goharbor/website/blob/release-2.14.0/docs/install-config/configure-yml-file.md)
[Create issue](https://github.com/goharbor/harbor/issues)