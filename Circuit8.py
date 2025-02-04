import schemdraw.elements as elm
from sympy import symbols, Eq, solve


def draw_circuit8_NPN(d, RB="RB", VCC="VCC", RC="RC", RE="RE"):
    transistor = d.add(elm.BjtNpn(circle=False).label("Q1").right())
    d += elm.Resistor().down().label(RE).at(transistor.emitter)
    d += elm.Line().length(3).right()
    d += elm.Ground()
    d += elm.Line().length(1).up()
    d += elm.BatteryCell().up().label(VCC).reverse()
    d += elm.Line().length(5).up()
    d += elm.Line().length(3).left()
    d += elm.Resistor().down().label(RC)
    d += elm.Resistor().left().label(RB)
    d += elm.Line().length(2.25).left().at(transistor.base)
    d += elm.Line().length(2.3).up()
    d += elm.Line().length(1.66).up().at(transistor.collector)
    return d


def draw_circuit8_NPN_Active(d, RB="RB", VCC="VCC", RC="RC", RE="RE"):
    d += elm.SourceControlledI().label("ic").down()
    d += elm.Resistor().down().label(RE)
    d += elm.Ground()
    d += elm.Line().length(3).right()
    d += elm.BatteryCell().up().label(VCC).reverse()
    d += elm.Line().length(6).up()
    d += elm.Line().length(3).left()
    d += elm.Resistor().down().label(RC)
    d += elm.Resistor().left().label(RB)
    d += elm.Line().length(3).down()
    d += elm.BatteryCell().right().label("VBE(act.)")
    return d


def draw_circuit8_NPN_Sat(d, RB="RB", VCC="VCC", RC="RC", RE="RE"):
    d += elm.BatteryCell().label("VCE(sat.)").down()
    d += elm.Resistor().down().label(RE)
    d += elm.Ground()
    d += elm.Line().length(3).right()
    d += elm.BatteryCell().up().label(VCC).reverse()
    d += elm.Line().length(6).up()
    d += elm.Line().length(3).left()
    d += elm.Resistor().down().label(RC)
    d += elm.Resistor().left().label(RB)
    d += elm.Line().length(3).down()
    d += elm.BatteryCell().right().label("VBE(sat.)")
    return d


def draw_circuit8_NPN_off(d, RB="RB", VCC="VCC", RC="RC", RE="RE"):
    d += elm.Dot().label("E").at((0.7516666666666666, -0.6966666666666667))
    d += elm.Resistor().down().label(RE)
    d += elm.Line().length(3).right()
    d += elm.Ground()
    d += elm.Line().length(1).up()
    d += elm.BatteryCell().up().label(VCC).reverse()
    d += elm.Line().length(5).up()
    d += elm.Line().length(3).left()
    d += elm.Resistor().down().label(RC)
    d += elm.Resistor().left().label(RB)
    d += elm.Dot().label("B").at((0.0, 0.0))
    d += elm.Line().length(2.25).left()
    d += elm.Line().length(2.3).up()
    d += elm.Dot().at((0.7516666666666666, 0.6966666666666667))
    d += elm.Line().length(1.66).up()
    return d


def draw_circuit8_PNP(d, RB="RB", VCC="VCC", RC="RC", RE="RE"):
    transistor = d.add(elm.BjtPnp2(circle=False).label("Q1").reverse())
    d += elm.Resistor().down().label(RE).at(transistor.emitter)
    d += elm.Line().length(3).right()
    d += elm.Ground()
    d += elm.Line().length(1).up()
    d += elm.BatteryCell().up().label(VCC)
    d += elm.Line().length(5).up()
    d += elm.Line().length(3).left()
    d += elm.Resistor().down().label(RC)
    d += elm.Resistor().left().label(RB)
    d += elm.Line().length(2.21).left().at(transistor.base)
    d += elm.Line().length(1.5).up()
    return d


def draw_circuit8_PNP_Active(d, RB="RB", VCC="VCC", RC="RC", RE="RE"):
    d += elm.SourceControlledI().label("ic").reverse().down()
    d += elm.Resistor().down().label(RE)
    d += elm.Ground()
    d += elm.Line().length(3).right()
    d += elm.BatteryCell().up().label(VCC)
    d += elm.Line().length(6).up()
    d += elm.Line().length(3).left()
    d += elm.Resistor().down().label(RC)
    d += elm.Resistor().left().label(RB)
    d += elm.Line().length(3).down()
    d += elm.BatteryCell().right().label("VEB(act.)").reverse()
    return d


def draw_circuit8_PNP_Sat(d, RB="RB", VCC="VCC", RC="RC", RE="RE"):
    d += elm.BatteryCell().label("VEC(sat.)").down().reverse()
    d += elm.Resistor().down().label(RE)
    d += elm.Ground()
    d += elm.Line().length(3).right()
    d += elm.BatteryCell().up().label(VCC)
    d += elm.Line().length(6).up()
    d += elm.Line().length(3).left()
    d += elm.Resistor().down().label(RC)
    d += elm.Resistor().left().label(RB)
    d += elm.Line().length(3).down()
    d += elm.BatteryCell().right().label("VEB(sat.)").reverse()
    return d


def draw_circuit8_PNP_off(d, RB="RB", VCC="VCC", RC="RC", RE="RE"):
    d += elm.Dot().label("E").at((0.7516666666666666, -0.6966666666666667))
    d += elm.Resistor().down().label(RE)
    d += elm.Line().length(3).right()
    d += elm.Ground()
    d += elm.Line().length(1).up()
    d += elm.BatteryCell().up().label(VCC)
    d += elm.Line().length(5).up()
    d += elm.Line().length(3).left()
    d += elm.Resistor().down().label(RC)
    d += elm.Resistor().left().label(RB)
    d += elm.Dot().label("B").at((0.0, 0.0))
    d += elm.Line().length(2.25).left()
    d += elm.Line().length(2.3).up()
    d += elm.Dot().at((0.7516666666666666, 0.6966666666666667))
    d += elm.Line().length(1.66).up()
    return d


def Analysis_for_circuit8_NPN(VCC, RE, RB, RC, Beta):
    IB = (VCC - 0.7) / (Beta + 1 + RB + (Beta + 1) * RE)
    kvl1 = "KVL 1: -VCC + (Beta+1) * IB + IB * RB + VBE + (Beta+1)*RE*IB = 0"
    if IB <= 0:
        return (
            ("off", 0, 0, VCC),
            draw_circuit8_NPN_off,
            kvl1,
        )
    IC = Beta * IB
    VCE = VCC - (Beta + 1) * IB * (RC + RE)
    kvl2 = "KVL 2: -VCC + (Beta+1) * IB * RC + VCE + (Beta + 1) * IB * RE = 0"
    if VCE > 0.2:
        return (("Active", IB, IC, VCE), draw_circuit8_NPN_Active, kvl1 + "\n" + kvl2)
    else:
        IB, IC = symbols('IC IB')
        eq1 = Eq(-VCC + (IB + IC) * RC + IB * RB + 0.8 + (IB + IC) * RE, 0)
        eq2 = Eq(-VCC + (IB + IC) * RC + 0.2 + (IB + IC) * RE, 0)
        kvl3 = "KVL 3: -VCC + (IB + IC) * RC + IB * RB + VBE(sat.) + (IB + IC) * RE = 0"
        kvl4 = "KVL 4: -VCC + (IB + IC) * RC + VCE(sat.) + (IB + IC) * RE = 0"
        solution = solve((eq1, eq2), (IC, IB))
        return (
            ("Sat", solution[IB], solution[IC], 0.2),
            draw_circuit8_NPN_Sat,
            kvl1 + "\n" + kvl2 + "\n" + kvl3 + "\n" + kvl4,
        )


def Analysis_for_circuit8_PNP(VCC, RE, RB, RC, Beta):
    IB = (-VCC - 0.7) / (Beta + 1) * (RE + RC) + RB
    kvl1 = "KVL 1: VCC + (Beta + 1) * IB * (RE + RC) + RB * IB + 0.7 = 0"
    if IB <= 0:
        return (
            ("off", 0, 0, VCC),
            draw_circuit8_PNP_off,
            kvl1,
        )
    IC = Beta * IB
    VEC = symbols('VCE')
    eq = Eq((IC + IB) * (RE + RC) + VEC + VCC, 0)
    kvl2 = "KVL 2: (IC + IB)*(RE + RC) + VEC + VCC = 0"
    solution = solve((eq), (VEC))
    VEC = solution[0]
    if VEC > 0.2:
        return (("Active", IB, IC, VEC), draw_circuit8_PNP_Sat, kvl1 + "\n" + kvl2)
    else:
        IB, IC = symbols('IB IC')
        eq1 = Eq((IC + IB) * (RE + RC) + IB * RB + 0.8 + VCC, 0)
        eq2 = Eq((IC + IB) * (RE + RC) + 0.2 + VCC, 0)
        kvl3 = "KVL 3: (IC + IB)*(RE + RC) + IB * RB + VEB(sat.) + VCC = 0"
        kvl4 = "KVL 4: (IC + IB) * (RE + RC) + VEC(sat.) + VCC = 0"
        solution = solve((eq1, eq2), (IB, IC))
        return (
            ("Sat", solution[IB], solution[IC], 0.2),
            draw_circuit8_PNP_Sat,
            kvl1 + "\n" + kvl2 + "\n" + kvl3 + "\n" + kvl4,
        )
