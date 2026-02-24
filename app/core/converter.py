class UnitConverter:
    @staticmethod
    def convert_length(value, from_unit, to_unit):
        to_meters = {
            'Миллиметры (мм)': 0.001,
            'Сантиметры (см)': 0.01,
            'Дециметры (дм)': 0.1,
            'Метры (м)': 1,
            'Километры (км)': 1000
        }
        meters = value * to_meters[from_unit]
        return meters / to_meters[to_unit]

    @staticmethod
    def convert_mass(value, from_unit, to_unit):
        to_grams = {
            'Граммы (г)': 1,
            'Килограммы (кг)': 1000,
            'Центнеры (ц)': 100000,
            'Тонны (т)': 1000000
        }
        grams = value * to_grams[from_unit]
        return grams / to_grams[to_unit]

    @staticmethod
    def convert_time(value, from_unit, to_unit):
        to_seconds = {
            'Секунды (с)': 1,
            'Минуты (мин)': 60,
            'Часы (ч)': 3600,
            'Дни (сут)': 86400
        }
        seconds = value * to_seconds[from_unit]
        return seconds / to_seconds[to_unit]

    @staticmethod
    def calculate(category, value, from_unit, to_unit):
        try:
            if category == 'Длина':
                return UnitConverter.convert_length(value, from_unit, to_unit)
            elif category == 'Масса':
                return UnitConverter.convert_mass(value, from_unit, to_unit)
            elif category == 'Время':
                return UnitConverter.convert_time(value, from_unit, to_unit)
            else:
                return None
        except Exception:
            return None