# Source: https://docs.pinecone.io/integrations/ai-engine.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# AI Engine

export const PrimarySecondaryCTA = ({primaryLabel, primaryHref, primaryTarget, secondaryLabel, secondaryHref, secondaryTarget}) => <div style={{
  display: 'flex',
  alignItems: 'center',
  gap: 16
}}>
   {primaryLabel && primaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  background: 'var(--brand-blue)',
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex'
}}>
      <a href={primaryHref} target={primaryTarget} style={{
  paddingLeft: 22,
  paddingRight: 22,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 4,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
        <div style={{
  textAlign: 'justify',
  color: 'var(--text-contrast)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
          {primaryLabel}
        </div>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{
  marginLeft: 2
}}>
          <path d="M9.70492 6L8.29492 7.41L12.8749 12L8.29492 16.59L9.70492 18L15.7049 12L9.70492 6Z" fill="white" style={{
  fille: "var(--text-contrast)"
}} />
        </svg>
      </a>
    </div>}

    {secondaryLabel && secondaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex',
  textDecoration: 'none'
}}>
        <a href={secondaryHref} target={secondaryTarget} style={{
  paddingLeft: 11,
  paddingRight: 11,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 8,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
          <div style={{
  textAlign: 'justify',
  color: 'var(--brand-blue)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
            {secondaryLabel}
          </div>
        </a>
      </div>}

  </div>;

AI Engine seamlessly connects WordPress with the world's leading AI models. Create intelligent chatbots, generate content, build AI forms, and automate tasks—all from your WordPress dashboard.

With AI Engine, you can create a chatbot to assist your visitors, answer support questions, or guide users through your products and services. Need fresh content? AI Engine can write posts in your voice, help rewrite existing ones, or translate them naturally into other languages. It can also generate custom images for your articles, refine messy text, or just lend a hand when you're stuck.

For developers and power users, AI Engine offers internal APIs, shortcode flexibility, and advanced features like function calling and real-time audio chat. You can build your own AI-powered tools, automate tasks, or even create AI-driven SaaS applications on top of WordPress. And with support for a wide range of providers — OpenAI, Anthropic, Google, Hugging Face, and more — you have full control over the models you want to use.

Everything is designed to feel native to WordPress. Whether you're exploring ideas in the AI Playground, using Copilot to help in the editor, or letting an AI agent manage your content through MCP, AI Engine is built to grow with you — and shaped by real user feedback every step of the way.

<PrimarySecondaryCTA primaryHref={"https://ai.thehiddendocs.com/services/pinecone/"} primaryLabel={"Get started"} primaryTarget={"_blank"} />
