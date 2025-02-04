import schemdraw
import schemdraw.elements as elm




def draw_circuit4_PNP_off(d,RB="RB",RC="RC",VCC="VCC"):

    d+= elm.Dot().at((-1.5033333333333332,1.8410523547181874e-16))
    d += elm.Line().length(2.25).left()
    d += elm.Resistor().up().label(RB)
    d += elm.Line().length(3).right()
    d += elm.Dot().at((-0.7516666666666665,0.6966666666666668))
    d += elm.Resistor().up().label(RC)
    d += elm.Line().length(2.5).right()
    d += elm.Line().length(1).down()
    d += elm.BatteryCell().down().label(VCC).reverse()
    d += elm.Line().length(2).down()
    d += elm.Line().length(2.5).left()
    d += elm.Dot().at((-0.7516666666666667,-0.6966666666666665))
    d += elm.Line().length(1.8).down()
    d += elm.Ground()
    return d
    
def draw_circuit4_PNP_Active(d,RB="RB",RC="RC",VCC="VCC"):
    d += elm.BatteryCell().left().label('VEB').at((-0.76,0.7))
    d += elm.Line().length(0.5).left()
    d += elm.Line().length(1).up()
    d += elm.Resistor().up().label(RB)
    d += elm.Line().length(1.45).up()
    d += elm.Line().length(3.5).right()
    d += elm.Line().length(0.01).up().at((-0.7516666666666665,0.6966666666666668))
    d += elm.SourceControlledI().label("BETA*IB")
    d += elm.Resistor().up().label(RC)
    d += elm.Line().length(2.5).right()
    d += elm.Line().length(1).down()
    d += elm.BatteryCell().down().label(VCC).reverse()
    d += elm.Line().length(2.7).down()
    d += elm.Line().length(2.5).left()
    d += elm.Line().length(1).down().at((-0.7516666666666667,0.7))
    d += elm.Ground()
    return d

def draw_circuit4_PNP_Sat(d,RB="RB",RC="RC",VCC="VCC"):
    d += elm.BatteryCell().left().label('VEB').at((-0.76,0.7))
    d += elm.Line().length(0.5).left()
    d += elm.Line().length(1).up()
    d += elm.Resistor().up().label(RB)
    d += elm.Line().length(1.45).up()
    d += elm.Line().length(3.5).right()
    d += elm.Line().length(0).up().at((-0.7516666666666665,0.6966666666666668))
    d += elm.BatteryCell().label("VEC")
    d += elm.Resistor().up().label(RC)
    d += elm.Line().length(2.5).right()
    d += elm.Line().length(1).down()
    d += elm.BatteryCell().label(VCC).reverse()
    d += elm.Line().length(2.7).down()
    d += elm.Line().length(2.5).left()
    d += elm.Line().length(1).down().at((-0.7516666666666667,0.7))
    d += elm.Ground()
    return d
    

def draw_circuit4_NPN(d,RB="RB",RC="RC",VCC="VCC"):

    transistor = d.add( elm.BjtNpn(circle=True).label('Q1').right() )
    d += elm.Line().length(2.25).left().at(transistor.base)
    d += elm.Resistor().up().label(RB)
    d += elm.Line().length(3).right()
    d += elm.Resistor().up().label(RC).at(transistor.collector)
    d += elm.Line().length(2.5).right()
    d += elm.Line().length(1).down()
    d += elm.BatteryCell().down().label(VCC)
    d += elm.Line().length(2).down()
    d += elm.Line().length(2.5).left()
    
    d += elm.Line().length(1.8).down().at(transistor.emitter)
    d += elm.Ground()
    return d

def draw_circuit4_PNP(d,RB="RB",RC="RC",VCC="VCC"):
    
    transistor = d.add( elm.BjtPnp2(circle=True).label('Q1').reverse() )
    d += elm.Line().length(2.25).left().at(transistor.base)
    d += elm.Resistor().up().label(RB)
    d += elm.Line().length(1).up()
    d += elm.Line().length(3).right()
    d += elm.Resistor().up().label(RC).at(transistor.collector)
    d += elm.Line().length(2.5).right()
    d += elm.Line().length(1).down()
    d += elm.BatteryCell().down().label(VCC).reverse()
    d += elm.Line().length(2).down()
    d += elm.Line().length(2.5).left()
    d += elm.Line().length(1).down().at(transistor.emitter)
    d += elm.Ground()
    return d

def draw_circuit4_NPN_off(d,RB="RB",RC="RC",VCC="VCC"):

    d+= elm.Dot().at((-1.5033333333333332,1.8410523547181874e-16))
    d += elm.Line().length(2.25).left()
    d += elm.Resistor().up().label(RB)
    d += elm.Line().length(3).right()
    d += elm.Dot().at((-0.7516666666666665,0.6966666666666668))
    d += elm.Resistor().up().label(RC)
    d += elm.Line().length(2.5).right()
    d += elm.Line().length(1).down()
    d += elm.BatteryCell().down().label(VCC)
    d += elm.Line().length(2).down()
    d += elm.Line().length(2.5).left()
    d += elm.Dot().at((-0.7516666666666667,-0.6966666666666665))
    d += elm.Line().length(1.8).down()
    d += elm.Ground()
    return d

    
def draw_circuit4_NPN_Active(d,RB="RB",RC="RC",VCC="VCC"):
    d += elm.BatteryCell().left().reverse().label('VBE').at((-0.76,0.7))
    d += elm.Line().length(0.5).left()
    d += elm.Line().length(1).up()
    d += elm.Resistor().up().label(RB)
    d += elm.Line().length(1.45).up()
    d += elm.Line().length(3.50).right()
    d += elm.Line().length(0.01).up().at((-0.7516666666666665,0.6966666666666668))
    d += elm.SourceControlledI().label("BETA*IB").reverse()
    d += elm.Resistor().up().label(RC)
    d += elm.Line().length(2.5).right()
    d += elm.Line().length(1).down()
    d += elm.BatteryCell().down().label(VCC)
    d += elm.Line().length(2.7).down()
    d += elm.Line().length(2.5).left()
    d += elm.Line().length(1).down().at((-0.7516666666666667,0.7))
    d += elm.Ground()
    return d

def draw_circuit4_NPN_Sat(d,RB="RB",RC="RC",VCC="VCC"):
    d += elm.BatteryCell().left().reverse().label('VBE').at((-0.76,0.7))
    d += elm.Line().length(0.5).left()
    d += elm.Line().length(1).up()
    d += elm.Resistor().up().label(RB)
    d += elm.Line().length(1.45).up()
    d += elm.Line().length(3.5).right()
    d += elm.Line().length(0).up().at((-0.7516666666666665,0.6966666666666668))
    d += elm.BatteryCell().label("VCE").reverse()
    d += elm.Resistor().up().label(RC)
    d += elm.Line().length(2.5).right()
    d += elm.Line().length(1).down()
    d += elm.BatteryCell().down().label(VCC)
    d += elm.Line().length(2.7).down()
    d += elm.Line().length(2.5).left()
    d += elm.Line().length(1).down().at((-0.7516666666666667,0.7))
    d += elm.Ground()
    return d

def Analysis_for_circuit4_NPN(RB,Beta,VCC,RC):
    Ibase = (VCC-0.7)/ RB
    if Ibase <= 0 :
        TEMP = "KVL 1: -VCC +  (IB) * RB + VBE(ACTIVE) = 0"
        return(("off",0,0,VCC),draw_circuit4_NPN_off,TEMP)
    Icollector = Beta * Ibase
    VCE = VCC - Icollector* RC
    if VCE > 0.2 :
        TEMP = "KVL 1: -VCC  + (IB) * RB + VBE(ACTIVE) = 0 \n KVL 2: -VCC + (IC) * RC  + VCE = 0 \n IC = BETA * IB"
        return(("Active",Ibase,Icollector,VCE),draw_circuit4_NPN_Active,TEMP)
    else:
        Ibase = (VCC-0.8)/ RB
        Icollector = (VCC - 0.2) / RC
        VCE = 0.2
        TEMP = "KVL 1: -VCC + (IB) * RB + VBE(SAT) = 0 \n KVL 2: -VCC + (IC) * RC  + VCE(SAT) = 0 \n IE = IB + IC"
        return(("Sat",Ibase,Icollector,VCE),draw_circuit4_NPN_Sat,TEMP)

def Analysis_for_circuit4_PNP(RB,Beta,VCC,RC):
    Ibase = (VCC-0.7)/ RB
    if Ibase <= 0 :
        TEMP = "KVL 1: VCC -  (IB) * RB - VEB(ACTIVE) = 0"
        return(("off",0,0,VCC),draw_circuit4_PNP_off,TEMP)
    Icollector = Beta * Ibase
    VEC = VCC - Icollector* RC
    if VEC > 0.2 :
        TEMP = "KVL 1: VCC  - (IB) * RB - VEB(ACTIVE) = 0 \n KVL 2: VCC - (IC) * RC  - VEC = 0 \n IC = BETA * IB"
        return(("Active",Ibase,Icollector,VEC),draw_circuit4_PNP_Active,TEMP)
    else:
        Ibase = (VCC-0.8)/ RB
        Icollector = (VCC - 0.2) / RC
        VEC = 0.2
        TEMP = "KVL 1: VCC - (IB) * RB - VEB(SAT) = 0 \n KVL 2: VCC - (IC) * RC  - VEC(SAT) = 0 \n IE = IB + IC"
        return(("Sat",Ibase,Icollector,VEC),draw_circuit4_PNP_Sat,TEMP)

