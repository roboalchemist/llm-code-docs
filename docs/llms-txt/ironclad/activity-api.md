# Source: https://clickwrap-developer.ironcladapp.com/docs/activity-api.md

# Activity API

The Activity API exposes a super-fast, highly available API. The purpose of this API is to manage 3 things:

* Determine in super real-time whether your user has agreed to the latest version of a contract
* Retrieving the versions and revisions of a Contract your Signers have agreed to
* Sending activity ("Signed", "Visited", etc.) in real-time within a web or mobile app

All Ironclad Clickwrap Activity can be passed as an `HTTP GET` call to the endpoints and the parameters passed as URL parameters.

*The API URL for the Ironclad Clickwrap Activity API is[https://pactsafe.io](https://pactsafe.io)*