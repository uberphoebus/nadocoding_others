# https://youtu.be/kla7FiwnAvE

# [조건]
# 1. 유튜버 이름은 리스트로 제공
# 2. 파일명은 '유튜버 이름.txt'로 저장

# [메일 본문]
# 안녕하세요? XXX님.

# (주)나도출판 편집자 나코입니다.
# 현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.
# XXX님의 유튜브 영상을 보고 연락을 드리게 되었습니다.
# 자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.

# 좋은 하루 보내세요 ^^
# 감사합니다.

# - 나코 드림.
names = [f'유튜버{i}' for i in range(1, 5)]

for name in names:
    with open(f'{name}.txt', 'w', encoding='utf8') as file:
        text = f"""
안녕하세요? {name}님.

(주)나도출판 편집자 나코입니다.
현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.
XXX님의 유튜브 영상을 보고 연락을 드리게 되었습니다.
자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.

좋은 하루 보내세요 ^^
감사합니다.
"""
        file.write(text)