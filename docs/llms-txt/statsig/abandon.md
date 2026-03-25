# Source: https://docs.statsig.com/experiments/ending/abandon.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Abandon an Experiment

> Learn how to abandon experiments and understand the implications for user assignment.

When you realize your experiment has an issue or need to stop it for any reason, you can abandon it. Abandoning an experiment will put it into the unstarted state, which will give every user the default experience back.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/KzTmSDyskL8DnHsb/images/experiments/ending/abandon/206825097-f8032cf2-64d6-4cad-b6ec-49f37d6e28cf.png?fit=max&auto=format&n=KzTmSDyskL8DnHsb&q=85&s=5ff0e607fdf453099901302207a412cd" alt="Experiment abandon interface" width="423" height="418" data-path="images/experiments/ending/abandon/206825097-f8032cf2-64d6-4cad-b6ec-49f37d6e28cf.png" />
</Frame>

When an experiment is abandoned, the "salt" that the experiment uses to randomize a user's group will also change. This means that when you re-start the experiment, your users will be randomly assigned to a group that is not necessarily the same group they were in prior to the experiment being abandoned. This is important because it makes sure that the new result for the group that was not performing well due to an issue like a bug or bad experience in the previous run, is not negatively affected even after the issue is addressed in the new wrong.


Built with [Mintlify](https://mintlify.com).