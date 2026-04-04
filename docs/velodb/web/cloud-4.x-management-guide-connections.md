# Source: https://docs.velodb.io/cloud/4.x/management-guide/connections

Version: 4.x

On this page

# Connections

## Private Link​

Private Link can help you securely and stably access services deployed in
other VPCs through a private network in VPC environments, greatly simplifying
network architecture and avoiding security risks associated with accessing
services through the public network.

The VeloDB Cloud warehouse is created and run in the VeloDB VPC, and
application systems or clients within the user's VPC can access the VeloDB
Cloud warehouse across VPC via Private Link. Private Link includes two parts:
endpoint service and endpoint.

When the user needs to access VeloDB in their own private network, VeloDB
Cloud will create and manage the endpoint service, and the user creates and
manages the endpoint.

When the user needs to use VeloDB to access their own private network, they
need to create an endpoint service and register it in VeloDB Cloud.
Subsequently, VeloDB Cloud will create an endpoint to connect to the user's
endpoint service.

### Access VeloDB from Your VPC​

![Access VeloDB from Your
VPC](/assets/images/AccessVeloDBfromYourVPC-9044402274dba781c781989f2e1cd2c9.gif)

Creating a connection to allow your data applications, such as reporting,
profiling, and log analytics, within your private network to access the VeloDB
Cloud warehouse.

> **Note** There is no additional fee on the VeloDB Cloud service side, but
> users need to pay the cloud platform for endpoint instances and traffic
> fees.

#### AWS​

  1. Switch to the target warehouse, click **Connections** on the navigation bar, and click **Set up Connection** to **Connect Your VPC to VeloDB** on the **Private Link** tab to create an endpoint.

![private link ad](/assets/images/private-link-
ad-5308ac3208b4d3765739491fedc22f9b.png)

  2. The page displays the Endpoint Service information required for creating an endpoint. You can click **Set up one or more endpoints** to go to the cloud platform's Private Link product console and create an endpoint.

![private link add endpoint](/assets/images/private-link-add-
endpoint-b0011c0707c63e95567bdec58229fa99.png)

  3. On the cloud platform's Private Link product console, you need to confirm that the current region is the same as the warehouse's endpoint service (limited by the cloud platform's Private Link product) and click **Create endpoint**.

![private link create endpoint on aws](/assets/images/private-link-create-
endpoint-on-aws-19e9b1a47a9681557c82ebfdd14d13ec.png)

> **Note** You need to sign in to AWS with the principal that has been allowed
> to access the endpoint service of VeloDB Cloud, so that you can successfully
> pass the service name verification when creating the endpoint.

  4. Follow the wizard prompts to fill in the form as follows:

![private link create endpoint on aws01](/assets/images/private-link-create-
endpoint-on-aws01-78c945819bf263a4482a9ee8f5814889.png)

![private link create endpoint on aws02](/assets/images/private-link-create-
endpoint-on-aws02-1f368bf72e0c3aa9940179e50ce53d3f.png)

**Parameter**| **Description**|  Name tag| Optional. Creates a tag with a key
of 'Name' and a value that you specify.| Service category| Required. Select
the service category. The endpoint service of the VeloDB Cloud warehouse
belongs to **Endpoint services that use NLBs and GWLBs** , so click to select
it.| Service name| Required. One-click shortcut to copy the Service Name of
the endpoint service of VeloDB Cloud warehouse in the page that displays the
Endpoint Service information required for creating an endpoint, fill in the
input box and click **Verify service** .| VPC| Required. Select the VPC in
which to create your endpoint.| Subnets| Required. Select the same
Availability Zone as the one where the endpoint service of the VeloDB Cloud
warehouse is located (limited by the cloud vendor's Private Link product), and
then select an appropriate subnet ID under it.| Security groups| Required.
Select a preset security group. Note that the security rules should allow the
protocol and port used by the VeloDB Cloud warehouse, as well as the IP
address of the source where the application/client connects to the VeloDB
Cloud warehouse.| Tags| Optional. You can add tags associated with the
resource.  
---|---  
  
  5. After the endpoint is created, its status will be changed from " **Pending** " to " **Available** ", indicating that the endpoint has successfully connected with the warehouse's endpoint service.

![private link create endpoint on aws pending](/assets/images/private-link-
create-endpoint-on-aws-pending-91f5a81fe597c6d7bd66cb05f97fbec7.png)

  6. After refreshing the **Connections** page of the VeloDB Cloud warehouse, the endpoint list will display the connection information of the endpoint.

![private link endpoint list table](/assets/images/private-link-endpoint-list-
table-cafe9e613032d86472fd091b081efeea.png)

![private link endpoint on aws details](/assets/images/private-link-endpoint-
on-aws-details-d7095c7a0337d3fff859ae69af87bc4b.png)

> **Note** You need to click **Find DNS Name** to open the **Endpoint
> Details** page of AWS Private Link product console, find the **DNS Name** of
> the endpoint and use it to access the VeloDB Cloud warehouse.

  7. The application/client can access the VeloDB Cloud warehouse through the DNS name of the endpoint by MySQL protocol or HTTP protocol. For the specific connection method, refer to the pop-up bubble for **Connection Examples** .

![private link connection example](/assets/images/private-link-connection-
example-435e64f083d0f407a65a11598e96d135.png)

> **Note**
>
>   * VeloDB Cloud includes two independent account systems: One is used to
> connect to the warehouse, as described in this topic. The other one is used
> to log into the console, which is described in the [Registration and
> Login](/cloud/4.x/management-guide/user-and-organization) topic.
>
>   * For first-time connection, please use the admin username and its
> password which can be initialized or reset on the **Settings** page.
>
>

#### Azure​

  1. Switch to the target warehouse, click **Connections** on the navigation bar, and click **New Connection** to **Access VeloDB from Your VPC** on the **Private Link** tab to create an endpoint. Firstly, you need to approve a subscription to access the endpoint service of VeloDB Cloud warehouse.

![azure private link access velodb 1 1](/assets/images/azure-private-link-
access-velodb-1-1-f9cfba82e9cad6bfb73e2f60cb7718fa.png)

![azure private link access velodb 1 2](/assets/images/azure-private-link-
access-velodb-1-2-5ea71ca83159813a2649c0f22d6666ac.png)

  2. After approving a subscription to access the endpoint service, the page displays the Endpoint Service information required for creating an endpoint. You can click **Go to Create** to go to the cloud platform's Private Link product console and create an endpoint.

![azure private link access velodb 2](/assets/images/azure-private-link-
access-velodb-2-9dc52b4a46250ba905eefdf868b7fe0c.png)

  3. In the **Basics** tab of the **Create a private endpoint** page on the cloud platform's Private Link product console, you need to confirm that the current region is the same as the endpoint service of VeloDB Cloud warehouse (limited by the cloud platform's Private Link product). Follow the wizard prompts to fill in the form as follows and click **Next: Resource**.

![azure private link access velodb 3](/assets/images/azure-private-link-
access-velodb-3-453e657d9a3433175aa84303de1b14b2.png)

Parameter| Category| Description| Subscription| Project details| Required.
Select the subscription to access the endpoint service of VeloDB Cloud
warehouse. All resources in an Azure subscription are billed together.|
Resource group| Project details| Required. Select a resource group for the
private endpoint to be created in it. If there is no suitable one, you can
create a new one. A resource group is a collection of resources that share the
same lifecycle, permissions, and policies.| Name| Instance details| Required.
The instance name of the private endpoint to be created. You can customize
it.| Network Interface Name| Instance details| Required. The network interface
name of the private endpoint to be created. When you enter the instance name,
it will be automatically generated and you can modify it.| Region| Instance
details| "Required. Select the region for the private endpoint to be created
in it. Note: You need to select the region is the same as the endpoint service
of VeloDB Cloud warehouse (limited by the cloud platform's Private Link
product)."  
---|---|---  
  
  4. In the **Resource** tab of the **Create a private endpoint** page, choose the connection method **Connect to an Azure resource** with a resource ID or alias and fill in the form as follows and click **Next: Virtual Network**.

![azure private link access velodb 4](/assets/images/azure-private-link-
access-velodb-4-2d33d206e95aea48e81f401aadf9608d.png)

Parameter| Description| Resource ID or alias| Required. When connecting to
someone else's resource, they must provide you with the resource ID or alias
for that resource in order for you to initiate a connection request. In the
current scene, you can one-click shortcut to copy the **Service Alias** value
of the endpoint service of VeloDB Cloud warehouse in the page that displays
the Endpoint Service information required for creating an endpoint, then fill
in the input box.| Request message| Optional. This message will be sent to the
resource owner (This refers to VeloDB Cloud.) to assist them in the connection
management process. Don't include private or sensitive information.  
---|---  
  
  5. In the **Virtual Network** tab of the **Create a private endpoint** page, Select the virtual network and subnet for the private endpoint to be created in it. Follow the wizard prompts to fill in the form as follows and click **Next: DNS**.

![azure private link access velodb 5](/assets/images/azure-private-link-
access-velodb-5-b8d8099780eee1eef9c733ede83bf7bc.png)

Parameter| Category| Description| Virtual network| Networking| Required. Only
virtual networks in the currently selected subscription and location are
listed. Select the virtual network for the private endpoint to be created in
it. If there is no suitable one, you can create a new one on the cloud
platform's Virtual network product console.| Subnet| Networking| Required.
Only subnets in the currently selected virtual network are listed. Select a
subnet for the private endpoint to be created in it. If there is no suitable
one, you can create a new one on the cloud platform's Virtual network product
console.| Network policy for private endpoints| Networking| Optional. The
network policy for the private endpoint to be created. The default is
disabled, you can edit it.| Private IP configuration| Private IP
configuration| Optional. You can choose Dynamically allocate IP address or
Statically allocate IP address. According to the virtual network and subnet
configured above, Dynamically allocate IP address is selected by default.|
Application security group| Application security group| Optional. Select the
application security group for the private endpoint to be created. If there is
no suitable one, you can create a new one.  
---|---|---  
  
  6. In the **DNS** tab of the **Create a private endpoint** page, Keep the default settings and click **Next: Tags**.

Note: To connect privately with your private endpoint, you need a DNS record.
You need to configure the resource configuration to support Private DNS.

![azure private link access velodb 6](/assets/images/azure-private-link-
access-velodb-6-e58196b663a472d9a3835b3c3490ceed.png)

  7. In the **Tags** tab of the **Create a private endpoint** page. , Keep the default settings and click **Next: Review + create**.

Note: If you want to categorize the private endpoint and view consolidated
billing, you can configure the tag for the private endpoint to be created.

![azure private link access velodb 7](/assets/images/azure-private-link-
access-velodb-7-8c4834cd96d68943e96c3a9cd5486ee0.png)

  8. In the **Review + create** tab of the **Create a private endpoint** page, you can review the settings for the private endpoint to be created. If some settings are not as expected, you can click **Previous** back to modify. If there is no problem, you can click **Create**.

![azure private link access velodb 8](/assets/images/azure-private-link-
access-velodb-8-06865e9b6e047808b718159f3cc32b84.png)

  9. After the endpoint is created, its status will be changed from "**Created** " to "**OK** ", indicating that the endpoint has successfully connected with the endpoint service of VeloDB Cloud warehouse.

![azure private link access velodb 9 1](/assets/images/azure-private-link-
access-velodb-9-1-34cf0662dbf97d64b3b4aa971b9170d1.png)

![azure private link access velodb 9 2](/assets/images/azure-private-link-
access-velodb-9-2-b35003bfc5a86366dbaecdb10ee5de2e.png)

  10. After refreshing the **Connections** page of the VeloDB Cloud warehouse, the endpoint list will display the connection information of the endpoint.

![azure private link access velodb 10](/assets/images/azure-private-link-
access-velodb-10-004b6563bf76ab9a0659f48692b262be.png)

  11. The application/client can access the VeloDB Cloud warehouse through the IP or DNS name of the endpoint by MySQL protocol or HTTP protocol. You can click **Find DNS Name** in the endpoint list to open the details page of the endpoint to find the IP or DNS name of it.

![azure private link access velodb 11](/assets/images/azure-private-link-
access-velodb-11-13de08c12429e2a133438a5b0f2c1451.png)

  12. For the specific connection method, you can hover the pop-up bubble for **Connection Examples** in the **Connections** page of the VeloDB Cloud warehouse.

![azure private link access velodb 12](/assets/images/azure-private-link-
access-velodb-12-a383dae143082e8b495f49c31438139f.png)

### VeloDB Accesses Your VPC​

![VeloDB Accesses Your
VPC](/assets/images/VeloDBAccessesYourVPC-3f95f331da978ca2ce8b056cd7a7e33c.gif)

> **Note** The endpoint instance and traffic fees generated by VeloDB's access
> to the private network are currently not charged to users.

#### AWS​

  1. Switch to the target warehouse, click **Connections** on the navigation bar, and click **New Connection** for **VeloDB Accesses Your VPC** on the **Private Link** tab to create a connection to your endpoint service.

![private link create connection choose endpoint
service](/assets/images/private-link-create-connection-choose-endpoint-
service-c9034deb178d98da02007ea71cd3b62d.png)

![private link create connection choose endpoint service
register](/assets/images/private-link-create-connection-choose-endpoint-
service-register-8c009c34d314872005d18bdba7ff5316.png)

  2. After clicking **\+ Endpoint Service** , the pages will display the **Current Region** of the warehouse and the **ARN of VeloDB**. You can click **Go to Create** to go to the cloud platform's Private Link product console and create an endpoint service.

  3. Sign in to the AWS Console, select VPC-Endpoint services and switch to the same region as the current warehouse.

  4. Click **Create endpoint service**.

![private link create endpoint service on aws](/assets/images/private-link-
create-endpoint-service-on-aws-8753ff6a1f9f49f518910ba2798f16fb.png)

  5. On the Endpoint Service configuration page, configure the relevant parameters and click **Create**.

![private link create connection choose endpoint service
create](/assets/images/private-link-create-connection-choose-endpoint-service-
create-ec1bb1494d197a06bb0c780ab7c814e7.png)

![private link create connection choose endpoint service create
1](/assets/images/private-link-create-connection-choose-endpoint-service-
create-1-c42467af40a719bbea92b6e54d5ae9e4.png)

  6. (Optional) If there is no available network load balancer, you need to click **Create Network Load Balancer** first. After the creation is completed, click the filter button to make a selection.

![private link create connection create nlb 0](/assets/images/private-link-
create-connection-create-nlb-0-0bb75f2f55591199c4e13d5a8682f5f9.png)

![private link create connection create nlb 1](/assets/images/private-link-
create-connection-create-nlb-1-35368125db89a47f7973f2c7ac6f6ecc.png)

![private link create connection create nlb 2](/assets/images/private-link-
create-connection-create-nlb-2-7437087c61b5380d6fc23590440923d8.png)

![private link create connection create nlb 3](/assets/images/private-link-
create-connection-create-nlb-3-9098c52fbe35e426110157f924b232e3.png)

  7. (Optional) If there is no available target group, you need to click **Create Target Group** first. After the creation is completed, click the refresh button on the right to make a selection.

![private link create connection create tg 0](/assets/images/private-link-
create-connection-create-tg-0-05dc539f4a6a2f4c6946abb02012847b.png)

![private link create connection create tg 1](/assets/images/private-link-
create-connection-create-tg-1-4fa21cc341f1f0388cc082696c548016.png)

  8. After creating the endpoint service, add the **ARN of VeloDB** in the **Allow principals** Tab of the endpoint service.

![private link create connection choose endpoint service
details](/assets/images/private-link-create-connection-choose-endpoint-
service-details-7605dc4ea57d09a24f3f8e7790062788.png)

![private link create connection choose endpoint service allow
principals](/assets/images/private-link-create-connection-choose-endpoint-
service-allow-principals-2b0d3f5d4378526b1499cd6b0649fd1f.png)

  9. Copy the **Service ID** and **Service Name** from the **Endpoint Service Details** page, and fill them in the Endpoint Service registration page of VeloDB Cloud.

![private link create connection choose endpoint service
details02](/assets/images/private-link-create-connection-choose-endpoint-
service-details02-9989268d92104bf402a03784c24a04f2.png)

  10. After the registration is complete, go to the next step, specify the **Endpoint Name** of VeloDB Cloud warehouse, and click **Create Now**.

![private link create connection choose endpoint service
chosen](/assets/images/private-link-create-connection-choose-endpoint-service-
chosen-304b58524e42096a965ee5d638eca32f.png)

![private link velodb acdess user vpc new connection create
endpoint](/assets/images/private-link-velodb-acdess-user-vpc-new-connection-
create-endpoint-b94352e6b17f835d3a47e25eac051288.png)

  11. ​Accept endpoint connection request​ in the **Endpoint connections** Tab of the endpoint service.

![private link velodb acdess user vpc endpoint accept](/assets/images/private-
link-velodb-acdess-user-vpc-endpoint-
accept-f8530ef4ede58dc29fdae67fe82248fb.png)

![private link velodb acdess user vpc endpoint accept
ok](/assets/images/private-link-velodb-acdess-user-vpc-endpoint-accept-
ok-743e691ee7c593765a5de75736b1e332.png)

  12. Refresh the page and wait for the status of the endpoint of VeloDB Cloud warehouse to be changed from "pendingAcceptance" to "available", which means the connection is successful.

![private link velodb acdess user vpc endpoint
pendingacceptance](/assets/images/private-link-velodb-acdess-user-vpc-
endpoint-pendingacceptance-e5d64c866b6c2063f73e6f2c431b94a7.png)

![private link velodb acdess user vpc endpoint
available](/assets/images/private-link-velodb-acdess-user-vpc-endpoint-
available-9c00edb5993ec894c464cd91b3d107ae.png)

#### Azure​

  1. Switch to the target warehouse, click **Connections** on the navigation bar, and click **New Connection** for **VeloDB Accesses Your VPC** on the **Private Link** tab to create a connection to your endpoint service.

![azure velodb access vpc 1](/assets/images/azure-velodb-access-
vpc-1-2036a40678c0bdacff6e3a68745f2cb8.png)

  2. After clicking **\+ Endpoint Service** , the page will display the **Current Region** of the warehouse and the **Subscription ID of VeloDB**. You can click **Go to Create** to go to the cloud platform's Private Link product console and create an endpoint service (This refers to Azure private link service).

![azure velodb access vpc 2](/assets/images/azure-velodb-access-
vpc-2-15342d65dd4309de1b03fdebfe11b7b9.png)

  3. Sign in to the **[Azure portal](https://portal.azure.com/)** with your Azure account. In the **Basics** tab of the **Create private link service** page on the Private Link product console, you need to confirm that the region is the same as the VeloDB Cloud warehouse (limited by the cloud platform's Private Link product). Follow the wizard prompts to fill in the form as follows and click **Next: Outbound settings**.

![azure velodb access vpc 3](/assets/images/azure-velodb-access-
vpc-3-a8c0d23849f7e98e333691c25e07b35f.png)

Parameter| Category| Description| Subscription| Project details| Required.
Select the subscription to create the private link service for database or
datalake. All resources in an Azure subscription are billed together.|
Resource group| Project details| Required. Select a resource group for the
private link service to be created in it. If there is no suitable one, you can
create a new one. A resource group is a collection of resources that share the
same lifecycle, permissions, and policies.| Name| Instance details| Required.
The instance name of the private link service to be created. You can customize
it.| Region| Instance details| Required. Select the Azure region for the
private link service to be created and located in it.Note: You need to select
the region is the same as the VeloDB Cloud warehouse (limited by the cloud
platform's Private Link product).  
---|---|---  
  
  4. In the **Outbound settings** tab of the **Create private link service** page. Follow the wizard prompts to fill in the form as follows and click **Next: Access Security**.

![azure velodb access vpc 4](/assets/images/azure-velodb-access-
vpc-4-94adfa01b8a961ee99f0be5436c1302b.png)

Parameter| Description| Load balancer| Required. Select a load balancer behind
the private link service to load balances database or datalake. If there is no
suitable one, you can create a new one on the cloud platform's Load Balancer
product console.| Load balancer frontend IP address| Required. Select frontend
IP address of the load balancer you selected above.| Source NAT Virtual
network| Required.| Source NAT subnet| Required.| Enable TCP proxy V2|
Required. Leave the default of No. If your application expects a TCP proxy v2
header, select Yes.| Private IP address settings| Leave the default settings  
---|---  
  
  5. In the **Access Security** tab of the **Create private link service** page, you need to choose **Restricted by subscription** for whom can request access to the private link service, and add the **Subscription ID of VeloDB** into the access whitelist of the private link service and choose **Yes** for auto-approve. Then click **Next: Tags**.

![azure velodb access vpc 5](/assets/images/azure-velodb-access-
vpc-5-12901ac888fbbb41ad1836dae2434ed6.png)

  6. In the **Tags** tab of the **Create private link service** page, keep the default settings and click **Next: Review + create**. Note: If you want to categorize the private link service and view consolidated billing, you can configure the tag for the private link service to be created.

![azure velodb access vpc 6](/assets/images/azure-velodb-access-
vpc-6-728b40c08e93abd61d084586db5f50a1.png)

  7. In the **Review + create** tab of the **Create private link service** page, you can review the settings for the private link service to be created. If some settings are not as expected, you can click **Previous** back to modify. If there is no problem, you can click **Create**.

![azure velodb access vpc 7](/assets/images/azure-velodb-access-
vpc-7-50fe955adb6152f225b4e524d61f9f9c.png)

  8. After the private link service is created, its status will be changed from "**Created** " to "**OK** ", indicating that the private link service has ready to be connected by the private endpoint of VeloDB Cloud warehouse.

![azure velodb access vpc 8](/assets/images/azure-velodb-access-
vpc-8-0ad8e3492cc64efb28e4bf0f30ae1d53.png)

![azure velodb access vpc 8 2](/assets/images/azure-velodb-access-
vpc-8-2-301315bd076b2c8872a877baca232e2c.png)

  9. After creating the private link service, copy the **Rescource ID** and **Alias** from the private link service **Details** page, and fill them in the Endpoint Service registration page of VeloDB Cloud.

![azure velodb access vpc 9 1](/assets/images/azure-velodb-access-
vpc-9-1-ebb8740fc6e0aa9aad2fc08f6ab52e8e.png)

![azure velodb access vpc 9 2](/assets/images/azure-velodb-access-
vpc-9-2-03179ffc1a27a7fb357749a5b538086c.png)

![azure velodb access vpc 9 3](/assets/images/azure-velodb-access-
vpc-9-3-518ed394ddccc66f08dd885bb12b6948.png)

  10. After the registration is complete, go to the next step, specify the **Endpoint Name** of VeloDB Cloud warehouse, and click **Create Now**.

![azure velodb access vpc 10 1](/assets/images/azure-velodb-access-
vpc-10-1-a3716547db46d049cffffda5b08937c4.png)

![azure velodb access vpc 10 2](/assets/images/azure-velodb-access-
vpc-10-2-3cca22bfc176e4513941fc05380615ba.png)

  11. Refresh the page and wait for the status of the endpoint of VeloDB Cloud warehouse to be changed from "**pendingAcceptance** " to "**Approve** ", which means the connection is successful.

![azure velodb access vpc 11 1](/assets/images/azure-velodb-access-
vpc-11-1-18047ac80c56fafd9138eb61a5166f16.png)

![azure velodb access vpc 11 2](/assets/images/azure-velodb-access-
vpc-11-2-9d0cbfd185f0dde8dec73ad0a4089679.png)

## Public Link​

On the **Connections** page, switch to the **Public Link** tab to manage the
public network connection.

### Add IP Whitelist​

In order to access the VeloDB Cloud warehouse via the public network, you need
to add the source public network IP address to the whitelist.

Click **IP Whitelist Management** on the right of the **Connect Warehouse**
card to add the source IP addresses or segments.

![public link](/assets/images/public-
link-6b95eb428f3ce8d1b9bfcd1fc4084fb3.png)

![public link ip whitelist](/assets/images/public-link-ip-
whitelist-40498cfa0943672f009fb66c31d213d5.png)

In the IP whitelist, you can add or delete IP addresses to enable or disable
their access to the warehouse.

> **Note** By default, the IP segment 0.0.0.0/0 is set, which means the
> warehouse is completely open to the public network. It is recommended to
> remove it in time after use to reduce security risks.

### Access Warehouse​

After adding the source public network IP address to the whitelist, you can
click **WebUI Login** to access the VeloDB Cloud warehouse through the public
network. For the specific connection method, please refer to the **Other
Methods**.

![public link connect warehouse methods](/assets/images/public-link-connect-
warehouse-methods-a71e78dcefb8fb020be24c5670be342a.png)

On This Page

  * Private Link
    * Access VeloDB from Your VPC
    * VeloDB Accesses Your VPC
  * Public Link
    * Add IP Whitelist
    * Access Warehouse

