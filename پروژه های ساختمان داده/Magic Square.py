def MagicSquare(n):  # تعریف تابع ایجاد جادوگریده برای اعداد فردی
    magicSquare = [[-1 for _ in range(n)] for _ in range(n)]  # ایجاد یک ماتریس n در n و مقداردهی اولیه با -1
    row, col = n // 2, 0  # مکان شروع اعداد

    for i in range(1, n * n + 1):
        magicSquare[row][col] = i  # قرار دادن عدد در ماتریس

        if i % n == 0:  # اگر عدد تقسیم‌پذیر بر n باشد، تغییر ستون
            col -= 1
        else:
            row -= 1  # در غیر این صورت، تغییر سطر و ستون به طور همزمان
            col += 1
        row = (row + n) % n  # حلقه میانبر برای مدیریت شروع از ابتدای ماتریس
        col = (col + n) % n

    # چاپ جادوگریده
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j], end=" ")
        print()

# ---------- Main ----------#
MagicSquare(5)  # تابع را با n=5 فراخوانی کن
