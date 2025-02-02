import schemdraw
import schemdraw.elements as elm
from sympy import symbols, Eq, solve


def draw_circuit2_PNP_off(d, VBB="VBB", Rb="Rb", VCC="VCC", Rc="Rc", Re="Re"):
    d += elm.Dot().at((-1.5033333333333332, 1.8410523547181874e-16))
    d += elm.Resistor().left().label(Rb)
    d += elm.SourceV().down().label(VBB)
    d += elm.Line().length(7).right()
    d += elm.Line().length(0.5).up()
    d += elm.SourceV().up().reverse().label(VCC)
    d += elm.Dot().at((-0.7516666666666665, 0.6966666666666668))
    d += elm.Line().length(0.5).up()
    d += elm.Resistor().right().label(Rc)
    d += elm.Line().length(0.25).right()
    d += elm.Line().length(1.7).down()
    d += elm.Dot().at((-0.7516666666666667, -0.6966666666666665))
    d += elm.Line().length(0).down()
    d += elm.Resistor().down().label(Re)
    d += elm.Line().length(0.4).down()
    d += elm.Ground()
    return d


def draw_circuit2_PNP_Active(d, VBB="VBB", Rb="Rb", VCC="VCC", Rc="Rc", Re="Re"):
    d += elm.Dot().at((-1.5033333333333332, 1.8410523547181874e-16))
    d += elm.BatteryCell().left().reverse().label('Vbe')
    d += elm.Resistor().left().label(Rb)
    d += elm.SourceV().down().label(VBB)
    d += elm.Line().length(10).right()
    d += elm.Line().length(2.5).up()
    d += elm.SourceV().up().reverse().label(VCC)
    d += elm.Dot().at((-0.7516666666666665, 0.6966666666666668))
    d += elm.SourceControlledI().label("ib").reverse()
    d += elm.Resistor().right().label(Rc)
    d += elm.Line().length(0.25).right()
    d += elm.Line().length(1.7).down()
    d += elm.Dot().at((-0.7516666666666667, -0.6966666666666665))
    d += elm.Line().length(0).down()
    d += elm.Resistor().down().label(Re)
    d += elm.Line().length(0.4).down()
    d += elm.Ground()
    return d


def draw_circuit2_PNP_Sat(d, VBB="VBB", Rb="Rb", VCC="VCC", Rc="Rc", Re="Re"):
    d += elm.Dot().at((-1.5033333333333332, 1.8410523547181874e-16))
    d += elm.BatteryCell().left().reverse().label('Vbe')
    d += elm.Resistor().left().label(Rb)
    d += elm.SourceV().down().label(VBB)
    d += elm.Line().length(10).right()
    d += elm.Line().length(2).up()
    d += elm.SourceV().up().reverse().label(VCC)
    d += elm.Dot().at((-0.7516666666666665, 0.6966666666666668))
    d += elm.BatteryCell().label("vce").reverse()
    d += elm.Resistor().right().label(Rc)
    d += elm.Line().length(0.25).right()
    d += elm.Line().length(1.7).down()
    d += elm.Dot().at((-0.7516666666666667, -0.6966666666666665))
    d += elm.Line().length(0).down()
    d += elm.Resistor().down().label(Re)
    d += elm.Line().length(0.4).down()
    d += elm.Ground()
    return d


def draw_circuit2_NPN(d, VBB="VBB", Rb="Rb", VCC="VCC", Rc="Rc", Re="Re"):
    d += elm.SourceV().up().label(VBB)
    d += elm.Resistor().right().label(Rb)
    transistor = d.add(elm.BjtNpn(circle=True).label('Q1').right())
    d += elm.Line().length(1).up()
    d += elm.Line().length(0.5).right()
    d += elm.Resistor().right().label(Rc)
    d += elm.SourceV().down().reverse().label(VCC)
    d += elm.Line().length(1.7).down()
    d += elm.Line().length(7.25).left()
    d += elm.Line().length(0).down().at(transistor.emitter)
    d += elm.Resistor().down().label(Re)
    d += elm.Line().length(0.4).down()
    d += elm.Ground()
    return d


def draw_circuit2_PNP(d, VBB="VBB", Rb="Rb", VCC="VCC", Rc="Rc", Re="Re"):
    transistor = d.add(elm.BjtPnp2(circle=True).label('Q1').reverse())
    d += elm.Resistor().left().label(Rb).at(transistor.base)
    d += elm.SourceV().down().label(VBB)
    d += elm.Line().length(7).right()
    d += elm.Line().length(0.5).up()
    d += elm.SourceV().up().reverse().label(VCC)
    d += elm.Resistor().right().label(Rc).at(transistor.collector)
    d += elm.Line().length(0.21).right()
    d += elm.Line().length(1.7).down()
    d += elm.Resistor().down().label(Re).length(0).down().at(transistor.emitter)
    d += elm.Line().length(0.5).down()
    d += elm.Ground()
    return d


def draw_circuit2_NPN_off(d, VBB="VBB", Rb="Rb", VCC="VCC", Rc="Rc", Re="Re"):
    d += elm.Dot().at((-1.5033333333333332, 1.8410523547181874e-16))
    d += elm.Resistor().left().label(Rb)
    d += elm.SourceV().down().reverse().label(VBB)
    d += elm.Line().length(7).right()
    d += elm.Line().length(0.5).up()
    d += elm.SourceV().up().label(VCC)
    d += elm.Dot().at((-0.7516666666666665, 0.6966666666666668))
    d += elm.Line().length(0.5).up()
    d += elm.Resistor().right().label(Rc)
    d += elm.Line().length(0.25).right()
    d += elm.Line().length(1.7).down()
    d += elm.Dot().at((-0.7516666666666667, -0.6966666666666665))
    d += elm.Line().length(0).down()
    d += elm.Resistor().down().label(Re)
    d += elm.Line().length(0.4).down()
    d += elm.Ground()
    return d


def draw_circuit2_NPN_Active(d, VBB="VBB", Rb="Rb", VCC="VCC", Rc="Rc", Re="Re"):
    d += elm.Dot().at((-1.5033333333333332, 1.8410523547181874e-16))
    d += elm.BatteryCell().left().reverse().label('Vbe')
    d += elm.Resistor().left().label(Rb)
    d += elm.SourceV().down().reverse().label(VBB)
    d += elm.Line().length(10).right()
    d += elm.Line().length(2.5).up()
    d += elm.SourceV().up().label(VCC)
    d += elm.Dot().at((-0.7516666666666665, 0.6966666666666668))
    d += elm.SourceControlledI().label("ib").reverse()
    d += elm.Resistor().right().label(Rc)
    d += elm.Line().length(0.25).right()
    d += elm.Line().length(1.7).down()
    d += elm.Dot().at((-0.7516666666666667, -0.6966666666666665))
    d += elm.Line().length(0).down()
    d += elm.Resistor().down().label(Re)
    d += elm.Line().length(0.4).down()
    d += elm.Ground()
    return d


def draw_circuit2_NPN_Sat(d, VBB="VBB", Rb="Rb", VCC="VCC", Rc="Rc", Re="Re"):
    d += elm.Dot().at((-1.5033333333333332, 1.8410523547181874e-16))
    d += elm.BatteryCell().left().reverse().label('Vbe')
    d += elm.Resistor().left().label(Rb)
    d += elm.SourceV().down().reverse().label(VBB)
    d += elm.Line().length(10).right()
    d += elm.Line().length(2).up()
    d += elm.SourceV().up().label(VCC)
    d += elm.Dot().at((-0.7516666666666665, 0.6966666666666668))
    d += elm.BatteryCell().label("vce").reverse()
    d += elm.Resistor().right().label(Rc)
    d += elm.Line().length(0.25).right()
    d += elm.Line().length(1.7).down()
    d += elm.Dot().at((-0.7516666666666667, -0.6966666666666665))
    d += elm.Line().length(0).down()
    d += elm.Resistor().down().label(Re)
    d += elm.Line().length(0.4).down()
    d += elm.Ground()
    return d


def Analysis_for_circuit2_NPN(VBB, RB, RE, Beta, VCC, RC):
    Ibase = (VBB-0.7)/(RB + RE*(Beta+1))
    if Ibase <= 0:
        return ((("off", 0, 0, VCC), draw_circuit2_NPN_off, "KVL 1: -VBB + (RB)*IB + (RE)*IE + VBE(ACTIVE) = 0"))
    Icollector = Beta * Ibase
    VCE = VCC - Icollector * (RC + ((Beta+1)/Beta)*RE)
    if VCE > 0.2:
        TEMP = "KVL 1: -VBB + (RB)*IB + VBE(ACTIVE) +(RE)*IE  = 0\n" + \
            "KVL 2: -VCC + (RC)*IC +  VCE  + (RE)*IE = 0 \n IC=BETA*IB"
        return ((("Active", Ibase, Icollector, VCE), draw_circuit2_NPN_Active, TEMP))
    else:
        Ibase, Icollector = symbols('Ibase,Icollector')
        eq1 = Eq(Ibase*(RB + RE) + Icollector*RE, VBB-0.8)
        eq2 = Eq(Ibase*RB + Icollector*(RC + RE), VCC-0.2)
        sol = solve((eq1, eq2), (Ibase, Icollector))
        TEMP = "KVL 1: -VBB + (RB)*IB  + VBE(SAT) + (RE)*IE = 0\n" + \
            "KVL 2: -VCC + (RC)*IC +  VCE  + (RE)*IE = 0 \n IE=IB + IC"
        return ((("Sat", sol[Ibase], sol[Icollector], 0.2), draw_circuit2_NPN_Sat, TEMP))


def Analysis_for_circuit2_PNP(VBB, RB, RE, Beta, VCC, RC):
    Ibase = (0.7 - VBB) / (RB + RE * (Beta + 1))
    if Ibase >= 0:
        return ((("off", 0, 0, VCC), draw_circuit2_PNP_off, "KVL 1: +VBB - (RB)*IB - (RE)*IE - VEB(ACTIVE) = 0"))
    Icollector = Beta * Ibase
    VCE = VCC - Icollector * (RC + ((Beta + 1) / Beta) * RE)

    if VCE > 0.2:
        TEMP = "KVL 1: +VBB - (RB)*IB - VEB(ACTIVE) -(RE)*IE  = 0\n" + \
            "KVL 2: +VCC - (RC)*IC -  VEC - (RE)*IE = 0 \n IC=BETA*IB"
        return ((("Active", Ibase, Icollector, VCE), draw_circuit2_PNP_Active, TEMP))
    else:
        Ibase, Icollector = symbols('Ibase Icollector')
        eq1 = Eq(Ibase * (RB + RE) + Icollector * RE, 0.7 - VBB)
        eq2 = Eq(Ibase * RB + Icollector * (RC + RE), VCC - 0.2)
        sol = solve((eq1, eq2), (Ibase, Icollector))
        TEMP = "KVL 1: +VBB - (RB)*IB - VEB(SAT) -(RE)*IE = 0\n" + \
            "KVL 2: +VCC - (RC)*IC -  VEC - (RE)*IE = 0 \n IE=IB + IC"
        return ((("Sat", sol[Ibase], sol[Icollector], 0.2), draw_circuit2_PNP_Sat, TEMP))
