# Source: https://docs.expo.dev/versions/latest/sdk/media-library-next

---
title: MediaLibrary (next)
description: A library that provides access to the device's media library.
sourceCodeUrl: 'https://github.com/expo/expo/tree/main/packages/expo-media-library/next'
packageName: 'expo-media-library'
iconUrl: '/static/images/packages/expo-media-library.png'
platforms: ['android', 'ios', 'tvos', 'expo-go']
isNew: true
---

# Expo MediaLibrary (next)

A library that provides access to the device's media library.
Android, iOS, tvOS, Included in Expo Go

`expo-media-library` provides access to the user's media library, allowing apps to read existing images and videos, as well as save new ones.

> On Android, full access to the media library (the main purpose of this package) is allowed only for apps that require broad access to photos. See [details on Google Play's Photo and Video Permissions policy](https://support.google.com/googleplay/android-developer/answer/14115180).

## Installation

```sh
npx expo install expo-media-library
```

If you are installing this in an [existing React Native app](/bare/overview), make sure to [install `expo`](/bare/installing-expo-modules) in your project.

## Usage

Add a new asset from the web

```tsx
import { View, Text } from 'react-native';
import { Image } from 'expo-image';
import { useEffect, useState } from 'react';
import { File, Paths } from 'expo-file-system';
import { Asset, requestPermissionsAsync } from 'expo-media-library/next';

export default function SaveToMediaLibraryExample() {
  const [asset, setAsset] = useState<Asset | null>(null);

  const downloadFile = async () => {
    const url = 'https://picsum.photos/200/300';
    const destinationFile = new File(Paths.cache, 'test_image.jpg');
    if (destinationFile.exists) {
      return destinationFile;
    } else {
      return File.downloadFileAsync(url, destinationFile);
    }
  };

  useEffect(() => {
    const downloadAndSaveAsset = async () => {
      const file = await downloadFile();
      const { status } = await requestPermissionsAsync();
      if (status !== 'granted') {
        return;
      }
      const asset = await Asset.create(file.uri);
      setAsset(asset);
    };

    downloadAndSaveAsset();
  }, []);

  return (
    <View>
      {asset ? (
        <>
          <Text>{asset.id}</Text>
          <Image source={{ uri: asset.id }} style={{ width: 200, height: 300 }} />
        </>
      ) : (
        <Text>Downloading and creating asset...</Text>
      )}
    </View>
  );
}
```
Retrieve asset properties

```tsx
import { View, Text } from 'react-native';
import { useEffect, useState } from 'react';
import { AssetField, MediaType, Query, requestPermissionsAsync } from 'expo-media-library/next';

export default function RetrievingAssetPropertiesExample() {
  const [assetInfo, setAssetInfo] = useState<{
    id: string;
    filename: string;
    mediaType: string;
    width: number;
    height: number;
    creationTime: number | null;
    modificationTime: number | null;
  } | null>(null);

  useEffect(() => {
    const querySomeAsset = async () => {
      const { status } = await requestPermissionsAsync();
      if (status !== 'granted') {
        return;
      }

      const [asset] = await new Query().limit(1).eq(AssetField.MEDIA_TYPE, MediaType.IMAGE).exe();

      if (asset) {
        const filename = await asset.getFilename();
        const mediaType = (await asset.getMediaType()).toString();
        const width = await asset.getWidth();
        const height = await asset.getHeight();
        const creationTime = await asset.getCreationTime();
        const modificationTime = await asset.getModificationTime();
        setAssetInfo({
          id: asset.id,
          filename,
          mediaType,
          width,
          height,
          creationTime,
          modificationTime,
        });
      } else {
        console.log('No assets found in the media library.');
      }
    };

    querySomeAsset();
  }, []);

  return (
    <View>
      {assetInfo ? (
        <View>
          <Text>Asset ID: {assetInfo.id}</Text>
          <Text>Filename: {assetInfo.filename}</Text>
          <Text>Media Type: {assetInfo.mediaType}</Text>
          <Text>
            Dimensions: {assetInfo.width} x {assetInfo.height}
          </Text>
          <Text>
            Creation Time:{' '}
            {assetInfo.creationTime
              ? new Date(assetInfo.creationTime).toLocaleString()
              : 'Unavailable'}
          </Text>
          <Text>
            Modification Time:{' '}
            {assetInfo.modificationTime
              ? new Date(assetInfo.modificationTime).toLocaleString()
              : 'Unavailable'}
          </Text>
        </View>
      ) : (
        <Text>Fetching asset ...</Text>
      )}
    </View>
  );
}
```
Create a new album

```tsx
import { View, Text, FlatList, Image, Button } from 'react-native';
import { useState } from 'react';
import {
  Asset,
  AssetField,
  MediaType,
  Query,
  requestPermissionsAsync,
  Album,
} from 'expo-media-library/next';

export default function CreateAlbumExample() {
  const [assets, setAssets] = useState<Asset[]>([]);
  const [album, setAlbum] = useState<Album | null>(null);
  const [albumTitle, setAlbumTitle] = useState<string>('');

  const createAlbumWithAsset = async () => {
    await requestPermissionsAsync();

    const [asset] = await new Query().limit(1).eq(AssetField.MEDIA_TYPE, MediaType.IMAGE).exe();

    if (!asset) {
      console.log('No assets found in the media library.');
      return;
    }

    const newAlbum = await Album.create('MyNewAlbum', [asset]);

    setAlbum(newAlbum);
    setAlbumTitle(await newAlbum.getTitle());
    const albumAssets = await newAlbum.getAssets();
    setAssets(albumAssets);
  };

  return (
    <View style={{ flex: 1, padding: 20 }}>
      <Button title="Create Album and Add Asset" onPress={createAlbumWithAsset} />

      {assets.length > 0 ? (
        <>
          <Text style={{ marginTop: 20, fontSize: 18, fontWeight: 'bold' }}>
            Assets in {albumTitle}:
          </Text>
          <FlatList
            data={assets}
            keyExtractor={item => item.id}
            renderItem={({ item }) => (
              <View style={{ marginVertical: 10 }}>
                <Image
                  source={{ uri: item.id }}
                  style={{ width: 100, height: 100, borderRadius: 8 }}
                />
              </View>
            )}
          />
        </>
      ) : (
        <Text style={{ marginTop: 20 }}>{album ? 'Album is empty.' : 'No album created yet.'}</Text>
      )}
    </View>
  );
}
```

## API

## Classes

### `Album`

Supported platforms: Android, iOS, tvOS.

Type: Class extends [Album](#album)

Album Properties

### `id`

Supported platforms: Android, iOS, tvOS.

Type: `string`

Unique identifier of the album. Can be used to re-instantiate an [`Album`](#album) later.

Album Methods

### `add(asset)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `asset` | [Asset](/versions/latest/sdk/asset#asset) | The [`Asset`](#asset) to add. |

  

Adds an asset to the album.

Returns: `Promise<void>`

A promise that resolves once the asset has been added.

Example

```ts
const asset = await Asset.create("file:///path/to/photo.png");
await album.add(asset);
```

### `create(name, assetsRefs, moveAssets)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name of the new album. |
| `assetsRefs` | string[] | [Asset[]](/versions/latest/sdk/asset#asset) | List of [`Asset`](#asset) objects or file paths (file:///. .) to include. |
| `moveAssets`(optional) | `boolean` | On Android, whether to move assets into the album. Default: `true` |

  

A static function. Creates a new album with a given name and assets. On Android, if assets are provided and `moveAssets` is true, the assets will be moved into the new album. If false or not supported, the assets will be copied.

Returns: `Promise<album>`

A promise resolving to the created [`Album`](#album).

Example

```ts
const album = await Album.create("My Album", [asset]);
console.log(await album.getTitle()); // "My Album"
```

### `delete()`

Supported platforms: Android, iOS, tvOS.

Permanently deletes the album from the device. On Android, it deletes the album and all its assets. On iOS, it deletes the album but keeps the assets in the main library.

Returns: `Promise<void>`

A promise that resolves once the deletion has completed.

Example

```ts
await album.delete();
```

### `delete(albums, deleteAssets)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `albums` | [Album[]](#album) | An array of [`Album`](#album) instances to delete. |
| `deleteAssets`(optional) | `boolean` | Whether to delete the assets in the albums as well. Default: `false` |

  

A static function. Deletes multiple albums at once.

Returns: `Promise<void>`

A promise that resolves once the albums have been deleted.

Example

```ts
const album = await Album.create("My Album", [asset]);
await Album.delete([album]);
```

### `get(title)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `title` | `string` | The title of the album to retrieve. |

  

A static function. Retrieves an album by its title.

Returns: `Promise<album>`

A promise resolving to the [`Album`](#album) if found, or `null` if not found.

Example

```ts
const album = await Album.get("Camera");
if (album) {
  console.log(await album.getTitle()); // "Camera"
}
```

### `getAssets()`

Supported platforms: Android, iOS, tvOS.

Retrieves all assets contained in the album.

Returns: `Promise<asset[]>`

A promise resolving to an array of [`Asset`](#asset) objects.

Example

```ts
const assets = await album.getAssets();
console.log(assets.length);
```

### `getTitle()`

Supported platforms: Android, iOS, tvOS.

Gets the display title (name) of the album. Note that album titles are not guaranteed to be unique.

Returns: `Promise<string>`

A promise resolving to the album’s title string.

Example

```ts
const title = await album.getTitle();
console.log(title); // "Camera"
```

### `Asset`

Supported platforms: Android, iOS, tvOS.

Type: Class extends [Asset](/versions/latest/sdk/asset#asset)

Asset Properties

### `id`

Supported platforms: Android, iOS, tvOS.

Type: `string`

ID of the asset. Can be used to re-instantiate an [`Asset`](#asset) later. For android it is a contentUri and PHAsset localIdentifier URI for iOS.

Asset Methods

### `create(filePath, album)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `filePath` | `string` | Local filesystem path (for example, `file:///. .`) of the file to import. |
| `album`(optional) | [Album](#album) | Optional [`Album`](#album) instance to place the asset in. |

  

A static function. Creates a new asset from a given file path. Optionally associates the asset with an album. On Android, if not specified, the asset will be placed in the default "Pictures" directory.

Returns: `Promise<asset>`

A promise resolving to the created [`Asset`](#asset).

Example

```ts
const asset = await Asset.create("file:///storage/emulated/0/DCIM/Camera/IMG_20230915_123456.jpg");
console.log(await asset.getFilename()); // "IMG_20230915_123456.jpg"
```

### `delete()`

Supported platforms: Android, iOS, tvOS.

Deletes the asset from the device’s media store.

Returns: `Promise<void>`

A promise that resolves once the deletion has completed.

Example

```ts
await asset.delete();
```

### `delete(assets)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `assets` | [Asset[]](/versions/latest/sdk/asset#asset) |

  

Returns: `Promise<void>`

### `getCreationTime()`

Supported platforms: Android, iOS, tvOS.

Gets the creation time of the asset.

Returns: `Promise<number>`

A promise resolving to the UNIX timestamp in milliseconds, or `null` if unavailable.

### `getDuration()`

Supported platforms: Android, iOS, tvOS.

Gets the duration of the asset. Applies only to assets with media type [`MediaType.audio`](#mediatypeaudio) or [`MediaType.video`](#mediatypevideo). For other media types, it returns `null`.

Returns: `Promise<number>`

A promise resolving to the duration in milliseconds, or `null` if not applicable.

### `getExif()`

Supported platforms: Android, iOS, tvOS.

Gets the exif data of the [`MediaType.image`](#mediatypeimage) asset. On Android, this method requires the `ACCESS_MEDIA_LOCATION` permission to access location metadata.

Returns: `Promise<undefined>`

A promise resolving to the exif data object or an empty object if the exif data is unavailable.

### `getFilename()`

Supported platforms: Android, iOS, tvOS.

Gets the filename of the asset, including its extension.

Returns: `Promise<string>`

A promise resolving to the filename string.

### `getHeight()`

Supported platforms: Android, iOS, tvOS.

Gets the height of the asset in pixels. Only applicable for image and video assets.

Returns: `Promise<number>`

A promise resolving to the height in pixels.

### `getInfo()`

Supported platforms: Android, iOS, tvOS.

Gets detailed information about the asset.

Returns: `Promise<assetinfo>`

A promise resolving to an [`AssetInfo`](#assetinfo)

### `getLocation()`

Supported platforms: Android, iOS, tvOS.

Gets the location of the asset. On Android, this method requires the `ACCESS_MEDIA_LOCATION` permission to access location metadata.

Returns: `Promise<location>`

A promise resolving to the [`Location`](#location) object or `null` if the location data is unavailable.

### `getMediaType()`

Supported platforms: Android, iOS, tvOS.

Gets the media type of the asset (image, video, audio or unknown).

Returns: `Promise<mediatype>`

A promise resolving to a [`MediaType`](#mediatype) enum value.

### `getModificationTime()`

Supported platforms: Android, iOS, tvOS.

Gets the last modification time of the asset.

Returns: `Promise<number>`

A promise resolving to the UNIX timestamp in milliseconds, or `null` if unavailable.

### `getShape()`

Supported platforms: Android, iOS, tvOS.

Gets the shape (width and height) of the asset.

Returns: `Promise<shape>`

A promise resolving to the [`Shape`](#shape) object, or `null` if any dimension is unavailable.

### `getUri()`

Supported platforms: Android, iOS, tvOS.

Gets the URI pointing to the asset’s location in the system. Example, for Android: `file:///storage/emulated/0/DCIM/Camera/IMG_20230915_123456.jpg`.

Returns: `Promise<string>`

A promise resolving to the string URI.

### `getWidth()`

Supported platforms: Android, iOS, tvOS.

Gets the width of the asset in pixels. Only applicable for image and video assets.

Returns: `Promise<number>`

A promise resolving to the width in pixels.

### `Query`

Supported platforms: Android, iOS, tvOS.

Type: Class extends [Query](#query)

Query Methods

### `album(album)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `album` | [Album](#album) | The album to filter assets by. |

  

Filters assets to only those contained in the specified album.

Returns: `Query`

The updated query object for chaining.

### `eq(field, value)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `field` | `T` | an [`AssetField`](#assetfield) to filter by. |
| `value` | `AssetFieldValueMap[T]` | The value that the field should equal. Each field has a specific unique type. |

  

Filters assets where the specified field is equal to the given value.

Returns: `Query`

The updated query object for chaining.

### `exe()`

Supported platforms: Android, iOS, tvOS.

Executes the query and retrieves the matching assets.

Returns: `Promise<asset[]>`

A promise that resolves to an array of [`Asset`](#asset) objects that match the query criteria.

Example

```ts
const assets = await new Query()
 .eq(AssetField.MEDIA_TYPE, MediaType.IMAGE)
 .lte(AssetField.HEIGHT, 1080)
 .orderBy(AssetField.CREATION_TIME)
 .limit(20)
 .exe();
```

### `gt(field, value)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `field` | [AssetField](#assetfield) | an [`AssetField`](#assetfield) to filter by. |
| `value` | `number` | The value that the field should be greater than. |

  

Filters assets where the specified field is greater than the given value.

Returns: `Query`

The updated query object for chaining.

### `gte(field, value)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `field` | [AssetField](#assetfield) | an [`AssetField`](#assetfield) to filter by. |
| `value` | `number` | The value that the field should be greater than or equal to. |

  

Filters assets where the specified field is greater than or equal to the given value.

Returns: `Query`

### `limit(limit)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `limit` | `number` | The maximum number of results to return. |

  

Limits the number of results returned by the query.

Returns: `Query`

The updated query object for chaining.

### `lt(field, value)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `field` | [AssetField](#assetfield) | an [`AssetField`](#assetfield) to filter by. |
| `value` | `number` | The value that the field should be less than. |

  

Filters assets where the specified field is less than the given value.

Returns: `Query`

The updated query object for chaining.

### `lte(field, value)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `field` | [AssetField](#assetfield) | an [`AssetField`](#assetfield) to filter by. |
| `value` | `number` | The value that the field should be less than or equal to. |

  

Filters assets where the specified field is less than or equal to the given value.

Returns: `Query`

The updated query object for chaining.

### `offset(offset)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `offset` | `number` | The number of results to skip. |

  

Skips the specified number of results.

Returns: `Query`

The updated query object for chaining.

### `orderBy(sortDescriptors)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `sortDescriptors` | [AssetField](#assetfield) | [SortDescriptor](#sortdescriptor) | An instance of SortDescriptor or an AssetField. If an AssetField is provided, the sorting will be done in ascending order by default. |

  

Orders the results by the specified sort descriptor or asset field.

Returns: `Query`

### `within(field, value)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `field` | `T` | an [`AssetField`](#assetfield) to filter by. |
| `value` | `undefined` | An array of values that the field should match. Each field has a specific unique type. |

  

Filters assets where the specified field's value is in the given array of values.

Returns: `Query`

The updated query object for chaining.

## Methods

### `MediaLibrary (next).requestPermissionsAsync(writeOnly, granularPermissions)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `writeOnly`(optional) | `boolean` | Default: `false` |
| `granularPermissions`(optional) | [GranularPermission[]](#granularpermission) | A list of [`GranularPermission`](#granularpermission) values. This parameter has an effect only on Android 13 and newer. By default, `expo-media-library` will ask for all possible permissions. When using granular permissions with a custom config plugin configuration, make sure that all the requested permissions are included in the plugin. |

  

Asks the user to grant permissions for accessing media in user's media library.

Returns: `Promise<permissionresponse>`

A promise that fulfils with [`PermissionResponse`](#permissionresponse) object.

## Types

### `AssetFieldValueMap`

Supported platforms: Android, iOS, tvOS.

| Property | Type | Description |
| --- | --- | --- |
| creationTime | `number` | - |
| duration | `number` | - |
| height | `number` | - |
| mediaType | [MediaType](#mediatype) | - |
| modificationTime | `number` | - |
| width | `number` | - |

### `AssetInfo`

Supported platforms: Android, iOS, tvOS.

| Property | Type | Description |
| --- | --- | --- |
| creationTime | `number | null` | - |
| duration | `number | null` | - |
| filename | `string` | - |
| height | `number` | - |
| id | `string` | - |
| mediaType | [MediaType](#mediatype) | - |
| modificationTime | `number | null` | - |
| uri | `string` | - |
| width | `number` | - |

### `GranularPermission`

Supported platforms: Android, iOS, tvOS.

Literal Type: `string`

Acceptable values are: `'audio'` | `'photo'` | `'video'`

### `SortDescriptor`

Supported platforms: Android, iOS, tvOS.

| Property | Type | Description |
| --- | --- | --- |
| ascending(optional) | `boolean` | - |
| key | [AssetField](#assetfield) | - |

## Enums

### `AssetField`

Supported platforms: Android, iOS, tvOS.

#### `CREATION_TIME`

`AssetField.CREATION_TIME = "creationTime"`

#### `DURATION`

`AssetField.DURATION = "duration"`

#### `HEIGHT`

`AssetField.HEIGHT = "height"`

#### `MEDIA_TYPE`

`AssetField.MEDIA_TYPE = "mediaType"`

#### `MODIFICATION_TIME`

`AssetField.MODIFICATION_TIME = "modificationTime"`

#### `WIDTH`

`AssetField.WIDTH = "width"`

### `MediaType`

Supported platforms: Android, iOS, tvOS.

#### `AUDIO`

`MediaType.AUDIO = "audio"`

#### `IMAGE`

`MediaType.IMAGE = "image"`

#### `UNKNOWN`

`MediaType.UNKNOWN = "unknown"`

#### `VIDEO`

`MediaType.VIDEO = "video"`
