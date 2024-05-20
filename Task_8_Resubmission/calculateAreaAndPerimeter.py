class Circle:
    # Private class variable
    __pi = 3.141

    def __init__(self, radii):
        # Initialize with a list of radii
        self.radii = radii

    @classmethod
    def area(cls, radius):
        # Calculate the area of a circle given its radius
        return cls.__pi * (radius ** 2)

    @classmethod
    def perimeter(cls, radius):
        # Calculate the perimeter (circumference) of a circle given its radius
        return 2 * cls.__pi * radius

    def calculate_areas(self):
        # Calculate areas for all radii in the list
        return [self.area(radius) for radius in self.radii]

    def calculate_perimeters(self):
        # Calculate perimeters for all radii in the list
        return [self.perimeter(radius) for radius in self.radii]


radii_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radii_list)

areas = circle.calculate_areas()
perimeters = circle.calculate_perimeters()

print("Radii:", radii_list)
print("Areas:", areas)
print("Perimeters:", perimeters)