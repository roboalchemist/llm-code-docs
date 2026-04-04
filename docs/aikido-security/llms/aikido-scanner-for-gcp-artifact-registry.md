# Source: https://help.aikido.dev/container-image-scanning/cloud-provider-registries/aikido-scanner-for-gcp-artifact-registry.md

# GCP Artifact Registry

## Introduction <a href="#introduction" id="introduction"></a>

Aikido supports scanning GCP Artifact images through both the **GCP scanner** and the **Aikido Scanner**. Opting for the Aikido Scanner provides several benefits:

* **Extended Scanning Capabilities**: Scans for licenses and end-of-life (EOL) runtimes for comprehensive security insights.
* **Quicker Results**: Delivers scan results promptly to accelerate development and deployment processes.
* **Targeted Scanning Efficiency**: Allows scanning based on specific tags, enhancing relevance and efficiency.
* **Continuous Scanning:** Unlike GCP, which scans once at the moment of push, Aikido performs daily scans—even if your image hasn't been updated in a while. This means Aikido can identify new Common Vulnerabilities and Exposures (CVEs) in the meantime, which GCP might miss.
* **Inclusive Pricing**: Included in every paid plan, offering unlimited scans without the additional costs associated with GCP's pay-per-push model.

## Installing the Aikido Scanner <a href="#installing-the-aikido-scanner" id="installing-the-aikido-scanner"></a>

1. **Navigate to** [**Containers Page**](https://app.aikido.dev/containers)
2. **Connect Registry**: Click on 'Connect registry' and select the first option: *'GCP artifact registry'*.
3. **Select Aikido Scanner**.\
   ​

   ![Choose a scanner for GCP Artifact Registry: Aikido or GCP Vulnerability scanning.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-4d3b1aa86ca937a09c11e65e1cfc22fec6f436e8%2Faikido-scanner-for-gcp-artifact-registry_9147058c-6e2b-4458-a794-2ccabd73f52b.png?alt=media)
4. **Fill in the Details**: Create a service account called 'AikidoContainerReader' and give it the role of "**Artifact Registry Reader**"\
   ​\
   Once the service account is created, you'll need to generate an access key and upload it to Aikido. This key will be used by Aikido to make the necessary API requests to scan your resources.\
   ​

   ![Enter GCP Project ID and upload JSON to connect GCP Artifact Registry service.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-5f030c33555a60bb34851b37a73ac947588b8871%2Faikido-scanner-for-gcp-artifact-registry_9c150fb3-cd81-4693-a5fa-2889129a2f79.png?alt=media)
5. **Completion**: Once the setup is complete, Aikido will scan the connected registry with the Aikido scanner on a nightly basis..

***
