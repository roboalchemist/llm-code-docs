# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.experimentvalue.md.txt

# ExperimentValue interface

Represents an Experiment value.

**Signature:**

    export interface ExperimentValue 

## Properties

| Property | Type | Description |
|---|---|---|
| [experimentId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.experimentvalue.md#experimentvalueexperimentid) | string | ID of the Experiment to which the value is linked. |
| [variantValue](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.experimentvalue.md#experimentvaluevariantvalue) | [ExperimentVariantValue](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.md#experimentvariantvalue)\[\] | Collection of `ExperimentVariantValue`s that represents the variants served by the Experiment. |

## ExperimentValue.experimentId

ID of the Experiment to which the value is linked.

**Signature:**

    experimentId: string;

## ExperimentValue.variantValue

Collection of `ExperimentVariantValue`s that represents the variants served by the Experiment.

**Signature:**

    variantValue: ExperimentVariantValue[];