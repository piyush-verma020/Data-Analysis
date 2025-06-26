# 🧹 Data Cleaning with Context: Handling Government Corrections

This repository demonstrates **best practices for cleaning real-world datasets**, particularly when dealing with **government-reported time series data** that may include **retroactive corrections**.

## 🔍 Problem Overview

In datasets such as COVID-19 case counts, economic indicators, or vaccination records, it's not uncommon to find:

- ✅ Negative values  
- ✅ Sudden spikes  
- ✅ Retroactive adjustments

These aren't always errors — sometimes they are **intentional corrections** issued by the source (e.g., removing duplicates, delayed data entry, or reclassification of earlier values).

## ⚠️ Why Blind Cleaning Can Be Risky

Replacing such values with the **mean** or interpolated values (like neighboring averages) without understanding the context can:

- Remove meaningful corrections  
- Introduce bias or false trends  
- Break auditability of the data

## ✅ Our Cleaning Approach

This repo uses a **context-aware cleaning strategy**:

### 1. Understand the Data First
- Check metadata or official source notes.
- Identify if the negative values were flagged as corrections.

### 2. Annotate, Don’t Erase
- Instead of dropping or overwriting directly, add a `note` column.
  - Example: `note = "government correction"`

### 3. Maintain Two Versions
- **Original Dataset** – remains untouched for full traceability.
- **Cleaned Dataset** – used for analysis and visualization only.
  - May include smoothed or imputed values, where appropriate.

### 4. Be Transparent
- All changes are logged in code comments or metadata columns.
- Example note:  
  `"Value modified due to government correction; original was -148"`

### 5. Visualize Responsibly
- Use rolling averages or filtered views to handle noisy or revised data.
- Always label graphs clearly if using processed values.

## 📁 Files Included
- `original_data.csv` – Raw dataset as received from the source.
- `cleaned_data.csv` – Processed copy used for analysis.
- `data_cleaning_script.py` – Code demonstrating the full pipeline.
- `notebook_analysis.ipynb` – Sample notebook with trend analysis.

## 📌 Summary

This repository shows how **data cleaning is not just about fixing missing or wrong values**, but about **understanding what the data means** and preserving its integrity.

> "Clean with context, not just with code."

---

Let me know if you want me to add badges, license info, or contributors section too!
