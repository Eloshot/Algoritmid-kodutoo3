a = [4,2,3,1,7,8,9,6,]

def linearotsing(list,otsitav):
    lenght = int(len(list)) - 1
    for i in range(len(list)):
        if list[i] == otsitav:
            return(f"element asub kohal {i} {}")
        if i == lenght:
            return("element pole sellises listis")
        
print(linearotsing(a,7))
        
        