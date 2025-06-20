import polars as pl
import time


df = pl.read_csv("winners.csv")


year = "2000"
driver = "Schumacher"

start_time = time.time()


year = df.filter(df["Date"].str.starts_with(year))
print(f"Вся информация по {year} году:")
print(year)


print(" Все победители за 2000 год:")
print(year.select("Winner").unique())


driver = df.filter(df["Winner"].str.contains(driver, literal=True))
print(f" Вся информация по гонщику {driver}:")
print(driver)


end_time = time.time()
print(f" Время выполнения (polars): {end_time - start_time:.6f} секунд")
