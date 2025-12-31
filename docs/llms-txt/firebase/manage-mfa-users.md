# Source: https://firebase.google.com/docs/auth/admin/manage-mfa-users.md.txt

<br />

This document shows you how to use theFirebaseAdmin SDKto manage your multi-factor users programmatically. When managing multi-factor users, you have access to an increased range of user properties compared to[single-factor users](https://firebase.google.com/docs/auth/admin/manage-users).

## Before you begin

[Install the Node.jsAdmin SDK](https://firebase.google.com/docs/admin/setup). OtherAdmin SDKlanguages are not currently supported.

## Getting users

You can retrieve user multi-factor related data, such as a list of enrolled second factors, from the`UserRecord`object. To get a user record, call`getUser()`or`getUserByEmail()`.

The example below shows a multi-factor enrolled user:  

    // console.log(userRecord.toJSON());
    {
      uid: 'some-uid',
      displayName: 'John Doe',
      email: 'johndoe@gmail.com',
      photoURL: 'http://www.example.com/12345678/photo.png',
      emailVerified: true,
      phoneNumber: '+11234567890',
      // Set this user as admin.
      customClaims: {admin: true},
      // User with Google provider.
      providerData: [{
        uid: 'google-uid',
        email: 'johndoe@gmail.com',
        displayName: 'John Doe',
        photoURL: 'http://www.example.com/12345678/photo.png',
        providerId: 'google.com'
      }],
      multiFactor: {
        enrolledFactors: [
          // 2FA with SMS as 2nd factor.
          {
            uid: '53HG4HG45HG8G04GJ40J4G3J',
            phoneNumber: '+16505551234',
            displayName: 'Work phone',
            enrollmentTime: 'Fri, 22 Sep 2017 01:49:58 GMT',
            factorId: 'phone',
          },
        ],
      },
    };

## Listing users

The code below shows how to list all users and check if they have a secondary factor enrolled:  

    admin.auth().listUsers(1000, nextPageToken)
      .then((listUsersResult) => {
        listUsersResult.users.forEach((userRecord) => {
          // Multi-factor enrolled users second factors can be retrieved via:
          if (userRecord.multiFactor) {
            userRecord.multiFactor.enrolledFactors.forEach((enrolledFactor) => {
              console.log(userRecord.uid, enrolledFactor.toJSON());
            });
          }
        });
      })
      .catch((error) => {
        console.log('Error listing users:', error);
      });

Users are returned in batches, ordered by their`uid`. Each batch of results contains a list of users, and a next page token used to fetch the next batch. When all users have been listed, no`pageToken`is returned.

The`maxResult`field specifies the maximum batch size. The default and maximum value is 1000.

## Creating a user

Call`createUser()`to create a new user. New users with secondary factors must have a verified email address (set`emailVerified`to`true`) and use a supported first factor to sign in. Up to 5 secondary factors are allowed per user.

The example shows how to create a new user with 2 secondary factors:  

    admin.auth().createUser({
      uid: '123456789',
      email: 'user@example.com',
      emailVerified: true,
      password: 'password',
      multiFactor: {
        enrolledFactors: [
          // When creating users with phone second factors, the uid and
          // enrollmentTime should not be specified. These will be provisioned by
          // the Auth server.
          // Primary second factor.
          {
            phoneNumber: '+16505550001',
            displayName: 'Corp phone',
            factorId: 'phone',
          },
          // Backup second factor.
          {
            phoneNumber: '+16505550002',
            displayName: 'Personal phone',
            factorId: 'phone'
          },
        ],
      },
    })
    .then((userRecord) => {
      console.log(userRecord.multiFactor.enrolledFactors);
    })
    .catch((error) => {
      console.log(error);
    });

## Updating a user

To update an existing user, call`updateUser()`:  

    admin.auth().updateUser(uid: '123456789', {
      multiFactor: {
        enrolledFactors: [
          {
            // uid will be auto-generated.
            phoneNumber: '+16505550003',
            displayName: 'Spouse\'s phone',
            factorId: 'phone',
          },
          {
            // uid can also be specified. This is useful if a new second factor is added and an
            // existing enrolled second factor is kept unmodified.
            uid: 'existing-enrolled-mfa-uid',
            phoneNumber: '+16505550004',
            displayName: 'Personal phone',
            factorId: 'phone',
          },
          {
            phoneNumber: '+16505550005',
            displayName: 'Backup phone',
            factorId: 'phone',
            // Enrollment time can also be explicitly specified.
            enrollmentTime: new Date().toUTCString(),
          },
        ],
      },
    })
    .then((userRecord) => {
      console.log(userRecord.multiFactor.enrolledFactors);
    })
    .catch((error) => {
      console.log(error);
    });

### Adding a new secondary factor

Calling`updateUser()`with a list of`enrolledFactors`will erase any of the user's current secondary factors. To add a new secondary factor while preserving the existing ones, look up the user first, then add the new factor to the list:  

    function enrollSecondFactor(userId, secondFactorPhoneNumber, secondFactorDisplayName) {
      return admin.auth().getUser(userId)
        .then((userRecord) => {
          const updatedList = (userRecord.multiFactor &&
            userRecord.multiFactor.toJSON().enrolledFactors) || [];
          updatedList.push({
            phoneNumber: secondFactorPhoneNumber,
            displayName: secondFactorDisplayName,
            factorId: 'phone',
          });
          return admin.auth().updateUser(userRecord.uid, {
            multiFactor: {
              enrolledFactors: updatedList,
            },
          });
        })
        .catch((error) => {
          console.log(error);
        });
    }

### Removing a secondary factor

To completely unenroll a user from multi-factor authentication, set`enrolledFactors`to`null`or an empty array:  

    admin.auth().updateUser(uid: '123456789', {
      multiFactor: {
        enrolledFactors: null,
      },
    })
    .then((userRecord) => {
      console.log(userRecord.multiFactor);
    })
    .catch((error) => {
      console.log(error);
    });