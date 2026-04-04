# Source: https://docs.buildnatively.com/guides/integration/scanner-qr-barcode.md

# Scanner (QR/Barcode)

* [Bubble.io Plugin](#bubble.io-plugin)
* [JavaScript SDK](#javascript-sdk)

Supported QR/Barcode formats:

| 1D product            | 1D industrial | 2D           |
| --------------------- | ------------- | ------------ |
| UPC-A                 | Code 39       | QR Code      |
| UPC-E                 | Code 93       | Data Matrix  |
| EAN-8                 | Code 128      | Aztec        |
| EAN-13                | Codabar       | PDF 417      |
| UPC/EAN Extension 2/5 | ITF           | MaxiCode     |
|                       |               | RSS-14       |
|                       |               | RSS-Expanded |

{% hint style="info" %}
The number of symbols in a barcode directly impacts the camera resolution required to scan it successfully. Barcodes with a higher density of symbols will generally need a higher resolution camera for accurate reading.
{% endhint %}

### 🧋 Bubble.io Plugin

#### \[Element] Natively - Scanner (QR/Barcode Scanner)

#### Events:

* Scanner Result Updated

#### States:

* Scanner Result - text

#### Actions:

* Show Scanner

### 🛠 JavaScript SDK

#### NativelyScanner

{% code overflow="wrap" lineNumbers="true" %}

```javascript
const scanner = new NativelyScanner()
const open_scanner_callback = function (resp) {
    console.log(resp.result); // result as string representation
};
scanner.showScanner(open_scanner_callback);
```

{% endcode %}
