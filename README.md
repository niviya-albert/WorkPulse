# 💼 WorkPulse: Unemployment Trends & Economic Insights
> **CodeAlpha Data Science Internship — Task 2: Unemployment Analysis with Python**  
> **Author:** Niviya Albert | **Domain:** Data Science & Economic Analytics

---

## 📌 Project Overview
**WorkPulse** is an end-to-end data analytics and economic insights project that investigates the dynamics of India's labor market between **May 2019 and October 2020**. 

Using Python, Pandas, Matplotlib, Seaborn, and Streamlit, this project evaluates the pre-COVID baseline, quantifies the acute disruption during the nationwide COVID-19 lockdown (March–May 2020), contrasts Rural vs. Urban vulnerabilities, and assesses the velocity of subsequent economic recovery.

---

## 🚀 Key Features & Highlights
- **Safe & Rigorous Data Pipeline:** Automated cleaning, missing-value handling, datetime standardization, and type casting without arbitrary data removal.
- **Exploratory Data Analysis (EDA):** Time-series analysis, state and zonal rankings, rural-urban disparities, and multi-state heatmaps.
- **Dedicated COVID-19 Impact Study:** Quantifies the structural shift between pre-lockdown (9.51% avg), lockdown shock (peak 24.88% national avg), and reopening (11.90%).
- **Interactive Multi-Page Streamlit Dashboard:** Dynamic KPI metric cards, state and date filters, and Plotly visualizations.
- **Interview-Ready Economic Insights:** Clear demarcation of observed empirical facts, analytical interpretations, and targeted policy interventions.

---

## 📂 Project Architecture

```text
WorkPulse/
│
├── data/
│   ├── Unemployment in India.csv              # Raw primary dataset (Rural/Urban split)
│   ├── Unemployment_Rate_upto_11_2020.csv      # Raw regional dataset (Zonal & GPS coordinates)
│   ├── cleaned_unemployment_data.csv          # Cleaned primary dataset
│   └── cleaned_unemployment_regional.csv      # Cleaned regional dataset
│
├── notebooks/
│   └── unemployment_analysis.ipynb            # Master Jupyter Notebook with complete analysis
│
├── reports/
│   └── figures/                               # Publication-quality exported charts
│       ├── 1_national_trend_rural_vs_urban.png
│       ├── 2_state_highest_vs_lowest.png
│       ├── 3_state_monthly_heatmap.png
│       └── 4_zonal_recovery_trajectory.png
│
├── src/
│   ├── data_cleaning.py                       # Modular data cleaning & preprocessing script
│   ├── analysis.py                            # Statistical aggregation & visualization generator
│   └── create_notebook.py                     # Programmatic notebook generator
│
├── app.py                                     # Interactive Streamlit Web Application
├── requirements.txt                           # Python package dependencies
├── .gitignore                                 # Git ignore rules
└── README.md                                  # Comprehensive project documentation
```

---

## 📊 Summary of Findings & Key Insights

### 1. Pre-COVID Baseline vs. Lockdown Shock
- **Pre-COVID (May 2019 – Feb 2020):** National unemployment remained stable between **8.87% and 9.96%** (mean: **9.51%**), with Labour Participation averaging **43.89%**.
- **Lockdown Shock (March – May 2020):** National unemployment surged to **23.64% in April** and peaked at **24.88% in May 2020** (an increase of >150%). Labour participation fell by **4.96 percentage points** as active job seeking was severely constrained.
- **Immediate Rebound (June 2020):** Rebounded quickly to **11.90%** as unlock phases commenced, reflecting the return of daily wage and informal labor.

### 2. Rural vs. Urban Divide
- Urban areas consistently showed higher baseline unemployment (10.55% vs 7.07% in May 2019).
- During the May 2020 lockdown peak, the gap expanded to **+7.19%** (Urban **28.40%** vs Rural **21.21%**), because urban manufacturing and service jobs required physical presence, while rural agricultural operations continued.

### 3. State-Level Performance
- **Chronically High Unemployment States:** Tripura (28.35% avg), Haryana (26.28% avg), Jharkhand (20.59% avg), and Bihar (18.92% avg).
- **Most Resilient States:** Meghalaya (4.80% avg), Odisha (5.66% avg), Assam (6.43% avg), Uttarakhand (6.58% avg), and Gujarat (6.66% avg).
- **Highest Lockdown Spikes:** Puducherry (peaked at **76.74%**), Jharkhand (**70.17%**), Bihar (**58.77%**), and Tamil Nadu (**53.19%**).

---

## 🏛️ Policy & Strategic Recommendations
1. **Urban Employment Guarantee:** Implement an urban equivalent to MGNREGA to protect informal urban daily wage earners during regional lockdowns or economic slowdowns.
2. **Targeted Regional Interventions:** Provide dedicated industrial incentives and skilling ecosystems for states like Haryana, Jharkhand, and Bihar facing structural employment deficits.
3. **High-Frequency Real-Time Monitoring:** Establish monthly labor tracking dashboards for swift, data-driven fiscal responses.

---

## 💻 How to Run the Project Locally

### 1. Clone or Open the Workspace
```bash
git clone https://github.com/your-username/WorkPulse.git
cd WorkPulse
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Data Cleaning & Visualization Pipeline
```bash
python src/data_cleaning.py
python src/analysis.py
```

### 4. Launch Interactive Streamlit Dashboard
```bash
streamlit run app.py
```

---

## 🛠️ Tech Stack
- **Language:** Python 3.11+
- **Data Manipulation:** Pandas, NumPy
- **Visual Analytics:** Matplotlib, Seaborn, Plotly Express
- **Interactive Web App:** Streamlit
- **Environment:** Jupyter Notebook / Antigravity IDE

---

## 📜 License & Acknowledgments
Developed as part of the **CodeAlpha Data Science Internship**. Data sourced from the Centre for Monitoring Indian Economy (CMIE) via Kaggle.
