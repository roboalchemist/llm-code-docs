# Source: https://planetscale.com/docs/postgres/imports/import-ips.md

# Import public IP addresses

> When importing a database, you may have IP restrictions in place on your source database and may need to grant a set of IP addresses access to your Postgres database so that PlanetScale can make the connection.

If you have IP restrictions on your source database, you'll need to allowlist the PlanetScale IP addresses so we can connect during the import process. The IPs you need depend on the region of your PlanetScale database.

## Retrieve IP addresses via API

You can get the list of IP addresses for your database's region by visiting the following URL in your browser while logged into PlanetScale:

```
https://api.planetscale.com/v1/organizations/<ORG>/databases/<DATABASE>
```

Replace `<ORG>` with your organization name and `<DATABASE>` with your database name.

The response includes a `region` object with a `public_ip_addresses` array containing all the IPs you need to allowlist:

```json  theme={null}
{
  "id": "rr0qdj0nin8q",
  "type": "Database",
  "region": {
    "id": "ri0pbcmdkjsh",
    "type": "Region",
    "provider": "AWS",
    "enabled": true,
    "public_ip_addresses": [
      "18.117.23.127",
      "3.131.243.164",
      "3.132.168.252",
      "3.131.252.213",
      "3.132.182.173",
      "3.15.49.114",
      "3.209.149.66",
      "3.215.97.46",
      "34.193.111.15"
    ],
    "display_name": "AWS us-east-2",
    "location": "Ohio",
    "slug": "aws-us-east-2"
  }
}
```

Add each IP address from the `public_ip_addresses` array to your source database's allowlist before starting the import.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt