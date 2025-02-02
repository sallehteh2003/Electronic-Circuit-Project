import schemdraw
import schemdraw.elements as elm


def draw_circuit6_NPN(d, RB="RB", VCC="VCC", RC="RC", RE="RE", VEE="VEE"):

    transistor = d.add(elm.BjtNpn(circle=True).label("Q1")).reverse()
    d += elm.Resistor().left().label(RB).at(transistor.base)
    d += elm.BatteryCell().down().label(VEE)
    d += elm.Line().length(0.7).down()
    d += elm.Line().length(7).right()
    d += elm.BatteryCell().up().label(VEE).reverse()
    d += elm.BatteryCell().up().label(VCC).reverse()
    d += elm.Line().length(1.4).up()
    d += elm.Resistor().up().label(RC).at(transistor.collector)
    d += elm.Line().length(3.2).right()
    d += elm.Resistor().down().label(RE).at(transistor.emitter)
    d += elm.Ground()

    return d


def draw_circuit6_NPN_off(d, RB="RB", VCC="VCC", RC="RC", RE="RE", VEE="VEE"):
    d += elm.Dot().at((-1.5033333333333332, 1.8410523547181874e-16))
    d += elm.Resistor().left().label(RB)
    d += elm.BatteryCell().down().label(VEE).reverse()
    d += elm.Line().length(7).right()
    d += elm.BatteryCell().up().label(VEE)
    d += elm.BatteryCell().up().label(VCC).reverse()
    d += elm.Dot().at((-0.7516666666666665, 0.6966666666666668))
    d += elm.Line().length(2.3).up()
    d += elm.Resistor().right().label(RC)
    d += elm.Line().length(0.25).right()
    d += elm.Dot().at((-0.7516666666666667, -0.6966666666666665))
    d += elm.Resistor().down().label(RE)
    d += elm.Line().length(0.25).down()
    d += elm.Ground()
    return d


def draw_circuit6_NPN_Sat(d, RB="RB", VCC="VCC", RC="RC", RE="RE", VEE="VEE"):

    d += elm.BatteryCell().left().label("VBE").reverse()
    d += elm.Resistor().left().label(RB)
    d += elm.BatteryCell().down().label(VEE)
    d += elm.Line().length(9).right()
    d += elm.BatteryCell().up().label(VEE).reverse()
    d += elm.BatteryCell().up().label(VCC).reverse()
    d += elm.Line().length(2).up()
    d += elm.Resistor().left().label(RC)
    d += elm.BatteryCell().down().label("VCE")
    d += elm.Line().length(2.5).down()
    d += elm.Resistor().down().label(RE)
    d += elm.Ground()

    return d



def draw_circuit6_NPN_Active(d, RB="RB", VCC="VCC", RC="RC", RE="RE", VEE="VEE"):

    d += elm.BatteryCell().left().label("VBE").reverse()
    d += elm.Resistor().left().label(RB)
    d += elm.BatteryCell().down().label(VEE)
    d += elm.Line().length(9).right()
    d += elm.BatteryCell().up().label(VEE).reverse()
    d += elm.BatteryCell().up().label(VCC).reverse()
    d += elm.Line().length(2).up()
    d += elm.Resistor().left().label(RC)
    d += elm.SourceControlledI().label("ib").down()
    d += elm.Line().length(2.5).down()
    d += elm.Resistor().down().label(RE)
    d += elm.Ground()

    return d


def draw_circuit6_PNP(d, RB="RB", VCC="VCC", RC="RC", RE="RE", VEE="VEE"):

    transistor = d.add(elm.BjtPnp2(circle=True).label("Q1").reverse())
    d += elm.Resistor().left().label(RB).at(transistor.base)
    d += elm.BatteryCell().down().label(VEE)
    d += elm.Line().length(1).down()
    d += elm.Line().length(7).right()
    d += elm.BatteryCell().up().label(VEE).reverse()
    d += elm.BatteryCell().up().label(VCC).reverse()
    d += elm.Line().length(2.49).up()
    d += elm.Resistor().up().label(RC).at(transistor.collector)
    d += elm.Line().length(3.2).right()
    d += elm.Resistor().down().label(RE).at(transistor.emitter)
    d += elm.Ground()

    return d


def draw_circuit6_PNP_off(d, RB="RB", VCC="VCC", RC="RC", RE="RE", VEE="VEE"):

    d += elm.Dot().at((-1.5033333333333332, 1.8410523547181874e-16))
    d += elm.Resistor().left().label(RB)
    d += elm.BatteryCell().down().label(VEE).reverse()
    d += elm.Line().length(7).right()
    d += elm.BatteryCell().up().label(VEE)
    d += elm.BatteryCell().up().label(VCC).reverse()
    d += elm.Dot().at((-0.7516666666666665, 0.6966666666666668))
    d += elm.Line().length(2.3).up()
    d += elm.Resistor().right().label(RC)
    d += elm.Line().length(0.25).right()
    d += elm.Dot().at((-0.7516666666666667, -0.6966666666666665))
    d += elm.Resistor().down().label(RE)
    d += elm.Line().length(0.25).down()
    d += elm.Ground()

    return d


def draw_circuit6_PNP_Sat(d, RB="RB", VCC="VCC", RC="RC", RE="RE", VEE="VEE"):

    d += elm.BatteryCell().left().label("VEB")
    d += elm.Resistor().left().label(RB)
    d += elm.BatteryCell().down().label(VEE)
    d += elm.Line().length(9).right()
    d += elm.BatteryCell().up().label(VEE).reverse()
    d += elm.BatteryCell().up().label(VCC).reverse()
    d += elm.Line().length(2).up()
    d += elm.Resistor().left().label(RC)
    d += elm.BatteryCell().down().label("VEC").reverse()
    d += elm.Line().length(2.5).down()
    d += elm.Resistor().down().label(RE)
    d += elm.Ground()

    return d


def draw_circuit6_PNP_Active(d, RB="RB", VCC="VCC", RC="RC", RE="RE", VEE="VEE"):

    d += elm.BatteryCell().left().label("VEB")
    d += elm.Resistor().left().label(RB)
    d += elm.BatteryCell().down().label(VEE)
    d += elm.Line().length(9).right()
    d += elm.BatteryCell().up().label(VEE).reverse()
    d += elm.BatteryCell().up().label(VCC).reverse()
    d += elm.Line().length(2).up()
    d += elm.Resistor().left().label(RC)
    d += elm.SourceControlledI().label("ib").down().reverse()
    d += elm.Line().length(2.5).down()
    d += elm.Resistor().down().label(RE)
    d += elm.Ground()

    return d


def Analysis_for_circuit6_NPN(VEE, RB, Beta, VCC, RC, RE):
    Ibase = (VEE - 0.7) / (RB + (Beta + 1) * RE)
    if Ibase <= 0:
        return (
            ("off", 0, 0, VCC),
            draw_circuit6_NPN_off,
            "KVL 1: -VEE + (RB)*IB + VBE(ACTIVE) + (Beta + 1)(IB)RE = 0",
        )
    Icollector = Beta * Ibase

    VCE = VCC + VEE - Icollector * (RC + (Beta + 1) * Ibase)
    if VCE > 0.2:
        TEMP = "KVL 1: -VEE + (RB)*IB + VBE(ACTIVE) + (Beta + 1)(IB)RE  = 0 \n KVL 2: -VCC - VEE + RC * IC + VCE + (Beta + 1)(IB)RE = 0 \n IC = BETA * IB"
        return (("Active", Ibase, Icollector, VCE), draw_circuit6_NPN_Active, TEMP)
    else:
        Ibase = (VEE - 0.8) / (RB + (Beta + 1) * RE)
        Icollector = (VCC + VEE - 0.2) / (RC + (Beta + 1) * RE)
        VCE = 0.2
        TEMP = "KVL 1: -VEE + (RB)*IB + VBE(sat) + (Beta + 1)(IB)RE = 0 \n IE = IC + IB"
        return (("Sat", Ibase, Icollector, VCE), draw_circuit6_NPN_Sat, TEMP)


def Analysis_for_circuit6_PNP(VEE, RB, Beta, VCC, RC, RE):
    Ibase = (VEE - 0.7) / (RB + (Beta + 1) * RE)
    if Ibase <= 0:
        return (
            ("off", 0, 0, VCC),
            draw_circuit6_PNP_off,
            "KVL 1: -VEE + (RB)*IB + VEB(ACTIVE) + (Beta + 1)(IB)RE = 0",
        )
    Icollector = Beta * Ibase
    VEC = VCC - Icollector * (RC + (Beta + 1) * Ibase)
    if VEC > 0.2:
        TEMP = "KVL 1: -VEE + (RB)*IB + VEB(ACTIVE) + (Beta + 1)(IB)RE = 0 \n KVL 2: -VCC - VEE + RC * IC + VEC + (Beta + 1)(IB)RE = 0 \n IC = BETA * IB"
        return (("Active", Ibase, Icollector, VEC), draw_circuit6_PNP_Active, TEMP)
    else:
        Ibase = (VEE - 0.8) / (RB + (Beta + 1) * RE)
        Icollector = (VCC - 0.2) / (RC + (Beta + 1) * Ibase)
        VEC = 0.2
        TEMP = "KVL 1: -VEE + (RB)*IB + VEB(sat) + (Beta + 1)(IB)RE = 0 \n IE = IC + IB"
        return (("Sat", Ibase, Icollector, VEC), draw_circuit6_PNP_Sat, TEMP)
