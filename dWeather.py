class DataWeather:
    def __init__(self):
        self.city_name = 'error'
        self.temp = 0
        self.humidity = 0
        self.pressure = 0
        self.wind = 0
        self.sunrise = 0
        self.sunset = 0

    def set_city(self, name):
        self.city_name = name

    def get_city(self):
        return self.city_name

    def set_temp(self, value):
        self.temp = value

    def get_temp(self):
        return self.temp

    def set_humidity(self, value):
        self.humidity = value

    def get_humidity(self):
        return self.humidity

    def set_pressure(self, value):
        self.pressure = value

    def get_pressure(self):
        return self.pressure

    def set_wind(self, value):
        self.wind = value

    def get_wind(self):
        return self.wind

    def set_sunrise(self, value):
        self.sunrise = value
        self.sunrise = str(self.sunrise)
        self.sunrise = self.sunrise.split()[1][:5]

    def get_sunrise(self):
        return self.sunrise

    def set_sunset(self, value):
        self.sunset = value
        self.sunset = str(self.sunset)
        self.sunset = self.sunset.split()[1][:5]

    def get_sunset(self):
        return self.sunset
