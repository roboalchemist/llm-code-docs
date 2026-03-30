# Source: https://io.net/docs/guides/clouds/deploy-vm-on-demand.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy VM on Demand

> Instantly deploy GPU accelerated virtual machines designed for AI and ML workloads. Configure, launch, and manage your compute VMs. CPUs are included with every instance.

**VM on Demand** provides a seamless way to deploy fully equipped virtual machines optimized for AI and machine learning workflows. Designed for data scientists, researchers, and builders, it enables you to launch high-performance GPU or CPU-powered environments with a few simple clicks.

You can scale resources as your workloads grow, monitor performance, and manage deployments, all through an intuitive interface. Whether you are training deep learning models, running data pipelines, or testing ML prototypes, **VM on Demand** delivers a fast, reliable, and frictionless compute experience.

## Quick Start:

1. Click **Deploy Virtual Machine** on the **Home** tab.
2. Choose your **Processor**.
3. Configure your **Virtual Machine**.
4. Monitor your deployment details in the sidebar.
5. Once the minimum requirements are met, review and deploy your cluster.
6. Start using your **Virtual Machine**.
7. View and manage your virtual machines in the **Virtual Machine** tab.

## Deploying Clusters

### 1. Getting Started

To begin, click the **Deploy** button in the **Virtual Machine** row on the **Home** tab of the io.net Cloud platform.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/aQkzom-bsqQctd2E/images/docs/cloud_vm_on_demand/IOCloud_VM_DeployHomeTab.png?fit=max&auto=format&n=aQkzom-bsqQctd2E&q=85&s=a2c463c6c14c01528ca52175a7604211" alt="IO Cloud VM Deploy Home Tab Pn" data-og-width="3404" width="3404" data-og-height="898" height="898" data-path="images/docs/cloud_vm_on_demand/IOCloud_VM_DeployHomeTab.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/aQkzom-bsqQctd2E/images/docs/cloud_vm_on_demand/IOCloud_VM_DeployHomeTab.png?w=280&fit=max&auto=format&n=aQkzom-bsqQctd2E&q=85&s=539bc04726663ced8688fc8df7f1d658 280w, https://mintcdn.com/ionet-cca8037f/aQkzom-bsqQctd2E/images/docs/cloud_vm_on_demand/IOCloud_VM_DeployHomeTab.png?w=560&fit=max&auto=format&n=aQkzom-bsqQctd2E&q=85&s=ab2eccfa70096ca0ac8236a3de9ea962 560w, https://mintcdn.com/ionet-cca8037f/aQkzom-bsqQctd2E/images/docs/cloud_vm_on_demand/IOCloud_VM_DeployHomeTab.png?w=840&fit=max&auto=format&n=aQkzom-bsqQctd2E&q=85&s=22933af87dfb463807dfc775250651e2 840w, https://mintcdn.com/ionet-cca8037f/aQkzom-bsqQctd2E/images/docs/cloud_vm_on_demand/IOCloud_VM_DeployHomeTab.png?w=1100&fit=max&auto=format&n=aQkzom-bsqQctd2E&q=85&s=b795cfbdf1dd1811300a72f1f48d4263 1100w, https://mintcdn.com/ionet-cca8037f/aQkzom-bsqQctd2E/images/docs/cloud_vm_on_demand/IOCloud_VM_DeployHomeTab.png?w=1650&fit=max&auto=format&n=aQkzom-bsqQctd2E&q=85&s=ca54b59dfcee37eb321bdb5e41a3df48 1650w, https://mintcdn.com/ionet-cca8037f/aQkzom-bsqQctd2E/images/docs/cloud_vm_on_demand/IOCloud_VM_DeployHomeTab.png?w=2500&fit=max&auto=format&n=aQkzom-bsqQctd2E&q=85&s=70c44847c45f6b1fa241e982c07f1266 2500w" />
</Frame>

You can also open the **Virtual Machine** tab directly and select **Deploy Virtual Machine** to start a new deployment.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/QE-7RntWqUBQq68h/images/docs/cloud_vm_on_demand/IOCloud_VM_DeployVM.png?fit=max&auto=format&n=QE-7RntWqUBQq68h&q=85&s=81d2d06ee58b7d7c94adbd23edce3315" alt="IO Cloud VM Deploy VM Pn" data-og-width="3374" width="3374" data-og-height="492" height="492" data-path="images/docs/cloud_vm_on_demand/IOCloud_VM_DeployVM.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/QE-7RntWqUBQq68h/images/docs/cloud_vm_on_demand/IOCloud_VM_DeployVM.png?w=280&fit=max&auto=format&n=QE-7RntWqUBQq68h&q=85&s=83a8636a7595c8651211bc95257b3e43 280w, https://mintcdn.com/ionet-cca8037f/QE-7RntWqUBQq68h/images/docs/cloud_vm_on_demand/IOCloud_VM_DeployVM.png?w=560&fit=max&auto=format&n=QE-7RntWqUBQq68h&q=85&s=0990f0cdcdccce60b97b8311b1d75683 560w, https://mintcdn.com/ionet-cca8037f/QE-7RntWqUBQq68h/images/docs/cloud_vm_on_demand/IOCloud_VM_DeployVM.png?w=840&fit=max&auto=format&n=QE-7RntWqUBQq68h&q=85&s=ce524255696007f55a4bae72d636866b 840w, https://mintcdn.com/ionet-cca8037f/QE-7RntWqUBQq68h/images/docs/cloud_vm_on_demand/IOCloud_VM_DeployVM.png?w=1100&fit=max&auto=format&n=QE-7RntWqUBQq68h&q=85&s=4b9fac7af58a1a04285b94efd61a2b42 1100w, https://mintcdn.com/ionet-cca8037f/QE-7RntWqUBQq68h/images/docs/cloud_vm_on_demand/IOCloud_VM_DeployVM.png?w=1650&fit=max&auto=format&n=QE-7RntWqUBQq68h&q=85&s=ea69683823c8134450950151a4d91fc4 1650w, https://mintcdn.com/ionet-cca8037f/QE-7RntWqUBQq68h/images/docs/cloud_vm_on_demand/IOCloud_VM_DeployVM.png?w=2500&fit=max&auto=format&n=QE-7RntWqUBQq68h&q=85&s=b8c394a23eb5842ffc2b8859db547493 2500w" />
</Frame>

### 2. Select your Virtual Machine Processor

Choose a processor based on your requirements. Each card displays its specifications, including:

* *Device Availability*
* *Price*
* *VRAM per card*
* *Storage*
* *Supplier*
* *Location*

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/OQxB7hEvXfxcrbuQ/images/docs/cloud_vm_on_demand/IOCloud_VM_ChooseCluster.png?fit=max&auto=format&n=OQxB7hEvXfxcrbuQ&q=85&s=0301c2f47e36d059ccd8dc3c2281ffba" alt="IO Cloud VM Choose Cluster Pn" data-og-width="2610" width="2610" data-og-height="1126" height="1126" data-path="images/docs/cloud_vm_on_demand/IOCloud_VM_ChooseCluster.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/OQxB7hEvXfxcrbuQ/images/docs/cloud_vm_on_demand/IOCloud_VM_ChooseCluster.png?w=280&fit=max&auto=format&n=OQxB7hEvXfxcrbuQ&q=85&s=7ee3f6f0f843c44709ae12c476e10f22 280w, https://mintcdn.com/ionet-cca8037f/OQxB7hEvXfxcrbuQ/images/docs/cloud_vm_on_demand/IOCloud_VM_ChooseCluster.png?w=560&fit=max&auto=format&n=OQxB7hEvXfxcrbuQ&q=85&s=6b01a9a355241bdf7c9b0ac8eb835147 560w, https://mintcdn.com/ionet-cca8037f/OQxB7hEvXfxcrbuQ/images/docs/cloud_vm_on_demand/IOCloud_VM_ChooseCluster.png?w=840&fit=max&auto=format&n=OQxB7hEvXfxcrbuQ&q=85&s=1507ff617327ca300fd1e4a539649bb8 840w, https://mintcdn.com/ionet-cca8037f/OQxB7hEvXfxcrbuQ/images/docs/cloud_vm_on_demand/IOCloud_VM_ChooseCluster.png?w=1100&fit=max&auto=format&n=OQxB7hEvXfxcrbuQ&q=85&s=17268558491fe6cc35148901907c1556 1100w, https://mintcdn.com/ionet-cca8037f/OQxB7hEvXfxcrbuQ/images/docs/cloud_vm_on_demand/IOCloud_VM_ChooseCluster.png?w=1650&fit=max&auto=format&n=OQxB7hEvXfxcrbuQ&q=85&s=a21d45b193b737a6d3241910d793a072 1650w, https://mintcdn.com/ionet-cca8037f/OQxB7hEvXfxcrbuQ/images/docs/cloud_vm_on_demand/IOCloud_VM_ChooseCluster.png?w=2500&fit=max&auto=format&n=OQxB7hEvXfxcrbuQ&q=85&s=239050a87a25708c72f393dedf52d65f 2500w" />
</Frame>

To view detailed technical information, click **More details**. This will display additional specifications such as interconnect technology, NVLink support, memory, and the number of virtual CPUs (vCPUs).

You can refine your selection using the **Search GPU Model** field or by applying filters. Click **Filter** to filter by:

* *GPU Family*
* *Region*
* *Supplier*
* *GPU Memory*
* *CPU Cores*
* *Device Memory*
* *Storage*

You can apply these filters individually or in combination.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/OQxB7hEvXfxcrbuQ/images/docs/cloud_vm_on_demand/IOCloud_VM_Filters.png?fit=max&auto=format&n=OQxB7hEvXfxcrbuQ&q=85&s=85d1861320d588e9140776deafbc417b" alt="IO Cloud VM Filters Pn" data-og-width="2544" width="2544" data-og-height="524" height="524" data-path="images/docs/cloud_vm_on_demand/IOCloud_VM_Filters.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/OQxB7hEvXfxcrbuQ/images/docs/cloud_vm_on_demand/IOCloud_VM_Filters.png?w=280&fit=max&auto=format&n=OQxB7hEvXfxcrbuQ&q=85&s=04d538fb3d879f7ba898b92b6ef2bfd1 280w, https://mintcdn.com/ionet-cca8037f/OQxB7hEvXfxcrbuQ/images/docs/cloud_vm_on_demand/IOCloud_VM_Filters.png?w=560&fit=max&auto=format&n=OQxB7hEvXfxcrbuQ&q=85&s=b2edaa647302c94a42d1ccdd53b18306 560w, https://mintcdn.com/ionet-cca8037f/OQxB7hEvXfxcrbuQ/images/docs/cloud_vm_on_demand/IOCloud_VM_Filters.png?w=840&fit=max&auto=format&n=OQxB7hEvXfxcrbuQ&q=85&s=66057bb2f422dc7042dc3c94ef3c8daf 840w, https://mintcdn.com/ionet-cca8037f/OQxB7hEvXfxcrbuQ/images/docs/cloud_vm_on_demand/IOCloud_VM_Filters.png?w=1100&fit=max&auto=format&n=OQxB7hEvXfxcrbuQ&q=85&s=a5ba5f6da861093da66020c89f4db8a7 1100w, https://mintcdn.com/ionet-cca8037f/OQxB7hEvXfxcrbuQ/images/docs/cloud_vm_on_demand/IOCloud_VM_Filters.png?w=1650&fit=max&auto=format&n=OQxB7hEvXfxcrbuQ&q=85&s=a824c27b17bfb1f3f45a74eb15948615 1650w, https://mintcdn.com/ionet-cca8037f/OQxB7hEvXfxcrbuQ/images/docs/cloud_vm_on_demand/IOCloud_VM_Filters.png?w=2500&fit=max&auto=format&n=OQxB7hEvXfxcrbuQ&q=85&s=3cdf84ffd362dcad0a18afee84d65a6f 2500w" />
</Frame>

After selecting your Virtual Machine Processor, click **Next Step** to continue.

### 3. Configure Environment and SSH Keys

Set up your environment and link SSH Keys for secure access. You can choose between two image types:

<Note>
  Partner-provided clusters include a preloaded image that cannot be changed.

  To choose a specific image, select a processor supplied by **io.net**.
</Note>

<Tabs>
  <Tab title="General Purpose Image">
    The **General Purpose Image** provides a clean, flexible foundation for building any type of compute environment.

    ***Specifications:***

    * **OS:** Ubuntu 24.04 (64-bit)
    * **Size:** 3.5 GB (uncompressed)
    * **Includes:** CUDA Toolkit and drivers
    * **Ideal for:** Users who prefer to fully customize their development environment and software stack.

    <Frame>
            <img src="https://mintcdn.com/ionet-cca8037f/J61co2AJELos4Tk_/images/docs/cloud_vm_on_demand/IOCloud_VM_GeneralPurposeImage.png?fit=max&auto=format&n=J61co2AJELos4Tk_&q=85&s=fa36e39872240d1648b545ece85bbd53" alt="IO Cloud VM General Purpose Image Pn" data-og-width="1230" width="1230" data-og-height="788" height="788" data-path="images/docs/cloud_vm_on_demand/IOCloud_VM_GeneralPurposeImage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/J61co2AJELos4Tk_/images/docs/cloud_vm_on_demand/IOCloud_VM_GeneralPurposeImage.png?w=280&fit=max&auto=format&n=J61co2AJELos4Tk_&q=85&s=b2c62a31a54bdb2e02ee141933b612cf 280w, https://mintcdn.com/ionet-cca8037f/J61co2AJELos4Tk_/images/docs/cloud_vm_on_demand/IOCloud_VM_GeneralPurposeImage.png?w=560&fit=max&auto=format&n=J61co2AJELos4Tk_&q=85&s=86df63c1c208631fcfdafccacf081fb1 560w, https://mintcdn.com/ionet-cca8037f/J61co2AJELos4Tk_/images/docs/cloud_vm_on_demand/IOCloud_VM_GeneralPurposeImage.png?w=840&fit=max&auto=format&n=J61co2AJELos4Tk_&q=85&s=2744a5897992f2cb0acbb8b8b89fffee 840w, https://mintcdn.com/ionet-cca8037f/J61co2AJELos4Tk_/images/docs/cloud_vm_on_demand/IOCloud_VM_GeneralPurposeImage.png?w=1100&fit=max&auto=format&n=J61co2AJELos4Tk_&q=85&s=7fca8d198ebf67e050e61e08959fcc4b 1100w, https://mintcdn.com/ionet-cca8037f/J61co2AJELos4Tk_/images/docs/cloud_vm_on_demand/IOCloud_VM_GeneralPurposeImage.png?w=1650&fit=max&auto=format&n=J61co2AJELos4Tk_&q=85&s=2fd942224b21dfef5808e9e89ea677ac 1650w, https://mintcdn.com/ionet-cca8037f/J61co2AJELos4Tk_/images/docs/cloud_vm_on_demand/IOCloud_VM_GeneralPurposeImage.png?w=2500&fit=max&auto=format&n=J61co2AJELos4Tk_&q=85&s=1e93dcb0599c825b8dfc4d11b6742697 2500w" />
    </Frame>
  </Tab>

  <Tab title="Data Science Image">
    The **Data Science Image** provides a ready-to-use environment for machine learning, artificial intelligence, and data analytics workloads. It comes fully configured with GPU acceleration and essential data science tools, allowing you to begin experimentation and model development immediately without additional setup.

    ***Specifications:***

    * **OS:** Ubuntu 24.04.2 LTS
    * **Includes:**
      * Python 3.12
      * Conda 25.7.0
      * CUDA 12.1
      * RAPIDS 25.6.0
    * **Ideal for:**
      * Building and training deep learning or machine learning models using GPU acceleration.
      * Analyzing and processing large datasets with GPU-accelerated data frames.
      * Running distributed computing tasks with frameworks such as **Ray**.
      * Developing, visualizing, and testing AI workflows directly from **Jupyter Notebooks**.

    [View full image specification →](/guides/clouds/data-science-image-full-specification)

    <Frame>
            <img src="https://mintcdn.com/ionet-cca8037f/J61co2AJELos4Tk_/images/docs/cloud_vm_on_demand/IOCloud_VM_DataScienceImage.png?fit=max&auto=format&n=J61co2AJELos4Tk_&q=85&s=519c9ba1aaa2573a950426d131a587f0" alt="IO Cloud VM Data Science Image Pn" data-og-width="1244" width="1244" data-og-height="804" height="804" data-path="images/docs/cloud_vm_on_demand/IOCloud_VM_DataScienceImage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/J61co2AJELos4Tk_/images/docs/cloud_vm_on_demand/IOCloud_VM_DataScienceImage.png?w=280&fit=max&auto=format&n=J61co2AJELos4Tk_&q=85&s=480005439d78afebe85c10439d6f8f8f 280w, https://mintcdn.com/ionet-cca8037f/J61co2AJELos4Tk_/images/docs/cloud_vm_on_demand/IOCloud_VM_DataScienceImage.png?w=560&fit=max&auto=format&n=J61co2AJELos4Tk_&q=85&s=d0cae84d73b0ffa13219c8a7a449ae19 560w, https://mintcdn.com/ionet-cca8037f/J61co2AJELos4Tk_/images/docs/cloud_vm_on_demand/IOCloud_VM_DataScienceImage.png?w=840&fit=max&auto=format&n=J61co2AJELos4Tk_&q=85&s=6f28be10086f9fab9a8b07e73e3bf233 840w, https://mintcdn.com/ionet-cca8037f/J61co2AJELos4Tk_/images/docs/cloud_vm_on_demand/IOCloud_VM_DataScienceImage.png?w=1100&fit=max&auto=format&n=J61co2AJELos4Tk_&q=85&s=dadd8d60d67a786f3eee8e466754f692 1100w, https://mintcdn.com/ionet-cca8037f/J61co2AJELos4Tk_/images/docs/cloud_vm_on_demand/IOCloud_VM_DataScienceImage.png?w=1650&fit=max&auto=format&n=J61co2AJELos4Tk_&q=85&s=724d780dd4566b7d570531aed4743471 1650w, https://mintcdn.com/ionet-cca8037f/J61co2AJELos4Tk_/images/docs/cloud_vm_on_demand/IOCloud_VM_DataScienceImage.png?w=2500&fit=max&auto=format&n=J61co2AJELos4Tk_&q=85&s=0a58529a9a5a0a491fa508ded6da452c 2500w" />
    </Frame>
  </Tab>
</Tabs>

#### 4. Add your SSH Key

Choose one of the following methods to access your VM securely:

<Note>
  Partner-supplied clusters only support **Manual SSH key input**. You must add your SSH key by entering a key name and pasting your public key directly.

  To use the **Fetch from GitHub** feature, select an **io.net-supplied processor**. This allows you to retrieve your public SSH key automatically by entering your *GitHub ID*, simplifying setup and secure access.
</Note>

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/BAZn7bjtM3VrZc51/images/docs/cloud_vm_on_demand/IOCloud_VM_SSHOptions.png?fit=max&auto=format&n=BAZn7bjtM3VrZc51&q=85&s=e37a9771614d4ad8a767741278c4c3a9" alt="IO Cloud VM SSH Options Pn" data-og-width="1260" width="1260" data-og-height="550" height="550" data-path="images/docs/cloud_vm_on_demand/IOCloud_VM_SSHOptions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/BAZn7bjtM3VrZc51/images/docs/cloud_vm_on_demand/IOCloud_VM_SSHOptions.png?w=280&fit=max&auto=format&n=BAZn7bjtM3VrZc51&q=85&s=8bfc4f49c71fb950d47533fe25bd76b7 280w, https://mintcdn.com/ionet-cca8037f/BAZn7bjtM3VrZc51/images/docs/cloud_vm_on_demand/IOCloud_VM_SSHOptions.png?w=560&fit=max&auto=format&n=BAZn7bjtM3VrZc51&q=85&s=a008ea70f9aad781c18bd23c6db211e8 560w, https://mintcdn.com/ionet-cca8037f/BAZn7bjtM3VrZc51/images/docs/cloud_vm_on_demand/IOCloud_VM_SSHOptions.png?w=840&fit=max&auto=format&n=BAZn7bjtM3VrZc51&q=85&s=55e49e00d79ae99ee7b8c2eac3428826 840w, https://mintcdn.com/ionet-cca8037f/BAZn7bjtM3VrZc51/images/docs/cloud_vm_on_demand/IOCloud_VM_SSHOptions.png?w=1100&fit=max&auto=format&n=BAZn7bjtM3VrZc51&q=85&s=8742670ca15c03f21aa30ab687373f19 1100w, https://mintcdn.com/ionet-cca8037f/BAZn7bjtM3VrZc51/images/docs/cloud_vm_on_demand/IOCloud_VM_SSHOptions.png?w=1650&fit=max&auto=format&n=BAZn7bjtM3VrZc51&q=85&s=1c0940aa7eacf358ca9858463bc1e2a7 1650w, https://mintcdn.com/ionet-cca8037f/BAZn7bjtM3VrZc51/images/docs/cloud_vm_on_demand/IOCloud_VM_SSHOptions.png?w=2500&fit=max&auto=format&n=BAZn7bjtM3VrZc51&q=85&s=5a1ad07d5ccca299f8998b9dd9f6869d 2500w" />
</Frame>

<Tabs>
  <Tab title="Manual Input">
    Use this option to add your SSH key directly.

    1. Enter a **Key Name** to identify the key.
    2. Paste your **public SSH key** into the field provided.

    You can repeat these steps to add multiple SSH keys if several users or systems require access. Each key you add will be authorized for SSH connections to your deployed VM.

    This method is especially useful if you manage SSH keys locally or use multiple machines. It also ensures that you can explicitly control which public keys are linked to your cluster.

    <Tip>
      Make sure that you paste only the public portion of your SSH key. Private keys should never be uploaded or shared.
    </Tip>

    <img src="https://mintcdn.com/ionet-cca8037f/y1wKR-9WM_bEW5dd/images/docs/cloud_vm_on_demand/Containers7.jpg?fit=max&auto=format&n=y1wKR-9WM_bEW5dd&q=85&s=b70924abba1ca893d807676659139ce3" alt="Containers7 Jp" title="Containers7 Jp" className="mx-auto" style={{ width:"83%" }} data-og-width="1516" width="1516" data-og-height="502" height="502" data-path="images/docs/cloud_vm_on_demand/Containers7.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/y1wKR-9WM_bEW5dd/images/docs/cloud_vm_on_demand/Containers7.jpg?w=280&fit=max&auto=format&n=y1wKR-9WM_bEW5dd&q=85&s=57f66861905582d49e01ee90e59c5e21 280w, https://mintcdn.com/ionet-cca8037f/y1wKR-9WM_bEW5dd/images/docs/cloud_vm_on_demand/Containers7.jpg?w=560&fit=max&auto=format&n=y1wKR-9WM_bEW5dd&q=85&s=2fbd7efb1a0611b28653a4188b353d53 560w, https://mintcdn.com/ionet-cca8037f/y1wKR-9WM_bEW5dd/images/docs/cloud_vm_on_demand/Containers7.jpg?w=840&fit=max&auto=format&n=y1wKR-9WM_bEW5dd&q=85&s=ff56b65904ccd07929ddfbc299f159a9 840w, https://mintcdn.com/ionet-cca8037f/y1wKR-9WM_bEW5dd/images/docs/cloud_vm_on_demand/Containers7.jpg?w=1100&fit=max&auto=format&n=y1wKR-9WM_bEW5dd&q=85&s=8322420e9775d67a8df9f21ee7d5e6b1 1100w, https://mintcdn.com/ionet-cca8037f/y1wKR-9WM_bEW5dd/images/docs/cloud_vm_on_demand/Containers7.jpg?w=1650&fit=max&auto=format&n=y1wKR-9WM_bEW5dd&q=85&s=9599a5494a90841d2c2d7fecd2bd9d87 1650w, https://mintcdn.com/ionet-cca8037f/y1wKR-9WM_bEW5dd/images/docs/cloud_vm_on_demand/Containers7.jpg?w=2500&fit=max&auto=format&n=y1wKR-9WM_bEW5dd&q=85&s=e2270b11624d6802fa15451b5c7ad834 2500w" />
  </Tab>

  <Tab title="Fetch from GitHub">
    If your public SSH keys are already associated with your GitHub account, you can retrieve them automatically using the Fetch from GitHub feature.

    1. Select the **Fetch SSH key from GitHub** option in the Type of *SSH key* field.
    2. Enter your **GitHub ID**, or multiple **GitHub IDs** separated with commas, in the field provided.
    3. The system will automatically retrieve and apply your public SSH keys from your GitHub profile.

    This option is a fast and convenient way to authenticate without copying or pasting keys manually. It is especially useful if you frequently rotate keys or work across multiple environments, since your GitHub account always stores the latest authorized keys.

    <Tip>
      You can view or manage your SSH keys in your GitHub account by navigating to **Settings > SSH and GPG keys**.
    </Tip>
  </Tab>
</Tabs>

### 5. Customize your Virtual Machine (Optional)

In this step, you can personalize your deployment by assigning a **name** and configuring **network services**.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/4HwAvqkbc2sS9qqW/images/docs/cloud_vm_on_demand/IOCloud_VM_Customize.png?fit=max&auto=format&n=4HwAvqkbc2sS9qqW&q=85&s=0e1169b29462aa9f9fc067b3ad1ad698" alt="IO Cloud VM Customize Pn" data-og-width="1410" width="1410" data-og-height="1482" height="1482" data-path="images/docs/cloud_vm_on_demand/IOCloud_VM_Customize.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/4HwAvqkbc2sS9qqW/images/docs/cloud_vm_on_demand/IOCloud_VM_Customize.png?w=280&fit=max&auto=format&n=4HwAvqkbc2sS9qqW&q=85&s=990c27623bd294d9641de0520b2b6e37 280w, https://mintcdn.com/ionet-cca8037f/4HwAvqkbc2sS9qqW/images/docs/cloud_vm_on_demand/IOCloud_VM_Customize.png?w=560&fit=max&auto=format&n=4HwAvqkbc2sS9qqW&q=85&s=e999313a7732ed66717bf61ae386a0bc 560w, https://mintcdn.com/ionet-cca8037f/4HwAvqkbc2sS9qqW/images/docs/cloud_vm_on_demand/IOCloud_VM_Customize.png?w=840&fit=max&auto=format&n=4HwAvqkbc2sS9qqW&q=85&s=2681acc348dae0b6e875d055899c0d74 840w, https://mintcdn.com/ionet-cca8037f/4HwAvqkbc2sS9qqW/images/docs/cloud_vm_on_demand/IOCloud_VM_Customize.png?w=1100&fit=max&auto=format&n=4HwAvqkbc2sS9qqW&q=85&s=17277f4bf19a5fe0c76b08bb85cf03f2 1100w, https://mintcdn.com/ionet-cca8037f/4HwAvqkbc2sS9qqW/images/docs/cloud_vm_on_demand/IOCloud_VM_Customize.png?w=1650&fit=max&auto=format&n=4HwAvqkbc2sS9qqW&q=85&s=94840e4b82ede7260701c048a9961d0e 1650w, https://mintcdn.com/ionet-cca8037f/4HwAvqkbc2sS9qqW/images/docs/cloud_vm_on_demand/IOCloud_VM_Customize.png?w=2500&fit=max&auto=format&n=4HwAvqkbc2sS9qqW&q=85&s=7fa513b7775d049c725bb7416af59006 2500w" />
</Frame>

**Cluster Name**

You can assign a unique name to your cluster to help identify and manage it easily.

Enter your preferred name in the **Your Cluster Name** field. This name will appear throughout your dashboard and logs, making it simpler to distinguish between different clusters or projects.

**Network Services**

Network services allow you to expose specific ports on your virtual machine that are necessary for your applications or workflows. These ports enable external access to services running inside your virtual machine, such as APIs, web applications, or databases.

By defining network services during setup, you ensure that your required tools and applications are reachable while keeping all other ports securely closed by default. This approach provides flexibility for your workloads without compromising security.

You can configure multiple network services depending on your use case.

<Note>
  Partner-supplied clusters expose all ports. However, the following ports are occupied by default:

  * ***Port 22 - SSH Access***
  * ***Port 53 - System DNS***
  * ***Port 5555 - NVIDIA Host Engine***
  * ***Port 9100 - Node Exporter: Metrics***
  * ***Port 9400 - DCGM Exporter: GPU Metrics***
  * ***Port 12345  and 12346 - Grafana Agent***
</Note>

To expose additional ports or services, follow these steps:

1. Click **Add Network Service**
2. Provide the required details:
   * *Service Name*
   * *Port Number*
   * *Protocol* (TCP or UDP)
   * *Whitelisted IPs* (IPv4 subnet)
3. Click the **+** button to add each IP to your whitelist.

<Warning>
  Network services and port configurations cannot be changed after virtual machine deployment. Ensure that all required ports are defined before deployment, and expose them in your Docker command inside the VM.
</Warning>

<Accordion title="Port Exposure on io.net">
  When deploying containers, you must expose ports in two locations:

  1. **Inside the VM (Docker):**

  Specify ports when running your container.

  ```bash  theme={null}
  docker run -d -p 8082:8082 your-image-name
  ```

  2. **io.net Network or Frontend Configuration:**

  After deployment, the platform assigns external ports that map to your container ports.\
  These external ports are used to access your services.

  <Note>
    Docker port exposure inside the VM does not automatically propagate to the external network. Both configurations are required for external accessibility.
  </Note>
</Accordion>

### 6. Review and Deploy

A sidebar on the right displays all your deployment details, including:

* *Machine Type*
* *Processor*
* *Cost*
* *GPUs per VM*
* *Location*
* *Duration type (Hourly, Daily, Weekly, Monthly)*
* *Duration*

After confirming that all details are correct and the minimum requirements are met, click **Pay & Deploy**.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/lK01lMJLid69zrYt/images/docs/cloud_vm_on_demand/IOCloud_VM_SummaryView.png?fit=max&auto=format&n=lK01lMJLid69zrYt&q=85&s=87832c4dc2a51ba95f9255e04c7b23ba" alt="IO Cloud VM Deployment and Summary" data-og-width="2952" width="2952" data-og-height="1784" height="1784" data-path="images/docs/cloud_vm_on_demand/IOCloud_VM_SummaryView.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/lK01lMJLid69zrYt/images/docs/cloud_vm_on_demand/IOCloud_VM_SummaryView.png?w=280&fit=max&auto=format&n=lK01lMJLid69zrYt&q=85&s=7ced19e51fa683b18db6b304be2f4215 280w, https://mintcdn.com/ionet-cca8037f/lK01lMJLid69zrYt/images/docs/cloud_vm_on_demand/IOCloud_VM_SummaryView.png?w=560&fit=max&auto=format&n=lK01lMJLid69zrYt&q=85&s=1e3612fd05244bf724998524454980d2 560w, https://mintcdn.com/ionet-cca8037f/lK01lMJLid69zrYt/images/docs/cloud_vm_on_demand/IOCloud_VM_SummaryView.png?w=840&fit=max&auto=format&n=lK01lMJLid69zrYt&q=85&s=481c3a280ef43d8ec8d9ebdda6714667 840w, https://mintcdn.com/ionet-cca8037f/lK01lMJLid69zrYt/images/docs/cloud_vm_on_demand/IOCloud_VM_SummaryView.png?w=1100&fit=max&auto=format&n=lK01lMJLid69zrYt&q=85&s=3a27aa99fe8a4989f920356e47d9feb7 1100w, https://mintcdn.com/ionet-cca8037f/lK01lMJLid69zrYt/images/docs/cloud_vm_on_demand/IOCloud_VM_SummaryView.png?w=1650&fit=max&auto=format&n=lK01lMJLid69zrYt&q=85&s=8df21bb6e43b29a5b708f993d05b17f3 1650w, https://mintcdn.com/ionet-cca8037f/lK01lMJLid69zrYt/images/docs/cloud_vm_on_demand/IOCloud_VM_SummaryView.png?w=2500&fit=max&auto=format&n=lK01lMJLid69zrYt&q=85&s=0f7d9de1f9d665ae53daaf9d620b6c21 2500w" />
</Frame>

A payment window will appear where you can complete the transaction using **IO Credits**, **Credit or Debit Cards**, **USDC**, or **IO Coin**.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/5G80a4_E0KSdwwvg/images/docs/cloud_vm_on_demand/IOCloud_VM_Payment.png?fit=max&auto=format&n=5G80a4_E0KSdwwvg&q=85&s=5767cd5023d7d146c88f37b56bf252bf" alt="IO Cloud VM Payment Pn" data-og-width="1288" width="1288" data-og-height="1074" height="1074" data-path="images/docs/cloud_vm_on_demand/IOCloud_VM_Payment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/5G80a4_E0KSdwwvg/images/docs/cloud_vm_on_demand/IOCloud_VM_Payment.png?w=280&fit=max&auto=format&n=5G80a4_E0KSdwwvg&q=85&s=dbb8c5e84775b18f235da3b31a93c121 280w, https://mintcdn.com/ionet-cca8037f/5G80a4_E0KSdwwvg/images/docs/cloud_vm_on_demand/IOCloud_VM_Payment.png?w=560&fit=max&auto=format&n=5G80a4_E0KSdwwvg&q=85&s=ad750d1520dfaa821bb843b241fb51dd 560w, https://mintcdn.com/ionet-cca8037f/5G80a4_E0KSdwwvg/images/docs/cloud_vm_on_demand/IOCloud_VM_Payment.png?w=840&fit=max&auto=format&n=5G80a4_E0KSdwwvg&q=85&s=d505fa142e65ee9c335f5920a177078e 840w, https://mintcdn.com/ionet-cca8037f/5G80a4_E0KSdwwvg/images/docs/cloud_vm_on_demand/IOCloud_VM_Payment.png?w=1100&fit=max&auto=format&n=5G80a4_E0KSdwwvg&q=85&s=2dd7332a070e40bc6c251e15f177a8a2 1100w, https://mintcdn.com/ionet-cca8037f/5G80a4_E0KSdwwvg/images/docs/cloud_vm_on_demand/IOCloud_VM_Payment.png?w=1650&fit=max&auto=format&n=5G80a4_E0KSdwwvg&q=85&s=56aef9bbad8e99e8592348127344de56 1650w, https://mintcdn.com/ionet-cca8037f/5G80a4_E0KSdwwvg/images/docs/cloud_vm_on_demand/IOCloud_VM_Payment.png?w=2500&fit=max&auto=format&n=5G80a4_E0KSdwwvg&q=85&s=b32d796e14a068a9480fe5be776bfea4 2500w" />
</Frame>

Once payment is confirmed, your cluster deployment will begin automatically.

## Viewing Virtual Machines

After deployment, you can view your virtual machines.

Navigate to the **Virtual Machines** tab to monitor performance or launch additional VMs.

The **Virtual Machines Dashboard** allows you to filter clusters by their current status. Click on a specific VM to open its details page.

Each **Detail** page shows you:

* Real-time resource usage information
* SSH connection details
* Billing and usage insights

### Connecting to your Virtual Machine

1. Locate the *SSH Access* field on your cluster page and copy the provided command.

<img src="https://mintcdn.com/ionet-cca8037f/y1wKR-9WM_bEW5dd/images/docs/cloud_vm_on_demand/Containers9.jpg?fit=max&auto=format&n=y1wKR-9WM_bEW5dd&q=85&s=e318bc99a641e882ab3a51875cbe9681" alt="Containers9 Jp" data-og-width="1547" width="1547" data-og-height="616" height="616" data-path="images/docs/cloud_vm_on_demand/Containers9.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/y1wKR-9WM_bEW5dd/images/docs/cloud_vm_on_demand/Containers9.jpg?w=280&fit=max&auto=format&n=y1wKR-9WM_bEW5dd&q=85&s=13019db5f2952bd661a11c11d60e7af3 280w, https://mintcdn.com/ionet-cca8037f/y1wKR-9WM_bEW5dd/images/docs/cloud_vm_on_demand/Containers9.jpg?w=560&fit=max&auto=format&n=y1wKR-9WM_bEW5dd&q=85&s=28ac60571df27532b61b82e376299d03 560w, https://mintcdn.com/ionet-cca8037f/y1wKR-9WM_bEW5dd/images/docs/cloud_vm_on_demand/Containers9.jpg?w=840&fit=max&auto=format&n=y1wKR-9WM_bEW5dd&q=85&s=c0d57605c7a86d757de66d4798057dd0 840w, https://mintcdn.com/ionet-cca8037f/y1wKR-9WM_bEW5dd/images/docs/cloud_vm_on_demand/Containers9.jpg?w=1100&fit=max&auto=format&n=y1wKR-9WM_bEW5dd&q=85&s=a41c7210b031e10a82eb1185e751f1af 1100w, https://mintcdn.com/ionet-cca8037f/y1wKR-9WM_bEW5dd/images/docs/cloud_vm_on_demand/Containers9.jpg?w=1650&fit=max&auto=format&n=y1wKR-9WM_bEW5dd&q=85&s=6fb43c974412d90153acc7f3a1b76131 1650w, https://mintcdn.com/ionet-cca8037f/y1wKR-9WM_bEW5dd/images/docs/cloud_vm_on_demand/Containers9.jpg?w=2500&fit=max&auto=format&n=y1wKR-9WM_bEW5dd&q=85&s=202aa4a336efebc7fa64b3ff2c6a3c54 2500w" />

2. Open your **Terminal** and paste the command, then press **Enter**.
3. When prompted to confirm the connection, type **yes** and press **Enter**.
4. Once connected, you will see the welcome message and gain access to your VM through the SSH terminal.
