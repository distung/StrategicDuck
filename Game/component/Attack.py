class Attack(object):
    """Attack"""
    def __init__(self, fightStats, rng):
        self.fightStats = fightStats
        self.range = rng
        self.aoe = 0

    def do_action(target):
        for entity in target:
            entity.components[FightStats].life -= fightStats.physicalDamage