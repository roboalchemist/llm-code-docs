# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.md.txt

# FirebaseVisionBarcode

public class **FirebaseVisionBarcode** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
**This class is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).

Represents a single recognized barcode and its value.

The barcode's raw, unmodified, and uninterpreted content is returned in the [getRawValue()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getRawValue()) field, while the barcode type (i.e. its encoding) can be found in
the [getFormat()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getFormat()) field.  

### Nested Class Summary

|------------|---|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| class      | [FirebaseVisionBarcode.Address](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Address) || An address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| @interface | [FirebaseVisionBarcode.BarcodeFormat](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.BarcodeFormat) || Barcode format constants - enumeration of supported barcode formats.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| @interface | [FirebaseVisionBarcode.BarcodeValueType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.BarcodeValueType) || Barcode value type constants - enumeration of supported barcode content value types Supported types include: 1. [TYPE_UNKNOWN](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_UNKNOWN) 2. [TYPE_CONTACT_INFO](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_CONTACT_INFO) 3. [TYPE_EMAIL](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_EMAIL) 4. [TYPE_ISBN](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_ISBN) 5. [TYPE_PHONE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_PHONE) 6. [TYPE_PRODUCT](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_PRODUCT) 7. [TYPE_SMS](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_SMS) 8. [TYPE_TEXT](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_TEXT) 9. [TYPE_URL](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_URL) 10. [TYPE_WIFI](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_WIFI) 11. [TYPE_GEO](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_GEO) 12. [TYPE_CALENDAR_EVENT](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_CALENDAR_EVENT) 13. [TYPE_DRIVER_LICENSE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_DRIVER_LICENSE) |
| class      | [FirebaseVisionBarcode.CalendarDateTime](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.CalendarDateTime) || DateTime data type used in calendar events.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| class      | [FirebaseVisionBarcode.CalendarEvent](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.CalendarEvent) || A calendar event extracted from QRCode.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| class      | [FirebaseVisionBarcode.ContactInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.ContactInfo) || A person's or organization's business card.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| class      | [FirebaseVisionBarcode.DriverLicense](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.DriverLicense) || A driver license or ID card.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| class      | [FirebaseVisionBarcode.Email](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Email) || An email message from a 'MAILTO:' or similar QRCode type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| class      | [FirebaseVisionBarcode.GeoPoint](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.GeoPoint) || GPS coordinates from a 'GEO:' or similar QRCode type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| class      | [FirebaseVisionBarcode.PersonName](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.PersonName) || A person's name, both formatted version and individual name components.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| class      | [FirebaseVisionBarcode.Phone](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Phone) || Phone number info.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| class      | [FirebaseVisionBarcode.Sms](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Sms) || A sms message from a 'SMS:' or similar QRCode type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| class      | [FirebaseVisionBarcode.UrlBookmark](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.UrlBookmark) || A URL and title from a 'MEBKM:' or similar QRCode type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| class      | [FirebaseVisionBarcode.WiFi](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.WiFi) || A wifi network parameters from a 'WIFI:' or similar QRCode type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

### Constant Summary

|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| int | [FORMAT_ALL_FORMATS](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#FORMAT_ALL_FORMATS)   | Barcode format constant representing the union of all supported formats.                                              |
| int | [FORMAT_AZTEC](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#FORMAT_AZTEC)               | Barcode format constant for AZTEC.                                                                                    |
| int | [FORMAT_CODABAR](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#FORMAT_CODABAR)           | Barcode format constant for Codabar.                                                                                  |
| int | [FORMAT_CODE_128](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#FORMAT_CODE_128)         | Barcode format constant for Code 128.                                                                                 |
| int | [FORMAT_CODE_39](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#FORMAT_CODE_39)           | Barcode format constant for Code 39.                                                                                  |
| int | [FORMAT_CODE_93](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#FORMAT_CODE_93)           | Barcode format constant for Code 93.                                                                                  |
| int | [FORMAT_DATA_MATRIX](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#FORMAT_DATA_MATRIX)   | Barcode format constant for Data Matrix.                                                                              |
| int | [FORMAT_EAN_13](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#FORMAT_EAN_13)             | Barcode format constant for EAN-13.                                                                                   |
| int | [FORMAT_EAN_8](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#FORMAT_EAN_8)               | Barcode format constant for EAN-8.                                                                                    |
| int | [FORMAT_ITF](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#FORMAT_ITF)                   | Barcode format constant for ITF (Interleaved Two-of-Five).                                                            |
| int | [FORMAT_PDF417](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#FORMAT_PDF417)             | Barcode format constant for PDF-417.                                                                                  |
| int | [FORMAT_QR_CODE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#FORMAT_QR_CODE)           | Barcode format constant for QR Code.                                                                                  |
| int | [FORMAT_UNKNOWN](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#FORMAT_UNKNOWN)           | Barcode format unknown to the current SDK.                                                                            |
| int | [FORMAT_UPC_A](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#FORMAT_UPC_A)               | Barcode format constant for UPC-A.                                                                                    |
| int | [FORMAT_UPC_E](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#FORMAT_UPC_E)               | Barcode format constant for UPC-E.                                                                                    |
| int | [TYPE_CALENDAR_EVENT](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_CALENDAR_EVENT) | Barcode value type constant for calendar events.                                                                      |
| int | [TYPE_CONTACT_INFO](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_CONTACT_INFO)     | Barcode value type constant for contact information.                                                                  |
| int | [TYPE_DRIVER_LICENSE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_DRIVER_LICENSE) | Barcode value type constant for driver's license data.                                                                |
| int | [TYPE_EMAIL](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_EMAIL)                   | Barcode value type constant for email message details.                                                                |
| int | [TYPE_GEO](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_GEO)                       | Barcode value type constant for geographic coordinates.                                                               |
| int | [TYPE_ISBN](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_ISBN)                     | Barcode value type constant for ISBNs.                                                                                |
| int | [TYPE_PHONE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_PHONE)                   | Barcode value type constant for phone numbers.                                                                        |
| int | [TYPE_PRODUCT](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_PRODUCT)               | Barcode value type constant for product codes.                                                                        |
| int | [TYPE_SMS](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_SMS)                       | Barcode value type constant for SMS details.                                                                          |
| int | [TYPE_TEXT](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_TEXT)                     | Barcode value type constant for plain text.                                                                           |
| int | [TYPE_UNKNOWN](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_UNKNOWN)               | Barcode value type unknown, which indicates the current version of SDK cannot recognize the structure of the barcode. |
| int | [TYPE_URL](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_URL)                       | Barcode value type constant for URLs/bookmarks.                                                                       |
| int | [TYPE_WIFI](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_WIFI)                     | Barcode value type constant for WiFi access point details.                                                            |

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Rect](https://developer.android.com/reference/android/graphics/Rect.html)                                                                                          | [getBoundingBox](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getBoundingBox())() Gets the bounding rectangle of the detected barcode.                                                                                                                                                                                                                                                                                                             |
| [FirebaseVisionBarcode.CalendarEvent](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.CalendarEvent) | [getCalendarEvent](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getCalendarEvent())() Gets parsed calendar event details (set iff [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) is [TYPE_CALENDAR_EVENT](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_CALENDAR_EVENT)).   |
| [FirebaseVisionBarcode.ContactInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.ContactInfo)     | [getContactInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getContactInfo())() Gets parsed contact details (set iff [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) is [TYPE_CONTACT_INFO](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_CONTACT_INFO)).                  |
| [Point\[\]](https://developer.android.com/reference/android/graphics/Point.html)                                                                                    | [getCornerPoints](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getCornerPoints())() Returns four corner points in clockwise direction starting with top-left.                                                                                                                                                                                                                                                                                      |
| [String](https://developer.android.com/reference/java/lang/String.html)                                                                                             | [getDisplayValue](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getDisplayValue())() Returns barcode value in a user-friendly format.                                                                                                                                                                                                                                                                                                               |
| [FirebaseVisionBarcode.DriverLicense](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.DriverLicense) | [getDriverLicense](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getDriverLicense())() Gets parsed driver's license details (set iff [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) is [TYPE_DRIVER_LICENSE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_DRIVER_LICENSE)). |
| [FirebaseVisionBarcode.Email](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Email)                 | [getEmail](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getEmail())() Gets parsed email details (set iff [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) is [TYPE_EMAIL](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_EMAIL)).                                              |
| int                                                                                                                                                                 | [getFormat](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getFormat())() Returns barcode format, for example [FORMAT_EAN_13](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#FORMAT_EAN_13).                                                                                                                                                                                         |
| [FirebaseVisionBarcode.GeoPoint](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.GeoPoint)           | [getGeoPoint](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getGeoPoint())() Gets parsed geo coordinates (set iff [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) is [TYPE_GEO](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_GEO)).                                          |
| [FirebaseVisionBarcode.Phone](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Phone)                 | [getPhone](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getPhone())() Gets parsed phone details (set iff [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) is [TYPE_PHONE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_PHONE)).                                              |
| byte\[\]                                                                                                                                                            | [getRawBytes](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getRawBytes())() Returns raw bytes as it was encoded in the barcode.                                                                                                                                                                                                                                                                                                                    |
| [String](https://developer.android.com/reference/java/lang/String.html)                                                                                             | [getRawValue](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getRawValue())() Returns barcode value as it was encoded in the barcode.                                                                                                                                                                                                                                                                                                                |
| [FirebaseVisionBarcode.Sms](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Sms)                     | [getSms](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getSms())() Gets parsed SMS details (set iff [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) is [TYPE_SMS](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_SMS)).                                                        |
| [FirebaseVisionBarcode.UrlBookmark](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.UrlBookmark)     | [getUrl](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getUrl())() Gets parsed URL bookmark details (set iff [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) is [TYPE_URL](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_URL)).                                               |
| int                                                                                                                                                                 | [getValueType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType())() Returns format type of the barcode value.                                                                                                                                                                                                                                                                                                                            |
| [FirebaseVisionBarcode.WiFi](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.WiFi)                   | [getWifi](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getWifi())() Gets parsed WiFi AP details (set iff [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) is [TYPE_WIFI](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_WIFI)).                                                |

### Inherited Method Summary

From class java.lang.Object  

|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [Object](https://developer.android.com/reference/java/lang/Object.html)          | clone()                                                                              |
| boolean                                                                          | equals([Object](https://developer.android.com/reference/java/lang/Object.html) arg0) |
| void                                                                             | finalize()                                                                           |
| final [Class](https://developer.android.com/reference/java/lang/Class.html)\<?\> | getClass()                                                                           |
| int                                                                              | hashCode()                                                                           |
| final void                                                                       | notify()                                                                             |
| final void                                                                       | notifyAll()                                                                          |
| [String](https://developer.android.com/reference/java/lang/String.html)          | toString()                                                                           |
| final void                                                                       | wait(long arg0, int arg1)                                                            |
| final void                                                                       | wait(long arg0)                                                                      |
| final void                                                                       | wait()                                                                               |

## Constants

#### public static final int
**FORMAT_ALL_FORMATS**

Barcode format constant representing the union of all supported formats. Pass into
[setBarcodeFormats(int, int...)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions.Builder#setBarcodeFormats(int, int...)) to select formats to recognize. This is also
the default setting.  
Constant Value: 0  

#### public static final int
**FORMAT_AZTEC**

Barcode format constant for AZTEC.

Pass into [setBarcodeFormats(int, int...)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions.Builder#setBarcodeFormats(int, int...)) to select formats to recognize, and also
specifies a detected Barcode's format via the [getFormat()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getFormat()) field.  
Constant Value: 4096  

#### public static final int
**FORMAT_CODABAR**

Barcode format constant for Codabar.

Pass into [setBarcodeFormats(int, int...)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions.Builder#setBarcodeFormats(int, int...)) to select formats to recognize, and also
specifies a detected Barcode's format via the [getFormat()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getFormat()) field.  
Constant Value: 8  

#### public static final int
**FORMAT_CODE_128**

Barcode format constant for Code 128.

Pass into [setBarcodeFormats(int, int...)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions.Builder#setBarcodeFormats(int, int...)) to select formats to recognize, and also
specifies a detected Barcode's format via the [getFormat()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getFormat()) field.  
Constant Value: 1  

#### public static final int
**FORMAT_CODE_39**

Barcode format constant for Code 39.

Pass into [setBarcodeFormats(int, int...)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions.Builder#setBarcodeFormats(int, int...)) to select formats to recognize, and also
specifies a detected Barcode's format via the [getFormat()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getFormat()) field.  
Constant Value: 2  

#### public static final int
**FORMAT_CODE_93**

Barcode format constant for Code 93.

Pass into [setBarcodeFormats(int, int...)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions.Builder#setBarcodeFormats(int, int...)) to select formats to recognize, and also
specifies a detected Barcode's format via the [getFormat()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getFormat()) field.  
Constant Value: 4  

#### public static final int
**FORMAT_DATA_MATRIX**

Barcode format constant for Data Matrix.

Pass into [setBarcodeFormats(int, int...)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions.Builder#setBarcodeFormats(int, int...)) to select formats to recognize, and also
specifies a detected Barcode's format via the [getFormat()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getFormat()) field.  
Constant Value: 16  

#### public static final int
**FORMAT_EAN_13**

Barcode format constant for EAN-13.

Pass into [setBarcodeFormats(int, int...)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions.Builder#setBarcodeFormats(int, int...)) to select formats to recognize, and also
specifies a detected Barcode's format via the [getFormat()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getFormat()) field.  
Constant Value: 32  

#### public static final int
**FORMAT_EAN_8**

Barcode format constant for EAN-8.

Pass into [setBarcodeFormats(int, int...)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions.Builder#setBarcodeFormats(int, int...)) to select formats to recognize, and also
specifies a detected Barcode's format via the [getFormat()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getFormat()) field.  
Constant Value: 64  

#### public static final int
**FORMAT_ITF**

Barcode format constant for ITF (Interleaved Two-of-Five).

Pass into [setBarcodeFormats(int, int...)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions.Builder#setBarcodeFormats(int, int...)) to select formats to recognize, and also
specifies a detected Barcode's format via the [getFormat()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getFormat()) field.  
Constant Value: 128  

#### public static final int
**FORMAT_PDF417**

Barcode format constant for PDF-417.

Pass into [setBarcodeFormats(int, int...)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions.Builder#setBarcodeFormats(int, int...)) to select formats to recognize, and also
specifies a detected Barcode's format via the [getFormat()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getFormat()) field.  
Constant Value: 2048  

#### public static final int
**FORMAT_QR_CODE**

Barcode format constant for QR Code.

Pass into [setBarcodeFormats(int, int...)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions.Builder#setBarcodeFormats(int, int...)) to select formats to recognize, and also
specifies a detected Barcode's format via the [getFormat()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getFormat()) field.  
Constant Value: 256  

#### public static final int
**FORMAT_UNKNOWN**

Barcode format unknown to the current SDK.  
Constant Value: -1  

#### public static final int
**FORMAT_UPC_A**

Barcode format constant for UPC-A.

Pass into [setBarcodeFormats(int, int...)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions.Builder#setBarcodeFormats(int, int...)) to select formats to recognize, and also
specifies a detected Barcode's format via the [getFormat()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getFormat()) field.  
Constant Value: 512  

#### public static final int
**FORMAT_UPC_E**

Barcode format constant for UPC-E.

Pass into [setBarcodeFormats(int, int...)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions.Builder#setBarcodeFormats(int, int...)) to select formats to recognize, and also
specifies a detected Barcode's format via the [getFormat()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getFormat()) field.  
Constant Value: 1024  

#### public static final int
**TYPE_CALENDAR_EVENT**

Barcode value type constant for calendar events. Specifies the format of a Barcode
value via the [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) field.  
Constant Value: 11  

#### public static final int
**TYPE_CONTACT_INFO**

Barcode value type constant for contact information. Specifies the format of a
Barcode value via the [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) field.  
Constant Value: 1  

#### public static final int
**TYPE_DRIVER_LICENSE**

Barcode value type constant for driver's license data. Specifies the format of a
Barcode value via the [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) field.  
Constant Value: 12  

#### public static final int
**TYPE_EMAIL**

Barcode value type constant for email message details. Specifies the format of a
Barcode value via the [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) field.  
Constant Value: 2  

#### public static final int
**TYPE_GEO**

Barcode value type constant for geographic coordinates. Specifies the format of a
Barcode value via the [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) field.  
Constant Value: 10  

#### public static final int
**TYPE_ISBN**

Barcode value type constant for ISBNs. Specifies the format of a Barcode value via
the [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) field.  
Constant Value: 3  

#### public static final int
**TYPE_PHONE**

Barcode value type constant for phone numbers. Specifies the format of a Barcode
value via the [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) field.  
Constant Value: 4  

#### public static final int
**TYPE_PRODUCT**

Barcode value type constant for product codes. Specifies the format of a Barcode
value via the [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) field.  
Constant Value: 5  

#### public static final int
**TYPE_SMS**

Barcode value type constant for SMS details. Specifies the format of a Barcode value
via the [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) field.  
Constant Value: 6  

#### public static final int
**TYPE_TEXT**

Barcode value type constant for plain text. Specifies the format of a Barcode value
via the [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) field.  
Constant Value: 7  

#### public static final int
**TYPE_UNKNOWN**

Barcode value type unknown, which indicates the current version of SDK cannot
recognize the structure of the barcode. Developers can inspect the raw value
instead.  
Constant Value: 0  

#### public static final int
**TYPE_URL**

Barcode value type constant for URLs/bookmarks. Specifies the format of a Barcode
value via the [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) field.  
Constant Value: 8  

#### public static final int
**TYPE_WIFI**

Barcode value type constant for WiFi access point details. Specifies the format of a
Barcode value via the [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) field.  
Constant Value: 9

## Public Methods

#### public [Rect](https://developer.android.com/reference/android/graphics/Rect.html) **getBoundingBox** ()

Gets the bounding rectangle of the detected barcode.

Returns null if the bounding rectangle can not be determined.  

#### public [FirebaseVisionBarcode.CalendarEvent](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.CalendarEvent) **getCalendarEvent** ()

Gets parsed calendar event details (set iff [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) is [TYPE_CALENDAR_EVENT](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_CALENDAR_EVENT)).  

#### public [FirebaseVisionBarcode.ContactInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.ContactInfo) **getContactInfo** ()

Gets parsed contact details (set iff [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) is [TYPE_CONTACT_INFO](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_CONTACT_INFO)).  

#### public [Point\[\]](https://developer.android.com/reference/android/graphics/Point.html)
**getCornerPoints** ()

Returns four corner points in clockwise direction starting with top-left.

Due to the possible perspective distortions, this is not necessarily a
rectangle.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getDisplayValue** ()

Returns barcode value in a user-friendly format. May omit some of the information
encoded in the barcode. For example, if [getRawValue()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getRawValue()) returns
`'MEBKM:TITLE:Google;URL://www.google.com;;'`, the display_value might be
`'//www.google.com'`. If valueFormat==TEXT, this field will be equal to
[getRawValue()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getRawValue()). This value may be multiline, for example, when line breaks
are encoded into the original TEXT barcode value. May include the supplement value.

Returns `null` if nothing found.  

#### public [FirebaseVisionBarcode.DriverLicense](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.DriverLicense) **getDriverLicense** ()

Gets parsed driver's license details (set iff [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) is [TYPE_DRIVER_LICENSE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_DRIVER_LICENSE)).  

#### public [FirebaseVisionBarcode.Email](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Email) **getEmail** ()

Gets parsed email details (set iff [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) is [TYPE_EMAIL](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_EMAIL)).  

#### public int **getFormat** ()

Returns barcode format, for example [FORMAT_EAN_13](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#FORMAT_EAN_13).  

#### public [FirebaseVisionBarcode.GeoPoint](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.GeoPoint) **getGeoPoint** ()

Gets parsed geo coordinates (set iff [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) is [TYPE_GEO](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_GEO)).  

#### public [FirebaseVisionBarcode.Phone](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Phone) **getPhone** ()

Gets parsed phone details (set iff [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) is [TYPE_PHONE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_PHONE)).  

#### public byte\[\] **getRawBytes** ()

Returns raw bytes as it was encoded in the barcode.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getRawValue** ()

Returns barcode value as it was encoded in the barcode. Structured values are not
parsed, for example: `'MEBKM:TITLE:Google;URL://www.google.com;;'`.

It's only available when the barcode is encoded in the UTF-8 format, and for
non-UTF8 ones use [getRawBytes()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getRawBytes()) instead.  

#### public [FirebaseVisionBarcode.Sms](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.Sms) **getSms**
()

Gets parsed SMS details (set iff [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) is [TYPE_SMS](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_SMS)).  

#### public [FirebaseVisionBarcode.UrlBookmark](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.UrlBookmark) **getUrl** ()

Gets parsed URL bookmark details (set iff [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) is [TYPE_URL](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_URL)).  

#### public int **getValueType** ()

Returns format type of the barcode value.

For example, [TYPE_TEXT](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_TEXT), [TYPE_PRODUCT](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_PRODUCT), [TYPE_URL](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_URL), etc.

If the value structure cannot be parsed, [TYPE_TEXT](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_TEXT) will be returned. If the recognized structure type is not defined
in your current version of SDK, [TYPE_UNKNOWN](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_UNKNOWN) will be returned.

Note that the built-in parsers only recognize a few popular value structures. For
your specific use case, you might want to directly consume [getRawValue()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getRawValue()) and implement your own parsing logic.  

#### public [FirebaseVisionBarcode.WiFi](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.WiFi) **getWifi**
()

Gets parsed WiFi AP details (set iff [getValueType()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#getValueType()) is [TYPE_WIFI](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode#TYPE_WIFI)).