# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/set-up-clusters-on-aks.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/set-up-clusters-on-aks.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/set-up-clusters-on-aks.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/set-up-clusters-on-aks.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/set-up-clusters-on-aks.md

# Step 2: Set up the primary and replica clusters on AKS

The setup instructions are based on a [architecture-example](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/architecture-example "mention").

### Requirements on AKS clusters <a href="#requirements" id="requirements"></a>

The only requirement for the AKS clusters creation step is to create the primary and replica clusters in different geographical regions.

Default networking (Azure CNI Overlay) and storage settings are supported and capable of hosting a SonarQube DCE instance using the Helm chart provided by Sonar.

Sizing of the clusters is outside the scope of this section.

### Step 1: Deploy your DCE on AKS <a href="#deploy-dce-on-aks" id="deploy-dce-on-aks"></a>

You must set in the Helm chart the access to the PostgreSQL Virtual Writer endpoint as follows:

1\. Modify the Helm chart for each cluster to add the JDBC URL with the Database Virtual Writer Endpoint as follows (see [customizing-helm-chart](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/customizing-helm-chart "mention")):

```yaml
jdbcOverwrite:
 enabled: true
 jdbcPassword: <somepassword>
 jdbcUrl: jdbc:postgresql://yourVirtualWriterEndpoint:5432/yourDB
 jdbcUsername: <dbUserName>
```

2. Deploy the two clusters following the instructions on the [installing-from-helm-repo](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/installing-from-helm-repo "mention") page.
3. Once the clusters are deployed, keep only the primary cluster up and stop the replica cluster as it could create conflicts.

{% hint style="info" %}
Do not enable the Nginx dependencies in the Helm chart since an Azure mechanism is used (see below).
{% endhint %}

### Step 2: Set up the Azure managed NGINX ingress controllers <a href="#set-up-ingress-controllers" id="set-up-ingress-controllers"></a>

You must create an ingress for each one of your clusters, primary and replica. These ingresses will be configured as origins for the Azure Front Door’s origin group.

{% hint style="info" %}
For production environments, Azure Front Door requires FQDNs with a CA-signed certificate (self-signed certificates are not supported). IP addresses can be used for testing purposes only.
{% endhint %}

For each cluster:

1\. Enable Application Routing using Azure CLI on your AKS cluster as follows.

```
az aks approuting enable --resource-group <ResourceGroupName> --name <ClusterName>
```

2. Configure Kubectl to connect to your AKS cluster as follows.

```
az aks get-credentials --resource-group <ResourceGroupName> --name <ClusterName>
```

3. Create the Ingress object. Copy the following YAML file into a new file named `ingress.yaml` and save it to your computer. If you used a namespace when deploying your SonarQube Server, it should be added to the metadata section.

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: sonarqube-dce
  namespace: sonarqube-dce
  annotations:
    nginx.ingress.kubernetes.io/proxy-body-size: 120m
spec:
  ingressClassName: webapprouting.kubernetes.azure.com
  rules:
  - http:
      paths:
      - backend:
          service:
            name: sonarqube-dce-sonarqube-dce
            port:
              number: 9000
        path: /
        pathType: Prefix
```

4. Create the ingress with the `kubectl` apply command (using a namespace is optional) as follows.

```
kubectl apply -f ingress.yaml -n <yourNameSpace>
```

5. Verify the Ingress was created as follows.

```
kubectl get ingress -n <yourNameSpace>
```

### Related pages

* [architecture-example](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/architecture-example "mention")
* [deploy-databases](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/deploy-databases "mention")
* [configure-azure-front-door](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/configure-azure-front-door "mention")
* [test-failover-scenarios](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/test-failover-scenarios "mention")
