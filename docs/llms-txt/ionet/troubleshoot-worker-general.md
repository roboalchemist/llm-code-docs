# Source: https://io.net/docs/guides/workers/troubleshoot-worker-general.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# General Worker Troubleshooting

> Here we've compiled essential use cases for working with Workers.

### How to Resolve Unsupported GPU Issues on Windows and Linux?

If a user's supported GPU is listed as unsupported on the website, they should verify their NVIDIA driver configuration. Often, when a Docker container running **nvidia-smi** fails, the backend receives this information and marks the GPU as unsupported.

To check the configuration, running the following command should provide the correct output:

```
docker run --gpus all nvidia/cuda:11.0.3-base-ubuntu18.04 nvidia-smi
```

### If I received a "device code authorization returned: Bad Request" error?

If this error is displayed following authorization:

```
Error: device code authorization returned: Bad Request
Error: Error authenticating: provided token has expired or invalid. Please re-authenticate using --no_cache=true flag.
```

This error might be caused by an issue with network connections. Visit [https://auth0.io.solutions/activate](https://auth0.io.solutions/activate). If the page does not open, it means **Auth0** is not reachable for you.

### How can I pause or reset a Worker if it has disconnection issues?

If your worker has been disconnected, here are a few steps to fix it:

1. Go to your running **Worker Page** and click on **Pause** for the Worker (located at the top-right corner).
2. **Optionally**, restart the device as needed.
3. After restarting the device, open your Worker page at IO.NET and copy the command from the **Re-Run docker command** block on the **Worker Page**, then run it Terminal.

   <Frame>
       <img src="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ff7c04f1f64b551ddf444b14341226b95028248aff8c51be17d631416a43a780-Step7.jpg?fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=99d4cf86513d098c4de77830c808fd5a" alt="" data-og-width="1804" width="1804" data-og-height="1128" height="1128" data-path="images/docs/ff7c04f1f64b551ddf444b14341226b95028248aff8c51be17d631416a43a780-Step7.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ff7c04f1f64b551ddf444b14341226b95028248aff8c51be17d631416a43a780-Step7.jpg?w=280&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=28cf15d6898f4943245643a18aa7e924 280w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ff7c04f1f64b551ddf444b14341226b95028248aff8c51be17d631416a43a780-Step7.jpg?w=560&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=12bf5a1f2a56e9105dd9083745cf57ff 560w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ff7c04f1f64b551ddf444b14341226b95028248aff8c51be17d631416a43a780-Step7.jpg?w=840&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=6a783f87106789b03647143faf14ae19 840w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ff7c04f1f64b551ddf444b14341226b95028248aff8c51be17d631416a43a780-Step7.jpg?w=1100&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=f75a750aa312578d4eca4d9455e6b4b5 1100w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ff7c04f1f64b551ddf444b14341226b95028248aff8c51be17d631416a43a780-Step7.jpg?w=1650&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=7d769670f6eea4ecf97373956e79c78c 1650w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/ff7c04f1f64b551ddf444b14341226b95028248aff8c51be17d631416a43a780-Step7.jpg?w=2500&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=cec2aaa5bc8d51d316ef16c5af8c9748 2500w" />
   </Frame>
4. If prompted, authorize the device using IO.ID. Remember, you have about 3 minutes to complete the authorization.

   <Frame>
       <img src="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/fd8c5f6c7ef7d789001be768989553ea9def8dc23f0a7bda8ecb623880263961-Step10.jpg?fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=e6ec16d059f1ce9cd7647d162fb67b69" alt="" data-og-width="1572" width="1572" data-og-height="507" height="507" data-path="images/docs/fd8c5f6c7ef7d789001be768989553ea9def8dc23f0a7bda8ecb623880263961-Step10.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/fd8c5f6c7ef7d789001be768989553ea9def8dc23f0a7bda8ecb623880263961-Step10.jpg?w=280&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=663203260252950c526c8ba23b3628d1 280w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/fd8c5f6c7ef7d789001be768989553ea9def8dc23f0a7bda8ecb623880263961-Step10.jpg?w=560&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=1e133897a857861207a58ed7449d84e4 560w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/fd8c5f6c7ef7d789001be768989553ea9def8dc23f0a7bda8ecb623880263961-Step10.jpg?w=840&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=85cfe11c990578978e7450c30aff7126 840w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/fd8c5f6c7ef7d789001be768989553ea9def8dc23f0a7bda8ecb623880263961-Step10.jpg?w=1100&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=bb1b5a8f246cb26254535dbd1d82280b 1100w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/fd8c5f6c7ef7d789001be768989553ea9def8dc23f0a7bda8ecb623880263961-Step10.jpg?w=1650&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=1b2139b2ed22856ec6dcdfb437715773 1650w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/fd8c5f6c7ef7d789001be768989553ea9def8dc23f0a7bda8ecb623880263961-Step10.jpg?w=2500&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=fc55ecb78ad7afa0082d8b5edf7d3e9a 2500w" />
   </Frame>
5. Confirm the removal of all previous containers in Docker.

   <Frame>
       <img src="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e8c4d67b711a2e53a3794f2cd4f9e57f8272770ea94874476d3f7abad4cb2e20-Step15.jpg?fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=76576768f83609812e9377cac22fa9af" alt="" data-og-width="1457" width="1457" data-og-height="450" height="450" data-path="images/docs/e8c4d67b711a2e53a3794f2cd4f9e57f8272770ea94874476d3f7abad4cb2e20-Step15.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e8c4d67b711a2e53a3794f2cd4f9e57f8272770ea94874476d3f7abad4cb2e20-Step15.jpg?w=280&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=d155bb6d6f5f16450528d7191d7ef125 280w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e8c4d67b711a2e53a3794f2cd4f9e57f8272770ea94874476d3f7abad4cb2e20-Step15.jpg?w=560&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=5f82bfbe0503161e72faa71271bc9f2d 560w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e8c4d67b711a2e53a3794f2cd4f9e57f8272770ea94874476d3f7abad4cb2e20-Step15.jpg?w=840&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=109bc6cc4a0204044f9c7d8f6fe2fd2e 840w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e8c4d67b711a2e53a3794f2cd4f9e57f8272770ea94874476d3f7abad4cb2e20-Step15.jpg?w=1100&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=1a578d6f48c7439b9d2ac3aaf231e560 1100w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e8c4d67b711a2e53a3794f2cd4f9e57f8272770ea94874476d3f7abad4cb2e20-Step15.jpg?w=1650&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=08b12e28181df134d920458280ac814b 1650w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e8c4d67b711a2e53a3794f2cd4f9e57f8272770ea94874476d3f7abad4cb2e20-Step15.jpg?w=2500&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=38b0f3e13b23be4f3eb884175178af7a 2500w" />
   </Frame>
6. Wait for up to 10 minutes to see the progress. Your worker is now ready to use again.

<Frame>
  <img src="https://files.readme.io/bf1efb1-7059edf-Step13.gif" alt="" className="mx-auto" style={{ width:"70%" }} />
</Frame>

### How can suppliers change their accounts in IO Worker?

To change accounts, suppliers should include the **--no\_cache=true** flag in the binary run command. This triggers a re-authentication process. Simply add **--no\_cache=true** at the end of your main request when connecting the device with the new login.

<CodeGroup>
  ```Text MacOs theme={null}
  ./launch_binary_mac --disable_sleep_mode=true --no_cache=true
  ```

  ```Text Windows theme={null}
  ./io_net_launch_binary_windows.exe --disable_sleep_mode=true --no_cache=true
  ```

  ```Text Linux theme={null}
  ./io_net_launch_binary_linux --disable_sleep_mode=true --no_cache=true
  ```
</CodeGroup>

<Info>
  After one successful sign-in, the token will be saved in memory.
</Info>

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3a4a99e26e742b0cad7b8c39a1ee97d8ca656a6ea95348f2e15d616c1c01f75c-UseCases-Cache.jpg?fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=97f552e12f60ad32ababaef7ab3487fd" alt="" data-og-width="1886" width="1886" data-og-height="462" height="462" data-path="images/docs/3a4a99e26e742b0cad7b8c39a1ee97d8ca656a6ea95348f2e15d616c1c01f75c-UseCases-Cache.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3a4a99e26e742b0cad7b8c39a1ee97d8ca656a6ea95348f2e15d616c1c01f75c-UseCases-Cache.jpg?w=280&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=71fde36f431dc096ec73ac051aee6477 280w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3a4a99e26e742b0cad7b8c39a1ee97d8ca656a6ea95348f2e15d616c1c01f75c-UseCases-Cache.jpg?w=560&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=036f57930f795457dcf1f561d7926592 560w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3a4a99e26e742b0cad7b8c39a1ee97d8ca656a6ea95348f2e15d616c1c01f75c-UseCases-Cache.jpg?w=840&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=c37df247bf17dcf4f7c44f9cf2cca4e2 840w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3a4a99e26e742b0cad7b8c39a1ee97d8ca656a6ea95348f2e15d616c1c01f75c-UseCases-Cache.jpg?w=1100&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=f4fe26f4db79be000391ff6fd9c08396 1100w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3a4a99e26e742b0cad7b8c39a1ee97d8ca656a6ea95348f2e15d616c1c01f75c-UseCases-Cache.jpg?w=1650&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=4a09fce637e8693c522278f5c10b6c6f 1650w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3a4a99e26e742b0cad7b8c39a1ee97d8ca656a6ea95348f2e15d616c1c01f75c-UseCases-Cache.jpg?w=2500&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=e03ba0e78e5bcbd8533578010599224a 2500w" />
</Frame>

### How can you run an existing worker UUID in the new authentication and authorization system?

As of May 2024, we have transitioned to a new authentication and authorization system. Follow these steps to run your existing worker UUID again.

#### 1. Run the Command to Connect the Device

Open the Terminal on your system by navigating to the Start menu and using the search function. The process is similar regardless of your operating system.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/32cea48-Terminals.jpg?fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=e0ec0504fc250fc6b0ef70b46efbb08f" alt="" data-og-width="1725" width="1725" data-og-height="499" height="499" data-path="images/docs/32cea48-Terminals.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/32cea48-Terminals.jpg?w=280&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=6a16677daccb9f47e0b1f6286766f8e6 280w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/32cea48-Terminals.jpg?w=560&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=2abf84ffa0bb208f69c837517e863673 560w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/32cea48-Terminals.jpg?w=840&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=2989da9817d3b9fbc1174db338d95bce 840w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/32cea48-Terminals.jpg?w=1100&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=1a806261114e3d87e750e809fbda9991 1100w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/32cea48-Terminals.jpg?w=1650&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=2ea82e6a4a36c10d6d56a8dd077bfbd3 1650w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/32cea48-Terminals.jpg?w=2500&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=feb0da3aa56459d085b4a6b01eb110bf 2500w" />
</Frame>

Then run the command in the Terminal. For Windows, start by downloading and running the executable file.

* Download the binary for your operating system running command. [**For Windows you need to download the executable file. You can see how it's done here**](/docs/install-on-windows#7-download-and-launch-io-binary)

  <CodeGroup>
    ```Text MacOS theme={null}
    curl -L https://github.com/ionet-official/io_launch_binaries/blob/main/io_net_launch_binary_mac -o io_net_launch_binary_mac
    ```

    ```Text Windows theme={null}
    https://github.com/ionet-official/io_launch_binaries/raw/main/io_net_launch_binary_windows.exe
    ```

    ```Text Linux theme={null}
    curl -L https://github.com/ionet-official/io_launch_binaries/blob/main/io_net_launch_binary_linux -o io_net_launch_binary_linux
    ```
  </CodeGroup>
* Use the following command to grant permissions to the new binary:

  <CodeGroup>
    ```Text MacOS theme={null}
    chmod +x io_net_launch_binary_mac
    ```

    ```Text Linux theme={null}
    chmod +x io_net_launch_binary_linux
    ```
  </CodeGroup>
* Launch the binary to connect your device to the platform.

  <CodeGroup>
    ```Text MacOS theme={null}
    ./io_net_launch_binary_mac --no_warnings=true 
    ```

    ```Text Windows theme={null}
    ./io_net_launch_binary_windows.exe --no_warnings=true 
    ```

    ```Text Linux theme={null}
    ./io_net_launch_binary_linux --no_warnings=true 
    ```
  </CodeGroup>

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8c7bc7b1f256f70475aacb34d2a06e2c8390b925e53f5b0b9036b338aa4d02ba-UseCases-newAuth.jpg?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=64bfbd5765b33fc8ec7e911178a0d969" alt="" data-og-width="1938" width="1938" data-og-height="764" height="764" data-path="images/docs/8c7bc7b1f256f70475aacb34d2a06e2c8390b925e53f5b0b9036b338aa4d02ba-UseCases-newAuth.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8c7bc7b1f256f70475aacb34d2a06e2c8390b925e53f5b0b9036b338aa4d02ba-UseCases-newAuth.jpg?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=958325dff718776b312f4d770de8067e 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8c7bc7b1f256f70475aacb34d2a06e2c8390b925e53f5b0b9036b338aa4d02ba-UseCases-newAuth.jpg?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=3a8a3fc206ad95492cf199c3ef910af2 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8c7bc7b1f256f70475aacb34d2a06e2c8390b925e53f5b0b9036b338aa4d02ba-UseCases-newAuth.jpg?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=d73fc011ddf84821941bb500fc7dcd0d 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8c7bc7b1f256f70475aacb34d2a06e2c8390b925e53f5b0b9036b338aa4d02ba-UseCases-newAuth.jpg?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=e79b58bf5f7160d6b980ab66dcc47830 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8c7bc7b1f256f70475aacb34d2a06e2c8390b925e53f5b0b9036b338aa4d02ba-UseCases-newAuth.jpg?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=4ccbb255c681b6a367bb53ee7aad148a 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8c7bc7b1f256f70475aacb34d2a06e2c8390b925e53f5b0b9036b338aa4d02ba-UseCases-newAuth.jpg?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=06d7001e630a805ee0a26c6e93447e79 2500w" />
</Frame>

#### 2: To authorize the device with [IO.ID](http://io.id/), follow one of the options below and verify your IO.ID account:

<Info>
  Remember, you will have about 1-2 minutes to complete the authorization of the device. If it expires, run the code again.
</Info>

You can do this in two ways: **Copy the Link from the Terminal**: Paste it into your browser and confirm the action.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/cb4a646957a70bc8052134b17266be88d9c50c598236ace4c048064ee041d65b-UseCases-newAuth2.jpg?fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=1ed62eb06a116bd43e042d1074375861" alt="" data-og-width="2096" width="2096" data-og-height="648" height="648" data-path="images/docs/cb4a646957a70bc8052134b17266be88d9c50c598236ace4c048064ee041d65b-UseCases-newAuth2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/cb4a646957a70bc8052134b17266be88d9c50c598236ace4c048064ee041d65b-UseCases-newAuth2.jpg?w=280&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=3fcd401f67a5596c815e0f04ec09ab14 280w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/cb4a646957a70bc8052134b17266be88d9c50c598236ace4c048064ee041d65b-UseCases-newAuth2.jpg?w=560&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=8300b68cafc5a1a591f99f181f7d7ec0 560w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/cb4a646957a70bc8052134b17266be88d9c50c598236ace4c048064ee041d65b-UseCases-newAuth2.jpg?w=840&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=e2ba572374f8923e3ff365b5d1c2fb2a 840w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/cb4a646957a70bc8052134b17266be88d9c50c598236ace4c048064ee041d65b-UseCases-newAuth2.jpg?w=1100&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=8f12875479b983b5afd9fecf97d655c2 1100w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/cb4a646957a70bc8052134b17266be88d9c50c598236ace4c048064ee041d65b-UseCases-newAuth2.jpg?w=1650&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=3c4f0410e5449b606b76bfbee14b9ab4 1650w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/cb4a646957a70bc8052134b17266be88d9c50c598236ace4c048064ee041d65b-UseCases-newAuth2.jpg?w=2500&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=507e0cf2a1c326796946e3b33b211995 2500w" />
</Frame>

After confirmation, the system will prompt you to log in.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1dc87cadac09127914c77424b44967156d54c228484310b59c9ab65f58529efe-Step11.jpg?fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=3ce3cb374df332e3239b7fb621c94de2" alt="" data-og-width="1077" width="1077" data-og-height="564" height="564" data-path="images/docs/1dc87cadac09127914c77424b44967156d54c228484310b59c9ab65f58529efe-Step11.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1dc87cadac09127914c77424b44967156d54c228484310b59c9ab65f58529efe-Step11.jpg?w=280&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=1be27a06acfb2de8b93d0362b6fbd9aa 280w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1dc87cadac09127914c77424b44967156d54c228484310b59c9ab65f58529efe-Step11.jpg?w=560&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=a179b7d8c9152aeef2de7aae72cd9de7 560w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1dc87cadac09127914c77424b44967156d54c228484310b59c9ab65f58529efe-Step11.jpg?w=840&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=e77eddc35bb991868f8bd5ada46a6a9b 840w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1dc87cadac09127914c77424b44967156d54c228484310b59c9ab65f58529efe-Step11.jpg?w=1100&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=e82ba7be606d70e5f41eb6b3216f4727 1100w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1dc87cadac09127914c77424b44967156d54c228484310b59c9ab65f58529efe-Step11.jpg?w=1650&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=0085a1b10c015841e6eb8d904bc9c99a 1650w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1dc87cadac09127914c77424b44967156d54c228484310b59c9ab65f58529efe-Step11.jpg?w=2500&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=f5829be862eeb7f934999bd26430f452 2500w" />
</Frame>

#### 3. Save the Token

The information below is found in the CLI. Keep this token accessible.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c3071c08f65eeb18651b364d95ddfe6a252f258eda6dcb875fd45a3a7a2fbc1a-UseCases-newAuth6.jpg?fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=3a1b0ef9a5dba0aadaf21131e26815ef" alt="" data-og-width="1858" width="1858" data-og-height="474" height="474" data-path="images/docs/c3071c08f65eeb18651b364d95ddfe6a252f258eda6dcb875fd45a3a7a2fbc1a-UseCases-newAuth6.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c3071c08f65eeb18651b364d95ddfe6a252f258eda6dcb875fd45a3a7a2fbc1a-UseCases-newAuth6.jpg?w=280&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=ad16f3b489ff9ffd44b3f15af117155d 280w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c3071c08f65eeb18651b364d95ddfe6a252f258eda6dcb875fd45a3a7a2fbc1a-UseCases-newAuth6.jpg?w=560&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=33ba8bc0d2eb6e8d3d8101e247e42d61 560w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c3071c08f65eeb18651b364d95ddfe6a252f258eda6dcb875fd45a3a7a2fbc1a-UseCases-newAuth6.jpg?w=840&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=d2c63226d883981060e85b62442a90f1 840w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c3071c08f65eeb18651b364d95ddfe6a252f258eda6dcb875fd45a3a7a2fbc1a-UseCases-newAuth6.jpg?w=1100&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=11c795811c2452dd3d38fc8aab36b371 1100w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c3071c08f65eeb18651b364d95ddfe6a252f258eda6dcb875fd45a3a7a2fbc1a-UseCases-newAuth6.jpg?w=1650&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=82be705f7cf031b5ca072537e4b17e24 1650w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c3071c08f65eeb18651b364d95ddfe6a252f258eda6dcb875fd45a3a7a2fbc1a-UseCases-newAuth6.jpg?w=2500&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=11216060f86b9b0008efbb5803a864e6 2500w" />
</Frame>

#### 4. For all other machines use the saved token

This does not require manual reauthentication and can be used for all your worker nodes.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3d2d51340f9c44bcc3a3f16d2a9d946212ddd8e018ebf96cfa2a6616da829c2f-UseCases-newAuth7.jpg?fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=5f334a0622eff694fb0152a42aa6b341" alt="" data-og-width="1182" width="1182" data-og-height="392" height="392" data-path="images/docs/3d2d51340f9c44bcc3a3f16d2a9d946212ddd8e018ebf96cfa2a6616da829c2f-UseCases-newAuth7.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3d2d51340f9c44bcc3a3f16d2a9d946212ddd8e018ebf96cfa2a6616da829c2f-UseCases-newAuth7.jpg?w=280&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=22ba52280365146afe4816bdc88e0ca2 280w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3d2d51340f9c44bcc3a3f16d2a9d946212ddd8e018ebf96cfa2a6616da829c2f-UseCases-newAuth7.jpg?w=560&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=6fb503b21d5afab2f38f77f2ac0303f1 560w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3d2d51340f9c44bcc3a3f16d2a9d946212ddd8e018ebf96cfa2a6616da829c2f-UseCases-newAuth7.jpg?w=840&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=1d81f75749c0df071339698a38ba5868 840w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3d2d51340f9c44bcc3a3f16d2a9d946212ddd8e018ebf96cfa2a6616da829c2f-UseCases-newAuth7.jpg?w=1100&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=ede281124a79d62fb5807b661f5f8f34 1100w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3d2d51340f9c44bcc3a3f16d2a9d946212ddd8e018ebf96cfa2a6616da829c2f-UseCases-newAuth7.jpg?w=1650&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=2487a15b3127eef246ee4faf2b6aacdf 1650w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3d2d51340f9c44bcc3a3f16d2a9d946212ddd8e018ebf96cfa2a6616da829c2f-UseCases-newAuth7.jpg?w=2500&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=8bd78b499787e529313d905c39acdf24 2500w" />
</Frame>

### Why Do Containers Disappear from Docker?

If the container disappears from docker, then your worker was likely blocked. If this happens, you must recreate the worker from scratch.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/aad7bbb2ab5db47b9c86f9069faca3651e44a06b41e4ceca5eb939e799323987-UseCases-NoContainers.jpg?fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=7be7c626d8dc4672dcf2127cc8425a6c" alt="" data-og-width="2072" width="2072" data-og-height="1198" height="1198" data-path="images/docs/aad7bbb2ab5db47b9c86f9069faca3651e44a06b41e4ceca5eb939e799323987-UseCases-NoContainers.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/aad7bbb2ab5db47b9c86f9069faca3651e44a06b41e4ceca5eb939e799323987-UseCases-NoContainers.jpg?w=280&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=f377a79070b7aa138fd569c2e16893ee 280w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/aad7bbb2ab5db47b9c86f9069faca3651e44a06b41e4ceca5eb939e799323987-UseCases-NoContainers.jpg?w=560&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=49ec58176ad22a83774cc8110c4f5bf7 560w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/aad7bbb2ab5db47b9c86f9069faca3651e44a06b41e4ceca5eb939e799323987-UseCases-NoContainers.jpg?w=840&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=c08ae375b547db0a230127df5e62f731 840w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/aad7bbb2ab5db47b9c86f9069faca3651e44a06b41e4ceca5eb939e799323987-UseCases-NoContainers.jpg?w=1100&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=5af08a481ef24ce5c6dc871a608e5e49 1100w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/aad7bbb2ab5db47b9c86f9069faca3651e44a06b41e4ceca5eb939e799323987-UseCases-NoContainers.jpg?w=1650&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=b9ba4e4a4bf4056ef2a5b818eaa787d9 1650w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/aad7bbb2ab5db47b9c86f9069faca3651e44a06b41e4ceca5eb939e799323987-UseCases-NoContainers.jpg?w=2500&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=4b999a9c87ae680320980bacf848eba8 2500w" />
</Frame>

### Why Is My Worker Blocked?

Blocked status is indicative that our system detected GPU utilization that was not authorized by our internal checks. It's important that GPU availability is dedicated 100% to the task being volunteered for the health of the <Tooltip tip="DePIN - Decentralized Physical InfrastructureNetworks, leverages blockchains, loT and the greaterWeb3 ecosystem to create, operate and maintainreal-world physical infrastructure. These networksleverage token incentives to coordinate, reward andsafeguard members of the network.">DePIN</Tooltip>.

Blocked status can occur for a few different reasons, primarily:

* **Excessive GPU Utilization:** Activities such as playing games or using graphics-intensive applications. (You'll need to pause these activities before you start usage.)
* **Mining Detection:** Our team has implemented an update to detect mining devices and instances with high GPU usage, resulting in an automatic ban.
* **Device and Hardware Switching:** Our team has implemented a mechanism for blocking device if they were verified and later a different device with a different hardware was detected. If you need to use a new hardware, please create a new device

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/2269274e8cea81ca4101419210eee0f613c1777326a4a35063d60755b72b1cdc-UseCases-BlockContainer.jpg?fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=9166ba5fe7201ffa4494af8fb9024b1f" alt="" className="mx-auto" style={{ width:"67%" }} data-og-width="1372" width="1372" data-og-height="526" height="526" data-path="images/docs/2269274e8cea81ca4101419210eee0f613c1777326a4a35063d60755b72b1cdc-UseCases-BlockContainer.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/2269274e8cea81ca4101419210eee0f613c1777326a4a35063d60755b72b1cdc-UseCases-BlockContainer.jpg?w=280&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=f716f9f22fa14b8e87208792251f6a4d 280w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/2269274e8cea81ca4101419210eee0f613c1777326a4a35063d60755b72b1cdc-UseCases-BlockContainer.jpg?w=560&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=ff899e25d2f0f1b788ce8cfd1d6797b8 560w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/2269274e8cea81ca4101419210eee0f613c1777326a4a35063d60755b72b1cdc-UseCases-BlockContainer.jpg?w=840&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=7c7709d886c285f94a8850857c628823 840w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/2269274e8cea81ca4101419210eee0f613c1777326a4a35063d60755b72b1cdc-UseCases-BlockContainer.jpg?w=1100&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=ccc6e8104ea7757860b2d68a4513a591 1100w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/2269274e8cea81ca4101419210eee0f613c1777326a4a35063d60755b72b1cdc-UseCases-BlockContainer.jpg?w=1650&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=32d3f78e128fc1b212d155e621e7b9e4 1650w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/2269274e8cea81ca4101419210eee0f613c1777326a4a35063d60755b72b1cdc-UseCases-BlockContainer.jpg?w=2500&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=55596a7cbe781e9cecada9aa0c06656b 2500w" />
</Frame>

### Why Does My Worker Have an Unsupported Status?

This occurs when your GPU/CPU is not listed among the supported devices on the IO Network. You can check the list of supported devices [here](/docs/supported-devices).

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4ab41e322d21b132680db4c30a3fbdae0a9b8941e504c343cec4b4c7e3fb2284-UseCases-BlockContainer2.jpg?fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=dbd8b3a23937e5e0984fcdf78930ecce" alt="" className="mx-auto" style={{ width:"46%" }} data-og-width="1137" width="1137" data-og-height="594" height="594" data-path="images/docs/4ab41e322d21b132680db4c30a3fbdae0a9b8941e504c343cec4b4c7e3fb2284-UseCases-BlockContainer2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4ab41e322d21b132680db4c30a3fbdae0a9b8941e504c343cec4b4c7e3fb2284-UseCases-BlockContainer2.jpg?w=280&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=f5ff6f2fc1e3412cc7e14be586b8b1e4 280w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4ab41e322d21b132680db4c30a3fbdae0a9b8941e504c343cec4b4c7e3fb2284-UseCases-BlockContainer2.jpg?w=560&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=6201e987e5de578a2c61365be73b60ca 560w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4ab41e322d21b132680db4c30a3fbdae0a9b8941e504c343cec4b4c7e3fb2284-UseCases-BlockContainer2.jpg?w=840&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=d43bf7b9a7e5e9055dd45d06e03d212b 840w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4ab41e322d21b132680db4c30a3fbdae0a9b8941e504c343cec4b4c7e3fb2284-UseCases-BlockContainer2.jpg?w=1100&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=e3707c30293d130903c755ddcd867400 1100w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4ab41e322d21b132680db4c30a3fbdae0a9b8941e504c343cec4b4c7e3fb2284-UseCases-BlockContainer2.jpg?w=1650&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=3adc83cb96661401fe764bc9eb234d89 1650w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/4ab41e322d21b132680db4c30a3fbdae0a9b8941e504c343cec4b4c7e3fb2284-UseCases-BlockContainer2.jpg?w=2500&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=9c0232aceb39301f8ad4e131b17e4a66 2500w" />
</Frame>

### Why Does My Worker Disappear from My Dashboard?

This issue can stem from a few main causes:

1. **Unsuccessful Connection**: You didn't successfully connect the new worker. Here's an example of a successful worker connection:

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6df4ffd-ConnecterWorkers.jpg?fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=4a05ee928d9fa9d4731ba1f29a451494" alt="" className="mx-auto" style={{ width:"77%" }} data-og-width="893" width="893" data-og-height="480" height="480" data-path="images/docs/6df4ffd-ConnecterWorkers.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6df4ffd-ConnecterWorkers.jpg?w=280&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=399ccb25aa2e350ddc7a0a3ac0a349f7 280w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6df4ffd-ConnecterWorkers.jpg?w=560&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=7e069f66e829feb226a5ebf4841e323c 560w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6df4ffd-ConnecterWorkers.jpg?w=840&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=3f53068aa72b07114e37086d7efc6a2c 840w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6df4ffd-ConnecterWorkers.jpg?w=1100&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=9b08245c0f60f883bb8dca614556c765 1100w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6df4ffd-ConnecterWorkers.jpg?w=1650&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=90c45af7279cff6c878c14385ec68458 1650w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6df4ffd-ConnecterWorkers.jpg?w=2500&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=38bd9f023f898ba3d5725111267c1c13 2500w" />
   </Frame>
2. **Unsupported Hardware**: If you successfully connected a new worker but the GPU/CPU you're using is not supported, you won't see your worker on the dashboard. You can check the list of supported devices [here](/docs/supported-devices).
3. **User Interface Issues**: If your worker was running normally and suddenly disappears from the dashboard, it could be due to a problem with the user interface (UI). In such cases, try refreshing the website. If the worker still doesn't appear, please try again later or [create a ticket](https://worker.io.net) for our support team to assist you.

### Creating Multiple Workers from the Same Device

Users may inadvertently create a new worker each time the previous one fails instead of re-running the existing worker. To address this issue, you need to **Terminate the old workers** and learn how to restart Docker to continue running the existing worker. Follow the instructions [here](/docs/troubleshoot-worker-general#how-can-i-pause-or-reset-a-worker-if-it-has-disconnection-issues).

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f0285dc36344fd292399c6d954b478c6c8e65ea904c34c00db0e994983fd5097-UseCases-BlockContainer3.jpg?fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=a7319c1b34e7382a8c67eee4b32065b1" alt="" className="mx-auto" style={{ width:"78%" }} data-og-width="1696" width="1696" data-og-height="594" height="594" data-path="images/docs/f0285dc36344fd292399c6d954b478c6c8e65ea904c34c00db0e994983fd5097-UseCases-BlockContainer3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f0285dc36344fd292399c6d954b478c6c8e65ea904c34c00db0e994983fd5097-UseCases-BlockContainer3.jpg?w=280&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=dcf38492ff493f7b6fb561daf96187bf 280w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f0285dc36344fd292399c6d954b478c6c8e65ea904c34c00db0e994983fd5097-UseCases-BlockContainer3.jpg?w=560&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=07ba54e445f46b0076faa8f86b999f0e 560w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f0285dc36344fd292399c6d954b478c6c8e65ea904c34c00db0e994983fd5097-UseCases-BlockContainer3.jpg?w=840&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=528814a790fec14b1949e82a76cd3336 840w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f0285dc36344fd292399c6d954b478c6c8e65ea904c34c00db0e994983fd5097-UseCases-BlockContainer3.jpg?w=1100&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=a46e9a048a00bfff6dbeabedaed3c3fb 1100w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f0285dc36344fd292399c6d954b478c6c8e65ea904c34c00db0e994983fd5097-UseCases-BlockContainer3.jpg?w=1650&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=3050223c8be85839061a103e75a4ee3e 1650w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f0285dc36344fd292399c6d954b478c6c8e65ea904c34c00db0e994983fd5097-UseCases-BlockContainer3.jpg?w=2500&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=5f0398fcc82ed045e3a17f5ee931998b 2500w" />
</Frame>

### Device Readiness Status

Your device status needs to be either **Cluster Ready** or **Hired** to be nominated for Block Rewards and be eligible for hiring. You can verify device status either on the device detail page or on the **Workers** tab in **IO Explore**. For more information, see the [Get Started - IO Worker](/docs/intro) doc.

The four possible **Readiness** statuses are:

| Status                     | Description                                                                                                                                                                                                                                                                                                                                        |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Cluster Ready**          | Device meets PoW requirements and passed several Cluster Formation verifications.                                                                                                                                                                                                                                                                  |
| **Hired**                  | Device is currently hired by a cluster.                                                                                                                                                                                                                                                                                                            |
| **Pending**                | The device has joined the network and is currently undergoing both the PoW and Cluster Readiness test. This process can take up to 12 hours of cumulative uptime after onboarding, but may complete sooner if your device passes our tests early. If your device remains in a Pending state after more than 12 hours of uptime, please contact us. |
| **Not Block Reward Ready** | Device doesn't meet the criteria for block reward eligibility, mainly Cluster Formation verifications.                                                                                                                                                                                                                                             |

**Not Block Reward Ready** offers one of three tooltips in the UI to provide troubleshooting tips.

* **Please check your device's computational capacity**- Your device's computational capacity is below the required threshold.
* **Please check your device setup and computational capacity**- Your device setup might not be configured correctly and its computational capacity is below the required threshold. Please refer to the worker setup guide.
* **Please check your device setup**- Your device setup might not be configured correctly. Please refer to the worker setup guide.

<Info>
  Feel free to [check our knowledge](https://support.io.net/en/support/home) base for answers, and if you still need help, don’t hesitate to open a support ticket!
</Info>
