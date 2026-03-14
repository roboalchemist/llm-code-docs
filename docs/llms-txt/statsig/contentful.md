# Source: https://docs.statsig.com/guides/contentful.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Guide to Contentful

The Statsig Contentful integration lets you create A/B/n tests and test different content blocks against each other directly from within Contentful. You can assess impact using business metrics on Statsig Cloud or Warehouse Native. Marketers can optimize content, obtain insights, and iterate continuously right from within Contentful.

* Run experiments on CMS content without engineering involvement
* Configure content to serve with each variation
* No performance penalty or flicker

The Statsig Contentful app will add a Statsig container that is connected to an experiment in Statsig. The user can then add Content Blocks to that container to start a test. The Statsig Contentful app lets marketers measure progress towards business objectives by testing content for lift in any core business metrics configured in Statsig.

## Integrating with Contentful

Our Contentful Marketplace App is publicly available. You can find it [here](https://www.contentful.com/marketplace/statsig). To use this integration effectively, you will need to do setup around the Contentful marketplace app, your Content types, and your actual codebase. These are one-time setups, then you will be able to seamlessly run A/B/n tests directly inside Contentful.

### Setting up the Statsig Marketplace App

* Navigate to the Marketplace in Contentful, and find the Statsig app. Click 'Install'.

* Statsig will prompt you to enter a Console API Key. You can find an existing Console API Key in your Statsig project under Settings > Keys & Environments. It's important that this key is **of type 'Console', and has read and write permissions**. Feel free to generate a new key of type 'Console' if a suitable one does not already exist for your project.

  <Frame>
    <img src="https://mintcdn.com/statsig-4b2ff144/n7aLPkvQ3ml2MAiO/images/guides/contentful/80a564ad-22db-45aa-8caa-246512aad0ee.png?fit=max&auto=format&n=n7aLPkvQ3ml2MAiO&q=85&s=abeeb9aaf818d350ce4897c4269476b8" alt="image.png" width="800" height="382" data-path="images/guides/contentful/80a564ad-22db-45aa-8caa-246512aad0ee.png" />
  </Frame>

* Once your API Key is entered, hit 'Install to selected environments'. Your app should now be configured. Returning to this page later will only show the *obfuscated* API Key.

### Setting up Statsig Variant Container

Once configured, a new Content model should have been added to your space called 'Statsig variant container'. We can check to make sure this is setup properly:

* Navigate to the 'Content model' tab in Contentful, and select the 'Statsig variant container'.

  <Frame>
    <img src="https://mintcdn.com/statsig-4b2ff144/n7aLPkvQ3ml2MAiO/images/guides/contentful/6010f051-2f05-462f-ace1-9f3194f73941.png?fit=max&auto=format&n=n7aLPkvQ3ml2MAiO&q=85&s=123aa693b630d4035f9a5fb649fdcea5" alt="image.png" width="1944" height="644" data-path="images/guides/contentful/6010f051-2f05-462f-ace1-9f3194f73941.png" />
  </Frame>

* You should see a list of 4 fields: Statsig Experiment Id, Entry Name, Default Variation (control), Treatment Variations.

  <Frame>
    <img src="https://mintcdn.com/statsig-4b2ff144/n7aLPkvQ3ml2MAiO/images/guides/contentful/486955a9-f31c-4870-8369-df956606bfb3.png?fit=max&auto=format&n=n7aLPkvQ3ml2MAiO&q=85&s=74b41be81e96ac5ebb2c30207e1fcad3" alt="image.png" width="1936" height="424" data-path="images/guides/contentful/486955a9-f31c-4870-8369-df956606bfb3.png" />
  </Frame>

* If your 'Statsig Experiment Id' field shows `Excluded from api response` next to it, we will need to update this field to be fetchable in API calls. We can do this by clicking the three dots on the right of the field, and click 'Include in API response'. Then click 'Save'.

  <Frame>
    <img src="https://mintcdn.com/statsig-4b2ff144/n7aLPkvQ3ml2MAiO/images/guides/contentful/ae81d2b5-7f3d-4aaa-bb7e-316ba28898fe.png?fit=max&auto=format&n=n7aLPkvQ3ml2MAiO&q=85&s=321c386679f4b3f9d1c5fc2c2ebc01bf" alt="image.png" width="1090" height="351" data-path="images/guides/contentful/ae81d2b5-7f3d-4aaa-bb7e-316ba28898fe.png" />
  </Frame>

Your 'Statsig variant container' is now setup and ready to associate with other Content types.

### Setting up Experiments in Content Types

You can configure your existing content types to run Statsig experiments in, automatically serving different variants of this content type to your users. The steps below walk through how to add a 'Statsig experiment' field to your target content type.

* Navigate to the 'Content model' tab in Contentful, and select your target content type (in this example, `page - Blog post`). You should see the list of fields for this content type:

  <Frame>
    <img src="https://mintcdn.com/statsig-4b2ff144/n7aLPkvQ3ml2MAiO/images/guides/contentful/39c0ba10-1ba3-49a3-a106-bad366ba8e6a.png?fit=max&auto=format&n=n7aLPkvQ3ml2MAiO&q=85&s=a0ee733ce0eb1d77be5256fd9d54c700" alt="image.png" width="1949" height="751" data-path="images/guides/contentful/39c0ba10-1ba3-49a3-a106-bad366ba8e6a.png" />
  </Frame>

* Click 'Add field', and choose 'Reference'. Enter `Statsig experiment` for the Name, then click 'Add and Configure'.

  <Frame>
    <img src="https://mintcdn.com/statsig-4b2ff144/n7aLPkvQ3ml2MAiO/images/guides/contentful/c077a3e3-797c-4600-9565-d8202f86db93.png?fit=max&auto=format&n=n7aLPkvQ3ml2MAiO&q=85&s=345f423ea23b24f109ce33eac4f3a278" alt="image.png" width="690" height="573" data-path="images/guides/contentful/c077a3e3-797c-4600-9565-d8202f86db93.png" />
  </Frame>

* Under 'Validation', select 'Accept only specified entry type', and choose 'Statsig variant container' from the dropdown.

  <Frame>
    <img src="https://mintcdn.com/statsig-4b2ff144/n7aLPkvQ3ml2MAiO/images/guides/contentful/b537b900-92ee-4e8a-ab47-75f4f4b9af46.png?fit=max&auto=format&n=n7aLPkvQ3ml2MAiO&q=85&s=69e0b4a2065337494d15c2a2b57019e8" alt="image.png" width="830" height="1005" data-path="images/guides/contentful/b537b900-92ee-4e8a-ab47-75f4f4b9af46.png" />
  </Frame>

* Confirm your new field, and save your content type.

Your content type is now setup to use Statsig Experiments! Feel free to repeat this process for any other content types you would like to be able to run experiments with.

### Running an Experiment on your Content

To run an experiment on your content, you can link a Statsig Experiment to it. Here's how:

* Navigate to the 'Content' tab in Contentful, and select your existing entry from the list. At the bottom of the Editor tab, you should now see an editable field for 'Statsig experiment':

  <Frame>
    <img src="https://mintcdn.com/statsig-4b2ff144/n7aLPkvQ3ml2MAiO/images/guides/contentful/63042ccf-382b-4e04-b23d-8c6bd8eb9cf1.png?fit=max&auto=format&n=n7aLPkvQ3ml2MAiO&q=85&s=f4a3051bb7d1d028fd37c725e58fbe7e" alt="image.png" width="1934" height="1082" data-path="images/guides/contentful/63042ccf-382b-4e04-b23d-8c6bd8eb9cf1.png" />
  </Frame>

* Click on 'Add content', and select 'Statsig variant container' from the New content dropdown. You should see a new Statsig variant container layover:

  <Frame>
    <img src="https://mintcdn.com/statsig-4b2ff144/n7aLPkvQ3ml2MAiO/images/guides/contentful/77688f35-b775-4c84-885d-67ee111d67e4.png?fit=max&auto=format&n=n7aLPkvQ3ml2MAiO&q=85&s=e05480506526ff8e6bd96424cffb629d" alt="image.png" width="2020" height="938" data-path="images/guides/contentful/77688f35-b775-4c84-885d-67ee111d67e4.png" />
  </Frame>

* Under the Statsig tab, enter the name of your experiment under the 'Entry Name' field. Add your control and treatment variations. In this example, we will add `component - Rich image` variations to experiment with. Please note that experiment name should exclude special characters.

* When your experiment setup is finalized, hit 'Publish' on the new Statsig variant container entry.

  <Note>
    Ensure your experiment setup is finalized before publishing, as this will create your experiment inside of Statsig.
  </Note>

  <Frame>
    <img src="https://mintcdn.com/statsig-4b2ff144/n7aLPkvQ3ml2MAiO/images/guides/contentful/872643fb-9782-4728-96ca-362375323cfa.png?fit=max&auto=format&n=n7aLPkvQ3ml2MAiO&q=85&s=df2abfb0d3906b4b06e6ab30fc2ab048" alt="image.png" width="1926" height="1154" data-path="images/guides/contentful/872643fb-9782-4728-96ca-362375323cfa.png" />
  </Frame>

* You should now be prompted to start your newly created experiment inside of Statsig. Follow the 'Go to Statsig Experiment' link to finalize your experiment's setup, add metrics, and start your experiment.

* Once your experiment has been started on Statsig, you should see a green banner at the top of your Statsig variant container, and your variation fields will no longer be editable.

* Return to your original entry, and hit 'Publish changes'.

Your experiment is now live!

### Integrating Statsig Experiments in your Codebase

We have provided an [example repository](https://github.com/statsig-io/contentful-blog-webapp-nextjs-example/tree/main) that outlines how you can integrate your Statsig experiments created from Contentful into your codebase. The `README` walks through the setup process, including pulling experiment fields from Contentful, calling a Statsig SDK, and matching assigned users to their respective variant.

### Troubleshoot Common Problems

#### I created an experiment and the 'Go to Experiment' button doesn't show up - what happened?

This indicates that the Statsig Experiment Id was not saved properly. To fix this error, navigate into 'Editor' and manually add the Statsig Experiment Id. Once you save it, then the button should populate as expected.

<img src="https://mintcdn.com/statsig-4b2ff144/jSOfdaalUX_b-LQZ/images/contentful_statsig_experiment_id.png?fit=max&auto=format&n=jSOfdaalUX_b-LQZ&q=85&s=a6561ccbcccc59fd074b9a6acea04311" alt="Contentful Statsig Experiment Id" width="1390" height="572" data-path="images/contentful_statsig_experiment_id.png" />


Built with [Mintlify](https://mintlify.com).