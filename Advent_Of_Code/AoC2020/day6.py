def part1():
    file = open('day6.dat', 'r')
    lines = file.readlines()
    chunk = []
    testChunk = []
    correctAnswers = 0

    for line in lines:
        if (line.strip() == ''):
            # for element in chunk:
            #     for letter in chunk:
            #         if element == letter:
            #             chunk.remove(element)

            # sum_unique += set_uniqueChuck(chunk)
            # sum_common += count_common(chunk)
            print(len(testChunk))
            correctAnswers += len(set(testChunk))
            testChunk = []
            
                
        else:
            #chunk.append(line)
            for element in line:
                testChunk.append(element)

    print(correctAnswers)
part1()

def set_uniqueChunk(group):
    uniques = {}
    for element in group:
        uniques.add(element)
    print(uniques)

