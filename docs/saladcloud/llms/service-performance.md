# Source: https://docs.salad.com/container-engine/explanation/core-concepts/service-performance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Service Performance and Reliability Overview

> To develop high-performance, reliable applications on SaladCloud

*Last Updated: Oct 2, 2025*

SaladCloud consists of tens of thousands of globally distributed nodes, primarily high-performance desktop computers and
servers running the SaladCloud agent. Each node is equipped with either consumer-grade or data center GPUs, along with
varying CPU and memory configurations. Node distribution is uneven across regions and countries: consumer GPU nodes in
the US and Canada account for 50–60% of the total, while nearly all data center GPU nodes are currently located in the
US.

When these devices are idle, SaladCloud leverages them to run workloads by dynamically pulling and executing container
images. Once a container group is stopped, the image and any associated runtime data are removed from the allocated
nodes, which are then released.

Due to its distributed architecture, nodes can vary in distance, latency, network throughput to specific endpoints,
startup times, uptimes, and processing capabilities—factors that should be carefully considered when designing
applications on SaladCloud.

## Startup Times

When a container group starts, its image is first pulled from your registry into SaladCloud’s internal caches in Europe
and the US (only once), and then distributed to the allocated nodes.

Startup times can range from a few minutes to longer, depending on image size and network conditions. Instances on nodes
located closer to a cache or with higher throughput typically come online faster. You can further improve startup speed
by using smaller images to reduce transfer and decompression time, and by deploying workloads in regions closer to the
EU or US.

[Our 2025 test](https://github.com/SaladTechnologies/performance-reliability-test-2025/) measured the startup times for
100 container instances at high-priority across all consumer GPU types and regions, using a 5.53 GB image. This metric
tracks the number of instances that became operational since startup:

<img src="https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp1.png?fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=7ae401ce2253d7e7c00d0ccf560fa1cd" data-og-width="2894" width="2894" data-og-height="1140" height="1140" data-path="container-engine/images/sp1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp1.png?w=280&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=8074af6aa5a73458cf8fd7921206035d 280w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp1.png?w=560&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=e49346c7d0c885ece0a29849852534ba 560w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp1.png?w=840&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=bca919d274fb4a2f76bdd8c725ea37bc 840w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp1.png?w=1100&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=db39a621b3dc055ad26419ad93ebe661 1100w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp1.png?w=1650&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=2717436e4b183f13c529f3dc0487080a 1650w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp1.png?w=2500&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=ad23d2b6b0990a0b0d2c1c39ba79e02a 2500w" />

Key observations are:

* Instances began coming online and reporting results within `3 minutes` of the test start.
* `50% of instances` came online by `10 minutes`, `80%` by `20 minutes` and `90%` by `40 minutes`.
* The count of online instances then briefly dropped by one, indicating one instance was just reallocated.
* By around `80 minutes`, nearly all 100 instances were online, with minor fluctuations afterward due to reallocations.

**SaladCloud’s data center nodes are typically deployed near the Internet backbone and offer higher bandwidth and
processing capacity, enabling faster startup.**

## Interruptions and Reallocations

An instance may go offline after coming online for several reasons. In such cases, a new instance is allocated to
continue processing:

* **Voluntary Interruptions**: Node owners (individuals or data center providers) may temporarily reclaim their
  resources for their own use, pausing sharing. However, high-priority workloads that run reliably over long periods
  generate higher earnings, giving owners less incentive to interrupt.

* **External Interruptions**: Factors such as power outages, network issues, or hardware failures can also take nodes
  offline.

* **Proactive Reallocations**: During periods of high demand, SaladCloud may reassign resources from lower-priority
  workloads to higher-priority ones. Applications can also trigger reallocation via IMDS Reallocate API if current
  instances fail to meet requirements.

The same 2025 test also tracked interruptions and reallocations for the 100 container instances over a 7-day period. To
avoid the effects of initial allocations, the first two hours after startup were excluded. The hourly and daily
reallocation results are shown below:

<img src="https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp11.png?fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=74dd579584dfc760b0e72c1906fffee5" data-og-width="2688" width="2688" data-og-height="892" height="892" data-path="container-engine/images/sp11.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp11.png?w=280&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=52a49c7ad39a8f975af186636e00be93 280w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp11.png?w=560&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=b9bac5d496bcb7a90933924f3616b472 560w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp11.png?w=840&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=2dca307cfa4964f13759ab6f0b5b9c05 840w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp11.png?w=1100&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=84f4a47b046dcb1d8d9ae820aad2c1ed 1100w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp11.png?w=1650&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=862dfcab9fd15370d6c965f74d0f727e 1650w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp11.png?w=2500&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=e3057172b72fe245751c08c5abb54fa2 2500w" />

<img src="https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp12.png?fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=7c9e4a4fb57658a9cf41143ce20090c9" data-og-width="2690" width="2690" data-og-height="890" height="890" data-path="container-engine/images/sp12.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp12.png?w=280&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=f596222f8b33c94fc48e18b32a3146d4 280w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp12.png?w=560&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=40fab765fadbd67d4ec2b07f78261660 560w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp12.png?w=840&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=07a620a478587d80229270fee8c2bbe4 840w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp12.png?w=1100&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=f36403856cb3cf8cddc57102c138a7a2 1100w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp12.png?w=1650&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=637bcdd1c7185c28cd4499adcc77004e 1650w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp12.png?w=2500&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=9e953fba656802e9d1dfb2a990f8d8cb 2500w" />

Key observations are:

* Maximum hourly reallocations: `6`
* Average hourly reallocations: `1.1 ( 182 reallocations over 168 hours )`
* Reallocations decreased over time, dropping from more than `45 per day` to fewer than `15 per day`, with some
  fluctuations along the way. **This trend shows that as applications run stably for longer periods on nodes, the
  likelihood of interruption by node owners decreases.**

**SaladCloud’s data center nodes are generally more stable when running workloads at high priority and are less likely
to be interrupted by their owners.**

## Uptimes

Additionally, the 2025 test measured the uptime distributions of instances over the same period, which are primarily
influenced by startup times and interruptions. The results show that:

<img src="https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp13.png?fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=4ad2678e28617b2a2187153e7611be4d" data-og-width="2688" width="2688" data-og-height="892" height="892" data-path="container-engine/images/sp13.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp13.png?w=280&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=84f67c0fe0a19a12270684a69acdd3d3 280w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp13.png?w=560&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=e5f466750733df88bc0c6d8ff37f6ab4 560w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp13.png?w=840&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=52f7c70bf43c9713051f8ed0ae6e955c 840w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp13.png?w=1100&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=dca6e138f6ae4fcc06040a6c05b9354c 1100w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp13.png?w=1650&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=c025638aae16c0e972b6e1edbd5dc3eb 1650w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp13.png?w=2500&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=41385f5b0d1dec4e32b65fa589f7eb9d 2500w" />

<img src="https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp14.png?fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=76022cefbbfa990e7a86a412de6ad1cc" data-og-width="2694" width="2694" data-og-height="894" height="894" data-path="container-engine/images/sp14.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp14.png?w=280&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=1cb685e335025eac54fcd3887b1bcf7c 280w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp14.png?w=560&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=99c857f095cdc7cd5eb091429dd17ae0 560w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp14.png?w=840&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=af772c24ef4ec79cb817c2b727cc3090 840w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp14.png?w=1100&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=82667d83f298160753a79ff794943bb6 1100w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp14.png?w=1650&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=26f2832eb76d36a18934e70ca91d020e 1650w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp14.png?w=2500&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=6dc156d8f0c41806199c3773f64929eb 2500w" />

Key observations are:

* 100 instances running over 7 days generated `282 samples` (instance runs).
* Before the container group was shut down, `182` instance runs had already completed (interrupted) while `100`
  instances were still running.
* `25` instances ran uninterrupted for full 7-day period.
* The average uptime across all instance runs (interrupted and uninterrupted) was `60 hours`.
* The average uptime of interrupted instance runs was `35 hours`.

**High-priority applications on SaladCloud’s data center nodes generally run uninterrupted for extended periods, though
this cannot be fully guaranteed.**

## Run-to-Request Ratio

The instance run-to-request ratio measures the actual compute capacity available compared to what is requested. For
example, if 100 instances are requested and 99 are running, the run-to-request ratio is 99%. When a node goes offline
and a replacement is allocated, additional time is required to download and decompress the image before the new instance
becomes operational. Because of variations in startup times and uptimes, a 100% run-to-request ratio cannot be
consistently guaranteed on SaladCloud’s consumer GPU nodes.

Large image sizes can increase startup times, which in turn lowers the run-to-request ratio. To mitigate this, it is
often necessary to provision additional instances (5\~10%) beyond the initial plan, particularly for real-time inference
workloads.

Results from the 2025 test show the instance run-to-request ratio over the 7-day period:

<img src="https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp15.png?fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=7c0133d2590ee863bfc113ddf3fcd968" data-og-width="2814" width="2814" data-og-height="1122" height="1122" data-path="container-engine/images/sp15.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp15.png?w=280&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=08f3239dd37b29185a63e6452af7669a 280w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp15.png?w=560&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=0d1b06d18c18cdade18b760e6aa395a2 560w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp15.png?w=840&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=f2fa89041529d9503fa91fe5f2feccf1 840w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp15.png?w=1100&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=b61ea7c3e14f96b2bb856cc91217d3d5 1100w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp15.png?w=1650&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=72895987b02411af5860c3836cf2b5f4 1650w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp15.png?w=2500&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=60a0a3f8577c3268d5733944f4b162e7 2500w" />

Key observations are:

* Lowest instance run-to-request ratio: `94%`
* Average instance run-to-request ratio: `more than 99%`
* The instance run-to-request ratio can `temporarily exceed 100%` from the application’s perspective. When nodes lose
  connection to SaladCloud (not charged in this case), applications may continue running briefly before the nodes are
  fully shut down. During this overlap, as new nodes are allocated and start running, the number of active instances can
  temporarily exceed the original request.

**SaladCloud’s data center nodes provide 8 GPUs per node. While these nodes are generally more stable and less likely to
be interrupted, any node going offline removes all 8 GPUs from the resource pool, so you should consider this impact
when deploying workloads.**

## Processing Performance

Nodes with the same consumer GPU type can exhibit different performance due to factors such as system configuration
(CPU, RAM), clock speed, cooling, and power limits. Even for the same node, performance may fluctuate over time because
of temperature changes and cooling efficiency.

Based on our tests, over 90% of SaladCloud’s consumer GPU nodes provide stable and consistent performance. Here is an
instance run from the 2025 test, illustrating stable performance (black line) and resource usage over the 7-day
execution period.

<img src="https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp16.png?fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=a97e800448b4642bbf2fdfaff1f08f83" data-og-width="2144" width="2144" data-og-height="1386" height="1386" data-path="container-engine/images/sp16.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp16.png?w=280&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=264cf1f0b9a67e50594d753a3b1ea668 280w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp16.png?w=560&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=eb2573bd65f91df3ac3d47a6a877c149 560w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp16.png?w=840&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=77df6a9512657afe27aee28d94b01b3b 840w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp16.png?w=1100&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=b0613c207a3bce5a92ca2363670ee828 1100w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp16.png?w=1650&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=f46f1c3817a6a48b997e2ba94ff4f789 1650w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp16.png?w=2500&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=47166e899641d7bd599b560a1d510a0c 2500w" />

Another instance run from the same test highlights performance fluctuations due to temperature changes: as GPU
temperatures increased, performance declined.

<img src="https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp17.png?fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=6d6ccbcbeeedf98c37d16ef5db2d3077" data-og-width="2142" width="2142" data-og-height="1390" height="1390" data-path="container-engine/images/sp17.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp17.png?w=280&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=80aee4228dc70bb3beb4ab22f71ae58a 280w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp17.png?w=560&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=39abdd635644bb869c58aae9423b0f5e 560w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp17.png?w=840&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=cde914c1e85cad88d16713128555c7f9 840w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp17.png?w=1100&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=4ae520a1dafb31cbc28b6300fbde89f7 1100w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp17.png?w=1650&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=618c1556331d012aefa000872f044a55 1650w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp17.png?w=2500&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=92fd4cf375d4d06773bfc3c2f90fc2de 2500w" />

To manage performance variances and fluctuations from a small number of consumer GPU nodes, we recommend conducting an
initial check and real-time performance monitoring to select suitable nodes and ensure they remain in an optimal state
for application execution. For more details, please refer to
[this guide](/container-engine/tutorials/performance/high-performance-apps#build-high-performance-applications).

**Based on our tests, SaladCloud’s data center nodes can always deliver stable and consistent performance.**

## Network Performance

Salad nodes with consumer GPUs often exhibit asymmetric bandwidth, as many operate on residential networks with high
download speeds—frequently hundreds of Mbps—but lower upload speeds, sometimes only tens of Mbps.

The 2025 test results, based on over 200 consumer GPU nodes performing upload and download tasks, reveal significant
speed variance and bandwidth asymmetry. Nevertheless, a substantial number of nodes still provide symmetric bandwidth
and strong overall performance.

<img src="https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp4.png?fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=de81d090fcbf67fdbcadbb1d436d3787" data-og-width="682" width="682" data-og-height="676" height="676" data-path="container-engine/images/sp4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp4.png?w=280&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=b83ce772bb7d529d9855969c704ce05f 280w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp4.png?w=560&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=308c23ab90a84220a06e36be7ca7ff97 560w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp4.png?w=840&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=e3bff3114a6a89a6460bef5e35143e82 840w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp4.png?w=1100&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=37acf3fd57142bf8b3481ff75652bed5 1100w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp4.png?w=1650&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=243e2eb443cba447915b68eeec88dbae 1650w, https://mintcdn.com/salad/iWPB8RRsH9OyCiWc/container-engine/images/sp4.png?w=2500&fit=max&auto=format&n=iWPB8RRsH9OyCiWc&q=85&s=55009668c5c79948cce929491e113fd5 2500w" />

**Most SaladCloud’s data center nodes offer symmetric bandwidth, delivering several gigabytes per second in both
directions.**

Round-trip time (RTT) is primarily determined by the geographical distance and underlying network latency between two
endpoints, and it plays a critical role in data transfer throughput. Since Salad nodes are globally distributed, nodes
with identical network speeds in different regions can exhibit varying throughput to a specific endpoint, such as a
cloud storage bucket in a particular location. Transfer tools and algorithms also matter—using chunked and parallel data
transfers can better utilize the available end-to-end bandwidth.

If your applications require higher throughput with lower latency, it is recommended to perform initial checks and apply
custom filters to select nodes that meet your specific network requirements and adopt advanced tools and algorithms .
Please check [this guide](/container-engine/tutorials/performance/high-performance-storage-solutions) for more
information.
