# Source: https://docs.salad.com/container-engine/explanation/infrastructure-platform/external-logging.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# External Logging

*Last Updated: October 15, 2024*

You may wish to stream event logs from your container group deployment to an external service for easier parsing,
retention, and monitoring. To configure external logging, click 'edit' on the External Logging Services section on the
Container Group Deployment page.

<img src="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-edit-external-logging.png?fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=735c47c96ef27e47c2aa826331b109d1" data-og-width="681" width="681" data-og-height="921" height="921" data-path="container-engine/images/portal-edit-external-logging.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-edit-external-logging.png?w=280&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=74a9f83262962e9c36dfd78e556dec10 280w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-edit-external-logging.png?w=560&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=5203aa64fc1d24d78cfda95cf6b88637 560w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-edit-external-logging.png?w=840&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=e305e2584e214125c1be0b876c54faec 840w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-edit-external-logging.png?w=1100&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=a99bdb7222eac84285a1b69c2795944b 1100w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-edit-external-logging.png?w=1650&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=e3b1d89a2b9a26d881cf1e6edd33be0e 1650w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-edit-external-logging.png?w=2500&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=193c03ad48c2e95606b0b5117edfe1f4 2500w" />

In the sidebar that appears, select the logging service you wish to use.

> ❓ Logging service not supported?
>
> We're working to expand the logging services supported on SaladCloud. If you're using an external logging service not
> listed here, please [get in touch](mailto:cloud@salad.com)!
>
> Under the hood, SaladCloud uses [Fluent Bit](https://docs.fluentbit.io/manual/pipeline/outputs) to collect and send
> container logs. Check the Fluent Bit documentation here to see if your preferred logging service is supported out of
> the box. If so, we can easily add support for it - just let us know.

<img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-select-logging-service.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=0880e2949b572579576ce51ffc4927ce" data-og-width="470" width="470" data-og-height="405" height="405" data-path="container-engine/images/portal-select-logging-service.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-select-logging-service.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=ef63c2183a71d1bba9b8787f4106e894 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-select-logging-service.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=20b481ec452e67a0834e5fd9abb55a83 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-select-logging-service.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=332d13a2c4f492decc80b893d6800b0b 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-select-logging-service.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=af0c4cab930b7ada6e0b01f6c02fd35e 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-select-logging-service.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=629c4cf1cdd8a8ed92a663956a316642 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-select-logging-service.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=e7c3304a6de63dfc3414da0f06f8f698 2500w" />

Finally, fill out the form fields and press Configure.

<img src="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-configure-logging-service.png?fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=d3494e8e9e24f54bc826b941450a4f26" data-og-width="486" width="486" data-og-height="850" height="850" data-path="container-engine/images/portal-configure-logging-service.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-configure-logging-service.png?w=280&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=b448243312ab08f5a44996ad20120b4d 280w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-configure-logging-service.png?w=560&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=fd35ee417b572ffb394f625dab222fac 560w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-configure-logging-service.png?w=840&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=ceefdc156bd62faae3614bc3fb7a3ff7 840w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-configure-logging-service.png?w=1100&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=b49bdb3272790080678998c6d8ca47ee 1100w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-configure-logging-service.png?w=1650&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=3949b7d15006178f956acf32d3a04a02 1650w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-configure-logging-service.png?w=2500&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=2ffbdfcb0e0059d4848e79d019596bd5 2500w" />

> 📘 Don't have an external logging provider?
>
> Check out the [Container Logs](/container-engine/explanation/container-groups/container-logs) feature in the
> SaladCloud Portal.
