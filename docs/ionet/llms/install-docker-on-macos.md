# Source: https://io.net/docs/guides/workers/install-docker-on-macos.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MacOS: Install Docker

> A step-by-step guide for installing Docker on MacOS-based machines.

<iframe width="100%" src="https://www.youtube.com/embed/EIbheOuHpOI" title="Docker Guide for MacOS" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

### What is Docker?

Let's take a quick look at what Docker is? Imagine Docker as a magic box where you put your software and everything it needs to run. This box can be easily carried to any computer, and when you open it, your software works just the way you packed it, without needing anything extra from that computer. Here are a few steps to install Docker:

### 1. Download Docker

Go to the [Docker website](https://www.docker.com/products/docker-desktop/) and click on "**Download for Mac - Apple Chip.**"

Downloading the Docker file may take some time. Please be patient.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0ffabf70a17c1d2ecd014da5fb1aa694df810f39530f6ede923eb2032f11c294-Step1.jpg?fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=0b5bac848ae1ec215abb20eed1865840" alt="" data-og-width="2124" width="2124" data-og-height="1444" height="1444" data-path="images/docs/0ffabf70a17c1d2ecd014da5fb1aa694df810f39530f6ede923eb2032f11c294-Step1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0ffabf70a17c1d2ecd014da5fb1aa694df810f39530f6ede923eb2032f11c294-Step1.jpg?w=280&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=a155fc4561b9cb9c47f4b4d5ec1e2c58 280w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0ffabf70a17c1d2ecd014da5fb1aa694df810f39530f6ede923eb2032f11c294-Step1.jpg?w=560&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=ecb38a6d86c24af98bf10531b8b0a805 560w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0ffabf70a17c1d2ecd014da5fb1aa694df810f39530f6ede923eb2032f11c294-Step1.jpg?w=840&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=f8e413d57e054f7c49fd8f7eff56710e 840w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0ffabf70a17c1d2ecd014da5fb1aa694df810f39530f6ede923eb2032f11c294-Step1.jpg?w=1100&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=dc8b14b61237b20975c1f6e46537b518 1100w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0ffabf70a17c1d2ecd014da5fb1aa694df810f39530f6ede923eb2032f11c294-Step1.jpg?w=1650&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=62249265d16cc0deb0c551733f8fcd6e 1650w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0ffabf70a17c1d2ecd014da5fb1aa694df810f39530f6ede923eb2032f11c294-Step1.jpg?w=2500&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=69f2c13d4306c8679cd8661b9661216a 2500w" />
</Frame>

### 2. Open the docker.dmg File and Drag It Into the Applications Folder

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6cde349-Step2.jpg?fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=2fe33ee26d17defcc4b1a28397980f96" alt="" className="mx-auto" style={{ width:"63%" }} data-og-width="1364" width="1364" data-og-height="706" height="706" data-path="images/docs/6cde349-Step2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6cde349-Step2.jpg?w=280&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=34342abae4565e636db58fd3aea3b675 280w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6cde349-Step2.jpg?w=560&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=5db0a94e0f5593a7a07ddabc8dc8e135 560w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6cde349-Step2.jpg?w=840&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=17e387f5c6d599353e1706eefddee5a5 840w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6cde349-Step2.jpg?w=1100&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=a3c3ff1b4cae4c26b0393e93fb07a28a 1100w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6cde349-Step2.jpg?w=1650&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=b19e27d6e149d4b22914d7abfd6451d7 1650w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6cde349-Step2.jpg?w=2500&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=c2222dadb7d322bc4aedfe63003e59f2 2500w" />
</Frame>

### 3. Start the Docker Installation From the Applications Folder

We recommend using the recommended settings during the installation wizard.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4eda55c186520c2223b78563edbbb047033d956cd780f898bb143b0d34b34e4c-Step3.jpg?fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=623faf0f1d9444f6bcb947dbe8abc96b" alt="" className="mx-auto" style={{ width:"73%" }} data-og-width="1402" width="1402" data-og-height="1004" height="1004" data-path="images/docs/4eda55c186520c2223b78563edbbb047033d956cd780f898bb143b0d34b34e4c-Step3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4eda55c186520c2223b78563edbbb047033d956cd780f898bb143b0d34b34e4c-Step3.jpg?w=280&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=3d1f605f5e9b0d8aaa1852e840587846 280w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4eda55c186520c2223b78563edbbb047033d956cd780f898bb143b0d34b34e4c-Step3.jpg?w=560&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=e9de9d1a43b3504fae6b78cc24cce95d 560w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4eda55c186520c2223b78563edbbb047033d956cd780f898bb143b0d34b34e4c-Step3.jpg?w=840&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=b64f1a239ae066110586acf5d3861627 840w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4eda55c186520c2223b78563edbbb047033d956cd780f898bb143b0d34b34e4c-Step3.jpg?w=1100&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=c646012d007d71b835d093e25157c46a 1100w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4eda55c186520c2223b78563edbbb047033d956cd780f898bb143b0d34b34e4c-Step3.jpg?w=1650&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=c66d63ec086768b03ae2fe9bf40ccfe1 1650w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4eda55c186520c2223b78563edbbb047033d956cd780f898bb143b0d34b34e4c-Step3.jpg?w=2500&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=1dc02470a410d1f45252799be145f68e 2500w" />
</Frame>

### 4. Open  Terminal Through Launchpad

Click the Launchpad icon in the Dock, type Terminal in the search field, then click Terminal

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7acc67f5656643749054e5dd9f6a39772cf8f7348f903cbbb925d83cc0f28c3b-Step4.jpg?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=f561dc3564c73e996e09550a9e26e4df" alt="" className="mx-auto" style={{ width:"64%" }} data-og-width="1830" width="1830" data-og-height="998" height="998" data-path="images/docs/7acc67f5656643749054e5dd9f6a39772cf8f7348f903cbbb925d83cc0f28c3b-Step4.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7acc67f5656643749054e5dd9f6a39772cf8f7348f903cbbb925d83cc0f28c3b-Step4.jpg?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=9c1137a1884160cf72435f1ce8228725 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7acc67f5656643749054e5dd9f6a39772cf8f7348f903cbbb925d83cc0f28c3b-Step4.jpg?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=12465a9d5aa191255741b2564cf2af5a 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7acc67f5656643749054e5dd9f6a39772cf8f7348f903cbbb925d83cc0f28c3b-Step4.jpg?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=ca58aeb3d2e29d1bf1371b7e4e1a6966 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7acc67f5656643749054e5dd9f6a39772cf8f7348f903cbbb925d83cc0f28c3b-Step4.jpg?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=4b5b04a46004493e823abeefcc41c11d 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7acc67f5656643749054e5dd9f6a39772cf8f7348f903cbbb925d83cc0f28c3b-Step4.jpg?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=e86f55363977f435960ef206d7498e0f 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7acc67f5656643749054e5dd9f6a39772cf8f7348f903cbbb925d83cc0f28c3b-Step4.jpg?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=22a25a073a87c5e10ce96b4692d52623 2500w" />
</Frame>

### 5. Verify the Installation in Terminal

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e901826dcc950343214ce2a5f06d6e6bc757b49adcfc715a8f143ddf8eb29ebc-Step5mac.jpeg?fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=9696b3cb0f9ae22f9dff35ceeee9762a" alt="" className="mx-auto" style={{ width:"47%" }} data-og-width="1380" width="1380" data-og-height="600" height="600" data-path="images/docs/e901826dcc950343214ce2a5f06d6e6bc757b49adcfc715a8f143ddf8eb29ebc-Step5mac.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e901826dcc950343214ce2a5f06d6e6bc757b49adcfc715a8f143ddf8eb29ebc-Step5mac.jpeg?w=280&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=08af8d8a6e1018f2a28b958c8574a502 280w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e901826dcc950343214ce2a5f06d6e6bc757b49adcfc715a8f143ddf8eb29ebc-Step5mac.jpeg?w=560&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=4d3b1723f765ede9b189b444d7daf494 560w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e901826dcc950343214ce2a5f06d6e6bc757b49adcfc715a8f143ddf8eb29ebc-Step5mac.jpeg?w=840&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=eb674b4036aed17302b6b59669750874 840w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e901826dcc950343214ce2a5f06d6e6bc757b49adcfc715a8f143ddf8eb29ebc-Step5mac.jpeg?w=1100&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=17dda7e3d3eb1340667db7f9d4940a81 1100w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e901826dcc950343214ce2a5f06d6e6bc757b49adcfc715a8f143ddf8eb29ebc-Step5mac.jpeg?w=1650&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=c0960ff53f23e17ac31aa3dae2f0050c 1650w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e901826dcc950343214ce2a5f06d6e6bc757b49adcfc715a8f143ddf8eb29ebc-Step5mac.jpeg?w=2500&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=a0e04065107f6fdf0f3e65d462a79be0 2500w" />
</Frame>

Copy and paste the following line into Terminal.

<CodeGroup>
  ```Text Terminal Command theme={null}
  docker --version
  ```
</CodeGroup>

The result will be the current version of Docker.

```
Docker version 24.0.6, build ed223bc
```

### Expanding Virtual Disk Limit

1. Click **Settings**.
2. Go to **Resources** on the left nav.

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/09b563bbd55cf92dc1979014994315fd6c16510df311303f8e2eb10436ed98d0-IO_docker_resources_left_nav.png?fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=9c997ee1ea13205dbb6242c2d39d89bc" alt={true} className="mx-auto" style={{ width:"35%" }} data-og-width="270" width="270" data-og-height="555" height="555" data-path="images/docs/09b563bbd55cf92dc1979014994315fd6c16510df311303f8e2eb10436ed98d0-IO_docker_resources_left_nav.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/09b563bbd55cf92dc1979014994315fd6c16510df311303f8e2eb10436ed98d0-IO_docker_resources_left_nav.png?w=280&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=f733bd9b3cd4823498d5578e34c29146 280w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/09b563bbd55cf92dc1979014994315fd6c16510df311303f8e2eb10436ed98d0-IO_docker_resources_left_nav.png?w=560&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=85d8c63e72d4d243fa1e2a2916750aa9 560w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/09b563bbd55cf92dc1979014994315fd6c16510df311303f8e2eb10436ed98d0-IO_docker_resources_left_nav.png?w=840&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=cf84073a357aa90de34fdc0d91318d1a 840w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/09b563bbd55cf92dc1979014994315fd6c16510df311303f8e2eb10436ed98d0-IO_docker_resources_left_nav.png?w=1100&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=c9cd40fa153b5c239682e7e96668e60d 1100w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/09b563bbd55cf92dc1979014994315fd6c16510df311303f8e2eb10436ed98d0-IO_docker_resources_left_nav.png?w=1650&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=59e6eb67c67af4bfec5cd7e9bdc76272 1650w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/09b563bbd55cf92dc1979014994315fd6c16510df311303f8e2eb10436ed98d0-IO_docker_resources_left_nav.png?w=2500&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=51972cf6051374793cb7967082177164 2500w" />
   </Frame>
3. Check the amount of space shown under **Virtual disk limit**. **Note:** Docker does not natively assign all of your disk space.

   <Frame>
       <img src="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ff1f4b08df586b67e267c8cd17be9b7f6638f4485495b4885a8b08f808a788a4-IO_virtual_disk_limit_macos.png?fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=0dfb60ec9c0885714e416b1c95221075" alt="" data-og-width="479" width="479" data-og-height="99" height="99" data-path="images/docs/ff1f4b08df586b67e267c8cd17be9b7f6638f4485495b4885a8b08f808a788a4-IO_virtual_disk_limit_macos.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ff1f4b08df586b67e267c8cd17be9b7f6638f4485495b4885a8b08f808a788a4-IO_virtual_disk_limit_macos.png?w=280&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=2dff7f9a9ac0eb6f1b2c35b705c55842 280w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ff1f4b08df586b67e267c8cd17be9b7f6638f4485495b4885a8b08f808a788a4-IO_virtual_disk_limit_macos.png?w=560&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=54a6bf30eb6c9b62fef3cf615eadfe49 560w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ff1f4b08df586b67e267c8cd17be9b7f6638f4485495b4885a8b08f808a788a4-IO_virtual_disk_limit_macos.png?w=840&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=1cb0bc17db2e146849b907eabf2103a1 840w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ff1f4b08df586b67e267c8cd17be9b7f6638f4485495b4885a8b08f808a788a4-IO_virtual_disk_limit_macos.png?w=1100&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=5163687eff3f87ad07b7830d2dae8a80 1100w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ff1f4b08df586b67e267c8cd17be9b7f6638f4485495b4885a8b08f808a788a4-IO_virtual_disk_limit_macos.png?w=1650&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=aa6b45217f76491409668b2b33b06142 1650w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ff1f4b08df586b67e267c8cd17be9b7f6638f4485495b4885a8b08f808a788a4-IO_virtual_disk_limit_macos.png?w=2500&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=48961903c0f316fbde789c90cd4076ac 2500w" />
   </Frame>
4. Drag the slider to your desired virtual disk limit amount.
5. Click **Apply & restart**.

### Congratulations on Successfully Setting up Docker

Now that Docker has been successfully installed and is running, you can proceed with [setting up the Worker](/guides/workers/install-on-macos).

<Info>
  Feel free to [check our knowledge base](https://support.io.net/en/support/home) for answers, and if you still need help, don’t hesitate to open a support ticket!
</Info>
