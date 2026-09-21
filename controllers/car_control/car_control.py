#car_control controller
from controller import Robot

robot = Robot()

timestep = int(robot.getBasicTimeStep())

print("Inicando rodas")
motorE = robot.getDevice('motorE')
motorD = robot.getDevice('motorD')
motorE.setPosition(float('inf'))
motorD.setPosition(float('inf'))
motorE.setVelocity(0.0)
motorD.setVelocity(0.0)

print("Iniciando sensores principais")
distSensorE = robot.getDevice('DSE')
distSensorD = robot.getDevice('DSD')
distSensorE.enable(timestep)
distSensorD.enable(timestep)

print("Ajustando valores sensibilidade")
enabledE = 0
enabledD = 0

sensibilidadeTroca = 1.0

print("Iniciando...")
while robot.step(timestep) != -1:
    parcialE = round(distSensorE.getValue(), 2)
    parcialD = round(distSensorD.getValue(), 2)
    enabledE = parcialE if parcialE - enabledE != 0 and parcialE > 0 else enabledE
    enabledD = parcialD if parcialD - enabledD != 0 and parcialD > 0 else enabledD
        
    if enabledE < enabledD:
        motorE.setVelocity(0.80)
        motorD.setVelocity(0.08)
    elif enabledD < enabledE:
        motorE.setVelocity(0.08)
        motorD.setVelocity(0.80)
    else:
        motorE.setVelocity(10.00)
        motorD.setVelocity(10.00)
