# Source: https://firebase.google.com/docs/remote-config/rollouts/about.md.txt

# Source: https://firebase.google.com/docs/remote-config/personalization/about.md.txt

<br />

Personalization uses machine learning---specifically a contextual multi-armed bandit algorithm---to determine the optimal experience for individual users to achieve an objective. In our case, the objective is to optimize for the total number or the total parameter value of specificGoogle Analyticsevents.

### What's a contextual multi-armed bandit algorithm?

The "multi-armed bandit" is a metaphor used to describe the situation where we want to continually choose a path that leads to the highest, most reliable rewards from a list of multiple paths. To visualize this, you can use the metaphor of a gambler in front of a row of slot machines--often colloquially referred to as a "one-armed bandit" because a slot machine has one handle (or arm) and takes your money. Since we want to solve for multiple "arms," the one-armed bandit becomes the*multi-armed*bandit.

For example, say we have three options and we want to determine which provides the most reliable reward: We could try each option, and then, after receiving a result, we could just keep choosing the arm that yielded the most rewards. This is what's referred to as a*greedy*algorithm: the option that yields the best result when we first attempt it is the one we'll continue to choose. But we can understand that this might not always work---for one thing, the high reward could be a fluke. Or maybe there's some user-specific context that resulted in higher rewards during that time period that wouldn't be as effective later.

So*context* is added to make the algorithm more effective. ForRemote Configpersonalization, this initial context is random sampling, or*uncertainty* , that provides some entropy to the experiment. This implements a "*contextual*multi-armed bandit." As the experiment continues to run, ongoing exploration and observation adds real learned context about which arms are most likely to elicit a reward to the model, making it more effective.

### What does this mean for my app?

Now, let's discuss what a multi-armed bandit algorithm means in the context of your app. Let's say you're optimizing for banner ad clicks. In this case, the "arms" of the personalization would be the*alternative values* you specify to represent the different banner ads you want to display to users. The banner ad click is the reward, which we refer to as an*objective*.
| **Key Term:** **Alternative values** may also sometimes be referred to as*variants*.

When you first launch a personalization, the model does not know which alternative value will be more likely to achieve your goal for each individual user. As the personalization explores each alternative value to understand the likelihood of achieving your objective, the underlying model grows more informed, improving its ability to predict and select the optimum experience for each user.

Personalization uses a*stickiness window*of 24 hours. This is the amount of time the personalization algorithm explores a single alternative value. You should provide your personalizations enough time to explore each alternative value multiple times (generally about 14 days). Ideally, you can let them run perpetually so that they can continually improve and adapt as your app and user behaviors change.
| **Note:** Multiple personalizations are supported, but each personalization learns the optimum values for each user independently.

### Track additional metrics

Remote Configpersonalization also provides the ability to track up to two additional metrics, to help you contextualize your results. Let's say you've developed a social app and have set different alternative values to encourage users to share content with friends to increase overall engagement.

In this case, you might choose to optimize for anAnalyticsevent like`link_received`and set your two metrics to`user_engagement`and`link_opened`to understand whether user engagement and the number of links the user opens rises (true engagement) or falls (possibly too many spammy links).

While these additional metrics won't be factored into the personalization algorithm, you can track them right alongside your personalization results, providing valuable insight into the personalization's ability to achieve your overall goals.

### Understand personalization results

After a personalization has been running for long enough to gather data, you can view its results.

To view personalization results:

1. Open the[Remote Configpage](https://console.firebase.google.com/project/_/config)and click[Personalizations](https://console.firebase.google.com/project/_/config/personalizations).

2. Select the personalization you want to view. You can search for the specific personalization by name or objective, and can sort by Name, Start time, or Total lift.

The results page summarizes the**Total lift** , or percentage difference in performance, that the personalization provides over the**Baseline**group.
| **Key Term:** The**baseline group**consists of about 20% of the number of users included in the personalized group. Its results are scaled up to provide an accurate comparison. Each user in the baseline group receives one of the values in the personalization, which never changes throughout the lifetime of the personalization.

The results page also shows the current status of the personalization, the attributes of the personalization, and an interactive graph that:

- Shows a detailed daily and total view of how the personalization performed against the baseline.

- Shows how each value performs overall across the baseline group.

- Displays goal outcomes and performance against the additional metrics you chose, accessible using the tabs at the top of the summary.

A personalization can be left running indefinitely and you can continue to revisit the results page to monitor its performance. The algorithm will continue to learn and adjust, so that it can adapt when user behavior changes.
| **Tip:** If a personalization does not have positive results after 14 days, the most likely reason is that the different alternatives do not produce substantially different results. In this case, you can end the personalization and choose any alternative.

## Understand personalization deletion

You can delete a personalization using theFirebaseconsole or by removing a personalization parameter from your template using the[Firebase Remote ConfigAPI](https://firebase.google.com/docs/remote-config/automate-rc#update_the_remote_config_template). Deleted personalizations cannot be restored. To learn about data retention, see[Data deletion](https://firebase.google.com/terms/data-processing-terms#6.-data-deletion).

You can also delete personalizations by[rolling back](https://firebase.google.com/docs/remote-config/templates#rollback)or[importing a template](https://firebase.google.com/docs/remote-config/templates#download_and_publish_templates).

### Rollbacks

If your current template has personalizations and you[roll back](https://firebase.google.com/docs/remote-config/templates#rollback)to a template that does not have the same personalizations, the personalizations are deleted. To revert to a previous template, use theFirebaseconsole or[`roll back`](https://firebase.google.com/docs/reference/remote-config/rest#rest-resource:-v1.projects.remoteconfig)using theFirebase Remote ConfigAPI.

When you delete a personalization and roll back to a previous template, a reference to that invalid personalization appears in theFirebaseconsole. You can remove the invalid personalization from the[Firebaseconsole](https://console.firebase.google.com//project/_/config)by editing the personalization in the Parameters tab of theRemote Configpage.

### Imports

Importing a template that no longer contains your current personalizations also deletes those personalizations. To import a template,[use theFirebaseconsole](https://firebase.google.com/docs/remote-config/templates#download_and_publish_templates)or use the[Remote ConfigREST API](https://firebase.google.com/docs/remote-config/automate-rc#update_the_remote_config_template).

## Next steps

- ExploreRemote Configpersonalization[use cases](https://firebase.google.com/docs/remote-config/personalization/use-cases).

- [Get started](https://firebase.google.com/docs/remote-config/personalization/get-started)withRemote Configpersonalization.