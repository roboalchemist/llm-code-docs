# Source: https://posthog.com/docs/experiments/testing-and-launching.md

# Testing and launching an experiment - Docs

Once you've written your code, it's a good idea to test that each variant behaves as you'd expect. If you find out your implementation had a bug after you've launched the experiment, you lose days of effort as the experiment results can no longer be trusted.

The best way to do this is **adding an optional override** to your [release conditions](/docs/feature-flags/creating-feature-flags.md#release-conditions). For example, you can create an override to assign a user to the `test` variant if their email is your own (or someone in your team). To do this:

1.  Go to your experiment feature flag.

2.  Ensure the feature flag is enabled by checking the "Enable feature flag" box.

3.  Add a new condition set with the condition to `email = your_email@domain.com`. Set the rollout percentage for this set to 100%.

    -   In cases where `email` is not available (such as when your users are logged out), you can use a parameter like `utm_source` and append `?utm_source=your_variant_name` to your URL.
4.  Set the optional override for the variant you'd like to assign these users to.

5.  Click "Save".

Once you test it works, launch your experiment.

## Further reading

Want to learn more about how to run successful experiments in PostHog? Try these tutorials:

-   [A software engineer's guide to A/B testing](/blog/ab-testing-guide-for-engineers.md)
-   [8 annoying A/B testing mistakes every engineer should know](/blog/ab-testing-mistakes.md)
-   [When and how to run group-targeted A/B tests](/blog/running-group-targeted-ab-tests.md)

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better