# Copyright of the Board of Trustees of Columbia University in the City of New York
# Script to manage registration functions including checking for redundancy

from pathlib import Path
import virtualscanner.server.registration.db_operations_mgr as dbom


"""
1. This script registers a subject
|2.Creates a database if it does not exist
|3.Appends registration data

Parameters
----------
    payload: dict
        all fields required in the REGISTRATION table

Returns
-------
    status: int
    0: successful creation of the database/insertion of a row in the REGISTRATION table/query of existing entry 
    1: fail

"""



root = Path(__file__)
db_path = root.parent / "subject.db"


def consume(payload):
    """
    1.This definition processes a payload
    |2.Creates a database if it does not exist
    |3.Appends registration data

    Parameters
    ----------
        payload: dict
            all fields required in the REGISTRATION table

    Returns
    -------
        status: int
        0: successful creation of the database (if required) and insertion of one row
        1: fail

    """

    # Check if  database 'subject' and table 'registration' exist, if not create them
    if not Path.is_file(db_path):
        dbom.create()

    # Add current registration payload to subject/registration and return status
    status = dbom.insert(payload)
    print(status)
    return status


# def check(payload):

def reuse(payload):
    """
        This definition queries if the subject is already registered


        Parameters
        ----------
            payload: dict
                all fields required in the REGISTRATION table

        Returns
        -------
            rows: dict
            row of the REGISTRATION table that match the subject being registered
            a null value indicates a new subject
            non null value(s) indicate matching subjects
        """
    rows = dbom.query(payload)
    return rows
