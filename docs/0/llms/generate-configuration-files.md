# Generate configuration files
./config
```

</TabItem>
<TabItem value="future" label="OPML, ZKML (Coming Soon)">
Support for additional verification methods including:
- **OPML**: Optimistic Machine Learning proofs
- **ZKML**: Zero-knowledge ML verification

Stay tuned for updates.
</TabItem>
</Tabs>

### Launch Provider Broker

Follow the instructions in [Dstack](https://github.com/Dstack-TEE/dstack?tab=readme-ov-file#-getting-started) or [0G-TAPP](https://github.com/0gfoundation/0g-tapp/blob/main/README.md) documentation to start the service using the config file and docker-compose.yml file generated in the previous step.

The broker will:
- Register your service on the network
- Handle user authentication and request routing
- Manage automatic settlement of payments

## Troubleshooting

<details>
<summary>Broker fails to start</summary>

- Verify Docker Compose is installed correctly
- Check port availability
- Ensure config.local.yaml syntax is valid
- Review logs: `docker compose logs`
</details>

<details>
<summary>Service not accessible</summary>

- Confirm firewall allows incoming connections
- Verify public IP/domain is correct
- Test local service: `curl http://localhost:8000/chat/completions`
</details>

<details>
<summary>Settlement issues</summary>

The automatic settlement engine handles payments. If issues occur:
- Check wallet has sufficient gas
- Verify network connectivity
- Monitor settlement logs in broker output
</details>

## Next Steps
- **Join Community** → [Discord](https://discord.gg/0glabs) for support
- **Explore Inference** → [Inference Documentation](./inference) for integration details

---

## Inference

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';