
all_txt = {}

with open('1.txt', encoding='UTF-8') as f:
    lines = f.readlines()
    all_txt[len(lines)] = ['1.txt\n'] + [str(len(lines))+'\n'] + lines


with open('2.txt', encoding='UTF-8') as f:
    lines = f.readlines()
    all_txt[len(lines)] = ['2.txt\n'] + [str(len(lines))+'\n'] + lines

with open('3.txt', encoding='UTF-8') as f:
    lines = f.readlines()
    all_txt[len(lines)] = ['3.txt\n'] + [str(len(lines))+'\n'] + lines

sort_all_txt = dict(sorted(all_txt.items()))

with open('all_txt.txt', 'w', encoding='UTF-8') as f:
    for t in sort_all_txt.values():
        f.writelines(t )
