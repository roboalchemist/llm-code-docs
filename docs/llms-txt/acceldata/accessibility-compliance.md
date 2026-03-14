# Source: https://docs.acceldata.io/documentation/accessibility-compliance.md

# Accessibility Compliance


Acceldata ensures that the ADOC application adheres to ADA compliance standards, specifically addressing **WCAG Level AA** accessibility guidelines. Comprehensive enhancements have been implemented for critical pages, including **Login**, **Alerts Listing**, and **Alert Details**.

---

### Summary of Accessibility Enhancements

Accessibility improvements include:


| **Accessibility Feature** | **Implementation Details** | 
| ---- | ---- | 
| Keyboard Navigation | All interactive elements accessible by keyboard (tab order improved, logical flow ensured). | 
| ARIA Labels and Roles | Properly defined for improved screen reader compatibility. | 
| Color and Contrast Adjustments | Updated color scheme to meet contrast ratio standards (at least 4.5:1 contrast ratio). | 
| Structural HTML and CSS Improvements | Ensured semantic correctness (e.g., using `<button>` instead of `<div>`). | 
| Consistent and Logical Navigation | Ensured uniform navigation patterns across pages. | 
| Dynamic Elements Management | Ensured announcements of dynamic changes to screen reader users. | 


---

### Testing Methodology

Accessibility compliance was validated using:

- **Accessibility Insights for Web (Chrome Plugin):** Quick Test (automated and manual) and Detailed accessibility audits and manual tests
- **Lighthouse Accessibility Audit (Chrome Developer Tools):** Quick automated accessibility checks and scoring

---

### Implementation Results


| **Page Name** | **Before Implementation** | **After Implementation** | 
| ---- | ---- | ---- | 
| **Login** | 28% failure &#124; Lighthouse score: 81 | 0% failure &#124; Lighthouse score: 88 | 
| **Alerts Listing** | 56% failure &#124; Lighthouse score: 69 | 1% failure &#124; Lighthouse score: 86 | 
| **Alert Details** | 28% failure &#124; Lighthouse score: 81 | 0% failure &#124; Lighthouse score: 91 | 
| **Discover Assets** | 56% failure &#124; Lighthouse score: 69 | 0% failure &#124; Lighthouse score: 85 | 
| **Asset Details** | 46% failure &#124; Lighthouse score: 77 | 1% failure &#124; Lighthouse score: 82 | 
| **Data Sources** | 46% failure &#124; Lighthouse score: 97 | 1% failure &#124; Lighthouse score: 97 | 



