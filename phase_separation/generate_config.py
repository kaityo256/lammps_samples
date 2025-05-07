import random


class Atom:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.type = random.randint(1,2)
        V0 = 1.0
        self.vx = V0 * random.uniform(-1, 1)
        self.vy = V0 * random.uniform(-1, 1)
        self.vz = V0 * random.uniform(-1, 1)

def make_config(M, R, s):
    atoms = []
    h = 0.5 * s
    for ix in range(-M, M):
        for iy in range(-M, M):
            for iz in range(-M, M):
                x = ix * s
                y = iy * s
                z = iz * s
                atoms.append(Atom(x, y, z))
                atoms.append(Atom(x, y+h, z+h))
                atoms.append(Atom(x+h, y, z+h))
                atoms.append(Atom(x+h, y+h, z))
    return atoms


def save_file(filename, atoms, L):
    with open(filename, "w") as f:
        f.write("Position Data\n\n")
        f.write(f"{len(atoms)} atoms\n")
        f.write("2 atom types\n\n")
        f.write(f"{-L} {L} xlo xhi\n")
        f.write(f"{-L} {L} ylo yhi\n")
        f.write(f"{-L} {L} zlo zhi\n")
        f.write("\n")
        f.write("Atoms\n\n")
        for i, a in enumerate(atoms):
            f.write(f"{i+1} {a.type} {a.x} {a.y} {a.z}\n")
        f.write("\n")
        f.write("Velocities\n\n")
        for i, a in enumerate(atoms):
            f.write(f"{i+1} {a.vx} {a.vy} {a.vz}\n")
    print(f"Generated {filename}")


if __name__ == "__main__":
    random.seed(0)
    M = 5
    R = 3.5
    s = 2.0
    atoms = make_config(M, R, s)
    L = M * s
    save_file("phase_separation.atoms", atoms, L)
