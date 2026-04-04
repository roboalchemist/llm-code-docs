# Source: https://io.net/docs/guides/workers/install-docker-on-windows.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Windows: Install Docker

> A step-by-step guide for installing Docker on Windows-based machines

<iframe width="100%" src="https://www.youtube.com/embed/ipMRoTos7BU" title="Docker Guide for Windows" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

### What is Docker?

Let's take a quick look at what **Docker** is? Imagine Docker as a magic box where you put your software and everything it needs to run. This box can be easily carried to any computer, and when you open it, your software works just the way you packed it, without needing anything extra from that computer. Here are a few steps to install Docker:

<Danger>
  **Network Capability Issue on Docker Desktop for Windows**

  We are currently investigating a network performance issue with Docker Desktop on Windows. This might be due to Docker's overhead, and we are exploring potential fixes.

  **Recommendation**: \
  If you experience this issue, we recommend switching to Linux as a temporary workaround.

  Thank you for your understanding and patience.
</Danger>

### First, verify that Virtualization is Enabled on your Computer.

To verify if virtualization is enabled, open **Task Manager** by pressing Ctrl+Alt+Del. Select "**Performance**" and then click on the "**CPU**" tab to view the information in the bottom right corner, as shown in the image below:

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/def0a77ce8b421fc05925437a64177eee107962c5b36a64bbd4872068c98e334-Step1.jpg?fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=05e23ad20851443ee4d084287d60edf6" alt="" data-og-width="1918" width="1918" data-og-height="1288" height="1288" data-path="images/docs/def0a77ce8b421fc05925437a64177eee107962c5b36a64bbd4872068c98e334-Step1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/def0a77ce8b421fc05925437a64177eee107962c5b36a64bbd4872068c98e334-Step1.jpg?w=280&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=8a9c47917df6f8292b2860e5314bd2f6 280w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/def0a77ce8b421fc05925437a64177eee107962c5b36a64bbd4872068c98e334-Step1.jpg?w=560&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=f32eb6970e467265a33b5d73deede666 560w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/def0a77ce8b421fc05925437a64177eee107962c5b36a64bbd4872068c98e334-Step1.jpg?w=840&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=ae1e003fcf42623c8c11ec785ea297f1 840w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/def0a77ce8b421fc05925437a64177eee107962c5b36a64bbd4872068c98e334-Step1.jpg?w=1100&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=f164578d0b6ad5a6e94ef47faa70bef0 1100w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/def0a77ce8b421fc05925437a64177eee107962c5b36a64bbd4872068c98e334-Step1.jpg?w=1650&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=b1f92f8a0ee00b411557536f3b225354 1650w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/def0a77ce8b421fc05925437a64177eee107962c5b36a64bbd4872068c98e334-Step1.jpg?w=2500&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=0f6c6f178c0f93e4b724af423ff9144a 2500w" />
</Frame>

<Warning>
  If it's not enabled, follow these steps:
</Warning>

1. To enable virtualization technology in your BIOS or UEFI settings, you need to access your computer's BIOS or UEFI configuration menu during the boot process. The specific steps can vary depending on your computer's manufacturer and model, but here are the general steps to enable virtualization.
2. Install WSL 2 by opening the PowerShell as an Administrator. To do this, search for "PowerShell" in the Start menu, right-click on "Windows PowerShell," and select "Run as administrator."
3. Run the following command to enable the WSL feature in **Windows 10/11** in Terminal:

   <CodeGroup>
     ```Text Terminal Command theme={null}
     dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
     ```
   </CodeGroup>
4. Then **Enable** the Virtual Machine Platform Feature while still in the same PowerShell window by running the following command:

   <CodeGroup>
     ```Text Terminal Command theme={null}
     dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
     ```
   </CodeGroup>
5. Then set WSL 2 as the Default Version (you might be required to restart your machine sometimes):

   <CodeGroup>
     ```Text Terminal Command theme={null}
     wsl --set-default-version 2
     ```
   </CodeGroup>

### 1. Download Docker

Go to the [Docker website](https://www.docker.com/products/docker-desktop/) and click on "**Download for Windows**." Downloading the Docker file may take some time. Please be patient.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/95a4cbd4f0ddf46a9d3ba867b4ca911ed1c7cd2851927842a9fed04a117aabd2-Step2.jpg?fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=12f93525abe755016f0de00dc5ae61ba" alt="" data-og-width="1063" width="1063" data-og-height="701" height="701" data-path="images/docs/95a4cbd4f0ddf46a9d3ba867b4ca911ed1c7cd2851927842a9fed04a117aabd2-Step2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/95a4cbd4f0ddf46a9d3ba867b4ca911ed1c7cd2851927842a9fed04a117aabd2-Step2.jpg?w=280&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=68bf0a62c3cc3cc6d9c3ce295960e394 280w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/95a4cbd4f0ddf46a9d3ba867b4ca911ed1c7cd2851927842a9fed04a117aabd2-Step2.jpg?w=560&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=4a10b9a1d0316ba57192e00c294f6512 560w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/95a4cbd4f0ddf46a9d3ba867b4ca911ed1c7cd2851927842a9fed04a117aabd2-Step2.jpg?w=840&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=78661964e8f2223ca62620555823fd7e 840w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/95a4cbd4f0ddf46a9d3ba867b4ca911ed1c7cd2851927842a9fed04a117aabd2-Step2.jpg?w=1100&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=eb881e9958dd4db7edbd9a47004e173a 1100w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/95a4cbd4f0ddf46a9d3ba867b4ca911ed1c7cd2851927842a9fed04a117aabd2-Step2.jpg?w=1650&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=8832cf0f6bc1b9b2447ac256f899e481 1650w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/95a4cbd4f0ddf46a9d3ba867b4ca911ed1c7cd2851927842a9fed04a117aabd2-Step2.jpg?w=2500&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=9f58270eb12256f831c81af7900727a7 2500w" />
</Frame>

### 2. Run the Installation Process

The installation starts when you open the file. Follow the prompts. When the installation process is completed, you need to **restart your computer.** Just click the "**Close and Restart**" button on the last step of the Docker wizard:

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e5eebdef187efd9de0b73eb2b2acc408d5c530c1bf8c197e3c484c0d8a1328fb-Step3.jpg?fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=bfa4f3e5363e9c47cca77c7d46cd41e0" alt="" data-og-width="1103" width="1103" data-og-height="487" height="487" data-path="images/docs/e5eebdef187efd9de0b73eb2b2acc408d5c530c1bf8c197e3c484c0d8a1328fb-Step3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e5eebdef187efd9de0b73eb2b2acc408d5c530c1bf8c197e3c484c0d8a1328fb-Step3.jpg?w=280&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=1a84020805e91c7b9c8e205cfeb39679 280w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e5eebdef187efd9de0b73eb2b2acc408d5c530c1bf8c197e3c484c0d8a1328fb-Step3.jpg?w=560&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=0b81c0dceb4f5a8d160fb732487c03bf 560w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e5eebdef187efd9de0b73eb2b2acc408d5c530c1bf8c197e3c484c0d8a1328fb-Step3.jpg?w=840&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=5e1e94a0963ecad52e1bdfb4513a5eb5 840w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e5eebdef187efd9de0b73eb2b2acc408d5c530c1bf8c197e3c484c0d8a1328fb-Step3.jpg?w=1100&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=2848ca7f22d92a44904f41753278f846 1100w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e5eebdef187efd9de0b73eb2b2acc408d5c530c1bf8c197e3c484c0d8a1328fb-Step3.jpg?w=1650&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=2adb93aa928a4cb2488d1c68f14527e9 1650w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e5eebdef187efd9de0b73eb2b2acc408d5c530c1bf8c197e3c484c0d8a1328fb-Step3.jpg?w=2500&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=1009acf732c1a885dc9a030239f73dda 2500w" />
</Frame>

After rebooting, open Docker and use the recommended settings from the installation wizard:

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/32e6c86ea6a2eaf00a84d4320612a2567b1e9e50fcf5dfc575d5e9bb137cff52-Step4.jpg?fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=98be96b3ced485a3c665123e4b43dc00" alt="" className="mx-auto" style={{ width:"86%" }} data-og-width="1402" width="1402" data-og-height="1004" height="1004" data-path="images/docs/32e6c86ea6a2eaf00a84d4320612a2567b1e9e50fcf5dfc575d5e9bb137cff52-Step4.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/32e6c86ea6a2eaf00a84d4320612a2567b1e9e50fcf5dfc575d5e9bb137cff52-Step4.jpg?w=280&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=1a45efa7b606ae1149110e024e5efd1b 280w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/32e6c86ea6a2eaf00a84d4320612a2567b1e9e50fcf5dfc575d5e9bb137cff52-Step4.jpg?w=560&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=f67318923b873e0d8ac40339c968ba36 560w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/32e6c86ea6a2eaf00a84d4320612a2567b1e9e50fcf5dfc575d5e9bb137cff52-Step4.jpg?w=840&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=450b0427270a5b12eb28f268ef27187e 840w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/32e6c86ea6a2eaf00a84d4320612a2567b1e9e50fcf5dfc575d5e9bb137cff52-Step4.jpg?w=1100&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=8dfc47fc26891e2fdc23051fb00218b0 1100w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/32e6c86ea6a2eaf00a84d4320612a2567b1e9e50fcf5dfc575d5e9bb137cff52-Step4.jpg?w=1650&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=fdbc2c33e6b01d438abfe413d6911415 1650w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/32e6c86ea6a2eaf00a84d4320612a2567b1e9e50fcf5dfc575d5e9bb137cff52-Step4.jpg?w=2500&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=2c6a53e6abfee26d3f01b78d43a38cd9 2500w" />
</Frame>

### 3. Configure WSL2  to Integrate with Docker Settings

Open the Docker settings. In the Resources section, choose <Tooltip tip="WSL 2 – It's a feature in Windows that lets you run a full Linux system on your computer without needing to set up a separate machine or use complex software. It provides a seamless way to use Linux tools and applications alongside your regular Windows programs, making it easier for developers and tech enthusiasts to work with both systems at the same time.">WSL 2</Tooltip> Integration and check the box for <Tooltip tip="WSL 2 – It's a feature in Windows that lets you run a full Linux system on your computer without needing to set up a separate machine or use complex software. It provides a seamless way to use Linux tools and applications alongside your regular Windows programs, making it easier for developers and tech enthusiasts to work with both systems at the same time.">WSL 2</Tooltip> to integrate.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/9acbba90f47ce6f03d814f729865c5267d2d970267770e3a0ca750d623ad0943-Step5.jpg?fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=f13e7c7b6d080cfe9854074ff18144e3" alt="" data-og-width="1128" width="1128" data-og-height="807" height="807" data-path="images/docs/9acbba90f47ce6f03d814f729865c5267d2d970267770e3a0ca750d623ad0943-Step5.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/9acbba90f47ce6f03d814f729865c5267d2d970267770e3a0ca750d623ad0943-Step5.jpg?w=280&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=fd71cf0341bb7d87526f7764de56782c 280w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/9acbba90f47ce6f03d814f729865c5267d2d970267770e3a0ca750d623ad0943-Step5.jpg?w=560&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=d7b3f502fbb945e2534d9d419b448f66 560w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/9acbba90f47ce6f03d814f729865c5267d2d970267770e3a0ca750d623ad0943-Step5.jpg?w=840&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=f4ffe776e2e7193c56edfdc08b60379a 840w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/9acbba90f47ce6f03d814f729865c5267d2d970267770e3a0ca750d623ad0943-Step5.jpg?w=1100&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=f40722ec4465c41133088849a3d24538 1100w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/9acbba90f47ce6f03d814f729865c5267d2d970267770e3a0ca750d623ad0943-Step5.jpg?w=1650&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=3591f91ff60cafe0214c4e10f1cd32bb 1650w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/9acbba90f47ce6f03d814f729865c5267d2d970267770e3a0ca750d623ad0943-Step5.jpg?w=2500&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=6a87bbe8827e26707b82a245a2a0fbd9 2500w" />
</Frame>

### 4. Open Terminal Through Start Menu

Click the Start Menu icon in the Popup Menu, type Terminal in the search field, then click Terminal

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a16c898ed54cc7b42064f07705a1fe247e042b6889129d914721c51157b1f891-Step6.jpg?fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=28df9a8c92a3a860140b4d0a0baf761e" alt="" className="mx-auto" style={{ width:"81%" }} data-og-width="1748" width="1748" data-og-height="832" height="832" data-path="images/docs/a16c898ed54cc7b42064f07705a1fe247e042b6889129d914721c51157b1f891-Step6.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a16c898ed54cc7b42064f07705a1fe247e042b6889129d914721c51157b1f891-Step6.jpg?w=280&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=23e90f8758923a44e7412697996dccea 280w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a16c898ed54cc7b42064f07705a1fe247e042b6889129d914721c51157b1f891-Step6.jpg?w=560&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=0153712e18aa8a27110752fb951f3050 560w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a16c898ed54cc7b42064f07705a1fe247e042b6889129d914721c51157b1f891-Step6.jpg?w=840&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=6bc95cd8e77cdf13428b9119a3624739 840w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a16c898ed54cc7b42064f07705a1fe247e042b6889129d914721c51157b1f891-Step6.jpg?w=1100&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=d9b6a8cad45900b38f7cb6d618e6609f 1100w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a16c898ed54cc7b42064f07705a1fe247e042b6889129d914721c51157b1f891-Step6.jpg?w=1650&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=07114e75a6cedab07384d04b6fa337fb 1650w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a16c898ed54cc7b42064f07705a1fe247e042b6889129d914721c51157b1f891-Step6.jpg?w=2500&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=a69cac6728df158fba6bda194962a78e 2500w" />
</Frame>

### 5. Verify the Installation in Terminal

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c61ab3eb3a5d3772de6250efa527f9037f5d64a14e5808442de346b6a797baa1-Step7.jpg?fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=1b075bcbb0477e78401a6619dd9cc686" alt="" className="mx-auto" style={{ width:"78%" }} data-og-width="1930" width="1930" data-og-height="952" height="952" data-path="images/docs/c61ab3eb3a5d3772de6250efa527f9037f5d64a14e5808442de346b6a797baa1-Step7.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c61ab3eb3a5d3772de6250efa527f9037f5d64a14e5808442de346b6a797baa1-Step7.jpg?w=280&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=eb2141f5c03a81ff7ac70997c36d08c1 280w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c61ab3eb3a5d3772de6250efa527f9037f5d64a14e5808442de346b6a797baa1-Step7.jpg?w=560&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=22ad8d6ffe948b1681cc6b3a321c11d0 560w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c61ab3eb3a5d3772de6250efa527f9037f5d64a14e5808442de346b6a797baa1-Step7.jpg?w=840&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=a72c0cb3ca0e46370036b78e4e383e3c 840w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c61ab3eb3a5d3772de6250efa527f9037f5d64a14e5808442de346b6a797baa1-Step7.jpg?w=1100&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=da6883af2ab1e44c6260f4d75fb2b3f6 1100w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c61ab3eb3a5d3772de6250efa527f9037f5d64a14e5808442de346b6a797baa1-Step7.jpg?w=1650&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=7957628231070b3ff397b07ca9f56099 1650w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c61ab3eb3a5d3772de6250efa527f9037f5d64a14e5808442de346b6a797baa1-Step7.jpg?w=2500&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=e179a2720ee95c1f4879ace243465f4a 2500w" />
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

### Congratulations on Successfully Setting up Docker

Now that Docker has been successfully installed and is running, you can proceed with [setting up the Worker](/guides/workers/install-on-windows).

<Info>
  If you encounter issues with Docker, please refer to our [Troubleshooting Docker guide](/guides/workers/troubleshoot-docker). If the problem persists or if you need further assistance, feel free to [check our knowledge base](https://support.io.net/en/support/home) for answers, and if you still need help, don’t hesitate to open a support ticket!
</Info>
