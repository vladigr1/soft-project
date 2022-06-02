
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
# implement filter in config

lparms = [
    Parameter('cognitive load', '[-5, 5]'),
    Parameter('amount of sleep', 'double'),
    Parameter('water consumption', 'double'),
    Parameter('physical activity', 'integer'),
    Parameter('time socializing', 'integer'),
]

parms = {
    'cognitive load': lparms[0],
    'amount of sleep': lparms[1],
    'water consumption': lparms[2],
    'physical activity': lparms[3],
    'time socilizing': lparms[4],
}