# Source: https://gokapi.readthedocs.io/en/stable/update.html

[]

# Updating Gokapi[](#updating-gokapi "Link to this heading")

## Docker[](#docker "Link to this heading")

To update, run the following command:

    docker pull f0rc3/gokapi:YOURTAG

Then stop the running container and follow the same steps as in SETUP. All userdata will be preserved, as it is saved to the [`gokapi-data`] and [`gokapi-data`] volume ([`-v`] argument during creation)

## Native deployment[](#native-deployment "Link to this heading")

### Stable version[](#stable-version "Link to this heading")

To update, download the latest release and unzip it to the directory that contains the old version. Overwrite any existing files.

### Unstable version[](#unstable-version "Link to this heading")

To update, execute the command [`git`]` `[`pull`] and then rebuild the binary with [`go`]` `[`build`]` `[`Gokapi/cmd/gokapi`].