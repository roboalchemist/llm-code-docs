# Source: https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/app-governed-root-of-trust.md

# App-Governed Root of Trust

In addition to providing an optimistic timeout period during which fraud can be challenged, Nomad's design has a secondary component to increase root of trust security — application specific governance having a say in its root of trust.

Functionally, this means cross-chain applications (or [xApps](https://docs.nomad.xyz/developers/application-developers/building-xapps)) built on Nomad can delegate Watcher permissions as they prefer. By enabling this choice at the *application* layer, Nomad ensures that local governance has a stake in preserving the safety of cross-chain messages processed by its respective application.

### Application-Specific Watcher Sets

As described in the previous sections on [fraud](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/fraud), Nomad relies on [Watchers](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/watchers) to flag any fraudulent attestations by the Updater. Because [Replicas](https://docs.nomad.xyz/the-nomad-protocol/smart-contracts/replica) wait for the optimistic timeout window to process messages, Watchers have the ability to inform the Replica of fraud via submitting a transaction and prevent processing of dishonest messages.&#x20;

Instead of having a system-level Watcher set, Nomad enables applications via the [Router pattern](https://docs.nomad.xyz/developers/application-developers/advanced/router-pattern) to define their own Watcher sets by deploying a xAppConnectionManager.&#x20;

#### [xAppConnectionManager](https://docs.nomad.xyz/the-nomad-protocol/smart-contracts/xappconnectionmanager)&#x20;

Every application must deploy a  contract that maintains a nested mapping called `watcherPermissions`. This data structure contains the following mappings:

`watcher address => replica remote domain id => permission boolean`

For example, a specific application may dictate that address `0xabcd` has permissions to disconnect its application from a Replica for Moonbeam, but not Evmos.

This level of granular permissions ensures that application developers have a full say on which watchers they delegate the responsibility of keeping their apps safe.&#x20;

For low overhead, applications can use the Nomad default set of watchers by using the Nomad-managed xAppConnectionManager. This xAppConnectionManager protects the Nomad Bridge and is a great option for developers wishing to bootstrap their application.

For more granular control, applications can configure their own set of Watchers by deploying a new xAppConnectionManager. Customized Watchers could be run by the application developer themselves, or any number of additional trusted parties who the app team wishes to include.

Furthermore, applications can switch from one xAppConnectionManager to another at any time. This makes it easy to begin with the default set of Watchers for ease of use, then graduate to a custom set of Watchers over time.
