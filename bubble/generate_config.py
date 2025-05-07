import random


class Atom:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.type = 1
        V0 = 1.0
        self.vx = V0 * random.uniform(-1, 1)
        self.vy = V0 * random.uniform(-1, 1)
        self.vz = V0 * random.uniform(-1, 1)


def add_atom(x, y, z, R, atoms):
    if x**2 + y**2 + z**2 < R**2:
        return
    atoms.append(Atom(x, y, z))


def make_config(M, R, s):
    atoms = []
    h = 0.5 * s
    for ix in range(-M, M):
        for iy in range(-M, M):
            for iz in range(-M, M):
                x = ix * s
                y = iy * s
                z = iz * s
                add_atom(x, y, z, R, atoms)
                add_atom(x, y + h, z + h, R, atoms)
                add_atom(x + h, y, z + h, R, atoms)
                add_atom(x + h, y + h, z, R, atoms)
    return atoms


def save_file(filename, atoms, L):
    with open(filename, "w") as f:
        f.write("Position Data\n\n")
        f.write(f"{len(atoms)} atoms\n")
        f.write("1 atom types\n\n")
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
    M = 5
    R = 3.5
    s = 1.55
    atoms = make_config(M, R, s)
    L = M * s
    save_file("bubble.atoms", atoms, L)
