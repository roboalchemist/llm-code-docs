# Source: https://docs.baseten.co/development/model-apis/deprecation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Deprecation

> Baseten's deprecation policy for Model APIs

As open source models advance rapidly, Baseten prioritizes serving the highest quality models and deprecates specific Model APIs when stronger alternatives are available. When a model is selected for deprecation, Baseten follows this process:

1. **Announcement**
   * Deprecations are announced approximately two weeks before the deprecation date.
   * Documentation is updated to identify the model being deprecated and recommend a replacement.
   * Affected users are contacted via email.
2. **Transition**
   * The deprecated model remains fully functional until the deprecation date. You have approximately two weeks to transition using one of these options:
     1. Migrate to a dedicated deployment with the deprecated model weights. [Contact us](https://www.baseten.co/talk-to-us/deprecation-inquiry/) for assistance.
     2. Update your code to use an active model (a recommendation is provided in the deprecation announcement).
3. **Deprecation date**
   * The model ID for the deprecated model becomes inactive and returns an error for all requests.
   * A changelog notification is published with the recommended replacement.

## Planned deprecations

| Deprecation Date | Model                          | Recommended Replacement                            | Dedicated Available |
| :--------------- | :----------------------------- | :------------------------------------------------- | :-----------------: |
| 2026-2-06        | Qwen3 Coder 480B A35B Instruct | [GLM 4.7](https://www.baseten.co/library/glm-4-7/) |          ✅          |
