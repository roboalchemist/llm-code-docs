# Source: https://firebase.google.com/docs/database/rest/app-management.md.txt

This document explains how you can manage your app's Firebase Realtime Database Security Rules through the REST API.

## Updating Firebase Realtime Database Security Rules


Using the REST API, you can write and update
[Firebase Realtime Database Security Rules](https://firebase.google.com/docs/database/security) for your
Firebase app by making a `PUT` request to the `/.settings/rules.json` path.
To do this, we'll need an access token to [authenticate our REST request](https://firebase.google.com/docs/database/rest/auth)


In this example, we enable read access for all data in our Firebase database:

```
curl -X PUT -d '{ "rules": { ".read": true } }' 'https://docs-examples.firebaseio.com/.settings/rules.json?access_token=<ACCESS_TOKEN>'
```

> [!IMPORTANT]
> Writing Firebase Realtime Database Security Rules through the REST API will overwrite any existing rules.

## Retrieving Firebase Realtime Database Security Rules


Similarly, we can make a GET request to the `/.settings/rules.json` path of our app's
URL to retrieve our Firebase Realtime Database Security Rules:

```
curl 'https://docs-examples.firebaseio.com/.settings/rules.json?access_token=<ACCESS_TOKEN>'
```


The response will contain all of the rules for our app.