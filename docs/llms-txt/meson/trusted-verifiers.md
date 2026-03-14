# Source: https://docs.meson.fi/protocol/meson/trusted-verifiers.md

# Trusted Verifiers

In a standard atomic swap process, the initiator of the swap (usually the user) needs to perform a second signature. This step is necessary for security reasons:

1. The user can personally verify that the counterparty (usually an LP) has correctly locked the corresponding funds on the target chain.
2. The user's funds are locked for a longer period than the LP's funds, so the user needs to sign a second time within the LP's lock period.

However, this can somewhat affect the user experience. The user needs to wait in the application interface for a period of time after initiating the swap to complete the second signature. To improve the user experience, we propose the role of *Trusted Verifiers*.

Trusted Verifiers perform the check on behalf of the user whether the LP has correctly locked funds on the target chain. They can represent the user or be neutral. This means that in a swap, the Trusted Verifier and the LP are different, and there should be no mutual interest between them.

A Trusted Verifier can be global meaning that it can be trusted by all users. Alternatively, a Trusted Verifier can be trusted by only one or a few users. The verification process is done through a signature, so a Trusted Verifier can be an individual or a group with multisig or other cryptographic settings.

Trusted Verifiers must be online at all times. The process of a swap involving a Trusted Verifier is as follows:

1. The user (she) can confirm in advance which verifiers she trusts;
2. The user publishes a swap request as in the normal process and her funds will be locked on the initial chain. Then, the LP (he) willing to match the swap completes the fund locking on the target chain;
3. The user can leave after she submits the swap request. The Trusted Verifier she trusts will verify that the LP's operation is correct, and after confirmation, will release a *verification signature*;
4. The verification signature contains a valid *release window* which is within the LP's fund locking period and shorter (for example, 10 minutes). The LP needs to complete his operation within this release window;
5. After receiving the verification signature, the matching LP can generate the release signature by himself. This release signature can be executed by anyone on both the initial and target chains to transfer the locked funds to the user and the LP, respectively;
6. To prioritize the user's receive of the swap funds, the release signature generated from verification can only release the LP's locked funds during the release window. However, during the entire LP fund locking period, LP's locked funds can be released to the user. The LP should prioritize releasing funds to the user within the release window. Otherwise, after the release window, anyone can still execute the release signature, but the LP will be penalized.

The main advantage of this process is that the user can stop paying attention to the swap process after submitting the swap request. The subsequent steps will be completed by her Trusted Verifiers and the matching LP. The user can set her trust strategy based on her security needs, such as trusting more verifiers for small swaps but trusting only a few or no other verifiers for large swaps. In the latter case, the user still signs twice to complete the entire swap process.
