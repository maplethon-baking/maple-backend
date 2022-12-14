#쿠키 - 버터, 초코, 커피 - 초코칩, 견과류, 잼
#케이크 - 초코, 치즈, 버터 - 과일, 견과류, 잼
#휘낭시에 - 버터, 얼그레이, 솔티드 카라멜 - 견과류, 초코, 없음

#python manage.py shell 실행 후 아래 코드를 따라해주세요.

from recipe.models import Category

a1 = Category(title='쿠키')
a2 = Category(title='케이크')
a3 = Category(title='휘낭시에')
a1.save()
a2.save()
a3.save()

b1 = Category(title='버터', parent=a1)
b2 = Category(title='초코', parent=a1)
b3 = Category(title='커피', parent=a1)
b1.save()
b2.save()
b3.save()

b4 = Category(title='초코', parent=a2)
b5 = Category(title='치즈', parent=a2)
b6 = Category(title='버터', parent=a2)
b4.save()
b5.save()
b6.save()

b7 = Category(title='버터', parent=a3)
b8 = Category(title='얼그레이', parent=a3)
b9 = Category(title='솔티드 카라멜', parent=a3)
b7.save()
b8.save()
b9.save()

c1 = Category(title='초코칩', parent=b1)
c2 = Category(title='견과류', parent=b1)
c3 = Category(title='잼', parent=b1)
c4 = Category(title='초코칩', parent=b2)
c5 = Category(title='견과류', parent=b2)
c6 = Category(title='잼', parent=b2)
c7 = Category(title='초코칩', parent=b3)
c8 = Category(title='견과류', parent=b3)
c9 = Category(title='잼', parent=b3)
c1.save()
c2.save()
c3.save()
c4.save()
c5.save()
c6.save()
c7.save()
c8.save()
c9.save()

d1 = Category(title='과일', parent=b4)
d2 = Category(title='견과류', parent=b4)
d3 = Category(title='잼', parent=b4)
d4 = Category(title='과일', parent=b5)
d5 = Category(title='견과류', parent=b5)
d6 = Category(title='잼', parent=b5)
d7 = Category(title='과일', parent=b6)
d8 = Category(title='견과류', parent=b6)
d9 = Category(title='잼', parent=b6)
d1.save()
d2.save()
d3.save()
d4.save()
d5.save()
d6.save()
d7.save()
d8.save()
d9.save()

e1 = Category(title='초코', parent=b7)
e2 = Category(title='견과류', parent=b7)
e3 = Category(title='없음', parent=b7)
e4 = Category(title='초코', parent=b8)
e5 = Category(title='견과류', parent=b8)
e6 = Category(title='없음', parent=b8)
e7 = Category(title='초코', parent=b9)
e8 = Category(title='견과류', parent=b9)
e9 = Category(title='없음', parent=b9)
e1.save()
e2.save()
e3.save()
e4.save()
e5.save()
e6.save()
e7.save()
e8.save()
e9.save()