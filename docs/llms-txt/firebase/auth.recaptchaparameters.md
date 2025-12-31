# Source: https://firebase.google.com/docs/reference/js/auth.recaptchaparameters.md.txt

# RecaptchaParameters interface

Interface representing reCAPTCHA parameters.

See the [reCAPTCHA docs](https://developers.google.com/recaptcha/docs/display#render_param) for the list of accepted parameters. All parameters are accepted except for `sitekey`: Firebase Auth provisions a reCAPTCHA for each project and will configure the site key upon rendering.

For an invisible reCAPTCHA, set the `size` key to `invisible`.

**Signature:**  

    export interface RecaptchaParameters