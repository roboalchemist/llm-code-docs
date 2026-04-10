# Source: https://directus.io/docs/raw/guides/files/transform.md

# Transform Files

> Learn how to transform files and set custom presets for these transformations.

<video-embed video-id="3fd6dfb4-644b-43d0-9aef-5a6e5488efa8">



</video-embed>

Directus allows you to transform assets using URL query parameters. You can pass these as either query parameters to the `assets` endpoint. If a processed asset does not yet exist, it is dynamically generated, stored, and returned.

## Custom Transformations

<video-embed video-id="59b18d30-080b-42cf-84ef-fdca7542388d">



</video-embed>

<table>
<thead>
  <tr>
    <th>
      Parameter
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        width
      </code>
    </td>
    
    <td>
      How wide the image is in pixels.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        height
      </code>
    </td>
    
    <td>
      How high the image is in pixels.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        quality
      </code>
    </td>
    
    <td>
      The overall image quality (1 to 100), defaults to <a href="https://sharp.pixelplumbing.com/api-output/#jpeg" rel="nofollow">
        the Sharp API's default for the given format
      </a>
      
       if omitted. The higher the value, the larger the image size. The lower the value, the more compression artifacts are in the image.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        withoutEnlargement
      </code>
    </td>
    
    <td>
      Disable automatically upscaling the image (true)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        format
      </code>
    </td>
    
    <td>
      What file format to return the image in. One of auto, jpg, png, webp, tiff auto default if omitted, Will try to format it in webp or avif if the browser supports it, otherwise it will fallback to jpg.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        fit
      </code>
    </td>
    
    <td>
      How the image should fit into the provided dimensions, values including: <ul>
        <li>
          <strong>
            <code>
              cover
            </code>
            
             (default if omitted)
          </strong>
          
          : try to fit the image into the dimensions while preserving the aspect ratio
        </li>
        
        <li>
          <strong>
            <code>
              contain
            </code>
          </strong>
          
          : contain within the dimensions while using "letterboxing" to fill the rest
        </li>
        
        <li>
          <strong>
            <code>
              inside
            </code>
          </strong>
          
          : Resize to be as large as possible within the dimensions
        </li>
        
         <li>
          <strong>
            <code>
              outside
            </code>
          </strong>
          
          : Resize to be as small as possible within or beyond the dimensions
        </li>
      </ul>
    </td>
  </tr>
</tbody>
</table>

<callout icon="material-symbols:info-outline">

**Focal Points**<br />


When transforming an image with `width` and/or `height` parameters, the focal point is taken from the `focal_point_x` and `focal_point_y` coordinate values stored in the file object, cropping the image around these. This defaults to the image's centre.

</callout>

<video-embed video-id="954941eb-b737-412f-967b-387295df72bf">



</video-embed>

<code-group>

```http [REST]
GET /assets/c984b755-e201-497e-b0a7-24156ad9c7e0
    ?width=300
    &height=300
    &quality=50
    &fit=contain
```

```graphql [GraphQL]
# Not supported by GraphQL
```

```js [SDK]
import { createDirectus, rest, readAssetRaw } from '@directus/sdk';

const FILE_ID = 'c984b755-e201-497e-b0a7-24156ad9c7e0';

const directus = createDirectus('directus_project_url').with(rest());

const result = await directus.request(
  readAssetRaw(FILE_ID, {
    width: 300,
    height: 300,
    quality: 50,
    fit: 'contain',
  }),
);
```

</code-group>

## Advanced Transformations

<video-embed video-id="1c8eb8c1-f7eb-4b24-9cac-e742a70a9da1">



</video-embed>

Directus allows full access to the [Sharp API](https://sharp.pixelplumbing.com/), giving you access to more complex image transformations.

This is done using the `transforms` parameter, whose value consists of a two dimensional array. Each sub-array contains the name of the operation, followed by its arguments: `[["operation1", …arguments], ["operation2", …otherArguments]]`.

<callout icon="material-symbols:info-outline">

**REST Values**<br />


When calling the REST API, datatypes like booleans need to be passed as strings.

</callout>

<table>
<thead>
  <tr>
    <th>
      sharp API Call
    </th>
    
    <th>
      transforms Equivalent
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        .rotate(90)
      </code>
    </td>
    
    <td>
      <code>
        [["rotate", 90]]
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        .rotate(90).blur(10).tint(255, 0, 255)
      </code>
    </td>
    
    <td>
      <code>
        [["rotate", 90], ["blur", 10], ["tint", "rgb(255, 0, 255)"]]
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        negate({lower: 10, upper: 50})
      </code>
    </td>
    
    <td>
      <code>
        [["negate", {"lower": 10, "upper": 50}]]
      </code>
    </td>
  </tr>
</tbody>
</table>

<code-group>

```http [REST]
GET /assets/c984b755-e201-497e-b0a7-24156ad9c7e0
    ?transforms=[["rotate", 90],["blur", 10],["tint", "rgb(255, 0, 255)"], ["negate", {"lower": 10, "upper": 50}]]
```

```graphql [GraphQL]
# Not supported by GraphQL
```

```js [SDK]
import { createDirectus, rest, readAssetRaw } from '@directus/sdk';

const FILE_ID = 'c984b755-e201-497e-b0a7-24156ad9c7e0';

const directus = createDirectus('directus_project_url').with(rest());

const result = await directus.request(
  readAssetRaw(FILE_ID, {
    transforms: [
      ['rotate', 90],
      ['blur', 10],
      ['tint', 'rgb(255, 0, 255)'],
      [
        'negate',
        {
          lower: 10,
          upper: 50,
        },
      ],
    ],
  }),
);
```

</code-group>

Custom and advanced transformations can also be used in conjunction.

<code-group>

```http [REST]
GET /assets/c984b755-e201-497e-b0a7-24156ad9c7e0
    ?transforms=[["flip"]]
    &fit=cover
    &width=300
    &height=100
```

```graphql [GraphQL]
# Not supported by GraphQL
```

```js [SDK]
import { createDirectus, rest, readAssetRaw } from '@directus/sdk';

const FILE_ID = 'c984b755-e201-497e-b0a7-24156ad9c7e0';

const directus = createDirectus('directus_project_url').with(rest());

const result = await directus.request(
  readAssetRaw(FILE_ID, {
    transforms: [['flip']],
    fit: 'cover',
    width: 300,
    height: 100,
  }),
);
```

</code-group>

## Preset Transformations

<video-embed video-id="731d8184-1ba4-4fa7-99e4-571492d1c552">



</video-embed>

In order to mitigate the creation a large number of files, you can restrict the transformations to a set of presets. You can create your own storage asset preset in the "Settings" section of your project's settings.

The following options are available:

- **Allowed Transformations**: for enabling, disabling, or limiting image transformations.
- **Default Folder**: sets the default folder where new assets are added. This does not affect existing files. Be aware
that fields may override this value.
- **Transformation Presets**: sets a specific image transformation configuration to simplify requests or limit usage.

  - **Key**: sets unique identifier allowing faster and easier image transformation requests.
  - **Fit**: contain *(keeps aspect ratio)*, Cover *(exact size)*, Fit Inside, or Fit Outside.
  - **Width**: sets the width of the image.
  - **Height**: sets the height of the image.
  - **Quality**: adjusts the compression or quality of the image.
  - **Upscaling**: when enabled, images won't be upscaled.
  - **Format**: changes the output format.
  - **Additional Transformations**: adds additional transformations using
  [Sharp](https://sharp.pixelplumbing.com/api-constructor).

You can then use this `key` as a parameter to when requesting a file to apply the preset.
