#!/usr/bin/env python
"""
IDEA drive library used to interface with ACM4826E but should work with
similar IDEA drives.

http://www.haydonkerkpittman.com/products/drives/steppermotorprogrammabledrives
Protcol Spec: http://www.haydonkerkpittman.com/-/media/ametekhaydonkerk/downloads/products/drives/idea_drive_communication_manual.pdf?la=en
"""

import serial


def open_port(device, speed):
    return serial.Serial(device, speed, timeout=1)


def read_until(ser, eol='\r'):
    """
    This func reads the serial device till a specified EOL is encountered OR if
    None is read, meaning timeout. The pyserial custom EOL is a PITA

    Args:
        ser: The opened serial object
        eol: Custom EOL character to stop reading

    Returns:
        reply (str): The reply the serial object returns

    """

    reply = ''
    resp = ser.read()
    while resp != '\r':
        reply = reply + resp
        resp = ser.read()
        if resp == '':
            # this captures timeouts
            break;

    return reply


def move(ser, steps, rsteps=500, runcur=2000, holdcur=250, delay=50, stepmode=1, boost=False ):
    """
    This funcs issues out the move command to the controller.

    Args:
        ser: the opened serial object
        steps: more of the position to go to in steps
        rsteps: run speed at top speed
        ssteps: the start speed of steps/second
        esteps: the end speed of steps/second
        accel: rate at which the speed should rise to start->run
        deccel: rate at which the speed should fall to run->end
        runcur: the rms current in milliamps
        holdcur: the rms of hold current
        accelcur: the rms current when accelerating
        deccelcur: the rms current when decellerating
        delay: ms between last step and hold current
        stepmode: step divided by multiple (1,2,4,8,16,32,64)
                  1 for full step, 64 for 1/64 of a step
    """
    steps = steps * 64

    accelcurr = runcur
    decelcurr = runcur

    if boost:
        accelcurr += 600
        decelcurr += 600

    cmd = 'M{},{},0,0,0,0,{},{},{},{},{},{}\r'.format(steps,
                                                      rsteps,
                                                      runcur,
                                                      holdcur,
                                                      accelcurr,
                                                      decelcurr,
                                                      delay,
                                                      stepmode)

    ser.write(cmd)


def enable_encoder(ser, deadband, encoder_res, motor_res, inter_priority=10):
    """
    This funcs enabled the encoder.

    Args:
        ser: the opened serial object
        deadband: the 1/64 steps to be in the deadband
        encoder_res: encoder counter per revolution
        motor_res: motor steps per revolution
        inter_priority: prioirty of interrupt 0-4, 10 to disable
    """

    cmd = 'z{},0,0,{},{},{}\r'.format(deadband,
                                    inter_priority,
                                    encoder_res,
                                    motor_res)

    print cmd
    ser.write(cmd)


def set_position(ser, pos):
    """
    This funcs set the position of the stepper. Good for resetting the position

    Args:
        ser: the opened serial object
        pos: the position wishing to set
    """

    cmd = 'Z{}\r'.format(pos)

    print cmd
    ser.write(cmd)

def factory_reset(ser):
    """
    This func factory resets the device.

    Args:
        ser: the opened serial object

    """
    ser.write('a\r')


def reset(ser):
    """
    This func resets the stepper, same as power cycling.

    Args:
        ser: the opened serial object

    """
    ser.write('R\r')


def abort(ser):
    """
    This func resets the stepper, same as power cycling.

    Args:
        ser: the opened serial object

    """
    ser.write('A\r')


def read_drive_number(ser):
    """
    This func queries the drive and gets its drive number.

    Args:
        ser: the opened serial object

    Returns:
        drive numer (str): The number ID associated with the drive.

    """
    ser.write('k\r')
    return read_until(ser)


def read_position(ser):
    """
    This func queries the drive and gets its drive number.

    Args:
        ser: the opened serial object

    Returns:
        drive numer (str): The number ID associated with the drive.

    """
    ser.write('l\r')
    resp = read_until(ser)
    read_until(ser)
    return resp


def read_moving(ser):
    """
    This func queries the drive and determines if the drive is moving or not.

    Args:
        ser: the opened serial object

    Returns:
        moving (str): If drive is moving reply string

    """
    ser.write('o\r')
    return read_until(ser)


def read_firmware_version(ser):
    """
    This func queries the drive and gets its current firmware.

    Args:
        ser: the opened serial object

    Returns:
        firmware (str): Firmware version reply string

    """
    ser.write('v\r')
    return read_until(ser)


def read_faults(ser):
    """
    This func queries the drive and gets its current firmware.

    Args:
        ser: the opened serial object

    Returns:
        faults (str): Faults output

    """
    ser.write('f\r')
    return read_until(ser)




# setup serial drive/rs485
#ser = open_port(args.device, args.port_speed)
#ser = open_port('/dev/ttyUSB0', 57600)
#import time

# lets reset the drive to clear anything
#factory_reset(ser)
#reset(ser)
#time.sleep(1)

# print out some debug info
#print 'Drive #: {}'.format(read_drive_number(ser))
#print 'Pos: {}'.format(read_position(ser))
#print 'Firmware version: {}'.format(read_firmware_version(ser))
#print 'Drive moving: {}'.format(read_moving(ser))
#print 'Faults: {}'.format(read_faults(ser))

# simple random test
#move(ser, 0, 350)
#import time
#time.sleep(5)
#count = 0
#import random
#while True:
#    count = count +1
#    time.sleep(0.1)
#    abort(ser)
#    move(ser, random.randint(0, 350), 350, boost=False, stepmode=1)
#
#    if count > 50:
#        break
#
#
#move(ser, 0, 400)
