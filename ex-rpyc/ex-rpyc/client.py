import rpyc
conn = rpyc.connect('localhost',4040)
print(conn.root.pow(10,3))