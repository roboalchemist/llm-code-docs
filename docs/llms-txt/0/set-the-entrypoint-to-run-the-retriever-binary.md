# Set the entrypoint to run the retriever binary
CMD ["/usr/local/bin/retriever"]
```

Replace the Config impl in `/retriever/src/config.rs` with the following:

```rust
impl Config {
    pub fn from_cli_file() -> Result<Self> {
        let matches = cli::cli_app().get_matches();
        let config_file = matches
            .get_one::<String>("config")
            .map(|s| s.as_str())
            .unwrap_or("/0g-da-retriever/run/config.toml");

        let c = RawConfig(
            config::Config::builder()
                .add_source(config::File::with_name(config_file))
                .build()?,
        );

        Ok(Self {
            log_level: c.get_string("log_level")?,
            eth_rpc_url: c.get_string("eth_rpc_endpoint")?,
            grpc_listen_address: c.get_string("grpc_listen_address")?,
            max_ongoing_retrieve_request: c.get_u64_opt("max_ongoing_retrieve_request")?,
        })
    }
}
```

**3. Update Configuration**

Update configuration file `run/config.toml` as needed with context below.

| Field | Description |
|-------|-------------|
| log_level | Set log level. |
| grpc_listen_address | Server listening address. |
| eth_rpc_endpoint | JSON RPC node endpoint for the blockchain network. |

**4. Build and Run the Docker Node**

```bash
docker build -t 0g-da-retriever . 
docker run -d --name 0g-da-retriever -p 34005:34005 0g-da-retriever
```

</TabItem>
</Tabs>

## Troubleshooting

<details>
<summary>DA Client connection issues</summary>

- Verify the RPC endpoint is accessible
- Check that your private key has sufficient funds for gas
- Ensure the contract addresses are correct for your network
- Review logs: `docker logs 0g-da-client`
</details>

<details>
<summary>Encoder GPU not detected</summary>

- Verify NVIDIA drivers are installed: `nvidia-smi`
- Check CUDA installation: `nvcc --version`
- Ensure Docker has GPU access if using containers
- Try running without cuda feature if GPU is not available
</details>

<details>
<summary>Retriever fails to start</summary>

- Check that port 34005 is not already in use
- Verify the Ethereum RPC endpoint is accessible
- Ensure config.toml is properly formatted
- Review container logs for specific errors
</details>

## Next Steps

- **Integration Examples** → [DA Examples Repository](https://github.com/0gfoundation/0g-da-example-rust)
- **Join Community** → [Discord](https://discord.gg/0glabs) for support
- **Run a DA Node** → [DA Node Guide](/run-a-node/da-node)

---

*Ready to integrate 0G DA into your application? Start with the DA Client and connect to the network.*

---

## Goldsky Subgraphs