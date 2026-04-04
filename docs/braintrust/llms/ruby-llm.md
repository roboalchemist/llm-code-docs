# Source: https://braintrust.dev/docs/integrations/sdk-integrations/ruby-llm.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# RubyLLM

[RubyLLM](https://rubyllm.com) is a Ruby gem that provides a unified interface for multiple AI providers including OpenAI, Anthropic, Google Gemini, AWS Bedrock, Mistral, and more. Braintrust traces RubyLLM applications to capture LLM calls, tool usage, and performance metrics across any supported provider.

## Setup

Install the Braintrust Ruby SDK and RubyLLM:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
gem install braintrust ruby_llm
```

Configure your environment variables:

```bash title=".env" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
BRAINTRUST_API_KEY=your-api-key

# Configure your preferred provider(s)
OPENAI_API_KEY=your-openai-key
# ANTHROPIC_API_KEY=your-anthropic-key
# GOOGLE_API_KEY=your-google-key
```

## Trace with RubyLLM

Enable automatic tracing by wrapping RubyLLM with Braintrust:

```ruby title="app.rb" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
require 'braintrust'
require 'ruby_llm'

# Initialize Braintrust
Braintrust.init(default_project: 'My Project')

# Enable automatic tracing for RubyLLM
Braintrust::Trace::Contrib::Github::Crmne::RubyLLM.wrap

# Configure RubyLLM with your provider
RubyLLM.configure do |config|
  config.openai_api_key = ENV['OPENAI_API_KEY']
end

# Create a chat and make requests (automatically traced)
chat = RubyLLM.chat(model: 'gpt-4o-mini')
response = chat.ask('What is machine learning?')

puts response.content
```

All RubyLLM calls are automatically traced, including:

* Chat completions across any provider
* Tool/function calls
* Token usage metrics
* Streaming responses

## Resources

* [RubyLLM documentation](https://rubyllm.com)
* [Braintrust Ruby SDK](https://github.com/braintrustdata/braintrust-sdk-ruby)
* [Tracing guide](/instrument/custom-tracing)
