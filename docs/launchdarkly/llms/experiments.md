# Source: https://launchdarkly.com/docs/api/experiments.md

> ### Available for subscription customers
>
> Experimentation is available to all customers on a Developer, Foundation, or Enterprise subscription. If you're on an older Pro or Enterprise plan, Experimentation is available as an add-on. To learn more, [read about our pricing](https://launchdarkly.com/pricing/). To change your plan, [contact Sales](https://launchdarkly.com/contact-sales/).


> ### This feature is in beta
>
> To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources](https://launchdarkly.com/docs/api#beta-resources).
>
> Resources that are in beta are still undergoing testing and development. They may change without notice, including becoming backwards incompatible.

Experimentation lets you validate the impact of features you roll out to your app or infrastructure. You can measure things like page views, clicks, load time, infrastructure costs, and more. By connecting metrics you create to flags in your LaunchDarkly environment, you can measure the changes in your customers' behavior based on what flags they evaluate. You can run experiments with any type of flag, including boolean, string, number, and JSON flags. To learn more, read [Experimentation](https://launchdarkly.com/docs/home/experimentation).

You can manage experiments by using the dedicated experiment endpoints described below.

Several of the endpoints require a treatment ID or a flag rule ID. Treatment IDs are returned as part of the expanded [Get experiment](https://launchdarkly.com/docs/api/experiments/get-experiment#expanding-the-experiment-response) response. Winning treatment IDs are also returned as part of the [Get experiment](https://launchdarkly.com/docs/api/experiments/get-experiment) response. They are the `winningTreatmentId` in the `currentIteration`, the `winningTreatmentId` in the `draftIteration`, and the `winningTreatmentId` in each element of the `previousIterations` array. In the flags object, the rule ID is the ID of the variation or rollout of the flag. Each flag variation ID is returned as part of the [Get feature flag](https://launchdarkly.com/docs/api/feature-flags/get-feature-flag) response. It is the `_id` field in each element of the `variations` array.
