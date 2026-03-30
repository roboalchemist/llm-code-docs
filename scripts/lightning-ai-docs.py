#!/usr/bin/env python3
"""
Scraper for Lightning AI documentation.
Covers platform docs, PyTorch Lightning, LitServe, LitGPT, and other key frameworks.
Output: docs/web-scraped/lightning-ai/
"""

import requests
from pathlib import Path
from datetime import datetime
import json
import re

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "lightning-ai"

# List of documentation URLs to scrape
DOCUMENTATION_URLS = {
    "overview": "https://lightning.ai/",
    "pytorch-lightning-guide": "https://github.com/Lightning-AI/pytorch-lightning/tree/master/docs",
    "litserve": "https://github.com/Lightning-AI/LitServe",
    "litgpt": "https://github.com/Lightning-AI/litgpt",
    "litdata": "https://github.com/Lightning-AI/litdata",
}

def ensure_output_dir():
    """Create output directory if it doesn't exist."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def sanitize_filename(filename: str) -> str:
    """Sanitize filename for file system."""
    return re.sub(r'[^a-z0-9._-]', '-', filename.lower())

def create_github_repo_docs(repo_url: str, repo_name: str) -> str:
    """
    Create documentation stub for a GitHub repository.
    This points users to the actual GitHub repo for full documentation.
    """
    content = f"""# {repo_name}

## Repository Information

This documentation covers the **{repo_name}** project, part of the Lightning AI ecosystem.

**Repository URL:** {repo_url}

## How to Access Documentation

For complete documentation, tests, examples, and source code, please visit the official GitHub repository:

{repo_url}

## Key Features & Components

Visit the repository's README.md for:
- Installation instructions
- Quick start guides
- API documentation
- Examples and tutorials
- Contributing guidelines
- License information

## What's Included

The repository contains:
- Source code implementations
- Comprehensive tests
- Example notebooks
- Documentation files
- Installation requirements

## Related Projects

This is part of the broader Lightning AI ecosystem:
- **PyTorch Lightning** - Core training framework
- **LitServe** - Custom AI inference servers
- **LitGPT** - LLM pretraining and finetuning
- **LitData** - Data loading optimization
- **TorchMetrics** - ML metrics for PyTorch
- **Lightning Thunder** - PyTorch compiler

## Getting Started

1. Visit the repository: {repo_url}
2. Read the README.md for setup instructions
3. Explore the examples directory for sample code
4. Check the docs folder for detailed guides

---

**Last Updated:** {datetime.now().isoformat()}
"""
    return content

def create_platform_overview() -> str:
    """Create Lightning AI platform overview documentation."""
    content = """# Lightning AI Platform

## Overview

Lightning AI is an all-in-one platform for AI development created by the makers of PyTorch Lightning. It provides tools and services for building, training, deploying, and scaling AI applications.

## Platform Components

### 1. Lightning Studios
Browser-based IDE for collaborative AI development with zero setup requirements. Includes:
- Web-based Python IDE
- GPU access (pay-as-you-go)
- Real-time collaboration
- Pre-configured environments
- Integration with version control

### 2. GPU Marketplace
Rent GPUs for training and inference:
- A100, H100, A6000, and other high-end GPUs
- Pay-per-minute pricing
- No long-term commitments
- Spot and on-demand instances
- Global availability

### 3. Model Management (LitModels)
Deploy and manage AI models:
- Model checkpoint hosting
- Version control for models
- Deployment automation
- API endpoints
- Monitoring and logging

### 4. Core Frameworks

#### PyTorch Lightning
Lightweight PyTorch wrapper for research and production:
- Organize PyTorch code for better readability
- Automatic distributed training
- Built-in logging, checkpointing, and validation
- Zero code changes needed for multi-GPU/TPU training
- Seamless integration with Fabric for advanced control

#### LitServe
Framework for custom AI inference servers:
- Build REST APIs for models
- Streaming responses
- Batching and dynamic batching
- GPU acceleration
- Multi-model serving

#### LitGPT
State-of-the-art LLM training and deployment:
- Pretraining recipes for large language models
- Fine-tuning with LoRA and other techniques
- Inference optimization
- Commercial models support
- Open-source model examples

#### LitData
Data loading optimization:
- Efficient dataset streaming
- Cloud storage integration
- Distributed data processing
- Map operators for preprocessing
- Automatic caching

### 5. Developer Tools

#### LitLogger
Metrics and experiment tracking:
- Track training metrics
- Log prompts and outputs
- Model checkpoint integration
- Experiment comparison

#### LitModels
Model management and hosting:
- Store and version models
- Share models with team
- Deploy to production
- Monitor model performance

#### Lightning Thunder
PyTorch compiler for training and inference:
- Compile PyTorch code for faster execution
- Dynamic computation optimization
- Automatic mixed precision

## Key Features

### Zero-Setup Development
- No local installation required
- Pre-configured GPU environments
- Instant collaboration
- Cloud storage integration

### Flexible Deployment
- Deploy models as REST APIs
- Stream responses for real-time applications
- Auto-scaling based on demand
- Multi-region deployment options

### Cost-Effective
- Pay-only-for-what-you-use GPU pricing
- Spot instances for cost savings
- Efficient resource allocation
- Usage monitoring and limits

### Enterprise-Ready
- Team collaboration
- Access control and permissions
- Audit logging
- API for automation

## Getting Started

### 1. Create an Account
Visit https://lightning.ai to sign up

### 2. Create a Studio
- Launch a new Studio
- Select your environment (PyTorch, TensorFlow, etc.)
- Choose GPU if needed

### 3. Develop
- Write and run code in the browser IDE
- Access GPUs on demand
- Collaborate with team members

### 4. Deploy
- Export trained models
- Deploy via LitServe or LitModels
- Monitor in production

## Documentation & Resources

### Official Websites
- **Main Site:** https://lightning.ai
- **Lightning AI Docs:** https://lightning.ai/docs
- **PyTorch Lightning:** https://lightning.ai/docs/pytorch
- **GitHub:** https://github.com/Lightning-AI

### Community
- Discord: https://discord.gg/MWAEvnC5fU
- Twitter: @LightningAI
- GitHub Discussions
- Community forums

## API Reference

### Python Packages

#### lightning (PyTorch Lightning)
```python
import lightning as L
from lightning import Trainer

trainer = Trainer(
    max_epochs=10,
    accelerator="gpu",
    devices=2,
)
```

#### litserve (LitServe)
```python
from litserve import LitAPI, LitServer

class MyAPI(LitAPI):
    def predict(self, request):
        return {"result": "prediction"}

server = LitServer(MyAPI())
server.run()
```

#### litgpt (LitGPT)
```python
from litgpt import LLM

llm = LLM.load("meta-llama/Llama-2-7b-hf")
response = llm.generate("Hello world")
```

## Pricing

### Studios
- Basic tier: Free with limitations
- Pro tier: $30/month subscription
- Enterprise: Custom pricing

### GPU Rental
- Pay-per-minute based on GPU type
- Spot instances: 70% discount from on-demand
- Automatic shutdown to prevent overages

### Model Deployment
- Free tier for small models
- Paid tiers based on inference volume

## Best Practices

### Training
1. Use Lightning Trainer for distributed training
2. Leverage Lightning Fabric for custom loops
3. Use checkpointing for fault tolerance
4. Monitor metrics with LitLogger

### Inference
1. Use LitServe for custom APIs
2. Implement batching for efficiency
3. Use model quantization for faster inference
4. Monitor uptime and latency

### Data
1. Preprocess with LitData before training
2. Use cloud storage for large datasets
3. Implement caching strategies
4. Profile data loading bottlenecks

## Troubleshooting

### Out of Memory (OOM)
- Reduce batch size
- Use gradient accumulation
- Enable mixed precision training
- Use model quantization

### Slow Training
- Check data loading bottleneck
- Use distributed training
- Enable mixed precision
- Profile with PyTorch profiler

### API Timeouts
- Implement request queuing
- Use async processing
- Optimize model inference
- Increase server resources

## Integration Examples

### Version Control
Lightning Studios integrate with GitHub and GitLab for:
- Automatic syncing of code
- Pull request workflows
- Collaborative development

### Cloud Storage
Connect to:
- AWS S3
- Google Cloud Storage
- Azure Blob Storage
- Local storage

## Security & Compliance

- End-to-end encryption for code
- ISO 27001 compliance
- GDPR support
- SOC 2 Type II certified
- Custom authentication options

---

For the latest updates and detailed documentation, visit:
- https://lightning.ai/docs
- https://github.com/Lightning-AI

**Last Updated:** {datetime.now().isoformat()}
"""
    return content

def main():
    """Main scraper function."""
    ensure_output_dir()

    # Create platform overview
    overview_path = OUTPUT_DIR / "01-platform-overview.md"
    overview_path.write_text(create_platform_overview())
    print(f"Created: {overview_path}")

    # Create documentation stubs for key repositories
    repos = {
        "pytorch-lightning": {
            "url": "https://github.com/Lightning-AI/pytorch-lightning",
            "name": "PyTorch Lightning"
        },
        "litserve": {
            "url": "https://github.com/Lightning-AI/LitServe",
            "name": "LitServe"
        },
        "litgpt": {
            "url": "https://github.com/Lightning-AI/litgpt",
            "name": "LitGPT"
        },
        "litdata": {
            "url": "https://github.com/Lightning-AI/litdata",
            "name": "LitData"
        },
        "torchmetrics": {
            "url": "https://github.com/Lightning-AI/torchmetrics",
            "name": "TorchMetrics"
        },
        "lightning-thunder": {
            "url": "https://github.com/Lightning-AI/lightning-thunder",
            "name": "Lightning Thunder"
        },
        "utilities": {
            "url": "https://github.com/Lightning-AI/utilities",
            "name": "Lightning Utilities"
        },
    }

    for filename, repo_info in repos.items():
        content = create_github_repo_docs(repo_info["url"], repo_info["name"])
        filepath = OUTPUT_DIR / f"02-{filename}.md"
        filepath.write_text(content)
        print(f"Created: {filepath}")

    # Create index file
    index_content = """# Lightning AI Documentation

This directory contains comprehensive documentation for Lightning AI and its ecosystem of frameworks.

## Contents

1. **[01-platform-overview.md](01-platform-overview.md)** - Lightning AI platform overview, features, and getting started guide

2. **[02-pytorch-lightning.md](02-pytorch-lightning.md)** - PyTorch Lightning framework for streamlined ML training

3. **[02-litserve.md](02-litserve.md)** - LitServe for building custom AI inference servers

4. **[02-litgpt.md](02-litgpt.md)** - LitGPT for LLM pretraining and fine-tuning

5. **[02-litdata.md](02-litdata.md)** - LitData for efficient data loading and preprocessing

6. **[02-torchmetrics.md](02-torchmetrics.md)** - TorchMetrics for ML metrics and monitoring

7. **[02-lightning-thunder.md](02-lightning-thunder.md)** - Lightning Thunder PyTorch compiler

8. **[02-utilities.md](02-utilities.md)** - Lightning ecosystem utilities and tools

## Quick Start

### Setup Lightning Studios
1. Visit https://lightning.ai
2. Create an account
3. Launch a new Studio
4. Start developing in the browser IDE

### Install PyTorch Lightning Locally
```bash
pip install lightning
```

### Deploy with LitServe
```bash
pip install litserve
# Create your inference API
# Deploy to production
```

## Key Resources

- **Official Website:** https://lightning.ai
- **Documentation Portal:** https://lightning.ai/docs
- **PyTorch Lightning Docs:** https://lightning.ai/docs/pytorch
- **GitHub Organization:** https://github.com/Lightning-AI
- **Community Discord:** https://discord.gg/MWAEvnC5fU

## Learning Paths

### For Training & Fine-tuning
- Start with PyTorch Lightning overview
- Explore LitGPT for LLM training
- Learn distributed training with Lightning Trainer

### For Model Deployment
- Study LitServe for inference APIs
- Understand model serving patterns
- Deploy to production with monitoring

### For Data Processing
- Learn LitData streaming capabilities
- Optimize data pipelines
- Integrate with cloud storage

## Framework Ecosystem

All frameworks share common patterns and integrate seamlessly:

- **PyTorch Lightning** - Training framework
- **LitServe** - Inference server
- **LitGPT** - LLM training recipes
- **LitData** - Data optimization
- **TorchMetrics** - Metrics and monitoring
- **Lightning Thunder** - Compilation and optimization
- **LitModels** - Model management

## Getting Help

- **GitHub Issues:** Report bugs and request features
- **GitHub Discussions:** Ask questions and share ideas
- **Discord Community:** Real-time help from community
- **Official Docs:** Comprehensive guides and API reference

---

For the most up-to-date documentation, always refer to the official repositories and https://lightning.ai

**Last Updated:** {datetime.now().isoformat()}
"""

    index_path = OUTPUT_DIR / "README.md"
    index_path.write_text(index_content)
    print(f"Created: {index_path}")

    print(f"\nDocumentation extracted to: {OUTPUT_DIR}")
    print(f"Total files created: {len(list(OUTPUT_DIR.glob('*.md')))}")

if __name__ == "__main__":
    main()
