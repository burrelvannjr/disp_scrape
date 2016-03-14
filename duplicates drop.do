clear
set more off
cd "/Users/burrelvannjr/Desktop/disp_scrape/"

insheet using "/Users/burrelvannjr/Desktop/disp_scrape/data/disp.csv"
duplicates drop id, force
replace states = "California" if states == "Californialifornia"
replace states = "California" if states == "Californialifornia."
replace states = "California" if states == "ca"
replace states = "Washington" if states == "Wa"
replace states = "Massachusetts" if states == "MA"
replace states = "Illinois" if states == "IL"
outsheet using "data/disp_clean.csv", comma replace
