prompts = [
    {
        "title": "스마트 글래스 광고 이미지 생성",
        "category": "이미지 생성",
        "content": "미래지향적이면서 따뜻한 분위기의 스마트 글래스 광고 이미지를 생성해주세요.",
        "favorite": False
    },
    {
        "title": "반려동물 병원 앱 UI 디자인",
        "category": "이미지 생성",
        "content": "민트색을 중심으로 강아지와 고양이의 접종 기록을 확인할 수 있는 모바일 앱 화면을 디자인해주세요.",
        "favorite": False
    },
    {
        "title": "재고 부족 알림 메일 작성",
        "category": "자동화",
        "content": "현재 재고가 안전 재고보다 부족한 상품의 이름과 수량을 포함한 알림 메일을 작성해주세요.",
        "favorite": False
    }
]

def show_menu():
    print()
    print("나만의 프롬프트 관리 프로그램")
    print("1. 프롬프트 추가")
    print("2. 전체 목록 보기")
    print("3. 카테고리별 보기")
    print("4. 프롬프트 검색")
    print("5. 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")

def show_list():
    if len(prompts) == 0:
        print("저장된 프롬프트가 없습니다.")

    else:
        print("전체 프롬프트 목록")

        for index, prompt in enumerate(prompts):
            if prompt["favorite"] == True:
                mark = "★"
            else:
                mark = ""

            print(
                index + 1,
                ".",
                "[" + prompt["category"] + "]",
                prompt["title"],
                mark
            )

        print()
        print("총", len(prompts), "개의 프롬프트")

def show_favorites():
    count = 0

    print("즐겨찾기 목록")

    for prompt in prompts:
        if prompt["favorite"] == True:
            count = count + 1

            print(
                count,
                ".",
                "[" + prompt["category"] + "]",
                prompt["title"],
                "★"
            )

    if count == 0:
        print("즐겨찾기한 프롬프트가 없습니다.")

    else:
        print()
        print("총", count, "개의 즐겨찾기")

def search_prompt():
    while True:
        keyword = input("검색어를 입력하세요: ").strip()

        if keyword != "":
            break

        print("검색어는 비워둘 수 없습니다.")

    count = 0

    print()
    print("검색 결과")

    for prompt in prompts:
        if (
            keyword.lower() in prompt["title"].lower()
            or keyword.lower() in prompt["content"].lower()
        ):
            count = count + 1

            if prompt["favorite"] == True:
                mark = "★"
            else:
                mark = ""

            print(
                count,
                ".",
                "[" + prompt["category"] + "]",
                prompt["title"],
                mark
            )

    if count == 0:
        print("검색 결과가 없습니다.")

    else:
        print()
        print("총", count, "개의 프롬프트를 찾았습니다.")

def show_detail():
    if len(prompts) == 0:
        print("저장된 프롬프트가 없습니다.")

    else:
        print("프롬프트 목록")

        for index, prompt in enumerate(prompts):
            print(index + 1, ".", prompt["title"])

        number_input = input("상세히 볼 번호를 입력하세요: ")

        if number_input.isdigit():
            number = int(number_input)

            if number >= 1 and number <= len(prompts):
                selected_prompt = prompts[number - 1]

                if selected_prompt["favorite"] == True:
                    mark = "★"
                else:
                    mark = "☆"

                print("프롬프트 상세 정보")
                print("제목:", selected_prompt["title"])
                print("카테고리:", selected_prompt["category"])
                print("즐겨찾기:", mark)
                print("내용:", selected_prompt["content"])

            else:
                print("올바른 번호를 입력해주세요.")

        else:
            print("숫자를 입력해주세요.")

def manage_favorite():
    if len(prompts) == 0:
        print("저장된 프롬프트가 없습니다.")

    else:
        print("프롬프트 목록")

        for index, prompt in enumerate(prompts):
            if prompt["favorite"] == True:
                mark = "★"
            else:
                mark = "☆"

            print(index + 1, ".", mark, prompt["title"])

        number_input = input("즐겨찾기를 변경할 번호를 입력하세요: ")

        if number_input.isdigit():
            number = int(number_input)

            if number >= 1 and number <= len(prompts):
                selected_prompt = prompts[number - 1]

                if selected_prompt["favorite"] == False:
                    selected_prompt["favorite"] = True
                    print("즐겨찾기에 등록되었습니다.")

                else:
                    selected_prompt["favorite"] = False
                    print("즐겨찾기에서 해제되었습니다.")

            else:
                print("올바른 번호를 입력해주세요.")

        else:
            print("숫자를 입력해주세요.")

def show_by_category():
    categories = [
        "텍스트 생성",
        "이미지 생성",
        "영상 생성",
        "페르소나",
        "자동화",
        "기타"
    ]

    print("조회할 카테고리를 선택하세요.")

    for index, category_name in enumerate(categories):
        print(index + 1, ".", category_name)

    print("7. 직접 입력")

    while True:
        category_choice = input("카테고리 번호를 입력하세요: ")

        if category_choice in ["1", "2", "3", "4", "5", "6"]:
            category_search = categories[int(category_choice) - 1]
            break

        elif category_choice == "7":
            category_search = input(
                "조회할 카테고리를 직접 입력하세요: "
            ).strip()

            if category_search != "":
                break

            print("카테고리는 비워둘 수 없습니다.")

        else:
            print("올바른 카테고리 번호를 입력해주세요.")

    count = 0

    print()
    print("[" + category_search + "] 카테고리 프롬프트")

    for prompt in prompts:
        if prompt["category"] == category_search:
            count = count + 1

            if prompt["favorite"] == True:
                mark = "★"
            else:
                mark = ""

            print(count, ".", prompt["title"], mark)

    if count == 0:
        print("해당 카테고리의 프롬프트가 없습니다.")

    else:
        print()
        print("총", count, "개의 프롬프트")

while True:
    show_menu()

    choice = input("메뉴를 선택하세요: ")

    if choice == "1":
        while True:
            title = input("프롬프트 제목을 입력하세요: ").strip()

            if title != "":
                break

            print("제목은 비워둘 수 없습니다.")

        categories = [
            "텍스트 생성",
            "이미지 생성",
            "영상 생성",
            "페르소나",
            "자동화",
            "기타"
        ]

        print("카테고리를 선택하세요.")

        for index, category_name in enumerate(categories):
            print(index + 1, ".", category_name)

        print("7. 직접 입력")

        while True:
            category_choice = input("카테고리 번호를 입력하세요: ")

            if category_choice in ["1", "2", "3", "4", "5", "6"]:
                category = categories[int(category_choice) - 1]
                break

            elif category_choice == "7":
                while True:
                    category = input("카테고리를 직접 입력하세요: ").strip()

                    if category != "":
                        break

                    print("카테고리는 비워둘 수 없습니다.")

                break

            else:
                print("올바른 카테고리 번호를 입력해주세요.")

        while True:
            content = input("프롬프트 내용을 입력하세요: ").strip()

            if content != "":
                break

            print("내용은 비워둘 수 없습니다.")
        prompt = {
            "title": title,
            "category": category,
            "content": content,
            "favorite": False
        }

        prompts.append(prompt)

        print("프롬프트가 추가되었습니다.")
        print(prompts)

    elif choice == "2":
        show_list()

    elif choice == "3":
        show_by_category()

    elif choice == "4":
        search_prompt()

    elif choice == "5":
        show_detail()

    elif choice == "6":
        manage_favorite()

    elif choice == "7":
        show_favorites()

    elif choice == "0":
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 메뉴 번호를 입력해주세요.")