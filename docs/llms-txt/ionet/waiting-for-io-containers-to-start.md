# Source: https://io.net/docs/guides/workers/waiting-for-io-containers-to-start.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Waiting for IO Containers to Start

> On Linux the above issue can be due to several reasons:

1. **Nvidia-container-toolkit.** Ensure the Nvidia-container-toolkit is installed and properly configured.
2. **Docker Daemon.** Check if Docker Daemon is running.
3. **GPU Configuration.** Docker needs to be configured with the Nvidia runtime to use the GPU inside a container. This can be fixed by installing and configuring the Nvidia-container-toolkit.

#### Debugging:

1. **Test GPU with Docker:** Run the following command to check if Docker can access the GPU:

   ```
   docker run --gpus all nvidia/cuda:11.0.3-base-ubuntu18.04 nvidia-smi
   ```

   If **nvidia-smi** output is visible, Docker can use the GPU inside the container. If not, try restarting Docker Daemon:

   ```
   sudo systemctl restart docker
   ```

   Else there might be some error similar to the following:

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/b20e0c8a98d9e63c35891572cd23469c5e9ccc677ee7c2b9b23554413ebb3b5b-DockerIssue2.jpg?fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=244c7992e2962f6766e090e519310872" alt="" className="mx-auto" style={{ width:"82%" }} data-og-width="1314" width="1314" data-og-height="1208" height="1208" data-path="images/docs/b20e0c8a98d9e63c35891572cd23469c5e9ccc677ee7c2b9b23554413ebb3b5b-DockerIssue2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/b20e0c8a98d9e63c35891572cd23469c5e9ccc677ee7c2b9b23554413ebb3b5b-DockerIssue2.jpg?w=280&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=7f1b97b1179f4c4cc731b0b04066dbe5 280w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/b20e0c8a98d9e63c35891572cd23469c5e9ccc677ee7c2b9b23554413ebb3b5b-DockerIssue2.jpg?w=560&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=4d9a03fecde9638befc637952567e46d 560w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/b20e0c8a98d9e63c35891572cd23469c5e9ccc677ee7c2b9b23554413ebb3b5b-DockerIssue2.jpg?w=840&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=9bb7c69f32e9b8d774cce195139d9f0f 840w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/b20e0c8a98d9e63c35891572cd23469c5e9ccc677ee7c2b9b23554413ebb3b5b-DockerIssue2.jpg?w=1100&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=52ea6b99c04eb2b82befb4bc254a4c26 1100w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/b20e0c8a98d9e63c35891572cd23469c5e9ccc677ee7c2b9b23554413ebb3b5b-DockerIssue2.jpg?w=1650&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=23bd177aae9a46546591603074ae8224 1650w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/b20e0c8a98d9e63c35891572cd23469c5e9ccc677ee7c2b9b23554413ebb3b5b-DockerIssue2.jpg?w=2500&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=85f42ac048a12495c66fe75e0be0f75e 2500w" />
   </Frame>
2. **Error Debugging:** If errors related to **nvidia-container-toolkit** are shown, it may not be installed or configured correctly.

#### Commands to Check Nvidia-container-toolkit Installation:

1. Check if Nvidia-container-toolkit is installed:

   ```
   nvidia-container-runtime --version
   dpkg -l | grep nvidia-container-toolkit
   ```
2. If it's installed but not configured properly, follow one of the two methods below:

#### Method 1: Configure daemon.json:

1. Open the daemon.json file:

   ```
   sudo nano /etc/docker/daemon.json
   ```
2. Paste the following:

   ```
   {
      "runtimes": {
        "nvidia": {
          "path": "nvidia-container-runtime",
          "runtimeArgs": []
        }
      },
      "default-runtime": "nvidia"
   }
   ```
3. Save and exit, then reboot the server:

   ```
   sudo reboot
   ```
4. After reboot, restart Docker:

   ```
   sudo systemctl restart docker
   ```

#### Method 2: Configure Nvidia-ctk Directly:

Run the following commands:

```
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```

#### If Nvidia-container-toolkit is Not Installed:

1. Install Nvidia-container-toolkit:

   ```
   curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg && /
   curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | /
   sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | /
   sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
   ```
2. Enable experimental features:

   ```
   sudo sed -i -e '/experimental/ s/^#//g' /etc/apt/sources.list.d/nvidia-container-toolkit.list
   ```
3. Update and install the toolkit:

   ```
   sudo apt-get update
   sudo apt-get install -y nvidia-container-toolkit
   sudo nvidia-ctk runtime configure --runtime=docker
   sudo systemctl restart docker
   ```

#### Verify Nvidia-container-toolkit:

1. Check if the toolkit is in the **\$PATH**:

   ```
   /usr/bin/nvidia-ctk --version
   echo $PATH
   ```
2. Verify the runtime is configured:

   ```
   docker info | grep -i runtime
   ```

   Sample output:

   <Frame>
       <img src="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/2db844b647732589a8c35320619060272498fdebdf2d0965fd7f8f1b68e85cc6-DockerIssue3.jpg?fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=abe3f20d44d6fb9db7acf3a8845f62be" alt="" data-og-width="1007" width="1007" data-og-height="365" height="365" data-path="images/docs/2db844b647732589a8c35320619060272498fdebdf2d0965fd7f8f1b68e85cc6-DockerIssue3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/2db844b647732589a8c35320619060272498fdebdf2d0965fd7f8f1b68e85cc6-DockerIssue3.jpg?w=280&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=b25be4082431ee32a90c791711af36b7 280w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/2db844b647732589a8c35320619060272498fdebdf2d0965fd7f8f1b68e85cc6-DockerIssue3.jpg?w=560&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=3cb4382cfb6413f7a6d1a67352bee2db 560w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/2db844b647732589a8c35320619060272498fdebdf2d0965fd7f8f1b68e85cc6-DockerIssue3.jpg?w=840&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=ebce70871831017b83313eb92560b2bc 840w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/2db844b647732589a8c35320619060272498fdebdf2d0965fd7f8f1b68e85cc6-DockerIssue3.jpg?w=1100&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=affcf891055bf1bd1a5becdde5f2a3ba 1100w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/2db844b647732589a8c35320619060272498fdebdf2d0965fd7f8f1b68e85cc6-DockerIssue3.jpg?w=1650&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=b95addcd2cf002396e71f55a24a44906 1650w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/2db844b647732589a8c35320619060272498fdebdf2d0965fd7f8f1b68e85cc6-DockerIssue3.jpg?w=2500&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=01949118c07735dd55432293c25e4741 2500w" />
   </Frame>

#### Final GPU Test:

Run the following command to test if Docker can use the GPU:

```
docker run --gpus all nvidia/cuda:11.0.3-base-ubuntu18.04 nvidia-smi
```
