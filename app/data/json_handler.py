import json
from pathlib import Path

class UnitsJSONHandler:
    _instance = None
    
    def __new__(cls, json_file='units.json'):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self, json_file='units.json'):
        if self._initialized:
            return
        
        self._initialized = True
        base_dir = Path(__file__).parent.parent.parent
        self.json_file = base_dir / json_file
        self.data = {}
        self.load()
    
    def load(self):
        try:
            if self.json_file.exists():
                with open(self.json_file, 'r', encoding='utf-8') as f:
                    self.data = json.load(f)
            else:
                self.data = self._get_default_data()
                self.save()
        except json.JSONDecodeError as e:
            print(f"Ошибка чтения JSON: {e}")
            self.data = self._get_default_data()
        except Exception as e:
            print(f"Ошибка загрузки: {e}")
            self.data = self._get_default_data()
    
    def save(self):
        try:
            with open(self.json_file, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Ошибка сохранения: {e}")
    
    def _get_default_data(self):
        return {
            "длина": {
                "метр": 1,
                "километр": 1000,
                "сантиметр": 0.01,
                "миллиметр": 0.001,
                "дециметр": 0.1
            },
            "вес": {
                "килограмм": 1,
                "грамм": 0.001,
                "тонна": 1000,
                "центнер": 100
            },
            "время": {
                "секунда": 1,
                "минута": 60,
                "час": 3600,
                "сутки": 86400
            }
        }
    
    def get_categories(self):
        return list(self.data.keys())
    
    def get_units(self, category):
        if category in self.data:
            return list(self.data[category].keys())
        return []
    
    def get_conversion_factor(self, category, unit):
        if category in self.data and unit in self.data[category]:
            return self.data[category][unit]
        return None
    
    def convert(self, category, value, from_unit, to_unit):
        if category not in self.data:
            return None
        
        from_factor = self.get_conversion_factor(category, from_unit)
        to_factor = self.get_conversion_factor(category, to_unit)
        
        if from_factor is None or to_factor is None:
            return None
        
        base_value = value * from_factor
        result = base_value / to_factor
        return result
    
    def reload(self):
        self.load()