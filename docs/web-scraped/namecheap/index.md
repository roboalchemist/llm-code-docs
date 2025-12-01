# Namecheap API Documentation

This documentation is extracted from the official [Namecheap Go SDK](https://github.com/namecheap/go-namecheap-sdk).

## Official Resources

- [Namecheap API Documentation](https://www.namecheap.com/support/api/intro/)
- [API Sandbox](https://www.sandbox.namecheap.com/)
- [Go SDK on GitHub](https://github.com/namecheap/go-namecheap-sdk)

## API Methods

### Domains
- `namecheap.domains.getList` - Returns list of domains for user
- `namecheap.domains.getInfo` - Get domain details

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
- `ApiUser` - Your Namecheap username
- `ApiKey` - Your API key (from account settings)
- `UserName` - Username on whose behalf the call is made
- `ClientIp` - Your whitelisted IP address

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
