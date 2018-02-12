class MFile:
    def __init__(self, file_name, sizes=[20], encoding='utf-8', filler='='):
        self.mdata = MData(sizes, filler=filler)
        self.file = open(file_name, "r+b")
        self.file.seek(0)
        self.data_length = sum([s for s in sizes])
        self.enc = encoding

        mdata = MData([20])
        data = str(self.file.read(20), self.enc)
        val = mdata.getObjFromData(data)[0]
        if val == '':
            self.file.write(bytearray(mdata.get_string_data([val]), self.enc))
            self.largest_id=0
        else:
            self.largest_id=int(val)

    def update_data(self, id, new_data):
        if id>self.largest_id:
            self.largest_id=id
            self.file.seek(0)
            mdata = MData([20])
            new_val = mdata.get_string_data([id])
            self.file.write(bytearray(new_val, self.enc))
        new_data = self.mdata.get_string_data(new_data)
        data = bytearray(new_data, self.enc)
        self.file.seek(id*self.data_length)
        self.file.write(data)

    def get_data(self, id):
        self.file.seek(id*self.data_length)
        data = self.mdata.getObjFromData(str(self.file.read(self.data_length), self.enc))
        return data

    def insert_data(self, new_data):
        id = 1
        while id<= self.largest_id:
            data = self.get_data(id)
            if data[0] == '':
                break
            id += 1
        self.update_data(id,new_data)
        return id

    def delete_data(self, id):
        data = bytearray("="*self.data_length, self.enc)
        self.file.seek(id * self.data_length)
        self.file.write(data)




class MData:
    def __init__(self, sizes=[10], filler='='):
        self.length = sum(i for i in sizes)
        self.sizes=sizes
        self.filler = filler

    def get_string_data(self, objects):
        data = ''
        i=0
        for ob in objects:
            l = str(ob)
            if self.sizes[i] < len(l): raise 1
            l += self.filler*(self.sizes[i]-len(l))
            data += l
            i += 1
        return data

    def getObjFromData(self, sttr):
        b=[]
        s=0
        for i in range(0, len(self.sizes)):
            b.append(sttr[s:s+self.sizes[i]])
            s += self.sizes[i]
        j=0
        for a in b:
            for i in range(0, len(a)):
                if a[i] == self.filler :
                    b[j] = a[0:i]
                    j+=1
                    break
                elif i == len(a)-1:
                    b[j] = a[0:i+1]
                    j += 1
                    break

        return b


'''
f=MFile("temp", [10,10])
print(f.largest_id)
f.insert_data(["Govind",100])
#print(f.get_data(3))
print(f.largest_id)
#f.delete_data(1)
'''
