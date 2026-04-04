# Source: https://docs.klarna.com/conversion-boosters/on-site-messaging/integrate-on-site-messaging/on-site-messaging-for-mobile/on-site-messaging-for-ios.md

# On-Site Messaging for iOS

Adding On-Site Messaging is as easy as it gets. To achieve this tailor made experience for the user you just need to:

- Request access to On-Site Messaging
- Create the native view
- Set the parameters
- Render the view

## Request Access to On-site Messaging

If you are using a version of the [SDK prior 2.3.2](https://github.com/klarna/klarna-mobile-sdk/blob/master/CHANGELOG.md#232---2022-10-31), to be able to integrate On-site Messaging our team needs to enable the access for it. You can request access through your dedicated Delivery Manager. Please refer the Merchant ID (MID) and/or the name of your brand/company (merchant name), the countries you request access and the environment (playground or production).

## Creating the Native View

The On-Site Messaging native view in iOS is called KlarnaOSMView. You can create KlarnaOSMView programmatically and add it to your view controller or custom views.

### Create the View Programmatically

You can create the native view programmatically and place it in your application with desired layout options.

``` swift
// Create the placement view
let osmView = KlarnaOSMView()
// Set constraints
// ...
osmView.translatesAutoresizingMaskIntoConstraints = false
view.addSubview(osmView)
```

## Parameters

Parameters used for the KlarnaOSMView are set as variables of the UIView instance. These can be identifier string values, amount or enumeration values.

| **Param** | **Type** | **Description** |
|----|----|----|
| clientId | String | On-Site Messaging Client Identifier gathered from Klarna Merchant Portal. |
| placementKey | String ("credit-promotion-badge" or "top-strip-promotion-badge") | Placement key identifier from Klarna Merchant Portal. At the moment the supported placement keys are "credit-promotion-badge" and "top-strip-promotion-badge" |
| locale | String | Locale string for the placement configuration, default value is en-US. |
| purchaseAmount | Int | Amount for the placement. Set in micro units (\$120.00 = 12000), used for amount based credit promotions. |
| environment | KlarnaOSMEnvironment | Enumerated environment value to specify merchant’s running environment. Default value is demo environment. |
| region | KlarnaOSMRegion | Enumerated region value to specify merchant’s running market region. |
| theme | KlarnaOSMTheme | Enumerated theme value to specify how to stylize the view on light and dark configurations. |
| styleConfiguration | KlarnaOSMStyleConfiguration | Can be used to customize the look and feel of the placement. If not set, a default look and feel will be used based on the specified theme. **Note: this is available from version 2.6.20.** |
| hostViewController | UIViewController | UIViewController instance to specify parent view controller. It will be used for inner linking for informational pages. The reference will be kept as a weak reference. |
| delegate | KlarnaOSMViewEventListener | This delegate will be used to notify your application for changes in size of the native view. |

### KlarnaOSMEnvironment

Environment enumeration will be used to define whether to use a demo placement or fetch placement configurations from either playground or production.

| **Name** | **Description** |
|----|----|
| demo | This environment ignores all other parameters and shows a demo placement config containing all On-Site Messaging features. |
| playground | This environment is for placement configurations from playground Merchant Portal. |
| production | This environment is for production builds of the app with placement configurations for production merchants. |

### KlarnaOSMRegion

Region enumeration will be used to define which endpoint to connect as a source for the placement configurations.

| **Name** | **Descriptions**                |
|----------|---------------------------------|
| eu       | Region value for Europe.        |
| na       | Region value for North America. |
| oc       | Region value for Oceania.       |

### KlarnaOSMTheme

Theme enumeration will be used to define which style of OSM to be used, depending on either the app’s configuration or the system setting. Each style has a predefined set of values for background color, text color, text size, ... that will be used to style the OSM view.

| **Name** | **Descriptions** |
|----|----|
| light | Light style for placement view. |
| dark | Dark style for placement view. |
| automatic | Automatic theme that will use the system’s user interface style. |

### KlarnaOSMStyleConfiguration

This feature is available from version 2.6.20. By using KlarnaOSMStyleConfiguration you can customize the appearance of the OSM view to some extend. As of now, you can customize the following:

- Background color
- Text color
- Text size
- Text font

Please note that `styleConfiguration` takes precedence over `theme`. This has the following implications:

- If you specify a value thorough `styleConfiguration` (text color, for example) then this value will be used to style the OSM view regardless of the value that `theme` provides.
- If your app supports light and dark mode, then it's your responsibility to update `styleConfiguration` and call the render method when the device's theme changes so that the appearance of the OSM view updates.

To set a custom style for the OSM view you can do like the following:

``` swift
let klarnaOsmStyleConfiguration = KlarnaOSMStyleConfiguration.Builder()
.setBackgroundColor(.white)
.setTextStyleConfiguration(
KlarnaTextStyleConfiguration.Builder()
.setTextColor(.black)
.setTextFont(.systemFont(ofSize: 0.0))
.setTextSize(14.0)
.build()
)
.build()
osmView?.styleConfiguration = klarnaOsmStyleConfiguration
```

## Setting the Parameters

All of the parameters for On-Site Messaging are stored as variables on the KlarnaOSMView instance. The required ones need to be set before calling the render method, otherwise the RenderResult will return a validation error for the missing parameter.

``` swift
osmView.clientId = "<client-id>"
osmView.placementKey = "<placement-key>"
osmView.locale = "en-US"
osmView.purchaseAmount = 1000
osmView.environment = .production
osmView.region = .na
osmView.theme = .dark
osmView.styleConfiguration = ...
osmView.delegate = self
osmView.hostViewController = self
```

## Handling Height Changes

Before rendering the OSM View and displaying its contents, the SDK doesn’t know how the view is integrated in your view hierarchy, so it exposes a ***delegate*** (for SDK versions \&lt;= 2.2.2) and a ***sizingDelegate*** (for SDK versions\&gt; 2.2.2). These delegates inform you about the corresponding size of the OSM View after the render function is called, allowing you to update the UI accordingly with the changes in the OSM view height. Depending on the SDK version you need to set one or the other, **not both**.

### Setting the Delegate

``` swift
osmView.delegate = self
```

The delegate conforms to the protocol ***KlarnaOSMViewEventListener*** that has only the following function to be implemented:

``` swift
func klarnaOSMViewResized(_ height: CGFloat)
```

That is where the calculated height of the OSM View based on the content rendered will be returned, so that your UI can be adjusted with that value.

### Setting the sizingDelegate

``` swift
osmView.sizingDelegate = self
```

This new delegate conforms to the protocol ***KlarnaSizingDelegate*** that has only the following function to be implemented:

``` swift
func klarnaComponent(_ klarnaComponent: KlarnaComponent, resizedToHeight height: CGFloat)
```

This new function will receive two parameters:

- **KlarnaComponent**: Since Klarna offers different components in the SDK, if you are using more than one, it is useful to know which component changed its height.
- **Height**: the final height of the OSMView calculated when the render method is called and returned based on the content.

Inside this method you can adjust your UI with the proper height calculated for the OSM View.

## Rendering the Placement

Once you have set all the parameters to the KlarnaOSMView, you are ready to render the actual placement view. To do that, you need to call the render method of the view with the RenderResult callback parameter. Once the render method is called, first the view will validate all the parameters. If there is a missing parameter the RenderResult callback will be invoked with corresponding error values. If parameters are valid then the view will try to fetch placement configuration from On-Site Messaging API. Any errors or failures from this network request will also invoke RenderResult callback if necessary. If the placement configuration is fetched and valid then the KlarnaOSMView will render it with native views and invoke the RenderResult callback with a null value.

### Calling the Render Method

The RenderResult callback can be used for logging purposes or to make the KlarnaOSMView visible or not, according to the error.

``` swift
osmView.render(callback: { [weak self] error in
...
})
```

## Identifying the Errors

Similar to other parts of the SDK, On-Site Messaging also makes use of the KlarnaMobileSDKError class. To read more about the error handling and error object properties refer to the [On-Site Messaging Error Handling guide](https://docs.klarna.com/conversion-boosters/on-site-messaging/integrate-on-site-messaging/on-site-messaging-for-mobile/).

### Klarna On-Site Messaging Error Names

These are the predefined names for errors that can happen during the placement render flow. These names are available as static String values with typealias KlarnaOSMError.

| **Error Name** | **Description** |
|----|----|
| KlarnaOSMErrorMissingClientId | Client ID was not set. Set the clientId variable and invoke render again. |
| KlarnaOSMErrorMissingPlacementKey | Placement key was not set. Set the placementKey variable and invoke render again. |
| KlarnaOSMErrorMissingRegion | Region was not set. Set the region variable and invoke render again. |
| KlarnaOSMErrorMissingHost | Hosting UIViewController was not set. Set the hostViewController variable and invoke render again. |
| KlarnaOSMErrorInvalidPlacementConfig | Fetched configuration from the API can not be rendered by the native view. |
| KlarnaOSMErrorPlacementError | On-Site Messaging API has returned an error. Message of this error will contain information sent from the API. |
| KlarnaOSMErrorNetworkError | A network error occurred and the placement will not be rendered. |
| KlarnaOSMErrorDisabled | Native On-Site Messaging has been disabled by Klarna, the placement will not be rendered. |</placement-key></client-id>