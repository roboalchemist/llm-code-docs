# Source: https://docs.statsig.com/guides/cms-integrations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Guide to General CMS Integrations

### Using Statsig with a CMS

One fairly common question we get is around how to use Statsig with an existing CMS. While we also offer a no-code solution - [Sidecar](/guides/sidecar-experiments/introduction),
there are clever ways you can set up your code to integrate your CMS and Statsig so you can write code once, and then run experiments on
arbitrary combinations of parameters in the future.

We recommend using [Layers](/layers) to wire this up, so take some time to read up before continuing.

<Info>
  Layers are a unit of mutual exclusion between experiments in Statsig. Every user participates in only one experiment in a layer at any given time.
  As such, we recommend you set up a layer for each surface you will be experimenting on with the help of your CMS
</Info>

For the remainder of this guide, we will assume you are experimenting on a single surface - but repeat these steps if you plan to experiment on separate surfaces like your landing page, product page, blog, etc.

For the sake of example, let's assume we are parameterizing the Statsig landing page to plug in our CMS.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/ZM1xE0fkOvd3nIHq/images/guides/cms-integrations/187345904-90ade71e-adc7-4205-85c7-751633a864da.png?fit=max&auto=format&n=ZM1xE0fkOvd3nIHq&q=85&s=9bd1f41d0f2e857095cc8da4e179974a" alt="Statsig landing page diagram showing CMS-provided sections" width="1262" height="484" data-path="images/guides/cms-integrations/187345904-90ade71e-adc7-4205-85c7-751633a864da.png" />
</Frame>

First, lets create a layer. Navigate to "Experiments" in the left hand column, and then "Layers" in the title bar:

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/ZM1xE0fkOvd3nIHq/images/guides/cms-integrations/187341751-7c5861a7-90cd-494d-b84d-75c9ea54f923.png?fit=max&auto=format&n=ZM1xE0fkOvd3nIHq&q=85&s=08b46089839ba0ab4512339b6bdb2ce0" alt="Layers list and create button in Statsig experiments UI" width="760" height="453" data-path="images/guides/cms-integrations/187341751-7c5861a7-90cd-494d-b84d-75c9ea54f923.png" />
</Frame>

Here, we'll create one for all content or parameters we want to experiment with on our landing page, so we call it "statsig\_landing\_page"

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/ZM1xE0fkOvd3nIHq/images/guides/cms-integrations/187346608-3314ca52-4c99-4442-b056-7081369d2b8f.png?fit=max&auto=format&n=ZM1xE0fkOvd3nIHq&q=85&s=e79b6c46b7593ffcba60646430f64627" alt="Create layer dialog naming statsig_landing_page" width="497" height="505" data-path="images/guides/cms-integrations/187346608-3314ca52-4c99-4442-b056-7081369d2b8f.png" />
</Frame>

Next, lets create some parameters. One for the title, subtitle, and primary CTA. For the value, we will use the actual ID of the content in the CMS

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/ZM1xE0fkOvd3nIHq/images/guides/cms-integrations/187346653-1be62abe-e6b9-4ed6-9bf6-b95e7b04e040.png?fit=max&auto=format&n=ZM1xE0fkOvd3nIHq&q=85&s=c550cef07e78d7ae32a93ead50617976" alt="Layer parameter creation form for CMS content IDs" width="498" height="467" data-path="images/guides/cms-integrations/187346653-1be62abe-e6b9-4ed6-9bf6-b95e7b04e040.png" />
</Frame>

It should look like this when you are done:

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/ZM1xE0fkOvd3nIHq/images/guides/cms-integrations/187346571-85013f61-6ca6-42f5-9c41-b4631931f93e.png?fit=max&auto=format&n=ZM1xE0fkOvd3nIHq&q=85&s=2eb524269f4e57161c1aec3c17df7191" alt="Layer parameters table listing title, subtitle, and CTA defaults" width="1386" height="1000" data-path="images/guides/cms-integrations/187346571-85013f61-6ca6-42f5-9c41-b4631931f93e.png" />
</Frame>

Note that each layer parameter has a default value. If the user is not in any experiments in that layer, that's the default they will get, which will be backed by the cms.

Now, in code, your integration will look something like this:

```js  theme={null}
const landingPageCmsIds = statsig.getLayer("statsig_landing_page");

const titleID = landingPageCmsIds.get("title", "<default_cms_title_id>"); // note that you have a default value in code as well

// exact library and function call will map to your cms client library
cmsClient.getEntry(titleID);
```

If you repeat this for the subtitle, CTA, and all the other parameters on your landing page, they all become dynamic!
When you put a new CMS ID into statsig, your code will pull the updated content for that section.

Now, you can create new content in your CMS, and create an experiment in Statsig to try out that new variant. After creating the content, come back
to your layer and hit "Create Experiment in Layer":

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/ZM1xE0fkOvd3nIHq/images/guides/cms-integrations/187347191-ac9a27bb-3ea3-4338-8680-c94b6d1e753b.png?fit=max&auto=format&n=ZM1xE0fkOvd3nIHq&q=85&s=9826007b8fa23d883f5c7cad7b09022b" alt="Create experiment in layer button location" width="1350" height="532" data-path="images/guides/cms-integrations/187347191-ac9a27bb-3ea3-4338-8680-c94b6d1e753b.png" />
</Frame>

Fill out the resulting form:

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/ZM1xE0fkOvd3nIHq/images/guides/cms-integrations/187347290-fc3ebc84-1cf0-4f3a-8256-d6cc5a4b21b3.png?fit=max&auto=format&n=ZM1xE0fkOvd3nIHq&q=85&s=c6e58f3e443415fba6a3ba07b6c8de17" alt="Layer experiment setup form with control and test weights" width="491" height="545" data-path="images/guides/cms-integrations/187347290-fc3ebc84-1cf0-4f3a-8256-d6cc5a4b21b3.png" />
</Frame>

And you have created an experiment! Now, we just need to set up the test and control groups for the experiment, and say which content will be used for each
of the parameters we have set up. In the Groups and parameters section, select "Add Parameter" and then choose one of your existing parameters, like title:

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/ZM1xE0fkOvd3nIHq/images/guides/cms-integrations/187347358-f336195a-0fa5-42d0-9896-ea0e0cf85875.png?fit=max&auto=format&n=ZM1xE0fkOvd3nIHq&q=85&s=cc3feac9b1a02b7e137693ed91107b40" alt="Groups and parameters section showing Add Parameter menu" width="1298" height="372" data-path="images/guides/cms-integrations/187347358-f336195a-0fa5-42d0-9896-ea0e0cf85875.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/ZM1xE0fkOvd3nIHq/images/guides/cms-integrations/187347464-e4a2dbe6-bcb8-48f1-b807-339f59b6e0b2.png?fit=max&auto=format&n=ZM1xE0fkOvd3nIHq&q=85&s=da51cf589d86eff7086f96bd211bbc1d" alt="Parameter value editor selecting CMS ID per group" width="582" height="520" data-path="images/guides/cms-integrations/187347464-e4a2dbe6-bcb8-48f1-b807-339f59b6e0b2.png" />
</Frame>

Update the value of the parameter to the id of the new title:

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/n7aLPkvQ3ml2MAiO/images/guides/cms-integrations/187347517-77ff4cfb-8f52-4db3-9dd1-92e453076b01.png?fit=max&auto=format&n=n7aLPkvQ3ml2MAiO&q=85&s=72aeb40acc2dbfbfabaab1f2ff52a626" alt="Updated parameter table showing new CMS content IDs per variation" width="621" height="375" data-path="images/guides/cms-integrations/187347517-77ff4cfb-8f52-4db3-9dd1-92e453076b01.png" />
</Frame>

If you want to create multiple experiment groups, or add more parameters, keep on adding until your experiment setup is complete.
After you have validated the experience in all the groups is what you expect, start your experiment and wait for results -
no code changes are required for all those parameters you already created, statsig will pull the updated ID, and then your code will load the updated content for each of those automatically!

The experimentation flow is the same as all other experiments on Statsig at this point, the value just ties to your CMS.

If you need more help setting up and running experiments, see [Experiments](/experiments-plus)


Built with [Mintlify](https://mintlify.com).