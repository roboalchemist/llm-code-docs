# Source: https://github.com/aquasecurity/trivy/blob/main/docs/guide/advanced/private-registries/self.md

BasicAuth server needs `TRIVY_USERNAME` and `TRIVY_PASSWORD`.

```bash
export TRIVY_USERNAME={USERNAME}
export TRIVY_PASSWORD={PASSWORD}

# if you want to use 80 port, use NonSSL
export TRIVY_NON_SSL=true
```
