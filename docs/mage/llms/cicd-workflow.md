# Source: https://docs.mage.ai/guides/data-sync/cicd-workflow.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Mage Pro CI/CD workflow

> Deploy and manage your pipeline code safely across environments using Mage Pro's integrated deployment application.

export const ProOnly = ({button = 'Get started for free', description = 'Try our fully managed solution to access this advanced feature.', source = 'documentation', title = 'Only in Mage Pro.'}) => <a href={`https://cloud.mage.ai/sign-up?source=${source}`} className="block my-4 px-5 py-4 overflow-hidden rounded-xl flex gap-3 border border-emerald-500/20 bg-emerald-50/50 dark:border-emerald-500/30 dark:bg-emerald-500/10" target="_blank">
    <div style={{
  display: 'flex',
  alignItems: 'center',
  width: '100%'
}}>
      <div className="text-sm prose min-w-0 text-emerald-900 dark:text-emerald-200" style={{
  flex: 1
}}>
        {title}
        <p className="normal">{description}</p>
      </div>

      <div> </div>

      <div>
        <ProButton label={button} href={`https://cloud.mage.ai/sign-up?source=${source}`} />
      </div>
    </div>
  </a>;

export const ProButton = ({href, label = 'Get started with Mage Pro for free', source = 'documentation'}) => <div style={{
  height: 32,
  position: 'relative'
}}>
    <a target="_blank" className="group px-4 py-1.5 relative inline-flex items-center text-sm font-medium rounded-full" href={href ?? `https://cloud.mage.ai/sign-up?source=${source}`}>
      <span className="absolute inset-0 bg-primary-dark dark:bg-primary-light/10 border-primary-light/30 rounded-full dark:border group-hover:opacity-[0.9] dark:group-hover:border-primary-light/60">
      </span>

      <div className="mr-0.5 space-x-2.5 flex items-center">
        <span class="z-10 text-white dark:text-primary-light">
          {label}
        </span>

        <svg width="3" height="24" viewBox="0 -9 3 24" class="h-5 rotate-0 overflow-visible text-white/90 dark:text-primary-light">
          <path d="M0 0L3 3L0 6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path>
        </svg>
      </div>
    </a>
  </div>;

<ProOnly source="git-terminal" />

## Introduction

Mage Pro supports two CI/CD approaches to fit different organizational needs. Both follow the same core workflow: develop → staging → deploy to production using the Git terminal and the Mage Pro deployment application.

This document clarifies the two primary CI/CD approaches available in Mage Pro:

1. **CI/CD by cluster** - Separate clusters for development, staging, and production
2. **CI/CD by workspace** - Multiple workspaces within a single cluster

Both approaches follow the same core principles: develop in isolation, test thoroughly, and deploy safely to production. The choice between cluster based and workspace based workflows depends on your infrastructure requirements, security policies, and team structure.

## 1. CI/CD by cluster

**Setup:** Separate clusters for each environment

* **Development cluster** - Active development
* **Staging cluster** (optional) - Pre-production validation
* **Production cluster** - Live pipelines

## 2. CI/CD by workspace

**Setup:** Single cluster with multiple workspaces (see our [workspaces guide](https://docs.mage.ai/guides/developer-ux/workspaces) for more details on configuring workspaces)

* **Development workspace** - Active development
* **Staging workspace** (optional) - Pre-production validation
* **Production workspace** - Live pipelines

## Git Branch Strategy & Environment Mapping

### Recommended Branch Structure

```python  theme={"system"}
main/master     → Production environment
staging         → Staging environment  
development     → Development environment
feature/*       → Development environment (feature branches)
```

### Workflow Best Practices

**Development:**

* Create feature branches from `development`: `feature/new-pipeline`
* Develop pipelines in feature branch and push changes to Github using the Git terminal (for more details on pushing code to Github see Mage Pro’s [Git terminal](https://docs.mage.ai/guides/data-sync/git-terminal) doc)

**Staging:**

* Merge `development` → `staging` when ready for testing
* Staging environment deploys from `staging` branch
* Run full validation and integration tests

**Production:**

* Merge `staging` → `main` after successful testing
* Production environment deploys from `main` branch only
* Use deployment application for controlled production releases (for more on Mage Pro’s deployment application see the [version control guide](https://docs.mage.ai/guides/data-sync/version-control-guide))

### Environment-Specific Configurations

**Same Code, Different Targets:**
The same codebase connects to different systems using environment-specific configurations:

**Environment Variables & Secrets:**

* Each cluster/workspace maintains its own connection settings
* `DATABASE_URL` points to dev/staging/prod databases
* `API_KEYS` use environment-appropriate credentials

**Configuration Examples:**

```python  theme={"system"}
Development:   DATABASE_URL = dev-warehouse.company.com
Staging:          DATABASE_URL = staging-warehouse.company.com  
Production:    DATABASE_URL = prod-warehouse.company.com
```

**In Mage Pro:**

* Configure different data source connections per environment
* Use environment variables in pipeline io\_config.yaml file: `{{ env_var('DATABASE_URL') }}`
  * or python interpolation in a block `os.environ.get('DB_USERNAME')`

Using these strategies will allow you to develop the same pipeline code, but select different source and targets for each cluster / workspace environment.

## Conclusion

Both approaches use the same tools and follow identical workflows. The choice depends on your infrastructure and security requirements. Use [Git terminal](https://docs.mage.ai/guides/data-sync/git-terminal) for code management and the deployment application for production deployments in either setup. Use our [version control guide](https://docs.mage.ai/guides/data-sync/version-control-guide) to implement this in your Mage Pro environment.


Built with [Mintlify](https://mintlify.com).