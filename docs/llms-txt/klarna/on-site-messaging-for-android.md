# Source: https://docs.klarna.com/conversion-boosters/on-site-messaging/integrate-on-site-messaging/on-site-messaging-for-mobile/on-site-messaging-for-android.md

# On-site Messaging for Android

​Adding On-Site Messaging is as easy as it gets. To achieve this tailor made experience for the user you just need to:

- Request access to On-Site Messaging
- Create the native view
- Set the parameters
- Render the view

## Request Access to On-Site Messaging

If you are using a version of the [SDK prior to 2.3.2](https://github.com/klarna/klarna-mobile-sdk-android/blob/master/CHANGELOG.md#232---2022-10-26), to be able to integrate On-site Messaging our team needs to enable the access for it. You can request access through your dedicated Delivery Manager. Please refer the Merchant ID (MID) and/or the name of your brand/company (merchant name), the countries you request access and the environment (playground or production).

## Creating the Native View

The On-Site Messaging native view in Android is called KlarnaOSMView. You can create KlarnaOSMView programmatically or inflate it from an XML file. Additionally you can also set the parameters from the XML.

### Create the View Programmatically

You can create the native view programmatically and add it to your layout with your desired layout options.

``` kotlin
// Create an instance of OSM view
val osmView = KlarnaOSMView(context)
// Add it to your layout with desired layout parameters
val osmLayoutParams = ViewGroup.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT,
ViewGroup.LayoutParams.WRAP_CONTENT)
containerViewGroup.addView(osmView, osmLayoutParams)
```

## Create the View from XML

You can also add the native view in your XML like below:

``` markup
<com.klarna.mobile.sdk.api.osm.klarnaosmview ...="" android:id="@+id/klarnaOsmView" android:layout_height="wrap_content" android:layout_width="match_parent"></com.klarna.mobile.sdk.api.osm.klarnaosmview>
```

Now you can access the view like this:

``` java
val osmView = findViewById<klarnaosmview>(R.id.klarnaOsmView)
```

## Parameters

Parameters used for KlarnaOSMView are set as variables of the View instance or as attributes in the XML declaration. These can be identifier string values, amount or enumeration values (parameters marked with \* are mandatory).

| **Param** | **Type** | **Description** |
|----|----|----|
| clientId\* | String | On-Site Messaging Client Identifier gathered from Klarna Merchant Portal. |
| placementKey\* | String ("credit-promotion-badge" or "top-strip-promotion-badge") | Placement key identifier from Klarna Merchant Portal. At the moment the supported placement keys are "credit-promotion-badge" and "top-strip-promotion-badge" |
| locale\* | String | Locale string for the placement configuration, default value is en-US. |
| purchaseAmount | Long | Amount for the placement. Set in micro units (\$120.00 = 12000), used for amount based credit promotions. |
| environment\* | KlarnaOSMEnvironment | Enumerated environment value to specify merchant’s running environment. Default value is DEMO. |
| region\* | KlarnaOSMRegion | Enumerated region value to specify merchant’s running market region. |
| theme\* | KlarnaOSMTheme | Enumerated theme value to specify how to stylize the view on light and dark configurations. |
| hostActivity\* | Activity | Activity instance to specify parent activity. It will be used for inner linking for informational pages. The reference will be kept as a weak reference. |
| styleConfiguration | KlarnaOSMStyleConfiguration | Can be used to customize the appearance of the OSM view. If not set, a default appearance will be used based on the specified theme. **Note: this is available from version 2.6.17.** |

### KlarnaOSMEnvironment

Environment enumeration will be used to define whether to use a demo placement or fetch placement configurations from either playground or production.

| **Name** | **Description** |
|----|----|
| DEMO | This environment ignores all other parameters and shows a demo placement config containing all On-Site Messaging features. |
| PLAYGROUND | This environment is for placement configurations from playground Merchant Portal. |
| PRODUCTION | This environment is for production builds of the app with placement configurations for production merchants. |

### KlarnaOSMRegion

Region enumeration will be used to define which endpoint to connect as a source for the placement configurations.

| **Name** | **Description**                 |
|----------|---------------------------------|
| EU       | Region value for Europe.        |
| NA       | Region value for North America. |
| OC       | Region value for Oceania.       |

### KlarnaOSMTheme

Theme enumeration will be used to define which style of OSM to be used, depending on either the app’s configuration or the system setting. Each style has a predefined set of values for background color, text color, text size, ... that will be used to style the OSM view.

| **Name** | **Descriptions** |
|----|----|
| LIGHT | Light style for placement view. |
| DARK | Dark style for placement view. |
| AUTOMATIC | Automatic theme that will use the system’s user interface style. |

### KlarnaOSMStyleConfiguration

This feature is available from version 2.6.17. By using KlarnaOSMStyleConfiguration you can customize the appearance of the OSM view to some extend. As of now, you can customize the following:

- Background color
- Text color
- Text size
- Text size unit
- Text font

Please note that `styleConfiguration` takes precedence over `theme`. This has the following implications:

- If you specify a value thorough `styleConfiguration` (text color, for example) then this value will be used to style the OSM view regardless of the value that `theme` provides.
- If your app supports light and dark mode, then it's your responsibility to update `styleConfiguration` and call the render method when the device's theme changes so that the appearance of the OSM view updates.

To set a custom style for the OSM view you can do like the following:

``` kotlin
val klarnaOSMStyleConfiguration = KlarnaOSMStyleConfiguration.Builder()
    .setBackgroundColor(0xFFFFFF)
    .setTextStyle(
        KlarnaTextStyleConfiguration.Builder()
            .setTextColor(0x000000)
            .setTextSize(unit = TypedValue.COMPLEX_UNIT_SP, size = 16f)
            .setTextFont(ResourcesCompat.getFont(this, R.font.merriweather_regular)) // assuming that there's a font file in the 'res/font' directory with the name 'merriweather_regular'
            .build()
    )
    .build()
osmView.styleConfiguration = klarnaOSMStyleConfiguration
```

## Setting the Parameters

All of the parameters for On-Site Messaging are stored as variables on the KlarnaOSMView instance. The required ones need to be set before calling the render method, otherwise the RenderResult will return a validation error for the missing parameter. Most of the parameters can be set either programmatically or in the XML layout file. The only two exceptions are hostActivity and styleConfiguration that you can only set them programatically. In both cases, the parameters will be stored in the View instance.

### Setting the Parameters Programmatically

``` kotlin
osmView.clientId = "<client-id>"
osmView.placementKey = "<placement-key>"
osmView.locale = "en-US"
osmView.purchaseAmount = 10000
osmView.environment = KlarnaOSMEnvironment.PRODUCTION
osmView.region = KlarnaOSMRegion.NA
osmView.theme = KlarnaOSMTheme.DARK
osmView.styleConfiguration = ...
osmView.hostActivity = this // assuming that 'this' refers to the current Activity
```

### Setting the Parameters in XML

``` markup
<com.klarna.mobile.sdk.api.osm.klarnaosmview ...="" app:klarnaosmclientid="&lt;client-id&gt;" app:klarnaosmenvironment="production" app:klarnaosmlocale="en-US" app:klarnaosmplacementkey="&lt;placement-key&gt;" app:klarnaosmpurchaseamount="1000" app:klarnaosmregion="na" app:klarnaosmtheme="dark"></com.klarna.mobile.sdk.api.osm.klarnaosmview>
```

## Rendering the Placement

Once you have set all the parameters to the KlarnaOSMView, you are ready to render the actual placement view. To do that, you need to call the render method of the view with the RenderResult callback parameter. Once the render method is called, first the view will validate all the parameters. If there is a missing parameter the RenderResult callback will be invoked with corresponding error values. If parameters are valid then the view will try to fetch placement configuration from On-Site Messaging API. Any errors or failures from this network request will also invoke RenderResult callback if necessary. If the placement configuration is fetched and valid then the KlarnaOSMView will render it and invoke the RenderResult callback with a null value.

### Calling the Render Method

The RenderResult callback can be used for logging purposes or to make the KlarnaOSMView visible or not, according to the error.

``` kotlin
osmView.render(RenderResult { error -&gt;
    ...
})
```

## Identifying the Errors

Similar to other parts of the SDK, On-Site Messaging also makes use of the KlarnaMobileSDKError class. To read more about the error handling and error object properties refer to the [On-Site Messaging Error Handling guide](https://docs.klarna.com/conversion-boosters/on-site-messaging/integrate-on-site-messaging/on-site-messaging-for-mobile/).

### Klarna On-Site Messaging Error Names

These are the predefined names for errors that can happen during the placement render flow. These names are available as static variables inside KlarnaOSMError class.

| **Error Name** | **Description** |
|----|----|
| KlarnaOSMErrorMissingClientId | Client ID was not set. Set the `clientId` variable and invoke render again. |
| KlarnaOSMErrorMissingPlacementKey | Placement key was not set. Set the `placementKey`variable and invoke render again. |
| KlarnaOSMErrorMissingRegion | Region was not set. Set the `region` variable and invoke render again. |
| KlarnaOSMErrorMissingHost | Hosting activity was not set. Set the `hostActivity` variable and invoke render again. |
| KlarnaOSMErrorInvalidPlacementConfig | Fetched configuration from the API can not be rendered by the native view. |
| KlarnaOSMErrorPlacementError | On-Site Messaging API has returned an error. Message of this error will contain information sent from the API. |
| KlarnaOSMErrorNetworkError | A network error occurred and the placement will not be rendered. |
| KlarnaOSMErrorDisabled | Native On-Site Messaging has been disabled by Klarna, the placement will not be rendered. |</placement-key></client-id></klarnaosmview>