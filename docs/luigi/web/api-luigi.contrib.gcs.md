# luigi.contrib.gcs

luigi bindings for Google Cloud Storage

Functions

`is_error_5xx`(err)

Classes

`AtomicGCSFile`(path, gcs_client)

A GCS file that writes to a temp file and put to GCS on close.

`GCSClient`([oauth_credentials, descriptor, ...])

An implementation of a FileSystem over Google Cloud Storage.

`GCSFlagTarget`(path[, format, client, flag])

Defines a target directory with a flag-file (defaults to _SUCCESS) used to signify job success.

`GCSTarget`(path[, format, client])

Initializes a FileSystemTarget instance.

Exceptions

`InvalidDeleteException`

luigi.contrib.gcs.is_error_5xx(*err*)

exception luigi.contrib.gcs.InvalidDeleteException

class luigi.contrib.gcs.GCSClient(*oauth_credentials=None*, *descriptor=''*, *http_=None*, *chunksize=10485760*, ***discovery_build_kwargs*)

An implementation of a FileSystem over Google Cloud Storage.

There are several ways to use this class. By default it will use the app
default credentials, as described at https://developers.google.com/identity/protocols/application-default-credentials .
Alternatively, you may pass an google-auth credentials object. e.g. to use a service account:

```
 credentials = google.auth.jwt.Credentials.from_service_account_info(
     '012345678912-ThisIsARandomServiceAccountEmail@developer.gserviceaccount.com',
     'These are the contents of the p12 file that came with the service account',
     scope='https://www.googleapis.com/auth/devstorage.read_write')
 client = GCSClient(oauth_credentials=credentails)

The chunksize parameter specifies how much data to transfer when downloading
or uploading files.

```