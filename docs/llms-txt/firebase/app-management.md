# Source: https://firebase.google.com/docs/database/rest/app-management.md.txt

<br />

This document explains how you can manage your app'sFirebase Realtime DatabaseSecurity Rulesthrough the REST API.  

## UpdatingFirebase Realtime DatabaseSecurity Rules

Using the REST API, you can write and update[Firebase Realtime DatabaseSecurity Rules](https://firebase.google.com/docs/database/security)for your Firebase app by making a`PUT`request to the`/.settings/rules.json`path. To do this, we'll need an access token to[authenticate our REST request](https://firebase.google.com/docs/database/rest/auth)

In this example, we enable read access for all data in our Firebase database:  

```
curl -X PUT -d '{ "rules": { ".read": true } }' 'https://docs-examples.firebaseio.com/.settings/rules.json?access_token=<ACCESS_TOKEN>'
```
WritingFirebase Realtime DatabaseSecurity Rulesthrough the REST API will overwrite any existing rules.  

## RetrievingFirebase Realtime DatabaseSecurity Rules

Similarly, we can make a GET request to the`/.settings/rules.json`path of our app's URL to retrieve ourFirebase Realtime DatabaseSecurity Rules:  

```
curl 'https://docs-examples.firebaseio.com/.settings/rules.json?access_token=<ACCESS_TOKEN>'
```

The response will contain all of the rules for our app.