# Source: https://docs.carv.io/carv-ecosystem/verifier-nodes/how-do-verifier-nodes-work/attestation.md

# Attestation

**Attestation Verification Process:**

* When a tee submits an attestation, the service contract requests a random number from Chainlink VRF. Upon receiving the random number, it selects up to 200 nodes from the active online node list as verification nodes for the attestation.
* **Random Node Selection Rules:**
  1. Determine the number of verification nodes C based on the current number of online nodes.
  2. If the number of online nodes is greater than 100, the verification nodes will be 10% of the online nodes.
  3. If the number of online nodes is between 10 and 100, the verification nodes will be 10 nodes.
  4. If the number of online nodes is fewer than 10, all online nodes will be verification nodes.
  5. Using the random number R obtained from VRF, calculate the starting index: $$Index\_{begin} = R mod C$$.
  6. Starting from the **Index\_begin** in the active node list, the next **C nodes** will be selected as verifier nodes for the round (if the index exceeds the list's length, it will loop back to the beginning).

The selected verification nodes must submit their verifications within the specified time frame. If more than half of the selected nodes submit their verifications, and a majority validate the attestation as valid, the attestation is approved.
