# Source: https://mastra.ai/guides/migrations/upgrade-to-v1/voice

# Voice Packages

Voice packages have been renamed from speech to voice with updated class names and API methods.

## Changed

### Voice configuration property names

Voice configuration properties have been renamed for consistency. `speakProvider` is now `output`, `listenProvider` is now `input`, and `realtimeProvider` is now `realtime`. This change provides more intuitive property names.

To migrate, update configuration property names when configuring agents with voice capabilities.

```diff
const agent = new Agent({
    voice: {
-     speakProvider: murfVoice,
-     listenProvider: deepgramVoice,
-     realtimeProvider: openaiRealtime,
+     output: murfVoice,
+     input: deepgramVoice,
+     realtime: openaiRealtime,
    },
  });
```

> **Codemod:** You can use Mastra's codemod CLI to update your code automatically:
>
> ```bash
> npx @mastra/codemod@latest v1/voice-property-names .
> ```