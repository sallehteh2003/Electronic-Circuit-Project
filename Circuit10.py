import schemdraw
import schemdraw.elements as elm
from sympy import symbols, Eq, solve


def draw_circuit10_PNP(d,RB1="RB1",RB2="RB2",VCC="VCC",RC="RC",VEE="VEE",RE="RE"):
    transistor = d.add( elm.BjtPnp2(circle=False).label('Q1').reverse())
    d += elm.Line().length(0.5).left().at(transistor.base)
    d += elm.Resistor().up().label(RB1)
    d += elm.Line().length(2).left()
    d += elm.BatteryCell().down().label(VCC).reverse()
    d += elm.Line().length(0.5).left()
    d += elm.Ground()
    d += elm.Line().length(0.5).right()
    d += elm.BatteryCell().down().reverse().label(VEE)
    d += elm.Line().length(2).right()
    d += elm.Resistor().up().label(RB2)
    d += elm.Line().length(1.5).down().at(transistor.emitter)
    d += elm.Resistor().right().label(RE)
    d += elm.BatteryCell().up().label(VEE)
    d += elm.Line().length(0.5).right()
    d += elm.Ground()
    d += elm.Line().length(0.5).left()
    d += elm.BatteryCell().up().label(VCC)
    d += elm.Line().length(1.5).up().at(transistor.collector)
    d += elm.Resistor().right().label(RC,'bottom')
    return d

def draw_circuit10_PNP_ACTIVE(d,RB1="RB1",RB2="RB2",VCC="VCC",RC="RC",VEE="VEE",RE="RE"):
    Battery = d.add( elm.BatteryCell().left().label('VEB(ACTIVE)').scale(0.7))
    d += elm.Resistor().up().label(RB1)
    d += elm.Line().length(2).left()
    d += elm.BatteryCell().down().label(VCC).reverse()
    d += elm.Line().length(0.5).left()
    d += elm.Ground()
    d += elm.Line().length(0.5).right()
    d += elm.BatteryCell().down().reverse().label(VEE)
    d += elm.Line().length(2).right()
    d += elm.Resistor().up().label(RB2)
    d += elm.Resistor().down().label(RE).at(Battery.start)
    d += elm.Line().length(3).right()
    d += elm.BatteryCell().up().label(VEE)
    d += elm.Line().length(0.5).right()
    d += elm.Ground()
    d += elm.Line().length(0.5).left()
    d += elm.BatteryCell().up().label(VCC)
    d += elm.SourceControlledI().up().label("Beta IB").at(Battery.start)
    d += elm.Resistor().right().label(RC)
    return d

def draw_circuit10_PNP_SAT(d,RB1="RB1",RB2="RB2",VCC="VCC",RC="RC",VEE="VEE",RE="RE"):
    Battery = d.add( elm.BatteryCell().left().label('VEB(SAT)').scale(0.7))
    d += elm.Resistor().up().label(RB1)
    d += elm.Line().length(2).left()
    d += elm.BatteryCell().down().label(VCC).reverse()
    d += elm.Line().length(0.5).left()
    d += elm.Ground()
    d += elm.Line().length(0.5).right()
    d += elm.BatteryCell().down().reverse().label(VEE)
    d += elm.Line().length(2).right()
    d += elm.Resistor().up().label(RB2)
    d += elm.Resistor().down().label(RE).at(Battery.start)
    d += elm.Line().length(3).right()
    d += elm.BatteryCell().up().label(VEE)
    d += elm.Line().length(0.5).right()
    d += elm.Ground()
    d += elm.Line().length(0.5).left()
    d += elm.BatteryCell().up().label(VCC)
    d += elm.BatteryCell().up().label("VEC(SAT)").at(Battery.start)
    d += elm.Resistor().right().label(RC)
    return d


def draw_circuit10_PNP_off(d,RB1="RB1",RB2="RB2",VCC="VCC",RC="RC",VEE="VEE",RE="RE"):
    d += elm.Resistor().up().label(RB1)
    d += elm.Line().length(2).left()
    d += elm.BatteryCell().down().label(VCC).reverse()
    d += elm.Line().length(0.5).left()
    d += elm.Ground()
    d += elm.Line().length(0.5).right()
    d += elm.BatteryCell().down().reverse().label(VEE)
    d += elm.Line().length(2).right()
    d += elm.Resistor().up().label(RB2)
    d += elm.Line().length(0.5).right()
    d += elm.Dot().label("B")
    d += elm.Line().length(0.5).left()
    d += elm.Dot().label("E",'right').at((1,-0.5))
    d += elm.Resistor().down().label(RE,'bottom')
    d += elm.Line().length(3).right()
    d += elm.BatteryCell().up().label(VEE)
    d += elm.Line().length(0.5).right()
    d += elm.Ground()
    d += elm.Line().length(0.5).left()
    d += elm.BatteryCell().up().label(VCC)
    d += elm.Resistor().left().label(RC)
    d += elm.Line().length(2).down()
    d += elm.Dot().label("C",'right')
    return d

def draw_circuit10_NPN(d,RB1="RB1",RB2="RB2",VCC="VCC",RC="RC",VEE="VEE",RE="RE"):
   
    d += elm.BatteryCell().down().label(VCC)
    d += elm.Line().length(0.5).left()
    d += elm.Ground()
    d += elm.Line().length(0.5).right()
    d += elm.BatteryCell().down().label(VEE)
    d += elm.Line().length(2).right()
    d += elm.Resistor().up().label(RB2)
    d += elm.Line().length(0.5).right()
    transistor = d.add( elm.BjtNpn(circle=False).label('Q1').right())
    d += elm.Line().length(0.5).left().at(transistor.base)
    d += elm.Resistor().up().label(RB1)
    d += elm.Line().length(2).left()
    d += elm.Resistor().down().label(RE).at(transistor.emitter)
    d += elm.Line().length(2).right()
    d += elm.BatteryCell().up().reverse().label(VEE)
    d += elm.Line().length(0.5).right()
    d += elm.Ground()
    d += elm.Line().length(0.5).left()
    d += elm.BatteryCell().up().label(VCC).reverse()
    d += elm.Line().length(1.41).up()
    d += elm.Line().length(2).left()
    d += elm.Resistor().up().label(RC).at(transistor.collector)
    return d
    
    
def draw_circuit10_NPN_ACTIVE(d,RB1="RB1",RB2="RB2",VCC="VCC",RC="RC",VEE="VEE",RE="RE"):
    d += elm.BatteryCell().down().label(VCC)
    d += elm.Line().length(0.5).left()
    d += elm.Ground()
    d += elm.Line().length(0.5).right()
    d += elm.BatteryCell().down().label(VEE)
    d += elm.Line().length(2).right()
    d += elm.Resistor().up().label(RB2)
    Battery = d.add( elm.BatteryCell().right().label('VBE(ACTIVE)').scale(0.7))
    d += elm.Resistor().up().label(RB1).at(Battery.start)
    d += elm.Line().length(2).left()
    d += elm.Resistor().down().label(RE).at(Battery.end)
    d += elm.Line().length(3).right()
    d += elm.BatteryCell().up().reverse().label(VEE)
    d += elm.Line().length(0.5).right()
    d += elm.Ground()
    d += elm.Line().length(0.5).left()
    d += elm.BatteryCell().up().label(VCC).reverse()
    d += elm.Resistor().left().label(RC)
    d += elm.SourceControlledI().down().label("Beta IB")
    return d

def draw_circuit10_NPN_SAT(d,RB1="RB1",RB2="RB2",VCC="VCC",RC="RC",VEE="VEE",RE="RE"):
    d += elm.BatteryCell().down().label(VCC)
    d += elm.Line().length(0.5).left()
    d += elm.Ground()
    d += elm.Line().length(0.5).right()
    d += elm.BatteryCell().down().label(VEE)
    d += elm.Line().length(2).right()
    d += elm.Resistor().up().label(RB2)
    Battery = d.add( elm.BatteryCell().right().label('VBE(ACTIVE)').scale(0.7))
    d += elm.Resistor().up().label(RB1).at(Battery.start)
    d += elm.Line().length(2).left()
    d += elm.Resistor().down().label(RE).at(Battery.end)
    d += elm.Line().length(3).right()
    d += elm.BatteryCell().up().reverse().label(VEE)
    d += elm.Line().length(0.5).right()
    d += elm.Ground()
    d += elm.Line().length(0.5).left()
    d += elm.BatteryCell().up().label(VCC).reverse()
    d += elm.Resistor().left().label(RC)
    d += elm.BatteryCell().down().label("VCE (sat)")
    return d
    
def draw_circuit10_NPN_OFF(d,RB1="RB1",RB2="RB2",VCC="VCC",RC="RC",VEE="VEE",RE="RE"):
    d += elm.BatteryCell().down().label(VCC)
    d += elm.Line().length(0.5).left()
    d += elm.Ground()
    d += elm.Line().length(0.5).right()
    d += elm.BatteryCell().down().label(VEE)
    d += elm.Line().length(2).right()
    d += elm.Resistor().up().label(RB2)
    d += elm.Line().length(0.5).right()
    d += elm.Dot().label("B")
    d += elm.Line().length(0.5).left()
    d += elm.Resistor().up().label(RB1)
    d += elm.Line().length(2).left()
    d += elm.Dot().label("E",'right').at((3.2,-3.5))
    d += elm.Resistor().down().label(RE)
    d += elm.Line().length(3).right()
    d += elm.BatteryCell().up().reverse().label(VEE)
    d += elm.Line().length(0.5).right()
    d += elm.Ground()
    d += elm.Line().length(0.5).left()
    d += elm.BatteryCell().up().label(VCC).reverse()
    d += elm.Resistor().left().label(RC)
    d += elm.Line().length(2).down()
    d += elm.Dot().label("C",'right')
    return d


def Analysis_for_circuit10_NPN(RB2,RB1,VEE,VCC,RC,RE,BETA):
    VTH = (RB2/(RB1+RB2))*(VCC+VEE)- VEE
    RTH = (RB1*RB2)/(RB1+RB2)
    IB = (VEE+VTH-0.7)/(RTH+((BETA+1)*RE))
    if IB <= 0 :
        return((("off",0,0,VCC+VEE),draw_circuit10_NPN_OFF,"KVL 1: -VBB + (RB)*IB + VBE(ACTIVE) = 0"))
    IC = BETA * IB
    VCE = VCC + VEE -  (IC * ( RC + ((BETA+1) / BETA *RE)))
    if VCE > 0.2 :
        TEMP = "KVL 1: -VTH + (RTH)*IB + VBE(ACTIVE) + RE * (BETA + 1) * IB = 0 \n KVL 2: -VCC + RC * IC + VCE + RE * (BETA + 1/ BETA) -VEE  = 0 \n IC = BETA * IB"
        return((("Active",IB,IC,VCE),draw_circuit10_NPN_ACTIVE,TEMP))
    else:
        IC, IB = symbols('IC IB')
        eq1 = Eq( -VTH + RTH * IB + 0.8 + (IC + IB) * RE -VEE , 0 )
        eq2 = Eq( -VCC + IC * RC + 0.2 + RE * (IC + IB) , 0 )
        solution = solve((eq1, eq2), (IC ,IB))
        TEMP = "KVL 1: -VTH + (RTH)*IB + VBE(sat) + RE * IE - VEE = 0 \n KVL 2: -VCC + IC *RC + VCE(SAT) + IE * RE   \n IE = IC + IB"
        return((("Sat",solution[IC],solution[IB],0.2),draw_circuit10_NPN_SAT,TEMP))

def Analysis_for_circuit10_PNP(RB2,RB1,VEE,VCC,RC,RE,BETA):
        VTH = (RB2/(RB1+RB2))*( (-1 * (VCC + VEE) )) + VEE
        RTH = (RB1*RB2)/(RB1+RB2)
        IB = (VEE-VTH-0.7)/(RTH+((BETA+1)*RE))
        if IB <= 0 :
            return((("off",0,0,VCC+VEE),draw_circuit10_PNP_off,"KVL 1: -VBB + (RB)*IB + VEB(ACTIVE) = 0"))
        IC = BETA * IB
        VEC = VCC + VEE -  (IC * ( RC + ((BETA+1) / BETA *RE)))
        if VEC > 0.2 :
            TEMP = "KVL 1: -VTH + (RTH)*IB + VEB(ACTIVE) + RE * (BETA + 1) * IB = 0 \n KVL 2: -VCC + RC * IC + VEC + RE * (BETA + 1/ BETA) -VEE  = 0 \n IC = BETA * IB"
            return((("Active",IB,IC,VEC),draw_circuit10_PNP_ACTIVE,TEMP))
        else:
            IC, IB = symbols('IC IB')
            eq1 = Eq( +VTH + RTH * IB + 0.8 + (IC + IB) * RE -VEE , 0 )
            eq2 = Eq( -VCC + IC * RC + 0.2 + RE * (IC + IB) , 0 )
            solution = solve((eq1, eq2), (IC ,IB))
            TEMP = "KVL 1: +VTH + (RTH)*IB + VEB(sat) + RE * IE - VEE = 0 \n KVL 2: -VCC + IC *RC + VEC(SAT) + IE * RE   \n IE = IC + IB"
            return((("Sat",solution[IC],solution[IB],0.2),draw_circuit10_PNP_SAT,TEMP))
