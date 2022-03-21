
class Parameter:
    def __init__(self, title : str, unit : str) -> None:
        self._title = title
        self._unit = unit

    def title(self, t = None):
        if t != None:
            self._title = t
        return self._title
# TODO: implement filter

parms = [
    Parameter('cognative load', 'interval'),
    Parameter('amount of sleep', 'double'),
    Parameter('water consumption', 'double'),
    Parameter('physical activity', 'integer'),
    Parameter('time socilizing', 'integer'),
]