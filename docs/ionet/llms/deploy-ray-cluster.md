# Source: https://io.net/docs/guides/clouds/deploy-ray-cluster.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy Ray Cluster

> This document explains how to deploy a Ray cluster by leveraging compute power in io.net's DePIN network.

## Payments

IO Cloud customers can load their io.net account prior to deploying clusters, or they can pay at the end of the deploy process. The main two ways to pay for clusters is using Solana and credit cards. To use Solana, you must set up a wallet. This can be done when you register your account or later in **Account Settings**.

To learn more about the types of payments we offer and step-by-step guides, see [IO Cloud Payments](/guides/payment/io-cloud-payments).

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/opWBPu98iR4" title="Deploy Ray Cluster on IO Cloud" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

## Configure Cluster

### 1. Create Cluster

Select Ray from the Cluster menu.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7be3fe5c51a8696d5933b951897f4b8bee94387cce8aa1d73c2bd54df2b793e9-Ray1.jpg?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=b6399bf9232bbb430760abc39bc8ef05" alt="" className="mx-auto" style={{ width:"49%" }} data-og-width="1082" width="1082" data-og-height="1288" height="1288" data-path="images/docs/7be3fe5c51a8696d5933b951897f4b8bee94387cce8aa1d73c2bd54df2b793e9-Ray1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7be3fe5c51a8696d5933b951897f4b8bee94387cce8aa1d73c2bd54df2b793e9-Ray1.jpg?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=a636a55333b1ad280c027b55d853069f 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7be3fe5c51a8696d5933b951897f4b8bee94387cce8aa1d73c2bd54df2b793e9-Ray1.jpg?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=0a5bcfca6a67c397d35b918be8eccbee 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7be3fe5c51a8696d5933b951897f4b8bee94387cce8aa1d73c2bd54df2b793e9-Ray1.jpg?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=83ea96264a8c29ccebe5249299f33775 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7be3fe5c51a8696d5933b951897f4b8bee94387cce8aa1d73c2bd54df2b793e9-Ray1.jpg?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=389005f6fb9342b252ce6b520906b9bd 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7be3fe5c51a8696d5933b951897f4b8bee94387cce8aa1d73c2bd54df2b793e9-Ray1.jpg?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=e79a62bbd4836013179e367a650a1f02 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7be3fe5c51a8696d5933b951897f4b8bee94387cce8aa1d73c2bd54df2b793e9-Ray1.jpg?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=93c1182b16d67e312e6704bad956dec4 2500w" />
</Frame>

### 2. Select Cluster Type

Select the cluster type that meets the scope of your project.

* **General** - This option works well for prototyping or general E2E workloads.
* **Inference** - Choose if you require production-ready clusters for low-latency inference and heavy workloads.
* **Train** - Choose if you require production-ready clusters for machine learning models, training, and fine-tuning.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c35726eb588c50a0ed8ba435617b98b29b97096e364fc861a5da644eb22d2a9b-Bitmap2.jpeg?fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=d209df593f5de323dee6a4f3ba734efe" alt="" className="mx-auto" style={{ width:"68%" }} data-og-width="1484" width="1484" data-og-height="1220" height="1220" data-path="images/docs/c35726eb588c50a0ed8ba435617b98b29b97096e364fc861a5da644eb22d2a9b-Bitmap2.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c35726eb588c50a0ed8ba435617b98b29b97096e364fc861a5da644eb22d2a9b-Bitmap2.jpeg?w=280&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=11c7f507a968601e517562e8497631db 280w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c35726eb588c50a0ed8ba435617b98b29b97096e364fc861a5da644eb22d2a9b-Bitmap2.jpeg?w=560&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=5e9b08c3dffbec859983681dabc27f91 560w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c35726eb588c50a0ed8ba435617b98b29b97096e364fc861a5da644eb22d2a9b-Bitmap2.jpeg?w=840&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=cfa6aa9d625de8db39220cb9aa20ecc9 840w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c35726eb588c50a0ed8ba435617b98b29b97096e364fc861a5da644eb22d2a9b-Bitmap2.jpeg?w=1100&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=03c1b6fb6944321dee031378cf81e27b 1100w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c35726eb588c50a0ed8ba435617b98b29b97096e364fc861a5da644eb22d2a9b-Bitmap2.jpeg?w=1650&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=80a5d9d6faeb81040b64f37dea9affe8 1650w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c35726eb588c50a0ed8ba435617b98b29b97096e364fc861a5da644eb22d2a9b-Bitmap2.jpeg?w=2500&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=dd5041f1b02ee3d005617e6680f4631f 2500w" />
</Frame>

### 3. Rename Cluster

Click the pencil icon to the right of the name to rename your cluster. In the screenshot below, the icon is highlighted in the blue box. Provide a unique name for your cluster.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/eb660e1-rename.png?fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=6db91ef0a9b6bca3bb67f42c1cb444a1" alt="" className="mx-auto" style={{ width:"75%" }} data-og-width="1776" width="1776" data-og-height="202" height="202" data-path="images/docs/eb660e1-rename.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/eb660e1-rename.png?w=280&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=ffdcb83fa805d2c9955ff380533f1226 280w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/eb660e1-rename.png?w=560&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=4662f6b161678a36d666a9493c9dfd84 560w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/eb660e1-rename.png?w=840&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=1f3d4da838786a4e52194fb96fb33daa 840w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/eb660e1-rename.png?w=1100&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=cf823e31bfa9536ba6ee0091ef5952ba 1100w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/eb660e1-rename.png?w=1650&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=1a5b4025b8f8c98628fdd0ce79ca66a4 1650w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/eb660e1-rename.png?w=2500&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=e7bfd400f4f12954f7f893d5bcdafa26 2500w" />
</Frame>

Click **Next Step**.

### 4. Security Compliance

Select the level and type of security for your cluster.

* **E2E Encrypted** - A method of secure communication that prevents bad actors from accessing data while it's transferred. It restricts data access to the sender and recipient. All data traffic between GPUs is encrypted.
* **SOC2/HIPAA** - (Coming Soon) A framework for managing and securing data related to technology and cloud computing services. All data traffic between GPUs is encrypted.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8a79ab3-sec_com.png?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=40b333b453f6092ba3eab0684e805114" alt="" className="mx-auto" style={{ width:"78%" }} data-og-width="1456" width="1456" data-og-height="548" height="548" data-path="images/docs/8a79ab3-sec_com.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8a79ab3-sec_com.png?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=90c9d905afa9ab7e98a59d11a4d22e98 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8a79ab3-sec_com.png?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=a841b44cabd4d95db343321ee002fa10 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8a79ab3-sec_com.png?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=aada582d46c6cc3ce26a97e318712e96 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8a79ab3-sec_com.png?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=5291974bd15fde685cf5b16213eb02f4 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8a79ab3-sec_com.png?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=e2d505f9ad38cbc9cc610a0da818674d 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8a79ab3-sec_com.png?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=46d75d88e6ef3afed9e54a40dbaa5a3d 2500w" />
</Frame>

Click **Next Step**.

### 5. Location

To select a location for our GPUs, enter a country name in the Search field or browse the country list (screenshot below is truncated). You can select multiple locations. Residents of countries with strict data residency can use this option to meet those requirements.

<Info>
  One reason to select a specific location is to reduce latency. If you're located in USA and select USA for location, then your clients can get results more quickly if, for example, your GPUs are inferencing.
</Info>

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/23f3bce-ray_location.png?fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=c297c94ecbc573200a45e555b51192d9" alt="" className="mx-auto" style={{ width:"71%" }} data-og-width="1358" width="1358" data-og-height="686" height="686" data-path="images/docs/23f3bce-ray_location.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/23f3bce-ray_location.png?w=280&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=2186eb52fe69860fb9f39f7c93a85abb 280w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/23f3bce-ray_location.png?w=560&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=ddd7736f72edcbbaf29c3633398be4a1 560w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/23f3bce-ray_location.png?w=840&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=210b3d4b22410582e0d8a50843e137a2 840w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/23f3bce-ray_location.png?w=1100&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=f32801d466e778d181c5f17d3c7dd503 1100w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/23f3bce-ray_location.png?w=1650&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=83ce11a8726a393cc08e4ca5624ef566 1650w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/23f3bce-ray_location.png?w=2500&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=1a7eab046d8c835febf2061befac197a 2500w" />
</Frame>

Click **Next Step**.

### 6. Connectivity Tiers

Select the connectivity speed for your project.

* **Ultra High Speed** - Download 1600 MB/s / 1200 MB/s Upload
* **High Speed** - Download 800 MB/s / 600 MB/s Upload
* **Medium** - Download 400 MB/s / 300 MB/s Upload
* **Low Speed** - Download 100 MB/s / 10 MB/s Upload

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/2991dc1-connect_ray.png?fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=b85d507ed660d961265d2aaf825d3e26" alt="" className="mx-auto" style={{ width:"78%" }} data-og-width="1400" width="1400" data-og-height="766" height="766" data-path="images/docs/2991dc1-connect_ray.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/2991dc1-connect_ray.png?w=280&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=9f6ce7d7053f3d4b384e35fb0b3d00d1 280w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/2991dc1-connect_ray.png?w=560&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=1e69211d7160c5a621e02ef91c17ae6c 560w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/2991dc1-connect_ray.png?w=840&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=f4d2cd95b3cae8ef3c1bd58be0789492 840w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/2991dc1-connect_ray.png?w=1100&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=55beb6b3920dc2c01a8a0ea6b24fa4af 1100w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/2991dc1-connect_ray.png?w=1650&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=48ef2d0fae96ec0800a4137773083c42 1650w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/2991dc1-connect_ray.png?w=2500&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=a5f4f1466e571a5b6d214841cd46691c 2500w" />
</Frame>

Click **Next Step**.

### 7. Select GPUs

Select the type of computing your project requires, **GPU** or **CPU**.

* If you select GPU, also select NVIDIA and browse for the model that satisfies your requirements.
* If you select CPU, you can choose between Apple of AMD CPUs.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/2507166-ray_clus_select.png?fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=09be8c9bd502c1965de5f138af7fadf5" alt="" className="mx-auto" style={{ width:"75%" }} data-og-width="1366" width="1366" data-og-height="842" height="842" data-path="images/docs/2507166-ray_clus_select.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/2507166-ray_clus_select.png?w=280&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=35ca5d4cd38ccdb4f7065b436117602c 280w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/2507166-ray_clus_select.png?w=560&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=3d8188fef9676f5e8fe5438c3074250e 560w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/2507166-ray_clus_select.png?w=840&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=c2a163b475328473c913a253fbd8f93a 840w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/2507166-ray_clus_select.png?w=1100&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=8b424c64192be6fcea2f3b77de4d680b 1100w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/2507166-ray_clus_select.png?w=1650&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=8eefb253ccbf9a4ab6342d6474d3b95c 1650w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/2507166-ray_clus_select.png?w=2500&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=303d53e671f3a06276de0414b7543f3c 2500w" />
</Frame>

Click **Next Step**.

### 8. Cluster Base Image

Ray is the only selection for now. We will release additional cluster base images soon such as:

* IOG
* Ludwig
* Pytorch FSDP
* Unreal Engine 5
* Unity Streaming

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/67a82eda17320fe5cd529db6bc82da5071188c4aa556096236702b858512991d-Bitmap.jpg?fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=1bcefecc905ee3824e45c72b79255b95" alt="" className="mx-auto" style={{ width:"77%" }} data-og-width="1467" width="1467" data-og-height="789" height="789" data-path="images/docs/67a82eda17320fe5cd529db6bc82da5071188c4aa556096236702b858512991d-Bitmap.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/67a82eda17320fe5cd529db6bc82da5071188c4aa556096236702b858512991d-Bitmap.jpg?w=280&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=ab5c4c9f4d044419c6e096dbb4024515 280w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/67a82eda17320fe5cd529db6bc82da5071188c4aa556096236702b858512991d-Bitmap.jpg?w=560&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=681532f7537598742aeb89ea87959400 560w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/67a82eda17320fe5cd529db6bc82da5071188c4aa556096236702b858512991d-Bitmap.jpg?w=840&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=7a19b518914875b78d0ae29feef95eed 840w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/67a82eda17320fe5cd529db6bc82da5071188c4aa556096236702b858512991d-Bitmap.jpg?w=1100&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=fa62a59dad5926eaa8bb1375b7d70346 1100w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/67a82eda17320fe5cd529db6bc82da5071188c4aa556096236702b858512991d-Bitmap.jpg?w=1650&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=bcbe300a3fb3e8006029e5d074836636 1650w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/67a82eda17320fe5cd529db6bc82da5071188c4aa556096236702b858512991d-Bitmap.jpg?w=2500&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=5a81a0b7429be54406866c4d58d48bbb 2500w" />
</Frame>

Click **Next Step**.

### 9. Master Configuration

All clusters include a preconfigured master node. These nodes are selected by io.net from reliable and security compliant data centers.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/78bc942-ray_ms_config.png?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=9c43542de54a542e1047eb84fc7f9ced" alt="" className="mx-auto" style={{ width:"76%" }} data-og-width="1446" width="1446" data-og-height="1248" height="1248" data-path="images/docs/78bc942-ray_ms_config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/78bc942-ray_ms_config.png?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=cf00d4895ff68d2cd00fe7ef6715fdd8 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/78bc942-ray_ms_config.png?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=5e35ea45de022649dc6e8e9fd7518fe5 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/78bc942-ray_ms_config.png?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=bcaf593927ffa1b54727defafa7c32a4 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/78bc942-ray_ms_config.png?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=ee5f40f7c8519ca643cbb1b61144cc2b 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/78bc942-ray_ms_config.png?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=b0c2520e4c2efa76af76b79aa56960dc 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/78bc942-ray_ms_config.png?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=bbab525109375b15924cdb66e5516699 2500w" />
</Frame>

Click **Next Step**.

### 10. Summary

On the Summary page, the choices you made in the process are displayed. You must select the number of GPUs and the duration of time that you will use them.

1. In the **Enter GPUs Quantity** field, select the number of GPUs in the dropdown. 2 GPUs will increase the cost.
2. In the **Enter Duration** field, select the length of time: Hourly, Daily, or Weekly. To the right, you can increase the quantity.
3. Review all the details of your cluster, including the **Total Cost**.
4. Click **Deploy Cluster**.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/3142dc3-fees1.png?fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=e3a253b6257f96c593c4b1d6a1aae112" alt="" className="mx-auto" style={{ width:"66%" }} data-og-width="1450" width="1450" data-og-height="1852" height="1852" data-path="images/docs/3142dc3-fees1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/3142dc3-fees1.png?w=280&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=396386802a4aa5d84799efa88b22d13b 280w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/3142dc3-fees1.png?w=560&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=b5ea786e0d3950a5af36929a256e1754 560w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/3142dc3-fees1.png?w=840&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=ff710b7a183b370ecc96ecae7f3462f9 840w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/3142dc3-fees1.png?w=1100&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=b0ccebf287b79d7a39d0b465f66562cb 1100w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/3142dc3-fees1.png?w=1650&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=4c570f5622dff125763e31bc69e72822 1650w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/3142dc3-fees1.png?w=2500&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=61d19e5a74659ce5d7a3942c1eb53b7b 2500w" />
</Frame>

### View Cluster

After payment is processed you can view your cluster loading.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/b30fc8f-Cluster_load.png?fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=06a1fa498f6a29f8a077ca73463074bd" alt="" data-og-width="2450" width="2450" data-og-height="722" height="722" data-path="images/docs/b30fc8f-Cluster_load.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/b30fc8f-Cluster_load.png?w=280&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=a81e774f485379b2711442eea27d2fef 280w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/b30fc8f-Cluster_load.png?w=560&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=561a70f206152f6a4d1604ec8b23a974 560w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/b30fc8f-Cluster_load.png?w=840&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=fb7242da3ba926b9142d91f385abbc04 840w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/b30fc8f-Cluster_load.png?w=1100&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=2229a7df82e0f4667666a337135adccb 1100w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/b30fc8f-Cluster_load.png?w=1650&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=24968062e0fefa99d3ba656ba8f88200 1650w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/b30fc8f-Cluster_load.png?w=2500&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=5f117d547157e58ad342340d6643a0c4 2500w" />
</Frame>

Click **Return to Clusters** after your cluster is successfully deployed. The screenshot below is a detail page of your cluster.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/72c4867-view_cluster2.png?fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=eac5df75045f2d47a80f912ce94231ca" alt="" data-og-width="2604" width="2604" data-og-height="2498" height="2498" data-path="images/docs/72c4867-view_cluster2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/72c4867-view_cluster2.png?w=280&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=f2e59d24aae1cb3bccdb389f2da47acf 280w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/72c4867-view_cluster2.png?w=560&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=490c63a6ab56da00c9ee4d0bcfa73be7 560w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/72c4867-view_cluster2.png?w=840&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=c1bf595bec8b89b56fdfacefecaeb791 840w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/72c4867-view_cluster2.png?w=1100&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=e687102442e8258128bef6ddee6517ac 1100w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/72c4867-view_cluster2.png?w=1650&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=1150a683c1211be67ad96039f01c3bb7 1650w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/72c4867-view_cluster2.png?w=2500&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=8bb04e6954e67dc972cef50f75afc1b1 2500w" />
</Frame>
