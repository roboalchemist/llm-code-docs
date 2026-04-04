# Source: https://io.net/docs/guides/workers/install-on-macos.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> A step-by-step guide for setting up the environment for io.net on Mac OS-based machines

<iframe width="100%" src="https://www.youtube.com/embed/7jc3dYbiiUs" title="IO Worker Guide for MacOS" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

### Before Starting, Check Your Mac Processor

We currently only support **Apple chip** processors (M3, M4). All currently supported processor and video card models can be [found here](/guides/workers/supported-devices).

To check your Mac processor:

1. On your Mac, click the Apple icon in the top-left corner of the menu bar.
2. Select the **About This Mac** option.
3. If you see **Apple M3** (or higher) in the **Chip** line, it means you’re using a Mac with an Apple Silicon CPU.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1c29ed6d34b2f9bbc8ab80f43279d2872964c560f867a81530e82ee76c6519f3-Step0.jpg?fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=1b9b895fbd195a301d37d5fa30bb9eb5" alt="" className="mx-auto" style={{ width:"83%" }} data-og-width="1603" width="1603" data-og-height="1170" height="1170" data-path="images/docs/1c29ed6d34b2f9bbc8ab80f43279d2872964c560f867a81530e82ee76c6519f3-Step0.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1c29ed6d34b2f9bbc8ab80f43279d2872964c560f867a81530e82ee76c6519f3-Step0.jpg?w=280&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=196c8ca06c42c7186809cc8438c25714 280w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1c29ed6d34b2f9bbc8ab80f43279d2872964c560f867a81530e82ee76c6519f3-Step0.jpg?w=560&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=2a714ce7bed73f756600ea8fd367c423 560w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1c29ed6d34b2f9bbc8ab80f43279d2872964c560f867a81530e82ee76c6519f3-Step0.jpg?w=840&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=2385f672d186db5d93b5aa5240d36b9e 840w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1c29ed6d34b2f9bbc8ab80f43279d2872964c560f867a81530e82ee76c6519f3-Step0.jpg?w=1100&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=7a7e0ba95b71e6c072e72d771058f2ba 1100w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1c29ed6d34b2f9bbc8ab80f43279d2872964c560f867a81530e82ee76c6519f3-Step0.jpg?w=1650&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=179c3492ced179d0a0958b7ca65dd5b2 1650w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1c29ed6d34b2f9bbc8ab80f43279d2872964c560f867a81530e82ee76c6519f3-Step0.jpg?w=2500&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=c8295ade0fc43435554873820e9188e2 2500w" />
</Frame>

### Go to [cloud.io.net](https://worker.io.net/worker/devices)

If you have not yet created an account, you can sign up on [io.net](http://io.net) using Google, Apple ID, GitHub, Hugging Face, X, Worldcoin, or simply with a one-time password by clicking the "Login with Email" button.

<img src="https://mintcdn.com/ionet-cca8037f/1nusXKdPVUHoDz-x/images/docs/login_process/newlogin1.jpg?fit=max&auto=format&n=1nusXKdPVUHoDz-x&q=85&s=470902a5e8a08e075157120cae667cd7" alt="Newlogin1 Jp" data-og-width="1868" width="1868" data-og-height="1058" height="1058" data-path="images/docs/login_process/newlogin1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/1nusXKdPVUHoDz-x/images/docs/login_process/newlogin1.jpg?w=280&fit=max&auto=format&n=1nusXKdPVUHoDz-x&q=85&s=129a29b9bac3df741db40e99bda417d2 280w, https://mintcdn.com/ionet-cca8037f/1nusXKdPVUHoDz-x/images/docs/login_process/newlogin1.jpg?w=560&fit=max&auto=format&n=1nusXKdPVUHoDz-x&q=85&s=4b7d81b89eb0b45a1c968b111b852850 560w, https://mintcdn.com/ionet-cca8037f/1nusXKdPVUHoDz-x/images/docs/login_process/newlogin1.jpg?w=840&fit=max&auto=format&n=1nusXKdPVUHoDz-x&q=85&s=7a6eb785992b9c0ecf6d76c5b0a9c3cf 840w, https://mintcdn.com/ionet-cca8037f/1nusXKdPVUHoDz-x/images/docs/login_process/newlogin1.jpg?w=1100&fit=max&auto=format&n=1nusXKdPVUHoDz-x&q=85&s=076a5c9517bc68d1a06efc5429ce5c8a 1100w, https://mintcdn.com/ionet-cca8037f/1nusXKdPVUHoDz-x/images/docs/login_process/newlogin1.jpg?w=1650&fit=max&auto=format&n=1nusXKdPVUHoDz-x&q=85&s=900b615e45f5d691226cbc7930a1ea3d 1650w, https://mintcdn.com/ionet-cca8037f/1nusXKdPVUHoDz-x/images/docs/login_process/newlogin1.jpg?w=2500&fit=max&auto=format&n=1nusXKdPVUHoDz-x&q=85&s=fd4ba61049c65504f7c2b618ed7762d3 2500w" />

### 1. From IO Elements Navigate to Worker Section

IO Elements serves as your new control panel for navigating the service efficiently. Click on **IO Worker** to delve deeper into its functionalities and features.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4ab2791afa1784c65f0b291076f9e8c0f91ca5e8f4fffe7fb922c26c352d19e2-Step2.jpg?fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=c78d69eb1afa6abb6c5851941b5ea2b9" alt="" className="mx-auto" style={{ width:"69%" }} data-og-width="735" width="735" data-og-height="539" height="539" data-path="images/docs/4ab2791afa1784c65f0b291076f9e8c0f91ca5e8f4fffe7fb922c26c352d19e2-Step2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4ab2791afa1784c65f0b291076f9e8c0f91ca5e8f4fffe7fb922c26c352d19e2-Step2.jpg?w=280&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=97529abc3778854c1cfd85ddaf37b4cb 280w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4ab2791afa1784c65f0b291076f9e8c0f91ca5e8f4fffe7fb922c26c352d19e2-Step2.jpg?w=560&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=c4c84af1e4e96701c93cd7720c6110c2 560w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4ab2791afa1784c65f0b291076f9e8c0f91ca5e8f4fffe7fb922c26c352d19e2-Step2.jpg?w=840&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=5c2c5a70ed657ebfcfbc80faa3cc0485 840w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4ab2791afa1784c65f0b291076f9e8c0f91ca5e8f4fffe7fb922c26c352d19e2-Step2.jpg?w=1100&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=630fa6a6a2e23020bf9cd91518004d62 1100w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4ab2791afa1784c65f0b291076f9e8c0f91ca5e8f4fffe7fb922c26c352d19e2-Step2.jpg?w=1650&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=e54a00e35078336e410e33305d60bafb 1650w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4ab2791afa1784c65f0b291076f9e8c0f91ca5e8f4fffe7fb922c26c352d19e2-Step2.jpg?w=2500&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=a399f810858556640f8d8e6af2ffe3e3 2500w" />
</Frame>

### 2. Use "Connect New Worker" Button to Open the Wizard

If Workers have not yet been added, you can use the central button. If the screen is full of information, find the same button in the upper right corner

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5274db0357e3ae99cfc95b57f3f1aa9c2af8cc906d358b53eaf857dac33a7ce1-Step3.jpg?fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=878a6d1119c7060b47b490a47449455a" alt="" className="mx-auto" style={{ width:"60%" }} data-og-width="735" width="735" data-og-height="539" height="539" data-path="images/docs/5274db0357e3ae99cfc95b57f3f1aa9c2af8cc906d358b53eaf857dac33a7ce1-Step3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5274db0357e3ae99cfc95b57f3f1aa9c2af8cc906d358b53eaf857dac33a7ce1-Step3.jpg?w=280&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=c2b6fbf87d535c1f2d13267454b2ab43 280w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5274db0357e3ae99cfc95b57f3f1aa9c2af8cc906d358b53eaf857dac33a7ce1-Step3.jpg?w=560&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=c74f99ccce3ae9952daf5672d09b9a2f 560w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5274db0357e3ae99cfc95b57f3f1aa9c2af8cc906d358b53eaf857dac33a7ce1-Step3.jpg?w=840&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=6bd56e132524279ad8787d85718cfb75 840w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5274db0357e3ae99cfc95b57f3f1aa9c2af8cc906d358b53eaf857dac33a7ce1-Step3.jpg?w=1100&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=efea7c53e91cfff1aeeff0f5bd09ceb4 1100w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5274db0357e3ae99cfc95b57f3f1aa9c2af8cc906d358b53eaf857dac33a7ce1-Step3.jpg?w=1650&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=09e7addc9cd567aa99c693b9db8bbc87 1650w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5274db0357e3ae99cfc95b57f3f1aa9c2af8cc906d358b53eaf857dac33a7ce1-Step3.jpg?w=2500&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=6b2f375daa7979764bf98bf5d774b5ea 2500w" />
</Frame>

### 3. Name Your Device

Click the "**Pencil**" icon to open the popup for editing the device name.

Please add a unique name for your device. An ideal format would be something like this: **My-Test-Device** 

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/560a01163ca32f581e247537775cc0996388c39442b09a3ff49f97c836b263db-Step4.jpg?fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=12550fcfb2e136f192c547001ac967c9" alt="" className="mx-auto" style={{ width:"85%" }} data-og-width="1251" width="1251" data-og-height="561" height="561" data-path="images/docs/560a01163ca32f581e247537775cc0996388c39442b09a3ff49f97c836b263db-Step4.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/560a01163ca32f581e247537775cc0996388c39442b09a3ff49f97c836b263db-Step4.jpg?w=280&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=e4bc8328b5efaab26b09a982fcd3d5eb 280w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/560a01163ca32f581e247537775cc0996388c39442b09a3ff49f97c836b263db-Step4.jpg?w=560&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=715e15bf6edbcc5fc71d44fa0d192b42 560w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/560a01163ca32f581e247537775cc0996388c39442b09a3ff49f97c836b263db-Step4.jpg?w=840&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=73b7bfb3c0ab6e86b8c30299dc8a7e74 840w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/560a01163ca32f581e247537775cc0996388c39442b09a3ff49f97c836b263db-Step4.jpg?w=1100&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=e97b33d651bc1016cd4eb4c6b4913185 1100w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/560a01163ca32f581e247537775cc0996388c39442b09a3ff49f97c836b263db-Step4.jpg?w=1650&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=025bf8329ba8b2cd42f1c60c064a65c9 1650w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/560a01163ca32f581e247537775cc0996388c39442b09a3ff49f97c836b263db-Step4.jpg?w=2500&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=e1da4241db567a1e15a9df63002ff43a 2500w" />
</Frame>

### 4. Select MacOS Operating System “OS”

Choose the Operating System “OS” of your device from **MacOS**, Windows or Ubuntu.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a757734d9ac6926db17891cada2e623939bb28c16ed646f75837aeeb4ba7cc08-Step5.jpg?fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=4a1dc0648c1b80f5699e3fbb7c9909e5" alt="" className="mx-auto" style={{ width:"71%" }} data-og-width="1045" width="1045" data-og-height="422" height="422" data-path="images/docs/a757734d9ac6926db17891cada2e623939bb28c16ed646f75837aeeb4ba7cc08-Step5.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a757734d9ac6926db17891cada2e623939bb28c16ed646f75837aeeb4ba7cc08-Step5.jpg?w=280&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=d1bee120ab917167c78f3dc14e973672 280w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a757734d9ac6926db17891cada2e623939bb28c16ed646f75837aeeb4ba7cc08-Step5.jpg?w=560&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=3b11ef97b5e5acaefefffcb6e53f9ad2 560w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a757734d9ac6926db17891cada2e623939bb28c16ed646f75837aeeb4ba7cc08-Step5.jpg?w=840&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=1bdd50aa9f1f8b58ed7431ccfdb7b61c 840w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a757734d9ac6926db17891cada2e623939bb28c16ed646f75837aeeb4ba7cc08-Step5.jpg?w=1100&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=4604a3216e0fcf2d7b22343787f4c860 1100w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a757734d9ac6926db17891cada2e623939bb28c16ed646f75837aeeb4ba7cc08-Step5.jpg?w=1650&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=55304ae2733957b651901f06c0d17bcb 1650w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a757734d9ac6926db17891cada2e623939bb28c16ed646f75837aeeb4ba7cc08-Step5.jpg?w=2500&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=840638f8ea9c409ab4bf0c7f858a5f12 2500w" />
</Frame>

### 5. Prerequisites for Mac

Download and install Docker Desktop for MacOS by [following the link](/docs/install-docker-on-macos).

<Info>
  It has been confirmed that some users limit the amount of system resources that IO Worker can access when performing compute verifications. Many users do not set the proper amount of device level resources available for the Docker engine. Many have used default settings or restricted the Worker’s RAM access to 8GB or lower. This would significantly impact the device capability in passing PoW. This is mostly common among Mac devices.
</Info>

<Check>
  To install Docker on MacOS computers, refer to the "[Installing Docker on MacOS](/docs/install-docker-on-macos)" instructions.
</Check>

### 6. Download and Launch IO Binary

**IO Binary** is a compiled executable file used to perform computational tasks and manage system operations. It is crucial for the smooth operation of the platform as it handles essential functions directly related to the performance and reliability of the computational resources.

<Warning>
  Do not modify or run code directly in io.net’s docker containers. This may disqualify your device from earning block rewards or being hired. If you have suggestions or ideas for custom code in our Docker containers, contact customer support to suggest them.
</Warning>

Follow the steps below to download and launch the IO binary:

1. Open the Terminal through **Launchpad**

   **Terminal** is a tool on your computer that lets you type in commands to tell the computer what to do. Instead of clicking on things with a mouse, you write instructions, and the computer follows them. It's like talking directly to your computer using text.

   Click the **Launchpad** icon in the Dock, start typing "**Terminal**" in the search field, then click the **Terminal** icon:

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3291b8cd2dda2294bc83c86b27ace24b4f14975f3736e73f954885e03ea562c4-Step7.jpg?fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=545c5f52d3d9dea25aec3906c6d41f4f" alt="" className="mx-auto" style={{ width:"64%" }} data-og-width="1830" width="1830" data-og-height="998" height="998" data-path="images/docs/3291b8cd2dda2294bc83c86b27ace24b4f14975f3736e73f954885e03ea562c4-Step7.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3291b8cd2dda2294bc83c86b27ace24b4f14975f3736e73f954885e03ea562c4-Step7.jpg?w=280&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=52cb263334139680712f39aa48a15142 280w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3291b8cd2dda2294bc83c86b27ace24b4f14975f3736e73f954885e03ea562c4-Step7.jpg?w=560&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=b0ea2ea8e04db9f47cb6f11beea67524 560w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3291b8cd2dda2294bc83c86b27ace24b4f14975f3736e73f954885e03ea562c4-Step7.jpg?w=840&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=1be94b4b4499c1fc70ea558d500298d8 840w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3291b8cd2dda2294bc83c86b27ace24b4f14975f3736e73f954885e03ea562c4-Step7.jpg?w=1100&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=7953b28907e4d0cd5548e276d562a237 1100w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3291b8cd2dda2294bc83c86b27ace24b4f14975f3736e73f954885e03ea562c4-Step7.jpg?w=1650&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=47013b67df6204e36975d11e575eabab 1650w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3291b8cd2dda2294bc83c86b27ace24b4f14975f3736e73f954885e03ea562c4-Step7.jpg?w=2500&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=4868a53bf0e5a9846de75209b2857961 2500w" />
   </Frame>
2. Download the IO Binary for MacOS using the following link in the Terminal:

   ```
   curl -L https://github.com/ionet-official/io_launch_binaries/raw/main/io_net_launch_binary_mac -o io_net_launch_binary_mac
   ```
3. Grant permissions to the new IO Binary with this command:

   ```
   chmod +x io_net_launch_binary_mac
   ```

   <Frame>
       <img src="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/62adb19e9554964bb2165220b1765c75fd4fd00f4d9969f2183bb93a38d0e40a-Step8.jpg?fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=590917394908d7570e3163126b5f7a67" alt="" data-og-width="2096" width="2096" data-og-height="932" height="932" data-path="images/docs/62adb19e9554964bb2165220b1765c75fd4fd00f4d9969f2183bb93a38d0e40a-Step8.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/62adb19e9554964bb2165220b1765c75fd4fd00f4d9969f2183bb93a38d0e40a-Step8.jpg?w=280&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=ca5a335c68f27788c9247d55c2d47e8e 280w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/62adb19e9554964bb2165220b1765c75fd4fd00f4d9969f2183bb93a38d0e40a-Step8.jpg?w=560&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=e10a37ff9319bccc69f3ce8887311bb1 560w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/62adb19e9554964bb2165220b1765c75fd4fd00f4d9969f2183bb93a38d0e40a-Step8.jpg?w=840&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=acba78dd418c6895fcbcb6221445d48f 840w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/62adb19e9554964bb2165220b1765c75fd4fd00f4d9969f2183bb93a38d0e40a-Step8.jpg?w=1100&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=7dfeb0dbc97d60fa829e98da7a244cca 1100w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/62adb19e9554964bb2165220b1765c75fd4fd00f4d9969f2183bb93a38d0e40a-Step8.jpg?w=1650&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=08e5b45671c58c24dcaed9db30ff2ed0 1650w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/62adb19e9554964bb2165220b1765c75fd4fd00f4d9969f2183bb93a38d0e40a-Step8.jpg?w=2500&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=b6d22c9047c9a2ec2e48732adbb498d3 2500w" />
   </Frame>
4. Copy generated the IO Binary address provided in the wizard and past it into Terminal to run further:

   ```
   ./io_net_launch_binary_mac
   ```

   <Info>
     To disable sleep mode for a device, pass the --disable\_sleep\_mode=true argument at the end of the command line.

     ```
     ./io_net_launch_binary_mac --disable_sleep_mode=true
     ```

     You can find more additional arguments to use with the IO Binary command [here](https://github.com/ionet-official/io_launch_binaries?tab=readme-ov-file#usage).
   </Info>

   <Frame>
       <img src="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/683fbce68de7b3917192602974b1798b2ec72ef9bce09131884c709ea3923ffe-Step9.jpg?fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=1d2f4c2df43a027bc8a5ebe1b7db8703" alt="" data-og-width="1882" width="1882" data-og-height="1050" height="1050" data-path="images/docs/683fbce68de7b3917192602974b1798b2ec72ef9bce09131884c709ea3923ffe-Step9.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/683fbce68de7b3917192602974b1798b2ec72ef9bce09131884c709ea3923ffe-Step9.jpg?w=280&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=4ec7a472c8b6a5539d96da12ab54b411 280w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/683fbce68de7b3917192602974b1798b2ec72ef9bce09131884c709ea3923ffe-Step9.jpg?w=560&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=fb2f39833c02dd21e51e051eec9811ca 560w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/683fbce68de7b3917192602974b1798b2ec72ef9bce09131884c709ea3923ffe-Step9.jpg?w=840&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=67e64b25ce1fbb91acc066b38498c892 840w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/683fbce68de7b3917192602974b1798b2ec72ef9bce09131884c709ea3923ffe-Step9.jpg?w=1100&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=29fa262f8e3cec5f2f9d35c8fa9e76ad 1100w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/683fbce68de7b3917192602974b1798b2ec72ef9bce09131884c709ea3923ffe-Step9.jpg?w=1650&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=db1ac7cc74e24d394627b36fb64e784d 1650w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/683fbce68de7b3917192602974b1798b2ec72ef9bce09131884c709ea3923ffe-Step9.jpg?w=2500&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=d774d5c319da6df77fb5ccaf6b319e1a 2500w" />
   </Frame>

### 7. Authorize Your New Device

The IO Binary may prompt you to authorize your new device.

<Info>
  Remember, you have 3+ minutes to complete the authorization of the device. If you miss it, rerun the code again.
</Info>

You can do this in two ways:

1. **Copy the Link from the Terminal**:

   <Frame>
       <img src="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1fe091affcc9ecea5a6c7ae920614ad99d92f7e0e8880e63b71d279e30f5e88e-Step10.jpg?fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=3aa44cd3fa2930549443499acc427ab3" alt="" data-og-width="1572" width="1572" data-og-height="1041" height="1041" data-path="images/docs/1fe091affcc9ecea5a6c7ae920614ad99d92f7e0e8880e63b71d279e30f5e88e-Step10.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1fe091affcc9ecea5a6c7ae920614ad99d92f7e0e8880e63b71d279e30f5e88e-Step10.jpg?w=280&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=5f32dacd0af826734d8d359c68efd56b 280w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1fe091affcc9ecea5a6c7ae920614ad99d92f7e0e8880e63b71d279e30f5e88e-Step10.jpg?w=560&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=2e6a293da7f5b14234fb91f21fccedb5 560w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1fe091affcc9ecea5a6c7ae920614ad99d92f7e0e8880e63b71d279e30f5e88e-Step10.jpg?w=840&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=01bf3eb98e6522ca077ffad5d514c0fb 840w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1fe091affcc9ecea5a6c7ae920614ad99d92f7e0e8880e63b71d279e30f5e88e-Step10.jpg?w=1100&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=e8e0ffe87bbcae0708f786f468167cd7 1100w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1fe091affcc9ecea5a6c7ae920614ad99d92f7e0e8880e63b71d279e30f5e88e-Step10.jpg?w=1650&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=a32155c9895ecf3447cb4d3dbd058d7e 1650w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1fe091affcc9ecea5a6c7ae920614ad99d92f7e0e8880e63b71d279e30f5e88e-Step10.jpg?w=2500&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=752f3a4b860981ac7fe653d36b7a156d 2500w" />
   </Frame>

   Paste it into your browser and confirm the action. After confirmation, the system will prompt you to log in.

   <Frame>
       <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/75a85cc630a26880d26fccca2842d9348507fca6dfb709e57f9d5f650c43d4ff-Step11.jpg?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=88bd0f0089a6aa47fefde8860ea820d6" alt="" data-og-width="1077" width="1077" data-og-height="564" height="564" data-path="images/docs/75a85cc630a26880d26fccca2842d9348507fca6dfb709e57f9d5f650c43d4ff-Step11.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/75a85cc630a26880d26fccca2842d9348507fca6dfb709e57f9d5f650c43d4ff-Step11.jpg?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=5184a0e8e26b81dcea0dcebb131f1506 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/75a85cc630a26880d26fccca2842d9348507fca6dfb709e57f9d5f650c43d4ff-Step11.jpg?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=04ebd53615edb443b7bca9d6dc62450c 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/75a85cc630a26880d26fccca2842d9348507fca6dfb709e57f9d5f650c43d4ff-Step11.jpg?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=6f8b3b38bbc5ffd6ea1004015068ffba 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/75a85cc630a26880d26fccca2842d9348507fca6dfb709e57f9d5f650c43d4ff-Step11.jpg?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=b227fcf98e2fe70bf3180eb9f2f59704 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/75a85cc630a26880d26fccca2842d9348507fca6dfb709e57f9d5f650c43d4ff-Step11.jpg?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=fbabcd0e4f39656991ed66a0dce74a6e 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/75a85cc630a26880d26fccca2842d9348507fca6dfb709e57f9d5f650c43d4ff-Step11.jpg?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=8d35599d76de8c3fc2cdeaabf2103ee8 2500w" />
   </Frame>
2. **Copy the Code from the Terminal**:

   <Frame>
       <img src="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4c7cc651857433572f524da527258c5a4642945c8dc0e016df457fada8f26477-Step12.jpg?fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=7a87823b35f5111f29d7198d5ad025a3" alt="" data-og-width="1870" width="1870" data-og-height="620" height="620" data-path="images/docs/4c7cc651857433572f524da527258c5a4642945c8dc0e016df457fada8f26477-Step12.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4c7cc651857433572f524da527258c5a4642945c8dc0e016df457fada8f26477-Step12.jpg?w=280&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=034873e788156e8f3850b50a64a953be 280w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4c7cc651857433572f524da527258c5a4642945c8dc0e016df457fada8f26477-Step12.jpg?w=560&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=62042e01b937bb6c03aa3b3c73fca571 560w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4c7cc651857433572f524da527258c5a4642945c8dc0e016df457fada8f26477-Step12.jpg?w=840&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=e1f478b68d64865291bb5d37a4996465 840w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4c7cc651857433572f524da527258c5a4642945c8dc0e016df457fada8f26477-Step12.jpg?w=1100&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=371c90467958a8211f680ed2f3bdf842 1100w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4c7cc651857433572f524da527258c5a4642945c8dc0e016df457fada8f26477-Step12.jpg?w=1650&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=a1732b2fd26877b29446760815e49cf7 1650w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4c7cc651857433572f524da527258c5a4642945c8dc0e016df457fada8f26477-Step12.jpg?w=2500&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=fe0e0643703f04bbdf23311843f50c64 2500w" />
   </Frame>

   Enter this code on the page [https://auth0.io.solutions/activate](https://auth0.io.solutions/activate) to authorize the device. You will be prompted to log in.

   <Frame>
       <img src="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/ec4ce726825eb4890de728b4c776d51a86f5a0439db945f3415ef5dda7a76c16-Step13.jpg?fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=125c07accdda32e64aa0dce75be8a608" alt="" data-og-width="1077" width="1077" data-og-height="564" height="564" data-path="images/docs/ec4ce726825eb4890de728b4c776d51a86f5a0439db945f3415ef5dda7a76c16-Step13.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/ec4ce726825eb4890de728b4c776d51a86f5a0439db945f3415ef5dda7a76c16-Step13.jpg?w=280&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=329d22a093d1e9465bee0b942e5d3893 280w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/ec4ce726825eb4890de728b4c776d51a86f5a0439db945f3415ef5dda7a76c16-Step13.jpg?w=560&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=84158e54820e483f167e65ec985a7e80 560w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/ec4ce726825eb4890de728b4c776d51a86f5a0439db945f3415ef5dda7a76c16-Step13.jpg?w=840&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=b7b23f21d99f0465587a327473e6d5f0 840w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/ec4ce726825eb4890de728b4c776d51a86f5a0439db945f3415ef5dda7a76c16-Step13.jpg?w=1100&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=d5ff1551fda645a78f062fd9020f5437 1100w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/ec4ce726825eb4890de728b4c776d51a86f5a0439db945f3415ef5dda7a76c16-Step13.jpg?w=1650&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=6d9dffdfc49f86210f5f47a261f2a770 1650w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/ec4ce726825eb4890de728b4c776d51a86f5a0439db945f3415ef5dda7a76c16-Step13.jpg?w=2500&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=daee1d4e7ad76233ee508e4e91659dbc 2500w" />
   </Frame>

<Info>
  **Onboard Multiple Devices by Bypassing Interactive Authentication**

  To onboard a new device, use the following command with the **--token** flag:

  <Frame>
        <img src="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6d8bb6bdbf6dd9d4579553b2acb5b66abc0b4de472f894ec26628363fe363738-Step14.png?fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=9f918fb751df5892e9017d73c6b3c8d8" alt="" data-og-width="1558" width="1558" data-og-height="574" height="574" data-path="images/docs/6d8bb6bdbf6dd9d4579553b2acb5b66abc0b4de472f894ec26628363fe363738-Step14.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6d8bb6bdbf6dd9d4579553b2acb5b66abc0b4de472f894ec26628363fe363738-Step14.png?w=280&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=0e7150bbc2ffd1831a28fa9ee545d061 280w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6d8bb6bdbf6dd9d4579553b2acb5b66abc0b4de472f894ec26628363fe363738-Step14.png?w=560&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=dd56cf5c34570cefb783fd074a7cbfc1 560w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6d8bb6bdbf6dd9d4579553b2acb5b66abc0b4de472f894ec26628363fe363738-Step14.png?w=840&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=ea4cfb25a976b26a187529d16d1989aa 840w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6d8bb6bdbf6dd9d4579553b2acb5b66abc0b4de472f894ec26628363fe363738-Step14.png?w=1100&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=0aa0c3019419ca5a1bd135271297b583 1100w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6d8bb6bdbf6dd9d4579553b2acb5b66abc0b4de472f894ec26628363fe363738-Step14.png?w=1650&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=570842612fa6b034b1b3f5c78620cd5a 1650w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6d8bb6bdbf6dd9d4579553b2acb5b66abc0b4de472f894ec26628363fe363738-Step14.png?w=2500&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=a6458633734378225bafb8025abde555 2500w" />
  </Frame>

  ```
  ./io_net_launch_binary_mac --token your-token-value
  ```

  This will allow you to bypass the interactive authentication process.
</Info>

### 8. Remove previously installed Docker containers

<Tooltip tip="IO Binary – It's a file that contains executable instructions in a format that a computer can directly execute. It represents a software application in a form that the computer's processor can understand and run.">IO Binary</Tooltip> will ask you questions related to previously installed Docker Containers. To continue the installation of <Tooltip tip="IO Worker – IO Worker is a component of the IO.NET ecosystem that enables users to rent out their computing devices like GPUs and CPUs to those needing computational power. By leasing their device's processing capabilities, users earn rewards for tasks like artificial intelligence computations or rendering. This setup fosters decentralized computing and resource sharing, fostering collaboration and mutual benefit among users on the IO.NET platform.">IO Worker</Tooltip>, you must agree to remove all old containers and proceed by typing: **Yes**

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c84db64596d5b5e755d2a1071dd28e317cdf17d3369203ef48934a38e7dbc95e-Step15.jpg?fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=4bf6029276d49e3b7de90df7a01ff922" alt="" data-og-width="1456" width="1456" data-og-height="627" height="627" data-path="images/docs/c84db64596d5b5e755d2a1071dd28e317cdf17d3369203ef48934a38e7dbc95e-Step15.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c84db64596d5b5e755d2a1071dd28e317cdf17d3369203ef48934a38e7dbc95e-Step15.jpg?w=280&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=ec5dfcb1072d6fd9c7c883346cc7530e 280w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c84db64596d5b5e755d2a1071dd28e317cdf17d3369203ef48934a38e7dbc95e-Step15.jpg?w=560&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=6bba2a3025c8098f3db98161c669b5a2 560w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c84db64596d5b5e755d2a1071dd28e317cdf17d3369203ef48934a38e7dbc95e-Step15.jpg?w=840&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=917f06bc1e6ebfb5f3601cf7d3fecdec 840w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c84db64596d5b5e755d2a1071dd28e317cdf17d3369203ef48934a38e7dbc95e-Step15.jpg?w=1100&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=6e1aef7471cb790c0e59ee58c833fa5e 1100w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c84db64596d5b5e755d2a1071dd28e317cdf17d3369203ef48934a38e7dbc95e-Step15.jpg?w=1650&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=259d8545b77b0bb12947727036ea5ead 1650w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c84db64596d5b5e755d2a1071dd28e317cdf17d3369203ef48934a38e7dbc95e-Step15.jpg?w=2500&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=33c5ca6200cb5fc99ae60130bb7d3194 2500w" />
</Frame>

### 9. Wait for Worker Connection to Complete

IO Binary will install all additional containers and images for your Docker. The process may take some time to complete as it installs additional packages for Docker. Please allow the installation process to finish.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/06971281dcd23dd8542851d0730f39e35c59f05d3d5ba7024fbee9b718c3a270-Step16.jpg?fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=1c2a32af66a2890a6b041d4240fd3100" alt="" data-og-width="1312" width="1312" data-og-height="1461" height="1461" data-path="images/docs/06971281dcd23dd8542851d0730f39e35c59f05d3d5ba7024fbee9b718c3a270-Step16.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/06971281dcd23dd8542851d0730f39e35c59f05d3d5ba7024fbee9b718c3a270-Step16.jpg?w=280&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=2536d0149553c425fbfed1aae0215537 280w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/06971281dcd23dd8542851d0730f39e35c59f05d3d5ba7024fbee9b718c3a270-Step16.jpg?w=560&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=743e80afbb8d385786e80cf8c2aab6ee 560w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/06971281dcd23dd8542851d0730f39e35c59f05d3d5ba7024fbee9b718c3a270-Step16.jpg?w=840&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=e20ab30a66274baef9c662c3a30a41e7 840w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/06971281dcd23dd8542851d0730f39e35c59f05d3d5ba7024fbee9b718c3a270-Step16.jpg?w=1100&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=e4e26fd0f89d249f353942788433b57a 1100w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/06971281dcd23dd8542851d0730f39e35c59f05d3d5ba7024fbee9b718c3a270-Step16.jpg?w=1650&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=ffa68cc12f67a4ab64eebc7ad1aedb4c 1650w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/06971281dcd23dd8542851d0730f39e35c59f05d3d5ba7024fbee9b718c3a270-Step16.jpg?w=2500&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=877d9fa183cf475701b450c2bdcfa265 2500w" />
</Frame>

Afterward, return to the browser to complete the installation.

You may need to wait for up to 10 minutes while the device checks and connects to the IO Ecosystem. If it doesn't connect, contact customer support by logging into your [IO.Net account](https://worker.io.net).

<Frame>
  ![](https://files.readme.io/7059edf-Step13.gif)
</Frame>

<Warning>
  Please disable power-saving mode when running your devices on IO Net. Power-saving mode can impair device performance, potentially leading to failure in PoW or being classified as not providing adequate computing power.
</Warning>

### Congratulations on Successfully Setting up Your First Worker.

Now that your Worker has been successfully created and is running, you can track its status on the Workers page.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/39d09fdd09c068a8aa8ab32d14562b94b1da1fbb7221dc4a01ad8ae3c8058104-step18.png?fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=fa0a15f117ea099fc30cd00ef53647ff" alt="" data-og-width="2356" width="2356" data-og-height="702" height="702" data-path="images/docs/39d09fdd09c068a8aa8ab32d14562b94b1da1fbb7221dc4a01ad8ae3c8058104-step18.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/39d09fdd09c068a8aa8ab32d14562b94b1da1fbb7221dc4a01ad8ae3c8058104-step18.png?w=280&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=5910c7eaef4afd59af07f92718d791ca 280w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/39d09fdd09c068a8aa8ab32d14562b94b1da1fbb7221dc4a01ad8ae3c8058104-step18.png?w=560&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=6f9bcdd78086c1556e009e3f58138e8f 560w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/39d09fdd09c068a8aa8ab32d14562b94b1da1fbb7221dc4a01ad8ae3c8058104-step18.png?w=840&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=d8bc46e02617a63360c60760801b8591 840w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/39d09fdd09c068a8aa8ab32d14562b94b1da1fbb7221dc4a01ad8ae3c8058104-step18.png?w=1100&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=e2d93451515249af3ba0a55b244c4ab4 1100w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/39d09fdd09c068a8aa8ab32d14562b94b1da1fbb7221dc4a01ad8ae3c8058104-step18.png?w=1650&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=d877c2c71dd53c9c2736675c24b8cdac 1650w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/39d09fdd09c068a8aa8ab32d14562b94b1da1fbb7221dc4a01ad8ae3c8058104-step18.png?w=2500&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=cae2546ea6c9999cfb03edde675e3222 2500w" />
</Frame>

<Info>
  If you're having trouble installing the Worker, please refer to our [MacOS Worker troubleshooting guide](/guides/workers/troubleshoot-macos-worker) or the [general Worker troubleshooting guide](/guides/workers/troubleshoot-worker-general). If the issue persists or you need further assistance, feel free to [check our knowledge base](https://support.io.net/en/support/home) for answers, and if you still need help, don’t hesitate to open a support ticket!
</Info>

<Warning>
  Be aware that you will be installing a 20GB size container. This contains all the packages needed to serve AI/ML apps. Everything happens inside the container, nothing within the container can access your filesystem
</Warning>
