# Source: https://firebase.google.com/docs/auth/admin/manage-users.md.txt

<br />

The Firebase Admin SDK provides an API for managing your
Firebase Authentication users with elevated privileges. The admin user management API
gives you the ability to programmatically complete the following tasks from a
secure server environment:

- Create new users without any throttling or rate limiting.
- Look up users by different criteria such as uid, email or phone number.
- List all the users of a specified project in batches.
- Access user metadata including account creation date and last sign-in date.
- Delete users without requiring their existing password.
- Update user properties - including their password - without having to sign in as the user.
- Verify emails without having to go through the out-of-band action flows for verifying emails.
- Change a user's email without sending email links to revoke these changes.
- Create a new user with a phone number without having to go through the SMS verification flow.
- Change a user's phone number without having to go through the SMS verification flow.
- Offline provision users in a disabled state and then later control when to enable them.
- Build custom user consoles that are tailored to a specific application's user management system.

## Before you begin

To use the user management API provided by the Firebase Admin SDK, you
must have a service account. Follow the [setup instructions](https://firebase.google.com/docs/admin/setup)
for more information on how to initialize the Admin SDK.

## Retrieve user data

The primary way to identify a user is by their `uid`, a unique identifier for
that user. The Admin SDK provides a method that allows fetching the profile
information of users by their `uid`:

### Node.js

    getAuth()
      .getUser(uid)
      .then((userRecord) => {
        // See the UserRecord reference doc for the contents of userRecord.
        console.log(`Successfully fetched user data: ${userRecord.toJSON()}`);
      })
      .catch((error) => {
        console.log('Error fetching user data:', error);
      });https://github.com/firebase/snippets-node/blob/92a575a9eb70b9193aac4d63954e7647cf50fd8f/auth/manage_users.js#L14-L22

### Java

    UserRecord userRecord = FirebaseAuth.getInstance().getUser(uid);
    // See the UserRecord reference doc for the contents of userRecord.
    System.out.println("Successfully fetched user data: " + userRecord.getUid());

### Python

    from firebase_admin import auth

    user = auth.get_user(uid)
    print(f'Successfully fetched user data: {user.uid}')

### Go

    // Get an auth client from the firebase.App
    client, err := app.Auth(ctx)
    if err != nil {
    	log.Fatalf("error getting Auth client: %v\n", err)
    }

    u, err := client.GetUser(ctx, uid)
    if err != nil {
    	log.Fatalf("error getting user %s: %v\n", uid, err)
    }
    log.Printf("Successfully fetched user data: %v\n", u)https://github.com/firebase/firebase-admin-go/blob/4f7026f0837678ceb33ab2d2c145a0d18d9952fd/snippets/auth.go#L149-L159

### C#

    UserRecord userRecord = await FirebaseAuth.DefaultInstance.GetUserAsync(uid);
    // See the UserRecord reference doc for the contents of userRecord.
    Console.WriteLine($"Successfully fetched user data: {userRecord.Uid}");

This method returns a `UserRecord`
object for the user corresponding to the `uid` provided to the method.

If the provided `uid` does not belong to an existing user or the user cannot be
fetched for any other reason, the above method throws an error.
For a full list of error codes, including descriptions and
resolution steps, see [Admin Auth API Errors](https://firebase.google.com/docs/auth/admin/errors).

In some cases you will have a user's email instead of their `uid`. The Firebase
Admin SDK supports looking up user information with an email:

### Node.js

    getAuth()
      .getUserByEmail(email)
      .then((userRecord) => {
        // See the UserRecord reference doc for the contents of userRecord.
        console.log(`Successfully fetched user data: ${userRecord.toJSON()}`);
      })
      .catch((error) => {
        console.log('Error fetching user data:', error);
      });https://github.com/firebase/snippets-node/blob/92a575a9eb70b9193aac4d63954e7647cf50fd8f/auth/manage_users.js#L26-L34

### Java

    UserRecord userRecord = FirebaseAuth.getInstance().getUserByEmail(email);
    // See the UserRecord reference doc for the contents of userRecord.
    System.out.println("Successfully fetched user data: " + userRecord.getEmail());

### Python

    from firebase_admin import auth

    user = auth.get_user_by_email(email)
    print(f'Successfully fetched user data: {user.uid}')

### Go

    u, err := client.GetUserByEmail(ctx, email)
    if err != nil {
    	log.Fatalf("error getting user by email %s: %v\n", email, err)
    }
    log.Printf("Successfully fetched user data: %v\n", u)https://github.com/firebase/firebase-admin-go/blob/4f7026f0837678ceb33ab2d2c145a0d18d9952fd/snippets/auth.go#L167-L171

### C#

    UserRecord userRecord = await FirebaseAuth.DefaultInstance.GetUserByEmailAsync(email);
    // See the UserRecord reference doc for the contents of userRecord.
    Console.WriteLine($"Successfully fetched user data: {userRecord.Uid}");

This method returns a `UserRecord` object for the
user corresponding to the email provided.

If the provided email does not belong to an existing user or the user cannot be
fetched for any other reason, the Admin SDK throws an error.
For a full list of error codes, including descriptions
and resolution steps, see [Admin Authentication API Errors](https://firebase.google.com/docs/auth/admin/errors).

> [!WARNING]
> **Warning:** For email lookup, you can only search the main (top level) email and not provider specific emails. For example, if a Facebook account with a different email `facebookUser@example.com` is linked to an existing user with email `user@example.com`, calling `getUserByEmail("facebookUser@example.com")` will yield no results whereas `getUserByEmail("user@example.com")` will return the expected user. In the case of the default "single account per email" setting, the first email used to sign in with will be used as the top level email unless modified afterwards. When "multiple accounts per email" is set, the main email is only set when a password user is created unless manually updated.

In other cases, you will have a user's phone number instead of their `uid`. The
Firebase Admin SDK supports looking up user information with a phone number:

### Node.js

    getAuth()
      .getUserByPhoneNumber(phoneNumber)
      .then((userRecord) => {
        // See the UserRecord reference doc for the contents of userRecord.
        console.log(`Successfully fetched user data:  ${userRecord.toJSON()}`);
      })
      .catch((error) => {
        console.log('Error fetching user data:', error);
      });https://github.com/firebase/snippets-node/blob/92a575a9eb70b9193aac4d63954e7647cf50fd8f/auth/manage_users.js#L38-L46

### Java

    UserRecord userRecord = FirebaseAuth.getInstance().getUserByPhoneNumber(phoneNumber);
    // See the UserRecord reference doc for the contents of userRecord.
    System.out.println("Successfully fetched user data: " + userRecord.getPhoneNumber());

### Python

    from firebase_admin import auth

    user = auth.get_user_by_phone_number(phone)
    print(f'Successfully fetched user data: {user.uid}')

### Go

    u, err := client.GetUserByPhoneNumber(ctx, phone)
    if err != nil {
    	log.Fatalf("error getting user by phone %s: %v\n", phone, err)
    }
    log.Printf("Successfully fetched user data: %v\n", u)https://github.com/firebase/firebase-admin-go/blob/4f7026f0837678ceb33ab2d2c145a0d18d9952fd/snippets/auth.go#L179-L183

### C#

    UserRecord userRecord = await FirebaseAuth.DefaultInstance.GetUserByPhoneNumberAsync(phoneNumber);
    // See the UserRecord reference doc for the contents of userRecord.
    Console.WriteLine($"Successfully fetched user data: {userRecord.Uid}");

This method returns a `UserRecord` object for the
user corresponding to the phone number provided.

If the provided phone number does not belong to an existing user or the user
cannot be fetched for any other reason, the Admin SDK throws an error.
For a full list of error codes, including descriptions
and resolution steps, see [Admin Authentication API Errors](https://firebase.google.com/docs/auth/admin/errors).

### Bulk retrieve user data

The Firebase Admin SDK also allows retrieving a list of users based on
identifiers that you provide. You can identify users by their user ID, email, or
phone number. A maximum of 100 identifiers can be supplied in a single call.
Identifiers can contain a mix of types:

### Node.js

    getAuth()
      .getUsers([
        { uid: 'uid1' },
        { email: 'user2@example.com' },
        { phoneNumber: '+15555550003' },
        { providerId: 'google.com', providerUid: 'google_uid4' },
      ])
      .then((getUsersResult) => {
        console.log('Successfully fetched user data:');
        getUsersResult.users.forEach((userRecord) => {
          console.log(userRecord);
        });

        console.log('Unable to find users corresponding to these identifiers:');
        getUsersResult.notFound.forEach((userIdentifier) => {
          console.log(userIdentifier);
        });
      })
      .catch((error) => {
        console.log('Error fetching user data:', error);
      });https://github.com/firebase/snippets-node/blob/92a575a9eb70b9193aac4d63954e7647cf50fd8f/auth/manage_users.js#L50-L70

### Java

    GetUsersResult result = FirebaseAuth.getInstance().getUsersAsync(Arrays.asList(
        new UidIdentifier("uid1"),
        new EmailIdentifier("user2@example.com"),
        new PhoneIdentifier("+15555550003"),
        new ProviderIdentifier("google.com", "google_uid4"))).get();

    System.out.println("Successfully fetched user data:");
    for (UserRecord user : result.getUsers()) {
      System.out.println(user.getUid());
    }

    System.out.println("Unable to find users corresponding to these identifiers:");
    for (UserIdentifier uid : result.getNotFound()) {
      System.out.println(uid);
    }

### Python

    from firebase_admin import auth

    result = auth.get_users([
        auth.UidIdentifier('uid1'),
        auth.EmailIdentifier('user2@example.com'),
        auth.PhoneIdentifier(+15555550003),
        auth.ProviderIdentifier('google.com', 'google_uid4')
    ])

    print('Successfully fetched user data:')
    for user in result.users:
        print(user.uid)

    print('Unable to find users corresponding to these identifiers:')
    for uid in result.not_found:
        print(uid)

### Go

    getUsersResult, err := client.GetUsers(ctx, []auth.UserIdentifier{
    	auth.UIDIdentifier{UID: "uid1"},
    	auth.EmailIdentifier{Email: "user@example.com"},
    	auth.PhoneIdentifier{PhoneNumber: "+15555551234"},
    	auth.ProviderIdentifier{ProviderID: "google.com", ProviderUID: "google_uid1"},
    })
    if err != nil {
    	log.Fatalf("error retriving multiple users: %v\n", err)
    }

    log.Printf("Successfully fetched user data:")
    for _, u := range getUsersResult.Users {
    	log.Printf("%v", u)
    }

    log.Printf("Unable to find users corresponding to these identifiers:")
    for _, id := range getUsersResult.NotFound {
    	log.Printf("%v", id)
    }

### C#

    GetUsersResult result = await FirebaseAuth.DefaultInstance.GetUsersAsync(
        new List<UserIdentifier>
        {
            new UidIdentifier("uid1"),
            new EmailIdentifier("user2@example.com"),
            new PhoneIdentifier("+15555550003"),
            new ProviderIdentifier("google.com", "google_uid4"),
        });

    Console.WriteLine("Successfully fetched user data:");
    foreach (UserRecord user in result.Users)
    {
        Console.WriteLine($"User: {user.Uid}");
    }

    Console.WriteLine("Unable to find users corresponding to these identifiers:");
    foreach (UserIdentifier uid in result.NotFound)
    {
        Console.WriteLine($"{uid}");
    }

This method returns a list the same size as the input list, with each entry
containing either the corresponding `UserRecord` or an error indicating why
that identifier was not able to be looked up. For a full list of error codes,
including descriptions and resolution steps, see [Admin Authentication API
Errors](https://firebase.google.com/docs/auth/admin/errors).

## Create a user

The Admin SDK provides a method that
allows you to create a new Firebase Authentication user. This method accepts an
object containing the profile information to include in the newly created
user account:

### Node.js

    getAuth()
      .createUser({
        email: 'user@example.com',
        emailVerified: false,
        phoneNumber: '+11234567890',
        password: 'secretPassword',
        displayName: 'John Doe',
        photoURL: 'http://www.example.com/12345678/photo.png',
        disabled: false,
      })
      .then((userRecord) => {
        // See the UserRecord reference doc for the contents of userRecord.
        console.log('Successfully created new user:', userRecord.uid);
      })
      .catch((error) => {
        console.log('Error creating new user:', error);
      });https://github.com/firebase/snippets-node/blob/92a575a9eb70b9193aac4d63954e7647cf50fd8f/auth/manage_users.js#L74-L90

### Java

    CreateRequest request = new CreateRequest()
        .setEmail("user@example.com")
        .setEmailVerified(false)
        .setPassword("secretPassword")
        .setPhoneNumber("+11234567890")
        .setDisplayName("John Doe")
        .setPhotoUrl("http://www.example.com/12345678/photo.png")
        .setDisabled(false);

    UserRecord userRecord = FirebaseAuth.getInstance().createUser(request);
    System.out.println("Successfully created new user: " + userRecord.getUid());

### Python

    user = auth.create_user(
        email='user@example.com',
        email_verified=False,
        phone_number='+15555550100',
        password='secretPassword',
        display_name='John Doe',
        photo_url='http://www.example.com/12345678/photo.png',
        disabled=False)
    print(f'Sucessfully created new user: {user.uid}')

### Go

    params := (&auth.UserToCreate{}).
    	Email("user@example.com").
    	EmailVerified(false).
    	PhoneNumber("+15555550100").
    	Password("secretPassword").
    	DisplayName("John Doe").
    	PhotoURL("http://www.example.com/12345678/photo.png").
    	Disabled(false)
    u, err := client.CreateUser(ctx, params)
    if err != nil {
    	log.Fatalf("error creating user: %v\n", err)
    }
    log.Printf("Successfully created user: %v\n", u)https://github.com/firebase/firebase-admin-go/blob/4f7026f0837678ceb33ab2d2c145a0d18d9952fd/snippets/auth.go#L214-L226

### C#

    UserRecordArgs args = new UserRecordArgs()
    {
        Email = "user@example.com",
        EmailVerified = false,
        PhoneNumber = "+11234567890",
        Password = "secretPassword",
        DisplayName = "John Doe",
        PhotoUrl = "http://www.example.com/12345678/photo.png",
        Disabled = false,
    };
    UserRecord userRecord = await FirebaseAuth.DefaultInstance.CreateUserAsync(args);
    // See the UserRecord reference doc for the contents of userRecord.
    Console.WriteLine($"Successfully created new user: {userRecord.Uid}");

By default, Firebase Authentication will generate a random `uid` for the new user. If
you instead want to specify your own `uid` for the new user, you can include it
as an argument passed to the user creation method:

### Node.js

    getAuth()
      .createUser({
        uid: 'some-uid',
        email: 'user@example.com',
        phoneNumber: '+11234567890',
      })
      .then((userRecord) => {
        // See the UserRecord reference doc for the contents of userRecord.
        console.log('Successfully created new user:', userRecord.uid);
      })
      .catch((error) => {
        console.log('Error creating new user:', error);
      });https://github.com/firebase/snippets-node/blob/92a575a9eb70b9193aac4d63954e7647cf50fd8f/auth/manage_users.js#L94-L106

### Java

    CreateRequest request = new CreateRequest()
        .setUid("some-uid")
        .setEmail("user@example.com")
        .setPhoneNumber("+11234567890");

    UserRecord userRecord = FirebaseAuth.getInstance().createUser(request);
    System.out.println("Successfully created new user: " + userRecord.getUid());

### Python

    user = auth.create_user(
        uid='some-uid', email='user@example.com', phone_number='+15555550100')
    print(f'Sucessfully created new user: {user.uid}')

### Go

    params := (&auth.UserToCreate{}).
    	UID(uid).
    	Email("user@example.com").
    	PhoneNumber("+15555550100")
    u, err := client.CreateUser(ctx, params)
    if err != nil {
    	log.Fatalf("error creating user: %v\n", err)
    }
    log.Printf("Successfully created user: %v\n", u)https://github.com/firebase/firebase-admin-go/blob/4f7026f0837678ceb33ab2d2c145a0d18d9952fd/snippets/auth.go#L234-L242

### C#

    UserRecordArgs args = new UserRecordArgs()
    {
        Uid = "some-uid",
        Email = "user@example.com",
        PhoneNumber = "+11234567890",
    };
    UserRecord userRecord = await FirebaseAuth.DefaultInstance.CreateUserAsync(args);
    // See the UserRecord reference doc for the contents of userRecord.
    Console.WriteLine($"Successfully created new user: {userRecord.Uid}");

Any combination of the following properties can be provided:

**Table 1. Properties supported by the create user operation**

| Property | Type | Description |
|---|---|---|
| `uid` | string | The `uid` to assign to the newly created user. Must be a string between 1-128 characters long, inclusive. If not provided, a random `uid` will be automatically generated. Shorter `uid`s offer better performance. |
| `email` | string | The user's primary email. Must be a valid email address. |
| `emailVerified` | boolean | Whether or not the user's primary email is verified. If not provided, the default is `false`. |
| `phoneNumber` | string | The user's primary phone number. Must be a valid E.164 spec compliant phone number. |
| `password` | string | The user's raw, unhashed password. Must be at least six characters long. |
| `displayName` | string | The users' display name. |
| `photoURL` | string | The user's photo URL. |
| `disabled` | boolean | Whether or not the user is disabled. `true` for disabled; `false` for enabled. If not provided, the default is `false`. |

> [!NOTE]
> **Note:** All of the above properties are optional. If a certain property is not specified, the value for that property will be empty unless a default is mentioned in the above table.

The user creation method returns a `UserRecord` object for the
newly created user.

If the provided `uid`, email or phone number is already in use by an existing
user or the user cannot be created for any other reason, the above method fails
with an error. For a full list of error codes, including
descriptions and resolution steps, see [Admin Authentication API
Errors](https://firebase.google.com/docs/auth/admin/errors).

## Update a user

The Firebase Admin SDK facilitates modifying an existing user's data. You need
to specify a `uid` along with the properties to update for that user:

### Node.js

    getAuth()
      .updateUser(uid, {
        email: 'modifiedUser@example.com',
        phoneNumber: '+11234567890',
        emailVerified: true,
        password: 'newPassword',
        displayName: 'Jane Doe',
        photoURL: 'http://www.example.com/12345678/photo.png',
        disabled: true,
      })
      .then((userRecord) => {
        // See the UserRecord reference doc for the contents of userRecord.
        console.log('Successfully updated user', userRecord.toJSON());
      })
      .catch((error) => {
        console.log('Error updating user:', error);
      });https://github.com/firebase/snippets-node/blob/92a575a9eb70b9193aac4d63954e7647cf50fd8f/auth/manage_users.js#L110-L126

### Java

    UpdateRequest request = new UpdateRequest(uid)
        .setEmail("user@example.com")
        .setPhoneNumber("+11234567890")
        .setEmailVerified(true)
        .setPassword("newPassword")
        .setDisplayName("Jane Doe")
        .setPhotoUrl("http://www.example.com/12345678/photo.png")
        .setDisabled(true);

    UserRecord userRecord = FirebaseAuth.getInstance().updateUser(request);
    System.out.println("Successfully updated user: " + userRecord.getUid());

### Python

    user = auth.update_user(
        uid,
        email='user@example.com',
        phone_number='+15555550100',
        email_verified=True,
        password='newPassword',
        display_name='John Doe',
        photo_url='http://www.example.com/12345678/photo.png',
        disabled=True)
    print(f'Sucessfully updated user: {user.uid}')

### Go

    params := (&auth.UserToUpdate{}).
    	Email("user@example.com").
    	EmailVerified(true).
    	PhoneNumber("+15555550100").
    	Password("newPassword").
    	DisplayName("John Doe").
    	PhotoURL("http://www.example.com/12345678/photo.png").
    	Disabled(true)
    u, err := client.UpdateUser(ctx, uid, params)
    if err != nil {
    	log.Fatalf("error updating user: %v\n", err)
    }
    log.Printf("Successfully updated user: %v\n", u)https://github.com/firebase/firebase-admin-go/blob/4f7026f0837678ceb33ab2d2c145a0d18d9952fd/snippets/auth.go#L250-L262

### C#

    UserRecordArgs args = new UserRecordArgs()
    {
        Uid = uid,
        Email = "modifiedUser@example.com",
        PhoneNumber = "+11234567890",
        EmailVerified = true,
        Password = "newPassword",
        DisplayName = "Jane Doe",
        PhotoUrl = "http://www.example.com/12345678/photo.png",
        Disabled = true,
    };
    UserRecord userRecord = await FirebaseAuth.DefaultInstance.UpdateUserAsync(args);
    // See the UserRecord reference doc for the contents of userRecord.
    Console.WriteLine($"Successfully updated user: {userRecord.Uid}");

Any combination of the following properties can be provided:

**Table 2. Properties supported by the update user operation**

| Property | Type | Description |
|---|---|---|
| `email` | string | The user's new primary email. Must be a valid email address. |
| `emailVerified` | boolean | Whether or not the user's primary email is verified. If not provided, the default is `false`. |
| `phoneNumber` | string \| `null` | The user's new primary phone number. Must be a valid E.164 spec compliant phone number. Set to `null` to clear the user's existing phone number. |
| `password` | string | The user's new raw, unhashed password. Must be at least six characters long. |
| `displayName` | string \| `null` | The users' new display name. Set to `null` to clear the user's existing display name. |
| `photoURL` | string \| `null` | The users' new photo URL. Set to `null` to clear the user's existing photo URL. If non-`null`, must be a valid URL. |
| `disabled` | boolean | Whether or not the user is disabled. `true` for disabled; `false` for enabled. |

> [!NOTE]
> **Note:** All of the above properties are optional. If a certain property is not specified, the existing value for that property remains unchanged.

The update user method returns an updated `UserRecord` object when the
update successfully completes.

If the provided `uid` does not correspond to an existing user, the provided
email or phone number is already in use by an existing user, or the user cannot
be updated for any other reason, the above method fails with an
error. For a full list of error codes, including descriptions and resolution
steps, see [Admin Authentication API Errors](https://firebase.google.com/docs/auth/admin/errors).

## Delete a user

The Firebase Admin SDK allows deleting existing users by their `uid`:

### Node.js

    getAuth()
      .deleteUser(uid)
      .then(() => {
        console.log('Successfully deleted user');
      })
      .catch((error) => {
        console.log('Error deleting user:', error);
      });https://github.com/firebase/snippets-node/blob/92a575a9eb70b9193aac4d63954e7647cf50fd8f/auth/manage_users.js#L130-L137

### Java

    FirebaseAuth.getInstance().deleteUser(uid);
    System.out.println("Successfully deleted user.");

### Python

    auth.delete_user(uid)
    print('Successfully deleted user')

### Go

    err := client.DeleteUser(ctx, uid)
    if err != nil {
    	log.Fatalf("error deleting user: %v\n", err)
    }
    log.Printf("Successfully deleted user: %s\n", uid)https://github.com/firebase/firebase-admin-go/blob/4f7026f0837678ceb33ab2d2c145a0d18d9952fd/snippets/auth.go#L269-L273

### C#

    await FirebaseAuth.DefaultInstance.DeleteUserAsync(uid);
    Console.WriteLine("Successfully deleted user.");

The delete user method returns an empty result when the deletion completes
successfully.

If the provided `uid` does not correspond to an existing user or the user cannot
be deleted for any other reason, the delete user method throws an error.
For a full list of error codes, including descriptions
and resolution steps, see [Admin Authentication API Errors](https://firebase.google.com/docs/auth/admin/errors).

### Delete Multiple Users

The Firebase Admin SDK can also delete multiple users at once. However,
note that using methods like `deleteUsers(uids)` to delete multiple users at
once will not trigger `onDelete()` event handlers for Cloud Functions for Firebase.
This is because batch delete does not trigger a user deletion event on
each user. Delete users one at
a time if you want user deletion events to fire for each deleted user.

### Node.js

    getAuth()
      .deleteUsers([uid1, uid2, uid3])
      .then((deleteUsersResult) => {
        console.log(`Successfully deleted ${deleteUsersResult.successCount} users`);
        console.log(`Failed to delete ${deleteUsersResult.failureCount} users`);
        deleteUsersResult.errors.forEach((err) => {
          console.log(err.error.toJSON());
        });
      })
      .catch((error) => {
        console.log('Error deleting users:', error);
      });

### Java

    DeleteUsersResult result = FirebaseAuth.getInstance().deleteUsersAsync(
        Arrays.asList("uid1", "uid2", "uid3")).get();

    System.out.println("Successfully deleted " + result.getSuccessCount() + " users");
    System.out.println("Failed to delete " + result.getFailureCount() + " users");
    for (ErrorInfo error : result.getErrors()) {
      System.out.println("error #" + error.getIndex() + ", reason: " + error.getReason());
    }

### Python

    from firebase_admin import auth

    result = auth.delete_users(["uid1", "uid2", "uid3"])

    print(f'Successfully deleted {result.success_count} users')
    print(f'Failed to delete {result.failure_count} users')
    for err in result.errors:
        print(f'error #{result.index}, reason: {result.reason}')

### Go

    deleteUsersResult, err := client.DeleteUsers(ctx, []string{"uid1", "uid2", "uid3"})
    if err != nil {
    	log.Fatalf("error deleting users: %v\n", err)
    }

    log.Printf("Successfully deleted %d users", deleteUsersResult.SuccessCount)
    log.Printf("Failed to delete %d users", deleteUsersResult.FailureCount)
    for _, err := range deleteUsersResult.Errors {
    	log.Printf("%v", err)
    }

### C#

    DeleteUsersResult result = await FirebaseAuth.DefaultInstance.DeleteUsersAsync(new List<string>
        {
            "uid1",
            "uid2",
            "uid3",
        });

    Console.WriteLine($"Successfully deleted {result.SuccessCount} users.");
    Console.WriteLine($"Failed to delete {result.FailureCount} users.");

    foreach (ErrorInfo err in result.Errors)
    {
        Console.WriteLine($"Error #{err.Index}, reason: {err.Reason}");
    }

The delete users method returns a list of failures for the users that were
unable to be deleted. For a full list of error codes, including descriptions
and resolution steps, see [Admin Authentication API Errors](https://firebase.google.com/docs/auth/admin/errors).

## List all users

The Firebase Admin SDK allows retrieving the entire list of users in batches:

### Node.js

    const listAllUsers = (nextPageToken) => {
      // List batch of users, 1000 at a time.
      getAuth()
        .listUsers(1000, nextPageToken)
        .then((listUsersResult) => {
          listUsersResult.users.forEach((userRecord) => {
            console.log('user', userRecord.toJSON());
          });
          if (listUsersResult.pageToken) {
            // List next batch of users.
            listAllUsers(listUsersResult.pageToken);
          }
        })
        .catch((error) => {
          console.log('Error listing users:', error);
        });
    };
    // Start listing users from the beginning, 1000 at a time.
    listAllUsers();https://github.com/firebase/snippets-node/blob/92a575a9eb70b9193aac4d63954e7647cf50fd8f/auth/manage_users.js#L156-L174

### Java

    // Start listing users from the beginning, 1000 at a time.
    ListUsersPage page = FirebaseAuth.getInstance().listUsers(null);
    while (page != null) {
      for (ExportedUserRecord user : page.getValues()) {
        System.out.println("User: " + user.getUid());
      }
      page = page.getNextPage();
    }

    // Iterate through all users. This will still retrieve users in batches,
    // buffering no more than 1000 users in memory at a time.
    page = FirebaseAuth.getInstance().listUsers(null);
    for (ExportedUserRecord user : page.iterateAll()) {
      System.out.println("User: " + user.getUid());
    }

### Python

    # Start listing users from the beginning, 1000 at a time.
    page = auth.list_users()
    while page:
        for user in page.users:
            print('User: ' + user.uid)
        # Get next batch of users.
        page = page.get_next_page()

    # Iterate through all users. This will still retrieve users in batches,
    # buffering no more than 1000 users in memory at a time.
    for user in auth.list_users().iterate_all():
        print('User: ' + user.uid)

### Go

    // Note, behind the scenes, the Users() iterator will retrive 1000 Users at a time through the API
    iter := client.Users(ctx, "")
    for {
    	user, err := iter.Next()
    	if err == iterator.Done {
    		break
    	}
    	if err != nil {
    		log.Fatalf("error listing users: %s\n", err)
    	}
    	log.Printf("read user user: %v\n", user)
    }

    // Iterating by pages 100 users at a time.
    // Note that using both the Next() function on an iterator and the NextPage()
    // on a Pager wrapping that same iterator will result in an error.
    pager := iterator.NewPager(client.Users(ctx, ""), 100, "")
    for {
    	var users []*auth.ExportedUserRecord
    	nextPageToken, err := pager.NextPage(&users)
    	if err != nil {
    		log.Fatalf("paging error %v\n", err)
    	}
    	for _, u := range users {
    		log.Printf("read user user: %v\n", u)
    	}
    	if nextPageToken == "" {
    		break
    	}
    }https://github.com/firebase/firebase-admin-go/blob/4f7026f0837678ceb33ab2d2c145a0d18d9952fd/snippets/auth.go#L394-L423

### C#

    // Start listing users from the beginning, 1000 at a time.
    var pagedEnumerable = FirebaseAuth.DefaultInstance.ListUsersAsync(null);
    var responses = pagedEnumerable.AsRawResponses().GetAsyncEnumerator();
    while (await responses.MoveNextAsync())
    {
        ExportedUserRecords response = responses.Current;
        foreach (ExportedUserRecord user in response.Users)
        {
            Console.WriteLine($"User: {user.Uid}");
        }
    }

    // Iterate through all users. This will still retrieve users in batches,
    // buffering no more than 1000 users in memory at a time.
    var enumerator = FirebaseAuth.DefaultInstance.ListUsersAsync(null).GetAsyncEnumerator();
    while (await enumerator.MoveNextAsync())
    {
        ExportedUserRecord user = enumerator.Current;
        Console.WriteLine($"User: {user.Uid}");
    }

Each batch of results contains a list of users and the next page token used to
list the next batch of users. When all the users have already been listed, no
`pageToken` is returned.

If no `maxResults` field is specified, the default 1000 users per batch is used.
This is also the maximum number of users allowed to be listed at a time. Any
value greater than the maximum will throw an argument error.
If no `pageToken` is specified, the operation will list users from the
beginning, ordered by `uid`.

For a full list of error codes, including descriptions
and resolution steps, see [Admin Authentication API Errors](https://firebase.google.com/docs/auth/admin/errors).

### Password hashes of listed users

This API also returns the `passwordSalt` and `passwordHash` hashed by the
Firebase Auth backend for password users if the user/service account used to
generate the request OAuth access token has the
`firebaseauth.configs.getHashConfig` permission. Otherwise the `passwordHash`
and `passwordSalt` will not be set.

Due to the sensitive nature of password hashes, the Firebase Admin SDK service
account does not have the `firebaseauth.configs.getHashConfig` permission by
default. You can't add a permission directly to a user/service account, but you
can do so indirectly by
[creating a custom IAM role](https://cloud.google.com/iam/docs/creating-custom-roles).

To create the custom IAM role:

1. Go to the **Roles** page in **IAM \& admin** panel in the Google Cloud console.
2. Select your project from the drop-down at the top of the page.
3. Click **CREATE ROLE**
4. Click **ADD PERMISSIONS**
5. Search for `firebaseauth.configs.getHashConfig` permission and select that checkbox.
6. Click **ADD**
7. Click **CREATE** to finish creating the new role.

Add the created custom role to the user/service account in the IAM page:

1. In the **IAM \& admin** panel, select **IAM**
2. Select the service or user account from the list of members for editing.
3. Click **ADD ANOTHER ROLE**.
4. Search for the new custom role previously created.
5. Click **SAVE**.

> [!WARNING]
> **Warning:** Do not use the `Editor` role as a means of adding the `firebaseauth.configs.getHashConfig` permission. This powerful role gives permissions beyond the intended scope.