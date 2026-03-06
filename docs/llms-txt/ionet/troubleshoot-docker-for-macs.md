# Source: https://io.net/docs/guides/workers/troubleshoot-docker-for-macs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MacOs: Troubleshoot Docker

### Incompatible CPU detected Error

To resolve this issue, ensure you download and install the appropriate Docker version. For macOS, Docker provides two options: "**Apple Chip**" and "**Intel Chip**."

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d87445a-Step6.jpg?fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=f4015cd5c8f3d63745d867eaa3d0aa29" alt="" className="mx-auto" style={{ width:"59%" }} data-og-width="663" width="663" data-og-height="705" height="705" data-path="images/docs/d87445a-Step6.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d87445a-Step6.jpg?w=280&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=563004c6721914e71ef7281242353fbe 280w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d87445a-Step6.jpg?w=560&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=6d8445a5b5ff15f00eafc2844c1d7b97 560w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d87445a-Step6.jpg?w=840&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=0161d0dab5ddc6a69b105b72716244de 840w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d87445a-Step6.jpg?w=1100&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=18ac28bed9ca408516ca6461c422e742 1100w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d87445a-Step6.jpg?w=1650&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=9b02d648e81e48f9bc9f1941516f119c 1650w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d87445a-Step6.jpg?w=2500&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=5a2d8cb9439ee13faff178ed5d472d60 2500w" />
</Frame>

First, you need to remove the previous version for the **Intel chip**. Click on the **Bug** icon to open Docker Settings, then click **Uninstall**.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a268dc3fbe5ec21efbd083196849729543a8da4b5d05e4e7cfce469183cf06cb-Step8.jpg?fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=d0e1e171d7affa5ee2c30899ad5bf3ef" alt="" data-og-width="1456" width="1456" data-og-height="944" height="944" data-path="images/docs/a268dc3fbe5ec21efbd083196849729543a8da4b5d05e4e7cfce469183cf06cb-Step8.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a268dc3fbe5ec21efbd083196849729543a8da4b5d05e4e7cfce469183cf06cb-Step8.jpg?w=280&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=7c0a2a4311b2044d4777da167ef58e46 280w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a268dc3fbe5ec21efbd083196849729543a8da4b5d05e4e7cfce469183cf06cb-Step8.jpg?w=560&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=f41ccef09f3201c26ce89c3beefd4e2c 560w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a268dc3fbe5ec21efbd083196849729543a8da4b5d05e4e7cfce469183cf06cb-Step8.jpg?w=840&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=e0dc05c9eb5445d4f9b9b4b87000e3f4 840w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a268dc3fbe5ec21efbd083196849729543a8da4b5d05e4e7cfce469183cf06cb-Step8.jpg?w=1100&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=d78ac6193f030c375ecb1241d29dd38d 1100w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a268dc3fbe5ec21efbd083196849729543a8da4b5d05e4e7cfce469183cf06cb-Step8.jpg?w=1650&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=6d745f74916151691de473f30a031860 1650w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a268dc3fbe5ec21efbd083196849729543a8da4b5d05e4e7cfce469183cf06cb-Step8.jpg?w=2500&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=782fa23ffc9b422b75c508a878fa1d5c 2500w" />
</Frame>

After that, visit the Docker website and download and install the version designed for the "**Apple Chip**." Downloading the Docker file may take some time, so please be patient..

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ed0ff6d93b2af567a5770329213d7d19abbf55718e2853b78be0cb61353f4712-Step1.jpg?fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=9062e55a315869d72e4a70965f477966" alt="" className="mx-auto" style={{ width:"69%" }} data-og-width="2124" width="2124" data-og-height="1444" height="1444" data-path="images/docs/ed0ff6d93b2af567a5770329213d7d19abbf55718e2853b78be0cb61353f4712-Step1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ed0ff6d93b2af567a5770329213d7d19abbf55718e2853b78be0cb61353f4712-Step1.jpg?w=280&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=17bf353bdeba669a09ea84dd923c8436 280w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ed0ff6d93b2af567a5770329213d7d19abbf55718e2853b78be0cb61353f4712-Step1.jpg?w=560&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=e9f9b8feaf83de6948dab70a3a4e29da 560w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ed0ff6d93b2af567a5770329213d7d19abbf55718e2853b78be0cb61353f4712-Step1.jpg?w=840&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=2d3304cd8e8849582c557cf524001959 840w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ed0ff6d93b2af567a5770329213d7d19abbf55718e2853b78be0cb61353f4712-Step1.jpg?w=1100&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=c3cb2c94a3e1c1015afb110ad0121fe6 1100w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ed0ff6d93b2af567a5770329213d7d19abbf55718e2853b78be0cb61353f4712-Step1.jpg?w=1650&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=1a68261e49b163edca6ea7a251009c9d 1650w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ed0ff6d93b2af567a5770329213d7d19abbf55718e2853b78be0cb61353f4712-Step1.jpg?w=2500&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=acf50f28407d9b44d0cff10e31234391 2500w" />
</Frame>

### Waiting for IO Containers to Start

Ensure the "**Use containerd for storing and pulling images**" option is **disabled** in Docker's General Settings.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5b05896a180bbf6c4b0c344f8c6a2ab29a7102cf5a3aa29bcabb956d99ae1789-DockerIssue1.jpg?fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=e0da3d8149e7c0bf6317ced681ca455e" alt="" data-og-width="2056" width="2056" data-og-height="1202" height="1202" data-path="images/docs/5b05896a180bbf6c4b0c344f8c6a2ab29a7102cf5a3aa29bcabb956d99ae1789-DockerIssue1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5b05896a180bbf6c4b0c344f8c6a2ab29a7102cf5a3aa29bcabb956d99ae1789-DockerIssue1.jpg?w=280&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=8fe7d8b9d01daa0a61fc8a97359f7fb3 280w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5b05896a180bbf6c4b0c344f8c6a2ab29a7102cf5a3aa29bcabb956d99ae1789-DockerIssue1.jpg?w=560&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=0cf1a247c9038e6046dd75850c5a99ec 560w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5b05896a180bbf6c4b0c344f8c6a2ab29a7102cf5a3aa29bcabb956d99ae1789-DockerIssue1.jpg?w=840&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=d993fda6a901e60a9f0332551b71cca6 840w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5b05896a180bbf6c4b0c344f8c6a2ab29a7102cf5a3aa29bcabb956d99ae1789-DockerIssue1.jpg?w=1100&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=bee64d52903f021286fdcb0e3706d300 1100w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5b05896a180bbf6c4b0c344f8c6a2ab29a7102cf5a3aa29bcabb956d99ae1789-DockerIssue1.jpg?w=1650&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=a77ffd5d247aaa34ceeba7bf6026731d 1650w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5b05896a180bbf6c4b0c344f8c6a2ab29a7102cf5a3aa29bcabb956d99ae1789-DockerIssue1.jpg?w=2500&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=685371e2b23ff07fd559305653eb03a1 2500w" />
</Frame>

Containerd may interfere with Docker’s default image management, **so it’s recommended to turn it off**.

## Worker Disconnecting Despite Containers Running

If your Worker disconnects even when the containers are up, try the following checks:

1. Ensure resources aren't limited. Make sure Docker's "**Resource Saver**" feature is **disabled** in the **Resources tab** of **Docker Settings**.

   <Frame>
       <img src="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/fca1d421123b295103d84f08b0214060405a6f1038f3a7f025185caeb7c8abab-DockerIssue5.jpg?fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=4ef0b3db77f94415eabcf2398e752f7c" alt="" data-og-width="2056" width="2056" data-og-height="1202" height="1202" data-path="images/docs/fca1d421123b295103d84f08b0214060405a6f1038f3a7f025185caeb7c8abab-DockerIssue5.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/fca1d421123b295103d84f08b0214060405a6f1038f3a7f025185caeb7c8abab-DockerIssue5.jpg?w=280&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=4299b9144c9c3688393058c918a82b11 280w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/fca1d421123b295103d84f08b0214060405a6f1038f3a7f025185caeb7c8abab-DockerIssue5.jpg?w=560&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=f8af31ae477bfb2ce31fd63763fd1dfe 560w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/fca1d421123b295103d84f08b0214060405a6f1038f3a7f025185caeb7c8abab-DockerIssue5.jpg?w=840&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=9da89c0c4edfaa153420796e39d3d113 840w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/fca1d421123b295103d84f08b0214060405a6f1038f3a7f025185caeb7c8abab-DockerIssue5.jpg?w=1100&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=e2fd179ab6408216f9d66873e3d634d3 1100w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/fca1d421123b295103d84f08b0214060405a6f1038f3a7f025185caeb7c8abab-DockerIssue5.jpg?w=1650&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=5183b14cfc2ff8f536a5b438339d0c58 1650w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/fca1d421123b295103d84f08b0214060405a6f1038f3a7f025185caeb7c8abab-DockerIssue5.jpg?w=2500&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=aad38da1eabd6c381e9eb182b72c4174 2500w" />
   </Frame>
2. Check Docker Resource Allocation. Ensure Docker is allocated the minimum required **CPU**, **RAM**, and **disk space**. System requirements are as follows:
   * **Memory**: At least 512MB of free RAM (2GB is recommended)
   * **Disk**: Adequate storage to run the Docker containers you intend to use
   * **GPU**: You can check the currently supported [GPUs](/guides/workers/supported-devices).

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
  <img src="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/37c7c1b2c41928a6d66458a8db5dadbf926f4e769866e45f089cdbfbcce87ec0-DockerIssue6.2.jpg?fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=f751a881192826b0321a776b640daf3f" alt="" className="mx-auto" style={{ width:"75%" }} data-og-width="1295" width="1295" data-og-height="1382" height="1382" data-path="images/docs/37c7c1b2c41928a6d66458a8db5dadbf926f4e769866e45f089cdbfbcce87ec0-DockerIssue6.2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/37c7c1b2c41928a6d66458a8db5dadbf926f4e769866e45f089cdbfbcce87ec0-DockerIssue6.2.jpg?w=280&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=2d2c773792981700df1914311cd11604 280w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/37c7c1b2c41928a6d66458a8db5dadbf926f4e769866e45f089cdbfbcce87ec0-DockerIssue6.2.jpg?w=560&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=294e386f9bc3cea4a592151bf98747c6 560w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/37c7c1b2c41928a6d66458a8db5dadbf926f4e769866e45f089cdbfbcce87ec0-DockerIssue6.2.jpg?w=840&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=1f95a643d93e2fb1a0bc36ff8fde7d7c 840w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/37c7c1b2c41928a6d66458a8db5dadbf926f4e769866e45f089cdbfbcce87ec0-DockerIssue6.2.jpg?w=1100&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=39117a47d580df05e4f242a16e0fe6c1 1100w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/37c7c1b2c41928a6d66458a8db5dadbf926f4e769866e45f089cdbfbcce87ec0-DockerIssue6.2.jpg?w=1650&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=f03b1c5089eaac72c4a39297f4040eee 1650w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/37c7c1b2c41928a6d66458a8db5dadbf926f4e769866e45f089cdbfbcce87ec0-DockerIssue6.2.jpg?w=2500&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=a3391e69ef02d1c4aad6c7596eae631b 2500w" />
</Frame>

We recommend running similar speed tests periodically within your containers to monitor connectivity performance. You can also guide users on how to perform these tests at regular intervals or during specific instances for troubleshooting.
