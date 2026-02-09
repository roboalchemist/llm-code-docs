# Source: https://braintrust.dev/docs/integrations/ai-providers/azure.md

# Source: https://braintrust.dev/docs/admin/self-hosting/azure.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Self-host on Azure

This guide shows you how to deploy the Braintrust data plane in your Azure subscription using the Braintrust [Terraform module](https://github.com/braintrustdata/terraform-azure-braintrust-data-plane) and [Helm chart](https://github.com/braintrustdata/helm). This is the recommended way to self-host Braintrust on Azure.

## Set up the data plane

Deploy the Braintrust data plane infrastructure in your Azure subscription.

<Steps>
  <Step title="Configure the Terraform module">
    The Braintrust [Terraform module](https://github.com/braintrustdata/terraform-azure-braintrust-data-plane) contains all the necessary resources for a self-hosted Braintrust data plane. A dedicated Azure subscription for your Braintrust deployment is recommended but not required.

    1. Copy the entire contents of the [`examples/default`](https://github.com/braintrustdata/terraform-azure-braintrust-data-plane/tree/main/examples/default) directory from the [terraform-azure-braintrust-data-plane](https://github.com/braintrustdata/terraform-azure-braintrust-data-plane) repository into your own repository.

    2. In `provider.tf`, configure your Azure subscription and tenant details.

    3. In `terraform.tf`, set up your remote backend (typically Azure Blob Storage).

    4. In `main.tf`, customize the Braintrust deployment settings.

       The default configuration is for a large production-sized deployment. Adjust them based on your needs, but keep in mind the [hardware requirements](/admin/self-hosting/index#hardware-requirements).

    5. Initially set `enable_front_door = false` in `main.tf`. You'll enable this later after configuring the load balancer.
  </Step>

  <Step title="Deploy the base infrastructure">
    Initialize and apply the Terraform configuration:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    terraform init
    terraform apply
    ```

    This will create all necessary Azure resources including:

    * AKS cluster for running Braintrust services
    * Azure Database for PostgreSQL
    * Azure Cache for Redis
    * Azure Storage Account
    * Virtual Network
    * Azure Key Vault for encryption and secrets

    This deployment typically takes 15-20 minutes.
  </Step>

  <Step title="Connect to AKS cluster">
    After the Terraform deployment completes, connect to your AKS cluster:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    az aks get-credentials --resource-group braintrust --name braintrust-aks
    ```

    Verify the connection:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    kubectl get nodes
    ```
  </Step>

  <Step title="Configure Helm values">
    Create a `helm-values.yaml` file for your deployment. Refer to the [Helm chart documentation](https://github.com/braintrustdata/helm) for configuration options.

    Configure the API service as a LoadBalancer with Azure internal annotation:

    ```yaml  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    api:
      service:
        type: LoadBalancer
        annotations:
          service.beta.kubernetes.io/azure-load-balancer-internal: "true"
    ```
  </Step>

  <Step title="Deploy Helm chart">
    Deploy the Braintrust [Helm chart](https://github.com/braintrustdata/helm) to your cluster:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    helm install braintrust \
      oci://public.ecr.aws/braintrust/helm/braintrust \
      --namespace braintrust \
      --create-namespace \
      --version <version> \
      --values helm-values.yaml
    ```
  </Step>

  <Step title="Configure Front Door">
    Retrieve the load balancer IP address and frontend configuration:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    lb_ip_address=$(kubectl get service braintrust-api -n braintrust \
      -o jsonpath='{.status.loadBalancer.ingress[0].ip}')

    az network lb list \
      --query "[?frontendIPConfigurations[?privateIPAddress=='$lb_ip_address']].{Name:name, ResourceGroup:resourceGroup, FrontendIPConfig:frontendIPConfigurations[0].name, Id:frontendIPConfigurations[0].id}" \
      -o table
    ```

    Save the load balancer IP address and frontend IP configuration ID for the next step.
  </Step>

  <Step title="Approve Private Link Service">
    In the Azure Portal, find the private link service named `<deployment>-aks-api-pls` and manually approve it.

    This step is required before Front Door can connect to your AKS cluster.
  </Step>

  <Step title="Enable Front Door in Terraform">
    Update `main.tf` with the values from the previous steps:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    enable_front_door = true
    front_door_api_backend_address = "<LB_IPAddress>"
    front_door_load_balancer_frontend_ip_config_id = "<LB_FrontendIPConfigId>"
    ```

    Apply the changes:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    terraform apply
    ```

    <Warning>
      Front Door deployment takes up to 45 minutes after the Terraform apply completes. Wait for the deployment to finish before proceeding.
    </Warning>
  </Step>

  <Step title="Get your API URL">
    After the Front Door deployment completes, get your API URL from the Terraform outputs:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    terraform output
    ```

    Test the endpoint:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    curl https://<endpoint-hostname>/
    ```

    You should receive a 200 OK response. Save this URL - you'll need it to configure your Braintrust organization.
  </Step>
</Steps>

## Configure your organization

Connect your Braintrust organization to your newly deployed data plane.

<Warning>
  Changing your live organization's API URL can disrupt access for existing users. If you are testing, create a new Braintrust organization for your data plane instead of updating your live environment.
</Warning>

<Steps>
  <Step title="Point your organization to your data plane">
    1. In the Braintrust UI, go to **Settings** > **Data plane**.
    2. In **API URL** area, select **Edit**.
    3. Enter the API URL from the last step.
    4. Leave the other fields blank.
    5. Select **Save**.
  </Step>

  <Step title="Verify the connection">
    The UI will automatically test the connection to your new data plane. Verify that the ping to each endpoint is successful.
  </Step>
</Steps>

## Update the deployment

Updating your Azure deployment involves two steps: updating infrastructure with Terraform and updating services with Helm.

### Update infrastructure (Terraform)

Run `terraform apply` to update infrastructure components (database, Redis, networking, storage, etc.):

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
terraform apply
```

<Warning>
  Carefully review the output of `terraform plan` before applying any changes to your deployment. If you see something unexpected, like deletion of a database or storage account, [contact Braintrust](mailto:support@braintrust.dev) for help.
</Warning>

To pin to a specific Terraform module version, add a `?ref=<version>` to the module source:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
module "braintrust-data-plane" {
  source = "github.com/braintrustdata/terraform-azure-braintrust-data-plane?ref=vX.Y.Z"

  # ... other configuration ...
}
```

Terraform releases: [GitHub Releases](https://github.com/braintrustdata/terraform-azure-braintrust-data-plane/releases)

### Update services (Helm)

After updating infrastructure, upgrade the Helm chart to update service containers and configurations:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
helm upgrade braintrust braintrust/braintrust-data-plane \
  --namespace braintrust \
  --reuse-values \
  --version <version>
```

<Note>
  In some cases, Terraform changes must be applied before Helm upgrades. Check the release notes for any specific upgrade ordering requirements.
</Note>

Helm releases: [GitHub Releases](https://github.com/braintrustdata/helm/releases)
