from matplotlib import pyplot as plt
import numpy as np

#entring data
front = ['Raunak', 'Ayush', 'Parth',
        'Arpit', 'Monika', 'Sanjana','Yashica']

Age = [18, 18, 18, 17, 17, 18, 18]

#creating pie chart
fig = plt.figure(figsize=(10, 7))
plt.pie(Age, labels=front)

#show
plt.show()
