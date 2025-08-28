# Historical-VAR---Value-at-Risk-Model

This project implements a Historical Simulation VaR model to measure potential losses on bad days for Eicher Motors stock.  
VaR is a widely used risk management metric that estimates the maximum loss over a specified time horizon at a given confidence level (α).  
Made in Collaboration with Colonel General

##  Overview
- Asset: Eicher Motors (NSE)  
- Method: Historical Simulation (non-parametric)  
- Confidence Level: 95% (α = 0.95)  
- Window Size: 252 trading days (~1 year)  

 ## Methodology
1. Data Cleaning: Imported NSE historical data (1-year).  
2. Log Returns: Computed daily log returns:  
3. VaR Calculation: Sorted returns and picked the 5th percentile.  

##  Results
- 1-Year 95% Historical VaR: 2%.  
- Breaches: 10 out of 12 days (~expected 5%).  


##  Next Steps
- Add Parametric VaR (Variance-Covariance method).  
- Add Monte Carlo Simulation for forward-looking risk.  
- Extend model to a portfolio of stocks.  
- Will upload them in seperate Repos,


## Author
Developed by Me & Colonel General as part ofrisk modeling practice.
