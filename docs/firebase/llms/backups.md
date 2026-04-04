# Source: https://firebase.google.com/docs/firestore/enterprise/backups.md.txt

# Source: https://firebase.google.com/docs/firestore/backups.md.txt

# Source: https://firebase.google.com/docs/database/backups.md.txt

<br />

[Blaze](https://firebase.google.com/pricing)plan users can set up theirFirebase Realtime Databasefor automatic backups, a self-service feature that enables daily backups of your Database application data and[rules](https://firebase.google.com/database/security)in JSON format to a[Cloud Storage](https://cloud.google.com/storage/docs/)bucket.

## Setup

To get started, visit the[Backups tab](https://console.firebase.google.com/project/_/database/backups)in the Database section of theFirebaseconsole, and the wizard will guide you through setting up your automated backups.

To save on storage costs, we enable[Gzip](https://firebase.google.com/docs/database/backups#gzip_compression)compression by default, and you can choose to enable a[30-day lifecycle policy](https://firebase.google.com/docs/database/backups#storage_lifecycle)on your bucket to have backups older than 30 days automatically deleted.

You can view the status and backup activity directly in theFirebaseconsole where you can also start a manual backup. This can be useful for taking specific timed snapshots or as a safety action before you perform any code changes.

Once set up, a newCloud Storagebucket will be created for you with the[WRITER permission](https://cloud.google.com/storage/docs/access-control/lists#permissions)for Firebase. You should not store data in this bucket you are not comfortable with Firebase having access to. Firebase will have no additional access to your otherCloud Storagebuckets or any other areas ofGoogle Cloud.

## Restoring from backups

To restore your Firebase from a backup, first download the file fromCloud Storageto your local disk. This can be done by clicking the filename within the backup activity section or from theCloud Storagebucket interface. If the file is Gzip compressed, first[decompress](https://firebase.google.com/docs/database/backups#gzip_compression)the file.

There are two ways you can import your data:

Method 1: Click the Import JSON button in your[Database's Data section](https://console.firebase.google.com/project/_/database/data)and select your application data JSON file.

Method 2: You can also issue a CURL request from your command line.

First retrieve a secret from your Firebase, which you can get by visiting the[Database settings page](https://console.firebase.google.com/project/_/settings/database).

Then enter the following into your terminal, replacing the`DATABASE_NAME`and`SECRET`fields with your own values:  

    curl 'https://<DATABASE_NAME>.firebaseio.com/.json?auth=<SECRET>&print=silent' -X PUT -d @<DATABASE_NAME>.json

If you are having trouble restoring a backup from a very large database, please reach out to our[support team](https://firebase.google.com/support/contact/troubleshooting).

## Scheduling

Your Database backup is assigned to a specific hour each day that ensures even load and highest availability for all backup customers. This scheduled backup will occur regardless of if you do any manual backups throughout the day.

## File naming

Files transferred to yourCloud Storagebucket will be timestamped (ISO 8601 standard) and use the following naming conventions:

- Database data:`YYYY-MM-DDTHH:MM:SSZ_<DATABASE_NAME>_data.json`
- Database rules:`YYYY-MM-DDTHH:MM:SSZ_<DATABASE_NAME>_rules.json`

If[Gzip](https://firebase.google.com/docs/database/backups#gzip_compression)is enabled, a`.gz`suffix will be appended to the filenames. You can easily find the backups from a specific date or time usingCloud Storageprefix searching.

## Gzip compression

By default, we compress your backup files using Gzip compression to save on storage costs and decrease transfer times. The compressed filesize varies depending on the data characteristics of your Database, but typical Databases may shrink to â their original size, saving you on storage costs and decreasing the upload time for your backups.

To decompress your Gzipped JSON files, issue a command line command using the`gunzip`binary which is shipped by default for OS-X and most Linux distributions.  

    gunzip <DATABASE_NAME>.json.gz  # Will unzip to <DATABASE_NAME>.json

## Storage 30 day lifecycle

We offer an easy to use configuration switch that enables a default 30 day object lifecycle policy for yourCloud Storagebucket. When enabled, files in your bucket will be automatically deleted after 30 days. This helps to reduce unwanted old backups, saving you on storage costs, and keeping your bucket directory clean. If you place other files into your Automated Backups bucket, they will also be deleted with the same policy.

## Costs

The backups feature can be enabled for projects on the[Blaze](https://firebase.google.com/pricing)plan for no additional cost. However, you will be charged at the[standard rates](https://cloud.google.com/storage/pricing)for the backup files placed in yourCloud Storagebucket. You can enable[Gzip Compression](https://firebase.google.com/docs/database/backups#gzip_compression)and[Storage 30 day Lifecycle](https://firebase.google.com/docs/database/backups#storage_lifecycle)to reduce your storage costs.