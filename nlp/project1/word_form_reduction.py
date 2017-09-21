import config as c
import re

_rule_set = set()
_dic = dict()


def read_rule():
    with open(c.RULE_PATH, encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n').split('\t')
            value = line[0] + '\t'
            if line[1] != '0':
                value += line[1]
            _rule_set.add(value)
    f.close()


def read_dic():
    with open(c.DIC_PATH, encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n').split('\t')
            value = ''
            if len(line) > 1:
                value = line[1]
                for l in line[2:]:
                    value += '\t'+l
            _dic[line[0]] = value
    f.close()


def reduction(word):
    if word in _dic:
        print(word + ":", end='')
        outputs = _dic[word].split('\t')
        for output in outputs:
            if re.match('[a-z]', output):
                print('')
            else:
                print('\t', end='')
            print(output, end='')
        print('')
    for rule in _rule_set:
        rule = rule.split('\t')
        if word.endswith(rule[0]):
            if rule[1] != '#':
                target = word[:word.index(rule[0])] + rule[1]
            else:
                target = word[:word.index(rule[0])-1]
            if target in _dic:
                print(target+" :", end='')
                outputs = _dic[target].split('\t')
                for output in outputs:
                    if re.match('[a-z]', output):
                        print('')
                    else:
                        print('\t', end='')
                    print(output, end='')
                print('')
    print('')


if __name__ == '__main__':
    read_rule()
    read_dic()
    # print(len(_dic))
    words = input("请输入一个或多个单词（多个单词用空格隔开）:\n")
    words = words.strip('.').split(' ')
    print(words)
    for word in words:
        reduction(word)
