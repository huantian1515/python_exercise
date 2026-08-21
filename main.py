from tracker import ExpenseTracker
def main():
    tracker = ExpenseTracker()
    while True:
        print("\n===== 个人记账本 v2 =====")
        print("1. 记一笔账")
        print("2. 查看所有记录")
        print("3. 按分类筛选")
        print("4. 退出")
        choice = input("请选择操作：")
        if choice == "1":
            tracker.add_record()
        elif choice == "2":
            tracker.show_all()
        elif choice == "3":
            tracker.show_by_category()
        elif choice == "4":
            tracker.save()
            print("感谢使用，再见！")
            break
if __name__ == "__main__":
    main()
