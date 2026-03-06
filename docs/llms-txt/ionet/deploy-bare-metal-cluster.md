# Source: https://io.net/docs/guides/clouds/deploy-bare-metal-cluster.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bare Metal (Self Serve) Moving Forward

> Bare Metal clusters give you direct access to hardware for maximum performance, low latency, high efficiency, and full control over configuration.

<Danger>
  ### Service Update: Bare Metal (Self Serve) Moving Forward

  Bare Metal on Demand will no longer be available starting Wednesday,  October 1, 2025.

  If you need Bare Metal, please contact our sales team at [business@io.net](mailto:business@io.net) for managed services.
</Danger>

The Bare Metal Automated Solution provides fast, self-service access to dedicated hardware resources, all of which eliminate delays from custom contracts and manual setup. This solution is ideal for high-performance workloads such as AI model training, making predictions (inferencing), and other compute-heavy tasks. Through an automated deployment flow, you can select and provision devices in minutes, while our real-time dashboard offers visibility into usage, performance metrics, and costs to optimize your deployments.

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/zv0JdhXfb0w" title="Deploying a Bare Metal Cluster on IO Cloud" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

<Info>
  Bare Metal On Demand clusters do not provide `sudo` or `root` access. Certain system-level operations requiring elevated privileges will not be possible. Please ensure your workloads and deployment requirements can operate within this restriction.
</Info>

### To deploy a Bare Metal On Demand Cluster:

1. From IO Cloud, next to **Bare Metal**, click **Request**.

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0fbcc44d953ba4178e1cb9a63503bdeef576eafd36fd3ddc5081b7b207d4ef4a-BareMetal1.jpg?fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=abdd7c56e867b6d764d07faf17d29283" alt="" className="mx-auto" style={{ width:"59%" }} data-og-width="1082" width="1082" data-og-height="1288" height="1288" data-path="images/docs/0fbcc44d953ba4178e1cb9a63503bdeef576eafd36fd3ddc5081b7b207d4ef4a-BareMetal1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0fbcc44d953ba4178e1cb9a63503bdeef576eafd36fd3ddc5081b7b207d4ef4a-BareMetal1.jpg?w=280&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=c9a4a27b7d410fc846d162e64e5cb547 280w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0fbcc44d953ba4178e1cb9a63503bdeef576eafd36fd3ddc5081b7b207d4ef4a-BareMetal1.jpg?w=560&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=51503fc3c1e08e5a93369c93a9d2b7ce 560w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0fbcc44d953ba4178e1cb9a63503bdeef576eafd36fd3ddc5081b7b207d4ef4a-BareMetal1.jpg?w=840&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=4ec8438571d80f2dc9dd4299db31e2ff 840w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0fbcc44d953ba4178e1cb9a63503bdeef576eafd36fd3ddc5081b7b207d4ef4a-BareMetal1.jpg?w=1100&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=6cb118933747f41ba7c8278dd09be95d 1100w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0fbcc44d953ba4178e1cb9a63503bdeef576eafd36fd3ddc5081b7b207d4ef4a-BareMetal1.jpg?w=1650&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=6dd27a9f0fa7a655a88a82d94261ffef 1650w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0fbcc44d953ba4178e1cb9a63503bdeef576eafd36fd3ddc5081b7b207d4ef4a-BareMetal1.jpg?w=2500&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=2a654006e20a999f930e653291593c83 2500w" />
   </Frame>
2. Select a location.

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/ddfb012168faf2274daf346dfdc31ea937c8c666854407b119c34298f03418b9-BareMetal2.jpg?fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=916a6342d1aaeaaf7e32ac7e99ac9bbd" alt="" className="mx-auto" style={{ width:"74%" }} data-og-width="1090" width="1090" data-og-height="676" height="676" data-path="images/docs/ddfb012168faf2274daf346dfdc31ea937c8c666854407b119c34298f03418b9-BareMetal2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/ddfb012168faf2274daf346dfdc31ea937c8c666854407b119c34298f03418b9-BareMetal2.jpg?w=280&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=789017c5836f3438f61f9eb1254a9f38 280w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/ddfb012168faf2274daf346dfdc31ea937c8c666854407b119c34298f03418b9-BareMetal2.jpg?w=560&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=6c7edd0f851e443ff6235eaf8bd52407 560w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/ddfb012168faf2274daf346dfdc31ea937c8c666854407b119c34298f03418b9-BareMetal2.jpg?w=840&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=7272b8565de84fcdd2ca55b822659458 840w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/ddfb012168faf2274daf346dfdc31ea937c8c666854407b119c34298f03418b9-BareMetal2.jpg?w=1100&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=5e66cce5af341b02b5174911972037d9 1100w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/ddfb012168faf2274daf346dfdc31ea937c8c666854407b119c34298f03418b9-BareMetal2.jpg?w=1650&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=05abac2002e8a5e32137cad66808c101 1650w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/ddfb012168faf2274daf346dfdc31ea937c8c666854407b119c34298f03418b9-BareMetal2.jpg?w=2500&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=016f3276ca15b795d5acdbd0315f9af5 2500w" />
   </Frame>
3. Select your Connectivity Tier.

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b67f868af99101df819bffde3ae8e381c96b3b887d9e90c87486a309277e97ed-BareMetal3.jpg?fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=4325d0073afddb0a446365b3606bd91e" alt="" className="mx-auto" style={{ width:"93%" }} data-og-width="1090" width="1090" data-og-height="560" height="560" data-path="images/docs/b67f868af99101df819bffde3ae8e381c96b3b887d9e90c87486a309277e97ed-BareMetal3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b67f868af99101df819bffde3ae8e381c96b3b887d9e90c87486a309277e97ed-BareMetal3.jpg?w=280&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=2e8e3b0d93b119a23c9c298c45e5aa77 280w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b67f868af99101df819bffde3ae8e381c96b3b887d9e90c87486a309277e97ed-BareMetal3.jpg?w=560&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=fc3b33ae5ba1dcfc8852e93a27d69bb8 560w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b67f868af99101df819bffde3ae8e381c96b3b887d9e90c87486a309277e97ed-BareMetal3.jpg?w=840&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=b1a1842c8841bbb540d6c151432967ba 840w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b67f868af99101df819bffde3ae8e381c96b3b887d9e90c87486a309277e97ed-BareMetal3.jpg?w=1100&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=d9c0fe7fe2549c195577dcbc8f3689f3 1100w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b67f868af99101df819bffde3ae8e381c96b3b887d9e90c87486a309277e97ed-BareMetal3.jpg?w=1650&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=a2b6513f755ff86e1ecd885ad612ec09 1650w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b67f868af99101df819bffde3ae8e381c96b3b887d9e90c87486a309277e97ed-BareMetal3.jpg?w=2500&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=2b22db1b1f346d661b5c157aaff788c7 2500w" />
   </Frame>
4. Select your processor.

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1b7faaf1f966d85f915abc5b27e469d61b99e0cfd1f5a903e0f7b1291bfb26b8-BareMetal4.jpg?fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=711375a0c2ca18c802c96adde3ecbc67" alt="" className="mx-auto" style={{ width:"77%" }} data-og-width="1090" width="1090" data-og-height="554" height="554" data-path="images/docs/1b7faaf1f966d85f915abc5b27e469d61b99e0cfd1f5a903e0f7b1291bfb26b8-BareMetal4.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1b7faaf1f966d85f915abc5b27e469d61b99e0cfd1f5a903e0f7b1291bfb26b8-BareMetal4.jpg?w=280&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=5e46f9dff87a0b6f750ff7b5ff1097db 280w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1b7faaf1f966d85f915abc5b27e469d61b99e0cfd1f5a903e0f7b1291bfb26b8-BareMetal4.jpg?w=560&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=812e29c74ffee9eabea8b4b9bcbc7da4 560w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1b7faaf1f966d85f915abc5b27e469d61b99e0cfd1f5a903e0f7b1291bfb26b8-BareMetal4.jpg?w=840&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=6dae799d6f93be0cd7f7bf7759f17077 840w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1b7faaf1f966d85f915abc5b27e469d61b99e0cfd1f5a903e0f7b1291bfb26b8-BareMetal4.jpg?w=1100&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=30af6ed441be32f4c73c005b7768bef6 1100w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1b7faaf1f966d85f915abc5b27e469d61b99e0cfd1f5a903e0f7b1291bfb26b8-BareMetal4.jpg?w=1650&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=605a0ebeab774c1be7ae8a20634936fd 1650w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1b7faaf1f966d85f915abc5b27e469d61b99e0cfd1f5a903e0f7b1291bfb26b8-BareMetal4.jpg?w=2500&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=470984bceab30fdf8d4546ce1ed49b90 2500w" />
   </Frame>
5. Before submitting your request, you can view a summary of all details of your bare metal solution, including the duration and pricing.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e6d02d6d693a8575196223ba1975dd182b7e4184543d8799fbda8536a38d2ba4-BareMetal5.jpg?fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=7c018de6b78fcfccd7ac1c92bfecce22" alt="" className="mx-auto" style={{ width:"73%" }} data-og-width="1090" width="1090" data-og-height="1704" height="1704" data-path="images/docs/e6d02d6d693a8575196223ba1975dd182b7e4184543d8799fbda8536a38d2ba4-BareMetal5.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e6d02d6d693a8575196223ba1975dd182b7e4184543d8799fbda8536a38d2ba4-BareMetal5.jpg?w=280&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=a79ff30a262d993ef09c32e5ba143819 280w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e6d02d6d693a8575196223ba1975dd182b7e4184543d8799fbda8536a38d2ba4-BareMetal5.jpg?w=560&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=65dc055b6fba855c481811feee8fabfe 560w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e6d02d6d693a8575196223ba1975dd182b7e4184543d8799fbda8536a38d2ba4-BareMetal5.jpg?w=840&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=5550b45179b05ab92fa3c29b84cddd11 840w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e6d02d6d693a8575196223ba1975dd182b7e4184543d8799fbda8536a38d2ba4-BareMetal5.jpg?w=1100&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=f03131c597fda66d7850719f830aa903 1100w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e6d02d6d693a8575196223ba1975dd182b7e4184543d8799fbda8536a38d2ba4-BareMetal5.jpg?w=1650&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=c7395d82163cdab0b4ed9a85a237d623 1650w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e6d02d6d693a8575196223ba1975dd182b7e4184543d8799fbda8536a38d2ba4-BareMetal5.jpg?w=2500&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=48b53f1973ce5ed2cb23ccf7dea91c38 2500w" />
</Frame>

### Bare Metal Dashboard

Our real-time dashboard provides the following insights to help you track and optimize your deployments:

|                     |                                                                                                                  |
| ------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Device Inventory    | View active, idle, and available devices in your cluster.                                                        |
| Performance Metrics | Track CPU, memory, and GPU utilization for each device, enabling real-time monitoring and adjustments.           |
| Usage Tracking      | View historical and current device usage data to understand and optimize resource allocation.                    |
| Pricing Information | Real-time cost breakdowns help you manage budget and understand the impact of each device on your overall spend. |
| Revenue Insights    | For multi-tenancy or resale scenarios, monitor revenue generated by specific devices and clusters.               |

<Info>
  At the end of your rental period, we securely wipe and restore each Bare Metal device to its original state. We adhere to strict data security protocols to prevent unauthorized access and maintain compliance with industry standards throughout the device lifecycle.
</Info>
