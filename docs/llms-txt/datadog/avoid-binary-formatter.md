# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/avoid-binary-formatter.md

---
title: Do not use BinaryFormatter as it is insecure and vulnerable
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use BinaryFormatter as it is insecure and vulnerable
---

# Do not use BinaryFormatter as it is insecure and vulnerable

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/avoid-binary-formatter`

**Language:** C#

**Severity:** Error

**Category:** Security

**CWE**: [502](https://cwe.mitre.org/data/definitions/502.html)

## Description{% #description %}

This rule prevents the usage of `BinaryFormatter` for serialization due to its inherent security vulnerabilities. `BinaryFormatter` has been found to be susceptible to deserialization attacks, where a malicious actor can control the input to the deserialization operation and exploit this to execute arbitrary code, manipulate program execution, or induce application crashes.

This security risk makes it crucial to avoid `BinaryFormatter`. Instead, opt for safer alternatives for serialization and deserialization. An alternative is [`System.Text.Json`](https://learn.microsoft.com/en-us/dotnet/standard/serialization/binaryformatter-migration-guide/migrate-to-system-text-json), which is not only secure, but also offers better performance. Additional alternatives include [`DataContractSerializer`](https://learn.microsoft.com/en-us/dotnet/standard/serialization/binaryformatter-migration-guide/migrate-to-datacontractserializer), [`MessagePack`](https://learn.microsoft.com/en-us/dotnet/standard/serialization/binaryformatter-migration-guide/migrate-to-messagepack), and [`protobuf-net`](https://learn.microsoft.com/en-us/dotnet/standard/serialization/binaryformatter-migration-guide/migrate-to-protobuf-net).

## Learn More:{% #learn-more %}

- [Microsoft Security Guide](https://learn.microsoft.com/en-us/dotnet/standard/serialization/binaryformatter-security-guide)
- [Microsoft Migration Guide](https://learn.microsoft.com/en-us/dotnet/standard/serialization/binaryformatter-migration-guide)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using System;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;

[Serializable]
public class User
{
    public string Username { get; set; }
    public string Password { get; set; }
}

class Program
{
    static void Main(string[] args)
    {
        // Serializing the object
        User user = new User { Username = "admin", Password = "password123" };
        BinaryFormatter formatter = new BinaryFormatter();

        using (FileStream stream = new FileStream("user.dat", FileMode.Create))
        {
            formatter.Serialize(stream, user);
        }

        // Deserializing the object
        using (FileStream stream = new FileStream("user.dat", FileMode.Open))
        {
            User deserializedUser = (User)formatter.Deserialize(stream);
            Console.WriteLine($"Username: {deserializedUser.Username}, Password: {deserializedUser.Password}");
        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
using System;
using System.IO;
using System.Text.Json;

[Serializable]
public class User
{
    public string Username { get; set; }
    public string Password { get; set; }
}

class Program
{
    static void Main(string[] args)
    {
        // Serializing the object
        User user = new User { Username = "admin", Password = "password123" };
        var options = new JsonSerializerOptions { WriteIndented = true };

        string jsonString = JsonSerializer.Serialize(user, options);
        File.WriteAllText("user.json", jsonString);

        // Deserializing the object
        string readJsonString = File.ReadAllText("user.json");
        User deserializedUser = JsonSerializer.Deserialize<User>(readJsonString);

        Console.WriteLine($"Username: {deserializedUser.Username}, Password: {deserializedUser.Password}");
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
