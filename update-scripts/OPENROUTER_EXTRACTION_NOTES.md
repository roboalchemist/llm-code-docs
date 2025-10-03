# OpenRouter Models Catalog Extraction - Implementation Notes

## Overview

The OpenRouter models extraction fetches the complete catalog of available models via the OpenRouter API, generating both JSON and markdown outputs for comprehensive reference.

**Success Rate:** 100% (single API call, 330+ models)
**API Endpoint:** https://openrouter.ai/api/v1/models
**Authentication:** Bearer token (OPENROUTER_API_KEY)

## Implementation Details

### Script Location
`/Users/joe/github/llm-code-docs/update-scripts/openrouter-models.py`

### API Details
- **Method:** GET
- **Authentication:** Bearer token in Authorization header
- **Response Format:** JSON with 'data' array of model objects
- **Pagination:** Not required (all models in single response)
- **Rate Limiting:** None observed (but polite delays implemented)

### Key Configuration
- **Timeout:** 10 seconds
- **Retry Logic:** 1 retry with 2-second delay
- **Output Directory:** `../openrouter/`
- **Dual Output:** JSON (complete) + Markdown (formatted table)

### Model Data Structure

Each model object contains 13 fields:
1. **id** - Model identifier (provider/model-name format)
2. **canonical_slug** - Canonical reference
3. **hugging_face_id** - HuggingFace model ID (optional)
4. **name** - Human-readable display name
5. **created** - Unix timestamp
6. **description** - Detailed model description
7. **context_length** - Maximum context window (tokens)
8. **architecture** - Input/output modalities, tokenizer
9. **pricing** - Prompt/completion costs, special costs
10. **top_provider** - Best provider info
11. **per_request_limits** - Request limits (if applicable)
12. **supported_parameters** - API parameters list
13. **default_parameters** - Default values

### Enhanced Metadata

The script now calculates comprehensive statistics:

#### Provider Statistics
- Total provider count
- Top 10 providers by model count
- Distribution of models across providers

#### Pricing Statistics
- Free models count
- Minimum, maximum, average prompt costs
- Minimum, maximum, average completion costs
- Filters out negative prices (Auto Router)

#### Context Window Statistics
- Minimum context length
- Maximum context length
- Average context length

#### Capability Statistics
- Multimodal models count (image/audio input)
- Text-only models count

### Output Files

#### 1. models-catalog.json (586+ KB)
- Complete API response with metadata wrapper
- All 330+ models with full details
- Enhanced metadata including:
  - Provider statistics (total count, top providers)
  - Pricing statistics (min/max/avg, free count)
  - Context statistics (min/max/avg)
  - Capability statistics (multimodal vs text-only)
- Use for: Programmatic access, filtering, analysis

#### 2. README.md (32+ KB)
- Human-readable markdown table
- Enhanced header with quick statistics
- Top providers section
- Columns: Model ID, Name, Context Length, Prompt Cost, Completion Cost
- Sorted alphabetically by name
- Filters out models without pricing (currently none)
- Use for: Quick reference, browsing, comparison

## Statistics

**As of 2025-10-03:**
- Total Models: 330+
- Unique Providers: 53+
- Free Models: 54+ (16.4%)
- Context Range: 2,824 - 2,000,000 tokens
- Price Range: Free - $0.60 per completion token

**Top Providers:**
- qwen: 42 models
- openai: 42 models
- mistralai: 35 models
- google: 24 models
- meta-llama: 21 models

## How to Run

### Prerequisites
1. Set OpenRouter API key:
   ```bash
   export OPENROUTER_API_KEY='your-key-here'
   ```

2. Install dependencies (if not installed):
   ```bash
   pip install requests
   ```

### Execution
```bash
# Standard run (quiet mode)
cd /Users/joe/github/llm-code-docs/update-scripts
python3 openrouter-models.py

# Verbose mode (shows debug info)
python3 openrouter-models.py --verbose
```

### Expected Output
```
OpenRouter Models Catalog Extraction
============================================================

Fetching models from OpenRouter API...
Fetched 330 models from OpenRouter API

Saved to /path/to/openrouter/models-catalog.json (586.2 KB)
Saved to /path/to/openrouter/README.md (32.0 KB)

============================================================
Extraction complete!
Total models: 330
JSON catalog: /path/to/openrouter/models-catalog.json
Markdown catalog: /path/to/openrouter/README.md
```

## Error Handling

The script handles:
- **Missing API Key:** Clear error message with setup instructions
- **Network Errors:** Timeout handling, retry logic
- **API Errors:** HTTP status code validation, error messages
- **Invalid JSON:** JSON parsing error handling
- **File I/O Errors:** Directory creation, write permission errors

## Update Frequency

**Recommended:** Weekly or bi-weekly
**Rationale:**
- OpenRouter adds new models frequently
- Pricing may change
- Models may be deprecated/removed

**Automation Options:**
- Add to cron job: `0 0 * * 0` (weekly Sunday midnight)
- GitHub Actions workflow on schedule
- Manual run before major updates

## Known Limitations

1. **No Historical Tracking:** Script doesn't track model changes over time
2. **Single View:** Markdown output is one large table (no grouping by provider in separate sections)
3. **No Filtering CLI:** Cannot filter by provider, modality, or price range via command-line
4. **Static Pricing:** Pricing is point-in-time (no trend analysis)

## Future Enhancements

**Potential additions:**
1. Provider grouping in separate markdown sections
2. Separate free models section
3. Multimodal models filtering
4. Diff tracking between runs (changelog generation)
5. Price change alerts
6. Search/filter CLI arguments

## Troubleshooting

### API Key Not Found
**Error:** `ERROR: OPENROUTER_API_KEY environment variable not set`
**Solution:** Export the key in your shell:
```bash
export OPENROUTER_API_KEY='sk-or-...'
```

### Network Timeout
**Error:** `Request timeout. Retrying...`
**Solution:** Check internet connection, OpenRouter API status

### Invalid JSON Response
**Error:** `ERROR: Invalid JSON response`
**Solution:** API may be down or changed format - check OpenRouter status

### File Permission Error
**Error:** `Failed to create output directory` or `Failed to write JSON file`
**Solution:** Check directory permissions, ensure write access

## Maintenance

### Script Updates
- **Location:** `/Users/joe/github/llm-code-docs/update-scripts/openrouter-models.py`
- **Version Control:** Committed in git repository
- **Testing:** Run with `--verbose` flag after changes

### API Changes
- Monitor OpenRouter API changelog
- Test script after API updates
- Update field parsing if schema changes

### Output Format
- Maintain backward compatibility
- Version output format if making breaking changes
- Document format version in metadata

## Enhancement History

### Task 18 (2025-10-02)
- Added comprehensive metadata calculation
- Enhanced JSON output with provider, pricing, context, and capability statistics
- Improved markdown header with quick statistics
- Added top providers section
- Maintained backward compatibility with existing outputs

### Task 16-17 (2025-10-02)
- Initial implementation
- Basic extraction with dual-format output
- Simple metadata wrapper
- Alphabetical sorting in markdown

---

**Last Updated:** 2025-10-02
**Script Version:** 1.1
**Data Format Version:** 1.0
