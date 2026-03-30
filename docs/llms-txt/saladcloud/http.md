# Source: https://docs.salad.com/container-engine/how-to-guides/external-logging/http.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# HTTP

*Last Updated: October 15, 2024*

To enable external logging service via HTTP on SaladCloud , you need to configure your Container Group Deployment with
the appropriate HTTP endpoint details. SaladCloud External Logging supports HTTP endpoints for receiving logs. This
example will guide you through the setup using an HTTP service.

## Prerequisite

Before configuring the HTTP external logging service, ensure the following prerequisites are met:

1. HTTP Endpoint: Have an HTTP endpoint (URL) ready to receive logs. This endpoint should be publicly reachable.
2. Port Availability: Choose a port number between 1 to 65535 for the HTTP service. Ensure that the selected port is
   available and not blocked by firewalls.
3. Authentication and Headers(Optional): If your HTTP service requires authentication or specific headers, gather the
   necessary information such as username, password, and custom headers.

## Step 1: Have a Publicly Accessible HTTP Endpoint

Ensure that you have an HTTP endpoint that is publicly accessible. This endpoint should be ready to receive logs.

## Step 2: Provide Information to SCE

while container group creation or configuration process at SaladCloud portal, locate the "External Logging Services"
section in Optional Settings.

1. Locate the "External Logging Services" section in the Optional Settings.
2. Click on “Edit” for External Logging Services.
3. In the provided form, fill in the following details:
   1. Host: Enter the IP address or hostname of the machine where your HTTP service is running.
   2. Port: Choose a port number between 1 and 65535. Ensure it matches the port on your publicly accessible HTTP
      endpoint.
   3. Path (Optional): Specify a valid path if required by your HTTP endpoint.
   4. User (Optional): If your HTTP service requires authentication, provide the username.
   5. Password (Optional): If your HTTP service requires authentication, provide the password.
   6. Headers (Optional): If your HTTP service requires custom headers, provide the name and value pairs.
   7. Click “Configure” to save the provided information.

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-http.png?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=a9783ede5e1c6ca4fac7c05c521affcb" data-og-width="428" width="428" data-og-height="886" height="886" data-path="container-engine/images/configure-http.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-http.png?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=d26e540a2b720884d74fa618be5b0ff1 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-http.png?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=a2db0b7734e30716c8f928dfb7288ed4 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-http.png?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=7ed50bf097412c88650f08d2db067586 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-http.png?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=ca1be2f79514b8513efad1a2eb3d62e7 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-http.png?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=4073ebb50713db999116cdf557aff227 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-http.png?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=a57ce7f3ecc9e581101989a275310de9 2500w" />

## Step 3: Deploy Container Group

Once you've provided the necessary information, deploy the Container Group by clicking on the “Deploy” and "Start"
buttons.

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/complete-http.png?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=0c05a43ea2d7ed592fb7621a9cdff740" data-og-width="1213" width="1213" data-og-height="488" height="488" data-path="container-engine/images/complete-http.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/complete-http.png?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=bb0a49b086553e6b9e706ba99a983316 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/complete-http.png?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=31230b7785bf4afb7ce09d3f72d9d70a 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/complete-http.png?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=eda60603a2d7d2f6afbec7032923231f 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/complete-http.png?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=7d5c16d7281d194dbc4900e90c1a5694 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/complete-http.png?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=29e222793f292684e4060daacf025880 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/complete-http.png?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=4228ac12f4f8d957816a3567fedb78ae 2500w" />

## Step 4: Verify Logs in HTTP Service

After the container is running, logs from your containers should be streaming to the specified HTTP endpoint. Verify
that your HTTP service is receiving the logs.

> 👍 Congratulations!
>
> You have successfully enabled the external logging service using HTTP.
