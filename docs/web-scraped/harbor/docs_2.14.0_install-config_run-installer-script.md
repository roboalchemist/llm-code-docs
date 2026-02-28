# Harbor docs | Run the Installer Script

**Source:** https://goharbor.io/docs/2.14.0/install-config/run-installer-script/

Run the Installer Script

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

Once you have configured `harbor.yml` copied from `harbor.yml.tmpl` and optionally set up a storage backend, you install and start Harbor by using the `install.sh` script. Note that it might take some time for the online installer to download all of the Harbor images from Docker hub.

You can install Harbor in different configurations:

* Just Harbor, without Trivy
* Harbor with Trivy

## Default installation without Trivy

The default Harbor installation does not include Trivy service. Run the following command

```bash
sudo ./install.sh
```

If the installation succeeds, you can open a browser to visit the Harbor interface at `http://reg.yourdomain.com`, changing `reg.yourdomain.com` to the hostname that you configured in `harbor.yml`. If you did not change them in `harbor.yml`, the default administrator username and password are `admin` and `Harbor12345`.

Log in to the admin portal and create a new project, for example, `myproject`. You can then use Docker commands to log in to Harbor, tag images, and push them to Harbor.

```bash
docker login reg.yourdomain.com
docker push reg.yourdomain.com/myproject/myrepo:mytag
```

* If your installation of Harbor uses HTTPS, you must provide the Harbor certificates to the Docker client. For information, see [Configure HTTPS Access to Harbor](configure-https.md#provide-the-certificates-to-harbor-and-docker).
* If your installation of Harbor uses HTTP, you must add the option `--insecure-registry` to your client’s Docker daemon and restart the Docker service. For more information, see [Connecting to Harbor via HTTP](#connect-http) below.

## Installation with Trivy

To install Harbor with Trivy service, add the `--with-trivy` parameter when you run `install.sh`:

```bash
sudo ./install.sh --with-trivy
```

For more information about Trivy, see the
[Trivy documentation](https://github.com/aquasecurity/trivy).
For more information about how to use Trivy in an webproxy environment see
[Configure custom Certification Authorities for trivy](administration/vulnerability-scanning/configure-custom-certs.md)

## Connecting to Harbor via HTTP

**IMPORTANT:** If your installation of Harbor uses HTTP rather than HTTPS, you must add the option `--insecure-registry` to your client’s Docker daemon. By default, the daemon file is located at `/etc/docker/daemon.json`.

For example, add the following to your `daemon.json` file:

```json
{
"insecure-registries" : ["myregistrydomain.com:5000", "0.0.0.0"]
}
```

After you update `daemon.json`, you must restart both Docker Engine and Harbor.

1. Restart Docker Engine.

   ```bash
   systemctl restart docker
   ```

2. Stop Harbor.

   ```bash
   docker compose down -v
   ```

3. Restart Harbor.

   ```bash
   docker compose up -d
   ```

## What to Do Next

* If the installation succeeds, see
  [Harbor Administration](/docs/2.14.0/administration/) for information about using Harbor.
* If you deployed Harbor with HTTP and you want to secure the connections to Harbor, see
  [Configure HTTPS Access to Harbor](/docs/2.14.0/install-config/configure-https/).
* If installation fails, see
  [Troubleshooting Harbor Installation](/docs/2.14.0/install-config/troubleshoot-installation/).

On this page

Contributing

[Page source](https://github.com/goharbor/website/blob/release-2.14.0/docs/install-config/run-installer-script.md)
[Create issue](https://github.com/goharbor/harbor/issues)
