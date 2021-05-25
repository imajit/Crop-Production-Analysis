import numpy
from sklearn.impute import SimpleImputer

my_data = numpy.genfromtxt('outx.csv', delimiter=',')


impute = SimpleImputer(missing_values=numpy.nan, strategy='mean')
impute.fit(my_data)
my_data = impute.transform(my_data)
my_data = my_data[:, 2]

my_data[my_data > 1] = 0
my_data[my_data < -1] = 0

print(my_data[:10])
print(numpy.mean(my_data, axis=0))
