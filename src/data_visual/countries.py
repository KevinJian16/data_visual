from pygal_maps_world.i18n import COUNTRIES

NAME_TO_CODE = {name: code for code, name in COUNTRIES.items()}

# World Bank dataset uses some names that differ from pygal.
COUNTRY_NAME_OVERRIDES = {
    "Bolivia": "Bolivia, Plurinational State of",
    "Congo, Dem. Rep.": "Congo, the Democratic Republic of the",
    "Congo, Rep.": "Congo",
    "Egypt, Arab Rep.": "Egypt",
    "Gambia, The": "Gambia",
    "Hong Kong SAR, China": "Hong Kong",
    "Iran, Islamic Rep.": "Iran, Islamic Republic of",
    "Korea, Dem. Rep.": "Korea, Democratic People's Republic of",
    "Korea, Rep.": "Korea, Republic of",
    "Kyrgyz Republic": "Kyrgyzstan",
    "Lao PDR": "Lao People's Democratic Republic",
    "Libya": "Libyan Arab Jamahiriya",
    "Macao SAR, China": "Macao",
    "Macedonia, FYR": "Macedonia, the former Yugoslav Republic of",
    "Moldova": "Moldova, Republic of",
    "Slovak Republic": "Slovakia",
    "Tanzania": "Tanzania, United Republic of",
    "Venezuela, RB": "Venezuela, Bolivarian Republic of",
    "Vietnam": "Viet Nam",
    "West Bank and Gaza": "Palestine, State of",
    "Yemen, Rep.": "Yemen",
}

# Manual ISO-3166 alpha-2 codes for names missing from pygal.
MANUAL_COUNTRY_CODES = {
    "American Samoa": "as",
    "Antigua and Barbuda": "ag",
    "Aruba": "aw",
    "Bahamas, The": "bs",
    "Barbados": "bb",
    "Bermuda": "bm",
    "British Virgin Islands": "vg",
    "Cabo Verde": "cv",
    "Cayman Islands": "ky",
    "Comoros": "km",
    "Czechia": "cz",
    "Curacao": "cw",
    "Dominica": "dm",
    "Eswatini": "sz",
    "Faroe Islands": "fo",
    "Faeroe Islands": "fo",
    "Fiji": "fj",
    "French Polynesia": "pf",
    "Gibraltar": "gi",
    "Grenada": "gd",
    "Isle of Man": "im",
    "Kiribati": "ki",
    "Korea, Dem. People's Rep.": "kp",
    "Kosovo": "xk",
    "Marshall Islands": "mh",
    "Micronesia, Fed. Sts.": "fm",
    "Nauru": "nr",
    "North Macedonia": "mk",
    "New Caledonia": "nc",
    "Northern Mariana Islands": "mp",
    "Palau": "pw",
    "Puerto Rico (US)": "pr",
    "Qatar": "qa",
    "Samoa": "ws",
    "Sint Maarten (Dutch part)": "sx",
    "Solomon Islands": "sb",
    "Somalia, Fed. Rep.": "so",
    "South Sudan": "ss",
    "St. Kitts and Nevis": "kn",
    "St. Lucia": "lc",
    "St. Martin (French part)": "mf",
    "St. Vincent and the Grenadines": "vc",
    "Tonga": "to",
    "Trinidad and Tobago": "tt",
    "Turks and Caicos Islands": "tc",
    "Turkiye": "tr",
    "Tuvalu": "tv",
    "Vanuatu": "vu",
    "Virgin Islands (U.S.)": "vi",
}

# Regional or aggregate groups from the World Bank dataset.
REGION_NAMES = {
    "Arab World",
    "Caribbean small states",
    "East Asia & Pacific (all income levels)",
    "East Asia & Pacific (developing only)",
    "Euro area",
    "Europe & Central Asia (all income levels)",
    "Europe & Central Asia (developing only)",
    "European Union",
    "Heavily indebted poor countries (HIPC)",
    "High income",
    "High income: OECD",
    "High income: nonOECD",
    "Latin America & Caribbean (all income levels)",
    "Latin America & Caribbean (developing only)",
    "Least developed countries: UN classification",
    "Low & middle income",
    "Low income",
    "Lower middle income",
    "Middle East & North Africa (all income levels)",
    "Middle East & North Africa (developing only)",
    "Middle income",
    "North America",
    "OECD members",
    "Other small states",
    "Pacific island small states",
    "Small states",
    "South Asia",
    "Sub-Saharan Africa (all income levels)",
    "Sub-Saharan Africa (developing only)",
    "Upper middle income",
    "World",
    "Channel Islands",
}


def is_region(country_name):
    """Check if the given country name is a region."""
    return country_name in REGION_NAMES


def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    if is_region(country_name):
        return None

    if country_name in COUNTRY_NAME_OVERRIDES:
        return NAME_TO_CODE.get(COUNTRY_NAME_OVERRIDES[country_name])

    if country_name in MANUAL_COUNTRY_CODES:
        return MANUAL_COUNTRY_CODES[country_name]

    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None
