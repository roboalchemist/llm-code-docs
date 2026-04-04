# Source: https://docs.sonarsource.com/sonarqube-community-build/server-installation/pre-installation/jwt-token.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/pre-installation/jwt-token.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/pre-installation/jwt-token.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/pre-installation/jwt-token.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/pre-installation/jwt-token.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/pre-installation/jwt-token.md

# Defining a JWT token

By default, users are logged out and sessions closed when server is restarted. If you prefer keeping user sessions open, a secret should be defined. Value is HS256 key encoded with base64. It must be unique for each installation of SonarQube Server.

The following examples illustrate how to generate a HS256 key encoded with base64, where `your_secret` and `your_key` are arbitrary strings that can be modified.

{% tabs %}
{% tab title="WINDOWS SYSTEM WITH POWERSHELL" %}

```powershell
$message = 'your_secret'
$secret = 'your_key'

$hmacsha = New-Object System.Security.Cryptography.HMACSHA256
$hmacsha.key = [Text.Encoding]::ASCII.GetBytes($secret)
$signature = $hmacsha.ComputeHash([Text.Encoding]::ASCII.GetBytes($message))
$signature = [Convert]::ToBase64String($signature)

echo $signature
```

{% endtab %}

{% tab title="UNIX SYSTEM" %}

```sh
echo -n "your_secret" | openssl dgst -sha256 -hmac "your_key" -binary | base64
```

{% endtab %}
{% endtabs %}
