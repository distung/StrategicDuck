class Entity(object):
    """Base entity class"""
    def __init___(self, components = none):
        if components:
            self.components = components
        else:
            self.components = {}