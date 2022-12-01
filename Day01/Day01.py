def read_data(file_path):
    f = open(file_path,'r')
    lines = f.read().split('\n\n')
    
    return lines

def calc_sums(data):
    elves = []
    for elf in data:
        elf_total = 0
        elf = elf.split('\n')

        for i in elf:
            elf_total += int(i)
        
        elves.append(elf_total)
        
    elves.sort(reverse=True)

    return elves

data = read_data('./data/Day01.txt')
elves = calc_sums(data)

print(f'Part 1 Solution: {max(elves)}')
print(f'Part 2 Solution: {sum(elves[:3])}')