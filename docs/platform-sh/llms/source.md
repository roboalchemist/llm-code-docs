# Source: https://docs.upsun.com/integrations/source.md

# Source: https://docs.upsun.com/create-apps/image-properties/source.md

# source


Contains information about the app’s source code and operations that can be run on it.

Optional in [single-runtime](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#primary-application-properties) and [composable](https://docs.upsun.com/create-apps/app-reference/composable-image.md#primary-application-properties) images.

The following table shows the properties that can be set in `source`:

| Name         | Type                     | Required | Description                                                                                                                       |
|--------------|--------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------|
| `operations` | An operations dictionary |          | Operations that can be applied to the source code. See [source operations](https://docs.upsun.com/create-apps/source-operations.md).                              |
| `root`       | `string`                 |          | The path where the app code lives. Useful for [multi-app setups](https://docs.upsun.com/create-apps/multi-app.md). <BR>**Single-runtime image**: Defaults to the directory of the `.upsun/config.yaml` file. <BR>**Composable image**: Defaults to the root project directory.|
