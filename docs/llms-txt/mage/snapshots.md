# Source: https://docs.mage.ai/guides/dbt/snapshots.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Run dbt snapshot

> Run multiple individual snapshots or bulk snapshots

## Multiple individual snapshots

You can add 1 or more snapshot SQL files into your pipeline as a dbt block.

Add a dbt block as if you were adding a [dbt model](/dbt/run-single-model).
However, select a snapshot file instead of a model file.

## Bulk snapshots

Instead of adding a snapshot file to your pipeline 1 at a time,
you can run the `dbt snapshot` command on an entire folder or exclude certain folders
by doing the following:

1. Add a dbt block and select the option labeled <b>Generic dbt command</b>.
2. In the text input field labeled <b>command</b>, enter the value `snapshot`.
3. You can optionally add the `--select` or `--exclude` flag in the body of the block.


Built with [Mintlify](https://mintlify.com).