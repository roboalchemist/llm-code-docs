# Source: https://docs.perplexity.ai/guides/returning-images

## 
[​](https://docs.perplexity.ai/guides/returning-images#overview)
Overview
Sonar models can return images as part of their responses to enhance the information provided. You can control which images are returned using domain and format filters, giving you fine-grained control over the sources and file types of image results.
**SDK Installation Required** : Install the official SDK first - `pip install perplexityai` for Python or `npm install @perplexity-ai/perplexity_ai` for TypeScript/JavaScript.
The `image_domain_filter` and `image_format_filter` parameters allow you to control the sources and file types of image results returned by the Sonar models.
You can include a maximum of 10 entries in each of the filter lists. These filters currently apply only when `"return_images": true` is set in your request.
## 
[​](https://docs.perplexity.ai/guides/returning-images#filter-types)
Filter Types
### 
[​](https://docs.perplexity.ai/guides/returning-images#domain-filtering)
Domain Filtering
The `image_domain_filter` parameter controls which image sources are included or excluded:
  * **Exclude domains** : Prefix with `-` (e.g., `-gettyimages.com`)
  * **Include domains** : Use domain name directly (e.g., `wikimedia.org`)


### 
[​](https://docs.perplexity.ai/guides/returning-images#format-filtering)
Format Filtering
The `image_format_filter` parameter restricts results to specific file formats:
  * Use lowercase file extensions: `gif`, `jpg`, `png`, `webp`
  * Omit the dot prefix: use `gif`, not `.gif`


## 
[​](https://docs.perplexity.ai/guides/returning-images#basic-usage)
Basic Usage
To enable image returns, your request must include `"return_images": true`.
cURL
Python
JavaScript
TypeScript
Copy
Ask AI
```
curl --request POST \
  --url https://api.perplexity.ai/chat/completions \
  --header "Authorization: Bearer $SONAR_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "sonar",
    "return_images": true,
    "messages": [
      {"role": "user", "content": "Show me images of Mount Everest"}
    ]
  }' | jq

```

## 
[​](https://docs.perplexity.ai/guides/returning-images#filtering-examples)
Filtering Examples
### 
[​](https://docs.perplexity.ai/guides/returning-images#1-exclude-specific-image-domains)
1. Exclude Specific Image Domains
Filter out images from specific providers like Getty Images:
cURL
Python
JavaScript
TypeScript
Copy
Ask AI
```
curl --request POST \
  --url https://api.perplexity.ai/chat/completions \
  --header "Authorization: Bearer $SONAR_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "sonar",
    "return_images": true,
    "image_domain_filter": ["-gettyimages.com"],
    "messages": [
      {"role": "user", "content": "What is the weather like today in London?"}
    ]
  }' | jq

```

### 
[​](https://docs.perplexity.ai/guides/returning-images#2-only-return-gifs)
2. Only Return GIFs
Restrict results to GIF images only:
cURL
Python
JavaScript
TypeScript
Copy
Ask AI
```
curl --request POST \
  --url https://api.perplexity.ai/chat/completions \
  --header "Authorization: Bearer $SONAR_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "sonar",
    "return_images": true,
    "image_format_filter": ["gif"],
    "messages": [
      {"role": "user", "content": "Show me a funny cat gif"}
    ]
  }' | jq

```

### 
[​](https://docs.perplexity.ai/guides/returning-images#3-combine-domain-and-format-filters)
3. Combine Domain and Format Filters
Use both filters together for precise control:
cURL
Python
JavaScript
TypeScript
Copy
Ask AI
```
curl --request POST \
  --url https://api.perplexity.ai/chat/completions \
  --header "Authorization: Bearer $SONAR_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "sonar",
    "return_images": true,
    "image_domain_filter": ["-gettyimages.com"],
    "image_format_filter": ["gif"],
    "messages": [
      {"role": "user", "content": "Show me a gif of a dog"}
    ]
  }' | jq

```

## 
[​](https://docs.perplexity.ai/guides/returning-images#advanced-filtering)
Advanced Filtering
### 
[​](https://docs.perplexity.ai/guides/returning-images#multiple-domain-exclusions)
Multiple Domain Exclusions
Copy
Ask AI
```
# Exclude multiple image providers
completion = client.chat.completions.create(
    model="sonar",
    return_images=True,
    image_domain_filter=["-gettyimages.com", "-shutterstock.com", "-stockphoto.com"],
    messages=[
        {"role": "user", "content": "Show me nature photography"}
    ]
)

```

### 
[​](https://docs.perplexity.ai/guides/returning-images#multiple-format-types)
Multiple Format Types
Copy
Ask AI
```
# Allow multiple image formats
completion = client.chat.completions.create(
    model="sonar",
    return_images=True,
    image_format_filter=["jpg", "png", "webp"],
    messages=[
        {"role": "user", "content": "Show me high-quality landscape images"}
    ]
)

```

### 
[​](https://docs.perplexity.ai/guides/returning-images#include-specific-domains)
Include Specific Domains
Copy
Ask AI
```
# Include only Wikipedia images
completion = client.chat.completions.create(
    model="sonar", 
    return_images=True,
    image_domain_filter=["wikimedia.org"],
    messages=[
        {"role": "user", "content": "Show me historical images"}
    ]
)

```

## 
[​](https://docs.perplexity.ai/guides/returning-images#common-use-cases)
Common Use Cases
### 
[​](https://docs.perplexity.ai/guides/returning-images#educational-content)
Educational Content
Copy
Ask AI
```
# Get educational images from trusted sources
image_domain_filter = ["wikimedia.org", "nasa.gov", "archive.org"]
image_format_filter = ["jpg", "png"]

```

### 
[​](https://docs.perplexity.ai/guides/returning-images#creative-projects)
Creative Projects
Copy
Ask AI
```
# Get animated content for presentations
image_format_filter = ["gif", "webp"]
image_domain_filter = ["-gettyimages.com", "-shutterstock.com"]  # Avoid watermarked images

```

### 
[​](https://docs.perplexity.ai/guides/returning-images#high-quality-photography)
High-Quality Photography
Copy
Ask AI
```
# Focus on professional photography formats
image_format_filter = ["jpg", "png"]
image_domain_filter = ["-lowres.com", "-thumbnail.com"]  # Exclude low-quality sources

```

## 
[​](https://docs.perplexity.ai/guides/returning-images#best-practices)
Best Practices
Domain Filtering Strategy
  * Use simple domain names like `example.com` or `-gettyimages.com`
  * Do not include `http://`, `https://`, or subdomains
  * Mix inclusion and exclusion in domain filters for precise control
  * Keep lists short (≤10 entries) for performance and relevance


Format Filtering Guidelines
  * File extensions must be lowercase: `["jpg"]`, not `["JPG"]`
  * Omit dot prefix: use `gif`, not `.gif`
  * Consider your use case: GIFs for animation, PNG for transparency, JPG for photos
  * WebP offers good compression but may have limited compatibility


Performance Optimization
  * Filters may slightly increase response time
  * Overly restrictive filters may reduce result quality or quantity
  * Test different filter combinations to find the right balance
  * Monitor response times with different filter configurations


## 
[​](https://docs.perplexity.ai/guides/returning-images#filter-reference)
Filter Reference
### 
[​](https://docs.perplexity.ai/guides/returning-images#supported-image-formats)
Supported Image Formats
Format | Extension | Best For  
---|---|---  
JPEG | `jpg` | Photographs, complex images  
PNG | `png` | Screenshots, images with transparency  
WebP | `webp` | Modern format with good compression  
GIF | `gif` | Animated images, simple graphics  
### 
[​](https://docs.perplexity.ai/guides/returning-images#common-domain-exclusions)
Common Domain Exclusions
Domain | Type | Reason  
---|---|---  
`-gettyimages.com` | Stock Photos | Watermarked content  
`-shutterstock.com` | Stock Photos | Watermarked content  
`-istockphoto.com` | Stock Photos | Watermarked content  
`-pinterest.com` | Social Media | Mixed quality/attribution  
Start with broad filters and gradually refine them based on the quality and relevance of returned images.
## 
[​](https://docs.perplexity.ai/guides/returning-images#limitations)
Limitations
  * Maximum of 10 entries in each filter list
  * Filters only apply when `"return_images": true` is set
  * Some domains may not be filterable due to CDN usage
  * Very restrictive filters may result in no images being returned


