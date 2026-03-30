# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/State.md.txt

# State

The possible lifecycle states of a Firebase App. Learn more about states in Google's [AIP-216 standard](https://google.aip.dev/216).

| Enums ||
|---|---|
| `STATE_UNSPECIFIED` | Unspecified state. |
| `ACTIVE` | The App is active. |
| `DELETED` | The App has been soft-deleted. After an App has been in the `DELETED` state for more than 30 days, it is considered expired and will be permanently deleted. Up until this time, you can restore the App by calling `Undelete` ([Android](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps/undelete) \| [iOS](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps/undelete) \| [web](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps/undelete)). |