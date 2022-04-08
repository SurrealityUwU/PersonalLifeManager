
class Property:
    property_type = ""

    def __init__(self, value):
        self.value = value

    def is_filtered(self, condition, object):
        # TODO
        pass

class Text(Property):
    value = ""
    property_type = "Text"

    def is_filtered(self, condition, object):
        # TODO
        return super().is_filtered(condition, object)

class Number(Property):
    value = 0
    property_type = "Number"

    def is_filtered(self, condition, object):
        # TODO
        return super().is_filtered(condition, object)

class Checkbox(Property):
    value = False
    property_type = "Checkbox"

    def is_filtered(self, condition, object):
        # TODO
        return super().is_filtered(condition, object)