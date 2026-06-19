# Add the necessary Rust target
rustup target add x86_64-unknown-linux-gnu
```

### Install CUDA (for GPU feature)

Ensure you have an NVIDIA GPU with the required drivers. Then follow the instructions from [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit).

Verify the installation:

```bash
nvidia-smi
nvcc --version
```

## Building Public Parameters

The public parameters for the cryptographic protocol are built in two steps:

### 1. Download and process the perpetual power of tau

We use the challenge_0084 file from the nearly most recent submission.

```bash
curl https://pse-trusted-setup-ppot.s3.eu-central-1.amazonaws.com/challenge_0084 -o challenge_0084
```

### 2. Build the AMT parameters

You can either construct these parameters yourself or download pre-built files.

#### Choice 1: Download the pre-built files

```bash
./dev-support/download_params.sh
```

#### Choice 2: Construct the parameters yourself

```bash
./dev_support/build_params.sh challenge_0084
```

## Running the Server

Run the server with the following command:

```bash
cargo run -r -p server --features grpc/parallel,grpc/cuda -- --config run/config.toml
```

:::note
If you do not have a CUDA environment, remove the cuda feature.
:::

DA Encoder will serve on port 34000 with specified gRPC interface.

## Using the Verification Logic

Add the following to `Cargo.toml` of your crate:

```toml
zg-encoder = { git = "https://github.com/0gfoundation/0g-da-encoder.git" }
```

Use the `zg_encoder::EncodedSlice::verify` function for verifying.

## Benchmark the Performance

Run the following task:

```bash
cargo bench -p grpc --features grpc/parallel,grpc/cuda --bench process_data --features zg-encoder/production_mode -- --nocapture
```

## Development and Testing

Run the following script for complete testing:

```bash
./dev_support/test.sh
```

</TabItem>
<TabItem value="docker" label="DA Retriever">

## DA Retriever Node Installation

**1. Clone the DA Retriever Node Repo**

```bash
git clone https://github.com/0gfoundation/0g-da-retriever.git
cd 0g-da-retriever
```

**2. Edit Files**

Add the following line to Dockerfile.dockerignore file:

```bash
!/run/config.toml
```

Replace Dockerfile with the following:

```dockerfile