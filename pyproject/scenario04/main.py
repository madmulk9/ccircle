import ccircle
import connection

con = connection.create()
con.send('set_name', {'name': 'weeeeeeeeeee'})
args = {
    'vx': 0,
    'vy': 0
}

window = ccircle.Window("control window")

while (window.isOpen()):
    window.clear(0.2, 0.2, 0.2)

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

    con.send('set_velocity', args)




# Write code to make money and kill the evil cat!
# See readme.txt !