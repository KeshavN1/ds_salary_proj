import glassdoor_scrap as gs
import pandas as pd
path = "D:/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist', 15, False, path, 15)