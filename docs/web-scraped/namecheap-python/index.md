# Namecheap API Documentation (namecheap-python)

Modern Python SDK with CLI and TUI tools

## Source Repository

- GitHub: https://github.com/adriangalilea/namecheap-python

## Official Namecheap Resources

- [Namecheap API Documentation](https://www.namecheap.com/support/api/intro/)
- [API Sandbox](https://www.sandbox.namecheap.com/)

## API Methods

### Domains
- `namecheap.domains.getList` - Returns list of domains for user
- `namecheap.domains.getInfo` - Get domain details
- `namecheap.domains.check` - Check domain availability

### DNS
- `namecheap.domains.dns.getHosts` - Get DNS host records
- `namecheap.domains.dns.getList` - Get DNS servers for domain
- `namecheap.domains.dns.setHosts` - Set DNS host records
- `namecheap.domains.dns.setCustom` - Set custom nameservers
- `namecheap.domains.dns.setDefault` - Set default Namecheap DNS

### Nameservers
- `namecheap.domains.ns.create` - Create nameserver
- `namecheap.domains.ns.delete` - Delete nameserver
- `namecheap.domains.ns.getInfo` - Get nameserver info
- `namecheap.domains.ns.update` - Update nameserver IP

## Authentication

All API calls require:
- `ApiUser` / `api_user` - Your Namecheap username
- `ApiKey` / `api_key` - Your API key (from account settings)
- `UserName` / `username` - Username on whose behalf the call is made
- `ClientIp` / `client_ip` - Your whitelisted IP address

## Environments

- **Production**: `https://api.namecheap.com/xml.response`
- **Sandbox**: `https://api.sandbox.namecheap.com/xml.response`

## Files in this directory

- [CLI](CLI.md)
- [README](README.md)
- [__init__](__init__.md)
- [client](client.md)
- [dns](dns.md)
- [domains](domains.md)
- [errors](errors.md)
- [examples-README](examples-README.md)
- [models](models.md)
- [quickstart](quickstart.md)
