# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-logs-from-archive.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible logs_from_archive

This command is used to retrieve container logs from your own [Disaster Log Archive](/core-concepts/observability/logs/s3-log-archives).

> ❗️ You must have enabled log archiving for your Dedicated Stack(s) in order to use this command.

# Synopsis

```
Usage:
  aptible logs_from_archive --bucket NAME --region REGION --stack NAME [ --decryption-keys ONE [OR MORE] ] [ --download-location LOCATION ] [ [ --string-matches ONE [OR MORE] ] | [ --app-id ID | --database-id ID | --endpoint-id ID | --container-id ID ] [ --start-date YYYY-MM-DD --end-date YYYY-MM-DD ] ] --bucket=BUCKET --region=REGION --stack=STACK

Options:
  --region=REGION                          # The AWS region your S3 bucket resides in
  --bucket=BUCKET                          # The name of your S3 bucket
  --stack=STACK                            # The name of the Stack to download logs from
  [--decryption-keys=one two three]        # The Aptible-provided keys for decryption. (Space separated if multiple)
  [--string-matches=one two three]         # The strings to match in log file names.(Space separated if multiple)
  [--app-id=N]                             # The Application ID to download logs for.
  [--database-id=N]                        # The Database ID to download logs for.
  [--endpoint-id=N]                        # The Endpoint ID to download logs for.
  [--container-id=CONTAINER_ID]            # The container ID to download logs for
  [--start-date=START_DATE]                # Get logs starting from this (UTC) date (format: YYYY-MM-DD)
  [--end-date=END_DATE]                    # Get logs before this (UTC) date (format: YYYY-MM-DD)
  [--download-location=DOWNLOAD_LOCATION]  # The local path place downloaded log files. If you do not set this option, the file names will be shown, but not downloaded.

Retrieves container logs from an S3 archive in your own AWS account. You must provide your AWS credentials via the environment variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY
```

> 📘 You can find resource ID's by looking at the URL of a resource on the Aptible Dashboard, or by using the [JSON output format](/reference/aptible-cli/cli-commands/overview#output-format) for the [`aptible db:list`](/reference/aptible-cli/cli-commands/cli-db-list) or [`aptible apps`](/reference/aptible-cli/cli-commands/cli-apps) commands.

> This command also allows retrieval of logs from deleted resources. Please contact [Aptible Support](/how-to-guides/troubleshooting/aptible-support) for assistance identifying the proper resource IDs of deleted resources.

# Examples

## Search for all archived logs for a specific Database

By default, no logs are downloaded. Matching file names are printed on the screen.

```shell  theme={null}
aptible logs_from_archive --database-id "$ID" \
        --stack "$STACK" \
        --region "$REGION" \
        --decryption-keys "$KEY"
```

## Search for archived logs for a specific Database within a specific date range

You can specify a date range in UTC to limit the search to logs emitted during a time period.

```shell  theme={null}
aptible logs_from_archive --database-id "$ID" --start-date "2022-08-30" --end-date "2022-10-03" \
        --stack "$STACK" \
        --region "$REGION" \
        --decryption-keys "$KEY"
```

## Download logs from a specific App to a local path

Once you have identified the files you wish to download, add the `--download-location` parameter to download the files to your local system.

> ❗️ Warning: Since container logs may include PHI or sensitive credentials, please choose the download location carefully.

```shell  theme={null}
aptible logs_from_archive --app-id "$ID" --download-location "$LOCAL_PATH" \
        --stack "$STACK" \
        --region "$REGION" \
        --decryption-keys "$KEY"
```

## Search for logs from a specific Container

You can search for logs for a specific container if you know the container ID.

```shell  theme={null}
aptible logs_from_archive --container-id "$ID" \
        --stack "$STACK" \
        --region "$REGION" \
        --decryption-keys "$KEY"
```
