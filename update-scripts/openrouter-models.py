#!/usr/bin/env python3
"""
OpenRouter Models Catalog Extractor

Fetches the complete OpenRouter models catalog via API and generates:
1. models-catalog.json - Raw API response with metadata
2. README.md - Human-readable markdown table of models

Usage:
    python openrouter-models.py [--verbose]

Requirements:
    - OPENROUTER_API_KEY environment variable must be set
    - requests library (pip install requests)

Author: Claude Code SDK
Date: 2025-10-02
"""

import os
import sys
import json
import requests
import time
from pathlib import Path
from datetime import datetime

# Configuration
API_ENDPOINT = "https://openrouter.ai/api/v1/models"
OUTPUT_DIR = Path(__file__).parent.parent / "web-scraped-docs/openrouter"
TIMEOUT = 10  # seconds
RETRY_DELAY = 2  # seconds
MAX_RETRIES = 1

# Global verbose flag
verbose = False


def log(message):
    """Print message if verbose mode enabled."""
    if verbose:
        print(f"[DEBUG] {message}")


def get_api_key():
    """
    Get API key from environment variable.

    Returns:
        str: API key

    Exits:
        1 if API key not found
    """
    key = os.environ.get('OPENROUTER_API_KEY')
    if not key:
        print("ERROR: OPENROUTER_API_KEY environment variable not set")
        print()
        print("Please set your OpenRouter API key:")
        print("  export OPENROUTER_API_KEY='your-api-key-here'")
        print()
        print("You can get an API key from: https://openrouter.ai/keys")
        sys.exit(1)

    log(f"API key found: {key[:10]}...")
    return key


def fetch_models(api_key):
    """
    Fetch models from OpenRouter API with retry logic.

    Args:
        api_key (str): OpenRouter API key

    Returns:
        dict: API response with 'data' key containing models array

    Raises:
        SystemExit: On fatal errors (network, API errors)
    """
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    log(f"Fetching models from {API_ENDPOINT}")
    log(f"Timeout: {TIMEOUT}s")

    retries = 0
    while retries <= MAX_RETRIES:
        try:
            response = requests.get(
                API_ENDPOINT,
                headers=headers,
                timeout=TIMEOUT
            )

            # Check for HTTP errors
            if response.status_code != 200:
                print(f"ERROR: API returned status {response.status_code}")
                print(f"Response: {response.text[:500]}")
                sys.exit(1)

            # Parse JSON
            data = response.json()

            # Validate response structure
            if 'data' not in data:
                print("ERROR: API response missing 'data' field")
                print(f"Response keys: {list(data.keys())}")
                sys.exit(1)

            log(f"Successfully fetched {len(data['data'])} models")
            return data

        except requests.exceptions.Timeout:
            if retries < MAX_RETRIES:
                retries += 1
                print(f"Request timeout. Retrying ({retries}/{MAX_RETRIES})...")
                time.sleep(RETRY_DELAY)
            else:
                print("ERROR: Request timed out after retries")
                sys.exit(1)

        except requests.exceptions.RequestException as e:
            print(f"ERROR: Network error: {e}")
            sys.exit(1)

        except json.JSONDecodeError as e:
            print(f"ERROR: Invalid JSON response: {e}")
            print(f"Response text: {response.text[:500]}")
            sys.exit(1)


def calculate_provider_stats(models):
    """
    Calculate provider statistics from models data.

    Args:
        models (list): List of model dictionaries

    Returns:
        dict: Provider statistics including count and top providers
    """
    providers = {}
    for model in models:
        provider = model.get('id', '').split('/')[0]
        if provider:
            providers[provider] = providers.get(provider, 0) + 1

    # Sort by count and get top 10
    top_providers = sorted(
        providers.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]

    return {
        'total_providers': len(providers),
        'top_providers': [{'provider': p, 'count': c} for p, c in top_providers]
    }


def calculate_pricing_stats(models):
    """
    Calculate pricing statistics from models data.

    Args:
        models (list): List of model dictionaries

    Returns:
        dict: Pricing statistics including min/max/avg costs
    """
    prompt_prices = []
    completion_prices = []
    free_count = 0

    for model in models:
        pricing = model.get('pricing', {})

        # Prompt pricing
        prompt = pricing.get('prompt', '0')
        try:
            prompt_val = float(prompt)
            if prompt_val == 0:
                free_count += 1
            prompt_prices.append(prompt_val)
        except (ValueError, TypeError):
            pass

        # Completion pricing
        completion = pricing.get('completion', '0')
        try:
            completion_val = float(completion)
            completion_prices.append(completion_val)
        except (ValueError, TypeError):
            pass

    # Filter out negative prices (like Auto Router)
    prompt_prices = [p for p in prompt_prices if p >= 0]
    completion_prices = [c for c in completion_prices if c >= 0]

    return {
        'free_models_count': free_count,
        'prompt_cost': {
            'min': min(prompt_prices) if prompt_prices else 0,
            'max': max(prompt_prices) if prompt_prices else 0,
            'avg': sum(prompt_prices) / len(prompt_prices) if prompt_prices else 0
        },
        'completion_cost': {
            'min': min(completion_prices) if completion_prices else 0,
            'max': max(completion_prices) if completion_prices else 0,
            'avg': sum(completion_prices) / len(completion_prices) if completion_prices else 0
        }
    }


def calculate_context_stats(models):
    """
    Calculate context window statistics from models data.

    Args:
        models (list): List of model dictionaries

    Returns:
        dict: Context window statistics
    """
    context_lengths = []
    for model in models:
        context = model.get('context_length', 0)
        if context and context > 0:
            context_lengths.append(context)

    return {
        'min_context': min(context_lengths) if context_lengths else 0,
        'max_context': max(context_lengths) if context_lengths else 0,
        'avg_context': int(sum(context_lengths) / len(context_lengths)) if context_lengths else 0
    }


def calculate_capability_stats(models):
    """
    Calculate capability statistics (multimodal, text-only, etc).

    Args:
        models (list): List of model dictionaries

    Returns:
        dict: Capability statistics
    """
    multimodal_count = 0
    text_only_count = 0

    for model in models:
        arch = model.get('architecture', {})
        input_modalities = arch.get('input_modalities', [])

        # Check if multimodal (has image or audio input)
        if 'image' in input_modalities or 'audio' in input_modalities:
            multimodal_count += 1
        else:
            text_only_count += 1

    return {
        'multimodal_models': multimodal_count,
        'text_only_models': text_only_count
    }


def save_json(data, output_path):
    """
    Save raw JSON response with metadata wrapper.

    Args:
        data (dict): API response data
        output_path (Path): Output file path
    """
    models = data['data']

    # Calculate enhanced metadata
    provider_stats = calculate_provider_stats(models)
    pricing_stats = calculate_pricing_stats(models)
    context_stats = calculate_context_stats(models)
    capability_stats = calculate_capability_stats(models)

    # Wrap with enhanced metadata
    output = {
        "metadata": {
            "source": "OpenRouter API",
            "api_endpoint": API_ENDPOINT,
            "updated": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
            "total_models": len(models),
            "providers": provider_stats,
            "pricing": pricing_stats,
            "context": context_stats,
            "capabilities": capability_stats
        },
        "models": models
    }

    log(f"Writing JSON to {output_path}")

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)

        # Get file size
        size_kb = output_path.stat().st_size / 1024
        log(f"JSON file size: {size_kb:.1f} KB")

    except IOError as e:
        print(f"ERROR: Failed to write JSON file: {e}")
        sys.exit(1)


def format_price(price_str):
    """
    Format price string for display.

    Args:
        price_str (str): Price as string (e.g., "0.000003")

    Returns:
        str: Formatted price (e.g., "$0.000003")
    """
    if not price_str or price_str == "0":
        return "Free"

    try:
        # Convert to float and format
        price_float = float(price_str)
        if price_float == 0:
            return "Free"
        elif price_float < 0.000001:
            return f"${price_float:.10f}"
        elif price_float < 0.0001:
            return f"${price_float:.9f}"
        elif price_float < 0.01:
            return f"${price_float:.6f}"
        else:
            return f"${price_float:.4f}"
    except (ValueError, TypeError):
        return price_str


def format_markdown(data):
    """
    Convert JSON data to formatted markdown table.

    Args:
        data (dict): API response data

    Returns:
        str: Markdown formatted content
    """
    models = data['data']
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')

    log("Generating markdown table")

    # Calculate statistics for header
    provider_stats = calculate_provider_stats(models)
    pricing_stats = calculate_pricing_stats(models)
    context_stats = calculate_context_stats(models)
    capability_stats = calculate_capability_stats(models)

    # Filter models with pricing (exclude null pricing)
    models_with_pricing = [
        m for m in models
        if m.get('pricing') and m['pricing'].get('prompt')
    ]

    log(f"Models with pricing: {len(models_with_pricing)}/{len(models)}")

    # Sort by name
    models_sorted = sorted(models_with_pricing, key=lambda m: m.get('name', ''))

    # Header with enhanced statistics
    md = "# OpenRouter Models Catalog\n\n"
    md += f"**Source:** OpenRouter API ({API_ENDPOINT})\n"
    md += f"**Last Updated:** {timestamp}\n"
    md += f"**Total Models:** {len(models)}\n"
    md += f"**Free Models:** {pricing_stats['free_models_count']} ({pricing_stats['free_models_count']*100//len(models)}%)\n"
    md += f"**Providers:** {provider_stats['total_providers']}\n\n"

    # Quick Stats section
    md += "## Quick Statistics\n\n"
    md += f"- **Context Lengths:** {context_stats['min_context']:,} - {context_stats['max_context']:,} tokens\n"

    # Format pricing range
    max_prompt = pricing_stats['prompt_cost']['max']
    max_completion = pricing_stats['completion_cost']['max']
    if max_prompt > 0 or max_completion > 0:
        md += f"- **Pricing Range:** Free - ${max(max_prompt, max_completion):.6f} per token\n"
    else:
        md += "- **Pricing Range:** Free - Variable\n"

    md += f"- **Multimodal Models:** {capability_stats['multimodal_models']} ({capability_stats['multimodal_models']*100//len(models)}%)\n"
    md += f"- **Text-only Models:** {capability_stats['text_only_models']} ({capability_stats['text_only_models']*100//len(models)}%)\n\n"

    # Top Providers section
    md += "## Top Providers\n\n"
    for provider_data in provider_stats['top_providers'][:5]:
        md += f"- **{provider_data['provider']}**: {provider_data['count']} models\n"
    md += "\n"

    md += "---\n\n"
    md += "## All Models\n\n"

    # Table header
    md += "| Model ID | Name | Context Length | Prompt Cost | Completion Cost |\n"
    md += "|----------|------|----------------|-------------|------------------|\n"

    # Table rows
    for model in models_sorted:
        model_id = model.get('id', 'N/A')
        name = model.get('name', 'N/A')
        context = model.get('context_length', 0)

        # Format context length with commas
        context_str = f"{context:,}" if context else "N/A"

        # Get pricing
        pricing = model.get('pricing', {})
        prompt_cost = format_price(pricing.get('prompt', '0'))
        completion_cost = format_price(pricing.get('completion', '0'))

        # Escape pipe characters in text
        model_id = model_id.replace('|', '\\|')
        name = name.replace('|', '\\|')

        md += f"| {model_id} | {name} | {context_str} | {prompt_cost} | {completion_cost} |\n"

    md += "\n---\n\n"

    # Usage guide section
    md += "## How to Use This Catalog\n\n"
    md += "### Finding a Model\n"
    md += "1. Browse the full table above (sorted alphabetically by name)\n"
    md += "2. Use Ctrl+F (Cmd+F on Mac) to search by provider, capability, or model name\n"
    md += "3. Look for models marked with \":free\" suffix for zero-cost options\n"
    md += "4. Check the Quick Statistics section for overall metrics\n\n"

    md += "### Understanding Pricing\n"
    md += "- **Prompt Cost:** Price per input token in USD\n"
    md += "- **Completion Cost:** Price per output token in USD\n"
    md += "- **Free Models:** Models with $0 cost for both prompt and completion\n"
    md += "- Typical costs range from $0.0001 to $0.01 per 1,000 tokens\n"
    md += "- Premium models (e.g., o1-pro, Claude Opus) can cost up to $0.60 per 1,000 output tokens\n\n"

    md += "### Context Length\n"
    md += "- Range: 2,824 - 2,000,000 tokens\n"
    md += "- Larger context = ability to process longer documents and conversations\n"
    md += "- Consider both context length AND pricing for cost-effective choices\n"
    md += "- 1 token ≈ 0.75 words (varies by tokenizer)\n\n"

    md += "### Multimodal Capabilities\n"
    md += "- Models with image/audio input support are included in the multimodal count\n"
    md += "- Check the JSON catalog for detailed architecture information\n"
    md += "- Look for models from Google (Gemini), Anthropic (Claude), OpenAI (GPT-4) for vision capabilities\n\n"

    md += "---\n\n"
    md += "## Updating This Catalog\n\n"
    md += "To refresh this catalog with the latest models:\n\n"
    md += "```bash\n"
    md += "export OPENROUTER_API_KEY='your-key'\n"
    md += "cd /Users/joe/github/llm-code-docs/update-scripts\n"
    md += "python3 openrouter-models.py\n"
    md += "```\n\n"

    md += "## Additional Resources\n\n"
    md += "- [OpenRouter Documentation](https://openrouter.ai/docs)\n"
    md += "- [OpenRouter Models Page](https://openrouter.ai/models)\n"
    md += "- [Get API Keys](https://openrouter.ai/keys)\n"
    md += "- [Extraction Script](../update-scripts/openrouter-models.py)\n"
    md += "- [Implementation Notes](../update-scripts/OPENROUTER_EXTRACTION_NOTES.md)\n\n"

    md += "---\n\n"
    md += "*This catalog is automatically generated from the OpenRouter API.*\n"
    md += "*For the most up-to-date information, visit https://openrouter.ai/models*\n"

    return md


def save_markdown(markdown, output_path):
    """
    Save markdown content to file.

    Args:
        markdown (str): Markdown content
        output_path (Path): Output file path
    """
    log(f"Writing markdown to {output_path}")

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)

        # Get file size
        size_kb = output_path.stat().st_size / 1024
        log(f"Markdown file size: {size_kb:.1f} KB")

    except IOError as e:
        print(f"ERROR: Failed to write markdown file: {e}")
        sys.exit(1)


def main():
    """Main extraction function."""
    global verbose

    # Parse command line arguments
    if '--verbose' in sys.argv:
        verbose = True

    print("OpenRouter Models Catalog Extraction")
    print("=" * 60)
    print()

    # Get API key
    api_key = get_api_key()

    # Create output directory
    log(f"Creating output directory: {OUTPUT_DIR}")
    try:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        print(f"ERROR: Failed to create output directory: {e}")
        sys.exit(1)

    # Fetch models
    print(f"Fetching models from OpenRouter API...")
    data = fetch_models(api_key)
    model_count = len(data['data'])
    print(f"Fetched {model_count} models from OpenRouter API")
    print()

    # Save JSON
    json_path = OUTPUT_DIR / "models-catalog.json"
    save_json(data, json_path)
    json_size_kb = json_path.stat().st_size / 1024
    print(f"Saved to {json_path} ({json_size_kb:.1f} KB)")

    # Generate and save markdown
    markdown = format_markdown(data)
    md_path = OUTPUT_DIR / "README.md"
    save_markdown(markdown, md_path)
    md_size_kb = md_path.stat().st_size / 1024
    print(f"Saved to {md_path} ({md_size_kb:.1f} KB)")

    print()
    print("=" * 60)
    print("Extraction complete!")
    print(f"Total models: {model_count}")
    print(f"JSON catalog: {json_path}")
    print(f"Markdown catalog: {md_path}")


if __name__ == "__main__":
    main()
