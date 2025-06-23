class Enigma:

    def __init__(self,re,r1,r2,r3,pb,kb):
        self.re = re
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.pb = pb
        self.kb = kb

    def set_rings(self, rings):

        self.r1.set_ring(rings[0])
        self.r2.set_ring(rings[1])
        self.r3.set_ring(rings[2])


    def set_key(self, key):
        self.r1.rotate_to_letter(key[0])
        self.r2.rotate_to_letter(key[1])
        self.r3.rotate_to_letter(key[2])

    def encipher(self,letter):

        if self.r2.left[0] == self.r2.notch and self.r3.left[0] == self.r3.notch:
            self.r1.rotate()
            self.r2.rotate()
            self.r3.rotate()
        elif self.r2.left[0] == self.r2.notch:
            self.r1.roate()
            self.r2.rotate()
            self.r3.rotate()
        elif self.r3.left[0] == self.r3.notch:
            self.r2.rotate()
            self.r3.rotate()
        else:
            self.r3.rotate()

        path = []
        components = [
            (self.kb, 'forward'),
            (self.pb, 'forward'),
            (self.r3, 'forward'),
            (self.r2, 'forward'),
            (self.r1, 'forward'),
            (self.re, 'reflect'),
            (self.r1, 'backward'),
            (self.r2, 'backward'),
            (self.r3, 'backward'),
            (self.pb, 'backward')
        ]
        i = 0
        signal = letter
        for component, method in components:
            signal = getattr(component, method)(signal)
            path.append(signal)
            path.append(signal)
            if i == 5:
                path.append(signal)
            i += 1


        cipher = self.kb.backward(signal)
        print(path)
        return path, cipher
