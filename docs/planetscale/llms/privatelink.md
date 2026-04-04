# Source: https://planetscale.com/docs/vitess/managed/aws/privatelink.md

# Set up AWS PrivateLink with PlanetScale Managed

> PlanetScale Managed can connect you to your databases via [AWS PrivateLink](https://aws.amazon.com/privatelink/). The following guide describes how PlanetScale Managed with AWS PrivateLink works and how to set it up.

## Overview

If you are on a Scaler Pro plan and would like to set up AWS PrivateLink, see our [Private connections documentation](/docs/vitess/connecting/private-connections).

## How PlanetScale Managed and AWS PrivateLink work

AWS PrivateLink requires two components:

* A [VPC endpoint service](https://docs.aws.amazon.com/vpc/latest/privatelink/endpoint-service-overview.html) deployed in the AWS Organizations member account that PlanetScale controls.
* A [VPC endpoint interface](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html), sometimes referred to as a "VPC endpoint" in AWS, deployed in the account that your applications operate in.

Once both components are operating correctly, the EC2 instances in the VPC that the VPC endpoint has been assigned to will leverage [Private DNS](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#vpce-private-dns) to connect to your VPC endpoint instead of the publicly accessible endpoint.

The connection strings that PlanetScale provides will operate successfully inside and outside your VPC, creating PrivateLink connections inside of your VPC and regular connections outside of your VPC.

## Step 1: Initiating the setup process

There is no fully automated way to establish a PrivateLink connection. If you would like to initiate the process, please get in touch with your Solutions Engineer and let them know the [AWS Account ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html) that you intend to create the [VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html) in.

Once they receive your AWS Account ID and forward it to the team responsible for provisioning your deployment, the team will provide the Solutions Engineer (and ultimately you) with the Service Name of the [VPC endpoint service](https://docs.aws.amazon.com/vpc/latest/privatelink/endpoint-service-overview.html) that will be responsible for accepting your connection.

<Note>
  It is important to keep the service name in your records. It is the only piece of information you need to input when creating your VPC endpoint.
</Note>

## Step 2: Establishing a VPC endpoint connection

<Warning>
  Only proceed to the next steps once a PlanetScale Solutions Engineer has provided the service name and confirmed cross-account authentication has been configured.
</Warning>

The following steps are an example of establishing a VPC endpoint connection in the AWS Console. In this example, the customer has requested that their deployment be in the `eu-west-1` region.

When you go through the steps, make sure that you have selected the region that matches the region that your PlanetScale Managed cluster deployment has been provisioned into.

<Steps>
  <Step>
    Navigate to the Endpoints section on the Virtual Private Cloud page and select "**Create Endpoint**."

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/nav_to_splash.png?fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=410a8cc156a78a51d8e5f8ea48a78643" alt="nav_to_splash" data-og-width="1572" width="1572" data-og-height="1090" height="1090" data-path="docs/images/assets/docs/managed/aws/privatelink/nav_to_splash.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/nav_to_splash.png?w=280&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=b5ac93ebfdc41198a7a0a1cef542348d 280w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/nav_to_splash.png?w=560&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=e62c2706799fb13f22008dde7a3d1714 560w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/nav_to_splash.png?w=840&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=d5da2ea8fabc40805aa7bfcd26fdad2f 840w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/nav_to_splash.png?w=1100&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=e29d28e4406495aa718adac5ee86976d 1100w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/nav_to_splash.png?w=1650&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=1201e6dae57dc8a8cfba3fdeb2438523 1650w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/nav_to_splash.png?w=2500&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=08ec647abfea620358d53f7cc9de5a4d 2500w" />
    </Frame>
  </Step>

  <Step>
    Select the "**Find service by name**" selector, input the provided Service Name, and select the "**Verify**" button.

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/verified.png?fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=9fc8c13b137c6316427fbd7386bbed5b" alt="verified" data-og-width="996" width="996" data-og-height="650" height="650" data-path="docs/images/assets/docs/managed/aws/privatelink/verified.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/verified.png?w=280&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=a112f9dbf7fa47fa30a1c271d41ce1b3 280w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/verified.png?w=560&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=811903960eb22be2519097ab702fdb79 560w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/verified.png?w=840&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=078ca796d8f3967f2cda0faa9e8ef133 840w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/verified.png?w=1100&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=2c0ee8d9a3dfed3f0c74c0ff796e1bb5 1100w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/verified.png?w=1650&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=969b2d29bcad6224189b7bb7423ed43c 1650w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/verified.png?w=2500&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=0904bea0888bae224575eba102bbf52f 2500w" />
    </Frame>
  </Step>

  <Step>
    Select the VPC in the drop-down where you wish to provision this VPC endpoint and the relevant subnets inside your VPC.

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/cyo_vpc.png?fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=7c83fac18a4586b519ceac3de61cba6b" alt="cyo_vpc" data-og-width="1274" width="1274" data-og-height="548" height="548" data-path="docs/images/assets/docs/managed/aws/privatelink/cyo_vpc.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/cyo_vpc.png?w=280&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=dfa500fe0bca2819e6f780dedde981aa 280w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/cyo_vpc.png?w=560&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=bf772e5f881647fe1d1299b76b68cef9 560w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/cyo_vpc.png?w=840&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=5789eda2e4fbe18b34c2fbcf10926bb1 840w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/cyo_vpc.png?w=1100&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=14f22d02e7f597c0f309fb7c84f11a31 1100w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/cyo_vpc.png?w=1650&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=d5401b743509e15e12fa4144d6645790 1650w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/cyo_vpc.png?w=2500&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=1ee58d0ac57df6d6d8c0495956e88d8b 2500w" />
    </Frame>
  </Step>

  <Step>
    Select the "**Enable DNS Name**" checkbox. Take note of the value of your "**Private DNS Name**" field. That is how we will verify that the connection is operating successfully.

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/enable_dns_name.png?fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=5076b63698f59daff686dea822ed84fd" alt="enable_dns_name" data-og-width="966" width="966" data-og-height="438" height="438" data-path="docs/images/assets/docs/managed/aws/privatelink/enable_dns_name.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/enable_dns_name.png?w=280&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=e40f181d7aa32649c2956d1a8776cafb 280w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/enable_dns_name.png?w=560&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=eeea9704de4430e098f226dfee20ce27 560w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/enable_dns_name.png?w=840&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=e64ad338e8787ce8b92849db48408f91 840w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/enable_dns_name.png?w=1100&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=fdaf45c01259dfb65249ac5459fc36c6 1100w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/enable_dns_name.png?w=1650&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=9168612958492030b7e2d608524e2436 1650w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/enable_dns_name.png?w=2500&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=12ae8174c2ea21d94cec152997d3fb97 2500w" />
    </Frame>
  </Step>

  <Step>
    Select the relevant Security Groups you want your VPC endpoint to adhere to.

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/select_sgs.png?fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=77fa4fc01f3426cc2061917468bfc018" alt="select_sgs" data-og-width="1654" width="1654" data-og-height="726" height="726" data-path="docs/images/assets/docs/managed/aws/privatelink/select_sgs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/select_sgs.png?w=280&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=9da44222e7be9b41a260c511c4c1be0f 280w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/select_sgs.png?w=560&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=5007ad5420a2c81308baaae4b981f581 560w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/select_sgs.png?w=840&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=3bc65832787751cbfb4cef2fa6e9e34e 840w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/select_sgs.png?w=1100&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=3d6ed64b1ee79fd95ecbf95afd75cc04 1100w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/select_sgs.png?w=1650&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=5791657e835a772fb75d60d6a8fae37a 1650w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/select_sgs.png?w=2500&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=d28da7cfe21579e80698f183b6d629b8 2500w" />
    </Frame>
  </Step>

  <Step>
    Add as many tags as your heart desires (up to 50) and select "**Create endpoint**."

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/click_it.png?fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=166bab6ba2d78b66b7e1af9263e176ac" alt="click_it" data-og-width="1226" width="1226" data-og-height="412" height="412" data-path="docs/images/assets/docs/managed/aws/privatelink/click_it.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/click_it.png?w=280&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=6abcefddababd2a0360a63502e7444c7 280w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/click_it.png?w=560&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=cc3e5f7e2896ff32eeef541d3e65791b 560w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/click_it.png?w=840&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=ffff1430be432c2d637671bce1bcd522 840w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/click_it.png?w=1100&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=283a0ec0e315c96d32def3b63f052f8c 1100w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/click_it.png?w=1650&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=286070e9498b13efecf8c49e26cc7d69 1650w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/click_it.png?w=2500&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=b23a5cf96045ceeaed859c268ed3a4af 2500w" />
    </Frame>
  </Step>

  <Step>
    The "Creating" spinner will spin momentarily and then deliver you the news of the endpoint creation. You should see a VPC endpoint in the `pending` state if it was successful. If the creation failed, record the reason and consult your Solutions Engineer.

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/pending.png?fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=eb05aa70bcff44fdaab0bd6e9c208abe" alt="pending" data-og-width="740" width="740" data-og-height="240" height="240" data-path="docs/images/assets/docs/managed/aws/privatelink/pending.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/pending.png?w=280&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=19aea33d536adf90f9d08b0a28b4f662 280w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/pending.png?w=560&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=fb09861e3d2a522927f3d6cb3e6fe727 560w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/pending.png?w=840&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=98c7a5e21556f6b58e8159c33675b5b5 840w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/pending.png?w=1100&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=c2bede53482994d46ae12065fe790264 1100w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/pending.png?w=1650&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=10c582399a04b04efc22a0596cd408a0 1650w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/pending.png?w=2500&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=99e6c2855c127163eda8b972140d89a2 2500w" />
    </Frame>
  </Step>

  <Step>
    After 2-10 minutes (make sure to refresh), your VPC endpoint will report an `available` state.

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/available.png?fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=3653f9ed7f50fe9c27bd2a796e3078dd" alt="available" data-og-width="766" width="766" data-og-height="210" height="210" data-path="docs/images/assets/docs/managed/aws/privatelink/available.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/available.png?w=280&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=4ef5fe4b690fc9879b34d4a080333d6d 280w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/available.png?w=560&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=f884cea3db162cfca24e08e538167d35 560w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/available.png?w=840&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=5d20504baaa97fd2a057b94c10b3931d 840w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/available.png?w=1100&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=c8489f7c25e7a3a1b8432558e12cd598 1100w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/available.png?w=1650&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=776db12391e5ca1c516b424d6493cff4 1650w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/managed/aws/privatelink/available.png?w=2500&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=b8f805c01c9bdcf4e68ff2848570a831 2500w" />
    </Frame>
  </Step>
</Steps>

## Step 3: Verifying a VPC endpoint connection

PlanetScale publishes a [wildcard DNS record](https://en.wikipedia.org/wiki/Wildcard_DNS_record) for your private region. AWS PrivateLink will override the DNS record in your VPC to point to your VPC endpoint instead of the publicly published record.

To verify that the DNS override is working correctly, issue the following `dig` command using the value of your "Private DNS Name" instead of the value in the example:

```shell  theme={null}
dig +short wildcard.frzzbztuqm3h-euwest1-1.psdb.cloud
172.31.16.197
172.31.13.7
```

If your `dig` command returns a set of static IP addresses, your VPC Endpoint connection is operating successfully. If it returns a `CNAME` to an ELB record (for example, something like `something.elb.region.amazoneaws.com`), your connection is not operating successfully, and you should consult your Solutions Engineer.

Once you've verified that your connection is operating successfully, you will need to verify that you can reach a database you've provisioned:

<Steps>
  <Step>
    [Create a connection string](/docs/vitess/connecting/connection-strings#creating-a-password) for a PlanetScale database using the "**Connect**" button. Select "**MySQL CLI**" and copy the command.
  </Step>

  <Step>
    Paste your MySQL CLI command into a command prompt of an EC2 instance running in your VPC with the `mysql-client` package installed:

    ```shell  theme={null}
    mysql -h <HOST_NAME> -u <USERNAME> -p --ssl-mode=VERIFY_IDENTITY --ssl-ca=/etc/pki/tls/certs/ca-bundle.crt
    Enter password:
    ...

    mysql>
    ```
  </Step>
</Steps>

<Info>
  The correct path for the CA root configuration for the `--ssl-ca` flag depends on your operating system. See the [CA root configuration documentation](/docs/vitess/connecting/secure-connections#ca-root-configuration) for more the correct path.
</Info>

If you receive the `mysql>` prompt, your connection is operating successfully, and you have just confirmed that your connections to PlanetScale will be established through AWS PrivateLink. If you do not receive the `mysql>` prompt, please consult your Solutions Engineer.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt