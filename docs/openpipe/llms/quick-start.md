# Source: https://docs.openpipe.ai/getting-started/quick-start.md

# Source: https://docs.openpipe.ai/features/fine-tuning/quick-start.md

# Source: https://docs.openpipe.ai/features/evaluations/quick-start.md

# Source: https://docs.openpipe.ai/features/dpo/quick-start.md

# Source: https://docs.openpipe.ai/features/datasets/quick-start.md

# Source: https://docs.openpipe.ai/features/criteria/quick-start.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.openpipe.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Criteria Quick Start

> Create and align your first criterion.

Criteria are a reliable way to detect and correct mistakes in LLM output. Criteria can be used when defining LLM evaluations, improving data quality, and for [runtime evaluation](/features/criteria/api#runtime-evaluation) when generating **best of N** samples.
This tutorial will walk you through creating and aligning your first criterion.

<Note>
  <b>Before you begin:</b> Before creating your first criterion, you should identify an issue with
  your model's output that you want to detect and correct. You should also have either an OpenPipe
  [dataset](/features/datasets/overview) or a [JSONL
  file](/features/criteria/alignment-set#importing-from-a-jsonl-file) containing several rows of
  data that exhibit the issue, and several that don't.
</Note>

### Creating a Criterion

<Steps>
  <Step title="Open the creation modal">
    Navigate to the **Criteria** tab and click the **New Criterion** button.
    The creation modal will open with a default prompt and judge model.

    <Frame>    <img src="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/create-criterion.png?fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=eb200d1409b0cffa44558aefcefac42c" alt="" data-og-width="1242" width="1242" data-og-height="1678" height="1678" data-path="images/features/criteria/create-criterion.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/create-criterion.png?w=280&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=d059240baa5a78fce91e94704442d105 280w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/create-criterion.png?w=560&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=48d65dc4db58e96a2ab7996b13dfc221 560w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/create-criterion.png?w=840&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=94345158e1bc6678269c15424026c0cd 840w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/create-criterion.png?w=1100&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=93da7135575961af8c0f70a6a1dc0a27 1100w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/create-criterion.png?w=1650&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=0f4f4ab5dc035d0190bfa2de4f6aac03 1650w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/create-criterion.png?w=2500&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=8af6be0c6f5745943de68c0cdd592d20 2500w" /></Frame>

    By default, each of the following fields will be templated into the criterion's prompt when assigning a judgement to an output:

    * `messages` *(optional):* The messages used to generate the output
    * `tools` *(optional):* The tools used to generate the output
    * `tool_choice` *(optional):* The tool choice used to generate the output
    * `output` *(required):* The chat completion object to be judged

    Many criteria do not require all of the input fields, and some may judge based soley on the `output`. You can exclude fields by removing them from the **Templated Variables** section.
  </Step>

  <Step title="Draft an initial prompt">
    Write an initial LLM prompt with basic instructions for identifying rows containing
    the issue you want to detect and correct. Don't worry about engineering a perfect
    prompt, you'll have a chance to improve it during the alignment process.

    As an example, if you want to detect rows in which the model's output is in a different language than the input,
    you might write a prompt like this:

    ```
    Mark the criteria as passed if the input and output are the same language.
    Mark it as failed if they are in different languages.
    ```

    <Tip>
      Make sure to use the terms `input`, `output`, `passed`, and `failed` in your prompt to match our
      internal templating.
    </Tip>

    Finally, import a few rows (we recommend at least 30) into an alignment set for the criterion.
  </Step>

  <Step title="Confirm creation">
    Click **Create** to create the criterion and run the initial prompt against the imported alignment set.
    You'll be redirected to the criterion's alignment page.

    <Frame>    <img src="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/overview.png?fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=24b50bd6b8388bffbd33261e23670910" alt="" data-og-width="2556" width="2556" data-og-height="1712" height="1712" data-path="images/features/criteria/overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/overview.png?w=280&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=93166a8b6614eb1e1ef4cf5fbe9f2cad 280w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/overview.png?w=560&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=901e3ff8482cce4c0620b8f4a01c4b61 560w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/overview.png?w=840&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=a9a0584e2939d2b45caa166b6f153d7d 840w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/overview.png?w=1100&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=f91532337ee5e1a5977441ac63e9b61c 1100w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/overview.png?w=1650&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=ceedf334cc0c9dd2a45c73fc156622af 1650w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/overview.png?w=2500&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=8aae63201c43ac2b4f35c81523da41e8 2500w" /></Frame>
  </Step>
</Steps>

### Aligning a Criterion

Ensuring your criterion's judgements are reliable involves two simple processes:

* Manually labeling outputs
* Refining the criterion

<Steps>
  <Step title="Manually labeling outputs">
    In order to know whether you agree with your criterion's judgements, you'll need to label some data yourself.
    Use the Alignment UI to manually label each output with `PASS` or `FAIL` based on the criterion. Feel free to `SKIP` outputs you aren't sure about and come back to them later.

    <Frame>    <img src="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/manually-label.png?fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=ef611fa04c4085111b5108505d6029b4" alt="" data-og-width="3000" width="3000" data-og-height="1718" height="1718" data-path="images/features/criteria/manually-label.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/manually-label.png?w=280&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=d635125cb9a0631982ec45ebd9d36bca 280w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/manually-label.png?w=560&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=9c21cf6266e7fe25d354526d13d1bd07 560w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/manually-label.png?w=840&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=77948ddbb14827e45fdb21ee54280868 840w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/manually-label.png?w=1100&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=5e0e42d95566e03e7b0bb347d18a59ae 1100w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/manually-label.png?w=1650&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=86bcb6243abcc0ba79d1ca8cc43d6726 1650w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/manually-label.png?w=2500&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=5e453888c5691823e0c1634c01bb0ebe 2500w" /></Frame>

    Try to label at least 30 rows to provide a reliable estimate of the LLM's precision and recall.
  </Step>

  <Step title="Refining the criterion">
    As you record your own judgements, alter the criterion's prompt and judge model to align its judgements with your own.

    <Frame>    <img src="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/edit-criterion.png?fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=972986b1aaf50bca638a567ce4d75abf" alt="" data-og-width="1192" width="1192" data-og-height="738" height="738" data-path="images/features/criteria/edit-criterion.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/edit-criterion.png?w=280&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=6c5c647701514e7499d213845c7f3f2e 280w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/edit-criterion.png?w=560&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=beacddcb134d48fa9a3ceb9527366c4c 560w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/edit-criterion.png?w=840&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=d2381cef9e62c1a3763a970dec722b11 840w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/edit-criterion.png?w=1100&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=8cc554e651d177b4e5c7a1ab0c23b58f 1100w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/edit-criterion.png?w=1650&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=a28a762d15e4fe266c2c0bcd17e8138f 1650w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/edit-criterion.png?w=2500&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=67f7f97bd0f7f36d40851d2fb14dc7bb 2500w" /></Frame>

    Investing time in a good prompt and selecting the best judge model pays dividends.
    High-quality LLM judgements help you quickly identify rows that fail the criterion, speeding up the process of manually labeling rows.

    <Frame>    <img src="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/llm-judgement.png?fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=915f6e9a72e3f2534bde9a271f13c84e" alt="" data-og-width="1440" width="1440" data-og-height="998" height="998" data-path="images/features/criteria/llm-judgement.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/llm-judgement.png?w=280&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=21b1a7dbad0d2e5e802f56e12b3ba402 280w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/llm-judgement.png?w=560&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=320ad841432bde64f584c1ac7266342a 560w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/llm-judgement.png?w=840&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=3fd670006f370cca44ebf65038a91830 840w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/llm-judgement.png?w=1100&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=0bc067850a7aa6fd37c7b529629bbebb 1100w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/llm-judgement.png?w=1650&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=1750409afff037e7f185e1007c38a4e1 1650w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/llm-judgement.png?w=2500&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=07d44719d1f73d4e6c21f673bb6f1215 2500w" /></Frame>

    As you improve your criterion prompt, you'll notice your [alignment stats](/features/criteria/alignment-set#alignment-stats) improving.
    Once you've labeled at least 30 rows and are satisfied with the precision and recall of your LLM judge, the criterion is ready to be deployed!
  </Step>
</Steps>

### Deploying a Criterion

The simplest way to deploy a criterion is to create a criterion eval. Unlike head to head evals, criterion evals are not pairwise comparisons.
Instead, they evaluate the quality of one or more models' output according to a specific criterion.

First, navigate to the Evals tab and click **New Evaluation** -> **Add criterion eval**.

Pick the models to evaluate and the test dataset on which to evaluate them. Next, select the criterion you would like to judge your models against.
The judge model and prompt you defined when creating the criterion will be used to judge individual outputs from your models.

<Frame><img src="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/create-criterion-eval.png?fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=d775f8f08340f9a1f308f2eed0d59900" alt="" data-og-width="1860" width="1860" data-og-height="1400" height="1400" data-path="images/features/criteria/create-criterion-eval.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/create-criterion-eval.png?w=280&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=3cadba3d53143fc3fafd45f92f6985c4 280w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/create-criterion-eval.png?w=560&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=ebe495d30075ce25da499756087ddf34 560w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/create-criterion-eval.png?w=840&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=4dfae257583c13fd13aabf33c1b8b746 840w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/create-criterion-eval.png?w=1100&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=5ac45c62cbb864a0d26343135e3660dc 1100w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/create-criterion-eval.png?w=1650&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=2b18161839377203d0c7811a5252973f 1650w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/create-criterion-eval.png?w=2500&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=8dce12f2e175fdd600f57be0560c67a6 2500w" /></Frame>

Finally, click **Create** to run the evaluation. Just like that, you're be able to view evaluation results based on aligned LLM judgements!

<Frame><img src="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/criterion-eval-results.png?fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=4f7a0a4d8502818aacc0b23104825de7" alt="" data-og-width="2548" width="2548" data-og-height="778" height="778" data-path="images/features/criteria/criterion-eval-results.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/criterion-eval-results.png?w=280&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=3ae4f896c9b2adea05802a12ace6be0a 280w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/criterion-eval-results.png?w=560&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=9e88751f489d0bcaa42a496b33f0399c 560w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/criterion-eval-results.png?w=840&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=b63e2c8034b48880207b6e693be6da93 840w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/criterion-eval-results.png?w=1100&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=c412b77b15f7f57322857107cb0dc434 1100w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/criterion-eval-results.png?w=1650&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=c1d9fe577cd57adc9ed686c66b6e7edf 1650w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/criteria/criterion-eval-results.png?w=2500&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=c7c2339530ecc6363e202a33c8feffa9 2500w" /></Frame>
