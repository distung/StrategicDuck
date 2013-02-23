class MovementSystem(object):
    """description of class"""
    def __init__(self, grid, movables={}):
        self.grid = grid
        self.movables=movables

    def move_entity(entity, x, y):
        grid.set_position(entity, position)
        entity.components["position"] = Position(x, y)

    def get_movable_positions(entity):
        grid.get_objects_in_bbox(entity.components["position"])