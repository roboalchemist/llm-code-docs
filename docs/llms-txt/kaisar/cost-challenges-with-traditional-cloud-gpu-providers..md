# Source: https://docs.kaisar.io/kaisar-network/origins/challenges/cost-challenges-with-traditional-cloud-gpu-providers..md

# Cost challenges with traditional cloud GPU providers.

The cost challenges associated with cloud GPU providers is highlighted by [Splunk](https://www.splunk.com/en_us/blog/learn/cloud-cost-trends.html) where the demand for GPUs, especially for training large AI models, has surged, leading to capacity constraints. Instances where multiple users require a large number of GPUs simultaneously can lead to contention and underutilization, driving up costs as cloud providers struggle to balance supply and demand efficiently.&#x20;

Other prominent reasons for cost challenges are:&#x20;

* Hidden costs such as egress fees also contribute significantly to the overall expense, often catching businesses by surprise (Source:[Splunk](https://www.splunk.com/en_us/blog/learn/cloud-cost-trends.html)).
* The methods for deploying GPU resources in the cloud, such as pass-through can be wasteful for smaller applications. GPU virtualization.(Source: [SpringerLink](https://link.springer.com/article/10.1007/s00170-023-11252-0)).
* Use of advanced technologies in AI models has introduced new costs in compute. While these technologies improve the performance of AI models they still require significant investment in infrastructure.(Source: [ar5iv](https://ar5iv.org/pdf/2401.12230)).

The plot from [ar5iv](https://ar5iv.org/pdf/2401.12230) below shows how the number of GPUs provisioned scales with the fluctuating request rate over time. As the request rate increases or decreases, the number of GPUs provisioned also adjusts accordingly to match the demand, demonstrating elastic resource scheduling.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeWBvB1Z0HKEyiofCTEeU2sYs-GC2YhP8kmtrg9yX4b8vhzzm5Yy05pP_eNX5m--y4O9qLtRFCcN2W_9Dn1LX2TDVWFJ63cNz1ApKg21x3Dw8AXEhjhr950i4XQwoGgomA3q0KHKDneCfOPrbXoMzewNtfd?key=UbI8YI3-VF8UhldN54mDkg" alt=""><figcaption></figcaption></figure>
