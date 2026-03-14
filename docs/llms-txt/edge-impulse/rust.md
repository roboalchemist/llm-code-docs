# Source: https://docs.edgeimpulse.com/tools/libraries/sdks/inference/linux/rust.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Linux Rust SDK

<Frame caption="Edge Impulse - rust api guide">
  <img src="https://mintcdn.com/edgeimpulse/BCrJzLAs8FGQ0Eny/.assets/images/rust/rust-api-guide.png?fit=max&auto=format&n=BCrJzLAs8FGQ0Eny&q=85&s=f25e13e6514c6a5f74e3a7052b10bde7" width="1051" height="1000" data-path=".assets/images/rust/rust-api-guide.png" />
</Frame>

This library lets you run machine learning models and collect sensor data on [Linux and macOS](/tools/libraries/sdks/inference/linux) machines using Rust. The SDK is open source and hosted on GitHub:

The Edge Impulse Rust SDK (via the edge\_impulse\_runner crate) provides safe, high-performance Rust bindings for running Edge Impulse models and uploading data on Linux and macOS. This library handles everything from model inference to sensor data ingestion, enabling seamless development of real-time and resource-efficient edge AI solutions.

## Overview

The Edge Impulse Rust library enables developers to seamlessly run Edge Impulse models in Rust projects, offering robust performance, safety, and ergonomics.

## Installation

To install the Edge Impulse Rust library, add the following dependency to your `Cargo.toml`:

```toml  theme={"system"}
[dependencies]
edge_impulse_runner = "1.0.0"
```

## Key Features

### Model Inference

Effortlessly run `.eim` models for:

* **Classification**
* **Object Detection**
* **Visual Anomaly Detection**

### Sensor Integration

Native support for:

* **Camera**
* **Microphone**

### Data Ingestion

Directly upload sensor data to Edge Impulse using the built-in Ingestion API.

### Continuous Classification

Execute models in continuous inference mode for real-time predictions.

## Quickstart Example

Here’s a simple example to perform classification using an Edge Impulse model:

```rust  theme={"system"}
use edge_impulse_runner::{EimModel, SensorType, InferenceResult};

fn main() -> Result<(), Box<dyn std::error::Error>> {
  let mut model = EimModel::new("path/to/model.eim")?;

  // Get model parameters
  let params = model.parameters()?;
  println!("Model type: {}", params.model_type);

  // Determine sensor type
  match model.sensor_type()? {
    SensorType::Camera => println!("Camera model"),
    SensorType::Microphone => println!("Audio model"),
    SensorType::Accelerometer => println!("Motion model"),
    SensorType::Positional => println!("Position model"),
    SensorType::Other => println!("Other sensor type"),
  }

  // Normalize and prepare input features
  let raw_features = vec![128, 128, 128];
  let features: Vec<f32> = raw_features.into_iter().map(|x| x as f32 / 255.0).collect();

  // Execute inference
  let result = model.infer(features, None)?;

  // Process inference results
  match result.result {
    InferenceResult::Classification { classification } => {
      for (label, probability) in classification {
        println!("{}: {:.2}", label, probability);
      }
    }
    _ => (),
  }

  Ok(())
}
```

## Data Ingestion Example

Use the ingestion feature to upload training data directly:

```rust  theme={"system"}
use edge_impulse_runner::ingestion::{Category, Ingestion, UploadOptions};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
  let ingestion = Ingestion::new("your-api-key").with_debug();

  let result = ingestion
    .upload_file(
      "path/to/file.jpg",
      Category::Training,
      Some("my_label".to_string()),
      Some(UploadOptions {
        disallow_duplicates: true,
        add_date_id: true,
      }),
    )
    .await?;

  println!("Upload successful: {}", result);

  Ok(())
}
```

## Example Projects

Explore comprehensive examples demonstrating the library's capabilities:

* **Basic Classification**
* **Image Processing**
* **Video-based Object Detection**
* **Sensor Data Ingestion**

Find and run these examples directly from the [GitHub repository](https://github.com/edgeimpulse/edge-impulse-runner-rs).

## API Quick Links

<Frame caption="cratesio package installation">
  <img src="https://mintcdn.com/edgeimpulse/BCrJzLAs8FGQ0Eny/.assets/images/rust/rust-features.png?fit=max&auto=format&n=BCrJzLAs8FGQ0Eny&q=85&s=b80159a38ee1c11611c41a9df95a6632" width="1431" height="1000" data-path=".assets/images/rust/rust-features.png" />
</Frame>

Refer to our api site for detailed information on structs, enums, type aliases, and constants. The crate structure includes:

* **error** – Error types for the Edge Impulse Runner (EimError, etc.)
* **inference** – Core inference logic (EimModel, model initialization, inference calls)
* **ingestion** – Data ingestion functionality (Ingestion, uploading files or sensor data)
* **types** – Common types (BoundingBox, ModelParameters, SensorType, etc.)

## Conclusion

The Edge Impulse Rust SDK is a powerful tool for developers looking to leverage machine learning on edge devices. With its focus on performance and safety, it allows you to build efficient applications that can run directly on Linux and macOS systems. The library is designed to be easy to use, with clear examples and comprehensive documentation to help you get started quickly.

By combining Rust’s speed and safety with Edge Impulse’s robust ML capabilities, you can create efficient, reliable edge AI applications on Linux and macOS. Check out our Comprehensive API Guide in Section 6 whenever you need deeper insights into the crate’s internals, error handling, or module-level details.

## Community

Engage with the Edge Impulse Rust community:

* **[GitHub Repository](https://github.com/edgeimpulse/edge-impulse-runner-rs):** Contribute, report issues, and collaborate.
* **Share your projects:** Inspire others by showcasing your Rust-based Edge AI applications.


Built with [Mintlify](https://mintlify.com).