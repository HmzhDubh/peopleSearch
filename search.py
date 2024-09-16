
# See https://github.com/peopledatalabs/peopledatalabs-python
from peopledatalabs import PDLPY

# Create a client, specifying your API key
CLIENT = PDLPY(
    # Replace this with Your API KEY
    api_key="Your_API_Key",
)

# Create a parameters JSON object according to the following minimum inputs role
''' profile OR email OR phone OR email_hash OR lid OR pdl_id OR (
#     (
#         (first_name AND last_name) OR name) AND
# (company OR school OR location OR street_address OR locality
# OR region OR country OR postal_code OR birth_date)
# )
'''
PARAMS = {
    "first_name": "Omar",
    "last_name": "Mohsen",
    "company": "Tamara"
}

# Pass the parameters to the Person Enrichment API
json_response = CLIENT.person.identify(
    **PARAMS,
    pretty = True
)

# Print the API response in JSON format

# print(json_response['data']["full_name"])
print(json_response.text)

