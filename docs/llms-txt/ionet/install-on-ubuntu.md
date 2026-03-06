# Source: https://io.net/docs/guides/workers/install-on-ubuntu.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> A step-by-step guide for setting up the environment for io.net on Ubuntu-based machines.

<iframe width="100%" src="https://www.youtube.com/embed/NwsW-usiMwI" title="IO Worker Guide for Linux" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

### Before Starting

##### 1. Open the Ubuntu Terminal through the Start Menu.

**Terminal** is a tool on your computer that lets you type in commands to tell the computer what to do. Instead of clicking on things with a mouse, you write instructions, and the computer follows them. It's like talking directly to your computer using text.

Click the **Start Menu** icon, start typing "**Terminal**" in the search field, then click the **Terminal** icon:

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8517ea8baf36302c57bf3a61da4ea487bbcfa11568ddfe8b6cc92f621f39a8d8-Step0-1.jpg?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=efbcbf4cba0341720725306b12ccc7d2" alt="" className="mx-auto" style={{ width:"65%" }} data-og-width="1830" width="1830" data-og-height="1036" height="1036" data-path="images/docs/8517ea8baf36302c57bf3a61da4ea487bbcfa11568ddfe8b6cc92f621f39a8d8-Step0-1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8517ea8baf36302c57bf3a61da4ea487bbcfa11568ddfe8b6cc92f621f39a8d8-Step0-1.jpg?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=732426dda8418ebe2de5951b89e7f888 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8517ea8baf36302c57bf3a61da4ea487bbcfa11568ddfe8b6cc92f621f39a8d8-Step0-1.jpg?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=1d0ab3f56497bdf824b7eac3a09c4dbd 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8517ea8baf36302c57bf3a61da4ea487bbcfa11568ddfe8b6cc92f621f39a8d8-Step0-1.jpg?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=27bc18dc99e4d6f055b2b3d5e9ee2009 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8517ea8baf36302c57bf3a61da4ea487bbcfa11568ddfe8b6cc92f621f39a8d8-Step0-1.jpg?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=98482a08c93253e944aeef73bf464687 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8517ea8baf36302c57bf3a61da4ea487bbcfa11568ddfe8b6cc92f621f39a8d8-Step0-1.jpg?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=bf90997486bd6b54ca70fdd0b757c151 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8517ea8baf36302c57bf3a61da4ea487bbcfa11568ddfe8b6cc92f621f39a8d8-Step0-1.jpg?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=f27cf5b7a03bd322d3e75173546cf98b 2500w" />
</Frame>

##### 2. Verify Your Ubuntu Version

For Linux users, ensure that your system is running Ubuntu 20.04 or later. You can check your Ubuntu version by executing the following command in the terminal.

<Info>
  We recommend that you use Ubuntu 22.04 LTS.
</Info>

```
lsb_release -a
```

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/ae306f4207b78534e59c457af2b16ba289b926cf3cc38ac108753f5c5230701a-Step0-2.jpg?fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=76f7e221c31eb0ac56e5178cfb0716ed" alt="" className="mx-auto" style={{ width:"65%" }} data-og-width="1182" width="1182" data-og-height="700" height="700" data-path="images/docs/ae306f4207b78534e59c457af2b16ba289b926cf3cc38ac108753f5c5230701a-Step0-2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/ae306f4207b78534e59c457af2b16ba289b926cf3cc38ac108753f5c5230701a-Step0-2.jpg?w=280&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=a33b6c1e67afe0bd07ce8685523e5c7f 280w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/ae306f4207b78534e59c457af2b16ba289b926cf3cc38ac108753f5c5230701a-Step0-2.jpg?w=560&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=79bcd5f5d20a57c134992862ae2d7eae 560w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/ae306f4207b78534e59c457af2b16ba289b926cf3cc38ac108753f5c5230701a-Step0-2.jpg?w=840&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=1087eda437a2b623b578b03d1371e275 840w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/ae306f4207b78534e59c457af2b16ba289b926cf3cc38ac108753f5c5230701a-Step0-2.jpg?w=1100&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=1968bae9a6058044f608e5d473586128 1100w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/ae306f4207b78534e59c457af2b16ba289b926cf3cc38ac108753f5c5230701a-Step0-2.jpg?w=1650&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=f8d55d3fa4dce6e0e8406b92da7214c0 1650w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/ae306f4207b78534e59c457af2b16ba289b926cf3cc38ac108753f5c5230701a-Step0-2.jpg?w=2500&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=a06b74e94a5f3bebfec317a3757413bc 2500w" />
</Frame>

##### 3. CPU Requirement for Linux

We currently support AMD & Intel processors. You can find all supported processor and video card models [found here](/guides/workers/supported-devices).

To check your processor type, use the following command in the terminal:

```
lscpu
```

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3a7aa65b8e36befd16e86476a5c1cc78d1ce6bc34c99e687f1276bb4c52545bb-Step0-3.jpg?fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=e36e2a12123dcb78f7ad1b3c37582617" alt="" className="mx-auto" style={{ width:"62%" }} data-og-width="1240" width="1240" data-og-height="1214" height="1214" data-path="images/docs/3a7aa65b8e36befd16e86476a5c1cc78d1ce6bc34c99e687f1276bb4c52545bb-Step0-3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3a7aa65b8e36befd16e86476a5c1cc78d1ce6bc34c99e687f1276bb4c52545bb-Step0-3.jpg?w=280&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=eb8533ef89558a58b42b35ef610c5c3f 280w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3a7aa65b8e36befd16e86476a5c1cc78d1ce6bc34c99e687f1276bb4c52545bb-Step0-3.jpg?w=560&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=3dc073a782197e0c6c60d9cc2c0175d0 560w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3a7aa65b8e36befd16e86476a5c1cc78d1ce6bc34c99e687f1276bb4c52545bb-Step0-3.jpg?w=840&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=772fac2ec2adc0f4cfe61e29c95de793 840w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3a7aa65b8e36befd16e86476a5c1cc78d1ce6bc34c99e687f1276bb4c52545bb-Step0-3.jpg?w=1100&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=4d452c63970f8599c13347ff31ddfa68 1100w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3a7aa65b8e36befd16e86476a5c1cc78d1ce6bc34c99e687f1276bb4c52545bb-Step0-3.jpg?w=1650&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=5a533fe742a394f02843304697e909d3 1650w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3a7aa65b8e36befd16e86476a5c1cc78d1ce6bc34c99e687f1276bb4c52545bb-Step0-3.jpg?w=2500&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=da2eb5706e6a8473631a552441918838 2500w" />
</Frame>

### Go to [cloud.io.net](https://cloud.io.net)

If you have not yet created an account, you can sign up on [io.net](http://io.net) using Google, Apple ID, GitHub, Hugging Face, X, Worldcoin, or simply with a one-time password by clicking the "Login with Email" button.

<img src="https://mintcdn.com/ionet-cca8037f/1nusXKdPVUHoDz-x/images/docs/login_process/newlogin1.jpg?fit=max&auto=format&n=1nusXKdPVUHoDz-x&q=85&s=470902a5e8a08e075157120cae667cd7" alt="Newlogin1 Jp" data-og-width="1868" width="1868" data-og-height="1058" height="1058" data-path="images/docs/login_process/newlogin1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/1nusXKdPVUHoDz-x/images/docs/login_process/newlogin1.jpg?w=280&fit=max&auto=format&n=1nusXKdPVUHoDz-x&q=85&s=129a29b9bac3df741db40e99bda417d2 280w, https://mintcdn.com/ionet-cca8037f/1nusXKdPVUHoDz-x/images/docs/login_process/newlogin1.jpg?w=560&fit=max&auto=format&n=1nusXKdPVUHoDz-x&q=85&s=4b7d81b89eb0b45a1c968b111b852850 560w, https://mintcdn.com/ionet-cca8037f/1nusXKdPVUHoDz-x/images/docs/login_process/newlogin1.jpg?w=840&fit=max&auto=format&n=1nusXKdPVUHoDz-x&q=85&s=7a6eb785992b9c0ecf6d76c5b0a9c3cf 840w, https://mintcdn.com/ionet-cca8037f/1nusXKdPVUHoDz-x/images/docs/login_process/newlogin1.jpg?w=1100&fit=max&auto=format&n=1nusXKdPVUHoDz-x&q=85&s=076a5c9517bc68d1a06efc5429ce5c8a 1100w, https://mintcdn.com/ionet-cca8037f/1nusXKdPVUHoDz-x/images/docs/login_process/newlogin1.jpg?w=1650&fit=max&auto=format&n=1nusXKdPVUHoDz-x&q=85&s=900b615e45f5d691226cbc7930a1ea3d 1650w, https://mintcdn.com/ionet-cca8037f/1nusXKdPVUHoDz-x/images/docs/login_process/newlogin1.jpg?w=2500&fit=max&auto=format&n=1nusXKdPVUHoDz-x&q=85&s=fd4ba61049c65504f7c2b618ed7762d3 2500w" />

### 1. From IO Elements Navigate to IO Worker

IO Elements serves as your new control panel for navigating the service efficiently. Click on **IO Worker** to delve deeper into its functionalities and features.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/29ccbbb2af3011e0d4b8324cc218a16e4613e048ac672c208ce3585122b9231f-Step2.jpg?fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=143f2a3e74053799589a5c48b34fd569" alt="" className="mx-auto" style={{ width:"65%" }} data-og-width="735" width="735" data-og-height="539" height="539" data-path="images/docs/29ccbbb2af3011e0d4b8324cc218a16e4613e048ac672c208ce3585122b9231f-Step2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/29ccbbb2af3011e0d4b8324cc218a16e4613e048ac672c208ce3585122b9231f-Step2.jpg?w=280&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=4999a912058968587c2cd6f34eddf569 280w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/29ccbbb2af3011e0d4b8324cc218a16e4613e048ac672c208ce3585122b9231f-Step2.jpg?w=560&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=941e13a9a3756828121577386f438a1c 560w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/29ccbbb2af3011e0d4b8324cc218a16e4613e048ac672c208ce3585122b9231f-Step2.jpg?w=840&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=d93c2717c6cddd73446cff868a193e35 840w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/29ccbbb2af3011e0d4b8324cc218a16e4613e048ac672c208ce3585122b9231f-Step2.jpg?w=1100&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=1804d5fcc8e7440a222d220837dfecaf 1100w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/29ccbbb2af3011e0d4b8324cc218a16e4613e048ac672c208ce3585122b9231f-Step2.jpg?w=1650&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=7972b5b95830b0d3f856a77699879d74 1650w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/29ccbbb2af3011e0d4b8324cc218a16e4613e048ac672c208ce3585122b9231f-Step2.jpg?w=2500&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=5c3fe0daf08b434b56f15377cc6c894c 2500w" />
</Frame>

### 2. Use "Connect New Worker" Button to Open the Wizard

If Workers have not yet been added, you can use the central button. If the screen is full of information, find the same button in the upper right corner.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3be64991eafe5044d5c65c8d340757f14235c2817d07841ded76148e8206b2ab-Step3.jpg?fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=bbc45df60e9da22f3cb3e13401e727aa" alt="" className="mx-auto" style={{ width:"58%" }} data-og-width="735" width="735" data-og-height="539" height="539" data-path="images/docs/3be64991eafe5044d5c65c8d340757f14235c2817d07841ded76148e8206b2ab-Step3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3be64991eafe5044d5c65c8d340757f14235c2817d07841ded76148e8206b2ab-Step3.jpg?w=280&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=90a2640cd3b85eefd87df561dcf89ac6 280w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3be64991eafe5044d5c65c8d340757f14235c2817d07841ded76148e8206b2ab-Step3.jpg?w=560&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=3d5198c7f802730943afa2078993a228 560w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3be64991eafe5044d5c65c8d340757f14235c2817d07841ded76148e8206b2ab-Step3.jpg?w=840&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=cc9f03bb291e28b477f72625c22c25a8 840w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3be64991eafe5044d5c65c8d340757f14235c2817d07841ded76148e8206b2ab-Step3.jpg?w=1100&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=e3389f0b55fd660ef7578f3b236b3751 1100w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3be64991eafe5044d5c65c8d340757f14235c2817d07841ded76148e8206b2ab-Step3.jpg?w=1650&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=4c906144e8c33c25990c7ec41fcf5308 1650w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3be64991eafe5044d5c65c8d340757f14235c2817d07841ded76148e8206b2ab-Step3.jpg?w=2500&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=51b39fe0251b6a937c16d3f28c71e348 2500w" />
</Frame>

### 3. Name Your Device

Click the "**Pencil**" icon to open the popup for editing the device name.

Please add a unique name for your device. An ideal format would be something like this: **My-Test-Device** .

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/70d65eb880726dae8e578bce534e1213fd1f218778ec3c6e2df4e4bfdf652093-Step4.jpg?fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=cdcb67cc83406cf602f33ddfb09c043c" alt="" className="mx-auto" style={{ width:"82%" }} data-og-width="1251" width="1251" data-og-height="561" height="561" data-path="images/docs/70d65eb880726dae8e578bce534e1213fd1f218778ec3c6e2df4e4bfdf652093-Step4.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/70d65eb880726dae8e578bce534e1213fd1f218778ec3c6e2df4e4bfdf652093-Step4.jpg?w=280&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=b8ab76bafa297c9a7618983776e90001 280w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/70d65eb880726dae8e578bce534e1213fd1f218778ec3c6e2df4e4bfdf652093-Step4.jpg?w=560&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=642a1f789bd812ccf5cff4b0ea0c844c 560w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/70d65eb880726dae8e578bce534e1213fd1f218778ec3c6e2df4e4bfdf652093-Step4.jpg?w=840&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=a04ad6b7c08acfd2a11d5e8b0bc58560 840w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/70d65eb880726dae8e578bce534e1213fd1f218778ec3c6e2df4e4bfdf652093-Step4.jpg?w=1100&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=b5416160cd0462fee10dedc286fff374 1100w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/70d65eb880726dae8e578bce534e1213fd1f218778ec3c6e2df4e4bfdf652093-Step4.jpg?w=1650&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=829b9c380700ac7d0d885b7f9c83eeab 1650w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/70d65eb880726dae8e578bce534e1213fd1f218778ec3c6e2df4e4bfdf652093-Step4.jpg?w=2500&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=965e14c8e5462197cddfc554514e5b50 2500w" />
</Frame>

### Select Ubuntu Operating System

Choose the Operating System of your device from MacOS, Windows or **Ubuntu**.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/ac2191e9516f42ccddad1b134243fcadd6919ae6a3f337839019cafbda239853-Step5.jpg?fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=3f8024e894a7fbbbed0abfeae74b9481" alt="" className="mx-auto" style={{ width:"84%" }} data-og-width="1054" width="1054" data-og-height="431" height="431" data-path="images/docs/ac2191e9516f42ccddad1b134243fcadd6919ae6a3f337839019cafbda239853-Step5.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/ac2191e9516f42ccddad1b134243fcadd6919ae6a3f337839019cafbda239853-Step5.jpg?w=280&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=34548fe25687e135cbd8bbeffd218385 280w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/ac2191e9516f42ccddad1b134243fcadd6919ae6a3f337839019cafbda239853-Step5.jpg?w=560&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=f83868b6c0855930d42daf088511561e 560w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/ac2191e9516f42ccddad1b134243fcadd6919ae6a3f337839019cafbda239853-Step5.jpg?w=840&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=fa080f1b3535726030c08ce081415cc9 840w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/ac2191e9516f42ccddad1b134243fcadd6919ae6a3f337839019cafbda239853-Step5.jpg?w=1100&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=1236b9f78398635f9bdae65bd431772f 1100w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/ac2191e9516f42ccddad1b134243fcadd6919ae6a3f337839019cafbda239853-Step5.jpg?w=1650&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=d259b9259b4a7b6881629d091e6fe2e2 1650w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/ac2191e9516f42ccddad1b134243fcadd6919ae6a3f337839019cafbda239853-Step5.jpg?w=2500&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=6ab005067b322f90f2668390cb10e82f 2500w" />
</Frame>

### 5. Select Device Type

You should choose the device type based on your task. A video card is better suited for AI tasks, while a processor is more suitable for graphic rendering.

<Tooltip tip="GPU – Graphics Processing Unit, is a special computer chip that helps make images and videos appear on your screen faster. It's like a supercharged engine for handling visual tasks, such as gaming, watching videos, and designing graphics. They accelerate the computational tasks involved in training and running machine learning models.">GPU</Tooltip> - This is the part of your computer or laptop that handles graphics - the video card. It's usually from Nvidea or Radeon. You can find a full list of video cards that io.net is compatible with [here](/guides/workers/supported-devices).

<Tooltip tip="CPU – CPU stands for Central Processing Unit. It is the primary component of a computer responsible for executing instructions and performing calculations required to run software programs and operating systems.">CPU</Tooltip> - This forms the core of every smart device in our world, including your computer or laptop. Now, alongside Intel and AMD processors, Apple's processors have also joined the lineup. You can find a comprehensive list of processors compatible with io.net [here](/guides/workers/supported-devices).

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/872107ee75e5126694ade8a5fc8c750406853031910e487ddafa4e9cbe04bee8-Step6.jpg?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=fa9a1e78b45f596bc857bd9ac6d12359" alt="" className="mx-auto" style={{ width:"85%" }} data-og-width="1028" width="1028" data-og-height="941" height="941" data-path="images/docs/872107ee75e5126694ade8a5fc8c750406853031910e487ddafa4e9cbe04bee8-Step6.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/872107ee75e5126694ade8a5fc8c750406853031910e487ddafa4e9cbe04bee8-Step6.jpg?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=52b6fb75022c81d828868d7dc868ff90 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/872107ee75e5126694ade8a5fc8c750406853031910e487ddafa4e9cbe04bee8-Step6.jpg?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=a64f49fc235802101339133601a76b25 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/872107ee75e5126694ade8a5fc8c750406853031910e487ddafa4e9cbe04bee8-Step6.jpg?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=8ee3892b95c2c8a9834695e99227f535 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/872107ee75e5126694ade8a5fc8c750406853031910e487ddafa4e9cbe04bee8-Step6.jpg?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=61f85e2d34dd13ed44230ed95e4f183d 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/872107ee75e5126694ade8a5fc8c750406853031910e487ddafa4e9cbe04bee8-Step6.jpg?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=11e5ced7bbed0a0b2db33e634dd957da 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/872107ee75e5126694ade8a5fc8c750406853031910e487ddafa4e9cbe04bee8-Step6.jpg?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=867c9f202a4ba1370151fb353a93e0ba 2500w" />
</Frame>

You can also verify whether your GPU or CPU is included in the list of devices supported by our service on the wizard page.

<Warning>
  If you select a GPU Worker and your device doesn't have GPU the setup will fail.
</Warning>

### 6. Prerequisites for Ubuntu - One-Time Setup for Hardware

Before proceeding, ensure you have the necessary tools installed on your Ubuntu system (**skip if Docker and NVIDIA driver are already installed and configured**).

<Info>
  Do not install and use beta drivers for Linux.
</Info>

If not, to install IO.Net Setup, follow these steps:

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/018212db70f2912f149a3bb9e4cca955769279517f78c9ce71bef4fd9358a79c-Step7.jpg?fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=1fde49a1c681349b752fd28271ae946f" alt="" className="mx-auto" style={{ width:"83%" }} data-og-width="1974" width="1974" data-og-height="1512" height="1512" data-path="images/docs/018212db70f2912f149a3bb9e4cca955769279517f78c9ce71bef4fd9358a79c-Step7.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/018212db70f2912f149a3bb9e4cca955769279517f78c9ce71bef4fd9358a79c-Step7.jpg?w=280&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=a2dd74056c81d0861f53417b4dde0299 280w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/018212db70f2912f149a3bb9e4cca955769279517f78c9ce71bef4fd9358a79c-Step7.jpg?w=560&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=eac92862903c4a00ba5768d4687db602 560w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/018212db70f2912f149a3bb9e4cca955769279517f78c9ce71bef4fd9358a79c-Step7.jpg?w=840&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=74af9c778e26fca5a0dd87dbc8d0e194 840w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/018212db70f2912f149a3bb9e4cca955769279517f78c9ce71bef4fd9358a79c-Step7.jpg?w=1100&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=48d13b96148e806a7a6cace8b508f3b7 1100w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/018212db70f2912f149a3bb9e4cca955769279517f78c9ce71bef4fd9358a79c-Step7.jpg?w=1650&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=918bf2e4a584411560b32fd7a50448a9 1650w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/018212db70f2912f149a3bb9e4cca955769279517f78c9ce71bef4fd9358a79c-Step7.jpg?w=2500&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=fa032ecdaee80aa48ef847825c17627c 2500w" />
</Frame>

1. Install the desktop IO.NET Setup Script using the installation command in the Terminal:

   ```
   curl -L https://github.com/ionet-official/io-net-official-setup-script/raw/main/ionet-setup.sh -o ionet-setup.sh
   ```

   <Warning>
     ```
     sudo apt install curl 
     ```
   </Warning>
2. Grant permissions to the new IO.NET Setup Script with this command:

   ```
   chmod +x ionet-setup.sh && ./ionet-setup.sh
   ```
3. **For systems equipped with GPUs**, wait for the system to restart. Once it has restarted, run the setup again using the command provided earlier.

<Warning>
  When using SXM or NV Link, ensure that Fabric Manager is [installed correctly](https://docs.nvidia.com/datacenter/tesla/pdf/fabric-manager-user-guide.pdf) and enabled. This will prevent initialization issues and ensure that all GPUs are functioning properly, thereby avoiding PoW verification failures.
</Warning>

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/696627b690cbe33a0067e4a09f76ffaa761288cd598aa3e465c09fa62abba658-Step8.jpg?fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=3a3bcedbe9254588ee3dfdbf267b11a6" alt="" data-og-width="1571" width="1571" data-og-height="1641" height="1641" data-path="images/docs/696627b690cbe33a0067e4a09f76ffaa761288cd598aa3e465c09fa62abba658-Step8.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/696627b690cbe33a0067e4a09f76ffaa761288cd598aa3e465c09fa62abba658-Step8.jpg?w=280&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=4daed60264234bc9925e5aae559ede1e 280w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/696627b690cbe33a0067e4a09f76ffaa761288cd598aa3e465c09fa62abba658-Step8.jpg?w=560&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=8f6dd68f4ba336ff9e43001d431e72fe 560w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/696627b690cbe33a0067e4a09f76ffaa761288cd598aa3e465c09fa62abba658-Step8.jpg?w=840&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=308d26e16aa291c1b2f1d04e33719f83 840w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/696627b690cbe33a0067e4a09f76ffaa761288cd598aa3e465c09fa62abba658-Step8.jpg?w=1100&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=d0fa2c4e63849ac178e82f600b7d1883 1100w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/696627b690cbe33a0067e4a09f76ffaa761288cd598aa3e465c09fa62abba658-Step8.jpg?w=1650&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=59065a5ea773a644da6d6a4e55de2a70 1650w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/696627b690cbe33a0067e4a09f76ffaa761288cd598aa3e465c09fa62abba658-Step8.jpg?w=2500&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=fcfda7f306406eb24ef9ed59c467f3b2 2500w" />
</Frame>

### 7. Download and Launch IO Binary

**IO Binary** is a compiled executable file used to perform computational tasks and manage system operations. It is crucial for the smooth operation of the platform as it handles essential functions directly related to the performance and reliability of the computational resources.

<Warning>
  Do not modify or run code directly in io.net’s docker containers. This may disqualify your device from earning block rewards or being hired. If you have suggestions or ideas for custom code in our Docker containers, contact customer support to suggest them.
</Warning>

In this step, follow these instructions in the Terminal:

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b343c9da6d0333a9fc465e3c7acb0837ff008b49116395dd900c3ce8c85d40d3-Step9.jpg?fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=aff5936eb6953903e65155be9fafa67b" alt="" data-og-width="2098" width="2098" data-og-height="1136" height="1136" data-path="images/docs/b343c9da6d0333a9fc465e3c7acb0837ff008b49116395dd900c3ce8c85d40d3-Step9.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b343c9da6d0333a9fc465e3c7acb0837ff008b49116395dd900c3ce8c85d40d3-Step9.jpg?w=280&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=f8fb7d1f92f21d71d78e3a9ccdf9cb76 280w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b343c9da6d0333a9fc465e3c7acb0837ff008b49116395dd900c3ce8c85d40d3-Step9.jpg?w=560&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=b830a7110bc180414d413b3ad25de7c7 560w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b343c9da6d0333a9fc465e3c7acb0837ff008b49116395dd900c3ce8c85d40d3-Step9.jpg?w=840&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=e8bf7190ffa0ac2eed80e9594416ff68 840w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b343c9da6d0333a9fc465e3c7acb0837ff008b49116395dd900c3ce8c85d40d3-Step9.jpg?w=1100&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=5ee41f8dd396e9a5120d293f93bebc79 1100w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b343c9da6d0333a9fc465e3c7acb0837ff008b49116395dd900c3ce8c85d40d3-Step9.jpg?w=1650&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=5056db94cc38144fb1b4c5785269bb28 1650w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b343c9da6d0333a9fc465e3c7acb0837ff008b49116395dd900c3ce8c85d40d3-Step9.jpg?w=2500&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=76895cabdad943c1d11f987ebf37afd2 2500w" />
</Frame>

1. Download the IO Binary for Ubuntu using the following link:

   ```
   curl -L https://github.com/ionet-official/io_launch_binaries/raw/main/io_net_launch_binary_linux -o io_net_launch_binary_linux
   ```
2. Grant permissions to the new IO Binary with this command:

   ```
   chmod +x io_net_launch_binary_linux
   ```

   <Frame>
       <img src="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/33e2d92e8840064f73aaac67a46177af10376a1cdd97599a1962146473899578-Step10.jpg?fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=6b117533c7dc3cdf24b06cd4eac86faf" alt="" data-og-width="1572" width="1572" data-og-height="693" height="693" data-path="images/docs/33e2d92e8840064f73aaac67a46177af10376a1cdd97599a1962146473899578-Step10.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/33e2d92e8840064f73aaac67a46177af10376a1cdd97599a1962146473899578-Step10.jpg?w=280&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=9eae452595751efcca26de2db5b29455 280w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/33e2d92e8840064f73aaac67a46177af10376a1cdd97599a1962146473899578-Step10.jpg?w=560&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=15507f17dbbf4c3b607710cc6d290a30 560w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/33e2d92e8840064f73aaac67a46177af10376a1cdd97599a1962146473899578-Step10.jpg?w=840&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=602766c726dccd08a8300386ffd22a5e 840w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/33e2d92e8840064f73aaac67a46177af10376a1cdd97599a1962146473899578-Step10.jpg?w=1100&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=f2a34e72f67458437ba780ce64c62899 1100w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/33e2d92e8840064f73aaac67a46177af10376a1cdd97599a1962146473899578-Step10.jpg?w=1650&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=24033321fa31f980a32737b3dd8cfa6a 1650w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/33e2d92e8840064f73aaac67a46177af10376a1cdd97599a1962146473899578-Step10.jpg?w=2500&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=57b0d5e776fdc7129db7c48848e194aa 2500w" />
   </Frame>
3. Copy generated the IO Binary address provided in the wizard and past it into Terminal to run further:

   ```
   ./io_net_launch_binary_linux
   ```

   <Info>
     If you want to disable sleep mode for a device, you can pass the --disable\_sleep\_mode=true argument at the end of the command line.

     ```
     ./io_net_launch_binary_linux --disable_sleep_mode=true
     ```

     You can find more additional arguments to use with the IO Binary command [here](https://github.com/ionet-official/io_launch_binaries?tab=readme-ov-file#usage).
   </Info>

   <Frame>
       <img src="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/13ffdd54332e490e94d96635e76a163211af5445aa20084d8f6670301f46e775-Step11.jpg?fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=6dc99f49a90cba6469401a932edd7dbe" alt="" data-og-width="2098" width="2098" data-og-height="1108" height="1108" data-path="images/docs/13ffdd54332e490e94d96635e76a163211af5445aa20084d8f6670301f46e775-Step11.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/13ffdd54332e490e94d96635e76a163211af5445aa20084d8f6670301f46e775-Step11.jpg?w=280&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=5617671a0d816e92a0bbe5dc547fc2a8 280w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/13ffdd54332e490e94d96635e76a163211af5445aa20084d8f6670301f46e775-Step11.jpg?w=560&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=e7478a2a89f580c79b44fb9993a5d89b 560w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/13ffdd54332e490e94d96635e76a163211af5445aa20084d8f6670301f46e775-Step11.jpg?w=840&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=40a6fc3c036b609d2034691e4649db1f 840w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/13ffdd54332e490e94d96635e76a163211af5445aa20084d8f6670301f46e775-Step11.jpg?w=1100&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=77d0bb175c94f43e96e482c76f42b258 1100w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/13ffdd54332e490e94d96635e76a163211af5445aa20084d8f6670301f46e775-Step11.jpg?w=1650&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=c9098cd4a3449db5cd7e9be532afa2bc 1650w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/13ffdd54332e490e94d96635e76a163211af5445aa20084d8f6670301f46e775-Step11.jpg?w=2500&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=d31449ab11cda3296b6f47223ff8fe81 2500w" />
   </Frame>

### 8. Authorize Your New Device

The IO Binary may prompt you to authorize your new device.

<Info>
  Remember, you have 3 minutes to complete the authorization of the device. If you miss it, you will need to rerun the code again.
</Info>

You can do this in two ways:

1. **Copy the Link from the Terminal**:

   <Frame>
       <img src="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/423a0b7594694de931c5d956fdb2cf6043b8315b8081961d8da38807747e3ca5-Step12.jpg?fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=1443eb3cb785fe380712747f3f56033c" alt="" data-og-width="1611" width="1611" data-og-height="1038" height="1038" data-path="images/docs/423a0b7594694de931c5d956fdb2cf6043b8315b8081961d8da38807747e3ca5-Step12.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/423a0b7594694de931c5d956fdb2cf6043b8315b8081961d8da38807747e3ca5-Step12.jpg?w=280&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=d402048b9cf01ee3b280e1f5165a86c7 280w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/423a0b7594694de931c5d956fdb2cf6043b8315b8081961d8da38807747e3ca5-Step12.jpg?w=560&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=b1c96f5c6e550dffcedd7c56e7c3e9ee 560w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/423a0b7594694de931c5d956fdb2cf6043b8315b8081961d8da38807747e3ca5-Step12.jpg?w=840&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=269b5eb9a6f75f6ab32c2fed5d59a875 840w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/423a0b7594694de931c5d956fdb2cf6043b8315b8081961d8da38807747e3ca5-Step12.jpg?w=1100&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=33c26207313d4d1113a2903047c7a1cd 1100w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/423a0b7594694de931c5d956fdb2cf6043b8315b8081961d8da38807747e3ca5-Step12.jpg?w=1650&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=98d899261fd8050ee3cb9e1e9629b967 1650w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/423a0b7594694de931c5d956fdb2cf6043b8315b8081961d8da38807747e3ca5-Step12.jpg?w=2500&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=e15b6109aaa33f46c8203c1e2aba8ce4 2500w" />
   </Frame>

   Paste it into your browser and confirm the action. After confirmation, the system will prompt you to log in.

   <Frame>
       <img src="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/014e9fce8385b397225aab90811258455daf1c00da5965addb59a3742ddefee7-Step13.jpg?fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=8d14f87d393cc829df9bc2915d860043" alt="" data-og-width="1077" width="1077" data-og-height="564" height="564" data-path="images/docs/014e9fce8385b397225aab90811258455daf1c00da5965addb59a3742ddefee7-Step13.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/014e9fce8385b397225aab90811258455daf1c00da5965addb59a3742ddefee7-Step13.jpg?w=280&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=b01a0dbc06097dfbafe3c82fed15bf4e 280w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/014e9fce8385b397225aab90811258455daf1c00da5965addb59a3742ddefee7-Step13.jpg?w=560&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=6a1cd24045a7820fa67256636c26e69f 560w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/014e9fce8385b397225aab90811258455daf1c00da5965addb59a3742ddefee7-Step13.jpg?w=840&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=8d4f635ec8907b796cb24ef9d26b69a0 840w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/014e9fce8385b397225aab90811258455daf1c00da5965addb59a3742ddefee7-Step13.jpg?w=1100&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=2d32a1bd7d5dfb2527a1d9eb44439113 1100w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/014e9fce8385b397225aab90811258455daf1c00da5965addb59a3742ddefee7-Step13.jpg?w=1650&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=8486829388bbaa4c5cc542232c5f9774 1650w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/014e9fce8385b397225aab90811258455daf1c00da5965addb59a3742ddefee7-Step13.jpg?w=2500&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=cf4c5cce47cbe7d11d8f2e4707923d7f 2500w" />
   </Frame>
2. **Copy the Code from the Terminal**:

   <Frame>
       <img src="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/dfb82203d9afd67d17dc3f378d385d3d9c4968e7dd1604915a2d8c126208de8b-Step14.jpg?fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=765736d94bf53e029f718aa991a56c1e" alt="" data-og-width="1876" width="1876" data-og-height="658" height="658" data-path="images/docs/dfb82203d9afd67d17dc3f378d385d3d9c4968e7dd1604915a2d8c126208de8b-Step14.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/dfb82203d9afd67d17dc3f378d385d3d9c4968e7dd1604915a2d8c126208de8b-Step14.jpg?w=280&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=31801e53d8db4b0c634ac5847022737c 280w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/dfb82203d9afd67d17dc3f378d385d3d9c4968e7dd1604915a2d8c126208de8b-Step14.jpg?w=560&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=f33558f76eb0bdd638be654622e71cef 560w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/dfb82203d9afd67d17dc3f378d385d3d9c4968e7dd1604915a2d8c126208de8b-Step14.jpg?w=840&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=945f00c6a2008744baecaa572e05cea2 840w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/dfb82203d9afd67d17dc3f378d385d3d9c4968e7dd1604915a2d8c126208de8b-Step14.jpg?w=1100&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=22fd5cd9b94b1ae348ed50285b867095 1100w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/dfb82203d9afd67d17dc3f378d385d3d9c4968e7dd1604915a2d8c126208de8b-Step14.jpg?w=1650&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=92cce023cc4350076ae1f95c1fbd33bd 1650w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/dfb82203d9afd67d17dc3f378d385d3d9c4968e7dd1604915a2d8c126208de8b-Step14.jpg?w=2500&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=3b144d1feead243c35f834b21649645d 2500w" />
   </Frame>

   Enter this code on the page [https://auth0.io.solutions/activate](https://auth0.io.solutions/activate) to authorize the device. After it, the system will prompt you to log in.

   <Frame>
       <img src="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/5f07fb0980481ed06c28798520ce170ea7dac0df0de99a64a8369b1c0b9f80ac-Step15.jpg?fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=407a064afddff714211ec4143b4cce6a" alt="" data-og-width="1077" width="1077" data-og-height="564" height="564" data-path="images/docs/5f07fb0980481ed06c28798520ce170ea7dac0df0de99a64a8369b1c0b9f80ac-Step15.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/5f07fb0980481ed06c28798520ce170ea7dac0df0de99a64a8369b1c0b9f80ac-Step15.jpg?w=280&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=5e59569bb82db79874c8fd0116e27bd2 280w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/5f07fb0980481ed06c28798520ce170ea7dac0df0de99a64a8369b1c0b9f80ac-Step15.jpg?w=560&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=acd42f18b5818e9097f11eb0fc5ae6bc 560w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/5f07fb0980481ed06c28798520ce170ea7dac0df0de99a64a8369b1c0b9f80ac-Step15.jpg?w=840&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=61e0cd0cc39d9b8c9f949a5aa48215bd 840w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/5f07fb0980481ed06c28798520ce170ea7dac0df0de99a64a8369b1c0b9f80ac-Step15.jpg?w=1100&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=3222087a3af0287d93127e574a6ddb49 1100w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/5f07fb0980481ed06c28798520ce170ea7dac0df0de99a64a8369b1c0b9f80ac-Step15.jpg?w=1650&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=99b8365a5a0a7e326c2780d6243d1572 1650w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/5f07fb0980481ed06c28798520ce170ea7dac0df0de99a64a8369b1c0b9f80ac-Step15.jpg?w=2500&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=47c4b753dad4a2783dbffef7d845cc3d 2500w" />
   </Frame>

<Info>
  **Onboarding Multiple Devices by Bypassing Interactive Authentication**

  To onboard a new device, use the following command with the **--token** flag:

  <Frame>
        <img src="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4502208042e69315b9ec20958e19099fc793541669e0735a801e63ca157c3fcc-Step16.jpg?fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=010a33fd0e5d12afc15eefd258c6f7a6" alt="" data-og-width="1634" width="1634" data-og-height="580" height="580" data-path="images/docs/4502208042e69315b9ec20958e19099fc793541669e0735a801e63ca157c3fcc-Step16.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4502208042e69315b9ec20958e19099fc793541669e0735a801e63ca157c3fcc-Step16.jpg?w=280&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=6b227b9f67da4e69239659dec2393a57 280w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4502208042e69315b9ec20958e19099fc793541669e0735a801e63ca157c3fcc-Step16.jpg?w=560&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=37bbb7fd51185502c88f688792ac549e 560w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4502208042e69315b9ec20958e19099fc793541669e0735a801e63ca157c3fcc-Step16.jpg?w=840&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=b3a8cf456071f23e7edeca843aa043ed 840w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4502208042e69315b9ec20958e19099fc793541669e0735a801e63ca157c3fcc-Step16.jpg?w=1100&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=4c44a72a38bdd31c8240bc28bd04f383 1100w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4502208042e69315b9ec20958e19099fc793541669e0735a801e63ca157c3fcc-Step16.jpg?w=1650&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=822d0a7dcfbff946e95dd78043b97959 1650w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4502208042e69315b9ec20958e19099fc793541669e0735a801e63ca157c3fcc-Step16.jpg?w=2500&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=b90e96562f5778d96d2e70b4ef35c9e1 2500w" />
  </Frame>

  ```
  ./io_net_launch_binary_linux --token your-token-value
  ```

  This will allow you to bypass the interactive authentication process.
</Info>

### 9. Remove previously installed Docker containers

<Tooltip tip="IO Binary – It's a file that contains executable instructions in a format that a computer can directly execute. It represents a software application in a form that the computer's processor can understand and run.">IO Binary</Tooltip> will ask you questions related to previously installed Docker Containers. To continue the installation of <Tooltip tip="IO Worker – IO Worker is a component of the IO.NET ecosystem that enables users to rent out their computing devices like GPUs and CPUs to those needing computational power. By leasing their device's processing capabilities, users earn rewards for tasks like artificial intelligence computations or rendering. This setup fosters decentralized computing and resource sharing, fostering collaboration and mutual benefit among users on the IO.NET platform.">IO Worker</Tooltip>, you must agree to remove all old containers and proceed by typing: **Yes**

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/fac78e9f33ba9e22f16e2648e6eb05a335cefafaab41e8dd0c0a7b1b951b1307-Step17.jpg?fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=b3f03426c77b3f46b56a1035a139f782" alt="" data-og-width="1453" width="1453" data-og-height="633" height="633" data-path="images/docs/fac78e9f33ba9e22f16e2648e6eb05a335cefafaab41e8dd0c0a7b1b951b1307-Step17.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/fac78e9f33ba9e22f16e2648e6eb05a335cefafaab41e8dd0c0a7b1b951b1307-Step17.jpg?w=280&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=1895f2b20549686a180753c332e923cf 280w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/fac78e9f33ba9e22f16e2648e6eb05a335cefafaab41e8dd0c0a7b1b951b1307-Step17.jpg?w=560&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=252f0948ff345268540c3228e9b73c06 560w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/fac78e9f33ba9e22f16e2648e6eb05a335cefafaab41e8dd0c0a7b1b951b1307-Step17.jpg?w=840&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=c1fbdeb1bd1580fa210bac27a250258a 840w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/fac78e9f33ba9e22f16e2648e6eb05a335cefafaab41e8dd0c0a7b1b951b1307-Step17.jpg?w=1100&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=f56b613aba5939cff574358f39136163 1100w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/fac78e9f33ba9e22f16e2648e6eb05a335cefafaab41e8dd0c0a7b1b951b1307-Step17.jpg?w=1650&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=3189ebc0155a2f1f19c2345501474751 1650w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/fac78e9f33ba9e22f16e2648e6eb05a335cefafaab41e8dd0c0a7b1b951b1307-Step17.jpg?w=2500&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=2c615c042d0523e02052bf0ee1277948 2500w" />
</Frame>

### 10. Waiting for Worker Connection to Complete

IO Binary will install all additional containers and images for your Docker. The process may take some time to complete as it installs additional packages for Docker. Please allow the installation process to finish.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c26b3c9a5a025c5b7a16c8c209c2904bdd8c68bc3e0303468f3bc9125849ab7d-Step18.jpg?fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=1ee0af5a5e683fd2de4e8623a9391234" alt="" data-og-width="1323" width="1323" data-og-height="1467" height="1467" data-path="images/docs/c26b3c9a5a025c5b7a16c8c209c2904bdd8c68bc3e0303468f3bc9125849ab7d-Step18.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c26b3c9a5a025c5b7a16c8c209c2904bdd8c68bc3e0303468f3bc9125849ab7d-Step18.jpg?w=280&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=e0d0ef02b5020bd6fefd690bd4dc6394 280w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c26b3c9a5a025c5b7a16c8c209c2904bdd8c68bc3e0303468f3bc9125849ab7d-Step18.jpg?w=560&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=d9f695b53a5c2d6739a2edfa69b7e409 560w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c26b3c9a5a025c5b7a16c8c209c2904bdd8c68bc3e0303468f3bc9125849ab7d-Step18.jpg?w=840&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=9d2ac81b4888388f0fa012e8fcfa2f4e 840w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c26b3c9a5a025c5b7a16c8c209c2904bdd8c68bc3e0303468f3bc9125849ab7d-Step18.jpg?w=1100&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=2ef4f25a7d2f94ce892e768e361811a8 1100w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c26b3c9a5a025c5b7a16c8c209c2904bdd8c68bc3e0303468f3bc9125849ab7d-Step18.jpg?w=1650&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=288e881b0ef51f6c89e45da88b9a8a98 1650w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c26b3c9a5a025c5b7a16c8c209c2904bdd8c68bc3e0303468f3bc9125849ab7d-Step18.jpg?w=2500&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=514f35ab5c4e9490c793beb394390c0b 2500w" />
</Frame>

Afterward, return to the browser to complete the installation.

You may need to wait for up to 10 minutes while the device checks and connects to the IO ecosystem. If it doesn't connect, reach out to our Support ticket by logging into your [IO.Net account](https://worker.io.net).

<Frame>
  <img src="https://files.readme.io/7059edf-Step13.gif" alt="" className="mx-auto" style={{ width:"72%" }} />
</Frame>

<Warning>
  Please disable power-saving mode when running your devices on IO Net. Power-saving mode can impair device performance, potentially leading to failure in PoW or being classified as not providing adequate computing power.
</Warning>

### Congratulations on Successfully Setting up Your First Worker.

Now that your Worker has been successfully created and is running, you can track its status on the Workers page.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8abd710bde90af9578fe8b0846052e36ac73e2e84069f14ba1ecaacd7c83956a-step20.png?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=01b240795b088b1136f64feb86d4b2a3" alt="" data-og-width="2364" width="2364" data-og-height="702" height="702" data-path="images/docs/8abd710bde90af9578fe8b0846052e36ac73e2e84069f14ba1ecaacd7c83956a-step20.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8abd710bde90af9578fe8b0846052e36ac73e2e84069f14ba1ecaacd7c83956a-step20.png?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=cae179dd964bc6f5b850ebde86ed473a 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8abd710bde90af9578fe8b0846052e36ac73e2e84069f14ba1ecaacd7c83956a-step20.png?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=2c99dbcc6c959a127aac147cda18e282 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8abd710bde90af9578fe8b0846052e36ac73e2e84069f14ba1ecaacd7c83956a-step20.png?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=ba986649c0eb7290df50120b10c7ac2f 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8abd710bde90af9578fe8b0846052e36ac73e2e84069f14ba1ecaacd7c83956a-step20.png?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=99cc87c30161c3243065b9a95472efc1 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8abd710bde90af9578fe8b0846052e36ac73e2e84069f14ba1ecaacd7c83956a-step20.png?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=8fd7d7ab9e38456ff480ea3949c386f3 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8abd710bde90af9578fe8b0846052e36ac73e2e84069f14ba1ecaacd7c83956a-step20.png?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=fc6554e66688b8b43d26b40bb3b336fe 2500w" />
</Frame>

<Info>
  If you're having trouble installing Worker, please refer to our [Worker troubleshooting guide](/guides/workers/troubleshoot-worker-general). If the issue persists or you need further assistance, feel free to [check our knowledge base](https://support.io.net/en/support/home) for answers, and if you still need help, don’t hesitate to open a support ticket
</Info>

<Warning>
  Be aware that you will be installing a 20GB size container. This contains all the packages needed to serve AI/ML apps. Everything happens inside the container, nothing within the container can access your filesystem.
</Warning>
