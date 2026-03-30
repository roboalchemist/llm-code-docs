# Source: https://help.cloudsmith.io/docs/import-files-from-a-folder.md

# Import files from a folder

How to a bulk import of packages into Cloudsmith in a folder

## Bulk Import

Once you have exported all your npm packages you can upload them to Cloudsmith- yay!

First make sure you install the [Cloudsmith CLI ](https://help.cloudsmith.io/docs/cli) and [export your token](https://help.cloudsmith.io/docs/cli).

A folder of packages in the correct format can be published to Cloudsmith using the script below. We support over 28+ format types. The supported formats can be found [here](https://help.cloudsmith.io/docs/supported-formats).\
Create the bash script below and call it `migrate_npm_to_cs.sh` and give it execute privileges.\
cd into the folder.

```shell
#!/bin/bash
FILES="."
for f in *
do
  echo "Processing $f file..."
  cloudsmith push "$1" "$2" $f
done
```

If your packages are organized into nested folders (subdirectories), the script above won’t process them by default. You can use the following version of the script to handle this situation.

```shell
#!/bin/bash
FILES=$(find . -type f)
for f in $FILES
do
  echo "Processing $f file..."
  cloudsmith push "$1" "$2" "$f"
done
```

Execute the `migrate_npm_to_cs.sh` file passing the [format type](https://help.cloudsmith.io/docs/supported-formats) and the path of `<CLOUDSMITH_ORG>/<CLOUDSMITH_REPO>`:

```shell
./migrate_npm_to_cs.sh python cloudsmith_org/cloudsmith_repo
```