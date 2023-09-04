# Task: Explore in Google and Make a document :

# 1. How to filter data in pandas dataframe?
'''Subset selection is one of the most frequently performed steps in data manipulation. 
Pandas by far offers many different ways to filter your dataframes to get your selected subsets of data. 
In this article, I will show you some cases that I encounter the most when manipulating data.'''

# 2. Types of data filters in pandas dataframe?
'''The core data structure of Pandas is DataFrame which stores data in tabular form with labeled rows and columns.
8 Pandas Filter Methods to Know. Logical operators. ...
1.Logical operators.
2.Isin.
3.Multiple logical operators.
4.Str accessor.
5.Tilde (~).
6.Query.
7.Nlargest and nsmallest.
8.Loc and iloc.'''

# Task: Write a program

# Q> create and import below files

import pandas as pd
# 1. Create a friend_names.xls file  (atleast 10 names, columns are FriendName,Quality)
friend_names_data=pd.read_excel(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\friend_names_dtfrm.xls")
print(friend_names_data)

# Q1> create a dataframe which contains only your intelligent friends list.
df_fr=friend_names_data[friend_names_data["Quality"]=="Inteligent"]
print(df_fr)

# Q2> create a dataframe which contains only your funny friends list.
df_fr1=friend_names_data[friend_names_data["Quality"]=="funny"]
print(df_fr1)

# 2. Create a family_members.xls file (atleast 10 names, columns are FamilyMemberName*Relation)
family_members_df=pd.read_excel(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\family_members10.xls")
print(family_members_df)

# Q1> create a dataframe which contains only your brothers and sisters list.
df_fm_s=family_members_df[(family_members_df["Relation"]=="Brother") | (family_members_df["Relation"]=="Sister")]
print(df_fm_s)

# Q2> create a dataframe which contains only your parents list.
df_fm_p=family_members_df[(family_members_df["Relation"]=="Father") | (family_members_df["Relation"]=="Mother")]
print(df_fm_p)

# Q3> create a dataframe which not contains your parents list.
df_fr1_np=family_members_df[(family_members_df["Relation"]!="Father") & (family_members_df["Relation"]!="Mother")]
print(df_fr1_np)

# Q4> create a dataframe which not contains your brothers list.
df_fm_nb=family_members_df[(family_members_df["Relation"]!="Brother")]
print(df_fm_nb)

# Q5> create a dataframe which contains either your brothers list or parents list.
df_fm_bp=family_members_df[(family_members_df["Relation"]=="Brother") | (family_members_df["Relation"]=="Father") & (family_members_df["Relation"]=="Mother")]
print(df_fm_bp)

# Q5> create a dataframe which contains your brothers list and parents list.
df_fm_bpt=family_members_df[(family_members_df["Relation"]=="Brother") & (family_members_df["Relation"]=="Father") & (family_members_df["Relation"]=="Mother")]
print(df_fm_bpt)


# 3. Create a Vegfood_items.xlsx file  (atleast 10 names, columns are VegFoodName*Taste)
dfveg_food_items=pd.read_excel(r"C:\Users\Abdul\Downloads\assignment8.a\Vegfood_items.xlsx")
print(dfveg_food_items)

# Q1>create a dataframe which are  soups items
df_biryani_item=dfveg_food_items[(dfveg_food_items["VegFoodNames"]=="Veg Biryani")]
print(df_biryani_item)

# Q2>create a dataframe which are curry items
df_curry_item=dfveg_food_items[(dfveg_food_items["VegFoodNames"]=="Palak Paneer") | (dfveg_food_items["VegFoodNames"]=="Mattar Paneer")]
print(df_curry_item)

# Q3>create a dataframe which are fry items
df_fry_items=dfveg_food_items[(dfveg_food_items["VegFoodNames"]=="Veg FriedRice") | (dfveg_food_items["VegFoodNames"]=="Veg Manchurian")]
print(df_fry_items)

# Q4>create a dataframe which contains soups and fry items
df_sp_fry_items=dfveg_food_items[(dfveg_food_items["VegFoodNames"]=="Veg Biryani") | (dfveg_food_items["VegFoodNames"]=="Veg FriedRice") | (dfveg_food_items["VegFoodNames"]=="Veg Manchurian")]
print(df_sp_fry_items)

# Q5>create a dataframe which not contains soups and fry items
df_ntsp_fry_items=dfveg_food_items[(dfveg_food_items["VegFoodNames"]!="Veg Biryani") & (dfveg_food_items["VegFoodNames"]!="Veg FriedRice") & (dfveg_food_items["VegFoodNames"]!="Veg Manchurian")]
print(df_ntsp_fry_items)

# Q6>create a dataframe which contains either soup or fry items
df_f_or_s=dfveg_food_items[(dfveg_food_items["VegFoodNames"]=="Veg Biryani") | (dfveg_food_items["VegFoodNames"]=="Veg FriedRice") & (dfveg_food_items["VegFoodNames"]=="Veg Manchurian")]
print(df_f_or_s)


# 4. Create a NonVegfood_items.xlsx file  (atleast 10 names, columns are NonVegFoodName*Taste)
df_NonVegfood_items=pd.read_excel(r"C:\Users\Abdul\Downloads\assignment8.a\NonVegfood_items.xlsx")
print(df_NonVegfood_items)

# Q1>create a dataframe which contains only chicken items
df_chicken_items=df_NonVegfood_items[(df_NonVegfood_items["NonVegFoodName"]=="Chicken Biryani") | (df_NonVegfood_items["NonVegFoodName"]=="Chicken Manchurian")]
print(df_chicken_items)

# Q2>create a dataframe which contains only mutton items
df_mutton_items=df_NonVegfood_items[(df_NonVegfood_items["NonVegFoodName"]=="Mutton Biryani") | (df_NonVegfood_items["NonVegFoodName"]=="Haleem")]
print(df_mutton_items)

# Q3>create a dataframe which contains only Fry items
df_mutton_fry_items=df_NonVegfood_items[(df_NonVegfood_items["NonVegFoodName"]=="Mutton Kabaab")]
print(df_mutton_fry_items)

# Q4>create a dataframe which contains only Fry and chicken items
df_chicken_fry_items=df_NonVegfood_items[(df_NonVegfood_items["NonVegFoodName"]=="Chicken Biryani") | (df_NonVegfood_items["NonVegFoodName"]=="Chicken Manchurian") | (df_NonVegfood_items["NonVegFoodName"]=="Mutton Kabaab")]
print(df_chicken_fry_items)

# Q5>create a dataframe which not contains Fry and chicken items
df_ntchicken_fry=df_NonVegfood_items[(df_NonVegfood_items["NonVegFoodName"]!="Chicken Biryani") & (df_NonVegfood_items["NonVegFoodName"]!="Chicken Manchurian") & (df_NonVegfood_items["NonVegFoodName"]!="Mutton Kabaab")]
print(df_ntchicken_fry)

# Q6>create a dataframe which contains either Fry or mutton items
df_mutton_or_fry_items=df_NonVegfood_items[(df_NonVegfood_items["NonVegFoodName"]=="Mutton Kabaab") | (df_NonVegfood_items["NonVegFoodName"]=="Mutton Biryani") & (df_NonVegfood_items["NonVegFoodName"]=="Haleem")]
print(df_mutton_or_fry_items)


# 5. Create a month_names.xlsx file (atleast 12 names, columns are MonthName*Season)
df_month_names=pd.read_excel(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\month_names.xlsx")
print(df_month_names)

# Q1>create a dataframe which contains only winter season months
df_winter_names=df_month_names[(df_month_names["Season"]=="winter")]
print(df_winter_names)

# Q2>create a dataframe which contains only summer season months
df_summer_names=df_month_names[(df_month_names["Season"]=="summer")]
print(df_summer_names)

# Q3>create a dataframe which contains only rainy season months
df_rainy_names=df_month_names[(df_month_names["Season"]=="rainy")]
print(df_rainy_names)
# Q4>create a dataframe which contains only winter and summer season months
df_winter_summer_names=df_month_names[(df_month_names["Season"]=="winter") | (df_month_names["Season"]=="summer")]
print(df_winter_summer_names)

# Q5>create a dataframe which not contains summer and rainy season months
df_sumr_or_rny_names=df_month_names[(df_month_names["Season"]!="rainy") & (df_month_names["Season"]!="summer")]
print(df_sumr_or_rny_names)
# Q6>create a dataframe which contains either winter or rainy items
df_ntwint_rny_names=df_month_names[(df_month_names["Season"]=="winter") | (df_month_names["Season"]=="rainy")]
print(df_ntwint_rny_names)


# 6. Create a flower_names.xlsx file  (atleast 12 names, columns are FlowercolourName_in_English^FlowercolourName_in_Hindi^FlowercolourName_in_Telugu)
df_colours_names=pd.read_excel(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\colours_names.xlsx")
print(df_colours_names)

# Q1>create a dataframe which contains only red colour flower list
df_red=df_colours_names[(df_colours_names["colourName_in_English"]=="Red")]
print(df_red)

# Q2>create a dataframe which contains only Green colour flower list
df_green=df_colours_names[(df_colours_names["colourName_in_English"]=="Green")]
print(df_green)

# Q3>create a dataframe which contains only pink colour flower list
df_pink=df_colours_names[(df_colours_names["colourName_in_English"]=="Pink")]
print(df_pink)

# Q4>create a dataframe which contains only red and pink colour list
df_rd_pk=df_colours_names[(df_colours_names["colourName_in_English"]=="Pink") | (df_colours_names["colourName_in_English"]=="Red")]
print(df_rd_pk)

# Q5>create a dataframe which not contains red and green colour list
df_rd_gr=df_colours_names[(df_colours_names["colourName_in_English"]=="Green") | (df_colours_names["colourName_in_English"]=="Red")]
print(df_rd_gr)

# Q6>create a dataframe which contains either red or pink colour list
df_rd_or_pk=df_colours_names[(df_colours_names["colourName_in_English"]=="Pink") | (df_colours_names["colourName_in_English"]=="Red")]
print(df_rd_or_pk)
