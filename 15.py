# 만약 입력으로 `김다정`이라는 이름이 주어지면
# 안녕하세요. 저는 김다정입니다.
# 라고 출력하게 해주세요.

name = input("이름을 입력하세요: ")

print(f'안녕하세요. 저는 {name}입니다.')
print('안녕하세요. 저는 {}입니다.'.format(name)) # f-string 포매팅
print('안녕하세요. 저는 %s입니다.' % name)