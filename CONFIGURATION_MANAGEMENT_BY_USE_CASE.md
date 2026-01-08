# Configuration Management Tools by Use Case

Quick-reference guide for selecting the right configuration management tool based on your specific needs.

## Quick Start: Choose by Scenario

### I'm building a Python web application
- **Best choice**: Pydantic Settings (if using FastAPI/modern Python) or Dynaconf (complex setups)
- **Also consider**: python-dotenv (simplest), environs (env-focused)
- **Add validation**: Pydantic for type safety
- **Example**: `pip install pydantic-settings` + define BaseSettings class

### I'm building a Node.js/TypeScript application
- **Best choice**: dotenv + Zod (TypeScript) or node-config (multi-env)
- **Also consider**: nconf (hierarchical), convict (schema validation)
- **If using Next.js/React**: dotenv + Zod for strict typing
- **Example**: `npm install dotenv zod` + .env file

### I'm building a Go CLI tool
- **Best choice**: Viper (widely used) or Koanf (simpler/customizable)
- **Integrate with**: Cobra for CLI framework
- **File formats**: YAML (recommended) or TOML
- **Example**: Viper + Cobra combination is de facto standard

### I'm building a Rust application
- **Best choice**: figment (type-safe) or config (most popular)
- **Also consider**: envy (env-only)
- **Foundation**: All use serde for serialization
- **Example**: `cargo add figment` + struct with serde

### I'm building a Java/Kotlin application
- **Best choice**: Typesafe Config (HOCON) or Spring ConfigurationProperties
- **If using Spring Boot**: Use @ConfigurationProperties with application.yml
- **For Kotlin**: kotlinx.serialization-hocon
- **Example**: application.yml + @ConfigurationProperties class

### I'm building a Ruby on Rails application
- **Best choice**: Rails.configuration (built-in) or Settingslogic (more features)
- **For development**: dotenv-rails for .env files
- **For secrets**: Rails credentials system (Rails 5.1+)
- **Example**: config/settings.yml + Settingslogic gem

### I'm building a PHP application
- **Best choice**: Symfony Dotenv (if using Symfony) or vlucas/phpdotenv
- **Add validation**: Respect/Validation
- **File format**: .env files (development) or PHP arrays (production)
- **Example**: `composer require vlucas/dotenv` + .env loading

### I'm building a .NET/C# application
- **Best choice**: appsettings.json + IConfiguration (built-in)
- **Use Options Pattern** for strongly-typed access
- **For secrets**: User Secrets (dev) or Azure Key Vault (production)
- **For logging config**: Serilog with appsettings.json
- **Example**: appsettings.json + IOptions<MySettings> injection

---

## Use Case: Multi-Environment Configuration

**Problem**: Need different configs for dev/staging/production

### Python Solutions
- **Dynaconf** with `@envvar` decorator: Best for automatic layering
- **Pydantic Settings** with multiple .env files: Simple and type-safe
- **Environment-specific approach**:
  ```python
  config = Settings(_env_file=f'.env.{os.getenv("ENV", "dev")}')
  ```

### JavaScript Solutions
- **node-config**: Built-in support via default.json + production.json
- **nconf**: Explicit hierarchical loading from multiple sources
- **Environment-based approach**:
  ```javascript
  const config = require(`./config.${process.env.NODE_ENV}.json`);
  ```

### Go Solutions
- **Viper**: `viper.SetConfigName("config")` with environment-specific files
- **Cobra flags**: Bind CLI flags to override file-based config
- **Example**: config.yaml, config.dev.yaml, config.prod.yaml

### All Languages
- Use environment variables to override file-based config
- Follow precedence: CLI args > env vars > config files > defaults
- Never hardcode environment-specific values

---

## Use Case: Type-Safe Configuration

**Problem**: Want compile-time/runtime type checking for configs

### Python (BEST)
1. **Pydantic Settings** - Type hints with validation errors
2. **Pydantic alone** - If not using BaseSettings
3. **dataclasses** + custom validation - If avoiding dependencies

```python
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    database_url: str
    debug: bool = False
    max_connections: int = Field(gt=0)
```

### TypeScript (BEST)
1. **Zod** - Runtime schema validation with TypeScript inference
2. **Joi** - Schema validation with detailed error messages
3. **Yup** - Simpler schema validation

```typescript
import { z } from 'zod';

const configSchema = z.object({
  DATABASE_URL: z.string().url(),
  DEBUG: z.coerce.boolean().default(false),
  MAX_CONNECTIONS: z.coerce.number().int().positive(),
});
```

### Go (LESS COMMON)
1. **validator** struct tags + Viper unmarshal
2. **Option pattern** for safe configuration objects
3. Manual field validation after unmarshaling

### Rust (NATIVE)
1. **figment** - Type-safe with serde
2. **config** - Unmarshal to structs with serde
3. **envy** - Direct struct derivation from env vars

```rust
#[derive(serde::Deserialize)]
struct Config {
    database_url: String,
    debug: bool,
}
```

### Java
1. **Typesafe Config** - Static typing via direct API
2. **Spring ConfigurationProperties** - Declarative with validation
3. **Jackson/Gson** - Manual JSON schema validation

---

## Use Case: Secret Management

**Problem**: Need to securely store and manage secrets (API keys, passwords, etc.)

### Development Environment
- **Use**: .env files (locally, NEVER in git)
- **Tool**: python-dotenv, dotenv (Node), godotenv (Go)
- **Gitignore**: Add .env to .gitignore, commit .env.example instead

### Staging/Production Environment
- **Use**: Cloud secret managers or HashiCorp Vault
- **Options by cloud**:
  - **AWS**: AWS Secrets Manager (recommended) or Parameter Store
  - **Azure**: Azure Key Vault
  - **GCP**: Google Cloud Secret Manager
  - **Self-hosted**: HashiCorp Vault (enterprise-grade)
- **Kubernetes**: Use Kubernetes Secrets + encrypt at rest + RBAC

### Libraries for Secret Handling
- **Python**: python-dotenv + os.getenv() or specialized crypto libraries
- **Node.js**: dotenv + process.env
- **Go**: godotenv + os.Getenv()
- **Rust**: envy or config crate with env vars
- **Java**: Spring Cloud Config or Vault client
- **Ruby**: Rails credentials or Figaro
- **PHP**: Symfony Dotenv or php-dotenv

### Never Do
- Hardcode secrets in code or config files
- Commit .env files to version control
- Log secrets or pass through command-line args
- Store secrets in plain text databases

---

## Use Case: Configuration Validation

**Problem**: Need to ensure configuration is valid before app startup

### Validation-First Tools

#### Python
1. **Pydantic** (BEST) - Type hints + automatic validation
2. **Marshmallow** - Schema-based with custom validators
3. **Voluptuous** - Lightweight schema validation

#### JavaScript
1. **Zod** (BEST for TypeScript) - Type inference + strict validation
2. **Joi** - Schema validation with detailed errors
3. **Yup** - Simple object schema validation

#### Go
1. **validator** struct tags - Post-unmarshal validation
2. **go-playground/validator** - Fluent validation
3. Manual validation function approach

#### Rust
1. **validator** crate - Struct-level validation
2. **serde** with custom deserializers
3. figment's type system ensures valid deserialization

#### Java
1. **Bean Validation (JSR-380)** - Standard annotations
2. **Spring Validation** - Framework-integrated
3. **Typesafe Config** validation methods

### Validation Patterns
```python
# Python: Fail on startup if config invalid
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str  # Required
    debug: bool = False  # Optional with default

# Raises ValidationError if required fields missing
config = Settings()
```

```typescript
// TypeScript: Strict schema validation
const config = configSchema.parse(process.env);
// Throws if validation fails
```

---

## Use Case: Hot Reload / Live Configuration Updates

**Problem**: Want to update configuration without restarting app

### Tools Supporting File Watching
1. **Viper** (Go) - `viper.WatchConfig()` with callback
2. **config** crate (Rust) - File watching with reload
3. **Dynaconf** (Python) - `Settings.reload()` method
4. **node-config** (JS) - Not native, but can implement manually
5. **Kubernetes ConfigMaps** - Update mounted config, restart pods

### General Approach
```go
// Go with Viper
viper.WatchConfig()
viper.OnConfigChange(func(in fsnotify.Event) {
    // Config reloaded, refresh dependent services
})
```

### When to Use
- Development/testing (faster iteration)
- Feature flags in production (with caution)
- Metrics/performance tuning configs
- NOT for database credentials (risk of inconsistent state)

### Better Alternative
- Use remote config service (Consul, etcd, feature flag platform)
- Implement manual reload endpoint/gRPC call
- Use configuration as environment variables (requires redeploy)

---

## Use Case: Distributed/Microservices Architecture

**Problem**: Multiple services need consistent configuration and secrets

### Recommended Approaches

#### Configuration Management
1. **Consul** (HashiCorp) - Service discovery + distributed config
2. **etcd** (CNCF) - Distributed key-value for Kubernetes
3. **AWS Parameter Store** - Hierarchical, free option
4. **Azure App Configuration** - Managed service on Azure
5. **Kubernetes ConfigMaps** - Native if using Kubernetes

#### Secret Management
1. **HashiCorp Vault** (recommended) - Dynamic secrets, rotation, audit
2. **AWS Secrets Manager** (AWS-native) - Automatic rotation
3. **Azure Key Vault** (Azure-native) - Certificate management
4. **Kubernetes Secrets** (encrypted at rest) - If not highly sensitive

#### Example Architecture
```
┌─────────────────────────────────────────┐
│   Distributed Config (Consul/etcd)      │
│   - App config (non-sensitive)          │
│   - Feature flags                       │
│   - Service discovery                   │
└─────────────────────────────────────────┘
                    ↑
         ┌──────────┴──────────┐
         │                     │
    Service A              Service B
    (connects via          (connects via
    client SDK)            client SDK)

┌─────────────────────────────────────────┐
│   Secret Manager (Vault/AWS Secrets)    │
│   - Database passwords                  │
│   - API keys                            │
│   - TLS certificates                    │
│   - Dynamic credentials                 │
└─────────────────────────────────────────┘
```

#### Language-Specific Clients
- **Go**: `consul/api`, `coreos/etcd` client
- **Python**: `hvac` (Vault), `boto3` (AWS), Azure SDK
- **Java**: Spring Cloud Config, HashiCorp Vault Spring
- **Node.js**: `node-consul`, `etcd3`, AWS SDK
- **Rust**: `consul` crate, `etcd-rs`

---

## Use Case: Configuration as Code

**Problem**: Want infrastructure and config defined together

### Tools for IaC
1. **Terraform** (most popular) - HCL-based, multi-cloud
2. **Ansible** (configuration management) - YAML-based playbooks
3. **Kubernetes** - YAML for config + secrets
4. **Pulumi** (multi-language) - Code in Python/Go/TypeScript
5. **CloudFormation** (AWS-only) - JSON/YAML templates

### Configuration File Approaches
```hcl
# Terraform (HCL)
variable "database_url" {
  type = string
  sensitive = true
}
```

```yaml
# Ansible/Kubernetes (YAML)
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  DATABASE_URL: postgres://...
```

```python
# Pulumi (Python)
config = pulumi.Config()
db_url = config.require_secret("database_url")
```

---

## Use Case: Dependency Injection + Configuration

**Problem**: Want to inject configuration into application components

### Language-Specific Solutions

#### Python
- **FastAPI** - Dependency injection + Settings
- **Flask** - Config class + custom loaders
- **Pydantic** - Settings as injectable models

#### Java
- **Spring Framework** - @Value, @ConfigurationProperties injection
- **Guice** - DI with configuration objects
- **Quarkus** - @ConfigProperty injection

#### Go
- **Wire** (Google) - Compile-time DI with Viper integration
- **Uber Dig** - Runtime DI library
- Manual dependency graphs with Viper config

#### Rust
- **dependency-injection** crates - Limited ecosystem
- Usually manual pattern with serde

#### .NET
- **IOptions<T>** pattern (built-in)
- **Microsoft.Extensions.DependencyInjection**

### Typical Pattern
```python
# FastAPI with Pydantic Settings
from fastapi import Depends
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str

async def get_settings() -> Settings:
    return Settings()

@app.get("/status")
async def status(settings: Settings = Depends(get_settings)):
    # Access settings.database_url
    pass
```

---

## Tool Selection Decision Tree

```
Start: What's your primary language?

├─ Python
│  ├─ FastAPI? → Use Pydantic Settings
│  ├─ Complex multi-env? → Use Dynaconf
│  └─ Simple? → Use python-dotenv
│
├─ JavaScript/TypeScript
│  ├─ TypeScript? → Use Zod + dotenv
│  ├─ Multi-env? → Use node-config
│  └─ Simple? → Use dotenv
│
├─ Go
│  ├─ CLI tool? → Use Viper + Cobra
│  ├─ Simpler/custom? → Use Koanf
│  └─ Env only? → Use godotenv
│
├─ Rust
│  ├─ Type-safe priority? → Use figment
│  ├─ Most flexible? → Use config crate
│  └─ Env vars only? → Use envy
│
├─ Java/Kotlin
│  ├─ Spring Boot? → Use ConfigurationProperties
│  ├─ Kotlin? → Use kotlinx.serialization-hocon
│  └─ HOCON needed? → Use Typesafe Config
│
├─ Ruby/Rails
│  ├─ Rails app? → Use Rails.configuration
│  ├─ More features? → Use Settingslogic
│  └─ Development? → Use dotenv-rails
│
└─ PHP
   ├─ Symfony? → Use Symfony Dotenv
   ├─ Need structure? → Use vlucas/phpdotenv
   └─ Custom? → Use Pimple + custom loaders

Question: Do you need secrets management?
├─ Yes, development → Use .env file + dotenv
├─ Yes, production → Use Vault / cloud secret manager
└─ No → Skip secrets management

Question: Do you need multi-environment support?
├─ Yes → Use tool with file merging (node-config, Viper, Dynaconf)
├─ Partially → Use env vars for overrides
└─ No → Use simple file loader
```

---

## Comparison Matrix: Top Tools by Language

### Python (Top 5)
| Tool | Type | Ease | Type Safety | Best For |
|------|------|------|-------------|----------|
| Pydantic Settings | Validation | Medium | Excellent | FastAPI, type safety |
| Dynaconf | Config Mgmt | Medium | Good | Complex multi-env |
| python-dotenv | Env Loader | Easy | None | Simple dev setup |
| Marshmallow | Validation | Medium | Medium | Schema-based config |
| Hydra | Framework | Hard | Medium | ML/research projects |

### JavaScript/TypeScript (Top 5)
| Tool | Type | Ease | Type Safety | Best For |
|------|------|------|-------------|----------|
| Zod | Validation | Medium | Excellent | TypeScript-first |
| dotenv | Env Loader | Easy | None | Universal .env |
| node-config | Config Mgmt | Medium | Low | Multi-environment |
| nconf | Hierarchical | Medium | Low | Complex hierarchies |
| convict | Validation | Medium | Medium | Schema validation |

### Go (Top 3)
| Tool | Type | Ease | Type Safety | Best For |
|------|------|------|-------------|----------|
| Viper | Complete | Hard | Medium | Standard choice |
| Cobra | CLI | Hard | Medium | CLI tools |
| Koanf | Config Mgmt | Medium | Low | Simpler alternatives |

### Java (Top 3)
| Tool | Type | Ease | Type Safety | Best For |
|------|------|------|-------------|----------|
| Spring ConfigurationProperties | Framework | Easy | Excellent | Spring Boot |
| Typesafe Config (HOCON) | Format | Medium | Good | HOCON files |
| Apache Commons Configuration | Library | Medium | Low | Generic Java |

---

## Performance Considerations

### Startup Time
- **Fast**: dotenv (Python/JS), python-decouple, godotenv
- **Medium**: Viper, node-config, Pydantic Settings
- **Slower**: Dynaconf (with Vault), Spring ConfigurationProperties (with external sources)

### Memory Usage
- **Minimal**: dotenv, python-decouple, env-var
- **Moderate**: Viper, node-config, config (Rust)
- **Heavier**: Dynaconf, Spring Boot, large config files

### Recommendation
- For most applications: Startup time difference negligible (<100ms)
- Consider if: App starts 1000s of times (serverless, containers)
- Optimize with: Lazy loading, caching, compiled configurations

---

## Key Takeaways

1. **Choose by language first** - Native/popular tools are proven
2. **Type safety matters** - Use Pydantic (Python), Zod (TypeScript), Typesafe Config (Java)
3. **Validate at startup** - Fail fast on configuration errors
4. **Separate secrets** - Never store secrets in code or committed files
5. **Follow 12-factor** - Externalize config to environment variables
6. **Use precedence** - CLI args > env vars > files > defaults
7. **Scale with architecture** - Simple apps: files, Complex/distributed: Vault/Consul
8. **Hot reload rarely needed** - Usually prefer container restart for config changes
