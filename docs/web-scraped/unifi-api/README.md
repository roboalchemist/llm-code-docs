# UniFi API Documentation

**Last Updated:** 2026-02-01

---

## Welcome to UniFi API Docs

This is comprehensive documentation for the **Ubiquiti UniFi Network API**, the official API for programmatically managing UniFi network infrastructure.

### What You'll Find Here

1. **[Quickstart Guide](quickstart.md)** - Get started in 5 minutes
   - Authentication setup
   - First API call
   - Common operations
   - Code examples

2. **[Architecture Guide](architecture.md)** - Understand the API deeply
   - UniFi hierarchy and concepts
   - API structure and patterns
   - Data models
   - Advanced features
   - Production patterns

3. **[OpenAPI Reference](openapi-reference.md)** - Complete endpoint documentation
   - All available endpoints
   - Request/response formats
   - Data schemas
   - Error codes

### Quick Links

- **Official Docs**: https://developer.ui.com/
- **GitHub**: https://github.com/ubiquiti-community/unifi-api
- **Postman**: https://www.postman.com/unifilabs/unifi-labs-s-public-workspace/
- **Help**: https://help.ui.com/

### API Capabilities

The UniFi API lets you:

- **Manage Devices** - Configure APs, switches, gateways
- **Control Clients** - Block/unblock users, get statistics
- **Network Config** - Create VLANs, SSIDs, firewall rules
- **Monitor** - Real-time traffic, events, metrics
- **Advanced** - SD-WAN, mesh networking, guest portals

### Base URL

```
https://api.ui.com/v1/
```

### Authentication

All requests require the `X-API-Key` header:

```bash
curl -H "X-API-Key: YOUR_API_KEY" https://api.ui.com/v1/sites
```

### Rate Limits

- **Early Access Tier**: 100 requests/minute
- **Stable v1 Tier**: 10,000 requests/minute

### Rate Limit Headers

```
X-RateLimit-Limit: 10000
X-RateLimit-Remaining: 9999
X-RateLimit-Reset: 1709212800
```

## Building CLI Tools

The UniFi API is ideal for creating CLI tools like `unifi-cli`:

```bash
# List all sites
unifi sites list

# Get devices in a site
unifi devices list --site "Site Name"

# Block a client
unifi clients block --mac "aa:bb:cc:dd:ee:ff" --site "Site Name"

# Get network stats
unifi stats get --site "Site Name"
```

See the quickstart guide for Python/Bash examples.

## Official UniFi Products

The API supports:

- **UniFi Network** - WiFi 5/6 APs, switches, gateways
- **UniFi Dream Machine** - All-in-one controller
- **UniFi Protect** - IP cameras and video management
- **UniFi Access** - Door locks and access control
- **UniFi Mobile** - Managed cellular

## Getting Started

### 1. Get an API Key

1. Log in to https://unifi.ui.com
2. Go to Settings → Account
3. Create an API key
4. Store it in an environment variable: `export UNIFI_API_KEY=your_key`

### 2. Make Your First Request

```bash
curl -H "X-API-Key: $UNIFI_API_KEY" https://api.ui.com/v1/sites
```

### 3. Choose Your Guide

- **New to the API?** → [Quickstart Guide](quickstart.md)
- **Building an app?** → [Architecture Guide](architecture.md)
- **Need exact endpoints?** → [OpenAPI Reference](openapi-reference.md)

## Support

- **Documentation**: https://developer.ui.com/
- **Community**: https://github.com/ubiquiti-community/unifi-api
- **Help Center**: https://help.ui.com/
- **GitHub Issues**: Report bugs in the community repo

---

**Next Step**: Read the [Quickstart Guide](quickstart.md) to start using the API!
