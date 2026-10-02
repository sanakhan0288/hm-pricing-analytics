# 🛍️ H&M Pricing Analytics

<p align="center">
  <h3 align="center">From Fashion Data → Pricing Intelligence</h3>
</p>

<p align="center">
  <em>
    An end-to-end analytics project exploring how price, discounts, and demand interact in fashion retail.
  </em>
</p>

<p align="center">
  <a href="https://github.com/sanakhan0288/hm-pricing-analytics/tree/main/notebooks">
    <img src="https://img.shields.io/badge/📓%20Notebooks-Explore-8B5CF6?style=for-the-badge" alt="Notebooks">
  </a>
  <a href="https://github.com/sanakhan0288/hm-pricing-analytics/tree/main/outputs">
    <img src="https://img.shields.io/badge/📊%20Outputs-Explore-06B6D4?style=for-the-badge" alt="Outputs">
  </a>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Project-Analytics-F97316?style=for-the-badge" alt="Analytics">
</p>

<p align="center">
  <a href="#-the-big-question">The Question</a> •
  <a href="#-the-analytics-journey">Journey</a> •
  <a href="#-what-this-project-explores">Analysis</a> •
  <a href="#-tech-stack">Tech Stack</a> •
  <a href="#-run-the-project">Run</a>
</p>

---

## 💭 The Big Question

> ### **What happens to demand when the price of a fashion product changes?**

Fashion pricing is a balancing act.

A lower price might attract more customers — but how much more demand does it actually create?

A higher discount might increase transactions — but does the additional demand justify the reduction in price?

This project uses **H&M transaction data** to investigate these questions through:

**📊 Exploratory Analysis**  
**📉 Price Elasticity**  
**🏷️ Discount Sensitivity**  
**📐 Statistical Modeling**  
**🔮 Pricing Scenarios**  
**💡 Business Recommendations**

---

# 🎯 What This Project Is About

This isn't just a project about calculating average prices.

It's about moving through the complete analytical journey:

```text
                RAW TRANSACTION DATA
                         │
                         ▼
                🔎 UNDERSTAND
                         │
                         ▼
                🧹 PREPARE
                         │
                         ▼
                📊 EXPLORE
                         │
                         ▼
                💰 ANALYZE PRICE
                         │
                         ▼
                📉 ESTIMATE ELASTICITY
                         │
                         ▼
                🧠 MODEL & CONTROL
                         │
                         ▼
                🔮 TEST SCENARIOS
                         │
                         ▼
                💡 RECOMMEND
                         │
                         ▼
                📈 SUPPORT DECISIONS
```

---

# 🧩 The Business Questions

<details>
<summary><strong>💰 Pricing</strong></summary>

<br>

- How does demand change as price changes?
- How sensitive are customers to price?
- Do different products behave differently?
- Are there meaningful pricing patterns across the data?

</details>

<details>
<summary><strong>🏷️ Discounts</strong></summary>

<br>

- How does discount depth relate to demand?
- Does a deeper discount always correspond to stronger demand?
- Where might additional discounting deserve further investigation?

</details>

<details>
<summary><strong>📉 Elasticity</strong></summary>

<br>

- How responsive is demand to price changes?
- What does estimated elasticity tell us?
- Does the relationship remain after controlling for other factors?

</details>

<details>
<summary><strong>🔮 Pricing Scenarios</strong></summary>

<br>

- What could happen if price changes?
- How can elasticity estimates be translated into scenarios?
- How can scenarios support pricing decisions?

</details>

---

# 🚀 The Analytics Journey

The project is built in **9 phases**, with each phase answering a different part of the business problem.

| Phase | What happens |
|:---:|---|
| **01** | 🔎 Data Understanding |
| **02** | 🧹 Data Preparation |
| **03** | 📊 Exploratory Analysis |
| **04** | 💰 Pricing Analysis |
| **05** | 📉 Elasticity Ladder |
| **06** | 🧠 Fixed-Effects Modeling |
| **07** | 🔮 Pricing Scenarios |
| **08** | 💡 Recommendations |
| **09** | 📈 Dashboard |

### The idea

```text
Don't just ask...

"What happened?"

          ↓

Ask...

"What relationship exists?"

          ↓

Then...

"How strong is it?"

          ↓

And finally...

"How could a business use this information?"
```

---

# 📉 Price Elasticity

One of the core concepts in this project is **price elasticity of demand**.

### The idea

Price elasticity measures how much demand changes when price changes.

```text
                % Change in Demand
Elasticity  =  ────────────────────
                % Change in Price
```

For example:

```text
Price ↑ 10%
      ↓
Demand ↓ 20%

Elasticity ≈ -2
```

The purpose of the analysis is not simply to calculate a number.

It is to understand **what that number means for pricing decisions.**

---

# 🏷️ Discount Sensitivity

Discounts are everywhere in fashion retail.

But:

> **A bigger discount does not automatically mean a better business outcome.**

This project investigates the relationship between:

```text
DISCOUNT
   ↓
PRICE CHANGE
   ↓
CUSTOMER RESPONSE
   ↓
DEMAND
```

The analysis helps frame questions around whether additional discounting is associated with meaningful incremental demand.

---

# 🧠 From Correlation to Modeling

A simple chart can show that price and demand move together.

But that isn't necessarily enough.

Products can differ in many ways.

So the project progresses toward statistical modeling and **fixed effects** to account for persistent differences within the data.

```text
Simple Relationship
        ↓
Log Transformation
        ↓
Elasticity Model
        ↓
Controlled Analysis
        ↓
Fixed Effects
        ↓
Scenario Analysis
```

This creates a more structured path from:

**Observation → Measurement → Modeling → Interpretation**

---

# 🔮 Pricing Scenarios

Once an estimated relationship has been established, it can be translated into hypothetical scenarios.

```text
                 CURRENT PRICE
                       │
          ┌────────────┼────────────┐
          ↓            ↓            ↓
        -10%          -5%          +5%
          │            │            │
          └────────────┼────────────┘
                       ↓
                ESTIMATED RESPONSE
```

These scenarios are **not predictions or guarantees**.

They are analytical tools for asking:

> *"If the price changed, what would the model suggest might happen to demand?"*

---

# 💡 From Analysis → Business Thinking

The final objective is to turn statistical output into something a business user can understand.

The project therefore considers questions such as:

### 🔹 Where is demand more price-sensitive?

Potentially useful when evaluating price increases.

### 🔹 Where might discounting deserve closer investigation?

Useful when considering promotional depth.

### 🔹 Where could pricing experiments be useful?

Potentially useful for testing hypotheses rather than relying entirely on historical observations.

### 🔹 What else matters?

```text
Price
  +
Demand
  +
Margin
  +
Inventory
  +
Competition
  +
Seasonality
       ↓
PRICING DECISION
```

---

# 📊 Project Outputs

The repository contains analytical notebooks and generated outputs.

### 📓 Notebooks

Step through the analysis from data preparation to modeling and recommendations.

👉 **[Explore the notebooks →](https://github.com/sanakhan0288/hm-pricing-analytics/tree/main/notebooks)**

### 📈 Outputs

Explore generated analytical outputs and visualizations.

👉 **[Explore the outputs →](https://github.com/sanakhan0288/hm-pricing-analytics/tree/main/outputs)**

---

# 🗂️ Repository Structure

```text
hm-pricing-analytics/
│
├── 📁 notebooks/
│   ├── Phase 01 — Data Understanding
│   ├── Phase 02 — Data Preparation
│   ├── Phase 03 — Exploratory Analysis
│   ├── Phase 04 — Pricing Analysis
│   ├── Phase 05 — Elasticity
│   ├── Phase 06 — Fixed Effects
│   ├── Phase 07 — Scenarios
│   ├── Phase 08 — Recommendations
│   └── Phase 09 — Dashboard
│
├── 📁 outputs/
│   └── Analysis outputs & visualizations
│
├── 📄 requirements-analysis.txt
├── 📄 .gitignore
└── 📄 README.md
```

---

# 🛠️ Tech Stack

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white">
<img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white">
<img src="https://img.shields.io/badge/Matplotlib-11557C?style=flat-square">
<img src="https://img.shields.io/badge/Seaborn-4C72B0?style=flat-square">
<img src="https://img.shields.io/badge/SciPy-8CAAE6?style=flat-square">
<img src="https://img.shields.io/badge/Statsmodels-3A6EA5?style=flat-square">
<img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white">
<img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white">

</p>

| Tool | Used for |
|---|---|
| 🐍 **Python** | Core analysis |
| 🐼 **Pandas** | Data manipulation |
| 🔢 **NumPy** | Numerical computation |
| 📊 **Matplotlib** | Visualization |
| 🎨 **Seaborn** | Statistical visualization |
| 📐 **Statsmodels** | Statistical modeling |
| 🧮 **SciPy** | Statistical computation |
| 🤖 **Scikit-learn** | Analytical workflows |
| 📓 **Jupyter** | Interactive notebooks |
| 🔧 **Git/GitHub** | Version control |

---

# 🚀 Run the Project

### 1. Clone

```bash
git clone https://github.com/sanakhan0288/hm-pricing-analytics.git
cd hm-pricing-analytics
```

### 2. Create a virtual environment

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements-analysis.txt
```

### 4. Launch Jupyter

```bash
jupyter notebook
```

Then open the notebooks in:

```text
notebooks/
```

---

# ⚠️ A Note on Interpretation

This project works with **observational transaction data**.

An observed relationship between price and demand does not automatically establish causation.

Purchasing behavior can also be influenced by:

- promotions
- seasonality
- inventory
- product popularity
- product lifecycle
- customer behavior
- other external factors

Therefore:

> **Elasticity estimates and pricing scenarios should be treated as analytical estimates, not guaranteed business outcomes.**

---

# 🔭 What's Next?

The project can evolve into a more complete **Fashion Pricing Intelligence System**.

```text
CURRENT
  │
  ├── Price Elasticity
  ├── Discount Sensitivity
  ├── Fixed Effects
  └── Pricing Scenarios
  │
  ▼
NEXT
  │
  ├── Competitor Pricing
  ├── Inventory
  ├── Product Margins
  ├── Demand Forecasting
  ├── Product-Level Elasticity
  └── Automated Pricing Recommendations
```

### Future ideas

- [ ] Competitor price integration
- [ ] Inventory-aware pricing
- [ ] Margin-aware scenarios
- [ ] Product-level elasticity
- [ ] Demand forecasting
- [ ] Interactive dashboard deployment
- [ ] Automated pricing recommendations
- [ ] Experimental validation

---

# 🎓 Skills Demonstrated

### 📊 Analytics

`EDA` · `Data Cleaning` · `Feature Engineering` · `Visualization`

### 📐 Statistics

`Elasticity` · `Regression` · `Fixed Effects` · `Scenario Analysis`

### 💼 Business

`Pricing` · `Discount Strategy` · `Demand Analysis` · `Recommendations`

### 🐍 Tools

`Python` · `Pandas` · `NumPy` · `Statsmodels` · `Jupyter` · `Git`

---

# 👩‍💻 About

### Sana Khan

Aspiring Data Analyst focused on building practical, business-oriented analytics projects.

**Interested in:**

`Retail Analytics` · `Fashion Analytics` · `Pricing` · `Customer Behavior` · `Business Intelligence`

<br>

<a href="https://github.com/sanakhan0288">
  <img src="https://img.shields.io/badge/Follow%20me%20on-GitHub-181717?style=for-the-badge&logo=github" alt="GitHub">
</a>

---

<p align="center">

### 🛍️ H&M Pricing Analytics

<strong>Data → Elasticity → Scenarios → Recommendations</strong>

<br><br>

<i>Turning fashion transaction data into questions worth asking.</i>

<br><br>

⭐ <strong>If you found the project interesting, consider starring the repository.</strong>

</p>
