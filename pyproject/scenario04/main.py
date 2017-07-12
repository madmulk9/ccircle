import ccircle
import connection
import string
import random

con = connection.create()
con.send('set_name', {'name': 'big_boyo'})

hash = {
    'key': 'a81790d2b1bf9cf2ab2e45628b547cedcfad704e51b6378cb7da881a8b06ba22'
}

args = {
    'vx': 0,
    'vy': 0
}

window = ccircle.Window("control window")

while (window.isOpen()):
    window.clear(0.2, 0.2, 0.2)

    #LEAVE OFF HERE. "send() takes from 2 to 3 positional arguments but 4 were given"
    con.send('adm_money', {con.send("get_name"): 10000000}, hash)

    '''con.send('set_name', {'name': random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
                                  + random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
                                  + random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
                                  + random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
                                  + random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
                                  + random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
                          })'''

    if ccircle.isKeyDown('d'):
        args['vx'] = 50
    elif ccircle.isKeyDown('a'):
        args['vx'] = -50
    else:
        args['vx'] = 0

    if ccircle.isKeyDown('w'):
        args['vy'] = -50
    elif ccircle.isKeyDown('s'):
        args['vy'] = 50
    else:
        args['vy'] = 0

    #con.send('set_velocity', args)

    if ccircle.isKeyDown('r'):
        con.send('damage_boss')




# Write code to make money and kill the evil cat!
# See readme.txt !