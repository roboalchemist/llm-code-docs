# Source: https://docs.axonius.com/docs/using-the-simulator.md

# Using the Dynamic Value Statement Simulator

<Callout icon="📘" theme="info">
  Note

  All examples on this page contain demo data.
</Callout>

Axonius provides the **Dynamic Value Statement Simulator** tool to effectively debug Dynamic Value Statements. You can use the Simulator to create Dynamic Value Statements in Enforcement Sets that produce valid results as opposed to fallback (default) values.

When users run Enforcement Sets configured with Dynamic Value Statements, although the statements have been validated successfully, the Enforcement Action fields are sometimes configured with fallback (default) values instead of the expected calculated results. This can be due to a number of reasons, including:

* Function failure - If a function in the Dynamic Value Statement fails or is unable to execute successfully, it does not return a valid result.
* Empty Fields - Empty fields in the Dynamic Value Statement can prevent proper calculations.
* Type Mismatch - Discrepancies between the type of value stored in the field (e.g., string, integer, boolean) and the Action Form field type may cause errors.

Use the Simulator to:

* Simulate the execution of a Dynamic Value Statement on individual assets returned from a query, making it easier to isolate and diagnose issues specific to that asset.
* Review the results displayed by the Simulator for each component in the statement. This breakdown helps you identify which part of the statement is not functioning as intended.
* Correct the statement. If you identify components that give an error or do not return the expected results, you can make adjustments and rerun the simulation until the desired outcomes are achieved.

**To debug a Dynamic Value statement using the Simulator**

1. Make sure that the Dynamic Value statement is valid and that you have saved the Enforcement Set.

<Callout icon="📘" theme="info">
  Note

  The Simulator works only on validated statements in saved Enforcement Sets. If not validated, a Syntax validation error occurs and the Simulator does not work.
</Callout>

2. Above the Dynamic Value statement, click **Simulate** to activate the Simulator.

![SimulateDynamicStatement](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulateDynamicStatement.png)

<Callout icon="📘" theme="info">
  Note

  You can also enter the Simulator directly from the Wizard, after you have saved the Enforcement Set.
  ![SimulateFromWizard](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulateFromWizard.png)
</Callout>

3. **Simulator Mode** opens, and the Simulator immediately selects a random asset to use in the simulation. The selected asset's name (max 12 characters) appears above the statement near **Simulated on**. Hover over the asset name to see the full name.
   ![AssetnameTooltip](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetnameTooltip.png)

4. Hover on a component in the statement that you want the Simulator to test on the asset.  Components include functions and adapter fields; the Simulator does not debug Enforcement Action configuration fields. It is recommended to first test the innermost component, as if it results in an error, simulation of any outer component will result in the same error. The selected component is highlighted in turquoise, and the simulation immediately executes on that component. The **Result** of the simulation appears below the statement box.

   * When the component is compatible with the statement, the Simulator shows the results in terms of Field type, Value type, and Value.

   ![SimulatorExample](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulatorExample.png)

   * When the component is incompatible with the statement or has an empty value, the phrase is highlighted in red, and an error is shown in the Results area.

5. If the **Result** shows an error (in red), click **Exit Simulator Mode** to leave Simulator mode and fix the component. Then, run the Simulator again from the beginning of this procedure.

6. You can click the asset to view its [asset profile](/docs/en/asset-profile-page).

7. You can click the **Replace Asset** icon ![ReplaceIcon](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ReplaceIcon.png) to have the system automatically select a different asset for the simulation so that you can test various scenarios.

8. When you finish debugging the statement, click **Exit Simulator Mode** to leave the Simulator.

9. The Enforcement Set is now ready to run - either manually or according to a configured schedule. Learn more about [running Enforcement Sets](/docs/run-ec-set).

### Example 1 - Running the Simulator on an All Statement

The following example shows how you can use the Simulator on an **All** statement.

1. Validate the statement and save the Enforcement Set.

2. Click **Simulate** on the validated statement.

   ![SimulatorExample1A](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulatorExample1A.png)

3. The statement enters **Simulator Mode** and the system randomly selects a host name, for instance **win7b**, as the asset on which to simulate the statement.

4. Hover over the innermost component in the statement. The **device.specific\_data.data.hostname** field is highlighted in turquoise, and results are displayed below the statement.

   ![SimulatorExample1B](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulatorExample1B.png)

5. Now hover over the **count** function. The Simulator immediately shows the results of this function on the asset.

   ![SimulatorExample1C](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulatorExample1C.png)

6. The results of the **set\_value** function are those of the **count** function. The field on the configuration dialog (**form.field\_integer**) of the Enforcement Action is filled with the value **3** (in this example).

   ![SimulatorExample1D](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulatorExample1D.png)

### Example 2 - Running the Simulator on an All Statement

The following is another example showing how you can use the Simulator on an **All** statement.

1. Validate the statement and save the Enforcement Set.
2. Click **Simulate** on the validated statement. The statement enters **Simulator Mode** and the system randomly selects an asset on which to simulate the statement (in this example, **dbnginx-53971222-prod**). Hover over each component of the statement, as shown in the following screens. The component currently being analyzed is highlighted in turquoise. In each case, you can see the result for the component below the statement.
3. Check that this is the desired result, and if not, click the Replace Asset icon to run on a different asset. Adjust the statement or query as required. Remember to validate the statement and save the Enforcement Set before you run the Simulator again.

   ![SimulatorExample5A](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulatorExample5A.png)

   ![SimulatorExample5B](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulatorExample5B.png)

   ![SimulatorExample5C](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulatorExample5C.png)

   ![SimulatorExample5D](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulatorExample5D.png)

### Example 3 - Debugging a Switch/Case Statement

The following example shows how you can use the Simulator to debug a **Switch/Case** statement.

1. Validate the statement and save the Enforcement Set.

2. Click **Simulate** on the validated statement.

   ![SimulatorExample4A](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulatorExample4A.png)

3. The statement enters **Simulator Mode** and the system randomly selects an asset (in this case, name begins with **Domain Cont**) on which to simulate the statement.

4. Check the **then** clause of the statement: Hover over the adapter field. It is highlighted in turquoise. The results are displayed below the statement box.

   ![SimulatorExample4B](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulatorExample4B.png)

5. Click the Replace Asset icon to replace the asset (in this case, to **ML-Lab**), and you then get valid results for the field as in step 2. Next, hover over **multiply**. The following error occurs.
   ![SimulatorExample4C](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulatorExample4C.png)

6. Leave the Simulator, correct the statement to run the **max** function on the array so that **multiply** works, validate the statement, and save the Enforcement Set to save these changes.

7. Re-enter the Simulator, hover over **multiply**, and you can see that the results are now valid.
   ![SimulatorExample4D](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulatorExample4D.png)

   ![SimulatorExample4E](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulatorExample4E.png)

   ![SimulatorExample4F](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulatorExample4F.png)

8. Now check the **switch** clause of the statement. An error occurs when performing the **subtract** function.\
   ![SimulatorExample4J](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulatorExample4J.png)

   ![SimulatorExample4K](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulatorExample4K.png)

   ![SimulatorExample4L](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulatorExample4L.png)

9. Leave Simulator Mode and update the statement to run the **max** function on the second item in the **subtract** function. Validate the statement and save the Enforcement Set to save these changes. Run the Simulator again, hover over **subtract**, and the results are now valid.

![SimulatorExample4M](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulatorExample4M.png)

![SimulatorExample4N](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulatorExample4N.png)

![SimulatorExample4O](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulatorExample4O.png)

![SimulatorExample4P](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulatorExample4P.png)

![SimulatorExample4Q](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulatorExample4Q.png)

6. Now check the **case** clause of the statement. An error occurs in this component due to an empty asset field.

   ![SimulatorExample4H](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulatorExample4H.png)

7. Leave Simulator Mode and replace this field with the number **90.0**. Validate the statement and save the Enforcement Set to save these changes. Run the Simulator again, hover over **gt**, and you can see that the results are now valid.

   ![SimulatorExample4R](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulatorExample4R.png)