# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.trendingissuedetails.md.txt

# alerts.crashlytics.TrendingIssueDetails interface

Generic Crashlytics trending issue interface

**Signature:**  

    export interface TrendingIssueDetails 

## Properties

|                                                                                           Property                                                                                            |                                                                            Type                                                                            |                             Description                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [eventCount](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.trendingissuedetails.md#alertscrashlyticstrendingissuedetailseventcount) | number                                                                                                                                                     | The number of crashes that occurred with the issue                   |
| [issue](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.trendingissuedetails.md#alertscrashlyticstrendingissuedetailsissue)           | [Issue](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.issue.md#alertscrashlyticsissue_interface) | Basic information of the Crashlytics issue                           |
| [type](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.trendingissuedetails.md#alertscrashlyticstrendingissuedetailstype)             | string                                                                                                                                                     | The type of the Crashlytics issue, e.g. new fatal, new nonfatal, ANR |
| [userCount](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.trendingissuedetails.md#alertscrashlyticstrendingissuedetailsusercount)   | number                                                                                                                                                     | The number of distinct users that were affected by the issue         |

## alerts.crashlytics.TrendingIssueDetails.eventCount

The number of crashes that occurred with the issue

**Signature:**  

    eventCount: number;

## alerts.crashlytics.TrendingIssueDetails.issue

Basic information of the Crashlytics issue

**Signature:**  

    issue: Issue;

## alerts.crashlytics.TrendingIssueDetails.type

The type of the Crashlytics issue, e.g. new fatal, new nonfatal, ANR

**Signature:**  

    type: string;

## alerts.crashlytics.TrendingIssueDetails.userCount

The number of distinct users that were affected by the issue

**Signature:**  

    userCount: number;