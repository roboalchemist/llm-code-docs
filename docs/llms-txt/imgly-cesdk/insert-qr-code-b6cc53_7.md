# Source: https://img.ly/docs/cesdk/macos/stickers-and-shapes/insert-qr-code-b6cc53/

---
title: "Insert QR Code"
description: "Generate a QR code with Core Image and insert it into a scene as an image fill, with positioning, sizing, and optional metadata for later updates."
platform: macos
url: "https://img.ly/docs/cesdk/macos/stickers-and-shapes/insert-qr-code-b6cc53/"
---

> This is one page of the CE.SDK macOS documentation. For a complete overview, see the [macOS Documentation Index](https://img.ly/docs/cesdk/macos.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/macos/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/macos/guides-8d8b00/) > [Create and Edit Shapes](https://img.ly/docs/cesdk/macos/shapes-9f1b2c/) > [Insert QR Code](https://img.ly/docs/cesdk/macos/stickers-and-shapes/insert-qr-code-b6cc53/)

---

QR codes are a practical way to turn any design into a scannable gateway for:

- Landing pages
- App installs
- Product info
- Event tickets
- You name it

CE.SDK doesn't include a built-in QR generator, but you can create the image with **Core Image** in just a few lines and place it on the canvas as an **image fill**. This guide shows the full workflow with Swift examples.

## What You'll Learn

- Generate a QR code image from a `String` using **Core Image**.
- Add it to a CE.SDK scene as an **image fill** on a shape block.
- Control **size**, **position**, and **color** for brand consistency.
- Store **metadata** for quick regeneration later.

## When You'll Use It

- Business cards, flyers, or packaging that need a **scannable link**.
- Apps that let users personalize templates with their own URLs.
- Automated workflows that embed links into generated designs.

```swift file=@cesdk_swift_examples/engine-guides-shapes-qrcode/QRCodeGenerator.swift reference-only
import CoreImage.CIFilterBuiltins
import IMGLYEngine
import SwiftUI

#if canImport(UIKit)
  import UIKit

  private typealias PlatformColor = UIColor
  private typealias PlatformImage = UIImage
#elseif canImport(AppKit)
  import AppKit

  private typealias PlatformColor = NSColor
  private typealias PlatformImage = NSImage
#endif

struct QRCanvasExampleView: View {
  // CE.SDK
  @State private var engine: Engine?
  @State private var scene: DesignBlockID = 0
  @State private var page: DesignBlockID = 0

  // UI state
  @State private var urlString: String = "https://example.com"

  var body: some View {
    VStack(spacing: 16) {
      // Canvas renders the current engine scene
      Group {
        if let engine {
          Canvas(engine: engine, isPaused: .constant(false))
            .frame(minHeight: 280)
            .clipShape(RoundedRectangle(cornerRadius: 12))
            .overlay(RoundedRectangle(cornerRadius: 12).stroke(Color.secondary.opacity(0.3)))
        } else {
          ZStack {
            RoundedRectangle(cornerRadius: 12).fill(Color.secondary.opacity(0.08))
            Text("Canvas will appear after Engine is created")
              .foregroundColor(.secondary)
              .padding()
          }
          .frame(minHeight: 280)
        }
      }

      // Controls
      VStack(spacing: 12) {
        HStack(spacing: 0) {
          TextField("https://example.com", text: $urlString)
          #if os(iOS)
            .autocapitalization(.none)
            .keyboardType(.URL)
          #endif
            .textFieldStyle(.roundedBorder)
          Spacer()

          Button("Insert QR") { Task { await insertQR() } }
            .disabled(engine == nil || page == 0)
            .padding(.horizontal, 12)
            .padding(.vertical, 8)
            .background(Color.accentColor)
            .foregroundColor(.white)
            .cornerRadius(8)
        }
      }
    }
    .padding()
    .onAppear { Task { await setupEngineIfNeeded() } }
  }

  // MARK: - Engine Setup

  @MainActor
  private func setupEngineIfNeeded() async {
    guard engine == nil else { return }
    do {
      let e = try await Engine(license: "<your license key>")
      engine = e
      let s = try e.scene.create()
      scene = s
      let p = try e.block.create(.page)
      try e.block.appendChild(to: s, child: p)
      page = p
    } catch {
      print("Engine setup error:", error)
    }
  }

  // MARK: - Insert QR

  @MainActor
  private func insertQR() async {
    guard let e = engine, page != 0 else { return }
    do {
      _ = try await insertQRCode(
        engine: e,
        page: page,
        urlString: urlString,
        position: CGPoint(x: 200, y: 200),
        size: 180,
      )
    } catch {
      print("Insert QR failed:", error)
    }
  }
}

// MARK: - QR Generation (Core Image)

/// Generate a QR code with brand colors.
/// - Parameters:
///   - string: Content to encode (use a full URL with scheme).
///   - correction: Error correction level (L, M, Q, H). "M" is a good default.
///   - scale: Pixel scale factor (increase for print).
///   - foreground: Dark module color.
///   - background: Light background color.
private func makeQRCode(
  from string: String,
  correction: String = "M",
  scale: CGFloat = 10,
  foreground: PlatformColor = .black,
  background: PlatformColor = .white,
) -> PlatformImage? {
  guard let data = string.data(using: .utf8) else { return nil }

  let qr = CIFilter.qrCodeGenerator()
  qr.setValue(data, forKey: "inputMessage")
  qr.setValue(correction, forKey: "inputCorrectionLevel")
  guard let output = qr.outputImage else { return nil }

  // Map black/white to brand colors
  let falseColor = CIFilter.falseColor()
  falseColor.inputImage = output
  #if canImport(UIKit)
    falseColor.color0 = CIColor(color: foreground)
    falseColor.color1 = CIColor(color: background)
  #elseif canImport(AppKit)
    falseColor.color0 = CIColor(color: foreground) ?? CIColor.black
    falseColor.color1 = CIColor(color: background) ?? CIColor.white
  #endif
  guard let colored = falseColor.outputImage else { return nil }

  // Scale up without interpolation
  let scaled = colored.transformed(by: CGAffineTransform(scaleX: scale, y: scale))
  let context = CIContext(options: [.useSoftwareRenderer: false])
  guard let cg = context.createCGImage(scaled, from: scaled.extent) else { return nil }

  #if canImport(UIKit)
    return UIImage(cgImage: cg, scale: 1.0, orientation: .up)
  #elseif canImport(AppKit)
    return NSImage(cgImage: cg, size: NSSize(width: cg.width, height: cg.height))
  #endif
}

// MARK: - CE.SDK Block Creation

@MainActor
func insertQRCode(
  engine: Engine,
  page: DesignBlockID,
  urlString: String,
  position: CGPoint = .init(x: 200, y: 200),
  size: CGFloat = 160,
) async throws -> DesignBlockID {
  guard let qr = makeQRCode(from: urlString, correction: "M", scale: 10, foreground: .black, background: .white) else {
    throw NSError(domain: "QR", code: 1, userInfo: [NSLocalizedDescriptionKey: "Failed to generate QR image"])
  }

  // Get PNG data from the image (platform-specific)
  #if canImport(UIKit)
    guard let png = qr.pngData() else {
      throw NSError(domain: "QR", code: 2, userInfo: [NSLocalizedDescriptionKey: "Failed to encode QR as PNG"])
    }
  #elseif canImport(AppKit)
    guard let tiffRepresentation = qr.tiffRepresentation,
          let bitmap = NSBitmapImageRep(data: tiffRepresentation),
          let png = bitmap.representation(using: .png, properties: [:]) else {
      throw NSError(domain: "QR", code: 2, userInfo: [NSLocalizedDescriptionKey: "Failed to encode QR as PNG"])
    }
  #endif

  let fileURL = FileManager.default.temporaryDirectory
    .appendingPathComponent(UUID().uuidString)
    .appendingPathExtension("png")
  try png.write(to: fileURL)

  // Create a visible graphic block with a rect shape
  let graphic = try engine.block.create(.graphic)
  let rectShape = try engine.block.createShape(.rect)
  try engine.block.setShape(graphic, shape: rectShape)

  // Create an image fill and point it to the QR file URL
  let imageFill = try engine.block.createFill(.image)
  try engine.block.setString(imageFill, property: "fill/image/imageFileURI", value: fileURL.absoluteString)
  try engine.block.setFill(graphic, fill: imageFill)

  // Size & position (keep square)
  try engine.block.setWidth(graphic, value: Float(size))
  try engine.block.setHeight(graphic, value: Float(size))
  try engine.block.setPositionX(graphic, value: Float(position.x))
  try engine.block.setPositionY(graphic, value: Float(position.y))

  // Optional metadata for future updates
  try? engine.block.setMetadata(graphic, key: "qr/url", value: urlString)

  // Add to page
  try engine.block.appendChild(to: page, child: graphic)

  return graphic
}

/// Update an existing QR code block with a new URL.
/// - Parameters:
///   - engine: The CE.SDK engine instance.
///   - qrBlock: The existing QR code block to update.
///   - newURL: The new URL to encode.
@MainActor
func updateQRCode(engine: Engine, qrBlock: DesignBlockID, newURL: String) throws {
  guard let qr = makeQRCode(from: newURL) else { return }

  // Get PNG data from the image (platform-specific)
  #if canImport(UIKit)
    guard let png = qr.pngData() else { return }
  #elseif canImport(AppKit)
    guard let tiffRepresentation = qr.tiffRepresentation,
          let bitmap = NSBitmapImageRep(data: tiffRepresentation),
          let png = bitmap.representation(using: .png, properties: [:]) else { return }
  #endif

  let fileURL = FileManager.default.temporaryDirectory
    .appendingPathComponent(UUID().uuidString)
    .appendingPathExtension("png")
  try png.write(to: fileURL)

  let fill = try engine.block.getFill(qrBlock)
  try engine.block.setString(fill, property: "fill/image/imageFileURI", value: fileURL.absoluteString)
  try? engine.block.setMetadata(qrBlock, key: "qr/url", value: newURL)
}

#Preview {
  QRCanvasExampleView()
}
```

## Platform Setup

The example uses type aliases to abstract platform differences between iOS (`UIKit`) and macOS (`AppKit`). `PlatformColor` maps to `UIColor` or `NSColor`, and `PlatformImage` maps to `UIImage` or `NSImage`.

```swift highlight-qr-imports
import CoreImage.CIFilterBuiltins
import IMGLYEngine
import SwiftUI

#if canImport(UIKit)
  import UIKit

  private typealias PlatformColor = UIColor
  private typealias PlatformImage = UIImage
#elseif canImport(AppKit)
  import AppKit

  private typealias PlatformColor = NSColor
  private typealias PlatformImage = NSImage
#endif
```

## Generate a QR Code Image

Use **Core Image** to create a high-resolution QR code, then colorize it to match your brand.

```swift highlight-qr-generate
/// Generate a QR code with brand colors.
/// - Parameters:
///   - string: Content to encode (use a full URL with scheme).
///   - correction: Error correction level (L, M, Q, H). "M" is a good default.
///   - scale: Pixel scale factor (increase for print).
///   - foreground: Dark module color.
///   - background: Light background color.
private func makeQRCode(
  from string: String,
  correction: String = "M",
  scale: CGFloat = 10,
  foreground: PlatformColor = .black,
  background: PlatformColor = .white,
) -> PlatformImage? {
  guard let data = string.data(using: .utf8) else { return nil }

  let qr = CIFilter.qrCodeGenerator()
  qr.setValue(data, forKey: "inputMessage")
  qr.setValue(correction, forKey: "inputCorrectionLevel")
  guard let output = qr.outputImage else { return nil }

  // Map black/white to brand colors
  let falseColor = CIFilter.falseColor()
  falseColor.inputImage = output
  #if canImport(UIKit)
    falseColor.color0 = CIColor(color: foreground)
    falseColor.color1 = CIColor(color: background)
  #elseif canImport(AppKit)
    falseColor.color0 = CIColor(color: foreground) ?? CIColor.black
    falseColor.color1 = CIColor(color: background) ?? CIColor.white
  #endif
  guard let colored = falseColor.outputImage else { return nil }

  // Scale up without interpolation
  let scaled = colored.transformed(by: CGAffineTransform(scaleX: scale, y: scale))
  let context = CIContext(options: [.useSoftwareRenderer: false])
  guard let cg = context.createCGImage(scaled, from: scaled.extent) else { return nil }

  #if canImport(UIKit)
    return UIImage(cgImage: cg, scale: 1.0, orientation: .up)
  #elseif canImport(AppKit)
    return NSImage(cgImage: cg, size: NSSize(width: cg.width, height: cg.height))
  #endif
}
```

Keep the foreground dark and the background light for reliable scanning.

## Insert the QR as an Image Fill

Create a `graphic` block, assign it a `rect` shape, and fill it with your generated QR image.

```swift highlight-qr-insert
@MainActor
func insertQRCode(
  engine: Engine,
  page: DesignBlockID,
  urlString: String,
  position: CGPoint = .init(x: 200, y: 200),
  size: CGFloat = 160,
) async throws -> DesignBlockID {
  guard let qr = makeQRCode(from: urlString, correction: "M", scale: 10, foreground: .black, background: .white) else {
    throw NSError(domain: "QR", code: 1, userInfo: [NSLocalizedDescriptionKey: "Failed to generate QR image"])
  }

  // Get PNG data from the image (platform-specific)
  #if canImport(UIKit)
    guard let png = qr.pngData() else {
      throw NSError(domain: "QR", code: 2, userInfo: [NSLocalizedDescriptionKey: "Failed to encode QR as PNG"])
    }
  #elseif canImport(AppKit)
    guard let tiffRepresentation = qr.tiffRepresentation,
          let bitmap = NSBitmapImageRep(data: tiffRepresentation),
          let png = bitmap.representation(using: .png, properties: [:]) else {
      throw NSError(domain: "QR", code: 2, userInfo: [NSLocalizedDescriptionKey: "Failed to encode QR as PNG"])
    }
  #endif

  let fileURL = FileManager.default.temporaryDirectory
    .appendingPathComponent(UUID().uuidString)
    .appendingPathExtension("png")
  try png.write(to: fileURL)

  // Create a visible graphic block with a rect shape
  let graphic = try engine.block.create(.graphic)
  let rectShape = try engine.block.createShape(.rect)
  try engine.block.setShape(graphic, shape: rectShape)

  // Create an image fill and point it to the QR file URL
  let imageFill = try engine.block.createFill(.image)
  try engine.block.setString(imageFill, property: "fill/image/imageFileURI", value: fileURL.absoluteString)
  try engine.block.setFill(graphic, fill: imageFill)

  // Size & position (keep square)
  try engine.block.setWidth(graphic, value: Float(size))
  try engine.block.setHeight(graphic, value: Float(size))
  try engine.block.setPositionX(graphic, value: Float(position.x))
  try engine.block.setPositionY(graphic, value: Float(position.y))

  // Optional metadata for future updates
  try? engine.block.setMetadata(graphic, key: "qr/url", value: urlString)

  // Add to page
  try engine.block.appendChild(to: page, child: graphic)

  return graphic
}
```

The preceding code creates a QR code and then saves it to a temporary directory to generate a file URL the block can use.

## Add Optional Metadata

Store the URL alongside the block for quick updates later. Metadata `key` values are anything you want. The `key` and the `value` must be `String` types.

```swift highlight-qr-metadata
// Optional metadata for future updates
try? engine.block.setMetadata(graphic, key: "qr/url", value: urlString)
```

## Update an Existing QR Code

If data changes, just regenerate the QR image and update the fill URI.

```swift highlight-qr-update
/// Update an existing QR code block with a new URL.
/// - Parameters:
///   - engine: The CE.SDK engine instance.
///   - qrBlock: The existing QR code block to update.
///   - newURL: The new URL to encode.
@MainActor
func updateQRCode(engine: Engine, qrBlock: DesignBlockID, newURL: String) throws {
  guard let qr = makeQRCode(from: newURL) else { return }

  // Get PNG data from the image (platform-specific)
  #if canImport(UIKit)
    guard let png = qr.pngData() else { return }
  #elseif canImport(AppKit)
    guard let tiffRepresentation = qr.tiffRepresentation,
          let bitmap = NSBitmapImageRep(data: tiffRepresentation),
          let png = bitmap.representation(using: .png, properties: [:]) else { return }
  #endif

  let fileURL = FileManager.default.temporaryDirectory
    .appendingPathComponent(UUID().uuidString)
    .appendingPathExtension("png")
  try png.write(to: fileURL)

  let fill = try engine.block.getFill(qrBlock)
  try engine.block.setString(fill, property: "fill/image/imageFileURI", value: fileURL.absoluteString)
  try? engine.block.setMetadata(qrBlock, key: "qr/url", value: newURL)
}
```

To generate many QR codes, for instance during a batch run, loop through your data and call `insertQRCode` for each.

## Troubleshooting

| Symptom | Cause | Solution |
|----------|--------|-----------|
| QR looks blurry | Image scaled too small | Increase the Core Image `scale` and block size. |
| QR won't scan | Low contrast or invalid URL | Use dark-on-light colors and percent-encode URLs. |
| QR not visible | Shape missing from block | Call `setShape` before applying the fill. |
| App crash writing file | Invalid temp URL | Always use `FileManager.default.temporaryDirectory`. |

## Next Steps

Now that you can generate QR codes, here are some related guides to help you learn more. Explore a complete code sample on [GitHub](https://github.com/imgly/cesdk-swift-examples/tree/v$UBQ_VERSION$/engine-guides-shapes-qrcode).

- [Insert Shapes or Stickers](https://img.ly/docs/cesdk/macos/insert-media/shapes-or-stickers-20ac68/) — Learn how fills and shapes interact.
- [Batch Processing](https://img.ly/docs/cesdk/macos/automation/batch-processing-ab2d18/) — Automate multiple QR insertions.
- [Export to PDF](https://img.ly/docs/cesdk/macos/export-save-publish/export/to-pdf-95e04b/) — Prepare print-ready designs.
- [Use Templates: Overview](https://img.ly/docs/cesdk/macos/create-templates/overview-4ebe30/) — Add a placeholder for QR blocks in templates.



---

## More Resources

- **[macOS Documentation Index](https://img.ly/docs/cesdk/macos.md)** - Browse all macOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/macos/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/macos/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
