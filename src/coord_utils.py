from astropy.coordinates import GCRS

def icrs_to_gcrs(coord, time):
    """
    Transform ICRS coordinates to GCRS
    """
    return coord.transform_to(GCRS(obstime=time))
