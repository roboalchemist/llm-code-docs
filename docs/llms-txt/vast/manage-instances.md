# Source: https://docs.vast.ai/documentation/instances/manage-instances.md

> ## Documentation Index
>>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Instances

> Learn how to manage running instances - start, stop, destroy, monitor status, and handle common operational tasks.

<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{
__html: JSON.stringify({
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": "Managing Vast.ai Instances",
  "description": "Complete guide to managing Vast.ai instances including starting, stopping, destroying, monitoring status, handling restarts, data management, connection methods, and troubleshooting instance states.",
  "author": {
    "@type": "Organization",
    "name": "Vast.ai"
  },
  "articleSection": "Instances Documentation",
  "keywords": ["instance management", "start", "stop", "destroy", "status monitoring", "troubleshooting", "vast.ai", "GPU instances"]
})
}}
/>

## Overview

The Instances page ([cloud.vast.ai/instances](https://cloud.vast.ai/instances)) is your central hub for managing rented instances. From here you can:

* View instance status and information
* Start, stop, and destroy instances
* Access connection details
* Monitor resource usage
* Transfer data between instances

## Instance Card Interface

<Frame caption="Instances Page">
    <img src="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide.webp?fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=122ccf4a5cabb0e8c40b476898bbee3e" alt="" data-og-width="865" width="865" data-og-height="421" height="421" data-path="images/console-instance-guide.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide.webp?w=280&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=3eabdbd625b2f04739dee5ec06efea88 280w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide.webp?w=560&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=c5be44c51078121e5eb2486807bea5f2 560w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide.webp?w=840&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=1a06be03d630d2d6fee6c7ecc4339b51 840w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide.webp?w=1100&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=29e5af14ff46bca642ac5cedb63103fc 1100w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide.webp?w=1650&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=0034aaa6fcd8ec220c7fdd3724868650 1650w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide.webp?w=2500&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=7a90acb5ca7b31b0e8c7ee6ca94da224 2500w" />
</Frame>

Each instance card displays comprehensive information about your rental:

### Main Status Button

<Frame caption="Open button">
    <img src="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-2.webp?fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=38a8c99429148ea4b347397c8b923e9b" alt="" data-og-width="800" width="800" data-og-height="202" height="202" data-path="images/console-instance-guide-2.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-2.webp?w=280&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=9568c18c7f8f6ec2970aefe3b72d6637 280w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-2.webp?w=560&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=69392e3c5b1ab7da7bb5423849e24ef0 560w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-2.webp?w=840&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=8bbffb4bfdbfae94e4a26b1fa8c4a45c 840w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-2.webp?w=1100&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=e3b5aa443a1c67fb7fc2d4038cce1f3a 1100w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-2.webp?w=1650&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=003b9d8d3cc32beaeed9cdc16e167c01 1650w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-2.webp?w=2500&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=e87ad65a858e16907b0a142e91a893ed 2500w" />
</Frame>

The main button (left side of card) shows instance status and provides quick access:

**Status Indicators:**

* **Open**: Instance loaded, click to access via browser
* **Connect**: Instance loaded, click for SSH info
* **Inactive**: Stopped but data preserved (can restart if GPU available)
* **Offline**: Machine disconnected from Vast servers
* **Scheduling**: Attempting to restart (waiting for GPU availability)
* **Creating**: Vast initiating instance creation
* **Loading**: Downloading Docker image
* **Connecting**: Docker running but connection not verified

### Instance Information

<Frame caption="ID numbers">
    <img src="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-9.webp?fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=45df3ca5eade69027abb1b63d11d2d91" alt="" data-og-width="1137" width="1137" data-og-height="265" height="265" data-path="images/console-instance-guide-9.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-9.webp?w=280&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=09376ffbc87f9898187000a4ff40c753 280w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-9.webp?w=560&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=b834904c3d7d25d0a895757d18dccc96 560w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-9.webp?w=840&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=612ab74906d4e37b7f48bca2eba02706 840w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-9.webp?w=1100&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=c156104dce169a17376e2d4bca82d21a 1100w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-9.webp?w=1650&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=5d615c24a6a55ea4c19f969141c0f18e 1650w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-9.webp?w=2500&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=65dcdb828fd4e6ce04037d4c72df13ac 2500w" />
</Frame>

**ID Information:**

* Instance ID - Unique identifier for your instance
* Host/Datacenter ID - Provider identification
* Machine ID - Physical machine identifier

**Hardware Details:**
<img src="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-10.webp?fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=e8598b22b07767de412534ef05d86644" alt="" data-og-width="800" width="800" data-og-height="194" height="194" data-path="images/console-instance-guide-10.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-10.webp?w=280&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=6b5a39bca4929960caddba21e5038e30 280w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-10.webp?w=560&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=2518cb4c39339170435eb81f4477e200 560w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-10.webp?w=840&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=9abc7ef1a9bc09b681aa0abfb4389fe8 840w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-10.webp?w=1100&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=7ab06edb75a83719e071da2d342a3be8 1100w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-10.webp?w=1650&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=81c72ca56dd9a0701a2f214d3be1a4b4 1650w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-10.webp?w=2500&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=d5bcbf5f46d5cfa68126c33361e348a7 2500w" />

* GPU model and count
* CPU and RAM allocation
* Storage capacity
* Network configuration

**Contract Info:**
<img src="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-12.webp?fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=20d3f1379bd41e625f646ba9769a16eb" alt="" data-og-width="800" width="800" data-og-height="396" height="396" data-path="images/console-instance-guide-12.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-12.webp?w=280&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=120388f90c8a9c25bbd968a1c078210d 280w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-12.webp?w=560&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=60a07f345df7fe155a2fbe4390c3209f 560w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-12.webp?w=840&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=21045200910f11781549c780e276a8b7 840w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-12.webp?w=1100&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=feaf4417b5b7b1cd49495517a5723108 1100w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-12.webp?w=1650&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=7eb294f05535573cc6ad8f043862ed7d 1650w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-12.webp?w=2500&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=03241fd0536aaaa8ade812c7541cbe0b 2500w" />

* Instance age (time since creation)
* Rental end date
* Remaining duration

## Instance Operations

### Starting, Stopping, and Destroying

<img src="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-5.webp?fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=82cbb83c39d36a1f1127f5a4537d94eb" alt="" data-og-width="1280" width="1280" data-og-height="307" height="307" data-path="images/console-instance-guide-5.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-5.webp?w=280&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=d687437cb212d7f3a065cfb4243e7228 280w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-5.webp?w=560&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=5449fc3a11300d3b46d890518f598625 560w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-5.webp?w=840&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=b4d7664c626e77e1062b93b12f7e42fa 840w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-5.webp?w=1100&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=f079369ef8cb17c3b9782b65924fad98 1100w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-5.webp?w=1650&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=a381b4275753b27ba092aa774ad97d06 1650w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-5.webp?w=2500&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=a69702ff4c5bc3d92ddf62b9b925c3e1 2500w" />

* **Stop Button** (square icon): Pauses instance, preserves data, continues storage charges
* **Destroy Button** (trash icon): Permanently deletes instance and all data
* **Restart Button** (play icon): Appears when stopped, attempts to reclaim GPU

<Warning>
  **Important:** Stopped instances continue incurring storage charges. Destroy instances when no longer needed to avoid ongoing costs.
</Warning>

### Restart Behavior

<Frame caption="Play button">
    <img src="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-6.webp?fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=7ab41ae42eb8246933307998fe70f765" alt="" data-og-width="1280" width="1280" data-og-height="306" height="306" data-path="images/console-instance-guide-6.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-6.webp?w=280&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=9dd3f2a097e4f88b561a8fa8b6925d20 280w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-6.webp?w=560&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=ea401cbfe1b6c515b63206cd7f6fbdfe 560w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-6.webp?w=840&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=043f6dc2c8f68addcf303ac4e78d3dd6 840w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-6.webp?w=1100&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=881c1894d50bf6e5e40adc4008aea402 1100w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-6.webp?w=1650&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=0218a4b1fbad303493afdebba232fd66 1650w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-6.webp?w=2500&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=64e94982b60bc5050f5421692728c522 2500w" />
</Frame>

When restarting a stopped instance:

1. Instance enters `SCHEDULING` status
2. Waits for GPU availability
3. If stuck >30 seconds, GPU likely rented by another user
4. Cancel scheduling by clicking stop again
5. Consider creating new instance if GPU unavailable

### Additional Controls

<img src="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-13.webp?fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=c9db6b0fcb2826990104f1df4b983f6c" alt="" data-og-width="1280" width="1280" data-og-height="306" height="306" data-path="images/console-instance-guide-13.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-13.webp?w=280&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=e0585ed33c63b0ad7e9d7536e285ac02 280w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-13.webp?w=560&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=83463e53647bf74cb687aeecf5680678 560w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-13.webp?w=840&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=f367200f941413057f93520e1c52bbe2 840w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-13.webp?w=1100&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=97942d6886dfae52e483eb78ccaf5a6d 1100w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-13.webp?w=1650&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=73d5d566f35cc7508b04450f143237ba 1650w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-13.webp?w=2500&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=3f390761af0b64f869443dc88741e742 2500w" />

* **Label Instance** - Add custom name for identification
* **Reboot Instance** - Restart without data loss
* **View Logs** - Access Docker container logs

## Data Management

<Frame caption="Data movement">
    <img src="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-7.webp?fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=108aedecb03c94c20252d40845e2c4fb" alt="" data-og-width="1280" width="1280" data-og-height="330" height="330" data-path="images/console-instance-guide-7.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-7.webp?w=280&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=9fa6cff4efe7a60dff881e7d6fb2ec46 280w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-7.webp?w=560&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=dcd56f53be5a0cf3a20d6cb7e682b4bc 560w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-7.webp?w=840&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=495eceed2e02eeb6a5fa78c69cc5a4f1 840w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-7.webp?w=1100&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=a6c7847f33165e34772cd12dae832f1f 1100w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-7.webp?w=1650&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=cbd830668fe7b799dfaf561ebf393279 1650w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-instance-guide-7.webp?w=2500&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=fafe2b12e21c1bb9948fd0f47d7d7b1b 2500w" />
</Frame>

* **Copy Data** - Transfer between your instances (see [Data Movement](/documentation/instances/storage/data-movement))
* **Cloud Sync** - Sync with cloud providers (see [Cloud Sync](/documentation/instances/storage/cloud-sync))

<Note>
  Use Cloud Sync only on trusted datacenters (indicated by **Secure** icon).
</Note>

## Connection Quick Reference

For detailed connection instructions, see [Connect to Instances](/documentation/instances/connect/overview):

* **SSH button** - Shows SSH command
* **Open button** - Launches web UI
* **IP/Ports button** - Network information

## Troubleshooting Instance States

### Instance Stuck on "Loading"

* Normal for 30 seconds with cached images
* Can take hours with slow internet/large images
* Not charged during loading
* Try machines with faster internet

### Instance Stuck on "Scheduling"

When stopped instances try to restart:

* GPU may be reassigned to other users
* High-priority jobs block restart
* May wait indefinitely for GPU availability
* Consider copying data to new instance

### Instance Stuck on "Connecting"

* Port configuration may be broken
* Report the machine
* Try different machine

### Machine Shows "Offline"

* Lost connection to Vast servers
* Often internet/power issues
* Host notified automatically
* May be maintenance or unforeseen problems

## Important Considerations

### Data Persistence

* **Stopped instances**: Data preserved, storage charges continue
* **Destroyed instances**: All data permanently deleted
* **Before destroying**: Copy important data or sync to cloud

### Contract Expiration

<Warning>
  Expired instances may be deleted 48 hours after expiration. Expired instances cannot restart. Retrieve your data promptly.
</Warning>

### Security

* Hosts can technically access files on their machines
* For sensitive data, use verified datacenters
* Implement encryption for critical data

### IP Addresses

Some instances have dynamic IPs that may change. Check IP type via the IP button on instance card. For static IPs, filter by "Static IP Address" when searching.

## Common Questions

### Can I run Docker inside my instance?

No, instances are already Docker containers. Docker-in-Docker is not supported.

### Do I pay for "Loading" instances?

No, you're not charged while instances show "Loading" status.

### Can I view past instances?

No, destroyed instances cannot be viewed. Recent template history is preserved for configuration reference.

### Why is my machine location showing only ", US"?

This means geolocation couldn't determine the state. It's not an indication of reliability.

### Can I run VMs or bare metal?

Currently only Docker containers are supported. VM and bare-metal options planned for future.

## Next Steps

<CardGroup cols={3}>
  <Card title="Data Movement" href="/documentation/instances/storage/data-movement" icon="arrows">
    Transfer files to and from your instances
  </Card>

  <Card title="Reserved Instances" href="/documentation/instances/choosing/reserved-instances" icon="calendar">
    Save up to 50% with long-term commitments
  </Card>

  <Card title="Instance Portal" href="/documentation/instances/instance-portal" icon="browser">
    Access web services running in your instances
  </Card>
</CardGroup>
