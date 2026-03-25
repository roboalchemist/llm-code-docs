# Source: https://docs.envzero.com/guides/cost-monitoring/setup-azure-costs.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure Azure Costs

> Set up Azure cost monitoring in env zero using a service principal and AZ CLI

## Create a Service Principal

In order to access resources a **Service Principal** needs to be created in your Tenant.\
It is easiest to do this via the AZ CLI.

1. First, make sure you are logged in:

   ```bash  theme={null}
   az login
   ```

   Follow the instructions to login.

2. Once logged in, your subscriptions will be returned:

   ```json5  theme={null}
   [
     {
       "cloudName": "AzureCloud",
       "id": "2d7e700a-8793-45ff-ba0a-9d92d15edf56", // this is your Subscription ID
       "isDefault": "true",
       "name": "Pay-As-You-Go",
       "state": "Enabled",
       "tenantId": "e522969-635a-4327-8807-7f7aac328e82",
       "user": {
         "name": "who@outlook.com",
         "type": "user"
       }
     }
   ]
   ```

3. Next, set your active subscription:

   ```bash  theme={null}
   az account set --subscription="${id}"
   ```

4. Then create a Service Principal for env zero to be able to query your Azure costs:

   ```bash  theme={null}
   az ad sp create-for-rbac -n "${name-of-your-choice}"
   ```

   That will return the metadata for your Service Principal:

   ```json5  theme={null}
   {
     "appId": "2dc2b1b3-11dd-4eb5-845-84fc-5bda87620cea", // this is your Client ID
     "displayName": "who",
     "name": "http://who",
     "password": "ab735025-151e-4337-b154-b7833d6929a9",  // this is your Client Secret
     "tenant": "5c8c7547-dd3f-4750-a8d9-f2e04e6015ba"     // this is your Tenant ID
   }
   ```

5. Assign "Cost Management Reader" role

   ```bash  theme={null}
   az role assignment create \
     --assignee-object-id <SP_OBJECT_ID> \
     --role "Cost Management Reader" \
     --scope /subscriptions/<SUBSCRIPTION_ID>

   ```

## Add the Azure cost credentials to your Organization

1. Under your **Organization Settings**, Select the **Credentials** tab
2. Click **Add Credential**
3. Select the `Azure Credentials` type.
4. Fill in the form with the credentials from the previous steps:\
   `Client ID` = `appId` (From step 4)\
   `Client Secret` = `password` (From step 4)\
   `Tenant ID` = `tenant` (From step 4)\
   `Subscription ID` = `id` (From step 1)
5. Click **Add**

## Enable cost monitoring

1. Go to the **Project Settings** of the desired project.
2. Select the **Credentials** tab.
3. Check the appropriate cloud provider checkbox, and select the credential you created in the steps above.
4. Click **Save**.

<Warning>
  Data Visibility

  Please note that after the configuration of cost monitoring is complete, a redeploy to the environments is needed, and once redeployed it can take 24-48 hours for data to show, depending on the cloud provider's cost exploration capabilities.
</Warning>

Built with [Mintlify](https://mintlify.com).
