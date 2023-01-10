import re 


# def part1():
    
#     file = open('day4.dat', 'r')
#     lines = file.readlines()

#     count = 0
#     password = []
#     passwordChunck = ""
    
    
    

#     for line in lines:
#         line = line.strip()
#         if (line == ''):
#             if(validate_passport(passwordChunck)):
#                 count += 1
#             passwordChunck = ""
#         else:
#             passwordChunck += line + " "
        
#     if(validate_passport(passwordChunck)):
#         count += 1
#     print('Part 1: ' + str(count))

# def validate_passport(passwordString):
#     print(passwordString)
#     reqs = ['byr',
#                     'iyr',
#                     'eyr',
#                     'hgt',
#                     'hcl',
#                     'ecl',
#                     'pid']

#     # passport = {}
#     # elements = passwordString.strip().split()

#     # for element in elements:
#     #     kvp = element.split(':')
#     #     passport[kvp[0]] = kvp[1]


#     print(all(req in passwordString for req in reqs))

#     return all(req in passwordString for req in reqs)

        
# part1()

reqs = ['byr',
                     'iyr',
                     'eyr',
                     'hgt',
                     'hcl',
                     'ecl',
                     'pid']


passports = []

def loadData(dataFile):
    passport = {}

    file = open(dataFile, 'r')
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        if line == '':
            passports.append(passport)
            passport = {}
        else:
            for element in line.split():
                k, v = element.split(':')
                passport[k] = v

    # Add the final passport to solve the fencepost problem
    passports.append(passport)





def part2():
    count = 0 
    for passport in passports:
        print(passport)
        if(all(req in passport.keys() for req in reqs)):
            print("here")
            byr = int(passport['byr'])
            if byr < 1920 or byr > 2002:
                continue
            # validate the issue year 
            iyr = int(passport['iyr'])
            if iyr < 2010 or iyr > 2020:
                continue

            #validate experation date 
            eyr = int(passport['eyr'])
            if eyr < 2020 or eyr > 2030:
                continue

            # validate hight 
            units = passport['hgt'][-2:]
            value = int(passport['hgt'][:-2])
            if units =='in':
                if value < 59 or value > 76:
                    continue 
            else: 
                if value < 150 or value > 193:
                    continue
            
            #Validate the hair color 
            hcl = passport['hcl']
            if re.search(r'^#[0-9a-f]{6}$', hcl) is None:
                continue

            # validat eye color 
            ecl = passport['ecl']
            if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                continue

            #validate pid
            pid = passport['pid']
            print(len(pid))
            if re.search(r'^[0-9]{9}$', pid) is None:
                continue


            
            print(str(value) + ' in ' + str(units))

            count += 1
    print('Part 2: ' + str(count))


loadData('day4.dat')
part2()