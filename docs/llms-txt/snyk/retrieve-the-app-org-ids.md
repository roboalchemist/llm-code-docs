# Source: https://docs.snyk.io/snyk-api/using-specific-snyk-apis/snyk-apps-apis/set-up-a-snyk-app-using-the-oauth2-api/retrieve-the-app-org-ids.md

# Retrieve the App Org IDs

Users may connect with a single Organization or a single Group. Most of the Snyk API endpoints require an `orgid` in the path, which is used for authorizing the action being performed.

To retrieve the `orgid` that is used by your App, send a GET request to the `orgs` endpoint, [List accessible organizations](https://docs.snyk.io/reference/orgs#get-orgs) at the following URL:

`https://api.snyk.io/rest/orgs?version={version}`

Snyk recommends you store this value and associate it with the user's details.
