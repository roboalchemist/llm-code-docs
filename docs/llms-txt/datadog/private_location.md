# Source: https://docs.datadoghq.com/getting_started/synthetics/private_location.md

---
title: Getting Started with Private Locations
description: >-
  Set up private locations to monitor internal applications and private URLs.
  Create custom locations for mission-critical areas and internal testing
  environments.
breadcrumbs: >-
  Docs > Getting Started > Getting Started with Synthetic Monitoring > Getting
  Started with Private Locations
---

# Getting Started with Private Locations

## Overview{% #overview %}

Private locations allow you to **monitor internal-facing applications** or private URLs that aren't accessible from the public internet.

{% image
   source="https://datadog-docs.imgix.net/images/synthetics/private_locations/private_locations_worker_1.a0a7ba80447a205e0b4c5bfa86f57616.png?auto=format"
   alt="Architecture diagram of how a private location works in Synthetic Monitoring" /%}

You can also use private locations to:

- **Create custom locations** in mission-critical areas of your business.
- **Verify the application performance in your internal testing environment** before you release new features to production with [Synthetic tests in your CI/CD pipelines](https://docs.datadoghq.com/continuous_testing/cicd_integrations).
- **Compare the application performance** from inside and outside your internal network.
- **[Authenticate Synthetic Monitoring tests using Kerberos SSO](https://docs.datadoghq.com/synthetics/guide/kerberos-authentication/)** for internal Windows-based sites and APIs.

Private locations are Docker containers or Windows services that you can install anywhere inside your private network. Retrieve the docker image on [Google Container Registry](https://console.cloud.google.com/gcr/images/datadoghq/GLOBAL/synthetics-private-location-worker?pli=1) or download the [Windows installer](https://ddsynthetics-windows.s3.amazonaws.com/datadog-synthetics-worker-1.64.0.amd64.msi).**\***

**Note**: Private locations on Docker containers are supported only on the amd64 architecture. If you have any questions about arm64 support, contact [Datadog support](https://www.datadoghq.com/support/).

**\*** **Use and operation of this software is governed by the End User License Agreement available [here](https://www.datadoghq.com/legal/eula/).**

Once you've created and installed your private location, you can assign [Synthetic tests](https://docs.datadoghq.com/getting_started/synthetics/) to your private location just like you would with a managed location.

Your private locations test results display identically to your managed location test results.

{% image
   source="https://datadog-docs.imgix.net/images/synthetics/private_locations/test_results_pl.d49df3a18d0a65500fce4b34c8dc0b9e.png?auto=format"
   alt="Assign a Synthetic test to private locations" /%}

## Create your private location{% #create-your-private-location %}

1. In the Datadog site, hover over **Digital Experience** and select **Settings** > [**Private Locations**](https://app.datadoghq.com/synthetics/settings/private-locations).

1. Click **Add Private Location**.

1. Fill out your private location details. Only `Name` and `API key` fields are mandatory.

1. Click **Save Location and Generate Configuration File** to generate the configuration file associated with your private location on your worker.

1. Depending on where you installed your private location, you may need to input additional parameters to your configuration file:

   - If you are using a proxy, input the URL as `http://<YOUR_USER>:<YOUR_PWD>@<YOUR_IP>:<YOUR_PORT>`.
   - If you want to block reserved IPs, toggle **Block reserved IPs** and enter the IP ranges.

For more information, see [Private Locations Configuration Options](https://docs.datadoghq.com/synthetics/private_locations/configuration/#configuration-options) and [Run Synthetic Tests from Private Locations](https://docs.datadoghq.com/synthetics/private_locations/?tab=docker#blocking-reserved-ips).

1. Copy and paste your private location configuration file to your working directory.

**Note**: The configuration file contains secrets for private location authentication, test configuration decryption, and test result encryption. Datadog does not store the secrets, so store them locally before leaving the **Private Locations** creation form. **You need to be able to reference the secrets again in order to add more workers to your private location**.

1. When you are ready, click **View Installation Instructions**.

1. Follow the installation instructions based on the environment you want to run the Private Location worker in.

1. If you are using Docker, launch your worker as a standalone container using the Docker `run` command and your configuration file:

   ```shell
   docker run --rm -v $PWD/worker-config-<LOCATION_ID>.json:/etc/datadog/synthetics-check-runner.json datadog/synthetics-private-location-worker
   ```

This command starts a Docker container and prepares your private location to run tests. Datadog recommends running the container in detached mode with proper restart policy.
Important alert (level: info): You can use another container runtime such as Podman. For more information, see the [Private Locations documentation](https://docs.datadoghq.com/synthetics/private_locations/?tab=podman#install-your-private-location).
If you are using Windows, [run the Synthetics Private Location Installer with a GUI](https://docs.datadoghq.com/synthetics/private_locations?tab=windows#install-your-private-location) or run the `msiexec` command on the command line inside the directory where you downloaded the installer:

   ```shell
   msiexec /i datadog-synthetics-worker-1.64.0.amd64.msi
   ```

1. If your private location reports correctly to Datadog, an `OK` health status displays under **Private Location Status** and on the **Private Locations** list in the **Settings** page:

   {% image
      source="https://datadog-docs.imgix.net/images/synthetics/private_locations/pl_health.a5b5c34e8a28a5856d2f9d12afe696ea.png?auto=format"
      alt="Private Location Health" /%}

Additionally, you can see private location logs in your terminal:

   ```text
   2022-02-28 16:20:03 [info]: Fetching 10 messages from queue - 10 slots available
   2022-02-28 16:20:03 [info]: Fetching 10 messages from queue - 10 slots available
   2022-02-28 16:20:04 [info]: Fetching 10 messages from queue - 10 slots available
   ```

1. Once you're done testing your internal endpoint, click **OK**.

## Run Synthetic tests with your private location{% #run-synthetic-tests-with-your-private-location %}

Use your new private location just like a managed location in your Synthetic tests.

1. Create an [API test](https://console.cloud.google.com/gcr/images/datadoghq/GLOBAL/synthetics-private-location-worker?pli=1), [multistep API test](https://docs.datadoghq.com/getting_started/synthetics/api_test#create-a-multistep-api-test), or [browser test](https://docs.datadoghq.com/getting_started/synthetics/browser_test) on any internal endpoint or application you want to monitor.

1. Under **Private Locations**, select your new private location:

   {% image
      source="https://datadog-docs.imgix.net/images/synthetics/private_locations/assign-test-pl-2.55317eb80c33d978b492d867a199a173.png?auto=format"
      alt="Assign a Synthetic test to a private location" /%}

1. Continue filling out your test!

## Further Reading{% #further-reading %}

- [Monitor your Synthetic private locations with Datadog](https://www.datadoghq.com/blog/synthetic-private-location-monitoring-datadog/)
- [Learn more about private locations](https://docs.datadoghq.com/synthetics/private_locations)
- [Kerberos Authentication for Synthetic Monitorings](https://docs.datadoghq.com/synthetics/guide/kerberos-authentication/)
