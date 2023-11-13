class datas:
    def __init__(self, txt):
        self.storage = txt

    def add(self, data):
        with open(self.storage, 'a') as f:
            f.write(data + '\n')

    def remove(self):
        temp = []
        with open(self.storage, 'r') as f:
            for line in f:
                temp.append(line)
        temp.pop()
        open(self.storage, "w").close()
        with open(self.storage, 'w') as g:
            g.writelines(temp)

    def print(self):
        with open(self.storage, 'r') as f:
            for line in f:
                print(line)
