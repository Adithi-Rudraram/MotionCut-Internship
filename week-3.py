import random
def password_gen(n_caps,n_small,n_nums,n_splchar):
    small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    splchar = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_gen = []
    #Using random library 
    for char in range(1, n_caps + 1):
        password_gen.append(random.choice(caps))

    for char in range(1, n_small + 1):
        password_gen += random.choice(small)

    for char in range(1, n_nums + 1):
        password_gen += random.choice(nums)

    for char in range(1, n_splchar + 1):
        password_gen += random.choice(splchar)

    random.shuffle(password_gen)

    password = ""
    for char in password_gen:
        password += char

    print(f"Your password is: {password}")




if __name__ == "__main__":
    print("WELCOME TO PASSWORD GENERATOR")
    a = int(input("Enter the length of the password : "))
    if a < 8:
        while True:
            print("Minimum length of the password must be 8. Please enter the number which is greater than or equal to 8")
            a = int(input("Enter the length of the password : "))
            if a >= 8:
                break

    n = 4

    #Dividing the given length into random parts
    arr = []
    for idx in range(n-1):
        arr.append(random.randint(1,a-sum(arr)-n+idx))
    arr.append(a-sum(arr))
    n_c, n_s, n_num, n_spl = arr[0], arr[1], arr[2], arr[3]
    password_gen(n_c,n_s,n_num,n_spl)
