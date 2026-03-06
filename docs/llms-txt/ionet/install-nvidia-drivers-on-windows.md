# Source: https://io.net/docs/guides/workers/install-nvidia-drivers-on-windows.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Install Nvidia Drivers

> A step-by-step guide for installing Nvidia Drivers on Windows-based machines.

### What are Nvidia Drivers?

NVIDIA drivers are software packages that allow your computer's operating system to communicate effectively with NVIDIA graphics cards. These drivers ensure that your GPU can perform optimally, providing support for various features such as graphical rendering, video playback, and gaming performance. Keeping your NVIDIA drivers up to date is important for maintaining system stability, compatibility with new software, and obtaining the best performance from your graphics card.

### 1. Open Windows Terminal From the Start Menu

Click the Start Menu icon in the popup Menu, type Terminal in the search field, then click **Terminal**.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/ae154c4-Step9-2-2.jpeg?fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=2b34318fdf98bb835a76770a7f0a0083" alt="" className="mx-auto" style={{ width:"63%" }} data-og-width="871" width="871" data-og-height="499" height="499" data-path="images/docs/ae154c4-Step9-2-2.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/ae154c4-Step9-2-2.jpeg?w=280&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=bd87d679f387d800a8720bf927303d07 280w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/ae154c4-Step9-2-2.jpeg?w=560&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=7400f709903a7d4d6d689b758b90e93b 560w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/ae154c4-Step9-2-2.jpeg?w=840&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=13a3b84d0f388f6c6df666e210591315 840w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/ae154c4-Step9-2-2.jpeg?w=1100&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=80a15c502dee6ec0b742f1c3f7588866 1100w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/ae154c4-Step9-2-2.jpeg?w=1650&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=2e9e44308baabb0e3ac66f88be75b3a8 1650w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/ae154c4-Step9-2-2.jpeg?w=2500&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=a850044f87755ae07699bee1e77deaa8 2500w" />
</Frame>

### 2. Verify That the Correct Drivers Are Installed

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a998aa8-Step2.jpg?fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=e5804d6d7b4d408bdd84aa23655012b8" alt="" className="mx-auto" style={{ width:"62%" }} data-og-width="771" width="771" data-og-height="407" height="407" data-path="images/docs/a998aa8-Step2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a998aa8-Step2.jpg?w=280&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=f1c32a7bbe8b520cdeb4e8c593f288c2 280w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a998aa8-Step2.jpg?w=560&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=d435e7116ed245b0d00ab21ae0c1a242 560w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a998aa8-Step2.jpg?w=840&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=a47622bd45037d81a6f97b48c096c3d7 840w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a998aa8-Step2.jpg?w=1100&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=6f9edf185ad046f83b373fee0220875c 1100w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a998aa8-Step2.jpg?w=1650&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=5aeb6b8414c3f3281450688c9cab76dd 1650w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a998aa8-Step2.jpg?w=2500&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=b46c2b99a955432933e4697ea9f9a819 2500w" />
</Frame>

To check that you have the correct drivers, open a command line on your Windows PC (Windows key + R, type cmd) and type into it the following.

<CodeGroup>
  ```Text Terminal Command theme={null}
  nvidia-smi
  ```
</CodeGroup>

If you encounter the following error message:

```
C://Users>nvidia-smi  
'nvidia-smi' is not recognized as an internal or external command,  
operable program or batch file.
```

It means that you do not have NVIDIA drivers installed. To install them, follow the steps below:

### 3. Go to [Nvidia Driver](https://www.nvidia.com/download/index.aspx) Download Page

Choose your GPU's name, then click on search.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/78d7e60-Step3.jpg?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=52a110e6e267feb9fa41789fd2e721c9" alt="" data-og-width="1314" width="1314" data-og-height="722" height="722" data-path="images/docs/78d7e60-Step3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/78d7e60-Step3.jpg?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=bca2008c79cb23023de98be4113f1480 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/78d7e60-Step3.jpg?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=3c4c641e00ece6807abe94a4838c7f2e 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/78d7e60-Step3.jpg?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=f46c94d2ad9cf693c743df39c5de695d 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/78d7e60-Step3.jpg?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=77169db78c6c784f7dd584f990152fc6 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/78d7e60-Step3.jpg?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=6c6734c01d77cf3b80b81b748e6f91cc 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/78d7e60-Step3.jpg?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=a160b88c9a4ee2d51cf5699ab0f20a22 2500w" />
</Frame>

### 4. Download the Driver Installation File

Click the **Download** button for the NVIDIA driver that matches your GPU and Windows version.

<Info>
  Driver Version 552.44 is currently the most stable & tested driver.
</Info>

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0d857d5-Step4.jpg?fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=69de1bb256d19036e4369bb4d9a0d681" alt="" data-og-width="1448" width="1448" data-og-height="674" height="674" data-path="images/docs/0d857d5-Step4.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0d857d5-Step4.jpg?w=280&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=65de6b79c8cc3956e85cbce149785ee3 280w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0d857d5-Step4.jpg?w=560&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=3d3087802a438f4bfc37eb9eff1fa301 560w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0d857d5-Step4.jpg?w=840&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=50371d97ce5db9a0aaee8f6b064867a4 840w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0d857d5-Step4.jpg?w=1100&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=a2863a746efd86edd4e774540c673934 1100w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0d857d5-Step4.jpg?w=1650&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=3ce37ba7f985367022bafa84c335f215 1650w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0d857d5-Step4.jpg?w=2500&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=b5ae518a035c10b3e56cbdda50af8a6d 2500w" />
</Frame>

### 5. Open the .Exe File and Proceed With the Installation Process

Once the download is complete, start the installation, select the first option and click on "Agree and Continue."

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/bf1998b-Step5.jpg?fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=e5422e0ea84671db78cd1f4d2acbd1dd" alt="" className="mx-auto" style={{ width:"67%" }} data-og-width="1580" width="1580" data-og-height="1232" height="1232" data-path="images/docs/bf1998b-Step5.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/bf1998b-Step5.jpg?w=280&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=2c468470d4d8f8e6710b336f5fc777aa 280w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/bf1998b-Step5.jpg?w=560&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=878979582d712540d13c6355c0ecd2e9 560w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/bf1998b-Step5.jpg?w=840&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=e2ce0b3039523909ef5c7e447e797b04 840w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/bf1998b-Step5.jpg?w=1100&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=8f9ebcc6efd7e65bc558da367aabedaa 1100w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/bf1998b-Step5.jpg?w=1650&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=cd2bc046376433d4159f5a68442b1f26 1650w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/bf1998b-Step5.jpg?w=2500&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=2c7fe4f15205c5379a935ad4fc592ad1 2500w" />
</Frame>

### 6. Reboot your computer

After the installation is complete, it's essential to reboot your computer. Restart your machine to ensure that the new NVIDIA driver is fully integrated into your system.

### 7. Verify the Installation Process

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d83fe1a-Step6.jpg?fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=6da0510b1bfc2a336c899dc58fa942ae" alt="" className="mx-auto" style={{ width:"66%" }} data-og-width="760" width="760" data-og-height="569" height="569" data-path="images/docs/d83fe1a-Step6.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d83fe1a-Step6.jpg?w=280&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=de187cda307ec757627687354d004f07 280w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d83fe1a-Step6.jpg?w=560&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=5c5ddc732834751a06c248ede4bd966d 560w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d83fe1a-Step6.jpg?w=840&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=d0ef2fb120be930061b7d74d9935b0f7 840w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d83fe1a-Step6.jpg?w=1100&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=84358a490cc4a25370acb7f070bac384 1100w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d83fe1a-Step6.jpg?w=1650&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=5de4efbca81e893d6c16a9f87cf2d4f6 1650w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d83fe1a-Step6.jpg?w=2500&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=1184d90a7d32d4dc1bbc40b6dec4fc54 2500w" />
</Frame>

After your computer reboots, open Windows Terminal from the Start Menu and enter the following command:

<CodeGroup>
  ```Text Terminal Command theme={null}
  nvidia-smi
  ```
</CodeGroup>

You should see this outcome:

```
+ — — — — — — — — — — — — — — — — — — — — — — — — + — — — — — — — — — —  +
| GPU  Name         TCC/WDDM                      | Bus-Id        Disp.A |
| Fan  Temp  Perf   Pwr:Usage/Cap                 |         Memory-Usage |
|                                                 |                      |
+ = = = = = = = = = = = = = = = = = = = = = = = = + = = = = = = = = = =  +
| 0   NVIDIA GeForce GTX 1070 Ti       WDDM       |     00000000:01:00.0 |
| 0%  53C    P8                  13W / 180W       |     503МіВ / 8192MiB |
|                                                 |                      |
+ — — — — — — — — — — — — — — — — — — — — — — — — + — — — — — — — — — —  +
| 0   NVIDIA GeForce GTX 1070 Ti       WDDM       | 00000000:02:00.0 0ff |
| 0%  49C    P8                  10W / 180W       |       OMiB / 8192MiB |
|                                                 |                      |
+ — — — — — — — — — — — — — — — — — — — — — — — — + — — — — — — — — — —  +
```

### That’s It. You Have the Nvidia Drivers Installed and Ready.

Now that CUDA Toolkit has been successfully installed and is running, you can proceed with [setting up the Worker](/guides/workers/install-on-windows).

<Info>
  Feel free to [check our knowledge base](https://support.io.net/en/support/home) for answers, and if you still need help, don’t hesitate to open a support ticket!
</Info>
