class Planet:  # Creation: "class" keyword and a name, starting with capital letter and a colon.


                # Define different attributes and different methods associated with this class.
                # Every object based on this class has those properties and methods.
                # To create attributes for class we need to define an init function.

    shape = "round"


# Class level Attributes: go to outside of the init function
# All planets are round, so you define it as class level attribute.
# It is not going to be unique for every instance
# Accessing to this attribute: instances and class can access.

    def __init__(self, name, radius, gravity, system):
                    # Initialization function: sets up the attribute
                    # It runs when we create new instance of this class (like constructor method).
                    # self parameter:
                        # Whenever a new instance is created, self param makes run this function.
                        # Refers to the instance of the object we create
                        # We use the class when making new objects
                        # We attach below attributes to self parameter and then to new instances.

        self.name = name # Instance Attributes
        self.radius = radius
        self.gravity = gravity
        self.system = system
                    # meaning they unique to instance
                    # dot notation: attaches attributes to instance


    def orbit(self): # Instance Methods
        return f"{self.name} is orbiting in the {self.system}"
            # We attach methods to instances, meaning they unique to instance.
            # When we call this function it is accessible by variables & instances.
            # When we create a new instance it inherits these properties.


    @classmethod
    def common(cls):
        return f"All planets are {cls.shape} because of gravity."

                # Class level methods, use decorator in the beginning
                # this method will be common


    @staticmethod
    def spin(speed="2000 miles per hour"):
        return f"The planet spins and spins a {speed}."


# now we can create a new instance of this object & class.
hoth = Planet("Hoth", 200000, 5.5, "Hoth System")
# hoth---> this is just a variable name,
# Planet -->new instance&object of this class
# ()--> to say we're invoking a new instance of this class
# bu şekil yazıldığında we run the function of def __init__(self)
# passing in this self this instance we're creating and -->
# attaching these different attributes defined by init function
# so now all these different attributes will be accesible on tihs "hoth" variable
# Madem hoth variable ile class attributelarına self parameter ile ulaşabiliyorum,
# self dışında başka parametrelerde yazarım, onalara da ulaşırım.

# below prints 3 different properties of hoth variable which they all have-->
# because we create a new instance of Planet class and attach them


naboo = Planet("Naboo", 300000, 8, "Naboo System")  # new instance of this class.
# that object as well as is going to have exactly the same property values
# multiple objects, but in essence all the same

# overall sum: we create a class with init function
# this init function takes in the instance that we're trying to create, this new object called "self".
# and it is attaching properties or attributes to that object.


# print(f"Name is:{naboo.name}")
# print(f"Radius is:{naboo.radius}")
# print(f"The gravity is: {naboo.gravity}")

print(Planet.shape)
# print(naboo.shape)
# print(Planet.common())
# print(naboo.common())
# print(naboo.orbit())# orbit method is used by instances.
# print(Planet.orbit())#orbit is instance method, it cannot access instance method on the class itself
# print(Planet.spin())# static method can be used on the class itself
# print(hoth.spin())#instances may use static method.
# print(Planet.spin("a very high speed"))# argument overwrites the default argument
