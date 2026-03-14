# Source: https://novita.ai/docs/guides/llm-dedicated-endpoint.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Dedicated Endpoint User Manual

## 1 Quickstart

### 1.1 Accessing Novita API Keys

* Account Registration:

1. Visit the official Novita website;
2. Click the "Log In" button located in the top-right corner;
3. Complete the user registration process.

* API Key Generation:

After successful registration, navigate to the [API key management page](https://novita.ai/settings/key-management?utm_source=getstarted). Generate and retrieve your API keys from this dashboard.

### 1.2 Creating Your First Dedicated Endpoint Instance

To create your first Dedicated Endpoint, first navigate to [Dedicated Endpoint](https://novita.ai/dedicated-endpoint), where you'll find two options: "LLM Dedicated Endpoints" and "Image Dedicated Endpoints" below the title. Click on "LLM Dedicated Endpoints" and then look for "High cost performance" section, where you will find the green "Create a new endpoint" button, click on it and you'll be redirected to [LLM Dedicated Endpoint](https://novita.ai/models-console/llm-dedicated-endpoints). Click either "+ New Endpoint" aligned with "Getting Started with Deployments" or "Get started" under "Create a new deployment". By now your Dedicated Endpoint creation journey formally begins:

1. After entering your Endpoint name, you'll see the "model" section below. For more information about this section, you can visit [**1.3**](#13-quick-deployment-of-huggingface-models) about them;
2. After successfully selecting base model and adding LoRA, you can choose hardware specifications and GPU quantity next, if you have any questions about this process, you can visit [**1.4**](#14-hardware-and-gpu-configuration) for more information;
3. After selecting your most suitable GPU and quantity, you'll enter autoscaling section, since this part is actually more complex, we've provided a detailed [**1.5**](#15-autoscaling-configuration) part for you to visit;
4. Eventually, you'll enter the last part of the whole process: setting your inference framework. Again we have an independent section for you to visit for more information: [**1.6**](#16-inference-framework-configuration)

And that's the complete process for creating your first Dedicated Endpoint. Enjoy using the service!

### 1.3 Quick Deployment of HuggingFace Models

After entering your desired model name, you'll see the Models module. Here's how to configure it:

1. To use models we provide for you for your Dedicated Endpoint, you need to get HuggingFace access token. Click Integrated-this link to log into HuggingFace;
2. Obtain your access token and then enter the token in the field below the "this link" button. This grants you access to private repositories and gated models;
3. Browse and select your preferred model from the available options;
4. If you want, you can also add the LoRA adapter by using the "+ add LoRA adapter" button at the bottom of the Models section. Enter the HuggingFace repository name for your desired LoRA adapter. For more details on LoRA adapters, refer to section [**2.3**](#23-best-practices-in-lora).

<Tip>
  While choosing model, You may notice a "Gated" label next to your choice, and this is completely normal!

  * GATED models on HuggingFace are restricted-access models, including Meta's LLaMA series, Mistral commercial license models and Medical and financial domain models
  * To access GATED models, log into your HuggingFace account, navigate to the model page (e.g., meta-llama) where you need to click "Access request" or "Request access" and provide usage description and accept terms of use. After doing all these things, you can just wait for approval before loading the model
</Tip>

### 1.4 Hardware and GPU Configuration

After selecting your model, you can configure your preferred hardware specifications and GPU count. At Novita, We are able to provide you with three different kinds of GPUs: H100 (High-performance enterprise GPU), H200 (Latest generation enterprise GPU) and RTX4090 (Cost-effective consumer GPU). you can choose to have 1,2 or 4 GPUs of one type. Feel free to combine any GPU type with any supported quantity to match your model requirements. But be careful! you are only allowed to use 8 GPUs in total. If you want to use more, you can purchase Enterprise Solution from our sales. After upgrading, you can adjust maximum GPU count in your account interface.

If you wonder which GPU and how many of them you should choose, we suggest you consider these factors:

* Model size - Larger models require more powerful/multiple GPUs;
* Performance needs - H100/H200 for high-performance, RTX4090 for cost-efficiency;
* Budget constraints - Balance performance requirements with costs.

### 1.5 Autoscaling Configuration

After configuring your hardware and GPU count, you'll reach the autoscaling module. In this part, if you choose the default settings, the autoscaling is enabled with minimum replicas as 1 and maximum replicas as 2. We do suggest you to turn on autoscaling, as it enables cost optimization, assures high performance and is resource-efficient. But of course, you can choose to turn off the autoscaling mode, by doing which your initial replica will be a fixed 1.

Under the autoscaling, you can adjust your Cooldown period (with default number of 300 seconds), you can adjust it to any time as long as it's longer than 120 seconds.

<Tip>
  If you are not very familiar with some terms written above, don't worry! We do have some explanations below:

  * Replica\
    An independent service instance that increases maximum supported QPS (queries per second). For example, if you have 2 GPUs with  min replicas as 1 and max replicas as 2, then the model will always run with ≥1 replica (2 GPUs) and can scale up to 2 replicas (4 GPUs total) during high traffic
  * Conditions for Minimum Replicas\
    Set to 0: Endpoint enters sleep mode during idle periods (cost-saving)\
    Set to >0: Maintains at least that many active replicas continuously
  * Conditions for Maximum Replicas\
    Defines the upper limit of replicas for handling traffic growth\
    System limit: Maximum 10 replicas
  * Cooldown Period\
    Delay before scaling down replicas, which can prevent premature resource release during temporary traffic drops.
</Tip>

### 1.6 Inference Framework Configuration

If you are reading this part, congratulations! You're just one step away from successfully deploying your Dedicated Endpoint. At this stage, you'll configure the inference framework settings.

Here you can choose your own engine with two choices: vLLM and SGLang. If your base model is a LLM and you want it to do tasks like text generation, completion and chat applications, we suggest choosing vLLM, which is optimized for Large Language Models (LLMs). If your base model is a Multimodal model or a non-LLM one and you want it to do tasks related to Vision or specialized AI applications, we suggest choosing SGLang, which has versatile framework for diverse model types.

After choosing your engine type, there'll be default engine version with the latest. If you want, you can also select older versions. --max-model-len controls context length, you'll be able to use model's default configuration when you left this blank empty. --max-num-seqs sets the number of sequences per iteration, affecting throughput and resource utilization. If you want to add more engine parameters, you can write them in Additional Arguments, which can fine-tune engine behavior for specific requirements.

## 2 Model Management

### 2.1 Supported Models and their capabilities

Up till now, there are five models supporting Dedicated Endpoints in Novita without being **gated** (see the tip in [1.3](#13-quick-deployment-of-huggingface-models) if you don't know what gate means):

| Model name                                | vision | reasoning | function-calling | structured output | context size | tensor type |
| ----------------------------------------- | ------ | --------- | ---------------- | ----------------- | ------------ | ----------- |
| deepseek/deepseek-r1-0528-qwen3-8b        | no     | yes       | no               | no                | 128000       | BF16        |
| meta-llama/llama-4-scout-17b-16e-instruct | yes    | no        | yes              | no                | 131072       | BF16        |
| deepseek/deepseek-r1-distill-llama-8b     | no     | yes       | no               | yes               | 32000        | BF16        |
| qwen/qwen3-8b-fp8                         | no     | yes       | no               | no                | 128000       | FP8         |
| qwen/qwen3-4b-fp8                         | no     | yes       | no               | no                | 128000       | FP8         |

there are six models supporting Dedicated Endpoints in Novita being gated:

| Model name                                   | vision | reasoning | function-calling | structured output | context size | tensor type |
| :------------------------------------------- | :----- | :-------- | :--------------- | :---------------- | :----------- | :---------- |
| meta-llama/llama-3.1-8b-instruct             | no     | no        | no               | no                | 16384        | FP8         |
| meta-llama/llama-3.3-70b-instruct            | no     | no        | yes              | yes               | 131072       | BF16        |
| meta-llama/llama-3.2-3b-instruct             | no     | no        | yes              | no                | 32768        | BF16        |
| novita/inflatebot-mn-12B-mag-mell-r1-awq-fp8 | yes    | no        | yes              | yes               | 32000        | FP8         |
| novita/sao10k-l3-8b-stheno-v3.2-awq-fp8      | no     | no        | no               | no                | 8192         | FP8         |
| deepseek/deepseek-v3-0324                    | no     | no        | yes              | no                | 163840       | FP8         |

### 2.2 Custom Upload (LoRA Adapters)

LoRA (Low-Rank Adaptation of LLMs) is a popular and lightweight training technique that dramatically reduces trainable parameters.

Core Mechanism of LoRA:

* **Parameter Insertion**: Adds minimal new weights to pre-trained models
* **Selective Training**: Only trains new parameters while keeping original weights frozen
* **Inference Integration**: Updated low-rank weights are merged with frozen base model weights

Key Advantages of LoRA:

* **Faster Training**: Significantly accelerated training process
* **Lower Memory Usage**: Dramatically reduced memory consumption
* **Compact Models**: Generates smaller weight files (only hundreds of MB)
* **Easy Sharing**: Simplified storage and distribution
  For more details, you can visit [LoRAs in Novita](https://novita.ai/docs/api-reference/model-apis-list-training-task)

Here at Novita, we not only support adding LoRA with PEFT or HuggingFace LoRA formats for fine-tuning models, but also allows Multi-Model Mounting, Hot-Switching Capabilities and adapter ensemble. So through our proprietary optimization technology, you can deploy and serve multiple LoRA models on a single endpoint using just one GPU. This simplifies operational workflows, maximizes resource utilization efficiency, and delivers greater flexibility and superior performance when customizing models—while supporting the loading and processing of image assets. Achieve efficient deployment without compromising top-tier inference quality.

### 2.3 Best Practices in LoRA

Follow these detailed steps to add LoRA adapters to your certain Dedicated Endpoint:

1. In the Dedicated Endpoints creation Models module, locate "+ Add LoRA adapter" at the bottom (separate from "Base Model"). Click to begin adapter configuration;
2. Enter the adapter's Hugging Face model ID. One base model can support multiple LoRA adapters, all adapters are deployed directly from Hugging Face Hub;
3. Once base model is selected, "+Add LoRA adapter" button becomes active. Click to open the LoRA adapter configuration modal;
4. If you succeeded in adding LoRA adapter, the plus button will change from gray to blue  However, if you see the message: "LoRA adapter does not match base model" , you may need to add your LoRA adapter again;
5. After successfully adding your LoRA adapter, you can test Your Deployment. You can see a new interface called "My New LoRA endpoint". If you want to test your adapter, you can go to "Playground" page for testing. You can use the highlighted dropdown menu to seamlessly switch between adapter models and base models for experimentation and comparison.

That's it! You've successfully deployed a LoRA adapter on your certain dedicated endpoint and tested it in the Playground. You're now ready to explore advanced multi-adapter configurations or integrate your model into production applications.

## 3. Private Endpoint Deployment

### 3.1 Private Endpoint Status Monitoring

Access the ​​"My Models - Dedicated Endpoints"​​ page, where all dedicated endpoint model deployment tasks are displayed. Click ​​Dedicated Endpoints → Model Name​​ to enter the model details page, which shows deployment configuration information and endpoint status. There are five possible status indicators:

* ​​Running​​ (In Service): The endpoint is fully operational, having completed initialization/version upgrade/scaling, and is ready to process inference requests—indicating a successful deployment.
* ​​Pending​​ (Cold Start): Resources and models are being initialized; the endpoint cannot accept requests yet (no available workers).
* ​​Rolling​​ (Version Updating): Configuration or model version is being updated. ​​
* Terminating​​ (Pausing): The endpoint is in the process of shutting down. ​​
* Terminated​​ (Stopped): The endpoint has been terminated, with min/max replicas set to 0,

GPU instances released, and billing halted. ​​Status Indicators & Actions​​:

* ​​Green Button​​: Endpoint is ​​Running​​ (active and serving requests). ​
* Yellow Button​​: Endpoint is in ​​Pending​​ (cold start) phase. ​​
* Cycling Symbol​​: Endpoint is ​​Rolling​​ (updating). ​​
* Red Button​​: Endpoint is either ​​Terminating​​ (shutting down) or ​​Terminated​​ (fully stopped).

Suggested status:

| combination of stutus    | situations                                                        |
| ------------------------ | ----------------------------------------------------------------- |
| Running                  | Able to accept reasoning requirement                              |
| Pending/Rolling→ Running | Restore available status automatically after changing deployments |
| Terminating→ Terminated  | Release resources, stop billing, support restart                  |

### **3.2 Endpoint Status Management Operations**

When your ​**​**Dedicated Endpoint​​ is in the ​**​**Running​​ state, you will see a ​**​**"Terminate"​​ button aligned with the Dedicated Endpoint name on the right side of the screen. Clicking this button will stop the endpoint. To restart it, simply click the ​**​**"Restart"​​ button located below the Dedicated Endpoint name.

<Note>
  ​**​Important Notes​**​:

  * ​​Deletion is not allowed​​ while the Dedicated Endpoint is in the ​**​**Running​​ state.
  * If you need to delete the model, first set the Dedicated Endpoint to a ​​stopped​​ state, then click ​**​**"Update"​​ followed by ​**​**"Delete"​​ to remove it.
</Note>

## 4. Commercial Capabilities

### 4.1 Dedicated Endpoint Billing Rules & Report Export

Your ​Dedicated Endpoints billing on the Novita platform follows this pricing logic:\
​​Total Cost = Number of GPUs × Duration (hours) × Price per GPU-hour​​

**​​Key Billing Details​​**

1. ​**​Duration Calculation​**​:
   * Measured in seconds by the backend system (configured at 1-second granularity).
   * ​Billed hourly​​ (rounded to the nearest hour).
   * Starts when the Dedicated Endpoint enters ​Running​​ status and ends when it stops (includes state transitions like scaling updates).
2. ​**​GPU Pricing​**​:
   * Pricing varies by ​GPU type​​ .
   * ​Dynamic scaling supported: The number of GPUs (2/4/8) is adjusted automatically based on workload, with Novita’s autoscaling system reporting real-time values.
   * If you want to learn more about it, you can visit our [pricing page](https://novita.ai/pricing) and click on "GPUs" to see more.
3. ​**​Usage Reporting​**​:
   * Data is reported ​​per minute​​ (one data point every minute).

For full pricing specifications, visit: [Novita Pricing - LLMs Dedicated Endpoints](https://novita.ai/pricing).

​​**Billing Statements & Export​​**

Access your Dedicated Endpoints usage reports at [Novita Billing Details](https://novita.ai/billing/details), where your report includes:

* Billing cycle dates
* Product category (LLM Dedicated Endpoints)
* Cost breakdown by DE (including ​Endpoints ID​​, GPU count, and price per GPU-second)

​​To export your report​​, just Click ​"LLM Dedicated Endpoints → Export"​​ to generate and download a copy.


Built with [Mintlify](https://mintlify.com).