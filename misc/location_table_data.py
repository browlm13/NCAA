"""

    State/Province, City Table  Data

"""

import numpy as np
import pandas as pd

US_CITIES_STATES_COUNTIES_CSV = "us_cities_states_counties.csv"

df = pd.read_csv(US_CITIES_STATES_COUNTIES_CSV, delimiter='|')



ca_province_to_abbrev ={
    "Alberta"  : "AB",
    "British Columbia" : "BC",
    "Manitoba" : "MB",
    "New Brunswick" : "NB",
    "Newfoundland & Labrador" : "NF",
    "Northwest Territories" : "NT",
    "Nova Scotia" : "NS",
    "Nunavut" : "NU",
    "Ontario" : "ON",
    "Prince Edward Island" : "PE",
    "Quebec" : "QC",
    #"Quebec" : ["QC", "PQ"],
    "Saskatchewan" : "SK",
    "Yukon" : "YT"
}

us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    #"Hawai'i": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
}

