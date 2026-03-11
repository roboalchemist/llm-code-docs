# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations/cloud-security/azure-cloud.md

# Azure Cloud

For a description of the supported Kubernetes connection models, including direct cloud integration and Inspector-based access, see [Kubernetes Reachability](https://docs.ox.security/ox-integrations/3rd-party-integrations/cloud-security/kubernetes-reachability).

### Automatic connection instructions

1. Make sure you are logged into your Azure Portal on the correct Tenant you want to connect and that you have a \\"User Access Administrator\\" Role which is required in order to run this script.
   * You can either run the script from the Azure Portal (Cloud Shell) or locally on your machine if you have Azure CLI installed.
   * If running locally you can run the following command to log in: 'az login --tenant $TENANT\_ID --use-device-code --output none'.
2. Click the 'Download Script' button In the OX Connector window to download the script.
3. Run the downloaded script by executing \`./azure-connector.sh -t TENANT\_ID -s SUBSCRIPTION\_ID\` in the terminal. TENANT\_ID is the ID of the tenant you want to connect (this parameter is required), SUBSCRIPTION\_ID is the ID of the Subscription you want to connect (this parameter is optional, if no SUBSCRIPTION\_ID has been entered the default Subscription will be chosen).
4. Once the script completes, it will output the Client ID and Client Secret that has been created.
5. In the OX Connector fields below, enter your Tenant ID and the values you got from running the script (Client ID and Client Secret).
6. Click Connect.
7. You should receive a message that the connection was successful, if not please repeat the steps above or contact support.

○ Note - if you want to create the required assets manually please follow the instructions below.

### Manual connection Instructions

1. Log in to your Azure portal.
2. Navigate to Microsoft Entra ID → App registrations → New registration.
3. You should be in the following screen:

   <figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-e8df1f600eb59fac4329fe9678b40d97e641c221%2FScreenshot%202023-10-04%20141427.png?alt=media" alt=""><figcaption></figcaption></figure>
4. In the Register an application screen:
   * Enter a name for the application, e.g. "ox-security-connector-sp".
   * Keep the single tenant option selected in the Supported account types.
   * Click Register.
5. Note the generated values:

   <figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-10e776950bdd94f91c3a745167d3f25e19e71dae%2FScreenshot%202023-10-04%20150010.png?alt=media" alt=""><figcaption></figcaption></figure>
6. Note down the Application (client) ID and Directory (tenant) ID.
7. Navigate to Subscriptions → Your subscription → Access control (IAM) → Add → Add role assignment.
8. In the Add role assignment screen:

   * Role tab: Click the “Reader” role and then click next.

   * Members tab: Click “Select Members”, search for the app you created in step 3, click it, and then click select so it will be added.

   * Click “Review + assign”.

   > **Note:** To connect to Azure Kubernetes Service (AKS), in addition to the Reader role, assign:
   >
   > * **Azure Kubernetes Service RBAC Reader** at the subscription or cluster level.
   > * **Azure Kubernetes Service Cluster User Role** at the subscription or cluster level.
9. Navigate back to App registrations → Your app → Certificates & secrets → New client secret.
10. Enter a description for the secret and set the expiration for the desired time period (note that if the secret expires you will have to reconnect again in the OX platform) and click “Add”.
11. Note down the Value of the client secret.
12. In the Ox Connector, enter the Tenant ID, Client ID, and Client Secret.
13. Click Connect.
14. You should receive a message that the connection was successful, if not please repeat the steps above or contact support.
