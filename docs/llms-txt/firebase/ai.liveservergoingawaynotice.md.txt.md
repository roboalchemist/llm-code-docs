# Source: https://firebase.google.com/docs/reference/js/ai.liveservergoingawaynotice.md.txt

# LiveServerGoingAwayNotice interface

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Notification that the server will not be able to service the client soon.

**Signature:**

    export interface LiveServerGoingAwayNotice 

## Properties

| Property | Type | Description |
|---|---|---|
| [timeLeft](https://firebase.google.com/docs/reference/js/ai.liveservergoingawaynotice.md#liveservergoingawaynoticetimeleft) | number | ***(Public Preview)*** The remaining time (in seconds) before the connection will be terminated. |
| [type](https://firebase.google.com/docs/reference/js/ai.liveservergoingawaynotice.md#liveservergoingawaynoticetype) | 'goingAwayNotice' | ***(Public Preview)*** |

## LiveServerGoingAwayNotice.timeLeft

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

The remaining time (in seconds) before the connection will be terminated.

**Signature:**

    timeLeft: number;

## LiveServerGoingAwayNotice.type

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    type: 'goingAwayNotice';