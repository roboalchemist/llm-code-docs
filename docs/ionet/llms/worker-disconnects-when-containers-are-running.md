# Source: https://io.net/docs/guides/workers/worker-disconnects-when-containers-are-running.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Worker Disconnects When Containers Are Running

> If your Worker disconnects even when the containers are up, try the following checks:

1. Ensure resources aren't limited. Make sure Docker's "**Resource Saver**" feature is **disabled** in the **Resources tab** of **Docker Settings**.

   <Frame>
       <img src="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/35af69f9e3afdc90b7f92bcc0da564ccc352b4a33230d164095d391fc283f084-DockerIssue5.5.jpg?fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=0a4188346477bc315feede8a35a71ec8" alt="" data-og-width="2056" width="2056" data-og-height="1202" height="1202" data-path="images/docs/35af69f9e3afdc90b7f92bcc0da564ccc352b4a33230d164095d391fc283f084-DockerIssue5.5.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/35af69f9e3afdc90b7f92bcc0da564ccc352b4a33230d164095d391fc283f084-DockerIssue5.5.jpg?w=280&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=bc23fb0376d798abb4b33ee705726e7c 280w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/35af69f9e3afdc90b7f92bcc0da564ccc352b4a33230d164095d391fc283f084-DockerIssue5.5.jpg?w=560&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=4e61964d0226f7a12dc8d07f84f468bc 560w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/35af69f9e3afdc90b7f92bcc0da564ccc352b4a33230d164095d391fc283f084-DockerIssue5.5.jpg?w=840&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=cfae06b5e6dfd9911ca530b0753805b9 840w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/35af69f9e3afdc90b7f92bcc0da564ccc352b4a33230d164095d391fc283f084-DockerIssue5.5.jpg?w=1100&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=536cfbf64233ace605e3e39575d5eaeb 1100w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/35af69f9e3afdc90b7f92bcc0da564ccc352b4a33230d164095d391fc283f084-DockerIssue5.5.jpg?w=1650&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=32478a3ea3acff5039518be9b56347cb 1650w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/35af69f9e3afdc90b7f92bcc0da564ccc352b4a33230d164095d391fc283f084-DockerIssue5.5.jpg?w=2500&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=f305033bbafaf250aa08e65fbe31527a 2500w" />
   </Frame>

2. Check Docker Resource Allocation. Ensure Docker is allocated the minimum required **CPU**, **RAM**, and **disk space**. System requirements are as follows:

   * **Memory**: At least 512MB of free RAM (2GB is recommended)
   * **Disk**: Adequate storage to run the Docker containers you intend to use
   * **CPU/GPU**: You can check the currently supported [CPUs/GPUs](/guides/workers/supported-devices).

3. Verify Power Supply to GPU(s). Ensure the GPU(s) are receiving adequate power for stable operation.
