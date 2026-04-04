# Source: https://www.promptfoo.dev/docs/red-team/strategies/best-of-n/

# Best-of-N (BoN) Jailbreaking Strategy

Best-of-N (BoN) is a simple but effective black-box jailbreaking algorithm that works by repeatedly sampling variations of a prompt with modality-specific augmentations until a harmful response is elicited.

Introduced by [Hughes et al. (2024)](https://arxiv.org/abs/2412.03556), it achieves high attack success rates across text, vision, and audio modalities.

<div class="theme-admonition theme-admonition-tip">
  <div class="admonitionHeading">tip</div>
  <div class="admonitionContent">
    While this technique achieves high attack success rates - 89% on GPT-4o and 78% on Claude 3.5 Sonnet - it generally requires a very large number of samples to achieve this.
  </div>
</div>

Use it like so in your `promptfooconfig.yaml`:

```yaml
strategies:
  - id: best-of-n
    config:
      useBasicRefusal: false
      maxConcurrency: 3  # Maximum concurrent API calls (default)
      nSteps: 10000  # Maximum number of attempts (optional)
      maxCandidatesPerStep: 1  # Maximum candidates per batch (optional)
```

## How It Works

![BoN Overview](https://promptfoo.dev/docs/red-team/strategies/best-of-n/data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4MDAgNjAwIj4KICA8IS0tIEJhY2tncm91bmQgLS0+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI2MDAiIGZpbGw9IiNmZmZmZmYiLz4KICAKICA8IS0tIFRpdGxlIC0tPgogIDx0ZXh0IHg9IjQwMCIgeT0iNTAiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIyNCIgZm9udC13ZWlnaHQ9ImJvbGQiPkJlc3Qtb2YtTiBKYWlsYnJlYWtpbmcgQ3ljbGU8L3RleHQ+CgogIDwhLS0gQ2VudGVyIHBvaW50IGZvciByb3RhdGlvbiBjYWxjdWxhdGlvbnMgLS0+CiAgPCEtLSBjeD00MDAsIGN5PTMyNSAtLT4KICAKICA8IS0tIExhcmdlIGNpcmNsZSBiYWNrZ3JvdW5kIC0tPgogIDxjaXJjbGUgY3g9IjQwMCIgY3k9IjMyNSIgcj0iMjAwIiBmaWxsPSJub25lIiBzdHJva2U9IiNkZGQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWRhc2hhcnJheT0iNSw1Ii8+CgogIDwhLS0gT3JpZ2luYWwgUmVxdWVzdCAtLT4KICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSg0MDAsMTI1KSI+CiAgICA8cmVjdCB4PSItOTAiIHk9Ii0zMCIgd2lkdGg9IjE4MCIgaGVpZ2h0PSI2MCIgcng9IjUiIGZpbGw9IiNlNmYzZmYiIHN0cm9rZT0iIzIxOTZmMyIgc3Ryb2tlLXdpZHRoPSIyIi8+CgogIDwhLS0gT3JpZ2luYWwgUmVxdWVzdCAtLT4KICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNTAsNDI1KSI+CiAgICA8cmVjdCB4PSItOTAiIHk9Ii05MCIgd2lkdGg9IjE4MCIgaGVpZ2h0PSI4MCIgcng9IjUiIGZpbGw9IiNmM2U1ZjUiIHN0cm9rZT0iIzljMjdiMCIgc3Ryb2tlLXdpZHRoPSIyIi8+CgogIDx0ZXh0IHg9IjAiIHk9IjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNCI+TGFuZ3VhZ2UgTW9kZWw8L3RleHQ+CiAgPC9nPgoKICA8IS0tIEFwcGx5IEF1Z21lbnRhdGlvbnMgLS0+CiAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoNjUwLDIyNSkiPgogICAgPHJlY3QgeD0iLTkwIiB5PSItNDAiIHdpZHRoPSIxODAiIGhlaWdodD0iODAiIHJ4PSI1IiBmaWxsPSIjZmZmM2U2IiBzdHJva2U9IiNmZjk4MDAiIHN0cm9rZS13aWR0aD0iMiIvPgogICAgPHRleHQgeD0iMCIgeT0iLTIwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LWZhbWlseT0iQXJpYWwiIGZvbnQtc2l6ZT0iMTQiPkhhcm0gQ2xhc3NpZmllcjwvdGV4dD4KICA8L2c+CgogIDwhLS0gTiBDb3VudGVyIEJveCAtLT4KICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNTAsMjI1KSI+CiAgICA8cmVjdCB4PSItOTAiIHk9Ii0zMCIgd2lkdGg9IjE4MCIgaGVpZ2h0PSI2MCIgcng9IjUiIGZpbGw9IiNmNWY1ZjUiIHN0cm9rZT0iIzY2NiIgc3Ryb2tlLXdpZHRoPSIyIi8+CgogICA8dGV4dCB4PSIwIiB5PSI1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LWZhbWlseT0iQXJpYWwiIGZvbnQtc2l6ZT0iMTQiPkFwcGx5IEF1Z21lbnRhdGlvbnM8L3RleHQ+CiAgICA8dGV4dCB4PSIwIiB5PSIwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LWZhbWlseT0iQXJpYWwiIGZvbnQtc2l6ZT0iMTIiPuKAoiBSYW5kb20gY2FwaXRhbGl6YXRpb248L3RleHQ+CiAgICA8dGV4dCB4PSIwIiB5PSIyMCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjEyIj7igKIgQ2hhcmFjdGVyIHNjcmFtYmxpbmc8L3RleHQ+CiAgICA8dGV4dCB4PSIwIiB5PSI0MCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjEyIj7igKIgQVNDSUkgbm9pc2U8L3RleHQ+CiAgPC9nPgoKICA8IS0tIExhbmd1YWdlIE1vZGVsIC0tPgogIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDY1MCw0MjUpIj4KICAgIDxyZWN0IHg9Ii05MCIgeT0iLTMwIiB3aWR0aD0iMTgwIiBoZWlnaHQ9IjYwIiByeD0iNSIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjNGNhZjUwIiBzdHJva2Utd2lkdGg9IjIiLz4KICAgIDx0ZXh0IHg9IjAiIHk9IjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNCI+TGFuZ3VhZ2UgTW9kZWw8L3RleHQ+CiAgPC9nPgoKICA8IS0tIFJlc3BvbnNlIC0tPgogIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQwMCw1MjUpIj4KICAgIDxyZWN0IHg9Ii05MCIgeT0iLTMwIiB3aWR0aD0iMTgwIiBoZWlnaHQ9IjYwIiByeD0iNSIgZmlsbD0iI2ZjZTRlYyIgc3Ryb2tlPSIjZTkxZTYzIiBzdHJva2Utd2lkdGg9IjIiLz4KICAgIDx0ZXh0IHg9IjAiIHk9IjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNCI+UmVzcG9uc2U8L3RleHQ+CiAgPC9nPgoKICA8IS0tIEhhcm0gQ2xhc3NpZmllciAtLT4KICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNTAsMjI1KSI+CiAgICA8cmVjdCB4PSItOTAiIHk9Ii0zMCIgd2lkdGg9IjE4MCIgaGVpZ2h0PSI2MCIgcng9IjUiIGZpbGw9IiNmM2U1ZjUiIHN0cm9rZT0iIzY2NiIgc3Ryb2tlLXdpZHRoPSIyIi8+CgogICAgPHRleHQgeD0iMCIgeT0iLTIwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LWZhbWlseT0iQXJpYWwiIGZvbnQtc2l6ZT0iMTQiPkhhcm0gQ2xhc3NpZmllcjwvdGV4dD4KICA8L2c+CgogIDwhLS0gTiBDb3VudGVyIEJveCAtLT4KICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNTAsNDI1KSI+CiAgICA8cmVjdCB4PSItOTAiIHk9Ii00MCIgd2lkdGg9IjE4MCIgaGVpZ2h0PSI4MCIgcng9IjUiIGZpbGw9IiNmNWY1ZjUiIHN0cm9rZT0iIzY2NiIgc3Ryb2tlLXdpZHRoPSIyIi8+CgogICA8dGV4dCB4PSIwIiB5PSI1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LWZhbWlseT0iQXJpYWwiIGZvbnQtc2l6ZT0iMTQiPkFwcGx5IEF1Z21lbnRhdGlvbnM8L3RleHQ+CiAgICA8dGV4dCB4PSIwIiB5PSItMTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNCI+U2FtcGxlIENvdW50ZXI8L3RleHQ+CiAgICA8dGV4dCB4PSIwIiB5PSIxNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjE0IiBmb250LXdlaWdodD0iYm9sZCI+TiByZW1haW5pbmc8L3RleHQ+CiAgPC9nPgoKICA8IS0tIENvbm5lY3RpbmcgQXJyb3dzIC0tPgogIDwhLS0gRGVmaW5lIGFycm93IG1hcmtlciAtLT4KICA8ZGVmcz4KICAgIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjEwIiBtYXJrZXJIZWlnaHQ9IjciIHJlZlg9IjkiIHJlZlk9IjMuNSIgb3JpZW50PSJhdXRvIj4KICAgICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDEwIDMuNSwgMCA3IiBmaWxsPSIjNjY2Ii8+CgAgICA8L21hcmtlcj4KICA8L2RlZnM+CgogIDwhLS0gQXJyb3dzIGNvbm5lY3RpbmcgdGhlIGNvbXBvbmVudHMgLS0+CiAgPGcgc3Ryb2tlPSIjNjY2IiBzdHJva2Utd2lkdGg9IjIiIGZpbGw9Im5vbmUiPgogICAgPCEtLSBPcmlnaW5hbCBSZXF1ZXN0IHRvIEF1Z21lbnRhdGlvbnMgLS0+CiAgICA8cGF0aCBkPSJNIDQ5MCAxMjUgUSA2MDAgMTI1IDY1MCAxODUiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIvPgogICAgPCEtLSBBdWdtZW50YXRpb25zIHRvIE1vZGVsIC0tPgogICAgPHBhdGggZD0iTSA2NTAgMjY1IEwgNjUwIDM5NSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIi8+CiAgICA8IS0tIE1vZGVsIHRvIFJlc3BvbnNlIC0tPgogICAgPHBhdGggZD0iTSA1NjAgNDI1IFEgNTAwIDQyNSA0MDAgNDk1IiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiLz4KICAgIDwhLS0gUmVzcG9uc2UgdG8gQ2xhc3NpZmllciAtLT4KICAgIDxwYXRoIGQ9Ik0gMzEwIDUyNSBRIDIwMCA1MjUgMTUwIDQ1NSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIi8+CiAgICA8IS0tIENsYXNzaWZpZXIgdG8gQ291bnRlciAtLT4KICAgIDxwYXRoIGQ9Ik0gMTUwIDM5NSBMIDE1MCAyNjUiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIvPgogICAgPCEtLSBDb3VudGVyIGJhY2sgdG8gQXVnbWVudGF0aW9ucyAoaWYgTj4wKSAtLT4KICAgIDxwYXRoIGQ9Ik0gMjQwIDIyNSBRIDQwMCAyMjUgNTYwIDIyNSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIi8+CiAgPC9nPgoKICA8IS0tIFN1Y2Nlc3MvRmFpbCBMYWJlbHMgLS0+CiAgPHRleHQgeD0iNDAwIiB5PSIyMDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzY2NiI+SWYgTiA+IDAgYW5kIG5vdCBoYXJtZnVsPC90ZXh0PgogIDx0ZXh0IHg9IjQwMCIgeT0iMjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LWZhbWlseT0iQXJpYWwiIGZvbnQtc2l6ZT0iMTIiIGZpbGw9IiM2NjYiPlRyeSBuZXh0IHZhcmlhdGlvbjwvdGV4dD4KPC9zdmc+Cg==</div>

BoN Jailbreaking works through a simple three-step process:

1. **Generate Variations**: Creates multiple versions of the input prompt using modality-specific augmentations:
    - Text: Random capitalization, character scrambling, character noising
    - Vision: Font variations, background colors, text positioning
    - Audio: Speed, pitch, volume, background noise modifications
2. **Concurrent Testing**: Tests multiple variations simultaneously against the target model
3. **Success Detection**: Monitors responses until a harmful output is detected or the maximum attempts are reached

The strategy's effectiveness comes from exploiting the stochastic nature of LLM outputs and their sensitivity to small input variations.

## Configuration Parameters

### useBasicRefusal

**Type:** `boolean`  
**Default:** `false`

When enabled, uses a simple refusal check instead of LLM-as-a-judge assertions. This is much faster and cheaper than using an LLM judge, making it ideal for testing when the typical response of an LLM to a prompt is a refusal.

We recommend using this setting whenever possible if the default response to your original prompts is a "Sorry, I can't do that"-style refusal.

### maxConcurrency

**Type:** `number`  
**Default:** `3`

Maximum number of prompt variations to test simultaneously. Higher values increase throughput. We recommend setting this as high as your rate limits allow.

### nSteps

**Type:** `number`  
**Default:** `undefined`

Maximum number of total attempts before giving up. Each step generates `maxCandidatesPerStep` variations. Higher values increase success rate but also cost. The original paper achieved best results with 10,000 steps.

### maxCandidatesPerStep

**Type:** `number`  
**Default:** `1`

Number of prompt variations to generate in each batch. Lower values provide more fine-grained control, while higher values are more efficient but may waste API calls if a successful variation is found early in the batch.

Usually best to set this to `1` and increase `nSteps` until you get a successful jailbreak.

<div class="theme-admonition theme-admonition-tip">
  <div class="admonitionHeading">tip</div>
  <div class="admonitionContent">
    For initial testing, we recommend starting with `useBasicRefusal: true` and relatively low values for `nSteps` and `maxCandidatesPerStep`. This allows you to quickly validate the strategy's effectiveness for your use case before scaling up to more comprehensive testing.
  </div>
</div>

## Performance

BoN achieves impressive attack success rates across different models and modalities:

- Text: 89% on GPT-4, 78% on Claude 3.5 Sonnet (10,000 samples)
- Vision: 56% on GPT-4 Vision
- Audio: 72% on GPT-4 Audio

The attack success rate follows a power-law scaling with the number of samples, meaning it reliably improves as more variations are tested. This illustrates why [ASR comparisons must account for attempt budget](/blog/asr-not-portable-metric/): a 1% per-attempt method becomes 98% with 392 tries.

## Key Features

- **Simple Implementation**: No need for gradients or model internals
- **Multi-modal Support**: Works across text, vision, and audio inputs
- **Highly Parallelizable**: Can test multiple variations concurrently
- **Predictable Scaling**: Success rate follows power-law behavior

## Related Concepts

- [GOAT Strategy](/docs/red-team/strategies/goat/)
- [Iterative Jailbreaks](/docs/red-team/strategies/iterative/)
- [Multi-turn Jailbreaks](/docs/red-team/strategies/multi-turn/)
- [Best of N configuration example](https://github.com/promptfoo/promptfoo/tree/main/examples/redteam-bestOfN-strategy)

For a comprehensive overview of LLM vulnerabilities and red teaming strategies, visit our [Types of LLM Vulnerabilities](/docs/red-team/llm-vulnerability-types/) page.