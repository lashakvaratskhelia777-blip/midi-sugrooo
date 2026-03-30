# შექმენით სახელების სია და filter-ით შეინახეთ მხოლოდ ის სახელები რომლებიც იწყება ა ასოთი
from os import system


saxelebi = ["ავთო", "ნინი", "გიორგი", "ალექსანდრე",  "ნინო", "მარიამი", "ბაჩო"]
filter = list(filter(lambda x: x.startswith("ა"),saxelebi))
print(filter)

