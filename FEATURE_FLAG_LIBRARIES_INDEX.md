# Feature Flag Libraries Index

Quick navigation guide to feature flag and feature toggle libraries across programming languages.

## Documents in This Collection

1. **FEATURE_FLAG_LIBRARIES_2025.md** - Comprehensive guide with detailed descriptions of all libraries, features, and selection criteria
2. **FEATURE_FLAG_LIBRARIES_QUICK_REFERENCE.csv** - Quick lookup table with package names, documentation links, and repositories
3. **FEATURE_FLAG_LIBRARIES_INDEX.md** - This navigation document

## Quick Language Links

### By Language

- **[JavaScript/TypeScript](#javascripttypescript)**
  - Reflag (Commercial, TypeScript-first)
  - PostHog (Commercial, All-in-one)
  - LaunchDarkly (Commercial)
  - Flagsmith (Commercial)
  - FeatBit (Open-Source)
  - GrowthBook (Open-Source)
  - Flipper Cloud (Open-Source)

- **[Python](#python)**
  - Statsig (Commercial)
  - LaunchDarkly (Commercial)
  - Flagsmith (Commercial)
  - Unleash (Open-Source)
  - FeatBit (Open-Source)
  - Azure App Configuration (Commercial)

- **[Java/JVM](#javajvm)**
  - LaunchDarkly (Commercial)
  - Unleash (Open-Source)
  - FeatBit (Open-Source)
  - Flagsmith (Commercial)

- **[Go](#go)**
  - GO Feature Flag (Open-Source, multi-language relay)
  - LaunchDarkly (Commercial)
  - Unleash (Open-Source)
  - Toggle (Open-Source)
  - dcdr/Decider (Open-Source)
  - GrowthBook (Open-Source)

- **[Ruby](#ruby)**
  - LaunchDarkly (Commercial)
  - Unleash (Open-Source)
  - Flagsmith (Commercial)
  - The Rollout Gem (Open-Source)
  - Additional community gems

- **[PHP](#php)**
  - Unleash (Open-Source)
  - LaunchDarkly (Commercial)
  - ConfigCat (Commercial, Laravel-focused)
  - Flagsmith (Commercial)
  - Toggler (Open-Source)
  - Symfony Feature Flags Bundle (Open-Source)

- **.NET/C#**
  - FeatBit (Open-Source)
  - LaunchDarkly (Commercial)
  - FeatureManagement-Dotnet (Commercial, Microsoft)
  - Unleash (Open-Source)
  - Flagsmith (Commercial)

## By Use Case

### Maximum Type Safety (TypeScript/C#/Java)
- **Reflag** - TypeScript with compile-time safety and auto-generated types
- **LaunchDarkly** - Strong typing across all languages
- **FeatureManagement-Dotnet** - Built-in type safety for .NET

### Open-Source & Self-Hosted
- **Unleash** - Multi-language support, local evaluation
- **GO Feature Flag** - Multi-language relay proxy, 100% open-source
- **FeatBit** - Open-source with managed option
- **GrowthBook** - Self-hosting friendly

### Framework-Specific Integration
- **Flask Feature Flags** - Flask extension
- **ConfigCat** - Excellent Laravel support
- **Symfony Feature Flags Bundle** - Symfony integration
- **FeatureManagement-Dotnet** - ASP.NET Core native

### Enterprise/Mission-Critical
- **LaunchDarkly** - Most mature commercial platform
- **PostHog** - Analytics + flags combined
- **Statsig** - Production-grade Python

### Multi-Language/Microservices
- **GO Feature Flag** - Relay proxy supporting 9+ languages
- **Unleash** - Self-hosted with multi-language SDKs
- **FeatBit** - OpenFeature standard support

### A/B Testing Focused
- **GrowthBook** - Purpose-built for A/B testing
- **PostHog** - Full analytics integration
- **Statsig** - Experiment management

### Simple/Lightweight Projects
- **Toggle** (Go) - Minimal dependencies
- **Toggler** (PHP) - Custom backend support
- **featuretoggles** (Python) - Minimal overhead

## Cross-Language Standards

### OpenFeature Compliance
Multiple vendors support the OpenFeature standard, allowing vendor-independent feature flag management:
- FeatBit
- Unleash
- LaunchDarkly

Website: https://openfeature.dev

## Comparison by Key Features

### Local Evaluation (Fast, Client-Side)
- Unleash
- GO Feature Flag
- GrowthBook
- PostHog

### Type-Safe Evaluation
- Reflag
- LaunchDarkly
- FeatureManagement-Dotnet
- FeatBit

### Webhook Support
- Unleash
- GO Feature Flag
- LaunchDarkly
- PostHog

### Self-Hosting Available
- Unleash
- GO Feature Flag
- FeatBit
- GrowthBook

### Managed Cloud Only
- LaunchDarkly
- PostHog
- Statsig
- ConfigCat

## Getting Started by Language

### For TypeScript/JavaScript Projects
1. **If type-safety is critical**: Use Reflag
2. **If you want analytics too**: Use PostHog
3. **If self-hosting**: Use Unleash or FeatBit
4. **For enterprise**: Use LaunchDarkly

### For Python Projects
1. **For production apps**: Use Statsig or LaunchDarkly
2. **For self-hosting**: Use Unleash or FeatBit
3. **For Flask apps**: Use Flask Feature Flags or Flagsmith
4. **For Django**: Use Unleash or Flagsmith

### For Java/JVM Projects
1. **For enterprise**: Use LaunchDarkly
2. **For self-hosting**: Use Unleash or FeatBit
3. **For Kotlin**: Use FeatBit with OpenFeature

### For Go Projects
1. **For multi-language support**: Use GO Feature Flag
2. **For enterprise**: Use LaunchDarkly
3. **For self-hosting**: Use Unleash or GO Feature Flag
4. **For simple needs**: Use Toggle or dcdr

### For Ruby Projects
1. **For Rails apps**: Use LaunchDarkly
2. **For self-hosting**: Use Unleash
3. **For community solutions**: Use The Rollout Gem or Flipper

### For PHP Projects
1. **For Laravel**: Use ConfigCat or Flagsmith
2. **For Symfony**: Use Symfony Feature Flags Bundle
3. **For general PHP**: Use Unleash or Toggler

### For .NET/C# Projects
1. **For enterprise**: Use LaunchDarkly
2. **For ASP.NET Core**: Use FeatureManagement-Dotnet
3. **For self-hosting**: Use FeatBit or Unleash

## Selection Checklist

When choosing a feature flag library, verify:

- [ ] Native SDK for your language
- [ ] Type safety support (if applicable)
- [ ] Framework-specific integrations needed
- [ ] Self-hosted or managed cloud preference
- [ ] Multi-language support requirements
- [ ] A/B testing capabilities needed
- [ ] Analytics integration requirements
- [ ] Compliance/data residency needs
- [ ] Team's operational expertise
- [ ] Budget constraints

## References

- Official Documentation Links: See FEATURE_FLAG_LIBRARIES_2025.md
- CSV Quick Reference: FEATURE_FLAG_LIBRARIES_QUICK_REFERENCE.csv
- OpenFeature Standard: https://openfeature.dev
- GO Feature Flag: https://gofeatureflag.org
- Unleash: https://docs.getunleash.io/
- LaunchDarkly: https://launchdarkly.com/docs/sdk

---

Last Updated: 2025-01-01
Research Methodology: Perplexity AI web research with current documentation sources
