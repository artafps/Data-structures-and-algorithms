class TreeNode:
    def __init__(self, val):
        # هر گره دارای مقدار، فرزند چپ، فرزند راست، و ارتفاع است.
        self.val = val
        self.left = None
        self.right = None
        self.height = 1  # ارتفاع ابتدایی یک است (برای گره‌های بدون فرزند).

class AVL:
    def __init__(self):
        self.pre = []  # یک لیست برای ذخیره مقادیر گره‌ها به ترتیب preorder.

    def insert(self, root, key):
        # تابع درج یک کلید در درخت AVL.
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # به‌روزرسانی ارتفاع گره.
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # بررسی و اعمال چرخش‌های مورد نیاز برای حفظ تعادل.
        balance = self.getBalance(root)

        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)

        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):
        # چرخش به چپ.
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        # به‌روزرسانی ارتفاع گره‌ها.
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rightRotate(self, z):
        # چرخش به راست.
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        # به‌روزرسانی ارتفاع گره‌ها.
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def getHeight(self, root):
        # تابع دریافت ارتفاع گره.
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        # تابع دریافت تعادل گره (تفاوت ارتفاع زیردرخت چپ و راست).
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def preOrder(self, root):
        # تابع گردش preorder درخت و چاپ مقادیر گره‌ها.
        if not root:
            return
        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def preOrdergetlist(self, root):
        # تابع گردش preorder درخت و ذخیره مقادیر گره‌ها در لیست.
        if not root:
            return
        self.pre.append(root.val)
        self.preOrdergetlist(root.left)
        self.preOrdergetlist(root.right)

def isAVL(tree):
    # تابع بررسی اینکه آیا یک لیست اعداد می‌تواند یک درخت AVL معتبر را نمایش دهد یا خیر.
    myTree = AVL()
    root = None
    for node in tree:
        root = myTree.insert(root, node)
    myTree.preOrdergetlist(root)
    return myTree.pre == tree

# مثال‌ها:
print(isAVL([30, 20, 10, 25, 40, 50]))  # True
print(isAVL([30, 20, 25, 10, 40, 50]))  # False
print(isAVL([1]))  # True

        
"""The constructed AVL Tree for [10, 20, 25, 30, 40, 50] would be
            30 
           /  \ 
         20   40 
        /  \     \ 
       10  25    50
"""

