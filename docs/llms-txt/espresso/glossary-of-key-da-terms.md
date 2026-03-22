# Source: https://docs.espressosys.com/network/appendix/glossary-of-key-da-terms.md

# Glossary of Key Terms

**Data Availability Layer** - Storage nodes that guarantee the availability and retrievability of transaction raw data and in charge of the eventual dissemination of the full data across the network.

**Data Availability Proposal** - The DA proposal is a proposal on a block for data availability. The consensus on a data availability proposal makes sure that enough parties have the block data. The DA proposal consists of the block and the corresponding view number.

**Data Availability Votes -** A DA vote is a vote indicating the receipt of either a DA proposal or a valid VID share. The vote contains the justify QC commitment, view number, block commitment, signature, and vote token.\
\
**Data Availability Certificate (DAC)** - DAC is a certificate that the proposed data is available to a quorum of distinct parties in the random small data availability (DA) committee. A DA leader, after receiving a sufficient number of votes on its DA proposal, assembles the votes into an optimistic DAC.\
\
**Data Retrievability Certificate -** A retrievability certificate is a certificate that valid VID shares are available to a quorum of replicas. This ensures the liveness/data availability of the HotShot protocol even if the random small DA committee is bribed by an adversary. A DA leader assembles the retrievability certificate after receiving enough votes from the entire node/replica set.

**Optimistic Data Availability Certificate -** A optimistic DA certificate is a certificate that the proposed data is available to a quorum of distinct parties in the random small data availability (DA) committee. A DA leader, after receiving a sufficient number of votes on its DA proposal, assembles the votes into an optimistic DAC.

\
**Commitment Proposal** - A commitment proposal is a proposal on a block commitment. A block can only be applied to the chain if the consensus on the commitment proposal is reached. A commitment proposal is used as follows:

* A (consensus) leader, upon receiving a DAC for this view or sufficient quorum votes for the previous view, will construct a commitment proposal and multicast it to replicas. The commitment proposal will contain the block commitment, view number, height, justify QC, and the proposer ID.
* A node, after receiving the commitment proposal, if also gets either the DAC or the DA proposal, will validate the set and send the quorum vote back to the leader.\\

**Quorum Vote** - quorum vote is a vote on the commitment proposal representing the status of the node/replica's decision on the proposal.

*`Yes Vote`:* is sent if the replica successfully verifies the commitment proposal. It consists of the justify QC commitment, view number, leaf commitment, signature, and vote token.\
\
\&#xNAN;*`No Vote`:* on the contrary, indicates the replica's rejection. A no vote has the same contents as a yes vote.

*`Timeout Vote`*: means the replica cannot decide due to timeout. Therefore, it does not include the leaf commitment as the yes or no vote does, but has all the other fields.

The node is not only signing on the data that is voted on but also the vote type, preventing a dishonest node from altering the vote. E.g., it is impossible to use the signature associated with a no vote to create a yes vote.\
\
**DA Vote** - A node vote on the data commitment, indicating the receipt of either the corresponding data proposal or a valid VID share.
