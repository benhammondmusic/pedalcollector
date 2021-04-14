# Add the pedal class & list and view function below the imports
class Pedal:  # Note that parens are optional if not inheriting from another class
  def __init__(self, brand, name, style, description, voltage, amperage):
    self.brand = brand
    self.name = name
    self.style = style
    self.description = description
    self.voltage = voltage
    self.amperage = amperage

pedals = [
    Pedal('Voodoo Labs', 'Sparkle Drive', 'Gain', 'Tube-screamer circuit with blendable clean boost', 9, 35),
    Pedal('Boss', 'OC-3', 'Octave', 'Octave down effect, with sweepable low-pass range to only double lower end of the guitar', 9, 50),
    Pedal('Strymon', 'El Capistan', 'Delay', 'Simulated tape delay', 9, 250),
]