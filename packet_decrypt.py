@numargs(0)
def FN_convert_hex(data, args):
    if len(data) % 2 == 0 and re.search('^[a-fA-F0-9]+$', data):

        i = 0
        j = 0
        off = 0

        hex_list = []

        offset = "%04X " % (off)              
        hex_list.extend(offset)
        hex_list.extend(' ')
        off += 1
        
        while (len(data) > i):
            hex_list.extend(data[i:i+2])
            hex_list.extend(' ')
            i+=2
            if i % 32 == 0 :
                j+=16
                hex_list.extend('_:_')
                
                offset = "%04X " % (off)  
                hex_list.extend(offset)
                hex_list.extend(' ')

            off += 1 


        while (len(data) > i) :

            hex_list.extend(data[i:i+2])
            hex_list.extend(' ')
            i+=2


        hex_list.extend('_:_')

    return hex_list

@numargs(0)
def FN_convert_line(data, args):
    
    if len(data) % 2 == 0 and re.search('^[a-fA-F0-9]+$', data):

	i = 0
	text = []
	data = binascii.unhexlify(data)

	while (len(data) > i):
	   text.extend(data[i:i+16])
	   text.extend('_:_')
	   i+=16

    return text;

@numargs(0)
def FN_convert_base(data, args):
    
    data = data.decode("hex")
    base = binascii.b2a_base64(data)
    base_list = []
    i = 0
    
    while (len(base) > i) :
        base_list.extend(base[i:i+64])
        i+=64
        base_list.extend('_:_')

    return base_list
