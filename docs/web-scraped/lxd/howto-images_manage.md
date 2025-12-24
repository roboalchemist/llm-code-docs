# Source: https://documentation.ubuntu.com/lxd/en/latest/howto/images_manage/

[]

# How to manage images[¶](#how-to-manage-images "Link to this heading")

When working with images, you can inspect various information about the available images, view and edit their properties and configure aliases to refer to specific images. You can also export an image to a file, which can be useful to [[copy or import it]](../images_copy/#images-copy) on another machine.

## List available images[¶](#list-available-images "Link to this heading")

CLI

API

UI

To list all images on a server, enter the following command:

    lxc image list [<remote>:]

If you do not specify a remote, the [[default remote]](../images_remote/#images-remote-default) is used.

Query the [`/1.0/images`] endpoint to list all images on the server:

    lxc query --request GET /1.0/images

To include information about each image, add [`recursion=1`]:

    lxc query --request GET /1.0/images?recursion=1

See [[`GET`]` `[`/1.0/images`]](/lxd/latest/api/#/images/images_get) and [[`GET`]` `[`/1.0/images?recursion=1`]](/lxd/latest/api/#/images/images_get_recursion1) for more information.

Note

The [`/1.0/images`] endpoint is available on LXD servers, but not on simple streams servers (see [[Remote server types]](../../reference/remote_image_servers/#remote-image-server-types)). Public image servers, like the [official Ubuntu image server](https://cloud-images.ubuntu.com/releases/), use the [simple streams format](https://git.launchpad.net/simplestreams/tree/).

To retrieve the list of images from a simple streams server, start at the [`streams/v1/index.sjson`] index (for example, [[`https://cloud-images.ubuntu.com/releases/streams/v1/index.sjson`]](https://cloud-images.ubuntu.com/releases/streams/v1/index.sjson)).

Go to [Images] to view all images on the local server.

[]

### Filter available images[¶](#filter-available-images "Link to this heading")

CLI

API

UI

To filter the results that are displayed, specify a part of the alias or fingerprint after the command. For example, to show all Ubuntu 24.04 LTS images, enter the following command:

    lxc image list ubuntu: 24.04

You can specify several filters as well. For example, to show all Arm 64-bit Ubuntu 24.04 LTS images, enter the following command:

    lxc image list ubuntu: 24.04 arm64

To filter for properties other than alias or fingerprint, specify the filter in [`<key>=<value>`] format. For example:

    lxc image list ubuntu: 24.04 architecture=x86_64

You can [[filter]](../../rest-api/#rest-api-filtering) the images that are displayed by any of their fields.

For example, to show all Ubuntu images, or all images for Ubuntu 24.04 LTS:

    lxc query --request GET /1.0/images?filter=properties.os+eq+ubuntu
    lxc query --request GET /1.0/images?filter=properties.version+eq+24.04

You can specify several filters as well. For example, to show all Arm 64-bit images for virtual machines, enter the following command:

    lxc query --request GET /1.0/images?filter=architecture+eq+arm64+and+type+eq+virtual-machine

You can also use a regular expression:

    lxc query --request GET "/1.0/images?filter=fingerprint+eq+be25.*"

See [[`GET`]` `[`/1.0/images`]](/lxd/latest/api/#/images/images_get) and [[Filtering]](../../rest-api/#rest-api-filtering) for more information.

To filter the images that are displayed, use the search box.

For example, to show all Ubuntu images, search for [`ubuntu`]. To display only images for version 24.04, search for [`24.04`].

## View image information[¶](#view-image-information "Link to this heading")

CLI

API

UI

To view information about an image, enter the following command:

    lxc image info <image_ID>

As the image ID, you can specify either the image's alias or its fingerprint. For a remote image, remember to include the remote server (for example, [`ubuntu:24.04`]).

To display only the image properties, enter the following command:

    lxc image show <image_ID>

You can also display a specific image property (located under the [`properties`] key) with the following command:

    lxc image get-property <image_ID> <key>

For example, to show the release name of the official Ubuntu 24.04 LTS image, enter the following command:

    lxc image get-property ubuntu:24.04 release

To view all information about an image, query it using its fingerprint:

    lxc query --request GET /1.0/images/<fingerprint>

See [[`GET`]` `[`/1.0/images/`]](/lxd/latest/api/#/images/image_get) for more information.

If you don't know the fingerprint but the alias, you can retrieve the fingerprint by querying the [`/1.0/images/aliases/`] endpoint:

    lxc query --request GET /1.0/images/aliases/<alias>

See [[`GET`]` `[`/1.0/images/aliases/`]](/lxd/latest/api/#/images/image_alias_get) for more information.

The UI does not currently support viewing detailed image information.

[]

## Edit image properties[¶](#edit-image-properties "Link to this heading")

CLI

API

UI

To set a specific image property that is located under the [`properties`] key, enter the following command:

    lxc image set-property <image_ID> <key> <value>

Note

These properties can be used to convey information about the image. They do not configure LXD's behavior in any way.

To edit the full image properties, including the top-level properties, enter the following command:

    lxc image edit <image_ID>

To set a specific image property that is located under the [`properties`] key, send a PATCH request to the image:

    lxc query --request PATCH /1.0/images/<fingerprint> --data '
    }'

See [[`PATCH`]` `[`/1.0/images/`]](/lxd/latest/api/#/images/image_patch) for more information.

Note

These properties can be used to convey information about the image. They do not configure LXD's behavior in any way.

To update the full image properties, including the top-level properties, send a PUT request with the full image data:

    lxc query --request PUT /1.0/images/<fingerprint> --data '<image_configuration>'

See [[`PUT`]` `[`/1.0/images/`]](/lxd/latest/api/#/images/image_put) for more information.

The UI does not currently support editing image properties.

## Delete an image[¶](#delete-an-image "Link to this heading")

CLI

API

UI

To delete a local copy of an image, enter the following command:

    lxc image delete <image_ID>

To delete a local copy of an image, send a DELETE request:

    lxc query --request DELETE /1.0/images/<fingerprint>

See [[`DELETE`]` `[`/1.0/images/`]](/lxd/latest/api/#/images/image_delete) for more information.

In the images list, click the [Delete] button (![](data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjE2IiB3aWR0aD0iMTYiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTQuNSA2djZhMS41IDEuNSAwIDAwMS4zNTYgMS40OTNMNiAxMy41aDRhMS41IDEuNSAwIDAwMS40OTMtMS4zNTZMMTEuNSAxMlY2SDEzdjZhMyAzIDAgMDEtMyAzSDZhMyAzIDAgMDEtMy0zVjZoMS41em0zIDB2NS45OTRINlY2aDEuNXptMi40OTggMHY1Ljk5NGgtMS41VjZoMS41ek04LjUgMEEyLjUgMi41IDAgMDExMSAyLjVWM2gzdjEuNUgyVjNoM3YtLjVBMi41IDIuNSAwIDAxNy41IDBoMXptMCAxLjVoLTFhMSAxIDAgMDAtLjk5My44ODNMNi41IDIuNVYzaDN2LS41YTEgMSAwIDAwLS44ODMtLjk5M0w4LjUgMS41eiIgZmlsbD0iJTIzMDAwIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPjwvcGF0aD48L3N2Zz4=)) next to an image to delete it.

You can also select several images and click the [Delete images] button at the top to delete all selected images.

Deleting an image won't affect running instances that are already using it, but it will remove the image locally.

After deletion, if the image was downloaded from a remote server, it will be removed from local cache and downloaded again on next use. However, if the image was manually created (not cached), the image will be deleted.

## Configure image aliases[¶](#configure-image-aliases "Link to this heading")

Configuring an alias for an image can be useful to make it easier to refer to an image, since remembering an alias is usually easier than remembering a fingerprint. Most importantly, however, you can change an alias to point to a different image, which allows creating an alias that always provides a current image (for example, the latest version of a release).

CLI

API

UI

You can see some of the existing aliases in the image list. To see the full list, enter the following command:

    lxc image alias list

You can directly assign an alias to an image when you [[copy or import]](../images_copy/#images-copy) or [[publish]](../images_create/#images-create-publish) it. Alternatively, enter the following command:

    lxc image alias create <alias_name> <image_fingerprint>

You can also delete an alias:

    lxc image alias delete <alias_name>

To rename an alias, enter the following command:

    lxc image alias rename <alias_name> <new_alias_name>

If you want to keep the alias name, but point the alias to a different image (for example, a newer version), you must delete the existing alias and then create a new one.

To retrieve a list of all defined aliases, query the [`/1.0/images/aliases`] endpoint:

    lxc query --request GET /1.0/images/aliases

To include information about each alias, add [`recursion=1`]:

    lxc query --request GET /1.0/images/aliases?recursion=1

See [[`GET`]` `[`/1.0/images/aliases`]](/lxd/latest/api/#/images/images_aliases_get) and [[`GET`]` `[`/1.0/images/aliases?recursion=1`]](/lxd/latest/api/#/images/images_aliases_get_recursion1) for more information.

You can directly assign an alias to an image when you [[copy or import]](../images_copy/#images-copy) or [[publish]](../images_create/#images-create-publish) it. Alternatively, send a POST request to the [`/1.0/images/aliases`] endpoint to create an alias:

    lxc query --request POST /1.0/images/aliases --data ''

See [[`POST`]` `[`/1.0/images/aliases`]](/lxd/latest/api/#/images/images_aliases_post) for more information.

You can also delete an alias:

    lxc query --request DELETE /1.0/images/aliases/<alias_name>

To rename an alias, send a POST request to the alias:

    lxc query --request POST /1.0/images/aliases/<alias_name> --data ''

If you want to keep the alias name, but point the alias to a different image (for example, a newer version), send a PATCH request to the alias:

    lxc query --request PATCH /1.0/images/aliases/<alias_name> --data ''

See [[`DELETE`]` `[`/1.0/images/aliases/`]](/lxd/latest/api/#/images/image_alias_delete), [[`POST`]` `[`/1.0/images/aliases/`]](/lxd/latest/api/#/images/images_alias_post), and [[`PATCH`]` `[`/1.0/images/aliases/`]](/lxd/latest/api/#/images/images_alias_patch) for more information.

The UI displays configured aliases in the images list, but it does not currently support configuring image aliases.

[]

## Export an image to a set of files[¶](#export-an-image-to-a-set-of-files "Link to this heading")

Images are located in the image store of your local server or a remote LXD server. You can export them to a file or a set of files though (see [[Image tarballs]](../../reference/image_format/#image-format-tarballs)). This method can be useful to back up image files or to transfer them to an air-gapped environment.

CLI

API

UI

To export a container image to a set of files, enter the following command:

    lxc image export [<remote>:]<image> [<output_directory_path>]

To export a virtual machine image to a set of files, add the [`--vm`] flag:

    lxc image export [<remote>:]<image> [<output_directory_path>] --vm

Send a query to the [`export`] endpoint of the image to retrieve it:

    curl -X GET --unix-socket /var/snap/lxd/common/lxd/unix.socket lxd/1.0/images/<fingerprint>/export \
    --output <output-file>

If the image is a [[split image]](../../reference/image_format/#image-format-split), the output file contains two separate tarballs in multipart format.

See [[`GET`]` `[`/1.0/images//export`]](/lxd/latest/api/#/images/image_export_get) for more information.

The UI does not currently support exporting images.

See [[Image format]](../../reference/image_format/#image-format) for a description of the file structure used for the image.