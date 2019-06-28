# Copyright of the Board of Trustees of Columbia University in the City of New York
# Unit test Script to check for registration functions independently


import virtualscanner.server.registration.register as reg

"""
1. This script unit tests the subject registration
|2. tests multiple cases of the registration implementation


Returns
-------
    status: int
    0: tests passed
    1: fail
"""

# os.chdir("./Virtual-Scanner")

def create_payload():
    """
    This definition creates a test payload

    Returns
    -------
        payload: dict
        all fields required by the REGISTRATION table in subject.db
    """
    # can make this more random later on, but for now we hardcode
    payload = {
        "SUBJECTTYPE": "numerical",
        "patid": 5466,  # random.randint(1, 1000)
        "name": "Numerical",
        "AGE": 0,  # random.randint(4, 100),
        "DOB": "4/17/2019",  # redundant but useful for an OR situation later
        "GENDER": "other",
        "WEIGHT": 3.0,  # random.randint(60, 300),
        "HEIGHT": 20.0,  # random.randint(60, 200),
        "ORIENTATION": "HFS",
        "ANATOMY": "brain"

    }
    return payload


# Simulate the payload to be received from the client
payload = create_payload()

# check for registering a subject
status = reg.consume(payload)

# check for existing subject
payload = {
    "PATID": 5465,
    # "NAME": "Mustang",
    # "AGE": 45,
    #  "DOB": "03/03/1983", #redundant but useful for an OR situation later
    #  "GENDER": "Female",
    #  "WEIGHT": 170,
    #  "HEIGHT": 165,
    #  "ORIENTATION":"Head first supine",
    # "ANATOMY":"Brain"

}
payload = reg.reuse(payload)
print(payload)

# TODO: handle different cases
