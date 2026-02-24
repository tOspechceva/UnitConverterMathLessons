STYLES = {
    "main_window": """
        QWidget {
            background-color: #fffafa;
        }
    """,
    
    "title_label": """
        QLabel {
            color: #2c3e50;
            padding: 10px;
        }
    """,
    
    "group_box": """
        QGroupBox {
            font-weight: bold;
            border: 2px solid #bdc3c7;
            border-radius: 10px;
            margin-top: 15px;
            padding-top: 15px;
            font-size: 14px;
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            left: 15px;
            padding: 0 10px;
            color: #2c3e50;
        }
    """,
    
    "convert_btn": """
        QPushButton {
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 8px 20px;
            font-weight: bold;
            font-size: 12px;
        }
        QPushButton:hover {
            background-color: #2980b9;
        }
        QPushButton:pressed {
            background-color: #1c5980;
        }
    """,
    
    "clear_btn": """
        QPushButton {
            background-color: #e74c3c;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 8px 20px;
            font-weight: bold;
            font-size: 12px;
        }
        QPushButton:hover {
            background-color: #c0392b;
        }
        QPushButton:pressed {
            background-color: #922b21;
        }
    """,
    
    "input_field": """
        QLineEdit {
            border: 2px solid #bdc3c7;
            border-radius: 5px;
            padding: 8px;
            font-size: 12px;
            background-color: white;
        }
        QLineEdit:focus {
            border: 2px solid #3498db;
        }
    """,
    
    "result_field": """
        QLineEdit {
            background-color: #ecf0f1;
            border: 2px solid #bdc3c7;
            border-radius: 5px;
            padding: 8px;
            font-size: 14px;
            font-weight: bold;
            color: #2c3e50;
        }
    """,
    
    "combo_box": """
        QComboBox {
            border: 2px solid #bdc3c7;
            border-radius: 5px;
            padding: 6px;
            font-size: 11px;
            background-color: white;
            min-width: 150px;
        }
        QComboBox:focus {
            border: 2px solid #3498db;
        }
        QComboBox::drop-down {
            border: none;
            width: 20px;
        }
        QComboBox::down-arrow {
            image: none;
            border-left: 5px solid transparent;
            border-right: 5px solid transparent;
            border-top: 8px solid #7f8c8d;
            margin-right: 5px;
        }
    """,
    
    "label": """
        QLabel {
            font-size: 11px;
            color: #34495e;
            font-weight: bold;
        }
    """,
    
    "menu_bar": """
        QMenuBar {
            background-color: #2c3e50;
            color: white;
            padding: 5px;
        }
        QMenuBar::item {
            padding: 5px 15px;
            background: transparent;
        }
        QMenuBar::item:selected {
            background-color: #3498db;
        }
        QMenu {
            background-color: white;
            border: 1px solid #bdc3c7;
        }
        QMenu::item {
            padding: 8px 25px;
        }
        QMenu::item:selected {
            background-color: #3498db;
            color: white;
        }
    """
}