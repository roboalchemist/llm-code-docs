# Source: https://doc.keepnetlabs.com/next-generation-product/platform/awareness-educator/training-completion-queries.md

# Training Completion Queries

### Overview

This document guides the address of issues related to training completion and certificate issuance within the Keepnet platform. It specifically targets situations where users have finished their training but have yet to receive their completion certificates and offers solutions to improve user experience and administrative responses.

### Problem Description

Users may report having completed their training without receiving the appropriate completion certificate. Investigations often reveal that these users have completed the training but have yet to trigger the necessary system signals to register their completion officially.

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2FEK3Uz5l4H7mEKnvNaZWf%2FScreenshot%202024-04-16%20at%2016.40.36.png?alt=media&#x26;token=97ddd510-0efd-4578-91ae-7ea77833a357" alt="Training or completion status screen — example 1."><figcaption><p>Training or completion status screen — example 1.</p></figcaption></figure>

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fo3AUqv8fdwnRGYU27feP%2FScreenshot%202024-05-14%20at%2008.57.10.png?alt=media&#x26;token=fbbe4651-e1b4-41ea-ba93-42f01a8c89eb" alt="Training or completion status screen — example 2."><figcaption><p>Training or completion status screen — example 2.</p></figcaption></figure>

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2FavsuEMYkpSZTepsGqUuh%2FScreenshot%202024-05-14%20at%2009.09.17.png?alt=media&#x26;token=14220cc2-07f1-4d1c-90b8-907643b4cd56" alt="Training or completion status screen — example 3."><figcaption><p>Training or completion status screen — example 3.</p></figcaption></figure>

### **Technical Explanation**

The Keepnet platform uses SCORM (Sharable Content Object Reference Model) to manage and track online training. A critical aspect of this model is the <mark style="color:blue;">**LMSFINISH**</mark> signal, which must be sent to the platform to officially mark a training session as completed. If a user finishes the training content but remains on the page without closing the window or clicking the "Save/Exit" button, the system does not receive the <mark style="color:blue;">**LMSFINISH**</mark> signal. Consequently, the session remains incomplete in the system records.

### Solution

To ensure that users properly complete training sessions and receive their certificates, the following solutions are proposed:

**User Experience Enhancements:**

Clear Instructions at Course End:

* Incorporate explicit instructions at the end of the training content prompting users to either:
  * "Please click 'Save and Exit' to finish your training," or
  * Notify users that "In 10 seconds, this page will automatically close," ensuring the trigger of the LMSFINISH signal.

Automated Page Closure:

* Implement an automatic closure feature for the training page after a short delay post-training completion. This ensures that the system correctly sends the LMSFINISH signal even if the user fails to manually exit.

**Guidelines for Managed Service Providers (MSPs):**

Verification of Training Completion:

* MSPs should verify the training completion status in the "Training Report > Users" section of the administrative platform.

Handling Discrepancies:

* If a user claims to have completed the training but the report indicates otherwise, MSPs should instruct the user to ensure they have clicked the "Save/Exit" button at the end of the session or have closed the training window to signal completion properly.

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2FZdxK26ZEe7qJuo97H8Ut%2FThis%20one.png?alt=media&#x26;token=34584f60-10f6-4c8b-a330-cb6215c1a766" alt="Training Report Users — verifying completion status."><figcaption><p>Training Report > Users — verifying completion status.</p></figcaption></figure>
