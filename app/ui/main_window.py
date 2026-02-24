from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from app.ui.styles import STYLES
from app.ui.converter_widget import ConverterWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Конвертер единиц измерения для уроков математики')
        self.setGeometry(400, 100, 1000, 800)
        self.setStyleSheet(STYLES["main_window"]) 
        
        main_layout = QVBoxLayout()
        
        title_label = QLabel('Конвертер единиц измерения')
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont('Tahoma', 20, QFont.Bold))
        main_layout.addWidget(title_label)
        
        # Группа Длина
        length_group = ConverterWidget('Длина', [
            'Миллиметры (мм)', 
            'Сантиметры (см)', 
            'Дециметры (дм)', 
            'Метры (м)', 
            'Километры (км)'
        ])
        main_layout.addWidget(length_group)
        
        # Группа Масса
        mass_group = ConverterWidget('Масса', [
            'Граммы (г)', 
            'Килограммы (кг)', 
            'Центнеры (ц)', 
            'Тонны (т)'
        ])
        main_layout.addWidget(mass_group)
        
        # Группа Время
        time_group = ConverterWidget('Время', [
            'Секунды (с)', 
            'Минуты (мин)', 
            'Часы (ч)', 
            'Дни (сут)'
        ])
        main_layout.addWidget(time_group)
        
        main_layout.addStretch()
        self.setLayout(main_layout)