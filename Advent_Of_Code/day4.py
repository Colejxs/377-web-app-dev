file = open('dau4.dat', 'r')
lines = file.readLines()

def start():
    global file
    global lines 

    for line in lines:
        line = line.strip()
        elves = line.split(",")

        elf1 = elves[0].split("-")
        elf2 = elves[1].split("-")

        elf_1_low = int(elf1[0])
        elf_1_high = int(elf1[1])

        elf_2_low = int(elf2[0])
        elf_2_high = int(elf2[1])

        if((elf_2_low >= elf_1_low and elf_2_low <= elf_1_high) or (elf_2_high >= elf_1_low and elf_2_high <= elf_1_high)):
            #a pair is found 
            count +=1
            
            
