from app.data.json_handler import UnitsJSONHandler

class UnitConverter:
    def __init__(self):
        self.json_handler = UnitsJSONHandler()
    
    def get_categories(self):
        return self.json_handler.get_categories()
    
    def get_units(self, category):
        return self.json_handler.get_units(category)
    
    def convert(self, category, value, from_unit, to_unit):
        return self.json_handler.convert(category, value, from_unit, to_unit)
    
    def reload_data(self):
        self.json_handler.reload()
    
    def get_json_handler(self):
        return self.json_handler