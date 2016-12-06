#coding=utf-8
# 소수점 이하 셋째 자리까지 부동소숫점 숫자표기(0.333)
print '{0:.3f}'.format(1.0/3)
#밑줄로 11칸 채우고 가운데 정렬(^)하기(________ hello_______)
print'{0:_^11}'.format('hello')
#사용자 지정 키워드를 이용해 (Swaroop worte A Byte of Python)표기
print '{name} wrote{book}'.format(name ='swaroop', book='A byte of Python')
