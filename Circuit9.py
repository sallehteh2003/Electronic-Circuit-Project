import schemdraw.elements as elm
from sympy import symbols, Eq, solve


def draw_circuit9_NPN(d, RC="RC", RB="RB", RE="RE", VCC="VCC"):
    transistor = d.add(elm.BjtNpn(circle=False).label("Q1"))
    d += elm.Resistor().up().label(RC).at(transistor.collector)
    d += elm.Dot().label(VCC).up()
    d += elm.Line().length(1.25).left().at(transistor.base)
    d += elm.Resistor().label(RB).up()
    d += elm.Line().length(2).right()
    d += elm.Resistor().label(RE).down().at(transistor.emitter)
    d += elm.Ground()
    return d


def draw_circuit9_NPN_Active(d, RC="RC", RB="RB", RE="RE", VCC="VCC"):
    d += elm.Dot().label(VCC).down()
    d += elm.Resistor().down().label(RC)
    sci = d.add(elm.SourceControlledI().down().label("ic"))
    d += elm.BatteryCell().left().label("VBE(act.)").reverse()
    d += elm.Resistor().label(RB).up()
    d += elm.Line().length(2.3).up()
    d += elm.Line().length(3).right()
    d += elm.Resistor().label(RE).down().at(sci.end)
    d += elm.Ground()
    return d


def draw_circuit9_NPN_Sat(d, RC="RC", RB="RB", RE="RE", VCC="VCC"):
    d += elm.Dot().label(VCC).down()
    d += elm.Resistor().down().label(RC)
    voltageSource = d.add(elm.BatteryCell().down().label("VCE(sat.)"))
    d += elm.BatteryCell().left().label("VBE(sat.)").reverse()
    d += elm.Resistor().label(RB).up()
    d += elm.Line().length(2.3).up()
    d += elm.Line().length(3).right()
    d += elm.Resistor().label(RE).down().at(voltageSource.end)
    d += elm.Ground()
    return d


def draw_circuit9_NPN_off(d, RC="RC", RB="RB", RE="RE", VCC="VCC"):
    d += elm.Dot().at((0.7516666666666666, 0.6966666666666667))
    d += elm.Resistor().up().label(RC)
    d += elm.Dot().label(VCC).up()
    d += elm.Dot().label("B").at((0.0, 0.0))
    d += elm.Line().length(1.25).left()
    d += elm.Resistor().label(RB).up()
    d += elm.Line().length(2).right()
    d += elm.Dot().label("E").at((0.7516666666666666, -0.6966666666666667))
    d += elm.Resistor().label(RE).down()
    d += elm.Ground()
    return d


def draw_circuit9_PNP(d, RC="RC", RB="RB", RE="RE", VCC="VCC"):
    transistor = d.add(elm.BjtPnp2(circle=False).label("Q1").reverse())
    d += elm.Resistor().up().label(RC).at(transistor.collector)
    d += elm.Dot().label(VCC).up()
    d += elm.Line().length(1.25).left().at(transistor.base)
    d += elm.Resistor().label(RB).up()
    d += elm.Line().length(1).up()
    d += elm.Line().length(2).right()
    d += elm.Resistor().label(RE).down().at(transistor.emitter)
    d += elm.Ground()
    return d


def draw_circuit9_PNP_Active(d, RC="RC", RB="RB", RE="RE", VCC="VCC"):
    d += elm.Dot().label(VCC).down()
    d += elm.Resistor().down().label(RC)
    sci = d.add(elm.SourceControlledI().down().label("ic").reverse())
    d += elm.BatteryCell().left().label("VEB(act.)")
    d += elm.Resistor().label(RB).up()
    d += elm.Line().length(2.3).up()
    d += elm.Line().length(3).right()
    d += elm.Resistor().label(RE).down().at(sci.end)
    d += elm.Ground()
    return d


def draw_circuit9_PNP_Sat(d, RC="RC", RB="RB", RE="RE", VCC="VCC"):
    d += elm.Dot().label(VCC).down()
    d += elm.Resistor().down().label(RC)
    valtageSource = d.add(elm.BatteryCell().down().label("VEC(sat.)").reverse())
    d += elm.BatteryCell().left().label("VEB(sat.)")
    d += elm.Resistor().label(RB).up()
    d += elm.Line().length(2.3).up()
    d += elm.Line().length(3).right()
    d += elm.Resistor().label(RE).down().at(valtageSource.end)
    d += elm.Ground()
    return d


def draw_circuit9_PNP_off(d, RC="RC", RB="RB", RE="RE", VCC="VCC"):
    d += elm.Dot().at((0.7516666666666666, 0.6966666666666667))
    d += elm.Resistor().up().label(RC)
    d += elm.Dot().label(VCC).up()
    d += elm.Dot().label("B").at((0.0, 0.0))
    d += elm.Line().length(1.25).left()
    d += elm.Resistor().label(RB).up()
    d += elm.Line().length(2).right()
    d += elm.Dot().label("E").at((0.7516666666666666, -0.6966666666666667))
    d += elm.Resistor().label(RE).down()
    d += elm.Ground()
    return d


def Analysis_for_circuit9_NPN(VCC, RC, RB, RE, Beta):
    IB = symbols('IB')
    eq = Eq(-VCC + IB * RB + 0.7 + (Beta + 1) * IB * RE, 0)
    kvl1 = "KVL 1: -VCC + IB * RB + VBE(act.) + (Beta + 1) * IB * RE = 0"
    solution = solve((eq), (IB))
    IB = solution[0]
    if IB <= 0:
        return (
            ("off", 0, 0, VCC),
            draw_circuit9_NPN_off,
            kvl1,
        )
    IC = Beta * IB
    VCE = symbols('VCE')
    eq = Eq(-VCC + IC * RC + VCE + (Beta + 1) * IB * RE, 0)
    kvl2 = "KVL 2: -VCC + IC * RC + VCE + (Beta + 1) * IB * RE = 0"
    solution = solve((eq), (VCE))
    VCE = solution[0]
    if VCE > 0.2:
        return (
            ("Active", IB, IC, VCE),
            draw_circuit9_NPN_Active,
            kvl1 + "\n" + kvl2,
        )
    IB, IC = symbols('IB IC')
    eq1 = Eq(-VCC + IB * RB + 0.8 + (IB + IC) * RE, 0)
    eq2 = Eq(-VCC + IC * RC + 0.2 + (IB + IC) * RE, 0)
    solution = solve((eq1, eq2), (IB, IC))
    kvl3 = "KVL 3: -VCC + IB * RB + VBE(sat.) + (IB + IC) * RE = 0"
    kvl4 = "KVL 4: -VCC + IC * RC + VCE(sat.) + (IB + IC) * RE = 0"
    return (
        ("Sat", solution[IB], solution[IC], 0.2),
        draw_circuit9_NPN_Sat,
        kvl1 + "\n" + kvl2 + "\n" + kvl3 + "\n" + kvl4,
    )


def Analysis_fort_circuit9_PNP(VCC, RC, RB, RE, Beta):
    IB = symbols('IB')
    eq = Eq((Beta + 1) * IB * RE + 0.7 + IB * RB + VCC, 0)
    solution = solve((eq), (IB))
    IB = solution[0]
    kvl1 = "KVL 1: (Beta + 1) * IB * RB + VEB(act.) + IB * RB + VCC = 0"
    if IB <= 0:
        return (("off", 0, 0, VCC), draw_circuit9_PNP_off, kvl1)
    IC = Beta * IB
    VEC = symbols('VEC')
    eq = Eq((IB + IC) * RE + VEC + IC * RC + VCC, 0)
    kvl2 = "KVL 2: (IB + IC) * RE + VEC + IC * RC + VCC = 0"
    solution = solve((eq), (VEC))
    VEC = solution[0]
    if VEC > 0.2:
        return (
            ("Active", IB, IC, VEC),
            draw_circuit9_PNP_Active,
            kvl1 + "\n" + kvl2,
        )
    IB, IC = symbols('IB IC')
    eq1 = Eq((IB + IC) * RE + 0.8 + IB * RB + VCC, 0)
    eq2 = Eq((IB + IC) * RE + 0.2 + IC * RC + VCC, 0)
    kvl3 = "KVL 3: (IB + IC) * RE + VEB(sat.) + IB * RB + VCC = 0"
    kvl4 = "KVL 4: (IB + IC) * RE + VEC(sat.) + IC * RC + VCC = 0"
    solution = solve((eq1, eq2), (IB, IC))
    return (
        ("Sat", solution[IB], solution[IC], 0.2),
        draw_circuit9_PNP_Sat,
        kvl1 + "\n" + kvl2 + "\n" + kvl3 + "\n" + kvl4,
    )
