<p align="center">
<img src="https://i.imgur.com/S7DkZtr.png" width="100" alt="People Data Labs Logo">
</p>
<h1 align="center">People Data Labs Python Client</h1>

[![CircleCI](https://dl.circleci.com/status-badge/img/circleci/Ls7XJrnWCFSQjxziEASrFA/Yqcwawv7yod9ubfvX5G1v/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/circleci/Ls7XJrnWCFSQjxziEASrFA/Yqcwawv7yod9ubfvX5G1v/tree/main)

## Table of Contents

- [🔧 Installation](#installation)
- [🚀 Usage](#usage)
- [🌐 Endpoints](#endpoints)

## 🔧 Installation <a name="installation"></a>

1. Install from PyPi using [pip](https://pip.pypa.io/en/latest/), a package manager for Python.

    ```bash
    pip install peopledatalabs
    ```

2. Sign up for a [free PDL API key](https://www.peopledatalabs.com/signup).

## 🚀 Usage <a name="usage"></a>

First, create the PDLPY client:

```python
from peopledatalabs import PDLPY


# specify your API key
client = PDLPY(
    api_key="YOUR API KEY",
)

```

Then, send requests to any PDL API Endpoint.


## 🌐 Endpoints <a name="endpoints"></a>

**Person Endpoints**

| API Endpoint                                                                                    | PDLPY Function                      |
| ----------------------------------------------------------------------------------------------- | ----------------------------------- |
| [Person Enrichment API](https://docs.peopledatalabs.com/docs/enrichment-api)                    | `PDLPY.person.enrichment(**params)` |
| [Person Bulk Enrichment API](https://docs.peopledatalabs.com/docs/bulk-enrichment-api)          | `PDLPY.person.bulk(**params)`       |
| [Person Search API](https://docs.peopledatalabs.com/docs/search-api)                            | `PDLPY.person.search(**params)`     |
| [Person Retrieve API](https://docs.peopledatalabs.com/docs/person-retrieve-api)                 | `PDLPY.person.retrieve(**params)`   |
| [Person Identify API](https://docs.peopledatalabs.com/docs/identify-api)                        | `PDLPY.person.identify(**params)`   |

**Company Endpoints**

| API Endpoint                                                                                    | PDLPY Function                       |
| ----------------------------------------------------------------------------------------------- | ------------------------------------ |
| [Company Enrichment API](https://docs.peopledatalabs.com/docs/company-enrichment-api)           | `PDLPY.company.enrichment(**params)` |
| [Company Bulk Enrichment API](https://docs.peopledatalabs.com/docs/bulk-company-enrichment-api) | `PDLPY.company.bulk(**params)`       |
| [Company Search API](https://docs.peopledatalabs.com/docs/company-search-api)                   | `PDLPY.company.search(**params)`     |

**Supporting Endpoints**

| API Endpoint                                                                              | PDLJS Function                     |
| ----------------------------------------------------------------------------------------- | ---------------------------------- |
| [Autocomplete API](https://docs.peopledatalabs.com/docs/autocomplete-api)                 | `PDLPY.autocomplete(**params)`     |
| [Company Cleaner API](https://docs.peopledatalabs.com/docs/cleaner-apis#companyclean)     | `PDLPY.company.cleaner(**params)`  |
| [Location Cleaner API](https://docs.peopledatalabs.com/docs/cleaner-apis#locationclean)   | `PDLPY.location.cleaner(**params)` |
| [School Cleaner API](https://docs.peopledatalabs.com/docs/cleaner-apis#schoolclean)       | `PDLPY.school.cleaner(**params)`   |
| [Job Title Enrichment API](https://docs.peopledatalabs.com/docs/job-title-enrichment-api) | `PDLPY.job_title(**params)`        |
| [Skill Enrichment API](https://docs.peopledatalabs.com/docs/skill-enrichment-api)         | `PDLPY.skill(**params)`            |
| [IP Enrichment API](https://docs.peopledatalabs.com/docs/ip-enrichment-api)               | `PDLPY.ip(**params)`               |

