class ActionSystem(object):
    """ActionSystem"""
    def __init__(self, grid, entities={}):
        self.grid = grid
        self.entities = entities

    def do_action(self, entity, action, x, y):
        aoe = entity.components[action].aoe
        target = grid.get_all_in_range(x, y, aoe)
        #target will be a list of 0 or more
        action.do_action(target)