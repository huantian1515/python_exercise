from datetime import datetime
from storage import load_records,save_records
from utils import format_record,calc_summary

class ExpenseTracker:
    def __init__(self):
        self.records = load_records()
    def save(self):
        save_records(self.records)
    def add_record(self):
        record_type = input("类型(1-收入 2-支出):")
        if record_type == "1":
            record_type = "收入"
        elif record_type == "2":
            record_type = "支出"
        else:
            print("无效类型")
            return
        try:
            amount = float(input("金额:"))
        except ValueError:
            print("无效金额")
            return
        category = input("分类:")
        note = input("备注:")
        date = datetime.now().strftime("%Y-%m-%d")
        record = {
            
            "date":date,
            "type":record_type,
            "category":category,
            "amount":amount,
            "note":note

        }
        self.records.append(record)
        self.save()
    def show_all(self):
        if not self.records:
            print("还没有任何记录")
            return
            
           
        sorted_records = sorted(self.records,key=lambda x:x["date"])
        for r in sorted_records:
            print(format_record(r))
        calc_summary(self.records)
    def show_by_category(self):
        category = input("输入要查询的分类:")
        show = [r for r in self.records if r["category"] == category]
        if not show:
            print(f"没有找到分类为「{category}」的记录")
            return

        for r in show:
            print(format_record(r))

        calc_summary(show) 
