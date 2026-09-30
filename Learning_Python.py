import streamlit as st
import pandas as pd

st.set_page_config(layout="centered")

if "chapter" not in st.session_state:
    st.session_state.chapter = 0
if "course" not in st.session_state:
    st.session_state.course = None
if "answered" not in st.session_state:
    st.session_state.answered = False

if st.session_state.chapter == 0:
    st.title("Welcome to Python learning guide")

    st.subheader("Here you can choose the learning path to Python")

    st.markdown("What course would you like to try?")

    if "course" not in st.session_state:
        st.session_state.course = None

    if st.button("OOP - Object-Oriented Programming"):
        st.session_state.course = "OOP"
        st.session_state.chapter = 1

    if st.button("SQL - Structured Query Language"):
        st.session_state.course = "SQL"
        st.session_state.chapter = 36

    if st.button("API - Application Programming Interface"):
        st.session_state.course = "API"

    if st.session_state.course == "API":
        st.subheader("Sorry for the inconvenience, API course is coming soon.")

    if st.session_state.course == "SQL":
        st.subheader("Here is the SQL couse for you")

    if st.session_state.course == "OOP":
        st.subheader("Here is the OOP couse for you")

if st.session_state.chapter == 1:
    st.title("OOP (Object-Oriented Programming) learning guide")

st.markdown("""<style>
body {background-color: #0b0f19;}
.chapter-label {color: #facc15; letter-spacing: 3px; font-weight: 700; font-size: 13px;}
.chapter-title {font-size: 46px; font-weight: 800; margin-bottom: 5px;}
.chapter-subtitle {color: #94a3b8; font-style: italic; font-size: 18px; margin-bottom: 30px;}
.section-title {color: #60a5fa; font-size: 26px; margin-top: 35px; margin-bottom: 10px;}
.tip-box {background-color: #0f2a24; border-left: 4px solid #34d399; padding: 15px; border-radius: 6px; margin-top: 20px;}
</style>""", unsafe_allow_html=True)


if "chapter" not in st.session_state:
    st.session_state.chapter = 1
    st.session_state.answered = False
if "correct" not in st.session_state:
    st.session_state.correct = False
if "selected" not in st.session_state:
    st.session_state.selected = None

def chapter(number, title, subtitle):
    st.markdown(f"""<div class="chapter-label">CHAPTER {number}</div> <div class="chapter-title">{title}</div> <div class="chapter-subtitle">{subtitle}</div> """, unsafe_allow_html=True)

if st.session_state.chapter == 1:
    chapter(
        1,
        "What is OOP?",
        "The big idea behind Object-Oriented Programming")

    st.markdown("""
                Imagine you're building a game. You need to track 50 different characters, each with a name, health,
                and attack power. Without OOP, you'd write **hundreds of variables** and functions tangled together.

                OOP lets you describe a *template* for a character once, then create as many as you want.

                OOP is a way of structuring your code around **objects** — bundles that hold both *data* (attributes)
                and *behaviour* (methods) in one place.""")

    st.markdown('<div class="section-title">The 4 Pillars of OOP</div>', unsafe_allow_html=True)

    st.markdown("""
                - **Encapsulation** — bundling data and methods, hiding internal details  
                - **Inheritance** — a class can inherit features from another class  
                - **Polymorphism** — different objects can respond to the same method differently  
                - **Abstraction** — hiding complexity, showing only what's necessary""")

    st.markdown("""<div class="tip-box">
                💡 You don't need to memorise these now. By the end of this course you'll understand them through hands-on examples.
                </div>""", unsafe_allow_html=True)

    st.markdown("")

    code1 = """
    # Even a number is an object!
    x = 42
    print(type(x))       # <class 'int'>
    print(x.bit_length()) # 6  — a method on an int!"""

    st.code(code1, language="python")

    st.markdown("### 🧠 Quick Check")
    st.markdown("**What is an object in OOP?**")

    options = [
        "Only a variable that stores numbers",
        "A bundle of data (attributes) and behaviour (methods)",
        "A type of loop in Python",
        "A file on your computer"]

    correct_answer = options[1]

    for option in options:
        if st.button(option, use_container_width=True, key=f"ch1{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Exactly! An object combines both data and behaviour in one unit.")
            if st.button("Next", key="ch1_next"):
                st.session_state.chapter = 2
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")

if st.session_state.chapter == 2:
    chapter(2,
    "Classes & Objects",
    "Blueprint vs. the thing itself")

    st.markdown("""A class is the blueprint. An object is what you build from it. Think of a class as a cookie cutter, and objects as the cookies.""")

    code2 = """
    class Dog:
        pass  # empty class for now

    # Creating objects (instances)
    my_dog = Dog()
    your_dog = Dog()

    print(type(my_dog))  # <class '__main__.Dog'>"""

    st.code(code2, language="python")

    st.markdown(" Each object is **independent**. Changing one doesn't affect the other.")

    st.markdown("""<div class="section-title">The __init__ method</div>""", unsafe_allow_html=True)

    st.markdown(" __init__ is a special method called automatically when you create an object. It's where you set up initial attributes.")

    code3 = """
    class Dog:
        def __init__(self, name, breed):
            self.name = name     # instance attribute
            self.breed = breed

    buddy = Dog("Buddy", "Labrador")
    rex   = Dog("Rex",   "German Shepherd")

    print(buddy.name)   # Buddy
    print(rex.breed)    # German Shepherd"""

    st.code(code3, language="python")

    st.markdown("""<div class="tip-box">
                💡 What is self? It's a reference to the specific object being created or used. When you call buddy.name, Python automatically passes buddy as self behind the scenes. You must always put self as the first parameter in any instance method. </div>""", unsafe_allow_html=True)

    st.markdown("### 🧠 Quick Check")
    st.markdown("**What does __init__ do?**")

    options = [
        "It deletes an object from memory",
        "It's called automatically when creating an object, to set up its initial state",
        "It's a required function you must call manually before using a class",
        "It defines the class name"]

    correct_answer = options[1]

    for option in options:
        if st.button(option, use_container_width=True, key=f"ch2{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Correct! __init__ is the initialiser — Python calls it for you when you do Dog().")
            if st.button("Next", key="ch2_next"):
                st.session_state.chapter = 3
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")

if st.session_state.chapter == 3:
    chapter(3,
            "Methods",
            "Giving your objects behaviour")
    
    st.markdown("Methods are just functions defined inside a class. They give your objects things they can do.")

    code4 = """
    class Dog:
        def __init__(self, name, breed):
            self.name  = name
            self.breed = breed
            self.tricks = []

        def bark(self):
            print(f"{self.name} says: Woof!")

        def learn_trick(self, trick):
            self.tricks.append(trick)
            print(f"{self.name} learned {trick}!")

        def show_tricks(self):
            if self.tricks:
                print(f"{self.name} can: {', '.join(self.tricks)}")
            else:
                print(f"{self.name} knows no tricks yet.")

    buddy = Dog("Buddy", "Labrador")
    buddy.bark()                 # Buddy says: Woof!
    buddy.learn_trick("sit")    # Buddy learned sit!
    buddy.learn_trick("roll over")
    buddy.show_tricks()          # Buddy can: sit, roll over"""

    st.code(code4, language="python")

    st.markdown("""<div class="section-title">Instance vs Class attributes</div>""", unsafe_allow_html=True)

    code5 = """
    class Dog:
        species = "Canis lupus familiaris"  # class attribute — shared by ALL dogs

        def __init__(self, name):
            self.name = name  # instance attribute — unique to each dog

    buddy = Dog("Buddy")
    rex   = Dog("Rex")

    print(buddy.species)   # Canis lupus familiaris
    print(rex.species)     # Canis lupus familiaris (same)
    print(buddy.name)      # Buddy
    print(rex.name)        # Rex (different)"""

    st.code(code5, language="python")

    st.markdown("""<div class="tip-box">
                💡  Class attributes are like facts about the type. Instance attributes are facts about a specific individual. </div>""", unsafe_allow_html=True)
    
    st.markdown("### 🧠 Quick Check")
    st.markdown("**If two Dog objects share a class attribute species, what happens if you change species on one instance?**")

    options = [
        "It changes for all Dog objects globally",
        "It creates a new instance attribute on that object only, shadowing the class attribute",
        "It raises an error",
        "It changes the class attribute permanently"]
    
    correct_answer = options[1]

    for option in options:
        if st.button(option, use_container_width=True, key=f"ch3{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Correct! Right! Setting an attribute on an instance creates a new instance-level attribute that shadows the class one — only that object is affected.")
            if st.button("Next", key="ch3_next"):
                st.session_state.chapter = 4
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")

if st.session_state.chapter == 4:
    chapter(4,
        "Encapsulation",
        "Keeping internals private — the first pillar")
    
    st.markdown("Encapsulation means hiding the internal details of an object and only exposing what's needed. It protects your data from accidental misuse.")
    
    st.markdown("""<div class="section-title">In Python, we use naming conventions to signal privacy:</div>""", unsafe_allow_html=True)
    
    st.markdown("""
                ***name*** — public, anyone can access it\n
                ***_name*** — "protected" by convention (a hint to developers)\n
                ***__name*** — "private" — Python name-mangles it to make it harder to access from outside""")
    
    code6 = """
    class BankAccount:
        def __init__(self, owner, balance):
            self.owner = owner
            self.__balance = balance  # private!

        def deposit(self, amount):
            if amount > 0:
                self.__balance += amount

        def withdraw(self, amount):
            if 0 < amount <= self.__balance:
                self.__balance -= amount
            else:
                print("Insufficient funds!")

        def get_balance(self):  # controlled access
            return self.__balance

    acc = BankAccount("Alice", 1000)
    acc.deposit(500)
    print(acc.get_balance())  # 1500

    # acc.__balance  ← This would raise AttributeError!"""

    st.code(code6, language="python")

    st.markdown("""<div class="section-title">Properties — the Pythonic way</div>""", unsafe_allow_html=True)

    st.markdown("Python's @property decorator lets you use *method calls that look like attribute access*. This is the clean, Pythonic approach to getters/setters.")

    code7 = """
    class Circle:
        def __init__(self, radius):
            self.__radius = radius

        @property
        def radius(self):
            return self.__radius

        @radius.setter
        def radius(self, value):
            if value < 0:
                raise ValueError("Radius can't be negative")
            self.__radius = value

    c = Circle(5)
    print(c.radius)   # 5  — looks like attribute access!
    c.radius = 10     # setter is called automatically"""

    st.code(code7, language="python")

    st.markdown("### 🧠 Quick Check")
    st.markdown("**What is the purpose of encapsulation?**")

    options = [
        "To make code run faster",
        "To hide internal implementation details and control access to data",
        "To allow one class to use another class's methods",
        "To create multiple objects from one class"]
    
    correct_answer = options[1]

    for option in options:
        if st.button(option, use_container_width=True, key=f"ch4{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Exactly! Encapsulation protects data and controls how it's accessed or modified.")
            if st.button("Next", key="ch4_next"):
                st.session_state.chapter = 5
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")

if st.session_state.chapter == 5:
    chapter(5, 
        "Inheritance",
        "Building on what already exists — the second pillar")
    
    st.markdown("Inheritance lets a class **reuse and extend** the attributes and methods of another class. The parent is called the ***base class*** or ***superclass***; the child is the ***subclass***.")

    code8 = """
    class Animal:  # Base class
        def __init__(self, name, sound):
            self.name  = name
            self.sound = sound

        def speak(self):
            print(f"{self.name} says {self.sound}")

    class Dog(Animal):  # Inherits from Animal
        def __init__(self, name):
            super().__init__(name, "Woof")  # call parent's __init__
            self.tricks = []

        def fetch(self):
            print(f"{self.name} fetches the ball!")

    class Cat(Animal):
        def __init__(self, name):
            super().__init__(name, "Meow")

    buddy = Dog("Buddy")
    whiskers = Cat("Whiskers")

    buddy.speak()     # Buddy says Woof  (inherited!)
    whiskers.speak()  # Whiskers says Meow
    buddy.fetch()     # Buddy fetches the ball!"""

    st.code(code8, language="python")

    st.markdown("""<div class="tip-box">
                💡 super() gives you access to the parent class. Use it to call the parent's __init__ or any other method you want to extend rather than replace. </div>""", unsafe_allow_html=True)
    
    st.markdown("""<div class="section-title">isinstance() — checking the family tree</div>""", unsafe_allow_html=True)

    code9 = """
        print(isinstance(buddy, Dog))     # True
        print(isinstance(buddy, Animal))  # True — Dog IS-A Animal
        print(isinstance(buddy, Cat))     # False"""
    
    st.code(code9, language="python")

    st.markdown("### 🧠 Quick Check")
    st.markdown("**What does super().__init__(...) do?**")

    options = [
        "Creates a new parent class",
        "Calls the parent class's __init__ so you don't have to duplicate that setup code",
        "Deletes the parent class",
        "Makes the class abstract"]
    
    correct_answer = options[1]

    for option in options:
        if st.button(option, use_container_width=True, key=f"ch5{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Correct! super() lets you delegate to the parent, so you build on top of it rather than rewriting everything.")
            if st.button("Next", key="ch5_next"):
                st.session_state.chapter = 6
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")

if st.session_state.chapter == 6:
    chapter(6,
        "Polymorphism",
        "Same interface, different behaviour — the third pillar")
    
    st.markdown("Polymorphism means 'many forms'. In OOP, it means you can call the ***same method name*** on different objects and each responds in its own way.")

    code10 = """
    class Shape:
        def area(self):
            raise NotImplementedError

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius
        def area(self):
            return 3.14159 * self.radius ** 2

    class Rectangle(Shape):
        def __init__(self, w, h):
            self.w, self.h = w, h
        def area(self):
            return self.w * self.h

    class Triangle(Shape):
        def __init__(self, base, height):
            self.base, self.height = base, height
        def area(self):
            return 0.5 * self.base * self.height

    # Polymorphism in action!
    shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]
    for shape in shapes:
        print(f"{type(shape).__name__}: area = {shape.area():.2f}")
    # Circle: area = 78.54
    # Rectangle: area = 24.00
    # Triangle: area = 12.00"""

    st.code(code10, language="python")

    st.markdown("The loop doesn't care **which** shape it has — it just calls .area() and each object handles it correctly. This is the power of polymorphism.")

    st.markdown("""<div class="tip-box">
                💡 This is also called "method overriding" — the child class overrides the parent's version of a method. </div>""", unsafe_allow_html=True)
    
    st.markdown("""<div class="section-title">Duck Typing</div>""", unsafe_allow_html=True)

    st.markdown("Python doesn't require a shared parent class for polymorphism. If it walks like a duck and quacks like a duck, it's a duck. As long as an object has the right method, Python is happy.")

    st.markdown("### 🧠 Quick Check")
    st.markdown("**Which best describes polymorphism?**")

    options = [
        "When one class inherits from multiple parents",
        "When many objects can respond to the same method name, each in their own way",
        "When a class has many attributes",
        "When you hide data with double underscores"]
    
    correct_answer = options[1]
    
    for option in options:
        if st.button(option, use_container_width=True, key=f"ch6{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Spot on! Polymorphism == same interface, different implementations.")
            if st.button("Next", key="ch6_next"):
                st.session_state.chapter = 7
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")
    
if st.session_state.chapter == 7:
    chapter(7,
        "Abstraction",
        "Hiding complexity — the fourth pillar")
    
    st.markdown("""Abstraction means exposing ***only what's necessary*** and hiding the implementation details. You use something without needing to know how it works inside.
                Python provides Abstract Base Classes (ABCs) via the abc module to enforce that subclasses implement certain methods.""")
    
    code11 = """
    from abc import ABC, abstractmethod

    class Vehicle(ABC):  # Abstract class — can't be instantiated
        def __init__(self, make, model):
            self.make  = make
            self.model = model

        @abstractmethod
        def start_engine(self):  # Subclasses MUST implement this
            pass

        def info(self):           # Concrete method — shared by all
            print(f"{self.make} {self.model}")

    class Car(Vehicle):
        def start_engine(self):
            print("Car engine: Vroom!")

    class ElectricCar(Vehicle):
        def start_engine(self):
            print("Electric motor: Whirr...")

    # Vehicle()  ← TypeError! Can't instantiate abstract class
    my_car = Car("Toyota", "Corolla")
    my_car.info()          # Toyota Corolla
    my_car.start_engine()  # Car engine: Vroom!"""

    st.code(code11, language="python")

    st.markdown("""Abstraction is about designing ***interfaces***. You say "all Vehicles must have a start_engine method" without specifying how each one does it.""")

    st.markdown("""<div class="tip-box">
                ⚠️ If a subclass doesn't implement ALL abstract methods, Python will raise a TypeError when you try to create an object from it. This enforces the "contract". </div>""", unsafe_allow_html=True)
    
    st.markdown("### 🧠 Quick Check")
    st.markdown("**What happens if you try to create an instance of an Abstract Base Class directly?**")

    options = [
        "It creates an empty object with no attributes",
        "Python raises a TypeError",
        "It works fine — abstract is just a label",
        "It raises an ImportError"]
    
    correct_answer = options[1]

    for option in options:
        if st.button(option, use_container_width=True, key=f"ch7{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Correct! ABCs can't be instantiated. They're templates that force subclasses to implement certain methods.")
            if st.button("Next", key="ch7_next"):
                st.session_state.chapter = 8
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")

if st.session_state.chapter == 8:
    chapter(8,
        "Dunder Methods",
        "Magic methods that make your objects feel native")
    
    st.markdown("Dunder (double-underscore) methods let your objects work with Python's built-in syntax — +, len(), print(), comparison operators, and more.")

    code12 = """
    class Vector:
        def __init__(self, x, y):
            self.x, self.y = x, y

        def __repr__(self):              # for developers / print()
            return f"Vector({self.x}, {self.y})"

        def __str__(self):               # for end users / str()
            return f"({self.x}, {self.y})"

        def __add__(self, other):        # v1 + v2
            return Vector(self.x + other.x, self.y + other.y)

        def __len__(self):               # len(v)
            return int((self.x**2 + self.y**2) ** 0.5)

        def __eq__(self, other):          # v1 == v2
            return self.x == other.x and self.y == other.y

    v1 = Vector(3, 4)
    v2 = Vector(1, 2)

    print(v1)          # (3, 4)          — uses __str__
    print(v1 + v2)     # (4, 6)          — uses __add__
    print(len(v1))      # 5               — uses __len__
    print(v1 == v2)    # False           — uses __eq__"""

    st.code(code12, language="python")

    st.markdown("""<div class="section-title">Common dunder methods</div>""", unsafe_allow_html=True)

    code13 = """
    # Representation
    __repr__   # repr(obj), used in REPL
    __str__    # str(obj), print(obj)

    # Math operators
    __add__    # obj + other
    __sub__    # obj - other
    __mul__    # obj * other

    # Comparisons
    __eq__     # obj == other
    __lt__     # obj < other

    # Container protocol
    __len__    # len(obj)
    __getitem__ # obj[key]
    __contains__ # x in obj

    # Context managers
    __enter__, __exit__  # with obj as x:"""

    st.code(code13, language="python")

    st.markdown("### 🧠 Quick Check")
    st.markdown("**Which dunder method lets you use + between two of your objects?**")

    options = [
        "__plus__",
        "__add__",
        "__sum__",
        "__combine__"]
    
    correct_answer = options[1]

    for option in options:
        if st.button(option, use_container_width=True, key=f"ch8{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Correct! __add__ is called when Python evaluates obj1 + obj2.")
            if st.button("Next", key="ch8_next"):
                st.session_state.chapter = 9
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")

if st.session_state.chapter == 9:
    chapter(9,
        "Composition",
        "Building complex objects from simpler ones",)
    
    st.markdown("""Inheritance says "is-a". Composition says "has-a". Instead of inheriting behaviour, you ***include other objects as attributes***. This is often more flexible.""")

    st.markdown("""<div class="tip-box">
                💡Rule of thumb: prefer composition over inheritance when the relationship isn't a clear "is-a" type.""", unsafe_allow_html=True)
    
    st.markdown("")

    code14 = """
    class Engine:
        def __init__(self, horsepower):
            self.horsepower = horsepower
        def start(self):
            print(f"Engine ({self.horsepower}hp) started")

    class GPS:
        def navigate(self, destination):
            print(f"Navigating to {destination}")

    class Car:
        def __init__(self, make):
            self.make   = make
            self.engine = Engine(300)  # Car HAS-A Engine
            self.gps    = GPS()         # Car HAS-A GPS

        def drive(self, destination):
            self.engine.start()
            self.gps.navigate(destination)

    my_car = Car("BMW")
    my_car.drive("Berlin")
    # Engine (300hp) started
    # Navigating to Berlin"""

    st.code(code14, language="python")

    st.markdown("Now Engine and GPS can be reused in other classes (Boat, Plane...) without duplicating code, and without forcing an awkward inheritance hierarchy.")

    st.markdown("""<div class="section-title">Inheritance vs Composition</div>""", unsafe_allow_html=True)

    code15 = """
    # Use Inheritance when:  "A Dog IS-A Animal"
    class Dog(Animal): ...

    # Use Composition when: "A Car HAS-A Engine"
    class Car:
        engine = Engine()"""
    
    st.code(code15, language="python")

    st.markdown("### 🧠 Quick Check")
    st.markdown("**When should you prefer composition over inheritance?**")

    options = [
        "Always — inheritance is never useful",
        "When the relationship is 'has-a' rather than 'is-a'",
        "When you need to override methods",
        "When using abstract classes"]
    
    correct_answer = options[1]

    for option in options:
        if st.button(option, use_container_width=True, key=f"ch9{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Right! 'has-a' relationships are best modelled with composition. It's also easier to swap out components later.")
            if st.button("Next", key="ch9_next"):
                st.session_state.chapter = 10
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")

if st.session_state.chapter == 10:
    chapter(10,
        "Putting It All Together",
        "A complete OOP project example")
    
    st.markdown("Let's build a small RPG system that uses every concept we've learned.")

    code16 = """
    from abc import ABC, abstractmethod
    import random

    # Abstraction — defines the contract
    class Character(ABC):
        def __init__(self, name, hp):
            self.name  = name
            self.__hp  = hp     # Encapsulation
            self.max_hp = hp

        @property
        def hp(self): return self.__hp

        def take_damage(self, dmg):
            self.__hp = max(0, self.__hp - dmg)
            print(f"  {self.name} takes {dmg} dmg → {self.__hp}/{self.max_hp} HP")

        @abstractmethod
        def attack(self, target): pass

        def is_alive(self): return self.__hp > 0

        def __repr__(self):  # Dunder method
            return f"{self.name} ({self.hp}/{self.max_hp} HP)"

    # Composition — Warrior has a Weapon
    class Weapon:
        def __init__(self, name, dmg):
            self.name, self.dmg = name, dmg

    # Inheritance — Warrior IS-A Character
    class Warrior(Character):
        def __init__(self, name):
            super().__init__(name, hp=100)
            self.weapon = Weapon("Sword", 25)

        def attack(self, target):  # Polymorphism
            dmg = random.randint(15, self.weapon.dmg)
            print(f"{self.name} swings {self.weapon.name}!")
            target.take_damage(dmg)

    class Mage(Character):
        def __init__(self, name):
            super().__init__(name, hp=70)
            self.mana = 100

        def attack(self, target):  # Polymorphism
            dmg = random.randint(20, 40)
            print(f"{self.name} casts Fireball!")
            target.take_damage(dmg)

    # Battle!
    hero    = Warrior("Arthur")
    villain = Mage("Morgana")
    print(hero, "vs", villain)

    while hero.is_alive() and villain.is_alive():
        hero.attack(villain)
        if villain.is_alive():
            villain.attack(hero)"""
    
    st.code(code16, language="python")

    st.markdown("""<div class="tip-box">
                🎉 You've reached the end! Try extending this: add a Healer class, a Shield item, or an experience/level system. That's where real learning happens. 🎉""", unsafe_allow_html=True)
    
    st.markdown("""<div class="section-title">What you've learned</div>""", unsafe_allow_html=True)

    st.markdown("""
                ***Classes & Objects*** — blueprints and instances\n
                ***__init__ & self*** — setting up state\n
                ***Methods*** — behaviour on objects\n
                ***Encapsulation*** — private attributes, properties\n
                ***Inheritance*** — reusing and extending with super()\n
                ***Polymorphism*** — same interface, different behaviour\n
                ***Abstraction*** — ABCs and enforced contracts\n
                ***Dunder methods*** — making objects feel native\n
                ***Composition*** — has-a vs is-a""")
    
    st.markdown("### 🧠 Quick Check")
    st.markdown("**In the RPG example, the Warrior 'has-a' Weapon and 'is-a' Character. Which pattern is each?**")

    options = [
        "Both are inheritance",
        "Weapon = inheritance, Character = composition",
        "Weapon = composition, Character = inheritance",
        "Both are composition"]
    
    correct_answer = options[2]

    for option in options:
        if st.button(option, use_container_width=True, key=f"ch10{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Exactly! Warrior IS-A Character (inheritance) and Warrior HAS-A Weapon (composition). You combined both patterns.")
            if st.button("Next", key="ch10_next"):
                st.session_state.chapter = 11
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")

if st.session_state.chapter == 11:
    chapter(
        11,
        "Congratulations!",
        "You have finished this Python OOP mini interactive course. Now it is your turn.")
    
    st.markdown("Try to make something *yours* using everything that you have learned so far.")

    st.markdown("""<div class="tip-box">
                🎉I am going to show you a game I made so you can play but try to do something similar or different to show off your skills.""", unsafe_allow_html=True)
    
    st.markdown("""<div class="section-title">Python mini game</div>""", unsafe_allow_html=True)

    code17 = """
    import pygame
    import random
    import sys

    pygame.init()

    WIDTH, HEIGHT = 600, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dodge the Enemies")

    clock = pygame.time.Clock()

    class Player:
        def __init__(self):
            self.rect = pygame.Rect(300, 500, 50, 50)
            self.speed = 6
            self.color = (0, 255, 0)

        def move(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.rect.x > 0:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT] and self.rect.x < WIDTH - 50:
                self.rect.x += self.speed

        def draw(self):
            pygame.draw.rect(screen, self.color, self.rect)

    # ---------------- ENEMY ----------------
    class Enemy:
        def __init__(self):
            x = random.randint(0, WIDTH - 40)
            self.rect = pygame.Rect(x, 0, 40, 40)
            self.speed = random.randint(3, 7)
            self.color = (255, 0, 0)

        def move(self):
            self.rect.y += self.speed

        def draw(self):
            pygame.draw.rect(screen, self.color, self.rect)

    # ---------------- GAME ----------------
    class Game:
        def __init__(self):
            self.player = Player()
            self.enemies = []
            self.spawn_timer = 0
            self.running = True

        def spawn_enemy(self):
            self.enemies.append(Enemy())

        def check_collision(self):
            for enemy in self.enemies:
                if self.player.rect.colliderect(enemy.rect):
                    print("GAME OVER")
                    self.running = False

        def update(self):
            self.player.move()

            for enemy in self.enemies:
                enemy.move()

            self.check_collision()

            # Spawn enemies over time
            self.spawn_timer += 1
            if self.spawn_timer > 30:
                self.spawn_enemy()
                self.spawn_timer = 0

        def draw(self):
            screen.fill((0, 0, 0))
            self.player.draw()

            for enemy in self.enemies:
                enemy.draw()

            pygame.display.update()

        def run(self):
            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                self.update()
                self.draw()
                clock.tick(60)
    # Start game
    game = Game()
    game.run()"""
    
    st.code(code17, language="python")

    st.markdown("""<div class="section-title">Don't stop learning and enjoy.</div>""", unsafe_allow_html=True)

    st.markdown("""<div class="tip-box">
                🧠 Do you want to get tasks to practice?""", unsafe_allow_html=True)
    
    st.markdown("")
    
    if st.button("Yes", key="ch12_next"):
        st.session_state.chapter = 12
    elif st.button("No", key="ch11_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 12:
    chapter(12, 
            "Great—here's the first task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the result.")
    
    st.markdown("""<div class="section-title">💡 Task 1: """, unsafe_allow_html=True)

    st.markdown("""
                In book.py,  create a Book class with these attributes set in __init__:\n
                ● title, author, isbn (string, e.g. "978-0-06-112008-4")\n
                ● is_available — a boolean, starts as True\n
                Add these methods:\n
                ● checkout() — sets is_available = False. Print a message if already checked out.\n
                ● return_book() — sets is_available = True\n
                ● __str__ — returns something like: "The Hobbit by J.R.R. Tolkien [AVAILABLE]"\n
                ● __repr__ — returns Book(isbn='...')""")
       
    st.markdown("""<div class="tip-box">
                ⚠️ Hint: Use a ternary in __str__: "[AVAILABLE]" if self.is_available else "[CHECKED OUT]""", unsafe_allow_html=True)
    
    st.markdown("")

    if st.button("Next", key="ch13_next"):
        st.session_state.chapter = 13
if st.session_state.chapter == 13:
    code18 = """
    class Book:
        def __init__(self, title, author, isbn):
            self.title = title
            self.author = author
            self.isbn = isbn
            self.is_available = True

        def checkout(self):
            if not self.is_available:
                print("This book is already checked out.")
            else:
                self.is_available = False

        def return_book(self):
            self.is_available = True

        def __str__(self):
            status = "[AVAILABLE]" if self.is_available else "[CHECKED OUT]"
            return f"{self.title} by {self.author} {status}"

        def __repr__(self):
            return f"Book(isbn='{self.isbn}')"
    """
    st.code(code18, language="python")

    st.markdown("""<div class="section-title">🧠 Did you manage to finish it? Ready for the next one?</div>""", unsafe_allow_html=True)

    if st.button("Yes", key="ch14_next"):
        st.session_state.chapter = 14
    elif st.button("No", key="ch14_NO_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 14:
    chapter(13,
            "Great—here's the next task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the result.")
    
    st.markdown("""<div class="section-title">💡 Task 2: """, unsafe_allow_html=True)

    st.markdown("""
                In member.py, create a Member class:\n
                ● Attributes: name, member_id, borrowed_books (empty list)\n
                ● Class attribute: MAX_BOOKS = 3 — the most a member can borrow at once\n
                ● Method can_borrow() — returns True if they haven't hit the limit\n
                ● Method borrow(book) — appends to borrowed_books if allowed\n
                ● Method return_book(book) — removes it from borrowed_books\n
                ● __str__ — e.g. "Alice (ID: M001) — 2 books borrowed""")
    
    st.markdown("""<div class="tip-box">
                ⚠️ Hint: Use len(self.borrowed_books) < self.MAX_BOOKS to check the limit.""", unsafe_allow_html=True)
    
    st.markdown("")
    
    if st.button("Next", key="ch15_next"):
        st.session_state.chapter = 15

if st.session_state.chapter == 15:
    code19 = """
    class Member:
        MAX_BOOKS = 3

        def __init__(self, name, member_id):
            self.name = name
            self.member_id = member_id
            self.borrowed_books = []

        def can_borrow(self):
            return len(self.borrowed_books) < self.MAX_BOOKS

        def borrow(self, book):
            if not self.can_borrow():
                print("Borrowing limit reached.")
                return       
            self.borrowed_books.append(book)

        def return_book(self, book):
            if book in self.borrowed_books:
                self.borrowed_books.remove(book)
        def __str__(self):
            return f"{self.name} (ID: {self.member_id}) — {len(self.borrowed_books)} books borrowed"
    """
    st.code(code19, language="python")

    st.markdown("""<div class="section-title">🧠 Did you manage to finish it? Ready for the next one?</div>""", unsafe_allow_html=True)

    if st.button("Yes", key="ch16_next"):
        st.session_state.chapter = 16
    elif st.button("No", key="ch16_NO_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 16:
    chapter(14,
            "Great—here's the next task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the result.")
      
    st.markdown("""<div class="section-title">💡 Task 3: """, unsafe_allow_html=True)

    st.markdown("""
                ● In loan.py, create a Loan class. This represents one borrowing event.\n
                ● Attributes: book (a Book object), member (a Member object), loan_date, due_date, returned (bool, starts False)\n
                ● Use Python's datetime module: from datetime import date, timedelta\n
                ● Set loan_date = date.today() and due_date = date.today() + timedelta(days=14)\n
                ● Method complete_return() — marks returned = True\n
                ● Method is_overdue() — returns True if not returned and past due date\n
                ● Method days_overdue() — returns how many days overdue (0 if not overdue)\n
                ● __str__ — something informative about the loan""")
     
    st.markdown("""<div class="tip-box">
                ⚠️ Hint: Keep in mind—datetime, composition and instance methods""", unsafe_allow_html=True)
    
    st.markdown("")
    
    if st.button("Next", key="ch15_next"):
        st.session_state.chapter = 17

if st.session_state.chapter == 17:
    code20 = """
    from datetime import date, timedelta

    class Loan:
        def __init__(self, book, member):
            self.book = book
            self.member = member
            self.loan_date = date.today()
            self.due_date = self.loan_date + timedelta(days=14)
            self.returned = False

        def complete_return(self):
            self.returned = True

        def is_overdue(self):
            return not self.returned and date.today() > self.due_date

        def days_overdue(self):
            if self.is_overdue():
                return (date.today() - self.due_date).days
            return 0

        def __str__(self):
            status = "Returned" if self.returned else "Active"
            overdue_info = ""
        
            if self.is_overdue():
                overdue_info = f" — Overdue by {self.days_overdue()} days"
        
            return (
                f"Loan: '{self.book.title}' to {self.member.name} | "
                f"Loaned: {self.loan_date} | Due: {self.due_date} | "
                f"Status: {status}{overdue_info}")
    """
    st.code(code20, language="python")

    st.markdown("""<div class="section-title">🧠 Did you manage to finish it? Ready for the next one?</div>""", unsafe_allow_html=True)

    if st.button("Yes", key="ch18_next"):
        st.session_state.chapter = 18
    elif st.button("No", key="ch18_NO_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 18:
    chapter(15,
            "Great—here's the next task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the result.")
    
    st.markdown("""<div class="section-title">💡 Task 4: """, unsafe_allow_html=True)

    st.markdown("""
                Go back to member.py and make member_id private (__member_id).\n
                ● Then add a @property so it can still be read from outside but not set directly.\n
                ● Accessing member.member_id should still work (returns the value)\n
                ● Trying member.member_id = "NEW" should raise an AttributeError (no setter)\n
                Also add a fine attribute (float, starts at 0.0) with a property. The setter should reject negative values:""")
    
    st.markdown("""<div class="tip-box">
                ⚠️ Hint:""", unsafe_allow_html=True)
    
    st.markdown("")

    code21 = """
    @fine.setter
    def fine(self, value):
        if value < 0:
            raise ValueError("Fine cannot be negative")
        self.__fine = value"""
    
    st.code(code21, language="python")

    if st.button("Next", key="ch19_next"):
        st.session_state.chapter = 19

if st.session_state.chapter == 19:
    code22 = """
    class Member:
        MAX_BOOKS = 3

        def __init__(self, name, member_id):
            self.name = name
            self.__member_id = member_id  # private
            self.borrowed_books = []
            self.__fine = 0.0  # private fine

        @property
        def member_id(self):
            return self.__member_id

        def can_borrow(self):
            return len(self.borrowed_books) < self.MAX_BOOKS

        def borrow(self, book):
            if not self.can_borrow():
                print("Borrowing limit reached.")
                return
            self.borrowed_books.append(book)

        def return_book(self, book):
            if book in self.borrowed_books:
                self.borrowed_books.remove(book)

        @property
        def fine(self):
            return self.__fine

        @fine.setter
        def fine(self, value):
            if value < 0:
                raise ValueError("Fine cannot be negative")
            self.__fine = value

        def __str__(self):
            return f"{self.name} (ID: {self.member_id}) — {len(self.borrowed_books)} books borrowed"
    """
    st.code(code22, language="python")

    st.markdown("""<div class="section-title">🧠 Did you manage to finish it? Ready for the next one?.</div>""", unsafe_allow_html=True)

    if st.button("Yes", key="ch20_next"):
        st.session_state.chapter = 20
    elif st.button("No", key="ch20_NO_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 20:
    chapter(16,
            "Great—here's the next task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the result.")
    
    st.markdown("""<div class="section-title">💡 Task 5: """, unsafe_allow_html=True)

    st.markdown("""
                In book.py, add an EBook class that inherits from Book:\n
                ● Extra attribute: file_size_mb (float) and format (e.g. "PDF", "EPUB")\n
                ● EBooks are always available — override checkout() to never change availability (print "EBooks can be borrowed by multiple members")\n
                ● Override __str__ to include format info\n""")
    
    st.markdown("")

    if st.button("Next", key="ch21_next"):
        st.session_state.chapter = 21

if st.session_state.chapter == 21:
    code23 = """
    class EBook(Book):
        def __init__(self, title, author, isbn, file_size_mb, format):
            super().__init__(title, author, isbn)
            self.file_size_mb = file_size_mb
            self.format = format

        def checkout(self):
            print("EBooks can be borrowed by multiple members")

        def __str__(self):
            status = "[AVAILABLE]"  # always available
            return (
                f"{self.title} by {self.author} "
                f"({self.format}, {self.file_size_mb}MB) {status}"
            )
    """
    st.code(code23, language="python")

    st.markdown("""<div class="section-title">🧠 Did you manage to finish it? Ready for the next one?</div>""", unsafe_allow_html=True)

    if st.button("Yes", key="ch22_next"):
        st.session_state.chapter = 22
    elif st.button("No", key="ch22_NO_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 22:
    chapter(17,
            "Great—here's the next task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the result.")
    
    st.markdown("""<div class="section-title">💡 Task 6: """, unsafe_allow_html=True)

    st.markdown("""
                In member.py, add a PremiumMember that inherits from Member:\n
                ● Premium members can borrow up to 10 books (override MAX_BOOKS)\n
                ● Premium members get a 50% fine discount — override a method apply_fine(days) that adds days * 0.10 instead of days * 0.20\n
                ● Call super().__init__() properly""")

    st.markdown("""<div class="tip-box">
                ⚠️ Hint:To override a class attribute in a subclass, just redefine it: MAX_BOOKS = 10 inside the PremiumMember class body.""", unsafe_allow_html=True)
    
    st.markdown("")

    if st.button("Next", key="ch23_next"):
        st.session_state.chapter = 23

if st.session_state.chapter == 23:
    code24 = """
    class PremiumMember(Member):
        MAX_BOOKS = 10

        def __init__(self, name, member_id):
            super().__init__(name, member_id)

        def apply_fine(self, days):
            self.fine += days * 0.10"""
    
    st.code(code24, language="python")

    st.markdown("""<div class="section-title">🧠 Did you manage to finish it? Ready for the next one?</div>""", unsafe_allow_html=True)

    if st.button("Yes", key="ch24_next"):
        st.session_state.chapter = 24
    elif st.button("No", key="ch24_NO_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 24:
    chapter(17,
            "Great—here's the next task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the result.")
    
    st.markdown("""<div class="section-title">💡 Task 7: """, unsafe_allow_html=True)

    st.markdown("""
                In library.py, create the main Library class. This is your system orchestrator — it has books, members, and loans (composition).\n
                ● Attributes: name, books (list), members (list), loans (list)\n
                ● add_book(book) — adds a Book or EBook to the library\n
                ● register_member(member) — adds a member\n
                ● checkout_book(isbn, member_id) — finds the book and member, creates a Loan, calls book.checkout() and member.borrow(book)\n
                ● return_book(isbn, member_id) — finds the active loan, calculates any fine, calls loan.complete_return()\n
                ● search_by_title(query) — returns a list of books whose title contains the query (case-insensitive)\n
                ● available_books() — returns all books where is_available == True\n
                ● member_report(member_id) — prints a summary of a member's loans and fines""")
    
    st.markdown("""<div class="tip-box">
                ⚠️ Hint: For checkout_book, use a helper to find by isbn: next((b for b in self.books if b.isbn == isbn), None)""", unsafe_allow_html=True)
    
    st.markdown("")

    if st.button("Next", key="ch25_next"):
        st.session_state.chapter = 25

if st.session_state.chapter == 25:
    code25 = """
    from datetime import date
    from book import Book, EBook
    from member import Member, PremiumMember
    from loan import Loan

    class Library:
        def __init__(self, name):
            self.name = name
            self.books = []
            self.members = []
            self.loans = []

        def add_book(self, book):
            if isinstance(book, (Book, EBook)):
                self.books.append(book)
            else:
                print("Can only add Book or EBook instances")

        def register_member(self, member):
            if isinstance(member, Member):
                self.members.append(member)
            else:
                print("Can only register Member instances")

        def checkout_book(self, isbn, member_id):
            book = next((b for b in self.books if b.isbn == isbn), None)
            if not book:
                print(f"No book with ISBN {isbn}")
                return

            member = next((m for m in self.members if m.member_id == member_id), None)
            if not member:
                print(f"No member with ID {member_id}")
                return

            if isinstance(book, Book) and not isinstance(book, EBook) and not book.is_available:
                print(f"Book '{book.title}' is already checked out.")
                return

            if not member.can_borrow():
                print(f"{member.name} has reached borrowing limit.")
                return

            book.checkout()
            member.borrow(book)
            loan = Loan(book, member)
            self.loans.append(loan)
            print(f"{member.name} checked out '{book.title}' successfully.")

        def return_book(self, isbn, member_id):
            loan = next(
                (l for l in self.loans if l.book.isbn == isbn 
                and l.member.member_id == member_id and not l.returned),
                None)

            if not loan:
                print("No active loan found for this book and member.")
                return

            overdue_days = loan.days_overdue()
            if overdue_days > 0:
                loan.member.apply_fine(overdue_days)
                print(f"Overdue by {overdue_days} days. Fine applied to {loan.member.name}.")

            loan.complete_return()
            if isinstance(loan.book, Book) and not isinstance(loan.book, EBook):
                loan.book.return_book()
            loan.member.return_book(loan.book)
            print(f"'{loan.book.title}' returned successfully by {loan.member.name}.")

        def search_by_title(self, query):
            query_lower = query.lower()
            return [b for b in self.books if query_lower in b.title.lower()]

        def available_books(self):
            return [b for b in self.books if isinstance(b, EBook) or b.is_available]

        def member_report(self, member_id):
            member = next((m for m in self.members if m.member_id == member_id), None)
            if not member:
                print(f"No member with ID {member_id}")
                return

            member_loans = [l for l in self.loans if l.member.member_id == member_id]
            print(f"--- Report for {member.name} (ID: {member.member_id}) ---")
            print(f"Fine: ${member.fine:.2f}")
            if not member_loans:
                print("No loans.")
                return
            for loan in member_loans:
                status = "Returned" if loan.returned else "Active"
                overdue_days = loan.days_overdue()
                overdue_text = f", Overdue by {overdue_days} days" if overdue_days else ""
                print(f"{loan.book.title} | Loaned: {loan.loan_date} | Due: {loan.due_date} | Status: {status}{overdue_text}")"""
    
    st.code(code25, language="python")

    st.markdown("""<div class="section-title">🧠 Did you manage to finish it? Ready for the next one?</div>""", unsafe_allow_html=True)

    if st.button("Yes", key="ch26_next"):
        st.session_state.chapter = 26
    elif st.button("No", key="ch26_NO_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 26:
    chapter(18,
            "Great—here's the next task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the result.")
    
    st.markdown("""<div class="section-title">💡 Task 8: """, unsafe_allow_html=True)

    st.markdown("""
                Refactor book.py to use an Abstract Base Class:\n
                ● Create an abstract LibraryItem class (import ABC and abstractmethod)\n
                ● It should have abstract methods: checkout() and get_info()\n
                ● Make Book and EBook both inherit from LibraryItem\n
                ● Each implements get_info() differently — Book returns physical details, EBook returns digital details""")
    
    st.markdown("""<div class="tip-box">
                ⚠️ Hint: Try passing a Book and an EBook to the same function. Python doesn't care which type it is — as long as it has get_info(), it works. That's polymorphism.""", unsafe_allow_html=True)
    
    st.markdown("")

    if st.button("Next", key="ch27_next"):
        st.session_state.chapter = 27

if st.session_state.chapter == 27:
    code26 = """
    from abc import ABC, abstractmethod

    class LibraryItem(ABC):
        def __init__(self, title, author, isbn):
            self.title = title
            self.author = author
            self.isbn = isbn

        @abstractmethod
        def checkout(self):
            pass

        @abstractmethod
        def get_info(self):
            pass


    class Book(LibraryItem):
        def __init__(self, title, author, isbn):
            super().__init__(title, author, isbn)
            self.is_available = True

        def checkout(self):
            if not self.is_available:
                print("This book is already checked out.")
            else:
                self.is_available = False

        def return_book(self):
            self.is_available = True

        def get_info(self):
            status = "AVAILABLE" if self.is_available else "CHECKED OUT"
            return f"{self.title} by {self.author} [Physical, {status}]"

        def __str__(self):
            return self.get_info()

        def __repr__(self):
            return f"Book(isbn='{self.isbn}')"


    class EBook(LibraryItem):
        def __init__(self, title, author, isbn, file_size_mb, format):
            super().__init__(title, author, isbn)
            self.file_size_mb = file_size_mb
            self.format = format

        def checkout(self):
            print("EBooks can be borrowed by multiple members")

        def get_info(self):
            return f"{self.title} by {self.author} [Digital, {self.format}, {self.file_size_mb}MB]"

        def __str__(self):
            return self.get_info()"""
    
    st.code(code26, language="python")

    st.markdown("""<div class="section-title">🧠 Did you manage to finish it? Ready for the next one?</div>""", unsafe_allow_html=True)

    if st.button("Yes", key="ch28_next"):
        st.session_state.chapter = 28
    elif st.button("No", key="ch28_NO_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 28:
    chapter(19,
            "Great—here's the next task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the result.")
    
    st.markdown("""<div class="section-title">💡 Task 9: """, unsafe_allow_html=True)

    st.markdown("In library.py, add a method print_catalogue() that loops through all items and calls item.get_info() — demonstrating polymorphism:")

    st.markdown("""<div class="tip-box">
                ⚠️ Hint: """, unsafe_allow_html=True)
    
    st.markdown("")
    
    code27 = """
    def print_catalogue(self):
        for item in self.books:
            print(item.get_info())"""
    
    st.code(code27, language="python")

    st.markdown("")

    if st.button("Next", key="ch27_next"):
        st.session_state.chapter = 29

if st.session_state.chapter == 29:
    code28 = """
    class Library:
        def __init__(self, name):
            self.name = name
            self.books = []    
            self.members = []
            self.loans = []
    ...        

        def print_catalogue(self):
            print(f"--- Catalogue of {self.name} ---")
            for item in self.books:
                print(item.get_info())"""
    
    st.code(code28, language="python")

    st.markdown("""<div class="section-title">🧠 Did you manage to finish it? Ready for the next one?</div>""", unsafe_allow_html=True)

    if st.button("Yes", key="ch3_next"):
        st.session_state.chapter = 30
    elif st.button("No", key="ch3_NO_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 30:
    chapter(20,
            "Great—here's the next task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the result.")
    
    st.markdown("""<div class="section-title">💡 Task 10: """, unsafe_allow_html=True)

    st.markdown("""
                Make your objects feel native in Python by adding dunder methods:\n
                ● On Library: add __len__ (returns number of books), __contains__ (so you can do book in library), and __iter__ (so you can loop over a library with for book in library)\n
                ● On Book: add __eq__ (two books are equal if they have the same isbn) and __lt__ (compare by title alphabetically, so you can sort() a list of books)\n
                ● On Member: add __eq__ (same member_id means same member)
                Test it in main.py:""")
    
    st.markdown("""<div class="tip-box">
                ⚠️ Hint: """, unsafe_allow_html=True)
    
    st.markdown("")
    
    code29 = """
    print(len(library))          # number of books
    print(hobbit in library)     # True
    books = sorted(library.books) # uses __lt__
    for book in library:           # uses __iter__
        print(book)"""
    
    st.code(code29, language="python")

    st.markdown("")

    if st.button("Next", key="ch31_next"):
        st.session_state.chapter = 31

if st.session_state.chapter == 31:
    st.markdown("""<div class="section-title">📘 book.py — add __eq__ and __lt__""", unsafe_allow_html=True)

    code30 = """
    from abc import ABC, abstractmethod

    class LibraryItem(ABC):
        def __init__(self, title, author, isbn):
            self.title = title
            self.author = author
            self.isbn = isbn

        @abstractmethod
        def checkout(self):
            pass

        @abstractmethod
        def get_info(self):
            pass

        def __eq__(self, other):
            if isinstance(other, LibraryItem):
                return self.isbn == other.isbn
            return False

        def __lt__(self, other):
            if isinstance(other, LibraryItem):
                return self.title < other.title
            return NotImplemented

    class Book(LibraryItem):
        def __init__(self, title, author, isbn):
            super().__init__(title, author, isbn)
            self.is_available = True

        def checkout(self):
            if not self.is_available:
                print("This book is already checked out.")
            else:
                self.is_available = False

        def return_book(self):
            self.is_available = True

        def get_info(self):
            status = "AVAILABLE" if self.is_available else "CHECKED OUT"
            return f"{self.title} by {self.author} [Physical, {status}]"

        def __str__(self):
            return self.get_info()

        def __repr__(self):
            return f"Book(isbn='{self.isbn}')"

    class EBook(LibraryItem):
        def __init__(self, title, author, isbn, file_size_mb, format):
            super().__init__(title, author, isbn)
            self.file_size_mb = file_size_mb
            self.format = format

        def checkout(self):
            print("EBooks can be borrowed by multiple members")

        def get_info(self):
            return f"{self.title} by {self.author} [Digital, {self.format}, {self.file_size_mb}MB]"

        def __str__(self):
            return self.get_info()"""
    
    st.code(code30, language="python")

    st.markdown("")

    if st.button("Next result", key="ch32_next"):
        st.session_state.chapter = 32

if st.session_state.chapter == 32:
    st.markdown("""<div class="section-title">👤 member.py — add __eq__""", unsafe_allow_html=True)

    code31 = """
    class Member:
        MAX_BOOKS = 3

        def __init__(self, name, member_id):
            self.name = name
            self.__member_id = member_id
            self.borrowed_books = []
            self.__fine = 0.0

        @property
        def member_id(self):
            return self.__member_id

        @property
        def fine(self):
            return self.__fine

        @fine.setter
        def fine(self, value):
            if value < 0:
                raise ValueError("Fine cannot be negative")
            self.__fine = value

        def can_borrow(self):
            return len(self.borrowed_books) < self.MAX_BOOKS

        def borrow(self, book):
            if not self.can_borrow():
                print("Borrowing limit reached.")
                return
            self.borrowed_books.append(book)

        def return_book(self, book):
            if book in self.borrowed_books:
                self.borrowed_books.remove(book)

        def apply_fine(self, days):
            self.fine += days * 0.20

        def __str__(self):
            return f"{self.name} (ID: {self.member_id}) — {len(self.borrowed_books)} books borrowed"

        def __eq__(self, other):
            if isinstance(other, Member):
                return self.member_id == other.member_id
            return False


    class PremiumMember(Member):
        MAX_BOOKS = 10

        def __init__(self, name, member_id):
            super().__init__(name, member_id)

        def apply_fine(self, days):
            self.fine += days * 0.10"""
    
    st.code(code31, language="python")

    st.markdown("")

    if st.button("Next result", key="ch33_next"):
        st.session_state.chapter = 33

if st.session_state.chapter == 33:
    st.markdown("""<div class="section-title">📚 library.py — add __len__, __contains__, __iter__""", unsafe_allow_html=True)

    code32 = """
    class Library:
        def __init__(self, name):
            self.name = name
            self.books = []
            self.members = []
            self.loans = []

        def add_book(self, book):
            self.books.append(book)

        def register_member(self, member):
            self.members.append(member)

        def __len__(self):
            return len(self.books)

        def __contains__(self, item):
            return item in self.books

        def __iter__(self):
            return iter(self.books)"""
    
    st.code(code32, language="python")

    st.markdown("")

    if st.button("Next result", key="ch34_next"):
        st.session_state.chapter = 34

if st.session_state.chapter == 34:
    st.markdown("""<div class="section-title">📝 main.py — testing everything""", unsafe_allow_html=True)

    code33 = """
    from book import Book, EBook
    from member import Member, PremiumMember
    from library import Library

    library = Library("City Library")

    book1 = Book("The Hobbit", "J.R.R. Tolkien", "978-0-06-112008-4")
    book2 = Book("1984", "George Orwell", "978-0-452-28423-4")
    ebook1 = EBook("Python 101", "John Doe", "123", 5.2, "PDF")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(ebook1)

    print(len(library))  # 3

    print(book1 in library)  # True
    print(EBook("Python 101", "John Doe", "123", 5.2, "PDF") in library)  # True (same ISBN)


    for item in library:
        print(item)

    books_sorted = sorted(library.books)
    for b in books_sorted:
        print(b)

    alice1 = Member("Alice", "M001")
    alice2 = Member("Alice Smith", "M001")
    bob = PremiumMember("Bob", "P001")
    print(alice1 == alice2)  # True
    print(alice1 == bob)     # False"""

    st.code(code33, language="python")

    st.markdown("")

    if st.button("Finish", key="ch35_next"):
        st.session_state.chapter = 35

if st.session_state.chapter == 35:
    chapter(20,
            "Congratulations! 🎉",
            "🎉You have successfully finished OOP learning guide!🎉")
    
    st.markdown("""<div class="section-title">🎉You have finished this learning guide!🎉 I am proud of you!</div>""", unsafe_allow_html=True)
    
    st.markdown("""<div class="tip-box">
                ⚠️Don't forget to keep practicing on your own! Programming has many more skills for you to learn! I wish you the best of luck! 💡
                </div>""", unsafe_allow_html=True)

    st.markdown("")

    if st.button("🏠 Return to menu", key="oop_finish_home"):
        st.session_state.chapter = 0
        st.session_state.course = None

if st.session_state.chapter == 36:
    st.title("SQL (Structured Query Language) learning guide")

st.markdown("""<style>
    body {background-color: #0b0f19;}
    .chapter-label {color: #facc15; letter-spacing: 3px; font-weight: 700; font-size: 13px;}
    .chapter-title {font-size: 46px; font-weight: 800; margin-bottom: 5px;}
    .chapter-subtitle {color: #94a3b8; font-style: italic; font-size: 18px; margin-bottom: 30px;}
    .section-title {color: #60a5fa; font-size: 26px; margin-top: 35px; margin-bottom: 10px;}
    .tip-box {background-color: #0f2a24; border-left: 4px solid #34d399; padding: 15px; border-radius: 6px; margin-top: 20px;}
    </style>""", unsafe_allow_html=True)

if "chapter" not in st.session_state:
    st.session_state.chapter = 36
    st.session_state.answered = False
if "correct" not in st.session_state:
    st.session_state.correct = False
if "selected" not in st.session_state:
    st.session_state.selected = None

def chapter(number, title, subtitle):
    st.markdown(f"""<div class="chapter-label">CHAPTER {number}</div> <div class="chapter-title">{title}</div> <div class="chapter-subtitle">{subtitle}</div> """, unsafe_allow_html=True)

books = pd.DataFrame({
    "id": [1,2,3,4,5],
    "title": ["To Kill a Mockingbird", "1984", "The Great Gatsby", "Pride and Prejudice", "The Hobbit"],
    "author": ["Harper Lee", "George Orwell", "F. Scott Fitzgerald", "Jane Austen", "J.R.R. Tolkien"],
    "year": [1960, 1949, 1925, 1813, 1937],
    "rating": [4.8, 4.7, 4.4, 4.6, 4.9]})

summary = pd.DataFrame({
    "Total books": [len(books)],
    "Average rating": [books["rating"].mean()],
    "Newest book year": [books["year"].max()]})

members = pd.DataFrame({"id": [1,2,3], "name": ["Alice", "Bob", "Charlie"], "email": ["alice@hotmail.com", "bob@gmail.com", "charlie@email.com"]})

loans = pd.DataFrame({"id": [1,2,3], "book_id": [1,2,4], "member_id": [2,1,3], "loan_date": ["2026-03-01", "2025-12-03", "2025-03-05"], "returned": [0,0,1]})

result = loans.merge(books, left_on="book_id", right_on="id").merge(members, left_on="member_id", right_on="id")

result = result[["name", "title", "loan_date"]]
result.columns = ["member", "book", "loan_date"]

if st.session_state.chapter == 36:
    chapter(1,
        "What is SQL?",
        "The language that talks to databases")
    
    st.markdown(""" SQL — ***Structured Query Language*** — is how you communicate with a database. You use it to create tables, insert data, ask questions, update records, and delete things. It's been around since the 1970s and is still one of the most important skills in tech.
                Think of a database as a collection of ***spreadsheets*** (called tables), where each table has rows and columns. SQL is how you read and manipulate those tables.""")
    
    st.markdown('<div class="section-title">The three databases you can use</div>', unsafe_allow_html=True)

    st.markdown("""<div class="tip-box">
                ● SQLite — file-based, zero setup, built into Python</div>""", unsafe_allow_html=True)
    st.markdown("""<div class="tip-box">
                ● PostgreSQL — powerful, open source, used in production</div>""", unsafe_allow_html=True)
    st.markdown("""<div class="tip-box">
                ● MySQL — widely used, especially in web apps</div>\n""", unsafe_allow_html=True)
    
    st.markdown('<div class="section-title"></div>', unsafe_allow_html=True)
    
    st.markdown("""In VS Code you'll use ***SQLite*** for practice (no installation needed — Python has it built in). Everything you learn transfers directly to PostgreSQL and MySQL. """)

    st.markdown('<div class="section-title">Setting up in VS Code</div>', unsafe_allow_html=True)

    st.markdown("""Install the ***SQLite Viewer*** extension in VS Code (search "SQLite Viewer" by Florian Klampfer). Then create a file called practice.py and you're ready:""")

    code34 = """
        import sqlite3

        # Connect (creates the file if it doesn't exist)
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()

        # Run SQL here...
        cursor.execute("your SQL goes here")

        conn.commit()   # save changes
        conn.close()    # close connection"""

    st.code(code34, language="python")

    st.markdown("""<div class="tip-box">
                💡 After running your script, right-click library.db in VS Code and choose "Open with SQLite Viewer" to see your tables visually.</div>""", unsafe_allow_html=True)
    
    st.markdown("### 🧠 Quick Check")
    st.markdown("**What does SQL stand for??**")

    options = [
        "Simple Query Lookup",
        "Structured Query Language",
        "System Queue Logic",
        "Standard Query Link"]
    
    correct_answer = options[1]

    for option in options:
        if st.button(option, use_container_width=True, key=f"ch36{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Correct! SQL = Structured Query Language — it's how you talk to relational databases.")
            if st.button("Next", key="ch36_next"):
                st.session_state.chapter = 37
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")

if st.session_state.chapter == 37:
    chapter(2,
        "CREATE TABLE & Data Types",
        "Defining the shape of your data")
    
    st.markdown("""Before you can store data, you need to define a ***table*** — its name, columns, and what type of data each column holds.""")

    code35 = """
        CREATE TABLE books (
            id       INTEGER  PRIMARY KEY AUTOINCREMENT,
            title    TEXT     NOT NULL,
            author   TEXT     NOT NULL,
            year     INTEGER,
            pages    INTEGER,
            rating   REAL
        )"""

    st.code(code35, language="python")

    st.markdown('<div class="section-title">Key concepts here</div>', unsafe_allow_html=True)

    st.markdown("""
                ● ***PRIMARY KEY*** — a unique identifier for each row. No two rows can have the same id.\n
                ● ***AUTOINCREMENT*** — SQLite automatically assigns the next number (1, 2, 3…)\n
                ● ***NOT NULL*** — this column must always have a value""")
    
    st.markdown('<div class="section-title">The main data types</div>', unsafe_allow_html=True)

    code36 = """
        INTEGER   -- whole numbers: 1, 42, -7
        REAL      -- decimals: 4.5, 9.99  (called FLOAT/NUMERIC in others)
        TEXT      -- strings: 'hello'   (VARCHAR in PostgreSQL/MySQL)
        BLOB      -- raw binary data (images, files)
        NULL      -- the absence of a value

        -- PostgreSQL/MySQL also have:
        BOOLEAN   -- true/false
        DATE      -- 2024-03-15
        TIMESTAMP -- 2024-03-15 14:30:00"""

    st.code(code36, language="python")

    st.markdown('<div class="section-title">In Python</div>', unsafe_allow_html=True)

    code37 = '''
        import sqlite3
        = sqlite3.connect("library.db")
         = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                title   TEXT    NOT NULL,
                author  TEXT    NOT NULL,
                year    INTEGER,
                rating  REAL
            )
            """)

        conn.commit()
        conn.close()
        print("Table created!")'''

    st.code(code37, language="python")

    st.markdown("""<div class="tip-box">
                💡 IF NOT EXISTS prevents an error if the table already exists. Always use this when creating tables in scripts you'll run more than once.</div>""", unsafe_allow_html=True)
    
    st.markdown("### 🧠 Quick Check")
    st.markdown("**What does PRIMARY KEY do??**")

    options = [
        "Encrypts the column",
        "Makes the column required",
        "Ensures every row has a unique identifier",
        "Sets the default value to 1"]
    
    correct_answer = options[2]

    for option in options:
        if st.button(option, use_container_width=True, key=f"ch37{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Right! PRIMARY KEY uniquely identifies each row — no two rows can share the same value in that column.")
            if st.button("Next", key="ch37_next"):
                st.session_state.chapter = 38
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")

if st.session_state.chapter == 38:
    chapter(3,
        "INSERT — Adding Data",
        "Putting rows into your tables")
    
    st.markdown("INSERT INTO adds new rows to a table. You specify which columns you're filling and what values to put in them.")

    code38 = """
        -- Single row
        INSERT INTO books (title, author, year, rating)
        VALUES ('The Hobbit', 'J.R.R. Tolkien', 1937, 4.9);

        -- Multiple rows at once
        INSERT INTO books (title, author, year, rating)
        VALUES
            ('Dune', 'Frank Herbert', 1965, 4.8),
            ('1984', 'George Orwell', 1949, 4.7),
            ('Neuromancer', 'William Gibson', 1984, 4.3);"""
    
    st.code(code38, language="python")

    st.markdown("""<div class="tip-box">
                🔒 Never use f-strings to insert user data into SQL. It creates a SQL injection vulnerability — a serious security hole. Always use parameterised queries with ? placeholders:</div>""", unsafe_allow_html=True)
    
    st.markdown("")

    code39 = """
    import sqlite3
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # ✓ Safe — use ? placeholders, pass values as a tuple
    books = [
        ('The Hobbit',    'J.R.R. Tolkien', 1937, 4.9),
        ('Dune',          'Frank Herbert',   1965, 4.8),
        ('1984',          'George Orwell',   1949, 4.7),
        ('Neuromancer',   'William Gibson',  1984, 4.3),
        ('Fahrenheit 451','Ray Bradbury',    1953, 4.5),
    ]

    cursor.executemany(
        "INSERT INTO books (title, author, year, rating) VALUES (?, ?, ?, ?)",
        books
    )

    conn.commit()
    conn.close()
    print(f"Inserted {len(books)} books")"""

    st.code(code39, language="python")

    st.markdown("""<div class="tip-box">
            💡 executemany() inserts a whole list in one go. Much cleaner than calling execute() in a loop.</div>""", unsafe_allow_html=True)
    
    st.markdown("### 🧠 Quick Check")
    st.markdown("**Why should you use ? placeholders instead of f-strings in SQL queries??**")

    options = [
        "? is faster to type",
        "f-strings don't work in Python 3",
        "SQLite doesn't support f-strings",
        "It prevents SQL injection attacks"]
    
    correct_answer = options[3]
    
    for option in options:
        if st.button(option, use_container_width=True, key=f"ch38{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Exactly! SQL injection is a real attack where malicious input can manipulate your queries. Parameterised queries prevent this.")
            if st.button("Next", key="ch38_next"):
                st.session_state.chapter = 39
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")

if st.session_state.chapter == 39:
    chapter(4,
        "SELECT — Querying Data",
        "Reading rows from your tables")
    
    st.markdown("SELECT is the most important SQL statement. You'll use it constantly. It retrieves rows from a table.")

    code40 = """
    -- Get everything
    SELECT * FROM books;

    -- Get specific columns
    SELECT title, author FROM books;

    -- Filter with WHERE
    SELECT * FROM books
    WHERE year > 1960;

    -- Multiple conditions
    SELECT title, rating FROM books
    WHERE year > 1950 AND rating >= 4.5;

    -- Sort results
    SELECT * FROM books
    ORDER BY rating DESC;  -- ASC for ascending

    -- Limit how many rows come back
    SELECT * FROM books
    ORDER BY rating DESC
    LIMIT 3;"""

    st.code(code40, language="python")

    st.dataframe(books)

    st.markdown('<div class="section-title">Useful WHERE operators</div>', unsafe_allow_html=True)

    code41 = """
    WHERE year = 1984          -- exact match
    WHERE year != 1984         -- not equal
    WHERE year BETWEEN 1950 AND 1980
    WHERE author LIKE '%Orwell%'  -- % is wildcard (contains)
    WHERE author LIKE 'Frank%'   -- starts with Frank
    WHERE year IN (1937, 1965, 1984)
    WHERE rating IS NULL
    WHERE rating IS NOT NULL"""

    st.code(code41, language="python")

    st.markdown('<div class="section-title">Reading results in Python</div>', unsafe_allow_html=True)

    code42 = '''
    cursor.execute("SELECT title, author, rating FROM books ORDER BY rating DESC")

    rows = cursor.fetchall()   # list of tuples
    for row in rows:
        print(f"{row[0]} by {row[1]} — ★ {row[2]}")

    # Or fetch just one row:
    cursor.execute("SELECT * FROM books WHERE id = ?", (1,))
    book = cursor.fetchone()
    print(book)'''

    st.code(code42, language="python")

    st.markdown("### 🧠 Quick Check")
    st.markdown("**Which clause filters rows based on a condition??**")

    options = [
        "ORDER BY",
        "FILTER",
        "WHERE",
        "LIMIT"]
    
    correct_answer = options[2]

    for option in options:
        if st.button(option, use_container_width=True, key=f"ch39{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Correct! WHERE is how you filter. ORDER BY sorts, LIMIT caps the number of results.")
            if st.button("Next", key="ch39_next"):
                st.session_state.chapter = 40
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")

if st.session_state.chapter == 40:
    chapter(5,
        "UPDATE & DELETE",
        "Modifying and removing data")
    
    st.markdown("UPDATE changes existing rows. DELETE removes them. Both are powerful — and dangerous without a WHERE clause.")

    code43 = '''
    -- Update a specific row
    UPDATE books
    SET rating = 4.95
    WHERE title = 'The Hobbit';

    -- Update multiple columns
    UPDATE books
    SET rating = 4.6, year = 1950
    WHERE id = 3;

    -- Delete a specific row
    DELETE FROM books
    WHERE id = 4;

    -- Delete rows matching a condition
    DELETE FROM books
    WHERE rating < 4.0;'''

    st.code(code43, language="python")

    st.markdown("""<div class="tip-box">
            ⚠️ The golden rule: always test your WHERE clause with a SELECT first before running UPDATE or DELETE. UPDATE books SET rating = 0 without a WHERE clause will update every single row.</div>""", unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">In Python</div>', unsafe_allow_html=True)

    code44 = '''
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Update with parameterised query
    cursor.execute(
        "UPDATE books SET rating = ? WHERE title = ?",
        (4.95, "The Hobbit")
    )
    print(f"Rows changed: {cursor.rowcount}")  # tells you how many rows were affected

    # Delete
    cursor.execute("DELETE FROM books WHERE id = ?", (4,))

    conn.commit()
    conn.close()'''
    
    st.code(code44, language="python")

    st.markdown("""<div class="tip-box">
            💡 cursor.rowcount tells you how many rows were affected by your last UPDATE or DELETE. It's a great sanity check — if you expected to update 1 row and rowcount is 0, something's wrong with your WHERE clause.</div>""", unsafe_allow_html=True)
    
    st.markdown("### 🧠 Quick Check")
    st.markdown("**What happens if you run UPDATE books SET rating = 5 without a WHERE clause??**")

    options = [
        "It updates the first row only",
        "It updates every single row in the table",
        "It raises an error",
        "Nothing — UPDATE requires WHERE"]
    
    correct_answer = options[1]

    for option in options:
        if st.button(option, use_container_width=True, key=f"ch40{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Exactly — without WHERE, UPDATE affects every row. Always write your WHERE clause first!")
            if st.button("Next", key="ch41_next"):
                st.session_state.chapter = 41
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")

if st.session_state.chapter == 41:
    chapter(6,
        "Aggregate Functions",
        "COUNT, SUM, AVG, MIN, MAX")
    
    st.markdown("""Aggregate functions compute a single result from a set of rows. They're how you answer questions like "how many books do we have?" or "what's the average rating?""")

    code45 = """
    -- How many books?
    SELECT COUNT(*) FROM books;              -- 5

    -- Average rating
    SELECT AVG(rating) FROM books;          -- 4.64

    -- Highest and lowest rated
    SELECT MAX(rating), MIN(rating) FROM books;

    -- Oldest book year
    SELECT MIN(year) FROM books;

    -- Give the result a readable name with AS
    SELECT
        COUNT(*) AS total_books,
        AVG(rating) AS avg_rating,
        MAX(year) AS newest_year
    FROM books;"""

    st.code(code45, language="python")

    st.table(summary)

    st.markdown('<div class="section-title">GROUP BY — aggregating per category</div>', unsafe_allow_html=True)

    st.markdown("""GROUP BY lets you run aggregates for each group of rows, not just the whole table:""")

    code46 = """
    -- How many books per author?
    SELECT author, COUNT(*) AS book_count
    FROM books
    GROUP BY author;

    -- Average rating per decade
    SELECT
        (year / 10) * 10 AS decade,
        AVG(rating) AS avg_rating,
        COUNT(*) AS books
    FROM books
    GROUP BY decade
    ORDER BY decade;

    -- HAVING filters groups (like WHERE but for aggregates)
    SELECT author, COUNT(*) AS book_count
    FROM books
    GROUP BY author
    HAVING book_count > 1;"""

    st.code(code46, language="python")

    st.markdown("""<div class="tip-box">
            💡 WHERE vs HAVING: WHERE filters individual rows before grouping. HAVING filters groups after aggregation. You can't use aggregate functions in WHERE.</div>""", unsafe_allow_html=True)
    
    st.markdown("### 🧠 Quick Check")
    st.markdown("**You want to find authors who have more than 2 books. Which clause filters the groups after aggregation??**")

    options = [
        "WHERE",
        "FILTER",
        "HAVING",
        "GROUP BY"]
    
    correct_answer = options[2]

    for option in options:
        if st.button(option, use_container_width=True, key=f"ch41{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Exactly HAVING! It works like WHERE but operates on the result of GROUP BY, after aggregation.")
            if st.button("Next", key="ch42_next"):
                st.session_state.chapter = 42
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")

if st.session_state.chapter == 42:
    chapter(7,
        "JOINs",
        "Combining data from multiple tables")
    
    st.markdown("""Real databases have multiple tables that relate to each other. ***JOIN*** is how you combine them. It's one of the most powerful — and most important — SQL concepts.

Let's add a members table and a loans table (sound familiar from OOP project?):""")
    
    code47 = """
    CREATE TABLE members (
        id    INTEGER PRIMARY KEY AUTOINCREMENT,
        name  TEXT    NOT NULL,
        email TEXT    UNIQUE
    );

    CREATE TABLE loans (
        id         INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id    INTEGER REFERENCES books(id),
          INTEGER REFERENCES members(id),
        loan_date  TEXT,
        returned   INTEGER DEFAULT 0  -- 0 = false, 1 = true
    );"""

    st.code(code47, language="python")

    st.markdown('<div class="section-title">INNER JOIN — rows that match in BOTH tables</div>', unsafe_allow_html=True)

    code48 = """
    -- Who borrowed which book?
    SELECT
        m.name       AS member,
        b.title      AS book,
        l.loan_date
    FROM loans l
    INNER JOIN books   b ON l.book_id   = b.id
    INNER JOIN members m ON l.member_id = m.id;"""

    st.code(code48, language="python")

    st.dataframe(result)

    st.markdown('<div class="section-title">The JOIN types</div>', unsafe_allow_html=True)

    code49 = """
    INNER JOIN  -- only rows that match in BOTH tables
    LEFT JOIN   -- all rows from the LEFT table, matching rows from right (NULL if no match)
    RIGHT JOIN  -- all rows from RIGHT table (not in SQLite)
    FULL JOIN   -- all rows from both tables (not in SQLite)"""

    st.code(code49, language="python")

    code50 = """
    -- All books, including ones never borrowed
    SELECT b.title, m.name AS borrowed_by
    FROM books b
    LEFT JOIN loans   l ON b.id = l.book_id
    LEFT JOIN members m ON l.member_id = m.id;
    -- Books with no loans show NULL for borrowed_by"""

    st.code(code50, language="python")

    st.markdown("### 🧠 Quick Check")
    st.markdown("**What does LEFT JOIN return that INNER JOIN doesn't??**")

    options = [
        "Rows from the left table even when there's no match in the right table",
        "Only matching rows from both tables",
        "Duplicate rows",
        "Only NULL values"]
    
    correct_answer = options[0]

    for option in options:
        if st.button(option, use_container_width=True, key=f"ch42{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Exactly HAVING! It works like WHERE but operates on the result of GROUP BY, after aggregation.")
            if st.button("Next", key="ch43_next"):
                st.session_state.chapter = 43
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")

if st.session_state.chapter == 43:
    chapter(8,
        "Foreign Keys & Relationships",
        "Connecting tables properly")
    
    st.markdown("""A ***foreign key*** is a column in one table that references the primary key of another. It's how relationships between tables are enforced.""")

    st.markdown("""● ***One-to-many***: one member can have many loans. loans.member_id → members.id""")

    st.markdown("""● ***Many-to-many***: a book can be borrowed by many members over time, and a member can borrow many books — handled through a joining table like loans""")
    
    st.markdown("""● ***One-to-***: rare, but exists (e.g. one member has one profile)""")

    code51 = """
    CREATE TABLE loans (
        id         INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id    INTEGER NOT NULL,
        member_id  INTEGER NOT NULL,
        loan_date  TEXT    NOT NULL,
        due_date   TEXT,
        returned   INTEGER DEFAULT 0,
        FOREIGN KEY (book_id)   REFERENCES books(id),
        FOREIGN KEY (member_id) REFERENCES members(id)
    );

    -- Enable FK enforcement in SQLite (off by default!)
    PRAGMA foreign_keys = ON;"""

    st.code(code51, language="python")

    st.markdown("""<div class="tip-box">
            ⚠️ SQLite doesn't enforce foreign keys unless you explicitly turn them on with PRAGMA foreign_keys = ON. PostgreSQL and MySQL enforce them automatically.</div>""", unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">CASCADE — what happens when you delete a parent?</div>', unsafe_allow_html=True)

    code52 = """
    FOREIGN KEY (book_id) REFERENCES books(id)
        ON DELETE CASCADE    -- delete loans when the book is deleted
        ON DELETE SET NULL   -- set book_id to NULL instead
        ON DELETE RESTRICT  -- prevent deleting if loans exist (default)"""
    
    st.code(code52, language="python")

    st.markdown("""<div class="tip-box">
            💡 Think of foreign keys as the SQL equivalent of composition from OOP — a loan "has-a" book and "has-a" member, and those relationships are enforced at the database level.</div>""", unsafe_allow_html=True)
    
    st.markdown("### 🧠 Quick Check")
    st.markdown("**A loans table has a member_id column that references members.id. What kind of relationship is this??**")

    options = [
        "Many-to-many",
        "One-to-one",
        "Primary key relationship",
        "Many-to-one (many loans belong to one member)"]
    
    correct_answer = options[3]

    for option in options:
        if st.button(option, use_container_width=True, key=f"ch43{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Right! One member can have many loans — that's a one-to-many relationship, modelled with a foreign key.")
            if st.button("Next", key="ch44_next"):
                st.session_state.chapter = 44
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")

if st.session_state.chapter == 44:
    chapter(9,
        "Subqueries & CTEs",
        "Queries inside queries")
    
    st.markdown("""Sometimes one query isn't enough. ***Subqueries*** let you nest a SELECT inside another query. CTEs (Common Table Expressions) let you name and reuse intermediate results — making complex queries readable.""")

    st.markdown('<div class="section-title">Subqueries</div>', unsafe_allow_html=True)

    code53 = """
    -- Books with above-average rating
    SELECT title, rating
    FROM books
    WHERE rating > (
        SELECT AVG(rating) FROM books
    );

    -- Members who have borrowed at least one book
    SELECT name FROM members
    WHERE id IN (
        SELECT DISTINCT member_id FROM loans
    );"""

    st.code(code53, language="python")

    st.markdown('<div class="section-title">CTEs — WITH clause</div>', unsafe_allow_html=True)

    st.markdown("CTEs are like temporary named results you define at the top and then query. They make complex logic much easier to read:")

    code54 = """
    -- Find the most active borrower
    WITH loan_counts AS (
        SELECT
            member_id,
            COUNT(*) AS total_loans
        FROM loans
        GROUP BY member_id
    ),
    member_totals AS (
        SELECT
            m.name,
            lc.total_loans
        FROM members m
        INNER JOIN loan_counts lc ON m.id = lc.member_id
    )   
    SELECT * FROM member_totals
    ORDER BY total_loans DESC
    LIMIT 1;"""

    st.code(code54, language="python")

    st.markdown("""<div class="tip-box">
            💡 Whenever you find yourself writing a subquery more than once, or a query that's hard to read, reach for a CTE. They work in SQLite, PostgreSQL, and MySQL.</div>""", unsafe_allow_html=True)
    
    st.markdown("### 🧠 Quick Check")
    st.markdown("**What is a CTE (Common Table Expression)??**")

    options = [
        "A type of index",
        "A named temporary result set defined with WITH that you can query",
        "A way to create permanent tables",
        "A type of JOIN"]
    
    correct_answer = options[1]

    for option in options:
        if st.button(option, use_container_width=True, key=f"ch44{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Exactly! CTEs let you name intermediate query results and reference them, making complex queries much more readable.")
            if st.button("Next", key="ch45_next"):
                st.session_state.chapter = 45
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")

if st.session_state.chapter == 45:
    chapter(10,
        "Indexes, Transactions & Best Practices",
        "Writing SQL that's fast, safe, and clean")
    
    st.markdown('<div class="section-title">Indexes — making queries fast</div>', unsafe_allow_html=True)

    st.markdown("""An index is a data structure that makes lookups on a column much faster — like an index in a book. Without one, the database reads every row to find a match (***full table scan***).""")

    code55 = """
    -- Create an index on a column you search often
    CREATE INDEX idx_books_author ON books(author);
    CREATE INDEX idx_loans_member ON loans(member_id);

    -- Unique index — also enforces uniqueness
    CREATE UNIQUE INDEX idx_members_email ON members(email);"""

    st.code(code55, language="python")

    st.markdown("""<div class="tip-box">
            ⚠️ Don't index everything — indexes speed up reads but slow down writes. Index columns you filter or JOIN on frequently.</div>""", unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">Transactions — all or nothing</div>', unsafe_allow_html=True)

    st.markdown("""A transaction groups multiple statements so they either ***all succeed*** or ***all fail***. Critical when accuracy matters (e.g. bank transfers).""")

    code56 = """
    import sqlite3

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO loans (book_id, member_id, loan_date) VALUES (?, ?, ?)",
                    (1, 1, "2024-03-15"))
        cursor.execute("UPDATE books SET available = 0 WHERE id = ?", (1,))
        conn.commit()       # ✓ both succeeded — save
        print("Loan created!")
    except Exception as e:
        conn.rollback()     # ✗ something failed — undo everything
        print(f"Error: {e}")
    finally:
        conn.close()"""
    
    st.code(code56, language="python")
    
    st.markdown('<div class="section-title">SQLite → PostgreSQL / MySQL in VS Code</div>', unsafe_allow_html=True)

    code57 = """
    # PostgreSQL — install: pip install psycopg2-binary
    import psycopg2
    conn = psycopg2.connect(host="localhost", dbname="mydb",
                            user="postgres", password="...")
    # Use %s instead of ? for placeholders

    # MySQL — install: pip install mysql-connector-python
    import mysql.connector
    conn = mysql.connector.connect(host="localhost", database="mydb",
                                   user="root", password="...")
    # Use %s instead of ? for placeholders
    # Everything else (SELECT, JOIN, etc.) is identical"""

    st.code(code57, language="python")

    st.markdown("""<div class="tip-box">
            🎉 You're done! The SQL you've learned here is 95% of what you'll use day-to-day in any database. Now go build the project.</div>""", unsafe_allow_html=True)
    
    st.markdown("### 🧠 Quick Check")
    st.markdown("**What does conn.rollback() do in a transaction??**")

    options = [
        "Undoes all changes since the last commit",
        "Commits all changes permanently",
        "Closes the connection",
        "Deletes all tables"]
    
    correct_answer = options[0]

    for option in options:
        if st.button(option, use_container_width=True, key=f"ch45{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Correct! rollback() reverts everything back to the state before the transaction started — essential for keeping data consistent when something goes wrong.")
            if st.button("Next", key="ch46_next"):
                st.session_state.chapter = 46
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")

if st.session_state.chapter == 46:
    chapter(11,
        "Congratulations!",
        "You have finished this Python SQL mini interactive course. Now it is your turn.")
    
    st.markdown("""<div class="tip-box">
                🧠 Do you want to get tasks to practice?""", unsafe_allow_html=True)
    
    st.markdown("")
    
    if st.button("Yes", key="ch47_next"):
        st.session_state.chapter = 47
    elif st.button("No", key="ch47_NO_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 47:
    chapter(12, 
            "Great—here's the first task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the result.")
    
    st.markdown("""<div class="section-title">💡 Task 1: """, unsafe_allow_html=True)
    
    st.markdown("""
                In 01_create_tables.py, create all four tables with proper types, constraints, and foreign keys:\n
                ● books — id, title, author, year, genre (TEXT), rating (REAL), available (INTEGER DEFAULT1)\n
                ● members — id, name, email (UNIQUE NOT NULL), join_date (TEXT), is_premium (INTEGER DEFAULT0)\n
                ● loans — id, book_id (FK → books), member_id (FK → members), loan_date, due_date, returned (DEFAULT0)\n
                ● fines — id, loan_id (FK → loans), member_id (FK → members), amount (REAL), paid (INTEGER DEFAULT0)\n
                Use CREATE TABLE IF NOT EXISTS for all tables. Run the script and verify the tables appear in SQLite Viewer.""")
    
    st.markdown("""<div class="tip-box">
                ⚠️ Hint: Put all FOREIGN KEY constraints at the bottom of each CREATE TABLE block, after the column definitions.""", unsafe_allow_html=True)
    
    st.markdown("")

    if st.button("Next", key="ch48_next"):
        st.session_state.chapter = 48
if st.session_state.chapter == 48:
    code58 = '''
    import sqlite3

    DB_NAME = "library.db"

    def create_tables():
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        #Enable foreign key support
        cursor.execute("PRAGMA foreign_keys = ON;")
        # books table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER,
                genre TEXT,
                rating REAL,
                available INTEGER DEFAULT 1
            );
        """)
        #Members table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS members (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                join_date TEXT,
                is_premium INTEGER DEFAULT 0
            );
        """)
        #Loans table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS loans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id INTEGER,
                member_id INTEGER,
                loan_date TEXT,
                due_date TEXT,
                returned INTEGER DEFAULT 0,

                FOREIGN KEY (book_id) REFERENCES books(id),
                FOREIGN KEY (member_id) REFERENCES members(id)
            );
        """)
        #Fines table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS fines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                loan_id INTEGER,
                member_id INTEGER,
                amount REAL,
                paid INTEGER DEFAULT 0,

                FOREIGN KEY (loan_id) REFERENCES loans(id),
                FOREIGN KEY (member_id) REFERENCES members(id)
            );
        """)
        conn.commit()
        conn.close()
        print("All tables created successfully.")

    if __name__ == "__main__":
        create_tables()
    '''

    st.code(code58, language="python")

    st.markdown("""<div class="section-title">🧠 Did you manage to finish it? Ready for the next task?</div>""", unsafe_allow_html=True)

    if st.button("Yes", key="ch49_next"):
        st.session_state.chapter = 49
    elif st.button("No", key="ch49_NO_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 49:
    chapter(13,
            "Great—here's the next task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the result.")
    
    st.markdown("""<div class="section-title">💡 Task 2: """, unsafe_allow_html=True)
    
    st.markdown("""
                In 02_insert_data.py, insert enough data to make queries interesting:\n
                ● At least 10 books across at least 3 genres (Sci-Fi, Fantasy, Classic, etc.)\n
                ● At least 5 members (2 premium, 3 regular)\n
                ● At least 8 loans — some returned, some still active, at least 2 overdue (set due_date in the past)\n
                ● At least 2 fines — one paid, one unpaid\n
                Use executemany() with lists of tuples and parameterised ? placeholders for all inserts.""")
    
    st.markdown("""<div class="tip-box">
                ⚠️ Hint: For dates, just store them as text strings in ISO format: '2024-01-15'. SQLite sorts text dates correctly if they're in YYYY-MM-DD format.""", unsafe_allow_html=True)
    
    st.markdown("")

    if st.button("Next", key="ch50_next"):
        st.session_state.chapter = 50
if st.session_state.chapter == 50:
    code59 ='''
    if __name__ == "__main__":
    create_tables()

    books = [("The Hobbit", "J.R.R. Tolkien", 1937, "fantasy", 4.3),
         ("The Fellowship of the Ring", "J.R.R. Tolkien", 1954, "fantasy", 4.4),
         ("The Two Towers", "J.R.R. Tolkien", 1955, "fantasy", 4.4),
         ("The Return of the King", "J.R.R. Tolkien", 1955, "fantasy", 4.5),
         ("The Silmarillion", "J.R.R. Tolkien", 1977, "fantasy", 4.9),
         ("Dune", "Frank Herbert", 1965, "sci-fi", 4.6),
         ("The Shining", "Stephen King", 1977, "horror", 4.4),
         ("Hyperion", "Dan Simmons", 1989, "sci-fi", 4.3),
         ("Pride and Prejudice", "Jane Austen", 1813, "romance", 4.2),
         ("The Count of Monte Cristo", "Alexandre Dumas and Auguste Maquet", 1846, "adventure", 4.3)]

    def insert_books():
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.executemany("""
                   INSERT INTO books(title, author, year, genre, rating) VALUES (?, ?, ?, ?, ?)""", books)
    
        conn.commit()
        conn.close()

    members = [("John", "john1@gmail.com", "2021-02-17", 0),
           ("Alice", "alice.smith@hotmail.com", "2025-03-21", 1),
           ("George", "george88@yahoo.com", "2022-07-08", 1),
           ("Bob", "bob_the_builer@mail.com", "2024-12-20", 0),
           ("Tom", "tom.tim.tum@live.com", "2023-09-24", 0)]

    def insert_member():
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.executemany("""
                       INSERT INTO members(name, email, join_date, is_premium) VALUES (?, ?, ?, ?)""", members)
    
        conn.commit()
        conn.close()

    loans = [(4, 2, "2026-02-19", "2026-07-08", 1),
         (2, 3, "2026-03-21", "2026-08-03", 0),
         (1, 4, "2025-12-25", "2026-01-19", 1),
         (3, 2, "2025-11-20", "2026-01-21", 0),
         (5, 1, "2025-10-13", "2025-12-25", 1),
         (7, 1, "2024-12-31", "2025-04-11", 0),
         (8, 4, "2026-01-01", "2026-05-01", 1),
         (6, 3, "2026-07-03", "2026-10-7", 0)]

    def insert_loans():
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.executemany("""
                       INSERT INTO loans(book_id, member_id, loan_date, due_date, returned) VALUES (?, ?, ?, ?, ?)""", loans)
    
        conn.commit()
        conn.close()

    def insert_fines():
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
                   INSERT INTO fines(loan_id, member_id, amount, paid) VALUES (?, ?, ?, ?)""", 
                   (3, 2, 14.99, 1))
    
        cursor.execute("""
                   INSERT INTO fines(loan_id, member_id, amount, paid) VALUES (?, ?, ?, ?)""", 
                   (7, 1, 18.99, 0))
    
        conn.commit()
        conn.close()
    
        def show_fines():
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
        
            cursor.execute("""
                SELECT members.name, fines.amount, fines.paid
                FROM fines
                JOIN members ON fines.member_id = members.id""")

            rows = cursor.fetchall()

            for name, amount, paid in rows:
                status = "PAID" if paid == 1 else "NOT PAID"
                print(f"{name} owes {amount} ({status})")

            conn.close()'''

    st.code(code59, language="python")

    st.markdown("""<div class="section-title">🧠 Did you manage to finish it? Ready for the next task?</div>""", unsafe_allow_html=True)

    if st.button("Yes", key="ch51_next"):
        st.session_state.chapter = 51
    elif st.button("No", key="ch51_NO_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 51:
    chapter(14,
            "Great—here's the next task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the result.")
    
    st.markdown("""<div class="section-title">💡 Task 3: """, unsafe_allow_html=True)

    st.markdown("""
                In 03_queries.py, write SELECT queries that answer these questions:\n
                ● All books sorted alphabetically by title\n
                ● All available books (available = 1)\n
                ● All books published before 1960\n
                ● All premium members\n
                ● All books in the "Sci-Fi" genre with a rating above 4.5\n
                ● All overdue loans (due_date < today, returned = 0). Use Python's date.today() as the parameter\n
                ● The 3 highest-rated books\n
                Print each result set with a clear label, e.g. print("--- Available books ---")""")
    
    st.markdown("""<div class="tip-box">
                ⚠️ Hint: For the overdue query: cursor.execute("SELECT * FROM loans WHERE due_date < ? AND returned = 0", (str(date.today()),))""", unsafe_allow_html=True)
    
    st.markdown("")

    if st.button("Next", key="ch52_next"):
        st.session_state.chapter = 52
if st.session_state.chapter == 52:
    code60 ='''
      def print_books(rows):
        for book in rows:
            print(f"""
                Title: {book[1]}
                Author: {book[2]}
                Year: {book[3]}
                Genre: {book[4]}
                Rating: {book[5]}
                Available: {book[6]}""")
        
    def show_books_sorted():
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM books
            ORDER BY title ASC""")

        rows = cursor.fetchall()
        print_books(rows)

        conn.close()

    def show_available_books():
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM books
            WHERE available = 1
            ORDER BY title ASC""")

        rows = cursor.fetchall()
        print_books(rows)

        conn.close()

    def show_books_before_1960():
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM books
            WHERE year < 1960
            ORDER BY year ASC""")

        rows = cursor.fetchall()
        print_books(rows)

        conn.close()

    def print_members(rows):
        for member in rows:
            status = "Premium" if member[4] == 1 else "Normal"

            print(f"""
            Name: {member[1]}
            Email: {member[2]}
            Join Date: {member[3]}
            Status: {status}""")

    def show_premium_members():
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM members
            WHERE is_premium = 1""")

        rows = cursor.fetchall()
        print_members(rows)

        conn.close()

    def show_highrated_scifi():
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM books
            WHERE genre = "sci-fi"
            AND rating > 4.5""")

        rows = cursor.fetchall()
        print_books(rows)

        conn.close()

    def print_loans(rows):
        for loan in rows:
            status = "Returned" if loan[5] == 1 else "NOT Returned"

            print(f"""
            Loan ID: {loan[0]}
            Book ID: {loan[1]}
            Member ID: {loan[2]}
            Loan Date: {loan[3]}
            Due Date: {loan[4]}
            Status: {status}""")

    def show_overdue_loans():
        conn =sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM loans
            WHERE due_date < ?
            AND returned = 0""",
            (str(datetime.date.today()),))
    
        rows = cursor.fetchall()
        print_loans(rows)

        conn.close()

    def show_rating():
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM books
            ORDER BY rating DESC
            LIMIT 3""")
    
        rows = cursor.fetchall()
        print_books(rows)

        conn.close()'''

    st.code(code60, language="python")

    st.markdown("""<div class="section-title">🧠 Did you manage to finish it? Ready for the next task?</div>""", unsafe_allow_html=True)

    if st.button("Yes", key="ch53_next"):
        st.session_state.chapter = 53
    elif st.button("No", key="ch53_NO_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 53:
    chapter(15,
            "Great—here's the next task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the result.")
    
    st.markdown("""<div class="section-title">💡 Task 4: """, unsafe_allow_html=True)

    st.markdown("""
                Write queries that answer these with aggregate functions:\n
                ● Total number of books in the library\n
                ● Average rating across all books\n
                ● Number of books per genre (GROUP BY)\n
                ● Total unpaid fines across all members\n
                ● The member with the most loans (GROUP BY member_id, ORDER BY COUNT DESC, LIMIT 1)\n
                ● Average rating per genre, only for genres with more than 2 books (use HAVING)""")
    
    st.markdown("")

    if st.button("Next", key="ch54_next"):
        st.session_state.chapter = 54
if st.session_state.chapter == 54:
    code61 ='''
    def count():
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(*)
            FROM books""")
    
        result = cursor.fetchone()[0]

        print("Total books:", result)

        conn.close()

    def average():
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT AVG(rating)
            FROM books""")
    
        result = cursor.fetchone()[0]

        print("Average rating:", result)

        conn.close()
    
    def books_by_genre():
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT genre, GROUP_CONCAT(title)
            FROM books
            GROUP BY genre""")

        rows = cursor.fetchall()

        for genre, titles in rows:
            print(f"{genre}: {titles}")

        conn.close()

    def unpaid_fines():
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT SUM(amount)
            FROM fines
            WHERE paid = 0""")
    
        result = cursor.fetchone()[0]

        print("Total unpaid fines:", result)

        conn.close()

    def total_members():
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT member_id, COUNT (*) AS loan count
            FROM loans
            GROUP BY member_id
            ORDER BY loan_count DESC
            LIMIT 1""")
       
        member_id, loan_count = cursor.fetchone()

        print(f"Member {member_id} has the most loans: {loan_count}")

        conn.close()

    def average_rating():
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute(""" 
            SELECT genre, AVG(rating) AS avg_rating, COUNT(*) AS book_count
            FROM books
            GROUP BY genre
            HAVING COUNT(*) > 2""")
    
        rows = cursor.fetchall()

        for genre, avg_rating, count in rows:
            print(f"{genre}: {avg_rating:.2f} ({count} books)")

        conn.close()'''
    
    st.code(code61, language="python")

    st.markdown("""<div class="section-title">🧠 Did you manage to finish it? Ready for the next task?</div>""", unsafe_allow_html=True)

    if st.button("Yes", key="ch55_next"):
        st.session_state.chapter = 55
    elif st.button("No", key="ch55_NO_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 55:
    chapter(16,
            "Great—here's the next task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the result.")
    
    st.markdown("""<div class="section-title">💡 Task 5: """, unsafe_allow_html=True)

    st.markdown("""
                Practice modifying data — always test your WHERE with a SELECT first:\n
                ● Mark a specific loan as returned (returned = 1) by loan id\n
                ● When marking a loan returned, also set the book's available = 1 (two separate UPDATE statements)\n
                ● Update a member's email address\n
                ● Mark all fines for a specific member as paid\n
                ● Delete all loans that are returned AND older than a certain date""")
    
    st.markdown("")

    st.markdown("""<div class="tip-box">
                ⚠️ Hint: After each operation, print cursor.rowcount to confirm how many rows changed.""", unsafe_allow_html=True)
                
    st.markdown("")
    
    if st.button("Next", key="ch56_next"):
        st.session_state.chapter = 56
if st.session_state.chapter == 56:
    code62 = '''
    import sqlite3

    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    loan_id = 1

    cursor.execute(
        "SELECT * FROM loans WHERE id = ?",
        (loan_id,)
    )
    print(cursor.fetchall())

    cursor.execute(
        "UPDATE loans SET returned = 1 WHERE id = ?",
        (loan_id,)
    )
    print(cursor.rowcount)

    book_id = 1

    cursor.execute(
        "SELECT * FROM books WHERE id = ?",
    (   book_id,)
    )
    print(cursor.fetchall())

    cursor.execute(
        "UPDATE books SET available = 1 WHERE id = ?",
        (book_id,)
    )
    print(cursor.rowcount)

    member_id = 1
    new_email = "newemail@example.com"

    cursor.execute(
        "SELECT * FROM members WHERE id = ?",
        (member_id,)
    )
    print(cursor.fetchall())

    cursor.execute(
        "UPDATE members SET email = ? WHERE id = ?",
        (new_email, member_id)
    )
    print(cursor.rowcount)

    cursor.execute(
        "SELECT * FROM fines WHERE member_id = ? AND paid = 0",
        (member_id,)
    )
    print(cursor.fetchall())

    cursor.execute(
        "UPDATE fines SET paid = 1 WHERE member_id = ? AND paid = 0",
        (member_id,)
    )
    print(cursor.rowcount)

    cutoff_date = "2025-01-01"

    cursor.execute(
        "SELECT * FROM loans WHERE returned = 1 AND loan_date < ?",
        (cutoff_date,)
    )
    print(cursor.fetchall())

    cursor.execute(
        "DELETE FROM loans WHERE returned = 1 AND loan_date < ?",
        (cutoff_date,)
    )
    print(cursor.rowcount)

    connection.commit()
    connection.close()'''

    st.code(code62, language="python")

    st.markdown("""<div class="section-title">🧠 Did you manage to finish it? Ready for the next task?</div>""", unsafe_allow_html=True)

    if st.button("Yes", key="ch57_next"):
        st.session_state.chapter = 57
    elif st.button("No", key="ch57_NO_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 57:
    chapter(17,
            "Great—here's the next task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the result.")
    
    st.markdown("""<div class="section-title">💡 Task 6: """, unsafe_allow_html=True)

    st.markdown("""
                In 04_joins.py, write JOIN queries that answer:\n
                ● All current loans — show member name, book title, loan date, and due date\n
                ● All overdue loans — show member name, book title, days overdue (calculate using date functions or Python)\n
                ● All books that have NEVER been borrowed (LEFT JOIN + WHERE loan id IS NULL)\n
                ● All members and their total outstanding fines (LEFT JOIN fines, GROUP BY member)\n
                ● Full loan history — member name, book title, loan date, returned status — ordered by loan date
                """)
    
    st.markdown("""<div class="tip-box">
                ⚠️ Hint: SELECT b.title FROM books b LEFT JOIN loans l ON b.id = l.book_id WHERE l.id IS NULL""", unsafe_allow_html=True)
    
    st.markdown("")
    
    if st.button("Next", key="ch58_next"):
        st.session_state.chapter = 58
if st.session_state.chapter == 58:
    code63 = '''
    import sqlite3
    from datetime import date

    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT m.name, b.title, l.loan_date, l.due_date
        FROM loans l
        JOIN members m ON l.member_id = m.id
        JOIN books b ON l.book_id = b.id
        WHERE l.returned = 0
    """)

    print("--- Current loans ---")
    for row in cursor.fetchall():
        print(row)

    cursor.execute("""
        SELECT
            m.name,
            b.title,
            julianday(?) - julianday(l.due_date) AS days_overdue
        FROM loans l
        JOIN members m ON l.member_id = m.id
        JOIN books b ON l.book_id = b.id
        WHERE l.due_date < ? AND l.returned = 0
    """, (str(date.today()), str(date.today())))

    print("--- Overdue loans ---")
    for row in cursor.fetchall():
        print(row)

    cursor.execute("""
        SELECT b.title
        FROM books b
        LEFT JOIN loans l ON b.id = l.book_id
        WHERE l.id IS NULL
    """)

    print("--- Never-borrowed books ---")
    for row in cursor.fetchall():
        print(row)

    cursor.execute("""
        SELECT
            m.name,
            COALESCE(SUM(CASE WHEN f.paid = 0 THEN f.amount ELSE 0 END), 0) AS outstanding_fines
        FROM members m
        LEFT JOIN fines f ON m.id = f.member_id
        GROUP BY m.id, m.name
    """)

    print("--- Outstanding fines by member ---")
    for row in cursor.fetchall():
        print(row)

    cursor.execute("""
        SELECT
            m.name,
            b.title,
            l.loan_date,
            l.returned
        FROM loans l
        JOIN members m ON l.member_id = m.id
        JOIN books b ON l.book_id = b.id
         BY l.loan_date
    """)

    print("--- Full loan history ---")
    for row in cursor.fetchall():
        print(row)

    connection.close()'''

    st.code(code63, language="python")

    st.markdown("""<div class="section-title">🧠 Did you manage to finish it? Ready for the next task?</div>""", unsafe_allow_html=True)

    if st.button("Yes", key="ch59_next"):
        st.session_state.chapter = 59
    elif st.button("No", key="ch59_NO_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 59:
    chapter(18,
            "Great—here's the next task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the result.")
    
    st.markdown("""<div class="section-title">💡 Task 7: """, unsafe_allow_html=True)

    st.markdown(""" 
                In 05_advanced.py, solve these with subqueries:\n
                ● Books with an above-average rating\n
                ● Members who have never borrowed any book (NOT IN subquery)\n
                ● The most-borrowed book — show its title and borrow count\n
                ● Members whose total unpaid fines are above the average unpaid fine
                """)
    
    st.markdown("""<div class="tip-box">
                ⚠️ Hint for never-borrowed members: WHERE id NOT IN (SELECT DISTINCT member_id FROM loans)""", unsafe_allow_html=True)
    
    st.markdown("")
    
    if st.button("Next", key="ch60_next"):
        st.session_state.chapter = 60
if st.session_state.chapter == 60:
    code64 = '''
    import sqlite3

    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM books
        WHERE rating > (
            SELECT AVG(rating)
            FROM books
        )
    """)

    print("--- Books with above-average rating ---")
    for row in cursor.fetchall():
        print(row)

    cursor.execute("""
        SELECT *
        FROM members
        WHERE id NOT IN (
            SELECT DISTINCT member_id
            FROM loans
        )
    """)

    print("--- Members who never borrowed a book ---")
    for row in cursor.fetchall():
        print(row)

    cursor.execute("""
        SELECT
            b.title,
            COUNT(l.id) AS borrow_count
        FROM books b
        JOIN loans l ON b.id = l.book_id
        GROUP BY b.id, b.title
        HAVING COUNT(l.id) = (
            SELECT MAX(borrow_count)
            FROM (
                SELECT COUNT(*) AS borrow_count
                FROM loans
                GROUP BY book_id
            )
        )
    """)

    print("--- Most-borrowed book ---")
    for row in cursor.fetchall():
        print(row)

    cursor.execute("""
        SELECT
            m.id,
            m.name,
            (
                SELECT COALESCE(SUM(f.amount), 0)
                FROM fines f
                WHERE f.member_id = m.id AND f.paid = 0
            ) AS unpaid_fines
        FROM members m
        WHERE (
            SELECT COALESCE(SUM(f.amount), 0)
            FROM fines f
            WHERE f.member_id = m.id AND f.paid = 0
        ) > (
            SELECT AVG(unpaid_total)
            FROM (
                SELECT
                    COALESCE(SUM(f.amount), 0) AS unpaid_total
                FROM members m2
                LEFT JOIN fines f ON m2.id = f.member_id AND f.paid = 0
                GROUP BY m2.id
            )
        )
    """)

    print("--- Members above average unpaid fines ---")
    for row in cursor.fetchall():
        print(row)

    connection.close()'''

    st.code(code64, language="python")

    st.markdown("""<div class="section-title">🧠 Did you manage to finish it? Ready for the next task?</div>""", unsafe_allow_html=True)

    if st.button("Yes", key="ch61_next"):
        st.session_state.chapter = 61
    elif st.button("No", key="ch61_NO_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 61:
    chapter(19,
            "Great—here's the next task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the result.")
    
    st.markdown("""<div class="section-title">💡 Task 8: """, unsafe_allow_html=True)

    st.markdown("""
                Use CTEs to write a member summary report. For every member, show:\n
                ● Their name and membership type (regular/premium)\n
                ● Total books borrowed (all time)\n
                ● Currently active loans\n
                ● Total fines owed (unpaid)\n
                Build it step by step using multiple CTEs — one for loan counts, one for active loans, one for fines — then JOIN them all together at the end.""")
    
    st.markdown("""<div class="tip-box">
                ⚠️ Structure: WITH loan_counts AS (...), active_loans AS (...), unpaid_fines AS (...) SELECT ... FROM members LEFT JOIN loan_counts ... LEFT JOIN active_loans ... LEFT JOIN unpaid_fines ...""", unsafe_allow_html=True)
    
    st.markdown("")
    
    if st.button("Next", key="ch62_next"):
        st.session_state.chapter = 62
if st.session_state.chapter == 62:
    code65 = '''
    import sqlite3

    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    cursor.execute("""
        WITH loan_counts AS (
            SELECT
                member_id,
                COUNT(*) AS total_borrowed
            FROM loans
            GROUP BY member_id
        ),
        active_loans AS (
            SELECT
                member_id,
                COUNT(*) AS active_count
            FROM loans
            WHERE returned = 0
            GROUP BY member_id
        ),
        unpaid_fines AS (
            SELECT
                member_id,
                SUM(amount) AS fines_owed
            FROM fines
            WHERE paid = 0
            GROUP BY member_id
        )
        SELECT
            m.name,
            CASE
                WHEN m.is_premium = 1 THEN 'premium'
                ELSE 'regular'
            END AS membership_type,
            COALESCE(lc.total_borrowed, 0) AS total_borrowed,
            COALESCE(al.active_count, 0) AS active_loans,
            COALESCE(uf.fines_owed, 0) AS fines_owed
        FROM members m
        LEFT JOIN loan_counts lc ON m.id = lc.member_id
        LEFT JOIN active_loans al ON m.id = al.member_id
        LEFT JOIN unpaid_fines uf ON m.id = uf.member_id
        ORDER BY m.name
    """)

    print("--- Member Summary Report ---")

    for row in cursor.fetchall():
        print(row)

    connection.close()'''

    st.code(code65, language="python")

    st.markdown("""<div class="section-title">🧠 Did you manage to finish it? Ready for the next task?</div>""", unsafe_allow_html=True)

    if st.button("Yes", key="ch63_next"):
        st.session_state.chapter = 63
    elif st.button("No", key="ch63_NO_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 63:
    chapter(20,
            "Great—here's the next task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the result.")
    
    st.markdown("""<div class="section-title">💡 Task 9: """, unsafe_allow_html=True)

    st.markdown("""
                    In 06_transactions.py, write a checkout_book(book_id, member_id) Python function that:\n
                    ● Checks the book exists and is available — raise a custom exception if not\n
                    ● Checks the member exists and hasn't hit their loan limit (3 for regular, 10 for premium) — raise if not\n
                    ● Inserts a new row into loans with today's date and a due_date 14 days from now\n
                    ● Updates the book's available = 0\n
                    ● Wraps steps 3 and 4 in a try/except with conn.commit() and conn.rollback()""")
        
    st.markdown("""<div class="tip-box">
                    ⚠️ Hint: Also write a return_book(loan_id) function that marks the loan returned, sets the book available again, and creates a fine record if it's overdue (€0.20 per day).""", unsafe_allow_html=True)
        
    st.markdown("")

    if st.button("Next", key="ch64_next"):
            st.session_state.chapter = 64
if st.session_state.chapter == 64:
    code66 = '''
        from datetime import date, timedelta

        class TransactionError(Exception):
            """Raised when a library transaction cannot be completed."""
            pass

        def checkout_book(book_id, member_id):
            cursor = conn.cursor()

            cursor.execute(
                "SELECT available FROM books WHERE id = ?",
                (book_id,)
            )
            book = cursor.fetchone()

            if book is None:
                raise TransactionError("Book does not exist.")

            if book[0] == 0:
                raise TransactionError("Book is not available.")

            cursor.execute(
                "SELECT membership_type FROM members WHERE id = ?",
                (member_id,)
            )
            member = cursor.fetchone()

            if member is None:
                raise TransactionError("Member does not exist.")

            is_premium = member[0]
            loan_limit = 10 if is_premium == 1 else 3

            cursor.execute(
                """
                SELECT COUNT(*)
                FROM loans
                WHERE member_id = ? AND returned_date = 0
                """,
                (member_id,)
            )
            current_loans = cursor.fetchone()[0]

            if current_loans >= loan_limit:
                raise TransactionError("Member has reached their loan limit.")

            try:
                loan_date = date.today()
                due_date = loan_date + timedelta(days=14)

                cursor.execute(
                    """
                    INSERT INTO loans (book_id, member_id, loan_date, due_date)
                    VALUES (?, ?, ?, ?)
                    """,
                    (book_id, member_id, loan_date.isoformat(), due_date.isoformat())
                )

                cursor.execute(
                    "UPDATE books SET available = 0 WHERE id = ?",
                    (book_id,)
                )
                conn.commit()

            except Exception:
                conn.rollback()
                raise

        def return_book(loan_id):
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT book_id, due_date, returned_date
                FROM loans
                WHERE id = ?
                """,
                (loan_id,)
            )
            loan = cursor.fetchone()

            if loan is None:
                raise TransactionError("Loan does not exist.")

            if loan[2] = 1:
                raise TransactionError("Book has already been returned.")

            book_id, due_date_str, _ = loan

            try:
                return_date = date.today()
                due_date = date.fromisoformat(due_date_str)

                cursor.execute(
                    """
                    UPDATE loans
                    SET returned = ?
                    WHERE id = ?
                    """,
                    (return_date.isoformat(), loan_id)
                )
                cursor.execute(
                    """
                    UPDATE books
                    SET available = 1
                    WHERE id = ?
                    """,
                    (book_id,)
                    )

                overdue_days = (return_date - due_date).days

                if overdue_days > 0:
                    fine_amount = overdue_days * 0.20

                    cursor.execute(
                        """
                        INSERT INTO fines (loan_id, amount)
                        VALUES (?, ?)
                        """,
                        (loan_id, fine_amount)
                    )

                conn.commit()

            except Exception:
                conn.rollback()
                raise'''

    st.code(code66, language="python")
    
    st.markdown("")
 
    if st.button("Finish", key="ch65_next"):
        st.session_state.chapter = 65
        st.stop()

if st.session_state.chapter == 65:
    chapter(21,
            "Congratulations! 🎉",
            "🎉You have successfully finished SQL learning guide!🎉")

    st.markdown("""<div class="section-title">🎉You have finished this learning guide!🎉 I am proud of you!</div>""", unsafe_allow_html=True)
        
    st.markdown("""<div class="tip-box">
                ⚠️Don't forget to keep practicing on your own! Programming has many more skills for you to learn! I wish you the best of luck! 💡
                </div>""", unsafe_allow_html=True)

    st.markdown("")

    if st.button("🏠 Return to menu", key="sql_finish_home"):
        st.session_state.chapter = 0
        st.session_state.course = None
