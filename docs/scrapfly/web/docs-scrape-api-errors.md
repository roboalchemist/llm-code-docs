# Source: https://scrapfly.io/docs/scrape-api/errors

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/scrape-api/errors

Markdown Content:
If you want to port those definitions into your application, you can checkout the [Exportable Definition](https://scrapfly.io/docs/scrape-api/errors#definition) section to retrieve the JSON describing errors.

Scrapfly provides API errors in two locations - in the response body and the response headers:

If you want to handle errors from your application without copy-pasting the whole error definition into your application to match errors, here is a portable JSON of error definition:

```
{
    "scraper_errors": {
        "ERR::ACCOUNT::PAYMENT_REQUIRED": {
            "code": "ERR::ACCOUNT::PAYMENT_REQUIRED",
            "http_code": 402,
            "description": "Unable to charge last invoice - Connect to your dashboard to solve the issue",
            "retryable": true,
            "type": "ACCOUNT",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::ACCOUNT::PAYMENT_REQUIRED"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::ACCOUNT::SUSPENDED": {
            "code": "ERR::ACCOUNT::SUSPENDED",
            "http_code": 429,
            "description": "Account Suspended",
            "retryable": true,
            "type": "ACCOUNT",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::ACCOUNT::SUSPENDED"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::API::INTERNAL_ERROR": {
            "code": "ERR::API::INTERNAL_ERROR",
            "http_code": 500,
            "description": "API Internal Error",
            "retryable": false,
            "type": "SCRAPER",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::API::INTERNAL_ERROR"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::ASP::CAPTCHA_ERROR": {
            "code": "ERR::ASP::CAPTCHA_ERROR",
            "http_code": 422,
            "description": "Something wrong happened with the captcha. We will figure out to fix the problem as soon as possible",
            "retryable": true,
            "type": "SCRAPER",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::ASP::CAPTCHA_ERROR"
            },
            "billed": false,
            "fair_use": true
        },
        "ERR::ASP::CAPTCHA_TIMEOUT": {
            "code": "ERR::ASP::CAPTCHA_TIMEOUT",
            "http_code": 422,
            "description": "The budgeted time to solve the captcha is reached",
            "retryable": true,
            "type": "SCRAPER",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::ASP::CAPTCHA_TIMEOUT"
            },
            "billed": false,
            "fair_use": true
        },
        "ERR::ASP::SHIELD_ERROR": {
            "code": "ERR::ASP::SHIELD_ERROR",
            "http_code": 422,
            "description": "The ASP encounter an unexpected problem. We will fix it as soon as possible. Our team has been alerted",
            "retryable": false,
            "type": "SCRAPER",
            "links": {
                "Checkout ASP documentation": "https://scrapfly.io/docs/scrape-api/anti-scraping-protection#maximize_success_rate",
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::ASP::SHIELD_ERROR"
            },
            "billed": false,
            "fair_use": true
        },
        "ERR::ASP::SHIELD_EXPIRED": {
            "code": "ERR::ASP::SHIELD_EXPIRED",
            "http_code": 422,
            "description": "The ASP shield previously set is expired, you must retry.",
            "retryable": true,
            "type": "SCRAPER",
            "links": null,
            "billed": false,
            "fair_use": true
        },
        "ERR::ASP::SHIELD_NOT_ELIGIBLE": {
            "code": "ERR::ASP::SHIELD_NOT_ELIGIBLE",
            "http_code": 422,
            "description": "The feature requested\tis not eligible while using the ASP for the given protection/target",
            "retryable": false,
            "type": "SCRAPER",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::ASP::SHIELD_NOT_ELIGIBLE"
            },
            "billed": false,
            "fair_use": true
        },
        "ERR::ASP::SHIELD_PROTECTION_FAILED": {
            "code": "ERR::ASP::SHIELD_PROTECTION_FAILED",
            "http_code": 422,
            "description": "The ASP shield failed to solve the challenge against the anti scrapping protection",
            "retryable": true,
            "type": "SCRAPER",
            "links": {
                "Checkout ASP documentation": "https://scrapfly.io/docs/scrape-api/anti-scraping-protection#maximize_success_rate",
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::ASP::SHIELD_PROTECTION_FAILED"
            },
            "billed": false,
            "fair_use": true
        },
        "ERR::ASP::TIMEOUT": {
            "code": "ERR::ASP::TIMEOUT",
            "http_code": 422,
            "description": "The ASP made too much time to solve or respond",
            "retryable": true,
            "type": "SCRAPER",
            "links": {
                "Checkout ASP documentation": "https://scrapfly.io/docs/scrape-api/anti-scraping-protection",
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::ASP::TIMEOUT"
            },
            "billed": false,
            "fair_use": true
        },
        "ERR::ASP::UNABLE_TO_SOLVE_CAPTCHA": {
            "code": "ERR::ASP::UNABLE_TO_SOLVE_CAPTCHA",
            "http_code": 422,
            "description": "Despite our effort, we were unable to solve the captcha. It can happened sporadically, please retry",
            "retryable": true,
            "type": "SCRAPER",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::ASP::UNABLE_TO_SOLVE_CAPTCHA"
            },
            "billed": false,
            "fair_use": true
        },
        "ERR::ASP::UPSTREAM_UNEXPECTED_RESPONSE": {
            "code": "ERR::ASP::UPSTREAM_UNEXPECTED_RESPONSE",
            "http_code": 422,
            "description": "The response given by the upstream after challenge resolution is not expected. Our team has been alerted",
            "retryable": false,
            "type": "SCRAPER",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::ASP::UPSTREAM_UNEXPECTED_RESPONSE"
            },
            "billed": false,
            "fair_use": true
        },
        "ERR::CRAWLER::ALREADY_SCHEDULED": {
            "code": "ERR::CRAWLER::ALREADY_SCHEDULED",
            "http_code": 422,
            "description": "The given crawler uuid is already scheduled",
            "retryable": false,
            "type": "CRAWLER",
            "links": {
                "Crawler Documentation": "https://scrapfly.io/docs/crawler-api/getting-started",
                "Crawler Troubleshooting": "https://scrapfly.io/docs/crawler-api/troubleshoot",
                "Related Error Doc": "https://scrapfly.io/docs/crawler-api/error/ERR::CRAWLER::ALREADY_SCHEDULED"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::CRAWLER::CONFIG_ERROR": {
            "code": "ERR::CRAWLER::CONFIG_ERROR",
            "http_code": 400,
            "description": "Crawler configuration error",
            "retryable": false,
            "type": "CRAWLER",
            "links": {
                "Crawler Documentation": "https://scrapfly.io/docs/crawler-api/getting-started",
                "Related Error Doc": "https://scrapfly.io/docs/crawler-api/error/ERR::CRAWLER::CONFIG_ERROR"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::CRAWLER::TIMEOUT": {
            "code": "ERR::CRAWLER::TIMEOUT",
            "http_code": 408,
            "description": "Crawler exceeded time limit",
            "retryable": false,
            "type": "CRAWLER",
            "links": {
                "Crawler Documentation": "https://scrapfly.io/docs/crawler-api/getting-started",
                "Crawler Troubleshooting": "https://scrapfly.io/docs/crawler-api/troubleshoot",
                "Related Error Doc": "https://scrapfly.io/docs/crawler-api/error/ERR::CRAWLER::TIMEOUT",
                "Timeout Configuration": "https://scrapfly.io/docs/crawler-api/getting-started#max_duration"
            },
            "billed": true,
            "fair_use": false
        },
        "ERR::EXTRACTION::CONFIG_ERROR": {
            "code": "ERR::EXTRACTION::CONFIG_ERROR",
            "http_code": 400,
            "description": "Parameters sent to the API are not valid",
            "retryable": false,
            "type": "EXTRACTION",
            "links": {
                "API Specification": "https://scrapfly.io/docs/extraction-api/getting-started#spec",
                "Related Error Doc": "https://scrapfly.io/docs/extraction-api/error/ERR::EXTRACTION::CONFIG_ERROR"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::EXTRACTION::CONTENT_TYPE_NOT_SUPPORTED": {
            "code": "ERR::EXTRACTION::CONTENT_TYPE_NOT_SUPPORTED",
            "http_code": 422,
            "description": "The content type of the response is not supported for extraction.",
            "retryable": false,
            "type": "EXTRACTION",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/extraction-api/error/ERR::EXTRACTION::CONTENT_TYPE_NOT_SUPPORTED"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::EXTRACTION::DATA_ERROR": {
            "code": "ERR::EXTRACTION::DATA_ERROR",
            "http_code": 422,
            "description": "Extracted data is invalid or have an issue",
            "retryable": true,
            "type": "EXTRACTION",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/extraction-api/error/ERR::EXTRACTION::DATA_ERROR"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::EXTRACTION::INVALID_RULE": {
            "code": "ERR::EXTRACTION::INVALID_RULE",
            "http_code": 400,
            "description": "The extraction rule is invalid",
            "retryable": false,
            "type": "EXTRACTION",
            "links": {
                "Feature Documentation": "https://scrapfly.io/docs/extraction-api/rules-and-template",
                "Related Error Doc": "https://scrapfly.io/docs/extraction-api/error/ERR::EXTRACTION::INVALID_TEMPLATE"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::EXTRACTION::INVALID_TEMPLATE": {
            "code": "ERR::EXTRACTION::INVALID_TEMPLATE",
            "http_code": 400,
            "description": "The template used for extraction is invalid",
            "retryable": false,
            "type": "EXTRACTION",
            "links": {
                "Feature Documentation": "https://scrapfly.io/docs/extraction-api/rules-and-template",
                "Related Error Doc": "https://scrapfly.io/docs/extraction-api/error/ERR::EXTRACTION::INVALID_TEMPLATE"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::EXTRACTION::NO_CONTENT": {
            "code": "ERR::EXTRACTION::NO_CONTENT",
            "http_code": 422,
            "description": "Target response is empty",
            "retryable": false,
            "type": "EXTRACTION",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/extraction-api/error/ERR::EXTRACTION::NO_CONTENT"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::EXTRACTION::OPERATION_TIMEOUT": {
            "code": "ERR::EXTRACTION::OPERATION_TIMEOUT",
            "http_code": 408,
            "description": "Extraction Operation Timeout",
            "retryable": true,
            "type": "EXTRACTION",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/extraction-api/error/ERR::EXTRACTION::OPERATION_TIMEOUT"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::EXTRACTION::OUT_OF_CAPACITY": {
            "code": "ERR::EXTRACTION::OUT_OF_CAPACITY",
            "http_code": 429,
            "description": "Not able to extract more data, backend are out of capacity, retry later.",
            "retryable": true,
            "type": "EXTRACTION",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/extraction-api/error/ERR::EXTRACTION::OUT_OF_CAPACITY"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::EXTRACTION::TEMPLATE_NOT_FOUND": {
            "code": "ERR::EXTRACTION::TEMPLATE_NOT_FOUND",
            "http_code": 404,
            "description": "The provided template do not exist",
            "retryable": false,
            "type": "EXTRACTION",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/extraction-api/error/ERR::EXTRACTION::TEMPLATE_NOT_FOUND"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::EXTRACTION::TIMEOUT": {
            "code": "ERR::EXTRACTION::TIMEOUT",
            "http_code": 422,
            "description": "The extraction was too long or did not had enough time to complete",
            "retryable": true,
            "type": "EXTRACTION",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/extraction-api/error/ERR::EXTRACTION::TIMEOUT",
                "Timeout documentation": "https://scrapfly.io/docs/scrape-api/understand-timeout"
            },
            "billed": true,
            "fair_use": true
        },
        "ERR::FINGERPRINT::CONFIG_FINGERPRINT": {
            "code": "ERR::FINGERPRINT::CONFIG_ERROR",
            "http_code": 400,
            "description": "Parameters sent to the API are not valid",
            "retryable": false,
            "type": "FINGERPRINT",
            "links": [],
            "billed": false,
            "fair_use": false
        },
        "ERR::JOB::NOT_FOUND": {
            "code": "ERR::JOB::NOT_FOUND",
            "http_code": 400,
            "description": "Job Not Found",
            "retryable": true,
            "type": "ACCOUNT",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::JOB::NOT_FOUND"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::PROXY::POOL_NOT_AVAILABLE_FOR_TARGET": {
            "code": "ERR::PROXY::POOL_NOT_AVAILABLE_FOR_TARGET",
            "http_code": 422,
            "description": "The desired proxy pool is not available for the given domain - mostly well known protected domain which require at least residential networks",
            "retryable": false,
            "type": "PROXY",
            "links": {
                "API Usage": "https://scrapfly.io/docs/scrape-api/getting-started#api_param_proxy_pool",
                "Proxy Documentation": "https://scrapfly.io/docs/scrape-api/proxy",
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::PROXY::POOL_NOT_AVAILABLE_FOR_TARGET"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::PROXY::POOL_NOT_FOUND": {
            "code": "ERR::PROXY::POOL_NOT_FOUND",
            "http_code": 400,
            "description": "Provided Proxy Pool Name do not exists",
            "retryable": false,
            "type": "PROXY",
            "links": {
                "API Usage": "https://scrapfly.io/docs/scrape-api/getting-started#api_param_proxy_pool",
                "Proxy Documentation": "https://scrapfly.io/docs/scrape-api/proxy",
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::PROXY::POOL_NOT_FOUND"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::PROXY::POOL_UNAVAILABLE_COUNTRY": {
            "code": "ERR::PROXY::POOL_UNAVAILABLE_COUNTRY",
            "http_code": 400,
            "description": "Country not available for given proxy pool",
            "retryable": false,
            "type": "PROXY",
            "links": {
                "API Usage": "https://scrapfly.io/docs/scrape-api/getting-started#api_param_proxy_pool",
                "Proxy Documentation": "https://scrapfly.io/docs/scrape-api/proxy",
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::PROXY::POOL_UNAVAILABLE_COUNTRY"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::PROXY::RESOURCES_SATURATION": {
            "code": "ERR::PROXY::RESOURCES_SATURATION",
            "http_code": 422,
            "description": "Proxy are saturated for the desired country, you can try on other countries. They will come back as soon as possible",
            "retryable": true,
            "type": "PROXY",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::PROXY::RESOURCES_SATURATION"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::PROXY::TIMEOUT": {
            "code": "ERR::PROXY::TIMEOUT",
            "http_code": 422,
            "description": "Proxy connection or website was too slow and timeout",
            "retryable": true,
            "type": "PROXY",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::PROXY::TIMEOUT",
                "Timeout Documentation": "https://scrapfly.io/docs/scrape-api/understand-timeout"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::PROXY::UNAVAILABLE": {
            "code": "ERR::PROXY::UNAVAILABLE",
            "http_code": 422,
            "description": "Proxy is unavailable - The domain (mainly gov website) is restricted, You are using session feature and the proxy is unreachable at the moment",
            "retryable": true,
            "type": "PROXY",
            "links": {
                "API Usage": "https://scrapfly.io/docs/scrape-api/getting-started#api_param_proxy_pool",
                "Proxy Documentation": "https://scrapfly.io/docs/scrape-api/proxy",
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::PROXY::UNAVAILABLE"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::SCHEDULE::DISABLED": {
            "code": "ERR::SCHEDULE::DISABLED",
            "http_code": 400,
            "description": "The targeted schedule has been disabled",
            "retryable": false,
            "type": "SCHEDULER",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCHEDULE::DISABLED"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::SCRAPE::BAD_PROTOCOL": {
            "code": "ERR::SCRAPE::BAD_PROTOCOL",
            "http_code": 422,
            "description": "The protocol is not supported only http:// or https:// are supported",
            "retryable": false,
            "type": "SCRAPER",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::BAD_PROTOCOL"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::SCRAPE::BAD_UPSTREAM_RESPONSE": {
            "code": "ERR::SCRAPE::BAD_UPSTREAM_RESPONSE",
            "http_code": 200,
            "description": "The website you target respond with an unexpected status code (>400)",
            "retryable": false,
            "type": "SCRAPER",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::BAD_UPSTREAM_RESPONSE"
            },
            "billed": true,
            "fair_use": true
        },
        "ERR::SCRAPE::CONFIG_ERROR": {
            "code": "ERR::SCRAPE::CONFIG_ERROR",
            "http_code": 400,
            "description": "Scrape Configuration Error",
            "retryable": false,
            "type": "SCRAPER",
            "links": {
                "Getting Started": "https://scrapfly.io/docs/scrape-api/getting-started",
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::CONFIG_ERROR"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::SCRAPE::COST_BUDGET_LIMIT": {
            "code": "ERR::SCRAPE::COST_BUDGET_LIMIT",
            "http_code": 422,
            "description": "Cost budget has been reached, you must increase the budget to pass this target",
            "retryable": true,
            "type": "SCRAPER",
            "links": {
                "Checkout ASP documentation": "https://scrapfly.io/docs/scrape-api/anti-scraping-protection",
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::COST_BUDGET_LIMIT"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::SCRAPE::COUNTRY_NOT_AVAILABLE_FOR_TARGET": {
            "code": "ERR::SCRAPE::COUNTRY_NOT_AVAILABLE_FOR_TARGET",
            "http_code": 422,
            "description": "Country not available",
            "retryable": false,
            "type": "SCRAPER",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::COUNTRY_NOT_AVAILABLE_FOR_TARGET"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::SCRAPE::DNS_NAME_NOT_RESOLVED": {
            "code": "ERR::SCRAPE::DNS_NAME_NOT_RESOLVED",
            "http_code": 422,
            "description": "The DNS of the targeted website is not resolving or not responding",
            "retryable": false,
            "type": "SCRAPER",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::DNS_NAME_NOT_RESOLVED"
            },
            "billed": true,
            "fair_use": true
        },
        "ERR::SCRAPE::DOMAIN_NOT_ALLOWED": {
            "code": "ERR::SCRAPE::DOMAIN_NOT_ALLOWED",
            "http_code": 422,
            "description": "The Domain targeted is not allowed or restricted",
            "retryable": false,
            "type": "SCRAPER",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::DOMAIN_NOT_ALLOWED"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::SCRAPE::DOM_SELECTOR_INVALID": {
            "code": "ERR::SCRAPE::DOM_SELECTOR_INVALID",
            "http_code": 422,
            "description": "The DOM Selector is invalid",
            "retryable": false,
            "type": "SCRAPER",
            "links": {
                "Javascript Documentation": "https://scrapfly.io/docs/scrape-api/javascript-rendering",
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::DOM_SELECTOR_INVALID"
            },
            "billed": true,
            "fair_use": false
        },
        "ERR::SCRAPE::DOM_SELECTOR_INVISIBLE": {
            "code": "ERR::SCRAPE::DOM_SELECTOR_INVISIBLE",
            "http_code": 422,
            "description": "The requested DOM selected is invisible (Mostly issued when element is targeted for screenshot)",
            "retryable": false,
            "type": "SCRAPER",
            "links": {
                "Javascript Documentation": "https://scrapfly.io/docs/scrape-api/javascript-rendering",
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::DOM_SELECTOR_INVISIBLE"
            },
            "billed": true,
            "fair_use": false
        },
        "ERR::SCRAPE::DOM_SELECTOR_NOT_FOUND": {
            "code": "ERR::SCRAPE::DOM_SELECTOR_NOT_FOUND",
            "http_code": 422,
            "description": "The requested DOM selected was not found in rendered content within 15s",
            "retryable": false,
            "type": "SCRAPER",
            "links": {
                "Javascript Documentation": "https://scrapfly.io/docs/scrape-api/javascript-rendering",
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::DOM_SELECTOR_NOT_FOUND"
            },
            "billed": true,
            "fair_use": false
        },
        "ERR::SCRAPE::DRIVER_CRASHED": {
            "code": "ERR::SCRAPE::DRIVER_CRASHED",
            "http_code": 422,
            "description": "Driver used to perform the scrape can crash for many reason",
            "retryable": true,
            "type": "SCRAPER",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::DRIVER_CRASHED"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::SCRAPE::DRIVER_INSUFFICIENT_RESOURCES": {
            "code": "ERR::SCRAPE::DRIVER_INSUFFICIENT_RESOURCES",
            "http_code": 422,
            "description": "Driver do not have enough resource to render the page correctly",
            "retryable": true,
            "type": "SCRAPER",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::DRIVEDRIVER_INSUFFICIENT_RESOURCES"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::SCRAPE::DRIVER_TIMEOUT": {
            "code": "ERR::SCRAPE::DRIVER_TIMEOUT",
            "http_code": 422,
            "description": "Driver timeout - No response received",
            "retryable": true,
            "type": "SCRAPER",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::DRIVER_TIMEOUT"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::SCRAPE::FORMAT_CONVERSION_ERROR": {
            "code": "ERR::SCRAPE::FORMAT_CONVERSION_ERROR",
            "http_code": 422,
            "description": "Response format conversion failed, unsupported input content type",
            "retryable": false,
            "type": "SCRAPER",
            "links": {
                "API Format Parameter": "https://scrapfly.io/docs/scrape-api/getting-started#api_param_format",
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::FORMAT_CONVERSION_ERROR"
            },
            "billed": true,
            "fair_use": false
        },
        "ERR::SCRAPE::JAVASCRIPT_EXECUTION": {
            "code": "ERR::SCRAPE::JAVASCRIPT_EXECUTION",
            "http_code": 422,
            "description": "The javascript to execute goes wrong, please read the associated message to figure out the problem",
            "retryable": false,
            "type": "SCRAPER",
            "links": {
                "Checkout Javascript Rendering Documentation": "https://scrapfly.io/docs/scrape-api/javascript-rendering",
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::JAVASCRIPT_EXECUTION"
            },
            "billed": true,
            "fair_use": false
        },
        "ERR::SCRAPE::NETWORK_ERROR": {
            "code": "ERR::SCRAPE::NETWORK_ERROR",
            "http_code": 422,
            "description": "Network error happened between Scrapfly server and remote server",
            "retryable": true,
            "type": "SCRAPER",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::NETWORK_ERROR"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::SCRAPE::NETWORK_SERVER_DISCONNECTED": {
            "code": "ERR::SCRAPE::NETWORK_SERVER_DISCONNECTED",
            "http_code": 422,
            "description": "Server of upstream website closed unexpectedly the connection",
            "retryable": false,
            "type": "SCRAPER",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::NETWORK_SERVER_DISCONNECTED"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::SCRAPE::NO_BROWSER_AVAILABLE": {
            "code": "ERR::SCRAPE::NO_BROWSER_AVAILABLE",
            "http_code": 422,
            "description": "No browser available in the pool",
            "retryable": true,
            "type": "SCRAPER",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::NO_BROWSER_AVAILABLE"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::SCRAPE::OPERATION_TIMEOUT": {
            "code": "ERR::SCRAPE::OPERATION_TIMEOUT",
            "http_code": 504,
            "description": "This is a generic error for when timeout occur. It happened when internal operation took too much time",
            "retryable": true,
            "type": "SCRAPER",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::OPERATION_TIMEOUT",
                "Timeout Documentation": "https://scrapfly.io/docs/scrape-api/understand-timeout"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::SCRAPE::PLATFORM_NOT_AVAILABLE_FOR_TARGET": {
            "code": "ERR::SCRAPE::PLATFORM_NOT_AVAILABLE_FOR_TARGET",
            "http_code": 422,
            "description": "Platform not available",
            "retryable": false,
            "type": "SCRAPER",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::PLATFORM_NOT_AVAILABLE_FOR_TARGET"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::SCRAPE::PROJECT_QUOTA_LIMIT_REACHED": {
            "code": "ERR::SCRAPE::PROJECT_QUOTA_LIMIT_REACHED",
            "http_code": 429,
            "description": "The limit set to the current project has been reached",
            "retryable": true,
            "type": "SCRAPER",
            "links": {
                "Project Documentation": "https://scrapfly.io/docs/project",
                "Quota Pricing": "https://scrapfly.io/pricing",
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::PROJECT_QUOTA_LIMIT_REACHED"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::SCRAPE::QUOTA_LIMIT_REACHED": {
            "code": "ERR::SCRAPE::QUOTA_LIMIT_REACHED",
            "http_code": 429,
            "description": "You reach your scrape quota plan for the month. You can upgrade your plan if you want increase the quota",
            "retryable": false,
            "type": "SCRAPER",
            "links": {
                "Project Quota And Usage": "https://scrapfly.io/docs/project",
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::QUOTA_LIMIT_REACHED",
                "Upgrade you subscription": "https://scrapfly.io/docs/billing#change_plan"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::SCRAPE::SCENARIO_DEADLINE_OVERFLOW": {
            "code": "ERR::SCRAPE::SCENARIO_DEADLINE_OVERFLOW",
            "http_code": 422,
            "description": "Submitted scenario would require more than 30s to complete",
            "retryable": false,
            "type": "SCRAPER",
            "links": {
                "Javascript Scenario Documentation": "https://scrapfly.io/docs/scrape-api/javascript-scenario",
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::SCENARIO_DEADLINE_OVERFLOW",
                "Timeout Documentation": "https://scrapfly.io/docs/scrape-api/understand-timeout"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::SCRAPE::SCENARIO_EXECUTION": {
            "code": "ERR::SCRAPE::SCENARIO_EXECUTION",
            "http_code": 422,
            "description": "Javascript Scenario Failed",
            "retryable": false,
            "type": "SCRAPER",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::SCENARIO_EXECUTION"
            },
            "billed": true,
            "fair_use": false
        },
        "ERR::SCRAPE::SCENARIO_TIMEOUT": {
            "code": "ERR::SCRAPE::SCENARIO_TIMEOUT",
            "http_code": 422,
            "description": "Javascript Scenario Timeout",
            "retryable": true,
            "type": "SCRAPER",
            "links": {
                "Javascript Scenario Documentation": "https://scrapfly.io/docs/scrape-api/javascript-scenario",
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::SCENARIO_EXECUTION",
                "Timeout Documentation": "https://scrapfly.io/docs/scrape-api/understand-timeout"
            },
            "billed": true,
            "fair_use": false
        },
        "ERR::SCRAPE::SSL_ERROR": {
            "code": "ERR::SCRAPE::SSL_ERROR",
            "http_code": 422,
            "description": "Upstream website have SSL error",
            "retryable": false,
            "type": "SCRAPER",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::SSL_ERROR"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::SCRAPE::TOO_MANY_CONCURRENT_REQUEST": {
            "code": "ERR::SCRAPE::TOO_MANY_CONCURRENT_REQUEST",
            "http_code": 429,
            "description": "You reach concurrent limit of scrape request of your current plan or project if you set a concurrent limit at project level",
            "retryable": true,
            "type": "SCRAPER",
            "links": {
                "Quota Pricing": "https://scrapfly.io/pricing",
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::TOO_MANY_CONCURRENT_REQUEST"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::SCRAPE::UNABLE_TO_TAKE_SCREENSHOT": {
            "code": "ERR::SCRAPE::UNABLE_TO_TAKE_SCREENSHOT",
            "http_code": 422,
            "description": "Unable to take screenshot",
            "retryable": true,
            "type": "SCRAPER",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::UNABLE_TO_TAKE_SCREENSHOT"
            },
            "billed": true,
            "fair_use": false
        },
        "ERR::SCRAPE::UPSTREAM_TIMEOUT": {
            "code": "ERR::SCRAPE::UPSTREAM_TIMEOUT",
            "http_code": 422,
            "description": "The website you target made too much time to response",
            "retryable": false,
            "type": "SCRAPER",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::UPSTREAM_TIMEOUT"
            },
            "billed": true,
            "fair_use": true
        },
        "ERR::SCRAPE::UPSTREAM_WEBSITE_ERROR": {
            "code": "ERR::SCRAPE::UPSTREAM_WEBSITE_ERROR",
            "http_code": 422,
            "description": "The website you tried to scrape have configuration or malformed response",
            "retryable": true,
            "type": "SCRAPER",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::UPSTREAM_WEBSITE_ERROR"
            },
            "billed": true,
            "fair_use": true
        },
        "ERR::SCREENSHOT::INVALID_CONTENT_TYPE": {
            "code": "ERR::SCREENSHOT::INVALID_CONTENT_TYPE",
            "http_code": 422,
            "description": "Only content type text/html is supported for screenshot",
            "retryable": false,
            "type": "SCREENSHOT",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/screenshot-api/error/ERR::SCREENSHOT::INVALID_CONTENT_TYPE"
            },
            "billed": true,
            "fair_use": true
        },
        "ERR::SCREENSHOT::UNABLE_TO_TAKE_SCREENSHOT": {
            "code": "ERR::SCREENSHOT::UNABLE_TO_TAKE_SCREENSHOT",
            "http_code": 422,
            "description": "For some reason we were unable to take the screenshot",
            "retryable": true,
            "type": "SCREENSHOT",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/screenshot-api/error/ERR::SCREENSHOT::UNABLE_TO_TAKE_SCREENSHOT"
            },
            "billed": true,
            "fair_use": true
        },
        "ERR::SESSION::CONCURRENT_ACCESS": {
            "code": "ERR::SESSION::CONCURRENT_ACCESS",
            "http_code": 429,
            "description": "Concurrent access to the session has been tried. If your spider run on distributed architecture, the same session name is currently used by another scrape",
            "retryable": true,
            "type": "SCRAPER",
            "links": {
                "Checkout Session Documentation": "https://scrapfly.io/docs/scrape-api/session",
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::SESSION::CONCURRENT_ACCESS"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::THROTTLE::MAX_API_CREDIT_BUDGET_EXCEEDED": {
            "code": "ERR::THROTTLE::MAX_API_CREDIT_BUDGET_EXCEEDED",
            "http_code": 429,
            "description": "Your scrape request has been throttled. API Credit Budget reached. If it's not expected, please check your throttle configuration for the given project and env.",
            "retryable": true,
            "type": "THROTTLER",
            "links": {
                "API Documentation": "https://scrapfly.io/docs/scrape-api/getting-started#api_param_cost_budget",
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::THROTTLE::MAX_API_CREDIT_BUDGET_EXCEEDED"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::THROTTLE::MAX_CONCURRENT_REQUEST_EXCEEDED": {
            "code": "ERR::THROTTLE::MAX_CONCURRENT_REQUEST_EXCEEDED",
            "http_code": 429,
            "description": "Your scrape request has been throttled. Too many concurrent access to the upstream. If it's not expected, please check your throttle configuration for the given project and env.",
            "retryable": true,
            "type": "THROTTLER",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::THROTTLE::MAX_CONCURRENT_REQUEST_EXCEEDED",
                "Throttler Documentation": "https://scrapfly.io/docs/throttling"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::THROTTLE::MAX_REQUEST_RATE_EXCEEDED": {
            "code": "ERR::THROTTLE::MAX_REQUEST_RATE_EXCEEDED",
            "http_code": 429,
            "description": "Your scrape request as been throttle. Too much request during the 1m window. If it's not expected, please check your throttle configuration for the given project and env",
            "retryable": true,
            "type": "THROTTLER",
            "links": {
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::THROTTLE::MAX_REQUEST_RATE_EXCEEDED",
                "Throttler Documentation": "https://scrapfly.io/docs/throttling"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::WEBHOOK::DISABLED": {
            "code": "ERR::WEBHOOK::DISABLED",
            "http_code": 400,
            "description": "Given webhook is disabled, please check out your webhook configuration for the current project / env",
            "retryable": false,
            "type": "WEBHOOK",
            "links": {
                "Checkout Webhook Documentation": "https://scrapfly.io/docs/scrape-api/webhook",
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::WEBHOOK::DISABLED"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::WEBHOOK::ENDPOINT_UNREACHABLE": {
            "code": "ERR::WEBHOOK::ENDPOINT_UNREACHABLE",
            "http_code": 422,
            "description": "We were not able to contact your endpoint",
            "retryable": true,
            "type": "WEBHOOK",
            "links": {
                "Checkout Webhook Documentation": "https://scrapfly.io/docs/scrape-api/webhook",
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::WEBHOOK::ENDPOINT_UNREACHABLE"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::WEBHOOK::MAX_CONCURRENCY_REACHED": {
            "code": "ERR::WEBHOOK::QUEUE_FULL",
            "http_code": 429,
            "description": "You reach the maximum concurrency limit",
            "retryable": true,
            "type": "WEBHOOK",
            "links": {
                "Checkout Webhook Documentation": "https://scrapfly.io/docs/scrape-api/webhook",
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::WEBHOOK::MAX_CONCURRENCY_REACHED"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::WEBHOOK::MAX_RETRY": {
            "code": "ERR::WEBHOOK::MAX_RETRY",
            "http_code": 429,
            "description": "Maximum retry exceeded on your webhook",
            "retryable": false,
            "type": "WEBHOOK",
            "links": {
                "Checkout Webhook Documentation": "https://scrapfly.io/docs/scrape-api/webhook",
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::WEBHOOK::MAX_RETRY"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::WEBHOOK::NOT_FOUND": {
            "code": "ERR::WEBHOOK::NOT_FOUND",
            "http_code": 400,
            "description": "Unable to find the given webhook for the current project / env",
            "retryable": false,
            "type": "WEBHOOK",
            "links": {
                "Checkout Webhook Documentation": "https://scrapfly.io/docs/scrape-api/webhook",
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::WEBHOOK::NOT_FOUND"
            },
            "billed": false,
            "fair_use": false
        },
        "ERR::WEBHOOK::QUEUE_FULL": {
            "code": "ERR::WEBHOOK::QUEUE_FULL",
            "http_code": 429,
            "description": "You reach the limit of scheduled webhook - You must wait pending webhook are processed",
            "retryable": true,
            "type": "WEBHOOK",
            "links": {
                "Checkout Webhook Documentation": "https://scrapfly.io/docs/scrape-api/webhook",
                "Related Error Doc": "https://scrapfly.io/docs/scrape-api/error/ERR::WEBHOOK::QUEUE_FULL"
            },
            "billed": false,
            "fair_use": false
        }
    }
}
```
