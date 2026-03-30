# Source: https://docs.statsig.com/experiments/layers-overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Layers

> Group related experiments into mutually exclusive universes and share parameters without code churn.

## What are Layers?

Layers (a.k.a. Universes) allow us to create experiments that are mutually exclusive to each other. Each layer has a logical representation of all your users and can have experiments created "within" this layer. Users that are in one experiment of a layer, cannot also be in another experiment in the same layer.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/TkTlZF5H4SWQBYsY/images/experiments/layers-concept.png?fit=max&auto=format&n=TkTlZF5H4SWQBYsY&q=85&s=c857197621169a1ffc5ccf0e398b4dcf" alt="Layer concept diagram showing mutually exclusive experiments" width="1464" height="824" data-path="images/experiments/layers-concept.png" />
</Frame>

You can add experiments to a layer (or create a layer) during experiment creation.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/TkTlZF5H4SWQBYsY/images/experiments/layers-create.png?fit=max&auto=format&n=TkTlZF5H4SWQBYsY&q=85&s=2d0502cbbf47a344fad1f8398f102860" alt="Experiment creation modal with layer selection" width="613" height="427" data-path="images/experiments/layers-create.png" />
</Frame>

Once you create a layer, you'll be able to manage them on the layer management tab under Experiments.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/TkTlZF5H4SWQBYsY/images/experiments/layers-tab.png?fit=max&auto=format&n=TkTlZF5H4SWQBYsY&q=85&s=bc7311aaa8f04eb8348d5fb2ba4dd090" alt="Layers overview tab listing active layers" width="1682" height="927" data-path="images/experiments/layers-tab.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/TkTlZF5H4SWQBYsY/images/experiments/layer-details.png?fit=max&auto=format&n=TkTlZF5H4SWQBYsY&q=85&s=430a32114cccf43672d72e6ba9fc3785" alt="Layer details page showing shared parameters" width="1681" height="1215" data-path="images/experiments/layer-details.png" />
</Frame>

In addition to that, **Layers are key to improving engineering efficiency and iteration velocity** for product teams. In a Layer, parameters exist at the Layer level, and can be shared across experiments within the Layer. Due to this characteristic, we can abstract the concept of "Experiment" away from the SDKs so that users only need to deal with parameters in code, which makes it super easy to run multiple experiments that change the same thing and iterate on the same experiment without any code changes.

Let's say your product has an important signup dialog, which contains some text that your team runs a lot of tests on, some of which were run in parallel, and some were iterations of previous experiments. If you work with Experiments directly, your code will look like this over time:

```jsx  theme={null}
let signUpText = DEFAULT_SIGNUP_TEXT;
const signUpTestV1 = statsig.getExperiment("sign_up_dialog_text_test_v1");
const signUpTestV2 = statsig.getExperiment("sign_up_dialog_text_test_v2");
const specialSignUpTest = statsig.getExperiment("sign_up_test_special_offer");
const holidaySignUpTest = statsig.getExperiment("sign_up_test_holiday");

if (signUpTestV1.get("is_in_test", false)) {
  // original test, added in app version v1.2
  signUpText = signUpTestV1.get("dialog_content", DEFAULT_SIGNUP_TEXT);
} else if (signUpTestV2.get("is_in_test", false)) {
  // v2 of the original test, added in app version v1.6 because we wanted to test a new copy but don't want to stop v1
  signUpText = signUpTestV2.get("dialog_content", DEFAULT_SIGNUP_TEXT);
} else if (specialSignUpTest.get("is_in_test", false)) {
  // test showing a special offer in the text, added in v2.0
  signUpText = specialSignUpTest.get("dialog_content", DEFAULT_SIGNUP_TEXT);
} else if (holidaySignUpTest.get("is_in_test", false)) {
  // test showing some holiday greetings in the dialog, added in v2.1
  signUpText = holidaySignUpTest.get("dialog_content", DEFAULT_SIGNUP_TEXT);
}

// Then we display the text in the dialog
```

Every time you add a new test, you need to change the code and it's only available in a new version.

However, things become **A LOT** easier if you work with Layers:

```jsx  theme={null}
let signUpText = statsig
  .getLayer("sign_up_tests")
  .get("sign_up_dialog_text", DEFAULT_SIGNUP_TEXT);

// Then we display the text in the dialog
```

That's all the code you ever need! No more code changes and app releases for new tests. Every time you want to add a new test, simply add a new experiment to the same Layer and choose the parameter `sign_up_dialog_text` as a parameter for the new experiment. The SDK takes care of figuring out which value to serve for the user, based on which experiment the user is allocated to.

## getExperiment vs getLayer API

<Warning title="Always call getLayer">
  Even though layered experiments remain technically accessible via `getExperiment`, that API evaluates only the current experiment. Use `getLayer` so the SDK honors layer-level decisions, mutual exclusion, and shared parameters.
</Warning>

## A Word on Exposures

Calling `getLayer(LayerName<string>)` by itself does not log an exposure. A `statsig::layer_exposure` event is logged when you access a specific parameter within the Layer using `getLayer(LayerName<string>).get(Parameter<string>)`.

* If the user is assigned to an experiment within the Layer, the `statsig::layer_exposure` event is billable.
* If the user is not assigned to an experiment within the Layer, the `statsig::layer_exposure` event is not billable.

<Note>
  Repeated reads of the same Layer parameter for the same user within the deduplication window may count as a single billable exposure.
  Reads of different Layer parameters may count separately.
</Note>


Built with [Mintlify](https://mintlify.com).