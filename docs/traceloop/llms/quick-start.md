# Source: https://www.traceloop.com/docs/prompts/quick-start.md

# Source: https://www.traceloop.com/docs/playgrounds/quick-start.md

# Source: https://www.traceloop.com/docs/datasets/quick-start.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Quick Start

Datasets are simple data tables that you can use to manage your data for experiments and evaluation of your AI applications.
Datasets are available in the SDK, and they enable you to create versioned snapshots for reproducible testing.

<Frame>
  <img className="block dark:hidden" src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/dataset/dataset-list-light.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=68d309644007054d2c6d59e30f9bff65" data-og-width="3266" width="3266" data-og-height="504" height="504" data-path="img/dataset/dataset-list-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/dataset/dataset-list-light.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=df9fd9ac97d1f77a1b619993afc5a257 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/dataset/dataset-list-light.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=0e3d9f932d21bff8156e03bd9c3e73a2 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/dataset/dataset-list-light.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=db41fe7734a4bf693c7aec25ebd83f85 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/dataset/dataset-list-light.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=292981a46bd2c1b476dc07c6de5be7b2 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/dataset/dataset-list-light.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=50c4edb6436cc75b5ef36a8b20e1b56b 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/dataset/dataset-list-light.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=c48d6fb122d9224b499550effdefbbbc 2500w" />

  <img className="hidden dark:block" src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/dataset/dataset-list-dark.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=6b3d9e87aef25951d5ac9919618117c5" data-og-width="3260" width="3260" data-og-height="504" height="504" data-path="img/dataset/dataset-list-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/dataset/dataset-list-dark.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=952dc18d44ab8c1c446916705c0c731b 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/dataset/dataset-list-dark.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=9190386ded054e8837617b5ebaea00f4 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/dataset/dataset-list-dark.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=9a4f3f08e48451bea85f57868361d1cf 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/dataset/dataset-list-dark.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=ccf5f86e4630c35378a13d44d259b322 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/dataset/dataset-list-dark.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=a814a4576326e39ce6e109432de72940 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/dataset/dataset-list-dark.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=011f67d16f6e91ee75fb82e787364155 2500w" />
</Frame>

<Steps>
  <Step title="Create a new dataset">
    Click **New Dataset** to create a dataset, give it a descriptive name that reflects its purpose or use case, add a description to help your team understand its context, and provide a slug that allows you to use the dataset in the SDK.
  </Step>

  <Step title="Add your data">
    Add rows and columns to structure your dataset.
    You can add different column types:

    * **Text**: For prompts, model responses, or any textual data
    * **Number**: For numerical values, scores, or metrics
    * **Boolean**: For true/false flags or binary classifications

    <Tip>
      Use meaningful column names that clearly describe what each field contains,
      making it easier to work with your dataset in code, ensure clarity when using evaluators, and collaborate with team members.
    </Tip>
  </Step>

  <Step title="Publish your dataset version">
    <Frame>
      <img className="block dark:hidden" src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/dataset/dataset-view-light.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=7b689bac69a6c16d58ccd89b0067dea1" data-og-width="3298" width="3298" data-og-height="600" height="600" data-path="img/dataset/dataset-view-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/dataset/dataset-view-light.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=c938347ad661bb64d658f38b20e8179f 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/dataset/dataset-view-light.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=0dc82764ba10265866d420650635a003 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/dataset/dataset-view-light.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=2c817c30c57c255f620f44079e35442b 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/dataset/dataset-view-light.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=2f020ff033baaa0d6074c61266fef1d4 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/dataset/dataset-view-light.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=1875e785ee47d014d627e02cb0ebe07f 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/dataset/dataset-view-light.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=19e03c3f00fc2ad34d6ef4502342cc46 2500w" />

      <img className="hidden dark:block" src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/dataset/dataset-view-dark.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=46aacf3c5fb12e1964b6af7f4497c9d0" data-og-width="3270" width="3270" data-og-height="594" height="594" data-path="img/dataset/dataset-view-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/dataset/dataset-view-dark.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=0fe4e0b9f202e48568ce6104e0a95364 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/dataset/dataset-view-dark.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=4e223bf675534280e854f6b9bc51d803 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/dataset/dataset-view-dark.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=734d8539842ca3008e62055e3a6a641b 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/dataset/dataset-view-dark.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=49cff0daa2c010610ddad09d050848f7 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/dataset/dataset-view-dark.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=edc1bb4a0e763f1f52bc7d8b703fd774 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/dataset/dataset-view-dark.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=2f822bac08383bf22c75da9b3dd5532b 2500w" />
    </Frame>

    Once you're satisfied with your dataset structure and data:

    1. Click **Publish Version** to create a stable snapshot
    2. Published versions are immutable
    3. Publish versions are accessible in the SDK
  </Step>

  <Step title="View your version history">
    You can access all published versions of your dataset by opening the version history modal. This allows you to:

    * Compare different versions of your dataset
    * Track changes over time
    * Switch between versions
  </Step>
</Steps>
