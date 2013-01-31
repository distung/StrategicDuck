class Hero(object):
    """The hero we need, not the hero we deserve"""
    def __init___(self, components = none):
        if components:
            self.components = components
        else:
            self.components = {}

    def addComponent(self, name, component):
        self.components[name] = component