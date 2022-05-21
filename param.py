
class Parameter:
    def __init__(self, title : str, unit : str) -> None:
        self._title = title
        self._unit = unit

    def title(self, t = None):
        if t != None:
            self._title = t
        return self._title

    def unit(self, t = None):
        if t != None:
            self._unit = t
        return self._unit
# TODO: implement filter


parms = {
    'cognitive load': Parameter('cognative load', 'interval'),
    'amount of sleep': Parameter('amount of sleep', 'double'),
    'water consumption': Parameter('water consumption', 'double'),
    'physical activity': Parameter('physical activity', 'integer'),
    'time socilizing': Parameter('time socilizing', 'integer'),
}

lparms = [
    Parameter('cognative load', 'interval'),
    Parameter('amount of sleep', 'double'),
    Parameter('water consumption', 'double'),
    Parameter('physical activity', 'integer'),
    Parameter('time socilizing', 'integer'),
]