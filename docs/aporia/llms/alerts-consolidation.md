# Source: https://docs.aporia.com/monitors-and-alerts/alerts-consolidation.md

# Alerts Consolidation

In the following guide we'll explain how you consolidate alerts within Aporia in order to avoid unnecessary noise when multiple alerts originate from the same monitor. In the following example, we have created a monitor to detect drift across all model's features. Out of the 15 features in this model, 8 are drifting.

<figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2Fw10mhb8SpJ2xkDp2IIRP%2Fimage.png?alt=media&#x26;token=c964e14c-e530-446d-9a3f-6700013f2d0e" alt="" width="563"><figcaption></figcaption></figure>

## Consolidating alerts over time

Let's assume that you don't want to be notified every time the monitor runs that your features are drifting but rather get a new alert if your features are still drifting after a week has gone by. In such case, you can tick the cadence limit checkbox as done in the following image:

<figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FwR3c1aNOYQH8HDYX5Fpz%2Fimage.png?alt=media&#x26;token=195a15a3-8744-4db9-a156-aeb3e247bec8" alt=""><figcaption></figcaption></figure>

That way you'll have have 8 alerts, one per each drifting feature, and every new instance of a specific feature alert will be consolidated with its already existing alert. In the following image you can see that each alert has 3 occurrences as this monitor has been running for 3 weeks.

<figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FbhUQ2IVOUIcsuMegggwc%2Fimage.png?alt=media&#x26;token=f4ff9955-2620-4a74-a263-c693e78f38db" alt=""><figcaption></figcaption></figure>

When clicking on "View all occurrences" you will be able to see all of the consolidated alerts separately

<figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2Fc4eDHRU53BIzrga0ra7O%2Fimage.png?alt=media&#x26;token=5dbf0d27-ffce-48b1-b031-20e8ba30dd93" alt=""><figcaption></figcaption></figure>

## Consolidating multiple features/segment/versions into one alert

Let's assume that you don't want to be notified separately per each drifting feature in this monitor but rather get notified once for all the drifting features. In such case, you can tick the grouping limit checkbox as done in the following image:

<figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FswCbm8Dkct2DP5TJSsfq%2Fimage.png?alt=media&#x26;token=0531c8f7-c54f-4d64-885d-49e5a0983b52" alt=""><figcaption></figcaption></figure>

That way you'll get only one alert if any of the 8 features are drifting, as you can see in the following image:

<figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2Fv0QnrMLYJSfTyBKv1kpI%2Fimage.png?alt=media&#x26;token=33792226-ef11-4658-af46-3670029d8928" alt=""><figcaption></figcaption></figure>

When clicking on "View all occurrences" you will be able to see visualization & explanation for each of the drifting features separately.

<figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FvaljDBSeT26NfF1S4cwI%2Fimage.png?alt=media&#x26;token=9d46724f-6138-4fa3-b13d-a969f4601f8c" alt=""><figcaption></figcaption></figure>

Please note that the consolidation by fields is only supported as an addition to the consolidation by time, and can't be used without the time consolidation.
