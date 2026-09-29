# HR Analytics Dashboard (anova)

An interactive employee-attrition dashboard built with Shiny for Python on the HR Analytics dataset (1,480 employees).

**Live demo:** https://anova-web-gamma.vercel.app

## Features
- KPI cards: Total Employees, Attrition, Attrition Rate, Average Age, Average Salary, Average Years at Company
- Department multi-select filter
- Six charts: attrition by Education level, age distribution by attrition, attrition by Gender, Monthly Income vs attrition (box plot), Years at Company vs attrition (box plot), attrition by Job Role

## Tech stack
- **App:** Python, Shiny for Python, pandas, matplotlib, seaborn (`app.py`)
- **Web version:** HTML, CSS, JavaScript and Chart.js (`web/`). It computes everything in the browser from `HR_Analytics.csv`, and the department filter updates every metric and chart.

## Run locally
```bash
pip install shiny pandas matplotlib seaborn
python app.py    # http://127.0.0.1:8501
```
Note: `app.py` reads `hr_data.csv` and expects `Attrition` as 0/1. Either rename `HR_Analytics.csv` and map `Yes`/`No` to `1`/`0`, or point the script at the file. The web version handles this automatically.

Web version: `npx serve web`.

---

Portfolio: [khuwaish-portfolio.vercel.app](https://khuwaish-portfolio.vercel.app) · Built by **Khuwaish Goyal**
