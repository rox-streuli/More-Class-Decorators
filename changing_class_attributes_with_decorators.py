def object_counter(class_):  # this line defines a decorating function that
    # accepts one parameter 'class_' (note the underscore)
    class_.__getattr__orig = class_.__getattribute__
    # the decorator makes a copy of the reference to the
    # __getattribute__ special method. This method is responsible
    # for returning the attribute values. The reference to this
    # original method will be used in a modified method.

    def new_getattr(self, name):
        # a definition of the method playing the role of the new
        # __getattribute__ method starts here. This method accepts
        # an attribute name – it’s a string.
        if name == 'mileage':
            # in case some code asks for the 'mileage' attribute, the next
            # line will be executed.
            print('We noticed that the mileage attribute was read')
            #  a simple alert is issued;
        return class_.__getattr__orig(self, name)  # the original method
        # __getattribute__ referenced by class_.__getattr__orig is called.
        # This ends the 'new_getattr' function definition.

    class_.__getattribute__ = new_getattr  # now the 'new_getattr' is defined,
    # so it can now be referenced as the new '__getattribute__'
    # method by a decorated class.
    return class_   # every well behaved and developed decorator should
    # return the decorated object – in our case it is a decorated class.


@object_counter
class Car:
    def __init__(self, vin):
        self.mileage = 0
        self.vin = vin


car = Car('ABC123')
print('The mileage is', car.mileage)
print('The VIN is', car.vin)


# output without the decorator...
# lass Car:
#     def __init__(self, vin):
#         self.mileage = 0
#         self.vin = vin
#
# The mileage is 0
# The VIN is ABC123

# output with decorator...
# We noticed that the mileage attribute was read
# The mileage is 0
# The VIN is ABC123

# Another example:
# def decorator_function(target):
#
#     def decorator_init(self):
#         print("Decorator running")
#
#     target.__init__ = decorator_init
#     return target
#
#
# @decorator_function
# class Target:
#     def __init__(self):
#         print("Target running")
#
#
# Target()

# Decorator running
