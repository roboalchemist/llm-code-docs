# HarmBench Plugin

The HarmBench plugin uses the [HarmBench dataset](https://github.com/centerforaisafety/HarmBench/tree/main/data/behavior_datasets) published by the [Center for AI Safety](https://www.safe.ai/) to test LLM responses to harmful prompts. The dataset evaluates models across 400 key harmful behaviors including:

- Chemical and biological threats (e.g., dangerous substances, weapons)
- Illegal activities (e.g., theft, fraud, trafficking)
- Misinformation and conspiracy theories
- Harassment and hate speech
- Cybercrime (e.g., malware, system exploitation)
- Copyright violations

Unlike many of our other plugins, the HarmBench plugin uses a statically generated dataset vs dynamically generating cases such as those for [Harmful behavior detection](/docs/red-team/plugins/harmful/) (which was partially based on HarmBench's classifications for harmful behavior), [excessive agency](/docs/red-team/plugins/excessive-agency/), [hallucination](/docs/red-team/plugins/hallucination/) and others. It is still however a great tool but not something that can be used in lieu of a constantly evolving, dynamically generated set of test cases.

## Configuration

To include the HarmBench plugin in your LLM red teaming setup:

```yaml
redteam:
  plugins:
    - harmbench
```

You can control the number of test cases using the `numTests` parameter:

```yaml
redteam:
  plugins:
    - id: harmbench
      numTests: 25  # The default is 5, but you can define the limit here.
```

## References

- [HarmBench Paper](https://arxiv.org/abs/2402.04249)
- [HarmBench Dataset](https://github.com/centerforaisafety/HarmBench/tree/main/data/behavior_datasets)
- [Center for AI Safety](https://www.safe.ai/)

## Related Concepts

- [Types of LLM Vulnerabilities](/docs/red-team/llm-vulnerability-types/)
- [Evaluating LLM safety with HarmBench](/docs/guides/evaling-with-harmbench/)
- [Harmful Content Plugin](/docs/red-team/plugins/harmful/)
- [BeaverTails Plugin](/docs/red-team/plugins/beavertails/)
- [CyberSecEval Plugin](/docs/red-team/plugins/cyberseceval/)
- [Pliny Plugin](/docs/red-team/plugins/pliny/)

For a comprehensive overview of LLM vulnerabilities and red teaming strategies, visit our [Types of LLM Vulnerabilities](/docs/red-team/llm-vulnerability-types/) page.