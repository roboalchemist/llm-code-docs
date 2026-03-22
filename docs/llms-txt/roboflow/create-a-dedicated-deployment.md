# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/dedicated-deployments/create-a-dedicated-deployment.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/dedicated-deployments/create-a-dedicated-deployment.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/dedicated-deployments/create-a-dedicated-deployment.md

# Source: https://docs.roboflow.com/deploy/dedicated-deployments/create-a-dedicated-deployment.md

# Create a Dedicated Deployment

{% hint style="warning" %}
Dedicated Deployments are not available on Public (free) tier.
{% endhint %}

### Create a Deployment in the Web Interface

Open your workspace dashboard page, click **Deployments** on the left panel:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fb5YR9XFhQq851BfVZLQR%2Fdedicated-deployment.png?alt=media&#x26;token=54668a76-0715-49da-b52e-89556f5e9cf8" alt=""><figcaption></figcaption></figure>

Click the **New Deployment** button, it brings up the **Create a Dedicated Deployment** dialog as shown below:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-329104fa343e90108f6a59da4afd0ae8debe0638%2Fimage.png?alt=media" alt=""><figcaption><p>Configure properties for your dedicated deployment.</p></figcaption></figure>

Each of the properties in the dialog are described in the table below. Fill the dialog and click on the **Create Dedicated Deployment** button. It may take anywhere from a few seconds to a few minutes to provision your deployment.

<table><thead><tr><th width="165">Property</th><th>Description</th></tr></thead><tbody><tr><td>Name</td><td><p>Choose a unique name (5-15 characters) to identify your Dedicated Deployment. This name will also become the subdomain for your deployment endpoint (e.g., <em><strong>dev-testing</strong>.roboflow.cloud</em>).</p><ul><li><strong>Easy to Remember:</strong> Pick a name that clearly reflects your deployment's purpose (e.g., "prod-inference", "dev-testing").</li><li><strong>Unique within Workspace:</strong> If your chosen name is already taken, a short random code will be added to create a unique subdomain.</li></ul><p><strong>Tips:</strong></p><ul><li>Use lowercase letters, numbers, and hyphens (-) for your name.</li><li>Avoid special characters or spaces.</li></ul></td></tr><tr><td>Machine Type</td><td>Whether a CPU-only or a GPU dedicated deployment is needed.</td></tr><tr><td>Deployment Type</td><td><p><strong>Development</strong>: ideal for development or experimental purpose, automatically expires in 3 hours.</p><p><strong>Production</strong>: ideal for serving production requests, permanent until manually deleted.</p></td></tr><tr><td>Autoscaling</td><td>This feature is only for <strong>prod-cpu</strong> and <strong>prod-gpu</strong>.</td></tr></tbody></table>

### Create a Dedicated Deployment with the CLI

The `roboflow deployment` command provides a set of subcommands to manage your Roboflow Dedicated Deployments. Before you proceed, please ensure you have the `roboflow` CLI installed and configured with your API key, as documented [here.](https://docs.roboflow.com/roboflow-cli/roboflow-cli-documentation)

#### **Subcommands**

* **`machine_type`**: List available machine types for your Dedicated Deployments. Currently, we support `dev-cpu, dev-gpu, prod-cpu, prod-gpu`.
* **`add`**: Create a new Dedicated Deployment.
* **`get`**: Get detailed information about a specific Dedicated Deployment.
* **`list`**: List all Dedicated Deployments in your workspace.
* **`usage_workspace`**: Get usage statistics for all Dedicated Deployments in your workspace.
* **`usage_deployment`**: Get usage statistics for a specific Dedicated Deployment.
* **`delete`**: Delete a Dedicated Deployment.
* **`log`**: View logs for a specific Dedicated Deployment.

#### **Subcommand Examples**

* **Create a new deployment**

  ```
  roboflow deployment add my-deployment -m prod-gpu -e YOUR_EMAIL@aaa.com
  ```
* **Get deployment information**

  ```
  roboflow deployment get my-deployment
  ```
* **List all deployments**

  ```
  roboflow deployment list
  ```

  Use code with caution.
* **Get workspace usage**

  ```
  roboflow deployment usage_workspace
  ```
* **Get deployment usage**

  ```
  roboflow deployment usage_deployment my-deployment
  ```
* **Delete a deployment**

  ```
  roboflow deployment delete my-deployment
  ```
* **View deployment logs**

  ```
  roboflow deployment log my-deployment -t 60 -n 20
  ```

#### **Additional Notes**

* For more detailed information and options for each subcommand, use the `--help` flag.
