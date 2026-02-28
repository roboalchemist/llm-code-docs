# Harbor docs | Reconfigure Harbor and Manage the Harbor Lifecycle

**Source:** https://goharbor.io/docs/2.14.0/install-config/reconfigure-manage-lifecycle/

Reconfigure Harbor and Manage the Harbor Lifecycle

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

You use `docker-compose` to manage the lifecycle of Harbor. This topic provides some useful commands. You must run the commands in the directory in which `docker-compose.yml` is located.

See the
[Docker Compose command-line reference](https://docs.docker.com/compose/reference/) for more information about `docker-compose`.

## Stop Harbor

To stop Harbor, run the following command.

```
sudo docker compose stop
Stopping nginx              ... done
Stopping harbor-portal      ... done
Stopping harbor-jobservice  ... done
Stopping harbor-core        ... done
Stopping registry           ... done
Stopping redis              ... done
Stopping registryctl        ... done
Stopping harbor-db          ... done
Stopping harbor-log         ... done
```

## Restart Harbor

To restart Harbor, run the following command.

```
sudo docker compose start
Starting log         ... done
Starting registry    ... done
Starting registryctl ... done
Starting postgresql  ... done
Starting core        ... done
Starting portal      ... done
Starting redis       ... done
Starting jobservice  ... done
Starting proxy       ... done
```

## Reconfigure Harbor

To reconfigure Harbor, perform the following steps.

1. Stop Harbor.

   ```
   sudo docker compose down -v
   ```
2. Update `harbor.yml`.

   ```
   vim harbor.yml
   ```
3. Run the `prepare` script to populate the configuration.

   ```
   sudo ./prepare
   ```

   To reconfigure Harbor to install Trivy, include the component in the `prepare` command.

   ```
   sudo ./prepare --with-trivy
   ```
4. Re-create and start the Harbor instance.

   ```
   sudo docker compose up -d
   ```

## Other Commands

Remove Harbor’s containers but keep all of the image data and Harbor’s database files in the file system:

```
sudo docker compose down -v
```

Remove the Harbor database and image data before performing a clean re-installation:

```
rm -r /data/database
rm -r /data/registry
rm -r /data/redis
```

On this page

  
  

Contributing

[Page source](https://github.com/goharbor/website/blob/release-2.14.0/docs/install-config/reconfigure-manage-lifecycle.md)
[Create issue](https://github.com/goharbor/harbor/issues)