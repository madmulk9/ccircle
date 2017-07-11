import ccircle
import connection

con = connection.create()
con.send('set_name', {'name': 'weeeeeeeeeee'})
args = {
    'vx': 15,
    'vy': 50
}

con.send('set_velocity', args)

# Write code to make money and kill the evil cat!
# See readme.txt !