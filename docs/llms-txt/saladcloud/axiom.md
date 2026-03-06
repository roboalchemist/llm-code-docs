# Source: https://docs.salad.com/container-engine/how-to-guides/external-logging/axiom.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Axiom

*Last Updated: October 15, 2024*

Axiom is our preferred external logging service provider.

To enable external logging service using Axiom, please follow these steps:

# Step 1: Get Dataset Name and API Key from Axiom

# Step 2: Add the Axiom configuration to your Container Group

* Click “Edit” on External Logging Services

* Select Axiom from the dropdown

  <img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/select-axiom.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=13b67a438ba94a441c7373c1526b7fa2" data-og-width="470" width="470" data-og-height="405" height="405" data-path="container-engine/images/select-axiom.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/select-axiom.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=87cbfc98aee6a59f456f2f56f2affc8b 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/select-axiom.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=d0e2470a0e33d6a780a86fa393b0d3cb 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/select-axiom.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=5e634af156ee75468bb10cfc2b376812 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/select-axiom.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=dbc7c034287a0a4580d1cb48572fcbcf 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/select-axiom.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=0c389ebeea364fd1fcb1688a379bb725 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/select-axiom.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=bfd7b99ad9de7741dc18f4835a9de99a 2500w" />

* Input the Dataset Name and API Key

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-axiom.png?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=076ecf2adf02ee2515af56bc7b65d7d3" data-og-width="476" width="476" data-og-height="839" height="839" data-path="container-engine/images/configure-axiom.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-axiom.png?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=bf331a4eb6a7014a0a8c8802e6255d69 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-axiom.png?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=421149fd4cae464c461fbb206d081d79 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-axiom.png?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=c0f996b9df5ea93a7d71ea1de0be6a70 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-axiom.png?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=a759543a905c1467deb0c647c6de9958 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-axiom.png?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=bc5758760e70885e0b7690a7dc2e4dd9 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-axiom.png?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=e269520ec7d9b64454b553bfa0fa327c 2500w" />

* Click the "Configure" button at the bottom.

# Step 3: Deploy Container Group

* Finish setting up the rest of your container group settings, and deploy it!
* Start the container group to run your container
* Your logs will be seamlessly transmitted to Axiom

# Step 4: Verify Logs in Axiom

* Once the container is running and logging something, verify that your logs are available in Axiom.
