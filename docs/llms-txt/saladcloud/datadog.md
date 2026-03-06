# Source: https://docs.salad.com/container-engine/how-to-guides/external-logging/datadog.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Datadog

*Last Updated: October 15, 2024*

Datadog is a platform for searching, monitoring, and analyzing machine-generated data. User need to generate credentials
from [Datadog](https://www.datadoghq.com/) and provide it to SCE.

To enable external logging service using Datadog, please follow the steps.

### **Step 1 : Create a Datadog Account**

Go to the [Datadog website](https://www.datadoghq.com/) and sign up for a Datadog account if you don't have one already.
You can select a plan that suits your needs, and Datadog typically offers a free trial period.

### **Step 2 :Enable Log Integration**

* In the Datadog portal, navigate to the [Log section ](https://us5.datadoghq.com/logs/onboarding/other)in the right
  tab.
* Inside the Log section, select the "Other" integration and choose "Fluentbit."
* Copy the Host and API key.

<img src="https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/datadog-get-credentials.png?fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=e113943c8c57e48b8ef207190ade4b07" data-og-width="1915" width="1915" data-og-height="937" height="937" data-path="container-engine/images/datadog-get-credentials.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/datadog-get-credentials.png?w=280&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=f368ab9be48a000eebf1e8e74e997b67 280w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/datadog-get-credentials.png?w=560&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=6b0f9a9ae95098e3f6f66b3efcf78fc6 560w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/datadog-get-credentials.png?w=840&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=b75f01d97ab9928ae21ef10273bf4f7c 840w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/datadog-get-credentials.png?w=1100&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=7953ee1d42c3bd91daf39dad3ca6a1c5 1100w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/datadog-get-credentials.png?w=1650&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=79ae95713a4f8ef15436af8b9b471339 1650w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/datadog-get-credentials.png?w=2500&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=f95e8889deda4f99c7e2f9cd5f56b103 2500w" />

### **Step 3 : Provide API Key and Host Information to SCE**:

while container group creation or configuration process at SaladCloud portal, locate the "External Logging Services"
section in Optional Settings.

* Click “Edit” on External Logging Services.
* In the sidebar appears at right, click on "**Datadog**" under the option of “Select a Container Logging Service”.
  Finally past the Host URL and API key that we generated from Datadog and simple click on “Configure”.

<img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/select-datadog.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=6c9145f178bb7da4f641a484c99373fb" data-og-width="1669" width="1669" data-og-height="1022" height="1022" data-path="container-engine/images/select-datadog.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/select-datadog.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=38ddf3198a8c1a5de7b91c2a96fb7da2 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/select-datadog.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=e86d41366bdca24e3ae7892b3f447a9d 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/select-datadog.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=c8034beaec365657cd8330b9319823cc 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/select-datadog.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=ea7d0d827128eaa807b2dc3bd70ffa4d 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/select-datadog.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=fba1569f44238ff44907b16dd5148fed 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/select-datadog.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=7d10fb4bc7cc87ed21ad478f4e93a200 2500w" />

### **Step 4 : Complete Configuration**:

Once the container is configured, you can deploy it by clicking on button “Deploy” and "Start".

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/complete-datadog.png?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=96c189c9c2ae01a2fc4da2f7b5b544a6" data-og-width="1213" width="1213" data-og-height="488" height="488" data-path="container-engine/images/complete-datadog.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/complete-datadog.png?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=86731afb3776df214142a74d052ad1fc 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/complete-datadog.png?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=dda6724056586cc9136edfddb3184abe 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/complete-datadog.png?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=09d0cadfe03fd6daa9739d203b18f196 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/complete-datadog.png?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=60feb6a00d791a502b2d4fccfc286b05 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/complete-datadog.png?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=970bd14638df02448e8e7a9f47eddcab 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/complete-datadog.png?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=c5beef8da458a4ae25f828296cec7554 2500w" />

Once you've started the container and it comes in \_running \_ state, the logs will be seamlessly transmitted to the
Datadog portal and you can view the logs at [Log dashboard](https://us5.datadoghq.com/logs).

<img src="https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/datadog-portal.png?fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=68ff42c8cf316976d7832b406cc15afe" data-og-width="1655" width="1655" data-og-height="844" height="844" data-path="container-engine/images/datadog-portal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/datadog-portal.png?w=280&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=30994e96a12bc2928a66115e4cce7603 280w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/datadog-portal.png?w=560&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=09c62966e085961528f93c6b44c5dd2f 560w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/datadog-portal.png?w=840&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=18321ebeee65f87577b876b4bd98ea1f 840w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/datadog-portal.png?w=1100&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=ff4e9347eda06d3d3ee9d514cda5fb52 1100w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/datadog-portal.png?w=1650&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=a785f8717d9c684fb96d6c69b2f3789b 1650w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/datadog-portal.png?w=2500&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=5f18172c79e51d8046287098e653a610 2500w" />

> 👍 Congratulations!
>
> You have successfully enabled the external logging service using Datadog.
