# Source: https://io.net/docs/guides/workers/install-on-hiveos.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# HiveOS: Install Worker

> A step-by-step process for running io.net on HiveOS:

### What is HiveOS?

HiveOS is an operating system designed specifically for mining cryptocurrencies. It is optimized for mining efficiency, stability, and ease of use, offering features such as remote monitoring, management of mining rigs, and support for a variety of mining hardware. HiveOS is popular among cryptocurrency miners for its user-friendly interface, robust performance, and support for a wide range of mining algorithms and coins..

### 1. [Download the HiveOS](https://hiveon.com/install/) Version from the Hiveon Website

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f99d5255e980cbaa58e7a8dc0037e8f1fa01d8e6faef8712d473130ff09e67d1-Step1.jpg?fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=406bbd411b7c44ebd924f58d3b34e112" alt="" className="mx-auto" style={{ width:"85%" }} data-og-width="1599" width="1599" data-og-height="594" height="594" data-path="images/docs/f99d5255e980cbaa58e7a8dc0037e8f1fa01d8e6faef8712d473130ff09e67d1-Step1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f99d5255e980cbaa58e7a8dc0037e8f1fa01d8e6faef8712d473130ff09e67d1-Step1.jpg?w=280&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=5d49f85b72a05d7062e0c3087676d026 280w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f99d5255e980cbaa58e7a8dc0037e8f1fa01d8e6faef8712d473130ff09e67d1-Step1.jpg?w=560&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=0256481f95d706460406de0de1adec6a 560w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f99d5255e980cbaa58e7a8dc0037e8f1fa01d8e6faef8712d473130ff09e67d1-Step1.jpg?w=840&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=f6da77e2ddf179bace9db60a4d95efaa 840w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f99d5255e980cbaa58e7a8dc0037e8f1fa01d8e6faef8712d473130ff09e67d1-Step1.jpg?w=1100&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=c8be13d62a6c6b2513c8538fe8a66294 1100w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f99d5255e980cbaa58e7a8dc0037e8f1fa01d8e6faef8712d473130ff09e67d1-Step1.jpg?w=1650&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=1fe60eb7cdb1f92d67c8d65c7f97d193 1650w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f99d5255e980cbaa58e7a8dc0037e8f1fa01d8e6faef8712d473130ff09e67d1-Step1.jpg?w=2500&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=d4ad1884b4fdf3d7bc3ef9865477964a 2500w" />
</Frame>

### 2. Burn the HiveOS image into the hard drive of the machine you want to rent using [Etcher.io](https://etcher.balena.io/)

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/9c4a2fe1bea74e88df9742a4b72f8f06ba5b3bf65498b578a523d24c280aca7b-Step2.jpg?fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=ba91eaaa2277ddae981d4a2a210fb866" alt="" data-og-width="1599" width="1599" data-og-height="594" height="594" data-path="images/docs/9c4a2fe1bea74e88df9742a4b72f8f06ba5b3bf65498b578a523d24c280aca7b-Step2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/9c4a2fe1bea74e88df9742a4b72f8f06ba5b3bf65498b578a523d24c280aca7b-Step2.jpg?w=280&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=c64d7d83bf97f18778e4a5b351c0edc0 280w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/9c4a2fe1bea74e88df9742a4b72f8f06ba5b3bf65498b578a523d24c280aca7b-Step2.jpg?w=560&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=9eeb9c0538c653326f68272be8c15c34 560w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/9c4a2fe1bea74e88df9742a4b72f8f06ba5b3bf65498b578a523d24c280aca7b-Step2.jpg?w=840&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=109eb20db30396cea71d93cfc76bbacf 840w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/9c4a2fe1bea74e88df9742a4b72f8f06ba5b3bf65498b578a523d24c280aca7b-Step2.jpg?w=1100&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=4b9175f7ca435b5af7ad3ddab42232a8 1100w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/9c4a2fe1bea74e88df9742a4b72f8f06ba5b3bf65498b578a523d24c280aca7b-Step2.jpg?w=1650&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=ee19ad7d68e13ffe49652e45a4a8f237 1650w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/9c4a2fe1bea74e88df9742a4b72f8f06ba5b3bf65498b578a523d24c280aca7b-Step2.jpg?w=2500&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=e303437ad0fda92eb20ac875b8a4c4b3 2500w" />
</Frame>

### 3. Add a new worker in HiveOS

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/4321a44c31018122f4d2a01dfd81118970bb82c0c69bf30165a5b67affcc635f-Step3.jpg?fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=6e287da5e44d5bb5a5696566f6ba7cba" alt="" data-og-width="1599" width="1599" data-og-height="711" height="711" data-path="images/docs/4321a44c31018122f4d2a01dfd81118970bb82c0c69bf30165a5b67affcc635f-Step3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/4321a44c31018122f4d2a01dfd81118970bb82c0c69bf30165a5b67affcc635f-Step3.jpg?w=280&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=18f5702dc14f1c8a9e0041bdd229eec5 280w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/4321a44c31018122f4d2a01dfd81118970bb82c0c69bf30165a5b67affcc635f-Step3.jpg?w=560&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=f16b428b59788f9490f178048d890ba5 560w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/4321a44c31018122f4d2a01dfd81118970bb82c0c69bf30165a5b67affcc635f-Step3.jpg?w=840&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=c6502b24e8a86e433ac938d7a3fb554a 840w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/4321a44c31018122f4d2a01dfd81118970bb82c0c69bf30165a5b67affcc635f-Step3.jpg?w=1100&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=7bdb72f339f2ad4f7efdc0e4931d85aa 1100w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/4321a44c31018122f4d2a01dfd81118970bb82c0c69bf30165a5b67affcc635f-Step3.jpg?w=1650&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=dd7e5c072df76e801f8e783ddfc5c0a8 1650w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/4321a44c31018122f4d2a01dfd81118970bb82c0c69bf30165a5b67affcc635f-Step3.jpg?w=2500&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=10078838a1c14f1947e5775f26fb5be8 2500w" />
</Frame>

In this step, what you are required to do is:

* Click on the plus icon on the toolbar and select **Add Worker** option.
* Enter the required information for the new worker, such as the worker name, rig type, and other details as needed.
* Save or confirm the changes to add the new worker to your account..

### 4. In the settings, enter the Rig ID and password in the rig

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/dc342aa474bcfdc6804913b158ac33f348fe6d25b48ca1e83ef9700d000660e8-Step4.jpg?fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=dc84464262aa4d95d1b948d893203b69" alt="" data-og-width="1599" width="1599" data-og-height="594" height="594" data-path="images/docs/dc342aa474bcfdc6804913b158ac33f348fe6d25b48ca1e83ef9700d000660e8-Step4.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/dc342aa474bcfdc6804913b158ac33f348fe6d25b48ca1e83ef9700d000660e8-Step4.jpg?w=280&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=792cb7bde9f4d7ade3cafac8ceb155b1 280w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/dc342aa474bcfdc6804913b158ac33f348fe6d25b48ca1e83ef9700d000660e8-Step4.jpg?w=560&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=880f041ccf0d401a0767eae12e9aae18 560w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/dc342aa474bcfdc6804913b158ac33f348fe6d25b48ca1e83ef9700d000660e8-Step4.jpg?w=840&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=653ad394fa2fa486fb78bbc4ba5aa28a 840w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/dc342aa474bcfdc6804913b158ac33f348fe6d25b48ca1e83ef9700d000660e8-Step4.jpg?w=1100&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=ecaab64ccd8b050a3c4371b7611fc7cc 1100w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/dc342aa474bcfdc6804913b158ac33f348fe6d25b48ca1e83ef9700d000660e8-Step4.jpg?w=1650&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=104d7b487ea12f2ef85f2b586826ef3d 1650w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/dc342aa474bcfdc6804913b158ac33f348fe6d25b48ca1e83ef9700d000660e8-Step4.jpg?w=2500&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=db144ddd848c727cbb00a4e10e944a8d 2500w" />
</Frame>

### 5. Open the console from the toolbar

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ed53cc1516b049d63547522e80346e5cb80ee259fa7ac8c3f086e9c633ceae95-Step5.jpg?fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=c008ab2f3e682d0d6773c869e48abefb" alt="" data-og-width="1599" width="1599" data-og-height="455" height="455" data-path="images/docs/ed53cc1516b049d63547522e80346e5cb80ee259fa7ac8c3f086e9c633ceae95-Step5.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ed53cc1516b049d63547522e80346e5cb80ee259fa7ac8c3f086e9c633ceae95-Step5.jpg?w=280&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=defbfbc51a562569cd044045029af774 280w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ed53cc1516b049d63547522e80346e5cb80ee259fa7ac8c3f086e9c633ceae95-Step5.jpg?w=560&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=be6a0e7516bd8c0fa29e884da3b049ac 560w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ed53cc1516b049d63547522e80346e5cb80ee259fa7ac8c3f086e9c633ceae95-Step5.jpg?w=840&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=ec80bcbdcba82cabe1390a5f28cdf0f1 840w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ed53cc1516b049d63547522e80346e5cb80ee259fa7ac8c3f086e9c633ceae95-Step5.jpg?w=1100&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=a2ffc57e09e49c020a6db74e08f9f271 1100w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ed53cc1516b049d63547522e80346e5cb80ee259fa7ac8c3f086e9c633ceae95-Step5.jpg?w=1650&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=0c5e65b0d0043934f3cd6d8430310c98 1650w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ed53cc1516b049d63547522e80346e5cb80ee259fa7ac8c3f086e9c633ceae95-Step5.jpg?w=2500&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=851a0be831ab3f973f66cb8ae4ae5746 2500w" />
</Frame>

Click on the Console icon in the toolbar to open the command line interface

### 6. Enter commands into the command line

**Command Line** is a tool on your computer that lets you type in commands to tell the computer what to do. Instead of clicking on things with a mouse, you write instructions, and the computer follows them. It's like talking directly to your computer using text.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f7cb363-Step6.jpg?fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=83b2b78898e9044dece3b1b110047856" alt="" data-og-width="1599" width="1599" data-og-height="511" height="511" data-path="images/docs/f7cb363-Step6.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f7cb363-Step6.jpg?w=280&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=63dea92f3d410cc9effde33a8559b6ba 280w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f7cb363-Step6.jpg?w=560&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=5cc1a3a23f13023323fb010b76f87e98 560w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f7cb363-Step6.jpg?w=840&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=4cb1087b90a0e1c7a93fc7764d22b5aa 840w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f7cb363-Step6.jpg?w=1100&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=261238eabd0ed0c3ac3b905eab053902 1100w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f7cb363-Step6.jpg?w=1650&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=3132bbf4a590915e823f29f3f1071e58 1650w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f7cb363-Step6.jpg?w=2500&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=886e7f0cf033eef25c66ec432f96815c 2500w" />
</Frame>

Enter the following commands in a row into the command line:

```
sudo apt-get update -y
```

```
sudo apt-get install -y gnupg1
```

```
cd ~
```

```
wget https://raw.githubusercontent.com/ionet-official/io-net-official-setup-script/main/ionet-setup.sh
```

```
chmod +x ionet-setup.sh
```

```
./ionet-setup.sh
```

```
sudo reboot
```

To check if all your graphics cards are connected, enter this additional command:

```
nvidia-smi
```

<Warning>
  When using SXM or NV Link, ensure that Fabric Manager is [installed correctly](https://docs.nvidia.com/datacenter/tesla/pdf/fabric-manager-user-guide.pdf) and enabled. This will prevent initialization issues and ensure that all GPUs are functioning properly, thereby avoiding PoW verification failures.
</Warning>

### 7. Execute the Docker command provided on the 'Connect New Device' page in your dashboard.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7a040c96d16e16b430c5219bb4a834af889ae830c4bb8260e4f4fa0da5662605-Step7.jpg?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=6cb882cc3076ed9a5fdf7e7602c1657f" alt="" data-og-width="1599" width="1599" data-og-height="485" height="485" data-path="images/docs/7a040c96d16e16b430c5219bb4a834af889ae830c4bb8260e4f4fa0da5662605-Step7.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7a040c96d16e16b430c5219bb4a834af889ae830c4bb8260e4f4fa0da5662605-Step7.jpg?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=ba52a913460058bc4c4ab3d35bfe6120 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7a040c96d16e16b430c5219bb4a834af889ae830c4bb8260e4f4fa0da5662605-Step7.jpg?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=fe02c99a2079084dd09a02f51fc4d9c5 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7a040c96d16e16b430c5219bb4a834af889ae830c4bb8260e4f4fa0da5662605-Step7.jpg?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=f5cbd458630c0ed78fd454defe0e5e47 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7a040c96d16e16b430c5219bb4a834af889ae830c4bb8260e4f4fa0da5662605-Step7.jpg?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=0fd7b03dd53dd144e55a3b8df7dedaad 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7a040c96d16e16b430c5219bb4a834af889ae830c4bb8260e4f4fa0da5662605-Step7.jpg?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=6ad4fa7ea1636577435facc6afbccc2f 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7a040c96d16e16b430c5219bb4a834af889ae830c4bb8260e4f4fa0da5662605-Step7.jpg?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=7c2f776a41bc4a919ceb06b310f46896 2500w" />
</Frame>

### 8. Check both IO-worker-monitor and IO-worker-vc are running

```
docker ps
```

Wait for the device to indicate "Running" on the device page.

<Warning>
  If only one container appears, run the command "docker ps" again.
</Warning>

### Congratulations on successfully setting up your first Worker.

Now that your Worker has been successfully created and is running, you can track its status on the Workers page.

<Info>
  If you're having trouble installing Worker, please refer to our \[Worker troubleshooting guide]/guides/workers/troubleshoot-worker-general). If the issue persists or you need further assistance, feel free to [check our knowledge base](https://support.io.net/en/support/home) for answers, and if you still need help, don’t hesitate to open a support ticket!
</Info>
