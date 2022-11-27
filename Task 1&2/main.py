# დავალება 1


# დაწერეთ პროგრამა, რომელშიც მომხმარებელი
# კონსოლიდან შეიტანს 5 String სტრიქონს, ხოლო
# კონსოლში დაიბეჭდება ყველაზე დიდი სტრიქონის სიგრძე.
lst = []
# lst = ['mmmm','yyyyy','yyy','rr','jjjjjj']
for i in range(0,5):
    lst.append(input(f'Enter {i+1}th string  '))

# i=0
# while i<5:
#     lst.append(input(f'Enter {i + 1}th string  '))
#     i+=1

#print(lst)
max = len(lst[0]) #4
max_element = lst[0] #'mmmm'
for i in lst:
    if max < len(i):
        max=len(i)
        max_element = i
print(f'Max element is: {max_element}')

#დაწერეთ ფუნქცია, რომელსაც გადაეცემა მთელი
# რიცხვების ლისტი და დააბრუნებს მათ შორის
# მაქსიმალურს.

def max_int (lst):
   max = lst[0]
   for i in lst:
       if max < i:
           max=i
   return max

lst = [1,5,8,23,0,5,2]
print(max_int(lst))

#დაწერეთ ფუნქცია, რომელსაც გადაეცემა რიცხვი n და
# რეკურსიულად დაითვლის n რიცხვის ფაქტორიალს.

def factor (n):
    if n == 0:
        return 1
    return n*factor(n-1)

print(factor(5))


# დავალება 2


# დაწერე პროგრამა რომელიც ფაილიდან წაიკითხავს 10
# რიცხვს და ამავე ფაილში ჩაწერს მხოლოდ მაქსიმალურს
# წაკითხული რიცხვებიდან
f = open ('file','r+')
lst = [x[:-1] for x in f]
lst = lst[:10]
f.writelines(max(lst))
f.close()

# დაწერე ფუნქცია, რომელსაც გადაეცემა Dictionary და
# დააბრუნებს რიცხვით value -ებს შორის მინიმალურს
def min_dct (dct):
    return min(dct.values())

print(min_dct({'Natia':27,'Mari':22,'Nino':50,'lily':8}))

# დაწერე ფუნქცია, რომელიც ფაილიდან წაიკითხავს
# ინფორმაციას, შეავსებს სეტს მხოლოდ უნიკალური
# ელემენტებით და დააბრუნებს ამ სეტს

def set_file (file_name):
    f= open(file_name,'r')
    s = set([x[:-1] for x in f])
    f.close()
    return s


print(set_file("file"))