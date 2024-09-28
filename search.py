
# See https://github.com/peopledatalabs/peopledatalabs-python
from peopledatalabs import PDLPY

# Create a client, specifying your API key
CLIENT = PDLPY(
    # Replace this with Your API KEY
    api_key="your_api_key",
)

# Create a parameters JSON object according to the following minimum inputs role
''' profile OR email OR phone OR email_hash OR lid OR pdl_id OR (
#     (
#         (first_name AND last_name) OR name) AND
# (company OR school OR location OR street_address OR locality
# OR region OR country OR postal_code OR birth_date)
# )
'''
profile = name = firstName = lastName = email = phone = company = locality = region = country = postalCode = birthDate = " "
PARAMS = {

}

print("Search By: \n 1. profile \n 2. email \n 3. phone "
      "\n 4. (first_name AND last_name) OR name) AND "
      "(company OR location OR street_address "
      "OR locality OR region OR country OR postal_code OR birth_date)")
choice = input("Enter Your Choice: ")
if choice == "1":
    profile = input("Enter the profile link: ")
    PARAMS.update({
        "profile": {profile}
    })
elif choice == "2":
    email = input("Enter the email (ie. renee.c.paulsen1959@yahoo.com): ")
    PARAMS.update({
        "email": email
    })
elif choice == "3":
    phone = input("Enter the phone number (ie. +1 555-234-1234): ")
    PARAMS.update({
        "phone": phone
    })
elif choice == "4":

    name = input("Enter the full name (ie. Jennifer C. Jackson): ")
    company = input("Enter the company (ie. Amazon Web Services): ")
    location = input("Enter the location (ie. Medford, OR USA): ")
    street_address = input("Enter the street address (ie. 1234 Main Street): ")
    locality = input("Enter the locality (ie. Boise): ")
    region = input("Enter the region (ie. Idaho): ")
    country = input("Enter the country (ie. United States): ")
    postalCode = input("Enter the postal code (ie. 83701): ")
    birthDate = input("Enter the birth date (ie. 1996-10-01): ")

    PARAMS.update({

        "name": name,
        "company": company,
        "location": location,
        "street_address": street_address,
        "locality": locality,
        "region": region,
        "country": country,
        "postal_code": postalCode,
        "birth_date": birthDate,

    })


print(PARAMS)

# Pass the parameters to the Person Enrichment API
json_response = CLIENT.person.enrichment(
    **PARAMS,
    pretty = True
)

# Print the API response in JSON format

# print(json_response['data']["full_name"])
print(json_response.text)

