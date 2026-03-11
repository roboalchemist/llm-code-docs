# Source: https://docs.architect.co/getting-started-with-rust.md

# Getting started with Rust

{% embed url="<https://github.com/architect-xyz/architect-sdk>" %}

## Installation

```bash
cargo add architect-api
cargo add architect-sdk
```

## Example

```rust
use anyhow::Result;
use architect_sdk::Architect;

#[tokio::main]
async fn main() -> Result<()> {
    // Connect to live trading
    let client = Architect::connect("<api key>", "<api secret>", false).await?;
    
    // Or connect to paper trading
    // let client = Architect::connect("<api key>", "<api secret>", true).await?;
    
    Ok(())
}
```
