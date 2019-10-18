import requests
import pytest

states = states_hash = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District Of Columbia': 'DC',
    'Federated States Of Micronesia': 'FM',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Marshall Islands': 'MH',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands': 'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Palau': 'PW',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}


def test_all_brew_not_empty():
    response = requests.get('https://api.openbrewerydb.org/breweries')
    assert response.json()


state_with_brews = (state.replace(' ', '_') for state in states_hash.keys() if state not in (
'American Samoa', 'Federated States Of Micronesia', 'Guam', 'Marshall Islands', 'Northern Mariana Islands', 'Palau',
'Puerto Rico', 'Virgin Islands'))


@pytest.mark.parametrize('state', state_with_brews)
def test_filter_brew_by_state(state):
    response = requests.get('https://api.openbrewerydb.org/breweries?by_state={state}'.format(state=state))
    assert response.json()


@pytest.mark.parametrize('per_page', (1, 2, 50))
def test_brew_paging(per_page):
    response = requests.get('https://api.openbrewerydb.org/breweries?per_page={per_page}'.format(per_page=per_page))
    assert len(response.json()) == per_page


def test_brew_sorting():
    response = requests.get('https://api.openbrewerydb.org/breweries?by_state=alaska&sort=name')
    response_json = response.json()
    for x in range(len(response_json) - 1):
        assert response_json[x]['name'] < response_json[x + 1]['name']


def test_brew_sorting_desc():
    response = requests.get('https://api.openbrewerydb.org/breweries?by_state=alaska&sort=-name')
    response_json = response.json()
    for x in range(len(response_json) - 1):
        assert response_json[x]['name'] > response_json[x + 1]['name']
