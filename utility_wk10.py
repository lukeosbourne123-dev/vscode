def write_to_file(file, msg):
    fid = open (file, 'w')
    fid.write(msg)
    fid.close()

def read_to_file(file):
    fid = open(file,'r')
    print(fid.readline())
    fid.close()
