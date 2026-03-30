# Source: https://docs.salad.com/container-engine/how-to-guides/ai-machine-learning/run-hugging-face-models-with-ollama.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run Hugging Face Models with Ollama (45,000 models)

> Use Ollama with any GGUF Model on Hugging Face Hub on SaladCloud.

*Last Updated: October 24, 2024*

## Introduction to Ollama

Ollama, built on the llama.cpp framework, now seamlessly integrates with a vast collection of GGUF format language
models available on Hugging Face. With over 45,000 public GGUF checkpoints, users can effortlessly run any of these
models on SaladCloud with minimal setup. This integration offers flexibility in selecting models, customizing
quantization schemes, and other options, making it one of the simplest and most efficient ways to deploy and use
language models.

## Run any Hugging Face Model with Ollama on SaladCloud

You can deploy any Hugging Face LLM model with Ollama on SaladCloud by passing the model as an environment variable
during deployment. Pick the model you want here:
[HF models](https://huggingface.co/models?pipeline_tag=text-generation\&library=gguf\&sort=trending) The environment
variable MODEL should follow the format below, allowing you to specify the model from Hugging Face, including optional
quantization settings:

```bash  theme={null}
hf.co/{username}/{repository}:{quantization}
```

### Here are example of models you can try:

```bash  theme={null}
MODEL hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF
MODEL hf.co/mlabonne/Meta-Llama-3.1-8B-Instruct-abliterated-GGUF
MODEL hf.co/bartowski/Llama-3.1-Nemotron-70B-Instruct-HF-GGUF

```

## Custom Quantization

By default, Ollama uses the Q4\_K\_M quantization scheme if it's available in the model repository. You can manually
select a quantization scheme by specifying it in the MODEL environment variable. To find quantization options open
model's Hugging Face page and choose ollama from "Use this model" dropdown. For example:

<img src="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-8.png?fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=38bc63c1ded83157185489049ab4e163" data-og-width="1677" width="1677" data-og-height="484" height="484" data-path="container-engine/images/ollama-hf-8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-8.png?w=280&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=930987db5e6c2de275729814f1a8b9a9 280w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-8.png?w=560&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=77ef2a374bb3fec643205b61988e59e1 560w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-8.png?w=840&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=02a0f24fc8745e9f50e71976b29ac773 840w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-8.png?w=1100&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=83ae2edd470643d5b650c5034ea9230d 1100w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-8.png?w=1650&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=d605a73c53676b9579de7b7e615d1ec1 1650w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-8.png?w=2500&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=16cd1a0e08efbf1e13b8f1e2d1daf78f 2500w" />

and choose the quantization you want:

<img src="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-9.png?fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=dbddde8fff487cb7fe95b081450f8926" data-og-width="924" width="924" data-og-height="658" height="658" data-path="container-engine/images/ollama-hf-9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-9.png?w=280&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=d8fbb4c98f3a228dd8c7f6f89ec1e150 280w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-9.png?w=560&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=00e6b9f0541db19bad49d55b7945b081 560w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-9.png?w=840&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=f0daadd1ebcdfbbbe7e0ada4edffa69a 840w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-9.png?w=1100&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=3aeebf722ccecd4d33703e41d46e3b52 1100w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-9.png?w=1650&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=8990bc6bfe6971dab90be73391b0d1bc 1650w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-9.png?w=2500&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=39edd64463288505700126bf8e91fd06 2500w" />

To specify a custom quantization, follow this format:

```bash  theme={null}
MODEL hf.co/{username}/{repository}:{quantization}
```

### Example with Custom Quantization:

```bash  theme={null}
MODEL hf.co/bartowski/Llama-3.1-Nemotron-70B-Instruct-HF-GGUF:IQ2_XS
```

## Deploying Hugging Face Models with Ollama on Salad Cloud

To run Hugging Face models on Salad Cloud using Ollama, follow one of these deployment options:

### Option 1: Fastest Way (Pre-built Recipe)

We have a pre-built recipe for deploying Llama3.1 with Ollama on SaladCloud. This recipe can also be used to run any
additional model from Hugging Face. As a result you will have both Llama 3.1 and model of your choice. Full
configuration takes less than a minute.

1. Click **Deploy a Container Group** and choose the **Ollama Llama 3.1** recipe.

<img src="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-1.png?fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=79cc889e05167ad9622f11012f2382b5" data-og-width="1608" width="1608" data-og-height="824" height="824" data-path="container-engine/images/ollama-hf-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-1.png?w=280&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=ca89c634cdeaafc15871978ee0305afb 280w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-1.png?w=560&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=e837244e9da8def5ca1a292075065ce2 560w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-1.png?w=840&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=861bddf027cda7e6789c791943f70b0d 840w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-1.png?w=1100&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=bd7091a156ca9156213689fc8bba11f6 1100w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-1.png?w=1650&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=70c757dd7e73d0af78ab5b51034eeac8 1650w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-1.png?w=2500&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=904bb2b8360c99a3fe804c138ae9a79f 2500w" />

<img src="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-2.png?fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=5cf4876fd62625824f0f09e9974f4b52" data-og-width="805" width="805" data-og-height="849" height="849" data-path="container-engine/images/ollama-hf-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-2.png?w=280&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=511c83e4512dc769ea99b9ef1a8bf2f5 280w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-2.png?w=560&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=38982726316b17c72170409572362ef0 560w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-2.png?w=840&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=d88cfd025754a7876f170efd8f39532c 840w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-2.png?w=1100&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=4e864227fca62c2c3ff9b87078bb503a 1100w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-2.png?w=1650&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=b1eaf89a5505aa68df1d9c2cd1e658c8 1650w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-2.png?w=2500&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=c1acad9c5ae1085fc0ae3c436742a30f 2500w" />

2. Add an environment variable: `MODEL` set to the desired model (as specified above).

<img src="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-3.png?fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=67834c71dee428882e2795eb07c2b376" data-og-width="1597" width="1597" data-og-height="764" height="764" data-path="container-engine/images/ollama-hf-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-3.png?w=280&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=d0ce857815636da8526be0533ff26cff 280w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-3.png?w=560&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=76a0297337946ad3b7e4694d3cc6f0c2 560w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-3.png?w=840&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=0273ff075970d5717a36971b0f18f3d5 840w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-3.png?w=1100&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=8ea62ac2dd04f24815215752e6ec8b72 1100w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-3.png?w=1650&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=03e6e1d85f4fea0688c53312cc272b20 1650w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-3.png?w=2500&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=97844959adb67be119e37868b85a734d 2500w" />

3. Continue through the steps (the default setup is 8 vCPUs, 8 GB RAM, and 12 GB GPU, RTX 3060). For better performance,
   select a higher-end GPU and other parameters.
4. On the final page, ensure **Autostart** is checked, then click **Deploy**.

<img src="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-4.png?fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=fabac9d527e4c726a4f39c1c8dc288b5" data-og-width="1162" width="1162" data-og-height="873" height="873" data-path="container-engine/images/ollama-hf-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-4.png?w=280&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=fa372f18e5c81ceb98592c4fb89e2088 280w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-4.png?w=560&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=31acedb2356d02059da0f7c13a298075 560w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-4.png?w=840&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=217061206bb65690bfcadd86acf8dfdc 840w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-4.png?w=1100&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=7c39c6b82a1c8acdbed2ed3583e6e58f 1100w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-4.png?w=1650&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=2ee3bd3035d04c64cb37fed8be1c8ff8 1650w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-4.png?w=2500&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=739161587f04aed747ebb204829ef2aa 2500w" />

### Option 2: Custom Container Group

1. Click **Deploy a Container Group** and choose **Custom Container Group**.

<img src="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-5.png?fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=88e217a0ed3c03d517b1c2796e7c227f" data-og-width="899" width="899" data-og-height="685" height="685" data-path="container-engine/images/ollama-hf-5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-5.png?w=280&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=6c659fef2873c0bb03232c0444079f05 280w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-5.png?w=560&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=bda085e91d28d63d26297c67443aef07 560w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-5.png?w=840&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=a66a87774316b0102f2d9947ddbe0abf 840w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-5.png?w=1100&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=9260661de784562d2dac7975d5b19a16 1100w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-5.png?w=1650&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=7e354f5b3d4f48b73f7791cb5d771260 1650w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-5.png?w=2500&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=738ed056c012840ab7f974c360bd3c1f 2500w" />

2. Set a deployment name. Edit the image source and enter `saladtechnologies/ollama-hf:1.0.0` as the image name, then
   click **Configure**.

   <img src="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-6.png?fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=c6a4c9c5446929dbe3ace749a6381e2b" data-og-width="1605" width="1605" data-og-height="872" height="872" data-path="container-engine/images/ollama-hf-6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-6.png?w=280&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=bb4e3e4efdd4d1df4ac31557c0d4f95a 280w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-6.png?w=560&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=b860a988cbea14b0a1b0f86595e6ec20 560w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-6.png?w=840&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=68a4833cc939eff0b037aeab7ab61313 840w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-6.png?w=1100&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=59989dda3ea432e17c8be958b8f15d6c 1100w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-6.png?w=1650&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=ca5a7b241fd5142796e93e0794c29763 1650w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-6.png?w=2500&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=a387f9fef7cb97f45cb77381e466b34a 2500w" />

3. Edit the **Environment Variables** and add the following:
   * `MODEL` set to the desired Hugging Face model (as specified above). Move to the next page

4. Select the desired CPU, RAM, GPU, storage, and priority for the deployment.

5. Add a **Container Gateway**:

   * Click **Enable**, set the port to `11434`, and select **Least number of connections** as the load balancer
     algorithm.
   * Optionally, limit each server to a single active connection.

   <img src="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-7.png?fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=04d444fe6c64905391091d9cc1da1a92" data-og-width="1611" width="1611" data-og-height="864" height="864" data-path="container-engine/images/ollama-hf-7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-7.png?w=280&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=33820c3eb576f8585be92549026ec2de 280w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-7.png?w=560&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=d605c4294ac5ff929dc2c8c9bd8adb81 560w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-7.png?w=840&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=a8ee405ee9eb4744f5f5dceeebbc497c 840w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-7.png?w=1100&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=0b1f3cc935373959d7a8f343b5267aaa 1100w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-7.png?w=1650&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=c115fbf93906db750294d603ea47a99a 1650w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-7.png?w=2500&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=4beb54bd2a26e06fd5aa59cc6a6e7732 2500w" />

6. Add a **Startup Probe**:
   * Click **Enable**, set the path to `/` and port to `11434`. Set the probe type to `HTTP` and the initial delay to
     desired number.

7. Ensure **Autostart** is checked, then click **Deploy**.

<img src="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-4.png?fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=fabac9d527e4c726a4f39c1c8dc288b5" data-og-width="1162" width="1162" data-og-height="873" height="873" data-path="container-engine/images/ollama-hf-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-4.png?w=280&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=fa372f18e5c81ceb98592c4fb89e2088 280w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-4.png?w=560&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=31acedb2356d02059da0f7c13a298075 560w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-4.png?w=840&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=217061206bb65690bfcadd86acf8dfdc 840w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-4.png?w=1100&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=7c39c6b82a1c8acdbed2ed3583e6e58f 1100w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-4.png?w=1650&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=2ee3bd3035d04c64cb37fed8be1c8ff8 1650w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-4.png?w=2500&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=739161587f04aed747ebb204829ef2aa 2500w" />

## Use your Deployment

Once the deployment is complete, click on the deployment name to access the deployment details. To verify the model was
uploaded you can open the terminal and run the following command:

```bash  theme={null}
ollama list
```

<img src="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-10.png?fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=cfa5f4f7b45f083f431596e2432b3171" data-og-width="1076" width="1076" data-og-height="694" height="694" data-path="container-engine/images/ollama-hf-10.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-10.png?w=280&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=cc234e7106a7ab405f942ef2087817d2 280w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-10.png?w=560&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=4d3118d5b8110316914bd2a052681386 560w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-10.png?w=840&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=2e787ae08a0eeeaf6c1b9b8b045df02d 840w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-10.png?w=1100&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=dd4f389222741a986cae2e718f700e82 1100w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-10.png?w=1650&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=1430d1c3162b0849fad46eb3af0999dd 1650w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/ollama-hf-10.png?w=2500&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=834415dddb451f00126317ee67aebbf9 2500w" />

## How To Send Requests

Once your Ollama server is running with, you can send requests to interact with the model. Follow the instructions
provided in the
[OpenAI Documentation](https://github.com/SaladTechnologies/salad-recipes/blob/master/src/ollama-llama3.1/openai.md)
file to learn how to properly structure and send requests to the API.
