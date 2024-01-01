import geocoder


def my_city():
    g = geocoder.ip('me')
    return g.city
