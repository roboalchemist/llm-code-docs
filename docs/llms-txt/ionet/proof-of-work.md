# Source: https://io.net/docs/guides/workers/proof-of-work.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Proof of Work

> io.net is committed to providing a reliable and trustworthy platform for distributed CPU/GPU resources. A key challenge in a decentralized network is to ensure that the computational resources offered by suppliers are genuine and perform as intended. We actively verify the authenticity and reliability of the network by implementing an hourly Proof-of-Work (PoW) verification process.

### What is Proof-of-Work?

Proof-of-Work is a cryptographic puzzle that requires significant computational resources to solve. It’s easy to verify the authenticity of a GPU/CPU after they successfully solve the puzzle. Our PoW algorithm leverages an industry-standard approach to verify computational resources, similar to the approaches used in cryptocurrencies such as Ethereum, prior to its Proof-of-Stake upgrade, and Bitcoin.

### Why Is This Necessary?

1. **Authenticity Verification**: PoW verifies that suppliers provide real and functional CPU/GPU resources rather than simulated or virtual environments.
2. **Performance Validation**: By requiring devices to solve complex puzzles, we can verify that they perform at the level claimed by the supplier.
3. **Fraud Prevention**: This mechanism makes it difficult and economically unfeasible for malicious actors to fake or overstate their computational capacity.
4. **Quality Assurance**: Regular PoW checks help maintain the overall quality and reliability of the io.net network.
5. **Fair Resource Allocation**: By verifying the authenticity and performance of resources, we ensure fair pricing and allocation for users hiring computational power.

Our hourly PoW process runs in the background, causing minimal disruption to normal operations while continuously ensuring the integrity of our network. Suppliers can expect some load on their devices normally for no more than 15 mins per hour to complete the hourly Proof-of-Work authentication process.

<Info>
  When you onboard your device into the io.net network, the device’s full capacity should be available to potential customers. If your device's computational capacity is compromised when connected to our platform, it might disqualify you from rewards and being hired. Please note that we expect resources including VRAM to be fully available while your device is made available on io.net.
</Info>

### The PoW Process

There are three parts in this process:

* **Binary Checker API:** This is a tool that helps us solve the puzzle. It checks if a solution meets the puzzle's requirements.
* **Challenges API**: These are the puzzles themselves. It involves finding a number that fits a specific pattern, such as having a certain number of zeros at the beginning.
* **Results Submission API**: Once we find a solution, we submit it to the system to check if it's correct.

Here's how it works in simple steps:

1. The **Binary Checker** receives a puzzle and attempts to find a solution (called a nonce) that fits the puzzle's pattern.
2. The system verifies that the device has the reported amount of VRAM to prevent devices with similar hash rates from misrepresenting their capacity.
3. When a solution is found, it sends it to the system for verification.
4. The system verifies that the solution matches the puzzle's requirements. For example, containing a specific number of zeros at the beginning.
5. If the solution matches the requirements, the system records this as a successful solution. The device has passed PoW challenge.

We have a monitoring system that regularly checks for new puzzles, finds solutions, and submits them for verification.

### Is My Device Verified?

There are two visible aspects of Proof of Work (PoW) in our system:

1. Users can directly see on their device page whether their device is **Verified** or **Not Verified**:

   Verified devices are indicated by a blue icon located underneath the name of your device:

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8a91d5629ff97056ef80a9aa4c49a25f068ace0e8a44c4feee85b4f0bf3fc440-NotVerified.jpg?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=f2e1a33ec170bcf3d95bd79083d2473f" alt="" className="mx-auto" style={{ width:"60%" }} data-og-width="894" width="894" data-og-height="342" height="342" data-path="images/docs/8a91d5629ff97056ef80a9aa4c49a25f068ace0e8a44c4feee85b4f0bf3fc440-NotVerified.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8a91d5629ff97056ef80a9aa4c49a25f068ace0e8a44c4feee85b4f0bf3fc440-NotVerified.jpg?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=506d40f269565a86e93b93c814024b07 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8a91d5629ff97056ef80a9aa4c49a25f068ace0e8a44c4feee85b4f0bf3fc440-NotVerified.jpg?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=2cae9f2a2f828eadfbdd963f3762b606 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8a91d5629ff97056ef80a9aa4c49a25f068ace0e8a44c4feee85b4f0bf3fc440-NotVerified.jpg?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=578c739292d53689af5ea5e7ce9d2782 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8a91d5629ff97056ef80a9aa4c49a25f068ace0e8a44c4feee85b4f0bf3fc440-NotVerified.jpg?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=5ca5eaf56c6e5b8678b8a5de0f4cb284 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8a91d5629ff97056ef80a9aa4c49a25f068ace0e8a44c4feee85b4f0bf3fc440-NotVerified.jpg?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=f8c6fea7fcf4a0df58bec1d00fdfad97 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8a91d5629ff97056ef80a9aa4c49a25f068ace0e8a44c4feee85b4f0bf3fc440-NotVerified.jpg?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=ed575b941af9e68ac220298f13172311 2500w" />
   </Frame>

   Devices that are awaiting verification have a gray mark:

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/df74e13116c0c16daaa0390eafe3fb9ff84a4b9b9059548079b81bed315ecd51-NotVerifiedYet.jpg?fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=4c53bb14af97cf02a5aa059af7957600" alt="" className="mx-auto" style={{ width:"60%" }} data-og-width="896" width="896" data-og-height="362" height="362" data-path="images/docs/df74e13116c0c16daaa0390eafe3fb9ff84a4b9b9059548079b81bed315ecd51-NotVerifiedYet.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/df74e13116c0c16daaa0390eafe3fb9ff84a4b9b9059548079b81bed315ecd51-NotVerifiedYet.jpg?w=280&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=81c26d57c532104c4586abc7a9223632 280w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/df74e13116c0c16daaa0390eafe3fb9ff84a4b9b9059548079b81bed315ecd51-NotVerifiedYet.jpg?w=560&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=48c521698f9478cf5b371e6dcbd2e963 560w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/df74e13116c0c16daaa0390eafe3fb9ff84a4b9b9059548079b81bed315ecd51-NotVerifiedYet.jpg?w=840&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=8854f93818c0763049ea9d45b7475eca 840w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/df74e13116c0c16daaa0390eafe3fb9ff84a4b9b9059548079b81bed315ecd51-NotVerifiedYet.jpg?w=1100&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=a86f7ecaa14212df997de02170af732a 1100w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/df74e13116c0c16daaa0390eafe3fb9ff84a4b9b9059548079b81bed315ecd51-NotVerifiedYet.jpg?w=1650&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=b027b0f7355289b2e8d0e09f8dae890b 1650w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/df74e13116c0c16daaa0390eafe3fb9ff84a4b9b9059548079b81bed315ecd51-NotVerifiedYet.jpg?w=2500&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=a9de086cf8d79281f83c239a18889587 2500w" />
   </Frame>

   Verification Failed have a red label:

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/9361f3a9e96e697420f04a1c38092f1f6e854341ebae4cabcab6eb3f57646813-VerFailed.jpg?fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=2f432acb037b1c576bfd071a1e231b11" alt="" className="mx-auto" style={{ width:"62%" }} data-og-width="894" width="894" data-og-height="342" height="342" data-path="images/docs/9361f3a9e96e697420f04a1c38092f1f6e854341ebae4cabcab6eb3f57646813-VerFailed.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/9361f3a9e96e697420f04a1c38092f1f6e854341ebae4cabcab6eb3f57646813-VerFailed.jpg?w=280&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=30c1e5f1d941890975dc002535f3994c 280w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/9361f3a9e96e697420f04a1c38092f1f6e854341ebae4cabcab6eb3f57646813-VerFailed.jpg?w=560&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=680ec1ef800d3330df0bce9b40d30115 560w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/9361f3a9e96e697420f04a1c38092f1f6e854341ebae4cabcab6eb3f57646813-VerFailed.jpg?w=840&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=4a638a4acfc4427cf42f0e1c148c2159 840w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/9361f3a9e96e697420f04a1c38092f1f6e854341ebae4cabcab6eb3f57646813-VerFailed.jpg?w=1100&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=87da1f67b8f1e9363d082a5a6f19667a 1100w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/9361f3a9e96e697420f04a1c38092f1f6e854341ebae4cabcab6eb3f57646813-VerFailed.jpg?w=1650&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=33c7f3b7973b45daf4cef69adb45f76c 1650w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/9361f3a9e96e697420f04a1c38092f1f6e854341ebae4cabcab6eb3f57646813-VerFailed.jpg?w=2500&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=e0bb49003f67b2817129332f958b924e 2500w" />
   </Frame>

### What Happens if Proof-of-Work Fails?

If Proof-of-Work fails on your device, you may find your device tagged **Verification Failed** and/or **Not Block Reward Ready.**

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/577cac763d88f4e1e94fd036b27fcbed43468457d4d368bc3cc73f33b8b03b29-pow.jpg?fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=f60a8a5a001b64c4224f9bd70611fc14" alt="" className="mx-auto" style={{ width:"58%" }} data-og-width="1212" width="1212" data-og-height="128" height="128" data-path="images/docs/577cac763d88f4e1e94fd036b27fcbed43468457d4d368bc3cc73f33b8b03b29-pow.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/577cac763d88f4e1e94fd036b27fcbed43468457d4d368bc3cc73f33b8b03b29-pow.jpg?w=280&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=939a0d96aec5fb14d03bae0ee61dfcf8 280w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/577cac763d88f4e1e94fd036b27fcbed43468457d4d368bc3cc73f33b8b03b29-pow.jpg?w=560&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=9823c0f07c7409cce4d3255fbaf4e0db 560w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/577cac763d88f4e1e94fd036b27fcbed43468457d4d368bc3cc73f33b8b03b29-pow.jpg?w=840&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=c4084bf100587da5f47f2051e6cd7a75 840w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/577cac763d88f4e1e94fd036b27fcbed43468457d4d368bc3cc73f33b8b03b29-pow.jpg?w=1100&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=861c23257a70d28498febe4e9649d6fc 1100w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/577cac763d88f4e1e94fd036b27fcbed43468457d4d368bc3cc73f33b8b03b29-pow.jpg?w=1650&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=778dff237028b1fb2bb9a810167b2ab0 1650w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/577cac763d88f4e1e94fd036b27fcbed43468457d4d368bc3cc73f33b8b03b29-pow.jpg?w=2500&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=66cba297a17509c5ac1314a57d9b7cab 2500w" />
</Frame>

You can use our [`Proof-of-Work logs`](https://pow-logs.io.solutions/) to troubleshoot any potential issues by searching for your device ID to view any errors that occurred during the hourly Proof-of-Work challenges. Please download logs corresponding to where PoW failure took please and either use grep if you are familiar with command line tools (recommended) or use Microsoft Excel to search for your device ID.

**Common errors you might encounter in the PoW log include:**

* If you find an **empty list passed** error: This is often caused by a CUDA memory allocation error. Your device might be occupied by some other jobs, Please check and stop using the device for other purposes when it's available on the IO platform.
* If you find a **wrong answer** error: Your device failed the PoW test. You may want to delete all containers, download the latest launcher, and restart the onboarding process following our documentation.
* If you find a **timeout** error: Due to the inherent indeterminacy of PoW, there is a slight chance that your device might fail a PoW test even if it's correctly configured. Mostly likely, if you repeat the setup process, it will pass PoW.

**Common issue that can cause errors:**

* If you run your devices on deprecated drivers or CUDA versions (in case of Nvidia Graphics cards).
* If you have more than 3 GPUs in your setup, we recommend running your device on Linux because there are intermittent issues with multi-card setups on Windows platforms. PoW tests have a high probability of failing in this instance.

If you use Linux, you can run a self-check binary to troubleshoot your devices. A successful self-check does not guarantee that your device will pass PoW; however, your device is highly unlikely to pass PoW if self-check returns any errors. This binary also works on Windows WSL2: [https://github.com/ionet-official/io-net-official-setup-script/releases/](https://github.com/ionet-official/io-net-official-setup-script/releases/).

<Info>
  Encountering problems? Feel free to open a support ticket by logging into [your IO.Net account](https://worker.io.net) and submitting a ticket.
</Info>
