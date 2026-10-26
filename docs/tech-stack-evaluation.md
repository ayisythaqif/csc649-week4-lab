# Tech Stack Evaluation

## 1. Project Information

**Project Name:** Web-Based AI Phishing URL and Scam Phone Number Detection System

**Purpose:** To help Malaysian internet users assess suspicious URLs using machine learning and check phone numbers against available scam-report information.

## 2. Project Requirements

The following requirements are based on the project's functional and non-functional requirements.

| ID | Requirement | Type |
|---|---|---|
| FR1 | The system shall allow users to submit a URL for analysis. | Functional |
| FR3 | The system shall classify a submitted URL into the risk categories supported by the model. | Functional |
| FR5 | The system shall allow users to submit a phone number to check available scam-report data. | Functional |
| NFR1 | The system should assess URLs within 3 seconds for at least 95% of requests under the defined test environment and workload. | Non-functional |
| NFR2 | The system shall validate submitted URLs and shall not automatically navigate to or execute them during analysis. | Non-functional |

## 3. Technology Stack Options

### Option A: Static Website Using GitHub Pages

- Frontend: HTML, CSS and JavaScript
- Hosting: GitHub Pages
- Backend: None
- Database: None

**Advantages:** Free hosting for eligible repositories, simple deployment and easy maintenance.

**Disadvantages:** GitHub Pages supports static websites rather than a Python server-side application. A separate backend would be required to run the machine learning model and perform database queries.

### Option B: Python Web Application with SQLite

- Frontend: HTML, CSS and JavaScript
- Backend: Python Flask
- Machine learning: Scikit-learn
- Database: SQLite
- Hosting: A paid cloud web host or a suitable self-managed server

**Advantages:** Flask integrates with Python machine learning libraries, while SQLite is simple to configure and suitable for a small prototype.

**Disadvantages:** SQLite is less suitable for concurrent database access than a server database. A deployed application also needs appropriate persistent storage and backup arrangements.

### Option C: Python Web Application with Supabase PostgreSQL

- Frontend: HTML, CSS and JavaScript
- Backend: Python Flask
- Machine learning: Scikit-learn
- Database: Supabase PostgreSQL
- Hosting: Render free web service for the prototype

**Advantages:** Supports server-side machine learning, persistent relational data storage, URL analysis and phone-number lookups. It also provides a possible path for expanding the system.

**Disadvantages:** Requires more configuration than a static website. Free hosting has limitations, including service sleep periods, and a separate database service adds configuration and security responsibilities.

## 4. Weighted Decision Matrix

### Scoring Scale

**Weight:**
- 1 = Least important
- 5 = Most important

**Score:**
- 1 = Very poor
- 2 = Poor
- 3 = Average
- 4 = Good
- 5 = Excellent

The weighted score is calculated using:

**Weighted Score = Weight × Option Score**

| Criterion | Weight | Option A Score | Option A Weighted | Option B Score | Option B Weighted | Option C Score | Option C Weighted |
|---|---:|---:|---:|---:|---:|---:|---:|
| Time to build | 5 | 5 | 25 | 4 | 20 | 3 | 15 |
| Machine learning compatibility | 5 | 1 | 5 | 5 | 25 | 5 | 25 |
| Database support | 4 | 1 | 4 | 3 | 12 | 5 | 20 |
| Security and control | 4 | 2 | 8 | 4 | 16 | 4 | 16 |
| Cost | 5 | 5 | 25 | 2 | 10 | 4 | 20 |
| Deployment and maintenance | 3 | 5 | 15 | 4 | 12 | 3 | 9 |
| **TOTAL** | **26** | | **82** | | **95** | | **105** |

### Result

1. Option A: 82
2. Option B: 95
3. Option C: 105

**Winning option: Option C — Python Flask, Scikit-learn, Supabase PostgreSQL and Render.**

## 5. Decision Record

### Context

The proposed system needs to analyse suspicious URLs using machine learning and check phone numbers against available scam-report information. Therefore, the technology stack must support Python-based model integration, database access, reasonable development time and security controls.

### Decision

I chose Option C: a Python Flask web application using Scikit-learn for URL classification, Supabase PostgreSQL for scam-report data, and Render for hosting the prototype.

### Reasons

Option C achieved the highest weighted score of 105. Flask and Scikit-learn support the machine learning functionality required by FR1 and FR3. Supabase PostgreSQL provides relational database storage to support FR5. Server-side URL validation also supports NFR2 by allowing submitted URLs to be inspected without automatically opening them.

The services have free tiers suitable for prototyping, subject to their current limits. However, the performance requirement in NFR1 must be tested rather than assumed. Free hosting may introduce delays after periods of inactivity.

### Consequences and Trade-offs

The selected stack supports both URL classification and phone-number lookup in one web application. PostgreSQL also provides a more suitable foundation for structured scam-report records than a static website without a database.

However, Option C requires additional setup for hosting, database connections, environment variables and deployment. Render's free web service may sleep after inactivity, so the application may not respond within three seconds on every request. Meeting NFR1 may require a different hosting plan or deployment arrangement.

### Risks

The system may produce incorrect classifications if the training dataset is incomplete or does not represent new phishing techniques. Phone numbers without existing scam reports may also produce inconclusive results.

The decision would change if the project had a larger budget, a strict requirement for consistently low response times, or substantially more users. In that situation, I would evaluate a paid hosting plan and additional deployment resources. If the project only needed to demonstrate a static interface, Option A would be sufficient.

## 6. Current Free-Plan Considerations

The following limitations were checked on 27 October 2026:

- **GitHub Pages:** Suitable for static HTML, CSS and JavaScript websites, but it does not support server-side Python applications.
- **Render:** Free web services sleep after 15 minutes without incoming traffic and can take about a minute to start again. The free service's local filesystem is also ephemeral.
- **Supabase:** Its free plan includes a 500 MB database quota and projects may be paused after one week of inactivity.

These limitations make the selected stack suitable for a student prototype, but they must be considered when testing performance and planning deployment.

## 7. Conclusion

Option C is the best fit for the proposed prototype because it supports machine learning, relational database queries and web application deployment. Although it requires more configuration than a static website, it meets more of the project's functional needs. Performance, security and dataset quality must still be evaluated through testing.