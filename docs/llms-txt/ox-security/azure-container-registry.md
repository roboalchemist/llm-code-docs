# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations/registry/azure-container-registry.md

# Azure Container Registry

Integrate Azure Container Registry with OX to centralize security findings alongside container, pipeline, cloud, and runtime signals already in OX.

OX scans the Azure Container Registry on a schedule and on demand, enriches findings with OX context (application mapping, workflows, and compliance), and presents a unified queue for investigation and reporting.

After you connect, Azure scan results appear in the Active issues page (use the filter **Source tool > Azure Container Registry**).

## What OX adds

* **Context and correlation**: OX maps Azure findings to applications, services, and teams to show impact and ownership.
* **Prioritization with severity factors:** OX may reprioritize scanner severities when exploitability and environment context reduce risk (for example, Critical → High). Severity factors explain why the priority changed.
* **Evidence at a glance:** When available, OX displays scanner evidence, file locations, and remediation guidance alongside OX analytics to speed triage.

## Connection Methods

For general information about connection methods, see[Connection methods](https://docs.ox.security/get-started/onboarding-to-ox/source-control/connection-methods).

Connect to OX with Azure Tenant ID, Client ID, Subscription ID, and Client Secret you create for this connection.

## Prerequisites

**OX**

* OX permission to configure connectors

**Azure Container Registry**

* Admin permissions to the Azure account you want to connect.

## Connect with Azure credentials

### Step 1: Create the credentials \[Azure]

This step has several parts.

**Register an app**

1. Verify that the [prerequisites](#prerequisites) are in place.
2. Log in to your Azure account.
3. From the Home page, use **Search** to open the Microsoft Entra ID page. Enter ‘add’ to find it.
4. From your account home page, select **+Add** and select **App registration**.<br>

   <figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-1ce1188888ffab46a26134ad8f4d7d2150a0a8e7%2FAzure%20Container%20%E2%80%93%20my%20account%20%E2%80%93%20add%20app%20reg.png?alt=media" alt=""><figcaption></figcaption></figure>
5. In **Register an application**, enter a name and ensure that the single tenant option is selected.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-0e71a262c7e8817dc020ec24f342812d77c33e61%2FAzure%20Container%20%E2%80%93%20register%20app.png?alt=media" alt=""><figcaption></figcaption></figure></div>
6. Select **Register**.
7. In the **App** screen, the Application (Client) ID and the Directory (Tenant) ID display. Save them. You’ll need them later.

**Assign roles**

1. From the header, use **Search** to locate the Subscriptions page.<br>

   <figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-481485b2e41b0ff496456d3e8a87c894fe3e8621%2FAzure%20Container%20%E2%80%93%20subscriptions%20page.png?alt=media" alt=""><figcaption></figcaption></figure>
2. Select the subscription.
3. From the Subscriptions page, select **Access Control (IAM)**.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-8b38a46b24941d4ea10944718b2aceaf5e256a20%2FAzure%20Container%20%E2%80%93%20access%20control%20IAM%20select.png?alt=media" alt=""><figcaption></figcaption></figure></div>
4. In **Access control (IAM)**, select **+Add > Role assignment**.
5. In **Add role assignment,** select the reader permission and select **Next**.
6. On the next screen, select **+Select members** and select the app from the list on the right.<br>

   <figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-369d632beb009c7260b388e55ad4af154d870f60%2FAzure%20Container%20%E2%80%93%20select%20app%20(select%20members).png?alt=media" alt=""><figcaption></figcaption></figure>
7. Select the **Select** button to continue.
8. On the next screen, select **Next**.
9. On the next screen, select **Review + assign**.This returns you to Subscription page > Access control (IAM).

**Create a client secret**

1. Use **Search** to locate the Microsoft Entra ID page.
2. From the left menu pane, select **Manage > App registration**.
3. In **App registrations**, select the app you created.<br>

   <figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-08741afb7c0c240e77875248ad47ed5be8843bb0%2FAzure%20Container%20%E2%80%93%20select%20the%20app%20you%20created.png?alt=media" alt=""><figcaption></figcaption></figure>
4. From the App registrations menu pane, select **Certificates & secrets**.\
   \
   ![](https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-71516a5bf9db0a8a8983951b13214c6031903d07%2FAzure%20Container%20%E2%80%93%20app%20select%20certificates%20%26%20secrets.png?alt=media)<br>
5. In **Certificates & secrets**, select **+ New client secret**.<br>

   <figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-bb821c83cfecb086a52428af53baafebca8cc8de%2FAzure%20Container%20%E2%80%93%20new%20client%20secret.png?alt=media" alt=""><figcaption></figcaption></figure>
6. Enter a name and expiry period.
7. Select **Add**.
8. The Secret value and Secret ID display. Copy and save them securely. You cannot view the Secret again.\
   **Best practice:** Store the token in a secrets manager and set a reminder to rotate it according to your policy.
9. Next, open the Subscription page and copy the Subscription ID.\
   You now have these four credentials:
   * Client ID
   * Tenant ID
   * Subscription ID
   * Token secret

### Step 2: Connect OX to Azure Container Registry \[OX]

1. Verify that the [prerequisites](#prerequisites) are in place.
2. In OX, go to **Connectors > Registry** and select **Azure Container Registry**.\
   \
   ![](https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-3d012f5a41aba22b256f9a3d8bcc2ee84cebf2bc%2Funknown%20\(8\)%20\(1\).png?alt=media)<br>
3. In **Configure your Azure Container Registry credentials**, select the link **CONNECTION INSTRUCTIONS** to open an online summary of the connection process.
4. Enter the parameters you created:
   * Tenant ID
   * Client ID
   * Client Secret
   * Subscription ID
5. Select **CONNECT**. OX validates the credentials.
6. In **Configure your Azure credentials**, select **VERIFY CONNECTIVITY**.\
   A green checkmark indicates a successful connection. If verification fails, check your credentials and permissions.

#### Optional configurations

* To change the images OX scans and monitors, see the section [Change the locations OX scans](#change-the-locations-ox-scans).
* To connect more Azure accounts to the same organization in the OX platform, repeat the process.
* For information on the OX Broker, see the article [OX Broker](https://docs.ox.security/get-started/onboarding-to-ox/prerequisites-and-access/ox-broker).

## Change the locations OX scans

Once you have a connection, you can change the locations that OX scans and monitors.

1. Use the **Gear** icon at the bottom of the Configuration screen.
2. OX displays the locations or objects that OX scans and monitors.
3. Change the selection as needed.
4. Select SAVE.

![](https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-1258743af4005adcc8366578f78e9576a3952305%2Funknown%20\(9\)%20\(1\).png?alt=media)<br>
