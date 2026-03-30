# Source: https://docs.wandb.ai/models/ref.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Reference overview

> Browse the generated API reference documentation for the W&B Python SDK, CLI, and query panel data types.

export const ClickableCard = ({href, children, className = ''}) => {
  const handleCardClick = e => {
    let target = e.target;
    while (target && target !== e.currentTarget) {
      if (target.tagName === 'A') {
        return;
      }
      target = target.parentElement;
    }
    window.location.href = href;
  };
  return <div className={`clickable-card ${className}`} onClick={handleCardClick} style={{
    cursor: 'pointer'
  }}>
      {children}
    </div>;
};

<CardGroup cols={2}>
  <Card title="Python Library" href="/models/ref/python/">
    Train, fine-tune, and manage models from experimentation to production.
  </Card>

  <Card title="Command Line Interface" href="/models/ref/cli/">
    Log in, run jobs, execute sweeps, and more using shell commands.
  </Card>
</CardGroup>

<CardGroup cols={2}>
  <Card title="Query Panels" href="/models/ref/query-panel/">
    A beta query language to select and aggregate data.
  </Card>

  <Card title="W&B Weave" href="/weave/">
    Looking for Weave API? See the W\&B Weave Docs.
  </Card>
</CardGroup>

## Weave Reference

<Card title="W&B Weave" href="/weave/">
  Looking for Weave API? See the W\&B Weave Docs.
</Card>
