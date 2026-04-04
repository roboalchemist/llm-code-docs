# Source: https://docs.frigade.com/sdk/js/step.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Step JS Type Definition

All of Frigade's Javascript SDKs share the same Flow Step type definition which is defined in the [Frigade JS SDK](https://www.npmjs.com/package/@frigade/js).

The Step type is a representation of a step in a Flow.

It contains all the data and methods needed to build custom components with Frigade and to interact with the Frigade API without writing a single custom network call.

# Properties

### \$state

**\$state**: `Object`

The state of the step for the given user in the given Flow.
Example:

```
{
 completed: true,
 skipped: false,
 started: true,
 visible: true,
 blocked: false,
 lastActionAt: "2014-01-01T23:28:56.782Z"
}
```

***

### autoMarkCompleted

`Optional` **autoMarkCompleted**: `boolean`

Automatically mark the step as completed when the primary button is clicked. Default is false.

***

### backButtonTitle

`Optional` **backButtonTitle**: `string`

Text on button if a back button is present.

***

### complete

**complete**: (#propertypayload), `optimistic?`: `boolean`) => `Promise`\<`void`>

Marks the step completed.

**Param**

If true, the step will be marked as completed without waiting for the API and validation of any targeting rules.

**Parameters**

| Name          | Type                                  | Description                                                                                                      |
| :------------ | :------------------------------------ | :--------------------------------------------------------------------------------------------------------------- |
| `properties?` | [`PropertyPayload`](#propertypayload) | -                                                                                                                |
| `optimistic?` | `boolean`                             | If true, the step will be marked as completed without waiting for the API and validation of any targeting rules. |

**Returns**

`Promise`\<`void`>

***

### completionCriteria

`Optional` **completionCriteria**: `string`

Criteria that needs to be met for the step to complete.
Completion criteria uses Frigade's [Targeting Engine](https://docs.frigade.com/v2/platform/targeting) to determine if the step should be completed.

***

### dismissible

`Optional` **dismissible**: `boolean`

Whether the step is dismissible (for instance, tooltips or other non-essential steps).

***

### flow

**flow**: `Flow`

Reference to this step's parent Flow

***

### iconUri

`Optional` **iconUri**: `string`

Icon url to be shown for components supporting icons.

***

### id

**id**: `string`

***

### imageUri

`Optional` **imageUri**: `string`

Image url to be shown for components supporting image.

***

### onStateChange

**onStateChange**: (`callback`: (`step`: [`FlowStep`](FlowStep.md), `previousStep?`: [`FlowStep`](FlowStep.md)) => `void`) => `void`

Event handler called when this step's state changes.

**Deprecated**

Use `frigade.on('step.complete' | 'step.skip' | 'step.reset' | 'step.start', handler)` instead.

**Parameters**

| Name       | Type                                                                                      |
| :--------- | :---------------------------------------------------------------------------------------- |
| `callback` | (`step`: [`FlowStep`](FlowStep.md), `previousStep?`: [`FlowStep`](FlowStep.md)) => `void` |

**Returns**

`void`

**Deprecated**

Use `frigade.on('step.complete' | 'step.skip' | 'step.reset' | 'step.start', handler)` instead.

***

### order

**order**: `number`

Order of the step in the Flow.

***

### primaryButton

`Optional` **primaryButton**: `Object`

Config for the primary button in this step

\| `action?` | [`StepAction`](#stepaction) | Primary button action. (defaults to step.complete) |
\| `target?` | `string` | Primary button URI target (defaults to \_self). |
\| `title?` | `string` | Primary button title. If omitted, the primary button will not be shown. |
\| `uri?` | `string` | Primary button URI. |

***

### primaryButtonTitle

`Optional` **primaryButtonTitle**: `string`

**Deprecated**

Use primaryButton.title instead

**Description**

Primary button title. If omitted, the primary button will not be shown.

***

### primaryButtonUri

`Optional` **primaryButtonUri**: `string`

**Deprecated**

Use primaryButton.uri instead

**Description**

Primary button URI.

***

### primaryButtonUriTarget

`Optional` **primaryButtonUriTarget**: `string`

**Deprecated**

Use primaryButton.target instead

**Description**

Primary button URI target (defaults to \_self).

***

### progress

`Optional` **progress**: `number`

Progress if the step is tied to another Frigade Flow through completionCriteria.

***

### removeStateChangeHandler

**removeStateChangeHandler**: (`callback`: (`step`: [`FlowStep`](FlowStep.md), `previousStep?`: [`FlowStep`](FlowStep.md)) => `void`) => `void`

Removes the given callback from the list of event handlers.

**Parameters**

| Name       | Type                                                                                      |
| :--------- | :---------------------------------------------------------------------------------------- |
| `callback` | (`step`: [`FlowStep`](FlowStep.md), `previousStep?`: [`FlowStep`](FlowStep.md)) => `void` |

**Returns**

`void`

***

### reset

**reset**: () => `Promise`\<`void`>

Resets the step (useful for undoing a finished step).

**Returns**

`Promise`\<`void`>

***

### secondaryButton

`Optional` **secondaryButton**: `Object`

Config for the secondary button in this step

\| `action?` | [`StepAction`](#stepaction) | Secondary button action. (defaults to step.complete) |
\| `target?` | `string` | Secondary button URI target (defaults to \_self). |
\| `title?` | `string` | Secondary button title. If omitted, the secondary button will not be shown. |
\| `uri?` | `string` | Secondary button URI. |

***

### secondaryButtonTitle

`Optional` **secondaryButtonTitle**: `string`

**Deprecated**

Use secondaryButton.title instead

**Description**

Secondary button title. If omitted, the secondary button will not be shown.

***

### secondaryButtonUri

`Optional` **secondaryButtonUri**: `string`

**Deprecated**

Use secondaryButton.uri instead

**Description**

Secondary button URI.

***

### secondaryButtonUriTarget

`Optional` **secondaryButtonUriTarget**: `string`

**Deprecated**

Use secondaryButton.target instead

**Description**

Secondary button URI target (defaults to \_self)

***

### skip

**skip**: (#propertypayload), `optimistic?`: `boolean`) => `Promise`\<`void`>

Marks the step skipped. Works similar to step.complete()

**Parameters**

| Name          | Type                                  |
| :------------ | :------------------------------------ |
| `properties?` | [`PropertyPayload`](#propertypayload) |
| `optimistic?` | `boolean`                             |

**Returns**

`Promise`\<`void`>

***

### skippable

`Optional` **skippable**: `boolean`

If true, the step will be marked as completed when the secondary button is clicked.

***

### start

**start**: (#propertypayload)) => `Promise`\<`void`>

Marks the step started. This will move the current step index to the given step.

**Parameters**

| Name          | Type                                  |
| :------------ | :------------------------------------ |
| `properties?` | [`PropertyPayload`](#propertypayload) |

**Returns**

`Promise`\<`void`>

***

### startCriteria

`Optional` **startCriteria**: `string`

Criteria that needs to be met for the step to start.
Start criteria uses Frigade's [Targeting Engine](https://docs.frigade.com/v2/platform/targeting) to determine if the step should be started.

***

### stepName

`Optional` **stepName**: `string`

Name of the step when shown in a list view.

***

### subtitle

`Optional` **subtitle**: `string`

Subtitle of the step.

***

### title

`Optional` **title**: `string`

Title of the step.

***

### videoUri

`Optional` **videoUri**: `string`

Video url to be shown for components supporting video.

***

### visibilityCriteria

`Optional` **visibilityCriteria**: `string`

Criteria that needs to be met for the step to be visible.
Visibility criteria uses Frigade's [Targeting Engine](https://docs.frigade.com/v2/platform/targeting) to determine if the step should be visible.

[View definition](https://github.com/FrigadeHQ/frigade-react/blob/b8996ad7/packages/js-api/src/core/types.ts#L216)
