clear
set more off
cd "/Users/burrelvannjr/Desktop/disp_scrape/"

insheet using "data/disp_clean.csv"
gen numdisp = 1
bys years: egen ndyear = sum(numdisp)
bys states: egen ndstate = sum(numdisp)
outsheet using "data/disp_sums.csv", comma replace
