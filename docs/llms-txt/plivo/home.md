# Source: https://plivo.com/docs/home.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

> Explore Plivo docs for voice, SMS, and SIP trunking API integration.

# Home

export function openSearch() {
  document.getElementById('search-bar-entry').click();
}

<div className="relative w-full flex items-center justify-center" style={{ height: '12rem', overflow: 'hidden'}}>
  <div className="absolute inset-0 bg-primary dark:bg-primary-light" style={{opacity: 0.05 }} />

  <div style={{ position: 'absolute', textAlign: 'center', padding: '0 1rem' }}>
    <div
      className="text-gray-900 dark:text-gray-200"
      style={{
     fontWeight: '600',
     fontSize: '28px',
     margin: '0',
    }}
    >
      Welcome to Plivo <span className="text-primary dark:text-primary-light">Documentation</span>
    </div>

    <p
      className="prose prose-gray dark:prose-invert"
      style={{
      marginTop: '1rem',
     fontWeight: '400',
     fontSize: '16px',
     maxWidth: '42rem'
    }}
    >
      Explore comprehensive guides, API references, and discussions to integrate, manage, and optimize your Plivo solutions.
    </p>
  </div>
</div>

<div
  style={{marginTop: '3rem', marginBottom: '3rem', maxWidth: '70rem', marginLeft: 'auto',
 marginRight: 'auto', paddingLeft: '1.25rem',
 paddingRight: '1.25rem' }}
>
  <h2 className="text-gray-900 dark:text-gray-200" style={{marginTop: '2rem', marginBottom: '2rem', fontWeight: '500'}} />

  <CardGroup cols={2}>
    <Card title="Voice Agents" icon="phone" href="/voice-agents/audio-streaming/overview" horizontal>
      Build AI-powered voice agents using AI Studio, Audio Streaming, or SIP Trunking integrations
    </Card>

    <Card title="Messaging Agents" icon="message-square" href="/aiagent/getstarted/messaging-agents-overview" horizontal>
      Build AI-powered messaging agents for WhatsApp, SMS, and Chat using AI Studio
    </Card>

    <Card title="Programmable APIs" icon="webhook" iconType="solid" href="/voice/quickstart/quickstart" horizontal>
      Full API access for Voice, Messaging, SIP Trunking, Verify, and more
    </Card>

    <Card title="FAQ" icon="circle-help" href="/faq/messaging/messaging-api" horizontal>
      Frequently asked questions about Messaging, Account Management, and Billing
    </Card>
  </CardGroup>
</div>
