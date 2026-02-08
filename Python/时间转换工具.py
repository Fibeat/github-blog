import pandas as pd

def get_weekly_workday_ranges(year, month):
    """按周获取工作日区间"""
    start_date = f"{year}-{month:02d}-01"
    end_date = pd.Timestamp(start_date) + pd.offsets.MonthEnd(1)
    
    workdays = pd.bdate_range(start=start_date, end=end_date)
    
    if len(workdays) == 0:
        return []
    
    # 按周分组
    weekly_ranges = []
    current_week = workdays[0].week
    
    week_start = workdays[0]
    
    for i in range(1, len(workdays)):
        if workdays[i].week != current_week:
            # 新的一周开始，保存上一周的区间
            week_end = workdays[i-1]
            weekly_ranges.append((
                week_start.strftime('%Y-%m-%d'),
                week_end.strftime('%Y-%m-%d')
            ))
            week_start = workdays[i]
            current_week = workdays[i].week
    
    # 添加最后一周
    weekly_ranges.append((
        week_start.strftime('%Y-%m-%d'),
        workdays[-1].strftime('%Y-%m-%d')
    ))
    
    return weekly_ranges

# 使用示例
weekly_ranges = get_weekly_workday_ranges(2025, 11)
print("2025年12月按周划分的工作日区间:")
for i, (start, end) in enumerate(weekly_ranges, 1):
    start,end = start.replace('-','.'),end.replace('-','.')
    print(f"{start}-{end}")