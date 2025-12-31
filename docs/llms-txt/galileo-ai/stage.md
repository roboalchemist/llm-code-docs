# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-protect/concepts/stage.md

# Stage

> A set of rulesets that are applied during _one_ invocation.

A stage can be composed of multiple rulesets, each of which is executed independently and defined as a prioritized list (i.e. order matters). The action for the ruleset with the highest priority is chosen for composing the response.

Stages can be managed centrally (i.e. registered once and updated dynamically) or locally within the application.

## Different Types of Stages

| Dimension                                                                              | Central                                                                                                                                    | Local                                                                                                                 |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| [Ruleset](/galileo/gen-ai-studio-products/galileo-protect/concepts/ruleset) Definition | During stage creation (i.e. [`gp.create_stage`](https://protect.docs.rungalileo.io/#galileo_protect.create_stage) step) before invocation. | Within the [`gp.invoke`](https://protect.docs.rungalileo.io/#galileo_protect.invoke) function, during the invocation. |
| Stage Versioning                                                                       | Central stage definitions can be updated and applied to all *future* invocations.                                                          | New versions are created to match the ruleset definitions within the invocation.                                      |
| Stage Management                                                                       | Central stage updated by using [`gp.update_stage`](https://protect.docs.rungalileo.io/#galileo_protect.update_stage).                      | Local stages definitions can be updated in the `gp.invoke` invocation.                                                |
| Stage Pause / Resumption                                                               | Central stage definitions can be paused and resumed.                                                                                       | Local stages are created and invoked can be paused or resumed.                                                        |

### When should I use central vs local stages?

We recommend using Central Stages, if:

* You want to allow non-application developers to update your Protect configuration

* You want to be able to dynamically update your Protect configuration on the fly. Without having to wait for code reviews or deployments.

We recommend using Local Stages, if:

* You're an application developer and are setting up Protect for the first time on your project. We find it's always easier to iterate through code.

* You want changes to your Protect configuration to go through the same code-review, release and deployment process as the rest of your application.
