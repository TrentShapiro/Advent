import math

#read data
current_day = 'day13'
with open(current_day+'_input.txt','r') as f:
	data_in = f.readlines()

data_in = [i.replace('\n','') for i in data_in]

time_target = int(data_in[0])
busses = data_in[1].split(',')

avail_busses = [int(i) for i in busses if i != 'x']


#Part 1
def time_to_bus(target, bus):
    return int(math.ceil(target/bus) * bus) - target

times = [time_to_bus(time_target, i) for i in avail_busses]
print('Part 1: ')
print(f'best bus to take is: { avail_busses[times.index(min(times))] }')
print(f'answer is: {avail_busses[times.index(min(times))] * min(times)}')


#Part 2
print('\n\nPart 2: ')
time_reqs = [(int(i), idx) for idx, i in enumerate(busses) if i != 'x']
time_reqs = sorted(time_reqs, key = lambda x: x[0])[::-1]
increment = 1
current_time = 0
solution = False
prev_highest_match = 0
while not solution:
    count_match = 0
    for idx,req in enumerate(time_reqs):
        if (current_time+req[1])%req[0] != 0:
            break
        else:
            count_match+=1
    
    #if we find a larger match than the previous one, then we know that a solution
    #will also be a number offset by the LCM of all busses matched until now, so we
    #can update our search increment to be this LCM value. 
    if count_match > prev_highest_match:
        print(f'found highest inc at {current_time}, matched {count_match}')
        bus_ids = [i[0] for i in time_reqs]
        increment = math.lcm(*[1]+bus_ids[0:count_match])
        prev_highest_match = count_match
    
    if count_match == len(time_reqs):
        print(f'SOLUTION FOUND AT {current_time}')
        solution = True
    else:
        current_time+=increment
