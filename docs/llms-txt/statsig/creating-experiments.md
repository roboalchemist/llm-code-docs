# Source: https://docs.statsig.com/guides/sidecar-experiments/creating-experiments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating Your First Experiment

> Learn how to create and configure A/B experiments using Sidecar without writing code or deploying to production.

Sidecar allows you to create and run A/B experiments easily without having to write code or push code to production.  Here we'll see how you can create one such experiment and get results

<Info>
  This guide assumes you have followed the previous steps of installing side-car, creating a statsig account and setting up the API Keys correctly.  Check out [Setup](/guides/sidecar-experiments/setup) for those instructions.
</Info>

### Step 1: Navigate to the web page

Navigate to the web page you want to experiment on.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/nSBTTgzvwOEKOriT/images/sidecarfull.png?fit=max&auto=format&n=nSBTTgzvwOEKOriT&q=85&s=86d5c7283f164d98a6c827de3387fa32" alt="Sidecar experiment interface showing the main dashboard" width="2444" height="1308" data-path="images/sidecarfull.png" />
</Frame>

### Step 2: New experiment

Hit the *New Experiment* button and fill out the details.  This will create a local experiment which hasn't been published yet. This allows you to configure all the details, verify that everything works and then you can publish it.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/JoVpINC5Q0MyHWkm/images/guides/sidecar-experiments/creating-experiments/d8cfc8bb-43e9-4a64-8ca8-002c579e7fff.png?fit=max&auto=format&n=JoVpINC5Q0MyHWkm&q=85&s=4c828906b6d65abdb1c84dbc566b8ff9" alt="New experiment creation form" width="339" height="246" data-path="images/guides/sidecar-experiments/creating-experiments/d8cfc8bb-43e9-4a64-8ca8-002c579e7fff.png" />
</Frame>

### Step 3 (Optional): Add url filter

You have the option to select what pages the experiment will run on. <br />This will be evaluated prior to any targeting rules you configure on the experiment within Statsig console.

*You can configure URL targeting using the following methods:*

* All Pages - anywhere Sidecar client is installed
* Contains - The page URL must contain the value as a substring
* Exact Match - The page URL must match the exact value specified here.
* Regex - Regular expressions, for example `(http|https):\/\/www.statsig.com\/pricing` matches pages `http://www.statsig.com/pricing` or `https://www.statsig.com/pricing`, and will activate this experiment on those pages.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/CwEVnzXRS2GJksur/images/sidecarurls.png?fit=max&auto=format&n=CwEVnzXRS2GJksur&q=85&s=bd30967274c66a04a947ec0e413275c8" alt="URL targeting configuration interface with filter options" width="1134" height="646" data-path="images/sidecarurls.png" />
</Frame>

### Step 4: Add actions

Click the *Add Action* button and you'll see a list of actions you can perform with this experiment. Let's try one of them here.

Go ahead and choose *Change content of an element*.  This will set you up to run an A/B test changing the content of an HTML element - like Headlines, descriptions, CTA, etc.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/nSBTTgzvwOEKOriT/images/sidecaraddaction.png?fit=max&auto=format&n=nSBTTgzvwOEKOriT&q=85&s=7d4cd3fc045b026a3e62178f2170f828" alt="Add action selection menu with available experiment actions" width="1350" height="576" data-path="images/sidecaraddaction.png" />
</Frame>

#### 💡 Use Redirect Action for running Landing Page and Split URL experiments

For running Landing Page and Split URL experiments, you can quickly add the "Redirect to another page" for any of your test groups and indicate the destination url as desired. Any query string parameters will be preserved and passed to the destination URL.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/CwEVnzXRS2GJksur/images/sidecarredirect.png?fit=max&auto=format&n=CwEVnzXRS2GJksur&q=85&s=4bae2a6d04c7ffdb0425b5661fb11863" alt="Redirect action configuration for landing page experiments" width="1372" height="644" data-path="images/sidecarredirect.png" />
</Frame>

### Step 5: Select an element

In order to run a content change experiment, you will need two things: 1. the element that you want to test with, 2. the content you want to change.

Click on the yellow *Target element path* text-box.  This will activate an element selector mode.

Now as you move your mouse over your web page you'll see a red selection rectangle.  Choose the element you want by clicking on it.  In this example, we're choosing the main Headline.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/CwEVnzXRS2GJksur/images/sidecarselect.png?fit=max&auto=format&n=CwEVnzXRS2GJksur&q=85&s=3fd350c0f8e200957249ebd68dec65d4" alt="Element selection with red highlight showing target element" width="1798" height="1278" data-path="images/sidecarselect.png" />
</Frame>

Sidecar will now reflect the path of the element that was selected.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/nSBTTgzvwOEKOriT/images/sidecarpath.png?fit=max&auto=format&n=nSBTTgzvwOEKOriT&q=85&s=c753895534511dadcff7aa6700a40d71" alt="Selected element path display in the configuration panel" width="1366" height="610" data-path="images/sidecarpath.png" />
</Frame>

### Step 6: Update content

Now, you can choose the two different text content you want to A/B test.  In the *Control content* text box, add your control text ("Build Better Products") and in the *Test content* text box, add your test variant ("Experiment Like a Pro").

You can validate these changes in realtime by clicking on the ▶ button above the text box for each variant.  This will immediately change the element's content so you can visually inspect how things look before publishing.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/CwEVnzXRS2GJksur/images/sidecarupdatelt.png?fit=max&auto=format&n=CwEVnzXRS2GJksur&q=85&s=bfd0905c5b8ad97923f45e0a395435bd" alt="Content update interface with preview functionality" width="1446" height="686" data-path="images/sidecarupdatelt.png" />
</Frame>

### Step 7: Add more actions

Feel free to add more actions within the same experiment and play with the capabilities of the tool

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/nSBTTgzvwOEKOriT/images/sidecar2ndaction.png?fit=max&auto=format&n=nSBTTgzvwOEKOriT&q=85&s=c94b9cbf1f6ed7279de8299ddae9fd02" alt="Adding additional experiment actions to the same test" width="1336" height="620" data-path="images/sidecar2ndaction.png" />
</Frame>

#### Congratulations!  You have created your first no-code experiment

## Next up: [Measuring Experiments](/guides/sidecar-experiments/measuring-experiments)


Built with [Mintlify](https://mintlify.com).