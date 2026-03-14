# Source: https://docs.statsig.com/guides/sidecar-experiments/publishing-experiments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Taking your experiments to production

> Learn how to publish, QA, and launch your Sidecar experiments in production with step-by-step guidance.

With the experiment configuration out of the way, we need to take this to production.  Sidecar makes this easy with just a few clicks.

<Info>
  This guide assumes you have followed the previous steps of creating an experiment in Sidecar.  Check out [Creating Experiments](/guides/sidecar-experiments/creating-experiments) for those instructions.
</Info>

### Step 1: Publish the experiments

Once you are satisfied with the experiment configuration, go ahead and hit the blue *Publish* button. This is essentially a way to store all of your configurations in Statsig. If you want to make sure these changes have been stored successfully, you can on the `...` menu and choose *Go to Experiment Console*.

Publishing changes will not start any experiments, it will do the following:

* Sync any unsaved changes to Statsig (making them accessible in Console where you can configure Metrics and other targeting conditions if applicable).
* Include any configured tests in the Sidecar script installed on your website.
* Allow you to QA experiments on your site while they're in an Unstarted state.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/nSBTTgzvwOEKOriT/images/sidecarconsole.png?fit=max&auto=format&n=nSBTTgzvwOEKOriT&q=85&s=dabceb65f7c7c226a4688aba390efdfb" alt="Statsig experiment console interface" width="1328" height="442" data-path="images/sidecarconsole.png" />
</Frame>

The experiment console will look like this, and allows you to configure rich targeting, metrics, and tweak advanced statistical knobs.  More on this later.

<img src="https://mintcdn.com/statsig-4b2ff144/JoVpINC5Q0MyHWkm/images/guides/sidecar-experiments/publishing-experiments/22f57816-6fdd-422c-87a9-90a5c08f36a5.png?fit=max&auto=format&n=JoVpINC5Q0MyHWkm&q=85&s=88408e00d7d8729d48968d5bf898bcd1" width="50%" alt="Statsig experiment setup tab with checklist and scorecard fields" data-path="images/guides/sidecar-experiments/publishing-experiments/22f57816-6fdd-422c-87a9-90a5c08f36a5.png" />

### Step 2: Preview & QA the experiment

At this point, your experiment is in a pre-started state, meaning your experiment will not be active to your site visitors.
You can pass a query string to your test page url by using the `overrideuser` query string parameter.

The override method uses the following convention to force a test & test group:<br />
`https://www.DOMAIN.com/?overrideuser=<EXPERIMENT_ID>_<TEST_GROUP_ID>`

The image below depicts where you can find the experiment ID and each variation ID. Based on this example, you can force a preview of the Test Group by visiting the following URL:<br />
`https://www.DOMAIN.com/?overrideuser=name_color_test_1`

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/CwEVnzXRS2GJksur/images/sidecarqa.png?fit=max&auto=format&n=CwEVnzXRS2GJksur&q=85&s=f6e15f302a050235d76b29a38b225a6b" alt="Sidecar experiment QA and preview interface" width="1312" height="720" data-path="images/sidecarqa.png" />
</Frame>

Note, this works best with the default test/control group names - if you change one of your group names, you'll also have to modify it in the Statsig Console by clicking "Manage Overrides".

### Step 3: Start the experiment

Refresh the page on your browser with the script embedded.  Sidecar will automatically pick up the experiment you have published and display all the experiment properties.

You can now start the experiment by clicking on the `...` menu and clicking on *Start Experiment*.  This will automatically start the experiment, serve the right variants for control and test, and start collecting metrics on your behalf.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/CwEVnzXRS2GJksur/images/sidecarstartexp.png?fit=max&auto=format&n=CwEVnzXRS2GJksur&q=85&s=0b36936d2cbee6c7c849d6b6705d56a2" alt="Sidecar experiment start interface" width="1290" height="626" data-path="images/sidecarstartexp.png" />
</Frame>

### Congratulations!  You have successfully built and shipped an experiment 🎉


Built with [Mintlify](https://mintlify.com).