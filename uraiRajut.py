def urai(huruf):
  hasil = ''
  for i in range(len(huruf)): #menghitung panjang karakter
    for j in range(i+1): 
      hasil += huruf[j] #ditambahkan setiap index ke j
  return hasil  

def rajut(huruf):
  hasil = ''
  counter = 2
  j = 1
  while j <= len(huruf):
    hasil+= huruf[j-1]
    j += counter
    counter += 1
  return hasil


print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))
print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))
                                                                                                                                                                                                                                                                                                                                                         