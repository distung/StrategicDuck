class TurnSystem(object):
    """description of class"""

    def __init__(self, entities={}):
        self.entities = entities
        self.counter = Counter(entities.iterkeys)

    def get_active_component(self):
        while(self.counter.most_common(1)[0][1] < 100):
            for k, v in entities.iteritems():
                self.counter[k] += v
        active = self.counter.most_common(1)[0][0]
        self.counter[active] = 0
        return active
           

    


