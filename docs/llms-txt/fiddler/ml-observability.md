# Source: https://docs.fiddler.ai/reference/glossary/ml-observability.md

# Source: https://docs.fiddler.ai/getting-started/ml-observability.md

# ML Observability

### Introduction

Fiddler is a comprehensive AI observability platform that helps data science teams monitor, explain, and improve their machine learning models and LLM applications in production. Our platform provides the visibility and insights you need to ensure your AI systems perform reliably and deliver business value.

With Fiddler, you can:

* **Monitor model health** across traditional ML and LLMs with specialized metrics
* **Detect issues early** through customizable alerts and drift detection
* **Debug problems quickly** with explainable AI and root cause analysis tools
* **Ensure model fairness** through segment analysis and bias detection
* **Optimize performance** with detailed traffic and performance tracking

Whether you're managing a few models or hundreds, Fiddler provides the tools to maintain confidence in your AI systems as they scale.

## Key Capabilities

### Comprehensive Monitoring

* **Performance Tracking**: Monitor model accuracy, precision, recall, and other ML metrics in real time across all your deployments
* **Data Drift Detection**: Identify shifts in your production data that could impact model performance before they cause issues
* **Data Integrity Checks**: Ensure your models receive valid, properly formatted data that meets your expectations
* **Vector Monitoring**: Specialized tools for monitoring embedding-based and vector search applications

### Advanced Analytics

* **Embedding Visualization**: Explore high-dimensional data using UMAP to understand patterns and clusters
* **Model Segmentation**: Analyze performance across different user cohorts to identify bias and uncover targeted improvements
* **Statistical Analysis**: Generate detailed statistics on model inputs, outputs, and performance metrics
* **Custom Metrics**: Define and track metrics specific to your business needs and use cases

### Getting Started

Implementing Fiddler ML monitoring requires just three steps:

1. **Onboard your LLM application** to Fiddler by defining its inputs, outputs, and related metadata
2. **Publish your application data** to Fiddler, typically the "digital exhaust" from your model serving platform
3. **Monitor performance** through dashboards and alerts that track the metrics most important to your use case

Fiddler automatically handles the complex work of generating metrics, detecting anomalies, and providing the visualizations you need to maintain high-quality ML applications.

### Next Steps

* **Quick Start**: [Simple ML Monitoring](https://app.gitbook.com/s/jZC6ysdlGhDKECaPCjwm/ml-monitoring/simple-ml-monitoring) ⏱️ 10 min
* **Learn**:
  * [Available auto-generated metrics](https://docs.fiddler.ai/observability/platform)
  * [Data drift and model performance](https://docs.fiddler.ai/observability/platform/performance-tracking-platform)
  * [Setting up alerts](https://docs.fiddler.ai/observability/platform/alerts-platform)
  * [Creating your own custom metrics](https://docs.fiddler.ai/reference/glossary/custom-metrics)
  * [Diagnose issues with Root Cause Analysis](https://docs.fiddler.ai/observability/analytics#root-cause-analysis)
  * [Auto-generated and custom dashboards](https://docs.fiddler.ai/observability/dashboards)
* **Reference**:
  * [Fiddler Python client SDK](https://app.gitbook.com/s/rsvU8AIQ2ZL9arerribd/fiddler-python-client-sdk)
  * [Fiddler Python client SDK guides](https://app.gitbook.com/s/jZC6ysdlGhDKECaPCjwm/client-library-reference)
