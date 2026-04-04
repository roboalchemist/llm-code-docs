# Source: https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/State.md.txt

# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/State.md.txt

# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/State.md.txt

# State

The state of an execution or a step that indicates their level of completion.

|                                                                                                Enums                                                                                                ||
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `unknownState` | Should never be in this state. Exists for proto deserialization backward compatibility.                                                                                             |
| `pending`      | The Execution/Step is created, ready to run, but not running yet. If an Execution/Step is created without initial state, it is assumed that the Execution/Step is in PENDING state. |
| `inProgress`   | The Execution/Step is in progress.                                                                                                                                                  |
| `complete`     | The finalized, immutable state. Steps/Executions in this state cannot be modified.                                                                                                  |