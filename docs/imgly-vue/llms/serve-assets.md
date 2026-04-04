# Serve Assets

Configure CE.SDK to load engine and content assets from your own servers instead of the IMG.LY CDN for production deployments.

Self-hosting assets is required for production use. The IMG.LY CDN is intended for development and prototyping only—you’ll see a console warning when using the default CDN configuration. Hosting assets yourself gives you control over performance, availability, and compliance requirements.

[Download Assets (v1.67.0)](https://cdn.img.ly/packages/imgly/cesdk-js/1.67.0/imgly-assets.zip)

This guide covers the asset categories CE.SDK uses, how to configure `baseURL` and asset source paths, and how to automate asset updates during SDK upgrades.

## Quick Start[#](#quick-start)

Download and extract the essential assets for your SDK version:

Terminal window

```