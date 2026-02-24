from PyQt5.QtWidgets import (QGroupBox, QGridLayout, QLabel, 
                             QComboBox, QLineEdit, QPushButton)
from PyQt5.QtGui import QFont
from app.core.converter import UnitConverter
from app.ui.styles import STYLES

class ConverterWidget(QGroupBox):
    def __init__(self, title, units, parent=None):
        super().__init__(title, parent)
        self.units = units
        self.category = title
        self.initUI()

    def initUI(self):
        self.setFont(QFont('Tahoma', 12, QFont.Bold))
        layout = QGridLayout()
        
        # Из
        from_label = QLabel('Из:')
        from_label.setFont(QFont('Tahoma', 10))
        layout.addWidget(from_label, 0, 0)
        
        self.from_combo = QComboBox()
        self.from_combo.addItems(self.units)
        self.from_combo.setFont(QFont('Tahoma', 10))
        self.from_combo.setMinimumWidth(150)
        layout.addWidget(self.from_combo, 0, 1)
        
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText('Введите число')
        self.input_field.setFont(QFont('Tahoma', 12))
        self.input_field.setMinimumHeight(30)
        layout.addWidget(self.input_field, 0, 2, 1, 2)
        
        # В
        to_label = QLabel('В:')
        to_label.setFont(QFont('Tahoma', 10))
        layout.addWidget(to_label, 1, 0)
        
        self.to_combo = QComboBox()
        self.to_combo.addItems(self.units)
        self.to_combo.setFont(QFont('Tahoma', 10))
        self.to_combo.setMinimumWidth(150)
        layout.addWidget(self.to_combo, 1, 1)
        
        # Кнопки
        self.convert_btn = QPushButton('Конвертировать')
        self.convert_btn.setFont(QFont('Tahoma', 10, QFont.Bold))
        self.convert_btn.setMinimumHeight(30)
        self.convert_btn.setStyleSheet(STYLES["convert_btn"])
        layout.addWidget(self.convert_btn, 1, 2)
        
        self.clear_btn = QPushButton('Очистить')
        self.clear_btn.setFont(QFont('Tahoma', 10))
        self.clear_btn.setMinimumHeight(30)
        self.clear_btn.setStyleSheet(STYLES["clear_btn"])
        layout.addWidget(self.clear_btn, 1, 3)
        
        # Результат
        result_label = QLabel('Результат:')
        result_label.setFont(QFont('Tahoma', 11, QFont.Bold))
        layout.addWidget(result_label, 2, 0)
        
        self.result_field = QLineEdit()
        self.result_field.setPlaceholderText('Здесь появится результат')
        self.result_field.setFont(QFont('Tahoma', 12))
        self.result_field.setMinimumHeight(30)
        self.result_field.setReadOnly(True)
        self.result_field.setStyleSheet(STYLES["result_field"])
        layout.addWidget(self.result_field, 2, 1, 1, 3)
        
        # Настройки макета
        layout.setHorizontalSpacing(20)
        layout.setVerticalSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)
        self.setLayout(layout)
        
        # Подключение сигналов
        self.convert_btn.clicked.connect(self.convert)
        self.clear_btn.clicked.connect(self.clear_fields)

    def convert(self):
        try:
            value = float(self.input_field.text())
            from_unit = self.from_combo.currentText()
            to_unit = self.to_combo.currentText()
            
            result = UnitConverter.calculate(self.category, value, from_unit, to_unit)
            
            if result is not None:
                self.result_field.setText(f"{value} {from_unit} = {result:.4f} {to_unit}")
            else:
                self.result_field.setText("Ошибка конвертации")
            
        except ValueError:
            self.result_field.setText("Ошибка: введите число!")

    def clear_fields(self):
        self.input_field.clear()
        self.result_field.clear()