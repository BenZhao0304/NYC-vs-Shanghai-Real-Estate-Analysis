import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 生成时间序列（48 个月 = 4 年）
months = 48
dates = pd.date_range(start="2020-01-01", periods=months, freq='M')

# 生成 NYC vs. 上海 关键数据（模拟）
np.random.seed(42)
nyc_rental_yield = np.random.normal(loc=4.5, scale=0.3, size=months)
shanghai_rental_yield = np.random.normal(loc=3.8, scale=0.6, size=months)

nyc_vacancy_rate = np.random.normal(loc=8.0, scale=1.5, size=months)
shanghai_vacancy_rate = np.random.normal(loc=12.2, scale=2.0, size=months)

nyc_esg_cost = np.random.normal(loc=2.5, scale=0.2, size=months)
shanghai_esg_cost = np.random.normal(loc=4.2, scale=0.3, size=months)

# 生成 NYC vs. 上海 租金收益趋势图
plt.figure(figsize=(10, 5))
plt.plot(dates, nyc_rental_yield, label="NYC Rental Yield (%)", color="blue")
plt.plot(dates, shanghai_rental_yield, label="Shanghai Rental Yield (%)", color="red", linestyle="dashed")
plt.xlabel("Year")
plt.ylabel("Rental Yield (%)")
plt.title("NYC vs. Shanghai Commercial Rental Yield Trends (2020-2024)")
plt.legend()
plt.grid()
plt.savefig("/Users/zivwu/Desktop/rental_yield_trend.png", dpi=300)
plt.show()

# 生成 NYC vs. 上海 空置率趋势图
plt.figure(figsize=(10, 5))
plt.plot(dates, nyc_vacancy_rate, label="NYC Vacancy Rate (%)", color="blue")
plt.plot(dates, shanghai_vacancy_rate, label="Shanghai Vacancy Rate (%)", color="red", linestyle="dashed")
plt.xlabel("Year")
plt.ylabel("Vacancy Rate (%)")
plt.title("NYC vs. Shanghai Commercial Vacancy Rate Trends (2020-2024)")
plt.legend()
plt.grid()
plt.savefig("/Users/zivwu/Desktop/vacancy_rate_trend.png", dpi=300)
plt.show()

# 生成 NYC vs. 上海 ESG 合规成本趋势图
plt.figure(figsize=(10, 5))
plt.plot(dates, nyc_esg_cost, label="NYC ESG Compliance Cost ($/sqft)", color="blue")
plt.plot(dates, shanghai_esg_cost, label="Shanghai ESG Compliance Cost ($/sqft)", color="red", linestyle="dashed")
plt.xlabel("Year")
plt.ylabel("ESG Compliance Cost ($/sqft)")
plt.title("NYC vs. Shanghai ESG Compliance Cost Trends (2020-2024)")
plt.legend()
plt.grid()
plt.savefig("/Users/zivwu/Desktop/esg_compliance_cost_trend.png", dpi=300)
plt.show()
# 生成 NYC vs. 上海 ESG 合规成本趋势图
plt.figure(figsize=(10, 5))
plt.plot(dates, nyc_esg_cost, label="NYC ESG Compliance Cost ($/sqft)", color="blue")
plt.plot(dates, shanghai_esg_cost, label="Shanghai ESG Compliance Cost ($/sqft)", color="red", linestyle="dashed")
plt.xlabel("Year")
plt.ylabel("ESG Compliance Cost ($/sqft)")
plt.title("NYC vs. Shanghai ESG Compliance Cost Trends (2020-2024)")
plt.legend()
plt.grid()

# 保存图片到桌面
plt.savefig("/Users/zivwu/Desktop/esg_compliance_cost_trend.png", dpi=300)

# 显示图像
plt.show()
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 生成时间序列
months = 48
dates = pd.date_range(start="2020-01-01", periods=months, freq='M')

# 生成随机数据
np.random.seed(42)
nyc_vacancy_rate = np.random.normal(loc=8.0, scale=1.5, size=months)
shanghai_vacancy_rate = np.random.normal(loc=12.2, scale=2.0, size=months)

# 生成 NYC vs. 上海 空置率趋势图
plt.figure(figsize=(10, 5))
plt.plot(dates, nyc_vacancy_rate, label="NYC Vacancy Rate (%)", color="blue")
plt.plot(dates, shanghai_vacancy_rate, label="Shanghai Vacancy Rate (%)", color="red", linestyle="dashed")
plt.xlabel("Year")
plt.ylabel("Vacancy Rate (%)")
plt.title("NYC vs. Shanghai Commercial Vacancy Rate Trends (2020-2024)")
plt.legend()
plt.grid()

# 保存图片到桌面
plt.savefig("/Users/zivwu/Desktop/vacancy_rate_trend.png", dpi=300)

# 显示图像
plt.show()
# 生成 NYC vs. 上海 空置率趋势图
plt.figure(figsize=(10, 5))
plt.plot(dates, nyc_vacancy_rate, label="NYC Vacancy Rate (%)", color="blue")
plt.plot(dates, shanghai_vacancy_rate, label="Shanghai Vacancy Rate (%)", color="red", linestyle="dashed")
plt.xlabel("Year")
plt.ylabel("Vacancy Rate (%)")
plt.title("NYC vs. Shanghai Commercial Vacancy Rate Trends (2020-2024)")
plt.legend()
plt.grid()

# 保存图片到桌面
plt.savefig("/Users/zivwu/Desktop/vacancy_rate_trend.png", dpi=300)

# 显示图像
plt.show()
# 生成 NYC vs. 上海 空置率趋势图
plt.figure(figsize=(10, 5))
plt.plot(dates, nyc_vacancy_rate, label="NYC Vacancy Rate (%)", color="blue")
plt.plot(dates, shanghai_vacancy_rate, label="Shanghai Vacancy Rate (%)", color="red", linestyle="dashed")
plt.xlabel("Year")
plt.ylabel("Vacancy Rate (%)")
plt.title("NYC vs. Shanghai Commercial Vacancy Rate Trends (2020-2024)")
plt.legend()
plt.grid()

# 保存图片到桌面
plt.savefig("/Users/zivwu/Desktop/vacancy_rate_trend.png", dpi=300)

# 显示图像
plt.show()
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 生成时间序列
months = 48
dates = pd.date_range(start="2020-01-01", periods=months, freq='M')

# 生成随机数据
np.random.seed(42)
nyc_rental_yield = np.random.normal(loc=4.5, scale=0.3, size=months)
shanghai_rental_yield = np.random.normal(loc=3.8, scale=0.6, size=months)

# 创建图表
plt.figure(figsize=(10, 5))
plt.plot(dates, nyc_rental_yield, label="NYC Rental Yield (%)", color="blue")
plt.plot(dates, shanghai_rental_yield, label="Shanghai Rental Yield (%)", color="red", linestyle="dashed")
plt.xlabel("Year")
plt.ylabel("Rental Yield (%)")
plt.title("NYC vs. Shanghai Commercial Rental Yield Trends (2020-2024)")
plt.legend()
plt.grid()

# 保存图片到桌面
plt.savefig("/Users/zivwu/Desktop/rental_yield_trend.png", dpi=300)

# 显示图像
plt.show()

