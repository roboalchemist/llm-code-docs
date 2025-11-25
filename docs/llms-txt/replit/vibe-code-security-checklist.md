# Source: https://docs.replit.com/tutorials/vibe-code-security-checklist.md

# Security checklist for vibe coding

> Follow this comprehensive security checklist to ensure your vibe coded applications follow best security practices.

export const AuthorCard = ({img = "https://replit.com/cdn-cgi/image/width=256,quality=80,format=auto/https://storage.googleapis.com/replit/images/1730840970400_e885f16578bbbb227adbfeb7b979be34.jpeg", href = "https://youtube.com/@mattpalmer", name = "Matt Palmer", role = "Head of Developer Relations"}) => {
  return <a href={href} target="_blank" className="card block not-prose font-normal group relative my-2 ring-2 ring-transparent rounded-xl bg-white/50 dark:bg-codeblock/50 border border-gray-100 shadow-md dark:shadow-none shadow-gray-300/10 dark:border-gray-800/50 overflow-hidden cursor-pointer hover:!border-primary dark:hover:!border-primary-light">
      <div className="flex items-center gap-2 p-4">
        <div className="flex-shrink-0">
          <img src={img} alt={name} className="w-12 h-12 rounded-full object-cover" />
        </div>
        <div className="flex-grow">
          <h3 className="text-base font-semibold mb-0.5 text-inherit">{name}</h3>
          <p className="text-sm text-gray-600 dark:text-gray-400 m-0">{role}</p>
        </div>
      </div>
    </a>;
};

<AuthorCard />

This guide provides a comprehensive security checklist to ensure your vibe coded applications follow best security practices.

While Replit provides many security features [out of the box](/tutorials/vibe-code-securely), it's important to understand and implement more security measures for your specific application needs.

<iframe src="https://www.youtube.com/embed/0D9FMFyNBWo" title="Vibe code security checklist" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

## Prerequisites

* A Replit account
* Basic understanding of your preferred programming language
* Familiarity with the Replit Workspace
* An application you're building on Replit

## Front-end security

<AccordionGroup>
  <Accordion title="HTTPS everywhere" icon="lock">
    Replit uses HTTPS by default for all applications. So you don't need to worry about it!
  </Accordion>

  <Accordion title="Input validation and sanitization" icon="shield-check">
    Always validate and sanitize user input to prevent cross-site scripting (XSS) attacks:

    ```javascript  theme={null}
    // Bad: Direct use of user input
    element.innerHTML = userInput;

    // Good: Sanitize input before using
    import { sanitize } from 'some-sanitizer-library';
    element.innerHTML = sanitize(userInput);
    ```

    You can ask Assistant:

    ```
    Help me validate and sanitize inputs to protect against XSS attacks
    ```
  </Accordion>

  <Accordion title="Keep sensitive data out of the browser" icon="eye-slash">
    You should use Replit Secrets to store sensitive information like API keys.

    Be sure you don't pass secrets to the client side or put them in the following places:

    * Local storage
    * Session storage
    * Client-side JavaScript
    * Cookies without proper security attributes

    You can ask Assistant / Agent:

    ```
    Help me keep sensitive data out of the browser. Am I doing this correctly?
    ```
  </Accordion>

  <Accordion title="CSRF protection" icon="shield">
    Implement Cross-Site Request Forgery (CSRF) protection for forms:

    ```javascript  theme={null}
    // Example of CSRF token implementation
    const csrfToken = generateToken();
    session.csrfToken = csrfToken;
    ```

    You can ask Agent / Assistant:

    ```
    Help me implement CSRF tokens for forms
    ```
  </Accordion>
</AccordionGroup>

## Back-end security

<AccordionGroup>
  <Accordion title="Authentication fundamentals" icon="key">
    When implementing authentication:

    * Use Replit Auth when possible
    * If building custom auth, use established libraries
    * Never store plain text passwords

    Ask Agent:

    ```
    Help me implement authentication for my application with Replit Auth
    ```
  </Accordion>

  <Accordion title="Authorization checks" icon="user-lock">
    Always verify permissions before performing actions:

    ```javascript  theme={null}
    // Example authorization check
    if (!user.canAccess(resource)) {
      return res.status(403).send('Access denied');
    }
    ```

    Ask Agent:

    ```
    Help me implement authorization checks for my application
    ```
  </Accordion>

  <Accordion title="API endpoint protection" icon="shield">
    Secure your API endpoints:

    * Add authentication to sensitive endpoints
    * Implement proper CORS settings
    * Consider rate limiting

    Ask Assistant:

    ```
    How do I properly authenticate endpoints in my app?
    ```
  </Accordion>

  <Accordion title="SQL injection prevention" icon="database">
    Agent uses ORMs by default, which helps prevent SQL injection. If writing custom database queries:

    ```javascript  theme={null}
    // Bad: String concatenation in queries
    db.query(`SELECT * FROM users WHERE username = '${username}'`);

    // Good: Parameterized queries with ORM
    db.query('SELECT * FROM users WHERE username = ?', [username]);
    ```
  </Accordion>

  <Accordion title="Security headers" icon="code">
    Add important security headers to your application:

    ```html  theme={null}
    <!-- In index.html or through your back-end -->
    <meta http-equiv="X-Frame-Options" content="DENY">
    <meta http-equiv="X-Content-Type-Options" content="nosniff">
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'">
    ```

    You can scan your site at [securityheaders.com](https://securityheaders.com) for recommendations.

    Ask Assistant:

    ```
    Can you add the security headers to my application?
    ```
  </Accordion>
</AccordionGroup>

## Ongoing security practices

<AccordionGroup>
  <Accordion title="Keep dependencies updated" icon="arrow-rotate-right">
    Regularly check for outdated packages that might have vulnerabilities:

    ```bash  theme={null}
    npm audit
    ```
  </Accordion>

  <Accordion title="Proper error handling" icon="exclamation">
    Don't expose sensitive information in error messages:

    ```javascript  theme={null}
    // Bad: Exposing sensitive details
    catch (err) {
      res.status(500).send(`Database error: ${err.message}`);
    }

    // Good: Generic error message
    catch (err) {
      console.error(err); // Log internally
      res.status(500).send('An error occurred');
    }
    ```

    Ask Agent:

    ```
    Help me implement proper error handling for my application
    ```
  </Accordion>

  <Accordion title="Secure cookies" icon="cookie">
    When using cookies:

    * Set HttpOnly flag to prevent JavaScript access
    * Use Secure attribute to require HTTPS
    * Implement SameSite attribute to prevent CSRF

    Ask Agent:

    ```
    Help me secure my cookies for my application
    ```
  </Accordion>

  <Accordion title="File upload security" icon="upload">
    If your application allows file uploads:

    * Restrict file types and sizes
    * Scan for malware if possible
    * Store files in Replit's object storage
    * Generate new filenames rather than using user-provided ones

    Ask Agent:

    ```
    Help me secure my file uploads for my application
    ```
  </Accordion>

  <Accordion title="Rate limiting" icon="clock">
    Implement rate limiting for API endpoints, especially authentication-related ones:

    ```javascript  theme={null}
    // Example rate limiting middleware
    const rateLimit = require('express-rate-limit');

    const limiter = rateLimit({
      windowMs: 15 * 60 * 1000, // 15 minutes
      max: 100 // limit each IP to 100 requests per windowMs
    });

    app.use('/api/', limiter);
    ```

    Ask Agent:

    ```
    Help me implement rate limiting for my application
    ```
  </Accordion>
</AccordionGroup>

## Checklist

Here's the above in a checklist to help you stay on top of your security practices.

## Front-end security

|   | Security Measure                          | Description                                                      |
| - | ----------------------------------------- | ---------------------------------------------------------------- |
| ☐ | Use HTTPS everywhere                      | Prevents basic eavesdropping and man-in-the-middle attacks       |
| ☐ | Input validation and sanitization         | Prevents XSS attacks by validating all user inputs               |
| ☐ | Don't store sensitive data in the browser | No secrets in local storage or client-side code                  |
| ☐ | CSRF protection                           | Implement anti-CSRF tokens for forms and state-changing requests |
| ☐ | Never expose API keys in frontend         | API credentials should always remain server-side                 |

## Back-end security

|   | Security Measure            | Description                                                           |
| - | --------------------------- | --------------------------------------------------------------------- |
| ☐ | Authentication fundamentals | Use established libraries, proper password storage (hashing+salting)  |
| ☐ | Authorization checks        | Always verify permissions before performing actions                   |
| ☐ | API endpoint protection     | Implement proper authentication for every API endpoint                |
| ☐ | SQL injection prevention    | Use parameterized queries or ORMs, never raw SQL with user input      |
| ☐ | Basic security headers      | Implement X-Frame-Options, X-Content-Type-Options, and HSTS           |
| ☐ | DDoS protection             | Use a CDN or cloud service with built-in DDoS mitigation capabilities |

## Practical security habits

|   | Security Measure          | Description                                                            |
| - | ------------------------- | ---------------------------------------------------------------------- |
| ☐ | Keep dependencies updated | Most vulnerabilities come from outdated libraries                      |
| ☐ | Proper error handling     | Don't expose sensitive details in error messages                       |
| ☐ | Secure cookies            | Set HttpOnly, Secure and SameSite attributes                           |
| ☐ | File upload security      | Validate file types, sizes, and scan for malicious content             |
| ☐ | Rate limiting             | Implement on all API endpoints, especially authentication-related ones |
