# Source: https://docs.verda.com/cpu-and-gpu-instances/tips-and-tricks/setting-environment-variables-on-startup.md

# Setting environment variables on startup

To have environment variables be set after each login the script with this format must be put as a startup script:

```bash
#!/bin/bash

cat << 'EOF' >> /etc/environment
SECRET1='SECRET1VALUE'

SECRET2='SECRET2VALUE'
EOF
```
