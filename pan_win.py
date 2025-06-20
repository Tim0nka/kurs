import pandas as pd
import time


df = pd.read_csv("winners.csv")


year = "2000"
driver_name = "Schumacher"  
start_time = time.time()


year = df[df["Date"].str.startswith(year)]
print(f" Вся информация по {year} году:")
print(year)


print(f" Все победители за 2000 год:")
print(year["Winner"].unique())


driver = df[df["Winner"].str.contains(driver_name, case=False, na=False)]
print(f"\n Вся информация по гонщику {driver_name}:")
print(driver)

end_time = time.time()
print(f" Время выполнения (pandas): {end_time - start_time:.6f} секунд")
