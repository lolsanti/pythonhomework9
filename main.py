#filename = "domains.txt"

#my_files = open(filename, 'r')
#date = my_files.read()
#print(date)
#my_files.close()


##########################################1#############################################
"""


def read_domains(filename):
    with open(filename, 'r') as my_file:
        domains = [line.strip() for line in my_file.readlines()]
    return [domain.replace('.', '') for domain in domains]


domains = read_domains('domains.txt')
print(domains)

"""
##########################################2#############################################
"""


def get_surnames_from_file(filename):
    with open(filename, 'r') as file:
        surnames = []
        for line in file:
            data = line.strip().split('\t')
            surname = data[1]
            surnames.append(surname)
    return surnames


surnames = get_surnames_from_file('name.txt')
print(surnames)
"""
##########################################3#############################################
"""


def get_dates_from_file(filename):
    dates = []
    with open(filename, 'r') as f:
        for line in f:
            words = line.strip().split()
            for word in words:
                if any(char.isdigit() for char in word):
                    dates.append({"date": word})
    return dates


dates = get_dates_from_file('authors.txt')
print(dates)

"""















