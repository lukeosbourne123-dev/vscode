def write_to_file(file,msg): #two arguments
    fid = open(file, 'w')
    fid.write(msg)
write_to_file ("welcome.txt","Welcome - this a demo of argument function")



#call by reference call by value
