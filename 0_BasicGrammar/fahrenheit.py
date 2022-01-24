print("본 프로그램은 섭씨를 화씨로 변환해주는 프로그램입니다.\n변환하고 싶은 섭씨 온도를 입력해 주세요:")
cel_input = float(input())
fah_value = ((9/5) * cel_input) + 32

print(f"섭씨온도 : {cel_input:.2f}")
print(f"화씨온도 : {fah_value:.2f}")