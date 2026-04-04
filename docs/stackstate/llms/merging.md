# Source: https://archivedocs.stackstate.com/5.1/stackpacks/integrations/opentelemetry/manual-instrumentation/merging.md

# Merging components

## Overview

StackState can merge components from a custom instrumentation with pre-existing components. You can use this to:

* Add extra attributes to pre-existing components.
* Create custom relations for pre-existing components.
* Influence the propagation of health state. For details, see the page [Span health state](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/opentelemetry/manual-instrumentation/span-health).

StackState will merge components with the [same identifier](#component-identifier). After merging, the original component will [inherit all properties](#merging-inheritance) from the component that merged with it. The component that was merged will no longer be visible.

{% hint style="info" %}
**Important to know when merging:**

When a custom instrumentation is merged with a pre-existing StackState component, it might seem that custom instrumentation component disappeared; it did not. All properties of the custom instrumentation component are inherited by the component with which it merges.
{% endhint %}

## Merging inheritance

When a custom instrumentation component is merged with a pre-existing component, the component with which it's merged will inherit all the properties, health, and relations from the custom instrumentation component. This means that, although the custom instrumentation component will no longer be visible, the component that it merged with now acts as both the original component and the custom instrumentation component. The resulting component will now contain, for example, all the labels, telemetry, and health from the custom instrumentation component.

The example below shows an unmerged child component; below are all the `labels` and `identifiers` for this child component.

![Topology Perspective - Labels and Identifiers](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-2d13c56f913896bd0f66fa5b6a291ef9bcb0a629%2Fv51_otel_unmerged_child.png?alt=media)

And on the right side, we included the list of health checks and telemetry also running on the child.

![Topology Perspective - Unmerged Healthy OTEL Component](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-1968f8c42651d491dd69d636a2b729b2db7ab62e%2Fv51_otel_unmerged_child_health.png?alt=media)

Now when we look at the component that we want to merge with, you will notice the `labels` and `identifiers` contain none of the same ones we looked at when viewing the child component.

![Topology Perspective - Labels and Identifiers After Merge](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-8456a6034a1b4fbdd55ac6ef2bdcde8ba9f8f332%2Fv51_otel_merging_attempt.png?alt=media)

This is the same for the health checks and telemetry on the right side.

![Topology Perspective - Component Merged Health State](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-5ce60fc63c0944df6693e643347bb63851894cb0%2Fv51_otel_merge_attempt_health.png?alt=media)

Now let's see the result after merging our child component with the pre-existing StackState component.

Let's look at the `identifiers` and `labels` again. As you can see in the image below the `identifiers` stayed the same but the `labels` merged, This StackState merged component now contain the values from both.

![Topology Perspective - Labels and Identifiers After Merge](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-05a9b3d6cd4aafc338119824cd4b2c12bf2995a9%2Fv51_otel_after_merge_labels.png?alt=media)

The same can be seen in the health checks and telemetry. You will notice that the health checks and telemetry streams are from both components.

![Topology Perspective - Component Merged Health State](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-92bc9946b377aadc343ae4a3d48e243af55cc5c1%2Fv51_otel_after_merge_health.png?alt=media)

## Component identifier

If two components in StackState have the same `identifier`, StackState will merge those two components.

For example, if you select a component and click on the `SHOW ALL PROPERTIES` button on the right panel

![Topology Perspective - Show All Properties Button Position](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-b554945447fbfb5d0f9a245a45e2d93ff74fe054%2Fv51_otel_relation_example_a.png?alt=media)

It will open a dialog; within this dialog, you can see the identifiers. If you reuse any of these within your span, it will merge with that component, We will have a few visual examples further down in the documentation.

![Topology Perspective - Component properties - Identifiers](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-1b7ee95cb94984293ca62918c8b7e603b8dbe616%2Fv51_otel_relation_example_b.png?alt=media)

## Example: Merging a component

Let's take the following example; we have three components that we create, all having the previous one as their parent span.

```
Service Name: Parent Component
|
---> Service Name: Child Component
     |
     ---> Service Name: Child 2 Component
```

That will create the following components with relations.

![Topology Perspective - OTEL Components Unmerged Example](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-e510278f5e42b4b8afcdfd2586cc9a010394ffa4%2Fv51_otel_topology_perspective_healthy_component.png?alt=media)

Now let's add a few pre-existing Lambda functions into the picture. We are focusing on the healthy Lambda function in the bottom right corner.

![Topology Perspective - OTEL Components and Pre-Existing Components](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-df164adf5cbef2c2965550a96e0ff0ee43c3ce11%2Fv51_otel_scenario_pre-existing_components.png?alt=media)

If we click on that Lambda function, we will be able to see what the identifier is by using the same `service identifier` `arn:aws:lambda:eu-west-1:965323806078:function:otel-example-custom-instrumentation-dev-create-custom-component` in our second component it will merge with that pre-existing component.

![Topology Perspective - Component properties - Identifier](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-12f98168bc8b7964cbfcb5a5b2fa72e98e46144f%2Fv51_otel_traces_merge_with_healthy.png?alt=media)

That will result in the following happening. As you can see, the component we merged now has new relations, and those relations are the same ones our component had as the merged component inherited the same relations

![Topology Perspective - Merged Component](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-84926485250e8de8de791595156f81289d292bb0%2Fv51_otel_traces_merge_with_healthy_complete.png?alt=media)
