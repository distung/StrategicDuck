class Grid(object):
    """description of class"""

    def __init___(self, x, y):
        self.nil = NilEntity()
        self.map= defaultdict(self.nil)
        for i in xrange( x ):
            for j in xrange( y ):
                self.map[ (i,j) ] = self.nil

    def set_position(self, entity, x, y):
       self.map[(entity.components["position"].x,entity.components["position"].y)].remove(entity)
       self.map[(x,y)].append(entity)

    def get_all_range(self, x, y, rng):
        entities = []
        for i in xrange(x - rng, x + rng):
            for j in xrange(y - rng, y + rng):
                entity = self.map[(i,j)]
                if entity is not self.nil:
                    entities.add(entity)

