# Cloud Load Balancing documentation  |  Google Cloud Documentation
# Source: https://docs.cloud.google.com/load-balancing/docs
# Path: /load-balancing/docs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)



# Cloud Load Balancing documentation

[Read product documentation](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)

Cloud Load Balancing allows you to put your resources behind a single IP address that is externally accessible or internal to your Virtual Private Cloud (VPC) network. 

[Go to the Cloud Load Balancing product page for more.](https://cloud.google.com/load-balancing/)

[Get started for free](https://console.cloud.google.com/freetrial)

#### Start your proof of concept with $300 in free credit

  * Develop with our latest Generative AI models and tools. 
  * Get free usage of 20+ popular products, including Compute Engine and AI APIs. 
  * No automatic charges, no commitment. 



[ View free product offers ](/free/docs/free-cloud-features#free-tier)

#### Keep exploring with 20+ always-free products.

Access 20+ free products for common use cases, including AI APIs, VMs, data warehouses, and more. 

##  Documentation resources 

Find quickstarts and guides, review key references, and get help with common issues. 

spoke 

### Load balancer types

  * [ Choose a load balancer ](/load-balancing/docs/choosing-load-balancer)

  * [ External Application Load Balancer ](/load-balancing/docs/https)

  * [ Internal Application Load Balancer ](/load-balancing/docs/l7-internal)

  * [ External passthrough Network Load Balancer ](/load-balancing/docs/network)

  * [ Internal passthrough Network Load Balancer ](/load-balancing/docs/internal)

  * [ External proxy Network Load Balancer ](/load-balancing/docs/tcp)

  * [ Internal proxy Network Load Balancer ](/load-balancing/docs/tcp/internal-proxy)




settings 

### Customize load balancers

  * [ Backend services ](/load-balancing/docs/backend-service)

  * [ Forwarding rules ](/load-balancing/docs/forwarding-rule-concepts)

  * [ Health checks ](/load-balancing/docs/health-check-concepts)

  * [ Network endpoint groups ](/load-balancing/docs/negs)

  * [ SSL certificates ](/load-balancing/docs/ssl-certificates)

  * [ SSL policies ](/load-balancing/docs/ssl-policies-concepts)

  * [ Target pools ](/load-balancing/docs/target-pools)

  * [ Target proxies ](/load-balancing/docs/target-proxies)

  * [ URL maps ](/load-balancing/docs/url-map-concepts)




group_work 

### References and resources

  * [ Load balancer features ](/load-balancing/docs/features)

  * [ API and gcloud references ](/load-balancing/docs/apis)

  * [ Pricing ](/vpc/network-pricing#lb)

  * [ Quotas and limits ](/load-balancing/docs/quotas)

  * [ Release notes ](/load-balancing/docs/release-notes)

  * [ Billing questions ](/load-balancing/docs/billing-questions)

  * [ Getting support ](/load-balancing/docs/getting-support)




##  Related resources 

Training and tutorials

Use cases

Code samples

Explore self-paced training, use cases, reference architectures, and code samples with examples of how to use and connect Google Cloud services. 

Training 

Training and tutorials

###  [ Application Load Balancer with Terraform ](https://www.cloudskillsboost.google/focuses/1206?parent=catalog)

Learn how to create an Application Load Balancer to forward traffic to a custom URL map. 

Training 

Training and tutorials

###  [ External Application Load Balancer ](https://www.cloudskillsboost.google/focuses/12007?parent=catalog)

Learn how to set up an external Application Load Balancer and how load balancing can help scale your applications on Compute Engine. 

Training 

Training and tutorials

###  [ External Application Load Balancer with Cloud Armor ](https://www.cloudskillsboost.google/focuses/1232?parent=catalog)

Learn how to configure an external Application Load Balancer with global backends, stress test the load balancer, and denylist the stress test IP address with Cloud Armor. 

Training 

Training and tutorials

###  [ Network Load Balancer ](https://www.cloudskillsboost.google/focuses/12007?parent=catalog)

Learn the differences between Network Load Balancers and Application Load Balancers and how to set them up for your applications running on Compute Engine virtual machines. 

Training 

Training and tutorials

###  [ Internal passthrough Network Load Balancer ](https://www.cloudskillsboost.google/focuses/1250?parent=catalog)

Learn how to configure and test an internal load balancer with instance groups as backends. 

Training 

Training and tutorials

###  [ Google Cloud networking 101 ](https://www.cloudskillsboost.google/catalog_lab/311)

Set up a load balanced application on Google Cloud. 

Training 

Training and tutorials

###  [ Hands on lab for hosting a web app on Compute Engine ](https://www.cloudskillsboost.google/focuses/11952?parent=catalog)

In this lab you will deploy a sample application, the "Fancy Store" ecommerce website, to show how a website can be deployed and scaled easily with Compute Engine. 

Use case 

Use cases

###  [ Request routing to a multi-region external Application Load Balancer ](/load-balancing/docs/https/setting-up-https)

Learn how to create an Application Load Balancer that selects backend services based on request URL paths, and then routes requests to backends that are close to the clients. 

multi-region load balancing

Use case 

Use cases

###  [ Use UDP with Network Load Balancers ](/load-balancing/docs/network/udp-with-network-load-balancing)

Learn how to handle User Datagram Protocol (UDP) traffic with a Network Load Balancer. 

UDP load balancing

Use case 

Use cases

###  [ Faster web performance and improved web protection for load balancing ](/load-balancing/docs/tutorials/faster-performance-improved-protection)

Learn the value of adding Cloud CDN and Google Cloud Armor to an existing external Application Load Balancer deployment. 

CDN Cloud Armor load balancing

Use case 

Use cases

###  [ Delivering HTTP and HTTPS content over the same published domain ](/load-balancing/docs/tutorials/http-https-over-same-domain)

Bind a reserved IP address to both the HTTP and HTTPS frontend configuration in the external Application Load Balancer. 

CDN load balancing

Use case 

Use cases

###  [ Optimizing application latency with load balancing ](/load-balancing/docs/tutorials/optimize-app-latency)

Learn how your choice of a specific load balancer on Google Cloud affects end-to-end latency. 

latency load balancing

Use case 

Use cases

###  [ Using load balancing for highly available applications ](/compute/docs/tutorials/high-availability-load-balancing)

Use load balancing with a regional managed instance group to redirect traffic away from busy or unavailable VM instances, allowing you to provide high availability even during a zonal outage. 

restricting incoming traffic load balancing

Code sample 

Code Samples

###  [ Global external Application Load Balancer ](https://github.com/terraform-google-modules/terraform-google-lb-http)

Create an external Application Load Balancer by using Terraform. 

Code sample 

Code Samples

###  [ External passthrough Network Load Balancer ](https://github.com/terraform-google-modules/terraform-google-lb)

Create an external passthrough Network Load Balancer by using Terraform. 

Code sample 

Code Samples

###  [ Internal passthrough Network Load Balancer ](https://github.com/terraform-google-modules/terraform-google-lb-internal)

Create an internal passthrough Network Load Balancer by using Terraform. 

##  Related videos 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-17 UTC."],[],[]] 
