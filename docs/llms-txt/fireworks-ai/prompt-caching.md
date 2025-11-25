# Source: https://docs.fireworks.ai/guides/prompt-caching.md

# Prompt caching

Prompt caching is a performance optimization feature that allows Fireworks to
respond faster to requests with prompts that share common prefixes. In many
situations, it can reduce time to first token (TTFT) by as much as 80%.

Prompt caching is enabled by default for all Fireworks models and deployments.

For dedicated deployments, prompt caching frees up resources, leading to higher
throughput on the same hardware. Dedicated deployments on the Enterprise plan allow
additional configuration options to further optimize cache performance.

## Using prompt caching

### Common use cases

Requests to LLMs often share a large portion of their prompt. For example:

* Long system prompts with detailed instructions
* Descriptions of available tools for function calling
* Growing previous conversation history for chat use cases
* Shared per-user context, like a current file for a coding assistant

Prompt caching avoids re-processing the cached prefix of the prompt and starts output generation much sooner.

### Structuring prompts for caching

Prompt caching works only for exact prefix matches within a prompt. To
realize caching benefits, place static content like instructions and examples at
the beginning of your prompt, and put variable content, such as user-specific
information, at the end.

For function calling models, tools are considered part of the prompt.

## Optimization techniques for maximum cache hits

Due to the autoregressive nature of LLMs, even a single-token difference can invalidate the cache from that token onward. Here are key strategies to maximize your cache hit rates:

### Keep your prompt prefix stable

The most critical rule for effective prompt caching is maintaining a stable prefix. Any change to the beginning of your prompt will invalidate the entire cache chain that follows.

<Warning>
  **Common mistake:** Including timestamps or other dynamic content at the beginning of your system prompt.

  ```python  theme={null}
  # ❌ DON'T: This kills cache hit rates
  system_prompt = f"""
  Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
  You are a helpful AI assistant...
  """
  ```

  Even a one-second difference in the timestamp will invalidate the entire cache, making it completely ineffective.
</Warning>

### Structure prompts for caching success

**✅ DO:** Place static content first, dynamic content last

```python  theme={null}
from fireworks import LLM

# ✅ Good: Static content first
system_prompt = """
You are a helpful AI assistant with expertise in software development.

Your guidelines:
- Provide clear, concise explanations
- Include practical examples when helpful
- Ask clarifying questions when requirements are unclear

Available tools:
- web_search: Search the internet for current information
- code_executor: Run code snippets safely
- file_manager: Read and write files
"""

# Build the complete prompt
user_message = ""

# Add dynamic content at the end
if user_context:
    user_message += f"User context: {user_context}\n\n"

if current_time_needed:
    user_message += f"Current time: {datetime.now().isoformat()}\n\n"

# User query goes last
user_message += user_query

# Use with Fireworks Build SDK
llm = LLM(model="llama-v3p1-70b-instruct", deployment_type="auto")

response = llm.chat.completions.create(
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]
)
```

### Smart timestamp handling

When you need to provide current time information, consider these strategies:

**Option 1: Rounded timestamps**

```python  theme={null}
# ✅ Round to larger intervals to increase cache hits
current_hour = datetime.now().replace(minute=0, second=0, microsecond=0)
system_prompt = f"""
You are a helpful assistant.
Current hour: {current_hour.strftime('%Y-%m-%d %H:00')}
...
"""
```

**Option 2: Conditional time injection**

```python  theme={null}
# ✅ Only add time when the query actually needs it
def build_prompt(user_query, system_base):
    prompt = system_base
    
    # Only add timestamp for time-sensitive queries
    time_keywords = ['today', 'now', 'current', 'latest', 'recent']
    if any(keyword in user_query.lower() for keyword in time_keywords):
        prompt += f"\nCurrent time: {datetime.now().isoformat()}"
    
    prompt += f"\nUser: {user_query}"
    return prompt
```

**Option 3: Move time to user message**

```python  theme={null}
from fireworks import LLM

# ✅ Keep system prompt static, add time context to user message
system_prompt = """
You are a helpful AI assistant...
""" # This stays the same

user_message = f"""
Current time: {datetime.now().isoformat()}

User query: {user_query}
"""

# Use with Fireworks Build SDK
llm = LLM(model="llama-v3p1-70b-instruct", deployment_type="auto")

response = llm.chat.completions.create(
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]
)
```

By following these optimization techniques, you can significantly improve your application's performance through effective prompt caching while maintaining the quality and functionality of your AI system.

### How it works

Fireworks will automatically find the longest prefix of the request that is
present in the cache and reuse it. The remaining portion of the prompt will be
processed as usual.

The entire prompt is stored in the cache for future reuse. Cached prompts
usually stay in the cache for at least several minutes. Depending on the model,
load level, and deployment configuration, it can be up to several hours. The
oldest prompts are evicted from the cache first.

Prompt caching doesn't alter the result generated by the model. The response you
receive will be identical to what you would get if prompt caching was not used.
Each generation is sampled from the model independently on each request and is not
cached for future usage.

## Monitoring

For dedicated deployments, information about prompt caching is returned in the
response headers. The header `fireworks-prompt-tokens` contains the number of tokens
in the prompt, out of which `fireworks-cached-prompt-tokens` are cached.

Aggregated metrics are also available in the [usage dashboard](https://fireworks.ai/account/usage?type=deployments).

## Data privacy

Serverless deployments maintain separate caches for each Fireworks account to prevent data leakage and timing attacks.

Dedicated deployments by default share a single cache across all requests.
Because prompt caching doesn't change the outputs, privacy is preserved even
if the deployment powers a multi-tenant application. It does open a minor risk
of a timing attack: potentially, an adversary can learn that a particular prompt
is cached by observing the response time. To ensure full isolation, you can pass
the `x-prompt-cache-isolation-key` header or the `prompt_cache_isolation_key`
field in the body of the request. It can contain an arbitrary string that acts
as an additional cache key, i.e., no sharing will occur between requests with
different IDs.

## Limiting or turning off caching

Additionally, you can pass the `prompt_cache_max_len` field in the request body to
limit the maximum prefix of the prompt (in tokens) that is considered for
caching. It's rarely needed in real applications but can come in handy for
benchmarking the performance of dedicated deployments by passing
`"prompt_cache_max_len": 0`.

## Advanced: cache locality for Enterprise deployments

Dedicated deployments on an Enterprise plan allow you to pass an additional hint in the request to improve cache hit rates.

First, the deployment needs to be created or updated with an additional flag:

```bash  theme={null}
firectl create deployment ... --enable-session-affinity
```

Then the client can pass an opaque identifier representing a single user or
session in the `user` field of the body or in the `x-session-affinity` header. Fireworks
will try to route requests with the identifier to the same server, further reducing response times.

It's best to choose an identifier that groups requests with long shared prompt
prefixes. For example, it can be a chat session with the same user or an
assistant working with the same shared context.

### Migration and traffic management

When migrating between deployments that use prompt caching, it's crucial to implement proper traffic routing to maintain optimal cache hit rates. When gradually routing traffic to a new deployment, use consistent user/session-based sampling rather than random sampling.

Here's the recommended implementation for traffic routing:

```python  theme={null}
import hashlib

# Configure traffic fraction (e.g., 20% to new deployment)
fireworks_traffic_fraction = 0.2
user_id = "session-id-123"

# Generate deterministic hash from user_id
hashed_user_id = int(hashlib.md5(user_id.encode()).hexdigest(), 16) # MD5 hash on user-id and convert to integer
MAX_HASH = 2**128 - 1  # MD5 hash maximum value

# Compute ratio for consistent routing
ratio = hashed_user_id / MAX_HASH # Returns 0.0 to 1.0

if (ratio < fireworks_traffic_fraction):
    send_to_new_deployment(user=hashed_user_id)  # Pass user ID for caching
else:
    send_elsewhere()  # Route to old deployment or serverless
```

<Warning>
  Avoid random sampling for traffic routing as it can negatively impact cache hit rates:

  ```python  theme={null}
  # Don't do this:
  if random() < fireworks_traffic_fraction:  # ❌ Reduces cache effectiveness
    send_to_new_deployment(user=hashed_user_id)
  ```

  Using consistent user-based routing ensures complete user sessions are maintained on the same deployment, optimizing prompt cache performance regardless of the traffic fraction.
</Warning>
