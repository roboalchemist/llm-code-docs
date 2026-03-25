# Source: https://docs.linkup.so/pages/documentation/tutorials/peers-finder/peers-finder.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Peers Finder

> Learn how to find comparable companies using the Linkup API with Google Sheets

Struggling to identify your company's true competitors and industry peers? This comprehensive step-by-step guide shows you how to leverage the powerful Linkup API with Google Sheets to build your own automated peer comparison tool. Perfect for investors, market analysts, and business strategists who need accurate competitive intelligence without expensive enterprise solutions.

Don't walk away if you're not a developer! This tutorial is designed to be accessible for everyone - no coding experience required. Just follow our simple copy-paste instructions and clear screenshots to set up your own peer comparison tool in minutes.

## Prerequisites

Before starting, ensure you have:

* A Google account
* A Linkup API key (required for making requests)

<Card title="Get your API key" icon="key" href="https://app.linkup.so" horizontal="True">
  Create a Linkup account for free to get your API key.
</Card>

## Setup Guide

### Step 1: Open Google Sheets

1. Open a new Google Sheet
2. Name it "Company Peer Finder" or any name you prefer

### Step 2: Access Apps Script

1. Click on "Extensions" in the menu bar
2. Select "Apps Script" from the dropdown menu

<img src="https://mintcdn.com/linkup-8b5c238e/eJ8cJjJOf3NSdL-t/pages/documentation/tutorials/peers-finder/assets/extensions-menu.png?fit=max&auto=format&n=eJ8cJjJOf3NSdL-t&q=85&s=d88bd3899994b87cf41bf70578079a94" alt="Extensions Menu" width="1486" height="558" data-path="pages/documentation/tutorials/peers-finder/assets/extensions-menu.png" />
*1: Accessing Apps Script through the Extensions menu*

### Step 3: Set Up the Script

1. In the Apps Script editor, delete any existing code
2. Copy and paste the following script:

```javascript  theme={null}
// Google Apps Script for Company Peer Finder with direct Linkup integration
// This script uses Linkup API to find peer companies based on input companies

// Configuration - replace with your actual Linkup API key
const LINKUP_API_KEY = "YOUR_API_KEY"; // Replace with your Linkup API key
const LINKUP_API_URL = "https://api.linkup.so/v1"; // Linkup API base URL

// Create the menu when the spreadsheet opens
function onOpen() {
  const ui = SpreadsheetApp.getUi();
  ui.createMenu('Peer Finder')
    .addItem('Extract Common Characteristics', 'extractCommonCharacteristics')
    .addItem('Find Peer Companies', 'findPeerCompanies')
    .addToUi();
}

// Function to extract common characteristics from input companies
function extractCommonCharacteristics() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const inputSheet = ss.getSheetByName('Input Companies');
  const charSheet = ss.getSheetByName('Characteristics');
  
  if (!inputSheet || !charSheet) {
    setupSpreadsheet();
    return;
  }

  const companies = inputSheet.getRange('A2:A6').getValues().flat().filter(Boolean);
  if (companies.length === 0) {
    SpreadsheetApp.getUi().alert('Please enter at least one company name in the Input Companies sheet.');
    return;
  }

  const characteristics = [];
  for (const company of companies) {
    const response = fetchCompanyData(company);
    if (response && response.characteristics) {
      characteristics.push(...response.characteristics);
    }
  }

  // Count frequency of each characteristic
  const charCount = {};
  characteristics.forEach(char => {
    charCount[char] = (charCount[char] || 0) + 1;
  });

  // Sort by frequency
  const sortedChars = Object.entries(charCount)
    .sort((a, b) => b[1] - a[1])
    .map(([char, count]) => [char, count, false]);

  // Update characteristics sheet
  charSheet.clear();
  charSheet.getRange(1, 1, 1, 3).setValues([['Characteristic', 'Frequency', 'Use for Search']]);
  if (sortedChars.length > 0) {
    charSheet.getRange(2, 1, sortedChars.length, 3).setValues(sortedChars);
  }
}

// Function to find peer companies based on selected characteristics
function findPeerCompanies() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const charSheet = ss.getSheetByName('Characteristics');
  const resultsSheet = ss.getSheetByName('Peer Companies');
  
  if (!charSheet || !resultsSheet) {
    setupSpreadsheet();
    return;
  }

  const selectedChars = charSheet.getRange('B2:B').getValues()
    .flat()
    .map((checked, i) => checked ? charSheet.getRange(i + 2, 1).getValue() : null)
    .filter(Boolean);

  if (selectedChars.length === 0) {
    SpreadsheetApp.getUi().alert('Please select at least one characteristic to use for finding peer companies.');
    return;
  }

  const peers = findPeersByCharacteristics(selectedChars);
  
  // Update results sheet
  resultsSheet.clear();
  resultsSheet.getRange(1, 1, 1, 4).setValues([['Company', 'Match Score', 'Industry', 'Size']]);
  if (peers.length > 0) {
    resultsSheet.getRange(2, 1, peers.length, 4).setValues(peers);
  }
}

// Helper function to fetch company data from Linkup API
function fetchCompanyData(companyName) {
  const options = {
    method: 'GET',
    headers: {
      'Authorization': `Bearer ${LINKUP_API_KEY}`,
      'Content-Type': 'application/json'
    }
  };

  try {
    const response = UrlFetchApp.fetch(`${LINKUP_API_URL}/companies/search?q=${encodeURIComponent(companyName)}`, options);
    return JSON.parse(response.getContentText());
  } catch (error) {
    console.error(`Error fetching data for ${companyName}:`, error);
    return null;
  }
}

// Helper function to find peers based on characteristics
function findPeersByCharacteristics(characteristics) {
  const options = {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${LINKUP_API_KEY}`,
      'Content-Type': 'application/json'
    },
    payload: JSON.stringify({ characteristics })
  };

  try {
    const response = UrlFetchApp.fetch(`${LINKUP_API_URL}/companies/peers`, options);
    return JSON.parse(response.getContentText());
  } catch (error) {
    console.error('Error finding peers:', error);
    return [];
  }
}

// Function to set up the initial spreadsheet structure
function setupSpreadsheet() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  
  // Create or clear sheets
  const sheets = ['Input Companies', 'Characteristics', 'Peer Companies'];
  sheets.forEach(sheetName => {
    let sheet = ss.getSheetByName(sheetName);
    if (!sheet) {
      sheet = ss.insertSheet(sheetName);
    }
    sheet.clear();
  });

  // Set up Input Companies sheet
  const inputSheet = ss.getSheetByName('Input Companies');
  inputSheet.getRange('A1').setValue('Enter up to 5 company names below:');
  inputSheet.getRange('A2:A6').setBackground('#f3f3f3');

  // Set up Characteristics sheet
  const charSheet = ss.getSheetByName('Characteristics');
  charSheet.getRange('A1:C1').setValues([['Characteristic', 'Frequency', 'Use for Search']]);
  charSheet.getRange('C2:C').setDataValidation(SpreadsheetApp.newDataValidation()
    .requireCheckbox()
    .build());

  // Set up Peer Companies sheet
  const resultsSheet = ss.getSheetByName('Peer Companies');
  resultsSheet.getRange('A1:D1').setValues([['Company', 'Match Score', 'Industry', 'Size']]);

  // Hide unused sheets
  ss.getSheets().forEach(sheet => {
    if (!sheets.includes(sheet.getName())) {
      sheet.hideSheet();
    }
  });

  SpreadsheetApp.getUi().alert('Spreadsheet setup complete! You can now enter company names and use the Peer Finder menu.');
}
```

### Step 4: Configure Your API Key

1. Replace `YOUR_API_KEY` with your actual Linkup API key
2. If you don't have an API key:
   * Go to [app.linkup.so](https://app.linkup.so)
   * Create an account or sign in
   * Navigate to your API settings
   * Copy your API key

### Step 5: Save the Script

1. Click the "Save" button (or press Ctrl+S/Cmd+S)

### Step 6: Authorize the Script

1. When prompted, authorize the script to:
   * Access your Google Sheets
   * Make external API calls
   * Display dialogs

<img src="https://mintcdn.com/linkup-8b5c238e/eJ8cJjJOf3NSdL-t/pages/documentation/tutorials/peers-finder/assets/authorization-screen.png?fit=max&auto=format&n=eJ8cJjJOf3NSdL-t&q=85&s=4b634da08dc98c6465f0e0353285871d" alt="Authorization Screen" width="1480" height="762" data-path="pages/documentation/tutorials/peers-finder/assets/authorization-screen.png" />
*2: The Google authorization screen*

### Step 7: Initialize the Spreadsheet

1. Click "Run" and select "SetupSpreadsheet"

<img src="https://mintcdn.com/linkup-8b5c238e/eJ8cJjJOf3NSdL-t/pages/documentation/tutorials/peers-finder/assets/setup-spreadsheet.png?fit=max&auto=format&n=eJ8cJjJOf3NSdL-t&q=85&s=d2943bc3180e915af1bdee5fbe7477fa" alt="Setup Spreadsheet" width="1999" height="948" data-path="pages/documentation/tutorials/peers-finder/assets/setup-spreadsheet.png" />
*3: Selecting SetupSpreadsheet*

### Step 8: Verify Setup

1. Look for a confirmation popup in your main sheet

<img src="https://mintcdn.com/linkup-8b5c238e/eJ8cJjJOf3NSdL-t/pages/documentation/tutorials/peers-finder/assets/confirmation-popup.png?fit=max&auto=format&n=eJ8cJjJOf3NSdL-t&q=85&s=8a039b250547deea867529e58fc3df4e" alt="Confirmation Popup" width="1872" height="1072" data-path="pages/documentation/tutorials/peers-finder/assets/confirmation-popup.png" />
*4: The confirmation popup*

### Step 9: Launch the Tool

1. Click "Run" and select "OnOpen"

<img src="https://mintcdn.com/linkup-8b5c238e/eJ8cJjJOf3NSdL-t/pages/documentation/tutorials/peers-finder/assets/onopen-selection.png?fit=max&auto=format&n=eJ8cJjJOf3NSdL-t&q=85&s=74d886e11604c004dbc01d3e4c4f29d9" alt="OnOpen Selection" width="1999" height="897" data-path="pages/documentation/tutorials/peers-finder/assets/onopen-selection.png" />
*5: Selecting OnOpen*

## Using the Peer Finder

### Step 1: Enter Companies

1. Go to the "Input Companies" sheet
2. Enter up to 5 companies in cells A2-A6
3. Make sure to enter the full company names

### Step 2: Extract Characteristics

1. Click on the "Peer Finder" menu
2. Select "Extract Common Characteristics"
3. Wait for the process to complete
4. Review the extracted characteristics in the "Characteristics" sheet

### Step 3: Select Characteristics

1. In the "Characteristics" sheet, review the list of common characteristics
2. Use the checkboxes in column B to select which characteristics to use for finding peer companies
3. Select at least one characteristic

### Step 4: Find Peer Companies

1. Click on the "Peer Finder" menu again
2. Select "Find Peer Companies"
3. Wait for the process to complete
4. Review the list of peer companies in the "Peer Companies" sheet

### Step 5: Review and Refine

1. Review the list of peer companies
2. If needed, go back to Step 3 and adjust your characteristic selections
3. Run the peer finder again with different characteristics

<Info>
  For more detailed examples and use cases, check out our [Prompt Catalog](../../../documentation/tutorials/prompt-catalog).
</Info>

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


Built with [Mintlify](https://mintlify.com).