# Source: https://docs.vespa.ai/en/basics/deploy-an-application-shell.html.md

# Deploy an application without Vespa CLI

 

This lets you deploy an application to the [dev zone](../operations/environments.html#dev)on Vespa Cloud (for free).

Alternative versions of this guide:

- [Deploy an application using pyvespa](https://pyvespa.readthedocs.io/en/latest/getting-started-pyvespa-cloud.html) - for Python developers
- [Deploy an application](deploy-an-application.html)
- [Deploy an application having Java components](deploy-an-application-java.html)
- [Deploy an application locally](deploy-an-application-local.html)
- [Deploy an application with Java components locally](deploy-an-application-local-java.html)

  

**Prerequisites:**

- git - or download the files from [album-recommendation](https://github.com/vespa-engine/sample-apps/tree/master/album-recommendation)
- zip - or other tool to create a .zip file
- curl - or other tool to send HTTP requests with security credentials
- OpenSSL

Steps:

1. **Create a [tenant](../learn/tenant-apps-instances.html) on Vespa Cloud:**

2. **Clone a sample [application](applications.html):**

3. **Add a certificate for [data plane access](../security/guide#data-plane) to the application:**

4. **Create a deployable application package zip:**

5. **Deploy the application:**

6. **Verify the application endpoint:**

7. **[Feed](../writing/reads-and-writes.html) [documents](../schemas/documents.html):**

8. **Run [queries](../querying/query-api.html):**

  

Congratulations, you have deployed your first Vespa application! Application instances in the [dev zone](../operations/environments.html#dev)will by default keep running for 14 days after the last deployment. You can control this in the[console](https://console.vespa-cloud.com/).

  

#### Next: [Vespa applications](applications.html)

 Copyright © 2025 - [Cookie Preferences](#)

