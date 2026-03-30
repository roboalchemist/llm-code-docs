# Source: https://glow-docs.xrpl-commons.org/technical-resources/application-workflow.md

# Application Workflow

The Glow platform implements a structured workflow for retroactive funding of contributions to the XRPL ecosystem. This document provides a technical overview of the process from nomination to disbursement.

## Cohort Creation

A cohort represents a time-bounded collection of nominations processed together.

### Technical Implementation

Cohorts are managed through the `Cohort` model with key fields:

* `name`: Cohort identifier (e.g., "Cohort 1")
* `startDate`: When the cohort begins accepting nominations
* `endDate`: When the cohort closes (null for active cohorts)
* `status`: Current state of the cohort

Only one cohort can be active at a time. When a Scout creates a nomination, it is automatically associated with the currently active cohort (where `endDate` is null and `startDate` is in the past).

The admin interface allows administrators to:

* Create new cohorts
* Set start dates
* Close cohorts by setting end dates
* View all nominations within a cohort

## Nomination Process

### Step 1: Scout Authentication

Scouts authenticate using their credentials through the authentication module. Role-based access control ensures only Scouts can create nominations.

### Step 2: Project and Contributor Selection

#### Nomination Workflow

1. **Scout Authentication**
   * Scout logs in to the Glow platform
   * System verifies scout role permissions
2. **Project Management**
   * Scout searches for existing projects
   * **If project exists:**
     * Scout selects the existing project
   * **If project doesn't exist:**
     * Scout creates a new project with required details:
       * Project name
       * Description
       * GitHub repository
       * X handle
       * Website URL
3. **Contributor Management**
   * Scout searches for the contributor
   * **If contributor exists:**
     * Scout selects the existing contributor
   * **If contributor doesn't exist:**
     * Scout creates a new contributor record with:
       * First and last name
       * Email address
       * GitHub username
       * X handle
       * Role (creator, maintainer, contributor, editor)
       * Active dates
       * Status
4. **Nomination Creation**
   * Scout provides contribution details:
     * Description of contribution
     * Date of contribution
   * System creates nomination linking:
     * Selected contributor
     * Selected project(s)
     * Current cohort
     * Scout information

#### Workflow Diagram

```
Scout Login
    │
    ▼
Search Projects
    │
    ├─────────────┐
    │             │
    ▼             ▼
Project Exists?   Project Doesn't Exist
    │             │
    │             ▼
    │         Create Project
    │             │
    │             │
    ▼             │
Select Project    │
    │             │
    └──────┬──────┘
           │
           ▼
Search Contributors
           │
           ├─────────────┐
           │             │
           ▼             ▼
Contributor Exists?  Contributor Missing
           │             │
           │             ▼
           │      Create Contributor
           │             │
           ▼             │
   Select Contributor    │
           │             │
           └──────┬──────┘
                  │
                  ▼
          Create Nomination
```

> Note: The diagram above is a simplified representation of the workflow. In actual implementation, the system uses API endpoints for these operations.

The platform provides search functionality with API endpoints:

* `/api/projects/search` - Find existing projects
* `/api/contributors/search` - Find existing contributors

When creating new records:

* New projects are added through `/api/projects`
* New contributors are added through `/api/contributors`

### Step 3: Nomination Details

When submitting a nomination, the scout provides:

* Contribution description
* Contribution date
* Project category

The system automatically records:

* Cohort ID (active cohort)
* Nominator ID (scout)
* Timestamp

### Technical Implementation

Nominations are stored in the `Nomination` model with relationships to:

* `contributorId`: Reference to the Contributor being nominated
* `projectsIds`: References to Projects involved
* `cohortId`: Reference to the current Cohort
* `nominatorId`: Reference to the Scout making the nomination

## Voting Process

### Step 1: Wallet Connection

Voters authenticate by connecting their XRPL wallet. This integration occurs through:

1. Wallet provider selection (Xaman, GemWallet, Crossmark, etc.)
2. Connection via the corresponding wallet provider API
3. Address verification

### Step 2: Wallet Verification

To prevent spam, voters must prove wallet ownership by signing a small transaction (1 drop) to a designated verification address. This registration is stored in the `Voter` model.

### Step 3: Casting Votes

Voters browse nominations through public pages and can cast three types of votes:

* Yay (+1)
* Nay (-1)
* Null (0)

The voting system enforces one vote per nomination per wallet.

### Technical Implementation

Votes are stored in the `Vote` model with:

* `voterId`: Reference to the Voter
* `nominationId`: Reference to the Nomination
* `vote`: The vote value
* `timestamp`: When the vote was cast

API endpoints for voting:

* `GET /api/nominations/list` - View nominations
* `POST /api/votes` - Cast votes
* `PUT /api/votes/:id` - Update votes

## Judging Process

### Step 1: Judge Review

Judges review nominations with access to:

* Contribution details
* Project information
* Contributor information
* Community voting metrics

### Step 2: Assessment Creation

Judges evaluate nominations against eligibility and quality criteria:

1. Is the contributor over 18?
2. Has the nominee contributed to core infrastructure?
3. Is the contribution recent work (within 6 months)?
4. Is it unpaid work?

### Step 3: Reward Size Assignment

Based on their assessment, judges assign a shirt size:

* Decline (0)
* Small (1)
* Medium (2)
* Large (3)

Multiple judges assess each nomination, typically a minimum of three.

### Step 4: Final Approval

Once all nominations in a cohort have been assessed, judges conduct a final review and approve the distribution.

### Technical Implementation

Judge assessments are stored in the `JudgeAssessment` model:

* `nominationId`: Reference to the Nomination
* `userId`: Reference to the Judge
* `status`: 'approved' or 'declined'
* `criteria`: Object containing evaluation criteria results
* `comment`: Optional judge feedback
* `rejectionReason`: Required if status is 'declined'

Key judge-related API endpoints:

* `GET /api/nominations/metrics` - View nomination metrics
* `POST /api/judgeAssessments` - Create assessments
* `PUT /api/judgeAssessments/:id` - Update assessments
* `POST /api/nominations/actions/approve` - Approve final distributions

## Contributor Application Process

### Step 1: Notification

Contributors receive email notifications about their nominations.

### Step 2: Account Creation

If contributors don't have an account, the system facilitates account creation with the 'contributor' role.

### Step 3: Eligibility Verification

Contributors must complete an eligibility questionnaire covering:

* Age verification (18+)
* Sanctioned region check
* Affiliation checks (e.g., not a Ripple employee)
* Conflict of interest checks (not a scout or judge)

### Step 4: Terms Acceptance

Contributors must accept:

* Terms of Service
* Code of Conduct

### Step 5: Wallet Registration

Contributors register their XRPL wallet to receive funds.

### Step 6: Application Submission

Contributors complete their application with additional project details:

* Previous XRPL grants or accelerator participation
* Website, GitHub, and social media links
* Additional project information

### Step 7: KYC Verification

Contributors may need to complete KYC verification through the integrated verification service.

### Technical Implementation

The contributor journey is managed through:

* `Contributor` model with verification fields
* `KycVerification` model for KYC status
* API endpoints for:
  * Getting contributor status
  * Updating eligibility
  * Accepting terms
  * Registering wallet
  * Submitting application details

## Disbursement Process

### Step 1: Verification Check

The system verifies all requirements are met:

* Nomination approved by judges
* Contributor completed application
* KYC verification (if required)
* Valid XRPL wallet connected

### Step 2: Payment Processing

Payments are processed through XRPL transactions to the contributor's registered wallet.

### Step 3: Transaction Recording

All disbursements are recorded for transparency and audit purposes.

## Integration Points

The workflow integrates with several external systems:

### Email Service

* Used for notifications to contributors
* Account verification
* Status updates

### XRPL Network

* Wallet connectivity
* Transaction signing
* Payment disbursements

### KYC Provider

* Identity verification
* Compliance checks

## Security Measures

The workflow includes multiple security controls:

* Role-based access control
* Wallet signature verification
* Multi-judge approval requirements
* KYC verification
* Transaction validation
