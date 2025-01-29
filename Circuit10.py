import schemdraw
import schemdraw.elements as elm

# __pycache__/Circuit1.cpython-312.pyc
# ven/Lib/site-packages/cycler/__pycache__/__init__.cpython-312.pyc
# ven/Lib/site-packages/dateutil/__pycache__/__init__.cpython-312.pyc
# ven/Lib/site-packages/dateutil/__pycache__/_common.cpython-312.pyc
# ven/Lib/site-packages/dateutil/__pycache__/_version.cpython-312.pyc
# ven/Lib/site-packages/dateutil/__pycache__/relativedelta.cpython-312.pyc
# ven/Lib/site-packages/dateutil/__pycache__/rrule.cpython-312.pyc
# ven/Lib/site-packages/dateutil/parser/__pycache__/__init__.cpython-312.pyc
# ven/Lib/site-packages/dateutil/parser/__pycache__/_parser.cpython-312.pyc
# ven/Lib/site-packages/dateutil/parser/__pycache__/isoparser.cpython-312.pyc
# ven/Lib/site-packages/dateutil/tz/__pycache__/__init__.cpython-312.pyc
# ven/Lib/site-packages/dateutil/tz/__pycache__/_common.cpython-312.pyc
# ven/Lib/site-packages/dateutil/tz/__pycache__/_factories.cpython-312.pyc
# ven/Lib/site-packages/dateutil/tz/__pycache__/tz.cpython-312.pyc
# ven/Lib/site-packages/dateutil/tz/__pycache__/win.cpython-312.pyc

def draw_circuit10_PNP(d):
    transistor = d.add( elm.BjtPnp2(circle=False).label('Q1').reverse())
    d += elm.Line().length(0.5).left().at(transistor.base)
    d += elm.Resistor().up().label('RB1')
    d += elm.Line().length(2).left()
    d += elm.BatteryCell().down().label('VCC').reverse()
    d += elm.Line().length(0.5).left()
    d += elm.Ground()
    d += elm.Line().length(0.5).right()
    d += elm.BatteryCell().down().reverse().label('VEE')
    d += elm.Line().length(2).right()
    d += elm.Resistor().up().label('RB2')
    d += elm.Line().length(1.5).down().at(transistor.emitter)
    d += elm.Resistor().right().label('RE')
    d += elm.BatteryCell().up().label('VEE')
    d += elm.Line().length(0.5).right()
    d += elm.Ground()
    d += elm.Line().length(0.5).left()
    d += elm.BatteryCell().up().label('VCC')
    d += elm.Line().length(1.5).up().at(transistor.collector)
    d += elm.Resistor().right().label('RC','bottom')

def draw_circuit10_PNP_ACTIVE(d):
    Battery = d.add( elm.BatteryCell().left().label('VEB(ACTIVE)').scale(0.7))
    d += elm.Resistor().up().label('RB1')
    d += elm.Line().length(2).left()
    d += elm.BatteryCell().down().label('VCC').reverse()
    d += elm.Line().length(0.5).left()
    d += elm.Ground()
    d += elm.Line().length(0.5).right()
    d += elm.BatteryCell().down().reverse().label('VEE')
    d += elm.Line().length(2).right()
    d += elm.Resistor().up().label('RB2')
    d += elm.Resistor().down().label('RE').at(Battery.start)
    d += elm.Line().length(3).right()
    d += elm.BatteryCell().up().label('VEE')
    d += elm.Line().length(0.5).right()
    d += elm.Ground()
    d += elm.Line().length(0.5).left()
    d += elm.BatteryCell().up().label('VCC')
    d += elm.SourceControlledI().up().label("Beta IB").at(Battery.start)
    d += elm.Resistor().right().label('RC')

def draw_circuit10_PNP_SAT(d):
    Battery = d.add( elm.BatteryCell().left().label('VEB(SAT)').scale(0.7))
    d += elm.Resistor().up().label('RB1')
    d += elm.Line().length(2).left()
    d += elm.BatteryCell().down().label('VCC').reverse()
    d += elm.Line().length(0.5).left()
    d += elm.Ground()
    d += elm.Line().length(0.5).right()
    d += elm.BatteryCell().down().reverse().label('VEE')
    d += elm.Line().length(2).right()
    d += elm.Resistor().up().label('RB2')
    d += elm.Resistor().down().label('RE').at(Battery.start)
    d += elm.Line().length(3).right()
    d += elm.BatteryCell().up().label('VEE')
    d += elm.Line().length(0.5).right()
    d += elm.Ground()
    d += elm.Line().length(0.5).left()
    d += elm.BatteryCell().up().label('VCC')
    d += elm.BatteryCell().up().label("VEC(SAT)").at(Battery.start)
    d += elm.Resistor().right().label('RC')


def draw_circuit10_PNP_off(d):
    d += elm.Resistor().up().label('RB1')
    d += elm.Line().length(2).left()
    d += elm.BatteryCell().down().label('VCC').reverse()
    d += elm.Line().length(0.5).left()
    d += elm.Ground()
    d += elm.Line().length(0.5).right()
    d += elm.BatteryCell().down().reverse().label('VEE')
    d += elm.Line().length(2).right()
    d += elm.Resistor().up().label('RB2')
    d += elm.Line().length(0.5).right()
    d += elm.Dot().label("B")
    d += elm.Line().length(0.5).left()
    d += elm.Dot().label("E",'right').at((1,-0.5))
    d += elm.Resistor().down().label('RE','bottom')
    d += elm.Line().length(3).right()
    d += elm.BatteryCell().up().label('VEE')
    d += elm.Line().length(0.5).right()
    d += elm.Ground()
    d += elm.Line().length(0.5).left()
    d += elm.BatteryCell().up().label('VCC')
    d += elm.Resistor().left().label('RC')
    d += elm.Line().length(2).down()
    d += elm.Dot().label("C",'right')

def draw_circuit10_NPN(d):
   
    d += elm.BatteryCell().down().label('VCC')
    d += elm.Line().length(0.5).left()
    d += elm.Ground()
    d += elm.Line().length(0.5).right()
    d += elm.BatteryCell().down().reverse().label('VEE')
    d += elm.Line().length(2).right()
    d += elm.Resistor().up().label('RB2')
    d += elm.Line().length(0.5).right()
    transistor = d.add( elm.BjtNpn(circle=True).label('Q1').right())
    d += elm.Line().length(0.5).left().at(transistor.base)
    d += elm.Resistor().up().label('RB1')
    d += elm.Line().length(2).left()
    d += elm.Resistor().down().label('RE').at(transistor.emitter)
    d += elm.Line().length(2).right()
    d += elm.BatteryCell().up().reverse().label('VEE')
    d += elm.Line().length(0.5).right()
    d += elm.Ground()
    d += elm.Line().length(0.5).left()
    d += elm.BatteryCell().up().label('VCC').reverse()
    d += elm.Line().length(1.41).up()
    d += elm.Line().length(2).left()
    d += elm.Resistor().up().label('RC').at(transistor.collector)
    
    
def draw_circuit10_NPN_ACTIVE(d):
    d += elm.BatteryCell().down().label('VCC')
    d += elm.Line().length(0.5).left()
    d += elm.Ground()
    d += elm.Line().length(0.5).right()
    d += elm.BatteryCell().down().reverse().label('VEE')
    d += elm.Line().length(2).right()
    d += elm.Resistor().up().label('RB2')
    Battery = d.add( elm.BatteryCell().right().label('VBE(ACTIVE)').scale(0.7))
    d += elm.Resistor().up().label('RB1').at(Battery.start)
    d += elm.Line().length(2).left()
    d += elm.Resistor().down().label('RE').at(Battery.end)
    d += elm.Line().length(2).right()
    d += elm.BatteryCell().up().reverse().label('VEE')
    d += elm.Line().length(0.5).right()
    d += elm.Ground()
    d += elm.Line().length(0.5).left()
    d += elm.BatteryCell().up().label('VCC').reverse()
    d += elm.Line().length(2).left()
    d += elm.SourceControlledI().down().label("Beta IB")

def draw_circuit10_NPN_SAT(d):
    d += elm.BatteryCell().down().label('VCC')
    d += elm.Line().length(0.5).left()
    d += elm.Ground()
    d += elm.Line().length(0.5).right()
    d += elm.BatteryCell().down().reverse().label('VEE')
    d += elm.Line().length(2).right()
    d += elm.Resistor().up().label('RB2')
    Battery = d.add( elm.BatteryCell().right().label('VBE(ACTIVE)').scale(0.7))
    d += elm.Resistor().up().label('RB1').at(Battery.start)
    d += elm.Line().length(2).left()
    d += elm.Resistor().down().label('RE').at(Battery.end)
    d += elm.Line().length(2).right()
    d += elm.BatteryCell().up().reverse().label('VEE')
    d += elm.Line().length(0.5).right()
    d += elm.Ground()
    d += elm.Line().length(0.5).left()
    d += elm.BatteryCell().up().label('VCC').reverse()
    d += elm.Line().length(2).left()
    d += elm.BatteryCell().down().label("VCE (sat)")
    
def draw_circuit10_NPN_OFF(d):
    d += elm.BatteryCell().down().label('VCC')
    d += elm.Line().length(0.5).left()
    d += elm.Ground()
    d += elm.Line().length(0.5).right()
    d += elm.BatteryCell().down().reverse().label('VEE')
    d += elm.Line().length(2).right()
    d += elm.Resistor().up().label('RB2')
    d += elm.Line().length(0.5).right()
    d += elm.Dot().label("B")
    d += elm.Line().length(0.5).left()
    d += elm.Resistor().up().label('RB1')
    d += elm.Line().length(2).left()
    d += elm.Dot().label("E",'right').at((3.2,-3.5))
    d += elm.Resistor().down().label('RE')
    d += elm.Line().length(2).right()
    d += elm.BatteryCell().up().reverse().label('VEE')
    d += elm.Line().length(0.5).right()
    d += elm.Ground()
    d += elm.Line().length(0.5).left()
    d += elm.BatteryCell().up().label('VCC').reverse()
    d += elm.Line().length(2).left()
    d += elm.Line().length(2).down()
    d += elm.Dot().label("C",'right')


    def Analysis_for_circuit1_NPN():
        vth = (rb2/(rb1+rb2))*(vcc-vee)+ vee
        ib = (vee-vth-vbe)/(rth+((b+1)*re))

    def Analysis_for_circuit1_PNP():
        pass
