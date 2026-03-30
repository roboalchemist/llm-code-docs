# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.experimentvariantexplicitvalue.md.txt

# ExperimentVariantExplicitValue interface

Interface representing a specific variant value within an Experiment.

**Signature:**

    export interface ExperimentVariantExplicitValue 

## Properties

| Property | Type | Description |
|---|---|---|
| [noChange](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.experimentvariantexplicitvalue.md#experimentvariantexplicitvaluenochange) | never | Represents an unset `noChange` value. To set `noChange`, use `ExperimentVariantNoChange` instead. |
| [value](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.experimentvariantexplicitvalue.md#experimentvariantexplicitvaluevalue) | string | Value of the variant within an Experiment. |
| [variantId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.experimentvariantexplicitvalue.md#experimentvariantexplicitvaluevariantid) | string | ID of the variant value within an Experiment. |

## ExperimentVariantExplicitValue.noChange

Represents an unset `noChange` value. To set `noChange`, use `ExperimentVariantNoChange` instead.

**Signature:**

    noChange?: never;

## ExperimentVariantExplicitValue.value

Value of the variant within an Experiment.

**Signature:**

    value: string;

## ExperimentVariantExplicitValue.variantId

ID of the variant value within an Experiment.

**Signature:**

    variantId: string;