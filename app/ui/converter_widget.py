from PyQt5.QtWidgets import QGridLayout, QLabel, QComboBox, QLineEdit, QPushButton, QGroupBox
from PyQt5.QtGui import QFont, QDoubleValidator
from PyQt5.QtCore import  pyqtSignal
from app.core.converter import UnitConverter
from app.ui.styles import STYLES

class NumericValidator(QDoubleValidator):
    def __init__(self):
        super().__init__()
        self.setNotation(QDoubleValidator.StandardNotation)
        self.setDecimals(6)
    
    def validate(self, text, pos):
        if not text:
            return (QDoubleValidator.Acceptable, text, pos)
        if text == '-':
            return (QDoubleValidator.Intermediate, text, pos)
        return super().validate(text, pos)

class ConverterWidget(QGroupBox):
 
    conversion_completed = pyqtSignal(str, str, str, str, float)
    
    def __init__(self, parent=None):
        super().__init__('Конвертер единиц измерения', parent)
        self.converter = UnitConverter()
        self.initUI()
    
    def initUI(self):
        self.setStyleSheet(STYLES["group_box"])
        self.setFont(QFont('Tahoma', 12, QFont.Bold))
        
        layout = QGridLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(25, 35, 25, 25)
        
        # === Категория ===
        category_label = QLabel('Категория:')
        category_label.setFont(QFont('Tahoma', 11, QFont.Bold))
        category_label.setStyleSheet(STYLES["label"])
        layout.addWidget(category_label, 0, 0)
        
        self.category_combo = QComboBox()
        self.category_combo.addItems(self.converter.get_categories())
        self.category_combo.setFont(QFont('Tahoma', 11))
        self.category_combo.setStyleSheet(STYLES["combo_box"])
        self.category_combo.setMinimumHeight(35)
        layout.addWidget(self.category_combo, 0, 1, 1, 3)
        
        # === Из ===
        from_label = QLabel('Из:')
        from_label.setFont(QFont('Tahoma', 11, QFont.Bold))
        from_label.setStyleSheet(STYLES["label"])
        layout.addWidget(from_label, 1, 0)
        
        self.from_combo = QComboBox()
        self.from_combo.setFont(QFont('Tahoma', 11))
        self.from_combo.setStyleSheet(STYLES["combo_box"])
        self.from_combo.setMinimumHeight(35)
        layout.addWidget(self.from_combo, 1, 1, 1, 2)
        
        # === Поле ввода ===
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText('Введите числовое значение')
        self.input_field.setFont(QFont('Tahoma', 12))
        self.input_field.setMinimumHeight(35)
        self.input_field.setStyleSheet(STYLES["input_field"])
        self.input_field.setValidator(NumericValidator())
        layout.addWidget(self.input_field, 1, 3)
        
        # === В ===
        to_label = QLabel('В:')
        to_label.setFont(QFont('Tahoma', 11, QFont.Bold))
        to_label.setStyleSheet(STYLES["label"])
        layout.addWidget(to_label, 2, 0)
        
        self.to_combo = QComboBox()
        self.to_combo.setFont(QFont('Tahoma', 11))
        self.to_combo.setStyleSheet(STYLES["combo_box"])
        self.to_combo.setMinimumHeight(35)
        layout.addWidget(self.to_combo, 2, 1, 1, 2)
        
        # === Кнопка Конвертировать ===
        self.convert_btn = QPushButton('Конвертировать')
        self.convert_btn.setFont(QFont('Tahoma', 11, QFont.Bold))
        self.convert_btn.setMinimumHeight(35)
        self.convert_btn.setStyleSheet(STYLES["convert_btn"])
        layout.addWidget(self.convert_btn, 2, 3)
        
        # === Результат ===
        result_label = QLabel('Результат:')
        result_label.setFont(QFont('Tahoma', 11, QFont.Bold))
        result_label.setStyleSheet(STYLES["label"])
        layout.addWidget(result_label, 3, 0)
        
        self.result_field = QLineEdit()
        self.result_field.setPlaceholderText('Здесь появится результат')
        self.result_field.setFont(QFont('Tahoma', 12, QFont.Bold))
        self.result_field.setMinimumHeight(35)
        self.result_field.setReadOnly(True)
        self.result_field.setStyleSheet(STYLES["result_field"])
        layout.addWidget(self.result_field, 3, 1, 1, 3)
        
        # === Кнопка Очистить ===
        self.clear_btn = QPushButton('Очистить')
        self.clear_btn.setFont(QFont('Tahoma', 11))
        self.clear_btn.setMinimumHeight(35)
        self.clear_btn.setStyleSheet(STYLES["clear_btn"])
        layout.addWidget(self.clear_btn, 4, 0, 1, 4)
        
        self.setLayout(layout)
        
        self.category_combo.currentTextChanged.connect(self._on_category_changed)
        self.convert_btn.clicked.connect(self.convert)
        self.clear_btn.clicked.connect(self.clear_fields)
        self.input_field.returnPressed.connect(self.convert)
        
        self._on_category_changed(self.category_combo.currentText())
    
    def _on_category_changed(self, category):
        units = self.converter.get_units(category)
        
        current_from = self.from_combo.currentText()
        current_to = self.to_combo.currentText()
        
        self.from_combo.clear()
        self.to_combo.clear()
        self.from_combo.addItems(units)
        self.to_combo.addItems(units)
        
        if current_from in units:
            self.from_combo.setCurrentText(current_from)
        if current_to in units:
            self.to_combo.setCurrentText(current_to)
        
        self.result_field.clear()
    
    def convert(self):
        input_text = self.input_field.text().strip()
        
        if not input_text:
            self._show_error('Введите значение')
            return
        
        try:
            value = float(input_text)
            category = self.category_combo.currentText()
            from_unit = self.from_combo.currentText()
            to_unit = self.to_combo.currentText()
            
            result = self.converter.convert(category, value, from_unit, to_unit)
            
            if result is not None:
                if result == int(result):
                    result_str = f"{int(result):,}".replace(',', ' ')
                else:
                    result_str = f"{result:.6f}".rstrip('0').rstrip('.')
                
                output = f'{value} {from_unit} = {result_str} {to_unit}'
                self.result_field.setText(output)
                self.result_field.setStyleSheet(STYLES["result_field"])
                
                self.conversion_completed.emit(
                    category, from_unit, to_unit, str(value), result
                )
            else:
                self._show_error('Ошибка конвертации')
        
        except ValueError:
            self._show_error('Ошибка: введите корректное число')
    
    def _show_error(self, message):
        self.result_field.setText(message)
        self.result_field.setStyleSheet("""
            QLineEdit {
                background-color: #ff7675;
                border: 2px solid #d63031;
                border-radius: 5px;
                padding: 8px;
                font-size: 14px;
                font-weight: bold;
                color: white;
            }
        """)
    
    def clear_fields(self):
        self.input_field.clear()
        self.result_field.clear()
        self.result_field.setStyleSheet(STYLES["result_field"])
        self.input_field.setFocus()
    
    def refresh_categories(self):
        current = self.category_combo.currentText()
        self.category_combo.clear()
        self.category_combo.addItems(self.converter.get_categories())
        if current in self.converter.get_categories():
            self.category_combo.setCurrentText(current)
        else:
            self._on_category_changed(self.category_combo.currentText())