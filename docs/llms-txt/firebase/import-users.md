# Source: https://firebase.google.com/docs/auth/admin/import-users.md.txt

<br />

The Firebase Admin SDK provides the[`Auth.importUsers()`](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth#baseauthimportusers)API for importing users in bulk toFirebase Authenticationwith elevated privileges. While this feature is also available in the[Firebase CLI](https://firebase.google.com/docs/cli/auth#authimport), the Admin SDK lets you upload existing users from an external authentication system or other Firebase project programmatically without having to create intermediate CSV or JSON files.

The user import API offers the following advantages:

- Ability to migrate users from an external authentication system using a different password hashing algorithm.
- Ability to migrate users from another Firebase project.
- Optimization for speedy and efficient bulk import operations. This operation processes users without checking for`uid`,`email`,`phoneNumber`or other identifier duplication.
- Ability to migrate existing or create new OAuth users (Google, Facebook, etc).
- Ability to import users with custom claims directly in bulk.

## Usage

Up to 1000 users can be imported in a single API call. Note that this operation is optimized for speed and does not check for`uid`,`email`,`phoneNumber`and other unique identifier duplication. Importing a user that collides with an existing`uid`will replace the existing user. Importing a user with any other field duplicated (e.g.`email`) will result in an additional user with the same value. Consequently, when you use this API, you must ensure that you do not duplicate any unique fields.  

### Node.js

    // Up to 1000 users can be imported at once.
    const userImportRecords = [
      {
        uid: 'uid1',
        email: 'user1@example.com',
        passwordHash: Buffer.from('passwordHash1'),
        passwordSalt: Buffer.from('salt1'),
      },
      {
        uid: 'uid2',
        email: 'user2@example.com',
        passwordHash: Buffer.from('passwordHash2'),
        passwordSalt: Buffer.from('salt2'),
      },
      //...
    ];

### Java

    // Up to 1000 users can be imported at once.
    List<ImportUserRecord> users = new ArrayList<>();
    users.add(ImportUserRecord.builder()
        .setUid("uid1")
        .setEmail("user1@example.com")
        .setPasswordHash("passwordHash1".getBytes())
        .setPasswordSalt("salt1".getBytes())
        .build());
    users.add(ImportUserRecord.builder()
        .setUid("uid2")
        .setEmail("user2@example.com")
        .setPasswordHash("passwordHash2".getBytes())
        .setPasswordSalt("salt2".getBytes())
        .build());

### Python

    # Up to 1000 users can be imported at once.
    users = [
        auth.ImportUserRecord(
            uid='uid1',
            email='user1@example.com',
            password_hash=b'password_hash_1',
            password_salt=b'salt1'
        ),
        auth.ImportUserRecord(
            uid='uid2',
            email='user2@example.com',
            password_hash=b'password_hash_2',
            password_salt=b'salt2'
        ),
    ]

### Go

    // Up to 1000 users can be imported at once.
    var users []*auth.UserToImport
    users = append(users, (&auth.UserToImport{}).
    	UID("uid1").
    	Email("user1@example.com").
    	PasswordHash([]byte("passwordHash1")).
    	PasswordSalt([]byte("salt1")))
    users = append(users, (&auth.UserToImport{}).
    	UID("uid2").
    	Email("user2@example.com").
    	PasswordHash([]byte("passwordHash2")).
    	PasswordSalt([]byte("salt2")))

### C#

    //  Up to 1000 users can be imported at once.
    var users = new List<ImportUserRecordArgs>()
    {
        new ImportUserRecordArgs()
        {
            Uid = "uid1",
            Email = "user1@example.com",
            PasswordHash = Encoding.ASCII.GetBytes("passwordHash1"),
            PasswordSalt = Encoding.ASCII.GetBytes("salt1"),
        },
        new ImportUserRecordArgs()
        {
            Uid = "uid2",
            Email = "user2@example.com",
            PasswordHash = Encoding.ASCII.GetBytes("passwordHash2"),
            PasswordSalt = Encoding.ASCII.GetBytes("salt2"),
        },
    };

In this example, the hashing options are specified to help Firebase securely authenticate these users the next time they try to sign in withFirebase Authentication. On successful sign-in, Firebase re-hashes the user's password with the internal Firebase hashing algorithm. Learn more about the required fields per algorithm below.

Firebase Authenticationattempts to upload the entire list of provided users even when a user-specific error occurs. The operation returns a result with the summary of successful and failed imports. Error details are returned per failed user import.  

### Node.js

    getAuth()
      .importUsers(userImportRecords, {
        hash: {
          algorithm: 'HMAC_SHA256',
          key: Buffer.from('secretKey'),
        },
      })
      .then((userImportResult) => {
        // The number of successful imports is determined via: userImportResult.successCount.
        // The number of failed imports is determined via: userImportResult.failureCount.
        // To get the error details.
        userImportResult.errors.forEach((indexedError) => {
          // The corresponding user that failed to upload.
          console.log(
            'Error ' + indexedError.index,
            ' failed to import: ',
            indexedError.error
          );
        });
      })
      .catch((error) => {
        // Some unrecoverable error occurred that prevented the operation from running.
      });

### Java

    UserImportOptions options = UserImportOptions.withHash(
        HmacSha256.builder()
            .setKey("secretKey".getBytes())
            .build());
    try {
      UserImportResult result = FirebaseAuth.getInstance().importUsers(users, options);
      System.out.println("Successfully imported " + result.getSuccessCount() + " users");
      System.out.println("Failed to import " + result.getFailureCount() + " users");
      for (ErrorInfo indexedError : result.getErrors()) {
        System.out.println("Failed to import user at index: " + indexedError.getIndex()
            + " due to error: " + indexedError.getReason());
      }
    } catch (FirebaseAuthException e) {
      // Some unrecoverable error occurred that prevented the operation from running.
    }

### Python

    hash_alg = auth.UserImportHash.hmac_sha256(key=b'secret_key')
    try:
        result = auth.import_users(users, hash_alg=hash_alg)
        print(
            f'Successfully imported {result.success_count} users. Failed to import '
            f'{result.failure_count} users.')
        for err in result.errors:
            print(f'Failed to import {users[err.index].uid} due to {err.reason}')
    except exceptions.FirebaseError:
        # Some unrecoverable error occurred that prevented the operation from running.
        pass

### Go

    client, err := app.Auth(ctx)
    if err != nil {
    	log.Fatalln("Error initializing Auth client", err)
    }

    h := hash.HMACSHA256{
    	Key: []byte("secretKey"),
    }
    result, err := client.ImportUsers(ctx, users, auth.WithHash(h))
    if err != nil {
    	log.Fatalln("Unrecoverable error prevented the operation from running", err)
    }

    log.Printf("Successfully imported %d users\n", result.SuccessCount)
    log.Printf("Failed to import %d users\n", result.FailureCount)
    for _, e := range result.Errors {
    	log.Printf("Failed to import user at index: %d due to error: %s\n", e.Index, e.Reason)
    }

### C#

    var options = new UserImportOptions()
    {
        Hash = new HmacSha256()
        {
            Key = Encoding.ASCII.GetBytes("secretKey"),
        },
    };

    try
    {
        UserImportResult result = await FirebaseAuth.DefaultInstance.ImportUsersAsync(users, options);
        Console.WriteLine($"Successfully imported {result.SuccessCount} users");
        Console.WriteLine($"Failed to import {result.FailureCount} users");
        foreach (ErrorInfo indexedError in result.Errors)
        {
            Console.WriteLine($"Failed to import user at index: {indexedError.Index}"
                + $" due to error: {indexedError.Reason}");
        }
    }
    catch (FirebaseAuthException)
    {
        // Some unrecoverable error occurred that prevented the operation from running.
    }

If no password hashing is needed (phone number, custom token user, OAuth user etc.), do not provide hashing options.

## Import users with Firebase scrypt hashed passwords

By default, Firebase uses a[modified Firebase version of the scrypt hashing algorithm](https://github.com/firebase/scrypt)to store passwords. Importing passwords hashed with modified scrypt is useful for migrating users from another existing Firebase project. In order to do so, the internal parameters need to be determined for the original project.

Firebase generates unique password hash parameters for each Firebase project. To access these parameters, navigate to the[**Users**tab](https://console.firebase.google.com/project/_/authentication/users)in theFirebaseconsole and select**Password Hash Parameters**from the drop down in the upper-right hand corner of the table list of users.

Parameters needed to construct the hash options for this algorithm include:

- `key`: the signer key normally provided in base64 encoding.
- `saltSeparator`: the salt separator normally provided in base64 encoding(optional).
- `rounds`: the number of rounds used to hash the passwords.
- `memoryCost`: the memory cost required for this algorithm.

### Node.js

    getAuth()
      .importUsers(
        [
          {
            uid: 'some-uid',
            email: 'user@example.com',
            // Must be provided in a byte buffer.
            passwordHash: Buffer.from('base64-password-hash', 'base64'),
            // Must be provided in a byte buffer.
            passwordSalt: Buffer.from('base64-salt', 'base64'),
          },
        ],
        {
          hash: {
            algorithm: 'SCRYPT',
            // All the parameters below can be obtained from the Firebase Console's users section.
            // Must be provided in a byte buffer.
            key: Buffer.from('base64-secret', 'base64'),
            saltSeparator: Buffer.from('base64SaltSeparator', 'base64'),
            rounds: 8,
            memoryCost: 14,
          },
        }
      )
      .then((results) => {
        results.errors.forEach((indexedError) => {
          console.log(`Error importing user ${indexedError.index}`);
        });
      })
      .catch((error) => {
        console.log('Error importing users :', error);
      });

### Java

    try {
      List<ImportUserRecord> users = Collections.singletonList(ImportUserRecord.builder()
          .setUid("some-uid")
          .setEmail("user@example.com")
          .setPasswordHash(BaseEncoding.base64().decode("password-hash"))
          .setPasswordSalt(BaseEncoding.base64().decode("salt"))
          .build());
      UserImportOptions options = UserImportOptions.withHash(
          Scrypt.builder()
              // All the parameters below can be obtained from the Firebase Console's "Users"
              // section. Base64 encoded parameters must be decoded into raw bytes.
              .setKey(BaseEncoding.base64().decode("base64-secret"))
              .setSaltSeparator(BaseEncoding.base64().decode("base64-salt-separator"))
              .setRounds(8)
              .setMemoryCost(14)
              .build());
      UserImportResult result = FirebaseAuth.getInstance().importUsers(users, options);
      for (ErrorInfo indexedError : result.getErrors()) {
        System.out.println("Failed to import user: " + indexedError.getReason());
      }
    } catch (FirebaseAuthException e) {
      System.out.println("Error importing users: " + e.getMessage());
    }

### Python

    users = [
        auth.ImportUserRecord(
            uid='some-uid',
            email='user@example.com',
            password_hash=base64.urlsafe_b64decode('password_hash'),
            password_salt=base64.urlsafe_b64decode('salt')
        ),
    ]

    # All the parameters below can be obtained from the Firebase Console's "Users"
    # section. Base64 encoded parameters must be decoded into raw bytes.
    hash_alg = auth.UserImportHash.scrypt(
        key=base64.b64decode('base64_secret'),
        salt_separator=base64.b64decode('base64_salt_separator'),
        rounds=8,
        memory_cost=14
    )
    try:
        result = auth.import_users(users, hash_alg=hash_alg)
        for err in result.errors:
            print('Failed to import user:', err.reason)
    except exceptions.FirebaseError as error:
        print('Error importing users:', error)

### Go

    b64URLdecode := func(s string) []byte {
    	b, err := base64.URLEncoding.DecodeString(s)
    	if err != nil {
    		log.Fatalln("Failed to decode string", err)
    	}

    	return b
    }
    b64Stddecode := func(s string) []byte {
    	b, err := base64.StdEncoding.DecodeString(s)
    	if err != nil {
    		log.Fatalln("Failed to decode string", err)
    	}
    	return b
    }
    // Users retrieved from Firebase Auth's backend need to be base64URL decoded
    users := []*auth.UserToImport{
    	(&auth.UserToImport{}).
    		UID("some-uid").
    		Email("user@example.com").
    		PasswordHash(b64URLdecode("password-hash")).
    		PasswordSalt(b64URLdecode("salt")),
    }

    // All the parameters below can be obtained from the Firebase Console's "Users"
    // section. Base64 encoded parameters must be decoded into raw bytes.
    h := hash.Scrypt{
    	Key:           b64Stddecode("base64-secret"),
    	SaltSeparator: b64Stddecode("base64-salt-separator"),
    	Rounds:        8,
    	MemoryCost:    14,
    }
    result, err := client.ImportUsers(ctx, users, auth.WithHash(h))
    if err != nil {
    	log.Fatalln("Error importing users", err)
    }
    for _, e := range result.Errors {
    	log.Println("Failed to import user", e.Reason)
    }

### C#

    try
    {
        var users = new List<ImportUserRecordArgs>()
        {
            new ImportUserRecordArgs()
            {
                Uid = "some-uid",
                Email = "user@example.com",
                PasswordHash = Encoding.ASCII.GetBytes("password-hash"),
                PasswordSalt = Encoding.ASCII.GetBytes("salt"),
            },
        };

        var options = new UserImportOptions()
        {
            // All the parameters below can be obtained from the Firebase Console's "Users"
            // section. Base64 encoded parameters must be decoded into raw bytes.
            Hash = new Scrypt()
            {
                Key = Encoding.ASCII.GetBytes("base64-secret"),
                SaltSeparator = Encoding.ASCII.GetBytes("base64-salt-separator"),
                Rounds = 8,
                MemoryCost = 14,
            },
        };

        UserImportResult result = await FirebaseAuth.DefaultInstance.ImportUsersAsync(users, options);
        foreach (ErrorInfo indexedError in result.Errors)
        {
            Console.WriteLine($"Failed to import user: {indexedError.Reason}");
        }
    }
    catch (FirebaseAuthException e)
    {
        Console.WriteLine($"Error importing users: {e.Message}");
    }

## Import users with standard scrypt hashed passwords

Firebase Authenticationsupports the standard scrypt algorithm as well as the modified version (above). For the standard scrypt algorithm, the following hashing parameters are required:

- `memoryCost`: the CPU/memory cost of the hashing algorithm.
- `parallelization`: the parallelization of the hashing algorithm.
- `blockSize`: the block size (normally 8) of the hashing algorithm.
- `derivedKeyLength`: The derived key length of the hashing algorithm

### Node.js

    getAuth()
      .importUsers(
        [
          {
            uid: 'some-uid',
            email: 'user@example.com',
            // Must be provided in a byte buffer.
            passwordHash: Buffer.from('password-hash'),
            // Must be provided in a byte buffer.
            passwordSalt: Buffer.from('salt'),
          },
        ],
        {
          hash: {
            algorithm: 'STANDARD_SCRYPT',
            memoryCost: 1024,
            parallelization: 16,
            blockSize: 8,
            derivedKeyLength: 64,
          },
        }
      )
      .then((results) => {
        results.errors.forEach((indexedError) => {
          console.log(`Error importing user ${indexedError.index}`);
        });
      })
      .catch((error) => {
        console.log('Error importing users :', error);
      });

### Java

    try {
      List<ImportUserRecord> users = Collections.singletonList(ImportUserRecord.builder()
          .setUid("some-uid")
          .setEmail("user@example.com")
          .setPasswordHash("password-hash".getBytes())
          .setPasswordSalt("salt".getBytes())
          .build());
      UserImportOptions options = UserImportOptions.withHash(
          StandardScrypt.builder()
              .setMemoryCost(1024)
              .setParallelization(16)
              .setBlockSize(8)
              .setDerivedKeyLength(64)
              .build());
      UserImportResult result = FirebaseAuth.getInstance().importUsers(users, options);
      for (ErrorInfo indexedError : result.getErrors()) {
        System.out.println("Failed to import user: " + indexedError.getReason());
      }
    } catch (FirebaseAuthException e) {
      System.out.println("Error importing users: " + e.getMessage());
    }

### Python

    users = [
        auth.ImportUserRecord(
            uid='some-uid',
            email='user@example.com',
            password_hash=b'password_hash',
            password_salt=b'salt'
        ),
    ]

    hash_alg = auth.UserImportHash.standard_scrypt(
        memory_cost=1024, parallelization=16, block_size=8, derived_key_length=64)
    try:
        result = auth.import_users(users, hash_alg=hash_alg)
        for err in result.errors:
            print('Failed to import user:', err.reason)
    except exceptions.FirebaseError as error:
        print('Error importing users:', error)

### Go

    users := []*auth.UserToImport{
    	(&auth.UserToImport{}).
    		UID("some-uid").
    		Email("user@example.com").
    		PasswordHash([]byte("password-hash")).
    		PasswordSalt([]byte("salt")),
    }
    h := hash.StandardScrypt{
    	MemoryCost:       1024,
    	Parallelization:  16,
    	BlockSize:        8,
    	DerivedKeyLength: 64,
    }
    result, err := client.ImportUsers(ctx, users, auth.WithHash(h))
    if err != nil {
    	log.Fatalln("Error importing users", err)
    }
    for _, e := range result.Errors {
    	log.Println("Failed to import user", e.Reason)
    }

### C#

    try
    {
        var users = new List<ImportUserRecordArgs>()
        {
            new ImportUserRecordArgs()
            {
                Uid = "some-uid",
                Email = "user@example.com",
                PasswordHash = Encoding.ASCII.GetBytes("password-hash"),
                PasswordSalt = Encoding.ASCII.GetBytes("salt"),
            },
        };

        var options = new UserImportOptions()
        {
            Hash = new StandardScrypt()
            {
                MemoryCost = 1024,
                Parallelization = 16,
                BlockSize = 8,
                DerivedKeyLength = 64,
            },
        };

        UserImportResult result = await FirebaseAuth.DefaultInstance.ImportUsersAsync(users, options);
        foreach (ErrorInfo indexedError in result.Errors)
        {
            Console.WriteLine($"Failed to import user: {indexedError.Reason}");
        }
    }
    catch (FirebaseAuthException e)
    {
        Console.WriteLine($"Error importing users: {e.Message}");
    }

## Import users with HMAC hashed passwords

HMAC hashing algorithms include:`HMAC_MD5`,`HMAC_SHA1`,`HMAC_SHA256`and`HMAC_SHA512`. For these hashing algorithms, you must provide the hash signer key.  

### Node.js

    getAuth()
      .importUsers(
        [
          {
            uid: 'some-uid',
            email: 'user@example.com',
            // Must be provided in a byte buffer.
            passwordHash: Buffer.from('password-hash'),
            // Must be provided in a byte buffer.
            passwordSalt: Buffer.from('salt'),
          },
        ],
        {
          hash: {
            algorithm: 'HMAC_SHA256',
            // Must be provided in a byte buffer.
            key: Buffer.from('secret'),
          },
        }
      )
      .then((results) => {
        results.errors.forEach((indexedError) => {
          console.log(`Error importing user ${indexedError.index}`);
        });
      })
      .catch((error) => {
        console.log('Error importing users :', error);
      });

### Java

    try {
      List<ImportUserRecord> users = Collections.singletonList(ImportUserRecord.builder()
          .setUid("some-uid")
          .setEmail("user@example.com")
          .setPasswordHash("password-hash".getBytes())
          .setPasswordSalt("salt".getBytes())
          .build());
      UserImportOptions options = UserImportOptions.withHash(
          HmacSha256.builder()
              .setKey("secret".getBytes())
              .build());
      UserImportResult result = FirebaseAuth.getInstance().importUsers(users, options);
      for (ErrorInfo indexedError : result.getErrors()) {
        System.out.println("Failed to import user: " + indexedError.getReason());
      }
    } catch (FirebaseAuthException e) {
      System.out.println("Error importing users: " + e.getMessage());
    }

### Python

    users = [
        auth.ImportUserRecord(
            uid='some-uid',
            email='user@example.com',
            password_hash=b'password_hash',
            password_salt=b'salt'
        ),
    ]

    hash_alg = auth.UserImportHash.hmac_sha256(key=b'secret')
    try:
        result = auth.import_users(users, hash_alg=hash_alg)
        for err in result.errors:
            print('Failed to import user:', err.reason)
    except exceptions.FirebaseError as error:
        print('Error importing users:', error)

### Go

    users := []*auth.UserToImport{
    	(&auth.UserToImport{}).
    		UID("some-uid").
    		Email("user@example.com").
    		PasswordHash([]byte("password-hash")).
    		PasswordSalt([]byte("salt")),
    }
    h := hash.HMACSHA256{
    	Key: []byte("secret"),
    }
    result, err := client.ImportUsers(ctx, users, auth.WithHash(h))
    if err != nil {
    	log.Fatalln("Error importing users", err)
    }
    for _, e := range result.Errors {
    	log.Println("Failed to import user", e.Reason)
    }

### C#

    try
    {
        var users = new List<ImportUserRecordArgs>()
        {
            new ImportUserRecordArgs()
            {
                Uid = "some-uid",
                Email = "user@example.com",
                PasswordHash = Encoding.ASCII.GetBytes("password-hash"),
                PasswordSalt = Encoding.ASCII.GetBytes("salt"),
            },
        };

        var options = new UserImportOptions()
        {
            Hash = new HmacSha256()
            {
                Key = Encoding.ASCII.GetBytes("secret"),
            },
        };

        UserImportResult result = await FirebaseAuth.DefaultInstance.ImportUsersAsync(users, options);
        foreach (ErrorInfo indexedError in result.Errors)
        {
            Console.WriteLine($"Failed to import user: {indexedError.Reason}");
        }
    }
    catch (FirebaseAuthException e)
    {
        Console.WriteLine($"Error importing users: {e.Message}");
    }

## Import users with MD5, SHA and PBKDF hashed passwords

MD5, SHA and PBKDF hashing algorithms include:`MD5`,`SHA1`,`SHA256`,`SHA512`,`PBKDF_SHA1`and`PBKDF2_SHA256`. For these hashing algorithms, you must provide the number of rounds (between 0 and 8192 for`MD5`, between 1 and 8192 for`SHA1`,`SHA256`and`SHA512`, and between 0 and 120000 for`PBKDF_SHA1`and`PBKDF2_SHA256`) used originally to hash the password. If a single hashing function was originally applied, rounds must be set to 1.  

### Node.js

    getAuth()
      .importUsers(
        [
          {
            uid: 'some-uid',
            email: 'user@example.com',
            // Must be provided in a byte buffer.
            passwordHash: Buffer.from('password-hash'),
            // Must be provided in a byte buffer.
            passwordSalt: Buffer.from('salt'),
          },
        ],
        {
          hash: {
            algorithm: 'PBKDF2_SHA256',
            rounds: 100000,
          },
        }
      )
      .then((results) => {
        results.errors.forEach((indexedError) => {
          console.log(`Error importing user ${indexedError.index}`);
        });
      })
      .catch((error) => {
        console.log('Error importing users :', error);
      });

### Java

    try {
      List<ImportUserRecord> users = Collections.singletonList(ImportUserRecord.builder()
          .setUid("some-uid")
          .setEmail("user@example.com")
          .setPasswordHash("password-hash".getBytes())
          .setPasswordSalt("salt".getBytes())
          .build());
      UserImportOptions options = UserImportOptions.withHash(
          Pbkdf2Sha256.builder()
              .setRounds(100000)
              .build());
      UserImportResult result = FirebaseAuth.getInstance().importUsers(users, options);
      for (ErrorInfo indexedError : result.getErrors()) {
        System.out.println("Failed to import user: " + indexedError.getReason());
      }
    } catch (FirebaseAuthException e) {
      System.out.println("Error importing users: " + e.getMessage());
    }

### Python

    users = [
        auth.ImportUserRecord(
            uid='some-uid',
            email='user@example.com',
            password_hash=b'password_hash',
            password_salt=b'salt'
        ),
    ]

    hash_alg = auth.UserImportHash.pbkdf2_sha256(rounds=100000)
    try:
        result = auth.import_users(users, hash_alg=hash_alg)
        for err in result.errors:
            print('Failed to import user:', err.reason)
    except exceptions.FirebaseError as error:
        print('Error importing users:', error)

### Go

    users := []*auth.UserToImport{
    	(&auth.UserToImport{}).
    		UID("some-uid").
    		Email("user@example.com").
    		PasswordHash([]byte("password-hash")).
    		PasswordSalt([]byte("salt")),
    }
    h := hash.PBKDF2SHA256{
    	Rounds: 100000,
    }
    result, err := client.ImportUsers(ctx, users, auth.WithHash(h))
    if err != nil {
    	log.Fatalln("Error importing users", err)
    }
    for _, e := range result.Errors {
    	log.Println("Failed to import user", e.Reason)
    }

### C#

    try
    {
        var users = new List<ImportUserRecordArgs>()
        {
            new ImportUserRecordArgs()
            {
                Uid = "some-uid",
                Email = "user@example.com",
                PasswordHash = Encoding.ASCII.GetBytes("password-hash"),
                PasswordSalt = Encoding.ASCII.GetBytes("salt"),
            },
        };

        var options = new UserImportOptions()
        {
            Hash = new Pbkdf2Sha256()
            {
                Rounds = 100000,
            },
        };

        UserImportResult result = await FirebaseAuth.DefaultInstance.ImportUsersAsync(users, options);
        foreach (ErrorInfo indexedError in result.Errors)
        {
            Console.WriteLine($"Failed to import user: {indexedError.Reason}");
        }
    }
    catch (FirebaseAuthException e)
    {
        Console.WriteLine($"Error importing users: {e.Message}");
    }

## Import users with BCRYPT hashed passwords

For BCRYPT hashed passwords, neither additional hash parameters, nor password salts per user are required.  

### Node.js

    getAuth()
      .importUsers(
        [
          {
            uid: 'some-uid',
            email: 'user@example.com',
            // Must be provided in a byte buffer.
            passwordHash: Buffer.from('password-hash'),
          },
        ],
        {
          hash: {
            algorithm: 'BCRYPT',
          },
        }
      )
      .then((results) => {
        results.errors.forEach((indexedError) => {
          console.log(`Error importing user ${indexedError.index}`);
        });
      })
      .catch((error) => {
        console.log('Error importing users :', error);
      });

### Java

    try {
      List<ImportUserRecord> users = Collections.singletonList(ImportUserRecord.builder()
          .setUid("some-uid")
          .setEmail("user@example.com")
          .setPasswordHash("password-hash".getBytes())
          .setPasswordSalt("salt".getBytes())
          .build());
      UserImportOptions options = UserImportOptions.withHash(Bcrypt.getInstance());
      UserImportResult result = FirebaseAuth.getInstance().importUsers(users, options);
      for (ErrorInfo indexedError : result.getErrors()) {
        System.out.println("Failed to import user: " + indexedError.getReason());
      }
    } catch (FirebaseAuthException e) {
      System.out.println("Error importing users: " + e.getMessage());
    }

### Python

    users = [
        auth.ImportUserRecord(
            uid='some-uid',
            email='user@example.com',
            password_hash=b'password_hash',
            password_salt=b'salt'
        ),
    ]

    hash_alg = auth.UserImportHash.bcrypt()
    try:
        result = auth.import_users(users, hash_alg=hash_alg)
        for err in result.errors:
            print('Failed to import user:', err.reason)
    except exceptions.FirebaseError as error:
        print('Error importing users:', error)

### Go

    users := []*auth.UserToImport{
    	(&auth.UserToImport{}).
    		UID("some-uid").
    		Email("user@example.com").
    		PasswordHash([]byte("password-hash")).
    		PasswordSalt([]byte("salt")),
    }
    h := hash.Bcrypt{}
    result, err := client.ImportUsers(ctx, users, auth.WithHash(h))
    if err != nil {
    	log.Fatalln("Error importing users", err)
    }
    for _, e := range result.Errors {
    	log.Println("Failed to import user", e.Reason)
    }

### C#

    try
    {
        var users = new List<ImportUserRecordArgs>()
        {
            new ImportUserRecordArgs()
            {
                Uid = "some-uid",
                Email = "user@example.com",
                PasswordHash = Encoding.ASCII.GetBytes("password-hash"),
                PasswordSalt = Encoding.ASCII.GetBytes("salt"),
            },
        };

        var options = new UserImportOptions()
        {
            Hash = new Bcrypt(),
        };

        UserImportResult result = await FirebaseAuth.DefaultInstance.ImportUsersAsync(users, options);
        foreach (ErrorInfo indexedError in result.Errors)
        {
            Console.WriteLine($"Failed to import user: {indexedError.Reason}");
        }
    }
    catch (FirebaseAuthException e)
    {
        Console.WriteLine($"Error importing users: {e.Message}");
    }

## Import users with Argon2 hashed passwords

You can import user records that have Argon2 hashed passwords by constructing an`Argon2`hash object. Note that this is currently only supported in the Admin Java SDK.

Parameters needed to construct the hash options for this algorithm include:

- `hashLengthBytes`: the desired hash length in bytes, provided as an integer
- `hashType`: the Argon2 variant to be used (`ARGON2_D`,`ARGON2_ID`,`ARGON2_I`)
- `parallelism`: the degree of parallelism, provided as an integer. Must be between 1 and 16 (inclusive)
- `iterations`: the number of iterations to perform, provided as an integer. Must be between 1 and 16 (inclusive)
- `memoryCostKib`: the memory cost required for this algorithm in kibibytes, must be less than 32768.
- `version`: the version of the Argon2 algorithm (`VERSION_10`or`VERSION_13`). Optional, defaults to VERSION_13 if not specified.
- `associatedData`: additional associated data, provided as a byte array, that is appended to the hash value to provide an additional layer of security. Optional, this data is base64 encoded before it is sent to the API.

### Java

    try {
      List<ImportUserRecord> users = Collections.singletonList(ImportUserRecord.builder()
          .setUid("some-uid")
          .setEmail("user@example.com")
          .setPasswordHash("password-hash".getBytes())
          .setPasswordSalt("salt".getBytes())
          .build());
      UserImportOptions options = UserImportOptions.withHash(
          Argon2.builder()
              .setHashLengthBytes(512)
              .setHashType(Argon2HashType.ARGON2_ID)
              .setParallelism(8)
              .setIterations(16)
              .setMemoryCostKib(2048)
              .setVersion(Argon2Version.VERSION_10)
              .setAssociatedData("associated-data".getBytes())
              .build());
      UserImportResult result = FirebaseAuth.getInstance().importUsers(users, options);
      for (ErrorInfo indexedError : result.getErrors()) {
        System.out.println("Failed to import user: " + indexedError.getReason());
      }
    } catch (FirebaseAuthException e) {
      System.out.println("Error importing users: " + e.getMessage());
    }

## Import users without passwords

You can import users without passwords. Users without passwords can be imported in combination with users that have OAuth providers, custom claims and phone numbers, and so on.  

### Node.js

    getAuth()
      .importUsers([
        {
          uid: 'some-uid',
          displayName: 'John Doe',
          email: 'johndoe@gmail.com',
          photoURL: 'http://www.example.com/12345678/photo.png',
          emailVerified: true,
          phoneNumber: '+11234567890',
          // Set this user as admin.
          customClaims: { admin: true },
          // User with Google provider.
          providerData: [
            {
              uid: 'google-uid',
              email: 'johndoe@gmail.com',
              displayName: 'John Doe',
              photoURL: 'http://www.example.com/12345678/photo.png',
              providerId: 'google.com',
            },
          ],
        },
      ])
      .then((results) => {
        results.errors.forEach((indexedError) => {
          console.log(`Error importing user ${indexedError.index}`);
        });
      })
      .catch((error) => {
        console.log('Error importing users :', error);
      });

### Java

    try {
      List<ImportUserRecord> users = Collections.singletonList(ImportUserRecord.builder()
          .setUid("some-uid")
          .setDisplayName("John Doe")
          .setEmail("johndoe@gmail.com")
          .setPhotoUrl("http://www.example.com/12345678/photo.png")
          .setEmailVerified(true)
          .setPhoneNumber("+11234567890")
          .putCustomClaim("admin", true) // set this user as admin
          .addUserProvider(UserProvider.builder() // user with Google provider
              .setUid("google-uid")
              .setEmail("johndoe@gmail.com")
              .setDisplayName("John Doe")
              .setPhotoUrl("http://www.example.com/12345678/photo.png")
              .setProviderId("google.com")
              .build())
          .build());
      UserImportResult result = FirebaseAuth.getInstance().importUsers(users);
      for (ErrorInfo indexedError : result.getErrors()) {
        System.out.println("Failed to import user: " + indexedError.getReason());
      }
    } catch (FirebaseAuthException e) {
      System.out.println("Error importing users: " + e.getMessage());
    }

### Python

    users = [
        auth.ImportUserRecord(
            uid='some-uid',
            display_name='John Doe',
            email='johndoe@gmail.com',
            photo_url='http://www.example.com/12345678/photo.png',
            email_verified=True,
            phone_number='+11234567890',
            custom_claims={'admin': True}, # set this user as admin
            provider_data=[ # user with Google provider
                auth.UserProvider(
                    uid='google-uid',
                    email='johndoe@gmail.com',
                    display_name='John Doe',
                    photo_url='http://www.example.com/12345678/photo.png',
                    provider_id='google.com'
                )
            ],
        ),
    ]
    try:
        result = auth.import_users(users)
        for err in result.errors:
            print('Failed to import user:', err.reason)
    except exceptions.FirebaseError as error:
        print('Error importing users:', error)

### Go

    users := []*auth.UserToImport{
    	(&auth.UserToImport{}).
    		UID("some-uid").
    		DisplayName("John Doe").
    		Email("johndoe@gmail.com").
    		PhotoURL("http://www.example.com/12345678/photo.png").
    		EmailVerified(true).
    		PhoneNumber("+11234567890").
    		CustomClaims(map[string]interface{}{"admin": true}). // set this user as admin
    		ProviderData([]*auth.UserProvider{                   // user with Google provider
    			{
    				UID:         "google-uid",
    				Email:       "johndoe@gmail.com",
    				DisplayName: "John Doe",
    				PhotoURL:    "http://www.example.com/12345678/photo.png",
    				ProviderID:  "google.com",
    			},
    		}),
    }
    result, err := client.ImportUsers(ctx, users)
    if err != nil {
    	log.Fatalln("Error importing users", err)
    }
    for _, e := range result.Errors {
    	log.Println("Failed to import user", e.Reason)
    }

### C#

    try
    {
        var users = new List<ImportUserRecordArgs>()
        {
            new ImportUserRecordArgs()
            {
                Uid = "some-uid",
                DisplayName = "John Doe",
                Email = "johndoe@gmail.com",
                PhotoUrl = "http://www.example.com/12345678/photo.png",
                EmailVerified = true,
                PhoneNumber = "+11234567890",
                CustomClaims = new Dictionary<string, object>()
                {
                    { "admin", true }, // set this user as admin
                },
                UserProviders = new List<UserProvider>
                {
                    new UserProvider() // user with Google provider
                    {
                        Uid = "google-uid",
                        Email = "johndoe@gmail.com",
                        DisplayName = "John Doe",
                        PhotoUrl = "http://www.example.com/12345678/photo.png",
                        ProviderId = "google.com",
                    },
                },
            },
        };

        UserImportResult result = await FirebaseAuth.DefaultInstance.ImportUsersAsync(users);
        foreach (ErrorInfo indexedError in result.Errors)
        {
            Console.WriteLine($"Failed to import user: {indexedError.Reason}");
        }
    }
    catch (FirebaseAuthException e)
    {
        Console.WriteLine($"Error importing users: {e.Message}");
    }

| **Note:** `some-uid`is a placeholder for the unique Firebase User ID, which is the primary identifier for a user within your project. In contrast,`google-uid`is a placeholder for the unique ID from the Google authentication provider. This ID links the user's Firebase account to their specific Google Account.