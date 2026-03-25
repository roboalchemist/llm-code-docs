# Source: https://docs.pentaho.com/pba/pentaho-interactive-reports-cp/add-logos-to-interactive-reports/change-logo-alignment.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-interactive-reports-cp/add-logos-to-interactive-reports/change-logo-alignment.md

# Change logo alignment

You can set the alignment of logos in Interactive Report templates to left, right, or center.

1. Navigate to the `\pentaho-server\tomcat\webapps\pentaho\WEB-INF\classes` folder, locate the file `classic-engine.properties`, and open it in a text editor.
2. Find the attribute **org.pentaho.reporting.engine.classic.core.environment.pirTemplateLogoAlignment**.

   The default alignment is set to **right**.
3. Change the default alignment to **left** or **center** as needed and save the file.

   **Note:** The only allowed values are **left**, **right**, and center.
4. Restart the server for the changes to take effect.
