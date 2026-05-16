SaaS Customer Retention & Attrition Analytics (RavenStack)
📌 Project Overview

This project focuses on identifying critical churn patterns, lifecycle drop-off trends, and product friction points for **RavenStack**, a B2B SaaS platform. Utilizing multi-table relational subscription data, this analysis diagnoses structural retention issues across 500 corporate accounts and provides data-driven, actionable recommendations to protect recurring revenue streams.

This dashboard and report are structured to simulate a formal presentation deliverable for a Product Manager, Startup Founder, or Business Stakeholder.

## 📈 Executive Summary & Core KPIs
An evaluation of RavenStack's customer portfolio reveals notable structural retention challenges. While early-stage subscription metrics show steady acquisition paths, a deep dive into historical cohorts indicates a recurring breaking point short of long-term contract maturity.

* **Total Portfolio Evaluated:** 500 Corporate Accounts
* **Gross Portfolio Account Churn:** 110 Accounts
* **Global Platform Churn Rate:** 22.00%
* **Global Portfolio Retention Rate:** 78.00%
* **Average Customer Lifespan Before Attrition:** 5.7 Months

🛠️ Tech Stack & Methodology
* **Language:** Python 3.13
* **Data Manipulation:** `pandas`, `numpy` (Table joins, automated data cleaning, handling null structures)
* **Visualization:** `matplotlib`, `seaborn` (Statistical plotting and customer voice distributions)
* **Executive Spreadsheet Automation:** `openpyxl` (Dynamic generation of stylized corporate KPI dashboards)
* **Reporting Environment:** Visual Studio Code

🔍 Core Diagnostic Findings & Insights

### 1. Attrition by Subscription Tier (The Pricing Paradox)
Segmenting customer attrition by subscription tier shows that pricing structures and tier feature gating are **not** pushing customers away. Churn remains uniform across the entire portfolio:
* **Basic Tier Churn Rate:** 22.02%
* **Pro Tier Churn Rate:** 21.91%
* **Enterprise Tier Churn Rate:** 22.08%

Strategic Takeaway:** Because high-budget Enterprise accounts cancel at the exact same rate as entry-level Basic tiers, the root cause of churn is tied to core product workflow issues rather than contract pricing boundaries.

### 2. Churn Concentrations Across Industry Verticals
Analyzing churn by vertical business sectors exposes a massive market alignment issue:
* 🚨 **DevTools Sector:** **30.97% Churn Rate** *(Critical High Risk)*
* ⚖️ **FinTech Sector:** 22.32% Churn Rate
* ⚖️ **HealthTech Sector:** 21.88% Churn Rate
* 🎓 **EdTech Sector:** 16.46% Churn Rate
* 🛡️ **Cybersecurity Sector:** 16.00% Churn Rate *(Best Retention)*

**Strategic Takeaway:** RavenStack is facing a major retention crisis within the developer ecosystem. Nearly 1 in 3 developer-focused companies cancel their subscriptions.

###
