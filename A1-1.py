prompts = []

while True:
    print()
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

        prompts.append(prompt)

        print("프롬프트가 추가되었습니다.")
        print(prompts)

    elif choice == "2":
        if len(prompts) == 0:
           print("저장된 프롬프트가 없습니다.")
        else:
            print("전체 프롬프트 목록")

            for prompt in prompts:
                print("제목:", prompt["title"])
                print("카테고리:", prompt["category"])
                print("내용:", prompt["content"])
                print()

    elif choice == "3":
        category_search = input("조회할 카테고리를 입력하세요: ")
        found = False

        for prompt in prompts:
            if prompt["category"] == category_search:
                print("제목:", prompt["title"])
                print("카테고리:", prompt["category"])
                print("내용:", prompt["content"])
                print()
                found = True

        if found == False:
            print("해당 카테고리의 프롬프트가 없습니다.")

    elif choice == "4":
        keyword = input("검색어를 입력하세요: ")
        found = False

        for prompt in prompts:
            if keyword in prompt["title"] or keyword in prompt["content"]:
                print("제목:", prompt["title"])
                print("카테고리:", prompt["category"])
                print("내용:", prompt["content"])
                print()
                found = True

        if found == False:
            print("검색 결과가 없습니다.")
            
    elif choice == "5":
        if len(prompts) == 0:
            print("저장된 프롬프트가 없습니다.")
        else:
            print("프롬프트 목록")

            for index, prompt in enumerate(prompts):
                print(index + 1, ".", prompt["title"])

            number = int(input("상세히 볼 번호를 입력하세요: "))

            if number >= 1 and number <= len(prompts):
                selected_prompt = prompts[number - 1]

                print("프롬프트 상세 정보")
                print("제목:", selected_prompt["title"])
                print("카테고리:", selected_prompt["category"])
                print("내용:", selected_prompt["content"])
            else:
                print("올바른 번호를 입력해주세요.")

    elif choice == "0":
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 메뉴 번호를 입력해주세요.")