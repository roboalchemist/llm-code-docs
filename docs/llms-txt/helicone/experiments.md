# Source: https://docs.helicone.ai/guides/cookbooks/experiments.md

# How to Run LLM Prompt Experiments

> Run experiments with historical datasets to test, evaluate, and improve prompts over time while preventing regressions in production systems.

<Warning>
  We are deprecating the Experiments feature and it will be removed from the platform on September 1st, 2025.
</Warning>

## Feature Highlight

* Create as many prompt versions as you like, without impacting production data.
* Evaluate the outputs of your new prompt (and have data to back you up 📈).
* Save cost by testing on specific datasets and making fewer calls to providers like OpenAI. 🤑

## Running your first prompt experiment

To start an experiment, first, go to the [Prompts](https://www.helicone.ai/prompts) tab and select a prompt.

<Steps>
  <Step title="Click `Start Experiment`">
    On the top right, click `Start Experiment`.

    <Frame>
      <img src="https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/start-button.png?fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=a9189c9e766f12164ba8f0f14dd1950c" alt="Start button in the Prompts tab for initiating an experiment in Helicone." data-og-width="1868" width="1868" data-og-height="1118" height="1118" data-path="images/use-cases/experiments/start-button.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/start-button.png?w=280&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=9d6d336280162b2ed89f41ee08f3365e 280w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/start-button.png?w=560&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=a3e45e39df1c3cef666f885769be1238 560w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/start-button.png?w=840&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=6dfccce6746e9baf139a42f947f23ef0 840w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/start-button.png?w=1100&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=796b1663bdc0bef762c3239884a37f70 1100w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/start-button.png?w=1650&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=ce131936f8fffc03591d7120085a6e36 1650w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/start-button.png?w=2500&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=b759667a19af8199d9aeb9dc6255c96f 2500w" />
    </Frame>
  </Step>

  <Step title="Select the base prompt">
    Select a base prompt and click `Continue`. You can edit the prompt in the
    next step.

    <Tip>
      To run an experiment on the production prompt, look for the `production`
      tag.
    </Tip>

    <Frame>
      <img src="https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/select-prompt.png?fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=953a43ec336fba471298b8f78cc69b83" alt="Selecting a base prompt to start an experiment in Helicone." data-og-width="1868" width="1868" data-og-height="1118" height="1118" data-path="images/use-cases/experiments/select-prompt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/select-prompt.png?w=280&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=173c5ce6cd59d76265393262c838a392 280w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/select-prompt.png?w=560&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=8b04e17a3b1612550e281eed90fb273c 560w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/select-prompt.png?w=840&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=b290ed7ee6af1dc1992efb2f1c1c11a8 840w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/select-prompt.png?w=1100&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=1cbffa457c95c7d0b4d87cbf1c89ab40 1100w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/select-prompt.png?w=1650&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=e088343ed7847dfb5a61eddde589e048 1650w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/select-prompt.png?w=2500&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=d77327324bd179ad5ec4e0ccfda37ea5 2500w" />
    </Frame>
  </Step>

  <Step title="Edit the prompt">
    Your changes will not affect the original prompt, but rather create a new
    one to test your experiment on.

    <Frame>
      <img src="https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/edit-prompt.png?fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=c4ac69d32c361a18b76a0b242071c583" alt="Editing a prompt without affecting the original prompt in production." data-og-width="1868" width="1868" data-og-height="1118" height="1118" data-path="images/use-cases/experiments/edit-prompt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/edit-prompt.png?w=280&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=a6bce4a2960eadf84c6057bf24b72f1e 280w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/edit-prompt.png?w=560&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=716709b7745cf0c0cf4e79ee95543eba 560w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/edit-prompt.png?w=840&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=030f303fb8763b389b92fbc969feb979 840w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/edit-prompt.png?w=1100&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=864ff9ea02ce3127404ad70ee20fd8a1 1100w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/edit-prompt.png?w=1650&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=dd7b907c37e320b534d06020f45e0d3d 1650w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/edit-prompt.png?w=2500&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=a485b395ca602e61c874384e6b147c54 2500w" />
    </Frame>
  </Step>

  <Step title="Configure your experiment">
    Select the dataset, model and provider keys.

    <Tip>
      To run your experiment on a random dataset, click `Generate random
            dataset`. We will pick up to 10 random data from your existing
      requests.{" "}
    </Tip>

    <Frame>
      <img src="https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/config.png?fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=26103e7178268ef560348b2bc85d30c7" alt="Configuring an experiment with a different dataset, model, and provider keys in Helicone." data-og-width="1868" width="1868" data-og-height="1118" height="1118" data-path="images/use-cases/experiments/config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/config.png?w=280&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=d5dbe687b1d3c2f7e5eba7e97e786faa 280w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/config.png?w=560&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=5d6f57053bd9e7ff9b7542d31130c030 560w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/config.png?w=840&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=02d8255df04486fdbaf0e1a8b9e663e6 840w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/config.png?w=1100&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=07ab01513874f310431ed952193d6e28 1100w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/config.png?w=1650&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=e4f3cd5fc5d5dde0298a2df2ca2ef949 1650w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/config.png?w=2500&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=9e0a05149eaf1cec144f6ea9edce2539 2500w" />
    </Frame>
  </Step>

  <Step title="Confirm and run">
    The `Diff Viewer` compares your new prompt to the base prompt that you
    selected.

    <Frame>
      <img src="https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/confirm.png?fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=af9cebbbd3b5d07f159e29fe598b60f3" alt="Confirming changes to your prompt in Helicone's Diff Viewer before running an experiment. " data-og-width="1868" width="1868" data-og-height="1118" height="1118" data-path="images/use-cases/experiments/confirm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/confirm.png?w=280&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=5ac87a3df6862b83bdcccc290951e79f 280w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/confirm.png?w=560&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=95e128a20401eecfaadd5e1c8acf286d 560w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/confirm.png?w=840&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=0858a6489e369ed62c3b54f30a19237d 840w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/confirm.png?w=1100&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=8898d3f2df4c9a71666022242c8323d6 1100w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/confirm.png?w=1650&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=b0fa7e3f98c49dea9836350e49edabe5 1650w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/experiments/confirm.png?w=2500&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=9e9c053687c35c4b53f2cf65daaa7ac3 2500w" />
    </Frame>
  </Step>

  <Step title="View outputs">
    Once the experiment is finished, click on it to see a list of inputs and the
    associated outputs from the base prompt and the experiment.

    <Frame>
      <img src="https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/experiments/view.png?fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=c8f5436ad8ebff5dd21677790e71eac4" alt="Comparing the outputs of an experiment compared to the original prompt in Helicone." data-og-width="1868" width="1868" data-og-height="1118" height="1118" data-path="images/use-cases/experiments/view.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/experiments/view.png?w=280&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=9720a87471ae4056b9bead51ecc12ecd 280w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/experiments/view.png?w=560&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=8fb7bd1d8d5f41e014b95a2c98fff966 560w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/experiments/view.png?w=840&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=98a4042c71041ab68f1a940f14b83bdd 840w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/experiments/view.png?w=1100&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=4723a138b2d99f6ef779aeb78acc4bcb 1100w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/experiments/view.png?w=1650&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=cdaafe46c77c86b71c9b44eadb159c8d 1650w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/use-cases/experiments/view.png?w=2500&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=d9f02bc853596323f0779d0cb233fcd7 2500w" />
    </Frame>
  </Step>
</Steps>
