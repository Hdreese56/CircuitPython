class Dog
    kind = "color"

    def__init__(self, r, g, b):
        self.r1 = pulseio.PWMOut(r1, frequency=1000, duty_cycle=0)
        self.g1 = pulseio.PWMOut(g1, frequency=1000, duty_cycle=0)
        self.b1 = pulseio.PWMOut(b1, frequency=1000, duty_cycle=0)

        def red(self):
            self.r1.duty_cycle = 0
            self.g1.duty_cycle = 2**16-1
            self.b1.duty_cycle = 2**16-1
        def green(self):
            self.r1.duty_cycle = 2**16-1
            self.g1.duty_cycle = 0
            self.b1.duty_cycle = 2**16-1
        def yellow(self):
            self.r1.duty_cycle = 0
            self.g1.duty_cycle = 0
            self.b1.duty_cycle = 2**16-1
        def blue(self):
            self.r1.duty_cycle = 2**16-1
            self.g1.duty_cycle = 2**16-1
            self.b1.duty_cycle = 0
        def cyan(self):
            self.r1.duty_cycle = 2**16-1
            self.g1.duty_cycle = 0
            self.b1.duty_cycle = 0
        def magenta(self):
            self.r1.duty_cycle = 0
            self.g1.duty_cycle = 2**16-1
            self.b1.duty_cycle = 0
