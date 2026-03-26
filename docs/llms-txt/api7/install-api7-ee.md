# Source: https://docs.api7.ai/enterprise/getting-started/install-api7-ee.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/getting-started/install-api7-ee.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/getting-started/install-api7-ee.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/getting-started/install-api7-ee.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/getting-started/install-api7-ee.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/getting-started/install-api7-ee.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/getting-started/install-api7-ee.md

# Source: https://docs.api7.ai/enterprise/3.8.x/getting-started/install-api7-ee.md

# Source: https://docs.api7.ai/enterprise/3.7.x/getting-started/install-api7-ee.md

# Source: https://docs.api7.ai/enterprise/3.6.x/getting-started/install-api7-ee.md

# Source: https://docs.api7.ai/enterprise/3.5.x/getting-started/install-api7-ee.md

# Source: https://docs.api7.ai/enterprise/3.4.x/getting-started/install-api7-ee.md

# Source: https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md

# Install API7 Enterprise

This tutorial walks you through installing API7 Enterprise in Docker using the quickstart script.

The installation will include the [API7 Enterprise components](https://docs.api7.ai/enterprise/3.3.x/introduction/architecture.md), data plane, control plane, dashboard, and external components, PostgreSQL and Prometheus, for managing configuration and monitoring, respectively.

tip

In this guide, a containerized all-in-one solution for Proof of Concept (PoC) tests is provided, including PostgreSQL and Prometheus. This eliminates the need for manual database and monitoring setup, streamlining your PoC process.

For production deployments, API7 Enterprise also supports MySQL and OceanBase in place of PostgreSQL. Deployment is supported only through container-based methods, such as Docker, or through container orchestration platforms like Kubernetes. Installation using deb or rpm packages is not supported.

Please [contact API7 experts](https://api7.ai/contact) to get solutions for high availability and scalability.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* Install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install). It is recommended to use 3.10.0-927 or higher versions. It is known that 3.10.0-327 or previous versions are incompatible.
* Install [cURL](https://curl.se/).
* Obtain a 30-day [free trial license](https://api7.ai/try?product=enterprise).
* Operating system: It is recommended to use Linux CentOS 7.6 or higher versions. It is known that Linux CentOS 7.2 or previous versions are incompatible.

## Install API7 Enterprise[â](#install-api7-enterprise "Direct link to Install API7 Enterprise")

```
curl -sL "https://run.api7.ai/api7/quickstart" | bash
```

You should see a response similar to the following:

```
â Container api7-ee-postgresql
â Container api7-ee-prometheus
â Container api7-ee-api7-ee-dashboard
â Container api7-ee-api7-ee-dp-manager
â Container api7-ee-api7-ee-gateway
...
â API7-EE is ready!

API7-EE Listening: Dashboard(https://192.168.2.102:7443), Control Plane Address(http://192.168.2.102:7900, https://192.168.2.102:7943), Gateway(http://192.168.2.102:9080, https://192.168.2.102:9443)
API7-EE Listening: Dashboard(https://26.26.26.1:7443), Control Plane Address(http://26.26.26.1:7900, https://26.26.26.1:7943), Gateway(http://26.26.26.1:9080, https://26.26.26.1:9443)
If you want to access Dashboard with HTTP Endpoint(:7080), you can turn server.listen.disable to false in dashboard_conf/conf.yaml, then restart dashboard container
```

### (Optional) Install ADC[â](#optional-install-adc "Direct link to (Optional) Install ADC")

You can also install the API Declarative CLI (ADC) to manage API7 Enterprise declaratively.

```
curl -sL "https://run.api7.ai/adc/install" | bash
```

To verify the installation, run:

```
adc help
```

You should see the following response:

```
Usage: adc [options] [command]

Options:
  -V, --version      output the version number
  -h, --help         display help for command

Commands:
  ping [options]     Verify connectivity with backend
  dump [options]     Dump configurations from the backend
  diff [options]     Show the difference between local and backend configurations
  sync [options]     Sync local configurations to backend
  convert [options]  Convert other API spec to ADC configurations
  lint [options]     Check provided configuration files, local execution only, ensuring inputs meet ADC requirements
  help [command]     display help for command
```

See the [Command Reference](https://docs.api7.ai/enterprise/3.3.x/reference/adc.md) for more details on the available commands and configurations.

## Activate API7 Enterprise[â](#activate-api7-enterprise "Direct link to Activate API7 Enterprise")

1. Visit the API7 Enterprise Dashboard at `https://{your_inet_ip_addr}:7443` and log in with the default username `admin` and password `admin`.

info

You can also access the dashboard at `https://localhost:7443/login`. However, the subsequent deployment scripts generated in the dashboard will default to use `localhost` as the IP address, which can lead to connectivity issues, such as when [deploying API7 gateway and ingress controller on Kubernetes](https://docs.api7.ai/enterprise/3.3.x/deployment/ingress-controller.md).

2. Select the license that you want to upload and then click **Upload** to activate API7 Enterprise.

### (Optional) Connect to API7 Enterprise with ADC[â](#optional-connect-to-api7-enterprise-with-adc "Direct link to (Optional) Connect to API7 Enterprise with ADC")

Before you can synchronize configurations to API7 Enterprise using ADC, first make sure your ADC client can authenticate and communicate with API7 Enterprise. You would need to configure a few variables either in a `.env` file or on the command flags.

Navigate to the API7 Enterprise Dashboard and [generate a token](https://docs.api7.ai/enterprise/3.3.x/best-practices/manage-token.md#3-obtain-a-token).

Create a `.env` file with the following variables:

.env

```
ADC_BACKEND=api7ee                   # specify the backend is API7 Enterprise
ADC_TOKEN=a7ee-YVDPvh6CXxMuz5iM...   # replace with your token
ADC_SERVER=https://localhost:7443    # update server address if you are not running API7 Enterprise locally
```

Alternatively, you could also specify these values in command flags. See the [ADC Environment Variables](https://docs.api7.ai/enterprise/3.3.x/reference/adc.md#using-environment-variables) for more information.

To verify connectivity, run:

```
adc ping
```

You should see the following response:

```
Connected to the "api7ee" backend successfully!
```

## Stop API7 Enterprise[â](#stop-api7-enterprise "Direct link to Stop API7 Enterprise")

If you have finished testing API7 Enterprise, you can stop API7 Enterprise using the following command under the `api7-ee` directory:

```
bash run.sh stop
```

## Next Steps[â](#next-steps "Direct link to Next Steps")

1. See [Deploy Gateway and Ingress Controller on Kubernetes](https://docs.api7.ai/enterprise/3.3.x/deployment/ingress-controller.md) if you would like to deploy API7 gateways on Kubernetes and use an ingress controller.
2. Follow the [getting started tutorials](https://docs.api7.ai/enterprise/3.3.x/getting-started/launch-your-first-api.md) to learn more about using API7 Enterprise.
3. Deploy API7 Enterprise in a [highly available configuration](https://docs.api7.ai/enterprise/3.3.x/high-availability/overview.md).
4. [Book a meeting](https://api7.ai/contact) with API7 experts to start using API7 Enterprise in production.
