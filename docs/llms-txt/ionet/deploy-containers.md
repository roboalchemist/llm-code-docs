# Source: https://io.net/docs/guides/clouds/deploy-containers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy CaaS

> Flexible & High-Performance Containers built for rapid deployment and scalable AI workloads

[io.net](http://io.net) offers a simple and powerful interface for deploying containers using high-performance infrastructure. Whether you are running inference, training models, or hosting APIs, the Containers system gives you flexibility and speed.

This guide will help you deploy using IO Cloud API keys on our CaaS clusters. For detailed API usage, refer to our [API Reference](/reference/get-started-with-caas-api).

<Note>
  Support for *AWS ECR* private images is not available at this time for **CaaS**.
</Note>

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/IZ7qjUFucdo" title="Start Using IO Cloud: Your First Steps Explained" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

## Deploy Container

Click the **Deploy Container** button to launch a wizard that guides you through the deployment process.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3516c8afcbb503d277926a87fd0571cdbb71614ebecd0f96d7ca551c007699db-Containers1.jpg?fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=d18cab212c7adc0377160b4ee96ee21c" alt={true} height="300" className="mx-auto" style={{ width:"60%" }} data-og-width="1082" data-og-height="1288" data-path="images/docs/3516c8afcbb503d277926a87fd0571cdbb71614ebecd0f96d7ca551c007699db-Containers1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3516c8afcbb503d277926a87fd0571cdbb71614ebecd0f96d7ca551c007699db-Containers1.jpg?w=280&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=c27cf64115ced5ed6045d9ca4a8a7f96 280w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3516c8afcbb503d277926a87fd0571cdbb71614ebecd0f96d7ca551c007699db-Containers1.jpg?w=560&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=c70a4175d3e2592fd5dba1bd5783031b 560w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3516c8afcbb503d277926a87fd0571cdbb71614ebecd0f96d7ca551c007699db-Containers1.jpg?w=840&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=9051c73bb760ca95ef1cc3d64d57e77b 840w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3516c8afcbb503d277926a87fd0571cdbb71614ebecd0f96d7ca551c007699db-Containers1.jpg?w=1100&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=0c36cc723f2770f831bb59dd76c7e7d6 1100w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3516c8afcbb503d277926a87fd0571cdbb71614ebecd0f96d7ca551c007699db-Containers1.jpg?w=1650&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=fb2447b81bd31c5865260ee5492f4aa7 1650w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3516c8afcbb503d277926a87fd0571cdbb71614ebecd0f96d7ca551c007699db-Containers1.jpg?w=2500&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=d049f47dac561e2f917bcca722723189 2500w" />
</Frame>

## Container Deployment Wizard

### Step 1: Basic Deployment Settings

Configure your container:

* **Container Image** *(required)* Example: `myorg/myimage:latest`
* **Image Type**
  * Public Image
  * Private Image
* **Start Command** Enter the start command in JSON array format, example:

  <CodeGroup>
    ```json json theme={null}
    ["python3","-m","vllm.entrypoints.openai.api_server","--model"]
    ```
  </CodeGroup>
* **Traffic Port** *(required)* Default: `8000`
* **Environment Variables** Click **Add Variable** to define key-value pairs. Options:
  * Normal Variable
  * Private Variable You can add or remove variables as needed.

Once all required fields are completed, click **Next Step**.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/32a23e67af9f05a46df9f0f99498ac37b4f3dd415c94c99333f51cb3b6b179b4-Containers2.jpg?fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=ba859211275b5d884f3996da0febff69" alt="" className="mx-auto" style={{ width:"71%" }} data-og-width="1082" width="1082" data-og-height="1070" height="1070" data-path="images/docs/32a23e67af9f05a46df9f0f99498ac37b4f3dd415c94c99333f51cb3b6b179b4-Containers2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/32a23e67af9f05a46df9f0f99498ac37b4f3dd415c94c99333f51cb3b6b179b4-Containers2.jpg?w=280&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=bf69fc192828253c9b652a3c4085b55c 280w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/32a23e67af9f05a46df9f0f99498ac37b4f3dd415c94c99333f51cb3b6b179b4-Containers2.jpg?w=560&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=69549e9576fb612b1853e15837fd747a 560w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/32a23e67af9f05a46df9f0f99498ac37b4f3dd415c94c99333f51cb3b6b179b4-Containers2.jpg?w=840&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=2444e2dd3a92dd6ae3f3f6596bef7f55 840w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/32a23e67af9f05a46df9f0f99498ac37b4f3dd415c94c99333f51cb3b6b179b4-Containers2.jpg?w=1100&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=16c29ce7edd576d524acec03dbdb920d 1100w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/32a23e67af9f05a46df9f0f99498ac37b4f3dd415c94c99333f51cb3b6b179b4-Containers2.jpg?w=1650&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=eac8d1a8b4bf967f31607d34ec4dff75 1650w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/32a23e67af9f05a46df9f0f99498ac37b4f3dd415c94c99333f51cb3b6b179b4-Containers2.jpg?w=2500&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=7b1bc512254149cdc82c491dddf23029 2500w" />
</Frame>

<Accordion title="Using Environment Variables in Entrypoints" icon="warning" iconType="duotone">
  To avoid deployment failures:

  * Always define environment variables in the `env_variables` section.
  * Do not substitute variables directly in the `entrypoint` or `args`.
  * When referencing variables in the entrypoint, **escape**`$`**as**   `$$`.

  Example:

  ```json  theme={null}
  "entrypoint": [
    "sh", "-c", "echo 'Variable value: $${TEST_VAR}' && sleep 3600"
  ],
  "env_variables": {
    "TEST_VAR": "This is a test"
  }
  ```

  * **Correct:** `$${TEST_VAR}` prints the variable value inside the container.
  * **Incorrect:** `$TEST_VAR` may cause deployment failure.
  * Always use `env_variables` for variable management.

  <Note>
    For advanced users: There is a known issue where Terraform variable interpolation (`$`) may conflict with service-layer substitution. Escaping with `$$` resolves this issue.
  </Note>
</Accordion>

### Step 2: Select Your Cluster Processor + Location

Choose the hardware and region for your deployment:

* **Available GPUs** Search by GPU model and view:
  * GPU Model
  * GPUs per Container
* **Location Selection** After selecting a GPU, you'll see a list of locations showing:
  * Region (e.g. Canada, Germany)
  * Available containers per location

Once both **GPU** and **location** are selected, proceed to the **next step**.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/fada87435d94daccfcaaa05513b5f3dc7e9a834e4a70ebb005bf2847734aed5f-Containers3.jpg?fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=f1e941915a52bc36262d868a761aab73" alt="" className="mx-auto" style={{ width:"65%" }} data-og-width="1090" width="1090" data-og-height="786" height="786" data-path="images/docs/fada87435d94daccfcaaa05513b5f3dc7e9a834e4a70ebb005bf2847734aed5f-Containers3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/fada87435d94daccfcaaa05513b5f3dc7e9a834e4a70ebb005bf2847734aed5f-Containers3.jpg?w=280&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=96b9e875bbb17f5a904e06e5704db86a 280w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/fada87435d94daccfcaaa05513b5f3dc7e9a834e4a70ebb005bf2847734aed5f-Containers3.jpg?w=560&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=52163564f16253aa66ab0c706155de7f 560w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/fada87435d94daccfcaaa05513b5f3dc7e9a834e4a70ebb005bf2847734aed5f-Containers3.jpg?w=840&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=aa34f013a24a9807bd61c1557d14ab31 840w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/fada87435d94daccfcaaa05513b5f3dc7e9a834e4a70ebb005bf2847734aed5f-Containers3.jpg?w=1100&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=84b31c99b2d6fbd312fa049968a5fb36 1100w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/fada87435d94daccfcaaa05513b5f3dc7e9a834e4a70ebb005bf2847734aed5f-Containers3.jpg?w=1650&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=1b4df394e2424dbb0993c3abe679131e 1650w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/fada87435d94daccfcaaa05513b5f3dc7e9a834e4a70ebb005bf2847734aed5f-Containers3.jpg?w=2500&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=8dfa9197faf9e4889319b95ac7fe98b0 2500w" />
</Frame>

### Step 3: Summary

On the Summary page, the choices you made in the process are displayed. You must select the number of Containers and the duration of time that you will use them.

1. In the **No. of Containers** field, select the number of Containers in the dropdown. 2 Containers will increase the cost.
2. In the **Enter Duration** field, select the length of time: Hourly, Daily, or Weekly. To the right, you can increase the quantity.
3. Review all the details of your cluster, including the **Total Cost**.
4. Click **Deploy Cluster**.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f3057dcfd2153e35cc6333fa037c8e21fd14cba6f8b856c4890ed889652ffceb-Containers4.jpg?fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=bde26634ae3614bdc9cb4c117d12c74b" alt="" className="mx-auto" style={{ width:"63%" }} data-og-width="1082" width="1082" data-og-height="2260" height="2260" data-path="images/docs/f3057dcfd2153e35cc6333fa037c8e21fd14cba6f8b856c4890ed889652ffceb-Containers4.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f3057dcfd2153e35cc6333fa037c8e21fd14cba6f8b856c4890ed889652ffceb-Containers4.jpg?w=280&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=9ea22dffe2f275ade57d2abcc5484451 280w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f3057dcfd2153e35cc6333fa037c8e21fd14cba6f8b856c4890ed889652ffceb-Containers4.jpg?w=560&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=08ca37373bffddc2e1179beac7bdd595 560w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f3057dcfd2153e35cc6333fa037c8e21fd14cba6f8b856c4890ed889652ffceb-Containers4.jpg?w=840&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=23617c60b5f6efca35f51bc1934e6736 840w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f3057dcfd2153e35cc6333fa037c8e21fd14cba6f8b856c4890ed889652ffceb-Containers4.jpg?w=1100&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=dbfb01e5d76ebc298f8640b2b3051744 1100w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f3057dcfd2153e35cc6333fa037c8e21fd14cba6f8b856c4890ed889652ffceb-Containers4.jpg?w=1650&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=32627d4a5054721ba7bd9d0af78e4bd9 1650w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f3057dcfd2153e35cc6333fa037c8e21fd14cba6f8b856c4890ed889652ffceb-Containers4.jpg?w=2500&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=34fe343444c59b5ab099ecabcfc2685c 2500w" />
</Frame>

### View Cluster

After payment is processed you can view your cluster loading.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/b30fc8f-Cluster_load.png?fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=06a1fa498f6a29f8a077ca73463074bd" alt="" data-og-width="2450" width="2450" data-og-height="722" height="722" data-path="images/docs/b30fc8f-Cluster_load.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/b30fc8f-Cluster_load.png?w=280&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=a81e774f485379b2711442eea27d2fef 280w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/b30fc8f-Cluster_load.png?w=560&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=561a70f206152f6a4d1604ec8b23a974 560w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/b30fc8f-Cluster_load.png?w=840&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=fb7242da3ba926b9142d91f385abbc04 840w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/b30fc8f-Cluster_load.png?w=1100&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=2229a7df82e0f4667666a337135adccb 1100w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/b30fc8f-Cluster_load.png?w=1650&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=24968062e0fefa99d3ba656ba8f88200 1650w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/b30fc8f-Cluster_load.png?w=2500&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=5f117d547157e58ad342340d6643a0c4 2500w" />
</Frame>

Click **Return to Clusters** after your cluster is successfully deployed. The screenshot below is a detail page of your cluster.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/81a933f12f6aceaf4230ec194f9c0eeb9b268d910ba86d03801bfb4c4fceefc7-Bitmap.jpg?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=09cb568a0e4c94406ae43175ff74fbb3" alt="" data-og-width="2171" width="2171" data-og-height="1190" height="1190" data-path="images/docs/81a933f12f6aceaf4230ec194f9c0eeb9b268d910ba86d03801bfb4c4fceefc7-Bitmap.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/81a933f12f6aceaf4230ec194f9c0eeb9b268d910ba86d03801bfb4c4fceefc7-Bitmap.jpg?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=dcdb273aeb1339425c2764f85e8f22c6 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/81a933f12f6aceaf4230ec194f9c0eeb9b268d910ba86d03801bfb4c4fceefc7-Bitmap.jpg?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=81da45675eed915062718280a0504236 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/81a933f12f6aceaf4230ec194f9c0eeb9b268d910ba86d03801bfb4c4fceefc7-Bitmap.jpg?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=d15bee326549d43e1c35381eb3a699c1 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/81a933f12f6aceaf4230ec194f9c0eeb9b268d910ba86d03801bfb4c4fceefc7-Bitmap.jpg?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=ddca3f1fff1b7ba46b244d8a15cfb197 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/81a933f12f6aceaf4230ec194f9c0eeb9b268d910ba86d03801bfb4c4fceefc7-Bitmap.jpg?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=c10a0946978f600e4f69c5879fa616e7 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/81a933f12f6aceaf4230ec194f9c0eeb9b268d910ba86d03801bfb4c4fceefc7-Bitmap.jpg?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=997d67ff7c8071da10f09a69a23e0468 2500w" />
</Frame>

> 🚧 Troubleshooting Container Issues
>
> If your container is not running, you do not need to delete the whole cluster. Instead, open the deployment settings, adjust any incorrect details (for example, the image name or registry credentials), and redeploy.
>
> This way, you avoid the minimum 1-hour charge for deleting and recreating a cluster.
>
> <img src="https://mintcdn.com/ionet-cca8037f/npZLUBS1u-f2Rolg/images/docs/cloud_caas/Containers9.jpg?fit=max&auto=format&n=npZLUBS1u-f2Rolg&q=85&s=4f14e2dc68ed187a021d0a33d7cbe16b" alt="Containers9 Jp" className="mx-auto" style={{ width:"87%" }} data-og-width="968" width="968" data-og-height="122" height="122" data-path="images/docs/cloud_caas/Containers9.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/npZLUBS1u-f2Rolg/images/docs/cloud_caas/Containers9.jpg?w=280&fit=max&auto=format&n=npZLUBS1u-f2Rolg&q=85&s=917d48f2c2c1b4c67389b542e4abe96d 280w, https://mintcdn.com/ionet-cca8037f/npZLUBS1u-f2Rolg/images/docs/cloud_caas/Containers9.jpg?w=560&fit=max&auto=format&n=npZLUBS1u-f2Rolg&q=85&s=e68a413cbd936ee813363192e450aa3f 560w, https://mintcdn.com/ionet-cca8037f/npZLUBS1u-f2Rolg/images/docs/cloud_caas/Containers9.jpg?w=840&fit=max&auto=format&n=npZLUBS1u-f2Rolg&q=85&s=6c06ac23808101c88356da115b05c996 840w, https://mintcdn.com/ionet-cca8037f/npZLUBS1u-f2Rolg/images/docs/cloud_caas/Containers9.jpg?w=1100&fit=max&auto=format&n=npZLUBS1u-f2Rolg&q=85&s=98868b3023531aa1b08cd64c181c9aa4 1100w, https://mintcdn.com/ionet-cca8037f/npZLUBS1u-f2Rolg/images/docs/cloud_caas/Containers9.jpg?w=1650&fit=max&auto=format&n=npZLUBS1u-f2Rolg&q=85&s=332058e93752aa247c43d9e1ec19e2ef 1650w, https://mintcdn.com/ionet-cca8037f/npZLUBS1u-f2Rolg/images/docs/cloud_caas/Containers9.jpg?w=2500&fit=max&auto=format&n=npZLUBS1u-f2Rolg&q=85&s=1bdbb5cb5f18c16be7dba02f9645f5fb 2500w" />
