clear
set more off
cd "/Users/burrelvannjr/Desktop/disp_scrape/"

insheet using "/Users/burrelvannjr/Desktop/disp_scrape/data/disp.csv"
duplicates drop id, force
outsheet using "data/disp_clean.csv", comma replace
