# Source: https://docs.statsig.com/experiments/ending/make-decision.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Make a Decision

> Learn how to analyze experiment results and make informed decisions about launching, abandoning, or continuing experiments.

Making a decision for an experiment enables you to 'ship' the winning group to all your users.
After you make the decision, the variant that your users see depends on whether you're using a **targeting gate** for your experiment. The results for your experiment will still be accessible after you make a decision, but they will stop updating.  The last day of metrics will be the day you "make a decision" on the experiment.

## Experiments With No Targeting Gate

When you ship a group in an experiment with no targeting gate, the parameter values from the shipped group will become the default values
for *all* your users going forward.

If the experiment happens to use parameters from a layer, the layer's parameters will now take on the shipped group's parameter values
as their defaults. These are the values that *all* your users will see going forward.

For example, suppose you have a **Demo Layer** that's configured with a parameter, **a\_param**. It's default value is set to *layer\_default* as shown below.

<img width="746" alt="Layer configuration showing default parameter value before experiment" src="https://mintcdn.com/statsig-4b2ff144/ax_yxPlGE0DmsCCZ/images/experiments/ending/make-decision/162633143-3ddd9652-4e99-4760-aac0-c89dec8ce70c.png?fit=max&auto=format&n=ax_yxPlGE0DmsCCZ&q=85&s=d9d1f04502e3e7907a7f167423e90e09" data-path="images/experiments/ending/make-decision/162633143-3ddd9652-4e99-4760-aac0-c89dec8ce70c.png" />

Say you decide to create an experiment, **Demo Experiment** in **Demo Layer** as shown below.

<img width="383" alt="Experiment creation dialog in Demo Layer with control and test groups" src="https://mintcdn.com/statsig-4b2ff144/ax_yxPlGE0DmsCCZ/images/experiments/ending/make-decision/162633041-633de059-f676-4f76-a0ef-4d17b03648a0.png?fit=max&auto=format&n=ax_yxPlGE0DmsCCZ&q=85&s=5dcc9e87d11093d90af2419bffdb7ae8" data-path="images/experiments/ending/make-decision/162633041-633de059-f676-4f76-a0ef-4d17b03648a0.png" />

You set up **Demo Experiment** with two groups: **Control** and **Test**, intending to experiment with new values for the layer-level parameter, **a\_param** as shown below.

<img width="630" alt="Experiment parameter table comparing control and test values for a_param" src="https://mintcdn.com/statsig-4b2ff144/ax_yxPlGE0DmsCCZ/images/experiments/ending/make-decision/162633712-a5e889dd-32ba-4248-8524-b6d5555b4dfd.png?fit=max&auto=format&n=ax_yxPlGE0DmsCCZ&q=85&s=97223e7067fcd812686f49c40652c7b3" data-path="images/experiments/ending/make-decision/162633712-a5e889dd-32ba-4248-8524-b6d5555b4dfd.png" />

Now if you decide to ship the **Control** group for the **Demo Experiment**, **a\_param** will take the value set for the **Control** group as its default: *experiment\_one\_control*

<img width="455" alt="Layer defaults updated to use control group value experiment_one_control" src="https://mintcdn.com/statsig-4b2ff144/ax_yxPlGE0DmsCCZ/images/experiments/ending/make-decision/162630956-1ffaa81f-c95f-4df7-9ced-b138cfe26d96.png?fit=max&auto=format&n=ax_yxPlGE0DmsCCZ&q=85&s=903cf09312b1bd7f0b4e9580916c6acc" data-path="images/experiments/ending/make-decision/162630956-1ffaa81f-c95f-4df7-9ced-b138cfe26d96.png" />

On the other hand, if you decide to ship the **Test** group, **a\_param** will take the value set for the **Test** group as its default: *experiment\_two\_test*

<img width="454" alt="Layer defaults updated to use test group value experiment_two_test" src="https://mintcdn.com/statsig-4b2ff144/ax_yxPlGE0DmsCCZ/images/experiments/ending/make-decision/162631111-daf31f6f-156b-481e-aa01-f29743f7e20a.png?fit=max&auto=format&n=ax_yxPlGE0DmsCCZ&q=85&s=707cf5c11d7a7c7a2689968b8b138160" data-path="images/experiments/ending/make-decision/162631111-daf31f6f-156b-481e-aa01-f29743f7e20a.png" />

## Experiment With a Targeting Gate / Targeting Rules

When you decide to ship a group in an experiment configured with a targeting gate or targeting rules, you can decide whether to continue targeting after shipping.

* If you decide to *discontinue* targeting, the parameter values from the shipped group will become the default values for all your users going forward. If the experiment happens to use parameters from a layer, the layer's parameters will now take on the shipped group's parameter values as their defaults. These are the values that your users will see going forward.
* If you decide to *continue* targeting with a **targeting gate**, this will add an override to the experiment layer so that:
  * all users who **pass** the targeting gate will see shipped group's parameter values
  * all users who **fail** the targeting gate will see the default value (layer-level parameter defaults or the defaults you set for the parameter in your code)
* If you decide to *continue* targeting with **targeting rules**, the experiment will only be shipped to users who pass the inline targeting rules as set in the experiment setup.

<Info>
  **Shipping with Targeting On**
  If you decide to continue targeting, shipping a group will not update the default value of any layer parameters.
</Info>

For example, suppose **Demo Experiment** in a **Demo Layer** that has a parameter called **targeted\_layer\_param**, whose default value is set to
*targeted\_layer\_default\_value*.

When you decide to ship **Demo Experiment**, if you discontinue targeting,
**targeted\_layer\_param** will now take on the value from the **Control** group, *targeted\_layer\_control*, as its default.

<img width="454" alt="Targeted layer parameter default switching to control value when targeting disabled" src="https://mintcdn.com/statsig-4b2ff144/KzTmSDyskL8DnHsb/images/experiments/ending/make-decision/162630927-e4b147a3-5b68-41d0-a439-f90ab001d737.png?fit=max&auto=format&n=KzTmSDyskL8DnHsb&q=85&s=86e3e469fb7684daffb00aa52e21aead" data-path="images/experiments/ending/make-decision/162630927-e4b147a3-5b68-41d0-a439-f90ab001d737.png" />

On the other hand, if you decide to continue targeting,
**targeted\_layer\_param** will now acquire an override so that:

* all users who **pass** the targeting gate will see the *overridden* value of the parameter
* all users who **fail** the targeting gate will see the *default* value of the parameter

In this case, the default value of **targeted\_layer\_param** in **Demo Layer** will not change. Also, any users who pass the targeting gate will not be eligible for future experiments run in this layer. For this reason, we do not encourage shipping experiments with targeting on, especially when the experiment is in a layer.

<img width="454" alt="Layer override showing targeted users receiving shipped parameter while others keep default" src="https://mintcdn.com/statsig-4b2ff144/ax_yxPlGE0DmsCCZ/images/experiments/ending/make-decision/162634627-ae327d9e-81a9-42f9-8171-836808cb6ffb.png?fit=max&auto=format&n=ax_yxPlGE0DmsCCZ&q=85&s=59885314ac12f9732674e66c7e8062b5" data-path="images/experiments/ending/make-decision/162634627-ae327d9e-81a9-42f9-8171-836808cb6ffb.png" />

## Rolling Out an Experiment Group

Rolling out an experiment group is an option available when you have decided the winning variant, but want to avoid a sudden, large shift of traffic into the winning variant group. You can use automated rollouts to schedule gradual rollout phases, which will increase your shipped group size to the desired percentage by reallocating users from all other groups proportionally.

### Setting up Rollouts

To set up rollouts, open the make decision form and select the winning group. Here you will be able to either use automated rollouts, or ship with rollout.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/ax_yxPlGE0DmsCCZ/images/experiments/ending/make-decision/549864e9-0509-4b44-a588-fd10ace1e365.png?fit=max&auto=format&n=ax_yxPlGE0DmsCCZ&q=85&s=4e6de0496de7226b2f13189dc0793a69" alt="Make decision rollout options interface" width="599" height="606" data-path="images/experiments/ending/make-decision/549864e9-0509-4b44-a588-fd10ace1e365.png" />
</Frame>

The ship with rollout option allows you to immediately update the shipped group size. Manual rollouts will clear any automated rollout phases.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/ax_yxPlGE0DmsCCZ/images/experiments/ending/make-decision/f200b795-0442-49ed-8c13-e220b3a77a81.png?fit=max&auto=format&n=ax_yxPlGE0DmsCCZ&q=85&s=76a1ca4e2b133dbe383376c9fb1fd20f" alt="Ship with rollout configuration screen" width="229" height="115" data-path="images/experiments/ending/make-decision/f200b795-0442-49ed-8c13-e220b3a77a81.png" />
</Frame>

Alternatively, you can set up automated rollouts, which will open the following dialog that you can populate with the rollout phases:

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/ax_yxPlGE0DmsCCZ/images/experiments/ending/make-decision/6fab7c0e-2566-4d14-bdb6-b94102fb08ac.png?fit=max&auto=format&n=ax_yxPlGE0DmsCCZ&q=85&s=4c527a916bc736c5bdcef6d98e650889" alt="Automated rollout phases configuration dialog" width="797" height="643" data-path="images/experiments/ending/make-decision/6fab7c0e-2566-4d14-bdb6-b94102fb08ac.png" />
</Frame>

From here, you can configure each phase of your Scheduled Rollout. To add phases to your rollout, click **Add Phase** and configure as many phases as you want.

Each scheduled rollout phase includes-

* Rollout date
* Rollout time\*
* Pass percentage

<Note>
  Rollout times are available in 15 minute increments. Additionally, each configured phase represents a discrete increase to the next rollout percentage, not a gradual rollout amortized over the course of the entire phase.
</Note>

Upon saving, you will be able to see a preview of the rollout and commit the schedule:

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/ax_yxPlGE0DmsCCZ/images/experiments/ending/make-decision/f1fd04b3-e6a0-4e32-91a8-fb24279ab923.png?fit=max&auto=format&n=ax_yxPlGE0DmsCCZ&q=85&s=688fd2669a0b248526ea81051bb5b799" alt="Rollout schedule preview and commit interface" width="599" height="791" data-path="images/experiments/ending/make-decision/f1fd04b3-e6a0-4e32-91a8-fb24279ab923.png" />
</Frame>

### Resizing Logic

During each phase, the rollout group is resized to the desired percentage, and all other groups are scaled proportionally in the following way:

You have *n* groups with sizes:

G₁, G₂, ..., Gₙ

Their total sum is:

100 = G₁ + G₂ + ... + Gₙ.

Now, suppose you **set one group** (say the k-th group) to a **new size** Gₖ′. Let

Delta = Gₖ′ − Gₖ.

Because the **grand total** must remain 100, you need to **adjust the remaining groups** proportionally. Let

T = 100 - Gₖ

Then, for each group i ≠ k,

Gᵢ′ = Gᵢ − (Delta × Gᵢ / T).

In other words, each group other than k is decreased (or increased, if Delta \< 0) by its fraction of T.

### A few notes

1. Experiment results will be frozen to a snapshot of when the rollout decision is made.
2. Rolling out a group to 100% does not fully ship the experiment, meaning configurations such as experiment/layer allocation, targeting, overrides, and so on will not change. To fully ship the experiment go through the usual flow without specifying any rollouts.
3. Groups can be rolled out and back, but the rollout % cannot be lower than the group's original size.

<Info>
  This is currently a beta feature.
</Info>

## Shipping with a Holdback

Shipping with holdback lets you release an experiment variant (the “shipped” group) to most of your users while keeping a percentage in the control group for ongoing comparisons. Here’s how it works:

1. Make a decision and select a group to ship: From the Make Decision dropdown, choose which variant you want to ship.

2. Turn on the Ship with holdback option and specify the percentage of users you want to keep in the control (holdback) group.

<img width="597" alt="Ship with holdback dialog specifying control percentage in Make Decision modal" src="https://mintcdn.com/statsig-4b2ff144/KzTmSDyskL8DnHsb/images/experiments/ending/make-decision/046fcb33-d4c0-4ca4-b58a-1c8e931b6161.png?fit=max&auto=format&n=KzTmSDyskL8DnHsb&q=85&s=c314ecff34c2f1176c3e07edc16ccd85" data-path="images/experiments/ending/make-decision/046fcb33-d4c0-4ca4-b58a-1c8e931b6161.png" />

3. Allocation of users:
   The control (holdback) group is set to your specified percentage.
   The remaining users are assigned to the shipped experience.

4. Splitting the shipped group:
   The shipped group is divided into two segments: Test and Launched.
   * The size of Test segment will have the same percentage allocation as the holdback group for an [equal sized comparison](/experiments/holdouts-introduction#how-to-read-holdouts) of 50:50.
   * The Launched segment will no longer appear in the pulse results, but users in this segment will continue to receive the shipped experience.

<img width="959" alt="Pulse results display separating test and launched segments when shipping with holdback" src="https://mintcdn.com/statsig-4b2ff144/ax_yxPlGE0DmsCCZ/images/experiments/ending/make-decision/48f999c5-f7d0-47fd-9af8-96512802d6cf.png?fit=max&auto=format&n=ax_yxPlGE0DmsCCZ&q=85&s=86bbf8d0e2ecaf07eb49a28d665ad332" data-path="images/experiments/ending/make-decision/48f999c5-f7d0-47fd-9af8-96512802d6cf.png" />

5. Continue monitoring the pulse results that evaluates the Test segment vs. Control (holdback)

6. Once you decide to end the holdback, you can make a decision to ship the variant to everyone which will include users in holdback.

<Note>
  Some users currently in control will move to the shipped group to achieve the desired allocation.
  However, any user who has previously been in a test or shipped group will not be reassigned to control.
  New users—those who have never been exposed to the experiment will be assigned based on the allocation percentages of each group.
</Note>

Note that the new pulse results (Test segment vs. Holdback) will start when you ship with holdback, but your original experiment's results from the point of holdback decision will be retained and remain available to you.

From the history of experiment, you will see the new log of experiment decision and a 'View Results Snapshot' button where you can view the read-only snapshot of original results.

<img alt="Snapshot of original experiment when using ship with holdback" src="https://mintcdn.com/statsig-4b2ff144/TjBAFsyeyvjjG3o1/images/experiments/ending/make-decision/ship_with_holdback.png?fit=max&auto=format&n=TjBAFsyeyvjjG3o1&q=85&s=31695061570a900d10a0475c2082a080" width="2852" height="690" data-path="images/experiments/ending/make-decision/ship_with_holdback.png" />

By using shipping with holdback, you maintain a dedicated, stable control group alongside a representative test segment of the shipped experience, making it easy to measure ongoing performance and user behavior post-launch.

<Info>
  This is currently a beta feature.
</Info>


Built with [Mintlify](https://mintlify.com).