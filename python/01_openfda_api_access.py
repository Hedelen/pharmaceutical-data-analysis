import requests


base_endpoint = 'https://api.fda.gov/drug/event.json'

glps = (
    'semaglutide',
    'liraglutide',
    'dulaglutide',
    'exenatide',
    'lixisenatide',
    'tirzepatide'
)

payload = {"search": }

r = requests.get(base_endpoint, params=payload)

# API key intentionally not stored in this repository.
# Keep secrets in a local .env file or environment variable.
