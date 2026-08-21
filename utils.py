def format_record(r):
    return f"{r['date']:<12}{r['type']:<6}{r['category']:<10}{r['amount']:<10.1f}{r['note']}"
def calc_summary(records):
    if not records:
        print("还没有任何记录")
    else:
        total_income = 0
        total_expense = 0
        for r in records:
            
            if r["type"] == "收入":
                total_income += r["amount"]
                   
            elif r["type"] == "支出":
                total_expense += r["amount"]
                    
        balance = total_income - total_expense
        return print(f"\n总收入: {total_income} | 总支出: {total_expense} | 结余: {balance}")