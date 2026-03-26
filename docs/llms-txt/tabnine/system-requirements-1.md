# Source: https://docs.tabnine.com/main/welcome/readme/system-requirements/system-requirements-1.md

# Optional Features / Additional Requirements

### Provenance and Attribution:

Storage: 5 TB available space

### **Domain Name System (DNS)**

DNS configured with an A or CNAME record for the load balancer where the application\
will be exposed.

### **TLS Certificate**

TLS certificate and private key issued and signed by a certificate authority that you trust (key and certificate in PEM format).

### **Network Connection**

* Connection to Tabnine container registry:
  * Host: registry.tabnine.com
  * IP: 34.72.243.185
  * Port: 443
* Connection to Tabnine logs gateway for collecting metrics and logs (optional):
  * Host: logs-gateway.tabnine.com
  * IP: 34.123.33.186
  * Port: 443

### **Databases**

<table><thead><tr><th width="57.7890625"></th><th>Databases</th></tr></thead><tbody><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-7aabb0dd08a6560efc2b4fe308c2b2acf25ee438%2FRedis.svg?alt=media" alt=""></td><td>Redis version 6.5+</td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-4656cb79adde771d6eb3bf58647f4e82e89e083b%2FPostgresSQL.svg?alt=media" alt=""></td><td>PostgreSQL version 15.0+</td></tr></tbody></table>

***

### Kubernetes

{% tabs %}
{% tab title="On-Premises Kubernetes" %}
**On-Premises Kubernetes** ​Tabnine Enterprise can be installed on a new or existing Kubernetes cluster. For customers installing on a brand new Kubernetes cluster, we recommend the following minimum hardware specifications for the Kubernetes control-plane only (non-inclusive of Tabnine requirements).

| **Specs (Per Node)** | **HA**         | **Non-HA**     |
| -------------------- | -------------- | -------------- |
| Number of Nodes      | 3              | 1              |
| CPU                  | 4 CPU          | 4 CPU          |
| Memory               | 16 GB          | 16 GB          |
| Disk                 | 256 GB SSD     | 256 GB SSD     |
| Network              | 1 GbE          | 1 GbE          |
| Operating System     | RHEL or Ubuntu | RHEL or Ubuntu |

**On-Premises**

| **Specs (Minimum)** | **1 - 200 Users** | **201 - 500 Users** | **501-1000 Users** | **1001-2000 Users** | **2000+ Users** |
| ------------------- | ----------------- | ------------------- | ------------------ | ------------------- | --------------- |
| CPU                 | 64                | 64                  | 72                 | 72                  | 96              |
| Memory              | 144 GB            | 144 GB              | 192 GB             | 192 GB              | 256 GB          |
| Disk                | 10 TB SSD         | 10 TB SSD           | 16 TB SSD          | 16 TB SSD           | 32 TB SSD       |
| {% endtab %}        |                   |                     |                    |                     |                 |

{% tab title="On-Prem Hybrid Kubernetes" %}
On-Prem Hybrid allows for a connection to external models for the main LLM, including Claude Sonnet, ChatGPT, Gemini, etc.

| **Specs (Per Node)** | **HA**         | **Non-HA**     |
| -------------------- | -------------- | -------------- |
| Number of Nodes      | 3              | 1              |
| CPU                  | 4 CPU          | 4 CPU          |
| Memory               | 16 GB          | 16 GB          |
| Disk                 | 256 GB SSD     | 256 GB SSD     |
| Network              | 1 GbE          | 1 GbE          |
| Operating System     | RHEL or Ubuntu | RHEL or Ubuntu |

**On-Premises Hybrid**

| **Specs (Minimum)** | **1 - 200 Users** | **201 - 500 Users** | **501-1000 Users** | **1001-2000 Users** | **2000+ Users** |
| ------------------- | ----------------- | ------------------- | ------------------ | ------------------- | --------------- |
| CPU                 | 64                | 64                  | 72                 | 72                  | 96              |
| Memory              | 144 GB            | 144 GB              | 192 GB             | 192 GB              | 256 GB          |
| Disk                | 10 TB SSD         | 10 TB SSD           | 16 TB SSD          | 16 TB SSD           | 32 TB SSD       |
| GPUs                | 2 x H100          | 2 x H100            | 4 x H100           | 6 x H100            | 10 x H100       |

<br>
{% endtab %}
{% endtabs %}
