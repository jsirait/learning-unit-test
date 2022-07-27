cheese = ['Cheddar', 'Stilton']
cheese.append('Oke')

machines = {'user100': 'yogi',

            'user1'  : 'booboo',
            
                        'user2'  : 'rupert',
                        
                                    'user3'  : 'teddy',
                                    
                                                'user4'  : 'care',
                                                
                                                            'user5'  : 'winnie',
                                                            
                                                                        'user6'  : 'sooty',
                                                                        
                                                                                    'user7'  : 'padders',
                                                                                    
                                                                                                'user8'  : 'polar',
                                                                                                
                                                                                                            'user9'  : 'grizzly',
                                                                                                            
                                                                                                                        'user10' : 'baloo',
                                                                                                                        
                                                                                                                                    'user11' : 'bungle',
                                                                                                                                    
                                                                                                                                                'user12' : 'fozzie',
                                                                                                                                                
                                                                                                                                                            'user13' : 'huggy',
                                                                                                                                                            
                                                                                                                                                                        'user14' : 'barnaby',
                                                                                                                                                                        
                                                                                                                                                                                    'user15' : 'hair',
                                                                                                                                                                                    
                                                                                                                                                                                                'user16' : 'greppy'}

print(len(machines))
del machines['user14']
print(len(machines))

machines['user15'] = 'cinnamon'

machines['user17'] = machines['user16']
del machines['user16']

leaving = ['user4', 'user5', 'user6']
unallocated = []
for ll in leaving:
    unallocated.append(machines.pop(ll))
print(f"unallocated: {unallocated}")

machines['user8'] = [machines['user8'], 'kodiak']

for uu in machines:
    print(f"User: {uu}; Machine: {machines[uu]}")

print(f"Unallocated machines: {sorted(unallocated)}")