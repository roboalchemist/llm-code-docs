# Source: https://io.net/docs/guides/intelligence/training-as-a-service.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Training as a Service (TaaS)

> Customize and fine-tune models to fit your needs - no need to train from scratch.

<Info>
  Note: This feature is currently in Beta. We are actively refining the experience and would love to hear your feedback.
</Info>

With IO Intelligence’s [Training as a Service (TaaS)](https://ai.io.net/ai/training), you can fine-tune powerful pre-trained models using your own data—achieving tailored performance without the complexity of training from scratch.

Built for builders, researchers, developers, and businesses, TaaS gives you greater control over how your AI learns and adapts. With support for advanced techniques such as PPO, DPO, and reward modeling, you can move beyond traditional fine-tuning and experiment at the cutting edge of machine learning.

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/TivZctC8MNs" title="Training as a Service with IO Intelligence" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

## Getting Started

To begin training your model:

* **Go to your** io.net Dashboard.
* Navigate to [**Training**](https://ai.io.net/ai/training) under the **IO Intelligence** section.

  <Frame>
      <img src="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/563e87f42b1ce782ecdd87a578d5ee0c93b568588f3516688bc6c495067d86b6-Trainin_Model-1.jpg?fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=76a0d057af4fbf5b1e6ea38c650f1ac4" alt="" data-og-width="1395" width="1395" data-og-height="240" height="240" data-path="images/docs/563e87f42b1ce782ecdd87a578d5ee0c93b568588f3516688bc6c495067d86b6-Trainin_Model-1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/563e87f42b1ce782ecdd87a578d5ee0c93b568588f3516688bc6c495067d86b6-Trainin_Model-1.jpg?w=280&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=19deeb71a3eafed699482aa45d8a08d8 280w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/563e87f42b1ce782ecdd87a578d5ee0c93b568588f3516688bc6c495067d86b6-Trainin_Model-1.jpg?w=560&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=69eca6d80c6827a61e0fb74cd1792a67 560w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/563e87f42b1ce782ecdd87a578d5ee0c93b568588f3516688bc6c495067d86b6-Trainin_Model-1.jpg?w=840&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=190487be5a0793d199867ee1a6843685 840w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/563e87f42b1ce782ecdd87a578d5ee0c93b568588f3516688bc6c495067d86b6-Trainin_Model-1.jpg?w=1100&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=5a42431344022d763687fddb625cc89d 1100w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/563e87f42b1ce782ecdd87a578d5ee0c93b568588f3516688bc6c495067d86b6-Trainin_Model-1.jpg?w=1650&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=b92c08709479142aaee91819caa0c356 1650w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/563e87f42b1ce782ecdd87a578d5ee0c93b568588f3516688bc6c495067d86b6-Trainin_Model-1.jpg?w=2500&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=661e72a9afbe523a7526ffc9b2478ca0 2500w" />
  </Frame>
* Click the **Start Training** button to launch the setup form.

  <Frame>
      <img src="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/dcd9da833435128ec197384b3fc2fd052179c4729f0326c52b9e87d16f7b1d88-Trainin_Model-2.jpg?fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=02ecdc02616f5e7ec5ffdef9aeecd00e" alt="" data-og-width="1468" width="1468" data-og-height="348" height="348" data-path="images/docs/dcd9da833435128ec197384b3fc2fd052179c4729f0326c52b9e87d16f7b1d88-Trainin_Model-2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/dcd9da833435128ec197384b3fc2fd052179c4729f0326c52b9e87d16f7b1d88-Trainin_Model-2.jpg?w=280&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=0f9b7dd9bdd5aea6e9f905d9120e9a14 280w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/dcd9da833435128ec197384b3fc2fd052179c4729f0326c52b9e87d16f7b1d88-Trainin_Model-2.jpg?w=560&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=ab6c27d4ecb537f4881f58f435dc00e0 560w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/dcd9da833435128ec197384b3fc2fd052179c4729f0326c52b9e87d16f7b1d88-Trainin_Model-2.jpg?w=840&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=57f0b49b8a6e5c17421be5de398283ed 840w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/dcd9da833435128ec197384b3fc2fd052179c4729f0326c52b9e87d16f7b1d88-Trainin_Model-2.jpg?w=1100&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=4587297cff3853201112149836992280 1100w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/dcd9da833435128ec197384b3fc2fd052179c4729f0326c52b9e87d16f7b1d88-Trainin_Model-2.jpg?w=1650&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=4ffa8b7263343ecb41953714918c0872 1650w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/dcd9da833435128ec197384b3fc2fd052179c4729f0326c52b9e87d16f7b1d88-Trainin_Model-2.jpg?w=2500&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=465ee5981fd2f199beecd6b36579c811 2500w" />
  </Frame>

<Info>
  io.net does not support training models from scratch. All training is done via fine-tuning or customization of existing models.
</Info>

## Build Your Training Workflow

The *Training Model* form is designed to guide you through the setup process, step by step.

### 1. Select a Training Method

Pick how your model should learn. You can choose from a variety of advanced methods:

* **Supervised Fine-Tuning**: Teach your model using labeled datasets for task-specific learning.
* **Reward Modeling:** Train your model to assign scores to generated responses.
* **Proximal Policy Optimization (PPO):** Use reinforcement learning with reward feedback.
* **Direct Preference Optimization (DPO):** Optimize the model directly using ranked preferences.
* **Controlled Tuning Optimization** *(Experimental):* Apply KL-regularized tuning for fine-grained control.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e57aa8c3c7c52a70659857d7a78ad7f93f6227b6868707ef7e294cf2373d27e2-Trainin_Model-10.jpg?fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=121043bc13909f4e34460ad6fb07a28c" alt="" data-og-width="2445" width="2445" data-og-height="649" height="649" data-path="images/docs/e57aa8c3c7c52a70659857d7a78ad7f93f6227b6868707ef7e294cf2373d27e2-Trainin_Model-10.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e57aa8c3c7c52a70659857d7a78ad7f93f6227b6868707ef7e294cf2373d27e2-Trainin_Model-10.jpg?w=280&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=218289f3c6608d68b719edddf1614324 280w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e57aa8c3c7c52a70659857d7a78ad7f93f6227b6868707ef7e294cf2373d27e2-Trainin_Model-10.jpg?w=560&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=8dfe26ec4347d396332b8f2adf355cac 560w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e57aa8c3c7c52a70659857d7a78ad7f93f6227b6868707ef7e294cf2373d27e2-Trainin_Model-10.jpg?w=840&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=cc68d77f444995fb54207389b31af9e3 840w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e57aa8c3c7c52a70659857d7a78ad7f93f6227b6868707ef7e294cf2373d27e2-Trainin_Model-10.jpg?w=1100&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=d44ff448f88162b44775c9a107a6a048 1100w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e57aa8c3c7c52a70659857d7a78ad7f93f6227b6868707ef7e294cf2373d27e2-Trainin_Model-10.jpg?w=1650&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=04538499325da168aec94e7513ec8ec0 1650w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e57aa8c3c7c52a70659857d7a78ad7f93f6227b6868707ef7e294cf2373d27e2-Trainin_Model-10.jpg?w=2500&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=95fe28c296c8cedf4da0e1718f9a79ff 2500w" />
</Frame>

### 2. Select a Base Model

You can select a **pre-integrated** model from our library or bring your own model from **Hugging Face**.

<Tabs>
  <Tab title="Option A - Use a Preloaded Model">
    Choose from our library of 561 open-source base models in the dropdown list, for example, LLaMA, Mistral, Falcon, GPT-Neo, and many more.

    <Frame>
            <img src="https://mintcdn.com/ionet-cca8037f/mb5icugukY5zzfmb/images/docs/io-intelligence/TaaS/TaaS_SelectModel_ChooseModel.png?fit=max&auto=format&n=mb5icugukY5zzfmb&q=85&s=fdeb91a89046b92243dc6ba7e44902b0" alt="TaaS Choose Preloaded Model" data-og-width="2574" width="2574" data-og-height="814" height="814" data-path="images/docs/io-intelligence/TaaS/TaaS_SelectModel_ChooseModel.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/mb5icugukY5zzfmb/images/docs/io-intelligence/TaaS/TaaS_SelectModel_ChooseModel.png?w=280&fit=max&auto=format&n=mb5icugukY5zzfmb&q=85&s=2507629be217c37c8b34d73960e258c4 280w, https://mintcdn.com/ionet-cca8037f/mb5icugukY5zzfmb/images/docs/io-intelligence/TaaS/TaaS_SelectModel_ChooseModel.png?w=560&fit=max&auto=format&n=mb5icugukY5zzfmb&q=85&s=b5a8204210c9cebda474d95d50544f6b 560w, https://mintcdn.com/ionet-cca8037f/mb5icugukY5zzfmb/images/docs/io-intelligence/TaaS/TaaS_SelectModel_ChooseModel.png?w=840&fit=max&auto=format&n=mb5icugukY5zzfmb&q=85&s=42dd6f00dd4e148c9aa70a1aefb4e9cf 840w, https://mintcdn.com/ionet-cca8037f/mb5icugukY5zzfmb/images/docs/io-intelligence/TaaS/TaaS_SelectModel_ChooseModel.png?w=1100&fit=max&auto=format&n=mb5icugukY5zzfmb&q=85&s=65b1db477f1dfad86de941789fa9637d 1100w, https://mintcdn.com/ionet-cca8037f/mb5icugukY5zzfmb/images/docs/io-intelligence/TaaS/TaaS_SelectModel_ChooseModel.png?w=1650&fit=max&auto=format&n=mb5icugukY5zzfmb&q=85&s=3c80acc444c85c4a08044bd7e0c088ad 1650w, https://mintcdn.com/ionet-cca8037f/mb5icugukY5zzfmb/images/docs/io-intelligence/TaaS/TaaS_SelectModel_ChooseModel.png?w=2500&fit=max&auto=format&n=mb5icugukY5zzfmb&q=85&s=5b1f99879601e70e51643c2bbdd178d8 2500w" />
    </Frame>
  </Tab>

  <Tab title="Option B - Link a Hugging Face Model">
    You can bring your own model from **Hugging Face** by following these steps:

    1. Paste your Hugging Face model repository link in the field.
    2. Click the **Test** button.
    3. If the connection is successful, you will see: “*Successfully tested.*”
    4. If the repository is **private** or **invalid**, a prompt will request your *Hugging Face Token* with the message: "*The repository is private or does not exist. Provide an HF Token".* For additional guidance, see [**How to get your Hugging Face Token**](https://huggingface.co/docs/hub/en/security-tokens).

    <Frame>
            <img src="https://mintcdn.com/ionet-cca8037f/mb5icugukY5zzfmb/images/docs/io-intelligence/TaaS/TaaS_SelectModel_HuggingFaceLink.png?fit=max&auto=format&n=mb5icugukY5zzfmb&q=85&s=28fbcdfada71660bcf66fc4a8ed7479d" alt="TaaS Select Model - Import from Hugging Face Link" data-og-width="2574" width="2574" data-og-height="814" height="814" data-path="images/docs/io-intelligence/TaaS/TaaS_SelectModel_HuggingFaceLink.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/mb5icugukY5zzfmb/images/docs/io-intelligence/TaaS/TaaS_SelectModel_HuggingFaceLink.png?w=280&fit=max&auto=format&n=mb5icugukY5zzfmb&q=85&s=6d5e2215ec3c183959d88af4ba5a24b2 280w, https://mintcdn.com/ionet-cca8037f/mb5icugukY5zzfmb/images/docs/io-intelligence/TaaS/TaaS_SelectModel_HuggingFaceLink.png?w=560&fit=max&auto=format&n=mb5icugukY5zzfmb&q=85&s=da1379b3bd8f95e32000f4dae7d9c009 560w, https://mintcdn.com/ionet-cca8037f/mb5icugukY5zzfmb/images/docs/io-intelligence/TaaS/TaaS_SelectModel_HuggingFaceLink.png?w=840&fit=max&auto=format&n=mb5icugukY5zzfmb&q=85&s=9fbf0021218c6b71f6a0d85cb50c02a1 840w, https://mintcdn.com/ionet-cca8037f/mb5icugukY5zzfmb/images/docs/io-intelligence/TaaS/TaaS_SelectModel_HuggingFaceLink.png?w=1100&fit=max&auto=format&n=mb5icugukY5zzfmb&q=85&s=251fd31af1d0c3036c8dc23d4a1a92bb 1100w, https://mintcdn.com/ionet-cca8037f/mb5icugukY5zzfmb/images/docs/io-intelligence/TaaS/TaaS_SelectModel_HuggingFaceLink.png?w=1650&fit=max&auto=format&n=mb5icugukY5zzfmb&q=85&s=b4c7c74c3f7bd4be3333faae53f4bbd6 1650w, https://mintcdn.com/ionet-cca8037f/mb5icugukY5zzfmb/images/docs/io-intelligence/TaaS/TaaS_SelectModel_HuggingFaceLink.png?w=2500&fit=max&auto=format&n=mb5icugukY5zzfmb&q=85&s=aa78095955e21e0e12f0e6997d336752 2500w" />
    </Frame>
  </Tab>
</Tabs>

### 3. Select a Dataset

Choose training data from a **curated list** or bring your own custom dataset.

<Tabs>
  <Tab title="Option A - Use a Built-in Dataset">
    Select a dataset from our list using the dropdown menu.

    <Frame>
            <img src="https://mintcdn.com/ionet-cca8037f/312yMOHnj52Nj5y_/images/docs/io-intelligence/TaaS/TaaS_SelectDataset_BaseDataset.png?fit=max&auto=format&n=312yMOHnj52Nj5y_&q=85&s=710c358e87def93b91f0f9525517307b" alt="TaaS Select Dataset - Base Dataset" data-og-width="2574" width="2574" data-og-height="814" height="814" data-path="images/docs/io-intelligence/TaaS/TaaS_SelectDataset_BaseDataset.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/312yMOHnj52Nj5y_/images/docs/io-intelligence/TaaS/TaaS_SelectDataset_BaseDataset.png?w=280&fit=max&auto=format&n=312yMOHnj52Nj5y_&q=85&s=815800a6ed1fe6a0fe6742cebb2e4848 280w, https://mintcdn.com/ionet-cca8037f/312yMOHnj52Nj5y_/images/docs/io-intelligence/TaaS/TaaS_SelectDataset_BaseDataset.png?w=560&fit=max&auto=format&n=312yMOHnj52Nj5y_&q=85&s=336f33c32f3a758adab0b6d422b0f325 560w, https://mintcdn.com/ionet-cca8037f/312yMOHnj52Nj5y_/images/docs/io-intelligence/TaaS/TaaS_SelectDataset_BaseDataset.png?w=840&fit=max&auto=format&n=312yMOHnj52Nj5y_&q=85&s=b6c792b4e679cfb4717e50f5967be03e 840w, https://mintcdn.com/ionet-cca8037f/312yMOHnj52Nj5y_/images/docs/io-intelligence/TaaS/TaaS_SelectDataset_BaseDataset.png?w=1100&fit=max&auto=format&n=312yMOHnj52Nj5y_&q=85&s=7dfa3b7884a19b57b98295c9f20e8897 1100w, https://mintcdn.com/ionet-cca8037f/312yMOHnj52Nj5y_/images/docs/io-intelligence/TaaS/TaaS_SelectDataset_BaseDataset.png?w=1650&fit=max&auto=format&n=312yMOHnj52Nj5y_&q=85&s=c313b7a0f9c56d79b7f66a5a926f76ca 1650w, https://mintcdn.com/ionet-cca8037f/312yMOHnj52Nj5y_/images/docs/io-intelligence/TaaS/TaaS_SelectDataset_BaseDataset.png?w=2500&fit=max&auto=format&n=312yMOHnj52Nj5y_&q=85&s=9c6c0ecc63dcafdfa85ffc9a1a18d263 2500w" />
    </Frame>
  </Tab>

  <Tab title="Option B - Link a Custom Dataset">
    Set up your dataset by completing the configuration fields.

    <Frame>
            <img src="https://mintcdn.com/ionet-cca8037f/mb5icugukY5zzfmb/images/docs/io-intelligence/TaaS/TaaS_SelectDataset_CustomDataset.png?fit=max&auto=format&n=mb5icugukY5zzfmb&q=85&s=b750c2d2a3a7831ef5fd84a10d40d048" alt="TaaS Select Dataset - Custom Dataset" data-og-width="2566" width="2566" data-og-height="1402" height="1402" data-path="images/docs/io-intelligence/TaaS/TaaS_SelectDataset_CustomDataset.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/mb5icugukY5zzfmb/images/docs/io-intelligence/TaaS/TaaS_SelectDataset_CustomDataset.png?w=280&fit=max&auto=format&n=mb5icugukY5zzfmb&q=85&s=a5c12e8e65fc748aff5d0aecc687b1a5 280w, https://mintcdn.com/ionet-cca8037f/mb5icugukY5zzfmb/images/docs/io-intelligence/TaaS/TaaS_SelectDataset_CustomDataset.png?w=560&fit=max&auto=format&n=mb5icugukY5zzfmb&q=85&s=dbb74b8f9ed7a142ee6d50229f9e6fba 560w, https://mintcdn.com/ionet-cca8037f/mb5icugukY5zzfmb/images/docs/io-intelligence/TaaS/TaaS_SelectDataset_CustomDataset.png?w=840&fit=max&auto=format&n=mb5icugukY5zzfmb&q=85&s=5c5d75a67cc8c6c9791f5493442a233a 840w, https://mintcdn.com/ionet-cca8037f/mb5icugukY5zzfmb/images/docs/io-intelligence/TaaS/TaaS_SelectDataset_CustomDataset.png?w=1100&fit=max&auto=format&n=mb5icugukY5zzfmb&q=85&s=53e8d823912dc137ccf652512d4147e2 1100w, https://mintcdn.com/ionet-cca8037f/mb5icugukY5zzfmb/images/docs/io-intelligence/TaaS/TaaS_SelectDataset_CustomDataset.png?w=1650&fit=max&auto=format&n=mb5icugukY5zzfmb&q=85&s=b7ceae977b0b6010c6c2bbfa1ed23b98 1650w, https://mintcdn.com/ionet-cca8037f/mb5icugukY5zzfmb/images/docs/io-intelligence/TaaS/TaaS_SelectDataset_CustomDataset.png?w=2500&fit=max&auto=format&n=mb5icugukY5zzfmb&q=85&s=e8cbea7b74d2b7263a539d3605d3c7fe 2500w" />
    </Frame>

    <Tip>
      Refer to the documentation link provided on top of the ***Configuration*** section for more details.
    </Tip>
  </Tab>
</Tabs>

### 4. Choose a Training Style

Depending on your goal, you can select between **Simple Creating** and **Advanced Creating** when training a model.

<Tabs>
  <Tab title="Option A - Simple Creating">
    Uses default settings for a quick and straightforward setup. Best if you want to get started fast without managing technical details.

    <Frame>
            <img src="https://mintcdn.com/ionet-cca8037f/mb5icugukY5zzfmb/images/docs/io-intelligence/TaaS/TaaS_SimpleTrainingStyle.png?fit=max&auto=format&n=mb5icugukY5zzfmb&q=85&s=4fac551e441a931a9619462a6bb6e845" alt="Taa S Simple Training Style Pn" data-og-width="2552" width="2552" data-og-height="490" height="490" data-path="images/docs/io-intelligence/TaaS/TaaS_SimpleTrainingStyle.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/mb5icugukY5zzfmb/images/docs/io-intelligence/TaaS/TaaS_SimpleTrainingStyle.png?w=280&fit=max&auto=format&n=mb5icugukY5zzfmb&q=85&s=d0463b22afa551409b0f69050e23c2ab 280w, https://mintcdn.com/ionet-cca8037f/mb5icugukY5zzfmb/images/docs/io-intelligence/TaaS/TaaS_SimpleTrainingStyle.png?w=560&fit=max&auto=format&n=mb5icugukY5zzfmb&q=85&s=f34357be8e85f9148092082749e78eac 560w, https://mintcdn.com/ionet-cca8037f/mb5icugukY5zzfmb/images/docs/io-intelligence/TaaS/TaaS_SimpleTrainingStyle.png?w=840&fit=max&auto=format&n=mb5icugukY5zzfmb&q=85&s=a127025aeec8d5e8feecaecff0cf189a 840w, https://mintcdn.com/ionet-cca8037f/mb5icugukY5zzfmb/images/docs/io-intelligence/TaaS/TaaS_SimpleTrainingStyle.png?w=1100&fit=max&auto=format&n=mb5icugukY5zzfmb&q=85&s=8ce4a0094dbdddc7fe481edfaafc4fb3 1100w, https://mintcdn.com/ionet-cca8037f/mb5icugukY5zzfmb/images/docs/io-intelligence/TaaS/TaaS_SimpleTrainingStyle.png?w=1650&fit=max&auto=format&n=mb5icugukY5zzfmb&q=85&s=c48a83df00a2a16175e4fe3240189d34 1650w, https://mintcdn.com/ionet-cca8037f/mb5icugukY5zzfmb/images/docs/io-intelligence/TaaS/TaaS_SimpleTrainingStyle.png?w=2500&fit=max&auto=format&n=mb5icugukY5zzfmb&q=85&s=e6789472413090d407c3dae254a653e3 2500w" />
    </Frame>
  </Tab>

  <Tab title="Option B - Advanced Creating">
    Offers full flexibility and control. Select this option if your goal is to customize every aspect of how your model learns, from hyperparameters to optimization strategies.

    <Note>
      For further technical documentation on each advanced configuration, refer to [Llama Factory](https://llamafactory.readthedocs.io/en/latest/).
    </Note>

    <Frame>
            <img src="https://mintcdn.com/ionet-cca8037f/XEVdGCr0JevSPqau/images/docs/io-intelligence/TaaS/TaaS_SelectTrainingStyle_Temp.png?fit=max&auto=format&n=XEVdGCr0JevSPqau&q=85&s=ce7cc6fb46ce3fd9882372f12d0f1235" alt="Taa S Select Training Style Temp Pn" data-og-width="2530" width="2530" data-og-height="1572" height="1572" data-path="images/docs/io-intelligence/TaaS/TaaS_SelectTrainingStyle_Temp.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/XEVdGCr0JevSPqau/images/docs/io-intelligence/TaaS/TaaS_SelectTrainingStyle_Temp.png?w=280&fit=max&auto=format&n=XEVdGCr0JevSPqau&q=85&s=26c64987ccb5cd0799d566e4d5545ec9 280w, https://mintcdn.com/ionet-cca8037f/XEVdGCr0JevSPqau/images/docs/io-intelligence/TaaS/TaaS_SelectTrainingStyle_Temp.png?w=560&fit=max&auto=format&n=XEVdGCr0JevSPqau&q=85&s=c9f353e4bc0d6ea6acdac70cb08eaf9d 560w, https://mintcdn.com/ionet-cca8037f/XEVdGCr0JevSPqau/images/docs/io-intelligence/TaaS/TaaS_SelectTrainingStyle_Temp.png?w=840&fit=max&auto=format&n=XEVdGCr0JevSPqau&q=85&s=a4ec44ce1235499b12d53249489947bf 840w, https://mintcdn.com/ionet-cca8037f/XEVdGCr0JevSPqau/images/docs/io-intelligence/TaaS/TaaS_SelectTrainingStyle_Temp.png?w=1100&fit=max&auto=format&n=XEVdGCr0JevSPqau&q=85&s=51efc5231b7aeebe2e99d81aa77b712a 1100w, https://mintcdn.com/ionet-cca8037f/XEVdGCr0JevSPqau/images/docs/io-intelligence/TaaS/TaaS_SelectTrainingStyle_Temp.png?w=1650&fit=max&auto=format&n=XEVdGCr0JevSPqau&q=85&s=aa76dd0a4a7de215eafc0df0dfcf3da2 1650w, https://mintcdn.com/ionet-cca8037f/XEVdGCr0JevSPqau/images/docs/io-intelligence/TaaS/TaaS_SelectTrainingStyle_Temp.png?w=2500&fit=max&auto=format&n=XEVdGCr0JevSPqau&q=85&s=17d14e6cb8b1b445a4d447ec89f687d4 2500w" />
    </Frame>
  </Tab>
</Tabs>

### 5. Start Training

After setting up the details of your model, click **Start Training** to begin.

## Training Dashboard

The following sections can be viewed in the ***Training Dashboard***.

#### Your Current Plan

At the top of the page, you can view your current plan details. To increase your training runs or access faster processing, click the **Upgrade** button.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0573093d86a6a6b604c7a770249fdba6412cde000fbffa94111b3263bf25236c-Trainin_Model-3.jpg?fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=6349d3046b3292736b608864fbb76c6e" alt="" className="mx-auto" style={{ width:"63%" }} data-og-width="710" width="710" data-og-height="298" height="298" data-path="images/docs/0573093d86a6a6b604c7a770249fdba6412cde000fbffa94111b3263bf25236c-Trainin_Model-3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0573093d86a6a6b604c7a770249fdba6412cde000fbffa94111b3263bf25236c-Trainin_Model-3.jpg?w=280&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=3eafafc58299dcbaf0bd590a68f2ba6f 280w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0573093d86a6a6b604c7a770249fdba6412cde000fbffa94111b3263bf25236c-Trainin_Model-3.jpg?w=560&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=d291f17145c8f611f79de9fc62fcb9b3 560w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0573093d86a6a6b604c7a770249fdba6412cde000fbffa94111b3263bf25236c-Trainin_Model-3.jpg?w=840&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=df0227dad1992cf97b9c4f4af3250625 840w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0573093d86a6a6b604c7a770249fdba6412cde000fbffa94111b3263bf25236c-Trainin_Model-3.jpg?w=1100&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=213cc170d7ba5508585026f36e88f32b 1100w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0573093d86a6a6b604c7a770249fdba6412cde000fbffa94111b3263bf25236c-Trainin_Model-3.jpg?w=1650&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=4ef20c13ae75e44942876022071faa3c 1650w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0573093d86a6a6b604c7a770249fdba6412cde000fbffa94111b3263bf25236c-Trainin_Model-3.jpg?w=2500&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=02c6a87c6baec7c518cd5035f8ddd66c 2500w" />
</Frame>

#### Your Training Jobs

Below your plan, there is a **Training Jobs** table where you can view and manage all your model training requests. Each row shows key details such as, *Job ID*, *Base Model*, *Type*, *Status*, and *Run Time.*

Click on any job to open the detailed view and see how it is progressing.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/Sa-6uYnlPwRnz7qP/images/docs/io-intelligence/TaaS/TaaS_YourTrainingJobs.png?fit=max&auto=format&n=Sa-6uYnlPwRnz7qP&q=85&s=c76995418a1449b390ef1940cd89f518" alt="Your Training Jobs table" data-og-width="2584" width="2584" data-og-height="852" height="852" data-path="images/docs/io-intelligence/TaaS/TaaS_YourTrainingJobs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/Sa-6uYnlPwRnz7qP/images/docs/io-intelligence/TaaS/TaaS_YourTrainingJobs.png?w=280&fit=max&auto=format&n=Sa-6uYnlPwRnz7qP&q=85&s=c9d44afe57724f7bf3210fa87418c513 280w, https://mintcdn.com/ionet-cca8037f/Sa-6uYnlPwRnz7qP/images/docs/io-intelligence/TaaS/TaaS_YourTrainingJobs.png?w=560&fit=max&auto=format&n=Sa-6uYnlPwRnz7qP&q=85&s=e64b577eddb828e6eb8bd60ec49fa0d9 560w, https://mintcdn.com/ionet-cca8037f/Sa-6uYnlPwRnz7qP/images/docs/io-intelligence/TaaS/TaaS_YourTrainingJobs.png?w=840&fit=max&auto=format&n=Sa-6uYnlPwRnz7qP&q=85&s=c97502e5ea382106486a585cd7993fde 840w, https://mintcdn.com/ionet-cca8037f/Sa-6uYnlPwRnz7qP/images/docs/io-intelligence/TaaS/TaaS_YourTrainingJobs.png?w=1100&fit=max&auto=format&n=Sa-6uYnlPwRnz7qP&q=85&s=bf6c8c481688aaeb4a6e874a4b388033 1100w, https://mintcdn.com/ionet-cca8037f/Sa-6uYnlPwRnz7qP/images/docs/io-intelligence/TaaS/TaaS_YourTrainingJobs.png?w=1650&fit=max&auto=format&n=Sa-6uYnlPwRnz7qP&q=85&s=5a08fa3f76f7fada15adc9f782f164f7 1650w, https://mintcdn.com/ionet-cca8037f/Sa-6uYnlPwRnz7qP/images/docs/io-intelligence/TaaS/TaaS_YourTrainingJobs.png?w=2500&fit=max&auto=format&n=Sa-6uYnlPwRnz7qP&q=85&s=6c9a3475669005c9f4a4092b7e6c32cd 2500w" />
</Frame>

## Job Details

Click on a job from the dashboard to open its ***Job Details***. This provides everything you need to track and manage your model training in real time.

At the top of the page are the following buttons and indicators:

* **Download Model** – Available once the job is complete, to download the final model.
* **Abort Training** – Manually stop the job if necessary.
* **Time Remaining** – Displays how much time is left for training to finish.
* **Time Passed** – Shows how long the job has been running.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6273b5b8b8470fe6464fa2c18e916d95a362cc655b24c1c6f34465e92cef8052-Trainin_Model-5.png?fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=34e1fba654180a058683cb27c183a10b" alt="" data-og-width="2516" width="2516" data-og-height="432" height="432" data-path="images/docs/6273b5b8b8470fe6464fa2c18e916d95a362cc655b24c1c6f34465e92cef8052-Trainin_Model-5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6273b5b8b8470fe6464fa2c18e916d95a362cc655b24c1c6f34465e92cef8052-Trainin_Model-5.png?w=280&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=bc075ba89f808c7a6686d9264b302b6d 280w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6273b5b8b8470fe6464fa2c18e916d95a362cc655b24c1c6f34465e92cef8052-Trainin_Model-5.png?w=560&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=814bdbb9af62eaf1b3a8b8d132639944 560w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6273b5b8b8470fe6464fa2c18e916d95a362cc655b24c1c6f34465e92cef8052-Trainin_Model-5.png?w=840&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=e37e15b48415631a58cccf5bbba4c837 840w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6273b5b8b8470fe6464fa2c18e916d95a362cc655b24c1c6f34465e92cef8052-Trainin_Model-5.png?w=1100&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=f40e4312dd3c03d723d43a74c31c5282 1100w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6273b5b8b8470fe6464fa2c18e916d95a362cc655b24c1c6f34465e92cef8052-Trainin_Model-5.png?w=1650&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=9d543e17a44dd4ae7a927624a8afbcbe 1650w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6273b5b8b8470fe6464fa2c18e916d95a362cc655b24c1c6f34465e92cef8052-Trainin_Model-5.png?w=2500&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=063fd8bcc9632aba5e2f5a5f4b59f1c7 2500w" />
</Frame>

### Training Metrics (Charts)

Track your model’s learning performance in real time.

* **Loss Chart** – Shows how training loss decreases over time.

This visual tool allows you to understand if your model is learning effectively - or if it needs adjustments.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b8f13767747274e13e4b3181fb13e9b3af03f142959486a57dde18251eec4742-Trainin_Model-6.jpg?fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=f599dea84a5c5dbb0d6b2b2d7b7f204b" alt="" data-og-width="2505" width="2505" data-og-height="1018" height="1018" data-path="images/docs/b8f13767747274e13e4b3181fb13e9b3af03f142959486a57dde18251eec4742-Trainin_Model-6.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b8f13767747274e13e4b3181fb13e9b3af03f142959486a57dde18251eec4742-Trainin_Model-6.jpg?w=280&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=ccbb0f36828a7ab6b7f6a8e8c5aac8b7 280w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b8f13767747274e13e4b3181fb13e9b3af03f142959486a57dde18251eec4742-Trainin_Model-6.jpg?w=560&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=e7cacc584037dc3090fac0b3e9e566f4 560w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b8f13767747274e13e4b3181fb13e9b3af03f142959486a57dde18251eec4742-Trainin_Model-6.jpg?w=840&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=820e6da1a6a2c209e07ae6c5b1537348 840w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b8f13767747274e13e4b3181fb13e9b3af03f142959486a57dde18251eec4742-Trainin_Model-6.jpg?w=1100&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=4525c576dd29ea6674a34716e9fc51e5 1100w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b8f13767747274e13e4b3181fb13e9b3af03f142959486a57dde18251eec4742-Trainin_Model-6.jpg?w=1650&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=52ef9b854128c04a671ccb6fc2074a22 1650w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b8f13767747274e13e4b3181fb13e9b3af03f142959486a57dde18251eec4742-Trainin_Model-6.jpg?w=2500&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=8e14758203fe3c7928831ce088f9f75f 2500w" />
</Frame>

### Training Details

A summary of the key information for the training job is provided as follows:

* **Status** – Created, Deploying, Deploy Failed, Training Failed, Training, or Completed.
* **Date Created**
* **Model Name**
* **Training Method**
* **Base Model Used**
* **Dataset Used**
* **User Tag** - Custom label or identifier.
* **End Date** - If completed or aborted.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7b3448dcffb21f3fa78a20022fb591b792549f0196dec1a5eb09e55b7127d878-Trainin_Model-7.jpg?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=4e5324b03e9d9568fe330c76f8074a48" alt="" data-og-width="2470" width="2470" data-og-height="939" height="939" data-path="images/docs/7b3448dcffb21f3fa78a20022fb591b792549f0196dec1a5eb09e55b7127d878-Trainin_Model-7.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7b3448dcffb21f3fa78a20022fb591b792549f0196dec1a5eb09e55b7127d878-Trainin_Model-7.jpg?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=7f30698c6f964093d777b8211a753cd9 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7b3448dcffb21f3fa78a20022fb591b792549f0196dec1a5eb09e55b7127d878-Trainin_Model-7.jpg?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=10e661c346063e22821bbacef7dfee77 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7b3448dcffb21f3fa78a20022fb591b792549f0196dec1a5eb09e55b7127d878-Trainin_Model-7.jpg?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=060e678a755f4f553e721328719bfcd3 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7b3448dcffb21f3fa78a20022fb591b792549f0196dec1a5eb09e55b7127d878-Trainin_Model-7.jpg?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=ff2046965da31baaf7bbfcd25452d026 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7b3448dcffb21f3fa78a20022fb591b792549f0196dec1a5eb09e55b7127d878-Trainin_Model-7.jpg?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=5b09a8b1abd5374898d1af7b22d78e60 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7b3448dcffb21f3fa78a20022fb591b792549f0196dec1a5eb09e55b7127d878-Trainin_Model-7.jpg?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=138f209c6c9b544b6701873b267daecf 2500w" />
</Frame>

### Training Logs

***Training Logs*** provide visibility into what occurs behind the scenes during the model training process. They contain a detailed list of steps, events, and status updates throughout the job’s lifecycle, making them especially useful for debugging, monitoring, or maintaining transparency.

Click the **Download Logs** button to save them locally for review or record-keeping.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/959697a437df64529dd8de1d4c318ec71bb41bf8cbb697a08714e18f259f216e-Trainin_Model-8_2.jpg?fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=1f11e7ed0fa23df734765d3d3a1d1c80" alt="" data-og-width="2498" width="2498" data-og-height="857" height="857" data-path="images/docs/959697a437df64529dd8de1d4c318ec71bb41bf8cbb697a08714e18f259f216e-Trainin_Model-8_2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/959697a437df64529dd8de1d4c318ec71bb41bf8cbb697a08714e18f259f216e-Trainin_Model-8_2.jpg?w=280&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=496194dadaa32100dfdb393d84bcd8fa 280w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/959697a437df64529dd8de1d4c318ec71bb41bf8cbb697a08714e18f259f216e-Trainin_Model-8_2.jpg?w=560&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=dae430a5a6468a5e09b7a34219494092 560w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/959697a437df64529dd8de1d4c318ec71bb41bf8cbb697a08714e18f259f216e-Trainin_Model-8_2.jpg?w=840&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=0dd743b5d00f4620cfda0ccfed56798d 840w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/959697a437df64529dd8de1d4c318ec71bb41bf8cbb697a08714e18f259f216e-Trainin_Model-8_2.jpg?w=1100&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=dc62595887a9dd1d7a17d0279a7fabad 1100w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/959697a437df64529dd8de1d4c318ec71bb41bf8cbb697a08714e18f259f216e-Trainin_Model-8_2.jpg?w=1650&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=cdd2fcb987104063aa81c14d3e9f2bb2 1650w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/959697a437df64529dd8de1d4c318ec71bb41bf8cbb697a08714e18f259f216e-Trainin_Model-8_2.jpg?w=2500&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=2a065ac05e0d36e51c8d3576689c9fa7 2500w" />
</Frame>
