# Source: https://docs.qodo.ai/qodo-documentation/on-prem/qodo-on-premise.md

# Qodo On Premise

{% hint style="info" %}
On-premises installation is recommended when your Git server is hosted on-premises. If your Git instance is running in the cloud, consider switching to a Single Tenant installation
{% endhint %}

Welcome to the Qodo on-premises installation documentation. This guide will help you deploy Qodo's t platform in your organization's infrastructure.

Qodo provides enterprise-grade AI agents for code review.&#x20;

The on-premises deployment gives you complete control over your environment while maintaining the highest security standards.

## Architecture

{% @mermaid/diagram content="graph TB
subgraph "External Access"
Users\[Users/Clients]
end

```
subgraph "Kubernetes Cluster"
    Ingress[Ingress Controller]
    
    subgraph "Qodo Gen"
        GenDeploy[Deployment]
        GenConfig[ConfigMaps]
        GenSecret[Secrets]
        GenSvc[Service]
    end
    
    subgraph "Qodo Merge"
        MergeDeploy[Deployment]
        MergeConfig[ConfigMaps]
        MergeSecret[Secrets]
        MergeSvc[Service]
    end
    
    subgraph "Qodo Engine"
        EngineDeploy[Deployment]
        EngineConfig[ConfigMaps]
        EngineSecret[Secrets]
        EngineSvc[Service]
    end
    
    subgraph "Additional Module"
        Module4Deploy[Deployment]
        Module4Config[ConfigMaps]
        Module4Secret[Secrets]
        Module4Svc[Service]
    end
    
    subgraph "Data Layer"
        DB[(Database)]
    end
end

Users -->|HTTPS| Ingress
Ingress -->|Route /gen| GenSvc
Ingress -->|Route /merge| MergeSvc
Ingress -->|Route /engine| EngineSvc
Ingress -->|Route /module4| Module4Svc

GenSvc --> GenDeploy
MergeSvc --> MergeDeploy
EngineSvc --> EngineDeploy
Module4Svc --> Module4Deploy

GenDeploy -.->|Uses| GenConfig
GenDeploy -.->|Uses| GenSecret
MergeDeploy -.->|Uses| MergeConfig
MergeDeploy -.->|Uses| MergeSecret
EngineDeploy -.->|Uses| EngineConfig
EngineDeploy -.->|Uses| EngineSecret
Module4Deploy -.->|Uses| Module4Config
Module4Deploy -.->|Uses| Module4Secret

GenDeploy -->|Read/Write| DB
EngineDeploy -->|Read/Write| DB

classDef moduleBox fill:#e1f5ff,stroke:#0066cc,stroke-width:2px
classDef dataBox fill:#fff4e6,stroke:#ff9800,stroke-width:2px
classDef ingressBox fill:#f3e5f5,stroke:#9c27b0,stroke-width:2px

class GenDeploy,MergeDeploy,EngineDeploy,Module4Deploy moduleBox
class DB dataBox
class Ingress ingressBox
```

" %}
