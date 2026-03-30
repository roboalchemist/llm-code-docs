# Source: https://docs.api7.ai/hub/ai-rate-limiting.md

# ai-rate-limiting

The `ai-rate-limiting` plugin enforces token-based rate limiting for requests sent to LLM services. It helps manage API usage by controlling the number of tokens consumed within a specified time frame, ensuring fair resource allocation and preventing excessive load on the service. It is often used with [`ai-proxy-multi`](https://docs.api7.ai/hub/ai-proxy-multi.md) plugin.

## Local vs Redis Rate Limiting[â](#local-vs-redis-rate-limiting "Direct link to Local vs Redis Rate Limiting")

The `ai-rate-limiting` plugin supports two modes of rate limiting:

* **Local rate limiting**: Limits are enforced independently on each gateway instance. Each instance maintains its own counters, so the effective limit is roughly (limit Ã number of instances) when traffic is spread across instances. This is the default when no `policy` is set or when `policy` is `local`.
* **Redis-based rate limiting**: Limits are shared across all gateway instances through Redis. All instances share the same quota, so the configured limit applies to all gateway instances.

## Demo[â](#demo "Direct link to Demo")

The following demonstrates the [configure instance priority and rate limiting example](#configure-instance-priority-and-rate-limiting). It shows how you can configure two models with different priorities and apply rate limiting on the instance with a higher priority in API7 Enterprise using the Dashboard. In the case where `fallback_strategy` is set to `["rate_limiting"]`, the plugin should continue to forward requests to the low priority instance once the high priority instance's rate limiting quota is fully consumed.

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure `ai-rate-limiting` for different scenarios.

### Rate Limit One Instance[â](#rate-limit-one-instance "Direct link to Rate Limit One Instance")

The following example demonstrates how you can use `ai-proxy-multi` to configure two models for load balancing, forwarding 80% of the traffic to one instance and 20% to the other. Additionally, use `ai-rate-limiting` to configure token-based rate limiting on the instance that receives 80% of the traffic, such that when the configured quota is fully consumed, the additional traffic will be forwarded to the other instance.

Create a route as such and update with your LLM providers, models, API keys, and endpoints:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-rate-limiting-route",
    "uri": "/anything",
    "methods": ["POST"],
    "plugins": {
      "ai-proxy-multi": {
        "instances": [
          {
            "name": "deepseek-instance-1",
            "provider": "deepseek",
            "weight": 8,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$DEEPSEEK_API_KEY"'"
              }
            },
            "options": {
              "model": "deepseek-chat"
            }
          },
          {
            "name": "deepseek-instance-2",
            "provider": "deepseek",
            "weight": 2,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$DEEPSEEK_API_KEY"'"
              }
            },
            "options": {
              "model": "deepseek-chat"
            }
          }
        ]
      },
      "ai-rate-limiting": {
        "policy": "local",
        "instances": [
          {
            "name": "deepseek-instance-1",
            "limit_strategy": "total_tokens",
            "limit": 100,
            "time_window": 30
          }
        ]
      }
    }
  }'
```

â¶ Apply rate limiting on `deepseek-instance-1` instance.

â· Apply rate limiting by `total_tokens`.

â¸ Configure a quota of 100 tokens.

â¹ Configure the time window to be 30 seconds.

Send a POST request to the route with a system prompt and a sample user question in the request body:

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "What is 1+1?" }
    ]
  }'
```

You should receive a response similar to the following:

```
{
  ...
  "model": "deepseek-chat",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "1 + 1 equals 2. This is a fundamental arithmetic operation where adding one unit to another results in a total of two units."
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  ...
}
```

If `deepseek-instance-1` instance rate limiting quota of 100 tokens has been consumed in a 30-second window, the additional requests will all be forwarded to `deepseek-instance-2`, which is not rate limited.

### Apply the Same Quota to All Instances[â](#apply-the-same-quota-to-all-instances "Direct link to Apply the Same Quota to All Instances")

The following example demonstrates how you can apply the same rate limiting quota to all LLM upstream instances in `ai-rate-limiting`.

For demonstration and easier differentiation, you will be configuring one OpenAI instance and one DeepSeek instance as the upstream LLM services.

Create a route as such and update with your LLM providers, models, API keys, and endpoints:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-rate-limiting-route",
    "uri": "/anything",
    "methods": ["POST"],
    "plugins": {
      "ai-proxy-multi": {
        "instances": [
          {
            "name": "openai-instance",
            "provider": "openai",
            "weight": 0,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$OPENAI_API_KEY"'"
              }
            },
            "options": {
              "model": "gpt-4"
            }
          },
          {
            "name": "deepseek-instance",
            "provider": "deepseek",
            "weight": 0,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$DEEPSEEK_API_KEY"'"
              }
            },
            "options": {
              "model": "deepseek-chat"
            }
          }
        ]
      },
      "ai-rate-limiting": {
        "policy": "local",
        "limit": 100,
        "time_window": 60,
        "rejected_code": 429,
        "limit_strategy": "total_tokens"
      }
    }
  }'
```

â¶ Configure a rate limiting quota of 100 tokens for all instances.

â· Configure the time window to be 60 seconds.

â¸ Set the rejection response HTTP status code to 429.

â¹ Apply rate limiting by `total_tokens`.

Send a POST request to the route with a system prompt and a sample user question in the request body:

```
curl -i "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "Explain Newtons laws" }
    ]
  }'
```

You should receive a response from either LLM instance, similar to the following:

```
{
  ...,
  "model": "gpt-4-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Sure! Sir Isaac Newton formulated three laws of motion that describe the motion of objects. These laws are widely used in physics and engineering for studying and understanding how things move. Here they are:\n\n1. Newton's First Law - Law of Inertia: An object at rest tends to stay at rest and an object in motion tends to stay in motion with the same speed and in the same direction unless acted upon by an unbalanced force. This is also known as the principle of inertia.\n\n2. Newton's Second Law of Motion - Force and Acceleration: The acceleration of an object is directly proportional to the net force acting on it and inversely proportional to its mass. This is usually formulated as F=ma where F is the force applied, m is the mass of the object and a is the acceleration produced.\n\n3. Newton's Third Law - Action and Reaction: For every action, there is an equal and opposite reaction. This means that any force exerted on a body will create a force of equal magnitude but in the opposite direction on the object that exerted the first force.\n\nIn simple terms: \n1. If you slide a book on a table and let go, it will stop because of the friction (or force) between it and the table.\n2.",
        "refusal": null
      },
      "logprobs": null,
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 23,
    "completion_tokens": 256,
    "total_tokens": 279,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    },
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "audio_tokens": 0,
      "accepted_prediction_tokens": 0,
      "rejected_prediction_tokens": 0
    }
  },
  "service_tier": "default",
  "system_fingerprint": null
}
```

Since the `total_tokens` value exceeds the configured quota of `100`, the next request within the 60-second window is expected to be forwarded to the other instance.

Within the same 60-second window, send another POST request to the route:

```
curl -i "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "Explain Newtons laws" }
    ]
  }'
```

You should receive a response from the other LLM instance, similar to the following:

```
{
  ...
  "model": "deepseek-chat",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Sure! Newton's laws of motion are three fundamental principles that describe the relationship between the motion of an object and the forces acting on it. They were formulated by Sir Isaac Newton in the late 17th century and are foundational to classical mechanics. Here's an explanation of each law:\n\n---\n\n### **1. Newton's First Law (Law of Inertia)**\n- **Statement**: An object will remain at rest or in uniform motion in a straight line unless acted upon by an external force.\n- **What it means**: This law introduces the concept of **inertia**, which is the tendency of an object to resist changes in its state of motion. If no net force acts on an object, its velocity (speed and direction) will not change.\n- **Example**: A book lying on a table will stay at rest unless you push it. Similarly, a hockey puck sliding on ice will keep moving at a constant speed unless friction or another force slows it down.\n\n---\n\n### **2. Newton's Second Law (Law of Acceleration)**\n- **Statement**: The acceleration of an object is directly proportional to the net force acting on it and inversely proportional to its mass. Mathematically, this is expressed as:\n  \\[\n  F = ma\n  \\]\n"
      },
      "logprobs": null,
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 13,
    "completion_tokens": 256,
    "total_tokens": 269,
    "prompt_tokens_details": {
      "cached_tokens": 0
    },
    "prompt_cache_hit_tokens": 0,
    "prompt_cache_miss_tokens": 13
  },
  "system_fingerprint": "fp_3a5770e1b4_prod0225"
}
```

Since the `total_tokens` value exceeds the configured quota of `100`, the next request within the 60-second window is expected to be rejected.

Within the same 60-second window, send a third POST request to the route:

```
curl -i "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "Explain Newtons laws" }
    ]
  }'
```

You should receive an `HTTP 429 Too Many Requests` response and observe the following headers:

```
X-AI-RateLimit-Limit-openai-instance: 100
X-AI-RateLimit-Remaining-openai-instance: 0
X-AI-RateLimit-Reset-openai-instance: 0
X-AI-RateLimit-Limit-deepseek-instance: 100
X-AI-RateLimit-Remaining-deepseek-instance: 0
X-AI-RateLimit-Reset-deepseek-instance: 0
```

### Configure Instance Priority and Rate Limiting[â](#configure-instance-priority-and-rate-limiting "Direct link to Configure Instance Priority and Rate Limiting")

The following example demonstrates how you can configure two models with different priorities and apply rate limiting on the instance with a higher priority. In the case where `fallback_strategy` is set to `["rate_limiting"]`, the plugin should continue to forward requests to the low priority instance once the high priority instance's rate limiting quota is fully consumed.

Create a route as such and update with your LLM providers, models, API keys, and endpoints:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-rate-limiting-route",
    "uri": "/anything",
    "methods": ["POST"],
    "plugins": {
      "ai-proxy-multi": {
        "fallback_strategy": ["rate_limiting"],
        "instances": [
          {
            "name": "openai-instance",
            "provider": "openai",
            "priority": 1,
            "weight": 0,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$OPENAI_API_KEY"'"
              }
            },
            "options": {
              "model": "gpt-4"
            }
          },
          {
            "name": "deepseek-instance",
            "provider": "deepseek",
            "priority": 0,
            "weight": 0,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$DEEPSEEK_API_KEY"'"
              }
            },
            "options": {
              "model": "deepseek-chat"
            }
          }
        ]
      },
      "ai-rate-limiting": {
        "policy": "local",
        "instances": [
          {
            "name": "openai-instance",
            "limit": 10,
            "time_window": 60
          }
        ],
        "limit_strategy": "total_tokens"
      }
    }
  }'
```

â¶ Set the `fallback_strategy` to `["rate_limiting"]`.

â· Set a higher priority on `openai-instance` instance.

â¸ Set a lower priority on `deepseek-instance` instance.

â¹ Apply rate limiting on `openai-instance` instance.

âº Configure a quota of 10 tokens.

â» Configure the time window to be 60 seconds.

â¼ Apply rate limiting by `total_tokens`.

Send a POST request to the route with a system prompt and a sample user question in the request body:

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "What is 1+1?" }
    ]
  }'
```

You should receive a response similar to the following:

```
{
  ...,
  "model": "gpt-4-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "1+1 equals 2.",
        "refusal": null
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 23,
    "completion_tokens": 8,
    "total_tokens": 31,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    },
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "audio_tokens": 0,
      "accepted_prediction_tokens": 0,
      "rejected_prediction_tokens": 0
    }
  },
  "service_tier": "default",
  "system_fingerprint": null
}
```

Since the `total_tokens` value exceeds the configured quota of `10`, the next request within the 60-second window is expected to be forwarded to the other instance.

Within the same 60-second window, send another POST request to the route:

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "Explain Newton law" }
    ]
  }'
```

You should see a response similar to the following:

```
{
  ...,
  "model": "deepseek-chat",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Certainly! Newton's laws of motion are three fundamental principles that describe the relationship between the motion of an object and the forces acting on it. They were formulated by Sir Isaac Newton in the late 17th century and are foundational to classical mechanics.\n\n---\n\n### **1. Newton's First Law (Law of Inertia):**\n- **Statement:** An object at rest will remain at rest, and an object in motion will continue moving at a constant velocity (in a straight line at a constant speed), unless acted upon by an external force.\n- **Key Idea:** This law introduces the concept of **inertia**, which is the tendency of an object to resist changes in its state of motion.\n- **Example:** If you slide a book across a table, it eventually stops because of the force of friction acting on it. Without friction, the book would keep moving indefinitely.\n\n---\n\n### **2. Newton's Second Law (Law of Acceleration):**\n- **Statement:** The acceleration of an object is directly proportional to the net force acting on it and inversely proportional to its mass. Mathematically, this is expressed as:\n  \\[\n  F = ma\n  \\]\n  where:\n  - \\( F \\) = net force applied (in Newtons),\n  -"
      },
      ...
    }
  ],
  ...
}
```

### Load Balance and Rate Limit by Consumers[â](#load-balance-and-rate-limit-by-consumers "Direct link to Load Balance and Rate Limit by Consumers")

The following example demonstrates how you can configure two models for load balancing and apply rate limiting by consumer.

Create a consumer `johndoe` and a rate limiting quota of 10 tokens in a 60-second window on `openai-instance` instance:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "username": "johndoe",
    "plugins": {
      "ai-rate-limiting": {
        "policy": "local",
        "instances": [
          {
            "name": "openai-instance",
            "limit": 10,
            "time_window": 60
          }
        ],
        "rejected_code": 429,
        "limit_strategy": "total_tokens"
      }
    }
  }'
```

Configure `key-auth` credential for `johndoe`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/johndoe/credentials" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "cred-john-key-auth",
    "plugins": {
      "key-auth": {
        "key": "john-key"
      }
    }
  }'
```

Create another consumer `janedoe` and a rate limiting quota of 10 tokens in a 60-second window on `deepseek-instance` instance:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "username": "johndoe",
    "plugins": {
      "ai-rate-limiting": {
        "policy": "local",
        "instances": [
          {
            "name": "deepseek-instance",
            "limit": 10,
            "time_window": 60
          }
        ],
        "rejected_code": 429,
        "limit_strategy": "total_tokens"
      }
    }
  }'
```

Configure `key-auth` credential for `janedoe`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/janedoe/credentials" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "cred-jane-key-auth",
    "plugins": {
      "key-auth": {
        "key": "jane-key"
      }
    }
  }'
```

Create a route as such and update with your LLM providers, models, API keys, and endpoints:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-rate-limiting-route",
    "uri": "/anything",
    "methods": ["POST"],
    "plugins": {
      "key-auth": {},
      "ai-proxy-multi": {
        "fallback_strategy": ["rate_limiting"],
        "instances": [
          {
            "name": "openai-instance",
            "provider": "openai",
            "weight": 0,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$OPENAI_API_KEY"'"
              }
            },
            "options": {
              "model": "gpt-4"
            }
          },
          {
            "name": "deepseek-instance",
            "provider": "deepseek",
            "weight": 0,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$DEEPSEEK_API_KEY"'"
              }
            },
            "options": {
              "model": "deepseek-chat"
            }
          }
        ]
      }
    }
  }'
```

â¶ Enable `key-auth` on the route.

â· Configure an `openai` instance.

â¸ Configure a `deepseek` instance.

Send a POST request to the route without any consumer key:

```
curl -i "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "What is 1+1?" }
    ]
  }'
```

You should receive an `HTTP/1.1 401 Unauthorized` response.

Send a POST request to the route with `johndoe`'s key:

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -H 'apikey: john-key' \
  -d '{
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "What is 1+1?" }
    ]
  }'
```

You should receive a response similar to the following:

```
{
  ...,
  "model": "gpt-4-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "1+1 equals 2.",
        "refusal": null
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 23,
    "completion_tokens": 8,
    "total_tokens": 31,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    },
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "audio_tokens": 0,
      "accepted_prediction_tokens": 0,
      "rejected_prediction_tokens": 0
    }
  },
  "service_tier": "default",
  "system_fingerprint": null
}
```

Since the `total_tokens` value exceeds the configured quota of the `openai` instance for `johndoe`, the next request within the 60-second window from `johndoe` is expected to be forwarded to the `deepseek` instance.

Within the same 60-second window, send another POST request to the route with `johndoe`'s key:

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -H 'apikey: john-key' \
  -d '{
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "Explain Newtons laws to me" }
    ]
  }'
```

You should see a response similar to the following:

```
{
  ...,
  "model": "deepseek-chat",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Certainly! Newton's laws of motion are three fundamental principles that describe the relationship between the motion of an object and the forces acting on it. They were formulated by Sir Isaac Newton in the late 17th century and are foundational to classical mechanics.\n\n---\n\n### **1. Newton's First Law (Law of Inertia):**\n- **Statement:** An object at rest will remain at rest, and an object in motion will continue moving at a constant velocity (in a straight line at a constant speed), unless acted upon by an external force.\n- **Key Idea:** This law introduces the concept of **inertia**, which is the tendency of an object to resist changes in its state of motion.\n- **Example:** If you slide a book across a table, it eventually stops because of the force of friction acting on it. Without friction, the book would keep moving indefinitely.\n\n---\n\n### **2. Newton's Second Law (Law of Acceleration):**\n- **Statement:** The acceleration of an object is directly proportional to the net force acting on it and inversely proportional to its mass. Mathematically, this is expressed as:\n  \\[\n  F = ma\n  \\]\n  where:\n  - \\( F \\) = net force applied (in Newtons),\n  -"
      },
      ...
    }
  ],
  ...
}
```

Send a POST request to the route with `janedoe`'s key:

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -H 'apikey: jane-key' \
  -d '{
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "What is 1+1?" }
    ]
  }'
```

You should receive a response similar to the following:

```
{
  ...,
  "model": "deepseek-chat",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The sum of 1 and 1 is 2. This is a basic arithmetic operation where you combine two units to get a total of two units."
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 14,
    "completion_tokens": 31,
    "total_tokens": 45,
    "prompt_tokens_details": {
      "cached_tokens": 0
    },
    "prompt_cache_hit_tokens": 0,
    "prompt_cache_miss_tokens": 14
  },
  "system_fingerprint": "fp_3a5770e1b4_prod0225"
}
```

Since the `total_tokens` value exceeds the configured quota of the `deepseek` instance for `janedoe`, the next request within the 60-second window from `janedoe` is expected to be forwarded to the `openai` instance.

Within the same 60-second window, send another POST request to the route with `janedoe`'s key:

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -H 'apikey: jane-key' \
  -d '{
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "Explain Newtons laws to me" }
    ]
  }'
```

You should see a response similar to the following:

```
{
  ...,
  "model": "gpt-4-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Sure, here are Newton's three laws of motion:\n\n1) Newton's First Law, also known as the Law of Inertia, states that an object at rest will stay at rest, and an object in motion will stay in motion, unless acted on by an external force. In simple words, this law suggests that an object will keep doing whatever it is doing until something causes it to do otherwise. \n\n2) Newton's Second Law states that the force acting on an object is equal to the mass of that object times its acceleration (F=ma). This means that force is directly proportional to mass and acceleration. The heavier the object and the faster it accelerates, the greater the force.\n\n3) Newton's Third Law, also known as the law of action and reaction, states that for every action, there is an equal and opposite reaction. Essentially, any force exerted onto a body will create a force of equal magnitude but in the opposite direction on the object that exerted the first force.\n\nRemember, these laws become less accurate when considering speeds near the speed of light (where Einstein's theory of relativity becomes more appropriate) or objects very small or very large. However, for everyday situations, they provide a good model of how things move.",
        "refusal": null
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  ...
}
```

This shows `ai-proxy-multi` load balance the traffic with respect to the rate limiting rules in `ai-rate-limiting` by consumers.

### Rate Limit by Rules[â](#rate-limit-by-rules "Direct link to Rate Limit by Rules")

The following example demonstrates how you can configure the plugin to apply different rate-limiting rules (available from API7 Enterprise 3.8.17) based on request attributes. In this example, rate limits are applied based on HTTP header values that represent the callerâs access tier.

Note that all rules are applied sequentially. If a configured key does not exist, the corresponding rule will be skipped.

tip

In addition to HTTP headers, you can also base rules on other [built-in variables](https://docs.api7.ai/enterprise/reference/built-in-variables.md) to implement more flexible and fine-grained rate-limiting strategies.

Create a route with the `ai-rate-limiting` plugin that applies different rate limits based on request headers, allowing requests to be rate limited per subscription (`X-Subscription-ID`) and enforcing a stricter limit for trial users (`X-Trial-ID`):

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-rate-limiting-route",
    "uri": "/anything",
    "methods": ["POST"],
    "plugins": {
      "ai-proxy-multi": {
        "fallback_strategy": ["rate_limiting"],
        "instances": [
          {
            "name": "openai-instance",
            "provider": "openai",
            "priority": 1,
            "weight": 0,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$OPENAI_API_KEY"'"
              }
            },
            "options": {
              "model": "gpt-4"
            }
          },
          {
            "name": "deepseek-instance",
            "provider": "deepseek",
            "priority": 0,
            "weight": 0,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$DEEPSEEK_API_KEY"'"
              }
            },
            "options": {
              "model": "deepseek-chat"
            }
          }
        ]
      },
      "ai-rate-limiting": {
        "policy": "local",
        "rejected_code": 429,
        "rules": [
          {
            "key": "${http_x_subscription_id}",
            "count": "${http_x_custom_count ?? 500}",
            "time_window": 60
          },
          {
            "key": "${http_x_trial_id}",
            "count": 50,
            "time_window": 60
          }
        ]
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

â¶ Use the value of the `X-Subscription-ID` request header as the rate-limiting key.

â· Set the request limit dynamically based on the `X-Custom-Count` header. If the header is not provided, a default count of 500 tokens is applied.

â¸ Use the value of the `X-Trial-ID` request header as the rate-limiting key.

To verify rate limiting, send several of the following requests to the route with the same subscription ID:

```
curl "http://127.0.0.1:9080/anything" -i -X POST \
  -H "X-Subscription-ID: sub-123456789" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "What is 1+1?" }
    ]
  }'
```

These requests should match the first rule with a default token count of 500. You should see that requests within the quota return `HTTP/1.1 200 OK`, while those exceeding it return `HTTP/1.1 429 Too Many Requests`:

```
HTTP/1.1 200 OK
...
X-AI-1-RateLimit-Limit: 500
X-AI-1-RateLimit-Remaining: 499
X-AI-1-RateLimit-Reset: 60

HTTP/1.1 200 OK
...
X-AI-1-RateLimit-Limit: 500
X-AI-1-RateLimit-Remaining: 344
X-AI-1-RateLimit-Reset: 57.989000082016

HTTP/1.1 429 Too Many Requests
...
X-AI-1-RateLimit-Limit: 500
X-AI-1-RateLimit-Remaining: 0
X-AI-1-RateLimit-Reset: 5.871000051498
```

Wait for the time window to reset. Send several of the following requests to the route with the same subscription ID and set the `X-Custom-Count` header to 10:

```
curl "http://127.0.0.1:9080/anything" -i -X POST \
  -H "X-Subscription-ID: sub-123456789" \
  -H "X-Custom-Count: 10" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "What is 1+1?" }
    ]
  }'
```

These requests should match the first rule with a custom token count of 10. You should see that requests within the quota return `HTTP/1.1 200 OK`, while those exceeding it return `HTTP/1.1 429 Too Many Requests`:

```
HTTP/1.1 200 OK
...
X-AI-1-RateLimit-Limit: 10
X-AI-1-RateLimit-Remaining: 9
X-AI-1-RateLimit-Reset: 60

HTTP/1.1 429 Too Many Requests
...
X-AI-1-RateLimit-Limit: 10
X-AI-1-RateLimit-Remaining: 0
X-AI-1-RateLimit-Reset: 40.422000169754
```

Finally, send several of the following requests to the route without any header:

```
curl "http://127.0.0.1:9080/anything" -i -X POST \
  -H "X-Trial-ID: trial-123456789" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "What is 1+1?" }
    ]
  }'
```

These requests should match the second rule with a token count of 50. You should see that requests within the quota return `HTTP/1.1 200 OK`, while those exceeding it return `HTTP/1.1 429 Too Many Requests`:

```
HTTP/1.1 200 OK
...
X-AI-2-RateLimit-Limit: 50
X-AI-2-RateLimit-Remaining: 49
X-AI-2-RateLimit-Reset: 60

HTTP/1.1 429 Too Many Requests
...
X-AI-2-RateLimit-Limit: 50
X-AI-2-RateLimit-Remaining: 0
X-AI-2-RateLimit-Reset: 44
```

### Share Quota Among Gateways with a Redis Server[â](#share-quota-among-gateways-with-a-redis-server "Direct link to Share Quota Among Gateways with a Redis Server")

The following example demonstrates how to configure distributed rate limiting across multiple gateway instances. This is particularly useful in production environments where you need cluster-wide rate limiting consistency.

This example applies to API7 Enterprise version 3.8.19 and later. It is not applicable to APISIX, as the `policy` feature is not yet supported.

#### Prerequisites[â](#prerequisites "Direct link to Prerequisites")

Before configuring Redis-based rate limiting, start a Redis instance.

```
docker run -d --name redis-standalone \
  -p 6379:6379 \
  -e REDIS_PASSWORD=p@ssw0rd \
  redis:7-alpine redis-server --requirepass p@ssw0rd
```

Then verify the Redis connection.

```
docker exec -it redis-standalone redis-cli -a p@ssw0rd ping
```

You should receive a response `PONG`, which shows successful connection.

#### Create Route and Configure Rate Limiting[â](#create-route-and-configure-rate-limiting "Direct link to Create Route and Configure Rate Limiting")

Create a route with the following configurations in the gateway group:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-rate-limiting-redis-route",
    "uri": "/anything",
    "methods": ["POST"],
    "plugins": {
      "ai-proxy-multi": {
        "instances": [
          {
            "name": "deepseek-instance",
            "provider": "deepseek",
            "weight": 8,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$DEEPSEEK_API_KEY"'"
              }
            },
            "options": {
              "model": "deepseek-chat"
            }
          },
          {
            "name": "openai-instance",
            "override": {
              "endpoint": "https://openrouter.ai/api/v1/chat/completions"
            },
            "provider": "openai-compatible",
            "weight": 2,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$OPENAI_API_KEY"'"
              }
            },
            "options": {
              "model": "gpt-4"
            }
          }
        ]
      },
      "ai-rate-limiting": {
        "instances": [
          {
            "name": "deepseek-instance",
            "limit_strategy": "total_tokens",
            "limit": 100,
            "time_window": 30
          },
          {
            "name": "openai-instance",
            "limit_strategy": "total_tokens",
            "limit": 50,
            "time_window": 30
          }
        ],
        "policy": "redis",
        "redis_host": "127.0.0.1",
        "redis_port": 6379,
        "redis_password": "p@ssw0rd",
        "allow_degradation": false,
        "rejected_code": 429
      }
    }
  }'
```

â¶ `policy`: Set to `redis` to use a Redis instance for rate limiting.

â· `redis_host`: Set to the Redis instance IP address.

â¸ `redis_port`: Set to Redis instance listening port.

â¹ `redis_password`: Set to the password of the Redis instance, if any.

âº `allow_degradation`: Set to `false` to reject requests if Redis is unavailable.

#### Verify[â](#verify "Direct link to Verify")

Send a POST request to the route with a system prompt and a sample user question in the request body.

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "What is 1+1?" }
    ]
  }'
```

You should see a response similar to the following:

```
{
  ...,
  "model": "deepseek-chat",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "In mathematics, under the usual rules of arithmetic, **1 + 1 = 2**.\n\nThis follows from the definition of natural numbers and addition in systems like Peano arithmetic, where:\n\n- 1 is the successor of 0.\n- 2 is the successor of 1.\n- Addition is defined recursively so that 1 + 1 = S(0) + S(0) = S(S(0)) = 2.\n\nIn different contexts, the answer might vary (e.g., in Boolean algebra, 1 + 1 = 1 for logical OR; in modular arithmetic mod 2, 1 + 1 = 0), but in standard arithmetic, the answer is **2**."
        },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  ...
}
```

Generate 3 requests to consume the quota:

```
for i in {1..3}; do
  curl -i "http://127.0.0.1:9080/anything" \
    -H "Content-Type: application/json" \
    -d '{
      "messages": [
        { "role": "system", "content": "You are a mathematician" },
        { "role": "user", "content": "What is 1+1?" }
      ]
    }' &
  sleep 1
done
wait
```

You should receive `HTTP/1.1 200 OK` responses. After consuming the rate limit quota, subsequent requests will be rejected. You should receive a `429 Too Many Requests` response when the rate limit is exceeded.

### Share Quota Among Gateway Nodes with a Redis Cluster[â](#share-quota-among-gateway-nodes-with-a-redis-cluster "Direct link to Share Quota Among Gateway Nodes with a Redis Cluster")

The following example demonstrates how to enable multiple gateway nodes to share the same rate limiting quota through a Redis cluster.

This example applies to API7 Enterprise version 3.8.19 and later. It is not applicable to APISIX, as the `policy` feature is not yet supported.

#### Prerequisites[â](#prerequisites-1 "Direct link to Prerequisites")

1. Create a Docker network:

   ```
   docker network create redis-cluster-network
   ```

   Ensure that your gateway instance is running within the same network as your Redis cluster.

2. Start 6 Redis nodes and wait for them to start:

   ```
   for port in $(seq 7000 7005); do
     docker run -d \
       --name redis-node-$port \
       --network redis-cluster-network \
       -p $port:$port \
       redis:7.2-alpine \
       redis-server \
       --port $port \
       --cluster-enabled yes \
       --cluster-config-file nodes.conf \
       --cluster-node-timeout 5000 \
       --appendonly yes \
       --requirepass redis-cluster-password \
       --masterauth redis-cluster-password
   done && sleep 5
   ```

3. Create a cluster:

   ```
   docker run --rm \
     --network redis-cluster-network \
     redis:7.2-alpine \
     sh -c "
     redis-cli \
     --cluster create \
     $(for port in $(seq 7000 7005); do echo -n \"redis-node-$port:$port \"; done) \
     --cluster-replicas 1 \
     --cluster-yes \
     -a redis-cluster-password
     "
   ```

   The expected output should be similar to the following:

   ```
   ...,
   [OK] All nodes agree about slots configuration.
   >>> Check for open slots...
   >>> Check slots coverage...
   [OK] All 16384 slots covered.
   ```

4. Verify cluster nodes:

   ```
   docker exec -it redis-node-7000 redis-cli -c -a redis-cluster-password -p 7000 cluster nodes
   ```

   The expected output should be similar to the following:

   ```
   node-id-1 172.XX.0.2:7000@17000 myself,master - 0 0 1 connected 0-5460
   node-id-2 172.XX.0.3:7001@17001 master - 0 0 2 connected 5461-10922
   node-id-3 172.XX.0.4:7002@17002 master - 0 0 3 connected 10923-16383
   node-id-4 172.XX.0.5:7003@17003 slave node-id-1 0 0 1 connected
   node-id-5 172.XX.0.6:7004@17004 slave node-id-2 0 0 2 connected
   node-id-6 172.XX.0.7:7005@17005 slave node-id-3 0 0 3 connected
   ```

5. Check cluster health (optional):

   ```
   docker exec redis-node-7000 redis-cli -c -a redis-cluster-password -p 7000 cluster info
   ```

   You should see the following response:

   ```
   cluster_state:ok
   cluster_slots_assigned:16384
   cluster_slots_ok:16384
   cluster_known_nodes:6
   cluster_size:3
   ...
   ```

#### Create Route and Configure Rate Limiting[â](#create-route-and-configure-rate-limiting-1 "Direct link to Create Route and Configure Rate Limiting")

Create a route with the following configurations in the gateway group:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-rate-limiting-redis-route",
    "uri": "/anything",
    "methods": ["POST"],
    "plugins": {
      "ai-proxy-multi": {
        "instances": [
          {
            "name": "deepseek-instance",
            "provider": "deepseek",
            "weight": 8,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$DEEPSEEK_API_KEY"'"
              }
            },
            "options": {
              "model": "deepseek-chat"
            }
          },
          {
            "name": "openai-instance",
            "override": {
              "endpoint": "https://openrouter.ai/api/v1/chat/completions"
            },
            "provider": "openai-compatible",
            "weight": 2,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$OPENAI_API_KEY"'"
              }
            },
            "options": {
              "model": "gpt-4"
            }
          }
        ]
      },
      "ai-rate-limiting": {
        "instances": [
          {
            "name": "deepseek-instance",
            "limit_strategy": "total_tokens",
            "limit": 200,
            "time_window": 60
          },
          {
            "name": "openai-instance",
            "limit_strategy": "total_tokens",
            "limit": 100,
            "time_window": 60
          }
        ],
        "policy": "redis-cluster",
        "redis_cluster_nodes": [
          "172.XX.0.2:7000",
          "172.XX.0.3:7001",
          "172.XX.0.4:7002",
          "172.XX.0.5:7003",
          "172.XX.0.6:7004",
          "172.XX.0.7:7005"
        ],
        "redis_password": "redis-cluster-password",
        "redis_cluster_name": "redis-cluster-1",
        "redis_timeout": 1000,
        "redis_connect_timeout": 1000,
        "allow_degradation": false,
        "rejected_code": 429
      }
    }
  }'
```

â¶ `policy`: Set to `redis-cluster` to use a Redis cluster for rate limiting.

â· `redis_cluster_nodes`: Set to Redis node addresses in the Redis cluster.

â¸ `redis_password`: Set to the password of the Redis cluster, if any.

â¹ `redis_cluster_name`: Set to the Redis cluster name.

#### Verify[â](#verify-1 "Direct link to Verify")

Send a POST request to the route with a system prompt and a sample user question in the request body.

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "What is 1+1?" }
    ]
  }'
```

You should see a response similar to the following:

```
{
  ...,
  "model": "deepseek-chat",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "In mathematics, under the usual rules of arithmetic, **1 + 1 = 2**.\n\nThis follows from the definition of natural numbers and addition in systems like Peano arithmetic, where:\n\n- 1 is the successor of 0.\n- 2 is the successor of 1.\n- Addition is defined recursively so that 1 + 1 = S(0) + S(0) = S(S(0)) = 2.\n\nIn different contexts, the answer might vary (e.g., in Boolean algebra, 1 + 1 = 1 for logical OR; in modular arithmetic mod 2, 1 + 1 = 0), but in standard arithmetic, the answer is **2**."
        },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  ...
}
```

Generate 3 requests to consume the quota:

```
for i in {1..3}; do
  curl -i "http://127.0.0.1:9080/anything" \
    -H "Content-Type: application/json" \
    -d '{
      "messages": [
        { "role": "system", "content": "You are a mathematician" },
        { "role": "user", "content": "What is 1+1?" }
      ]
    }' &
  sleep 1
done
wait
```

You should receive `HTTP/1.1 200 OK` responses for most requests, with the remainder being `HTTP 429 Too Many Requests` responses. This verifies routes configured in different gateway nodes share the same quota.

Verify that the rate limiting counters are being stored in the Redis cluster by checking all nodes for rate limiting keys:

```
for port in {7000..7005}; do
  echo "Checking node redis-node-$port:"
  docker exec redis-node-$port redis-cli -c -a redis-cluster-password -p $port keys "plugin-ai-rate-limiting*" 2>/dev/null | grep -v "^$" || echo "No related keys found"
done
```

You should see output similar to the following:

```
Checking node redis-node-7000:
No related keys found
Checking node redis-node-7001:
No related keys found
Checking node redis-node-7002:
plugin-ai-rate-limitingroute&service<route-id>&<service-id>:<timestamp>:<client-ip>:<rate-limit-instance>
Checking node redis-node-7003:
plugin-ai-rate-limitingroute&service<route-id>&<service-id>:<timestamp>:<client-ip>:<rate-limit-instance>
Checking node redis-node-7004:
No related keys found
Checking node redis-node-7005:
No related keys found
```

### Share Quota Among Gateway Nodes with a Redis Sentinel[â](#share-quota-among-gateway-nodes-with-a-redis-sentinel "Direct link to Share Quota Among Gateway Nodes with a Redis Sentinel")

This example applies to API7 Enterprise version 3.9.2 and later. It is not applicable to APISIX, as the `policy` feature is not yet supported.

Use Redis Sentinel when you need automatic failover and high availability but don't require data sharding. This pattern is simpler to manage and suitable for most high-availability requirements.

Ensure that your Redis instances are running in [Sentinel mode](https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/).

#### Prerequisites[â](#prerequisites-2 "Direct link to Prerequisites")

1. Create a Docker network:

   ```
   docker network create redis-sentinel-network
   ```

   Ensure that your gateway instance is running within the same network as your Redis Sentinel cluster.

2. Start a Redis master node:

   ```
   docker run -d --name redis-master --network redis-sentinel-network \
     -p 6379:6379 \
     redis:7.2-alpine \
     redis-server --requirepass StrongP@ss123 --appendonly yes
   ```

3. Start Sentinel replica nodes:

   ```
   for i in 1 2; do
     PORT=$((6380 + i - 1))
     docker run -d --name redis-slave-$i --network redis-sentinel-network \
       -p $PORT:6379 \
       redis:7.2-alpine \
       redis-server --slaveof redis-master 6379 \
                   --requirepass StrongP@ss123 \
                   --masterauth StrongP@ss123 \
                   --appendonly yes
   done
   ```

4. Get master node IP address for next step:

   ```
   MASTER_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' redis-master)
   echo "Redis master node IP: $MASTER_IP"
   ```

5. Start Sentinel cluster and replace `$MASTER_IP` with your master node IP:

   ```
   for i in 1 2 3; do
     docker run -d --name redis-sentinel-$i --network redis-sentinel-network -p $((26378+i-1)):26379 \
       redis:7.2-alpine \
       sh -c "
   cat << 'EOF' > /sentinel.conf
   port 26379
   sentinel monitor mymaster $MASTER_IP 6379 2
   sentinel auth-pass mymaster StrongP@ss123
   requirepass admin-password
   sentinel down-after-milliseconds mymaster 5000
   sentinel failover-timeout mymaster 10000
   sentinel parallel-syncs mymaster 1
   protected-mode no
   EOF
   redis-sentinel /sentinel.conf
   "
   done
   echo "â Sentinel cluster started successfully."
   ```

   You can see the following response:

   ```
   Starting redis-sentinel-1 (port:26379)...
   eb9efacb629d0cfdfaa48856f42ba8c67642baa79f1589df5b251c11d3ec6e1a
   Starting redis-sentinel-2 (port:26380)...
   7f23f4b6e63c9b6be4c5e1903a244f078d481952a1465a9650c743ea2ee4600f
   Starting redis-sentinel-3 (port:26381)...
   1df087502124e3903df7ae665ef597bf735669c5ce3f9d87696c4acd82526626
   â Sentinel cluster started successfully.
   ```

6. Confirm the Sentinel environment is running correctly:

   ```
   echo "Waiting for Sentinel cluster establishment (10 seconds)..."
   sleep 10

   echo -e "\nVerifying Sentinel cluster status:"
   for i in 1 2 3; do
     echo "--- Sentinel $i status ---"
     if docker ps | grep -q "redis-sentinel-$i"; then
       echo "Container: â Running"
       docker exec redis-sentinel-$i redis-cli -p 26379 SENTINEL master mymaster 2>&1 | grep -E "(flags|num-slaves|num-other-sentinels)"
     else
       echo "Container: â Not running (run 'docker logs redis-sentinel-$i' to check)"
     fi
     echo ""
   done
   ```

   You can see the following response:

   ```
   Verifying Sentinel cluster status:
   --- Sentinel 1 status ---
   Container: â Running

   --- Sentinel 2 status ---
   Container: â Running

   --- Sentinel 3 status ---
   Container: â Running
   ```

7. Get Sentinel IP addresses for plugin configuration:

   ```
   echo -e "Getting Sentinel container IP addresses:"
   for i in 1 2 3; do
     IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' redis-sentinel-$i)
     echo "  redis-sentinel-$i : $IP"
   done
   ```

   You can see the following response:

   ```
   Getting Sentinel container IP addresses:
     redis-sentinel-1 : 172.22.0.4
     redis-sentinel-2 : 172.22.0.5
     redis-sentinel-3 : 172.22.0.6
   ```

8. Conduct detailed status check:

   ```
   echo "Checking detailed Sentinel cluster status..."
   for i in 1 2 3; do
     echo "=== Sentinel $i details ==="
     docker exec redis-sentinel-$i redis-cli -p 26379 SENTINEL master mymaster
     echo ""
   done
   ```

   You can see the following response:

   ```
   Checking detailed Sentinel cluster status...

   === Sentinel 1 Details ===
   name: mymaster
   ip: 172.22.0.2
   port: 6379
   runid: ${YOUR_RUN_ID}
   flags: master
   link-pending-commands: 0
   link-refcount: 1
   last-ping-sent: 0
   last-ok-ping-reply: 113
   last-ping-reply: 113
   down-after-milliseconds: 5000
   info-refresh: 6979
   role-reported: master
   role-reported-time: 107360
   config-epoch: 0
   num-slaves: 1
   num-other-sentinels: 2
   quorum: 2
   failover-timeout: 10000
   parallel-syncs: 1
   ...
   ```

#### Create Route and Configure Rate Limiting[â](#create-route-and-configure-rate-limiting-2 "Direct link to Create Route and Configure Rate Limiting")

Create a route with the following configurations in the gateway group:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-rate-limiting-redis-route",
    "uri": "/anything",
    "methods": ["POST"],
    "plugins": {
      "ai-proxy-multi": {
        "instances": [
          {
            "name": "deepseek-instance",
            "provider": "deepseek",
            "weight": 8,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$DEEPSEEK_API_KEY"'"
              }
            },
            "options": {
              "model": "deepseek-chat"
            }
          },
          {
            "name": "openai-instance",
            "override": {
              "endpoint": "https://openrouter.ai/api/v1/chat/completions"
            },
            "provider": "openai-compatible",
            "weight": 2,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$OPENAI_API_KEY"'"
              }
            },
            "options": {
              "model": "gpt-4"
            }
          }
        ]
      },
      "ai-rate-limiting": {
        "instances": [
          {
            "name": "deepseek-instance",
            "limit_strategy": "total_tokens",
            "limit": 100,
            "time_window": 60
          },
          {
            "name": "openai-instance",
            "limit_strategy": "total_tokens",
            "limit": 100,
            "time_window": 60
          }
        ],
        "policy": "redis-sentinel",
        "redis_sentinels": [
          {"host": "172.22.0.4", "port": 26379},
          {"host": "172.22.0.5", "port": 26379},
          {"host": "172.22.0.6", "port": 26379}
        ],
        "redis_master_name": "mymaster",
        "redis_password": "StrongP@ss123",
        "redis_role": "master",
        "sentinel_username": "admin",
        "sentinel_password": "admin-password",
        "rejected_code": 429
      }
    }
  }'
```

â¶ `policy`: Set to `redis-sentinel` to use a Redis in sentinel mode for rate limiting.

â· `redis_sentinels`: Configure a list of Sentinel node addresses (host and port).

â¸ `redis_master_name`: Configure the name of the Redis master group that Sentinels are monitoring.

â¹ `redis_password`: Set to the password of the Redis instance, if any.

âº `redis_role`: Set to `master` to connect to the current Redis master.

â» `sentinel_username`: Configure the username used to authenticate with Redis Sentinel.

â¼ `sentinel_password`: Configure the password used to authenticate with Redis Sentinel.

#### Verify[â](#verify-2 "Direct link to Verify")

Send a POST request to the route with a system prompt and a sample user question in the request body.

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "What is 1+1?" }
    ]
  }'
```

You should see a response similar to the following:

```
{
  ...,
  "model": "deepseek-chat",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "In mathematics, under the usual rules of arithmetic, **1 + 1 = 2**.\n\nThis follows from the definition of natural numbers and addition in systems like Peano arithmetic, where:\n\n- 1 is the successor of 0.\n- 2 is the successor of 1.\n- Addition is defined recursively so that 1 + 1 = S(0) + S(0) = S(S(0)) = 2.\n\nIn different contexts, the answer might vary (e.g., in Boolean algebra, 1 + 1 = 1 for logical OR; in modular arithmetic mod 2, 1 + 1 = 0), but in standard arithmetic, the answer is **2**."
        },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  ...
}
```

Generate 3 requests to consume the quota:

```
for i in {1..3}; do
  curl -i "http://127.0.0.1:9080/anything" \
    -H "Content-Type: application/json" \
    -d '{
      "messages": [
        { "role": "system", "content": "You are a mathematician" },
        { "role": "user", "content": "What is 1+1?" }
      ]
    }' &
  sleep 1
done
wait
```

You should receive `HTTP/1.1 200 OK` responses. After consuming the rate limit quota, subsequent requests will be rejected. You should receive a `429 Too Many Requests` response when the rate limit is exceeded.
