# Source: https://docs.salad.com/container-engine/how-to-guides/external-logging/splunk-logging.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Splunk

*Last Updated: October 15, 2024*

Splunk is a software platform for searching, monitoring, and analyzing machine-generated data. User need to generate
credentials from Splunk cloud and provide it to SCE.

To enable external logging service using Splunk, please follow the steps.

### Step 1: Generate Credentials of Splunk

1. Visit [Splunk Cloud](https://www.splunk.com/en_us/products/splunk-cloud-platform.html) and login to the portal
   Logging in to the Splunk Cloud portal using your credentials. If you don't have an account, sign up to get started.
2. Visit a setting section and click on Data inputs.
3. Select the Http Event Collector in the Local inputs section.
4. Configure the Global settings enable(SSL and All tokens).
5. Click on “New Token”, provide name, source name and description.
6. Click on “Next”, will be prompted with “Token Value” and “Start searching” option.
   <img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/splunk-get-credentials.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=7899d27a8c644e428b919a7af8acccbe" data-og-width="1469" width="1469" data-og-height="701" height="701" data-path="container-engine/images/splunk-get-credentials.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/splunk-get-credentials.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=41970669f6c85ee2d82e16e9f1894b3e 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/splunk-get-credentials.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=d9584c66230ea9c76a59902d20f90312 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/splunk-get-credentials.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=b2bd163a6f855d1d9221cc6e377b0d50 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/splunk-get-credentials.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=997230515832773c0c4abdb5fc675d27 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/splunk-get-credentials.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=98346acd2babfca92875dddcbe2e1b4c 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/splunk-get-credentials.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=217f48adaf3dc103f5cdfd55f92953fd 2500w" />

*Note: For additional information regarding HEC, tokens, and host URLs, please refer to the
[Splunk official documentation](https://docs.splunk.com/Documentation/Splunk/9.1.0/Data/UsetheHTTPEventCollector). Once
you have obtained the token and
[host URL](https://docs.splunk.com/Documentation/Splunk/9.1.0/Data/UsetheHTTPEventCollector#:~:text=Splunk%20Dev%20Portal.-,Send%20data%20to%20HTTP%20Event%20Collector%20on%20Splunk%20Cloud%20Platform,-You%20must%20send),
you can proceed to create container group on [SaladCloud portal](https://portal.salad.com/).*

### Step 2: Configure credentials for SaladCloud Container

while container group creation or configuration process, locate the "External Logging Services" section in Optional
Settings and click on the "Edit" button.

1. Click “Edit” on External Logging Services.
   <img src="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-edit-external-logging.png?fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=735c47c96ef27e47c2aa826331b109d1" data-og-width="681" width="681" data-og-height="921" height="921" data-path="container-engine/images/portal-edit-external-logging.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-edit-external-logging.png?w=280&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=74a9f83262962e9c36dfd78e556dec10 280w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-edit-external-logging.png?w=560&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=5203aa64fc1d24d78cfda95cf6b88637 560w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-edit-external-logging.png?w=840&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=e305e2584e214125c1be0b876c54faec 840w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-edit-external-logging.png?w=1100&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=a99bdb7222eac84285a1b69c2795944b 1100w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-edit-external-logging.png?w=1650&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=e3b1d89a2b9a26d881cf1e6edd33be0e 1650w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-edit-external-logging.png?w=2500&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=193c03ad48c2e95606b0b5117edfe1f4 2500w" />
2. In the sidebar appears at right, click on "**Splunk**" under the option of “Select a Container Logging Service”.
   Finally past the Host URL and token that we generated from Splunk and simple click on “Configure”.
   <img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/select-and-configure-splunk.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=c16a1bbc5b3ddf2d51ee8ab475e93a40" data-og-width="1494" width="1494" data-og-height="636" height="636" data-path="container-engine/images/select-and-configure-splunk.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/select-and-configure-splunk.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=4c2eadd2bd4bcf7493a8eb8634af70d0 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/select-and-configure-splunk.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=6b2858fad88485cf74b302d676e307d0 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/select-and-configure-splunk.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=8fd2011c92c8b76a3ab8233c0d57e9ad 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/select-and-configure-splunk.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=37e00ad7e1c30d3a92c84b2eaaab03e4 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/select-and-configure-splunk.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=d1e05ac3f61f81762080b18dc19d8a48 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/select-and-configure-splunk.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=de6c87aa24dbda3a0fc1bba70c2d5d50 2500w" />

### Step 3: Run Your Container

Once the container is configured, you can deploy it by clicking on button “Deploy” and "Start".

Once you've started the container and it comes in \_running \_ state, the logs will be seamlessly transmitted to the
Splunk portal. Monitor your container's status to ensure it's in the running state, and then head to the Splunk portal
to see your SaladCloud Container logs in action.
