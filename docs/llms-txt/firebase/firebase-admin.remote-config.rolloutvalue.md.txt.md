# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.rolloutvalue.md.txt

# RolloutValue interface

Interface representing a value that is linked to a Rollout.

**Signature:**

    export interface RolloutValue 

## Properties

| Property | Type | Description |
|---|---|---|
| [percent](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.rolloutvalue.md#rolloutvaluepercent) | number | The rollout percentage representing the exposure of the rollout value in the target audience. |
| [rolloutId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.rolloutvalue.md#rolloutvaluerolloutid) | string | The ID of the Rollout to which the value is linked. |
| [value](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.rolloutvalue.md#rolloutvaluevalue) | string | The value that is being rolled out. |

## RolloutValue.percent

The rollout percentage representing the exposure of the rollout value in the target audience.

**Signature:**

    percent: number;

## RolloutValue.rolloutId

The ID of the Rollout to which the value is linked.

**Signature:**

    rolloutId: string;

## RolloutValue.value

The value that is being rolled out.

**Signature:**

    value: string;