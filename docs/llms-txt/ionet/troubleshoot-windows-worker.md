# Source: https://io.net/docs/guides/workers/troubleshoot-windows-worker.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Windows: Troubleshoot Worker

> Here we've compiled essential use cases for working with Workers.

### How to Resolve Unsupported GPU Issues?

If a user's supported GPU is listed as unsupported on the website, they should verify their NVIDIA driver configuration. Often, when a Docker container running **nvidia-smi** fails, the backend receives this information and marks the GPU as unsupported.

To check the configuration, running the following command should provide the correct output:

```
docker run --gpus all nvidia/cuda:11.0.3-base-ubuntu18.04 nvidia-smi
```

### Regulate RAM Usage

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/18ae7a1-RamIssue.jpg?fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=fa56275b59ab71ffd450138724d42b3c" alt="" className="mx-auto" style={{ width:"77%" }} data-og-width="1194" width="1194" data-og-height="138" height="138" data-path="images/docs/18ae7a1-RamIssue.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/18ae7a1-RamIssue.jpg?w=280&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=eed9831a44ebc7eeae88279b245bf65f 280w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/18ae7a1-RamIssue.jpg?w=560&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=5dd139095bf7663615d2489961b6526d 560w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/18ae7a1-RamIssue.jpg?w=840&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=3859e9d5322584a8da1171fe72a711d9 840w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/18ae7a1-RamIssue.jpg?w=1100&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=804803bf9f71283ee71e3ed12319cb0c 1100w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/18ae7a1-RamIssue.jpg?w=1650&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=a84d30cb18fa8182cc9ff03ec8783bb4 1650w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/18ae7a1-RamIssue.jpg?w=2500&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=06b45bb730bb7efc8f9bb531c41caed3 2500w" />
</Frame>

Create a file called **.wslconfig** to restrict the resources used by **WSL2** (Windows Subsystem for Linux). Follow the steps below to create it:

* **Open File Explorer** and navigate to your user's home directory (usually **`C:/Users/<Username>`**).
* **Create a new text file** in your home directory and name it **.wslconfig**.
* **Edit the .wslconfig File:** Right-click on the newly created **.wslconfig** file and open it with a text editor such as Notepad.
* **Add the following configuration parameters** to limit memory (set values according to your preference):

  ```
  [wsl2]  
  memory=4GB # Limits the VM memory in WSL between 2 and 4 GB  
  processors=2 # Limits the number of processors to 2  
  swap=8GB # Sets the swap size to 8 GB
  ```
* **Save the file and restart your computer**. If the worker does not connect automatically, you may [need to install it again](/guides/workers/troubleshoot-worker-general#how-can-i-pause-or-reset-a-worker-if-it-has-disconnection-issues).

### Computer Time Synchronization Issue

Make sure your computer's time is synchronized with the server. If it's not, the IO binary won't work properly. Click the **Start Menu** and open the **Settings** app.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8ea9a4c3c0f092316eec2a18c72e10d22af5863b8583b032a6c22600d08c2384-win1.jpg?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=22b3d44adac98a9834769894d07a8c89" alt="" className="mx-auto" style={{ width:"75%" }} data-og-width="2236" width="2236" data-og-height="876" height="876" data-path="images/docs/8ea9a4c3c0f092316eec2a18c72e10d22af5863b8583b032a6c22600d08c2384-win1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8ea9a4c3c0f092316eec2a18c72e10d22af5863b8583b032a6c22600d08c2384-win1.jpg?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=e9cd5fca4b3ed6899d6cf5fbe36bdaf2 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8ea9a4c3c0f092316eec2a18c72e10d22af5863b8583b032a6c22600d08c2384-win1.jpg?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=0d05ceb739e6a6c78fddc220ebccc82c 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8ea9a4c3c0f092316eec2a18c72e10d22af5863b8583b032a6c22600d08c2384-win1.jpg?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=bfcaa92a8ab2808fce739a45497fa506 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8ea9a4c3c0f092316eec2a18c72e10d22af5863b8583b032a6c22600d08c2384-win1.jpg?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=268dfaebe483a846e2e2ec6a45817545 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8ea9a4c3c0f092316eec2a18c72e10d22af5863b8583b032a6c22600d08c2384-win1.jpg?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=222faed284befc3e890e45001d83ff0f 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8ea9a4c3c0f092316eec2a18c72e10d22af5863b8583b032a6c22600d08c2384-win1.jpg?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=828725f32a573a92723fecde3ab55650 2500w" />
</Frame>

Next, in the **Settings** app, go to **Time & Language** and select **Date & Time**. Then, under **Additional settings,** click the **Sync now** button to synchronize your computer's time with the server.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3c9dc71d5678cdf1e0cdfa4d7499f6b80c4c37af21365540c7ca1116643a87ac-win2.jpg?fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=ad0fb2a718ec9dd7e7214c29494f33e5" alt="" data-og-width="2422" width="2422" data-og-height="906" height="906" data-path="images/docs/3c9dc71d5678cdf1e0cdfa4d7499f6b80c4c37af21365540c7ca1116643a87ac-win2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3c9dc71d5678cdf1e0cdfa4d7499f6b80c4c37af21365540c7ca1116643a87ac-win2.jpg?w=280&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=da8800871d486c58f5a9eb79a6689559 280w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3c9dc71d5678cdf1e0cdfa4d7499f6b80c4c37af21365540c7ca1116643a87ac-win2.jpg?w=560&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=1b2740e6d50e6dcab4e90feeb746beec 560w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3c9dc71d5678cdf1e0cdfa4d7499f6b80c4c37af21365540c7ca1116643a87ac-win2.jpg?w=840&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=9d4cb18f2e3585a29dde9f27bab66e5c 840w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3c9dc71d5678cdf1e0cdfa4d7499f6b80c4c37af21365540c7ca1116643a87ac-win2.jpg?w=1100&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=055f2b9af4f6f205dc2f040b6e8a546f 1100w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3c9dc71d5678cdf1e0cdfa4d7499f6b80c4c37af21365540c7ca1116643a87ac-win2.jpg?w=1650&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=7034973806db0d83d3b8c784a1e480e4 1650w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3c9dc71d5678cdf1e0cdfa4d7499f6b80c4c37af21365540c7ca1116643a87ac-win2.jpg?w=2500&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=77c14d814fce602878f199cbf07a6998 2500w" />
</Frame>

### Common Issue: Container CPU Dropping to 0

A common issue that many users encounter is the CPU of the container dropping to 0.

This problem is often due to missing necessary software components. For instance, on Windows, you need to ensure [CUDA](/guides/workers/cuda-toolkit-optional) and [WSL2](/guides/workers/install-docker-on-windows#3-configure-wsl2-to-integrate-with-docker-settings) are installed.

If you still encounter this issue after installing all the necessary software components, try deleting the containers and images, then **re-run** the worker command and wait. You may need to repeat this process 3 or 4 times until they function normally. If the issue persists after these steps, it may indicate a system-level error.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/76dd63ed4563198c02ef6d3a7c1fb01de5776790ab965a9437a56ab13604bf0a-UseCases-NoContainersCPU0_Copy.jpg?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=6cb89cf6909998a40bdaf89cccf5fee8" alt="" data-og-width="2072" width="2072" data-og-height="1198" height="1198" data-path="images/docs/76dd63ed4563198c02ef6d3a7c1fb01de5776790ab965a9437a56ab13604bf0a-UseCases-NoContainersCPU0_Copy.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/76dd63ed4563198c02ef6d3a7c1fb01de5776790ab965a9437a56ab13604bf0a-UseCases-NoContainersCPU0_Copy.jpg?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=77f531a74dda18110835a4b2a06691a0 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/76dd63ed4563198c02ef6d3a7c1fb01de5776790ab965a9437a56ab13604bf0a-UseCases-NoContainersCPU0_Copy.jpg?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=fd3d8889b9b9703c401a8c4f5c860579 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/76dd63ed4563198c02ef6d3a7c1fb01de5776790ab965a9437a56ab13604bf0a-UseCases-NoContainersCPU0_Copy.jpg?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=8a6a85530fbe83667396c6b903fc06a2 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/76dd63ed4563198c02ef6d3a7c1fb01de5776790ab965a9437a56ab13604bf0a-UseCases-NoContainersCPU0_Copy.jpg?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=b681daa4c31e175e0ec574a208679c9f 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/76dd63ed4563198c02ef6d3a7c1fb01de5776790ab965a9437a56ab13604bf0a-UseCases-NoContainersCPU0_Copy.jpg?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=89c6b5fac63d9409a78757c03b48d37a 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/76dd63ed4563198c02ef6d3a7c1fb01de5776790ab965a9437a56ab13604bf0a-UseCases-NoContainersCPU0_Copy.jpg?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=69a11f26f4329e104024a5ebb11f11f9 2500w" />
</Frame>

<Info>
  For general questions about the Worker, no matter the operating system, check [here](https://docs.io.net/docs/troubleshoot-worker-general)
</Info>

<Info>
  Feel free to [check our knowledge base](/guides/workers/troubleshoot-worker-general) for answers, and if you still need help, don’t hesitate to open a support ticket!
</Info>
