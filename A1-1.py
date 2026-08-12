print("나만의 프롬프트 관리 프로그램")
print("1. 프롬프트 추가")
print("2. 전체 목록 보기")
print("3. 카테고리별 보기")
print("4. 프롬프트 검색")
print("5. 상세 보기")
print("6. 즐겨찾기 관리")
print("0. 종료")
choice = input("메뉴를 선택하세요: ")
if choice == "1":
    title = input("프롬프트 제목을 입력하세요: ")
    category = input("카테고리를 입력하세요: ")
    content = input("프롬프트 내용을 입력하세요: ")
    prompt = {
    "title": title,
    "category": category,
    "content": content
}

    print("프롬프트가 추가되었습니다.")
    print(prompt)
elif choice == "2":
    print("전체 목록 보기를 선택했습니다.")
elif choice == "0":
    print("프로그램을 종료합니다.")
else:
    print("올바른 메뉴 번호를 입력해주세요.")