import schemdraw
import schemdraw.elements as elm



def draw_circuit1_off(d):
    d+= elm.Dot().at((-1.5033333333333332,1.8410523547181874e-16))
    d += elm.Resistor().left().label('Rb 200kΩ')
    d += elm.SourceV().down().label('VBB 5V')
    d += elm.Line().length(7).right()
    d += elm.Line().length(0.5).up()
    d += elm.SourceV().up().reverse().label('Vcc 10V')
    d += elm.Dot().at((-0.7516666666666665,0.6966666666666668))
    d += elm.Line().length(0.5).up()
    d += elm.Resistor().right().label('3kΩ')
    d += elm.Line().length(0.25).right()
    d += elm.Line().length(1.7).down()
    d += elm.Dot().at((-0.7516666666666667,-0.6966666666666665))
    d += elm.Line().length(2.5).down()
    d += elm.Ground()
    return d
    
def draw_circuit1_Active(d):
    d+= elm.Dot().at((-1.5033333333333332,1.8410523547181874e-16))
    d += elm.BatteryCell().left().reverse().label('Vbe')
    d += elm.Resistor().left().label('Rb 200kΩ')
    d += elm.SourceV().down().label('VBB 5V')
    d += elm.Line().length(10).right()
    d += elm.Line().length(0.5).up()
    d += elm.SourceV().up().reverse().label('Vcc 10V')
    d += elm.Dot().at((-0.7516666666666665,0.6966666666666668))
    d += elm.SourceControlledI().label("ib").reverse()
    d += elm.Resistor().right().label('3kΩ')
    d += elm.Line().length(0.25).right()
    d += elm.Line().length(1.7).down()
    d += elm.Dot().at((-0.7516666666666667,-0.6966666666666665))
    d += elm.Line().length(2.5).down()
    d += elm.Ground()
    return d

def draw_circuit1_Sat(d):
    d+= elm.Dot().at((-1.5033333333333332,1.8410523547181874e-16))
    d += elm.BatteryCell().left().reverse().label('Vbe')
    d += elm.Resistor().left().label('Rb 200kΩ')
    d += elm.SourceV().down().label('VBB 5V')
    d += elm.Line().length(10).right()
    d += elm.Line().length(2).up()
    d += elm.SourceV().up().reverse().label('Vcc 10V')
    d += elm.Dot().at((-0.7516666666666665,0.6966666666666668))
    d += elm.BatteryCell().label("vce").reverse()
    d += elm.Resistor().right().label('3kΩ')
    d += elm.Line().length(0.25).right()
    d += elm.Line().length(1.7).down()
    d += elm.Dot().at((-0.7516666666666667,-0.6966666666666665))
    d += elm.Line().length(2.5).down()
    d += elm.Ground()
    return d
    

def draw_circuit1_NPN(d):
    d += elm.SourceV().up().label('VBB 5V')
    d += elm.Resistor().right().label('Rb 200kΩ')
    transistor = d.add( elm.BjtNpn(circle=True).label('Q1').right() )
    d += elm.Line().length(1).up()
    d += elm.Line().length(0.5).right()
    d += elm.Resistor().right().label('3kΩ')
    d += elm.SourceV().down().reverse().label('Vcc 10V')
    d += elm.Line().length(1.7).down()
    d += elm.Line().length(7.25).left()
    d += elm.Line().length(2.8).down().at(transistor.emitter)
    d += elm.Ground()
    return d

def draw_circuit1_PNP(d):
    transistor = d.add( elm.BjtPnp2(circle=True).label('Q1').reverse())
    d += elm.Resistor().left().label('Rb 200kΩ').at(transistor.base)
    d += elm.SourceV().down().label('VBB 5V')
    d += elm.Line().length(7).right()
    d += elm.Line().length(0.5).up()
    d += elm.SourceV().up().reverse().label('Vcc 10V')
    d += elm.Resistor().right().label('3kΩ').at(transistor.collector)
    d += elm.Line().length(0.21).right()
    d += elm.Line().length(1.7).down()
    d += elm.Line().length(2).down().at(transistor.emitter)
    d += elm.Ground()
    return d