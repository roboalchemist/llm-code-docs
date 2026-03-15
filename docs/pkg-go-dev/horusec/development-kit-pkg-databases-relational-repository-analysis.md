### Overview ¶

nolint

    
### Index ¶

- 
          type IAnalysisRepository

- 

  - 
            func NewAnalysisRepository(databaseRead SQL.InterfaceRead, databaseWrite SQL.InterfaceWrite) IAnalysisRepository

- 
          type Mock

- 

  - 
            func (m *Mock) Create(_ *horusec.Analysis, _ SQL.InterfaceWrite) error

  - 
            func (m *Mock) GetByID(_ uuid.UUID) (*horusec.Analysis, error)

  - 
            func (m *Mock) GetDetailsCount(_, _ uuid.UUID, _, _ time.Time) (int, error)

  - 
            func (m *Mock) GetDetailsPaginated(_, _ uuid.UUID, _, _ int, _, _ time.Time) ([]dashboard.VulnDetails, error)

  - 
            func (m *Mock) GetDeveloperCount(_, _ uuid.UUID, _, _ time.Time) (count int, err error)

  - 
            func (m *Mock) GetRepositoryCount(_, _ uuid.UUID, _, _ time.Time) (count int, err error)

  - 
            func (m *Mock) GetVulnByDeveloper(_, _ uuid.UUID, _, _ time.Time) ([]dashboard.VulnByDeveloper, error)

  - 
            func (m *Mock) GetVulnByLanguage(_, _ uuid.UUID, _, _ time.Time) ([]dashboard.VulnByLanguage, error)

  - 
            func (m *Mock) GetVulnByRepository(_, _ uuid.UUID, _, _ time.Time) ([]dashboard.VulnByRepository, error)

  - 
            func (m *Mock) GetVulnBySeverity(_, _ uuid.UUID, _, _ time.Time) ([]dashboard.VulnBySeverity, error)

  - 
            func (m *Mock) GetVulnByTime(_, _ uuid.UUID, _, _ time.Time) ([]dashboard.VulnByTime, error)

- 
          type Repository

- 

  - 
            func (ar *Repository) Create(analysis *horusec.Analysis, tx SQL.InterfaceWrite) error

  - 
            func (ar *Repository) GetByID(analysisID uuid.UUID) (*horusec.Analysis, error)

  - 
            func (ar *Repository) GetDetailsCount(companyID, repositoryID uuid.UUID, initialDate, finalDate time.Time) (int, error)

  - 
            func (ar *Repository) GetDetailsPaginated(companyID, repositoryID uuid.UUID, page, size int, ...) (vulnDetails []dashboard.VulnDetails, err error)

  - 
            func (ar *Repository) GetDeveloperCount(companyID, repositoryID uuid.UUID, initialDate, finalDate time.Time) (int, error)

  - 
            func (ar *Repository) GetRepositoryCount(companyID, repositoryID uuid.UUID, initialDate, finalDate time.Time) (int, error)

  - 
            func (ar *Repository) GetVulnByDeveloper(companyID, repositoryID uuid.UUID, initialDate, finalDate time.Time) (vulnByDeveloper []dashboard.VulnByDeveloper, err error)

  - 
            func (ar *Repository) GetVulnByLanguage(companyID, repositoryID uuid.UUID, initialDate, finalDate time.Time) (vulnByLanguage []dashboard.VulnByLanguage, err error)

  - 
            func (ar *Repository) GetVulnByRepository(companyID, repositoryID uuid.UUID, initialDate, finalDate time.Time) (vulnByRepository []dashboard.VulnByRepository, err error)

  - 
            func (ar *Repository) GetVulnBySeverity(companyID, repositoryID uuid.UUID, initialDate, finalDate time.Time) (vulnBySeverity []dashboard.VulnBySeverity, err error)

  - 
            func (ar *Repository) GetVulnByTime(companyID, repositoryID uuid.UUID, initialDate, finalDate time.Time) (vulnByTime []dashboard.VulnByTime, err error)

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type IAnalysisRepository ¶
  
    
  

    
    
      

```
type IAnalysisRepository interface {
	Create(analysis *horusec.Analysis, tx SQL.InterfaceWrite) error
	GetByID(analysisID uuid.UUID) (*horusec.Analysis, error)
	GetDetailsPaginated(companyID, repositoryID uuid.UUID, page, size int, initialDate,
		finalDate time.Time) (vulnDetails []dashboard.VulnDetails, err error)
	GetDetailsCount(companyID, repositoryID uuid.UUID, initialDate,
		finalDate time.Time) (count int, err error)
	GetDeveloperCount(companyID, repositoryID uuid.UUID, initialDate,
		finalDate time.Time) (count int, err error)
	GetRepositoryCount(companyID, repositoryID uuid.UUID, initialDate,
		finalDate time.Time) (count int, err error)
	GetVulnBySeverity(companyID, repositoryID uuid.UUID, initialDate,
		finalDate time.Time) (vulnBySeverity []dashboard.VulnBySeverity, err error)
	GetVulnByDeveloper(companyID, repositoryID uuid.UUID, initialDate,
		finalDate time.Time) (vulnByDeveloper []dashboard.VulnByDeveloper, err error)
	GetVulnByLanguage(companyID, repositoryID uuid.UUID, initialDate,
		finalDate time.Time) (vulnByLanguage []dashboard.VulnByLanguage, err error)
	GetVulnByRepository(companyID, repositoryID uuid.UUID, initialDate,
		finalDate time.Time) (vulnByRepository []dashboard.VulnByRepository, err error)
	GetVulnByTime(companyID, repositoryID uuid.UUID, initialDate,
		finalDate time.Time) (vulnByTime []dashboard.VulnByTime, err error)
}
```

    
  

    
  
  
    
#### 
      func NewAnalysisRepository ¶
  
    
  

    
    
      

```
func NewAnalysisRepository(databaseRead SQL.InterfaceRead, databaseWrite SQL.InterfaceWrite) IAnalysisRepository
```