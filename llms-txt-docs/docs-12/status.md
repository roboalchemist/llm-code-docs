# Source: https://docs.baseten.co/status/status.md

# Baseten platform status

> Current operational status of Baseten's services.

This page automatically refreshes with real-time data from our status monitoring system.

<div id="status-cards">
  <div className="status-banner">
    <div className="banner-icon">
      <Icon icon="circle-check" iconType="solid" />
    </div>

    <div className="banner-text">All systems are operational.</div>
  </div>

  <CardGroup cols={3}>
    <Card title="Model Inference" icon="circle-check" iconType="solid" href="https://status.baseten.co/">
      <div className="status-indicator">Normal</div>
    </Card>

    <Card title="Management API" icon="circle-check" iconType="solid" href="https://status.baseten.co/">
      <div className="status-indicator">Normal</div>
    </Card>

    <Card title="Web Application" icon="circle-check" iconType="solid" href="https://status.baseten.co/">
      <div className="status-indicator">Normal</div>
    </Card>
  </CardGroup>
</div>

<div style={{textAlign: "right", fontSize: "0.8rem", color: "#666", marginTop: "1rem", marginBottom: "2rem"}}>
  <span id="last-refreshed">Last updated: Loading...</span>
</div>
