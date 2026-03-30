# Source: https://docs.salad.com/container-engine/explanation/container-groups/disk-space.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Disk Space

*Last Updated: October 15, 2024*

# How Disk Space is Calculated

When you deploy a workload to the SaladCloud Network, nodes are filtered on the criteria that you specify. If you do not
specify disk space requirements, nodes are provided which meet a minimum free space allotment. This is calculated based
on the size of the downloaded container, plus some extra buffer to account for operations like extracting the container,
installing dependencies, and caching results.

# Requesting additional Disk Space on nodes

If you expect to need significantly more free space on your nodes than your container itself requires, configure it by
selecting a Disk Space option when configuring your container group in the Portal or in the API by passing
a`"storage_amount": x` in megabytes on the resources object.

<img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-select-disk-space.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=31801e1c40530b3ae0d10ee912c07802" data-og-width="661" width="661" data-og-height="361" height="361" data-path="container-engine/images/portal-select-disk-space.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-select-disk-space.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=4e0e2adc4ac3d976ed2935df576110d0 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-select-disk-space.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=f5b2c6b1417e8def08274fb1ae46ed0e 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-select-disk-space.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=3b56fc92583cdd57f2793e3608bea532 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-select-disk-space.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=c69bab1ab9a89179434a56d592027c4c 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-select-disk-space.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=dadd5d2ff2f6cbb30c0b382f8e0a1b76 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-select-disk-space.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=3640f9a728c41487b8e83bbe9261fee5 2500w" />

> 📘 Need more space?
>
> SaladCloud's disk space requirements for nodes are minimum thresholds; nodes may provide significantly more free space
> than the minimum. However, if you expect to regularly need more than highest disk space option provided, reach out to
> your account manager or email [cloud@salad.com](mailto:cloud@salad.com) to request nodes with additional space. We can
> take a look at how many nodes are available with high levels of free space to help guide you to the right balance of
> space requirements and node counts.
