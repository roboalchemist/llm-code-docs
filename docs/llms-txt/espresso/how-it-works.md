# Source: https://docs.espressosys.com/network/concepts/the-espresso-network/properties-of-hotshot/espresso-data-availability-layer/how-it-works.md

# How It Works

### **Overview**

The data availability process initiates with sequencers submitting blocks to HotShot. Each view[^1], a leader is selected within [HotShot](https://github.com/EspressoSystems/HotShot/blob/main/docs/HotShotDocs/main.md) who bundles these blocks into a single block within HotShot. Rather than sending the full block data to other HotShot nodes, the leader only sends a commitment to the block for other nodes to vote on. All HotShot nodes also participate as storage nodes in the VID protocol and receive a small chunk representing their VID share of the respective block. The [DA leader](#user-content-fn-2)[^2] sends a [DA proposal](#user-content-fn-3)[^3] to the randomly sampled DA committee and all HotShot nodes. After receiving enough votes from the DA committee and the nodes in the network, the DA leader constructs a data availability certificate (DAC).

The DAC is composed of an optimistic DAC obtained from the DA committee and a retrievability certificate from the VID protocol. The optimistic DAC certifies that the proposed data is available to a quorum of the DA committee. The retrievability certificate in turn certifies that VID chunks are available to a quorum of nodes. The DAC design thus enables the best of both worlds, fast DA through DA committees, and robustness through VID. By combining the block commitment with the DAC, Tiramisu ensures that HotShot blocks will only finalized if data is guaranteed to be available.

**Exhibit A: DA and Rollup Architecture**

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-b43689a93843fad8c7d65bc6ea441ab1d4419fec%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

### **Process Steps**

**Step 1:** The DA leader begins a broadcast to ensure data is available for all nodes in the network that consists of:

* Sending the DA proposal to the DA committee.
* Sending the VID chunks to all replicas/nodes.
* Gradually sending the DA proposal to all replicas/nodes. Broadcasting proceeds concurrently, prioritized by order of initialization.

A DA proposal will be rejected in either of the following cases:

* The view number is earlier than the view corresponding to the latest valid [quorum certificate](#user-content-fn-4)[^4] (QC).
* The proposal is not from the correct leader.

**Step 2:** Nodes receive the DA proposal (and/or VID share) and submit the data availability vote.

Anyone who receives and approves the DA proposal sends a strong DA vote to the DA leader, while anyone who only receives the VID share sends a normal DA vote.

**Step 3:** The DAC is formed.

The DAC is formed with the creation of the retrievability certificate and optimistic DAC certificate.

The retrievability certificate can be formed by:

* The DA leader receives f + 1 strong votes, which may come from nodes on the committee or just regular nodes who happened to receive the DA proposal quickly enough. f = number of faulty nodes (nodes not performing correct function) in the entire network.
* f + m normal votes, where m is the number of VID shares the block was split into.

The optimistic DAC can be formed in the following way:

1\. The DA leader receives 2f + 1 strong votes from the DA committee (where, unlike above, f is the number faulty nodes in the committee, not in the entire network)

The DA leader stops broadcasting to the nodes after the DAC is formed, or when the quorum certificate from the next leader is received.

**Step 4:** The block commitment proposal is sent to replicas/nodes. The block commitment is a a cryptographic proof that a block is valid and has guaranteed DA.

The leader, once getting sufficient quorum votes for the previous view and the DAC is obtained, sends the commitment proposal. A block can only be applied to a chain if consensus on the commitment proposal is reached by HotShot consensus nodes. The leader also sends the QC to the next leader if one can be constructed.

**Step 5:** The HotShot nodes validate the commitment proposal.

The replicas/nodes validate the commitment proposal if either of the following set is received:

* Commitment proposal and the DAC.
* Commitment proposal and DA proposal, which is simply a block and the view number proposed

The node will send a quorum vote to the next consensus leader once the commitment proposal is validated. As long as over 2/3 of HotShot stake is honest, it is impossible for an adversary, even if bribing the DA committee, to forge a DAC. Utilizing the randomly elected DA committee alongside VID thus enables fast and secure DA, and disincentivizes bribery attacks.

**Exhibit B: DA Process Overview**

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-6e8454f48747acdc354c687ce81f60e5ff549d53%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

### **Implementation Options**

By integrating with the Espresso Network, chains can utilize EspressoDA without any additional integration work. However, chains retain the flexibility to use the DA solution of their choice (i.e., chains can use the Espresso Network for fast confirmations, but use Ethereum or another third-party provider for DA).

[^1]: *A view is a period of time during which nodes in the network perform their tasks. For each view, a leader is selected. The leader and nodes coordinate in the view to try to reach consensus.*

[^2]: This is always the same entitiy as the HotShot leader

[^3]: a proposal on a data blob for data availability that consists of the block's transaction data and view number

[^4]: certificate of all the votes nodes have sent to the leader for some specific block
