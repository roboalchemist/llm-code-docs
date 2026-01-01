# Source: https://www.traceloop.com/docs/prompts/registry.md

# Prompt Registry

> Manage your prompts on the Traceloop platform

Traceloop's Prompt Registry is where you manage your prompts. You can create, edit, evaluate and deploy prompts to your environments.

## Configuring Prompts

<Frame>
  <img className="block dark:hidden" src="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-configuration-light.png?fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=f02ab8b4912d10fd398785e7aaeb524c" data-og-width="3024" width="3024" data-og-height="1808" height="1808" data-path="img/prompt-configuration-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-configuration-light.png?w=280&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=416ca2bcdfdc4ad52cbbe5b5c766b4a2 280w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-configuration-light.png?w=560&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=926fbcd30c669b149669216c48abe69b 560w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-configuration-light.png?w=840&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=f914e3de83f13357428c6804eb68d957 840w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-configuration-light.png?w=1100&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=5b71e5380013daf711f1df27a32a86b4 1100w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-configuration-light.png?w=1650&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=d3f399364ee6ce9937daabebf12f87a4 1650w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-configuration-light.png?w=2500&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=4f1aaae2a34e76d016560813e3768f2b 2500w" />

  <img className="hidden dark:block" src="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-configuration-dark.png?fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=7fc4c5cebcbef9a037d36738354afc7a" data-og-width="3024" width="3024" data-og-height="1809" height="1809" data-path="img/prompt-configuration-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-configuration-dark.png?w=280&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=085af81ba4452f848ed2d9c97fc96a90 280w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-configuration-dark.png?w=560&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=b544c148ed3477146d675c31764c7489 560w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-configuration-dark.png?w=840&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=3474b0b11a2701bbe9ddb18276672891 840w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-configuration-dark.png?w=1100&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=0e45b2d71090f815ace968b3338b6b85 1100w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-configuration-dark.png?w=1650&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=e2eefd1a01cd813ccac9b2f6794dcd2f 1650w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-configuration-dark.png?w=2500&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=c51e8dd61c6dc53fd6724bf513a145f4 2500w" />
</Frame>

The prompt configuration is composed of two parts:

* The prompt template (system and/or user prompts)
* The model configuration (temperature, top\_p, etc.)

<Tip>
  Your prompt template can include variables. Variables are defined according to
  the syntax of the parser specified. For example, if using `jinjia2` the syntax
  will be `{{ variable_name }}`. You can then pass variable values to the SDK
  when calling `get_prompt`. See the example on the [SDK
  Usage](/prompts/sdk-usage) section.
</Tip>

Initially, prompts are created in `Draft Mode`. In this mode, you can make changes to the prompt and configuration. You can also test your prompt in the playground (see below).

## Testing a Prompt Configuration (Prompt Playground)

By using the prompt playground you can iterate and refine your prompt before deploying it.

<Frame>
  <img className="block dark:hidden" src="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-playground-light.png?fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=c538ba31864dc369f5f53787eff52edb" data-og-width="3024" width="3024" data-og-height="1809" height="1809" data-path="img/prompt-playground-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-playground-light.png?w=280&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=ebf2b8051158894bb256a00f9e576375 280w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-playground-light.png?w=560&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=71b74bfe4c021669a2135a8e210b967d 560w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-playground-light.png?w=840&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=827ed91ff327ec0e2c7dcc82d1f5499e 840w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-playground-light.png?w=1100&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=7a12f2391f3116916e7f1bc20588f463 1100w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-playground-light.png?w=1650&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=06fd29dcf053ff6a892983455b147fe3 1650w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-playground-light.png?w=2500&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=9a060c5a835279d2da2d77481912aac0 2500w" />

  <img className="hidden dark:block" src="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-playground-dark.png?fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=9fcac82a6348ba53fa431744b80b4743" data-og-width="3021" width="3021" data-og-height="1808" height="1808" data-path="img/prompt-playground-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-playground-dark.png?w=280&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=77eee38335a603d0b5b57d54a330ce87 280w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-playground-dark.png?w=560&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=d90439f0a836c19ee3088d5ffc199f39 560w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-playground-dark.png?w=840&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=084eaba6e309f37f20f8380d964d77a7 840w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-playground-dark.png?w=1100&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=4856f559484f10bf58e457229340b82f 1100w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-playground-dark.png?w=1650&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=e60a29141ab734a4266708710d60267f 1650w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-playground-dark.png?w=2500&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=9bd56097f5b2bcdd7964a317bacbc367 2500w" />
</Frame>

Simply click on the `Test` button in the playground tab at the bottom of the screen.

If your prompt includes variables, then you need to define values for them before testing.
Choose `Variables` in the right side bar and assign a value to each.

Once you click the `Test` button your prompt template will be rendered with the values you provided and will be sent to the configured LLM with the model configuration defined.
The completion response (including token usage) will be displayed in the playground.

## Deploying Prompts

<Frame>
  <img className="block dark:hidden" src="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-deployment-light.png?fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=8f2584bf665c9147ad09d334f214d599" data-og-width="3024" width="3024" data-og-height="1808" height="1808" data-path="img/prompt-deployment-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-deployment-light.png?w=280&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=59bff189cbbb2bab93843889ac66041f 280w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-deployment-light.png?w=560&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=8898148c5b1306c853dba35ed23a58b3 560w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-deployment-light.png?w=840&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=9094fbfc405493c8ddbbceee5bccfd93 840w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-deployment-light.png?w=1100&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=3496570a631ac716d436d14184e890c6 1100w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-deployment-light.png?w=1650&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=c419b7fb786e7058ffaba83b86492575 1650w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-deployment-light.png?w=2500&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=820f521e61e9f565e8522d336e98eb6e 2500w" />

  <img className="hidden dark:block" src="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-deployment-dark.png?fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=e4b36122965eeac6d561ad7796d7a8d3" data-og-width="3024" width="3024" data-og-height="1805" height="1805" data-path="img/prompt-deployment-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-deployment-dark.png?w=280&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=6e864a00d18e77ad702a86b3ffbf312d 280w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-deployment-dark.png?w=560&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=482b98719fbc9ed005be5f0f28fdf328 560w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-deployment-dark.png?w=840&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=5d8f1199ea7f6a251602439462cd07c8 840w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-deployment-dark.png?w=1100&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=067833165557412eecf0eca8f420f2ef 1100w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-deployment-dark.png?w=1650&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=49b78293de15fe20c2ebe698074d8b4e 1650w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/prompt-deployment-dark.png?w=2500&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=92f3f0184809fbd233f8d0fcdf0d9fd4 2500w" />
</Frame>

Draft mode prompts can only be deployed to the `development` environment.

Once you are satisfied with the prompt, you can publish it and make it available to deploy in all environments.
Once published, the prompt version cannot be edited anymore.

Choose the `Deploy` Tab to navigate to the deployments page for your prompt.

Here, you can see all recent prompt versions, and which environments they are deployed to.
Simply click on the `Deploy` button to deploy a prompt version to an environment. Similarly, click `Rollback` to revert to a previous prompt version for a specific environment.

<Note>
  As a safeguard, you cannot deploy a prompt to the `Staging` environment before
  first deploying it to `Development`. Similarly, you cannot deploy to
  `Production` without first deploying to `Staging`.
</Note>

To fetch prompts from a specific environment, you must supply that environment's API key to the Traceloop SDK. See the [SDK Configuration](/openllmetry/integrations/traceloop) for details

## Prompt Versions

If you want to make changes to your prompt after deployment, simply create a new version by clicking on the `New Version` button. New versions will be created in `Draft Mode`.

<Warning>
  If you change the names of variables or add/remove existing variables, you
  will be required to create a new prompt.
</Warning>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://www.traceloop.com/docs/llms.txt