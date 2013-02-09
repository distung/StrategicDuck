class turn_system(object):
    """description of class"""

    def __init__(self, components={}):
        self.components = components
        self.counter = Counter(components.iterkeys)

    def get_active_component(self):
        while(self.counter.most_common(1)[0][1] < 100):
            for k, v in components.iteritems():
                self.counter[k] += v
        active = self.counter.most_common(1)[0][0]
        self.counter[active] = 0
        return active
           

    


