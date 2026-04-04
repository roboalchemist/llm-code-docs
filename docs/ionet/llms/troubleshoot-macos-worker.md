# Source: https://io.net/docs/guides/workers/troubleshoot-macos-worker.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MacOS: Troubleshoot Worker

> Here we've compiled essential use cases for working with Workers.

### Bad CPU Type in Executable Error

If you come across an error message like "**bad CPU type in executable**," it's likely because you are trying to run software intended for an Intel processor on an Apple Silicon device. To resolve this issue, you'll need to install <Tooltip tip="Rosetta 2 - It's a special software for Applecomputers with M1 chips that lets them run appsdesigned for older Intel-based Macs. It works behindthe scenes to translate the app's instructions so theycan work on the new hardware, allowing you to useyour favorite apps even if they haven't been updatedfor the new chips.">Rosetta 2</Tooltip>, which enables support for Intel processors to operate within <Tooltip tip="Docker - Docker is a platform that allows developersto develop, ship, and run applications in containers.Containers are lightweight, portable, and self-sufficient units that contain everything needed torun an application, including the code, runtimesystem tools, libraries, and settings. Docker providesa way to package and distribute applications alongwith their dependencies, making it easier to deployand manage software across different environments.">Docker</Tooltip> on Apple Silicon devices.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4a32aae9cbd68b26055a5b9b77e61acf30e4af23669266ddc0c4f72a34defdf8-BadCPU.jpg?fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=bb40f8a71acfcac302f13d63b30d8c02" alt="" data-og-width="1571" width="1571" data-og-height="594" height="594" data-path="images/docs/4a32aae9cbd68b26055a5b9b77e61acf30e4af23669266ddc0c4f72a34defdf8-BadCPU.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4a32aae9cbd68b26055a5b9b77e61acf30e4af23669266ddc0c4f72a34defdf8-BadCPU.jpg?w=280&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=67c7cf899ad65aa8819653a8b70ef231 280w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4a32aae9cbd68b26055a5b9b77e61acf30e4af23669266ddc0c4f72a34defdf8-BadCPU.jpg?w=560&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=5d4ff91371a02caa95f04f8922332cb9 560w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4a32aae9cbd68b26055a5b9b77e61acf30e4af23669266ddc0c4f72a34defdf8-BadCPU.jpg?w=840&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=784b5020b701643b58684d2397d76402 840w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4a32aae9cbd68b26055a5b9b77e61acf30e4af23669266ddc0c4f72a34defdf8-BadCPU.jpg?w=1100&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=20b621d1818ef4cdd3e85843cdfa2817 1100w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4a32aae9cbd68b26055a5b9b77e61acf30e4af23669266ddc0c4f72a34defdf8-BadCPU.jpg?w=1650&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=33df1deb62b39230a31f3fcb0f69a838 1650w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4a32aae9cbd68b26055a5b9b77e61acf30e4af23669266ddc0c4f72a34defdf8-BadCPU.jpg?w=2500&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=80921e90eebcde27e8bbff9ac923c981 2500w" />
</Frame>

To check if Rosetta is installed and active, enter the following command in the Terminal and press Enter:

```
/usr/sbin/sysctl sysctl.proc_translated
```

If the output is **sysctl.proc\_translated: 1**, Rosetta is installed and active on your system. If the output is either **sysctl.proc\_translated: 0** or there is **no output**, Rosetta is not installed or not active.

If Rosetta 2 is not installed, use this command to install it:

```
softwareupdate --install-rosetta --agree-to-license
```

Once Rosetta 2 installation is complete, rerun the execution command:

```
./io_net_launch_binary_mac
```

### Common Issue: Container CPU Dropping to 0

A common issue that many users encounter is the CPU of the container dropping to 0.

This problem is often due to missing necessary software components. You need to install[Rosetta](/guides/workers/install-on-macos#7-download-and-launch-io-binary). Detailed instructions on how to install these software components can be found in this section above.

If you still encounter this issue after installing all the necessary software components, try deleting the containers and images, then **re-run** the worker command and wait. You may need to repeat this process 3 or 4 times until they function normally. If the issue persists after these steps, it may indicate a system-level error.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6405c7cfbb60fe583e7f6cc3c7c930ca249f2417e4f1287522a7341f25c37272-UseCases-NoContainersCPU0.jpg?fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=906cf8bcb8beb78688c531ec4559b681" alt="" data-og-width="2072" width="2072" data-og-height="1198" height="1198" data-path="images/docs/6405c7cfbb60fe583e7f6cc3c7c930ca249f2417e4f1287522a7341f25c37272-UseCases-NoContainersCPU0.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6405c7cfbb60fe583e7f6cc3c7c930ca249f2417e4f1287522a7341f25c37272-UseCases-NoContainersCPU0.jpg?w=280&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=2c4f6046f93f5277f7ed0d5e23057406 280w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6405c7cfbb60fe583e7f6cc3c7c930ca249f2417e4f1287522a7341f25c37272-UseCases-NoContainersCPU0.jpg?w=560&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=695c4e89902cb5d7ab827fd11e805b06 560w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6405c7cfbb60fe583e7f6cc3c7c930ca249f2417e4f1287522a7341f25c37272-UseCases-NoContainersCPU0.jpg?w=840&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=bc3edf29d89687dba8e624f80eb31d1f 840w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6405c7cfbb60fe583e7f6cc3c7c930ca249f2417e4f1287522a7341f25c37272-UseCases-NoContainersCPU0.jpg?w=1100&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=ba433e2847291d066b3d098ead01e3e4 1100w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6405c7cfbb60fe583e7f6cc3c7c930ca249f2417e4f1287522a7341f25c37272-UseCases-NoContainersCPU0.jpg?w=1650&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=f31bca48299ba384dad0488359e6ef08 1650w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6405c7cfbb60fe583e7f6cc3c7c930ca249f2417e4f1287522a7341f25c37272-UseCases-NoContainersCPU0.jpg?w=2500&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=59375a6f072ac6acc036da149db78bcd 2500w" />
</Frame>

<Info>
  For general questions about the Worker, no matter the operating system, check [here](/guides/workers/troubleshoot-worker-general)
</Info>

<Info>
  Feel free to [check our knowledge base](https://support.io.net/en/support/home) for answers, and if you still need help, don’t hesitate to open a support ticket!
</Info>
