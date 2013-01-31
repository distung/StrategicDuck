class Entity(object):
    """base entity class"""
    def __init___(self, components = none):
        if components:
            self.components = components
        else:
            self.components = {}

    def addComponent(self, name, component):
        self.components[name] = component