# Source: https://docs.startree.ai/thirdeye/getting-started/install-thirdeye.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Install ThirdEye

ThirdEye is available as a managed platform with StarTree Cloud.

It can also be installed from a binary file, from sources or using Docker.

Before you start, read [ThirdEye Infrastructure Requirements](/thirdeye/getting-started/infrastructure-requirements) for details about capacity planning, components, and deployment planning.

<Tabs>
  <Tab title="StarTree Cloud">
    StarTree Cloud provides managed hosting for ThirdEye on all major cloud platforms, including AWS and GCP.

    To start using ThirdEye in StarTree Cloud, [**sign up for StarTree Cloud**](https://startree.ai/demo).
  </Tab>

  <Tab title="Helm">
    To install ThirdEye on Kubernetes using Helm, complete the steps in this doc.

    ## Prerequisites

    * Access to StarTree ThirdEye artifacts
    * [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl) installed
    * `kubectl` is connected to the k8s cluster where you want to install ThirdEye
    * [Helm 3.x](https://helm.sh/docs/intro/install/) installed

    ### Access to StarTree ThirdEye artifacts

    Contact [StarTree](https://startree.ai/contact-us) to obtain credentials to create a k8s secret that lets helm access ThirdEye source files.

    Use these to set up access to the Artifactory repo.

    ```bash  theme={null}
     # This assumes you are installing Thirdeye in the "thirdeye" namespace
    namespace="thirdeye"
    username="<YOUR_USERNAME>"
    STARTREE_REPO_URL="<STARTREE_REPO_URL>"
    ARTIFACTORY_API_KEY="<YOUR_API_KEY>"

    kubectl create secret docker-registry startree -n $namespace \
    --docker-server=$STARTREE_REPO_URL \
    --docker-username=$username \
    --docker-password=$ARTIFACTORY_API_KEY
    ```

    ## ThirdEye Installation

    To install ThirdEye, complete the follow steps to set up a Helm repo and run the Helm install.

    ### Set up Helm repo

    Edit the following script to include your credentials.

    ```powershell  theme={null}
    STARTREE_HELM_REPO_URL="<STARTREE_HELM_REPO_URL>"

    # Add stable helm repo
    helm repo add helmstable https://charts.helm.sh/stable
    helm repo add startree $STARTREE_HELM_REPO_URL --username $username --password $ARTIFACTORY_API_KEY

    # Update your local repo
    helm repo update

    # fetch dependencies. example: mysql. See Chart.yaml
    helm dependency update
    ```

    Verify the `startree-thirdeye` chart is accessible.

    ```shell  theme={null}
    helm search repo startree-thirdeye
    ```

    Expected Output:

    ```
    NAME                       CHART VERSION APP VERSION    DESCRIPTION                         
    startree/startree-thirdeye 2.4.0         0.5.0-SNAPSHOT One Stop Shop For Anomaly Detection.
    ```

    ### Running Helm Install

    Edit the following script to include your credentials.\`\`\`

    ```shell  theme={null}
    # setup StarTree Docker repo
    export DOCKER_CONTAINER_URL="<DOCKER_CONTAINER_URL>"

    # Your ThirdEye domain name
    export THIRDEYE_UI_PUBLIC_URL="http://thirdeye.internal.company.com"

    # Artifact Versions
    HELM_VERSION="2.6.0"
    TE_VERSION="0.154.0"
    TE_UI_VERSION="2.41.4"

    helm install thirdeye startree/startree-thirdeye \
    --version ${HELM_VERSION} \
    -n $namespace \
    --set image.repository="${DOCKER_CONTAINER_URL}/startree-thirdeye" \
    --set ui.image.repository="${DOCKER_CONTAINER_URL}/startree-thirdeye-ui" \
    --set ui.publicUrl="${THIRDEYE_UI_PUBLIC_URL}" \
    --set image.tag=${TE_VERSION} \
    --set ui.image.tag=${TE_UI_VERSION}
    ```

    ## Upgrading ThirdEye

    ```shell  theme={null}
    # For example, This upgrades ThirdEye to the desired development image.
    helm upgrade --install thirdeye -n "${namespace}" . \
    --set image.tag=${TE_VERSION} \
    --set ui.image.tag=${TE_UI_VERSION}
    ```

    ## Uninstalling ThirdEye

    ```shell  theme={null}
    helm uninstall thirdeye -n $namespace
    ```

    ## Configurations

    To specify ThirdEye configurations, do one of the following:

    * Set parameters by adding `--set key=value[,key=value]` arguments to the `helm install` command.
    * Create a YAML file to specify parameters values, like this:

    Alternatively, you can create a YAML file that specifies the values for the parameters, then load it like this:

    ```bash  theme={null}
    helm install thirdeye . -f values.yaml
    ```

    ### Dynamic Secrets

    ThirdEye has plugin infrastructure which lets you to create your own plugins. To avoid creating `Secret` resources for the sensitive data for each new plugin, create dynamic secrets. For example, add the following information to a `values.yaml` file:

    ```yaml  theme={null}
    secrets:
      smtpUsername:
        env: SMTP_USER
        value: tobefedexternally
      smtpPassword:
        env: SMTP_PASSWORD
        value: tobefedexternally
      holidayLoaderKey:
        encoded: true
        value: <base 64 encoded json key>
    ```

    Here are some important details:

    1. A single `Secret` resource is created with data fields corresponding to each entry in `secrets`.
    2. A secret data field is injected as an environment variable. In our example, we see the key `env`. In the server pods, if we pass `env`, `smtpUsername` is injected as an environment variable with the variable name `SMTP_USER` and value `tobefedexternally`, while `holidayLoaderKey` won't be injected as environment variable.
    3. The values are processed as plain text by default and encoded internally unless you provide `encoded: true`, then the value isn't encoded because Helm assumes the value is already encoded.
    4. We recommend passing values other than simple strings (like the JSON payload) as `base64` encoded values to avoid parsing issues.

    ### Holiday Events

    ThirdEye lets you display events from external Google calendars. To enable this feature, provide a **base64 encoded** JSON key. See [https://docs.simplecalendar.io/google-api-key/](https://docs.simplecalendar.io/google-api-key/) for more details.

    To install this feature:

    ```bash  theme={null}
    helm install thirdeye . \
      --set secrets.holidayLoaderKey.value="<base64 encoded key>" \
      --set secrets.holidayLoaderKey.encoded=true
    ```

    ### Custom Calendar List

    The ThirdEye Helm chart has a default list of the following calendars:

    * en.australian#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.austrian#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.brazilian#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.canadian#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.china#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.christian#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.danish#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.dutch#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.finnish#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.french#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.german#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.greek#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.hong\_kong#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.indian#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.indonesian#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.irish#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.islamic#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.italian#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.japanese#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.jewish#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.malaysia#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.mexican#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.new\_zealand#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.norwegian#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.philippines#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.polish#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.portuguese#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.russian#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.singapore#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.sa#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.south\_korea#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.spain#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.swedish#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.taiwan#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.uk#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.usa#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)
    * en.vietnamese#[holiday@group.v.calendar.google.com](mailto:holiday@group.v.calendar.google.com)

    But if you want to pass a selected list of calendars, do this:

    ```bash  theme={null}
    helm install thirdeye . \
      --set config.calendars="{en.australian#holiday@group.v.calendar.google.com,en.austrian#holiday@group.v.calendar.google.com}"
    ```

    ### SSL/TLS Support

    To enable SSL/TLS on ThirdEye components, contact [StarTree](https://startree.ai/contact-us).

    ### Basic Authentication Support

    To configure basic authentication, add the following to your `server.yaml` file:

    ```yaml  theme={null}
    auth:
      enabled: true
      basic:
        enabled: true
        users:
          - username: admin
          - password: admin
    ```

    Details

    | Property                 | Description                                        |
    | ------------------------ | -------------------------------------------------- |
    | `enabled`                | Flag to enable/disable auth                        |
    | `basic.enabled`          | Flag to enable/disable Basic authentication filter |
    | `basic.users[].username` | Username for authentication                        |
    | `basic.users[].password` | Password for authentication                        |

    ### Other Customizations

    | Property                                           | Description                                                                                                          |
    | -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
    | `image.repository`                                 | Docker repository where ThirdEye server image is present                                                             |
    | `image.tag`                                        | Docker image tag of ThirdEye server image                                                                            |
    | `ui.image.repository`                              | Docker repository where ThirdEye UI image is present                                                                 |
    | `ui.image.tag`                                     | Docker image tag of ThirdEye UI image                                                                                |
    | `ui.port`                                          | UI service port                                                                                                      |
    | `ui.publicUrl`                                     | Url on which ThirdEye UI is exposed publicly. All the notifications will use this url to share the anomaly page link |
    | `scheduler.enabled`                                | Flag to run a separate scheduler. If not enabled then coordinator itself will take care of scheduling tasks          |
    | `worker.enabled`                                   | Flag to run a separate worker. If not enabled then coordinator itself will take care of running tasks                |
    | `worker.replicas`                                  | Number of worker pods required                                                                                       |
    | `worker.randomWorkerIdEnabled`                     | Flag to enable assigning random worker ids to worker pods. Must be set true for multiple workers.                    |
    | `prometheus.enabled`                               | Flag to expose prometheus metrics and adding annotations for prometheus to scrape the metrics                        |
    | `mysql.enabled`                                    | Flag to disable MySQL deployment if using external instance                                                          |
    | `mysql.url`                                        | Database URL if using external instance                                                                              |
    | `mysql.port`                                       | Database port if using external instance                                                                             |
    | `mysql.mysqlUser`                                  | Database username                                                                                                    |
    | `mysql.mysqlPassword`                              | Database password                                                                                                    |
    | `mysql.persistence.size`                           | Size of persistent volume created for database storage                                                               |
    | `config.jdbcParameters`                            | Config to pass additional parameters to the jdbc connection string                                                   |
    | `[coordinator/worker/scheduler].strategy`          | Specifies the strategy used to replace old Pods by new ones.                                                         |
    | `tls.[coordinator/worker/scheduler/ui].secretName` | When provided it will override the default secret names referred for tls keys                                        |
  </Tab>

  <Tab title="From Source">
    * See [Build](https://github.com/startreedata/thirdeye#build) procedure on Github
  </Tab>

  <Tab title="Docker">
    The Docker image is not publicly available yet, but you can build it manually.

    * See [Build](https://github.com/startreedata/thirdeye#build) on Github
    * See [Docker](https://github.com/startreedata/thirdeye#docker)

    To be the first to know when public docker images are available, [join the StarTree Community slack](https://inviter.co/startree-community).
  </Tab>

  <Tab title="From Binary">
    Binaries are not publicly available yet, but you can build from the sources manually.

    * See [Build](https://github.com/startreedata/thirdeye#build) on Github
    * See [Running from distribution](https://github.com/startreedata/thirdeye#running-thirdeye-from-distribution)

    To be the first to know when public binaries are available, [join the StarTree Community slack](https://inviter.co/startree-community).
  </Tab>
</Tabs>

### Recommended ThirdEye Version

| Build             | Edition    | Version |
| ----------------- | ---------- | ------- |
| helm chart        | Community  | 2.6.0   |
| thirdeye          | Community  | 1.199.0 |
| thirdeye-ui       | Community  | 2.41.4  |
| startree-thirdeye | Enterprise | 0.154.0 |

Built with [Mintlify](https://mintlify.com).
