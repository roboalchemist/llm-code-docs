# Source: https://docs.vespa.ai/en/basics/deploy-an-application.html.md

# Deploy an application

 

Follow these steps to deploy a Vespa application to the [dev zone](../operations/environments.html#dev)on Vespa Cloud (for free).

Alternative versions of this guide:

- [Deploy an application using pyvespa](https://pyvespa.readthedocs.io/en/latest/getting-started-pyvespa-cloud.html) - for Python developers
- [Deploy an application having Java components](deploy-an-application-java.html)
- [Deploy an application without Vespa CLI](deploy-an-application-shell.html)
- [Deploy an application locally](deploy-an-application-local.html)
- [Deploy an application having Java components locally](deploy-an-application-local-java.html)

Steps:

1. **Create a [tenant](../learn/tenant-apps-instances.html) on Vespa Cloud:**

2. **Install the [Vespa CLI](../clients/vespa-cli.html)** using [Homebrew](https://brew.sh/):

3. **Configure the Vespa client:**

4. **Get Vespa Cloud control plane access:**

5. **Clone a sample [application](applications.html):**

6. **Add a certificate for [data plane access](../security/guide#data-plane) to the application:**

7. **[Deploy](applications.html#deploying-applications) the application:**

8. **[Feed](../writing/reads-and-writes.html) [documents](../schemas/documents.html):**

9. **Run [queries](../querying/query-api.html):**

  

Congratulations, you have deployed your first Vespa application! Application instances in the [dev zone](../operations/environments.html#dev)will by default keep running for 14 days after the last deployment. You can control this in the[console](https://console.vespa-cloud.com/).

  

#### Next: [Vespa applications](applications.html)

 Copyright © 2025 - [Cookie Preferences](#)

