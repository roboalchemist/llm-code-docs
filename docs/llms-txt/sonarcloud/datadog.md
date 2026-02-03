# Source: https://docs.sonarsource.com/sonarqube-community-build/server-installation/on-kubernetes-or-openshift/set-up-monitoring/datadog.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/setup-and-upgrade/deploy-on-kubernetes/set-up-monitoring/datadog.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/setup-and-upgrade/deploy-on-kubernetes/set-up-monitoring/datadog.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/deploy-on-kubernetes/set-up-monitoring/datadog.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/setup-and-upgrade/deploy-on-kubernetes/set-up-monitoring/datadog.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/deploy-on-kubernetes/set-up-monitoring/datadog.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/setup-and-update/deploy-on-kubernetes/set-up-monitoring/datadog.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/on-kubernetes-or-openshift/set-up-monitoring/datadog.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/on-kubernetes-or-openshift/set-up-monitoring/datadog.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/deploy-on-kubernetes/set-up-monitoring/datadog.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/on-kubernetes-or-openshift/set-up-monitoring/datadog.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/on-kubernetes-or-openshift/set-up-monitoring/datadog.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/set-up-monitoring/datadog.md

# Setting up with Datadog

In the following, we assume that you are installing both SonarQube Server and Datadog to a Kubernetes cluster via the corresponding Helm charts.

### Introduction <a href="#introduction" id="introduction"></a>

To set up Datadog to monitor SonarQube Server, you have to specify an annotation in SonarQube Server’s Helm chart related to Datadog. Since Datadog doesn’t understand the Prometheus’ Bearer authentication annotation, you cannot use it. Instead, you can specify an annotation that will manage a Datadog configuration file.

The illustration below shows the setup and monitoring process:

* When you install the SonarQube Server’s Helm chart in the Kubernetes cluster, the chart deploys the Datadog configuration file on the Pod.
* The Datadog agent then:
  1. Reads the Datadog configuration file.
  2. Authenticates to the SonarQube Server’s Web API endpoint and pulls the Prometheus metrics from the endpoint.
  3. Pushes the metrics to the Datadog dashboard.

<figure><img src="broken-reference" alt="SonarQube monitoring setup with Datadog"><figcaption></figcaption></figure>

### Setting up the Datadog authentication to the Web API endpoint <a href="#authentication" id="authentication"></a>

You need to create a secret containing the monitoring passcode and then mount that secret in the Datadog agent. To do so, add the code below to the `values.yaml` file of the Datadog’s Helm chart. In this example, we mount the subkey `passcode` from the `datadog-api-secret` secret into `/etc/secret-volume`.

```css-79elbk
agents:
 volumes:
 - name: secret-volume
   secret:
     secretName: datadog-api-secret
     items:
     - key: passcode
       path: passcode
 volumeMounts:
 - name: secret-volume
   mountPath: /etc/secret-volume
```

### Specifying the annotation for the Datadog agent <a href="#annotation" id="annotation"></a>

Add the code below to the `values.yaml` file of the SonarQube Server’s Helm chart. Note that:

* This example corresponds to the example shown shown in **Setting up the Datadog authentication to the Web API endpoint** above: you must adapt the `reader` and `writer` sections to your values.
* If a webcontext is used in the path at which to serve SonarQube Server then you must add it to the `openmetrics_endpoint`. For example, if the`/sonarqube` web context were used here then we would have:\
  `"openmetrics_endpoint": "http://%%host%%:9000/sonarqube/api/monitoring/metrics"`

```yaml
# Set annotations for pods
annotations:
 #ad.datadoghq.com/<EXPECTED_POD_NAME>.checks  
 ad.datadoghq.com/sonarqube-dce.checks: |
     {
       "openmetrics": {
         "init_config": {},
         "instances": [
           {
             "openmetrics_endpoint": "http://%%host%%:9000/api/monitoring/metrics",
             "metrics": [".*"],
             "auth_token": 
             {
               "reader": 
               {
                 "type": "file",
                 "path": "/etc/secret-volume/passcode"
               },
               "writer":
               {
                 "type": "header",
                 "name": "Authorization",
                 "value": "Bearer <TOKEN>"
               }
             }
           }
         ]
       }
     }
```
