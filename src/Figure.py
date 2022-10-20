class Figure:

    def __init__(self):
        self.name = Figure

    def add_area(self, figure):

        if isinstance(figure, Figure):
            return self.area + figure.area
        
        else:
            raise ValueError("It's not a figure!")
