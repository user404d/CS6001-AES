"""
A bunch of magic constants (precomputed heavy lifting)
"""
s_box = (
    b'\x63\x7c\x77\x7b\xf2\x6b\x6f\xc5\x30\x01\x67\x2b\xfe\xd7\xab\x76',
    b'\xca\x82\xc9\x7d\xfa\x59\x47\xf0\xad\xd4\xa2\xaf\x9c\xa4\x72\xc0',
    b'\xb7\xfd\x93\x26\x36\x3f\xf7\xcc\x34\xa5\xe5\xf1\x71\xd8\x31\x15',
    b'\x04\xc7\x23\xc3\x18\x96\x05\x9a\x07\x12\x80\xe2\xeb\x27\xb2\x75',
    b'\x09\x83\x2c\x1a\x1b\x6e\x5a\xa0\x52\x3b\xd6\xb3\x29\xe3\x2f\x84',
    b'\x53\xd1\x00\xed\x20\xfc\xb1\x5b\x6a\xcb\xbe\x39\x4a\x4c\x58\xcf',
    b'\xd0\xef\xaa\xfb\x43\x4d\x33\x85\x45\xf9\x02\x7f\x50\x3c\x9f\xa8',
    b'\x51\xa3\x40\x8f\x92\x9d\x38\xf5\xbc\xb6\xda\x21\x10\xff\xf3\xd2',
    b'\xcd\x0c\x13\xec\x5f\x97\x44\x17\xc4\xa7\x7e\x3d\x64\x5d\x19\x73',
    b'\x60\x81\x4f\xdc\x22\x2a\x90\x88\x46\xee\xb8\x14\xde\x5e\x0b\xdb',
    b'\xe0\x32\x3a\x0a\x49\x06\x24\x5c\xc2\xd3\xac\x62\x91\x95\xe4\x79',
    b'\xe7\xc8\x37\x6d\x8d\xd5\x4e\xa9\x6c\x56\xf4\xea\x65\x7a\xae\x08',
    b'\xba\x78\x25\x2e\x1c\xa6\xb4\xc6\xe8\xdd\x74\x1f\x4b\xbd\x8b\x8a',
    b'\x70\x3e\xb5\x66\x48\x03\xf6\x0e\x61\x35\x57\xb9\x86\xc1\x1d\x9e',
    b'\xe1\xf8\x98\x11\x69\xd9\x8e\x94\x9b\x1e\x87\xe9\xce\x55\x28\xdf',
    b'\x8c\xa1\x89\x0d\xbf\xe6\x42\x68\x41\x99\x2d\x0f\xb0\x54\xbb\x16',)


is_box = (
    b'\x52\x09\x6a\xd5\x30\x36\xa5\x38\xbf\x40\xa3\x9e\x81\xf3\xd7\xfb',
    b'\x7c\xe3\x39\x82\x9b\x2f\xff\x87\x34\x8e\x43\x44\xc4\xde\xe9\xcb',
    b'\x54\x7b\x94\x32\xa6\xc2\x23\x3d\xee\x4c\x95\x0b\x42\xfa\xc3\x4e',
    b'\x08\x2e\xa1\x66\x28\xd9\x24\xb2\x76\x5b\xa2\x49\x6d\x8b\xd1\x25',
    b'\x72\xf8\xf6\x64\x86\x68\x98\x16\xd4\xa4\x5c\xcc\x5d\x65\xb6\x92',
    b'\x6c\x70\x48\x50\xfd\xed\xb9\xda\x5e\x15\x46\x57\xa7\x8d\x9d\x84',
    b'\x90\xd8\xab\x00\x8c\xbc\xd3\x0a\xf7\xe4\x58\x05\xb8\xb3\x45\x06',
    b'\xd0\x2c\x1e\x8f\xca\x3f\x0f\x02\xc1\xaf\xbd\x03\x01\x13\x8a\x6b',
    b'\x3a\x91\x11\x41\x4f\x67\xdc\xea\x97\xf2\xcf\xce\xf0\xb4\xe6\x73',
    b'\x96\xac\x74\x22\xe7\xad\x35\x85\xe2\xf9\x37\xe8\x1c\x75\xdf\x6e',
    b'\x47\xf1\x1a\x71\x1d\x29\xc5\x89\x6f\xb7\x62\x0e\xaa\x18\xbe\x1b',
    b'\xfc\x56\x3e\x4b\xc6\xd2\x79\x20\x9a\xdb\xc0\xfe\x78\xcd\x5a\xf4',
    b'\x1f\xdd\xa8\x33\x88\x07\xc7\x31\xb1\x12\x10\x59\x27\x80\xec\x5f',
    b'\x60\x51\x7f\xa9\x19\xb5\x4a\x0d\x2d\xe5\x7a\x9f\x93\xc9\x9c\xef',
    b'\xa0\xe0\x3b\x4d\xae\x2a\xf5\xb0\xc8\xeb\xbb\x3c\x83\x53\x99\x61',
    b'\x17\x2b\x04\x7e\xba\x77\xd6\x26\xe1\x69\x14\x63\x55\x21\x0c\x7d',)


a_x_2 = (
    b'\x00\x02\x04\x06\x08\x0a\x0c\x0e\x10\x12\x14\x16\x18\x1a\x1c\x1e',
    b'\x20\x22\x24\x26\x28\x2a\x2c\x2e\x30\x32\x34\x36\x38\x3a\x3c\x3e',
    b'\x40\x42\x44\x46\x48\x4a\x4c\x4e\x50\x52\x54\x56\x58\x5a\x5c\x5e',
    b'\x60\x62\x64\x66\x68\x6a\x6c\x6e\x70\x72\x74\x76\x78\x7a\x7c\x7e',
    b'\x80\x82\x84\x86\x88\x8a\x8c\x8e\x90\x92\x94\x96\x98\x9a\x9c\x9e',
    b'\xa0\xa2\xa4\xa6\xa8\xaa\xac\xae\xb0\xb2\xb4\xb6\xb8\xba\xbc\xbe',
    b'\xc0\xc2\xc4\xc6\xc8\xca\xcc\xce\xd0\xd2\xd4\xd6\xd8\xda\xdc\xde',
    b'\xe0\xe2\xe4\xe6\xe8\xea\xec\xee\xf0\xf2\xf4\xf6\xf8\xfa\xfc\xfe',
    b'\x1b\x19\x1f\x1d\x13\x11\x17\x15\x0b\x09\x0f\x0d\x03\x01\x07\x05',
    b'\x3b\x39\x3f\x3d\x33\x31\x37\x35\x2b\x29\x2f\x2d\x23\x21\x27\x25',
    b'\x5b\x59\x5f\x5d\x53\x51\x57\x55\x4b\x49\x4f\x4d\x43\x41\x47\x45',
    b'\x7b\x79\x7f\x7d\x73\x71\x77\x75\x6b\x69\x6f\x6d\x63\x61\x67\x65',
    b'\x9b\x99\x9f\x9d\x93\x91\x97\x95\x8b\x89\x8f\x8d\x83\x81\x87\x85',
    b'\xbb\xb9\xbf\xbd\xb3\xb1\xb7\xb5\xab\xa9\xaf\xad\xa3\xa1\xa7\xa5',
    b'\xdb\xd9\xdf\xdd\xd3\xd1\xd7\xd5\xcb\xc9\xcf\xcd\xc3\xc1\xc7\xc5',
    b'\xfb\xf9\xff\xfd\xf3\xf1\xf7\xf5\xeb\xe9\xef\xed\xe3\xe1\xe7\xe5',)

a_x_3 = (
    b'\x00\x03\x06\x05\x0c\x0f\x0a\x09\x18\x1b\x1e\x1d\x14\x17\x12\x11',
    b'\x30\x33\x36\x35\x3c\x3f\x3a\x39\x28\x2b\x2e\x2d\x24\x27\x22\x21',
    b'\x60\x63\x66\x65\x6c\x6f\x6a\x69\x78\x7b\x7e\x7d\x74\x77\x72\x71',
    b'\x50\x53\x56\x55\x5c\x5f\x5a\x59\x48\x4b\x4e\x4d\x44\x47\x42\x41',
    b'\xc0\xc3\xc6\xc5\xcc\xcf\xca\xc9\xd8\xdb\xde\xdd\xd4\xd7\xd2\xd1',
    b'\xf0\xf3\xf6\xf5\xfc\xff\xfa\xf9\xe8\xeb\xee\xed\xe4\xe7\xe2\xe1',
    b'\xa0\xa3\xa6\xa5\xac\xaf\xaa\xa9\xb8\xbb\xbe\xbd\xb4\xb7\xb2\xb1',
    b'\x90\x93\x96\x95\x9c\x9f\x9a\x99\x88\x8b\x8e\x8d\x84\x87\x82\x81',
    b'\x9b\x98\x9d\x9e\x97\x94\x91\x92\x83\x80\x85\x86\x8f\x8c\x89\x8a',
    b'\xab\xa8\xad\xae\xa7\xa4\xa1\xa2\xb3\xb0\xb5\xb6\xbf\xbc\xb9\xba',
    b'\xfb\xf8\xfd\xfe\xf7\xf4\xf1\xf2\xe3\xe0\xe5\xe6\xef\xec\xe9\xea',
    b'\xcb\xc8\xcd\xce\xc7\xc4\xc1\xc2\xd3\xd0\xd5\xd6\xdf\xdc\xd9\xda',
    b'\x5b\x58\x5d\x5e\x57\x54\x51\x52\x43\x40\x45\x46\x4f\x4c\x49\x4a',
    b'\x6b\x68\x6d\x6e\x67\x64\x61\x62\x73\x70\x75\x76\x7f\x7c\x79\x7a',
    b'\x3b\x38\x3d\x3e\x37\x34\x31\x32\x23\x20\x25\x26\x2f\x2c\x29\x2a',
    b'\x0b\x08\x0d\x0e\x07\x04\x01\x02\x13\x10\x15\x16\x1f\x1c\x19\x1a',)

a_inv_x_9 = (
    b'\x00\x09\x12\x1b\x24\x2d\x36\x3f\x48\x41\x5a\x53\x6c\x65\x7e\x77',
    b'\x90\x99\x82\x8b\xb4\xbd\xa6\xaf\xd8\xd1\xca\xc3\xfc\xf5\xee\xe7',
    b'\x3b\x32\x29\x20\x1f\x16\x0d\x04\x73\x7a\x61\x68\x57\x5e\x45\x4c',
    b'\xab\xa2\xb9\xb0\x8f\x86\x9d\x94\xe3\xea\xf1\xf8\xc7\xce\xd5\xdc',
    b'\x76\x7f\x64\x6d\x52\x5b\x40\x49\x3e\x37\x2c\x25\x1a\x13\x08\x01',
    b'\xe6\xef\xf4\xfd\xc2\xcb\xd0\xd9\xae\xa7\xbc\xb5\x8a\x83\x98\x91',
    b'\x4d\x44\x5f\x56\x69\x60\x7b\x72\x05\x0c\x17\x1e\x21\x28\x33\x3a',
    b'\xdd\xd4\xcf\xc6\xf9\xf0\xeb\xe2\x95\x9c\x87\x8e\xb1\xb8\xa3\xaa',
    b'\xec\xe5\xfe\xf7\xc8\xc1\xda\xd3\xa4\xad\xb6\xbf\x80\x89\x92\x9b',
    b'\x7c\x75\x6e\x67\x58\x51\x4a\x43\x34\x3d\x26\x2f\x10\x19\x02\x0b',
    b'\xd7\xde\xc5\xcc\xf3\xfa\xe1\xe8\x9f\x96\x8d\x84\xbb\xb2\xa9\xa0',
    b'\x47\x4e\x55\x5c\x63\x6a\x71\x78\x0f\x06\x1d\x14\x2b\x22\x39\x30',
    b'\x9a\x93\x88\x81\xbe\xb7\xac\xa5\xd2\xdb\xc0\xc9\xf6\xff\xe4\xed',
    b'\x0a\x03\x18\x11\x2e\x27\x3c\x35\x42\x4b\x50\x59\x66\x6f\x74\x7d',
    b'\xa1\xa8\xb3\xba\x85\x8c\x97\x9e\xe9\xe0\xfb\xf2\xcd\xc4\xdf\xd6',
    b'\x31\x38\x23\x2a\x15\x1c\x07\x0e\x79\x70\x6b\x62\x5d\x54\x4f\x46',)

a_inv_x_b = (
    b'\x00\x0b\x16\x1d\x2c\x27\x3a\x31\x58\x53\x4e\x45\x74\x7f\x62\x69',
    b'\xb0\xbb\xa6\xad\x9c\x97\x8a\x81\xe8\xe3\xfe\xf5\xc4\xcf\xd2\xd9',
    b'\x7b\x70\x6d\x66\x57\x5c\x41\x4a\x23\x28\x35\x3e\x0f\x04\x19\x12',
    b'\xcb\xc0\xdd\xd6\xe7\xec\xf1\xfa\x93\x98\x85\x8e\xbf\xb4\xa9\xa2',
    b'\xf6\xfd\xe0\xeb\xda\xd1\xcc\xc7\xae\xa5\xb8\xb3\x82\x89\x94\x9f',
    b'\x46\x4d\x50\x5b\x6a\x61\x7c\x77\x1e\x15\x08\x03\x32\x39\x24\x2f',
    b'\x8d\x86\x9b\x90\xa1\xaa\xb7\xbc\xd5\xde\xc3\xc8\xf9\xf2\xef\xe4',
    b'\x3d\x36\x2b\x20\x11\x1a\x07\x0c\x65\x6e\x73\x78\x49\x42\x5f\x54',
    b'\xf7\xfc\xe1\xea\xdb\xd0\xcd\xc6\xaf\xa4\xb9\xb2\x83\x88\x95\x9e',
    b'\x47\x4c\x51\x5a\x6b\x60\x7d\x76\x1f\x14\x09\x02\x33\x38\x25\x2e',
    b'\x8c\x87\x9a\x91\xa0\xab\xb6\xbd\xd4\xdf\xc2\xc9\xf8\xf3\xee\xe5',
    b'\x3c\x37\x2a\x21\x10\x1b\x06\x0d\x64\x6f\x72\x79\x48\x43\x5e\x55',
    b'\x01\x0a\x17\x1c\x2d\x26\x3b\x30\x59\x52\x4f\x44\x75\x7e\x63\x68',
    b'\xb1\xba\xa7\xac\x9d\x96\x8b\x80\xe9\xe2\xff\xf4\xc5\xce\xd3\xd8',
    b'\x7a\x71\x6c\x67\x56\x5d\x40\x4b\x22\x29\x34\x3f\x0e\x05\x18\x13',
    b'\xca\xc1\xdc\xd7\xe6\xed\xf0\xfb\x92\x99\x84\x8f\xbe\xb5\xa8\xa3',)

a_inv_x_d = (
    b'\x00\x0d\x1a\x17\x34\x39\x2e\x23\x68\x65\x72\x7f\x5c\x51\x46\x4b',
    b'\xd0\xdd\xca\xc7\xe4\xe9\xfe\xf3\xb8\xb5\xa2\xaf\x8c\x81\x96\x9b',
    b'\xbb\xb6\xa1\xac\x8f\x82\x95\x98\xd3\xde\xc9\xc4\xe7\xea\xfd\xf0',
    b'\x6b\x66\x71\x7c\x5f\x52\x45\x48\x03\x0e\x19\x14\x37\x3a\x2d\x20',
    b'\x6d\x60\x77\x7a\x59\x54\x43\x4e\x05\x08\x1f\x12\x31\x3c\x2b\x26',
    b'\xbd\xb0\xa7\xaa\x89\x84\x93\x9e\xd5\xd8\xcf\xc2\xe1\xec\xfb\xf6',
    b'\xd6\xdb\xcc\xc1\xe2\xef\xf8\xf5\xbe\xb3\xa4\xa9\x8a\x87\x90\x9d',
    b'\x06\x0b\x1c\x11\x32\x3f\x28\x25\x6e\x63\x74\x79\x5a\x57\x40\x4d',
    b'\xda\xd7\xc0\xcd\xee\xe3\xf4\xf9\xb2\xbf\xa8\xa5\x86\x8b\x9c\x91',
    b'\x0a\x07\x10\x1d\x3e\x33\x24\x29\x62\x6f\x78\x75\x56\x5b\x4c\x41',
    b'\x61\x6c\x7b\x76\x55\x58\x4f\x42\x09\x04\x13\x1e\x3d\x30\x27\x2a',
    b'\xb1\xbc\xab\xa6\x85\x88\x9f\x92\xd9\xd4\xc3\xce\xed\xe0\xf7\xfa',
    b'\xb7\xba\xad\xa0\x83\x8e\x99\x94\xdf\xd2\xc5\xc8\xeb\xe6\xf1\xfc',
    b'\x67\x6a\x7d\x70\x53\x5e\x49\x44\x0f\x02\x15\x18\x3b\x36\x21\x2c',
    b'\x0c\x01\x16\x1b\x38\x35\x22\x2f\x64\x69\x7e\x73\x50\x5d\x4a\x47',
    b'\xdc\xd1\xc6\xcb\xe8\xe5\xf2\xff\xb4\xb9\xae\xa3\x80\x8d\x9a\x97',)

a_inv_x_e = (
    b'\x00\x0e\x1c\x12\x38\x36\x24\x2a\x70\x7e\x6c\x62\x48\x46\x54\x5a',
    b'\xe0\xee\xfc\xf2\xd8\xd6\xc4\xca\x90\x9e\x8c\x82\xa8\xa6\xb4\xba',
    b'\xdb\xd5\xc7\xc9\xe3\xed\xff\xf1\xab\xa5\xb7\xb9\x93\x9d\x8f\x81',
    b'\x3b\x35\x27\x29\x03\x0d\x1f\x11\x4b\x45\x57\x59\x73\x7d\x6f\x61',
    b'\xad\xa3\xb1\xbf\x95\x9b\x89\x87\xdd\xd3\xc1\xcf\xe5\xeb\xf9\xf7',
    b'\x4d\x43\x51\x5f\x75\x7b\x69\x67\x3d\x33\x21\x2f\x05\x0b\x19\x17',
    b'\x76\x78\x6a\x64\x4e\x40\x52\x5c\x06\x08\x1a\x14\x3e\x30\x22\x2c',
    b'\x96\x98\x8a\x84\xae\xa0\xb2\xbc\xe6\xe8\xfa\xf4\xde\xd0\xc2\xcc',
    b'\x41\x4f\x5d\x53\x79\x77\x65\x6b\x31\x3f\x2d\x23\x09\x07\x15\x1b',
    b'\xa1\xaf\xbd\xb3\x99\x97\x85\x8b\xd1\xdf\xcd\xc3\xe9\xe7\xf5\xfb',
    b'\x9a\x94\x86\x88\xa2\xac\xbe\xb0\xea\xe4\xf6\xf8\xd2\xdc\xce\xc0',
    b'\x7a\x74\x66\x68\x42\x4c\x5e\x50\x0a\x04\x16\x18\x32\x3c\x2e\x20',
    b'\xec\xe2\xf0\xfe\xd4\xda\xc8\xc6\x9c\x92\x80\x8e\xa4\xaa\xb8\xb6',
    b'\x0c\x02\x10\x1e\x34\x3a\x28\x26\x7c\x72\x60\x6e\x44\x4a\x58\x56',
    b'\x37\x39\x2b\x25\x0f\x01\x13\x1d\x47\x49\x5b\x55\x7f\x71\x63\x6d',
    b'\xd7\xd9\xcb\xc5\xef\xe1\xf3\xfd\xa7\xa9\xbb\xb5\x9f\x91\x83\x8d',)

rcon = (
    b'\x00\x00\x00\x00',
    b'\x01\x00\x00\x00',
    b'\x02\x00\x00\x00',
    b'\x04\x00\x00\x00',
    b'\x08\x00\x00\x00',
    b'\x10\x00\x00\x00',
    b'\x20\x00\x00\x00',
    b'\x40\x00\x00\x00',
    b'\x80\x00\x00\x00',
    b'\x1b\x00\x00\x00',
    b'\x36\x00\x00\x00',
    b'\x36\x00\x00\x00',)

"""
AES Implementation itself
"""

def rot_word(s):
    """
    left rotation of items
    """
    s[0],s[1],s[2],s[3] = s[1],s[2],s[3],s[0]

def sub_byte(elem, box):
    """
    Helper function to index into magic arrays
    """
    return box[(elem & 0xf0) >> 4][(elem & 0x0f)]

def sub_bytes(state, box):
    for s in state:
        for b in s:
            b = sub_byte(b, box)

def shift_rows(state):
    """
    left rotate the row
    """
    permute = (0,1,2,3)
    for i in range(1,4):
        p0,p1,p2,p3 = permute
        state[0][i], state[1][i], state[2][i], state[3][i] = state[p1][i], state[p2][i], state[p3][i], state[p0][i]
        permute = [p1,p2,p3,p0]

        
def inv_shift_rows(state):
    """
    right rotate the row
    """
    permute = (0,1,2,3)
    for i in range(1,4):
        p0,p1,p2,p3 = permute
        state[0][i], state[1][i], state[2][i], state[3][i] = state[p3][i], state[p0][i], state[p1][i], state[p2][i]
        permute = (p3,p0,p1,p2)

        
def mix_cols(state):
    """
    s0' = ({02} * s0) ^ ({03} * s1) ^ s2 ^ s3
    blahblah
    """
    for s in state:
        s[0],s[1],s[2],s[3] = (sub_byte(s[0],a_x_2) ^ sub_byte(s[1],a_x_3) ^ s[2] ^ s[3],
                               s[0] ^ sub_byte(s[1],a_x_2) ^ sub_byte(s[2],a_x_3) ^ s[3],
                               s[0] ^ s[1] ^ sub_byte(s[2],a_x_2) ^ sub_byte(s[3],a_x_3),
                               sub_byte(s[0], a_x_3) ^ s[1] ^ s[2] ^ sub_byte(s[3],a_x_2))

def inv_mix_cols(state):
    """
    s0' = ({0e} * s0) ^ ({0b} * s1) ^ ({0d} * s2) ^ ({09} * s3)
    blahblah
    """
    for s in state:
        s[0],s[1],s[2],s[3] = (sub_byte(s[0],a_inv_x_e) ^ sub_byte(s[1],a_inv_x_b) ^ sub_byte(s[2],a_inv_x_d) ^ sub_byte(s[3],a_inv_x_9),
                               sub_byte(s[0],a_inv_x_9) ^ sub_byte(s[1],a_inv_x_e) ^ sub_byte(s[2],a_inv_x_b) ^ sub_byte(s[3],a_inv_x_d),
                               sub_byte(s[0],a_inv_x_d) ^ sub_byte(s[1],a_inv_x_9) ^ sub_byte(s[2],a_inv_x_e) ^ sub_byte(s[3],a_inv_x_b),
                               sub_byte(s[0],a_inv_x_b) ^ sub_byte(s[1],a_inv_x_d) ^ sub_byte(s[2],a_inv_x_9) ^ sub_byte(s[3],a_inv_x_e))

def inv_mix_cols_vec(s):
    """
    in place mix_cols on single vector
    """
    s[0],s[1],s[2],s[3] = (sub_byte(s[0],a_inv_x_e) ^ sub_byte(s[1],a_inv_x_b) ^ sub_byte(s[2],a_inv_x_d) ^ sub_byte(s[3],a_inv_x_9),
                           sub_byte(s[0],a_inv_x_9) ^ sub_byte(s[1],a_inv_x_e) ^ sub_byte(s[2],a_inv_x_b) ^ sub_byte(s[3],a_inv_x_d),
                           sub_byte(s[0],a_inv_x_d) ^ sub_byte(s[1],a_inv_x_9) ^ sub_byte(s[2],a_inv_x_e) ^ sub_byte(s[3],a_inv_x_b),
                           sub_byte(s[0],a_inv_x_b) ^ sub_byte(s[1],a_inv_x_d) ^ sub_byte(s[2],a_inv_x_9) ^ sub_byte(s[3],a_inv_x_e))

def add_round_key(state, rk):
    for i in range(4):
        for j in range(4):
            state[i][j] ^= rk[i][j]

def gen_key_schedule(key):
    """
    generates key schedule for 128,192,256 key lengths
    inv_key_schedule currently broken
    """
    if not (len(key) in [16,24,32]):
        print("wrong key size")
        exit(1)

    nk = len(key)//4
    nr = nk + 6
    key_schedule = [0] * 4*(nr+1)
    inv_key_schedule = key_schedule
            
    for i in range(4*(nr + 1)):
        if i < nk:
            key_schedule[i] = key[i*4:(i+1)*4]
        else:
            key_schedule[i] = key_schedule[i-1]
            if i % nk == 0:
                rot_word(key_schedule[i])
                key_schedule[i] = [sub_byte(b,s_box) ^ r for b,r in zip(key_schedule[i],rcon[i // nk])]
            elif nk > 6 and i % nk == 4:
                key_schedule[i] = [sub_byte(b,s_box) for b in key_schedule[i]]
            key_schedule[i] = [b ^ w_i for b,w_i in zip(key_schedule[i - nk],key_schedule[i])]
        inv_key_schedule[i] = key_schedule[i]

    for i in range(1,nr):
        inv_mix_cols(inv_key_schedule[i*4:(i+1)*4])

    return key_schedule,inv_key_schedule

#implement encryption/decrytpion
def encrypt(data, key_schedule):
    """
    working, though above implementations should be improved
    """
    state = data
    add_round_key(state, key_schedule[0:4])
    
    for r in range(1,len(key_schedule)//4 - 1):
        sub_bytes(state, s_box)
        shift_rows(state)
        mix_cols(state)
        add_round_key(state, key_schedule[r*4:(r+1)*4])

    sub_bytes(state, s_box)
    shift_rows(state)
    add_round_key(state, key_schedule[-4:])
    
    return state

def decrypt(data, key_schedule):
    """
    working
    """
    state = data
    add_round_key(state, key_schedule[-4:])

    for r in reversed(range(1,len(key_schedule)//4 - 1)):
        inv_shift_rows(state)
        sub_bytes(state, is_box)
        add_round_key(state, key_schedule[r*4:(r+1)*4])
        inv_mix_cols(state)

    inv_shift_rows(state)
    sub_bytes(state, is_box)
    add_round_key(state, key_schedule[0:4])
    
    return state

def nice_decrypt(data, inv_key_schedule):
    """
    currently borked
    """
    state = data
    add_round_key(state, inv_key_schedule[-4:])

    for r in reversed(range(1,len(inv_key_schedule)//4 - 1)):
        sub_bytes(state, is_box)
        inv_shift_rows(state)
        inv_mix_cols(state)
        add_round_key(state, inv_key_schedule[r*4:(r+1)*4])

    sub_bytes(state, is_box)
    inv_shift_rows(state)
    add_round_key(state, inv_key_schedule[0:4])
    
    return state
