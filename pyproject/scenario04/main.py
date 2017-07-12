import ccircle
import connection
import string
import random

con = connection.create()
con.send('set_name', {'name': 'big_boyo'})
print("name sent")

args = {
    'vx': 0,
    'vy': 0
}

window = ccircle.Window("control window")

while (window.isOpen()):
    window.clear(0.2, 0.2, 0.2)

    players = con.send('get_player_ids')
    print(players)

    for plyr in range(len(players)):
        con.send("get_player_pos", players[plyr])
        print("sent get player position request")

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