# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-llm-fine-tune/taking-action.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Taking Action

> Take actionable steps in Galileo LLM Fine-Tune to address model performance issues, refine outputs, and achieve targeted AI improvements.

Once you've identified [issues in your data](/galileo/gen-ai-studio-products/galileo-llm-fine-tune/console-walkthrough), Galileo empowers you to take action on them. Galileo supports the following actions:

<img src="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-taking-action.png?fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=47119704a9ea2b880133470e69ec61bf" alt="" data-og-width="1868" width="1868" data-og-height="272" height="272" data-path="images/finetune-taking-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-taking-action.png?w=280&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=62b4e43be31475992ae02ff65a7e1487 280w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-taking-action.png?w=560&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=d7e80c2278c8881473772d1159ac3b50 560w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-taking-action.png?w=840&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=ed953402624d9c757b07cca8f6a78ea9 840w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-taking-action.png?w=1100&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=6423d91d774c652d1d9a22d37a90ecc4 1100w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-taking-action.png?w=1650&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=c9d9488a5686fda75d90abd1e373e7aa 1650w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-taking-action.png?w=2500&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=b7b89ea47184951d283d1fd63976c8a9 2500w" />

* Find Similar - Need to add more "similar" samples to your dataset? Find similar helps you find samples from other splits or from unlabeled datasets.

* Export - Download the selected samples as a CSV file, to S3/GCS, or programmatically.

* Removing Samples - Remove samples from your dataset. This is useful if you've found garbage samples or are looking to reduce your dataset size.

* Editing Samples - Edit the Target (Expected Output) of your sample. Use this if you've found an error in your Target.

* Send to Annotators - Do you use a labeling tool to manage your annotation work? Send to Annotators leverages our labeling integrations to hook into your annotation tool. Send your samples to your annotators for relabeling.

### Edits Cart

The **Edits Cart** serves as the single place to track all your changes. From here you can track who's done what changes, review their work, and download "clean" versions of your dataset.

<img src="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-taking-action-cart.png?fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=c4afe51b4f74884cc6d66f6ad80f864c" alt="" data-og-width="2500" width="2500" data-og-height="668" height="668" data-path="images/finetune-taking-action-cart.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-taking-action-cart.png?w=280&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=7f1ab23f75de77fc08951ed7ae9024e0 280w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-taking-action-cart.png?w=560&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=bb4f38003af4a5fe9e802b77daa9921a 560w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-taking-action-cart.png?w=840&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=545289dbfdffdb6dc4ebe1308e00150c 840w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-taking-action-cart.png?w=1100&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=8455dcd30b6e18c14c896bb1e9cb80bf 1100w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-taking-action-cart.png?w=1650&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=b9e649149c1975adffd7ba13aba16240 1650w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-taking-action-cart.png?w=2500&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=9efb0c2c476309ddcc5c7b7db62589e8 2500w" />

### Retrain

Once you're satisfied with the changes you've made to your dataset. You can export the "clean" dataset, and retrain your model to see your model improvements.
