
class Property:
    type = ""

    def is_filtered(self, condition, object):
        # TODO
        pass

class Text(Property):
    value = ""

    def is_filtered(self, condition, object):
        # TODO
        return super().is_filtered(condition, object)

class Number(Property):
    value = 0

    def is_filtered(self, condition, object):
        # TODO
        return super().is_filtered(condition, object)

class Checkbox(Property):
    value = False

    def is_filtered(self, condition, object):
        # TODO
        return super().is_filtered(condition, object)