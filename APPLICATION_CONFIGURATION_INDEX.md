# Application Configuration Frameworks - Quick Index

## Configuration Tools by Primary Use Case

### Configuration File Format Parsing

**Best for:** Reading/writing configuration files in standard formats (YAML, TOML, JSON, INI)

| Format | Language | Tool | Description |
|--------|----------|------|-------------|
| YAML | Python | PyYAML | Pure Python YAML 1.1 parser and emitter |
| YAML | Python | ruamel.yaml | YAML parser preserving comments and formatting |
| YAML | Java | SnakeYAML | Java YAML parser with object representation |
| YAML | Go | Go-yaml | Go YAML parser with struct tag support |
| YAML | C++ | yaml-cpp | C++ YAML library with custom type support |
| TOML | Python | tomli/tomllib | Python stdlib TOML parser (3.11+) |
| TOML | Rust | serde_toml | Rust TOML with zero-copy parsing |
| TOML | Go | go-toml | Go TOML parser with spec compliance |
| TOML | Java | toml4j | Java TOML parser with fluent API |
| JSON | Java | Jackson | Fast JSON processing with data binding |
| JSON | Java | Gson | Google's JSON serialization library |
| JSON | Rust | serde_json | Fast memory-efficient JSON for Rust |
| JSON | JavaScript | AJV | Fastest JSON Schema validator |
| INI | Python | configparser | Python stdlib INI file parser |
| INI | Go | go-ini | Go INI-style configuration parser |
| INI | .NET | IniParser | .NET INI file reader/writer |

---

### Environment Variable Management

**Best for:** Loading environment variables, .env files, and environment-based configuration

| Language | Tool | Purpose | Key Features |
|----------|------|---------|--------------|
| Python | python-dotenv | Load .env files | Simple file loading; override support |
| Python | environs | Parse env vars | Type casting; validation; defaults |
| Node.js | dotenv | Load .env files | Zero dependencies; comment support |
| JavaScript | envalid | Validate env vars | Type coercion; custom validators |
| Rust | envy | Deserialize env to structs | Serde integration; error handling |
| Go | cleanenv | Struct-based env parsing | Validation; sensible defaults |
| General | direnv | Directory-based env management | Per-directory .envrc loading |

---

### Python Application Configuration

**Best for:** Python web apps, CLI tools, data science projects, microservices

| Tool | Type | Best Use Case | When to Use |
|------|------|---------------|------------|
| **pydantic** | Data validation + settings | Type-safe config; validation | Most Python projects |
| **python-dotenv** | Environment file loader | Development .env files | Local development |
| **dynaconf** | Hierarchical config | Multi-backend; complex apps | Large applications; microservices |
| **hydra** | Experiment config | ML training; multi-run jobs | ML/AI projects |
| **environs** | Env var parser | Lightweight env parsing | Simple config needs |
| **pydantic-settings** | Pydantic extension | App configuration class | Django/FastAPI apps |

**Typical Stack:**
- Small project: `python-dotenv` + `pydantic`
- Large project: `dynaconf` or `hydra` + `pydantic`
- ML project: `hydra` + `pydantic`

---

### Java/Spring Boot Application Configuration

**Best for:** Spring Boot microservices, enterprise Java applications

| Tool | Scope | Use Case |
|------|-------|----------|
| **application.properties/yml** | Built-in | Single application configuration |
| **Spring Cloud Config** | Microservices | Centralized Git-backed config server |
| **@ConfigurationProperties** | Type-safe binding | Map config sections to typed classes |
| **Quarkus Config** | Native optimization | GraalVM native images; low memory |
| **Micronaut Configuration** | Lightweight | Compile-time DI; fast startup |
| **Spring Boot Profiles** | Environment selection | dev/test/prod configurations |

**Typical Stack for Spring Boot:**
```
application.yml (base)
  → application-dev.yml (dev profile)
  → application-prod.yml (prod profile)
  → Environment variables (overrides)
  → Command-line args (final override)
```

With optional `Spring Cloud Config Server` for microservices.

---

### JavaScript/Node.js Configuration

**Best for:** Node.js backends, Express, NestJS, Next.js applications, frontend projects

**Recommended Stack by Project Type:**

| Project Type | Config Tool | Validation | When to Use |
|-------------|-------------|-----------|------------|
| **Node.js Backend** | `node-config` | `joi` or `zod` | Production APIs; multiple environments |
| **Express/NestJS** | `dotenv` + `joi` | `joi` or `class-validator` | Microservices; REST APIs |
| **Next.js App** | Environment variables | `zod` | TypeScript-first; type safety |
| **React Frontend** | `vite` env vars | `zod` | Build-time configuration |
| **CLI Tool** | `commander` + `joi` | `joi` or `yup` | CLI applications |
| **Tool Config Discovery** | `cosmiconfig` | `joi` or `zod` | Tools like ESLint, Prettier, Babel |

**Validation Library Comparison:**

- **joi** - Most feature-rich; server-side focus (149kb)
- **yup** - Client-side optimized; Joi-like syntax (60kb)
- **zod** - TypeScript-first; best type inference (45kb)
- **valibot** - Lightweight; modular alternative (smaller bundle)
- **class-validator** - Class/decorator-based for NestJS

---

### Rust Configuration

**Best for:** Rust CLI tools, web servers, systems programming, microservices

**Configuration Stack by Project Type:**

| Project | File Config | Env Vars | CLI Args | Typical Setup |
|---------|------------|----------|----------|---------------|
| **CLI Tool** | `confy` | `envy` | `clap` | clap + figment for full stack |
| **Web Server** | `figment` | `envy` | `clap` | figment for layered config |
| **Daemon/Service** | `config-rs` | `envy` | `pflag` (if Go interop) | config-rs + TOML files |
| **Library** | N/A | `envy` | `clap` | Minimal; envy for optional config |

**Recommended Combinations:**
- **Simple app**: `confy` (TOML) + `clap` (CLI)
- **Complex app**: `figment` (layered) + `clap` + `serde`
- **Services**: `config-rs` (multi-format) + environment variables
- **Serialization**: `serde` + `serde_json`/`serde_yaml`/`toml`

---

### Go Application Configuration

**Best for:** Go CLI tools, microservices, cloud-native applications, DevOps tools

| Tool | Purpose | GitHub Stars | When to Use |
|------|---------|--------------|------------|
| **Viper** | Multi-source config manager | 27.6k | Most Go projects; complex config |
| **Cobra** | CLI framework + config | High | CLI applications with subcommands |
| **cleanenv** | Struct-based env parsing | Active | Simple; lightweight; 12-factor apps |
| **pflag** | POSIX flag parsing | Active | Command-line arguments; Cobra integration |
| **gcfg** | INI file parser | Legacy | Backward compatibility; old formats |

**Recommended Stacks:**

- **CLI Tool**: Cobra (for CLI) + Viper (for config)
- **Microservice**: Viper + environment variables
- **Simple App**: cleanenv + pflag
- **Legacy App**: gcfg for INI parsing

---

### .NET/C# Configuration

**Best for:** ASP.NET Core, Windows services, .NET microservices, enterprise applications

**Core System:**
1. **Microsoft.Extensions.Configuration** (foundational)
   - Multiple sources: JSON, environment vars, INI, XML, custom
   - ConfigurationBuilder for composition

2. **Options Pattern** (type-safe access)
   - `IOptions<T>` (static snapshot)
   - `IOptionsSnapshot<T>` (per-request reload)
   - `IOptionsMonitor<T>` (real-time monitoring)

**Recommended Stack:**

```
appsettings.json (base)
  → appsettings.{environment}.json (dev/test/prod)
  → Environment variables (overrides)
  → Secrets.json in dev (secure dev secrets)
  → Azure Key Vault / HashiCorp Vault (production secrets)
```

**With Logging:**
- Serilog (structured logging)
- NLog (enterprise logging)
- Both integrate with IConfiguration

**With DI/IoC:**
- Built-in Microsoft.Extensions.DependencyInjection
- Autofac (lightweight alternative)
- Castle Windsor (complex scenarios)

---

### Feature Flags and Feature Management

**Best for:** Progressive rollouts, A/B testing, canary deployments, feature toggling

**Decision Matrix:**

| Need | Best Tool | Why |
|------|-----------|-----|
| **Self-hosted open-source** | Unleash | Full control; flexible strategies |
| **Managed SaaS (enterprise)** | LaunchDarkly | Industry leader; comprehensive features |
| **Simple self-hosted** | Flagsmith | Easy deployment; good UI |
| **Lightweight server** | Flipt | Stateless; scales easily |
| **Experimentation focus** | GrowthBook | Open-source A/B testing |
| **Data-driven teams** | Split.io | Advanced analytics and insights |
| **Enterprise + CI/CD** | CloudBees FF | Instant rollback; audit logging |

**Common Features Across Platforms:**
- Gradual rollouts (percentage-based)
- User/segment targeting
- A/B testing capabilities
- Real-time flag updates
- Multi-environment support
- Audit logging
- SDK support for multiple languages

---

### Configuration Schema Validation

**Best for:** Validating configuration structure, type safety, runtime validation

**By Language:**

| Language | Top Choice | Alternative | Bundle Size |
|----------|-----------|-------------|-------------|
| **TypeScript** | zod | valibot | 45kb (zod) / smaller (valibot) |
| **JavaScript** | AJV + JSON Schema | joi or yup | Varies |
| **Python** | pydantic | jsonschema | N/A (package) |
| **.NET** | DataAnnotations | FluentValidation | N/A (packages) |
| **Java** | Jakarta Bean Validation | Hibernate Validator | N/A (packages) |

**Schema Validation Comparison:**

- **JSON Schema** (standard) - Language-agnostic; broad adoption
- **Pydantic** (Python) - Type hints; automatic validation
- **Joi** (JavaScript) - Rich API; large ecosystem (19k stars)
- **Zod** (TypeScript) - Best type inference; immutable
- **Class-Validator** (TypeScript) - Decorator-based; NestJS friendly
- **FluentValidation** (.NET) - Fluent API; chainable rules

---

### Multi-Environment Configuration Management

**Best for:** Infrastructure, Kubernetes, cloud deployments, multi-cloud setup

**Tool Categories:**

**Infrastructure as Code (IaC):**
- **Terraform** - Declarative; any cloud; state management
- **Pulumi** - General-purpose languages; Python/TypeScript/Go
- **AWS CDK** - AWS-specific; high-level constructs

**Kubernetes Configuration:**
- **Helm** - Package manager; templated values; easiest adoption
- **Kustomize** - No templating language; overlays for env differences
- **ArgoCD / Flux** - GitOps; Git as source of truth

**Advanced Orchestration:**
- **Crossplane** - Kubernetes-native multi-cloud; unified objects
- **Spacelift** - Terraform automation; policy as code; drift detection

**Recommended Selection:**

| Scenario | Recommended |
|----------|------------|
| Single cloud (AWS/GCP/Azure) | Terraform + Helm |
| Multi-cloud | Pulumi (for code) + Helm (for K8s) |
| Kubernetes only | Helm + Kustomize overlays |
| GitOps workflow | ArgoCD + Kustomize or Helm |
| Hybrid + legacy systems | Terraform + specialized tools |

---

### 12-Factor Application Configuration

**Best for:** Cloud-native apps, microservices, containerized applications

**Principles:**

1. **Store config in environment variables**
   - No .properties or .xml files in production
   - Use secrets management for sensitive data

2. **Tools for Implementation:**
   - Python: `python-dotenv` (dev) + environment vars (prod)
   - Node.js: `dotenv` (dev) + environment vars (prod)
   - Go: `cleanenv` (env-based config)
   - Rust: `envy` (env-based config)
   - Java: Spring Boot env var binding
   - .NET: IConfiguration + Key Vault

3. **Secrets Management:**
   - HashiCorp Vault (self-hosted)
   - AWS Secrets Manager (AWS)
   - Azure Key Vault (.NET/cloud)
   - Google Secret Manager (GCP)

---

## Language-Specific Quick Start Guides

### Python Quick Start
```python
# Option 1: Simple
from dotenv import load_dotenv
import os
load_dotenv()
config = {"db_url": os.getenv("DATABASE_URL")}

# Option 2: Type-safe
from pydantic import BaseSettings
class Config(BaseSettings):
    database_url: str
    debug: bool = False
config = Config()

# Option 3: Complex
from dynaconf import Dynaconf
config = Dynaconf(settings_files=["settings.yaml", ".secrets.yaml"])
```

### Java/Spring Boot Quick Start
```yaml
# application.yml
app:
  name: my-app
  database:
    url: ${DATABASE_URL}
---
spring:
  config:
    activate:
      on-profile: prod
  datasource:
    url: jdbc:mysql://prod-db:3306/myapp
```

### JavaScript/Node.js Quick Start
```javascript
// .env
DATABASE_URL=postgres://localhost/mydb
DEBUG=true

// index.js
require('dotenv').config();
const config = {
  dbUrl: process.env.DATABASE_URL,
  debug: process.env.DEBUG === 'true'
};
```

### Rust Quick Start
```rust
// Cargo.toml
[dependencies]
figment = { version = "0.10", features = ["env", "toml"] }
serde = { version = "1.0", features = ["derive"] }

// src/main.rs
use figment::{Figment, providers::{Env, Toml}};
use serde::Deserialize;

#[derive(Deserialize)]
struct Config { db_url: String }

let config: Config = Figment::new()
    .merge(Toml::file("config.toml"))
    .merge(Env::prefixed("APP_"))
    .extract().unwrap();
```

### Go Quick Start
```go
import "github.com/spf13/viper"

func init() {
    viper.SetConfigFile("config.yaml")
    viper.BindEnv("database.url", "DATABASE_URL")
    viper.ReadInConfig()
}

dbUrl := viper.GetString("database.url")
```

### .NET Quick Start
```csharp
// appsettings.json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=localhost;Database=myapp"
  },
  "AppSettings": {
    "Debug": true
  }
}

// Program.cs
var builder = WebApplication.CreateBuilder(args);
builder.Services.Configure<AppSettings>(
    builder.Configuration.GetSection("AppSettings")
);

// Usage
public class MyService {
    public MyService(IOptions<AppSettings> options) {
        _settings = options.Value;
    }
}
```

---

## Related Documentation

- **[APPLICATION_CONFIGURATION_FRAMEWORKS.md](/APPLICATION_CONFIGURATION_FRAMEWORKS.md)** - Comprehensive tool catalog
- **[APPLICATION_CONFIGURATION_FRAMEWORKS.csv](/APPLICATION_CONFIGURATION_FRAMEWORKS.csv)** - Quick reference table
- [12 Factor App - Config](https://12factor.net/config) - Configuration best practices
- [JSON Schema](https://json-schema.org) - Configuration schema standard
- [llms.txt Format](https://llmstxt.org) - Documentation standard for LLMs

---

## Maintenance Notes

This index is organized by primary use case and includes:
- Configuration format parsing tools
- Language-specific frameworks
- Feature flag platforms
- Multi-environment management
- Schema validation libraries
- Code examples for common patterns

Recommendations follow 2026 trends and community adoption metrics (GitHub stars, maintenance status, commercial backing).

