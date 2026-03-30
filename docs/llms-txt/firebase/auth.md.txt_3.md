# Source: https://firebase.google.com/docs/cli/auth.md.txt

- The [`auth:import`](https://firebase.google.com/docs/cli/auth#auth-import) command imports user accounts into Firebase
  projects.

- The [`auth:export`](https://firebase.google.com/docs/cli/auth#auth-export) command exports user accounts to JSON and
  CSV files.

## Password hash parameters

To determine the password hash parameters used for your project navigate to
the **Authentication** \> **Users** section of the Firebase console and click
the three dots icon above the list of users. You will see a dialog with a list
of password hash parameters you can use with the `auth:import` and `auth:export`
commands:

    hash_config {
      algorithm: SCRYPT,
      base64_signer_key: <...sensitive...>,
      base64_salt_separator: <...sensitive...>,
      rounds: 8,
      mem_cost: 14,
    }

These values are sensitive, so store them with care. Most Firebase projects use
`SCRYPT`, a [modified version of the scrypt hashing algorithm](https://github.com/firebase/scrypt),
which is the default for new projects.

## auth:import

```
firebase auth:import ACCOUNT_FILE    \
    --hash-algo=HASH_ALGORITHM         \
    --hash-key=KEY                     \
    --salt-separator=SALT_SEPARATOR    \
    --rounds=ROUNDS                    \
    --mem-cost=MEM_COST                \
    --parallelization=PARALLELIZATION  \
    --block-size=BLOCK_SIZE            \
    --dk-len=DK_LEN                    \
    --hash-input-order=HASH_INPUT_ORDER
```

| Parameters ||
|---|---|
| account_file | The CSV or JSON file that contains the user accounts to import. See [File format](https://firebase.google.com/docs/cli/auth#file_format). |
| hash-algo | The algorithm used to hash passwords in the user account file. Required to import accounts with password fields. One of the following values: `BCRYPT`, `SCRYPT`, `STANDARD_SCRYPT`, `HMAC_SHA512`, `HMAC_SHA256`, `HMAC_SHA1`, `HMAC_MD5`, `MD5`, `SHA512`, `SHA256`, `SHA1`, `PBKDF_SHA1`, `PBKDF2_SHA256`. |
| hash-key | Key used to hash passwords. Required for the `SCRYPT`, `HMAC_SHA512`, `HMAC_SHA256`, `HMAC_SHA1`, and `HMAC_MD5` algorithms. This argument must be formatted as a **base64-encoded** string. |
| salt-separator | Salt separator which will be appended to salt when verifying password. Optional for all algorithms. This argument must be formatted as a **base64-encoded** string. |
| rounds | The number of rounds used to hash passwords. Required for the `SCRYPT`, `MD5`, `SHA512`, `SHA256`, `SHA1`, `PBKDF_SHA1` and `PBKDF2_SHA256` algorithms. |
| mem-cost | This parameter represents either the memory cost required for the `SCRYPT` algorithm OR the CPU/memory cost required for the `STANDARD_SCRYPT` algorithm. |
| parallelization | The parallelization of the hashing algorithm. Required for the `STANDARD_SCRYPT` algorithm. |
| block-size | The block size (normally is 8) of the hashing algorithm. Required for the `STANDARD_SCRYPT` algorithm. |
| dk-len | The derived key length of the hashing algorithm. Required for the `STANDARD_SCRYPT` algorithm. |
| hash-input-order | The order of password and salt. Possible values are `SALT_FIRST` and `PASSWORD_FIRST`. This flag applies to `SHA512`, `SHA256`, `SHA1`, `MD5`, `HMAC_SHA512`, `HMAC_SHA256`, `HMAC_SHA1`, and `HMAC_MD5`. |

> [!NOTE]
> **Note:** `STANDARD_SCRYPT` is the standard [scrypt algorithm](https://en.wikipedia.org/wiki/Scrypt). `SCRYPT` is Firebase Auth internal modified version of scrypt. When you migrate from one Firebase project to another, you still need to specify `SCRYPT` in `auth:import`.

## auth:export

```
firebase auth:export ACCOUNT_FILE --format=FILE_FORMAT
```

> [!NOTE]
> **Note:** the `auth:export` command only exports passwords hashed using the scrypt algorithm, which is used by the Firebase backend. Account records with passwords hashed using other algorithms are exported with empty `passwordHash` and `salt` fields. Projects might have passwords hashed with other algorithms after importing user records from a file, since passwords are only re-hashed with scrypt when an imported user signs in for the first time.

| Parameters ||
|---|---|
| account_file | The CSV or JSON file to export to. See [File format](https://firebase.google.com/docs/cli/auth#file_format). |
| file_format | **Optional.** The file format to export: either CSV or JSON. If the file name specified in the `account_file` parameter ends with `.csv` or `.json`, that format is used and this parameter is ignored. |

## File format

The user account file can be formatted as [CSV](https://firebase.google.com/docs/cli/auth#CSV) or [JSON](https://firebase.google.com/docs/cli/auth#JSON).

### CSV

A CSV user account file has the following format:

| Column number | Field description | Field type | Comments |
|---|---|---|---|
| 1 | UID | String | Required This ID should be unique among all accounts in your Firebase projects. If you import an account with a UID that already exists, then the account will be overwritten. |
| 2 | Email | String | Optional |
| 3 | Email Verified | Boolean | Optional |
| 4 | Password Hash | String | Optional A base64 encoded string. This field requires the caller to have [Editor or Owner role](https://firebase.google.com/docs/projects/iam/roles-basic). |
| 5 | Password Salt | String | Optional A base64 encoded string. This field requires the caller to have [Editor or Owner role](https://firebase.google.com/docs/projects/iam/roles-basic). |
| 6 | Name | String | Optional |
| 7 | Photo URL | String | Optional |
| 8 | Google ID | String | Optional |
| 9 | Google Email | String | Optional |
| 10 | Google Display Name | String | Optional |
| 11 | Google Photo URL | String | Optional |
| 12 | Facebook ID | String | Optional |
| 13 | Facebook Email | String | Optional |
| 14 | Facebook Display Name | String | Optional |
| 15 | Facebook Photo URL | String | Optional |
| 16 | Twitter ID | String | Optional |
| 17 | Twitter Email | String | Optional |
| 18 | Twitter Display Name | String | Optional |
| 19 | Twitter Photo URL | String | Optional |
| 20 | GitHub ID | String | Optional |
| 21 | GitHub Email | String | Optional |
| 22 | GitHub Display Name | String | Optional |
| 23 | GitHub Photo URL | String | Optional |
| 24 | User Creation Time | Long | Optional Epoch Unix Timestamp in milliseconds. |
| 25 | Last Sign-In Time | Long | Optional Epoch Unix Timestamp in milliseconds. |
| 26 | Phone Number | String | Optional |

If you leave an optional value unspecified, ensure that you still include an
empty field for the value. An empty field can be any number of space
characters.

For example, the following line represents a user account:

    111, test@test.org, false, Jlf7onfLbzqPNFP/1pqhx6fQF/w=, c2FsdC0x, Test User, http://photo.com/123, , , , , 123, test@test.org, Test FB User, http://photo.com/456, , , , , , , , , 1486324027000, 1486324027000

### JSON

A JSON user account file has the following format:

```
{
  "users": [
    {
      "localId": UID,
      "email": EMAIL_ADDRESS
      "emailVerified": EMAIL_VERIFIED,
      "passwordHash": BASE64_ENCODED_PASSWORD_HASH,
      "salt": BASE64_ENCODED_PASSWORD_SALT,
      "displayName": NAME,
      "photoUrl": PHOTO_URL,
      "createdAt": CREATED_AT_IN_MILLIS,
      "lastSignedInAt": LAST_SIGNEDIN_AT_IN_MILLIS,
      "phoneNumber": PHONE_NUMBER
      "providerUserInfo": [
        {
          "providerId": PROVIDER_ID,
          "rawId": PROVIDER_UID,
          "email":  PROVIDER_EMAIL,
          "displayName": PROVIDER_NAME,
          "photoUrl": PROVIDER_PHOTO_URL
        },
        ...
      ]
    },
    ...
  ]
}
```

Replace <var translate="no">PROVIDER_ID</var> with one of the following values:

- `google.com`
- `facebook.com`
- `github.com`
- `twitter.com`