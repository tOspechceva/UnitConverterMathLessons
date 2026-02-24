import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, 
                             QComboBox, QLabel, QGridLayout, QVBoxLayout, 
                             QHBoxLayout, QGroupBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Конвертер единиц измерения для уроков математики')
        self.setGeometry(400, 100, 1000, 800)
        self.setStyleSheet("background-color: #fffafa;") 
        
        main_layout = QVBoxLayout()
        
        title_label = QLabel('Конвертер единиц измерения')
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont('Tahoma', 20, QFont.Bold))
        main_layout.addWidget(title_label)
        
        length_group = self.create_converter_group('Длина', [
            'Миллиметры (мм)', 
            'Сантиметры (см)', 
            'Дециметры (дм)', 
            'Метры (м)', 
            'Километры (км)'
        ])
        main_layout.addWidget(length_group)
        
        mass_group = self.create_converter_group('Масса', [
            'Граммы (г)', 
            'Килограммы (кг)', 
            'Центнеры (ц)', 
            'Тонны (т)'
        ])
        main_layout.addWidget(mass_group)
        
        time_group = self.create_converter_group('Время', [
            'Секунды (с)', 
            'Минуты (мин)', 
            'Часы (ч)', 
            'Дни (сут)'
        ])
        main_layout.addWidget(time_group)
        
        main_layout.addStretch()
        self.setLayout(main_layout)
    
    def create_converter_group(self, title, units):
        group_box = QGroupBox(title)
        group_box.setFont(QFont('Tahoma', 12, QFont.Bold))
        
        layout = QGridLayout()
        
        from_label = QLabel('Из:')
        from_label.setFont(QFont('Tahoma', 10))
        layout.addWidget(from_label, 0, 0)
        from_combo = QComboBox()
        from_combo.addItems(units)
        from_combo.setFont(QFont('Tahoma', 10))
        from_combo.setMinimumWidth(150)
        layout.addWidget(from_combo, 0, 1)
        
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText('Введите число')
        self.input_field.setFont(QFont('Tahoma', 12))
        self.input_field.setMinimumHeight(30)
        layout.addWidget(self.input_field, 0, 2, 1, 2)
        
        to_label = QLabel('В:')
        to_label.setFont(QFont('Tahoma', 10))
        layout.addWidget(to_label, 1, 0)
        to_combo = QComboBox()
        to_combo.addItems(units)
        to_combo.setFont(QFont('Tahoma', 10))
        to_combo.setMinimumWidth(150)
        layout.addWidget(to_combo, 1, 1)
        
        convert_btn = QPushButton('Конвертировать')
        convert_btn.setFont(QFont('Tahoma', 10, QFont.Bold))
        convert_btn.setMinimumHeight(30)
        convert_btn.setStyleSheet("""
            QPushButton {
                background-color: #afeeee;
                color: #919192;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #256d7b;
            }
        """)
        layout.addWidget(convert_btn, 1, 2)
        
        clear_btn = QPushButton('Очистить')
        clear_btn.setFont(QFont('Tahoma', 10))
        clear_btn.setMinimumHeight(30)
        clear_btn.setStyleSheet("""
            QPushButton {
                background-color: #ffcbdb;
                color: #919192;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #da190b;
            }
        """)
        layout.addWidget(clear_btn, 1, 3)
        
        result_label = QLabel('Результат:')
        result_label.setFont(QFont('Tahoma', 11, QFont.Bold))
        layout.addWidget(result_label, 2, 0)
        
        self.result_field = QLineEdit()
        self.result_field.setPlaceholderText('Здесь появится результат')
        self.result_field.setFont(QFont('Tahoma', 12))
        self.result_field.setMinimumHeight(30)
        self.result_field.setReadOnly(True)
        self.result_field.setStyleSheet("background-color: #f0f0f0;")
        layout.addWidget(self.result_field, 2, 1, 1, 3)
        
        layout.setHorizontalSpacing(20)
        layout.setVerticalSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)
        
        group_box.setLayout(layout)
        
        group_box.from_combo = from_combo
        group_box.to_combo = to_combo
        group_box.input_field = self.input_field
        group_box.result_field = self.result_field
        group_box.convert_btn = convert_btn
        group_box.clear_btn = clear_btn
        
        convert_btn.clicked.connect(lambda: self.convert(group_box))
        clear_btn.clicked.connect(lambda: self.clear_fields(group_box))
        
        return group_box
    
    def convert(self, group):
        try:
            value = float(group.input_field.text())
            from_unit = group.from_combo.currentText()
            to_unit = group.to_combo.currentText()
            
            group_title = group.title()
            
            if group_title == 'Длина':
                result = self.convert_length(value, from_unit, to_unit)
            elif group_title == 'Масса':
                result = self.convert_mass(value, from_unit, to_unit)
            elif group_title == 'Время':
                result = self.convert_time(value, from_unit, to_unit)
            else:
                result = None
            
            if result is not None:
                group.result_field.setText(f"{value} {from_unit} = {result:.4f} {to_unit}")
            else:
                group.result_field.setText("Ошибка конвертации")
            
        except ValueError:
            group.result_field.setText("Ошибка: введите число!")

    def convert_length(self, value, from_unit, to_unit):
        to_meters = {
            'Миллиметры (мм)': 0.001,
            'Сантиметры (см)': 0.01,
            'Дециметры (дм)': 0.1,
            'Метры (м)': 1,
            'Километры (км)': 1000
        }
        meters = value * to_meters[from_unit]
        result = meters / to_meters[to_unit]
        return result

    def convert_mass(self, value, from_unit, to_unit):
        to_grams = {
            'Граммы (г)': 1,
            'Килограммы (кг)': 1000,
            'Центнеры (ц)': 100000,
            'Тонны (т)': 1000000
        }
        grams = value * to_grams[from_unit]
        result = grams / to_grams[to_unit]
        return result

    def convert_time(self, value, from_unit, to_unit):
        to_seconds = {
            'Секунды (с)': 1,
            'Минуты (мин)': 60,
            'Часы (ч)': 3600,
            'Дни (сут)': 86400
        }
        seconds = value * to_seconds[from_unit]
        result = seconds / to_seconds[to_unit]
        return result
    
    def clear_fields(self, group):
        group.input_field.clear()
        group.result_field.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())