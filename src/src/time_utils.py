from astropy.time import Time

def utc_to_tt(utc_string):
    """
    Convert UTC string to Terrestrial Time (TT)
    """
    return Time(utc_string, scale="utc").tt
