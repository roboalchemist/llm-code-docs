# set api keys
os.environ["DEEPGRAM_API_KEY"] = ""
audio_file = open("/path/to/audio.mp3", "rb")

response = transcription(model="deepgram/nova-2", file=audio_file)

print(f"response: {response}")

```

### **Fireworks AI - Vision** support for all models [​](https://docs.litellm.ai/release_notes/tags/dependency-upgrades\#fireworks-ai---vision-support-for-all-models "Direct link to fireworks-ai---vision-support-for-all-models")

LiteLLM supports document inlining for Fireworks AI models. This is useful for models that are not vision models, but still need to parse documents/images/etc.
LiteLLM will add `#transform=inline` to the url of the image\_url, if the model is not a vision model [See Code](https://github.com/BerriAI/litellm/blob/1ae9d45798bdaf8450f2dfdec703369f3d2212b7/litellm/llms/fireworks_ai/chat/transformation.py#L114)

## Proxy Admin UI [​](https://docs.litellm.ai/release_notes/tags/dependency-upgrades\#proxy-admin-ui "Direct link to Proxy Admin UI")

- `Test Key` Tab displays `model` used in response

- `Test Key` Tab renders content in `.md`, `.py` (any code/markdown format)

## Dependency Upgrades [​](https://docs.litellm.ai/release_notes/tags/dependency-upgrades\#dependency-upgrades "Direct link to Dependency Upgrades")

- (Security fix) Upgrade to `fastapi==0.115.5` [https://github.com/BerriAI/litellm/pull/7447](https://github.com/BerriAI/litellm/pull/7447)

## Bug Fixes [​](https://docs.litellm.ai/release_notes/tags/dependency-upgrades\#bug-fixes "Direct link to Bug Fixes")

- Add health check support for realtime models [Here](https://docs.litellm.ai/docs/proxy/health#realtime-models)
- Health check error with audio\_transcription model [https://github.com/BerriAI/litellm/issues/5999](https://github.com/BerriAI/litellm/issues/5999)

## Docker Image Release Notes
[Skip to main content](https://docs.litellm.ai/release_notes/tags/docker-image#__docusaurus_skipToContent_fallback)

`docker image`, `security`, `vulnerability`