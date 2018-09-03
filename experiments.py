

from matplotlib import pyplot as plt

# Initialize variables
years =  [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007,2008, 2009]
movies =    [2, 2, 2, 3,1, 1, 2, 3, 4, 1, 4]
drownings = [109, 102, 102, 98, 85, 95, 96, 98, 123, 94, 102]

movies_scaling_factor = 10

# Apply scaling
scaled_movies = []
for i in movies:
    scaled_movies.append(i * movies_scaling_factor)
print (scaled_movies)

# Show plot table
index = 0
print('Source Data'.center(30))
print('Years'.center(9), 'Movies'.center(9), 'Drownings'.center(9))
while index < len(years):    
    print (repr(years[index]).rjust(9), repr(movies[index]).rjust(9), repr(drownings[index]).rjust(9))
    index += 1
#print(repr(num).center(3))
#print (str(s).center(3))
#print (repr(s))

# Plot
plt.close('all')
plt.plot(years, scaled_movies)
plt.plot(years, drownings)
plt.title('Cage Movies Versus Drownings')
plt.xlabel('Year')
plt.legend(['movies', 'drownings']) 


# Show plots
plt.show()

plt.close('all')
#plt.subplots_adjust(hspace=0.3)

ax_drownings = plt.subplot(2,1,1)
ax_drownings.set_xticks([])
ax_drownings.plot(years, drownings, color='pink', marker='o')
plt.ylabel('Drownings')

ax_movies = plt.subplot(2,1,2)
ax_movies.plot(years, movies, color='grey', marker='o')
plt.xlabel('Years')
plt.ylabel('Movies')

plt.show()#plt.close('all')

figs = plt.figure()
plt.plot(years,movies, color='grey')
plt.title('Movies')
plt.xlabel('Years')
plt.ylabel('Movies')
plt.show()
plt.close('all')

fig2 = plt.figure()
plt.plot(years, drownings, color='red')
plt.title("Drownings")
plt.xlabel('Years')
plt.ylabel('Drownings')
plt.show()
plt.close('all')


