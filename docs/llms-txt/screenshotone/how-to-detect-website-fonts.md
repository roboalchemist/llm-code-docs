# Source: https://screenshotone.com/docs/guides/how-to-detect-website-fonts/

# Detect website fonts

## How to use the font detection API

The font detection API is available in the [ScreenshotOne API "take" method as an additional option](/docs/options/#metatada_fonts).

```
https://api.screenshotone.com/take?metatada_fonts=true&url=https://example.com&access_key=<your access key>&response_type=json
```

The result is:

```json
{
    "fonts": [
        {
            "first": "Arial",
            "fallback": ["Helvetica", "sans-serif"],
            "elements": ["p"]
        }
        // ...
    ]
}
```

## Use cases

There are many use cases for using the font detection API by ScreenshotOne:

- **[Design tools font detection](/use-cases/design-apps-font-detection/)**: integrate font detection to help designers identify and analyze typography on any website.
- **[Brand consistency font checks](/use-cases/brand-consistency-font-checks/)**: automatically verify font consistency across web pages to maintain brand integrity.
- **[Automated web audits with font analysis](/use-cases/automated-web-audits-fonts/)**: generate comprehensive typography reports to optimize websites for aesthetics and performance.
- **[Educational font detection tool](/use-cases/educational-font-detection/)**: enable students to explore and learn from typography used in real-world web applications.
- **[Font accessibility checks](/use-cases/font-accessibility-checks/)**: analyze whether websites use readable fonts for people with visual impairments or reading disabilities.
- **[Font marketplace enhancement](/use-cases/font-marketplace-enhancement/)**: show how fonts look on live websites to enhance the customer purchasing experience.
- **[Font trends analysis](/use-cases/font-trends/)**: provide insights into typography trends of top-ranking websites across various industries.
- **[UX font analysis](/use-cases/ux-font-analysis/)**: examine the impact of different fonts on user engagement and website usability.
- **[Browser extension font detection](/use-cases/browser-extension-font-detection/)**: allow users to identify and learn about fonts on any website with a single click.
- **[Font legal compliance check](/use-cases/font-legal-compliance/)**: ensure fonts used on websites are legally compliant to avoid copyright issues.

## Support

In case you have any questions or feedback, please, feel free to reach out at `support@screenshotone.com` and we will be happy to help.