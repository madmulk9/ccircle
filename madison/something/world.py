class World:
    def __init__(self):
        self.objects = []

    def add(self, obj):
        self.objects.append(obj)

    def draw(self, window):
        window.drawRect(0, 0, 800, 400, 0.3, 0.5, 1.0)
        window.drawRect(0, 400, 800, 200, 0.2, 0.5, 0.1)
        for obj in self.objects:
            obj.draw(window)

    def update(self):
        for obj in self.objects:
            obj.update()
        # TODO: World updater
        pass