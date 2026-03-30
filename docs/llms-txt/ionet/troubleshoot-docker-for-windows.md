# Source: https://io.net/docs/guides/workers/troubleshoot-docker-for-windows.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Windows: Troubleshoot Docker

### Windows Uptime

Follow the instructions below if you experience inconsistent uptime on Windows.

<Info>
  To ensure that the DHCP lease time on the router is set to a duration exceeding 24 hours, access the group policy editor within the Windows operating system. Proceed by enabling the specified settings in the following sequence:
</Info>

1. Open the group policy editor and go to **Computer Configuration**.
2. In Computer Configuration, find the **Administrative Templates** section.
3. Under **Administrative Templates**, go to **System**.
4. In the **System** menu, choose **Power Management**.
5. Access the **Sleep Settings** subsection within **Power Management**.
6. Activate both **Allow network connectivity during connected-standby (on battery)** and **Allow network connectivity during connected-standby (plugged in)** options.

Adjust the settings above to meet your requirements.

### Fixing the "Docker Desktop - Unexpected WSL error" in Windows

This error occurs when you haven't updated to the latest version of WSL or haven't enabled the Hyper-V feature. Follow these steps:

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/63989d6-UseCases-DockerWSL.jpg?fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=c4ba2b8de097a392803945b952eaec26" alt="" className="mx-auto" style={{ width:"73%" }} data-og-width="1856" width="1856" data-og-height="898" height="898" data-path="images/docs/63989d6-UseCases-DockerWSL.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/63989d6-UseCases-DockerWSL.jpg?w=280&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=c043e0494f6524ce5e359edd82235ece 280w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/63989d6-UseCases-DockerWSL.jpg?w=560&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=a72fcb15ebd6914f55f4e65a077cffe7 560w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/63989d6-UseCases-DockerWSL.jpg?w=840&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=e355e42506d5c713a2090281e0c7d364 840w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/63989d6-UseCases-DockerWSL.jpg?w=1100&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=d3564967c963e74b74fc8e86ba6db4f6 1100w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/63989d6-UseCases-DockerWSL.jpg?w=1650&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=910e899c96772137b29189301b595b53 1650w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/63989d6-UseCases-DockerWSL.jpg?w=2500&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=b3ff2d584230852fc3fafda17d2b83cd 2500w" />
</Frame>

1. **Check and Update WSL Version**: First, ensure that you’re running the latest version of WSL. You can check your current WSL version by opening a command prompt and typing:

   ```
   wsl --version
   ```

   If you find that you’re not on WSL 2, you can set the default version to 2 by executing:

   ```
   wsl --set-default-version 2
   ```
2. **Enable Hyper-V Feature**: Hyper-V is a virtualization technology tool that needs to be enabled in Windows. To check if Hyper-V is enabled, you can use the Windows Features dialog via Search:

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/95eca0ec814f73628c619d3f020cd61e9c52e6ad5ac9b004caf5a8d4d2e4d3b0-UseCases-DockerWSL-2.jpg?fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=e8275272c85752e26cf16b9e85a94068" alt="" className="mx-auto" style={{ width:"71%" }} data-og-width="1260" width="1260" data-og-height="780" height="780" data-path="images/docs/95eca0ec814f73628c619d3f020cd61e9c52e6ad5ac9b004caf5a8d4d2e4d3b0-UseCases-DockerWSL-2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/95eca0ec814f73628c619d3f020cd61e9c52e6ad5ac9b004caf5a8d4d2e4d3b0-UseCases-DockerWSL-2.jpg?w=280&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=bf65c0edf8ce69fd10fada7ddb0286c1 280w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/95eca0ec814f73628c619d3f020cd61e9c52e6ad5ac9b004caf5a8d4d2e4d3b0-UseCases-DockerWSL-2.jpg?w=560&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=8edd9c7553373eee0f9aebd29827936e 560w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/95eca0ec814f73628c619d3f020cd61e9c52e6ad5ac9b004caf5a8d4d2e4d3b0-UseCases-DockerWSL-2.jpg?w=840&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=6b990be60dd9ff12d9c462289da0cd73 840w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/95eca0ec814f73628c619d3f020cd61e9c52e6ad5ac9b004caf5a8d4d2e4d3b0-UseCases-DockerWSL-2.jpg?w=1100&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=c253335ba01d678a296dca137fa0bb37 1100w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/95eca0ec814f73628c619d3f020cd61e9c52e6ad5ac9b004caf5a8d4d2e4d3b0-UseCases-DockerWSL-2.jpg?w=1650&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=779179fce6dbe215a4d9467516cb502e 1650w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/95eca0ec814f73628c619d3f020cd61e9c52e6ad5ac9b004caf5a8d4d2e4d3b0-UseCases-DockerWSL-2.jpg?w=2500&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=46e8e1cf145470f4c293092f22e34c81 2500w" />
   </Frame>

   In the **Windows Features** dialog, scroll down and check **Windows Hypervisor Platform**, then click OK.:

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0346c11c13e1b8ddd972467c09f4a81bb31bb9a5ab1383baef3c92aa726203cf-UseCases-DockerWSL-3.jpg?fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=fab82c3f30f904566e0c9062f84fae52" alt="" className="mx-auto" style={{ width:"63%" }} data-og-width="1374" width="1374" data-og-height="1538" height="1538" data-path="images/docs/0346c11c13e1b8ddd972467c09f4a81bb31bb9a5ab1383baef3c92aa726203cf-UseCases-DockerWSL-3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0346c11c13e1b8ddd972467c09f4a81bb31bb9a5ab1383baef3c92aa726203cf-UseCases-DockerWSL-3.jpg?w=280&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=cd167b3e97f21137d5223bf2fcb536e7 280w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0346c11c13e1b8ddd972467c09f4a81bb31bb9a5ab1383baef3c92aa726203cf-UseCases-DockerWSL-3.jpg?w=560&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=edfb143b7f93139decf94be9dd9d8467 560w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0346c11c13e1b8ddd972467c09f4a81bb31bb9a5ab1383baef3c92aa726203cf-UseCases-DockerWSL-3.jpg?w=840&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=c98d0aea71185ce449a7ea035792d838 840w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0346c11c13e1b8ddd972467c09f4a81bb31bb9a5ab1383baef3c92aa726203cf-UseCases-DockerWSL-3.jpg?w=1100&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=5c526439ff5981164dae12814f5045b1 1100w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0346c11c13e1b8ddd972467c09f4a81bb31bb9a5ab1383baef3c92aa726203cf-UseCases-DockerWSL-3.jpg?w=1650&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=9966682f70df148a1d4c7b2e42335af4 1650w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0346c11c13e1b8ddd972467c09f4a81bb31bb9a5ab1383baef3c92aa726203cf-UseCases-DockerWSL-3.jpg?w=2500&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=4210320ab371d1638a6f864bb474a28b 2500w" />
   </Frame>

   After installing **Windows Hypervisor Platform**, the problem should disappear.

### Stop the Docker with all Containers and Images

Run the command below in Terminal to stop the platform and remove all containers for Windows.

<CodeGroup>
  ```Text Terminal Command theme={null}
  # Stop all running containers
  docker stop $(docker ps -aq)

  # Remove all containers
  docker rm $(docker ps -aq)

  # Remove all images
  docker rmi $(docker images -aq)
  ```
</CodeGroup>

### Restart the Platform

* Reboot your computer or server.
* After the device reboots, restart the platform by entering this command into the Terminal:

  ```
  ./io_net_launch_binary_windows.exe 
  ```

### Additional Guides

#### Ports

Expose the ports below to ensure platform stability for Windows:

* TCP: 443, 25061, 5432, 80
* UDP: 80, 443, 41641, 3478

Ensure that these ports are open and accessible to enable smooth operation of the platform.

#### How can I verify that program has started successfully?

* When running the following command on Terminal, **you should always have 2 Docker containers running**:

  <CodeGroup>
    ```Text Terminal Command theme={null}
     docker ps
    ```
  </CodeGroup>
* If there are no containers or only one container running after running the docker run **-d ... command** from the website:
  * Stop the platform using the command provided in the guide above.
  * Restart the platform using the command from the website again.

### Waiting for IO Containers to Start

Ensure the "**Use containerd for storing and pulling images**" option is **disabled** in Docker's General Settings.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/790b54eb86adbf616cd0b0bfb8e30bad3899827e4b56a043bc3711322b96ebcc-DockerIssue1.5.jpg?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=c0e52d58fbaad9beecd73752e536191b" alt="" data-og-width="2056" width="2056" data-og-height="1202" height="1202" data-path="images/docs/790b54eb86adbf616cd0b0bfb8e30bad3899827e4b56a043bc3711322b96ebcc-DockerIssue1.5.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/790b54eb86adbf616cd0b0bfb8e30bad3899827e4b56a043bc3711322b96ebcc-DockerIssue1.5.jpg?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=954bc19beab4a7607e619a5ca8c595ad 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/790b54eb86adbf616cd0b0bfb8e30bad3899827e4b56a043bc3711322b96ebcc-DockerIssue1.5.jpg?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=a40bc3f8e7b166aa83cee5ff19c5c590 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/790b54eb86adbf616cd0b0bfb8e30bad3899827e4b56a043bc3711322b96ebcc-DockerIssue1.5.jpg?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=43e4eacee267105b3692de936cb27f55 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/790b54eb86adbf616cd0b0bfb8e30bad3899827e4b56a043bc3711322b96ebcc-DockerIssue1.5.jpg?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=44b4292636b19c3360adf2b81abe9940 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/790b54eb86adbf616cd0b0bfb8e30bad3899827e4b56a043bc3711322b96ebcc-DockerIssue1.5.jpg?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=5f96b76f45ac6163be9e4032a83833f4 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/790b54eb86adbf616cd0b0bfb8e30bad3899827e4b56a043bc3711322b96ebcc-DockerIssue1.5.jpg?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=9922bdd2c16bac28e883d09bf64c2407 2500w" />
</Frame>

Containerd may interfere with Docker’s default image management, **so it’s recommended to turn it off**.

## Worker Disconnecting Despite Containers Running

If your Worker disconnects even when the containers are up, try the following checks:

1. Ensure resources aren't limited. Make sure Docker's "**Resource Saver**" feature is **disabled** in the **Resources tab** of **Docker Settings**.

   <Frame>
       <img src="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ec67447f68fd986bf9eb405aa9aa03bb07ee65eaf0f95bd5e88f00cb450af13f-DockerIssue5.5.jpg?fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=b82f2f3ddd648aaad7794a27376844c3" alt="" data-og-width="2056" width="2056" data-og-height="1202" height="1202" data-path="images/docs/ec67447f68fd986bf9eb405aa9aa03bb07ee65eaf0f95bd5e88f00cb450af13f-DockerIssue5.5.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ec67447f68fd986bf9eb405aa9aa03bb07ee65eaf0f95bd5e88f00cb450af13f-DockerIssue5.5.jpg?w=280&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=3ac35949317f4d19427e00704b9789d4 280w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ec67447f68fd986bf9eb405aa9aa03bb07ee65eaf0f95bd5e88f00cb450af13f-DockerIssue5.5.jpg?w=560&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=1828a9d49e9f3f821e4ddd81b98b595b 560w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ec67447f68fd986bf9eb405aa9aa03bb07ee65eaf0f95bd5e88f00cb450af13f-DockerIssue5.5.jpg?w=840&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=34c1157448658832cc971fa2b5c7944a 840w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ec67447f68fd986bf9eb405aa9aa03bb07ee65eaf0f95bd5e88f00cb450af13f-DockerIssue5.5.jpg?w=1100&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=4e48d7e0164686dbb0635c496da203ed 1100w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ec67447f68fd986bf9eb405aa9aa03bb07ee65eaf0f95bd5e88f00cb450af13f-DockerIssue5.5.jpg?w=1650&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=e63a325e3d3a29d45266cddf9516100f 1650w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ec67447f68fd986bf9eb405aa9aa03bb07ee65eaf0f95bd5e88f00cb450af13f-DockerIssue5.5.jpg?w=2500&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=4baab7d7b3510758a3efacd562efe8d3 2500w" />
   </Frame>
2. Check Docker Resource Allocation. Ensure Docker is allocated the minimum required **CPU**, **RAM**, and **disk space**. System requirements are as follows:
   * **Memory**: At least 512MB of free RAM (2GB is recommended)
   * **Disk**: Adequate storage to run the Docker containers you intend to use
   * **CPU/GPU**: You can check the currently supported [CPUs/GPUs](/guides/workers/supported-devices).
3. Verify Power Supply to GPU(s). Ensure the GPU(s) are receiving adequate power for stable operation.

## Connectivity Tier Not Displaying Correctly

To troubleshoot connectivity tier issues, users can test network speeds via a sample Docker container. Here's how:

1. Pull the Python 3.9 Slim container:

   ```
   docker pull python:3.9-slim
   ```
2. Run the container:

   ```
   docker run -it --name speedtest-container python:3.9-slim /bin/bash
   ```
3. Install the speedtest tool:

   ```
   pip install speedtest-cli
   ```
4. Test the network speed:

   ```
   speedtest-cli
   ```

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4f78a04e7dcac9a77ef208709f38bb2e8821bb81dce7cd1921b08fada7e100e6-DockerIssue6.1.jpg?fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=6a8d9ff798fd7cf97882a6db259c8966" alt="" className="mx-auto" style={{ width:"74%" }} data-og-width="1696" width="1696" data-og-height="1842" height="1842" data-path="images/docs/4f78a04e7dcac9a77ef208709f38bb2e8821bb81dce7cd1921b08fada7e100e6-DockerIssue6.1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4f78a04e7dcac9a77ef208709f38bb2e8821bb81dce7cd1921b08fada7e100e6-DockerIssue6.1.jpg?w=280&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=8a35bdf7e6e9f16130f347bd03af3a05 280w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4f78a04e7dcac9a77ef208709f38bb2e8821bb81dce7cd1921b08fada7e100e6-DockerIssue6.1.jpg?w=560&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=8687dc7df1d09c8f7a873a96323ef2de 560w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4f78a04e7dcac9a77ef208709f38bb2e8821bb81dce7cd1921b08fada7e100e6-DockerIssue6.1.jpg?w=840&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=c39ed06cafa9abd803bb05ad7adedfdb 840w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4f78a04e7dcac9a77ef208709f38bb2e8821bb81dce7cd1921b08fada7e100e6-DockerIssue6.1.jpg?w=1100&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=aea7038432306e8b15ac9803142ba35a 1100w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4f78a04e7dcac9a77ef208709f38bb2e8821bb81dce7cd1921b08fada7e100e6-DockerIssue6.1.jpg?w=1650&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=02ee5f22bc136c4172fb65721723f8f8 1650w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4f78a04e7dcac9a77ef208709f38bb2e8821bb81dce7cd1921b08fada7e100e6-DockerIssue6.1.jpg?w=2500&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=6ad91fc9b2135de30b4353897330585d 2500w" />
</Frame>

We recommend running similar speed tests periodically within your containers to monitor connectivity performance. You can also guide users on how to perform these tests at regular intervals or during specific instances for troubleshooting.
