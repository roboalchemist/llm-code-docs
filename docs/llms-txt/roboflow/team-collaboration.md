# Source: https://docs.roboflow.com/roboflow/roboflow-ko/annotate/team-collaboration.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/anotto/team-collaboration.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/annotate/team-collaboration.md

# Source: https://docs.roboflow.com/annotate/team-collaboration.md

# Collaborate on Labeling

Whether you have a small team working on labeling hundreds of images or a large team working on millions, creating a dataset is about more than drawing boxes. A big part of labeling is in the process of getting an image from the real world into a trained model's stored knowledge that involves image collection, storage, organization, selection, assignment, labeling, and review.

Roboflow offers collaborative features that allow you to:

* Divide work between multiple team members by assigning labeling jobs to anyone on the team
* Organize images into batches as you upload them
* Provide image labeling instructions to help guide work and ensure consistency
* Get an at-a-glance view of labeling work in progress
* See a historical timeline of all labeling work
* Revert changes
* Add comments to images and view image comment history
* Send images with labeling issues back to team members for changes
* Approve or reject labels before including them in a dataset

### Assign Labeling Jobs

You can divide labeling work among a team or assign it to specific people responsible for labeling. Assigning jobs to individual team members means you won't have to worry about stepping on each others' work if you're online at the same time.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-3d03f750bc80afa125f9c70dfdfe5c2ede3f0e88%2FScreenshot%202025-06-27%20at%2015.58.55.png?alt=media" alt=""><figcaption></figcaption></figure>

You can choose to assign jobs to one or more people on your team and if you haven’t included a team member to your workspace yet, you can also [invite them](https://docs.roboflow.com/workspaces/team-members/invite-a-team-member) and assign an labeling job to be completed at the same time.

### **Provide** Labeling Instructions

You can provide instructions to labelers from the Assign Images tab. Click "Add Instructions" to add instructions to a batch before assigning the batch to an labeler. When you have set your instructions, click "Assign Images".

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-9425465335ac442051fe5f8b66d8a2b95069e1a1%2FScreenshot%202025-06-27%20at%2016.00.33.png?alt=media" alt=""><figcaption></figcaption></figure>

Click "Edit" to assign instructions:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-208d4f5de293fdaece24a1e0439b313660ab9b1d%2FScreenshot%202025-06-27%20at%2016.09.22.png?alt=media" alt=""><figcaption></figcaption></figure>

Click "Save Instructions" to save the labeling instructions.

### Job Notifications

Once a labeling job has been assigned, a notification will alert your team members when there's work assigned to them.

### Labeling Jobs Board

The labeling jobs board gives an at-a-glance view of the current state of your individually assigned jobs as they go through the labeling process.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-763594df65168569a56cfe229cd094d0f4cf9b2a%2FScreenshot%202025-06-27%20at%2016.04.23.png?alt=media" alt=""><figcaption></figcaption></figure>

To view statistics for a particular labeler, specify a value in the `Labeler` dropdown.

### Job Details

Clicking on individual jobs on the labeling jobs board gives a more detailed view of the individual job and its progress. You can quickly see images that still need to be labeling and reassign jobs to different team members as needed.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-6ed68f7f7521a5de9a7e9e63bcb97dd3e3ca8342%2FScreenshot%202025-06-27%20at%2016.05.41.png?alt=media" alt=""><figcaption></figcaption></figure>

### Review Mode

You can individually approve or reject labeled images and send them back to the labeler for rework when necessary. To do so, click on a batch of images. Then, navigate between the Approved, Rejected, and To Do tabs to view the state of images in a job.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-dc9c04eb0d0d59159e8281aec2a6c94477c755ea%2FScreenshot%202025-06-27%20at%2016.06.07.png?alt=media" alt=""><figcaption></figcaption></figure>
