# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/dedicated-deployments.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/dedicated-deployments.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/dedicated-deployments.md

# Source: https://docs.roboflow.com/deploy/dedicated-deployments.md

# Dedicated Deployments

### **What are Dedicated Deployments?**

Dedicated Deployments are private cloud servers managed by Roboflow, specifically designed to run your computer vision models. These models can include:

* Object detection
* Image segmentation
* Classification
* Keypoint detection
* Foundation models like CLIP (if trained on Roboflow)
* Roboflow Workflows (low-code vision applications)
* ...and many others!

### **Benefits of Dedicated Deployments**

* **Focus on your machine vision business problem, leave the infrastructure to us:** Spin up inference serving infrastructure with a few clicks and without having to signup with cloud providers, installing and securing servers, managing TLS certificates or worrying about server management, patching, updates etc.
* **Dedicated Resources:** Get cloud servers allocated specifically for your use, ensuring consistent performance for your models.
* **Secure Access:** Dedicated Deployments are accessible with your workspace's unique API key and utilize HTTPS for secure communication.
* **Easy Integration:** Each deployment receives a subdomain within `roboflow.cloud`, simplifying integration with your applications.
* **Pay-Per-Hour:** You're only charged for the duration of the server's existence (billed in 1 minute intervals).
* **Auto Pause & Resume**: Your Dedicated Deployments will automatically pause after a configurable period of inactivity. For `dev-cpu` or `dev-gpu` deployment types, this period is fixed at 1 hour. They can be quickly resumed by sending a request with your API key. This feature is designed to help you save on costs.

### **Current Limitations**

* All dedicated deployments are currently hosted in US-based data centers; users from other Geographies may see higher latencies. Please contact us for a customized solution if you are outside of US, we can help you to reduce the network latency.
* Dedicated Deployments are available to Core and Enterprise plan workspaces. See [Roboflow plans](https://roboflow.com/pricing).

### Types of Dedicated Deployments

Roboflow offers 4 different types of Dedicated Deployments, i.e., dev-cpu, dev-gpu, prod-cpu, and prod-gpu. While dev-cpu and dev-gpu are designed for development and testing purposes, will be deleted automatically after a few hours, prod-cpu and prod-gpu are persistent, ideally for serving large-scale production traffic.

<table><thead><tr><th width="184">Type</th><th>Features</th></tr></thead><tbody><tr><td>dev-cpu</td><td><p><strong>Ephemeral</strong>: will be automatically deleted after 3 hours</p><p><strong>CPU</strong>: model inference can be done on the CPU</p><p>Ideal for <strong>testing integrations</strong> and <strong>prototyping</strong> applications</p></td></tr><tr><td>dev-gpu</td><td><p><strong>Ephemeral</strong>: will be automatically deleted after 3 hours</p><p><strong>Ideal for testing integrations</strong> and <strong>prototyping</strong> applications</p><p><strong>GPU</strong>: models need GPU acceleration (like Florence 2)</p><p>Ideal for <strong>testing integrations</strong> and <strong>prototyping</strong> applications</p></td></tr><tr><td>prod-cpu</td><td><p><strong>Persistent</strong>: dedicated subdomain <code>&#x3C;some-name>.roboflow.cloud</code></p><p><strong>CPU</strong>: model inference can be done on the CPU</p><p>Ideal for <strong>serving production traffic</strong></p></td></tr><tr><td>prod-gpu</td><td><p><strong>Persistent</strong>: dedicated subdomain <code>&#x3C;some-name>.roboflow.cloud</code></p><p><strong>GPU</strong>: models need GPU acceleration (like Florence 2)</p><p>Ideal for <strong>serving production traffic</strong></p></td></tr></tbody></table>

### **Bill Information**

The rate for GPU deployments (dev-gpu, prod-gpu) is **1 credit/hour**, while the rate for CPU deployments (dev-cpu, prod-cpu) is **0.25 credit/hour**.

If you prefer to be billed based on number of requests sent to your dedicated deployment server, please [click here to contact our sales](https://roboflow.com/sales).

All dedicated deployment servers will run [Roboflow Inference](https://inference.roboflow.com/), our open-source inference server. Review the [Roboflow Inference documentation](https://inference.roboflow.com/) to learn more about all of the features available.

### Useful Links <a href="#provision-and-manage-dedicated-deployments-web-application" id="provision-and-manage-dedicated-deployments-web-application"></a>

* [How to create a dedicated deployment (Roboflow App)](#provision-and-manage-dedicated-deployments-web-application-2)
* [How to create a dedicated deployment (Roboflow CLI)](https://docs.roboflow.com/deploy/create-a-dedicated-deployment#create-a-dedicated-deployment-with-the-cli)
* [How to use a dedicated deployment](https://docs.roboflow.com/deploy/dedicated-deployments/make-requests-to-a-dedicated-deployment)
* [HTTP APIs](https://docs.roboflow.com/deploy/dedicated-deployments/manage-dedicated-deployments-with-an-api)
