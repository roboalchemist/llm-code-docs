# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/pay-kit-sdk/pay-kit-android/ui-components.mdx

# Pay Kit Android: UI Components

## Buttons

The Pay Kit SDK provides an unmanaged custom styled `Button`. Cash App provides Jetpack Compose components as well as View-based buttons. The buttons are an **optional** dependency, and must be included separately.

<Note>
  The Button provided by the SDK is unmanaged. It is a stylized button that isn't aware of SDK events out-of-the-box. It is the developer's responsibility to call the above method when the button is clicked and also manage any disabled and loading states.
</Note>

You can change the size of the styled buttons within certain limits.

These limits are:

* at least `34dp` tall
* at least `122dp` wide
* at most `54dp` tall

## Styles

There are four basic static styles that do not change dynamically if your app switches between light and dark mode.

The examples below show the button styles and *disabled* variants.

<img alt="CAP Android Button basic styles" src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/docs/technical-documentation/sdks/pay-kit/cap-android-basic-styles.png" noZoom />

## Jetpack Compose

To add the Jetpack Compose version of the CAP button, use the following implementation:

```
implementation "app.cash.paykit:ui-compose:X.Y.Z"
```

Or via Gradle version catalogs (`libs.toml`):

```
group = "app.cash.paykit", name = "ui-compose"
```

To use the Cash App Pay themed button:

```kotlin
@Composable
fun CashAppPayButton(
  onClick: () -> Unit,
  modifier: Modifier = Modifier,
  style: CashAppPayButtonStyle = CashAppPayButtonStyle.Default,
  enabled: Boolean = true,
)
```

Available `CashAppPayButtonStyle` styles

* `Default` : Polychrome (green) Cash App logo on dark background
* `Alt` : Dark monochrome Cash App logo on green background
* `MonochromeDark` : Light Cash App logo on dark background
* `MonochromeLight` : Dark Cash App logo on light outlined background
* `Monochrome` : Theme-aware monochrome style that automatically picks `MonochromeDark` or `MonochromeLight` based on the app's current UI mode configuration.

## View-based

To add the Views version of the CAP button, use the following:

```
implementation "app.cash.paykit:ui-views:X.Y.Z"
```

Or via Gradle version catalogs (`libs.toml`):

```
group = "app.cash.paykit", name = "ui-views"
```

To use the Cash App Pay light background button:

```xml
<app.cash.paykit.ui.views.CashAppPayButton
    style="@style/CAPButtonStyle.Default"
    android:layout_height="48dp"
    android:layout_marginTop="4dp"
    android:layout_width="match_parent"
    android:layout_marginHorizontal="8dp"
    />
```

Available `CashAppPayButtonStyle` styles:

* `Default` : Polychrome (green) Cash logo on dark background
* `Alt` : Dark monochrome Cash logo on green background
* `MonochromeDark` : Light Cash logo on dark background
* `MonochromeLight` : Dark Cash logo on light outlined background

<Note>
  Use Android's Resource Qualifiers, such as `values-night`, to  provide a button variation that follows the system's theme.
</Note>
