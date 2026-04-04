# Source: https://developer.nvidia.com/gpudirect-storage.md

# Magnum IO GPUDirect Storage

## A Direct Path Between Storage and GPU Memory

As datasets increase in size, the time spent loading data can impact application performance. GPUDirect® Storage creates a direct data path between local or remote storage, such as NVMe or NVMe over Fabrics (NVMe-oF), and GPU memory. By enabling a direct-memory access (DMA) engine near the network adapter or storage, it moves data into or out of GPU memory—without burdening the CPU.

  
[Download](#Download)[Technical overview](https://nvdam.widen.net/s/k8vrp9xkft/tech-overview-magnum-io-1790750-r5-web) [Read blog](/blog/accelerating-io-in-the-modern-data-center-magnum-io-storage-partnerships/)

![GPU direct storage](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/magnum-io-gpudirect-storage-l.svg)
_GPUDirect Storage enables a direct data path between storage and GPU memory and avoids extra copies through a bounce buffer in the CPU’s memory._

## Partner Ecosystem

### GA

NVIDIA GPUDirect Storage integrated solution in production.

[![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/ddn-logo-190w-107h.svg)](https://www.ddn.com/)

[![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/dellemc-logo-190w-107h.svg)](https://www.delltechnologies.com/en-us/storage/powerscale.html)

[![](https://developer.download.nvidia.com/images/HS_Horiz_Tag_Blk@300x-8.png)](https://hammerspace.com/)

[![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/hpe-logo-190w-107h.svg)](https://www.hpe.com)

[![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/hitachi-inspire-the-next-logo-1902-107h.svg)](https://www.hitachivantara.com/en-us/home.html)

[![IBM logo](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/Logo-IBM-Azul.png)](https://www.ibm.com/us-en/)

[![Kioxia logo](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/kioxia-logo-190w-107h.svg)](https://www.kioxia.com/en-us/top.html)

[![Liqid logo](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/liqid-logo-190w-107h.svg)](https://www.liqid.com/)

[![Micron logo](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/micron-logo-190w-107h.svg)](https://www.micron.com/about/blog/2020/july/maximize-your-investment-in-micron-ssds-for-ai-ml-workloads-with-nvidia-gpudirect-storage)

[![Netapp logo](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/netapp-logo-190w-107h.svg)](http://www.netapp.com/)

[![Netapp logo](https://developer.download.nvidia.com/images/Nutanix-Logo-Charcoal-Gray-Digital.svg)](https://www.nutanix.com/)

[![Pure storage logo](https://developer.download.nvidia.com/images/pure-storage-logo.svg)](https://www.purestorage.com/)

[![Samsung logo](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/190w-107h-samsung-logo.svg)](https://www.samsung.com/us/)

[![Scaleflux logo](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/scaleflux-logo-190w-107h.svg)](https://www.scaleflux.com/)

[![Supermicro logo](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/Supermicro_GreenC_NewLogo_WhiteBackground.png)](https://www.supermicro.com/en/)

[![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/vast-logo-190w-107h.svg)](https://vastdata.com/)

[![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/weka-logo-190w-107h.svg)](https://www.weka.io/)

## Key Features of v1.14

The following features have been added in v1.14:

- Updated GDS user level stats to show P2PDMA stats
- Updated GDS kernel mode driver (nvidia-fs.ko) to support 6.12 kernel
- Added Get/Put API support for GDS Parameters, enabling read/write access for size\_t, bool, and string types.
- Assorted bug fixes

## Software Download

**GPUDirect Storage v1.14 Release**

NVIDIA Magnum IO GPUDirect® Storage (GDS) is now part of CUDA.   
See [https://docs.nvidia.com/gpudirect-storage/index.html](https://docs.nvidia.com/gpudirect-storage/index.html) for more information.

 GDS is currently supported on Linux x86-64 distributions; it is not supported on Windows. When choosing which CUDA packages to download, please select Linux first followed by x86-64 then either RHEL or Ubuntu distributions along with the desired packaging format(s).
  
[Download](/cuda-downloads)

## Resources

- [Read the blog: Accelerating IO in the modern data center - magnum IO storage partnerships](/blog/accelerating-io-in-the-modern-data-center-magnum-io-storage-partnerships/)
- [NVIDIA Magnum IO™ SDK](https://developer.nvidia.com/magnum-io)
- [Read the blog: Optimizing data movement in GPU applications with the NVIDIA Magnum IO developer environment](https://developer.nvidia.com/blog/optimizing-data-movement-in-gpu-apps-with-magnum-io-developer-environment/)
- [Read the blog: accelerating IO in the modern data center: Magnum IO Architecture](https://developer.nvidia.com/blog/accelerating-io-in-the-modern-data-center-magnum-io-architecture)
- [Watch the webinar: NVIDIA GPUDirect Storage: Accelerating the data path to the GPU](https://info.nvidia.com/gpudirect-storage-webinar-reg-page.html?ondemandrgt=yes)
- [NVIDIA-Certified Systems configuration guide](https://docs.nvidia.com/ngc/ngc-deploy-on-premises/nvidia-certified-configuration-guide/index.html)
- [NVIDIA-Certified Systems](https://www.nvidia.com/en-us/data-center/products/certified-systems/)
- Contact us at [gpudirectstorageext@nvidia.com](mailto:gpudirectstorageext@nvidia.com)


