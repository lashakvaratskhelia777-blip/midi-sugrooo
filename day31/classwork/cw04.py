# შექმენით tuple ჩვენი ჯგუფის მოსწავლეებით, გამოიყენეთ unpacking პირველი სტუდენტი შეინახოს ცვლადში Student1, მეორე Student2ში ხოლო დანარჩენი ლისთში სახელად Others
info = ("ბაჩო", "გიორგი", "ვაჟა", "გაგა", "ნიკა")
Student1, Student2, *Others = students
print("Student1:", Student1)
print("Student2:", Student2)
print("Others:", Others)

