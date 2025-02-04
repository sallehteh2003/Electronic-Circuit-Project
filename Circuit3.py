import schemdraw
import schemdraw.elements as elm




def draw_circuit3_PNP_off(d,RB="RB",RC="RC",VCC="VCC"):

    d+= elm.Dot().at((-1.5033333333333332,1.8410523547181874e-16))
    d += elm.Line().length(2.25).left()
    d += elm.Line().length(1.5).up()
    d += elm.Resistor().right().label(RB)
    d += elm.Dot().at((-0.7516666666666665,0.6966666666666668))
    d += elm.Line().length(1.4).up()
    d += elm.Line().length(0.5).right()
    d += elm.Resistor().right().label(RC)
    d += elm.BatteryCell().down().label(VCC).reverse()
    d += elm.Line().length(0.7).down()
    d += elm.Line().length(3.5).left()
    d += elm.Dot().at((-0.7516666666666667,-0.6966666666666665))
    d += elm.Line().length(1.8).down()
    d += elm.Ground()
    return d
    
def draw_circuit3_PNP_Active(d,RB="RB",RC="RC",VCC="VCC"):
    d += elm.BatteryCell().left().label('VEB').at((-0.76,0.7))
    d += elm.Line().length(0.5).left()
    d += elm.Line().length(2.7).up()
    d += elm.Line().length(0.5).right()
    d+= elm.Resistor().right().label(RB)
    d += elm.SourceControlledI().label("BETA*IB").at((-0.7516666666666665,0.6966666666666668))
    d += elm.Line().length(0.5).right()
    d += elm.Resistor().right().label(RC)
    d += elm.BatteryCell().down().label(VCC).reverse()
    d += elm.Line().length(1.3).down()
    d += elm.Line().length(3.5).left()
    d += elm.Line().length(1.2).down().at((-0.7516666666666667,0.7))
    d += elm.Ground()
    return d

    


def draw_circuit3_PNP_Sat(d,RB="RB",RC="RC",VCC="VCC"):
    
    d += elm.BatteryCell().left().label('VEB').at((-0.76,0.7))
    d += elm.Line().length(0.5).left()
    d += elm.Line().length(2.7).up()
    d += elm.Line().length(0.5).right()
    Rb = d.add(elm.Resistor().right().label(RB))
    d += elm.Line().length(0.01).up().at((-0.7516666666666665,0.6966666666666668))
    d += elm.BatteryCell().label("VEC")
    d += elm.Line().length(0.5).right()
    d += elm.Resistor().right().label(RC)
    d += elm.BatteryCell().down().label(VCC).reverse()
    d += elm.Line().length(1.3).down()
    d += elm.Line().length(3.5).left()
    d += elm.Line().length(1.2).down().at((-0.7516666666666667,0.7))
    d += elm.Ground()
    return d
    

def draw_circuit3_NPN(d,RB="RB",RC="RC",VCC="VCC"):

    transistor = d.add( elm.BjtNpn(circle=True).label('Q1').right() )
    d += elm.Line().length(2.25).left().at(transistor.base)
    d += elm.Line().length(1.5).up()
    d += elm.Resistor().right().label(RB)
    d += elm.Line().length(1.4).up().at(transistor.collector)
    d += elm.Line().length(0.5).right()
    d += elm.Resistor().right().label(RC)
    d += elm.BatteryCell().down().label(VCC)
    d += elm.Line().length(0.7).down()
    d += elm.Line().length(3.5).left()
    
    d += elm.Line().length(1).down().at(transistor.emitter)
    d += elm.Ground()
    return d

def draw_circuit3_PNP(d,RB="RB",RC="RC",VCC="VCC"):

    transistor = d.add( elm.BjtPnp2(circle=True).label('Q1').reverse() )
    d += elm.Line().length(2.25).left().at(transistor.base)
    d += elm.Line().length(1.5).up()
    d += elm.Resistor().right().label(RB)
    d += elm.Line().length(1.4).up().at(transistor.collector)
    d += elm.Line().length(0.5).right()
    d += elm.Resistor().right().label(RC)
    d += elm.BatteryCell().down().label(VCC).reverse()
    d += elm.Line().length(0.7).down()
    d += elm.Line().length(3.5).left()
    
    d += elm.Line().length(0.1).down().at(transistor.emitter)
    d += elm.Ground()
    return d

def draw_circuit3_NPN_off(d,RB="RB",RC="RC",VCC="VCC"):
    
    d+= elm.Dot().at((-1.5033333333333332,1.8410523547181874e-16))
    d += elm.Line().length(2.25).left()
    d += elm.Line().length(1.5).up()
    d += elm.Resistor().right().label(RB)
    d += elm.Dot().at((-0.7516666666666665,0.6966666666666668))
    d += elm.Line().length(1.4).up()
    d += elm.Line().length(0.5).right()
    d += elm.Resistor().right().label(RC)
    d += elm.BatteryCell().down().label(VCC)
    d += elm.Line().length(0.7).down()
    d += elm.Line().length(3.5).left()
    d += elm.Dot().at((-0.7516666666666667,-0.6966666666666665))
    d += elm.Line().length(1.2).down()
    d += elm.Ground()
    return d


    
def draw_circuit3_NPN_Active(d,RB="RB",RC="RC",VCC="VCC"):
    d += elm.BatteryCell().left().reverse().label('VBE').at((-0.76,0.7))
    d += elm.Line().length(0.5).left()
    d += elm.Line().length(2.7).up()
    d += elm.Line().length(0.5).right()
    d+= elm.Resistor().right().label(RB)
    d += elm.SourceControlledI().label("BETA*IB").reverse().at((-0.7516666666666665,0.6966666666666668))
    d += elm.Line().length(0.5).right()
    d += elm.Resistor().right().label(RC)
    d += elm.BatteryCell().down().label(VCC)
    d += elm.Line().length(1.3).down()
    d += elm.Line().length(3.5).left()
    d += elm.Line().length(1.2).down().at((-0.7516666666666667,0.7))
    d += elm.Ground()
    return d




def draw_circuit3_NPN_Sat(d,RB="RB",RC="RC",VCC="VCC"):
    d += elm.BatteryCell().left().reverse().label('VBE').at((-0.76,0.7))
    d += elm.Line().length(0.5).left()
    d += elm.Line().length(2.7).up()
    d += elm.Line().length(0.5).right()
    Rb = d.add(elm.Resistor().right().label(RB))
    d += elm.Line().length(0.01).up().at((-0.7516666666666665,0.6966666666666668))
    d += elm.BatteryCell().label("VCE").reverse()
    d += elm.Line().length(0.5).right()
    d += elm.Resistor().right().label(RC)
    d += elm.BatteryCell().down().label(VCC)
    d += elm.Line().length(1.3).down()
    d += elm.Line().length(3.5).left()
    d += elm.Line().length(1.2).down().at((-0.7516666666666667,0.7))
    d += elm.Ground()
    return d

def Analysis_for_circuit3_NPN(RB,Beta,VCC,RC):
    Ibase = (VCC-0.7)/(RB + ((Beta+1) * RC ) )
    if Ibase <= 0 :
        TEMP = "KVL 1: -VCC + (IB + IC) * RC + (IB) * RB + VBE(ACTIVE) = 0"
        return(("off",0,0,VCC),draw_circuit3_NPN_off,TEMP)
    Icollector = Beta * Ibase
    VCE = VCC - ((Beta+1)/Beta) * RC * Icollector 
    if VCE > 0.2 :
        TEMP = "KVL 1: -VCC + (IB + IC) * RC + (IB) * RB + VBE(ACTIVE) = 0 \n KVL 2: -VCC + (IB + IC) * RC + VCE = 0 \n IC = BETA * IB"
        return(("Active",Ibase,Icollector,VCE),draw_circuit3_NPN_Active,TEMP)
    else:
        Ibase = (VCC-0.8)/(RB + ((Beta+1) * RC ) )
        Icollector = (VCC - 0.2) / ((Beta+1)/Beta) * RC
        VCE = 0.2
        TEMP = "KVL 1: -VCC + (IB + IC) * RC + (IB) * RB + VBE(SAT) = 0 \n KVL 2: -VCC + (IB + IC) * RC  + VCE(SAT) = 0 \n IE = IB + IC"
        return(("Sat",Ibase,Icollector,VCE),draw_circuit3_NPN_Sat,TEMP)

def Analysis_for_circuit3_PNP(RB,Beta,VCC,RC):
    Ibase = (VCC-0.7)/(RB + ((Beta+1) * RC ) )
    if Ibase <= 0 :
        TEMP = "KVL 1: VCC - (IB + IC) * RC - (IB) * RB - VEB(ACTIVE) = 0"
        return(("off",0,0,VCC),draw_circuit3_PNP_off,TEMP)
    Icollector = Beta * Ibase
    VEC = VCC - ((Beta+1)/Beta) * RC * Icollector 
    if VEC > 0.2 :
        TEMP = "KVL 1: VCC - (IB + IC) * RC - (IB) * RB - VEB(ACTIVE) = 0 \n KVL 2: VCC - (IB + IC) * RC  - VEC = 0 \n IC = BETA * IB"
        return(("Active",Ibase,Icollector,VEC),draw_circuit3_PNP_Active,TEMP)
    else:
        Ibase = (VCC-0.8)/(RB + ((Beta+1) * RC ) )
        Icollector = (VCC - 0.2) / ((Beta+1)/Beta) * RC
        VEC = 0.2
        TEMP = "KVL 1: VCC - (IB + IC) * RC - (IB) * RB - VEB(SAT) = 0 \n KVL 2: VCC - (IB + IC) * RC  - VEC(SAT) = 0 \n IE = IB + IC"
        return(("Sat",Ibase,Icollector,VEC),draw_circuit3_PNP_Sat,TEMP)

