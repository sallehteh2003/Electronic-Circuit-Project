import schemdraw
import schemdraw.elements as elm


def draw_circuit1_PNP_off(d,RB="RB",VCC="VCC",RC="RC",VBB="VBB"):
    d+= elm.Dot().at((-1.5033333333333332,1.8410523547181874e-16))
    d += elm.Resistor().left().label(RB)
    d += elm.BatteryCell().down().label(VBB).reverse()
    d += elm.Line().length(7).right()
    d += elm.Line().length(0.5).up()
    d += elm.BatteryCell().up().label(VCC)
    d += elm.Dot().at((-0.7516666666666665,0.6966666666666668))
    d += elm.Line().length(0.5).up()
    d += elm.Resistor().right().label(RC)
    d += elm.Line().length(0.25).right()
    d += elm.Line().length(1.7).down()
    d += elm.Dot().at((-0.7516666666666667,-0.6966666666666665))
    d += elm.Line().length(2.5).down()
    d += elm.Ground()
    return d
    
def draw_circuit1_PNP_Active(d,RB="RB",VCC="VCC",RC="RC",VBB="VBB"):
    d += elm.BatteryCell().left().label('VEB')
    d += elm.Resistor().left().label(RB)
    d += elm.BatteryCell().down().label(VBB).reverse()
    d += elm.Line().length(9).right()
    d += elm.Line().length(0.5).up()
    d += elm.BatteryCell().up().label(VCC)
    d += elm.Line().length(2).up()
    d += elm.Resistor().left().label(RC)
    d += elm.SourceControlledI().label("ib").down().reverse()
    d += elm.Line().length(3).down()
    d += elm.Ground()
    return d

def draw_circuit1_PNP_Sat(d,RB="RB",VCC="VCC",RC="RC",VBB="VBB"):
    d += elm.BatteryCell().left().label('VEB')
    d += elm.Resistor().left().label(RB)
    d += elm.BatteryCell().down().label(VBB).reverse()
    d += elm.Line().length(9).right()
    d += elm.Line().length(0.5).up()
    d += elm.BatteryCell().up().label(VCC)
    d += elm.Line().length(2).up()
    d += elm.Resistor().left().label(RC)
    d += elm.BatteryCell().label("VEC").down().reverse()
    d += elm.Line().length(3).down()
    d += elm.Ground()
    return d
    

def draw_circuit1_NPN(d,RB="RB",VCC="VCC",RC="RC",VBB="VBB"):
    d += elm.BatteryCell().up().label(VBB).reverse()
    d += elm.Resistor().right().label(RB)
    transistor = d.add( elm.BjtNpn(circle=True).label('Q1').right() )
    d += elm.Line().length(1).up()
    d += elm.Line().length(0.5).right()
    d += elm.Resistor().right().label(RC)
    d += elm.BatteryCell().down().label(VCC)
    d += elm.Line().length(1.7).down()
    d += elm.Line().length(7.25).left()
    d += elm.Line().length(2.8).down().at(transistor.emitter)
    d += elm.Ground()
    return d

def draw_circuit1_PNP(d,RB="RB",VCC="VCC",RC="RC",VBB="VBB"):
    transistor = d.add( elm.BjtPnp2(circle=True).label('Q1').reverse())
    d += elm.Resistor().left().label(RB).at(transistor.base)
    d += elm.BatteryCell().down().label(VBB).reverse()
    d += elm.Line().length(7).right()
    d += elm.Line().length(0.5).up()
    d += elm.BatteryCell().up().label(VCC)
    d += elm.Resistor().right().label(RC).at(transistor.collector)
    d += elm.Line().length(0.21).right()
    d += elm.Line().length(1.7).down()
    d += elm.Line().length(2).down().at(transistor.emitter)
    d += elm.Ground()
    return d

def draw_circuit1_NPN_off(d,RB="RB",VCC="VCC",RC="RC",VBB="VBB"):
    d+= elm.Dot().at((-1.5033333333333332,1.8410523547181874e-16))
    d += elm.Resistor().left().label(RB)
    d += elm.BatteryCell().down().label(VBB)
    d += elm.Line().length(7).right()
    d += elm.Line().length(0.5).up()
    d += elm.BatteryCell().up().label(VCC).reverse()
    d += elm.Dot().at((-0.7516666666666665,0.6966666666666668))
    d += elm.Line().length(0.5).up()
    d += elm.Resistor().right().label(RC)
    d += elm.Line().length(0.25).right()
    d += elm.Line().length(1.7).down()
    d += elm.Dot().at((-0.7516666666666667,-0.6966666666666665))
    d += elm.Line().length(2.5).down()
    d += elm.Ground()
    return d
    
def draw_circuit1_NPN_Active(d,RB="RB",VCC="VCC",RC="RC",VBB="VBB"):
   
    d += elm.BatteryCell().left().reverse().label('Vbe')
    d += elm.Resistor().left().label(RB)
    d += elm.BatteryCell().down().label(VBB)
    d += elm.Line().length(9).right()
    d += elm.Line().length(0.5).up()
    d += elm.BatteryCell().up().label(VCC).reverse()
    d += elm.Line().length(2).up()
    d += elm.Resistor().left().label(RC)
    d += elm.SourceControlledI().label("ib").down()
    d += elm.Line().length(3).down()
    d += elm.Ground()
    return d

def draw_circuit1_NPN_Sat(d,RB="RB",VCC="VCC",RC="RC",VBB="VBB"):
    d += elm.BatteryCell().left().reverse().label('Vbe')
    d += elm.Resistor().left().label(RB)
    d += elm.BatteryCell().down().label(VBB)
    d += elm.Line().length(9).right()
    d += elm.Line().length(0.5).up()
    d += elm.BatteryCell().up().label(VCC).reverse()
    d += elm.Line().length(2).up()
    d += elm.Resistor().left().label(RC)
    d += elm.BatteryCell().label("VCE").down()
    d += elm.Line().length(3).down()
    d += elm.Ground()
    return d

  
def Analysis_for_circuit1_NPN(VBB,RB,Beta,VCC,RC):
    Ibase = (VBB-0.7)/RB
    if Ibase <= 0 :
        return((("off",0,0,VCC),draw_circuit1_NPN_off,"KVL 1: -VBB + (RB)*IB + VBE(ACTIVE) = 0"))
    Icollector = Beta * Ibase


    VCE = VCC - Icollector* RC
    if VCE > 0.2 :
        TEMP = "KVL 1: -VBB + (RB)*IB + VBE(ACTIVE) = 0 \n KVL 2: -VCC + RC * IC + VCE = 0 \n IC = BETA * IB"
        return((("Active",Ibase,Icollector,VCE),draw_circuit1_NPN_Active,TEMP))
    else:
        Ibase = (VBB-0.8)/RB
        Icollector = (VCC - 0.2) / RC
        VCE = 0.2
        TEMP = "KVL 1: -VBB + (RB)*IB + VBE(sat) = 0 \n IE = IC + IB"
        return((("Sat",Ibase,Icollector,VCE),draw_circuit1_NPN_Sat,TEMP))

def Analysis_for_circuit1_PNP(VBB,RB,Beta,VCC,RC):
    Ibase = (VBB-0.7)/RB
    if Ibase <= 0 :
        return((("off",0,0,VCC),draw_circuit1_PNP_off,"KVL 1: -VBB + (RB)*IB + VBE(ACTIVE) = 0"))
    Icollector = Beta * Ibase
    VEC = VCC - Icollector* RC
    if VEC > 0.2 :
        TEMP = "KVL 1: -VBB + (RB)*IB + VEB(ACTIVE) = 0 \n KVL 2: -VCC + RC * IC + VEC = 0 \n IC = BETA * IB"
        return((("Active",Ibase,Icollector,VEC),draw_circuit1_PNP_Active,TEMP))
    else:
        Ibase = (VBB-0.8)/RB
        Icollector = (VCC - 0.2) / RC
        VEC = 0.2
        TEMP = "KVL 1: -VBB + (RB)*IB + VEB(sat) = 0 \n IE = IC + IB"
        return((("Sat",Ibase,Icollector,VEC),draw_circuit1_PNP_Sat,TEMP))


