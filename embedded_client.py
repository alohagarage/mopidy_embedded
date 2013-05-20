#!/usr/bin/python

from mpd import MPDClient

from lcd_plate import Adafruit_CharLCDPlate

HOST = "localhost"
PORT = "6600"


def mpd_message(client, cmd):
    try:
        return eval(cmd)
    except:
        while True:
            try:
                client.disconnect()
                break
            except:
                pass
        client.connect(HOST, PORT)
        return eval(cmd)

def main():
    lcd = Adafruit_CharLCDPlate()
    buttons = [
        {
            "button": lcd.SELECT, 
            "message": "Play", 
            "command": "play"
        },
        {
            "button": lcd.LEFT, 
            "message": "Prev",
            "command": "previous"
        },
        {
            "button": lcd.RIGHT, 
            "message": "Next", 
            "command": "next"
        }
    ]
    client = MPDClient()
    client.connect(HOST, PORT)
    client.stop()
    message = "VVISIGOTH\nINDUSTRIES" 
    lcd.begin(16,2)
    lcd.clear()
    lcd.backlight(lcd.BLUE)
    lcd.message(message)
    #mpd_message(client, "client.play()")

    prev = -1
    n = 0
    playing = False
    while True:
        if n == len(buttons):
            n = 0
        b = buttons[n]
        if lcd.buttonPressed(b['button']):
            lcd.clear()
            message = b['message']
            # Toggle Play
            if b['command'] == 'play':
                print b['command']
                if playing == True:
                    cmd = "client.stop()"
                    message = "Stop"
                    playing = False
                elif playing == False:
                    cmd = "client.play()"
                    playing = True
            else:
                cmd = "client." + b['command'] + "()"
            lcd.message(message)
            mpd_message(client, cmd)
            prev = b
        n += 1

if __name__ == '__main__':
    main()
