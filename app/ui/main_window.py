from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QAction, QMessageBox, QStatusBar, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from app.ui.styles import STYLES
from app.ui.converter_widget import ConverterWidget
from app.core.converter import UnitConverter
from app.data.json_handler import UnitsJSONHandler


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.converter = UnitConverter()
        self.json_handler = UnitsJSONHandler()
        self.conversion_history = []
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Конвертер единиц измерения')
        self.setGeometry(400, 100, 650, 550)
        self.setMinimumSize(550, 500)
        self.setStyleSheet(STYLES["main_window"])
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
    
        self._create_menu()
        
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage('Готов к работе')

        main_layout = QVBoxLayout()
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(30, 10, 30, 30)
        

        title_label = QLabel('Конвертер единиц измерения')
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont('Tahoma', 22, QFont.Bold))
        title_label.setStyleSheet(STYLES["title_label"])
        main_layout.addWidget(title_label)
        
        self.converter_widget = ConverterWidget()
        self.converter_widget.conversion_completed.connect(self._on_conversion_completed)
        main_layout.addWidget(self.converter_widget)
        
        central_widget.setLayout(main_layout)
    
    def _create_menu(self):
        menubar = self.menuBar()
        menubar.setStyleSheet(STYLES["menu_bar"])
        
        file_menu = menubar.addMenu('Файл')
        
        reload_action = QAction('Перезагрузить данные', self)
        reload_action.triggered.connect(self._reload_data)
        file_menu.addAction(reload_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction('Выход', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        help_menu = menubar.addMenu('История')
        
        history_action = QAction('История конвертаций', self)
        history_action.triggered.connect(self._show_history)
        help_menu.addAction(history_action)
    
    def _on_conversion_completed(self, category, from_unit, to_unit, value, result):
        self.conversion_history.append({
            'category': category,
            'from': from_unit,
            'to': to_unit,
            'value': value,
            'result': result
        })
        
        if len(self.conversion_history) > 10:
            self.conversion_history.pop(0)
        
        self.status_bar.showMessage(
            f'Конвертация: {value} {from_unit} → {result:.4f} {to_unit}',
            5000
        )
    
    def _reload_data(self):
        self.json_handler.reload()
        self.converter.reload_data()
        self.converter_widget.refresh_categories()
        self.status_bar.showMessage('Данные перезагружены', 3000)
        QMessageBox.information(
            self, 
            'Обновлено', 
            'Данные единиц измерения успешно перезагружены из JSON файла'
        )
    
    def _show_history(self):
        if not self.conversion_history:
            QMessageBox.information(
                self,
                'История',
                'История конвертаций пуста'
            )
            return
        
        history_text = '<h3> История конвертаций</h3><ul>'
        for record in reversed(self.conversion_history):
            history_text += (
                f"<li>{record['value']} {record['from']} = "
                f"{record['result']:.4f} {record['to']} "
                f"({record['category']})</li>"
            )
        history_text += '</ul>'
        
        QMessageBox.about(self, 'История', history_text)