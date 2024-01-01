from weather import *
from geolocation import *
from data_base import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap
import sys


class Track(QWidget):
    def __init__(self):
        super().__init__()

        # Настройки окна
        self.setFixedSize(400, 300)
        self.setWindowTitle('Погода')
        self.setStyleSheet('color: rgb(0, 0, 0);')

        # Фон
        self.pixmap1 = QPixmap('photo/bg.png')
        self.image_bg = QLabel(self)
        self.image_bg.setPixmap(self.pixmap1)
        self.image_bg.resize(400, 300)

        # Изображение температуры
        self.pixmap = QPixmap('photo/temperature-high.png')
        self.image_temp = QLabel(self)
        self.image_temp.setPixmap(self.pixmap)
        self.image_temp.hide()

        # изображение ветра
        self.pixmap2 = QPixmap('photo/wind.png')
        self.image_wind = QLabel(self)
        self.image_wind.setPixmap(self.pixmap2)
        self.image_wind.hide()

        # Изображение влажности
        self.pixmap3 = QPixmap('photo/raindrops.png')
        self.image_humidity = QLabel(self)
        self.image_humidity.setPixmap(self.pixmap3)
        self.image_humidity.hide()

        # Изображение давления
        self.pixmap4 = QPixmap('photo/barometer.png')
        self.image_pressure = QLabel(self)
        self.image_pressure.setPixmap(self.pixmap4)
        self.image_pressure.hide()

        # Изображение восхода
        self.pixmap5 = QPixmap('photo/sunrise-alt.png')
        self.image_sunrise = QLabel(self)
        self.image_sunrise.setPixmap(self.pixmap5)
        self.image_sunrise.hide()

        # Изображение заката
        self.pixmap6 = QPixmap('photo/sunset.png')
        self.image_sunset = QLabel(self)
        self.image_sunset.setPixmap(self.pixmap6)
        self.image_sunset.hide()

        # Изображение здания
        self.pixmap7 = QPixmap('photo/cityscape.png')
        self.image_building = QLabel(self)
        self.image_building.setPixmap(self.pixmap7)
        self.image_building.hide()

        self.inscription = QLabel('Введите название города →', self)
        self.inscription.setStyleSheet('font: 16pt "Times New Roman";')
        self.inscription.move(20, 40)
        self.inscription.hide()

        self.city_name = QLineEdit(self)
        self.city_name.setStyleSheet('background-color: rgba(255, 255, 255, 0);')
        self.city_name.move(220, 40)
        self.city_name.hide()

        # Ошибка в названии
        self.city_name_error = QLabel(self)
        self.city_name_error.hide()

        # Вывод названия города
        self.city_name_lable = QLabel(self)
        self.city_name_lable.setStyleSheet('font: 22pt "Times New Roman";')
        self.city_name_lable.resize(320, 25)
        self.city_name_lable.move(200, 10)

        # Вывод температуры
        self.temp_btn = QLabel(self)
        self.temp_btn.setStyleSheet('font: 16pt "Times New Roman";')
        self.temp_btn.resize(250, 20)
        self.temp_btn.move(90, 60)

        # Вывод влажности
        self.humidity_btn = QLabel(self)
        self.humidity_btn.setStyleSheet('font: 16pt "Times New Roman";')
        self.humidity_btn.resize(250, 20)
        self.humidity_btn.move(240, 60)

        # Вывод давления
        self.pressure_btn = QLabel(self)
        self.pressure_btn.setStyleSheet('font: 16pt "Times New Roman";')
        self.pressure_btn.resize(250, 20)
        self.pressure_btn.move(450, 60)

        # Вывод рассвета
        self.sunrise_btn = QLabel(self)
        self.sunrise_btn.setStyleSheet('font: 16pt "Times New Roman";')
        self.sunrise_btn.resize(250, 40)
        self.sunrise_btn.move(240, 120)

        # Вывод заката
        self.sunset_btn = QLabel(self)
        self.sunset_btn.setStyleSheet('font: 16pt "Times New Roman";')
        self.sunset_btn.resize(250, 40)
        self.sunset_btn.move(450, 120)

        # Скорость ветра
        self.wind_btn = QLabel(self)
        self.wind_btn.setStyleSheet('font: 16pt "Times New Roman";')
        self.wind_btn.resize(250, 20)
        self.wind_btn.move(100, 130)

        self.weather_search_btn = QPushButton('Узнать погоду', self)
        self.weather_search_btn.setStyleSheet('background-color: rgba(255, 255, 255, 0); font: 75 14pt "Futura";')
        self.weather_search_btn.move(120, 100)
        self.weather_search_btn.clicked.connect(self.run)
        self.weather_search_btn.hide()

        self.my_city_btn = QPushButton('Погода в моём городе', self)
        self.my_city_btn.setStyleSheet('background-color: rgba(255, 255, 255, 0); font: 75 14pt "Futura";')
        self.my_city_btn.move(100, 200)
        self.my_city_btn.clicked.connect(self.default_city)
        self.my_city_btn.hide()

        self.name = QLabel('Введите логин', self)
        self.name.move(70, 40)

        self.username = QLineEdit(self)
        self.username.setStyleSheet('background-color: rgba(255, 255, 255, 0);')
        self.username.move(180, 40)

        self.password_lb = QLabel('Введите пароль', self)
        self.password_lb.move(70, 100)

        self.password = QLineEdit(self)
        self.password.setStyleSheet('background-color: rgba(255, 255, 255, 0);')
        self.password.move(180, 100)

        self.reg_btn = QPushButton('Зарегистрироваться', self)
        self.reg_btn.move(110, 150)
        self.reg_btn.setStyleSheet('background-color: rgba(255, 255, 255, 0); font: 75 14pt "Futura";')
        self.reg_btn.clicked.connect(self.registration)

        self.log_btn = QPushButton('Войти', self)
        self.log_btn.move(110, 200)
        self.log_btn.setStyleSheet('background-color: rgba(255, 255, 255, 0); font: 75 14pt "Futura";')
        self.log_btn.clicked.connect(self.log)

        self.attempt = QLabel(self)
        self.attempt.resize(200, 20)
        self.attempt.move(80, 235)

    def run(self, name=''):
        try:
            if name:
                data = get_weather(name)
            else:
                data = get_weather(self.city_name.text())
            self.my_city_btn.hide()
            self.image_building.move(500, 320)
            self.image_bg.resize(650, 450)
            self.city_name_error.clear()
            self.setFixedSize(650, 450)
            self.inscription.move(120, 250)
            self.city_name.move(320, 250)
            self.city_name.clear()
            self.weather_search_btn.move(220, 300)

            # Вывод всех картинок
            self.image_temp.show()
            self.image_wind.show()
            self.image_humidity.show()
            self.image_pressure.show()
            self.image_sunrise.show()
            self.image_sunset.show()
            self.image_building.show()

            # Название города
            self.city_name_lable.setText(f'Погода в городе {data.get_city()}')

            # Температура
            self.image_temp.move(50, 60)
            self.temp_btn.setText(f'{data.get_temp()}°C')

            # Влажность
            self.humidity_btn.setText(f'Влажность {data.get_humidity()}%')
            self.image_humidity.move(200, 60)

            # Давление
            self.pressure_btn.setText(f'Давление {data.get_pressure()} мм.рт.ст.')
            self.image_pressure.move(400, 60)

            # Рассвет
            self.sunrise_btn.setText(f'Рассвет \n{data.get_sunrise()}')
            self.image_sunrise.move(200, 130)

            # Закат
            self.sunset_btn.setText(f'Закат \n{data.get_sunset()}')
            self.image_sunset.move(400, 130)

            # Ветер
            self.wind_btn.setText(f'{data.get_wind()}м/с')
            self.image_wind.move(60, 130)

        except KeyError:
            self.my_city_btn.hide()
            self.city_name.clear()
            self.city_name_lable.clear()
            self.temp_btn.clear()
            self.humidity_btn.clear()
            self.pressure_btn.clear()
            self.sunrise_btn.clear()
            self.sunset_btn.clear()
            self.wind_btn.clear()

            self.image_temp.hide()
            self.image_wind.hide()
            self.image_humidity.hide()
            self.image_pressure.hide()
            self.image_sunrise.hide()
            self.image_sunset.hide()

            self.setFixedSize(400, 250)
            self.inscription.move(20, 80)
            self.city_name_error.show()
            self.city_name_error.resize(200, 30)
            self.city_name_error.setText('Проверьте название города!')
            self.city_name_error.move(100, 20)
            self.city_name.move(220, 80)
            self.weather_search_btn.move(120, 140)

    def default_city(self):
        self.run(my_city())

    def registration(self):
        if len(self.username.text()) != 0 and len(self.password.text()) != 0:
            result = reg(self.username.text(), self.password.text())
            if result == self.username.text():
                self.name.hide()
                self.username.hide()
                self.password_lb.hide()
                self.password.hide()
                self.reg_btn.hide()
                self.log_btn.hide()
                self.attempt.hide()

                self.inscription.show()
                self.weather_search_btn.show()
                self.city_name.show()
                self.my_city_btn.show()
            elif result != self.username:
                self.attempt.setText(result)
                self.password.clear()
                self.username.clear()
        else:
            self.attempt.setText('Проверьте логин или пароль')

    def log(self):
        if len(self.username.text()) != 0 or len(self.password.text()) != 0:
            result = login(self.username.text(), self.password.text())
            if result == self.username.text():
                self.name.hide()
                self.username.hide()
                self.password_lb.hide()
                self.password.hide()
                self.reg_btn.hide()
                self.log_btn.hide()
                self.attempt.hide()

                self.inscription.show()
                self.weather_search_btn.show()
                self.city_name.show()
                self.my_city_btn.show()
            else:
                self.password.clear()
                self.username.clear()
                self.attempt.setText('Проверьте логин или пароль')
        else:
            self.attempt.setText('Проверьте логин или пароль')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    icon = QIcon('photo/cloud.png')
    app.setWindowIcon(icon)
    ex = Track()
    ex.show()
    sys.exit(app.exec_())