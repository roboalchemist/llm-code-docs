# Source: https://flatfile.com/docs/getting-started/quickstart/autobuild.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started with AutoBuild

> Get up and running with Flatfile in minutes using AutoBuild to create a complete data import solution

## What is AutoBuild?

The easiest way to get started with Flatfile is using AutoBuild.

With AutoBuild, you can transform existing import templates or documentation into a fully
functional Flatfile app in minutes. Simply drop your example files into AutoBuild, and it will automatically create and deploy a [Blueprint](/core-concepts/blueprints) (for schema definition) and a [Listener](/core-concepts/listeners) (for validations and transformations) to your Flatfile [App](/core-concepts/apps).

Once you've started with AutoBuild, you can always download your Listener code and continue building with code from there!

## Setting Up Your Account

To get started, you'll need to [sign up for a Flatfile account](https://platform.flatfile.com/oauth/login).

During account setup, enter your company name and select "Start with an existing template or project file."

<Frame>
  <img src="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/account_setup.png?fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=a1d956d85f8e9b870fb4056564bb77a5" width="476" data-og-width="952" data-og-height="1036" data-path="getting-started/quickstart/assets/account_setup.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/account_setup.png?w=280&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=027f7be155652ebf54a4dafc87d28598 280w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/account_setup.png?w=560&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=484d905d507536b5766882c432624e79 560w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/account_setup.png?w=840&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=08d464f5a4d8053d82cf0a9aa5c5e37a 840w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/account_setup.png?w=1100&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=932be7640ef19674721df4d8631abee7 1100w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/account_setup.png?w=1650&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=f9061ca76fc72af4d7e2157f398d82b1 1650w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/account_setup.png?w=2500&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=b796344a4b92c6c9a3812b23432c89eb 2500w" />
</Frame>

<Accordion title="Using AutoBuild in an existing Flatfile account">
  If you already have an active Flatfile account, you can still use AutoBuild to create a new app.

  From the Flatfile dashboard, click the "New App" button.

  <Frame>
    <img src="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/create_new_app.png?fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=7dd1a0400b0b3a53add9d3ca84d852ae" width="275" data-og-width="546" data-og-height="678" data-path="getting-started/quickstart/assets/create_new_app.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/create_new_app.png?w=280&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=02df4b8850b81122b3e4821f9b92ac70 280w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/create_new_app.png?w=560&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=55c385daf90fc137db7b78112f20e3e9 560w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/create_new_app.png?w=840&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=572c1dcef22194ecd1925e84a9dfd52b 840w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/create_new_app.png?w=1100&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=ee9ae9d5e0ffa7f5d6307f250d62ad6b 1100w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/create_new_app.png?w=1650&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=68edbb3ffec9e3ff9da8b5fd5461916d 1650w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/create_new_app.png?w=2500&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=ba56ce014568db65e16a2bdc1a15943c 2500w" />
  </Frame>

  Then select "Build with AutoBuild."

  <Note>
    If the AutoBuild option isn't available on your account, please reach out to
    support via [Slack](https://flatfile.com/join-slack/) or
    [Email](mailto:support@flatfile.com) to gain access!{" "}
  </Note>
</Accordion>

## Uploading Files and Context

Next, you'll upload files and provide additional context to the AutoBuild agent.

You can upload any of the following to help the AI understand your requirements:

* Import templates
* System documentation
* Complete data files
* Any other files that provide useful context

You may also provide an additional prompt to guide the AutoBuild agent. Use this to give
context about your uploaded files, explain specific data challenges, or outline additional requirements.

When you're ready, click "Get Started." The Flatfile AutoBuild agent will now build your space template.

## Working in Build Mode

After a few moments, you'll be taken to your new Flatfile app in Build Mode, which you can
access anytime to make changes.

On the right side, you'll see the blueprint of your space. Here you can inspect and edit the sheets
and fields that the AutoBuild agent has generated. You can easily add or remove fields,
update constraints and validations, or make other basic edits to your blueprint.

<Frame>
  <img src="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/blueprint.png?fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=192293c3e9e426a8f3e97fb925034d11" width="610" data-og-width="2208" data-og-height="1220" data-path="getting-started/quickstart/assets/blueprint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/blueprint.png?w=280&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=2beeb16864eca2ba75cb20970c247e3f 280w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/blueprint.png?w=560&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=acaa133942daef0eb10964032ed6dbfd 560w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/blueprint.png?w=840&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=08552e21f24eb8fc0008f4dab3669467 840w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/blueprint.png?w=1100&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=2ad5add9beb17c21eac3ae146a38ea12 1100w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/blueprint.png?w=1650&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=529b582eb1ac869056ccc4a502b692d7 1650w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/blueprint.png?w=2500&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=c5734b27cdcd63bd304d0a7a5e518ee2 2500w" />
</Frame>

For more advanced changes, you can chat with the Flatfile Assistant. The Assistant can help you
with anything from small tweaks to complex validations, data egress actions, or large reorganization
of your sheets.

<Frame>
  <img src="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/build_mode_assistant.png?fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=72b21702dad113960972e8563cbadfde" width="423" data-og-width="846" data-og-height="1386" data-path="getting-started/quickstart/assets/build_mode_assistant.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/build_mode_assistant.png?w=280&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=2c1d5b3b9666f3ecd84ad5e002253af3 280w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/build_mode_assistant.png?w=560&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=eb6b3fc26368a5c637e86f288d0436d8 560w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/build_mode_assistant.png?w=840&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=214d402779f7a415dc59f410d2ec4eb3 840w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/build_mode_assistant.png?w=1100&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=2ac78ae85d2a124141d8bb80d2290fec 1100w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/build_mode_assistant.png?w=1650&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=683d47c930b0be8740772ffef995663d 1650w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/build_mode_assistant.png?w=2500&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=7339c2bc8f8171cb44b98e7b71fcfc27 2500w" />
</Frame>

At any point, you can check the Data Preview tab to see what your Flatfile project will look like for
your users. You can add or edit data to test your validations and transformations.

<Frame>
  <img src="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/data_preview.png?fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=013ee455c94bcf5e03fdb70d1ccf0f40" width="1103" data-og-width="2206" data-og-height="1202" data-path="getting-started/quickstart/assets/data_preview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/data_preview.png?w=280&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=dd42ce5cc0be77ef31a2f70f7f5c9e75 280w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/data_preview.png?w=560&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=fdff572c707f2e7953cd0c7651f764f1 560w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/data_preview.png?w=840&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=555bcc40511f6dcbe7ee391b563e5505 840w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/data_preview.png?w=1100&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=97a5a70461bff726a18288fae0f1d7c7 1100w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/data_preview.png?w=1650&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=b9ef4d0b47bfdfe1418e4c8aa997861e 1650w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/getting-started/quickstart/assets/data_preview.png?w=2500&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=e206f9ef5863b85ffdde430d08ded6af 2500w" />
</Frame>

## Deploying Your App

When you're finished building your space, click "Configure & Deploy."

You'll be prompted to give your app a name, and then it's ready to be deployed!

From here, you'll be taken to your new app in the dashboard.

Your autobuild agent is deployed and you're ready to create your first project and start importing data!
