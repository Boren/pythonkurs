#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'Notebooks'))
	print(os.getcwd())
except:
	pass

#%%
navn = "Fredrik"
print(navn)


#%%
alder = 25
årstall = 2019
høyde = 1.75


#%%
12 + 30


#%%
fødselsår = årstall - alder
print(fødselsår)


#%%
byer = ["Oslo", "Stockholm", "Wien", "Berlin"]
print(byer)


#%%
byer.append("Trondheim")
byer.remove("Oslo")
print(byer)


#%%
len(byer)


#%%
byer.sort()
print(byer)


#%%
by = "Oslo"

if by in byer:
  print("Du har besøkt byen")
else:
  print("Du har ikke besøkt byen")


