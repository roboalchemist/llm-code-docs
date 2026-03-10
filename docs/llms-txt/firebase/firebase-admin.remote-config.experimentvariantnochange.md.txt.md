# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.experimentvariantnochange.md.txt

# ExperimentVariantNoChange interface

Represents a no-change variant value within an Experiment.

**Signature:**

    export interface ExperimentVariantNoChange 

## Properties

| Property | Type | Description |
|---|---|---|
| [noChange](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.experimentvariantnochange.md#experimentvariantnochangenochange) | true | Represents a no-change variant value within an Experiment. If `true`, the variant served to the client is equal to the value against the next condition in the evaluation order (or the default value if no conditions are applicable). |
| [value](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.experimentvariantnochange.md#experimentvariantnochangevalue) | never | Represents an unset value as only one of `noChange` or `value` can be set. To set a variant value, use `ExperimentVariantExplicitValue` instead. |
| [variantId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.experimentvariantnochange.md#experimentvariantnochangevariantid) | string | ID of the variant value within an Experiment. |

## ExperimentVariantNoChange.noChange

Represents a no-change variant value within an Experiment. If `true`, the variant served to the client is equal to the value against the next condition in the evaluation order (or the default value if no conditions are applicable).

**Signature:**

    noChange: true;

## ExperimentVariantNoChange.value

Represents an unset value as only one of `noChange` or `value` can be set. To set a variant value, use `ExperimentVariantExplicitValue` instead.

**Signature:**

    value?: never;

## ExperimentVariantNoChange.variantId

ID of the variant value within an Experiment.

**Signature:**

    variantId: string;