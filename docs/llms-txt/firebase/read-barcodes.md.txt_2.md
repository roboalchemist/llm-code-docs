# Source: https://firebase.google.com/docs/ml-kit/read-barcodes.md.txt

# Barcode Scanning

> [!CAUTION]
> This page describes an old version of the Barcode Scanning API, which was part
> of ML Kit for Firebase. Development of this API has been moved to the
> standalone ML Kit SDK, which you can use with or without Firebase.
> [Learn more](https://developers.google.com/ml-kit/migration).
>
> See
> [Barcode Scanning](https://developers.google.com/ml-kit/vision/barcode-scanning)
> for the latest documentation.

![](https://firebase.google.com/static/docs/ml-kit/images/barcode_scanning@2x.png)

With ML Kit's barcode scanning API, you can read data encoded using most
standard barcode formats. Barcode scanning happens on the device, and doesn't
require a network connection.

Barcodes are a convenient way to pass information from the real world to your
app. In particular, when using 2D formats such as QR code, you can encode
structured data such as contact information or WiFi network credentials. Because
ML Kit can automatically recognize and parse this data, your app can respond
intelligently when a user scans a barcode.

[iOS](https://firebase.google.com/docs/ml-kit/ios/read-barcodes)
[Android](https://firebase.google.com/docs/ml-kit/android/read-barcodes)

If you're a Flutter developer, you might be interested in
[FlutterFire](https://github.com/FirebaseExtended/flutterfire/tree/master/packages/firebase_ml_vision),
which includes a plugin for Firebase's ML Vision APIs.
This is a beta release of ML Kit for Firebase. This API might be changed in backward-incompatible ways and is not subject to any SLA or deprecation policy.

## Key capabilities

|---|---|
| Reads most standard formats | - Linear formats: Codabar, Code 39, Code 93, Code 128, EAN-8, EAN-13, ITF, UPC-A, UPC-E - 2D formats: Aztec, Data Matrix, PDF417, QR Code |
| Automatic format detection | Scan for all supported barcode formats at once, without having to specify the format you're looking for. Or, boost scanning speed by restricting the detector to only the formats you're interested in. |
| Extracts structured data | Structured data stored using one of the supported 2D formats are automatically parsed. Supported information types include URLs, contact information, calendar events, email addresses, phone numbers, SMS message prompts, ISBNs, WiFi connection information, geographic location, and AAMVA-standard driver information. |
| Works with any orientation | Barcodes are recognized and scanned regardless of their orientation: right-side-up, upside-down, or sideways. |
| Runs on the device | Barcode scanning is performed completely on the device, and doesn't require a network connection. |

## Example results

|---|---|
| ![](https://firebase.google.com/static/docs/ml-kit/images/examples/EAN-Obst.jpg) | | Result || |---|---| | **Corners** | (49,125), (172,125), (172,160), (49,160) | | **Raw value** | 2404105001722 | |

|---|---|
| ![](https://firebase.google.com/static/docs/ml-kit/images/examples/qrcode.png) | | Result || |---|---| | **Corners** | (87,87) (612,87) (612,612) (87,612) | | **Raw value** | `WIFI:S:SB1Guest;P:12345;T:WEP;;` | | **WiFi information** | |---|---| | **SSID** | SB1Guest | | **Password** | 12345 | | **Type** | WEP | | |