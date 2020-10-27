import numpy as npP
import pandas as pd
import requests

_host = "localhost:3000/api"


class OracleSessionInstance:
    """Instance Docstring"""

    def __init__(self, username, userkey, datatype, labeltype, jobtype, sessionkey):
        # TODO: initialize session on server
        res = apicall.parsed
        if res:
            self.session_started = True
        else:
            self.session_started = False
        self.username = username
        self.userkey = userkey
        self.datatype = datatype
        self.labeltype = labeltype
        self.jobtype = jobtype
        self.sessionkey = sessionkey


def username_check(username):
    # TODO: write check


def userkey_check(username, userkey):
    # TODO: write check


def datatype_check(datatype):
    # TODO: write check


def labeltype_check(datatype, labeltype):
    # TODO: write check


def jobtype_check(jobtype):
    # TODO: write check


def sessionkey_check(username, sessionkey):
    # TODO: write check


def initialize(username, userkey, datatype, labeltype, jobtype, sessionkey=None):
    username_check(username)
    userkey_check(username, userkey)
    datatype_check(datatype)
    labeltype_check(datatype, labeltype)
    jobtype_check(jobtype)
    sessionkey_check(username, sessionkey)
    return OracleSessionInstance(username, userkey, datatype, labeltype, jobtype, sessionkey)
