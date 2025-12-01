# Namecheap API Documentation (namecheap-go)

Official Go SDK for Namecheap API

## Source Repository

- GitHub: https://github.com/namecheap/go-namecheap-sdk

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

- [CONTRIBUTING](CONTRIBUTING.md)
- [README](README.md)
- [domains](domains.md)
- [domains_dns](domains_dns.md)
- [domains_dns_get_hosts](domains_dns_get_hosts.md)
- [domains_dns_get_list](domains_dns_get_list.md)
- [domains_dns_set_custom](domains_dns_set_custom.md)
- [domains_dns_set_default](domains_dns_set_default.md)
- [domains_dns_set_hosts](domains_dns_set_hosts.md)
- [domains_get_info](domains_get_info.md)
- [domains_get_list](domains_get_list.md)
- [domains_ns](domains_ns.md)
- [domains_ns_create](domains_ns_create.md)
- [domains_ns_delete](domains_ns_delete.md)
- [domains_ns_get_info](domains_ns_get_info.md)
- [domains_ns_update](domains_ns_update.md)
- [namecheap](namecheap.md)
